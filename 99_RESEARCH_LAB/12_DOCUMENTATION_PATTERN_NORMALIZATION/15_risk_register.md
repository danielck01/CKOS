---
title: Risk Register
file: 15_risk_register.md
layer: study
doc_type: risk_register
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
source_type: local_study
source_path: 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: high
canonical_candidate: false
tags: [ckos, risk, governance, migration]
---

# Risk Register

## Objective

Record risks for documentation normalization before any sweep.

## Risks

| risk_id | risk | level | cause | mitigation | approval needed |
|---|---|---|---|---|---|
| RISK_001 | Breaking links | high | Rename or move during normalization | No rename/delete in early phases | founder |
| RISK_002 | Losing legacy context | high | Replacing `_folder_memory.md` too early | Inventory and archive mapping first | pmo_ckos |
| RISK_003 | Study promoted as canonical by mistake | critical | Missing layer/doc_type distinction | Require `layer` and `canonical_candidate` | founder |
| RISK_004 | YAML invalid | medium | Bulk frontmatter generation | Parse validation before and after | pmo_ckos |
| RISK_005 | Owner normalized incorrectly | high | Display name ambiguity | Use approved mapping only | pmo_ckos |
| RISK_006 | Approval field weakened | critical | Free-form conversion error | Manual review for canonical docs | founder |
| RISK_007 | Tags lose useful retrieval signal | medium | Over-aggressive tag deletion | Preserve unknown tags in report | pmo_ckos |
| RISK_008 | Roadmap treated as canonical | high | Folder naming or status confusion | Layer field and README authority | pmo_ckos |
| RISK_009 | Backend implied by documentation | high | Study contains implementable examples | Explicit backend relation and blockers | technical |
| RISK_010 | Automation changes body text | high | Unsafe sweep | Phase 2 only adds minimal YAML | founder |
| RISK_011 | Sensitive content exposed | medium | RAW source metadata copied blindly | Redaction review for source_path/payload | pmo_ckos |
| RISK_012 | Confidence inflated | high | Agent fills `high` without evidence | Default `unverified` for uncertain docs | metacognik |

## Risk Policy

- Critical risks block automation.
- High risks require PMO review.
- Canonical risks require Founder or technical review when applicable.
- Unknown cases should be deferred, not guessed.

## What Not To Do Now

- Do not run bulk edits.
- Do not delete legacy memory.
- Do not overwrite canonical YAML.
- Do not normalize approval fields without human review.
