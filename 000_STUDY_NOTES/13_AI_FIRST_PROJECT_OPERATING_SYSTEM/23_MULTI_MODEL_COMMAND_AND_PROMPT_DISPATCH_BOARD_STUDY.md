# 23_MULTI_MODEL_COMMAND_AND_PROMPT_DISPATCH_BOARD_STUDY.md

**Study Layer**: 13_AI_FIRST_PROJECT_OPERATING_SYSTEM  
**Note**: 23  
**Status**: Study-only, non-canonical  
**Classification**: AUXILIARY OPERATIONAL; not a direct Doc 27 candidate  
**Created**: 2026-06-01  
**Purpose**: Multi-model command and prompt dispatch board for coordinating Codex, Claude, Antigravity, Windsurf and ChatGPT PMO sessions

## Non-Authority Boundary

This file is study-only, draft and unverified. It is not canonical.

It does not authorize Doc 27. It does not create Doc 27. It does not authorize backend, UI, API, database, migrations, real agents, runtime automations, n8n JSONs, MCP servers, webhooks or production schemas.

It may coordinate future sessions as a non-canonical operating note. It may not override `SESSION_REGISTRY.md`, `MULTI_SESSION_EXECUTION_POLICY.md`, canonical docs, Founder approval or PMO/Metacognik audit.

This note may inform local Founder operation, prompt hygiene and session discipline. It must not be promoted directly into Doc 27 architecture. If any concept from this note is later reused, it must be reclassified through Claude/PMO fan-in and explicit Founder gate.

Identifier warning: `session_id`, `task_id`, `work_order_id`, `lock_id`, `release_id` and `approval_id` in templates are study placeholders or registry references only. They do not create Doc 11 tables, schemas, migrations, RLS rules or API contracts without a future approved Doc 11 patch.

## Overview

This note creates a dispatch board for coordinating multiple AI model sessions (Codex, Claude, Antigravity, Windsurf, ChatGPT PMO) operating on 2 machines simultaneously. The dispatch board provides role definitions, session start/finish protocols, BRA packet triggers, blocking rules, Founder approval gates, and minimum prompts for each session type.

This is a markdown-and-discipline convention only. It is not a real backend, queue, event bus, API or schema.

## 1. Role Map By Tool

| Tool | Role | Primary Function | Authority Boundary |
|------|------|------------------|-------------------|
| **Founder** | Strategic approver | Approves gates, exceptions, batch size, scope changes, high-impact decisions | Final authority; decisions must be explicit, not inferred |
| **ChatGPT PMO** | Coordination dispatcher | Coordinates sessions, synthesizes releases, frames Founder decisions, manages BRA packets | Decides sequencing and asks Founder for approval; does not silently open Doc 27 |
| **Codex 1** | Primary executor | Controlled documentary writing, study-only patches, auxiliary updates | Writes study/auxiliary material inside lock and emits checkout release |
| **Codex 2** | Secondary executor | Auxiliary patches, reconciliations, non-overlapping scoped work | Handles small reconciliations after PMO scope; must not touch Codex 1 files unless handed off |
| **Claude 1** | Architectural auditor | Audits Doc 26, ghost artifacts, dependency risks, canonical coherence | Read-only audit by default; produces findings, not patches unless separately scoped |
| **Claude 2** | Study auditor | Audits Study Layer 13, Work Orders, BRA, notes/RAG, Doc 27 readiness | Read-only audit by default; produces findings, not patches unless separately scoped |
| **Antigravity** | UI/UX study | Visual/product study without implementation | Design study only; no UI files, no frontend code, no implementation |
| **Windsurf** | Lightweight dispatcher | Local PMO of support, prompt generation, BRA packet management | Support role only; no canonical authority; generates prompts from vault context |

### Role Priority Stack

```txt
Founder explicit decision
  > approved canonical docs
  > active checkout lock
  > PMO/Metacognik risk decision
  > latest valid release
  > BRA Packet
  > chat memory
  > agent inference
```

## 2. How Each Session Should Start

### Universal Start Protocol

Every session must start with:

1. **Session Declaration**:
   - `session_id`: Unique identifier
   - `session_type`: One approved type from `MULTI_SESSION_EXECUTION_POLICY.md`
   - `agent`: Tool identity (Codex, Claude, Antigravity, Windsurf, PMO, Founder)
   - `scope`: Allowed and forbidden folders/files
   - `status`: `planned`, `active`, `blocked`, `released`, `cancelled` or `superseded`
   - `started_at`: Start date/time or date
   - `expected_outputs`: Authorized deliverables
   - `estimated_cost`: CKC/token/time/tool cost estimate or `low`, `medium`, `high`, `unknown`
   - `intelligence_level`: `low`, `medium`, `high` or `highest`

2. **Checkout Lock Verification**:
   - Verify lock in `SESSION_REGISTRY.md` or obtain explicit PMO/Founder scoped permission
   - Confirm allowed scope does not overlap with active locks
   - Confirm forbidden scope is explicit

3. **Mode Declaration**:
   - `read-only`: Produce findings only, no edits
   - `patch study-only`: Patch only explicitly allowed study files
   - `patch auxiliary`: Patch only auxiliary maps/memory
   - `canonical_patch`: Only after separate Founder/PMO/Metacognik approval

### Tool-Specific Start Protocols

#### Founder
- Start with explicit decision request
- Declare decision scope (gate, exception, batch size, scope change)
- Declare required evidence before decision
- Declare decision expiry if applicable

#### ChatGPT PMO
- Start with coordination context from `SESSION_REGISTRY.md`
- Declare which sessions are being coordinated
- Declare BRA packet management role
- Declare Founder decision framing scope

#### Codex 1
- Start with checkout lock verification
- Declare allowed file scope (study-only or auxiliary)
- Declare forbidden scope (canonical, docs 27-34, implementation)
- Declare expected checkout release format

#### Codex 2
- Start with checkout lock verification
- Declare non-overlapping scope with Codex 1
- Declare auxiliary or reconciliation scope
- Declare expected checkout release format

#### Claude 1
- Start with read-only mode declaration
- Declare audit scope (Doc 26, ghost artifacts, dependencies)
- Declare forbidden scope (no edits, no Doc 27, no implementation)
- Declare expected audit output format

#### Claude 2
- Start with read-only mode declaration
- Declare audit scope (Study Layer 13, Work Orders, BRA, notes/RAG)
- Declare forbidden scope (no edits, no Doc 27, no implementation)
- Declare expected audit output format

#### Antigravity
- Start with design study mode declaration
- Declare Founder-approved gate reference
- Declare forbidden scope (no UI files, no frontend code, no implementation)
- Declare expected study output format

#### Windsurf
- Start with support role declaration
- Declare prompt generation scope (from vault context only)
- Declare forbidden scope (no canonical authority, no Doc 27)
- Declare expected prompt output format

## 3. How Each Session Should Finish

### Universal Finish Protocol

Every session must finish with:

1. **CHECKOUT RELEASE**:
   - `files_created`: List of new files
   - `files_changed`: List of modified files
   - `files_not_touched`: Explicit statement of what was NOT touched
   - `validation`: What was validated
   - `risks_remaining`: Residual risks
   - `next_step`: Smallest safe next action
   - `status`: `released`, `released_with_required_external_audit`, or `blocked`

2. **SESSÃO FINALIZADA**:
   - Explicit statement: "SESSÃO FINALIZADA"
   - This is NOT automatic from "done" in chat
   - Requires explicit CHECKOUT RELEASE

3. **Re-entry Prompt**:
   - Leave a prompt for re-entry if the session will be resumed
   - Include current state, blockers, and next action

### Tool-Specific Finish Protocols

#### Founder
- Finish with explicit decision text
- Include decision rationale
- Include decision scope (what is approved, what is blocked)
- Include decision expiry if applicable
- Include CHECKOUT RELEASE

#### ChatGPT PMO
- Finish with coordination summary
- Include BRA packets emitted
- Include Founder decision framing
- Include next session recommendations
- Include CHECKOUT RELEASE

#### Codex 1
- Finish with files created/changed/not touched
- Include validation that forbidden scope was respected
- Include CHECKOUT RELEASE
- Leave re-entry prompt if patch will continue

