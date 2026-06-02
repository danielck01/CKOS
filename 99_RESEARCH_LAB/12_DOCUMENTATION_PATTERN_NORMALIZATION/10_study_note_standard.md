---
title: Study Note Standard
file: 10_study_note_standard.md
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
source_path: 000_STUDY_NOTES/_templates/STUDY_NOTE_TEMPLATE.md
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: medium
canonical_candidate: true
tags: [ckos, study, research, documentation]
---

# Study Note Standard

## Objective

Define how CKOS study notes should work.

## Authority

Study notes are always:

```txt
status: study/draft/unverified
authority: non-canonical
```

## Study Notes Can

- Compare options.
- Generate preliminary recommendations.
- Raise risks.
- Propose canonical candidates.
- Preserve provenance.
- Prepare implementation briefs after approval.

## Study Notes Cannot

- Become system rules automatically.
- Overwrite canonical documents.
- Define final schema without approval.
- Generate final migrations.
- Authorize backend or frontend work by themselves.

## Required YAML

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
responsible_agent:
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
related_docs: []
related_notes: []
tags: []
---
```

## Required Body

```md
# [Title]

## Objective

## Context

## Sources Reviewed

## Options Analyzed

## Preliminary Recommendation

## Why This Recommendation

## Trade-offs

## Risks

## Implementation Later

## Dependencies

## What Not To Do Now
```

## Promotion Criteria

A study note can become a canonical candidate only when:

- provenance is clear;
- confidence is at least `medium`;
- risk is documented;
- owner and reviewer are declared;
- canonical target file is named;
- human approval is requested.

## What Not To Do Now

- Do not promote study notes in bulk.
- Do not treat `canonical_candidate: true` as approval.
- Do not remove uncertainty from study notes to make them look final.
