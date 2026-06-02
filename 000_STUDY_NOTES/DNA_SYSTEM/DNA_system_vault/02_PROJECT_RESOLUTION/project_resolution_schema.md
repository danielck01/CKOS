---
title: Project Resolution Schema
folder: 02_PROJECT_RESOLUTION
type: backend_spec
status: implementable
version: 1.0.0
owner: CKOS PMO
backend_module: project_resolver_service
tables: [projects, project_resolution_events]
related_files: [project_resolver.md, project_resolution_api.md]
---

# Project Resolution Schema

Canonical data contracts for the Project Resolver. TypeScript interfaces are the source of truth for the service; JSON Schema is the wire contract for the API; SQL touchpoints map to `28_SUPABASE_SCHEMA/schema_v1.sql`.

## 1. Enums

```ts
type ProjectType =
  | "branding" | "campaign" | "research" | "ecommerce"
  | "content" | "social" | "other";

type ProjectStatus =
  | "draft" | "active" | "paused" | "completed" | "archived";

type ResolutionType =
  | "attached_existing"   // confidence high; bound to an existing project
  | "needs_confirmation"  // medium confidence; UI must confirm top candidate
  | "ambiguous"           // 2+ strong candidates; UI must disambiguate
  | "created_draft";      // low confidence; new Project Draft created

type NextStepKind =
  | "assemble_context" | "confirm_project" | "disambiguate_project"
  | "complete_briefing";
```

## 2. Core entities

```ts
interface Project {
  id: string;                  // uuid v7
  org_id: string;              // RLS scope
  workspace_id: string;
  name: string;
  type: ProjectType;
  status: ProjectStatus;
  briefing_summary: string | null;
  embedding_ref: string | null; // pointer to stored intent/briefing embedding
  entities: string[];           // brand/product/campaign tokens for entity_overlap
  created_by: string;           // actor_id
  created_at: string;           // ISO 8601
  updated_at: string;
}

interface MatchSignal {
  signal: "semantic" | "entity_overlap" | "recency" | "active_status"
        | "same_actor" | "current_prior";
  raw: number;     // signal value before weighting
  weight: number;  // weight applied
  contribution: number; // raw * weight
}

interface ProjectCandidate {
  project_id: string;
  name: string;
  status: ProjectStatus;
  score: number;            // [0,1], final weighted score
  signals: MatchSignal[];   // full explainability
}

interface NextStep {
  kind: NextStepKind;
  reason: string;
  blocking: boolean;        // must be done before a workflow can start
}

interface ProjectDraftMeta {
  provisional_name: string;
  inferred_type: ProjectType;
  needs_briefing: true;
}
```

## 3. Result contract

```ts
interface ProjectResolutionResult {
  project_id: string;            // resolved or provisional (for confirm/ambiguous)
  resolution_type: ResolutionType;
  confidence: number;            // [0,1] = top candidate score (1.0 for explicit hint)
  degraded: boolean;             // true if embeddings were unavailable
  candidates: ProjectCandidate[];// ranked; top N (default 5)
  required_next_steps: NextStep[];
  resolution_event_id: string;   // events.id of the appended ProjectResolutionEvent
  draft?: ProjectDraftMeta;      // present only when resolution_type = created_draft
  idempotency_key: string;
  created_at: string;
}
```

## 4. Event contract (append-only)

```ts
interface ProjectResolutionEvent {
  id: string;                    // uuid v7 = events.id
  type: "ProjectResolved" | "ProjectDraftCreated"
      | "ProjectConfirmationRequested" | "ProjectDisambiguationRequested";
  aggregate_type: "project";
  aggregate_id: string;          // project_id
  org_id: string;
  workspace_id: string;
  project_id: string;
  actor_id: string;
  resolution_type: ResolutionType;
  confidence: number;
  degraded: boolean;
  candidates_considered: number;
  correlation_id: string;        // groups intent → memory
  causation_id: string;          // the IntentSubmitted/IntentResolved event id
  created_at: string;
}
```

