---
title: Project Resolution API
folder: 02_PROJECT_RESOLUTION
type: backend_spec
status: implementable
version: 1.0.0
owner: CKOS PMO
backend_module: project_resolver_service
endpoint: POST /projects/resolve
related_files: [project_resolver.md, project_resolution_schema.md]
---

# Project Resolution API

## 1. Endpoint

```
POST /projects/resolve
```

Resolves an intent to a project (attach / confirm / disambiguate / draft). Idempotent by intent.

## 2. Auth & scope

- Requires a session token carrying `org_id`, `workspace_id`, `actor_id`.
- `org_id` from the token sets `app.current_org_id` (Postgres RLS). The body cannot override tenant scope.
- Permission checked: `policy_engine.can(actor, "resolve_project", workspace)`.

## 3. Request

Headers: `Authorization: Bearer <token>`, `Content-Type: application/json`, optional `Idempotency-Key`.

Body (`ResolveProjectInput`):
```json
{
  "intent_id": "int_88",
  "raw_intent": null,
  "current_project_id": "proj_aurora",
  "hints": { "project_id": null, "create_new": false }
}
```
`workspace_id`, `org_id`, `actor_id` come from the token, not the body. Exactly one of `intent_id` / `raw_intent` required.

## 4. Responses

| Status | Meaning | Body |
|---|---|---|
| `200 OK` | Resolved (any resolution_type) | `ProjectResolutionResult` |
| `201 Created` | Resolved as `created_draft` (new project row) | `ProjectResolutionResult` |
| `400 Bad Request` | invalid input (neither/both of intent_id & raw_intent) | `ErrorBody` |
| `401 Unauthorized` | missing/invalid token | `ErrorBody` |
| `403 Forbidden` | actor lacks `resolve_project` | `ErrorBody` |
| `409 Conflict` | idempotency replay with different body | `ErrorBody` |
| `503 Service Unavailable` | event not durable (resolution rolled back) | `ErrorBody` |

`ErrorBody`:
```json
{ "error": "invalid_input", "message": "exactly one of intent_id or raw_intent required",
  "correlation_id": "corr_123" }
```

## 5. Behavior by resolution_type

```txt
attached_existing  -> 200; projects.updated_at touched; next: assemble_context
needs_confirmation -> 200; no mutation; UI shows confirm(top candidate)
ambiguous          -> 200; no mutation; UI shows disambiguate(candidates[])
created_draft      -> 201; new projects row (status=draft); next: complete_briefing
```

## 6. Idempotency

- Key = `Idempotency-Key` header if present, else `sha256(org_id + ':' + (intent_id ?? hash(raw_intent)))`.
- First call performs resolution and stores result keyed by idempotency_key.
- Repeat call with same key + same body → returns the stored result (same status).
- Repeat call with same key + different body → `409 Conflict`.

## 7. Side effects

- Appends exactly one row to `events` (`ProjectResolved | ProjectDraftCreated | ProjectConfirmationRequested | ProjectDisambiguationRequested`).
- `created_draft` also inserts one `projects` row.
- On `403`/cross-tenant hint: appends to `audit_logs` (`PermissionDenied` / `TenantBoundaryViolationAttempted`).
- No workflow, no cost, no external provider call. Resolution is cheap and synchronous.

## 8. curl examples

**Attach**
```bash
curl -sX POST https://api.ckos.local/projects/resolve \
 -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
 -d '{"intent_id":"int_88","current_project_id":"proj_aurora"}'
# 200 -> resolution_type: attached_existing
```

**New draft from raw intent**
```bash
curl -sX POST https://api.ckos.local/projects/resolve \
 -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
 -d '{"raw_intent":"criar perfil instagram para advogada penal recem-formada"}'
# 201 -> resolution_type: created_draft, draft.inferred_type: social
```

**Force new**
```bash
curl -sX POST https://api.ckos.local/projects/resolve \
 -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
 -d '{"intent_id":"int_90","hints":{"create_new":true}}'
# 201 -> created_draft
```

## 9. Terminal acceptance test (before frontend)

```txt
1. POST /intent/submit            -> intent_id
2. POST /projects/resolve {intent_id}  (empty workspace) -> 201 created_draft
3. POST /projects/resolve {intent_id} again -> 200, same project_id (idempotent)
4. POST /projects/resolve {intent_id, current_project_id} (matching) -> 200 attached_existing
5. SELECT * FROM events WHERE aggregate_type='project'  -> 1 row per distinct resolve
6. Cross-tenant current_project_id -> hint ignored + audit_logs entry
```

## 10. Failure-mode HTTP mapping

| Internal failure (project_resolver.md §8) | HTTP |
|---|---|
| invalid input | 400 |
| permission denied | 403 |
| embeddings down | 200 with `degraded:true` (never fails the request) |
| event write failed | 503 (`resolution_not_durable`) |
| idempotency body mismatch | 409 |
