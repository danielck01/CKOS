---
title: Local PMO Multi-Model Control Room Study
file: 26_LOCAL_PMO_MULTI_MODEL_CONTROL_ROOM_STUDY.md
layer: study
doc_type: study_note
phase: 000_STUDY_NOTES
category: ai_first_project_operating_system
status: draft
version: 0.1.0
created_at: 2026-06-01
updated_at: 2026-06-01
owner: pmo_ckos
responsible_agent: windsurf
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
  - metacognik
source_type: user_request
source_path: Windsurf session - Local PMO Multi-Model Control Room
source_tool: windsurf
provenance_status: unverified
confidence: medium
risk_level: high
intelligence_level: high
project: ckos
purpose: Study a minimal, backend-free operational layer that lets Windsurf act as a local PMO of support to coordinate simultaneous Codex, Claude Code, Antigravity, Claude Design and Founder sessions using only markdown, SESSION_REGISTRY, BRA Packets, ck_tasks, ck_memory and roadmaps.
inputs:
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/README.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_tasks.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/20_PROMPT_PACK_FOR_MULTI_SESSION_CLAUDE_AUDITS_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/21_BRA_BRIEFING_RELAY_ARCHITECTURE_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/22_MULTI_SESSION_EXECUTION_ROADMAP_AND_SPRINT_BOARD_STUDY.md
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/README.md
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/ck_memory.md
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/06_CKOS_ADOPTION_CANDIDATES_FOR_DOC27_STUDY.md
outputs:
  - local PMO role definition for Windsurf
  - per-agent role map for parallel sessions
  - backend-free BRA coordination model
  - markdown pseudo-webhook convention
  - wait/parallel/approval rules
  - prompt-generation templates without ChatGPT dependency
  - minimal Founder kanban and sprint board
framework:
  - context read -> lock check -> BRA check -> dependency check -> prompt generation -> session run -> release -> registry update
edge_cases:
  - Windsurf treated as canonical authority instead of local PMO of support
  - markdown pseudo-webhook treated as a real runtime queue or event bus
  - Codex 1 and Codex 2 writing the same file
  - read-only Claude audit becoming a patch session
  - Claude Design or Antigravity language triggering UI implementation
  - long context window hiding stale decisions
  - Doc 27 opened from coordination momentum
related_docs:
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
related_notes:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/20_PROMPT_PACK_FOR_MULTI_SESSION_CLAUDE_AUDITS_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/21_BRA_BRIEFING_RELAY_ARCHITECTURE_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/22_MULTI_SESSION_EXECUTION_ROADMAP_AND_SPRINT_BOARD_STUDY.md
tags:
  - study
  - multi_session
  - local_pmo
  - windsurf
  - control_room
  - bra
  - auxiliary_operational
---

# 26_LOCAL_PMO_MULTI_MODEL_CONTROL_ROOM_STUDY.md

**Note**: 26  
**Classification**: AUXILIARY OPERATIONAL; not a direct Doc 27 candidate  
**Index reconciliation**: This file was previously named `23_LOCAL_PMO_MULTI_MODEL_CONTROL_ROOM_STUDY.md`. It was renamed to `26_LOCAL_PMO_MULTI_MODEL_CONTROL_ROOM_STUDY.md` on 2026-06-01 to resolve a duplicate `23_*` ordinal. This is index reconciliation only, not new conceptual material and not a Doc 27 action.

## 1. Non-Authority Boundary

This file is study-only, draft and unverified. It is not canonical.

It does not create Doc 27. It does not open Doc 27. It does not decide a Doc 27 title. It does not alter docs 01-26, does not alter docs 27-34, does not update `ARCHITECTURE_PATCH_REPORT.md`, does not edit `00_SYSTEM_GOVERNANCE/*`, and does not touch auxiliary maps.

It does not authorize backend, UI, API, database, migrations, real agents, runtime automations, n8n JSONs, MCP servers, webhooks or production schemas.

**Windsurf is a local PMO of support only. It is not canonical authority.** Windsurf may read context, check locks, verify BRA Packets, identify dependencies and generate ready-to-run prompts for each session. Windsurf may not approve canon, may not open Doc 27, may not override `SESSION_REGISTRY.md`, `MULTI_SESSION_EXECUTION_POLICY.md`, canonical docs, Founder approval or PMO/Metacognik audit.

