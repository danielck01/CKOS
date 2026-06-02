---
title: Documentation Pattern Normalization Study
file: README.md
layer: study
doc_type: study_index
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
source_path: 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: medium
canonical_candidate: false
tags: [ckos, study, documentation, governance, yaml, standards]
---

# Documentation Pattern Normalization Study

## Objective

Create a study-only proposal for CKOS documentation normalization before any automated sweep, safe patch, canonical migration, rename, delete, backend work or frontend work.

## Scope

This folder studies the documentation pattern only. It does not apply normalization to the canonical vault.

Allowed scope:

- Read local patterns.
- Document current inconsistencies.
- Propose standards.
- Define migration strategy.
- List risks and human approval gates.

Forbidden scope:

- Rename files.
- Delete files.
- Patch canonical documents.
- Generate backend migrations.
- Create frontend.
- Promote study output to canonical without approval.

## Files

| File | Purpose |
|---|---|
| `ck_memory.md` | Local memory for this study folder |
| `ck_feedback.md` | Local feedback and open review notes |
| `01_current_patterns_audit.md` | Snapshot of current patterns and layer separation |
| `02_yaml_standard_proposal.md` | YAML standard proposal by document type |
| `03_readme_standard_proposal.md` | README folder standard proposal |
| `04_ck_memory_standard.md` | `ck_memory.md` standard proposal |
| `05_ck_tasks_standard.md` | `ck_tasks.md` Kanban standard proposal |
| `06_checkout_lock_standard.md` | Checkout lock standard proposal |
| `07_handoff_standard.md` | Agent and PMO handoff standard |
| `08_release_standard.md` | Release note standard |
| `09_patch_report_standard.md` | Patch report standard |
| `10_study_note_standard.md` | Study note standard |
| `11_canonical_doc_standard.md` | Canonical document standard |
| `12_naming_and_enums_standard.md` | Naming and enum normalization proposal |
| `13_tags_taxonomy_proposal.md` | Controlled tags taxonomy proposal |
| `14_migration_strategy.md` | Four-phase migration strategy |
| `15_risk_register.md` | Risk register |
| `16_promotion_to_canonical_proposal.md` | Promotion proposal after human review |

## Main Recommendations

- Separate documentation into layers: RAW, STUDY, CANONICAL, ROADMAP, PATCH_REPORT, HANDOFF, RELEASE, TASK, MEMORY, FEEDBACK and LOCK.
- Treat `ck_memory.md` as the active local folder memory pattern.
- Treat `_folder_memory.md` as legacy until a human-approved migration plan exists.
- Add provenance and confidence metadata to RAW/STUDY material before any canonical promotion.
- Use controlled enums for `owner`, `responsible_agent`, `approval_required`, `status`, `doc_type`, `layer`, `phase`, `category`, `risk_level` and `confidence`.
- Keep roadmaps auxiliary and non-canonical unless explicitly approved.
- Make migration multi-phase and review-gated.

## Human Approval Required

Human approval is required before:

- applying frontmatter to existing files;
- normalizing owners, reviewers or tags in canonical docs;
- replacing `_folder_memory.md` with `ck_memory.md`;
- changing any canonical template;
- running bulk scripts;
- promoting any proposed standard from this study.

## Relation To Canonical Vault

This folder is not canonical. It can become evidence for a future canonical patch report or governance update after Founder, PMO_CKOS and technical review.
