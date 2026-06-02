---
title: 000_ROADMAPS — ck_risks
file: ck_risks.md
phase: 000_ROADMAPS
category: risk_register
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
purpose: Registro de riscos da camada auxiliar governada 000_ROADMAPS.
inputs:
  - 000_ROADMAPS/README.md
  - 000_ROADMAPS/ck_memory.md
outputs:
  - riscos classificados
  - mitigacoes
  - donos de mitigacao
framework: Documental, governance, cost/context, agent and premature implementation risk control.
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
tags: [roadmaps, risks, governance]
---

# ck_risks — 000_ROADMAPS

| risk_id | risk_type | severity | probability | impact | trigger | mitigation | owner | status | related_notes |
|---|---|---:|---:|---|---|---|---|---|---|
| RR-001 | risco documental | alta | media | Roadmap tratado como fonte canonica | Agente cita roadmap como decisao final | Declarar camada auxiliar e exigir patch plan para canonizacao | pmo_ckos | aberto | README.md |
| RR-002 | risco de governanca | alta | media | Alteracao fora de escopo | Sessao edita governanca canonica ou docs 01-25 | Checkout lock com files_allowed/files_forbidden | pmo_ckos | aberto | ck_tasks.md |
| RR-003 | risco de custo/contexto | media | alta | Custo alto e ruido por leitura excessiva | Agente le todo o vault no inicio | Regra de contexto minimo: README, ck_memory e 3 a 7 docs obrigatorios | ceo_agent | aberto | ck_memory.md |
| RR-004 | risco de agente | alta | media | Sessoes paralelas se atropelam | Dois agentes editam mesma pasta | Regra um agente escreve, outro audita; handoff obrigatorio | pmo_ckos | aberto | ck_agent_handoffs.md |
| RR-005 | risco de implementacao prematura | alta | media | UI/backend/API criados antes dos gates | Estudo visual vira tela ou runtime real | Bloqueio explicito de UI, backend, API, banco, migrations e agentes reais | founder | aberto | README.md |
| RR-006 | risco de duplicidade | media | media | Roadmaps antigos competem com o P0 | Packs em `000_UPGRADE` usados como roadmap atual | Usar `000_ROADMAPS/` como controle de trafego auxiliar e auditar referencias antigas | pmo_ckos | aberto | CKOS_FILETREE_MAP.md |
| RR-007 | risco de desatualizacao | media | media | Memoria da pasta fica atrasada | Patch feito sem atualizar `ck_memory.md` | Atualizar memoria em todo checkout release | roadmap_keeper | aberto | ck_memory.md |
| RR-008 | risco de roteamento | alta | media | Roadmap antigo e novo recebem tarefas paralelas | Sessao escolhe `02/06/07/10` em vez de `14/15/16/17` sem criterio | Usar `ROADMAP_ROUTING_MATRIX.md` antes de abrir P2 ou handoff | pmo_ckos | aberto | ROADMAP_ROUTING_MATRIX.md |
| RR-009 | risco de higiene documental | baixa | baixa | Caracteres NUL quebram leitura minima em READMEs `14-21` | Conteudo gerado com escape incorreto em P1 | Corrigido no P1.6; validar NUL em todo release | pmo_ckos | mitigado | `14-21` READMEs |
| RR-010 | risco Antigravity visual-first | alta | media | Antigravity transforma referencia visual em UI sem motor operacional | Study Mode iniciado sem contexto minimo e sem matriz | Handoff restrito deve citar `ROADMAP_ROUTING_MATRIX.md` e bloquear frontend/UI implementation | founder | aberto | ck_agent_handoffs.md |
| RR-011 | risco multi-sessao | alta | media | Codex, Claude, Antigravity ou especialista editam o mesmo arquivo em paralelo | Sessao inicia sem registry ou sem lock | `SESSION_REGISTRY.md`, checkout lock obrigatorio e regra one file, one writer | pmo_ckos | aberto | SESSION_REGISTRY.md |
| RR-012 | risco de nivel de inteligencia | media | media | Sessao usa modelo/contexto fraco para decisao de alto risco | `intelligence_level` ausente ou subestimado | Matriz `low/medium/high/highest` em `MULTI_SESSION_EXECUTION_POLICY.md` | pmo_ckos | aberto | MULTI_SESSION_EXECUTION_POLICY.md |
| RR-013 | risco de pergunta sem decisao | media | alta | Perguntas aumentam conversa sem reduzir risco, custo, ROI ou governanca | Agente pergunta por preferencia sem consequencia operacional | Regra P1.7: toda pergunta de decisao deve declarar impacto em ROI, risco, custo ou governanca | ceo_agent | aberto | 01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md |

## Politica de mitigacao

- Risco alto exige PMO Auditor antes de execucao.
- Excecao de escopo exige Founder approval.
- Nenhum risco pode ser fechado sem registrar evidencia ou decisao no arquivo apropriado.
