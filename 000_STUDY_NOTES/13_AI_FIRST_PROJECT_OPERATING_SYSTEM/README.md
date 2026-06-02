---
title: AI-first Project Operating System Study Layer
file: README.md
layer: study
phase: 000_STUDY_NOTES
category: ai_first_project_operating_system
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
purpose: Define the non-canonical study layer for Project AI-first, Task AI-first, Notes AI-first and intelligent question operations before any Doc 27 canonical work.
inputs:
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
  - 000_ROADMAPS/ROADMAP_ROUTING_MATRIX.md
  - 000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - 02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md
  - 02_EXECUTION_SYSTEM/07_WORKFLOW_BLUEPRINTS.md
  - 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - 03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - 03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - 07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md
outputs:
  - study folder index
  - operating memory controls
  - Doc 27 preparation notes
  - canonical patch candidates
framework:
  - intention -> intelligent questions -> briefing -> plan -> tasks -> agents -> notes -> memory -> execution -> feedback -> ROI -> learning
  - RAW -> STUDY -> CANONICAL
  - checkout lock -> controlled write -> checkout release
edge_cases:
  - generic task list mistaken for AI-first operating system
  - study note mistaken for canonical Doc 27
  - agent pack created before architecture approval
  - Antigravity or UI work started from study language
integrations:
  - PMO_CKOS
  - Metacognik
  - future Doc 27
  - Multi-Session Execution Policy
prompts:
  - Keep this layer as study only. Convert nothing to implementation without future canonical approval.
metrics:
  - all notes declare non-authority
  - zero canonical docs created
  - zero runtime agents created
  - Doc 27 scope made clearer after audit
related_notes:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/14_ACCEPTANCE_CRITERIA_FOR_DOC27.md
tags:
  - study
  - ai_first
  - projects
  - tasks
  - notes
  - questions
  - doc27_candidate
---

# AI-first Project Operating System Study Layer

## Status

This folder is STUDY only. It does not create Doc 27, does not authorize implementation, does not create UI, backend, API, database, migrations, agents, MCP servers, n8n JSONs or runtime automations.

The purpose is to prepare the cognitive-operational infrastructure that must exist before a canonical architecture for intelligent tasks and agent work orchestration is written.

The file inventory below is an operational study index only. It is not a canonical source of truth, not a provenance claim that this reconciliation created older notes, and not authority to promote any note into Doc 27.

Ordinal cleanup applied on 2026-06-01: `23_MULTI_MODEL_COMMAND_AND_PROMPT_DISPATCH_BOARD_STUDY.md` remains note 23. The former `23_LOCAL_PMO_MULTI_MODEL_CONTROL_ROOM_STUDY.md` was renamed to `26_LOCAL_PMO_MULTI_MODEL_CONTROL_ROOM_STUDY.md`, the next free study ordinal. This is an index reconciliation only, not a new conceptual note and not a Doc 27 action.

## Operating Thesis

CKOS should not treat tasks as simple checklist items. A CKOS task is the operational result of intention, context, intelligent questions, briefing, risk, cost, approval, evidence, agent allocation, memory, feedback and learning.

The study object of this folder is:

```txt
intention
  -> intelligent questions
  -> briefing
  -> plan
  -> AI-first tasks
  -> superagents / agents / subagents
  -> notes
  -> memory
  -> controlled execution
  -> feedback
  -> ROI
  -> learning
  -> self-documenting project evolution
```

## Files

