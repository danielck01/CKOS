---
title: P0 Dev Hardening Skill Pack Architecture
file: 05_P0_DEV_HARDENING_SKILL_PACK_ARCHITECTURE.md
phase: 000_ROADMAPS
category: skill_pack_architecture
status: draft_ready_for_founder_review
owner: pmo_ckos
created_at: 2026-06-02
pack_id: P0_DEV_HARDENING_SKILL_PACK
skill_files_created: false
canonical_patch: false
no_runtime_authority: true
implementation_authorized: false
purpose: >
  Definir a arquitetura previa do bloco P0 de skills de desenvolvimento que
  tornam Claude Code, Codex e Windsurf executores CKOS-native, reduzindo
  dependencia de prompts genericos e memoria implicita de LLM.
source_docs:
  - 00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md
  - 02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md
  - 02_EXECUTION_SYSTEM/07_WORKFLOW_BLUEPRINTS.md
  - 02_EXECUTION_SYSTEM/08_PROMPT_LIBRARY.md
  - 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - 03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - 03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - 06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md
  - 06_BUSINESS_SYSTEMS/22_FEEDBACK_SYSTEM_ARCHITECTURE.md
  - 06_BUSINESS_SYSTEMS/23_SUPPORT_SYSTEM_ARCHITECTURE.md
  - 06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md
  - 000_ROADMAPS/22_CONSOLIDATION/03_BACKEND_MVP_THIN_SLICE_PLAN.md
confidence: high
---

# 1. Proposito

Este documento define a arquitetura previa das 6 skills P0 de endurecimento de desenvolvimento:

1. `ckos-implementation-brief`
2. `ckos-backend-thin-slice`
3. `ckos-data-model-migration`
4. `ckos-policy-rls-security`
5. `ckos-event-runtime-contract`
6. `ckos-qa-gate`

O objetivo e transformar executores genericos, como Claude Code, Codex e Windsurf, em executores governados pelo CKOS. A skill deve carregar o contrato de qualidade, escopo, risco, evidencia e validacao que o modelo nao deve precisar lembrar por improviso.

Este arquivo nao cria as skills instalaveis em `.codex/skills`, nao altera o Doc 06, nao cria backend, API, banco, migrations, UI, agentes reais, automacoes runtime, MCP server, webhook ou JSON n8n.

# 2. Diagnostico

O pack operacional ja criado cobre o trilho de trabalho:

```txt
project-intake -> briefing-builder -> note-normalizer/document-ingestion
-> context-pack-builder -> work-order-draft -> risk-gap-review -> checkout-release
```

Esse trilho e necessario, mas nao suficiente para desenvolvimento real. Backend, banco, security, events, cost, evals e billing possuem invariantes que precisam virar skill explicita. Sem isso, cada executor tende a cair em padroes genericos:

- criar CRUD antes de event log;
- tratar UI como origem de estado;
- sugerir migration sem RLS/tenant scope;
- aplicar permissao como pos-filtro;
- misturar `cost_ledger` com billing;
- inventar schema a partir de estudo ou prompt;
- fazer QA apenas por build/test, sem auditabilidade CKOS.

# 3. Principios do Pack

1. **Skill nao e prompt.** Cada skill deve ter trigger, entradas, saidas, limites, verificacao e criterios de reprovacao.
2. **Implementation brief antes de codigo.** Nenhum executor tecnico recebe tarefa aberta sem escopo, arquivos, risco, testes e rollback.
3. **Runtime antes de produto.** Desenvolvimento P0 prova `intent -> event -> run -> artifact -> memory/ROI`, nao uma tela bonita.
4. **Event log e fonte de verdade.** Estado operacional deriva de eventos append-only e projecoes.
5. **Security fail-closed.** Ausencia de policy, RLS, namespace, approval ou secret_ref bloqueia a acao.
6. **Banco nao nasce de improviso.** Schema e migration derivam do Doc 11 ou viram `ARCHITECTURE_QUESTION`.
7. **QA precisa auditar CKOS, nao so compilar.** Build/test e necessario, mas insuficiente.
8. **Skills ficam pequenas.** Detalhe canonico pesado deve ir em `references/` ao criar os `SKILL.md`.

# 4. Sequencia Operacional

