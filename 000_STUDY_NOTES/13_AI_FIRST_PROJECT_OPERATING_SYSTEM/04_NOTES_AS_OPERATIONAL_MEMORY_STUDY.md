---
title: Notes As Operational Memory Study
file: 04_NOTES_AS_OPERATIONAL_MEMORY_STUDY.md
layer: study
phase: 000_STUDY_NOTES
category: notes_operational_memory
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
purpose: Study notes as units of memory, decision, execution context and learning rather than loose documents.
inputs:
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
outputs:
  - note taxonomy
  - folder control standard
framework:
  - note -> metadata -> memory role -> context role -> audit role -> learning role
edge_cases:
  - note becomes canonical without approval
  - unverified AI output treated as trusted memory
integrations:
  - memoryPolicyRegistry candidate
  - RAG metadata candidate
prompts:
  - Classify what kind of memory this note should become before using it as context.
metrics:
  - notes with clear memory type
  - fewer stale context errors
related_notes:
  - 12_RAG_METADATA_AND_VECTOR_CATEGORY_STUDY.md
tags:
  - notes
  - memory
  - rag
---

# Notes As Operational Memory

## Core Rule

```txt
note is not only document
note is memory, decision context, execution context, evidence pointer and learning unit
```

## Note Types

| Type | Memory role |
|---|---|
| `canonical_note` | Approved source of truth reference. |
| `study_note` | Interpreted but unverified study context. |
| `roadmap_note` | Planning context, not authority. |
| `task_note` | Work context and decision trace. |
| `decision_note` | Approved or pending decision record. |
| `memory_note` | Active memory summary. |
| `learning_note` | Reusable lesson from outcomes. |
| `feedback_note` | Feedback classified for action or learning. |
| `prompt_note` | Reusable prompt pattern candidate. |
| `risk_note` | Governance, technical or operational risk. |
| `roi_note` | Value, cost and benefit context. |
| `handoff_note` | Transfer of context across agents or sessions. |
| `patch_candidate_note` | Candidate for future canonical patch. |
| `source_manifest_note` | Provenance and source inventory. |

## Folder Control Pattern

| File | Required when |
|---|---|
| `README.md` | Always in governed study folders. |
| `ck_memory.md` | Always in active governed study folders. |
| `ck_tasks.md` | When the folder manages study work. |
| `ck_risks.md` | When there is governance or implementation drift risk. |
| `ck_roi.md` | When priority, value or cost matters. |
| `ck_feedback.md` | When ongoing review is expected. |
| `ck_agent_handoffs.md` | When multi-agent handoff is discussed. |
| `ck_learning.md` | Candidate only when learning accumulates across sessions. |
| `ck_prompts.md` | Candidate only when prompts become reusable study assets. |

## Candidate For Doc 27

Doc 27 should connect tasks to notes and memory. A task without memory behavior becomes ordinary project management.
