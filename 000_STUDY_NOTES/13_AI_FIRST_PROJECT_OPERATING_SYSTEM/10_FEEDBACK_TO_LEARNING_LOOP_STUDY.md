---
title: Feedback To Learning Loop Study
file: 10_FEEDBACK_TO_LEARNING_LOOP_STUDY.md
layer: study
phase: 000_STUDY_NOTES
category: feedback_to_learning_loop
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
purpose: Study how feedback becomes memory, learning and future patch candidates.
inputs:
  - 03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - 06_BUSINESS_SYSTEMS/22_FEEDBACK_SYSTEM_ARCHITECTURE.md
outputs:
  - feedback learning pattern
framework:
  - feedback -> classify -> affected objects -> memory -> learning -> patch candidate -> audit
edge_cases:
  - feedback applied without classification
  - preference promoted to policy
integrations:
  - learning_loop_engine candidate
  - memory_writer candidate
prompts:
  - What should this feedback change next time?
metrics:
  - feedback converted to learning
  - fewer repeated corrections
related_notes:
  - ck_feedback.md
tags:
  - feedback
  - learning
  - memory
---

# Feedback To Learning Loop

## Flow

```txt
Founder feedback
  -> classify feedback
  -> affected notes
  -> affected prompts
  -> affected skills
  -> affected tasks
  -> update memory
  -> update learning
  -> create patch candidate
  -> audit
```

## Feedback Types

Feedback de execução deve referenciar os feedback_types do Doc 22 e não criar taxonomia paralela.

| Type | Possible result |
|---|---|
| `correction_feedback` | Fix note or candidate. |
| `preference_feedback` | Store preference memory if recurring. |
| `quality_feedback` | Add acceptance criterion. |
| `risk_feedback` | Add or escalate risk. |
| `roi_feedback` | Re-score priority. |
| `design_feedback` | Keep as design study only until gate. |
| `technical_feedback` | Create future implementation candidate only after canon. |
| `strategic_feedback` | Update PMO next-step memory. |

## Learning Rules

- Feedback is not automatically canonical.
- Feedback must identify affected note or decision.
- Repeated feedback becomes learning candidate.
- High-risk feedback requires Metacognik review.
- Implementation feedback remains blocked until proper gate.

## Candidate For Doc 27

Doc 27 should connect task completion to feedback and learning capture. A task that finishes without learning may still be operationally incomplete.
