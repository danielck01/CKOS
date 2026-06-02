---
title: Paperclip Heartbeat Execution Study
file: 02_PAPERCLIP_HEARTBEAT_EXECUTION_STUDY.md
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
source_type: paperclip_benchmark_study
source_tool: codex
provenance_status: unverified
confidence: unverified
risk_level: high
purpose: Study Paperclip heartbeat, liveness and recovery semantics as non-authoritative future CKOS reference material.
---

# 02_PAPERCLIP_HEARTBEAT_EXECUTION_STUDY.md

**Study Layer**: 14_PAPERCLIP_AGENT_OPERATING_MODEL  
**Note**: 02  
**Status**: Study-only, non-canonical  
**Created**: 2026-06-01  
**Purpose**: Analyze Paperclip's heartbeat execution model, liveness recovery, and execution semantics

## Non-Authority Boundary

This file is study-only, draft and unverified. It is not canonical.

It does not authorize Doc 27. It does not create Doc 27. It does not authorize backend, UI, API, database, migrations, real agents, runtime automations, n8n JSONs, MCP servers, webhooks or production schemas.

It may coordinate future sessions as a non-canonical operating note. It may not override `SESSION_REGISTRY.md`, `MULTI_SESSION_EXECUTION_POLICY.md`, canonical docs, Founder approval or PMO/Metacognik audit.

## Overview

Paperclip's heartbeat execution model is the core of its agent orchestration system. Agents wake on a schedule, check work, and act. The system handles execution locks, budget checks, workspace resolution, secret injection, skill loading, and adapter invocation. It includes sophisticated recovery mechanisms for crashes, restarts, and silent runs.

## Core Execution Model

### Two-Layer Separation

Paperclip separates four concepts that are easy to blur together:

1. **Structure**: parent/sub-issue relationships (work breakdown, rollup context)
2. **Dependency**: blocker relationships (explicit waiting relationships)
3. **Ownership**: who is responsible for the issue now (assignee)
4. **Execution**: whether the control plane currently has a live path to move the issue forward

The system works best when these are kept separate.

### Single-Assignee Model

An issue has at most one assignee:
- `assigneeAgentId`: issue owned by an agent
- `assigneeUserId`: issue owned by a human board user
- Both cannot be set at the same time

This is a hard invariant. Paperclip is single-assignee by design.

### Status Semantics

Paperclip issue statuses imply different expectations about ownership and execution:

**backlog**
- Issue is not ready for active work
- No execution expectation
- No pickup expectation
- Safe resting state for future work

**todo**
- Issue is actionable but not actively claimed
- May be assigned or unassigned
- No checkout/execution lock required yet
- For agent-assigned work, Paperclip may need a wake path

**in_progress**
- Issue is actively owned work
- Requires an assignee
- For agent-owned issues: strict execution-backed state
- For user-owned issues: human ownership state, not backed by heartbeat execution

**blocked**
- Issue cannot proceed until something external changes
- Waiting on another issue, human decision, or external dependency
- Work that automatic recovery could not safely continue

**in_review**
- Execution work paused because next move belongs to reviewer or approver
- External review service can also be a valid review path

**done**
- Work is complete and terminal

**cancelled**
- Work will not continue and is terminal

## Checkout and Active Execution

Checkout is the bridge from issue ownership to active agent execution.

### Checkout vs Execution

- `checkoutRunId`: represents issue-ownership lock for the current agent run
- `executionRunId`: represents the currently active execution path for the issue

These are related but not identical:
- `checkoutRunId` answers who currently owns execution rights for the issue
- `executionRunId` answers which run is actually live right now

Paperclip clears stale execution locks and can adopt some stale checkout locks when the original run is gone.

### Atomic Execution

Task checkout and budget enforcement are atomic, so no double-work and no runaway spend.

## Agent-Owned vs User-Owned Execution

### Agent-Owned Issues

Agent-owned issues are part of the control plane's execution loop:
- Paperclip can wake the assignee
- Paperclip can track runs linked to the issue
- Paperclip can recover some lost execution state after crashes/restarts

### User-Owned Issues

User-owned issues are not executed by the heartbeat scheduler:
- Paperclip can track ownership and status
- Paperclip cannot rely on heartbeat/run semantics to keep them moving
- Stranded-work reconciliation does not apply to them

This is why `in_progress` can be strict for agents without forcing the same runtime rules onto human-held work.

## Parent/Sub-Issue vs Blockers

### Parent/Sub-Issue (`parentId`)

This is structural. Use it for:
- Work breakdown
- Rollup context
- Explaining why a child issue exists
- Waking the parent assignee when all direct children become terminal