#### Codex 2
- Finish with files created/changed/not touched
- Include validation that scope did not overlap with Codex 1
- Include CHECKOUT RELEASE
- Leave re-entry prompt if reconciliation will continue

#### Claude 1
- Finish with audit findings
- Include blockers, patch candidates, open questions
- Include CHECKOUT RELEASE
- Leave re-entry prompt if audit will continue

#### Claude 2
- Finish with audit findings
- Include blockers, patch candidates, open questions
- Include CHECKOUT RELEASE
- Leave re-entry prompt if audit will continue

#### Antigravity
- Finish with design study outputs
- Include validation that no UI files were created
- Include CHECKOUT RELEASE
- Leave re-entry prompt if design study will continue

#### Windsurf
- Finish with prompts generated
- Include validation that prompts are from vault context only
- Include CHECKOUT RELEASE
- Leave re-entry prompt if prompt generation will continue

## 4. When To Emit BRA Packet

A session should emit a BRA Packet when its output changes what the target session must know before acting.

### Mandatory Triggers

- A read-only audit produced findings for a patcher
- A mapper found source files that an auditor must review
- A study session created candidates for later PMO synthesis
- An executor completed a release and another session must fan-in results
- A blocker requires a narrower or different session
- A risk changes the allowed next action
- A parallel session changes the scope, risk or blocker state of another active or planned session
- A Founder decision is needed before the next session can proceed
- Multiple sessions need the same current state without sharing long chat history

### BRA Packet Emission Protocol

1. **Create BRA Packet** with all required fields from note 21
2. **Include checkout_lock_ref** (active lock id, `pending_pmo_approval`, or `not_required_read_only`)
3. **Include expiry** when handoff_request implies writing, lock request or later target action
4. **Paste BRA Packet** into target session or save as markdown for handoff
5. **Register BRA Packet** in session release
6. **Do not treat BRA Packet as approval** - it is relay context only

### BRA Packet Examples

See note 21 for full examples:
- Claude Auditor → Codex Patcher
- Codex Mapper → Claude Auditor
- Antigravity Study → Claude Design Auditor
- ChatGPT PMO → All Sessions

## 5. When To Wait For Another Session

A session should wait when it cannot safely act without a dependency being completed or clarified.

### Wait Conditions

- Another active session holds write scope for the same file
- Required audit output has not been released
- Source files listed in the prompt were not read
- Expected target session is still producing findings
- Founder decision is pending and affects scope, risk, cost or governance
- A BRA Packet references outputs that do not exist yet
- Target file numbering or path conflicts with another planned output
- Memory or release state is inconsistent

### Minimum Wait Statement

```txt
status: waiting
waiting_for: [session or release]
reason: [scope/risk/approval/dependency]
safe_action_now: read-only only | none | prepare questions
```

### Wait Protocol

1. Declare wait status explicitly
2. Identify what session or release is being waited for
3. State the reason for waiting
4. State what safe action is possible now (if any)
5. Do not proceed with blocked action
6. Re-evaluate wait condition periodically

## 6. When To Block Advancement

A session must block when continuing would violate authority, scope, evidence or safety.

### Block Conditions

- Target action would create Doc 27 without explicit gate
- Target action would alter canonical docs outside an approved canonical patch
- Target action would edit `ARCHITECTURE_PATCH_REPORT.md` without scope
- Requested action would create backend, UI, API, database, migrations, n8n JSONs, runtime agents or automations
- Two sessions need write access to the same file
- Audit finds implementation drift
- A packet claims approval but no Founder/PMO decision is cited
- Source evidence is missing for a high-risk claim
- Cost, risk or governance impact exceeds approved envelope
- An executor is asked to self-approve final release

### Block Statement Format

```yaml
blocked_by:
  type: scope_violation | missing_approval | lock_conflict | evidence_gap | risk_escalation | dependency_gap
  detail:
  required_decision:
  safe_next_action:
```

### Block Protocol

1. Declare block status explicitly
2. Identify block type and detail
3. Identify required decision to unblock
4. State safe next action (if any)
5. Do not proceed with blocked action
6. Request Founder/PMO decision if required

