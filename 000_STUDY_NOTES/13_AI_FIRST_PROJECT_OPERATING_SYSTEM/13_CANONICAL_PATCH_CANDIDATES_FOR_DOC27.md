---
title: Canonical Patch Candidates For Doc 27
file: 13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md
layer: study
phase: 000_STUDY_NOTES
category: canonical_patch_candidates
status: draft
version: 0.1.0
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
  - metacognik
confidence: unverified
provenance_status: unverified
source_tool: codex
purpose: List candidate sections and decisions for a future Doc 27 without creating it.
inputs:
  - README.md
  - 01_PROJECT_AI_FIRST_OPERATING_MODEL.md
  - 05_TASK_AI_FIRST_SYSTEM_STUDY.md
outputs:
  - Doc 27 candidates
framework:
  - candidate -> audit -> PMO decision -> canonical patch plan
edge_cases:
  - candidate treated as canonical
  - Doc 27 scope becomes too broad
integrations:
  - future Doc 27
prompts:
  - Candidate only until Founder/PMO/Metacognik approval.
metrics:
  - clear Doc 27 scope
related_notes:
  - 14_ACCEPTANCE_CRITERIA_FOR_DOC27.md
tags:
  - doc27
  - patch_candidates
  - study
---

# Canonical Patch Candidates For Doc 27

## Likely Doc 27 Title

```txt
27_INTELLIGENT_TASKS_AND_AGENT_WORK_ORCHESTRATION_ARCHITECTURE.md
```

This is a candidate only.

## Candidate Sections

| Candidate | Rationale |
|---|---|
| Task Object Model | Prevents generic task cards. |
| Task State Machine | Defines controlled task lifecycle. |
| Question-to-Task Transformer | Links questions to task creation. |
| Briefing-to-Task Transformer | Links briefing answers to work. |
| Agent Work Allocation | Defines who plans, executes, audits and learns. |
| Parallel Execution Policy | Embeds checkout lock discipline. |
| Founder Batch Approval | Allows controlled scale without losing governance. |
| Task ROI Model | Makes value explicit. |
| Task Feedback Loop | Converts completion and correction into learning. |
| Task Memory Update | Ensures execution updates memory. |
| Evidence and Context Requirements | Connects tasks to sources and context packs. |
| Non-Implementation Boundary | Blocks UI/backend/API/agents until future gates. |

## Deferred Candidates

The following may be too broad for Doc 27 and may become future docs:

| Candidate | Possible future doc |
|---|---|
| Notes, Memory and Project Knowledge System | Doc 28 candidate |
| Intelligent Briefing and Context Transformers | Doc 29 candidate |
| Learning, Feedback and Self-Documenting Projects | Doc 30 candidate |

## Gate

No candidate in this file is canonical until PMO/Founder/Metacognik approval and a separate canonical checkout.