Every coordination concept in this note (control room, pseudo-webhook, channel, queue) is a markdown-and-discipline convention only. It is not a database table, not an event bus, not a message broker, not an API contract and not a runtime service. No field or convention here grants write authority. Authority still comes from `SESSION_REGISTRY.md`, an active checkout lock, or explicit PMO/Founder approval, exactly as defined in `MULTI_SESSION_EXECUTION_POLICY.md` and note 21 (BRA).

Paperclip (Study Layer 14) is referenced only as an external benchmark. No Paperclip pattern is copied directly, adopted or implemented by this note.

This note may inform local Founder operation, prompt generation and session discipline. It must not be promoted directly into Doc 27 architecture. Any later canonical reuse requires Claude/PMO fan-in, explicit Founder gate and a separate canonical checkout.

Identifier warning: `task_id`, `work_order_id`, `approval_id`, `lock_id` and `release_id` in this note are study placeholders or registry references only. They do not create Doc 11 tables, fields, migrations, RLS rules, APIs or production schemas without a future approved Doc 11 patch.

## 2. Current Operational Problem

The Founder is operating multiple screens and models simultaneously: Codex sessions, Claude Code sessions, Antigravity, Claude Design and the Founder's own decisions. This creates leverage but the current flow is slow because manual ChatGPT relay became the human bottleneck.

Concrete symptoms today:

| Symptom | Effect |
|---|---|
| ChatGPT used as manual relay between every session | Founder time spent copy-pasting context instead of deciding. |
| Context rebuilt by hand for each new chat | High token cost, repeated explanations, drift between sessions. |
| No single place that shows who is writing what right now | Two sessions can touch the same file without seeing each other. |
| Decisions live inside long chat windows | Approvals are inferred from momentum, not recorded. |
| Audit findings handed off informally | Read-only audits get treated as patch instructions. |
| Sessions end late or never declare closure | Stale locks and unclear state accumulate. |

The goal of this note is to remove the manual ChatGPT relay from the critical path and let Windsurf, which already has local vault access, perform the mechanical PMO work: read context, check locks, verify BRA, find dependencies and emit prompts, while the Founder keeps decision authority and PMO_CKOS/Metacognik keep audit authority.

## 3. Windsurf As Local PMO

Windsurf acts as a **local PMO of support**: a coordination assistant that operates the markdown control surfaces of the vault. It is operational, not authoritative.

Windsurf MAY:

- read `SESSION_REGISTRY.md`, `MULTI_SESSION_EXECUTION_POLICY.md`, roadmaps, `ck_memory.md`, `ck_tasks.md` and study notes;
- check whether a file is already locked by an active session;
- verify that a BRA Packet has the required fields before a handoff;
- identify dependencies and ordering between planned sessions;
- generate ready-to-run prompts for Codex, Claude Code, Antigravity and Claude Design;
- draft BRA Packets, kanban updates and registry entries as proposals;
- flag conflicts, missing approvals, stale sessions and scope drift.

Windsurf MUST NOT:

- approve canonical work or declare canon;
- open or create Doc 27 (or docs 27-34);
- override the registry, the policy, Founder approval or PMO/Metacognik audit;
- treat its own coordination output as permission to write canonical or implementation surfaces;
- create backend, UI, API, database, migrations, agents, MCP servers, webhooks, n8n JSONs or runtime automations;
- self-approve a release it executed.

Windsurf authority posture:

```txt
Founder decides.
PMO_CKOS owns scope, locks and release requirements.
Metacognik audits risk and confidence.
Windsurf coordinates the markdown control surfaces and prepares prompts.
Windsurf recommends; it never governs.
```

## 4. Roles Of Each Agent

This note studies role responsibilities only. It does not create real agents.