## 7. When To Ask For Founder Approval

A session should ask for Founder approval when the action requires strategic decision, exception handling, or high-impact authorization.

### Approval Triggers

- Opening Doc 27 gate
- Approving next 5 or 10 tasks with Work Order boundaries
- Scope changes that affect risk ceiling or cost ceiling
- Exceptions to checkout lock or forbidden scope
- High-risk or high-value decisions
- Batch approval when risk or scope is unstable
- Canonical patch approval
- Implementation readiness approval
- Multi-user access approval
- Budget or policy changes

### Minimum Approval Request Format

```txt
Founder approval requested for [action].

Context:
- Current scope: [scope]
- Risk ceiling: [level]
- Cost ceiling: [limit]
- Evidence: [sources]

Decision needed:
- Approve or reject
- If approve, state allowed scope, forbidden scope, expiry
- If reject, state reason and alternative

ROI impact: [value_created, risk_reduced, context_saved, decision_unlocked]
```

### Approval Protocol

1. Frame decision clearly with context
2. State risk ceiling and cost ceiling
3. State required evidence
3. State ROI impact
4. Request explicit approve/reject decision
5. Do not infer approval from momentum
6. Record decision explicitly in release

## 8. How To Operate 2 Machines And Multiple Sessions

### Machine Assignment Strategy

**Machine 1 (Primary)**:
- Codex 1 (primary executor)
- Claude 1 (architectural auditor)
- ChatGPT PMO (coordination dispatcher)

**Machine 2 (Secondary)**:
- Codex 2 (secondary executor)
- Claude 2 (study auditor)
- Windsurf (lightweight dispatcher)
- Antigravity (UI/UX study, if activated)

### Parallel Execution Rules

**Allowed Parallel Patterns**:
- Multiple read-only audits reading the same source files
- One mapper preparing a context map while another read-only auditor reviews a different lane
- One study note patch in a locked file while other sessions remain read-only
- Antigravity design study reading context while Codex patches a different study note
- ChatGPT PMO coordinating releases while execution sessions write non-overlapping files

**Forbidden Parallel Patterns**:
- Two sessions writing to the same file
- Read-only audit becoming patch session without explicit scope change
- Session using stale chat memory as authority
- Trae or another reader being treated as approver
- Founder approval being inferred instead of recorded
- Patch being made before relevant audit finishes
- Fan-out completing but fan-in never happening

### Cross-Machine Coordination

1. **SESSION_REGISTRY.md** is shared truth across both machines
2. **BRA Packets** carry context between machines
3. **Checkout locks** prevent cross-machine write conflicts
4. **ChatGPT PMO** coordinates across both machines
5. **Windsurf** generates prompts locally from vault context on Machine 2
6. **Fan-in audit** happens before any decision

### Session Handoff Between Machines

1. Origin session emits CHECKOUT RELEASE on Machine 1
2. Origin session creates BRA Packet
3. BRA Packet is copied to Machine 2
4. Target session on Machine 2 reads BRA Packet
5. Target session verifies checkout lock in SESSION_REGISTRY.md
6. Target session starts work with declared scope
7. Target session emits CHECKOUT RELEASE on Machine 2
8. Target session may emit BRA Packet back to Machine 1

### Conflict Resolution

If two machines attempt to write to the same file:
1. First session to acquire checkout lock wins
2. Second session must wait or request narrower scope
3. PMO may pause one session if scope overlap is detected
4. Founder decides exceptions

## 9. Minimum Prompt For Each Session Type

### Codex Patch Study-Only

```txt
You are Codex acting as study-only patch executor for CKOS.

Mode discipline:
- PATCH STUDY-ONLY mode
- Do not edit canonical docs 01-26
- Do not create docs 27-34
- Do not edit ARCHITECTURE_PATCH_REPORT.md
- Do not edit 00_SYSTEM_GOVERNANCE/*
- Do not create backend, UI, API, database, migrations, n8n JSONs, runtime agents or real automations
- Patch only the explicitly allowed study file

Checkout lock:
- Verify lock in SESSION_REGISTRY.md
- Allowed scope: [allowed files/folders]
- Forbidden scope: [forbidden files/folders]

Expected outputs:
- [list of expected deliverables]

Intelligence level: [low/medium/high/highest]

Start with session declaration and checkout lock verification.
End with CHECKOUT RELEASE and SESSÃO FINALIZADA.
```

