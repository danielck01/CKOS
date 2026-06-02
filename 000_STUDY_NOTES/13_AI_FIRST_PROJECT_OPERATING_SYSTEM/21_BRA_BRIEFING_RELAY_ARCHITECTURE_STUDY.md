---
title: BRA Briefing Relay Architecture Study
file: 21_BRA_BRIEFING_RELAY_ARCHITECTURE_STUDY.md
layer: study
doc_type: study_note
phase: 000_STUDY_NOTES
category: ai_first_project_operating_system
status: draft
version: 0.1.0
created_at: 2026-05-31
updated_at: 2026-05-31
owner: pmo_ckos
responsible_agent: codex
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
  - metacognik
source_type: user_request
source_path: Codex session - codex_bra_protocol_study_patch
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: high
intelligence_level: high
project: ckos
purpose: Study BRA as a non-canonical protocol for indirect communication between parallel CKOS sessions.
inputs:
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
  - 000_ROADMAPS/ck_agent_handoffs.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_agent_handoffs.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/20_PROMPT_PACK_FOR_MULTI_SESSION_CLAUDE_AUDITS_STUDY.md
outputs:
  - BRA purpose
  - BRA packet candidate
  - cross-session relay rules
  - anti-chaos rules
  - future Doc 27 candidates
framework:
  - session -> packet -> handoff -> lock -> work -> release -> memory -> next session
edge_cases:
  - session treats chat as canonical memory
  - two agents write the same file
  - read-only audit becomes patch session
  - BRA packet grants authority by accident
  - Doc 27 is opened before gate
related_notes:
  - 07_PARALLEL_EXECUTION_AND_CHECKOUT_LOCK_STUDY.md
  - 13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md
  - 14_ACCEPTANCE_CRITERIA_FOR_DOC27.md
  - 15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md
  - 20_PROMPT_PACK_FOR_MULTI_SESSION_CLAUDE_AUDITS_STUDY.md
tags:
  - ckos
  - study
  - bra
  - briefing_relay
  - multi_session
  - handoff
  - checkout_lock
  - doc27_candidate
---

# BRA Briefing Relay Architecture Study

## Non-Authority Boundary

This file is study-only. It does not create Doc 27, does not alter canonical docs, does not update `ARCHITECTURE_PATCH_REPORT.md`, and does not authorize backend, UI, API, database, migrations, n8n JSONs, runtime agents or real automations.

BRA in this note is a proposed operating protocol for cross-session communication. It is not a database schema, not an API contract, not a runtime queue, not an agent implementation and not a permission grant.

No field described here is a database schema field. No language in this study authorizes runtime automation, agent-to-agent automation, backend work, UI work, API work, migrations, n8n JSONs or canonical document edits.

Identifier and Doc 11 warning: `approval_id`, `task_id`, `work_order_id`, `lock_id` and `release_id`, if referenced by a BRA Packet, Work Order, lock or release example in this study layer, are study placeholders or registry references only. They do not create canonical Doc 11 tables, fields, migrations, policies or API contracts without a future approved Doc 11 patch.

## 1. Proposito Do BRA

BRA means Briefing Relay Architecture.

Its purpose is to let CKOS sessions communicate indirectly, safely and auditably while multiple agents or tools work in parallel. BRA does this through structured packets that summarize context, scope, outputs, risks, blockers, open questions and recommended next action.

BRA is the relay layer between:

- one session finishing work;
- another session needing context;
- PMO needing traceability;
- Founder needing decisions without reading every chat;
- auditors needing evidence without trusting loose memory.

Core thesis:

```txt
Chat is conversation.
Session is a bounded work run.
BRA Packet is the transferable operational briefing between sessions.
Release is the proof of what actually happened.
Memory is the governed record after release.
```

## 2. Por Que BRA Existe

The Founder operates CKOS through simultaneous sessions in Claude, Codex, Antigravity, Windsurf/Trae and ChatGPT PMO. This creates leverage, but also risk:

- duplicate work;
- conflicting summaries;
- two sessions editing the same file;
- audit sessions becoming patch sessions;
- patch sessions assuming approval from chat context;
- study material being treated as canonical;
- lost decisions after long context windows;
- parallel outputs that cannot be reconciled.

BRA exists to turn session-to-session communication into a structured relay instead of a memory game.

Without BRA:

- a Claude audit may produce findings that Codex cannot safely patch;
- a Codex mapper may prepare context that Claude cannot trust;
- an Antigravity study may imply design execution before gate;
- ChatGPT PMO may coordinate five sessions without a shared release language.

With BRA:

- every session states what it read;
- every output declares what it changed and did not change;
- open questions are explicit;
- blockers are not hidden;
- ROI impact is carried forward;
- Founder decisions are isolated from agent inference.

## 3. Diferenca Entre Chat, Sessao, Agente, Executor, Auditor E Founder

| Term | BRA definition | Authority boundary |
|---|---|---|
| `chat` | The conversation surface where prompts, answers and clarifications happen. | Chat alone is not memory, approval or release. |
| `session` | A bounded work run with mode, scope, intelligence level, expected output and release. | Session may act only inside its declared lock and mode. |
| `agent` | A role or tool identity such as Codex, Claude, Antigravity, ChatGPT PMO or specialist. | Agent identity does not grant permission. |
| `executor` | The session role that creates or changes approved files inside lock. | Executor cannot be final auditor of its own output. |
| `auditor` | The session role that reviews output, scope, risks, evidence and non-authority boundaries. | Auditor should remain read-only unless a patch scope is separately approved. |
| `Founder` | Final strategic approver for exceptions, gates, batch size, scope changes and high-impact decisions. | Founder decision must be captured as explicit decision, not inferred from momentum. |

Short rule:

```txt
Chat can discuss.
Session can operate.
Agent can perform a role.
Executor can change locked files.
Auditor can validate.
Founder can decide.
BRA carries context between them.
```

## 4. Quando Uma Sessao Deve Falar Com Outra

A session should relay to another session when its output changes what the target session must know before acting.

Valid triggers:

- a read-only audit produced findings for a patcher;
- a mapper found source files that an auditor must review;
- a study session created candidates for later PMO synthesis;
- an executor completed a release and another session must fan-in results;
- a blocker requires a narrower or different session;
- a risk changes the allowed next action;
- a parallel session changes the scope, risk or blocker state of another active or planned session;
- a Founder decision is needed before the next session can proceed;
- multiple sessions need the same current state without sharing long chat history.

BRA relay is especially useful when:

- the target session has lower context;
- the target tool differs from the origin tool;
- the target mode differs, such as read-only audit to patch;
- the target action touches checkout lock, release, memory, ROI or Doc 27 readiness.

## 5. Quando Uma Sessao Deve Esperar

A session should wait when it cannot safely act without a dependency being completed or clarified.

Wait conditions:

- another active session holds write scope for the same file;
- required audit output has not been released;
- source files listed in the prompt were not read;
- expected target session is still producing findings;
- Founder decision is pending and affects scope, risk, cost or governance;
- a BRA Packet references outputs that do not exist yet;
- target file numbering or path conflicts with another planned output;
- memory or release state is inconsistent.

Waiting is not failure. In CKOS, waiting is a control state that prevents context collisions.

Minimum wait statement:

```txt
status: waiting
waiting_for: [session or release]
reason: [scope/risk/approval/dependency]
safe_action_now: read-only only | none | prepare questions
```

## 6. Quando Uma Sessao Deve Bloquear

A session must block when continuing would violate authority, scope, evidence or safety.

Block conditions:

- target action would create Doc 27 without explicit gate;
- target action would alter canonical docs outside an approved canonical patch;
- target action would edit `ARCHITECTURE_PATCH_REPORT.md` without scope;
- requested action would create backend, UI, API, database, migrations, n8n JSONs, runtime agents or automations;
- two sessions need write access to the same file;
- audit finds implementation drift;
- a packet claims approval but no Founder/PMO decision is cited;
- source evidence is missing for a high-risk claim;
- cost, risk or governance impact exceeds approved envelope;
- an executor is asked to self-approve final release.

BRA block statement:

```yaml
blocked_by:
  type: scope_violation | missing_approval | lock_conflict | evidence_gap | risk_escalation | dependency_gap
  detail:
  required_decision:
  safe_next_action:
```

## 7. Quando Uma Sessao Pode Trabalhar Em Paralelo

Parallel work is allowed when each session has distinct scope, distinct mode and distinct release.

Allowed parallel patterns:

- multiple read-only audits reading the same source files;
- one mapper preparing a context map while another read-only auditor reviews a different lane;
- one study note patch in a locked file while other sessions remain read-only;
- Antigravity design study reading context while Codex patches a different study note;
- ChatGPT PMO coordinating releases while execution sessions write non-overlapping files.

Parallel write is allowed only when:

- allowed files do not overlap;
- forbidden files are explicit;
- each session has a checkout lock or explicit Founder/PMO scoped permission;
- each session emits a release;
- fan-in audit is planned before treating the batch as complete.

Parallelism rule:

```txt
Read in parallel freely.
Write in parallel only with non-overlapping locks.
Decide after fan-in, not from the loudest session.
```

## 8. Estrutura Do BRA Packet

A BRA Packet is the minimum transferable context bundle between sessions.

It should be short enough to paste into another session, complete enough to prevent dangerous inference and structured enough for PMO audit.

Candidate shape:

```yaml
bra_id:
timestamp:
origin_session:
target_session:
scope:
mode:
checkout_lock_ref:
intelligence_level:
files_read:
files_created:
files_changed:
findings:
open_questions:
risks:
blocked_by:
handoff_request:
expiry:
recommended_next_action:
founder_decision_required:
roi_impact:
```

Optional fields for future study:

```yaml
related_work_order:
related_batch:
release_ref:
memory_update:
evidence_refs:
cost_estimate:
status:
```

BRA Packet should not carry full transcripts unless explicitly needed. It carries the usable operational state.

Required `bra_id` pattern:

```txt
BRA-{ORIGIN_AGENT}-{TARGET_AGENT}-{YYYYMMDD}-{SEQ}
```

`checkout_lock_ref` is mandatory in every packet and may contain only one of these value classes:

- active lock id;
- `pending_pmo_approval`;
- `not_required_read_only`.

`checkout_lock_ref` is a reference or status declaration only. It is not a checkout lock, does not create a checkout lock and does not grant write authority.

`expiry` is mandatory when `handoff_request` implies writing, a lock request or any later target action. For pure read-only informational relay with no requested target action, `expiry` may be `not_applicable`, but it should not be omitted when action timing could affect safety.

## 9. Campos Obrigatorios

| Field | Required meaning | Failure mode if missing |
|---|---|---|
| `bra_id` | Unique relay identifier using `BRA-{ORIGIN_AGENT}-{TARGET_AGENT}-{YYYYMMDD}-{SEQ}`. | Target cannot cite or reconcile packet. |
| `timestamp` | When the packet was emitted. | Target cannot judge freshness, sequencing or expiry. |
| `origin_session` | Session that produced the relay. | Provenance is lost. |
| `target_session` | Intended receiver or receiver class. | Packet becomes generic advice. |
| `scope` | Allowed and forbidden work boundary. | Target may overreach. |
| `mode` | read-only, patch study-only, audit, mapping, synthesis or other declared mode. | Target may edit when it should read. |
| `checkout_lock_ref` | Active lock id, `pending_pmo_approval` or `not_required_read_only`. | Target may confuse relay context with write authority. |
| `intelligence_level` | low, medium, high or highest with risk fit. | Risk/cost posture is unclear. |
| `files_read` | Context actually consumed. | Target trusts unsupported claims. |
| `files_created` | New files created by origin. | Fan-in cannot verify output. |
| `files_changed` | Existing files modified by origin. | Conflict detection fails. |
| `findings` | Material observations or results. | Packet carries no signal. |
| `open_questions` | Unresolved questions that affect action. | Target may invent answers. |
| `risks` | Current risks, including implementation/canon drift. | Target may proceed unsafely. |
| `blocked_by` | Concrete blockers, or `none`. | Waiting/blocking state is ambiguous. |
| `handoff_request` | What origin asks target to do. | Target may choose wrong next action. |
| `expiry` | Required when `handoff_request` implies writing, lock request or later target action; otherwise `not_applicable` may be used. | Stale packets may drive unsafe work. |
| `recommended_next_action` | Smallest safe next action. | PMO cannot sequence. |
| `founder_decision_required` | Decision needed from Founder, or `false`. | Approval may be inferred. |
| `roi_impact` | Operational value, risk reduction, context saved, adoption cost or decision unlocked. | Work may proceed without value hypothesis. |

Minimum packet rule:

```txt
If a field is unknown, write unknown.
If a field is not applicable, write not_applicable.
Do not omit required or conditionally required fields.
```

## 10. Exemplos De BRA Packet

