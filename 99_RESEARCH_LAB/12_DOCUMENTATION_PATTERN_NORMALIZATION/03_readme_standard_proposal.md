---
title: README Standard Proposal
file: 03_readme_standard_proposal.md
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
source_path: README patterns
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: low
canonical_candidate: true
tags: [ckos, readme, documentation, governance]
---

# README Standard Proposal

## Objective

Define a folder README standard that tells humans and agents what a folder is allowed to contain and how to read it.

## Required README Sections

```md
# [Folder Name]

## Operational Status

## Folder Authority

## What This Folder Can Contain

## What This Folder Cannot Contain

## Short Reading Order

## Required Files

## Relation To Memory

## Relation To Tasks

## Current Locks Or Blockers

## Relation To ROI

## Relation To Backend

## Promotion Rules

## Human Approval Required
```

## Field Guidance

| Section | Meaning |
|---|---|
| Operational Status | Whether the folder is active, draft, archived, study-only or canonical |
| Folder Authority | Whether the folder is canonical, auxiliary, raw, study or operational |
| Can Contain | Allowed file types and topics |
| Cannot Contain | Explicit forbidden material |
| Reading Order | Minimal order to avoid context overload |
| Required Files | README, memory, tasks, feedback or other required local files |
| Relation To Memory | Whether folder uses `ck_memory.md` or legacy memory |
| Relation To Tasks | Whether folder requires `ck_tasks.md` |
| Locks Or Blockers | Active checkout locks or blocked decisions |
| Relation To ROI | Whether ROI is applicable and where it is tracked |
| Relation To Backend | Whether backend implementation is allowed, blocked or not applicable |
| Promotion Rules | What can move to another layer and by which gate |
| Human Approval Required | Who must approve changes |

## Recommended README YAML

```yaml
---
title:
file: README.md
layer:
doc_type: readme
status:
version:
created_at:
updated_at:
owner:
responsible_agent:
reviewers: []
approval_required: []
authority:
allowed_content: []
forbidden_content: []
required_files: []
related_memory:
related_tasks:
tags: []
---
```

## Rules

- README states folder rules; it does not silently override canonical governance.
- README should be short enough for agents to read before work.
- README should reference `ck_memory.md` for current local state.
- README should reference `ck_tasks.md` only when the folder has active work.
- Backend relation must be explicit: `not_applicable`, `study_only`, `blocked`, `allowed_after_approval` or `active`.

## What Not To Do Now

- Do not add README YAML in bulk.
- Do not rewrite existing README bodies automatically.
- Do not use README to promote study material to canonical.