### Codex Read-Only Mapper

```txt
You are Codex acting as read-only mapper for CKOS.

Mode discipline:
- READ-ONLY mode
- Do not edit any files
- Do not create docs 27-34
- Do not edit ARCHITECTURE_PATCH_REPORT.md
- Do not edit 00_SYSTEM_GOVERNANCE/*
- Produce findings only

Files to read:
- [list of source files]

Expected outputs:
- [list of expected findings/maps]

Intelligence level: [low/medium/high/highest]

Start with session declaration and read-only mode.
End with CHECKOUT RELEASE and SESSÃO FINALIZADA.
```

### Claude Read-Only Audit

```txt
You are Claude acting as PMO_CKOS + Metacognik auditor for CKOS.

Mode discipline:
- READ-ONLY mode
- Do not edit canonical docs
- Do not create docs 27-34
- Do not update ARCHITECTURE_PATCH_REPORT.md
- Do not edit 00_SYSTEM_GOVERNANCE/*
- Do not create backend, UI, API, database, migrations, n8n JSONs, runtime agents or real automations
- Produce findings only

Authority discipline:
- Study material can recommend, never govern
- Roadmaps can sequence, never replace canonical specs
- Memory can preserve context, never authorize implementation
- canonical_candidate means candidate, not approval

Files to read:
- [list of source files]

Audit questions:
- [list of audit questions]

Expected outputs:
- [list of expected audit findings]

Intelligence level: [low/medium/high/highest]

Start with session declaration and read-only mode.
End with CHECKOUT RELEASE and SESSÃO FINALIZADA.
```

### Claude Synthesis Audit

```txt
You are Claude acting as PMO_CKOS + Metacognik synthesis auditor for CKOS.

Mode discipline:
- SYNTHESIS mode
- Synthesize audit findings from multiple sessions
- Do not create canonical docs
- Do not open Doc 27 without explicit gate
- Do not claim approval
- Do not hide uncertainty

Inputs:
- [list of audit outputs to synthesize]

Required report sections:
1. Executive verdict
2. What is safe now
3. What remains blocked
4. Doc 27 gate recommendation
5. Ghost artifact register summary
6. Candidate patch list
7. Prohibited automation list
8. Five-session operating plan for Founder
9. Open questions requiring Founder/PMO decision
10. CHECKOUT RELEASE

Rules:
- Do not create or edit canonical docs
- Do not open Doc 27
- Do not claim approval
- Do not hide uncertainty
- Every recommendation must be marked: study-only, patch_candidate, blocked or canonical_dependency

Intelligence level: highest

Start with session declaration and synthesis mode.
End with CHECKOUT RELEASE and SESSÃO FINALIZADA.
```

### Antigravity Study Mode

```txt
You are Antigravity acting as UI/UX study designer for CKOS.

Mode discipline:
- DESIGN STUDY mode
- Study visual/product direction without implementation
- Do not create UI files
- Do not create frontend code
- Do not create backend, API, database, migrations, n8n JSONs, runtime agents or real automations
- Produce design study notes, questions, risks, evidence maps only

Founder gate reference:
- [reference to approved gate in 12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md]

Allowed outputs:
- design study notes
- visual/product questions with ROI, risk, cost or governance impact
- evidence maps
- risk lists
- non-canonical recommendations

Forbidden outputs:
- UI implementation
- frontend files
- backend/API/database/migrations
- runtime agent creation
- JSONs n8n
- canonical docs
- docs 26-34

Intelligence level: [low/medium/high/highest]

Start with session declaration and design study mode.
End with CHECKOUT RELEASE and SESSÃO FINALIZADA.
```

### Windsurf Support Read-Only