### 10.1 Claude Auditor -> Codex Patcher

Use when Claude audited a document or study layer and Codex must apply a narrow patch.

```yaml
bra_id: BRA-CLAUDE-CODEX-20260531-001
timestamp: 2026-05-31T00:00:00-03:00
origin_session: claude_study_layer_13_audit_readonly
target_session: codex_study_layer_13_patch
scope:
  allowed:
    - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/[approved_output].md
  forbidden:
    - docs 01-26
    - docs 27-34
    - ARCHITECTURE_PATCH_REPORT.md
    - backend
    - UI
    - APIs
    - migrations
    - database
    - n8n JSONs
    - real agents
mode: patch study-only
checkout_lock_ref: pending_pmo_approval
intelligence_level: high
files_read:
  - Study Layer 13 notes 01-20
files_created: []
files_changed: []
findings:
  - Work Order and Batch concepts are coherent but need clearer relay protocol.
  - Doc 27 remains blocked until PMO gate.
open_questions:
  - Should BRA be canonicalized inside future Doc 27 or remain auxiliary PMO protocol?
risks:
  - Codex may over-patch beyond approved study file.
blocked_by: none
handoff_request: Create one study-only BRA note using audit findings.
expiry: 2026-06-01T00:00:00-03:00
recommended_next_action: Patch only approved study note and emit checkout release.
founder_decision_required: false
roi_impact: Reduces context handoff cost and lowers duplicate-work risk across sessions.
```

### 10.2 Codex Mapper -> Claude Auditor

Use when Codex maps files, sources or diffs and Claude must audit without editing.

```yaml
bra_id: BRA-CODEX-CLAUDE-20260531-001
timestamp: 2026-05-31T00:00:00-03:00
origin_session: codex_context_mapper_readonly
target_session: claude_doc27_gate_decision_readonly
scope:
  allowed:
    - read mapped source files
    - produce findings in chat
  forbidden:
    - create Doc 27
    - edit canonical docs
    - edit ARCHITECTURE_PATCH_REPORT.md
mode: read-only audit
checkout_lock_ref: not_required_read_only
intelligence_level: highest
files_read:
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/14_ACCEPTANCE_CRITERIA_FOR_DOC27.md
files_created: []
files_changed: []
findings:
  - Study Layer 13 has enough candidate material for scoping analysis.
  - Final Doc 27 gate still needs external audit verdict.
open_questions:
  - Is Doc 27 about task system, work order system or full project operating system?
risks:
  - Gate audit may be mistaken for permission to create Doc 27.
blocked_by:
  type: approval_gap
  detail: Founder/PMO/Metacognik gate not yet granted.
handoff_request: Audit readiness and return explicit OPEN/BLOCKED verdict.
expiry: 2026-06-01T00:00:00-03:00
recommended_next_action: Produce read-only gate memo with blockers.
founder_decision_required: true
roi_impact: Prevents premature canonical work and saves future rework.
```

### 10.3 Antigravity Study -> Claude Design Auditor

Use when Antigravity produced visual/product study material and Claude must audit design logic without allowing implementation.

```yaml
bra_id: BRA-ANTIGRAVITY-CLAUDE-20260531-001
timestamp: 2026-05-31T00:00:00-03:00
origin_session: antigravity_design_study
target_session: claude_design_audit_readonly
scope:
  allowed:
    - read design study notes
    - audit product/design assumptions
  forbidden:
    - frontend files
    - UI implementation
    - design system code
    - backend
    - API
    - database
    - migrations
mode: read-only design audit
checkout_lock_ref: not_required_read_only
intelligence_level: high
files_read:
  - design study sources supplied by Founder/PMO
files_created:
  - study-only design note, if origin was approved to patch
files_changed: []
findings:
  - Design direction needs audit against CKOS operational UI and approval gates.
open_questions:
  - Which design patterns improve Founder command flow without increasing cognitive load?
risks:
  - Visual study language may trigger premature UI build.
blocked_by:
  type: implementation_gate
  detail: No UI implementation gate approved.
handoff_request: Audit design study as evidence only.
expiry: 2026-06-01T00:00:00-03:00
recommended_next_action: Return design audit memo with patch candidates only.
founder_decision_required: false
roi_impact: Reduces visual drift and protects implementation budget.
```

### 10.4 ChatGPT PMO -> Todas As Sessoes