```txt
Work Order / context pack
  -> ckos-implementation-brief
  -> seleciona guardas especificas:
       ckos-backend-thin-slice
       ckos-data-model-migration
       ckos-policy-rls-security
       ckos-event-runtime-contract
  -> executor tecnico aplica mudanca
  -> ckos-qa-gate
  -> checkout-release
```

As quatro skills de guarda podem ser usadas em paralelo quando o trabalho tocar varias superficies. `ckos-qa-gate` sempre fecha a cadeia antes de qualquer release.

# 5. Contrato Padrao de Cada Skill

Cada skill P0 deve ser criada depois com esta estrutura minima:

```yaml
name:
description:
category: development_hardening
owner_agent:
review_agent:
autonomy_level:
approval_required:
allowed_tools:
required_inputs:
outputs:
when_to_use:
when_not_to_use:
forbidden_scope:
validation:
failure_modes:
canonical_refs:
```

O `SKILL.md` deve conter o procedimento essencial. Se a skill precisar de checklist longa, schemas ou exemplos, isso vai para `references/`.

# 6. Skill 1 - ckos-implementation-brief

## 6.1 Funcao

Transformar Work Order, briefing, context pack ou decisao Founder em um briefing tecnico executavel para Claude Code, Codex ou Windsurf.

## 6.2 Quando usar

- Antes de qualquer implementacao, refatoracao, migration, API, worker, teste ou patch tecnico.
- Quando um pedido ainda esta em linguagem de produto/estrategia e precisa virar tarefa tecnica governada.
- Quando multiplos executores precisam receber o mesmo contrato de escopo.

## 6.3 Quando nao usar

- Para brainstorming sem autorizacao de execucao.
- Para editar canonicamente Doc 06/10/11/12/13 sem gate documental.
- Para substituir `work-order-draft`; ela consome Work Order, nao o substitui.

## 6.4 Entradas minimas

- Objetivo tecnico.
- Fonte de autoridade: Work Order, briefing, context pack ou decisao Founder.
- Escopo permitido e proibido.
- Arquivos ou superficies provaveis.
- Risco, dados sensiveis, custo, rollback e criterios de aceite.

## 6.5 Saida verificavel

Um implementation brief com:

- executor recomendado;
- task decomposition;
- file impact map;
- forbidden scope;
- acceptance criteria;
- validation commands;
- rollback/fallback;
- security/data/event/cost checks aplicaveis;
- release evidence esperado.

## 6.6 Guardrails

- Se nao houver fonte de autoridade, parar e pedir Work Order/context pack.
- Se schema/migration for necessario mas nao estiver no Doc 11, gerar `ARCHITECTURE_QUESTION`.
- Se tocar risk high, dados sensiveis, billing, policy ou deploy, exigir approval explicito.

# 7. Skill 2 - ckos-backend-thin-slice

## 7.1 Funcao

Guiar implementacao ou planejamento de backend P0 do CKOS como thin-slice auditavel, sem cair em UI-first, chat-first ou CRUD generico.

## 7.2 Quando usar

- Em tarefas do GATE 5/F1 backend.
- Quando o trabalho tocar ingress, intent resolver, workflow run, agent run, context pack, event store, approval gate, memory boundary ou ROI proxy.
- Quando for preciso decidir se algo pertence ao backend P0 ou deve esperar.

## 7.3 Quando nao usar

- Para frontend, dashboard, painel, design system ou UX rica.
- Para especificar internals de RAG, embeddings, chunking ou vector ranking.
- Para autorizar implementacao antes de Founder approval.

## 7.4 Entradas minimas

- Sprint ou slice alvo.
- Fluxo `intent -> event -> run -> output`.
- Componentes runtime afetados.
- Superficies de dados previstas no Doc 11.
- Politicas de approval, tenant, secret e custo.

## 7.5 Saida verificavel

Um plano ou execucao backend com:

- backend-only boundary;
- evento inicial e eventos consequentes;
- correlation_id, causation_id e idempotency_key;
- context pack minimo;
- policy/approval checkpoint;
- output simples com evidencia;
- custo e trace;
- criterio de replay causal.

## 7.6 Guardrails

- Reprovar se UI for criterio de pronto.
- Reprovar se estado operacional viver fora de eventos/projecoes.
- Reprovar se RLS/tenant isolation for adiado.
- Reprovar se Work Order virar tabela fisica sem Doc 11/AQ.