```txt
You are Windsurf acting as local PMO of support for CKOS.

Mode discipline:
- SUPPORT READ-ONLY mode
- Generate prompts from vault context only
- Do not claim canonical authority
- Do not open Doc 27
- Do not edit canonical docs
- Do not edit ARCHITECTURE_PATCH_REPORT.md
- Do not edit 00_SYSTEM_GOVERNANCE/*
- Do not create backend, UI, API, database, migrations, n8n JSONs, runtime agents or real automations

Role:
- Local PMO of support
- Prompt generation from vault context
- BRA packet management
- Coordination surface only

Allowed outputs:
- Prompts for Codex and Claude Code
- BRA packets
- Coordination notes

Forbidden outputs:
- Canonical authority
- Doc 27
- Implementation work

Intelligence level: [low/medium/high/highest]

Start with session declaration and support role.
End with CHECKOUT RELEASE and SESSÃO FINALIZADA.
```

## 10. Intelligence Level Table

| Intelligence Level | Use When | Minimum Behavior | Typical Cost Posture | Examples |
|-------------------|----------|------------------|----------------------|----------|
| **low** | Small clerical update with no policy ambiguity | Follow exact scope, no broad reasoning | lowest | Typo in auxiliary task list after approval |
| **medium** | Routine auxiliary planning, memory or study work | Check local context, estimate risk/cost, avoid scope drift | controlled | Roadmap task update, folder README update |
| **medium-high** | Study layer creation, prompt pack generation, BRA protocol study | Read required context, reason through conflicts, document risks and release | justified by reduced rework | Study Layer 13/14 creation, prompt pack, BRA study |
| **high** | Cross-session, multi-agent, risk-bearing or governance-sensitive work | Read required context, reason through conflicts, document risks and release | justified by reduced rework | P1.7, routing, audit, Study Mode gates |
| **highest** | Canonical, high-risk, irreversible, legal/security/cost-heavy or architecture-defining work | Full gate discipline, explicit approvals, audit trail, rollback thinking | high; must be justified | Canonical patch, security policy, production implementation readiness |

### Intelligence Level Assignment by Session Type

| Session Type | Default Intelligence Level | When to Upgrade |
|--------------|---------------------------|-----------------|
| Codex patch study-only | medium-high | Upgrade to high if scope is material or governance-sensitive |
| Codex read-only mapper | medium | Upgrade to high if mapping affects canonical decisions |
| Claude read-only audit | high | Upgrade to highest if audit affects Doc 27 gate |
| Claude synthesis audit | highest | Always highest for synthesis |
| Antigravity study mode | high | Upgrade to highest if design affects implementation gate |
| Windsurf support read-only | medium | Upgrade to high if prompt generation affects strategic decisions |
| ChatGPT PMO coordination | high | Upgrade to highest if coordination affects Doc 27 gate |
| Founder decision | highest | Always highest for Founder decisions |

## 11. Session Validity System

### Long Session Termination

A long session must terminate with explicit "SESSÃO FINALIZADA" statement.

Rules:
- "done" in chat is NOT session termination
- "SESSÃO FINALIZADA" requires explicit CHECKOUT RELEASE
- Session is not valid until CHECKOUT RELEASE is emitted
- Re-entry prompt is required if session will be resumed

### Re-entry Prompt

Every session that may be resumed must leave a re-entry prompt:

```txt
RE-ENTRY PROMPT FOR [session_id]:

Current state:
- Last action: [description]
- Files created: [list]
- Files changed: [list]
- Current blockers: [list]
- Open questions: [list]

Next action:
- [smallest safe next action]

Context needed:
- [files to read]
- [decisions needed]

Continue from this state with same scope and mode.
```

### BRA Packet When Impacting Another Session

When a session's output impacts another session, it must emit a BRA Packet.

Rules:
- BRA Packet is mandatory for cross-session impact
- BRA Packet must include all required fields from note 21
- BRA Packet must include checkout_lock_ref
- BRA Packet must include expiry when handoff_request implies writing
- BRA Packet does not grant authority - it is relay context only

### Session Validity Checklist