Use when PMO coordinates a multi-session batch.

```yaml
bra_id: BRA-PMO-ALLSESSIONS-20260531-001
timestamp: 2026-05-31T00:00:00-03:00
origin_session: chatgpt_pmo_coordination
target_session: all_active_sessions
scope:
  allowed:
    - each session follows its own prompt and lock
  forbidden:
    - cross-editing another session output
    - opening Doc 27 without gate
    - runtime or implementation work
mode: coordination relay
checkout_lock_ref: pending_pmo_approval
intelligence_level: high
files_read:
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
  - current releases supplied by sessions
files_created: []
files_changed: []
findings:
  - Sessions may run in parallel only with non-overlapping scopes.
  - Sessions 1-4 should be read-only by default.
  - Final synthesis should patch only one approved study file.
open_questions:
  - Which release should be treated as source of truth if audits conflict?
risks:
  - Contradictory audit findings may be merged without fan-in.
blocked_by: none
handoff_request: Each session must repeat allowed files, forbidden files and release format before acting.
expiry: 2026-06-01T00:00:00-03:00
recommended_next_action: Complete read-only audits, then run one synthesis session.
founder_decision_required: true
roi_impact: Preserves Founder attention and reduces coordination overhead across five sessions.
```

## 11. Regras De Anti-Caos

BRA anti-chaos rules:

- one packet per meaningful handoff;
- one file, one writer;
- one session, one declared mode;
- read-only means no edits;
- patch mode means patch only the approved file;
- no session inherits permission from another session;
- no target session may act on a BRA Packet write instruction without verifying `SESSION_REGISTRY.md` or explicit PMO/Founder approval;
- no target session acts on a packet that omits scope, mode or forbidden files;
- no broad packet should replace checkout lock;
- no packet should treat `checkout_lock_ref` as a lock grant;
- no packet should claim Founder approval without a concrete decision reference;
- no release should omit files not touched;
- no memory update should convert unverified study into canonical truth;
- no parallel fan-out should be closed without fan-in audit;
- no Doc 27 action should start from BRA alone.

Priority stack for conflict:

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

## 12. Relacao Com Checkout Lock E Release

BRA does not replace checkout lock or release.

Plain boundary:

```txt
A BRA Packet is not a checkout lock.
checkout_lock_ref points to lock state or approval state only.
Write authority still comes from SESSION_REGISTRY, active checkout lock, or explicit PMO/Founder approval.
```

BRA sits between them:

```txt
origin session release
  -> BRA Packet
  -> target session lock
  -> target session work
  -> target session release
```

Checkout lock answers:

- who can write;
- what can be written;
- what is forbidden;
- what output is expected;
- what release is required.

BRA Packet answers:

- why the next session matters;
- what context must travel;
- what findings must not be lost;
- what questions remain open;
- what risk or ROI changed;
- what target action is recommended.

Release answers:

- what actually happened;
- what was created;
- what changed;
- what was not touched;
- what validation was done;
- what risks remain;
- what next action is safe.

Rule:

```txt
BRA can request a lock.
BRA cannot grant a lock.
BRA can cite a release.
BRA cannot replace a release.
```

### 12.1 BRA Packet Vs Work Order context_pack

BRA Packet and Work Order `context_pack` are related but not interchangeable.

| Item | Purpose | Boundary |
|---|---|---|
| BRA Packet | Relay context between sessions. | Carries what another session must know before acting; it is not a lock, approval or execution state. |
| Work Order `context_pack` | Governed execution state inside one Work Order. | Carries the task state, constraints, evidence and execution context inside that governed Work Order; it is not cross-session relay. |

Rule:

```txt
BRA relays between sessions.
Work Order context_pack governs execution state.
BRA does not replace checkout lock, approval or Work Order context_pack.
Work Order context_pack does not replace BRA between sessions.
```

## 13. Relacao Com Memory Updates

BRA is transient relay memory. It should not automatically become long memory.

Suggested memory routing:

| BRA content | Memory destination |
|---|---|
| Active blockers, running target, current lock | Short/session memory. |
| Open questions, pending PMO decision, unresolved conflict | Medium/project memory. |
| Accepted release summary after audit | Long/governed memory. |
| Reusable packet template | Study note or future protocol candidate. |
| Unverified finding | Audit output only until reviewed. |
| Rejected or superseded packet | Archive/reference, not strong memory. |

Memory update rule:

