---
title: 000_ROADMAPS — ck_tasks
file: ck_tasks.md
phase: 000_ROADMAPS
category: kanban
version: 1.0.0
status: active
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
  - metacognik
purpose: Kanban raiz da camada auxiliar governada 000_ROADMAPS.
inputs:
  - 000_ROADMAPS/README.md
  - 000_ROADMAPS/ck_memory.md
outputs:
  - tarefas rastreaveis
  - bloqueios visiveis
  - proximos lotes
framework: Backlog, Ready, In Progress, Review, Done, Blocked.
edge_cases: Roadmap treated as canonical source; agent reads excessive context; implementation starts from planning material.
integrations: codex, claude, antigravity, ceo_agent, pmo_auditor and founder review sessions.
prompts: Read README and ck_memory before task-specific planning, patching or handoff.
metrics: YAML valid; 0 canonical docs created; 0 implementation changes; handoff logged when sessions change.
confidence: unverified
provenance_status: unverified
source_tool: chatgpt
related_notes:
  - README.md
  - ck_memory.md
tags: [roadmaps, tasks, kanban]
---

# ck_tasks — 000_ROADMAPS

## Backlog

| task_id | owner_session | status | scope | files_allowed | files_forbidden | estimated_ckc | approval_required | checkout_lock |
|---|---|---|---|---|---|---:|---|---|
| ROADMAPS_P2_LANE_EXPANSION | pmo_ckos | backlog | Expandir lanes apos roteamento P1.6, sem implementacao | `000_ROADMAPS/14_RUNTIME_BACKEND_ROADMAP/` a `000_ROADMAPS/21_LEARNING_AND_KNOWLEDGE_ROADMAP/` | docs canonicos, UI, backend, API, banco, migrations, JSONs n8n, agentes reais | 42 | founder | required |
| ANTIGRAVITY_STUDY_MODE_HANDOFF | ceo_agent | backlog | Preparar handoff Antigravity em modo estudo restrito com contexto minimo aprovado | `000_ROADMAPS/19_UIUX_STUDY_ROADMAP/`, `000_ROADMAPS/03_FRONTEND_UIUX_ROADMAP/`, `000_ROADMAPS/ROADMAP_ROUTING_MATRIX.md` | UI implementation, frontend, design final, backend, API, docs canonicos | 18 | founder | required |
| ANTIGRAVITY_DESIGN_STUDY_ACTIVATION | founder/pmo_ckos | backlog | Ativar Antigravity apenas se Founder aprovar gate formal de `design_study` | `000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md`, contexto minimo aprovado | UI implementation, frontend, backend, API, banco, migrations, docs canonicos, docs 26-34 | 18 | founder | required |

## Ready

| task_id | owner_session | status | scope | files_allowed | files_forbidden | estimated_ckc | approval_required | checkout_lock |
|---|---|---|---|---|---|---:|---|---|
| ROADMAPS_P0_VALIDATE | ceo_agent | ready | Validar P0 apos patch | `000_ROADMAPS/`, mapas auxiliares permitidos | arquivos fora do checkout | 6 | pmo_ckos | active |
| PMO_AUDIT_P1_7_MULTI_SESSION_POLICY | pmo_ckos/metacognik | ready | Auditar P1.7, registry, politica multi-sessao e gate Antigravity | `000_ROADMAPS/SESSION_REGISTRY.md`, `000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md`, `000_STUDY_NOTES/12_SESSION_GATES/` | docs canonicos, `ARCHITECTURE_PATCH_REPORT.md`, UI, backend, Antigravity activation | 8 | founder/pmo_ckos | required |

## In Progress

| task_id | owner_session | status | scope | files_allowed | files_forbidden | estimated_ckc | approval_required | checkout_lock |
|---|---|---|---|---|---|---:|---|---|
| none | none | none | Nenhuma tarefa em andamento registrada apos P1.6 | none | none | 0 | none | none |

## Review

