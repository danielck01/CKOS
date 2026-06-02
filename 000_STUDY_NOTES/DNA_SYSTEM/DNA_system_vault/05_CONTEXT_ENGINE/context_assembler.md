---
title: Context Assembler
folder: 05_CONTEXT_ENGINE
type: backend_spec
status: implementable
version: 1.0.0
owner: CKOS PMO
backend_module: context_assembler_service
depends_on: [project_resolver_service, memory_retriever, rag_retriever, evidence_registry, policy_engine, embeddings_service]
tables: [context_packets, context_sources, events]
endpoints: [POST /context/assemble, GET /context/:id]
related_files: [context_packet_schema.md, context_validation.md]
---

# Context Assembler

## 1. Purpose (one line)

Build a `ContextPacket` for a resolved project + intent: gather candidate sources, permission-filter, score by trust × relevance, fit a token budget, detect missing context, compute trust, validate, persist, and emit an event. Runs after Project Resolver, before Question Engine / Planner.

## 2. Inputs / outputs

```ts
interface AssembleContextInput {
  org_id: string; workspace_id: string; actor_id: string;
  project_id: string;        // from Project Resolver (required)
  intent_id: string;         // required
  token_budget?: number;     // default 8000
  refresh?: boolean;         // bypass cache and rebuild
}
// output: ContextPacket  (see context_packet_schema.md)
```

## 3. Assembly algorithm (canonical, 10 steps)

```txt
assembleContext(input):

1. AUTHZ + LOAD
   - policy_engine.can(actor, "assemble_context", project) else 403
   - project = projects.get(project_id) scoped by org_id
   - intent  = intent_submissions.get(intent_id); intent_embedding = embed(intent.text)

2. GATHER CANDIDATE SOURCES (parallel, all tenant-scoped)
   - project record      -> SourceType "project"        trust db_record
   - project briefing     -> "briefing"                   trust project_briefing
   - recent decisions     -> "decision"                   trust approved_decision/db_record
   - memory (mid+long)    -> memory_retriever.search(project_id, intent_embedding, k=12)
   - rag chunks           -> rag_retriever.search(namespace=org:project, intent, k=8)
   - evidence_items       -> evidence_registry.forProject(project_id)
   - explicit user instr. -> "user_instruction"           trust user_instruction
   - active workflow state-> "workflow"
   NOTE: memory_retriever / rag_retriever may be MOCKED in MVP (return []).

3. PERMISSION FILTER (pre-condition, not post-filter)
   - drop any source whose namespace != org:workspace:project
   - drop PII sources unless policy permits for this actor
   - any cross-tenant hit -> log VectorNamespaceViolationAttempted (P0), exclude

4. SCORE
   - for each source: trust_score = TRUST_MAP[trust_level]
                      relevance   = cosine(intent_embedding, source.embedding) or token-overlap fallback
                      priority    = 0.6*trust_score + 0.4*relevance

5. DEDUPE
   - collapse near-duplicate sources (cosine > 0.95); keep highest trust; mark others excluded(duplicate)

6. BUDGET FIT
   - sort by priority desc
   - include sources until tokens_used + tokens > token_budget
   - overflow: if trust_score >= 0.70 -> compress (summarize to fit); else exclude(budget)
   - always reserve 400 tokens for schema + agent instructions

7. DISTILL
   - project_summary = summarize(project + briefing + top decisions) <= 600 tokens
   - known_facts     = extract facts from included high-trust sources (each carries source_ref + confidence)
   - assumptions     = mark inferred/low-confidence statements; needs_validation=true if confidence<0.5
   - constraints     = legal/brand/budget/technical/time/policy pulled from sources

8. DETECT MISSING CONTEXT  (drives Question Engine)
   - required_fields = REQUIRED_BY_INTENT[intent.type]   (see context_validation.md §3)
   - for each required field not covered by a fact -> MissingContextItem(blocking=true, suggested_question_id)
   - optional fields not covered -> MissingContextItem(blocking=false)

9. COMPUTE TRUST + VALIDATE
   - trust_score = token-weighted avg of included sources' trust_score
   - validation_status = validate(packet)   (delegated to context_validation rules)

10. PERSIST + EMIT
   - insert context_packets + context_sources
   - events.append(ContextAssembled{ packet_id, project_id, trust_score, validation_status,
       missing_blocking_count, correlation_id=intent.correlation_id, causation_id=resolution_event_id })
   - return ContextPacket
```

## 4. TRUST_MAP and REQUIRED fields

`TRUST_MAP` is the locked table in `context_packet_schema.md §3`. `REQUIRED_BY_INTENT` lives in `context_validation.md §3` (per intent type).

## 5. Caching

- Key = `sha256(project_id + ':' + intent_id + ':' + project.updated_at)`.
- A packet is reused while the project is unchanged and `refresh != true`.
- New decision/briefing/evidence on the project invalidates the cache (project.updated_at bumps).

## 6. Failure modes

| Failure | Behavior |
|---|---|
| `project_id` not found / cross-tenant | `404`/`403`; never assemble |
| memory/rag retriever down | proceed with available sources; set assumption "context may be incomplete"; status likely `partial` |
| embeddings down | relevance falls back to keyword overlap; packet still builds (degraded) |
| budget too small for required facts | include required high-trust facts first; push optional to `missing_context`; status `partial` |
| a blocking source is PII-restricted | exclude(permission); if it was required → `blocked` with reason `permission:<field>` |
| zero usable sources (fresh draft) | status `partial` (not blocked); all required fields become `missing_context` → Question Engine |

## 7. Endpoints

```
POST /context/assemble   body: AssembleContextInput   -> 200 ContextPacket (201 if newly built)
GET  /context/:id        -> 200 ContextPacket | 404
```
`POST` is idempotent by cache key. Cross-tenant `:id` on GET → 404 (RLS).

## 8. Relationships

- **Project Resolver** must have produced `project_id` (no_project_no_workflow).
- **Question Engine** consumes `missing_context[]` (esp. blocking) to generate smart questions.
- **Planner** refuses to plan on a `blocked` packet; may plan on `partial` only if no blocking item touches a high-risk step.
- **Memory Writer** later reads `memory_refs` to know what was used (lineage).
- **ROI**: `constraints` (budget) and `assumptions` seed the ROI hypothesis later.

## 9. Codex implementation checklist

```txt
[ ] context_assembler_service.assemble(input): ContextPacket
[ ] gather(): parallel source fetchers; memory/rag mockable
[ ] permission filter BEFORE scoring; cross-tenant -> audit P0
[ ] priority = 0.6*trust + 0.4*relevance; budget fit with compress/exclude
[ ] missing-context detector keyed by REQUIRED_BY_INTENT
[ ] trust_score weighted avg; validation_status via context_validation rules
[ ] persist context_packets + context_sources; append ContextAssembled event
[ ] cache by sha256(project_id:intent_id:project.updated_at)
[ ] POST /context/assemble + GET /context/:id
[ ] tests: fresh draft -> partial + all required missing; PII required -> blocked
```