| Agent | Role | Default mode | May write? | Authority boundary |
|---|---|---|---|---|
| Windsurf | Local PMO of support: context, locks, BRA, dependencies, prompt generation. | Coordination / patch study-only when explicitly scoped. | Only files explicitly scoped in a Founder/PMO-approved checkout (e.g. study notes, `ck_*`, registry). | Coordinates and recommends; never opens Doc 27; never canon; never implementation. |
| Codex 1 | Primary controlled documentary writer. | Patch study-only. | Yes, only in approved files inside its lock. | Writes study/auxiliary material inside lock; emits checkout release. |
| Codex 2 | Auxiliary patches and reconciliations. | Patch auxiliary or study-only. | Yes, only non-overlapping scoped files. | Must not touch Codex 1 files unless handed off via BRA + PMO scope. |
| Claude Code 1 | Architectural / canonical-readiness audit. | Read-only audit by default. | No, unless a later patch scope is explicit. | Audits architecture, ghosts, dependency risks; findings are not patch permission. |
| Claude Code 2 | Study Layer audit. | Read-only audit by default. | No, unless a later patch scope is explicit. | Audits Study Layer 13/14, Work Orders, BRA, notes/RAG, Doc 27 readiness. |
| Antigravity | Visual / product design study. | `design_study`, only after Founder-approved gate. | No (study notes only after gate). | Blocked until `12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md` is approved; no UI/frontend files ever from study. |
| Claude Design | Read-only design auditor for design study material. | Read-only design audit. | No, unless a later study-only patch scope is explicit. | Audits design assumptions; no UI implementation, no design-system code. |
| Founder | Final strategic approver. | Decision. | Authority source. | Approves exceptions, gates, batch size, scope, Doc 27; decision must be recorded, not inferred. |

Short rule:

```txt
Codex writes. Claude Code audits. Antigravity/Claude Design study and audit design.
Windsurf coordinates and prepares prompts. Founder decides.
No identity grants permission by itself; the lock and the Founder do.
```

## 5. Simultaneous Sessions Per Machine Model

The Founder runs several screens/models at once. This is the proposed per-machine session model, study-only:

```txt
Machine / screen
  -> one tool surface (Codex, Claude Code, Antigravity, Claude Design)
  -> one session_id
  -> one declared mode (read-only audit | patch study-only | design_study | coordination)
  -> one declared scope (allowed + forbidden files)
  -> one checkout lock (only if writing)
  -> one checkout release at the end
```

Proposed simultaneous layout (example, non-binding):

| Slot | Screen/tool | Session | Mode | Conflict boundary |
|---|---|---|---|---|
| 1 | Codex 1 | study-only patch of one approved note | write | only files in its lock |
| 2 | Codex 2 | auxiliary reconciliation | write | non-overlapping files only |
| 3 | Claude Code 1 | architecture/readiness audit | read-only | no edits |
| 4 | Claude Code 2 | Study Layer audit | read-only | no edits |
| 5 | Antigravity (if gated) / Claude Design | design study / design audit | design_study / read-only | study notes only, no UI files |
| — | Windsurf | local PMO coordination | coordination | reads all; writes only scoped control files |
| — | Founder | decisions | decision | authority source |

Per-machine rules:

- one tool surface holds one active session at a time for writing;
- a single machine may host one writer plus several read-only screens;
- every writer is visible in `SESSION_REGISTRY.md` with an active lock before writing;
- read-only sessions may run freely in parallel as long as they do not produce conflicting summaries that get merged without fan-in.

## 6. Using BRA Between Agents Without A Backend

BRA (note 21, Briefing Relay Architecture) is the existing study-only protocol for indirect, auditable session-to-session communication. It needs no backend: a BRA Packet is just structured markdown that the Founder (or Windsurf) pastes from one session into another.

Backend-free BRA flow:

```txt
origin session emits CHECKOUT RELEASE
  -> Windsurf (or Founder) extracts a BRA Packet (markdown)
  -> packet is stored as text (chat, note, or registry reference)
  -> target session reads the packet before acting
  -> target session verifies lock state in SESSION_REGISTRY
  -> target session works inside its own lock
  -> target session emits its own release
```

Rules carried over from note 21 (unchanged):

- a BRA Packet is **not** a checkout lock and does not grant write authority;
- `checkout_lock_ref` may only be an active lock id, `pending_pmo_approval`, or `not_required_read_only`;
- no target session acts on a write instruction without verifying `SESSION_REGISTRY.md` or explicit PMO/Founder approval;
- one packet per meaningful handoff; do not spam packets for trivial updates.

Windsurf's BRA role is mechanical: build the packet, check the required fields, and confirm the `checkout_lock_ref` is honest. Windsurf does not turn a packet into authority.

## 7. Simulating Webhooks With Markdown, BRA Packet And SESSION_REGISTRY

**This is a simulation by convention, not a real webhook, queue, event bus or backend.** No runtime service is created. The "pseudo-webhook" is a disciplined polling-and-relay pattern over markdown files.

The metaphor maps to existing markdown surfaces:

| Real webhook concept | Markdown convention (study-only) | Where it lives |
|---|---|---|
| Event emitted | A new `CHECKOUT RELEASE` block | session output + Checkout Release Log in `SESSION_REGISTRY.md` |
| Event payload | A BRA Packet | note 21 packet shape, pasted as text |
| Subscriber | A target session that reads the packet/release | the next chat/tool surface |
| Event log / queue | The Active Sessions + Checkout Release Log tables | `SESSION_REGISTRY.md` |
| Delivery | Founder or Windsurf pastes the packet into the target session | manual relay |
| Ack / consume | Target session cites the `bra_id` and emits its own release | target session output |

Pseudo-webhook loop (study-only):

```txt
1. Session A finishes and writes a release + a BRA Packet (the "event").
2. Windsurf appends the release to the registry log and validates the packet.
3. Windsurf identifies which session(s) should "subscribe" (depend on it).
4. Founder/Windsurf relays the packet to the target session.
5. Target session checks the registry lock state, then acts.
6. Target session emits its own release ("ack"), closing the loop.
```

Hard limits of the simulation:

- there is no automatic trigger; relay is manual and human-paced;
- there is no guaranteed delivery, retry or ordering beyond what the registry records;
- the registry is the only shared state; if it is not updated, the "event" did not happen;
- nothing here may be promoted into a real queue/event/API/table without a separate runtime/data gate (Docs 10/11) and Founder/PMO approval.

## 8. When A Session Must Wait

A session must wait when it cannot safely act without a dependency being completed or clarified (aligned with note 21 §5):

- another active session holds write scope for the same file;
- a required audit has not been released yet;
- source files listed in the prompt were not read;
- a BRA Packet references outputs that do not exist yet;
- target file numbering or path conflicts with another planned output;
- a Founder decision is pending and affects scope, risk, cost or governance;
- memory or release state is inconsistent.

Minimum wait statement:

```txt
status: waiting
waiting_for: [session_id or release_id]
reason: [scope | risk | approval | dependency | lock_conflict]
safe_action_now: read-only only | prepare questions | none
```

Waiting is a control state, not a failure.

## 9. When A Session May Advance In Parallel

Parallel work is allowed when each session has distinct scope, distinct mode and distinct release (aligned with note 21 §7 and note 22 §7):

- multiple read-only audits reading the same source files;
- one Codex patch in a locked file while other sessions stay read-only;
- Codex 2 patching an auxiliary file that does not overlap with Codex 1, after explicit PMO scope;
- Antigravity (if gated) or Claude Design reading/auditing design context while Codex patches a different study note;
- Windsurf coordinating while execution sessions write non-overlapping files.

Parallel write is allowed only when allowed files do not overlap, forbidden files are explicit, each writer has a lock, each session emits a release, and a fan-in audit is planned before the batch is treated as complete.

```txt
Read in parallel freely.
Write in parallel only with non-overlapping locks.
Decide after fan-in, not from the loudest session.
```

## 10. When The Founder Must Approve

Founder approval is required (decision must be recorded, never inferred) when:

- opening or creating Doc 27, or any canonical patch;
- activating Antigravity `design_study` (gate file approval);
- approving the next 5 or 10 tasks as a bounded batch (note 22 §12);
- expanding a lock scope mid-run;
- accepting a risk above the approved ceiling (security, legal, cost, canonical, implementation drift);
- promoting any study material toward canonical candidate;
- any action touching forbidden surfaces (docs 01-34, governance, backend, UI, API, runtime).

Minimum Founder decision template (from note 20):

```txt
Decision:
Approved next action:
Allowed output file:
Forbidden files:
Mode:
Required reviewers:
Reason:
Risks accepted:
Risks rejected:
Expiration:
```

Windsurf prepares the decision request; the Founder records the decision.

## 11. Generating Prompts For Codex And Claude Without ChatGPT

Windsurf generates prompts locally from vault context, removing the ChatGPT relay from the critical path. The pattern reuses the prompt-pack discipline from note 20.

Windsurf prompt-generation procedure:

```txt
1. Read SESSION_REGISTRY (locks + recent releases).
2. Read the relevant note(s), ck_memory and ck_tasks.
3. Identify the smallest safe next action and its dependencies.
4. Select mode (read-only audit | patch study-only | design study).
5. Fill the matching template (Sections 17-19) with allowed/forbidden scope.
6. Attach the global guardrail preface (note 20).
7. Output the prompt for the Founder to paste into the target tool.
```

Global guardrail preface (reused from note 20, applied to every generated prompt):