```txt
Packet first.
Release second.
Memory third.
Canonical only after separate gate.
```

Minimum BRA-to-memory entry, when needed:

```txt
[date] [session] recorded BRA packet [bra_id] as study-only relay for [target_session]; no canonical or implementation authority granted.
```

## 14. Relacao Com ROI

BRA should reduce coordination cost and increase decision quality.

ROI dimensions:

| Dimension | BRA impact |
|---|---|
| Context saved | Target sessions receive the smallest usable context instead of full transcripts. |
| Rework reduced | Scope, blockers and risks travel with findings. |
| Founder attention protected | Only decisions with real consequence reach Founder. |
| Audit quality improved | Files read, files changed and assumptions are explicit. |
| Parallel speed increased | Sessions can work concurrently without shared confusion. |
| Risk reduced | Forbidden files and blocked conditions are visible before action. |
| Learning improved | Releases and packet patterns become auditable memory candidates. |
| Adoption cost | Time and attention required to create, validate and consume the packet. |

BRA should not exist as bureaucracy. A packet is justified when it unlocks one of these:

- safer patching;
- clearer audit;
- lower context cost;
- fewer duplicate sessions;
- better Founder decision;
- stronger fan-in release.

Adoption cost metric:

```txt
BRA is ROI-positive only when expected coordination savings, risk reduction or decision quality exceed the cost of creating and validating the packet.
```

## 15. Relacao Com Doc 27 Futuro

BRA is a strong candidate for future Doc 27 only if Doc 27 becomes a Work Order, task orchestration or project operating architecture document.

Possible Doc 27 placement:

- section on session relay protocol;
- section on Work Order handoff;
- section on batch fan-out/fan-in;
- section on release and memory handoff;
- appendix with required packet fields;
- anti-chaos rules for parallel agents.

Open question for Doc 27:

- Where does BRA relay end and Work Order `context_pack` begin, especially when a handoff becomes an executable governed task?

Doc 27 blockers:

- BRA must not become a runtime queue before data/runtime gates;
- BRA must not imply new tables, services, events or APIs;
- BRA must not authorize agents to communicate directly as runtime actors;
- BRA must remain subordinate to checkout lock, release, PMO audit and Founder approval;
- canonical language must be audited against Docs 10, 11, 12, 13, 21 and 26 if promoted.

Doc 27 rule:

```txt
This study may inform Doc 27 scope.
It does not open Doc 27.
It does not decide Doc 27 title.
It does not create Doc 27 authority.
```

## 16. Anti-Patterns

- Using a raw chat summary as if it were a BRA Packet.
- Omitting forbidden files because the target session "already knows".
- Sending a packet without `mode`.
- Treating a BRA Packet as approval to edit files.
- Acting on a BRA Packet without validating lock state in `SESSION_REGISTRY.md`.
- Treating read-only audit findings as patch instructions without PMO scope.
- Hiding blockers under generic "risks".
- Writing "Founder approved" without concrete decision text.
- Merging conflicting packets without fan-in audit.
- Updating long memory from unverified packet claims.
- Letting Antigravity study language trigger UI implementation.
- Opening Doc 27 because packets are coherent.
- Creating a backend queue, event bus, API or database table from BRA terminology.
- Having an executor write the packet, patch the file and final-audit itself.
- Creating multiple packets for tiny updates that do not affect risk, ROI, scope or next action.
- Making BRA so heavy that agents stop using it.

## 17. Acceptance Criteria

This note is acceptable only if:

- it exists only in `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/`;
- it remains study-only and non-canonical;
- it does not create Doc 27;
- it does not alter docs 01-26;
- it does not alter docs 27-34;
- it does not update `ARCHITECTURE_PATCH_REPORT.md`;
- it does not create backend, UI, API, database, migrations, n8n JSONs, runtime agents or automations;
- it does not present any BRA Packet field as a database schema field;
- it does not authorize runtime automation;
- it defines why BRA exists;
- it distinguishes chat, session, agent, executor, auditor and Founder;
- it states when sessions should speak, wait, block and work in parallel;
- it defines a BRA Packet with all required fields;
- it requires `timestamp`, `checkout_lock_ref` and conditionally required `expiry`;
- it states the required `bra_id` pattern;
- it states that BRA Packet is not a checkout lock;
- it distinguishes BRA Packet from Work Order `context_pack`;
- it includes the mandatory trigger when a parallel session changes another session's scope, risk or blocker state;
- it includes examples for Claude -> Codex, Codex -> Claude, Antigravity -> Claude and ChatGPT PMO -> all sessions;
- it explains anti-chaos rules, checkout lock/release relation, memory updates, ROI and future Doc 27 relation;
- it requires future integration with `MULTI_SESSION_EXECUTION_POLICY.md` and `SESSION_REGISTRY.md` before any canonical promotion;
- it includes anti-patterns;
- it closes with CHECKOUT RELEASE.

