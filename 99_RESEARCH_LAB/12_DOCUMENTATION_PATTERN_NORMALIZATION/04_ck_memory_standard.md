---
title: CK Memory Standard
file: 04_ck_memory_standard.md
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
source_path: ck_memory.md patterns
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: low
canonical_candidate: true
tags: [ckos, memory, documentation, governance]
---

# CK Memory Standard

## Objective

Define the standard for `ck_memory.md`.

## Core Rule

`ck_memory.md` is local folder memory. It is not global system memory and it does not replace canonical architecture.

## Required Structure

```md
# CK Memory - [Folder Name]

## Operational Status

## Current Context

## Decisions Registered

## Open Questions

## Active Constraints

## Related Tasks

## Last Updates

## Next Step
```

## Required YAML

```yaml
---
title: CK Memory - [Folder Name]
file: ck_memory.md
layer: memory
doc_type: folder_memory
status:
version:
created_at:
updated_at:
owner:
responsible_agent:
reviewers: []
approval_required: []
source_type: local_folder_state
source_path:
source_tool:
provenance_status:
confidence:
risk_level:
canonical_candidate: false
tags: []
---
```

## Allowed Content

- Current folder context.
- Local decisions.
- Open questions.
- Constraints.
- Related tasks.
- Short next step.

## Forbidden Content

- Final canonical rules.
- Backend implementation instructions unless the folder explicitly allows backend work.
- Global memory claims without source.
- Unapproved promotion decisions.

## Update Rule

Update `ck_memory.md` when local folder state changes. Do not update it as a substitute for a release note or patch report.

## Migration Note

Legacy `_folder_memory.md` should be inventoried first. It may contain useful historical memory and should not be deleted or renamed automatically.

## What Not To Do Now

- Do not replace `_folder_memory.md` automatically.
- Do not treat local memory as canonical.
- Do not write global system decisions into local memory only.
