---
title: Migration Strategy
file: 14_migration_strategy.md
layer: study
doc_type: migration_strategy
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
source_path: CKOS_DOCUMENTATION_REVIEWED
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: high
canonical_candidate: true
tags: [ckos, migration, documentation, governance]
---

# Migration Strategy

## Objective

Define a safe four-phase strategy for documentation normalization.

## Phase 1 - Inventory

Read files, detect frontmatter, classify `layer` and `doc_type`.

Rules:

- Do not alter files.
- Produce inventory report.
- Detect YAML presence.
- Detect missing `tags`.
- Detect legacy `_folder_memory.md`.
- Detect possible canonical candidates.
- Detect files with risky ambiguity.

Outputs:

- Inventory CSV or Markdown report.
- Layer classification report.
- Risk list.

## Phase 2 - Safe Patch

Add minimum frontmatter only in files without YAML, without changing body.

Rules:

- Only low-risk folders.
- No canonical docs without review.
- No content rewrite.
- Preserve original title/body.
- Add `provenance_status: unverified` when source is not reviewed.

Outputs:

- Patch report.
- Validation report.
- Files changed list.

## Phase 3 - Standard Alignment

Normalize divergent fields in low-risk documents.

Rules:

- Normalize tags only from approved mapping.
- Normalize owner/reviewer values only when mapping is certain.
- Avoid semantic changes.
- Keep report of uncertain cases.
- Do not touch high-risk canonical docs.

Outputs:

- Before/after report.
- Deferred list.
- Risk register update.

## Phase 4 - Canonical Review

Canonical documents go through human review before patch.

Rules:

- Founder/PMO/technical approval when required.
- Review diffs manually.
- Validate YAML.
- Check links.
- Check SemVer.
- Update patch report.

Outputs:

- Approved canonical patch.
- Patch report.
- Release note.

## Required Risks To Track

- Breaking links.
- Losing legacy context.
- Promoting study as canonical by mistake.
- Deleting useful memory.
- Generating invalid YAML.
- Normalizing names incorrectly.
- Hiding uncertainty.
- Damaging RAG retrieval quality.

## Automation Boundary

Automation can assist inventory and validation. Automation should not decide authority, approval, confidence, canonical promotion or semantic meaning.

## What Not To Automate Yet

- Canonical doc rewrites.
- `_folder_memory.md` migration.
- Owner normalization where source is ambiguous.
- Approval_required normalization where approval basis is unclear.
- Tag deletion.
- Study-to-canonical promotion.
