---
title: Project AI-first Operating Model Study
file: 01_PROJECT_AI_FIRST_OPERATING_MODEL.md
layer: study
phase: 000_STUDY_NOTES
category: project_ai_first_operating_model
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
purpose: Study what makes a CKOS project AI-first before any canonical task orchestration document is created.
inputs:
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - 02_EXECUTION_SYSTEM/07_WORKFLOW_BLUEPRINTS.md
  - 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
outputs:
  - project operating model
  - future Doc 27 candidate concepts
framework:
  - Founder intention -> CEO interpretation -> context pack -> questions -> briefing -> plan -> task graph -> agent allocation -> execution -> memory -> feedback -> ROI -> learning
edge_cases:
  - project becomes folder tree only
  - project starts execution without briefing
  - project memory becomes ungoverned chat history
integrations:
  - context_pack_builder
  - workflow_engine
  - approval_gate
  - memory_writer
prompts:
  - What decision does this project need before it becomes executable?
metrics:
  - fewer premature tasks
  - clearer approval gates
  - better project memory reuse
related_notes:
  - 03_BRIEFING_TO_TASKS_TRANSFORMER_STUDY.md
  - 05_TASK_AI_FIRST_SYSTEM_STUDY.md
tags:
  - project
  - ai_first
  - study
---

# Project AI-first Operating Model

## Definition

A CKOS project is not a folder plus tasks. It is a governed operating object that evolves from intention into decisions, memory, evidence, tasks, agents, approvals, outputs, feedback and learning.

## Proposed Study Flow

```txt
Founder intention
  -> CEO Agent interpretation
  -> minimal context pack
  -> intelligent questions
  -> briefing
  -> project plan
  -> task graph
  -> agent allocation
  -> controlled execution
  -> notes and memory
  -> feedback
  -> ROI snapshot
  -> learning capture
```

## Project AI-first Requirements

| Requirement | Study meaning |
|---|---|
| Intention trace | Every project starts with explicit origin intent. |
| Context packet | The project knows which memory, constraints and evidence matter. |
| Question loop | The project can ask intelligent questions at any step. |
| Briefing spine | Answers become structured briefing, not scattered chat. |
| Task graph | Tasks are related by dependency, risk, evidence and approval. |
| Agent allocation | Work is assigned by capability, scope and permission. |
| Memory loop | Decisions and learning become project memory. |
| ROI loop | Project work is justified by operational or financial value. |

## Non-Authority

This note is not a runtime state machine, not a database model and not a product UI specification. It studies what future canonical work must preserve.

## Candidate For Doc 27

Doc 27 should treat the project as the parent operating context for intelligent tasks. A task that cannot point back to project intention, briefing, context and approval should not be considered AI-first.
