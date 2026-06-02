---
title: Naming And Enums Standard
file: 12_naming_and_enums_standard.md
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
source_path: 00_SYSTEM_GOVERNANCE/00_TAXONOMY_AND_NAMING.md
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: medium
canonical_candidate: true
tags: [ckos, taxonomy, enums, governance]
---

# Naming And Enums Standard

## Objective

Propose normalization for `owner`, `responsible_agent`, `reviewers`, `approval_required`, `tags`, `status`, `doc_type`, `layer`, `phase`, `category`, `risk_level` and `confidence`.

## Naming Rule

YAML uses system IDs in lowercase snake_case. Prose can use display names.

## Proposed Normalizations

| Current display/name | Proposed system_id |
|---|---|
| PMO_CKOS | pmo_ckos |
| Cognik | cognik |
| Metacognik | metacognik |
| Builder Lead | builder_lead |
| QA Lead | qa_lead |
| Founder | founder |
| Technical | technical |
| Client | client |
| Legal | legal |
| Codex | codex |
| Claude | claude |
| Antigravity | antigravity |

## owner

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

## responsible_agent

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

## reviewers

Use a list of system IDs:

```yaml
reviewers:
  - pmo_ckos
  - metacognik
```

## approval_required

Use a list, even when there is one approver:

```yaml
approval_required:
  - founder
```

Allowed values:

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

## status

Use a controlled status by doc layer. Do not mix maturity, workflow state and approval state into one value.

## doc_type

Use nouns:

```txt
canonical_doc
study_note
raw_source
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

## layer

Use one of:

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

## phase

Use folder-level system IDs. Avoid prose phase names.

## category

Use domain nouns. Avoid one-off phrases.

## risk_level

```txt
low
medium
high
critical
```

## confidence

```txt
unverified
low
medium
high
verified
```

## Tags

Tags must be lowercase snake_case, maximum 8 per file, and should come from the taxonomy proposal.

## What Not To Do Now

- Do not rename existing files.
- Do not normalize display names in prose automatically.
- Do not rewrite canonical YAML without approval.
