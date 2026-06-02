---
title: Multi-Session Execution Policy - P1.7
system_id: multi_session_execution_policy_p1_7_20260528
layer: auxiliary
phase: 000_ROADMAPS
category: execution_policy
status: auxiliary
version: 1.0.0
owner: pmo_ckos
responsible_agent: codex
reviewers:
  - founder
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
confidence: unverified
provenance_status: unverified
source_tool: codex
created_at: 2026-05-28
version_note: "v1.0.0 — promoted after PMO/Metacognik audit of P1.7."
purpose: Define auxiliary multi-session rules for Codex, Claude, Antigravity and future specialist chats without granting canonical or implementation authority.
inputs:
  - 000_ROADMAPS/README.md
  - 000_ROADMAPS/ck_memory.md
  - 000_ROADMAPS/ck_agent_handoffs.md
  - 000_ROADMAPS/ROADMAP_ROUTING_MATRIX.md
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md
outputs:
  - multi-session session type matrix
  - checkout lock policy
  - checkout release policy
  - intelligence level policy
  - Antigravity Study Mode gate dependency
framework:
  - auxiliary governance
  - checkout lock
  - one writer, another auditor
  - Intent -> Question -> Plan -> Approval -> Execution -> Memory
edge_cases:
  - parallel agents writing the same file
  - Antigravity starting visual implementation from study language
  - canonical patch session inferred from auxiliary roadmap
  - decision question without ROI, risk, cost or governance impact
metrics:
  - zero canonical docs created by this policy
  - zero implementation actions authorized by this policy
  - every session declares registry fields
  - every writing session emits checkout release
related_notes:
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md
tags:
  - multi_session
  - execution_policy
  - checkout_lock
  - antigravity_gate
  - auxiliary
---

# Multi-Session Execution Policy - P1.7

> Toda sessão que toca o vault CKOS declara escopo, declara o que não tocará, abre checkout lock, opera dentro do escopo declarado e fecha com checkout release. Nenhuma exceção. Nenhuma sessão rápida sem lock.

## 1. Status

Version note: v1.0.0 — promoted after PMO/Metacognik audit of P1.7.

This policy is AUXILIARY GOVERNED. It is not canonical. It does not authorize implementation. It does not create docs 26-34. It does not start UI/UX. It does not start Antigravity.

This policy exists to let CKOS operate multiple simultaneous sessions without conflict between Codex, Claude, Antigravity and future specialist chats.

> **Reconciliação 2026-06-02 (S-P1-RECONCILE-CLAUDE-20260602-004):** quando esta policy foi redigida (P1.7, 2026-05-28), o canônico ia até 01-25 e os Docs 26-34 não existiam. Desde então, **Docs 26, 27 e 28 foram criados via gates dedicados aprovados**. Leitura vigente: canônico vivo = **01-28**; bloqueio de criação sem gate = **docs 29-34**; alteração de qualquer doc canônico 01-28 só via sessão `canonical_patch` com gate. As referências "01-25" e "26-34" nas §1-§2 abaixo permanecem como redigidas em P1.7 (registro histórico); esta nota rege a interpretação atual. Fonte autoritativa da fronteira: `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`.

## 2. Non-Authority Boundary

This policy may govern auxiliary sessions, locks, gates, handoffs and memory updates. It may not:

- alter canonical docs 01-25;
- create docs 26-34;
- update `ARCHITECTURE_PATCH_REPORT.md` in P1.7;
- update `QA_DOCUMENTATION_CHECKLIST.md`;
- implement UI, UX, backend, API, database, migrations, JSONs n8n, runtime workers or real agents;
- move, rename or delete files;
- treat Antigravity as active before a Founder-approved Design Study Session gate.

## 3. Required Session Declaration

Every future CKOS session must declare these fields before action:

| field | required |
|---|---|
| `session_id` | Unique session identifier. |
| `session_type` | One approved type from the session matrix. |
| `agent` | Codex, Claude, Antigravity, PMO, Founder, CEO Agent or specialist. |
| `scope` | Allowed and forbidden folders/files. |
| `status` | `planned`, `active`, `blocked`, `released`, `cancelled` or `superseded`. |
| `started_at` | Start date/time or date. |
| `expected_outputs` | Authorized deliverables. |
| `estimated_cost` | CKC/token/time/tool cost estimate or `low`, `medium`, `high`, `unknown`. |
| `intelligence_level` | `low`, `medium`, `high` or `highest`. |

No writing session may begin unless it is visible in `000_ROADMAPS/SESSION_REGISTRY.md` or has an explicit checkout lock supplied by Founder/PMO.

## 4. Session Type Matrix

| session_type | purpose | allowed outputs | write permission | approval posture | default intelligence_level |
|---|---|---|---|---|---|
| `planning` | Prepare sequence, scope, costs, risks and handoff. | plans, task packs, questions, handoffs | auxiliary only, if checkout lock allows | PMO/Founder when cost or scope changes | medium |
| `audit` | Review scope, YAML, risks, costs, consistency and forbidden actions. | findings, blockers, QA notes, release validation | auxiliary audit files only, if allowed | PMO/Metacognik recommended | high |
| `execution` | Apply an approved auxiliary patch in a locked scope. | files created/changed exactly as authorized | only files in checkout lock | Founder/PMO approval required when scope is material | high |
| `study` | Interpret sources and create non-canonical study material. | study notes, source maps, questions, risks | `000_STUDY_NOTES/` only when locked | PMO/Founder if it affects future canon | medium |
| `research` | Gather evidence and references without canonizing. | research summaries, evidence maps, source manifests | auxiliary research/study files only | PMO/Founder if external tools/costs are used | high |
| `design_study` | Study visual/product direction without implementation. | design study notes, questions, risks, evidence maps | study folders only; no UI files | Founder gate required for Antigravity | high |
| `memory_refresh` | Update maps, folder memory and operational state. | memory updates, filetree notes, refresh reports | auxiliary memory/map files only | PMO required if broad refresh | medium |
| `patch_candidate` | Prepare a non-canonical candidate for later patch plan. | patch candidate, rationale, risks, acceptance criteria | `000_STUDY_NOTES/07_CANONICAL_PATCH_CANDIDATES/` only if separately authorized | Founder/PMO before promotion | high |
| `canonical_patch` | Apply an approved canonical patch. | canonical doc changes and patch report updates | canonical files only inside separate canonical checkout | Founder + PMO + Metacognik approval required | highest |

`canonical_patch` is listed for policy completeness only. P1.7 does not open a canonical patch session.

## 5. Intelligence Level Matrix

| intelligence_level | use when | minimum behavior | typical cost posture | examples |
|---|---|---|---|---|
| `low` | Small clerical update with no policy ambiguity. | Follow exact scope, no broad reasoning. | lowest | typo in auxiliary task list after approval |
| `medium` | Routine auxiliary planning, memory or study work. | Check local context, estimate risk/cost, avoid scope drift. | controlled | roadmap task update, folder README update |
| `high` | Cross-session, multi-agent, risk-bearing or governance-sensitive work. | Read required context, reason through conflicts, document risks and release. | justified by reduced rework | P1.7, routing, audit, Study Mode gates |
| `highest` | Canonical, high-risk, irreversible, legal/security/cost-heavy or architecture-defining work. | Full gate discipline, explicit approvals, audit trail, rollback thinking. | high; must be justified | canonical patch, security policy, production implementation readiness |

The chosen level must match risk, not model prestige. A session may be upgraded when risk, governance, ambiguity, cost or blast radius increases.

## 6. Layer Permission Matrix