Do not treat `parentId` as execution dependency by itself.

### Blockers (`blockedByIssueIds`)

This is dependency semantics. Use it for:
- "This issue cannot continue until that issue changes state"
- Explicit waiting relationships
- Automatic wakeups when all blockers resolve

Blocked issues should stay idle while blockers remain unresolved. Paperclip should not create a queued heartbeat run for that issue until the final blocker is done and the `issue_blockers_resolved` wake can start real work.

If a parent is truly waiting on a child, model that with blockers. Do not rely on the parent/child relationship alone.

## Accepted-Plan Decomposition

An accepted plan confirmation is permission to decompose one specific accepted plan revision into child issues.

### Exact-Once Fingerprint

The canonical decomposition fingerprint is:
- `(sourceIssueId, acceptedPlanRevisionId)`

Where:
- `sourceIssueId` is the issue whose `plan` document revision was accepted
- `acceptedPlanRevisionId` is the accepted `plan` document revision

This is the product contract because the accepted revision is the thing being authorized for decomposition. Re-accepting, re-waking, or re-reading the same accepted revision must not authorize a second child tree.

### Durable Claim and Durable Result

Before creating child issues, the first decomposition attempt must create or reuse a durable record for the fingerprint.

That durable record must be able to answer, without reconstructing the thread from comments or transcripts:
- Whether decomposition for the fingerprint is `in_flight` or `completed`
- Which run or owner currently holds the in-flight claim
- Which child issues, if any, have already been created under that fingerprint
- Which final child issue ids belong to the completed result

### Parent Live Path While Decomposition Is In Flight

While decomposition for an accepted fingerprint is incomplete, the source issue must expose an explicit live path for that same fingerprint:
- The active decomposition run
- A queued continuation wake for the same assignee
- A monitor or explicit recovery action tied to the same decomposition claim
- A blocked state that names the real blocker for finishing that claimed decomposition

### Concurrent and Repeat Attempts

Every later run that encounters the same accepted-plan fingerprint must consult the durable claim/result before creating children:
- If no claim exists, the run may atomically create the claim and become the decomposition owner
- If a claim exists and is `in_flight`, the later run must reuse that claim
- If a claim exists and is `completed`, the later run must reuse the recorded child result and must not create new sibling issues
- If the prior attempt ended after partial child creation, the retry must continue under the same fingerprint and preserve the already-created child ids

## Non-Terminal Issue Liveness Contract

For agent-owned, non-terminal issues, Paperclip should never leave work in a state where nobody is responsible for the next move and nothing will wake or surface it.

This is a visibility contract, not an auto-completion contract. If Paperclip cannot safely infer the next action, it should surface the ambiguity with a blocked state, a visible notice, or an explicit recovery action.

### Valid Action-Path Primitives

An issue is healthy when the product can answer "what moves this forward next?" without requiring a human to reconstruct intent from the whole thread. Valid action-path primitives:
- An active run linked to the issue
- A queued wake or continuation that can be delivered to the responsible agent
- A typed execution-policy participant (e.g., `executionState.currentParticipant`)
- A pending issue-thread interaction or linked approval waiting for a specific responder
- A one-shot issue monitor (`executionPolicy.monitor.nextCheckAt`) that will wake the assignee for a future check
- A human owner via `assigneeUserId`
- A first-class blocker chain whose unresolved leaf issues are themselves healthy
- An open explicit recovery action that names the owner and action needed to restore liveness

### Explicit Recovery Actions

An explicit recovery action is a typed liveness repair path for a source issue. A valid recovery action must name:
- The source issue and company
- The recovery kind and idempotency fingerprint
- The recovery owner, plus previous or return owner when ownership may temporarily shift
- The cause, bounded evidence, and next action
- The wake, monitor, timeout, retry, or escalation policy that will move the action forward
- The resolution outcome when closed (restored, delegated, false positive, blocked, escalated, or cancelled)

### Agent-Assigned Status States

**todo** (dispatch state)
- Healthy when: issue has a queued wake path, or intentionally resting after completed heartbeat, or surfaced as stranded through visible blocked/recovery path
- Stalled when: dispatch was interrupted, no wake remains queued, no recovery path opened

**backlog** (parked state)
- Valid when: creator is deliberately parking the work
- Must not wake the assignee just because it has an assignee
- Becomes liveness problem when: another issue is blocked on it and no explicit waiting path exists

**in_progress** (active-work state)
- Healthy when: active run exists, queued continuation exists, active one-shot monitor exists, or open explicit recovery action exists
- Stalled when: no active run, no queued continuation, no explicit recovery surface