```txt
You are acting as a CKOS session under MULTI_SESSION_EXECUTION_POLICY.
- Do not edit canonical docs. Do not create docs 27-34.
- Do not update ARCHITECTURE_PATCH_REPORT.md or 00_SYSTEM_GOVERNANCE/*.
- Do not create backend, UI, API, database, migrations, n8n JSONs, runtime agents or automations.
- If mode is read-only, produce findings only.
- If mode is patch study-only, patch only the explicitly allowed file and emit CHECKOUT RELEASE.
- Study material can recommend, never govern. Roadmaps can sequence, never replace canon.
```

This keeps prompt generation fast and local while preserving every guardrail. ChatGPT may still be used by the Founder, but it is no longer a required relay.

## 12. Avoiding File Conflicts

- One file, one active writer (policy §11, note 15 §13-14).
- Every writer declares allowed and forbidden files and holds a lock in `SESSION_REGISTRY.md`.
- Codex 1 and Codex 2 must never share a target file unless a BRA handoff + PMO scope transfers it.
- A broader-scope session must not overwrite a narrower active lock.
- Windsurf checks the lock index before generating any write prompt and refuses to generate a prompt that overlaps an active lock.
- New files get a unique number/path checked against the folder before creation.
- Read-only sessions never write, even to "fix a small thing".

Conflict priority stack (from notes 15 and 21):

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

## 13. Avoiding Long Context And Late Session Closure

Long context windows hide stale decisions and inflate cost. Mitigations:

- prefer one BRA Packet (small, structured) over pasting full transcripts;
- keep each session scoped to one note or one audit lane;
- record decisions in the registry/memory, not only in chat;
- close a session as soon as its declared output exists and is released;
- when context grows, summarize into a BRA Packet and start a fresh session instead of stretching the old one;
- Windsurf flags any session that has produced its output but not emitted a release.

Trigger to start a fresh session instead of continuing:

```txt
If the next safe action needs less than 20% of what is in the current context,
emit a release + BRA Packet and open a new scoped session.
```

## 14. "SESSÃO FINALIZADA" Rule

A session is only finished when it emits an explicit closure. Saying "done" in chat is not closure.

**SESSÃO FINALIZADA** requires a `CHECKOUT RELEASE` containing: `files_created`, `files_changed`, `files_not_touched`, `validation`, `risks_remaining`, `next_step`, `status` (policy §8, Release Rule in `SESSION_REGISTRY.md`).

```txt
SESSÃO FINALIZADA =
  CHECKOUT RELEASE emitted
  + registry updated (or update proposed to Windsurf/PMO)
  + lock released
  + next_step stated
  + status set (released | released_with_required_external_audit | blocked | cancelled)
```

Until those exist, the session is still `active` and its lock still holds. Windsurf must not generate a dependent prompt until the upstream session is `SESSÃO FINALIZADA`.

## 15. Template - New Session Start

In this template, `task_id` means the existing `SESSION_REGISTRY.md` task identifier for a session. It is not a Work Order ID and does not create a Work Order schema.

```txt
SESSION START
session_id: S-P1-13-[AGENT]-[YYYYMMDD]-[SEQ]
task_id: [TASK_ID]
agent: [windsurf | codex_1 | codex_2 | claude_code_1 | claude_code_2 | antigravity | claude_design | founder]
session_type: [study | audit | execution | design_study | memory_refresh | planning]
mode: [read-only audit | patch study-only | design_study | coordination]
intelligence_level: [low | medium | high | highest] + reason
scope_allowed:
  - [files/folders]
scope_forbidden:
  - docs 01-26, docs 27-34, 00_SYSTEM_GOVERNANCE/*, ARCHITECTURE_PATCH_REPORT.md
  - backend, UI, API, database, migrations, n8n JSONs, MCP servers, real agents, runtime automations
checkout_lock: [lock_id | not_required_read_only | pending_pmo_approval]
expected_outputs:
  - [deliverables]
estimated_cost: [low | medium | high | unknown]
approval_basis: [Founder/PMO decision reference or none]
release_required: [true | false]
files_read_first:
  - [required context files]
```

## 16. Template - Operational BRA Packet

Reuses note 21 required fields. `bra_id` pattern: `BRA-{ORIGIN_AGENT}-{TARGET_AGENT}-{YYYYMMDD}-{SEQ}`.

