---
title: "Roadmap Routing Matrix - P1.6"
system_id: roadmap_routing_matrix_p1_6_20260528
layer: auxiliary
phase: 000_ROADMAPS
category: routing_matrix
status: auxiliary
version: 1.0.0
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
created_at: 2026-05-28
purpose: "Route old and new 000_ROADMAPS workstreams without promoting the roadmap layer to canonical authority."
inputs:
  - "000_ROADMAPS/README.md"
  - "000_ROADMAPS/ROADMAP_RECONCILIATION_REPORT.md"
  - "000_ROADMAPS/02_RUNTIME_BACKEND_ROADMAP/"
  - "000_ROADMAPS/03_FRONTEND_UIUX_ROADMAP/"
  - "000_ROADMAPS/04_CONNECTORS_MCP_INTEGRATIONS_ROADMAP/"
  - "000_ROADMAPS/05_SUPERAGENTS_AGENTS_SUBAGENTS_ROADMAP/"
  - "000_ROADMAPS/06_SECURITY_GOVERNANCE_ROADMAP/"
  - "000_ROADMAPS/07_BUSINESS_ROI_BILLING_ROADMAP/"
  - "000_ROADMAPS/08_LEARNING_STUDY_MEMORY_ROADMAP/"
  - "000_ROADMAPS/10_RELEASES_AND_GATES/"
  - "000_ROADMAPS/14_RUNTIME_BACKEND_ROADMAP/"
  - "000_ROADMAPS/15_SECURITY_GOVERNANCE_ROADMAP/"
  - "000_ROADMAPS/16_BUSINESS_SYSTEMS_ROADMAP/"
  - "000_ROADMAPS/17_RELEASES_GATES_ROADMAP/"
  - "000_ROADMAPS/18_CONNECTORS_MCP_INTEGRATIONS_ROADMAP/"
  - "000_ROADMAPS/19_UIUX_STUDY_ROADMAP/"
  - "000_ROADMAPS/20_AGENT_CIVILIZATION_ROADMAP/"
  - "000_ROADMAPS/21_LEARNING_AND_KNOWLEDGE_ROADMAP/"
outputs:
  - "routing table for old and new roadmap folders"
  - "usage rules for each roadmap"
  - "duplicate-risk controls"
  - "PMO routing recommendations"
framework:
  - "Intent -> Question -> Plan -> Execution"
  - "roadmap routing"
  - "legacy-index without rename"
  - "study before implementation"
edge_cases:
  - "old active roadmap overrides new wrapper"
  - "new draft roadmap is mistaken for canonical source"
  - "Antigravity enters UI implementation instead of study mode"
  - "connector roadmap triggers external tool or secret use"
  - "agent roadmap triggers real agent creation"
integrations:
  - "Codex"
  - "PMO_CKOS"
  - "Metacognik"
  - "future Antigravity Study Mode"
prompts:
  - "Read this matrix before choosing between old and new roadmap folders."
  - "Use old folders as source/history when marked source or legacy-index."
  - "Use new folders as P2 workstream wrappers when marked wrapper."
metrics:
  - "0 renames"
  - "0 moves"
  - "0 deletes"
  - "0 canonical docs created"
  - "routing visible before Antigravity study"
related_notes:
  - "000_ROADMAPS/ROADMAP_RECONCILIATION_REPORT.md"
  - "000_ROADMAPS/ck_memory.md"
  - "000_ROADMAPS/ck_tasks.md"
tags:
  - "roadmaps"
  - "routing"
  - "p1_6"
  - "auxiliary"
---

# Roadmap Routing Matrix - P1.6

## Status

This is an auxiliary routing layer. It does not replace canonical documents, does not authorize implementation and does not rename, move or delete any roadmap folder.

## Routing principles

- Old roadmaps can remain useful as source, history, acceptance references or legacy-index folders.
- New roadmaps `14-21` act as P1/P2 workstream wrappers with clearer scope, risks, ROI and handoff controls.
- A roadmap marked `legacy-index_candidate` remains readable and preserved until Founder/PMO approve a later patch.
- Antigravity remains blocked until a separate Study Mode handoff with minimum context is approved.
- UI, backend, API, database, migrations, JSONs n8n and real agents remain blocked.

## Primary matrix

