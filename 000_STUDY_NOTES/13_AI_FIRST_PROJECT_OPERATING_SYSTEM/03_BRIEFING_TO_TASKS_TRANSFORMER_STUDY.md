---
title: Briefing To Tasks Transformer Study
file: 03_BRIEFING_TO_TASKS_TRANSFORMER_STUDY.md
layer: study
phase: 000_STUDY_NOTES
category: briefing_to_tasks_transformer
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
purpose: Study how intelligent briefing answers become AI-first task candidates without creating runtime transformer implementation.
inputs:
  - 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md
  - 02_EXECUTION_SYSTEM/07_WORKFLOW_BLUEPRINTS.md
outputs:
  - transformer candidate
  - task candidate rules
framework:
  - briefing answer -> intent extraction -> missing context detection -> task candidate -> risk -> agents -> cost -> approval -> batch
edge_cases:
  - answer becomes task without context
  - briefing creates too many low-value tasks
integrations:
  - transformerRegistry candidate
  - workflow_engine candidate
prompts:
  - Convert only decisions or gaps into task candidates when they change work.
metrics:
  - fewer low-value tasks
  - stronger task provenance
related_notes:
  - 02_INTELLIGENT_QUESTION_SYSTEM_STUDY.md
  - 05_TASK_AI_FIRST_SYSTEM_STUDY.md
tags:
  - briefing
  - transformer
  - tasks
---

# Briefing To Tasks Transformer

## Study Flow

```txt
briefing answer
  -> intent extraction
  -> missing context detection
  -> task candidate
  -> risk classification
  -> required agents
  -> cost estimate
  -> approval mode
  -> execution batch candidate
```

## Transformation Rules

| Rule | Meaning |
|---|---|
| Preserve origin | Every task candidate links to the briefing answer or question that created it. |
| Detect gaps first | Missing context may create a question, not a task. |
| Classify before planning | Risk, cost and approval mode come before execution. |
| Avoid task spam | If no decision, risk, evidence or output changes, do not create a task. |
| Use memory | Existing project memory should prevent duplicate tasks. |

## Candidate Task Derivation

```yaml
origin_briefing_ref:
source_question_ref:
intent_detected:
missing_context:
task_candidate:
risk_level:
cost_estimate:
required_skill_candidates:
required_agent_role_candidates:
approval_mode:
evidence_required:
memory_refs:
```

## Non-Implementation Boundary

This note does not create a transformerRegistry entry, database table, backend service or automation. It only describes the future contract that Doc 27 may canonize.

## Candidate For Doc 27

Doc 27 should include a briefing-to-task transformer section so tasks do not appear as isolated user instructions.