```yaml
bra_id: BRA-[ORIGIN]-[TARGET]-[YYYYMMDD]-[SEQ]
timestamp: [ISO datetime]
origin_session: [session_id]
target_session: [session_id or class]
scope:
  allowed:
    - [files/folders]
  forbidden:
    - docs 01-26, docs 27-34, ARCHITECTURE_PATCH_REPORT.md, 00_SYSTEM_GOVERNANCE/*
    - backend, UI, API, database, migrations, n8n JSONs, real agents, runtime automations
mode: [read-only audit | patch study-only | design study | coordination]
checkout_lock_ref: [active lock id | pending_pmo_approval | not_required_read_only]
intelligence_level: [low | medium | high | highest]
files_read: [ ... ]
files_created: [ ... ]
files_changed: [ ... ]
findings: [ ... ]
open_questions: [ ... ]
risks: [ ... ]
blocked_by: [none | {type, detail, required_decision, safe_next_action}]
handoff_request: [what origin asks target to do]
expiry: [datetime | not_applicable]
recommended_next_action: [smallest safe next action]
founder_decision_required: [true | false]
roi_impact: [value / risk reduced / context saved / decision unlocked]
```

## 17. Template - Prompt For Codex Executor

```txt
[GLOBAL GUARDRAIL PREFACE from Section 11]

ROLE: Codex executor (patch study-only).
SESSION: S-P1-13-CODEX-[YYYYMMDD]-[SEQ]
MODE: patch study-only.
INTELLIGENCE LEVEL: high.

READ FIRST (do not write until read):
- [exact files]

ALLOWED TO WRITE (only these):
- [exact file path(s) inside lock]

FORBIDDEN:
- docs 01-26, docs 27-34, 00_SYSTEM_GOVERNANCE/*, ARCHITECTURE_PATCH_REPORT.md, auxiliary maps
- backend, UI, API, database, migrations, n8n JSONs, MCP servers, real agents, runtime automations
- any file held by another active lock

TASK:
- [single, scoped writing task]

CONSTRAINTS:
- Repeat allowed and forbidden files before writing.
- Do not open Doc 27. Do not canonize. Do not implement.
- If a needed file is outside the lock, STOP and report (do not expand scope).

CLOSE WITH:
- CHECKOUT RELEASE (files_created, files_changed, files_not_touched, validation,
  risks_remaining, next_step, status).
```

## 18. Template - Prompt For Claude Auditor

```txt
[GLOBAL GUARDRAIL PREFACE from Section 11]

ROLE: Claude Code auditor (read-only).
SESSION: S-P1-13-CLAUDE-[YYYYMMDD]-[SEQ]
MODE: read-only audit.
INTELLIGENCE LEVEL: high or highest.

READ:
- [exact files]

FORBIDDEN:
- editing any file (read-only).
- docs 27-34 creation, ARCHITECTURE_PATCH_REPORT.md edits, 00_SYSTEM_GOVERNANCE/* edits.
- implying backend/UI/API/runtime work as approved.

AUDIT GOAL:
- [coherence | non-authority | Doc 27 readiness | ghost artifacts | ROI | memory | smart questions | roles]

RETURN:
- verdict;
- findings ordered by severity (critical / high / medium / low);
- open questions;
- patch_candidates (labeled candidate, not applied);
- blocked items;
- recommended next PMO session.

CLOSE WITH:
- CHECKOUT RELEASE (files_created: none, files_changed: none, files_not_touched, validation,
  risks_remaining, next_step, status: released).
```

## 19. Template - Prompt For Antigravity / Claude Design

```txt
[GLOBAL GUARDRAIL PREFACE from Section 11]

ROLE: Antigravity design study (only if Founder gate approved) OR Claude Design read-only audit.
SESSION: S-P1-13-[ANTIGRAVITY|CLAUDEDESIGN]-[YYYYMMDD]-[SEQ]
MODE: design_study (gated) | read-only design audit.
INTELLIGENCE LEVEL: high.

GATE CHECK (Antigravity only):
- Confirm 12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md is Founder-approved.
- If not approved, STOP: Antigravity remains blocked.

READ:
- [design study sources supplied by Founder/PMO]

ALLOWED OUTPUT:
- design study notes / design audit memo (study-only).

FORBIDDEN (always):
- frontend files, UI implementation, design-system code.
- backend, API, database, migrations, n8n JSONs, runtime agents, automations.
- canonical docs, docs 27-34.

TASK:
- [study/audit visual-product direction; produce questions + patch candidates only]

CLOSE WITH:
- CHECKOUT RELEASE (study-only; no UI files; risks_remaining; next_step; status).
```

## 20. Minimal Operational Kanban For Founder

A backend-free kanban the Founder reads at a glance. It is a study mirror of `ck_tasks.md`, not a runtime board.