A session is valid only when:
- [ ] Session declaration includes all required fields
- [ ] Checkout lock is verified or explicit PMO/Founder permission is cited
- [ ] Mode is declared (read-only, patch study-only, patch auxiliary, canonical_patch)
- [ ] Allowed scope is explicit
- [ ] Forbidden scope is explicit
- [ ] Intelligence level matches risk
- [ ] CHECKOUT RELEASE is emitted
- [ ] "SESSÃO FINALIZADA" is stated
- [ ] Re-entry prompt is left if session will be resumed
- [ ] BRA Packet is emitted if another session is impacted

## 12. Rules To Avoid Chaos

### No Agent Assumes Canonical Authority

- Study material can recommend, never govern
- Roadmaps can sequence, never replace canonical specs
- Memory can preserve context, never authorize implementation
- canonical_candidate means candidate, not approval
- No session may canonize study material without separate Founder/PMO/Metacognik gate

### No BRA Is Checkout Lock

- BRA Packet is not a checkout lock
- checkout_lock_ref points to lock state or approval state only
- Write authority still comes from SESSION_REGISTRY, active checkout lock, or explicit PMO/Founder approval
- No target session may act on a BRA Packet write instruction without verifying SESSION_REGISTRY.md or explicit PMO/Founder approval

### No Study Turns Into Implementation

- Study notes remain study-only until separate canonical approval
- No study schema becomes database schema without Doc 11 alignment
- No study protocol becomes runtime automation without implementation gate
- No study UI/UX becomes frontend code without Product/UI approval

### No Prompt Opens Doc 27 By Inference

- Doc 27 requires explicit Founder/PMO/Metacognik gate
- No prompt may infer Doc 27 approval from study momentum
- No prompt may create Doc 27 without explicit checkout lock
- Doc 27 gate decision must be explicit OPEN/BLOCKED with title, allowed sections, forbidden sections

### Additional Anti-Chaos Rules

- One file, one writer
- One session, one declared mode
- Read-only means no edits
- Patch mode means patch only the approved file
- No session inherits permission from another session
- No target session acts on a BRA Packet write instruction without verifying SESSION_REGISTRY.md or explicit PMO/Founder approval
- No target session acts on a packet that omits scope, mode or forbidden files
- No broad packet should replace checkout lock
- No packet should treat checkout_lock_ref as a lock grant
- No packet should claim Founder approval without a concrete decision reference
- No release should omit files not touched
- No memory update should convert unverified study into canonical truth
- No parallel fan-out should be closed without fan-in audit
- No Doc 27 action should start from BRA alone

## 13. Mini-Roadmap Operational Next 7 Steps

This mini-roadmap is an AUXILIARY OPERATIONAL sequencing aid only. It is not an implementation roadmap, not canonical architecture and not permission to open Doc 27.

### Step 1: Regularize Layer 14

**Session**: Codex 1  
**Mode**: Patch study-only  
**Scope**: `000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/ck_memory.md`, `ck_tasks.md`  
**Expected Output**: Update memory and tasks to reflect completion of all study notes  
**Dependencies**: None  
**Intelligence Level**: medium-high  
**BRA Packet**: Not required (no cross-session impact)

### Step 2: Reconcile Layer 13 + Layer 14

**Session**: Codex 1  
**Mode**: Patch study-only  
**Scope**: `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md`, `README.md`  
**Expected Output**: Update Study Layer 13 memory to reference Paperclip benchmarking findings  
**Dependencies**: Step 1 complete  
**Intelligence Level**: medium-high  
**BRA Packet**: Not required (no cross-session impact)

### Step 3: Audit Doc 26 v1.0.4

**Session**: Claude 1  
**Mode**: Read-only audit  
**Scope**: Doc 26 and related governance/runtime docs  
**Expected Output**: Audit findings, blockers, patch candidates  
**Dependencies**: None (can run in parallel with Step 1-2)  
**Intelligence Level**: high  
**BRA Packet**: Emit BRA Packet to Codex 1 if patch candidates are identified

### Step 4: Audit Study Layer 13 Notes 01-22

**Session**: Claude 2  
**Mode**: Read-only audit  
**Scope**: Study Layer 13 notes 01-22  
**Expected Output**: Audit findings, blockers, Doc 27 readiness assessment  
**Dependencies**: None (can run in parallel with Step 1-2)  
**Intelligence Level**: high  
**BRA Packet**: Emit BRA Packet to Codex 1 if patch candidates are identified

