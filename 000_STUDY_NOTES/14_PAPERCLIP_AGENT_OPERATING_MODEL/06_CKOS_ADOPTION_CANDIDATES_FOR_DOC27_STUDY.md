---
title: CKOS Adoption Candidates For Future Doc 27 Study
file: 06_CKOS_ADOPTION_CANDIDATES_FOR_DOC27_STUDY.md
layer: study
study_layer: 14_PAPERCLIP_AGENT_OPERATING_MODEL
doc_type: study_note
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
source_type: paperclip_benchmark_study_regularized
source_tool: codex
provenance_status: unverified
confidence: unverified
risk_level: high
purpose: Synthesize Paperclip patterns as study-only candidates for possible future Doc 27 consideration without approving Doc 27 or implementation.
---

# 06_CKOS_ADOPTION_CANDIDATES_FOR_DOC27_STUDY.md

**Study Layer**: 14_PAPERCLIP_AGENT_OPERATING_MODEL  
**Note**: 06  
**Status**: Study-only, non-canonical  
**Created**: 2026-06-01  
**Purpose**: Synthesize specific Paperclip patterns as study-only candidates for possible future CKOS Doc 27 consideration

## Non-Authority Boundary

This file is study-only, draft and unverified. It is not canonical.

It does not authorize Doc 27. It does not create Doc 27. It does not authorize backend, UI, API, database, migrations, real agents, runtime automations, n8n JSONs, MCP servers, webhooks or production schemas.

It may coordinate future sessions as a non-canonical operating note. It may not override `SESSION_REGISTRY.md`, `MULTI_SESSION_EXECUTION_POLICY.md`, canonical docs, Founder approval or PMO/Metacognik audit.

Paperclip is benchmarking material only. It is not a CKOS blueprint, not a roadmap to implement and not evidence that CKOS should copy Paperclip runtime architecture. The labels below are study classification tiers, not implementation phases.

Regularization note: every adopt/adapt/defer/reject label below is a study classification only. No table, field, API, runtime adapter, backend service, UI screen, migration, scheduler, webhook, MCP server, real agent or automation is approved here. Any schema/API/roadmap wording inherited from Paperclip analysis is a future evaluation topic, not an implementation instruction.

## Overview

This note synthesizes the adoption candidates from notes 01-05 into a prioritized study list for possible future Doc 27 consideration. It categorizes patterns by study posture (adopt, adapt, defer, reject) and provides non-authoritative evaluation notes for each candidate.

## Adoption Priority Framework

### Adopt
Patterns that CKOS could keep as future canonical candidates with minimal conceptual change, if later approved.

### Adapt
Patterns that CKOS could adapt to fit CKOS's philosophical and architectural differences, if later approved.

### Defer
Patterns that CKOS should keep outside any initial Doc 27 candidate scope unless a later audit reopens them.

### Reject
Patterns that CKOS should reject for current CKOS scope because they do not align with study findings.

## High-Priority Adoptions (Adopt)

### 1. Single-Assignee Model

**Source**: Paperclip execution semantics (note 02)

**Description**: Each task has at most one assignee (agent or user, never both).

**Rationale for Adoption**:
- Prevents confusion and double-work
- Clear ownership semantics
- Simplifies execution logic
- Proven in production by Paperclip

**Study-Only Evaluation Notes**:
- Future canon could evaluate whether agent/user assignee concepts are needed.
- Future canon could require a single-assignee invariant without naming physical fields.
- Future canon could define unassigned as a safe resting state.
- Future implementation details, APIs and constraints remain forbidden here.

**CKOS Adaptation**: None needed - adopt as-is.

### 2. Atomic Checkout with Execution Locks

**Source**: Paperclip execution semantics (note 02)

**Description**: Task checkout and execution locks are atomic, preventing double-work.

**Rationale for Adoption**:
- Ensures no double-work
- Prevents race conditions in parallel execution
- Critical for multi-agent systems
- Aligns with CKOS Study Layer 13 checkout lock concept

**Study-Only Evaluation Notes**:
- Future canon could evaluate separate ownership-lock and live-execution concepts.
- Future canon could preserve atomic checkout as a conceptual invariant.
- Startup, restart, index and lock-clearing details remain implementation-only and forbidden here.

**CKOS Adaptation**: None needed - adopt as-is.

### 3. Company-Scoped Data Isolation

**Source**: Paperclip agent and issue schemas (notes 01, 03)

