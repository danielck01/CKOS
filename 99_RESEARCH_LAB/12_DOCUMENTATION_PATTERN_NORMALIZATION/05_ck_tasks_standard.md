---
title: CK Tasks Standard
file: 05_ck_tasks_standard.md
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
  - pmo_ckos
source_type: local_vault_audit
source_path: ck_tasks.md patterns
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: medium
canonical_candidate: true
tags: [ckos, tasks, kanban, governance]
---

# CK Tasks Standard

## Objective

Define a Kanban standard for `ck_tasks.md` used in active operational folders.

## Required Kanban Columns

```txt
Backlog
Ready
In Progress
Review
Done
Blocked
```

## Required Task Fields

```txt
task_id
title
scope
allowed_files
forbidden_files
owner
status
approval_required
cost_limit
checkout_lock_required
output_expected
done_criteria
```

## Recommended Task Row

```md
| task_id | title | scope | allowed_files | forbidden_files | owner | status | approval_required | cost_limit | checkout_lock_required | output_expected | done_criteria |
|---|---|---|---|---|---|---|---|---:|---|---|---|
| TASK_001 | Example | Study only | `99_RESEARCH_LAB/...` | canonical vault | pmo_ckos | ready | pmo_ckos | 0 | required | study note | files created and verified |
```

## Status Rules

- `Backlog`: not ready.
- `Ready`: scoped and approved to start.
- `In Progress`: one owner actively working.
- `Review`: output exists and needs review.
- `Done`: done criteria met.
- `Blocked`: cannot proceed without decision or input.

## Checkout Rule

Any task that edits files must declare whether checkout lock is required. If required, the lock must list allowed and forbidden scope.

## Cost Rule

Tasks should carry a `cost_limit` even if the value is `0` for documentation-only work.

## What Not To Do Now

- Do not convert every checklist into `ck_tasks.md`.
- Do not mark work `Done` without done criteria.
- Do not let tasks authorize canonical edits without approval.
