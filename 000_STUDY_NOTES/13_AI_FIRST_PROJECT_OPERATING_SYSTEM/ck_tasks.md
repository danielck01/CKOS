---
title: AI-first Project Operating System Tasks
file: ck_tasks.md
layer: study
phase: 000_STUDY_NOTES
category: ai_first_project_operating_system_tasks
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
purpose: Track study tasks for Study Layer 13 using Kanban without creating runtime tasks.
inputs:
  - README.md
outputs:
  - study Kanban
framework:
  - Backlog
  - Ready
  - In Progress
  - Review
  - Done
  - Blocked
edge_cases:
  - Kanban mistaken for production task engine
  - Done mistaken for Founder approval
integrations:
  - SESSION_REGISTRY.md
prompts:
  - Keep tasks as study tasks only.
metrics:
  - all created study notes tracked
related_notes:
  - 05_TASK_AI_FIRST_SYSTEM_STUDY.md
tags:
  - tasks
  - kanban
  - study
---

# Study Tasks

This Kanban controls only the creation and audit of the study layer. It is not a runtime task board.

## Backlog

- PMO decide whether Doc 28 should become Notes/Memory/Knowledge or stay deferred.
- PMO decide whether a future agent civilization pack is needed after Doc 27 audit.
- Prepare final PMO fan-in synthesis after Claude audits of Doc 26 and Study Layer 13.

## Ready

- Claude/Metacognik audit of Study Layer 13.
- Claude read-only audit of Doc 26 v1.0.4 before Doc 27 or target-doc patches.
- PMO triage of canonical candidates from `13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md`.
- Founder review of next 5 or 10 tasks only after Work Order scope, risk ceiling, cost ceiling and fan-in audit are defined.
- Claude read-only audit of note 24 Doc 27 scope reconciliation and gate proposal.
- Claude/PMO audit of note 24 pre-gate allowed/forbidden/gate section list.
- Claude read-only audit of the 2026-06-01 Layer 13/14 gate cleanup.

## In Progress

- None.

## Review

- Study Layer 13 requires external audit after this creation session.
- Note 22 multi-session roadmap requires PMO/Metacognik audit before being used as strong operating guidance.
- Note 23 multi-model command and prompt dispatch board is AUXILIARY OPERATIONAL and requires PMO/Metacognik audit before being used as strong operating guidance.
- Note 24 Doc 27 scope reconciliation requires Claude/PMO/Metacognik audit before any Doc 27 checkout.
- Note 24 pre-gate section list requires Claude/PMO fan-in before Doc 27 may open.
- Note 25 local operator control room is AUXILIARY OPERATIONAL and requires PMO/Metacognik audit before being used as strong operational guidance.
- Note 26 local PMO multi-model control room is AUXILIARY OPERATIONAL and requires PMO/Metacognik audit before being used as strong operational guidance.

## Done

- Folder structure created.
- Root controls created.
- Notes 01-14 created.
- Checkout lock registered.
- Note 22 created as study-only multi-session roadmap and sprint board.
- Note 23 created as study-only multi-model command and prompt dispatch board (Windsurf as local PMO of support).
- Note 24 created as study-only Doc 27 scope reconciliation and gate proposal.
- Note 24 pre-gate section list created/updated with explicit allowed sections, forbidden sections and gate conditions.
- Note 25 created as study-only local operator control room and autonomous dispatch (Windsurf as local PMO of support and multi-model dispatch operator).
- Duplicate `23_*` ordinal reconciled: `23_MULTI_MODEL_COMMAND_AND_PROMPT_DISPATCH_BOARD_STUDY.md` remains note 23; former `23_LOCAL_PMO_MULTI_MODEL_CONTROL_ROOM_STUDY.md` was renamed to `26_LOCAL_PMO_MULTI_MODEL_CONTROL_ROOM_STUDY.md` as index cleanup only.
- Mandatory Layer 13/14 gate cleanup applied study-only: task vs Work Order boundary clarified, Doc 11 identifier warnings added, BRA Packet vs Work Order `context_pack` boundary reinforced, Paperclip wording regularized.
- Candidate split recorded: Doc 27 = Work Orders and Multi-Session Orchestration; future Doc 28 = Notes/RAG and retrieval governance; Doc 26 = connectors/MCP/external tools/webhooks/secret_refs.

## Blocked

- Doc 27 creation is blocked until Claude read-only audit of this cleanup, Claude PMO fan-in and explicit Founder/PMO gate.
- Doc 27 creation is also blocked until Doc 26 audit fan-in and explicit Founder/PMO gate.
- Doc 27 creation remains blocked until note 24 is audited and Founder/PMO explicitly approve a separate canonical checkout.
- Doc 27 creation remains blocked until Claude/PMO fan-in reconciles Codex 1, Codex 2, Claude 1, Claude 2 and Windsurf support.
- Notes/RAG full architecture is blocked from Doc 27 and deferred to future Doc 28 candidate scope.
- Antigravity remains blocked.
- Runtime implementation remains blocked.