## 18. Candidatos Para Canonizacao Futura

Candidate sections for future canonical or auxiliary promotion, subject to separate audit and approval:

| Candidate | Why it matters | Suggested posture |
|---|---|---|
| BRA Packet required fields | Gives every session a shared handoff grammar. | Strong Doc 27 candidate if Doc 27 covers orchestration. |
| Session relay lifecycle | Connects release, packet, target lock and next release. | Strong candidate. |
| Anti-chaos rules | Prevents duplicate work, authority drift and lock conflict. | Strong candidate. |
| Founder decision flag | Separates agent recommendation from human decision. | Strong candidate. |
| ROI impact field | Keeps handoffs tied to value, not chatter. | Strong candidate. |
| Adoption cost metric | Prevents BRA from becoming heavier than the coordination problem it solves. | Strong candidate. |
| checkout_lock_ref field | Forces packets to declare lock status without granting authority. | Strong candidate, subject to SESSION_REGISTRY integration. |
| Block/wait/parallel rules | Gives sessions explicit stop conditions. | Strong candidate. |
| BRA-to-memory routing | Prevents packet claims from becoming false long memory. | Candidate requiring memory architecture audit. |
| Fan-in reconciliation | Allows five-session work without merging contradictions blindly. | Strong candidate. |

Deferred candidates:

| Candidate | Reason to defer |
|---|---|
| BRA database schema | Requires Doc 11 and implementation gate. |
| BRA event model | Requires runtime/event architecture approval. |
| BRA UI widget | Requires future Product/UI approval. |
| BRA automation runner | Requires backend/runtime/security approval. |
| Direct agent-to-agent messaging | Requires agent/runtime governance and safety model. |

## CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: codex_1_bra_study_patch_p1_p4_l1_l6
mode: patch study-only
allowed_scope:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/21_BRA_BRIEFING_RELAY_ARCHITECTURE_STUDY.md
files_created: []
files_changed:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/21_BRA_BRIEFING_RELAY_ARCHITECTURE_STUDY.md
files_not_touched:
  - Doc 27
  - docs 01-26
  - docs 27-34
  - 00_SYSTEM_GOVERNANCE/
  - ARCHITECTURE_PATCH_REPORT.md
  - SESSION_REGISTRY.md
  - auxiliary maps
  - QA_DOCUMENTATION_CHECKLIST.md
  - 000_ROADMAPS/
  - 000_UPLOADS/
  - 000_UPGRADE/
  - backend
  - UI
  - APIs
  - migrations
  - database
  - n8n JSONs
  - real agents
  - runtime automations
validation:
  - patched only the requested study-only BRA note
  - added timestamp as required BRA Packet field
  - added checkout_lock_ref as mandatory field with active lock id, pending_pmo_approval or not_required_read_only values
  - moved expiry out of optional fields and made it mandatory when handoff_request implies writing, lock request or later target action
  - added anti-chaos rule requiring SESSION_REGISTRY or PMO/Founder approval before acting on BRA write instruction
  - clarified that BRA Packet is not checkout lock
  - distinguished BRA Packet from Work Order context_pack
  - added bra_id pattern, adoption cost ROI metric, parallel-session trigger, Doc 27 open question, future integration acceptance criteria and lock-validation anti-pattern
  - did not create Doc 27
  - did not modify canonical docs, governance files, architecture patch report, session registry, auxiliary maps or runtime assets
risks_remaining:
  - future sessions may treat BRA Packet as approval unless lock, registry and release rules remain explicit
  - BRA versus Work Order context_pack boundary still needs Doc 27 audit before canonical promotion
  - future Doc 27 scoping still needs PMO/Metacognik audit before canonization
next_step:
  - PMO/Metacognik audit this study note with the rest of Study Layer 13 before any Doc 27 checkout
status: released_as_study_note_only
```
