---
title: 000_ROADMAPS — ck_agent_handoffs
file: ck_agent_handoffs.md
phase: 000_ROADMAPS
category: agent_handoff
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
purpose: Controlar handoffs entre sessoes e agentes na camada auxiliar governada 000_ROADMAPS.
inputs:
  - 000_ROADMAPS/README.md
  - 000_ROADMAPS/ck_memory.md
  - 000_ROADMAPS/ck_tasks.md
outputs:
  - handoffs rastreaveis
  - bloqueios visiveis
  - proximas acoes
framework: CEO Agent plans, PMO Auditor validates, executor acts only inside approved scope.
edge_cases: Roadmap treated as canonical source; agent reads excessive context; implementation starts from planning material.
integrations: codex, claude, antigravity, ceo_agent, pmo_auditor and founder review sessions.
prompts: Read README and ck_memory before task-specific planning, patching or handoff.
metrics: YAML valid; 0 canonical docs created; 0 implementation changes; handoff logged when sessions change.
confidence: unverified
provenance_status: unverified
source_tool: chatgpt
related_notes:
  - README.md
  - ck_tasks.md
tags: [roadmaps, handoff, agents]
---

# ck_agent_handoffs — 000_ROADMAPS

## Regras de sessao

- CEO Agent planeja, prioriza, estima CKC e prepara handoff.
- PMO Auditor valida escopo, YAML, riscos, custo e governanca.
- Executor atua apenas em escopo aprovado e com checkout lock.
- Founder aprova bloqueios, proximos lotes e excecoes.
- Nenhum agente assume autoridade canonica.
- Toda sessao nova deve ler `README.md` + `ck_memory.md` antes de agir.
- Um agente escreve, outro audita.

## Formato obrigatorio de handoff

| handoff_id | from | to | date | scope | done | not_done | files_touched | risks | blockers | next_action | status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H-ROADMAPS-P0-001 | Founder/CEO Agent | Executor | 2026-05-28 | Estabilizar `000_ROADMAPS/` | Plano P0 aprovado | Study note, docs 26-34, UI/UX, Antigravity | A definir no release | YAML e escopo | Nenhum se checkout respeitado | Executar P0 e validar | active |
| H-ROADMAPS-P1-6-001 | Founder/PMO_CKOS | PMO_CKOS | 2026-05-28 | Roadmap Cleanup + Routing Layer | `ROADMAP_ROUTING_MATRIX.md` criado, NULs corrigidos, mapas auxiliares atualizados | Antigravity, UI implementation, docs canonicos, renames, moves, deletes | `000_ROADMAPS/`, mapas auxiliares permitidos | dual-source, Antigravity visual-first, camada auxiliar confundida com canonica | Antigravity segue bloqueado sem handoff restrito | Preparar handoff de Study Mode ou abrir P2 | released |
| H-ROADMAPS-P1-7-001 | Founder/PMO_CKOS | Codex Executor | 2026-05-28 | Multi-Session Execution Policy | `SESSION_REGISTRY.md`, `MULTI_SESSION_EXECUTION_POLICY.md` e gate Antigravity Study Mode criados; registros auxiliares atualizados | Implementacao, docs canonicos, docs 26-34, `ARCHITECTURE_PATCH_REPORT.md`, Antigravity activation | `000_ROADMAPS/`, `000_STUDY_NOTES/12_SESSION_GATES/`, mapas auxiliares permitidos | sessoes simultaneas sem lock, pergunta sem ROI/risco/custo/governanca, Antigravity visual-first | Antigravity segue bloqueado ate gate Founder de `design_study` | PMO/Metacognik auditar P1.7; Founder decidir ativacao futura | released |

## Contexto minimo antes de agir

1. Nota curta da tarefa ou handoff recebido.
2. `000_ROADMAPS/README.md`.
3. `000_ROADMAPS/ck_memory.md`.
4. README e `ck_memory.md` da pasta-alvo.
5. Apenas 3 a 7 docs obrigatorios da tarefa.

## Contexto minimo para Antigravity Study Mode

Antigravity continua bloqueado ate Founder aprovar handoff separado. Quando aprovado, a sessao deve ler apenas:

1. Nota curta da tarefa ou handoff.
2. `000_ROADMAPS/SESSION_REGISTRY.md`.
3. `000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md`.
4. `000_ROADMAPS/README.md`.
5. `000_ROADMAPS/ck_memory.md`.
6. `000_ROADMAPS/ROADMAP_ROUTING_MATRIX.md`.
7. `000_ROADMAPS/19_UIUX_STUDY_ROADMAP/README.md`.
8. `000_ROADMAPS/19_UIUX_STUDY_ROADMAP/ck_memory.md`.
9. `000_ROADMAPS/03_FRONTEND_UIUX_ROADMAP/01_UIUX_STUDY_TO_CANONICAL_ROADMAP.md`.
10. `000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md`.
11. `000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md`.

Saidas permitidas: study notes, perguntas, riscos, evidence map e patch candidates. Saidas proibidas: UI, frontend, backend, API, banco, migrations, JSONs n8n e agentes reais.

## Bloqueios permanentes neste P0

- Nao criar docs canonicos.
- Nao criar docs 26-34.
- Nao iniciar UI/UX.
- Nao iniciar Antigravity.
- Nao alterar governanca canonica.
- Nao executar backend, API, banco, migrations, JSONs n8n ou agentes reais.

## Regras P1.7 para handoff futuro

- Toda sessao deve declarar `session_id`, `session_type`, `agent`, `scope`, `status`, `started_at`, `expected_outputs`, `estimated_cost` e `intelligence_level`.
- Toda escrita exige checkout lock e checkout release.
- Nenhuma pergunta de decisao pode ser apresentada sem impacto em ROI, risco, custo ou governanca.
- Antigravity so pode operar em `design_study` apos gate formal aprovado pelo Founder.