| task_id | owner_session | status | scope | files_allowed | files_forbidden | estimated_ckc | approval_required | checkout_lock |
|---|---|---|---|---|---|---:|---|---|
| PMO_AUDIT_ROADMAPS_P0 | pmo_auditor | review | Auditar escopo, YAML, mapas auxiliares e guardrails do P0 | `000_ROADMAPS/`, mapas auxiliares permitidos | docs canonicos, implementacao | 8 | pmo_ckos | required |

## Done

| task_id | owner_session | status | scope | files_allowed | files_forbidden | estimated_ckc | approval_required | checkout_lock |
|---|---|---|---|---|---|---:|---|---|
| ROADMAPS_AUDIT_20260528_001 | ceo_agent | done | Auditoria read-only inicial de `000_ROADMAPS/` | leitura apenas | escrita em qualquer arquivo | 14 | founder | released |
| ROADMAPS_P0_STABILIZATION_20260528 | ceo_agent | done | Estabilizar camada auxiliar `000_ROADMAPS/` | `000_ROADMAPS/`, mapas auxiliares permitidos | governanca canonica, docs 01-25, docs 26-34, implementacao | 78 | founder | released |
| ROADMAPS_P1_MISSING_ROADMAPS_COMPLETION_20260528 | ceo_agent | done | Criar roadmaps auxiliares `14-21` | `000_ROADMAPS/14_RUNTIME_BACKEND_ROADMAP/` a `000_ROADMAPS/21_LEARNING_AND_KNOWLEDGE_ROADMAP/` | docs canonicos, docs 26-34, implementacao | 64 | founder | released |
| ROADMAPS_P1_5_RECONCILIATION_20260528 | pmo_ckos | done | Reconciliar roadmaps antigos e novos | `000_ROADMAPS/ROADMAP_RECONCILIATION_REPORT.md` | renames, moves, deletes, docs canonicos, implementacao | 24 | founder | released |
| ROADMAPS_P1_6_CLEANUP_ROUTING_LAYER_20260528 | pmo_ckos | done | Criar routing matrix, limpar NULs e atualizar mapas auxiliares | `000_ROADMAPS/`, mapas auxiliares permitidos | renames, moves, deletes, docs canonicos, implementacao, Antigravity | 22 | founder | released |
| P1.7_MULTI_SESSION_EXECUTION_POLICY_20260528 | codex | done | Criar registry, politica multi-sessao e gate Antigravity Study Mode | `000_ROADMAPS/`, `000_STUDY_NOTES/12_SESSION_GATES/`, mapas auxiliares permitidos | docs canonicos, docs 26-34, `ARCHITECTURE_PATCH_REPORT.md`, UI, backend, Antigravity activation | 28 | founder/pmo_ckos | released |

## Blocked

| task_id | owner_session | status | scope | files_allowed | files_forbidden | estimated_ckc | approval_required | checkout_lock |
|---|---|---|---|---|---|---:|---|---|
| DOCS_28_TO_34_CANONICAL | pmo_ckos | blocked | Criar docs canonicos 28-34 (Doc 26 e Doc 27 ja aprovados — ver nota abaixo) | nenhum neste P0 | docs 28-34 | 0 | founder | not_allowed |
| UIUX_ANTIGRAVITY_EXECUTION | uiux_study_agent | blocked | Acionar Antigravity para estudo UI/UX | nenhum neste P0 | UI, frontend, visual implementation | 0 | founder | not_allowed |

> **Nota de sincronizacao PMO (2026-06-01):** O tracking canonico vivo nao mora neste arquivo (escopo = camada auxiliar 000_ROADMAPS). Estado real dos docs canonicos esta em `000_ROADMAPS/SESSION_REGISTRY.md`, `000_ROADMAPS/TASK_KANBAN.md` e `ARCHITECTURE_PATCH_REPORT.md`. Resumo: **Doc 26 v1.0.4 aprovado** (auditoria externa), **Doc 27 aprovado** (sign-off formal 2026-06-01). Proximo: Doc 28 (Notes/RAG/Knowledge). Este `ck_tasks.md` raiz permanece congelado em P1.6/P1.7 por design e nao deve receber tarefas canonicas.
