---
title: Patch Report Standard
file: 09_patch_report_standard.md
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
source_path: ARCHITECTURE_PATCH_REPORT.md
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: high
canonical_candidate: true
tags: [ckos, patch_report, governance, audit]
---

# Patch Report Standard

## Objective

Define a standard for patch reports that preserve traceability, provenance, validation and residual risk.

## Required YAML

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

## Required Body

```md
# Patch Report - [Title]

## Trigger

## Objective

## Files Created

## Files Changed

## Files Not Touched

## Patches Applied

## Patches Deferred

## Validation

## Risks Remaining

## Gate

## Next Step
```

## Rules

- Patch reports must record what was not touched.
- Patch reports must separate applied patches from deferred patches.
- Patch reports must include validation evidence.
- Patch reports must declare whether the gate is passed, blocked or pending.
- Patch reports should include `confidence` and `provenance_status`.

## Recommended Gate Values

```txt
pending_review
passed
passed_with_risks
blocked
rejected
```

## What Not To Do Now

- Do not rewrite existing patch reports automatically.
- Do not infer validation that was not performed.
- Do not treat this proposal as a replacement for existing governance.
