---
title: Project Self Documentation System Study
file: 11_PROJECT_SELF_DOCUMENTATION_SYSTEM_STUDY.md
layer: study
phase: 000_STUDY_NOTES
category: project_self_documentation_system
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
purpose: Study how CKOS projects document themselves while preserving approval, provenance and memory boundaries.
inputs:
  - 07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
outputs:
  - self-documentation candidate pattern
framework:
  - project birth -> README -> memory -> briefing -> tasks -> decisions -> feedback -> learning
edge_cases:
  - self-documentation becomes self-approval
  - generated notes become trusted without audit
integrations:
  - memory_writer candidate
  - PMO governance
prompts:
  - What documentation should be created by this project state, and who must audit it?
metrics:
  - documentation reduces future context cost
related_notes:
  - 04_NOTES_AS_OPERATIONAL_MEMORY_STUDY.md
tags:
  - self_documentation
  - projects
  - memory
---

# Project Self Documentation System

## Study Pattern

```txt
project starts
  -> folder exists
  -> README exists
  -> ck_memory exists
  -> briefing exists
  -> tasks exist
  -> decisions are registered
  -> feedback updates memory
  -> learning updates patterns
  -> roadmaps evolve only with approval
```

## Principles

- Self-documentation is not self-approval.
- Generated notes start as unverified.
- Every memory write needs source and confidence.
- Canonical docs change only through approved patch plans.
- Project notes should reduce future context cost.

## Candidate Outputs

| Output | Authority |
|---|---|
| Project README | Auxiliary or project-local, not canonical. |
| Project memory | Context support, not truth without confidence. |
| Task notes | Execution trace, not approval. |
| Decision notes | Authority only after proper approver. |
| Learning notes | Candidate for future pattern updates. |

## Candidate For Doc 27

Doc 27 should require task orchestration to produce memory and documentation, but should avoid creating autonomous self-writing canon.