**Description**: All entities are company-scoped with complete data isolation.

**Rationale for Adoption**:
- Enables multi-tenancy
- Clean separation of concerns
- Future-proof for multi-organization support
- Aligns with CKOS's potential whitelabel needs

**Study-Only Evaluation Notes**:
- Future canon could evaluate an organization/company scope boundary.
- Future canon could require isolation semantics without approving tables, routes or indexes.
- API, database and access-control implementation details remain forbidden here.

**CKOS Adaptation**: May rename "company" to "organization" to align with CKOS terminology.

### 4. Activity Logging

**Source**: Paperclip governance (note 04)

**Description**: All mutating actions are logged with actor, action, entity, and changes.

**Rationale for Adoption**:
- Complete audit trail
- Debugging support
- Compliance requirements
- Learning and improvement

**Study-Only Evaluation Notes**:
- Future canon could evaluate activity logging as an audit concept.
- Future canon could define minimum actor/action/entity/change semantics.
- Tables, indexes and UI viewers remain forbidden implementation details here.

**CKOS Adaptation**: None needed - adopt as-is.

## High-Priority Adoptions (Adapt)

### 5. Parent/Sub-Issue Structure

**Source**: Paperclip issue model (note 03)

**Description**: Hierarchical structure for work breakdown and rollup context.

**Rationale for Adoption**:
- Clear work breakdown
- Rollup context for reporting
- Explains why child tasks exist
- Wakes parent when all children complete

**Study-Only Evaluation Notes**:
- Future canon could evaluate parent/sub-task structure as a work-breakdown concept.
- Future canon could limit depth and clarify that structure is not dependency.
- Fields, queries, wake logic and indexes remain forbidden implementation details here.

**CKOS Adaptation**:
- Rename "issue" to "task" to align with CKOS terminology
- Simplify to 2-3 levels of depth (not arbitrary nesting)
- Integrate with superagent/agent/subagent model from Study Layer 13

### 6. Blocker Dependencies

**Source**: Paperclip issue model (note 03)

**Description**: Explicit waiting relationships with automatic wakeups.

**Rationale for Adoption**:
- Clear dependency semantics
- Automatic wakeups when blockers resolve
- Prevents blocked tasks from executing
- Separates structure from dependency

**Study-Only Evaluation Notes**:
- Future canon could evaluate explicit blocker relationships.
- Future canon could clarify whether blocker resolution creates a review signal or a future wake candidate.
- Tables, fields, automatic wake logic and UI visualization remain forbidden implementation details here.

**CKOS Adaptation**:
- Rename "issue" to "task" to align with CKOS terminology
- Simplify to direct blocking only (no transitive blocking initially)
- Integrate with superagent/agent/subagent model from Study Layer 13

### 7. Adapter-Based Execution

**Source**: Paperclip agent model (note 01)

**Description**: "If it can receive a heartbeat, it's hired" - flexible adapter model.

**Rationale for Adoption**:
- Flexibility to work with different AI providers
- Extensible without core changes
- Aligns with CKOS's need to work with Claude, Codex, etc.
- Future-proofs for new providers

**Study-Only Evaluation Notes**:
- Future canon could evaluate adapter boundaries at the concept level only.
- Future canon should decide whether heartbeat belongs in CKOS or remains rejected for initial scope.
- Real adapters, registries, loaders and agent schemas remain forbidden implementation details here.

**CKOS Adaptation**:
- Simplify to on-demand execution (not heartbeat-based)
- Focus on briefing-to-tasks transformation
- Integrate with CKOS's intelligent question system

### 8. Workspace Isolation

**Source**: Paperclip issue model (note 03)

**Description**: Separate project and execution workspaces for clean separation of concerns.

**Rationale for Adoption**:
- Clean separation of project context and execution context
- Supports git worktrees and sandbox environments
- Prevents execution from polluting project context
- Aligns with CKOS's project execution needs

**Study-Only Evaluation Notes**:
- Future canon could evaluate project and execution workspace separation.
- Future canon could map this to existing CKOS checkout-lock discipline before adding new concepts.
- Tables, task fields, resolution logic and APIs remain forbidden implementation details here.

**CKOS Adaptation**:
- Simplify to single workspace type initially
- Add execution workspace isolation in future iterations
- Integrate with CKOS's project model

## Medium-Priority Adoptions (Adopt)

### 9. Approval Workflows

**Source**: Paperclip governance (note 04)

