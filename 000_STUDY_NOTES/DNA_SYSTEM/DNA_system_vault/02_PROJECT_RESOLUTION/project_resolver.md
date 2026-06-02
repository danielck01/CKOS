---
title: Project Resolver
folder: 02_PROJECT_RESOLUTION
type: backend_spec
status: implementable
version: 1.0.0
owner: CKOS PMO
backend_module: project_resolver_service
depends_on: [intent_service, embeddings_service, events_store, policy_engine]
tables: [projects, intent_submissions, project_resolution_events, events]
endpoints: [POST /projects/resolve]
related_files:
  - project_resolution_schema.md
  - project_resolution_api.md
  - ../05_CONTEXT_ENGINE/context_assembler.md
---

# Project Resolver

## 1. Purpose (one line)

Given an intent, decide **which project it belongs to** — attach to an existing project, ask the user to confirm, or create a Project Draft — and emit an auditable resolution event. No workflow may start without a resolved `project_id` (`no_project_no_workflow` policy).

## 2. Responsibility boundary

| Does | Does NOT |
|---|---|
| Resolve `project_id` for an intent | Build the context packet (that is `context_assembler`) |
| Compute match confidence against existing projects | Run the plan or workflow |
| Create a Project Draft when no good match exists | Classify project *type* in depth (that is `project_type_classifier`, called as a sub-step) |
| Emit `project_resolution_event` | Write long-term memory |

## 3. Inputs and outputs

**Input** (`ResolveProjectInput`):
```ts
interface ResolveProjectInput {
  workspace_id: string;        // tenant scope (required)
  org_id: string;              // tenant scope (required, RLS)
  actor_id: string;            // user or agent_service making the request
  intent_id?: string;          // preferred: reference to intent_submissions
  raw_intent?: string;         // fallback when intent not yet persisted
  current_project_id?: string; // active project in the UI session, if any
  hints?: {                    // optional explicit signals
    project_id?: string;       // user explicitly picked a project
    create_new?: boolean;      // user explicitly asked for a new project
  };
}
```
Exactly one of `intent_id` or `raw_intent` must be present. If `hints.project_id` is set and the actor has permission, resolution short-circuits to `attached_existing` with `confidence = 1.0`. If `hints.create_new` is true, resolution short-circuits to `created_draft`.

**Output**: `ProjectResolutionResult` (full schema in `project_resolution_schema.md`).

## 4. Resolution algorithm (canonical, 10 steps)

```txt
resolveProject(input):

1. LOAD INTENT
   - if input.intent_id: intent = db.intent_submissions.get(intent_id) scoped by org_id
   - else: intent = { text: input.raw_intent }  (ephemeral)
   - extract intent_text, intent_entities (named entities, brand/product/campaign tokens),
     intent_embedding (embeddings_service.embed(intent_text))

2. HONOR EXPLICIT HINTS (short-circuit)
   - if hints.project_id and policy_engine.can(actor, "attach", project): 
       return attach(project, confidence=1.0, reason="explicit_user_pick")
   - if hints.create_new: 
       return createDraft(reason="explicit_user_new")

3. CHECK CURRENT PROJECT (strong prior)
   - if input.current_project_id and project is status in (active, draft):
       candidate_current = score(intent, current_project) with prior_boost = +0.20

4. LOAD CANDIDATE PROJECTS
   - candidates = db.projects.where(workspace_id, status in (active, draft, paused))
                    .orderBy(updated_at desc).limit(25)
   - RLS enforced by org_id (Postgres). No cross-tenant candidate is ever loaded.

5. SCORE EACH CANDIDATE   (see §5 scoring model)
   - for each c in candidates: c.score = matchScore(intent, c)
   - merge candidate_current prior if present

6. RANK
   - sort candidates by score desc
   - top = candidates[0], second = candidates[1] (may be undefined)

7. DECIDE RESOLUTION TYPE   (see §6 decision table)
   - high confidence (top.score >= 0.80) and not ambiguous -> attached_existing
   - ambiguous (top.score >= 0.50 and second.score >= 0.50 and top.score - second.score <= 0.10) -> ambiguous
   - medium confidence (0.50 <= top.score < 0.80) -> needs_confirmation
   - low confidence (top.score < 0.50 or no candidates) -> created_draft

8. APPLY RESOLUTION
   - attached_existing: project_id = top.project_id; touch projects.updated_at
   - needs_confirmation / ambiguous: project_id = top.project_id (provisional); do NOT attach yet
   - created_draft: project = createDraft(intent); project_id = project.id

9. EMIT EVENT (append-only)
   - events.append(ProjectResolutionEvent { type, project_id, resolution_type, confidence,
       candidates_considered, actor_id, correlation_id = intent.correlation_id })

10. RETURN
   - { project_id, resolution_type, confidence, candidates, required_next_steps,
       resolution_event_id, draft? }
```

## 5. Scoring model (deterministic, tunable)

`matchScore(intent, project) → number in [0,1]`:

```txt
score =
    0.45 * semantic_similarity        // cosine(intent_embedding, project.embedding_ref)
  + 0.25 * entity_overlap             // Jaccard(intent_entities, project.entities)
  + 0.15 * recency_decay              // exp(-days_since_update / 14)   (half-life ~10d)
  + 0.10 * active_status_weight       // active=1.0, draft=0.6, paused=0.4, else 0
  + 0.05 * same_actor                 // 1.0 if intent.actor_id == project.created_by else 0
  + prior_boost                       // +0.20 only if project == current_project_id
score = clamp(score, 0, 1)
```

Default weights live in `project_resolver_config` (seedable). All six signals are logged per candidate in `MatchSignal[]` so the score is fully explainable and replayable.

- `semantic_similarity`: if either embedding is missing, this term = 0 and resolution leans on entities + recency (degraded but functional — see failure modes).
- `entity_overlap`: brand names, product names, campaign names, handles, domains.
- `recency_decay`: prevents stale projects from capturing new intents.

## 6. Decision table

| Condition | resolution_type | project attached? | required_next_steps |
|---|---|---|---|
| `top.score >= 0.80` and not ambiguous | `attached_existing` | yes | `assemble_context` |
| `top.score >= 0.50` and `second.score >= 0.50` and `Δ <= 0.10` | `ambiguous` | no (provisional) | `disambiguate_project` (return top-N candidates to UI) |
| `0.50 <= top.score < 0.80` | `needs_confirmation` | no (provisional) | `confirm_project` (yes/no on `top`) |
| `top.score < 0.50` or no candidates | `created_draft` | yes (new draft) | `complete_briefing`, `assemble_context` |

`confidence` returned = `top.score` (or `1.0` for explicit hint, `0.0`-band reported as the draft's own low score).

## 7. Project Draft rules

A Project Draft is a real `projects` row with `status = 'draft'` plus draft metadata. It is **not** a separate table (keeps MVP simple; one lifecycle).

Create a draft when:
- no candidate scores ≥ 0.50, OR
- `hints.create_new = true`, OR
- the workspace has zero projects.

Draft seeding:
```txt
project = {
  id: uuidv7(), org_id, workspace_id,
  name: deriveProvisionalName(intent_text),   // e.g. first salient entity + intent verb
  type: project_type_classifier(intent_text), // best-effort; may be 'other'
  status: 'draft',
  briefing_summary: null,                      // filled by briefing/context later
  embedding_ref: store(intent_embedding),
  created_by: actor_id, created_at: now()
}
```
A draft must complete briefing before it can move to `status='active'`. `required_next_steps` for a draft always includes `complete_briefing`.

## 8. Failure modes

| Failure | Detection | Behavior (fail-safe) |
|---|---|---|
| Embeddings service down | `embed()` throws/tim《out》 | Degrade: set semantic term = 0, resolve on entities+recency, set `degraded: true` in event; never block |
| No `intent_id` and empty `raw_intent` | input validation | `400 invalid_input`; do not create draft |
| Actor lacks permission on `hints.project_id` | `policy_engine.can` = deny | Ignore hint, fall through to scoring; emit `PermissionDenied` to audit_logs |
| Cross-tenant `current_project_id` | project.org_id != input.org_id | Reject hint, log `TenantBoundaryViolationAttempted` (P0), continue |
| Two+ candidates tied very high (≥0.80, Δ≤0.10) | rank step | Force `ambiguous` (never silently attach the wrong project) |
| DB write of event fails after attach | post-commit check | Roll back attach; return `503 resolution_not_durable`; idempotency_key allows safe retry |
| Duplicate resolve (same intent) | `idempotency_key = hash(intent_id)` | Return the prior `ProjectResolutionResult` (no duplicate draft) |

## 9. Idempotency & events

- `idempotency_key = sha256(org_id + ':' + (intent_id ?? hash(raw_intent)))`.
- Re-running resolve with the same key returns the original result and does **not** create a second draft.
- Every resolution appends one `project_resolution_event` to the `events` table (`aggregate_type='project'`), carrying `correlation_id` (groups the whole intent→memory chain) and `causation_id` (the `IntentSubmitted` event).

## 10. Agent / runtime relationships

- Called by the runtime immediately after `IntentResolved`, before `context_assembler`.
- `Cognik` may be invoked to interpret ambiguous intents (entity extraction); `Metacognik` audits resolutions flagged `ambiguous` or `degraded`.
- Emits `ProjectResolved | ProjectDraftCreated | ProjectDisambiguationRequested` for the UI projection.

## 11. Codex implementation checklist

```txt
[ ] service: project_resolver_service.resolve(input): ProjectResolutionResult
[ ] embeddings_service.embed(text): number[]   (mockable: returns zero-vector → degraded path)
[ ] matchScore() pure function + unit tests for each band (attach/confirm/ambiguous/draft)
[ ] createDraft() writes projects(status='draft') + embedding_ref
[ ] events.append(ProjectResolutionEvent) with correlation/causation
[ ] idempotency by sha256 key
[ ] RLS: all project reads scoped by org_id
[ ] POST /projects/resolve wired to service (see project_resolution_api.md)
[ ] tests: tied-high → ambiguous; empty workspace → draft; explicit hint → attach 1.0
```