**in_review** (review/approval state)
- Healthy when: typed execution-policy participant exists, pending interaction/approval exists, human owner exists, active monitor exists, active run exists, queued wake exists, or open explicit recovery action exists
- Stalled when: no typed participant, no pending interaction/approval, no user owner, no active monitor, no active run, no queued wake, and no explicit recovery action

### Issue Monitors

An issue monitor is a one-shot deferred action path for agent-owned issues in `in_progress` or `in_review`.

Use a monitor when the current assignee owns a future check against an async system or external service (e.g., Greptile review loops, GitHub checks, Vercel deployments).

Monitor policy lives under `executionPolicy.monitor`:
- `nextCheckAt`: when Paperclip should wake the assignee
- `notes`: non-secret instructions for what the assignee should check
- `serviceName`: optional non-secret external-service context
- `externalRef`: optional external-service reference input (secret-adjacent, redacted)
- `timeoutAt`, `maxAttempts`, and `recoveryPolicy`: optional recovery hints for bounded waits

Monitors are not recurring intervals. When a monitor fires, Paperclip clears the scheduled monitor and queues an `issue_monitor_due` wake for the assignee.

## Crash and Restart Recovery

Paperclip treats crash/restart recovery as a stranded-assigned-work problem, not just a stranded-run problem.

### Stranded Assigned `todo`

Example:
- Issue is assigned to an agent
- Status is `todo`
- The original wake/run died during or after dispatch
- After restart there is no queued wake and nothing picks the issue back up

Recovery rule:
- If the latest issue-linked run failed/timed out/cancelled and no live execution path remains, Paperclip queues one automatic assignment recovery wake
- If that recovery wake also finishes and the issue is still stranded, Paperclip moves the issue to `blocked` and opens or updates an explicit recovery action when a bounded owner/action is known

### Stranded Assigned `in_progress`

Example:
- Issue is assigned to an agent
- Status is `in_progress`
- The live run disappeared
- After restart there is no active run and no queued continuation

Recovery rule:
- Paperclip queues one automatic continuation wake
- If that continuation wake also finishes and the issue is still stranded, Paperclip moves the issue to `blocked` and opens or updates an explicit recovery action when a bounded owner/action is known

### Recovery Model-Profile Lane

Cheap model profiles are only for status-only operational recovery overhead. Paperclip may request `modelProfile: "cheap"` for bounded recovery-owner work that updates task liveness, clears bad status, records a disposition, or asks for human/manager intervention.

Automatic retries that can continue source work must use the original/normal model lane.

## Startup and Periodic Reconciliation

On startup and on the periodic recovery loop, Paperclip does five things in sequence:
1. Reap orphaned `running` runs
2. Resume persisted `queued` runs
3. Reconcile stranded assigned work
4. Scan silent active runs, revalidate their source issues, and either fold source-resolved watchdogs or create/update explicit watchdog recovery actions
5. Reconcile productivity reviews

## Silent Active-Run Watchdog

An active run can still be unhealthy even when its process is `running`. Paperclip treats prolonged output silence as a watchdog signal, not as proof that the run is failed.

The recovery service owns this contract:
- Classify active-run output silence as `ok`, `suspicious`, `critical`, `snoozed`, or `not_applicable`
- Collect bounded evidence from run logs, recent run events, child issues, and blockers
- Preserve redaction and truncation before evidence is written to issue descriptions
- Create at most one open watchdog recovery action per run
- Honor active snooze decisions before creating more review work

### Source-Aware Watchdog Folding

Active-run watchdog work is source-aware. Before the watchdog creates, refreshes, escalates, or blocks on reviewer work, it must re-read the linked source issue and decide whether the watchdog signal is still about productive source work or only about stale run/process bookkeeping.

Fold watchdog work when all of these are true:
- The run is linked to a source issue in the same company
- The source issue is terminal (`done` or `cancelled`)
- Durable source activity from the same run proves the source issue reached that terminal disposition after the stale-run or output-silence evidence point
- There is no independent evidence that the still-running or detached process is doing harmful work

## Auto-Recover vs Explicit Recovery vs Human Escalation

Paperclip uses three different recovery outcomes:

### Auto-Recover

Auto-recovery is allowed when ownership is clear and the control plane only lost execution continuity:
- Requeue one dispatch wake for an assigned `todo` issue whose latest run failed
- Requeue one continuation wake for an assigned `in_progress` issue whose live execution path disappeared
- Assign an orphan blocker back to its creator when that blocker is already preventing other work

Auto-recovery preserves the existing owner. It does not choose a replacement agent.

### Explicit Recovery Action