**Description**: Typed approval workflows with request/review/decision phases.

**Rationale for Adoption**:
- Structured governance
- Clear approval audit trail
- Supports Founder approval batch control from Study Layer 13
- Extensible for different approval types

**Study-Only Evaluation Notes**:
- Future canon could evaluate typed approvals as an extension of Founder control.
- Future canon could define request/review/decision semantics without creating workflow infrastructure.
- Tables, APIs and UI remain forbidden implementation details here.

**CKOS Adaptation**:
- Simplify to Founder approval only initially
- Add multi-user approvals in future iterations
- Integrate with CKOS's Founder approval batch control

### 10. Cost Tracking

**Source**: Paperclip governance (note 04)

**Description**: Multi-level cost tracking (company, agent, project, goal, task).

**Rationale for Adoption**:
- Visibility into spend
- Supports ROI calculations
- Enables budget enforcement
- Aligns with CKOS's ROI-aware model

**Study-Only Evaluation Notes**:
- Future canon could evaluate cost events as ROI evidence.
- Future canon could decide whether cost should be tracked by project, task, model or session.
- Tables, aggregation queries and UI visualization remain forbidden implementation details here.

**CKOS Adaptation**:
- Focus on ROI-based cost tracking (not cents-level precision)
- Track at project and task level (not agent level)
- Integrate with CKOS's ROI-aware task model

## Medium-Priority Adoptions (Adapt)

### 11. Goal Hierarchy

**Source**: Paperclip issue model (note 03)

**Description**: Company → team → agent → task goal hierarchy.

**Rationale for Adoption**:
- Goal alignment for all work
- Agents see the "why" not just the "what"
- Supports strategic alignment
- Aligns with CKOS's intelligent question system

**Study-Only Evaluation Notes**:
- Future canon could evaluate goal hierarchy as context for why work exists.
- Future canon could start with project-to-task goal language if approved.
- Tables, fields, queries and UI visualization remain forbidden implementation details here.

**CKOS Adaptation**:
- Simplify to project → task goal hierarchy initially
- Add team and agent levels in future iterations
- Integrate with CKOS's intelligent question system

### 12. Task Status Semantics

**Source**: Paperclip execution semantics (note 02)

**Description**: Clear status semantics (backlog, todo, in_progress, blocked, in_review, done, cancelled).

**Rationale for Adoption**:
- Clear state machine
- Prevents ambiguous states
- Supports execution logic
- Aligns with CKOS's task model

**Study-Only Evaluation Notes**:
- Future canon could evaluate a minimal status vocabulary.
- Future canon could define status semantics before any state machine exists.
- Enums, transition logic, queries and UI visualization remain forbidden implementation details here.

**CKOS Adaptation**:
- Simplify to 5-6 statuses initially
- Add advanced statuses (in_review, blocked) in future iterations
- Integrate with CKOS's briefing-to-tasks transformation

## Low-Priority Adoptions (Defer)

### 13. Issue Monitors

**Source**: Paperclip execution semantics (note 02)

**Description**: One-shot deferred actions for async external checks.

**Rationale for Deferral**:
- CKOS uses on-demand execution, not autonomous 24/7 execution
- Async checks may not be needed initially
- Can add in future if async workflows are required

**Study-Only Evaluation Notes**: Keep deferred as a future evaluation topic only. No Doc 27 v2 or implementation scope is authorized here.

### 14. Silent Active-Run Watchdog

**Source**: Paperclip execution semantics (note 02)

**Description**: Detects unhealthy but still-running processes.

**Rationale for Deferral**:
- CKOS uses on-demand execution, not long-running autonomous processes
- Simpler timeout model may suffice
- Can add in future if long-running tasks are required

**Study-Only Evaluation Notes**: Keep deferred as a future evaluation topic only. No Doc 27 v2 or implementation scope is authorized here.

### 15. Sophisticated Liveness Recovery

**Source**: Paperclip execution semantics (note 02)

**Description**: Auto-recover, explicit recovery actions, human escalation.

**Rationale for Deferral**:
- CKOS uses on-demand execution, not autonomous 24/7 execution
- Simpler retry model may suffice
- Can add in future if autonomous execution is required

**Study-Only Evaluation Notes**: Keep deferred as a future evaluation topic only. No Doc 27 v2 or implementation scope is authorized here.

### 16. Multi-User Board Access

**Source**: Paperclip governance (note 04)

