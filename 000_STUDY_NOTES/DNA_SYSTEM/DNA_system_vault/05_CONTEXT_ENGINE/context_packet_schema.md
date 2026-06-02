---
title: Context Packet Schema
folder: 05_CONTEXT_ENGINE
type: backend_spec
status: implementable
version: 1.0.0
owner: CKOS PMO
backend_module: context_assembler_service
tables: [context_packets, context_sources, events]
related_files: [context_assembler.md, context_validation.md]
---

# Context Packet Schema

The ContextPacket is the minimal-sufficient, permission-filtered, token-budgeted bundle the runtime builds **before any LLM call** and feeds to the Planner/Question Engine. It is the single source of "what the agent is allowed to know right now." It is persisted and replayable.

## 1. Top-level contract

```ts
interface ContextPacket {
  id: string;                       // uuid v7
  org_id: string;                   // RLS scope
  workspace_id: string;
  project_id: string;
  intent_id: string;
  sources: ContextSource[];         // everything considered, with included flag
  project_summary: string;          // <= 600 tokens, distilled
  known_facts: ContextFact[];
  assumptions: ContextAssumption[];
  missing_context: MissingContextItem[];
  constraints: ContextConstraint[];
  memory_refs: string[];            // memories.id used
  evidence_refs: string[];          // evidence_items.id used
  token_budget: number;             // ceiling for this packet
  tokens_used: number;              // actual tokens of included sources
  trust_score: number;              // [0,1] weighted avg of included sources
  validation_status: "valid" | "partial" | "blocked";
  blocking_reasons: string[];       // non-empty iff status != valid
  created_at: string;
}
```

## 2. Sub-contracts

```ts
type SourceType =
  | "project" | "briefing" | "decision" | "memory" | "rag"
  | "evidence" | "user_instruction" | "artifact" | "workflow" | "event";

// Trust hierarchy (Doc 05 §5.5 alignment). Higher = prevails on conflict.
type TrustLevel =
  | "approved_decision"   // 1.00
  | "contract"            // 0.95
  | "db_record"           // 0.90
  | "user_instruction"    // 0.85
  | "project_briefing"    // 0.80
  | "recent_artifact"     // 0.70
  | "retrieved_doc"       // 0.55  (RAG)
  | "agent_inference"     // 0.40
  | "web_research"        // 0.30
  | "weak_hypothesis";    // 0.15

interface ContextSource {
  id: string;
  type: SourceType;
  ref: string;                 // id of the underlying row (memory/evidence/decision/...)
  trust_level: TrustLevel;
  trust_score: number;         // numeric mapping of trust_level
  relevance: number;           // [0,1] similarity/match to intent
  priority: number;            // computed = f(trust_score, relevance); sort key
  tokens: number;              // token cost of this source's text
  included: boolean;           // survived budgeting + permission filter
  excluded_reason?: "budget" | "permission" | "stale" | "low_trust" | "duplicate";
  summary: string;             // the text actually injected (possibly compressed)
}

interface ContextFact {
  id: string;
  statement: string;
  source_ref: string;          // ContextSource.id backing this fact
  confidence: number;          // [0,1]
  evidence_ref?: string;       // evidence_items.id if any
}

interface ContextAssumption {
  id: string;
  statement: string;
  confidence: number;
  needs_validation: boolean;
  risk_if_wrong: "low" | "medium" | "high";
}

interface MissingContextItem {
  id: string;
  field: string;               // e.g. "target_audience", "budget", "jurisdiction"
  why_needed: string;
  blocking: boolean;           // true => validation_status cannot be "valid"
  suggested_question_id?: string; // hook into Question Engine
}

interface ContextConstraint {
  id: string;
  type: "legal" | "brand" | "budget" | "technical" | "time" | "policy";
  statement: string;
  source_ref: string;
}
```

## 3. Trust hierarchy → numeric map (locked)