# 8. Skill 3 - ckos-data-model-migration

## 8.1 Funcao

Blindar modelagem de dados, schema, migration, seed e persistencia contra improviso, drift canonico e falhas multi-tenant.

## 8.2 Quando usar

- Antes de criar ou alterar tabela, coluna, indice, enum, view, projection, migration ou seed.
- Quando um executor sugerir schema derivado de prompt, estudo ou conveniencia.
- Quando o trabalho tocar `events`, `workflow_runs`, `agent_runs`, `context_packs`, `audit_logs`, `cost_ledger`, `approvals`, `documents`, `memories`, `embeddings` ou billing.

## 8.3 Quando nao usar

- Para decidir produto ou UX.
- Para inventar schema fisico de Work Orders sem decisao canonica.
- Para criar migrations reais em fase documental.

## 8.4 Entradas minimas

- Mudanca pretendida.
- Doc 11 ou patch/AQ que autoriza a superficie.
- Tenant/org/workspace/project scope.
- RLS requirement.
- Migration direction, rollback/compensation e impacto em dados existentes.

## 8.5 Saida verificavel

Uma proposta ou checklist de dados com:

- mapping para Doc 11;
- tabelas/colunas/indices afetados;
- `org_id`/`workspace_id`/`project_id` quando aplicavel;
- RLS/FORCE RLS esperado;
- append-only ou compensating model quando aplicavel;
- idempotency e uniqueness constraints;
- migration validation e rollback/fallback;
- AQs quando a autoridade nao existir.

## 8.6 Guardrails

- Ausencia de tenant scope em tabela de dominio e falha P0.
- `events`, `audit_logs`, billing events e cost ledger devem ser append-only.
- Vector namespace e pre-condicao, nao pos-filtro.
- Secret real nunca entra em tabela; apenas `secret_ref`.

# 9. Skill 4 - ckos-policy-rls-security

## 9.1 Funcao

Aplicar o modelo de seguranca CKOS: deny-by-default, RBAC+ABAC, RLS, policyRegistry, approval policies, secrets, tenant isolation, vector/storage isolation e audit trail.

## 9.2 Quando usar

- Qualquer tarefa que toque auth, permissions, roles, RLS, policy, approval, tool/model routing, secrets, PII, vector namespace, storage, billing, support ou dados de cliente.
- Antes de expor dados a agente, modelo, tool externa, projection ou frontend.

## 9.3 Quando nao usar

- Para reduzir seguranca por conveniencia de MVP.
- Para permitir bypass sem registro e approval.
- Para fazer policy hardcoded em controller como fonte de verdade.

## 9.4 Entradas minimas

- Ator, acao, recurso e contexto.
- Classificacao do dado.
- Tenant/project scope.
- Policies aplicaveis.
- Approval requirement.
- Secret/model/tool exposure.

## 9.5 Saida verificavel

Um security contract com:

- decisao `allow | deny | needs_approval`;
- RBAC+ABAC rationale;
- RLS e tenant isolation checks;
- allowed tools/model constraints;
- secret handling via vault/secret_ref;
- audit events obrigatorios;
- incident/fail-closed behavior.

## 9.6 Guardrails

- Ausencia de policy equivale a deny.
- Policy engine e unico arbitro; agente nao altera policyRegistry.
- PII/confidential nao entra em context pack/model call sem necessidade, mascara e policy.
- Retry on deny nao e permitido.
- Qualquer cross-tenant attempt gera audit/incident P0.

# 10. Skill 5 - ckos-event-runtime-contract

## 10.1 Funcao

Garantir que runtime, workflows, agents, projections e rollback sigam contrato event-sourced/CQRS do CKOS.

## 10.2 Quando usar

- Ao criar fluxo, worker, run, state machine, projection, event handler, replay, rollback, approval pause ou artifact pipeline.
- Ao revisar qualquer implementacao que mude estado operacional.

## 10.3 Quando nao usar

- Para logs observacionais que nao sao fonte causal.
- Para substituir Data Model ou Security.
- Para justificar complexidade de event sourcing onde o trabalho e apenas documental.

## 10.4 Entradas minimas

- Estado que muda.
- Evento que causa a mudanca.
- Actor, correlation_id, causation_id e idempotency key.
- State machine afetada.
- Projection/read model afetado.
- Rollback/compensation esperado.