**Description**: Multi-user board access with role-based permissions.

**Rationale for Deferral**:
- CKOS may start as single-user
- Multi-user adds significant complexity
- Can add in future when multi-user is required

**Study-Only Evaluation Notes**: Keep deferred as a future evaluation topic only. No Doc 27 v2 or implementation scope is authorized here.

### 17. Skills Catalog and Injection

**Source**: Paperclip skills catalog (not deeply analyzed)

**Description**: Runtime skill injection for agents.

**Rationale for Deferral**:
- CKOS focuses on intelligent questions and briefing transformation
- Skills may be over-engineering for initial scope
- Can add in future if skill-based execution is required

**Study-Only Evaluation Notes**: Keep deferred as a future evaluation topic only. No Doc 27 v2 or implementation scope is authorized here.

### 18. Plugin System

**Source**: Paperclip plugin system (not deeply analyzed)

**Description**: Out-of-process plugin workers with capability-gated host services.

**Rationale for Deferral**:
- CKOS may not need extensibility initially
- Plugin system adds significant complexity
- Can add in future if extensibility is required

**Study-Only Evaluation Notes**: Keep deferred as a future evaluation topic only. No Doc 27 v2 or implementation scope is authorized here.

## Rejected Patterns

### 1. Hierarchical Org Chart

**Source**: Paperclip agent model (note 01)

**Description**: Corporate-style org chart with CEO, CTO, etc.

**Rationale for Rejection**:
- CKOS targets project execution, not autonomous companies
- Superagent/agent/subagent model from Study Layer 13 is more appropriate
- Corporate hierarchies don't align with project work

**Alternative**: Use superagent/agent/subagent model from Study Layer 13.

### 2. Per-Agent Monthly Budgets

**Source**: Paperclip agent model (note 01)

**Description**: Monthly budget limits per agent with hard stops.

**Rationale for Rejection**:
- CKOS focuses on ROI-aware tasks, not per-agent salaries
- Per-agent budgets don't align with project execution model
- ROI-aware budget model from Study Layer 13 is more appropriate

**Alternative**: Use ROI-aware task budgets from Study Layer 13.

### 3. Heartbeat-Based Autonomous Execution

**Source**: Paperclip execution semantics (note 02)

**Description**: Scheduled heartbeats for 24/7 autonomous execution.

**Rationale for Rejection**:
- CKOS targets on-demand execution triggered by briefings
- 24/7 autonomous execution is not the initial goal
- On-demand model aligns better with project execution

**Alternative**: Use on-demand execution triggered by briefings.

### 4. Rich Issue Model with 40+ Fields

**Source**: Paperclip issue model (note 03)

**Description**: Very rich issue model with many fields and tables.

**Rationale for Rejection**:
- Over-engineering for CKOS's initial needs
- Simpler task model suffices for project execution
- Can add fields incrementally as needed

**Alternative**: Future canon could evaluate a simpler task model and defer field-level detail.

### 5. Multi-Company Isolation

**Source**: Paperclip architecture (README)

**Description**: One deployment running multiple companies with complete isolation.

**Rationale for Rejection**:
- CKOS may not need multi-company support initially
- Single-organization focus may simplify any future approved scope
- Can add multi-organization support in future

**Alternative**: Future canon could start with single-organization language and defer multi-organization support.

## Future Doc 27 Candidate Sequence (Study Only)

This sequence is not a roadmap to build. It is a classification aid for a later Founder/PMO/Metacognik decision about whether any narrow Doc 27 checkout should exist.

### Candidate Theme 1: Core Task Model

**Adopt**:
- Single-assignee model
- Atomic checkout with execution locks
- Company-scoped data isolation
- Activity logging

**Adapt**:
- Parent/sub-task structure (simplified)
- Blocker dependencies (simplified)
- Adapter-based execution (simplified for on-demand)

**Future review questions**:
- Which task fields are minimal enough for a future canonical draft?
- Which assignment boundaries are conceptual only versus runtime-specific?
- Which execution terms must remain blocked until implementation readiness?
- Which audit log concepts belong in Doc 27 versus a later governance doc?

### Candidate Theme 2: Governance And Budget

**Adopt**:
- Approval workflows (simplified to Founder approval)
- Cost tracking (ROI-based)

**Adapt**:
- Goal hierarchy (simplified to project → task)
- Task status semantics (simplified)

