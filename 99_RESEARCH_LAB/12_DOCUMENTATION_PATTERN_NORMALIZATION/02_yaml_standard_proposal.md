---
title: YAML Standard Proposal
file: 02_yaml_standard_proposal.md
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
source_path: 00_SYSTEM_GOVERNANCE/00_DOCUMENT_TEMPLATE.md
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: medium
canonical_candidate: true
tags: [ckos, yaml, governance, documentation, schema]
---

# YAML Standard Proposal

## Objective

Propose a unified YAML standard with variations by document type. This is a study proposal, not a canonical template update.

## Base YAML For Canonical Documents

```yaml
---
title:
file:
phase:
category:
version:
status:
owner:
responsible_agent:
reviewers:
  - metacognik
approval_required:
  - founder
purpose:
inputs:
outputs:
framework:
edge_cases:
integrations:
prompts:
metrics:
related_notes: []
tags: []
created_at:
updated_at:
---
```

## RAW/STUDY Additional Required Fields

```yaml
layer:
doc_type:
source_type:
source_path:
source_tool:
provenance_status:
confidence:
risk_level:
canonical_candidate:
```

## RAW/STUDY Full Proposal

```yaml
---
title:
file:
layer: study
doc_type: study_note
status: draft
version: 0.1.0
created_at:
updated_at:
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - metacognik
approval_required:
  - pmo_ckos
source_type:
source_path:
source_tool:
provenance_status: unverified
confidence: unverified
risk_level: medium
canonical_candidate: false
project: ckos
related_docs: []
related_notes: []
tags: []
---
```

## Roadmap YAML

```yaml
---
title:
file:
doc_type: roadmap
status:
owner:
phase:
scope:
dependencies: []
risks: []
roi_relevance:
related_notes: []
tags: []
---
```

## Patch Report YAML

```yaml
---
title:
file:
doc_type: patch_report
trigger:
objective:
files_created: []
files_changed: []
files_not_touched: []
patches_applied: []
patches_deferred: []
validation:
risks_remaining: []
gate:
confidence:
provenance_status:
tags: []
---
```

## Proposed Enums

### status

```txt
draft
active
raw
received
study
unverified
ready
blocked
in_progress
review
done
open
triaged
resolved
ready_for_review
accepted
rejected
completed
pending_review
passed
passed_with_risks
released
released_with_risks
rolled_back
deprecated
archived
stale
expired
cancelled
conflict
```

Rule: canonical docs should use only `draft`, `active`, `deprecated` or `archived` unless governance approves more.

### phase

```txt
ROOT
000_ROADMAPS
000_STUDY_NOTES
000_UPLOADS
00_SYSTEM_GOVERNANCE
01_THINKING_SYSTEM
02_EXECUTION_SYSTEM
03_RUNTIME_SYSTEM
04_PRODUCT_SYSTEM
05_IMPLEMENTATION_SYSTEM
06_BUSINESS_SYSTEMS
07_EVOLUTION_SYSTEM
99_RESEARCH_LAB
```

### category

```txt
governance
template
taxonomy
architecture
runtime
runtime_data
runtime_observability
security
workflow
memory
approval
cost_control
roi
feedback
roadmap
study
patch_report
handoff
release
task
lock
folder_memory
readme
```

### owner

```txt
founder
pmo_ckos
technical
qa_lead
builder_lead
metacognik
client
legal
```

### responsible_agent

```txt
nick
cognik
metacognik
pmo_ckos
qa_lead
builder_lead
datta
codex
claude
antigravity
ceo_agent
```

### approval_required

```txt
none
founder
pmo_ckos
technical
qa_lead
metacognik
client
legal
```

### confidence

```txt
unverified
low
medium
high
verified
```

### risk_level

```txt
low
medium
high
critical
```

### doc_type

```txt
raw_source
study_note
canonical_doc
roadmap
patch_report
handoff
release_note
task_board
folder_memory
feedback_log
checkout_lock
readme
study_index
standard_proposal
audit_note
migration_strategy
risk_register
promotion_proposal
```

### layer

```txt
raw
study
canonical
roadmap
patch_report
handoff
release
task
memory
feedback
lock
```

## Validation Rules

- YAML must parse cleanly.
- Lists must be lists, not comma-separated strings.
- Dates use `YYYY-MM-DD`.
- Names in YAML use system IDs.
- Tags use lowercase snake_case.
- Maximum 8 tags per file.
- `confidence` and `provenance_status` are mandatory for RAW/STUDY.

## What Not To Do Now

- Do not replace the canonical template from this file.
- Do not backfill YAML automatically.
- Do not infer fields that require human judgement.
