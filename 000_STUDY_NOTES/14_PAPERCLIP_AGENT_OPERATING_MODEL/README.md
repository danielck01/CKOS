---
title: Study Layer 14 Paperclip Agent Operating Model
file: README.md
layer: study
study_layer: 14_PAPERCLIP_AGENT_OPERATING_MODEL
doc_type: study_index
phase: 000_STUDY_NOTES
category: paperclip_agent_operating_model
status: draft
version: 0.1.1
created_at: 2026-06-01
updated_at: 2026-06-01
owner: pmo_ckos
responsible_agent: codex
reviewers:
  - claude
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
  - metacognik
source_type: study_regularization
source_tool: codex
provenance_status: unverified
confidence: unverified
risk_level: high
purpose: Index the Paperclip Agent Operating Model study layer without granting canonical, Doc 27, or implementation authority.
---

# Study Layer 14: Paperclip Agent Operating Model

**Status**: Study-only, non-canonical  
**Purpose**: Comparative benchmarking of Paperclip as a non-authoritative reference for possible future CKOS agent operating system design  
**Created**: 2026-06-01  
**Layer**: 14_PAPERCLIP_AGENT_OPERATING_MODEL

## Non-Authority Boundary

This study layer is **non-canonical**, draft and unverified. It does not authorize any implementation, database migrations, API endpoints, real agents, MCP servers, webhooks or runtime automations. It is research material that may inform a future Doc 27 scope decision only after audit and explicit approval.

Paperclip is benchmarking material, not a CKOS blueprint. No Paperclip control-plane, heartbeat, schema, adapter, UI, scheduler, queue or runtime pattern is approved for implementation here.

Gate cleanup applied on 2026-06-01: note 06 now uses study classification tiers instead of implementation-style phases. Doc 27 remains blocked until Claude PMO fan-in and explicit Founder gate.

**This study does not:**
- Authorize Doc 27 creation
- Create database schemas
- Implement backend services
- Generate API endpoints
- Create runtime agents
- Authorize any production code

**This study does:**
- Benchmark Paperclip's architecture against CKOS requirements
- Identify possible future Doc 27 candidates for audit
- Document differentiation points
- Provide structured analysis for PMO decision-making

## Purpose

Study Layer 14 benchmarks Paperclip (paperclipai/paperclip) as a reference implementation for AI-first project operating systems. Paperclip is an open-source control plane for autonomous AI companies that orchestrates teams of agents with org charts, budgets, governance, goal alignment, and accountability.

**Research Questions:**
1. How does Paperclip model agent organizations and reporting structures?
2. What is Paperclip's heartbeat execution model and how does it handle liveness?
3. How does Paperclip structure work, tasks, and ticket systems?
4. What governance, approval, and budget control mechanisms does Paperclip provide?
5. Where does CKOS differ from Paperclip in philosophy and operating posture?
6. Which Paperclip patterns are viable study-only candidates for future CKOS Doc 27 consideration?

## Files

### Core Study Notes
- `01_PAPERCLIP_ORG_CHART_AND_AGENT_MODEL_STUDY.md` - Agent registry, org charts, roles, reporting lines
- `02_PAPERCLIP_HEARTBEAT_EXECUTION_STUDY.md` - Heartbeat scheduling, execution semantics, liveness recovery
- `03_PAPERCLIP_WORK_TASK_AND_TICKET_SYSTEM_STUDY.md` - Issue model, parent/sub-structure, blockers, execution policies
- `04_PAPERCLIP_GOVERNANCE_APPROVALS_AND_BUDGETS_STUDY.md` - Approval workflows, budget policies, cost control
- `05_CKOS_DIFFERENTIATION_FROM_PAPERCLIP_STUDY.md` - Philosophical and architectural differences
- `06_CKOS_ADOPTION_CANDIDATES_FOR_DOC27_STUDY.md` - Specific patterns to adopt or adapt
- `07_PAPERCLIP_TO_CKOS_TRANSLATION_MATRIX_STUDY.md` - Translation matrix with keep/adapt/reject, ROI, risk, Doc 27 candidacy, and forbidden interpretations

### Memory and Control
- `ck_memory.md` - Active memory for this study layer
- `ck_tasks.md` - Kanban-style task control for study work

## Paperclip Architecture Overview

Paperclip is a two-layer system:

**Layer 1: Control Plane (Node.js server + React UI)**
- Agent registry and org chart
- Task assignment and status tracking
- Budget and token spend tracking
- Issue comments, documents, work products, attachments
- Goal hierarchy (company → team → agent → task)
- Heartbeat monitoring and execution locks

**Layer 2: Execution Services (adapters)**
- Local CLI/session adapters (Claude Code, Codex, Gemini, Cursor)
- HTTP/process-style adapters for custom runtimes
- OpenClaw gateway for remote agents
- External adapter plugins

**Key Principle**: "If it can receive a heartbeat, it's hired."

## Study Methodology

1. **Code Analysis**: Read Paperclip source code, schema definitions, and documentation
2. **Pattern Extraction**: Identify architectural patterns, data models, and execution semantics
3. **Comparative Analysis**: Map Paperclip patterns to CKOS Study Layer 13 concepts
4. **Differentiation**: Document where CKOS should diverge from Paperclip
5. **Adoption Recommendations**: Propose study-only patterns for possible future Doc 27 evaluation

## Relationship to Study Layer 13

Study Layer 13 defined CKOS's AI-first project operating system concepts:
- Intelligent question system
- Briefing-to-tasks transformation
- Notes as operational memory
- Task AI-first system
- Superagent/agent/subagent work allocation
- Parallel execution and checkout locks
- Founder approval batch control
- ROI-aware tasks, notes, and questions
- Feedback to learning loop
- Project self-documentation
- RAG metadata and vector categories
- Canonical patch candidates for Doc 27

Study Layer 14 benchmarks Paperclip against these concepts to validate design decisions and identify gaps.

## Next Steps

After this regularization:
1. Claude read-only audit of Study Layer 14
2. PMO/Metacognik review of audit findings
3. Founder/PMO decision on whether any future Doc 27 scope may be opened
4. Separate canonical checkout only if explicitly approved

---

**Study First. Audit Second. Only Then Scope Doc 27.**