| old_or_existing_roadmap | new_or_related_roadmap | function_old | function_new | when_to_use_old | when_to_use_new | dependencies | duplicate_risk | PMO decision |
|---|---|---|---|---|---|---|---|---|
| `02_RUNTIME_BACKEND_ROADMAP` | `14_RUNTIME_BACKEND_ROADMAP` | legacy-index_candidate for runtime/backend planning | wrapper for runtime/backend P2 planning | use for historical context and prior P0 task references | use for event bus, policy engine, model router, context pack builder, approval gate, cost guard, audit logs and projection engine planning | docs `03_RUNTIME_SYSTEM/*`, security, cost guard, approval gates | high if both receive tasks | route new tasks to `14`; keep `02` preserved |
| `06_SECURITY_GOVERNANCE_ROADMAP` | `15_SECURITY_GOVERNANCE_ROADMAP` | legacy-index_candidate for security/governance | wrapper for transversal security/governance planning | use for previous security lane memory | use for data sensitivity, cross-tenant risk, secrets, audit, policy checks and cost guard planning | governance, runtime, connectors, UI study, business systems | high if agents cite old active folder as source of current execution | route new tasks to `15`; keep `06` preserved |
| `07_BUSINESS_ROI_BILLING_ROADMAP` | `16_BUSINESS_SYSTEMS_ROADMAP` | legacy-index_candidate and historical ROI/billing source | wrapper for business systems planning | use for prior ROI, credits and billing vocabulary | use for ROI, feedback, support, credits, plans, billing, cost ledger, plan gates and usage events | docs `06_BUSINESS_SYSTEMS/*`, cost control, approvals | medium if billing/pricing is treated as implementation | route new tasks to `16`; keep `07` preserved |
| `10_RELEASES_AND_GATES` | `17_RELEASES_GATES_ROADMAP` | legacy-index_candidate for release/gate history | wrapper for formal Gate A-G readiness planning | use for prior gate language and historical release notes | use for Gate A Documentation, Gate B Runtime, Gate C Product, Gate D Security, Gate E UI/UX Study, Gate F Implementation Readiness and Gate G MVP P0 | acceptance criteria, PMO, Metacognik, QA | high if gate status is inferred without evidence | route new tasks to `17`; keep `10` preserved |
| `04_CONNECTORS_MCP_INTEGRATIONS_ROADMAP` | `18_CONNECTORS_MCP_INTEGRATIONS_ROADMAP` | source roadmap with connector rules | wrapper for connectors/MCP/integrations P2 planning | use for existing MCP, API, webhook, OAuth, n8n and connector policy notes | use for new scoped planning and handoff controls | `14`, `15`, `16`, tool routing, approval gate, cost guard, audit logs | medium/high if connector planning triggers external tool use | keep both; `18` depends on runtime, security and cost |
| `03_FRONTEND_UIUX_ROADMAP` | `19_UIUX_STUDY_ROADMAP` | source roadmap with UI/UX study content | wrapper for UI/UX Study Mode readiness | use for UI/UX study taxonomy, operational grammar and visual-study substance | use for Antigravity context pack and study-only gates | `15`, `17`, study note Intent/Question/Plan/Execution | high if visual references become implementation | keep both; Antigravity blocked until approved minimum context |
| `05_SUPERAGENTS_AGENTS_SUBAGENTS_ROADMAP` | `20_AGENT_CIVILIZATION_ROADMAP` | preserved source for agent hierarchy and handoffs | wrapper for agent civilization planning | use for historical and current agent hierarchy source | use for future P2 capability/handoff planning | Founder authority, PMO, Metacognik, checkout locks | high if wrapper is treated as authority to create real agents | keep `05` preserved without rename; `20` stays auxiliary |
| `08_LEARNING_STUDY_MEMORY_ROADMAP` | `21_LEARNING_AND_KNOWLEDGE_ROADMAP` | source roadmap for memory operating standard | wrapper for learning/knowledge planning | use for short/mid/long memory rules and folder memory standards | use for learning mode, knowledge readiness, source governance, study notes, feedback loops and future RAG planning | memory architecture, study notes, source governance, feedback | medium if learning planning triggers ingestion/RAG implementation | keep both; `21` depends on memory and source governance |

## Standalone support routing

| roadmap | function | when_to_use | risk | PMO decision |
|---|---|---|---|---|
| `00_MASTER_ROADMAP` | macro coordination | use for overall phase/gate sequencing | can be over-read as full context | keep active as overview |
| `01_DOCUMENTATION_ROADMAP` | docs 26-34 planning | use only for canonical sequence planning, not creation | docs 26-34 could be created prematurely | keep active; creation remains blocked |
| `09_CLIENT_PROJECT_CREATOR_MODE_ROADMAP` | intent-to-project planning | use for client/project creator flow | can trigger project artifacts without filetree approval | keep active |
| `11_TEMPLATES` | checkout/release/note templates | use for controlled patches | template may be mistaken for completed approval | keep active |
| `12_PROMPTS` | model/session prompts | use to prepare Codex, Claude, Antigravity or PMO sessions | prompt may exceed context or authorize too much | keep active; prompt updates require checkout |
| `13_ACCEPTANCE_CRITERIA` | acceptance criteria | use for QA and release validation | criteria may be skipped under time pressure | keep active |

## Antigravity gate

Antigravity may only enter Study Mode after a separate Founder-approved handoff. The minimum context pack should include:

1. task note or handoff;
2. `000_ROADMAPS/README.md`;
3. `000_ROADMAPS/ck_memory.md`;
4. `000_ROADMAPS/ROADMAP_ROUTING_MATRIX.md`;
5. `000_ROADMAPS/19_UIUX_STUDY_ROADMAP/README.md`;
6. `000_ROADMAPS/19_UIUX_STUDY_ROADMAP/ck_memory.md`;
7. `000_ROADMAPS/03_FRONTEND_UIUX_ROADMAP/01_UIUX_STUDY_TO_CANONICAL_ROADMAP.md`;
8. `000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md`.

Study Mode output must be study notes, questions, risks, evidence maps or patch candidates only. No UI implementation, frontend files, backend files, API work, database work, migrations, n8n JSONs or real agents are authorized.

## PMO recommended decision

Proceed to Antigravity Study Mode only after Founder approval of a restricted handoff that cites this routing matrix. If Founder prefers more consolidation first, open P2 for lane expansion instead of starting Antigravity.
