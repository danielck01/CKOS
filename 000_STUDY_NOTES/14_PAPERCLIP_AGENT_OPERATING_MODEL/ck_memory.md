---
title: CK Memory - Study Layer 14 Paperclip Agent Operating Model
file: ck_memory.md
layer: study
study_layer: 14_PAPERCLIP_AGENT_OPERATING_MODEL
doc_type: study_memory
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
purpose: Track Study Layer 14 memory, file inventory, risks, and audit posture without granting canonical or implementation authority.
---

# CK Memory: Study Layer 14 - Paperclip Agent Operating Model

**Status**: Active memory for study layer, draft and unverified  
**Last Updated**: 2026-06-01  
**Purpose**: Track study progress, findings, and decisions for Paperclip benchmarking

## Study Sequence

| Note | Status | Summary |
|------|--------|---------|
| `README.md` | created | Study layer overview and non-authority boundary |
| `ck_memory.md` | created | This file - active memory |
| `ck_tasks.md` | created | Kanban for study tasks |
| `01_PAPERCLIP_ORG_CHART_AND_AGENT_MODEL_STUDY.md` | created | Agent registry, org charts, roles, reporting lines |
| `02_PAPERCLIP_HEARTBEAT_EXECUTION_STUDY.md` | created | Heartbeat scheduling, execution semantics, liveness recovery |
| `03_PAPERCLIP_WORK_TASK_AND_TICKET_SYSTEM_STUDY.md` | created | Issue model, parent/sub-structure, blockers, execution policies |
| `04_PAPERCLIP_GOVERNANCE_APPROVALS_AND_BUDGETS_STUDY.md` | created | Approval workflows, budget policies, cost control |
| `05_CKOS_DIFFERENTIATION_FROM_PAPERCLIP_STUDY.md` | created | Philosophical and architectural differences |
| `06_CKOS_ADOPTION_CANDIDATES_FOR_DOC27_STUDY.md` | regularized | Specific study-only patterns to keep, adapt, defer or reject for possible future Doc 27 consideration |
| `07_PAPERCLIP_TO_CKOS_TRANSLATION_MATRIX_STUDY.md` | created | Paperclip-to-CKOS translation matrix with forbidden interpretations |

## Layer 14 File Inventory

All Study Layer 14 files are expected to remain `layer: study`, `status: draft`, `provenance_status: unverified`, and `confidence: unverified` until external audit says otherwise.

| File | Role | Audit posture |
|------|------|---------------|
| `README.md` | Study index | pending Claude/PMO audit |
| `ck_memory.md` | Study memory | pending Claude/PMO audit |
| `ck_tasks.md` | Study task control | pending Claude/PMO audit |
| `01_PAPERCLIP_ORG_CHART_AND_AGENT_MODEL_STUDY.md` | Paperclip org chart and agent model study | pending Claude/PMO audit |
| `02_PAPERCLIP_HEARTBEAT_EXECUTION_STUDY.md` | Paperclip heartbeat and liveness study | pending Claude/PMO audit |
| `03_PAPERCLIP_WORK_TASK_AND_TICKET_SYSTEM_STUDY.md` | Paperclip work/task/ticket study | pending Claude/PMO audit |
| `04_PAPERCLIP_GOVERNANCE_APPROVALS_AND_BUDGETS_STUDY.md` | Paperclip governance/budget study | pending Claude/PMO audit |
| `05_CKOS_DIFFERENTIATION_FROM_PAPERCLIP_STUDY.md` | CKOS differentiation study | pending Claude/PMO audit |
| `06_CKOS_ADOPTION_CANDIDATES_FOR_DOC27_STUDY.md` | Study-only adoption candidate synthesis | pending Claude/PMO audit |
| `07_PAPERCLIP_TO_CKOS_TRANSLATION_MATRIX_STUDY.md` | Translation matrix and forbidden interpretation guardrail | pending Claude/PMO audit |

## Paperclip Source Analysis

### Repository Structure
- **Location**: `paperclip_study/` (cloned from paperclipai/paperclip)
- **Tech Stack**: Node.js, TypeScript, React, PostgreSQL (Drizzle ORM), pnpm
- **Key Directories**:
  - `server/` - Express REST API and orchestration services
  - `ui/` - React + Vite board UI
  - `packages/db/` - Drizzle schema, migrations, DB clients
  - `packages/shared/` - Shared types, constants, validators
  - `packages/adapters/` - Agent adapter implementations (Claude, Codex, Cursor, etc.)
  - `packages/plugins/` - Plugin system packages
  - `packages/skills-catalog/` - Skills catalog (bundled and optional)

### Key Documentation Read
- `README.md` - Product overview, features, architecture
- `AGENTS.md` - Engineering rules, repo map, dev setup
- `doc/GOAL.md` - Vision, problem, architecture (2-layer model)
- `doc/execution-semantics.md` - Execution model (542 lines, detailed)
- `doc/DATABASE.md` - Database setup (embedded PG, Docker, Supabase)
- `ROADMAP.md` - Milestones and roadmap