Paperclip opens an explicit recovery action when the system can identify a problem but cannot safely complete the work itself:
- Automatic stranded-work retry was already exhausted
- A dependency graph has an invalid/uninvokable owner, unassigned blocker, or invalid review participant
- An active run is silent past the watchdog threshold

### Human Escalation

Human escalation is required when the next safe action depends on board judgment, budget/approval policy, or information unavailable to the control plane:
- All candidate recovery owners are paused, terminated, pending approval, or budget-blocked
- The issue is human-owned rather than agent-owned
- The run is intentionally quiet but needs an operator decision before cancellation or continuation

## Comparison with CKOS Study Layer 13

### CKOS Concepts (Study Layer 13)
- Parallel execution and checkout locks
- Founder approval batch control
- Task AI-first system
- Briefing-to-tasks transformation

### Paperclip Model
- Single-assignee model with atomic checkout
- Sophisticated liveness recovery
- Watchdog for silent runs
- Explicit recovery actions
- Human escalation paths

### Key Differences

| Aspect | Paperclip | CKOS (Study Layer 13) |
|--------|-----------|----------------------|
| Assignee model | Single-assignee (agent OR user) | Not specified |
| Checkout | Atomic checkout with execution locks | Checkout locks mentioned |
| Liveness | Sophisticated recovery with watchdogs | Not specified |
| Recovery | Auto-recover, explicit recovery, human escalation | Not specified |
| Monitors | One-shot deferred actions for async checks | Not specified |

## Adoption Candidates for CKOS

### Strong Candidates

1. **Single-assignee model**: Prevents confusion and double-work
2. **Atomic checkout with execution locks**: Ensures no double-work
3. **Liveness contract**: Non-terminal issues must have a live path or explicit recovery
4. **Explicit recovery actions**: Typed liveness repair paths with clear ownership
5. **Separation of structure vs dependency**: Parent/sub-issue for structure, blockers for dependencies
6. **Crash and restart recovery**: Automatic recovery for stranded assigned work

### Moderate Candidates

1. **Issue monitors**: One-shot deferred actions for async checks
2. **Silent active-run watchdog**: Detects unhealthy but still-running processes
3. **Source-aware watchdog folding**: Avoids creating review work for already-terminal issues
4. **Auto-recover vs explicit recovery vs human escalation**: Three-tier recovery model

### Weak Candidates

1. **Accepted-plan decomposition**: CKOS may not need plan-based decomposition
2. **Recovery model-profile lane**: Cheap model profiles for status-only recovery may be over-engineering
3. **Startup and periodic reconciliation**: May be too complex for CKOS's initial scope

## Risks and Considerations

### Risks

1. **Complexity**: Paperclip's execution semantics are very sophisticated (542-line document)
2. **Over-engineering**: CKOS may not need all of Paperclip's recovery mechanisms
3. **Operational overhead**: Watchdog scans, periodic reconciliation, and recovery actions add complexity
4. **Debugging difficulty**: Sophisticated recovery mechanisms can be hard to debug

### Considerations

1. **CKOS scope**: Does CKOS need autonomous 24/7 execution or scheduled batch execution?
2. **Recovery needs**: Does CKOS need automatic recovery or can it rely on manual intervention?
3. **Liveness requirements**: Does CKOS need sophisticated liveness monitoring or can it use simpler heuristics?
4. **Async checks**: Does CKOS need issue monitors for async external services?

## Open Questions for PMO

1. Should CKOS adopt Paperclip's single-assignee model?
2. Should future CKOS canon evaluate atomic checkout with execution locks?
3. Should future CKOS canon evaluate sophisticated liveness recovery like Paperclip?
4. Should CKOS use issue monitors for async external checks?
5. Should future CKOS canon evaluate silent active-run watchdogs?
6. What is CKOS's target execution model: autonomous 24/7 or scheduled batch?

## CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: Codex — Paperclip Benchmarking
mode: study-only
files_created:
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/02_PAPERCLIP_HEARTBEAT_EXECUTION_STUDY.md
files_changed:
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/ck_memory.md (to be updated)
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
  - Paperclip execution semantics analyzed (542-line document)
  - Single-assignee model documented
  - Checkout and execution locks documented
  - Liveness recovery mechanisms documented
  - Watchdog and recovery actions documented
  - Comparison with CKOS Study Layer 13 completed
  - Adoption candidates identified
risks_remaining:
  - Paperclip execution semantics are very sophisticated
  - CKOS scope not yet defined (autonomous 24/7 vs scheduled batch)
  - Recovery needs not yet defined
next_step:
  - Create note 03: Paperclip Work Task and Ticket System Study
status: released_as_study_note_only
```
