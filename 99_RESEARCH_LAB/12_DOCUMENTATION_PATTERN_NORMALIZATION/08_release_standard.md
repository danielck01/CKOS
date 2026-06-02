---
title: Release Standard
file: 08_release_standard.md
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
source_path: release patterns
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: medium
canonical_candidate: true
tags: [ckos, release, governance, documentation]
---

# Release Standard

## Objective

Define a release note pattern for documentation and future implementation batches.

## Required Fields

```txt
release_id
scope
files_created
files_changed
files_not_touched
validation
tests
risks_remaining
next_step
status
```

## Proposed Template

```md
# Release - [release_id]

## Scope

## Files Created

## Files Changed

## Files Not Touched

## Validation

## Tests

## Risks Remaining

## Next Step

## Status
```

## Status Enum

```txt
draft
released
released_with_risks
rolled_back
archived
```

## Release Rules

- Release note is not the same as patch report.
- Release note summarizes a completed batch.
- Patch report explains why and how changes happened.
- Release must state validation and residual risk.
- Documentation-only releases should still list forbidden files not touched.

## What Not To Do Now

- Do not create release notes for unreviewed study drafts.
- Do not use release notes to bypass patch reports.
- Do not omit tests because the work is Markdown.