### Schema Analysis
- `packages/db/src/schema/index.ts` - 86 exports, full schema
- `agents.ts` - Agent registry with org chart fields
- `issues.ts` - Issue model with execution semantics
- `budget_policies.ts` - Budget control
- `approvals.ts` - Approval workflows

## Key Findings (Draft)

### 1. Paperclip Architecture
- **Two-layer model**: Control plane + Execution services (adapters)
- **Control plane**: Node.js server + React UI
- **Execution services**: Adapters for Claude, Codex, Cursor, OpenClaw, HTTP, etc.
- **Philosophy**: "If it can receive a heartbeat, it's hired"
- **Goal**: Backbone of autonomous economy, control plane for AI companies

### 2. Agent Model
- **Agent registry**: `agents` table with org chart fields
- **Fields**: name, role, title, icon, status, reportsTo, capabilities, adapterType, adapterConfig, runtimeConfig, budgetMonthlyCents, spentMonthlyCents, pauseReason, permissions, lastHeartbeatAt
- **Org chart**: Hierarchical via `reportsTo` field
- **Multi-company**: Company-scoped agents
- **Budget per agent**: Monthly budget tracking

### 3. Execution Semantics
- **Single-assignee model**: At most one assignee per issue (agent or user, never both)
- **Status semantics**: backlog, todo, in_progress, blocked, in_review, done, cancelled
- **Checkout vs execution**: `checkoutRunId` (ownership lock) vs `executionRunId` (live execution)
- **Parent/sub-structure**: Structural (work breakdown, rollup context)
- **Blockers**: Dependency semantics (explicit waiting relationships)
- **Liveness contract**: Non-terminal issues must have a live path or explicit recovery

### 4. Heartbeat Execution
- **DB-backed wakeup queue** with coalescing
- **Budget checks** before execution
- **Workspace resolution** and secret injection
- **Skill loading** and adapter invocation
- **Structured logs**, cost events, session state, audit trails
- **Recovery** handles orphaned runs automatically

### 5. Issue Model
- **Company-scoped**: All issues belong to a company
- **Goal hierarchy**: company → team → agent → task
- **Execution policy**: JSONB field for execution rules
- **Execution state**: JSONB field for runtime state
- **Monitor support**: One-shot deferred actions for async checks
- **Workspace isolation**: Project workspaces and execution workspaces

### 6. Governance
- **Approvals table**: Type-based approval workflows
- **Budget policies**: Per-scope budget limits with warn percent and hard stop
- **Activity log**: All mutating actions traced
- **Board access**: Full-control operator context
- **Agent API keys**: Hashed at rest, company-scoped

### 7. Cost Control
- **Token and cost tracking**: By company, agent, project, goal, issue, provider, model
- **Budget policies**: Scoped policies with warning thresholds and hard stops
- **Overspend handling**: Pauses agents and cancels queued work automatically

## Comparison with Study Layer 13

### CKOS Study Layer 13 Concepts
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

### Paperclip vs CKOS (Initial Assessment)
- **Similar**: Single-assignee model, checkout locks, budget control, approval workflows
- **Different**: Paperclip focuses on autonomous AI companies; CKOS focuses on AI-first project operating system
- **Paperclip strength**: Mature execution semantics, liveness recovery, multi-company isolation
- **CKOS strength**: Intelligent questions, briefing transformation, notes as memory, ROI awareness

## Gate Cleanup 2026-06-01

Codex 1 applied the mandatory pre-gate cleanup for Study Layer 14:

- note 06 was changed from implementation-style phase language to study classification tiers;
- Paperclip was reinforced as benchmarking material, not a CKOS blueprint;
- Paperclip runtime concepts remain forbidden as implementation instructions;
- Doc 27 remains blocked until Claude PMO fan-in and explicit Founder gate.

The next safe action is Claude read-only audit of this cleanup together with the Layer 13 cleanup.

## Open Questions for PMO

1. Should future CKOS canon evaluate Paperclip's two-layer model (control plane + adapters)?
2. Should future CKOS canon evaluate Paperclip's heartbeat execution model, or keep it rejected for initial scope?
3. Should future CKOS canon evaluate Paperclip's org chart model or use a different structure?
4. Should future CKOS canon evaluate Paperclip's budget and cost control mechanisms?
5. What is CKOS's target scope: project operating system or autonomous company control plane?
6. Should CKOS support multi-company isolation like Paperclip?
7. Should CKOS adopt Paperclip's approval workflow system?

## Next Steps

1. Claude read-only audit of Study Layer 14 notes 01-07 plus README, memory and tasks.
2. PMO/Metacognik classify candidates as study-only, future canonical candidate, rejected or blocked.
3. Founder/PMO decide whether any future Doc 27 checkout may open.
4. Keep Doc 27, backend, UI, API, database, migrations, MCP server real, JSON n8n, real agents and runtime automations blocked unless separately approved.

---

**Study First. Audit Second. Only Then Scope Doc 27.**
