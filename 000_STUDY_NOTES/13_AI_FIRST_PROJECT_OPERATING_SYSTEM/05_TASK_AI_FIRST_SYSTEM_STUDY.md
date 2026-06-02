---
title: Task AI-first System Study
file: 05_TASK_AI_FIRST_SYSTEM_STUDY.md
layer: study
phase: 000_STUDY_NOTES
category: task_ai_first_system
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
purpose: Study the AI-first task object without creating schemas, APIs, UI or runtime task automation.
inputs:
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
outputs:
  - task object candidate
  - task state candidate
framework:
  - task = intent + context + approval + evidence + output + learning
edge_cases:
  - task becomes generic status card
  - task runs without approval or checkout lock
integrations:
  - workflow_engine candidate
  - approval_gate candidate
  - cost_guard candidate
prompts:
  - What intent, question, risk, cost, approval and learning does this task carry?
metrics:
  - fewer untraceable tasks
  - tasks with evidence and ROI
related_notes:
  - 03_BRIEFING_TO_TASKS_TRANSFORMER_STUDY.md
  - 07_PARALLEL_EXECUTION_AND_CHECKOUT_LOCK_STUDY.md
tags:
  - tasks
  - ai_first
  - doc27_candidate
---

# Task AI-first System

## Task Definition

A generic task says what to do. An AI-first CKOS task explains why, from which context, with which risk, who may execute, what it costs, what evidence is needed and what learning should be captured.

## Candidate Task Fields

```yaml
task_id:
origin_intent:
source_question:
related_briefing:
context_pack:
required_skills:
required_agents:
risk_level:
cost_estimate:
roi_hypothesis:
approval_required:
checkout_lock:
execution_state:
evidence_required:
output_type:
feedback_loop:
learning_capture:
```

These are study fields, not a database schema.

## Candidate States

```txt
draft
needs_context
needs_question
ready
approved
locked
running
waiting_agent
waiting_founder
blocked_by_cost
blocked_by_risk
blocked_by_scope
in_review
released
rejected
archived
```

## AI-first Acceptance

A task is AI-first only when it can answer:

- What intention created it?
- What question or briefing answer shaped it?
- What context and memory does it need?
- What risk, cost and ROI does it carry?
- Who can approve it?
- What evidence proves it was done well?
- What feedback and learning should update memory?

## Candidate For Doc 27

Doc 27 should define tasks as governed operating objects, not as UI cards or plain Kanban items.
