---
title: Canonical Doc Standard
file: 11_canonical_doc_standard.md
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
  - technical
  - metacognik
source_type: local_vault_audit
source_path: canonical architecture docs
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: high
canonical_candidate: true
tags: [ckos, canonical, governance, documentation]
---

# Canonical Doc Standard

## Objective

Define the expected standard for canonical CKOS documents.

## Canonical Requirements

Canonical docs should include:

- SemVer.
- Formal approval.
- Controlled enums.
- Numbered body.
- Implementable examples.
- Backend relation when applicable.
- ROI relation when applicable.
- Memory relation when applicable.
- Failure modes.
- Test plan.

## Required YAML

Use the canonical base from `02_yaml_standard_proposal.md`.

## Required Body Structure

```md
# 1. Purpose

# 2. Function Inside CKOS

# 3. Inputs

# 4. Outputs

# 5. Operational Framework

# 6. Responsible Agent

# 7. Agents Involved

# 8. Skills Required

# 9. Prompts Related

# 10. Integrations

# 11. Memory And Context

# 12. Backend Relation

# 13. ROI Relation

# 14. Failure Modes

# 15. Test Plan

# 16. Approval Criteria

# 17. Rejection Criteria

# 18. Related Notes
```

## Canonical Authority Rules

- Canonical docs can define runtime rules.
- Canonical docs can constrain implementation.
- Canonical docs can reference study notes as evidence.
- Canonical docs must not depend on unverified study claims as final truth.

## Version Rules

- `0.x.x`: proposal or draft.
- `1.x.x`: approved baseline.
- Minor version: compatible expansion.
- Patch version: correction without major semantic change.
- Major version: breaking conceptual or contract change.

## Approval Rules

Canonical updates require the approval list declared in YAML. If backend, security, billing or data model is affected, technical and Founder review should be required.

## What Not To Do Now

- Do not edit canonical docs from this study.
- Do not infer approval from active status alone.
- Do not remove examples, failure modes or tests for brevity when they affect implementation.
