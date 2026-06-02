---
title: Acceptance Criteria For Doc 27
file: 14_ACCEPTANCE_CRITERIA_FOR_DOC27.md
layer: study
phase: 000_STUDY_NOTES
category: doc27_acceptance_criteria
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
purpose: Define study-layer acceptance criteria before a future Doc 27 may be created.
inputs:
  - 13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
outputs:
  - acceptance criteria
  - rejection criteria
framework:
  - study audit -> PMO decision -> canonical checkout
edge_cases:
  - Doc 27 becomes Kanban
  - Doc 27 authorizes implementation
integrations:
  - future Doc 27
  - Metacognik audit
prompts:
  - Reject Doc 27 if it lacks AI-first cognition, approval, memory, ROI and learning.
metrics:
  - criteria ready before canonical creation
related_notes:
  - 13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md
tags:
  - acceptance
  - doc27
  - study
---

# Acceptance Criteria For Doc 27

## Must Have

Doc 27 may be created only if the approved scope:

- does not create a generic task list;
- does not become a normal Kanban document;
- does not skip intelligent briefing;
- does not ignore intelligent questions;
- does not allow execution without approval gates;
- does not allow parallelism without checkout lock;
- does not treat agents as loose executors;
- does not measure tasks only by status;
- always records cost, risk, ROI, evidence and learning;
- preserves tenant isolation, permission and audit principles;
- keeps implementation blocked until later gates.

## Must Include

| Area | Required treatment |
|---|---|
| Task model | Origin intent, source question, briefing, context pack and output type. |
| Task state | Draft through released/rejected/archived, with blockers. |
| Approval | Founder/PMO/Metacognik gates where risk, cost or canon changes. |
| Agent allocation | Planner, executor, auditor and approver separation. |
| Memory | Task completion updates notes and memory under policy. |
| Feedback | Feedback becomes learning or patch candidate after classification. |
| ROI | Operational ROI is explicit. |
| Parallel execution | Checkout lock/release is part of orchestration. |

## Must Not Include

- UI components or screen design.
- Backend/API/database/migration instructions.
- Real agents, service accounts or runtime automations.
- MCP server creation.
- n8n workflow JSON.
- Changes to docs 01-26.
- Creation of docs 28-34.

## Audit Requirement

Metacognik should audit Study Layer 13 before Doc 27 is authorized. If critical blockers remain, PMO should request light patches to this study layer before canonical work.