## 10.5 Saida verificavel

Um runtime event contract com:

- eventos emitidos/consumidos;
- payload minimo;
- causation/correlation;
- idempotency;
- valid state transitions;
- projection update;
- retry/timeout/DLQ;
- compensating events;
- replay evidence.

## 10.6 Guardrails

- UPDATE/DELETE nao substitui evento causal.
- Rollback e compensacao, nao apagamento de historico.
- Workflow engine deve ser stateless; estado vive em event log + projection.
- UI/projection nao escreve source-of-truth.
- Approval pendente pausa run; nao e comentario cosmetico.

# 11. Skill 6 - ckos-qa-gate

## 11.1 Funcao

Validar uma entrega tecnica CKOS antes de release, merge, deploy ou handoff. A QA deve verificar compilacao e testes, mas tambem escopo, canonicidade, seguranca, eventos, banco, custo, observabilidade e release evidence.

## 11.2 Quando usar

- No fim de qualquer implementacao ou patch tecnico.
- Antes de declarar entrega pronta.
- Quando um executor afirmar que "esta funcionando".

## 11.3 Quando nao usar

- Para aprovar trabalho que ainda nao tem artefato verificavel.
- Para substituir Metacognik/Founder em risco alto.
- Para validar so por leitura superficial sem evidencias.

## 11.4 Entradas minimas

- Work Order/implementation brief.
- Lista de arquivos alterados.
- Forbidden scope.
- Comandos de validacao disponiveis.
- Riscos e AQs.
- Evidencia de build/test/manual checks.

## 11.5 Saida verificavel

Um QA gate report com:

- pass/fail/conditional;
- coverage de acceptance criteria;
- scope drift;
- tests/build/lint;
- data/security/event/cost checks;
- rollback readiness;
- release blockers;
- evidence table;
- next action unica.

## 11.6 Guardrails

- Build verde nao aprova se RLS, policy, event log ou audit estiverem quebrados.
- QA nao pode aprovar escopo que o Work Order proibiu.
- QA nao pode esconder risco como "follow-up" se bloqueia seguranca ou replay.
- Se nao houve teste possivel, declarar explicitamente.

# 12. Matriz de Acionamento

| Sinal no trabalho | Skill obrigatoria |
|---|---|
| Pedido tecnico aberto | `ckos-implementation-brief` |
| Backend F1/GATE5 | `ckos-backend-thin-slice` |
| Tabela, migration, seed, indice, enum ou projection | `ckos-data-model-migration` |
| Auth, RLS, policy, secrets, PII, model/tool access | `ckos-policy-rls-security` |
| Evento, workflow, run, state machine, rollback, projection | `ckos-event-runtime-contract` |
| Entrega pronta ou quase pronta | `ckos-qa-gate` |

# 13. Mapeamento Por Executor

| Executor | Uso esperado | Guardrail |
|---|---|---|
| Claude Code | Implementacao, refatoracao, revisao tecnica, patches amplos | Sempre receber `ckos-implementation-brief` e `ckos-qa-gate`; usar guardas especificas conforme superficie. |
| Codex | Codigo, scripts, backend, migrations, testes, validacao local | Deve aplicar data/security/event checks antes de editar e relatar validacao real. |
| Windsurf | Edicao assistida no IDE, navegacao de repo, implementacao incremental | Deve seguir file impact map e nao expandir escopo por sugestao contextual do IDE. |
| Antigravity | UI/UX/prototipos visuais | Fora deste P0 pack salvo quando um brief explicitar que e design study isolado. |

# 14. Relacao Com Skills Ja Criadas

| Skill existente | Papel no trilho |
|---|---|
| `project-intake` | Origina projeto governado. |
| `briefing-builder` | Converte contexto solto em briefing. |
| `document-ingestion` / `note-normalizer` | Preparam conhecimento para contexto. |
| `context-pack-builder` | Monta contexto minimo antes de execucao. |
| `work-order-draft` | Cria envelope governado. |
| `risk-gap-review` | Audita riscos antes/depois. |
| `checkout-release` | Fecha entrega com evidencia e limites. |

As 6 skills P0 entram entre `work-order-draft` e `checkout-release`.

# 15. Arquitetura Dos Futuros SKILL.md

