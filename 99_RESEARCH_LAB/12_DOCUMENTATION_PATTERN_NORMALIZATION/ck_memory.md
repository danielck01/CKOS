---
title: Documentation Pattern Normalization - ck_memory
file: ck_memory.md
layer: memory
doc_type: folder_memory
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
source_type: local_study
source_path: 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: low
canonical_candidate: false
tags: [ckos, memory, study, documentation]
---

# CK Memory - Documentation Pattern Normalization

## Operational Status

Study folder created inside `99_RESEARCH_LAB/`. It is non-canonical and should not be used as a direct source of implementation or migration.

## Current Context

The local vault snapshot found:

- 1036 Markdown files.
- 372 files without frontmatter.
- 376 files with frontmatter but without `tags`.
- `_folder_memory.md` exists as a legacy pattern in study/upload areas.
- `ck_memory.md`, `ck_tasks.md` and `ck_feedback.md` are active in roadmap-style folders.

## Decisions Registered

- This study uses ASCII-only Markdown.
- This study proposes standards but does not apply them.
- `ck_memory.md` is treated as local folder memory, not global system memory.
- `_folder_memory.md` should be migrated only after explicit human review.

## Open Questions

- Should `ck_memory.md` become mandatory for every operational folder or only active work areas?
- Should legacy `_folder_memory.md` be deprecated, archived or retained as historical memory?
- Should ROADMAP folders use the same YAML base as canonical docs or a smaller auxiliary schema?
- What level of confidence is required before a STUDY note can become a canonical candidate?

## Active Constraints

- Do not edit canonical vault.
- Do not rename files.
- Do not delete files.
- Do not apply automated patches.
- Do not implement backend or frontend.
- Do not promote any recommendation to canonical.

## Related Tasks

- Define layer separation.
- Propose YAML standards.
- Propose README, memory, task, lock, handoff, release and patch report standards.
- Define migration strategy and risk register.

## Last Updates

- 2026-05-31: Study folder and files created as research-only material.

## Next Step

PMO_CKOS and Metacognik should review this study and decide which items are candidates for canonical governance update.