| layer/folder | planning | audit | execution | study/research/design_study | memory_refresh | patch_candidate | canonical_patch |
|---|---|---|---|---|---|---|---|
| `000_ROADMAPS/` | allowed with lock | allowed with lock | allowed with lock | read/reference | allowed with lock | read/reference | read/reference |
| `000_STUDY_NOTES/` | allowed with lock | allowed with lock | allowed with lock | allowed with lock | allowed with lock | allowed only in authorized candidate folder | read/reference |
| `000_UPLOADS/` | read/reference only unless separate lock | read/reference | no write in P1.7 | read/reference only | no write in P1.7 | no write in P1.7 | read/reference |
| canonical folders `00-07` | read only when required | read only when required | forbidden in P1.7 | read only when required | forbidden in P1.7 | read only | separate Founder-approved canonical patch only |
| root canonical controls | read only | read only | forbidden in P1.7 | read only | auxiliary maps only if listed | read only | separate Founder-approved canonical patch only |
| implementation/runtime assets | forbidden | forbidden | forbidden | forbidden | forbidden | forbidden | only after separate implementation readiness gate |

When in doubt, the session must choose the narrower read/write scope.

## 7. Checkout Lock Policy

A checkout lock is mandatory before writing. It must declare:

- `task_id`;
- `session_id` or session holder;
- `session_type`;
- `agent`;
- allowed folders and files;
- forbidden folders and files;
- expected outputs;
- estimated cost;
- intelligence level;
- approval basis;
- release requirements.

If the same file is already locked by another active session, the new session must stop or ask PMO/Founder for a narrowed non-overlapping lock.

## 8. Checkout Release Policy

Every writing session must end with:

- files_created;
- files_changed;
- files_not_touched;
- validation;
- risks_remaining;
- next_step;
- status.

The release must state whether canonical docs, docs 26-34, `ARCHITECTURE_PATCH_REPORT.md`, implementation, UI/UX, Antigravity or forbidden folders were touched.

## 9. Decision Question Rule

Nenhuma pergunta de decisao pode ser apresentada sem impacto em ROI, risco, custo ou governanca.

If a question does not affect ROI, risk, cost, governance, approval, scope, evidence, reversibility or memory, it must be removed or rewritten.

## 10. Antigravity Rule

Antigravity may only operate in a `design_study` session after a formal Founder-approved gate.

The gate must be represented in `000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md`. Until the gate is explicitly approved for activation, Antigravity remains blocked.

Allowed Antigravity Design Study outputs after approval:

- design study notes;
- visual/product questions with ROI, risk, cost or governance impact;
- evidence maps;
- risk lists;
- non-canonical recommendations;
- patch candidates only if separately authorized.

Forbidden Antigravity outputs:

- UI implementation;
- frontend files;
- backend/API/database/migrations;
- runtime agent creation;
- JSONs n8n;
- canonical docs;
- docs 26-34.

## 11. Concurrency Rules

- One file, one writer.
- One agent writes, another audits when risk is material.
- Read-only parallel sessions are allowed when they do not create conflicting summaries.
- A session with broader scope must not overwrite a narrower active lock.
- PMO may pause a session when scope, cost, approval status or provenance is unclear.
- Founder decides exceptions, escalations and activation of Antigravity Design Study.

## 12. Acceptance Criteria

- `SESSION_REGISTRY.md` exists and was created before this policy.
- This policy declares auxiliary layer, `confidence: unverified` and `provenance_status: unverified`.
- Session types include `planning`, `audit`, `execution`, `study`, `research`, `design_study`, `memory_refresh`, `patch_candidate` and `canonical_patch`.
- Intelligence levels include `low`, `medium`, `high` and `highest`.
- Checkout lock and release are required for writing sessions.
- Antigravity is blocked unless a Founder-approved Design Study Session gate exists.
- No canonical docs are changed by P1.7.
- No docs 26-34 are created by P1.7.
- No implementation, UI/UX or Antigravity run is started by P1.7.
