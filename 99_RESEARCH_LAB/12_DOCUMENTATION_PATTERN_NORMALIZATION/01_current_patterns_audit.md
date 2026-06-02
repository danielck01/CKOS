---
title: Current Patterns Audit
file: 01_current_patterns_audit.md
layer: study
doc_type: audit_note
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
source_path: CKOS_DOCUMENTATION_REVIEWED
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: medium
canonical_candidate: false
tags: [ckos, study, audit, documentation, governance]
---

# Current Patterns Audit

## Objective

Record current documentation patterns and propose a layer model before any automated normalization.

## Snapshot

Local snapshot on 2026-05-31:

- Markdown files: 1036.
- Without frontmatter: 372.
- With frontmatter but without `tags`: 376.
- `_folder_memory.md` appears as a legacy memory pattern in uploads and study areas.
- `ck_memory.md`, `ck_tasks.md` and `ck_feedback.md` appear as newer operational patterns in roadmap-style folders.
- Canonical docs generally have richer YAML than README, RAW and STUDY material.
- Patch reports have strong traceability but inconsistent provenance/confidence metadata.

These numbers include existing lab files and should be treated as a current local snapshot, not a historical baseline.

## Main Findings

- There is no single layer vocabulary across the vault.
- YAML quality is stronger in canonical architecture docs than in README and folder memory files.
- Some files have frontmatter but miss `tags`.
- Some study material lacks `confidence` and `provenance_status`.
- Naming alternates between display names and system IDs.
- `approval_required` appears as list, prose or mixed values.
- Tags are useful but not controlled enough for reliable automation.
- Roadmaps act as planning and coordination layers, not canonical architecture.
- DNA repair material requires implementable technical documentation, but not every study note should be promoted.

## Layer Separation Principle

Do not mix authority layers. A document can refer to another layer, but it should not silently inherit its authority.

## Layer Matrix

| Layer | Authority | Allowed status | Required fields | Optional fields | Who can edit | Promotion rule | Do not promote when |
|---|---|---|---|---|---|---|---|
| RAW | Evidence only | raw, received, archived | layer, doc_type, source_type, source_path, provenance_status, confidence | source_tool, risk_level, tags | intake agents, PMO | Promote to STUDY after source review | source is unknown or unsafe |
| STUDY | Non-canonical analysis | study, draft, unverified, archived | layer, doc_type, source_type, provenance_status, confidence, risk_level, canonical_candidate | recommendations, related_notes | research agents, PMO | Promote to candidate after review | confidence is low or claim lacks evidence |
| CANONICAL | System authority | draft, active, deprecated, archived | canonical YAML base, version, approvals, tags | test plan, failure modes | approved owner only | Already canonical after formal approval | approval is missing |
| ROADMAP | Auxiliary planning | draft, active, blocked, done, archived | doc_type, status, owner, scope, dependencies, risks | roi_relevance, tasks | PMO, roadmap agent | Can inform canonical work after gate | roadmap contradicts canonical source |
| PATCH_REPORT | Traceability | draft, active, archived | trigger, objective, files_created, files_changed, validation, gate | patches_deferred | PMO, auditor | Can support canonical update | validation is incomplete |
| HANDOFF | Continuity | draft, active, completed, blocked | from, to, scope, done, not_done, next_action, status | blockers, risks | sending agent, receiving agent | Can become release evidence | scope is ambiguous |
| RELEASE | Change summary | draft, released, rolled_back, archived | release_id, scope, files_created, files_changed, validation, status | tests, risks_remaining | release owner, PMO | Can support audit trail | validation absent |
| TASK | Execution control | backlog, ready, in_progress, review, done, blocked | task_id, title, scope, owner, status, allowed_files, forbidden_files | cost_limit | PMO, assigned owner | Can produce handoff/release | no checkout scope |
| MEMORY | Local folder memory | draft, active, stale, archived | operational status, context, decisions, constraints, next step | open questions | folder owner, PMO | Can inform README or canonical after review | memory is stale or local only |
| FEEDBACK | Review input | open, triaged, resolved, archived | source, feedback, status | priority, owner | reviewers, PMO | Can become task or patch candidate | duplicate or unverified |
| LOCK | Edit control | active, released, expired, cancelled | task_id, session_id, allowed_scope, forbidden_scope, expires_at | cost_limit, release_required | PMO, session owner | Can become release evidence | lock expired or scope conflict |

## Pattern Interpretation

- `_folder_memory.md` should be treated as legacy memory unless local governance says otherwise.
- `ck_memory.md` is the proposed active local memory pattern.
- `ck_tasks.md` is appropriate for folders with ongoing work, not passive archives.
- `ck_feedback.md` is appropriate where review loops are expected.

## Immediate Recommendation

Do not normalize automatically. First classify each file by layer and doc_type, then apply the four-phase migration strategy from `14_migration_strategy.md`.

## What Not To Do Now

- Do not rename `_folder_memory.md`.
- Do not bulk-add YAML to canonical docs without review.
- Do not convert roadmaps into canonical docs.
- Do not infer approval from tags or folder names.
- Do not use this audit as final authority.