### Step 5: Audit Study Layer 14

**Session**: Claude 2  
**Mode**: Read-only audit  
**Scope**: Study Layer 14 notes 01-06  
**Expected Output**: Audit findings, adoption candidate validation  
**Dependencies**: Step 1 complete  
**Intelligence Level**: high  
**BRA Packet**: Emit BRA Packet to Codex 1 if adoption candidates need adjustment

### Step 6: Create Doc 27 Scope Proposal

**Session**: ChatGPT PMO  
**Mode**: Coordination synthesis  
**Scope**: Synthesize audit outputs from Steps 3-5  
**Expected Output**: Doc 27 scope proposal with title, allowed sections, forbidden sections, dependencies  
**Dependencies**: Steps 3-5 complete, fan-in audit complete  
**Intelligence Level**: highest  
**BRA Packet**: Emit BRA Packet to Founder with scope proposal

### Step 7: Founder Decides Doc 27 Gate

**Session**: Founder  
**Mode**: Decision  
**Scope**: Review Doc 27 scope proposal  
**Expected Output**: Explicit OPEN/BLOCKED decision with rationale  
**Dependencies**: Step 6 complete  
**Intelligence Level**: highest  
**BRA Packet**: Emit BRA Packet to all sessions with decision

## 14. Acceptance Criteria

This note is acceptable only if:

- It exists only in `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/`
- It remains study-only and non-canonical
- It does not create Doc 27
- It does not alter docs 01-26
- It does not alter docs 27-34
- It does not update `ARCHITECTURE_PATCH_REPORT.md`
- It does not create backend, UI, API, database, migrations, n8n JSONs, runtime agents or automations
- It defines role map by tool (Founder, ChatGPT PMO, Codex, Claude, Antigravity, Windsurf)
- It defines how each session should start
- It defines how each session should finish
- It defines when to emit BRA Packet
- It defines when to wait for another session
- It defines when to block advancement
- It defines when to ask for Founder approval
- It defines how to operate 2 machines and multiple sessions
- It provides minimum prompt for each session type
- It provides intelligence level table
- It provides session validity system
- It provides rules to avoid chaos
- It provides mini-roadmap of next 7 steps
- It closes with CHECKOUT RELEASE

## CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: windsurf_pmo_dispatcher_multi_model_command_prompt_dispatch_board
mode: patch study-only
allowed_scope:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/23_MULTI_MODEL_COMMAND_AND_PROMPT_DISPATCH_BOARD_STUDY.md
files_created:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/23_MULTI_MODEL_COMMAND_AND_PROMPT_DISPATCH_BOARD_STUDY.md
files_changed:
  - none
files_not_touched:
  - docs 01-26
  - docs 27-34
  - 00_SYSTEM_GOVERNANCE/*
  - ARCHITECTURE_PATCH_REPORT.md
  - auxiliary maps
  - backend
  - UI
  - API
  - database
  - migrations
  - n8n JSONs
  - real agents
  - runtime automations
validation:
  - created only the requested study-only dispatch board note
  - included role map by tool
  - included session start/finish protocols
  - included BRA packet triggers
  - included wait/block/approval rules
  - included 2-machine operation guidance
  - included minimum prompts for each session type
  - included intelligence level table
  - included session validity system
  - included anti-chaos rules
  - included mini-roadmap of next 7 steps
  - did not create Doc 27
  - did not modify canonical docs, governance files, architecture patch report, auxiliary maps or runtime assets
risks_remaining:
  - this note still requires PMO/Metacognik audit before strong operational use
  - 2-machine coordination requires disciplined BRA packet usage
  - Founder approval gates must remain explicit to prevent inference drift
next_step:
  - Update ck_memory.md to note creation of note 23
  - Update ck_tasks.md to mark note 23 as done
  - Update SESSION_REGISTRY.md to register this session
  - Request Claude audit of Study Layer 13 and 14 before Doc 27 scope proposal
status: released_as_study_note_only
```