**Future review questions**:
- Which approval concepts map to Founder control without overbuilding?
- Which cost/ROI concepts belong in canonical language before any runtime work?
- Which goal hierarchy terms are safe without creating ghost tables?
- Which status semantics are required for audit clarity only?

### Candidate Theme 3: Workspace Isolation

**Adopt**:
- Workspace isolation (simplified)

**Future review questions**:
- Should workspace isolation be canonical in Doc 27 or deferred?
- What forbidden interpretation prevents workspace language from becoming runtime work?
- Which existing CKOS checkout-lock concepts already cover this need?

### Candidate Theme 4: Advanced Features

**Defer**:
- Issue monitors
- Silent active-run watchdog
- Sophisticated liveness recovery
- Multi-user board access
- Skills catalog and injection
- Plugin system

**Future review questions**:
- Should advanced execution remain blocked until a later architecture layer?
- Should multi-user support remain outside initial Doc 27 scope?
- Should extensibility features stay rejected until PMO sees measurable ROI?

## Summary Table

| Pattern | Priority | Action | Study classification tier |
|---------|----------|--------|-------|
| Single-assignee model | High | Adopt | Tier A - strongest study candidate |
| Atomic checkout with execution locks | High | Adopt | Tier A - strongest study candidate |
| Company-scoped data isolation | High | Adopt | Tier A - strongest study candidate |
| Activity logging | High | Adopt | Tier A - strongest study candidate |
| Parent/sub-task structure | High | Adapt | Tier A - strongest study candidate |
| Blocker dependencies | High | Adapt | Tier A - strongest study candidate |
| Adapter-based execution | High | Adapt | Tier A - strongest study candidate |
| Workspace isolation | High | Adapt | Tier B - secondary study candidate |
| Approval workflows | Medium | Adopt | Tier B - secondary study candidate |
| Cost tracking | Medium | Adopt | Tier B - secondary study candidate |
| Goal hierarchy | Medium | Adapt | Tier B - secondary study candidate |
| Task status semantics | Medium | Adapt | Tier B - secondary study candidate |
| Issue monitors | Low | Defer | Tier C - deferred study topic |
| Silent active-run watchdog | Low | Defer | Tier C - deferred study topic |
| Sophisticated liveness recovery | Low | Defer | Tier C - deferred study topic |
| Multi-user board access | Low | Defer | Tier C - deferred study topic |
| Skills catalog and injection | Low | Defer | Tier C - deferred study topic |
| Plugin system | Low | Defer | Tier C - deferred study topic |
| Hierarchical org chart | - | Reject | - |
| Per-agent monthly budgets | - | Reject | - |
| Heartbeat-based autonomous execution | - | Reject | - |
| Rich issue model with 40+ fields | - | Reject | - |
| Multi-company isolation | - | Reject | - |

## Open Questions for PMO

1. Does this study-only candidate list align with CKOS's strategic positioning?
2. Should the Tier A study classification be expanded or contracted?
3. Should any deferred patterns be moved to a stronger study classification tier?
4. Should any rejected patterns be reconsidered?
5. What audit sequence would be required before any future Doc 27 checkout?
6. Which future executor, if any, may draft a Doc 27 candidate after explicit approval?

## CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: Codex — Paperclip Benchmarking
mode: study-only
files_created:
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/06_CKOS_ADOPTION_CANDIDATES_FOR_DOC27_STUDY.md
files_changed:
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/ck_memory.md (to be updated)
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/ck_tasks.md (to be updated)
files_not_touched:
  - docs 01-26
  - docs 27-34
  - 00_SYSTEM_GOVERNANCE/*
  - ARCHITECTURE_PATCH_REPORT.md
  - backend/UI/API/banco/migrations
  - JSONs n8n
  - agentes reais
  - automações runtime
validation:
  - Adoption candidates synthesized from notes 01-05
  - Prioritized by adoption priority (adopt, adapt, defer, reject)
  - Study-only evaluation notes provided for each candidate
  - Future Doc 27 candidate sequence created as a non-authoritative classification aid
  - Summary table created
  - Open questions for PMO identified
risks_remaining:
  - PMO audit of study-only candidate list pending
  - Doc 27 scope not yet finalized
  - Future canonical and implementation gates are not defined
next_step:
  - Update ck_memory.md to reflect completion of all study notes
  - Update ck_tasks.md to mark study notes as done
  - Request Claude audit of Study Layer 14
status: released_as_study_note_only
```