| File | Function |
|---|---|
| `ck_memory.md` | Active memory and PMO state for this study layer. |
| `ck_tasks.md` | Kanban-style study task control. |
| `ck_risks.md` | Risk register for premature canonization or implementation drift. |
| `ck_roi.md` | Operational ROI model for questions, notes, tasks and learning. |
| `ck_feedback.md` | Feedback capture and conversion into study or patch candidates. |
| `ck_agent_handoffs.md` | Role and handoff study for Founder, PMO, Metacognik and future agents. |
| `01_PROJECT_AI_FIRST_OPERATING_MODEL.md` | Project AI-first operating model. |
| `02_INTELLIGENT_QUESTION_SYSTEM_STUDY.md` | Intelligent question system. |
| `03_BRIEFING_TO_TASKS_TRANSFORMER_STUDY.md` | Briefing-to-task transformation. |
| `04_NOTES_AS_OPERATIONAL_MEMORY_STUDY.md` | Notes as operational memory. |
| `05_TASK_AI_FIRST_SYSTEM_STUDY.md` | AI-first task model. |
| `06_SUPERAGENT_AGENT_SUBAGENT_WORK_ALLOCATION_STUDY.md` | Work allocation across agent layers. |
| `07_PARALLEL_EXECUTION_AND_CHECKOUT_LOCK_STUDY.md` | Parallel session and checkout lock study. |
| `08_FOUNDER_APPROVAL_BATCH_CONTROL_STUDY.md` | Founder batch approval modes. |
| `09_ROI_AWARE_TASKS_NOTES_AND_QUESTIONS_STUDY.md` | ROI-aware operation. |
| `10_FEEDBACK_TO_LEARNING_LOOP_STUDY.md` | Feedback-to-learning loop. |
| `11_PROJECT_SELF_DOCUMENTATION_SYSTEM_STUDY.md` | Self-documenting project system. |
| `12_RAG_METADATA_AND_VECTOR_CATEGORY_STUDY.md` | RAG metadata and vector category rules. |
| `13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md` | Candidate material for Doc 27. |
| `14_ACCEPTANCE_CRITERIA_FOR_DOC27.md` | Acceptance criteria before Doc 27 may be created. |
| `15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md` | Work Orders, batch execution, fan-out/fan-in, lock and release study. |
| `16_SMART_QUESTIONS_AND_CONTEXTUAL_INTERVENTION_STUDY.md` | Contextual smart questions before and during execution. |
| `17_COGNIK_METACOGNIK_TASK_ORCHESTRATION_STUDY.md` | Cognik and Metacognik responsibilities in task orchestration. |
| `18_AI_FIRST_PROJECT_NOTE_SYSTEM_AND_RAG_GOVERNANCE_STUDY.md` | Project note system and RAG governance for orchestration support. |
| `19_FOUNDER_CONTROL_APPROVAL_BATCHES_AND_AUTONOMY_LEVELS_STUDY.md` | Founder approval envelopes, batch limits and autonomy boundaries. |
| `20_PROMPT_PACK_FOR_MULTI_SESSION_CLAUDE_AUDITS_STUDY.md` | Prompt pack study for multi-session Claude/Metacognik audits. |
| `21_BRA_BRIEFING_RELAY_ARCHITECTURE_STUDY.md` | BRA briefing relay architecture study for cross-session communication. |
| `22_MULTI_SESSION_EXECUTION_ROADMAP_AND_SPRINT_BOARD_STUDY.md` | Multi-session roadmap and sprint board study. |
| `23_MULTI_MODEL_COMMAND_AND_PROMPT_DISPATCH_BOARD_STUDY.md` | AUXILIARY OPERATIONAL dispatch board for multi-model command and prompt coordination; not a direct Doc 27 candidate. |
| `24_DOC27_SCOPE_RECONCILIATION_AND_GATE_PROPOSAL_STUDY.md` | Study-only Doc 27 scope reconciliation and gate proposal. |
| `25_LOCAL_OPERATOR_CONTROL_ROOM_AND_AUTONOMOUS_DISPATCH_STUDY.md` | AUXILIARY OPERATIONAL local operator control room; not a direct Doc 27 candidate. |
| `26_LOCAL_PMO_MULTI_MODEL_CONTROL_ROOM_STUDY.md` | AUXILIARY OPERATIONAL local PMO control room, index-reconciled from the former duplicate `23_LOCAL...`; not a direct Doc 27 candidate. |

## Non-Authority Boundary

This folder may:

- study operating models;
- identify future canonical patch candidates;
- register risks, ROI and handoffs;
- prepare questions for PMO/Founder/Metacognik review.

This folder may not:

- create canonical docs 27-34;
- modify docs 01-26;
- define production schemas or migrations;
- create services, APIs, UI, agents, MCP servers, webhooks or automations;
- promote Antigravity, n8n or any provider to CKOS runtime.

## Doc 27 Preparation Rule

Doc 27 can only be scoped after PMO and Metacognik audit this folder. Until then, likely Doc 27 material remains candidate-only.

Notes 01-26 remain study artifacts. Listing them together reconciles operational readability only; it does not canonize the sequence, create Doc 27, create docs 28-34, or authorize implementation.