Ao criar os arquivos instalaveis:

```txt
C:\Users\GustavoBxx\.codex\skills\ckos-implementation-brief\SKILL.md
C:\Users\GustavoBxx\.codex\skills\ckos-backend-thin-slice\SKILL.md
C:\Users\GustavoBxx\.codex\skills\ckos-data-model-migration\SKILL.md
C:\Users\GustavoBxx\.codex\skills\ckos-policy-rls-security\SKILL.md
C:\Users\GustavoBxx\.codex\skills\ckos-event-runtime-contract\SKILL.md
C:\Users\GustavoBxx\.codex\skills\ckos-qa-gate\SKILL.md
```

Cada pasta deve conter apenas:

```txt
SKILL.md
agents/openai.yaml
references/   # somente se necessario
```

Nao criar README, changelog, guia de instalacao ou documentacao auxiliar redundante.

# 16. Referencias Sugeridas Por Skill

| Skill | Referencias provaveis |
|---|---|
| `ckos-implementation-brief` | Doc 06, Doc 07, Doc 08, Doc 09, Doc 27 |
| `ckos-backend-thin-slice` | Doc 10, Doc 11, Doc 12, Doc 13, `03_BACKEND_MVP_THIN_SLICE_PLAN.md` |
| `ckos-data-model-migration` | Doc 11, Doc 12, Doc 13 |
| `ckos-policy-rls-security` | Doc 12, Doc 10, Doc 11, Doc 13 |
| `ckos-event-runtime-contract` | Doc 10, Doc 11, Doc 13 |
| `ckos-qa-gate` | Doc 06, Doc 09, Doc 10, Doc 11, Doc 12, Doc 13, Work Order/Release docs |

Ao criar as skills, preferir referencia compacta com anchors e checks, nao copia integral dos docs.

# 17. Criterios de Pronto do Pack

O P0 Dev Hardening Skill Pack esta pronto quando:

- as 6 skills existem em `.codex/skills`;
- cada skill tem trigger claro no `description`;
- cada skill tem `when_to_use` e `when_not_to_use`;
- cada skill produz output verificavel;
- cada skill tem criterios de reprovacao;
- `agents/openai.yaml` existe para cada pasta;
- nenhum `SKILL.md` vira copia longa dos docs canonicos;
- `ckos-qa-gate` consegue revisar saidas das outras 5;
- a cadeia completa funciona: Work Order -> implementation brief -> guardas -> QA -> checkout release.

# 18. Criterios de Reprovacao

O pack deve ser reprovado se:

- alguma skill depender de prompt generico;
- alguma skill permitir backend/UI/API/migration sem gate;
- alguma skill misturar estudo com canonico;
- alguma skill autorizar schema nao previsto sem AQ;
- alguma skill tratar security como checklist opcional;
- `ckos-qa-gate` aprovar sem evidencia;
- as skills duplicarem textos canonicos em vez de carregar procedimentos curtos.

# 19. Architecture Questions

| ID | Pergunta | Impacto |
|---|---|---|
| AQ-P0-DEVSKILL-01 | O Doc 06 deve receber patch canonico registrando essas 6 skills depois que os `SKILL.md` forem validados? | Evita divergencia entre skill local e registry canonico. |
| AQ-P0-DEVSKILL-02 | `ckos-backend-thin-slice` deve ser temporaria para GATE5/F1 ou permanente como skill de backend CKOS? | Define manutencao futura. |
| AQ-P0-DEVSKILL-03 | O `ckos-qa-gate` deve acionar subchecks obrigatorios das outras skills automaticamente quando detectar data/security/event scope? | Aumenta robustez, mas pode elevar custo/contexto. |
| AQ-P0-DEVSKILL-04 | Claude Code, Codex e Windsurf terao prompts/handoffs separados ou um brief executor-agnostico com adaptadores? | Impacta o futuro `ckos-executor-handoff`. |

# 20. Proximo Passo

Criar os 6 `SKILL.md` e `agents/openai.yaml` a partir desta arquitetura, em lote unico ou em dois lotes:

```txt
Lote A: implementation-brief, qa-gate
Lote B: backend-thin-slice, data-model-migration, policy-rls-security, event-runtime-contract
```

Recomendacao: criar em lote unico, porque as skills se validam como cadeia.
