---
title: Intelligent Question System Study
file: 02_INTELLIGENT_QUESTION_SYSTEM_STUDY.md
layer: study
phase: 000_STUDY_NOTES
category: intelligent_question_system
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
purpose: Study intelligent questions as decision-unlocking operating objects that may appear at any phase of a CKOS project.
inputs:
  - 000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md
  - 03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
outputs:
  - question taxonomy
  - question quality contract
framework:
  - gap -> question -> answer -> decision -> memory
edge_cases:
  - generic question with no consequence
  - question asked after execution should have paused earlier
integrations:
  - context_pack_builder
  - approval_gate
  - eval_runner
prompts:
  - Ask only when the answer changes decision, risk, cost, ROI, approval, evidence or memory.
metrics:
  - questions with explicit decision impact
  - fewer rework loops
related_notes:
  - 03_BRIEFING_TO_TASKS_TRANSFORMER_STUDY.md
  - 09_ROI_AWARE_TASKS_NOTES_AND_QUESTIONS_STUDY.md
tags:
  - questions
  - ai_first
  - study
---

# Intelligent Question System

## Rule

No CKOS question should be asked without declaring:

```txt
reason
decision_unlocked
risk_reduced
roi_improved
consequence_if_unanswered
```

## Question Types

| Type | Use |
|---|---|
| `clarification_question` | Clarify ambiguous intention or output. |
| `risk_question` | Detect legal, security, operational or reputation risk. |
| `roi_question` | Decide whether work is worth the cost. |
| `cost_question` | Estimate CKC, token, tool, model or human effort. |
| `source_question` | Ask for evidence or source provenance. |
| `approval_question` | Stop until the right actor approves. |
| `scope_question` | Separate included and excluded work. |
| `memory_question` | Decide what should be retained, expired or ignored. |
| `learning_question` | Capture what should improve future runs. |
| `briefing_question` | Fill a structured briefing gap. |
| `feedback_question` | Convert feedback into action or memory. |
| `execution_question` | Pause execution when context changes. |

## Quality Contract

```yaml
question:
reason:
decision_unlocked:
risk_reduced:
roi_improved:
cost_or_time_impact:
consequence_if_unanswered:
recommended_default:
fallback_if_unanswered:
memory_update_needed:
```

## Example

Bad:

```txt
What is the project objective?
```

CKOS-quality:

```txt
Which result should be reached first: strategic clarity, fast execution or low-cost validation?

reason: The answer selects briefing, research or task planning as the next step.
decision_unlocked: Which workflow becomes P0.
risk_reduced: Avoids generating unnecessary documents.
roi_improved: Reduces context cost before agent allocation.
consequence_if_unanswered: The system may over-plan or execute the wrong path.
```

## Candidate For Doc 27

Doc 27 should define question-to-task and question-to-approval transformations. It should not treat questions as chat UX alone.