```txt
approved_decision 1.00 | contract 0.95 | db_record 0.90 | user_instruction 0.85
project_briefing  0.80 | recent_artifact 0.70 | retrieved_doc 0.55
agent_inference   0.40 | web_research 0.30 | weak_hypothesis 0.15
```
On conflict between two facts, the one whose source has the higher `trust_score` prevails; ties escalate to `Metacognik` as a `context_conflict` (see `context_validation.md`).

## 4. Priority formula (budgeting sort key)

```txt
priority = 0.6 * trust_score + 0.4 * relevance
```
Sources are included in descending `priority` until `tokens_used + source.tokens > token_budget`. Overflow sources are either compressed (summarize) or excluded with `excluded_reason="budget"`.

## 5. Token budget defaults

```txt
token_budget default = 8000
project_summary       <= 600
known_facts (total)   <= 2500
memory/rag (total)    <= 3000
evidence (total)      <= 1500
reserve (schema/instr)  400
```
Configurable per intent risk in `context_budget_config`.

## 6. SQL touchpoints (full DDL in 28_SUPABASE_SCHEMA)

```sql
context_packets(
  id uuid pk, org_id uuid not null, workspace_id uuid not null,
  project_id uuid not null, intent_id uuid not null,
  project_summary text, token_budget int not null default 8000,
  tokens_used int not null default 0, trust_score numeric,
  validation_status text not null default 'partial',
  blocking_reasons jsonb default '[]',
  known_facts jsonb default '[]', assumptions jsonb default '[]',
  missing_context jsonb default '[]', constraints jsonb default '[]',
  memory_refs jsonb default '[]', evidence_refs jsonb default '[]',
  created_at timestamptz default now()
);
context_sources(
  id uuid pk, context_packet_id uuid fk->context_packets,
  type text, ref text, trust_level text, trust_score numeric,
  relevance numeric, priority numeric, tokens int,
  included bool, excluded_reason text, summary text
);
create index idx_ctx_sources_packet on context_sources(context_packet_id);
-- RLS by org_id on both tables.
```

## 7. Worked example (abridged)

```json
{
  "id": "ctx_001", "org_id":"org1","workspace_id":"ws1",
  "project_id": "proj_aurora", "intent_id": "int_88",
  "project_summary": "Aurora skincare launch; premium, dermatologist-backed; audience 28-45 women BR.",
  "known_facts": [
    {"id":"f1","statement":"Brand tone is clinical-warm","source_ref":"s2","confidence":0.9,"evidence_ref":"ev_12"}
  ],
  "assumptions": [
    {"id":"a1","statement":"Launch budget ~R$50k","confidence":0.4,"needs_validation":true,"risk_if_wrong":"high"}
  ],
  "missing_context": [
    {"id":"m1","field":"launch_date","why_needed":"sequences campaign","blocking":true,
     "suggested_question_id":"q_launch_date"}
  ],
  "constraints": [
    {"id":"c1","type":"legal","statement":"No medical efficacy claims","source_ref":"s4"}
  ],
  "sources": [
    {"id":"s2","type":"briefing","ref":"brief_7","trust_level":"project_briefing",
     "trust_score":0.8,"relevance":0.88,"priority":0.83,"tokens":420,"included":true,"summary":"..."}
  ],
  "memory_refs": ["mem_3"], "evidence_refs": ["ev_12"],
  "token_budget": 8000, "tokens_used": 3120, "trust_score": 0.78,
  "validation_status": "partial", "blocking_reasons": ["missing:launch_date"],
  "created_at": "2026-05-31T12:05:00Z"
}
```

## 8. Invariants

- `trust_score` = token-weighted average of `included` sources' `trust_score`.
- `validation_status="valid"` requires zero `blocking` missing items and `trust_score >= 0.60` (see `context_validation.md`).
- `tokens_used <= token_budget` always.
- Every `ContextFact.source_ref` and `ContextConstraint.source_ref` must reference an `included` source.
- Packet creation appends one `ContextAssembled` event with `correlation_id` from the intent.