```txt
NOW (active, locked)        | who | lock_id | release expected
---------------------------------------------------------------
[ ]                          |     |         |

WAITING (blocked/depends)   | waiting_for | reason
---------------------------------------------------------------
[ ]                          |             |

READY (scoped, no lock yet) | mode | scope
---------------------------------------------------------------
[ ]                          |      |

FOUNDER DECISION             | decision needed | impact
---------------------------------------------------------------
[ ]                          |                 |

DONE (released)             | release_id | status
---------------------------------------------------------------
[ ]                          |            |
```

Rules: a card enters NOW only with a lock; it leaves NOW only with a release; nothing reaches DONE without `SESSÃO FINALIZADA`.

## 21. Sprint Board - Short, Medium, Long Term

Study-only sequencing, subordinate to note 22's roadmap phases and the Founder/PMO Doc 27 gate.

| Horizon | Focus | Allowed work | Exit condition |
|---|---|---|---|
| Short | Stand up the local PMO control surfaces. | This note + memory/tasks/registry updates; Windsurf coordination; read-only audits. | Registry shows current state; Windsurf can generate prompts and check locks. |
| Medium | Run parallel audits and fan-in. | Claude Code read-only audits of Doc 26 and Study Layer 13/14; one Codex synthesis after fan-in; design audit if gated. | Audit releases exist; conflicts classified; Doc 27 readiness estimated. |
| Long | Founder/PMO Doc 27 gate decision. | Read-only gate memo; Founder/PMO decision capture; only then a separate canonical checkout. | Explicit OPEN/BLOCKED Doc 27 decision with narrow scope; implementation still gated. |

The control room (this note) is a coordination surface for the short/medium horizon. It does not advance the long horizon by itself; only the Founder/PMO gate does.

## 22. Relation To Cognik, Metacognik, Skills, Transformers, Policies, Prompts And RAG

Study-only mapping. None of these become runtime here.

| Concept | Source (study/canonical) | Role in the control room | Boundary |
|---|---|---|---|
| Cognik | note 17 | Organizes context, briefing gaps, retrieval candidates for prompt generation. | Context organizer, not executor or approver. |
| Metacognik | note 17 | Audits risk, confidence, evidence, self-approval; can pause weak work. | Risk/confidence auditor, not implementer. |
| Skills | Doc 06 / `17_SKILLS_REGISTRY` | Reusable capability references a prompt may cite. | No runtime skill injection from this note. |
| Transformers | Doc 09 / `18_TRANSFORMERS` | Briefing -> tasks / packets transformation pattern Windsurf imitates by convention. | Conceptual; no pipeline implementation. |
| Policies | `MULTI_SESSION_EXECUTION_POLICY.md` | The governing rules every session and Windsurf obey. | Authoritative auxiliary governance; this note is subordinate. |
| Prompts | note 20 / `19_PROMPT_ENGINEERING` | The prompt-pack grammar Windsurf reuses to generate prompts. | Operational guidance; requires PMO scope before use. |
| RAG | note 18 / `14_RAG_VECTOR_SYSTEM` | Future retrieval of context/packets; routing by trust and lifespan. | No vector store, schema or ingestion created here. |

Windsurf orchestrates references to these concepts; it does not instantiate any of them as services.

## 23. How The System Evolves Without A Backend (For Now)

The control room runs entirely on markdown discipline plus human relay. Evolution path, all study-only:

```txt
Stage 0 (now): markdown surfaces + manual relay
  - SESSION_REGISTRY (state), BRA Packets (handoff), ck_tasks/ck_memory (memory),
    roadmaps (sequence), Windsurf (coordination), Founder (decision).

Stage 1: tighter conventions
  - stable bra_id sequence, standard release blocks, Windsurf lint of locks/packets.

Stage 2: candidate consolidation
  - audited Work Order / BRA / release patterns become Doc 27 candidates (only after gate).

Stage 3 (NOT now): runtime
  - only after Docs 10/11/12 gates: real queue/event/store, real agents, automations.
    Requires separate Founder/PMO/Metacognik + technical approval.
```

Each stage is gated. Nothing crosses into Stage 3 from this note. The benchmark insight from Paperclip (Study Layer 14) — that liveness, locks and single-assignee discipline matter — is noted as reference only; CKOS keeps on-demand, human-paced coordination until a real runtime is separately approved.

## 24. Limits - What Cannot Be Automated Yet