## 5. JSON Schema (wire contract for `POST /projects/resolve` response)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ProjectResolutionResult",
  "type": "object",
  "required": ["project_id", "resolution_type", "confidence", "degraded",
               "candidates", "required_next_steps", "resolution_event_id",
               "idempotency_key", "created_at"],
  "properties": {
    "project_id": { "type": "string", "format": "uuid" },
    "resolution_type": {
      "type": "string",
      "enum": ["attached_existing", "needs_confirmation", "ambiguous", "created_draft"]
    },
    "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
    "degraded": { "type": "boolean" },
    "candidates": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["project_id", "name", "status", "score", "signals"],
        "properties": {
          "project_id": { "type": "string", "format": "uuid" },
          "name": { "type": "string" },
          "status": { "type": "string",
            "enum": ["draft","active","paused","completed","archived"] },
          "score": { "type": "number", "minimum": 0, "maximum": 1 },
          "signals": { "type": "array", "items": { "type": "object" } }
        }
      }
    },
    "required_next_steps": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["kind", "reason", "blocking"],
        "properties": {
          "kind": { "type": "string",
            "enum": ["assemble_context","confirm_project",
                     "disambiguate_project","complete_briefing"] },
          "reason": { "type": "string" },
          "blocking": { "type": "boolean" }
        }
      }
    },
    "resolution_event_id": { "type": "string", "format": "uuid" },
    "draft": { "type": ["object", "null"] },
    "idempotency_key": { "type": "string" },
    "created_at": { "type": "string", "format": "date-time" }
  }
}
```

## 6. SQL touchpoints (full DDL in 28_SUPABASE_SCHEMA)

```sql
-- projects (draft = same table, status='draft')
projects(
  id uuid pk, org_id uuid not null, workspace_id uuid not null,
  name text not null, type text not null default 'other',
  status text not null default 'draft',
  briefing_summary text, embedding_ref text, entities jsonb default '[]',
  created_by uuid not null, created_at timestamptz default now(),
  updated_at timestamptz default now()
);
-- index for candidate loading
create index idx_projects_ws_status_updated
  on projects(workspace_id, status, updated_at desc);
-- RLS: org_id = current_setting('app.current_org_id')

-- resolution events are rows in the shared append-only events table
-- (aggregate_type='project'); no separate physical table required.
```

## 7. Worked examples

**Example A — attach (high confidence)**
```json
// input
{ "workspace_id":"ws1","org_id":"org1","actor_id":"u1",
  "intent_id":"int_88","current_project_id":"proj_aurora" }
// output
{ "project_id":"proj_aurora","resolution_type":"attached_existing",
  "confidence":0.91,"degraded":false,
  "candidates":[{"project_id":"proj_aurora","name":"Aurora Launch",
    "status":"active","score":0.91,"signals":[/*...*/]}],
  "required_next_steps":[{"kind":"assemble_context",
    "reason":"project bound","blocking":true}],
  "resolution_event_id":"evt_001","idempotency_key":"...","created_at":"2026-05-31T12:00:00Z" }
```

**Example B — draft (empty workspace / low confidence)**
```json
{ "project_id":"proj_new_01","resolution_type":"created_draft",
  "confidence":0.12,"degraded":false,"candidates":[],
  "required_next_steps":[
    {"kind":"complete_briefing","reason":"draft needs briefing","blocking":true},
    {"kind":"assemble_context","reason":"after briefing","blocking":false}],
  "resolution_event_id":"evt_002",
  "draft":{"provisional_name":"Penal Law IG Profile",
           "inferred_type":"social","needs_briefing":true},
  "idempotency_key":"...","created_at":"2026-05-31T12:01:00Z" }
```

**Example C — ambiguous (two strong candidates)**
```json
{ "project_id":"proj_a","resolution_type":"ambiguous","confidence":0.74,
  "degraded":false,
  "candidates":[
    {"project_id":"proj_a","name":"Spring Campaign","status":"active","score":0.74,"signals":[]},
    {"project_id":"proj_b","name":"Spring Social","status":"active","score":0.69,"signals":[]}],
  "required_next_steps":[{"kind":"disambiguate_project",
    "reason":"two candidates within 0.10","blocking":true}],
  "resolution_event_id":"evt_003","idempotency_key":"...","created_at":"..." }
```

## 8. Invariants (must hold)

- A `ProjectResolutionResult` always carries a `project_id` (provisional for confirm/ambiguous).
- `attached_existing` and `created_draft` are the only types that durably bind/create; `needs_confirmation` and `ambiguous` never mutate `projects`.
- `confidence` equals `candidates[0].score` unless an explicit hint forced `1.0`.
- Every result has exactly one appended event (`resolution_event_id`).
