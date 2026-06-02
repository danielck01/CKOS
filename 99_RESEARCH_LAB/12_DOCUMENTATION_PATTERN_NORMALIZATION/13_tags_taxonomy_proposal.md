---
title: Tags Taxonomy Proposal
file: 13_tags_taxonomy_proposal.md
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
source_path: tag patterns
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: low
canonical_candidate: true
tags: [ckos, taxonomy, tags, governance]
---

# Tags Taxonomy Proposal

## Objective

Propose a controlled tag taxonomy for CKOS documentation.

## Tag Rules

- Always lowercase.
- Always snake_case.
- No accents.
- No long phrases.
- Maximum 8 tags per file.
- Prefer controlled vocabulary.
- Add new tags only when no existing tag fits.

## Core Tags

```txt
ckos
runtime
backend
frontend
branddock
dna
research
study
canonical
roadmap
policy
schema
api
agent
workflow
roi
memory
feedback
qa
approval
cost_guard
supabase
openrouter
mcp
observability
```

## Extended Controlled Tags

```txt
governance
documentation
yaml
template
taxonomy
security
permissions
data_model
event_bus
workflow_engine
agent_runtime
background_jobs
rag
pgvector
model_routing
tools_registry
handoff
release
patch_report
task
lock
readme
folder_memory
audit
risk
migration
```

## Tag Selection Pattern

Recommended order:

```txt
project/domain
layer
system area
specific topic
control topic
```

Example:

```yaml
tags: [ckos, study, runtime, workflow, approval, cost_guard]
```

## Anti-Patterns

- `AI First Project Operating System Deep Research`.
- `runtime/backend/Supabase`.
- `Metacognik Review Needed`.
- `aprovacao`.
- More than 8 tags.

## Migration Guidance

- First inventory existing tags.
- Map obvious synonyms to controlled tags.
- Do not delete rare tags until reviewed.
- Preserve unknown tags in a report before normalization.

## What Not To Do Now

- Do not bulk rewrite tags.
- Do not remove tags just because they are rare.
- Do not convert body keywords into tags automatically.