- No automatic event delivery, trigger, retry or ordering (no real webhooks/queues).
- No automatic write authority from any packet or coordination output.
- No automatic Doc 27 creation, canonization or scope decision.
- No automatic canonical patch, governance edit or patch-report update.
- No automatic agent-to-agent messaging as runtime actors.
- No automatic memory/RAG promotion of unverified study output.
- No automatic Antigravity activation (Founder gate required).
- No automatic implementation: backend, UI, API, database, migrations, n8n JSONs, MCP servers, real agents.
- No automatic release self-approval by the executor.

Everything above stays manual, human-paced and gated until separately approved.

## 25. Acceptance Criteria

This note is acceptable only if:

- it exists only in `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/`;
- it remains study-only, draft and unverified, with no canonical authority;
- it does not create Doc 27 and does not create docs 27-34;
- it does not alter docs 01-26, governance files, `ARCHITECTURE_PATCH_REPORT.md` or auxiliary maps;
- it does not create backend, UI, API, database, migrations, n8n JSONs, MCP servers, webhooks, real agents or runtime automations;
- it records explicitly that Windsurf is a local PMO of support, not canonical authority;
- it does not present any pseudo-webhook/markdown convention as a real backend, queue, event bus or schema;
- it uses Paperclip only as a benchmark and copies no Paperclip pattern directly;
- it covers all 25 required sections, including roles for Codex 1/2, Claude Code 1/2, Antigravity, Claude Design and Founder;
- it defines the simultaneous-sessions-per-machine model;
- it explains backend-free BRA usage and the markdown pseudo-webhook simulation with explicit limits;
- it states when sessions wait, advance in parallel, and when the Founder must approve;
- it explains local prompt generation without ChatGPT dependency;
- it includes file-conflict, long-context and "SESSÃO FINALIZADA" rules;
- it includes templates for session start, operational BRA Packet, Codex executor prompt, Claude auditor prompt and Antigravity/Claude Design prompt;
- it includes a minimal Founder kanban and a short/medium/long sprint board;
- it maps Cognik, Metacognik, Skills, Transformers, Policies, Prompts and RAG without instantiating them;
- it describes backend-free evolution and the limits of automation;
- it remains subordinate to `SESSION_REGISTRY.md`, `MULTI_SESSION_EXECUTION_POLICY.md`, Founder approval and PMO/Metacognik audit;
- it closes with CHECKOUT RELEASE.

## CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: S-P1-13-WINDSURF-20260601-005
task_id: STUDY13_LOCAL_PMO_MULTI_MODEL_CONTROL_ROOM_20260601
mode: patch study-only
intelligence_level: high
allowed_scope:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/26_LOCAL_PMO_MULTI_MODEL_CONTROL_ROOM_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_tasks.md
  - 000_ROADMAPS/SESSION_REGISTRY.md
files_created:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/26_LOCAL_PMO_MULTI_MODEL_CONTROL_ROOM_STUDY.md
files_changed:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_tasks.md
  - 000_ROADMAPS/SESSION_REGISTRY.md
files_not_touched:
  - docs 01-26
  - docs 27-34
  - 00_SYSTEM_GOVERNANCE/*
  - ARCHITECTURE_PATCH_REPORT.md
  - QA_DOCUMENTATION_CHECKLIST.md
  - auxiliary maps
  - 000_UPLOADS/
  - 000_UPGRADE/
  - backend, UI, API, database, migrations
  - n8n JSONs, MCP servers, webhooks, real agents, runtime automations
validation:
  - created only the requested study-only local PMO control room note; later index-reconciled from duplicate note 23 to note 26 without adding conceptual material
  - registered Windsurf as local PMO of support, not canonical authority
  - covered all 25 required sections plus templates
  - treated pseudo-webhook as a markdown convention only, not a real backend
  - used Paperclip as benchmark only; no Paperclip pattern copied
  - Doc 27 remains blocked; no canonical docs or implementation created
risks_remaining:
  - future readers may treat the control room or pseudo-webhook as real infrastructure
  - parallel sessions may still diverge if they ignore the registry, BRA and fan-in
  - this note requires PMO/Metacognik external audit before strong operational use
  - Doc 27 scope remains undecided until external audits and a Founder/PMO gate
next_step:
  - PMO/Metacognik audit this note with Study Layer 13 notes 01-22 and Study Layer 14
  - run Claude Code read-only audits, then PMO fan-in before any Doc 27 checkout
status: released_with_required_external_audit
```
