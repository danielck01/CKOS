---
title: ROI-aware Tasks Notes And Questions Study
file: 09_ROI_AWARE_TASKS_NOTES_AND_QUESTIONS_STUDY.md
layer: study
phase: 000_STUDY_NOTES
category: roi_aware_tasks_notes_questions
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
purpose: Study how ROI applies to questions, notes, tasks, agents, feedback and learning.
inputs:
  - ck_roi.md
  - 06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md
outputs:
  - ROI evaluation pattern
framework:
  - object -> ROI hypothesis -> cost -> risk -> evidence -> outcome
edge_cases:
  - ROI reduced to revenue only
  - low-value questions increase context cost
integrations:
  - cost_guard
  - eval_runner
  - ROI system candidate
prompts:
  - What operational value does this object create?
metrics:
  - fewer duplicate tasks
  - lower context cost
  - higher decision quality
related_notes:
  - ck_roi.md
tags:
  - roi
  - questions
  - tasks
  - notes
---

# ROI-aware Tasks, Notes And Questions

## ROI Scopes

```txt
ROI of question
ROI of note
ROI of task
ROI of briefing
ROI of agent
ROI of execution
ROI of learning
ROI of roadmap
```

## Operating ROI

| ROI Type | Example |
|---|---|
| Entropy reduction | The system knows what not to do. |
| Context cost reduction | Future agents need fewer files to understand state. |
| Duplicate prevention | Existing memory blocks redundant work. |
| Decision quality | Founder answers fewer but better questions. |
| Execution speed | Tasks are ready with context and approval. |
| Risk reduction | Sensitive or high-cost work pauses early. |
| Reuse | Notes become reusable context packs. |
| Learning | Feedback changes future behavior. |

## Evaluation Prompt

```txt
object:
roi_scope:
value_created:
cost_estimate:
risk_reduced:
evidence_needed:
memory_impact:
decision_unlocked:
```

## Candidate For Doc 27

Doc 27 should require every task to carry an ROI hypothesis. Status alone is not value.
