---
title: Checkout Lock Standard
file: 06_checkout_lock_standard.md
layer: study
doc_type: standard_proposal
status: draft
version: 0.1.0
created_at: 2026-05-31
updated_at: 2026-05-31
owner: pmo_ckos
responsible_agent: codex
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
source_type: local_vault_audit
source_path: roadmap lock patterns
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: high
canonical_candidate: true
tags: [ckos, lock, governance, tasks]
---

# Checkout Lock Standard

## Objective

Define a lock pattern to avoid concurrent edits and scope drift.

## Core Rule

No agent should edit outside `allowed_scope`.

## Required Fields

```txt
task_id
session_id
session_type
agent
allowed_scope
forbidden_scope
outputs
cost_limit
intelligence_level
approval_basis
created_at
expires_at
release_required
```

## Proposed Lock Template

```yaml
lock_id:
task_id:
session_id:
session_type:
agent:
status: active
allowed_scope: []
forbidden_scope: []
outputs: []
cost_limit:
intelligence_level:
approval_basis:
created_at:
expires_at:
release_required: true
```

## Status Enum

```txt
active
released
expired
cancelled
conflict
```

## Validation Rules

- `allowed_scope` must be explicit.
- `forbidden_scope` must list canonical vault, backend, frontend or migrations when blocked.
- `expires_at` must be present.
- If the lock edits files, a release or handoff is required.
- A lock cannot expand itself; expansion requires approval.

## Conflict Handling

If two sessions claim the same file:

1. Stop editing.
2. Record conflict.
3. Ask PMO_CKOS to choose owner.
4. Resume only after lock is updated.

## What Not To Do Now

- Do not create live lock infrastructure.
- Do not retroactively lock past sessions.
- Do not use a lock to bypass approval.
