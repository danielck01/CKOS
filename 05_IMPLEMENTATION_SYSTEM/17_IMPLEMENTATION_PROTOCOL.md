---
title: 17 — Implementation Protocol
file: 17_IMPLEMENTATION_PROTOCOL.md
system_id: implementation_protocol
phase: 05_IMPLEMENTATION_SYSTEM
category: implementation_system
version: 1.2.1
status: draft
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - founder
  - technical
  - metacognik
approval_required:
  - founder
  - technical
  - metacognik
inputs: >
  Runtime Architecture (10 v1.1.1); Data Model (11 v1.2.0);
  Security (12 v1.1.0); Evals (13 v1.1.0);
  Project Dashboard (14 v1.2.0); Command Center (15 v1.2.1);
  Node Canvas (16 v1.2.0); Object Model (02); Autonomy (04);
  Workflow Blueprints (07)
outputs: >
  Ordem canônica de implementação; Fases 0–12; Gates A–J;
  MVP P0 scope; Engineering rules; Failure mode catalog;
  Rollback protocol; Approval checkpoints; 7-wave roadmap;
  Required future documents list
related_notes:
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - ../04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md
  - ../04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md
  - ../04_PRODUCT_SYSTEM/16_NODE_CANVAS_ARCHITECTURE.md
  - 18_RESEARCH_PROTOCOL.md
  - 19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md
  - 20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md
  - ../ARCHITECTURE_PATCH_REPORT.md
tags:
  - implementation
  - protocol
  - phases
  - gates
  - mvp
  - engineering-rules
  - rollback
---

> **Frase central:**
> "CKOS implementation must start from runtime foundations, not from UI screens. Every interface, agent, workflow and dashboard must be implemented as a projection of events, registries, policies and state machines."

---

# 1. Propósito

Este documento define o protocolo mestre de implementação do CKOS: a ordem correta, os gates obrigatórios, as regras de engenharia, os pontos de aprovação e as fases que transformam a arquitetura documentada em software funcional sem perda de contexto, retrabalho ou decisões arbitrárias.

A implementação do CKOS **não começa pela UI**. Começa pelos fundamentos de runtime — event bus, schema, políticas, state machines, registries, memória, custo e projections. Qualquer interface, agente, workflow ou dashboard é uma projeção do estado do runtime, não uma fonte de verdade independente.

```
documentação aprovada
  → runtime fundacional (event bus, schema, RLS, policies)
  → agent layer (registry, model_router, eval)
  → projections (CQRS read models, SSE)
  → product layer (Command Center, Node Canvas, Dashboard)
  → QA + Evals + Cost
  → launch
```

Este protocolo é **uma referência operacional**, não um checklist genérico. Cada seção é engineer-ready: contém decisões, dependências, riscos e bloqueios explícitos.

---

# 2. O que é este protocolo

- A ordem canônica de implementação do CKOS do zero ao launch.
- O conjunto de gates que impedem que uma fase comece antes de sua fundação estar sólida.
- As regras de engenharia não-negociáveis derivadas de docs 10–16.
- Os checkpoints de aprovação para decisões críticas.
- O catálogo de modos de falha conhecidos e como evitá-los.
- O roadmap de 7 ondas que mapeia fases à linha do tempo.
- A lista de documentos futuros obrigatórios antes de implementação de domínios ainda não especificados.

---

# 3. O que NÃO é este protocolo

- **Não é um sprint board.** Não substitui gestão de tarefas por ferramenta (Linear, Jira, etc.).
- **Não é código.** Não contém implementação, migration SQL em produção, ou configuração de serviço.
- **Não é um guia de UI/UX.** Decisões visuais pertencem a docs 14–16 e ao Design System.
- **Não é uma substituição dos docs 10–16.** Este documento pressupõe que os docs Runtime e Product System foram lidos e aprovados.
- **Não é autorização para começar.** Cada fase requer gate explícito passado antes do início.
- **Não cobre domínios sem doc próprio aprovado.** ROI Architecture, Feedback System, Support System e Credits/Billing têm gaps documentados em docs 14–16. Implementação desses domínios só começa após doc aprovado.

---

# 4. Princípios de implementação

Os 13 princípios abaixo são derivados diretamente dos docs 10–16. Qualquer decisão de implementação que os viole exige aprovação explícita do Fundador + Metacognik antes de prosseguir.

**1. Runtime-first**
Nenhuma interface, agente ou workflow pode ser implementado antes do runtime que o sustenta. UI sem event bus ativo é protótipo, não produto.

**2. Event-driven sem exceção**
Todo estado muda por evento. Toda ação emite um evento. Nenhuma mutação direta de tabela de domínio sem registro no event store. `INSERT INTO events` antes de qualquer `UPDATE` em tabela de estado.

**3. Projections-only UI**
O frontend lê projeções (CQRS read models). O frontend **nunca recalcula verdade**. O frontend **nunca chama provedores diretamente**. O frontend **nunca expõe tokens, actor_id ou segredos**. Toda chamada de ação passa por `POST /api/...` → runtime.

**4. Policy deny-by-default**
Toda ação passa pela policy engine antes de execução. Permissão é pré-condição, não pós-filtro. Deny é o estado padrão; grant é a exceção explícita documentada.

**5. Gate-locked por fase**
Nenhuma fase começa sem o gate anterior passado e registrado. Gate é verificado, não assumido. A pressão de prazo não substitui um gate.

**6. Documentation-first**
Nenhum componente de produção é implementado sem documento aprovado que o especifica. Código sem doc é protótipo. Doc sem aprovação é rascunho.

**7. Scope-locked**
Implementação não expande escopo silenciosamente. Todo item fora do escopo definido vai para `out_of_scope_recommendation` no backlog. Escopo expandido sem aprovação é defeito de processo.

**8. Audit-everything**
Toda ação de usuário, agente ou sistema produz uma entrada em `audit_log`. Ações sensíveis (aprovações, escalações, mudanças de política) produzem entradas imutáveis com `source_event_id`.

**9. Tenant isolation absoluta**
Todas as tabelas de domínio têm RLS ativo. Toda query de domínio inclui `tenant_id` como pré-condição, não pós-filtro. Cross-tenant vazamento é falha P0.

**10. Agentes não se auto-escalam**
Agentes não podem alterar suas próprias permissões, políticas de aprovação ou critérios de autonomia. Metacognik audita, não aprova ações sensíveis de outros agentes sem checkpoint humano.

**11. Secret isolation**
Tokens, chaves de API e segredos nunca são armazenados em tabelas normais. Apenas `secret_ref` aponta para vault/secret manager. Violation é P0 de segurança.

**12. Rollback-ready**
Toda fase tem um plano de rollback definido antes do início da execução. Migration sem rollback documentado é bloqueio.

**13. Metacognik-supervised**
Todo run de agente em produção produz uma entrada em `evals`. Metacognik audita qualidade, custo, confiança e risco de cada run. Evals sem rastreabilidade são inválidos.

---

# 5. Relação com a documentação CKOS

Este protocolo não duplica os docs 10–16. Pressupõe que foram lidos.

| Doc | Versão | O que fornece para implementação |
|-----|--------|----------------------------------|
| 10 — Runtime Architecture | v1.1.1 | Event bus, canonical flow, SSE/projection engine, agent_router, model_router |
| 11 — Data Model | v1.2.0 | Schema completo, node_edges, ui_projections (13), ROI/Feedback/Support/Billing tables |
| 12 — Security | v1.1.0 | RBAC, ABAC, RLS, secret isolation, tenant model |
| 13 — Evals | v1.1.0 | eval_runner, cost_ledger, Metacognik eval loop, observability |
| 14 — Project Dashboard | v1.2.0 | 10 widgets, presets, profile views, CommandBar, state machines |
| 15 — Command Center | v1.2.1 | Intent Taxonomy (10 famílias), 22 slash commands, intent_router flow |
| 16 — Node Canvas | v1.2.0 | 20 node types, 14 edge types, 16 canvas events, 3 state machines |
| 02 — Object Model | current | Objeto vivo, propriedades universais, hierarquia |
| 04 — Autonomy | current | Approval gates, autonomy levels, escalation protocol |
| 07 — Workflow Blueprints | current | Workflow types, state machines de workflow |

**Dependências não cobertas ainda (sem doc aprovado):**

| Domínio | Status | Bloqueio |
|---------|--------|----------|
| ROI Architecture | gap documentado em docs 11/14/16 | Implementação de ROI nodes/projections bloqueada |
| Feedback System | gap documentado em docs 11/14/16 | Implementação de feedback workflows bloqueada |
| Support System | gap documentado em docs 11/14/16 | Implementação de support tickets bloqueada |
| Credits/Plans/Billing | gap documentado em doc 11 §33 | Implementação de billing bloqueada |
| Whitelabel System | mencionado em docs 14–16 | Implementação de multi-brand bloqueada |
| Collector Registry | mencionado em doc 16 | Implementação de collectors externos bloqueada |

---

# 6. Ordem canônica de implementação

A ordem abaixo é obrigatória. Não é uma sugestão. Implementar uma fase sem a anterior concluída cria acoplamento sem fundação.

```
Fase 0  — Documentation Gate
Fase 1  — Runtime Foundation (DB + event store + RLS + auth)
Fase 2  — Event Bus (event routing, consumer registry)
Fase 3  — Policy Engine (RBAC + ABAC + deny-by-default)
Fase 4  — Workflow Engine (state machines + orchestration)
Fase 5  — Agent Layer (registry + model_router + tool_calls)
Fase 6  — Context, Memory & Evidence (context_packs + memory store)
Fase 7  — Projections & SSE (ui_projection_engine + 13 projections)
Fase 8  — Command Center (intent_router + slash commands + CC UI)
Fase 9  — Node Canvas (canvas rendering + nodes + edges + approvals)
Fase 10 — Project Dashboard (widgets + presets + CommandBar + profile views)
Fase 11 — QA, Evals & Cost Control (eval_runner + cost_ledger + observability)
Fase 12 — Self-Evolving System (feedback loops + Metacognik improvement)
```

**Paralelismo permitido após gate:**
- Fases 2–3 podem rodar em paralelo após Fase 1 concluída.
- Fases 5–6 podem rodar em paralelo após Fase 4 concluída.
- Fases 8–10 podem iniciar em paralelo após Fase 7 concluída (dependência apenas de projections).
- Fase 11 pode ter track de observabilidade rodando desde Fase 5.

---

# 7. Fase 0 — Documentation Gate

**Objetivo:** Garantir que toda a documentação de arquitetura está aprovada, consistente e acessível antes de qualquer linha de código de produção.

**Entrada:** Docs 10–17 em status `draft` ou `review`.

**Saída esperada:** Docs 10–17 em status `approved` pelo Founder + Metacognik + Technical. A base Runtime + Product + Implementation Protocol está pronta para submissão do Gate A — a implementação permanece bloqueada até essa aprovação ser registrada formalmente.

**Checklist obrigatório:**
- [ ] Doc 10 (Runtime Architecture) v1.1.1+ aprovado
- [ ] Doc 11 (Data Model) v1.2.0+ aprovado com patches P11-1 a P11-8
- [ ] Doc 12 (Security) v1.1.0+ aprovado
- [ ] Doc 13 (Evals) v1.1.0+ aprovado
- [ ] Doc 14 (Project Dashboard) v1.2.0+ aprovado
- [ ] Doc 15 (Command Center) v1.2.1+ aprovado
- [ ] Doc 16 (Node Canvas) v1.2.0+ aprovado
- [ ] ARCHITECTURE_PATCH_REPORT v1.2.0+ registrado com todos os patches como APPLIED
- [ ] Todos os gaps documentados como `gap_registered` (não bloqueiam Fase 0, mas devem estar visíveis)

**Bloqueios:**
- Doc em status `draft` sem revisão registrada → bloqueio de gate.
- Inconsistência não resolvida entre dois docs (ex: schema em doc 11 diverge de referência em doc 16) → bloqueio de gate.
- Gap sem registro formal → warning, não bloqueio.

**Gate A:** Documentation Gate — ver §20.

---

# 8. Fase 1 — Runtime Foundation

**Objetivo:** Criar a base de dados, o event store, o sistema de autenticação, RLS e o schema completo conforme doc 11 v1.2.0.

**Entradas:** Doc 11 v1.2.0 (schema completo), Doc 12 v1.1.0 (RLS + auth).

**Componentes:**
- Postgres com RLS ativo em todas as tabelas de domínio
- Tabelas core: `tenants`, `organizations`, `workspaces`, `projects`, `users`, `memberships`
- Event store: `events` (append-only, imutável)
- `audit_log` (imutável, `source_event_id` FK)
- Auth: JWT com `actor_id`, `tenant_id`, `org_id`, `workspace_id` no token
- `secret_refs` (tabela de referências a vault — nunca o segredo em si)
- Migrations versionadas e testadas com rollback documentado

**Regras críticas:**
- RLS DEVE estar ativo antes de qualquer dado de domínio inserido.
- Nenhuma tabela de domínio sem `tenant_id` explicit (não só `org_id`).
- Event store é append-only desde o primeiro dia — nenhum UPDATE ou DELETE em `events`.
- `audit_log` é append-only com constraint de banco.

**Rollback:** Drop schema + restore de snapshot de banco limpo. Migration com `--dry-run` testada antes de qualquer ambiente compartilhado.

**Gate B:** Schema Gate — ver §20.

---

# 9. Fase 2 — Event Bus

**Objetivo:** Implementar o event bus: roteamento de eventos, registro de consumers, dispatch e replay.

**Entradas:** Doc 10 §5.3 (event catalog), Fase 1 concluída.

**Componentes:**
- `event_router`: recebe evento, identifica consumers registrados, despacha
- `consumer_registry`: mapa de `event_type → [handler]`
- Event dispatch: síncrono para eventos críticos (policy check, approval); assíncrono para projections e notificações
- `event_replay`: capacidade de reprocessar eventos a partir de um `sequence_number` ou `timestamp` (necessário para rebuild de projections)
- Dead letter queue para eventos que falharam dispatch após N tentativas

**Eventos mínimos para gate:**

| Evento | Emitido por | Consumido por |
|--------|-------------|---------------|
| `IntentSubmitted` | Command Center | intent_router |
| `WorkflowCreated` | workflow_engine | canvas, projections |
| `NodeCreated` | Runtime | canvas, projections |
| `AgentRunStarted` | agent_router | eval_runner, projections |
| `ApprovalRequested` | approval_gate | projections, notification |

**Rollback:** Consumer registry é stateless — pode ser desregistrado sem impacto em dados. Event store permanece intacto.

**Gate C:** Event Gate — ver §20.

---

# 10. Fase 3 — Policy Engine

**Objetivo:** Implementar policy engine deny-by-default: RBAC + ABAC, permissões como pré-condição de execução.

**Entradas:** Doc 12 §4–§8, Fase 2 concluída.

**Componentes:**
- `policy_engine`: avalia `(actor, action, resource, context)` → `allow | deny | escalate`
- RBAC: `roles_registry` com 8 roles mínimas (viewer, commenter, contributor, project_member, project_lead, admin, billing_admin, super_admin)
- ABAC: `resource_policies` com atributos de contexto (workspace, project, data_classification, time_window)
- `policy_cache`: TTL curto (30s) com invalidação por evento `PolicyUpdated`
- `permission_audit`: toda decisão de policy registrada em `audit_log`

**Regra crítica:** Agentes não podem criar ou alterar policies para si mesmos. `policy_engine` é lido por agentes mas escrito apenas por humanos com role `admin+`.

**Casos de teste obrigatórios antes do gate:**
- Usuário sem role → deny em toda action
- Ação sensível com role correta → allow + audit entry
- Agente tentando escalar própria permissão → deny + alert Metacognik
- Cross-tenant request → deny + audit entry

**Gate D:** Policy Gate — ver §20.

---

# 11. Fase 4 — Workflow Engine

**Objetivo:** Implementar o workflow engine: state machines, workflow blueprints, orchestração de steps.

**Entradas:** Doc 07 (Workflow Blueprints), Doc 10 §5.5–§5.6, Fase 3 concluída.

**Componentes:**
- `workflow_engine`: cria, avança e finaliza workflow runs
- `state_machine_registry`: mapa de `workflow_type → state_machine_definition`
- `workflow_runs` table (com `status` gerido por state machine, não por UPDATE livre)
- `workflow_steps` com `depends_on`, `assigned_to_agent`, `approval_required`
- State machine de workflow (doc 16 §9): `created → planned → queued → running → waiting_* → completed | failed | cancelled | rolled_back`
- Transition validada por policy engine antes de aplicada

**Workflows mínimos para gate:**
- Research workflow (intent → collect → evidence → synthesis → artifact)
- Approval workflow (request → pending → approved/rejected → logged)

**Gate E:** Workflow Gate — ver §20.

---

# 12. Fase 5 — Agent Layer e Model Router

**Objetivo:** Implementar o agent registry, o model router, o tool_call system e o eval hook.

**Entradas:** Doc 03 (Agent Operating Model), Doc 10 §5.7–§5.9, Doc 13, Fase 4 concluída.

**Componentes:**
- `agent_registry`: catálogo de agentes com capabilities, permissions_scope, cost_tier, trust_level
- `model_router`: seleciona modelo com base em `(task_type, complexity, cost_budget, latency_requirement)`
- `tool_call_system`: execução de tools com policy check + cost tracking antes de cada call
- `agent_run` lifecycle: `queued → assigned → running → waiting_input | waiting_approval → completed | failed`
- `eval_hook`: todo run de agente dispara eval entry em `evals` (doc 13) ao completar
- `approval_gate`: runs que atingem `autonomy_threshold` param pausam e emitem `ApprovalRequested`

**Regras críticas:**
- Agente só pode chamar tools listadas em seu `capabilities` no registry.
- Model router considera `cost_budget` do projeto — se esgotado, run é pausado, não cancelado silenciosamente.
- `secret_ref` resolvido pelo runtime, nunca passado para o agente como string plain.

**Manus (nota de posicionamento):**
Manus é uma ferramenta externa temporária de bootstrap de pesquisa. Não é infraestrutura CKOS. Não é um agente registrado no `agent_registry` de produção. Tarefas de pesquisa no período de bootstrap usam Manus via protocolo doc 18 (Research Protocol for Manus). A substituição gradual segue a direção: Perplexity/OpenRouter (LLM search), Apify (web crawl), PubMed connectors (domain research), RAG privado (base de conhecimento interna), collectors especializados por vertical.

**Gate F:** Agent Gate — ver §20.

---

# 13. Fase 6 — Context, Memory e Evidence

**Objetivo:** Implementar context_pack_builder, memory store e evidence system.

**Entradas:** Doc 05 (Memory & Context Architecture), Doc 11 §12–§14, Fase 5 concluída.

**Componentes:**
- `context_pack_builder`: agrega `project_state`, `recent_events`, `agent_history`, `user_preferences`, `relevant_memory` em um pack estruturado para cada agent run
- Memory store: `memory_items` com tipos (short/medium/long/permanent), `tenant_id` isolado, TTL por tipo
- `evidence_items`: registros de evidência linkados a nodes via `node_edges` (edge_type `evidence`)
- `hypothesis_tracker`: hipóteses com `confidence_score`, `evidence_links`, `contradictions`
- Vector store: embeddings com `namespace = tenant_id + workspace_id` como **pré-condição** de busca (nunca pós-filtro)
- `relevance_scorer`: ranking de itens de memória/evidência por proximidade semântica e freshness

**Regra crítica de vector search:**
```
CORRETO:   WHERE namespace = '{tenant_id}:{workspace_id}' AND embedding <-> query < threshold
INCORRETO: embedding <-> query < threshold [sem namespace] → resultado filtrado depois
```
Busca sem namespace como pré-condição é P0 de isolamento de tenant.

**Gate F continua válido** (agent layer + context juntos formam o "agent foundation").

---

# 14. Fase 7 — Projections e SSE

**Objetivo:** Implementar o ui_projection_engine, as 13 projections e o sistema de SSE/polling.

**Entradas:** Doc 10 §5.12 (SSE e Polling, adicionado por P10-1), Doc 11 §21 (13 projections), Fase 6 concluída.

**Componentes:**
- `ui_projection_engine`: subscribe a eventos → recalcula projections afetadas → push via SSE ou marca como stale
- 13 projections (ver doc 11 §21):
  - SSE (push imediato): `project_pulse`, `agent_activity`, `node_health`, `decision_queue`, `approval`, `canvas_graph`, `command_center_context`
  - Polling (intervalo): `cost_credit` (60s), `roi_snapshot` (60s), `feedback_loop` (30s), `support_friction` (120s), `artifact_feed` (30s), `risk_gap_evidence` (30s)
- Permission filtering: toda projection é filtrada por `(user, tenant, project)` **antes** de ser enviada
- Staleness tracking: `is_stale` + `last_updated_at` expostos ao frontend — nunca silenciados
- `projection_rebuild`: job que reconstrói projection do zero a partir do event log (necessário após rollback ou migration)

**Projection states (6):**
`projection_created → projection_updated → projection_stale → projection_permission_filtered → projection_failed → projection_rebuilt`

**Regra crítica:** SSE stream é sempre scoped a `project_id + user_id`. Não existe broadcast de projection cross-project.

**Gate G:** Projection Gate — ver §20.

---

# 15. Fase 8 — Command Center

**Objetivo:** Implementar o intent_router, os slash commands, a UI do Command Center e o fluxo completo de intenção.

**Entradas:** Doc 15 v1.2.1 (Intent Taxonomy, 22 slash commands, §5.3–§5.6), Fase 7 concluída.

**Componentes:**
- `intent_router`: parseia input → identifica `intent_type` (10 famílias, ver doc 15 §5.3) → seleciona handler
- `intent_parser`: extrai entidades, contexto e confidence do texto livre
- Command Center UI: input bar + modo conversacional + slash commands + menções (@node, @agent, @workflow)
- 22 slash commands MVP (ver doc 15 §5.4): `/brief /task /status /agent /decision /roi /feedback /support /credits /audit /diagnosis /competitors /workflow /artifact /cost /memory /evidence /replay /admin` + base
- `command_history` table (P11-2 de doc 11): registra comandos com `intent_type`, `resolved_at`, `context_snapshot`
- Resposta estruturada: toda resposta do Command Center referencia `source_projection` ou `source_event`

**Fluxo canônico (doc 10 §5.2):**
```
User input
  → Command Center
  → IntentSubmitted (event)
  → intent_router
  → context_pack_builder
  → policy_engine
  → workflow_engine (se necessário)
  → agent_router
  → model_router
  → approval_gate (se threshold atingido)
  → eval_runner / Metacognik
  → ui_projection_engine
  → SSE → UI update
```

**Gate H (parcial):** Product Gate requer CC + Canvas + Dashboard. CC é o primeiro dos três.

---

# 16. Fase 9 — Node Canvas

**Objetivo:** Implementar a superfície visual do Node Canvas: renderização de nodes, edges, state machines, approval layer e agent activity layer.

**Entradas:** Doc 16 v1.2.0, Fase 7 concluída, Fase 8 parcialmente concluída.

**Componentes:**
- Canvas rendering: viewport livre, clusters por workflow, zoom/pan
- `node_renderer`: exibe node com `status`, `state_machine`, `approval_status`, `confidence_score`, `cost_estimate`, risk badges
- `edge_renderer`: 14 tipos de edge (doc 16 §7) com visual diferenciado por `edge_type`
- Side panel: evidências, hipóteses, agent activity, approval history, cost estimate
- Agent activity layer: agentes no canvas com estado `working | suggested | blocked | awaiting_approval | audited`
- Approval layer: nodes com `approval_status = pending` destacados com visual de urgência
- State machine display: transições visíveis e atuais para cada node
- `canvas_graph` projection (SSE) como fonte única de verdade do estado do canvas

**Regra crítica:** Node Canvas **não escreve diretamente** no banco. Toda ação do canvas emite um evento → runtime processa → projection atualiza → canvas re-renderiza. Canvas é superfície, não fonte de verdade.

**Node creation flow:**
```
Usuário cria node no canvas
  → NodeCreateRequested (canvas event)
  → intent_router
  → policy_engine (permission check)
  → workflow_engine (node lifecycle)
  → NodeCreated (event store)
  → canvas_graph projection update
  → SSE → canvas re-renderiza com novo node
```

**Gate H (continua).**

---

# 17. Fase 10 — Project Dashboard

**Objetivo:** Implementar os 10 widgets obrigatórios, presets, profile views, CommandBar e sistema de personalização do Project Dashboard.

**Entradas:** Doc 14 v1.2.0, Fases 7–9 concluídas (projections e Product Layer ativas).

**Componentes:**
- 10 widgets obrigatórios (doc 14 §9.2):
  1. Project Pulse (SSE: `project_pulse`)
  2. What Needs Decision (SSE: `decision_queue`)
  3. AI Activity Monitor (SSE: `agent_activity`)
  4. Node Health Overview (SSE: `node_health`)
  5. ROI Snapshot (polling 60s: `roi_snapshot`)
  6. Cost & Credits (polling 60s: `cost_credit`)
  7. Feedback Loop (polling 30s: `feedback_loop`)
  8. Support & Friction (polling 120s: `support_friction`)
  9. Artifacts Generated (polling 30s: `artifact_feed`)
  10. Risk/Gap/Evidence Monitor (polling 30s: `risk_gap_evidence`)
- `dashboard_preferences` table (doc 11 §34): layout por `user_id + project_id`, `hidden_widgets` não pode incluir `fixed_required`
- 8 presets (doc 14 §24): Executive, Creative, Operations, Financial, Client, Founder, Support, AI Activity
- 4 profile views: Stakeholder, Client, Admin, Founder
- CommandBar: 24 intents de exemplo, flow idêntico ao Command Center (doc 14 §25)
- `project_activity_feed` (doc 11 §35): timeline append-only de eventos do projeto

**Regra crítica:** Dashboard **nunca recalcula** dados de widget. Lê exclusivamente das projections definidas em doc 11 §21. Widget que precisa de dado não coberto por projection existente → registrar como patch sugerido antes de implementar nova projection.

**Gate H:** Product Gate = CC + Canvas + Dashboard funcionais. Ver §20.

---

# 18. Fase 11 — QA, Evals e Cost Control

**Objetivo:** Garantir que todos os P0 paths passam por eval, que o cost ledger está operacional e que observabilidade está instrumentada.

**Entradas:** Doc 13 v1.1.0, Fase 10 concluída (produto básico operacional).

**Componentes:**
- `eval_runner`: executa eval em todo agent run, armazena resultado em `evals` table
- `cost_ledger`: registra custo de token, tool e operação por `(agent_run, project, org, tenant)`
- Metacognik: audita evals com baixo score, sinaliza runs com custo anômalo, sugere melhoria
- Observability stack: logs estruturados com `trace_id`, `span_id`, `event_id` para correlação
- `quota_policies` (doc 11 §33): limites de uso por plano, validados antes de cada run
- Alertas: custo acima de threshold → `CostThresholdExceeded` event → notificação + pausa de runs não-críticos
- QA visual: smoke tests para P0 user paths (intent → output visible no dashboard)

**Gate I:** QA Gate — ver §20.

---

# 19. Fase 12 — Self-Evolving System

**Objetivo:** Ativar os loops de melhoria: feedback de usuário → Metacognik → melhoria de workflows, prompts e policies.

**Entradas:** Doc 25 (Self-Evolving System Architecture), Fase 11 concluída.

**Componentes:**
- `feedback_loop_engine`: processa `feedback_items` → identifica padrões → sugere melhoria a Metacognik
- Metacognik improvement cycle: review de evals com baixo score → proposta de refinamento → Founder approval → deploy de melhoria
- Prompt evolution: prompts em `prompt_library` versionados, melhorias rastreadas como eventos
- Workflow evolution: novos blueprints sugeridos por Metacognik com base em run history
- `memory_consolidation`: Metacognik consolida memória de longo prazo periodicamente

**Restrição absoluta:** Metacognik pode **sugerir** melhorias. Toda mudança em policy, prompt de produção ou workflow blueprint requer aprovação humana explícita (Founder ou Technical, dependendo do nível). Self-evolution não significa self-deployment.

**Gate J:** Launch Gate — ver §20.

---

# 20. Gates de implementação (A–J)

Gates são verificações formais que determinam se a fase anterior está sólida o suficiente para a próxima começar. Não são cerimônias opcionais.

| Gate | Nome | Fase de transição | Verificador |
|------|------|-------------------|-------------|
| A | Documentation Gate | → Fase 1 | Founder + Metacognik + Technical |
| B | Schema Gate | → Fase 2 | Technical + PMO_CKOS |
| C | Event Gate | → Fase 3 | Technical + Metacognik |
| D | Policy Gate | → Fase 4 | Founder + Technical |
| E | Workflow Gate | → Fase 5 | PMO_CKOS + Technical |
| F | Agent Gate | → Fases 7 | Technical + Metacognik |
| G | Projection Gate | → Fases 8–10 | Technical + PMO_CKOS |
| H | Product Gate | → Fase 11 | Founder + PMO_CKOS + QA Lead |
| I | QA Gate | → Fase 12 | Founder + QA Lead + Metacognik |
| J | Launch Gate | → Produção | Founder (obrigatório) + todos |

**Critérios de gate por tipo:**

**Gate A (Documentation):**

> O Gate A pode ser submetido para aprovação formal. A implementação continua bloqueada até aprovação registrada por Founder + Technical + Metacognik. Gate A aprovado não autoriza implementação automática — autoriza o início da Fase 1 sob supervisão formal dos revisores.

- Docs 10–17 em status `approved` (docs 10–16 Runtime + Product; doc 17 Implementation Protocol)
- ARCHITECTURE_PATCH_REPORT com todos os patches registrados como APPLIED
- Nenhuma inconsistência não resolvida entre docs
- Todos os gaps registrados formalmente como `gap_registered`
- Docs 18, 19, 20 existentes e referenciados (não precisam de re-aprovação se já aprovados)
- Aprovação registrada formalmente: `approved_by: [founder, technical, metacognik]` + data

**Gate B (Schema):**
- Todas as tabelas do doc 11 §1–§29 criadas com migrations testadas
- RLS ativo e testado com user cross-tenant (deve ser bloqueado)
- Rollback de migration executado com sucesso em ambiente de teste
- `events` e `audit_log` com constraints append-only verificadas

**Gate C (Event):**
- 5+ tipos de evento fluindo através do event_router
- Consumer registry com pelo menos 3 consumers ativos
- Event replay testado: rebuild de estado a partir de eventos

**Gate D (Policy):**
- Deny-by-default verificado: usuário sem role não consegue executar nenhuma action
- 4 roles mínimas testadas com ações permitidas e bloqueadas
- Agente não consegue alterar própria permissão
- Cross-tenant deny verificado e logado

**Gate E (Workflow):**
- 2 workflows completos rodando do início ao fim
- State machine transitions validadas por policy (não bypass)
- Approval workflow: request → pending → approved/rejected → audit entry

**Gate F (Agent):**
- 1 agente completando run completo: intake → context → execution → eval → projection update
- Model router selecionando modelo corretamente para 3 task types diferentes
- Custo de run registrado em `cost_ledger`
- Eval entry criada em `evals` após run

**Gate G (Projection):**
- Todas as 13 projections construídas e servindo dados reais
- SSE estabelecido e recebendo updates em tempo real para pelo menos 3 projections SSE
- Permission filtering verificado: user sem permissão não recebe dados de projection restrita
- `is_stale` corretamente exposto quando projection não pôde ser atualizada

**Gate H (Product):**
- Command Center: intent → evento → projection update → response visível
- Node Canvas: node criado via canvas → event → canvas atualiza sem F5
- Project Dashboard: ao menos 5 widgets renderizando dados reais de projections
- Nenhum widget recalculando dados localmente

**Gate I (QA):**
- Todos os P0 user paths passando em QA (lista em §21 MVP P0)
- Metacognik auditando runs com score abaixo de threshold
- Cost ledger operacional com quota enforcement
- Smoke tests automatizados para P0 paths

**Gate J (Launch):**
- Security audit completo (doc 12)
- Rollback plan documentado e testado para cada componente de produção
- Performance baseline estabelecido
- Monitoring + alertas ativos
- Founder: go/no-go explícito

---

# 21. MVP P0 — Escopo mínimo viável

MVP P0 é o conjunto mínimo que torna o CKOS operacional como produto: um projeto pode ser criado, comandos emitidos, agentes rodando, outputs visíveis e aprovações funcionando.

**Tabelas P0 (subset de doc 11):**
```
tenants, organizations, workspaces, projects, users, memberships
events (append-only)
audit_log (append-only)
nodes (campos essenciais: id, type, title, status, project_id, tenant_id)
node_edges (schema completo de doc 11 §10 — incluso no P0)
workflows, workflow_runs, workflow_steps
agents_registry, agent_runs
approvals
evals
cost_ledger
context_packs
memory_items
artifact_items
project_activity_feed (doc 11 §35)
dashboard_preferences (doc 11 §34)
command_history (doc 11 via P11-2)
ui_projections (13 read models)
```

**Intents P0 (subset de doc 15 §5.3):**
- `/brief` — cria briefing node e inicia contexto de projeto
- `/task` — cria task node
- `/status` — consulta project_pulse projection
- `/agent` — agenda agent run
- `/decision` — registra decision node + emite ApprovalRequested
- `/diagnosis` — dispara workflow de diagnosis estratégico

**Widgets P0 (subset de doc 14 §9.2):**
- Project Pulse (obrigatório, SSE)
- What Needs Decision (obrigatório, SSE)
- AI Activity Monitor (obrigatório, SSE)
- Node Health Overview (obrigatório, SSE)
- Cost & Credits (obrigatório, polling 60s)

**Node types P0 (subset de doc 16 §5):**
- Strategy, Briefing, Research, Task, Workflow, Agent, Decision, Approval

**Agentes P0:**
- Cognik (principal executor de tarefas)
- Metacognik (eval + auditoria)
- PMO_CKOS (orchestração de implementação)

**User paths P0 (devem passar no Gate I):**
1. Usuário envia `/brief` → briefing node criado → Project Pulse atualiza
2. Usuário envia `/task` → task node criado → Node Canvas exibe
3. Agente executa run → eval gerada → cost registrado → AI Activity atualiza
4. Ação atinge approval threshold → ApprovalRequested → Decision Queue aparece → usuário aprova/rejeita
5. Usuário abre Node Canvas → vê nodes ativos → conecta dois nodes → edge criada → canvas_graph atualiza

---

# 22. Explicitamente fora do MVP P0

Estes itens não são implementados no P0. Qualquer implementação antes do doc aprovado de seu domínio é **bloqueada**.

| Domínio | Status | Doc necessário antes de implementar |
|---------|--------|--------------------------------------|
| ROI Tracking completo | gap registrado | `21_ROI_ARCHITECTURE.md` |
| Feedback System | gap registrado | `22_FEEDBACK_SYSTEM_ARCHITECTURE.md` |
| Support System | gap registrado | `23_SUPPORT_SYSTEM_ARCHITECTURE.md` |
| Credits/Plans/Billing | gap registrado | `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md` |
| Whitelabel multi-brand | mencionado | `25_WHITELABEL_SYSTEM.md` |
| Collector Registry | mencionado | `26_COLLECTOR_REGISTRY.md` |
| Self-evolving automático | Fase 12 | Após Gates I–J |
| Campaign nodes | P0+ | After Feedback + ROI |
| Persona/Brand nodes | P0+ | After Whitelabel doc |
| Mobile app | Fase futura | After Product Gate estável |
| API pública externa | Fase futura | After Security audit completo |
| Marketplace de agentes | Fase futura | After Agent Layer maduro |

---

# 23. Regras de engenharia

Estas regras são derivadas diretamente dos docs 10–16 e das restrições absolutas do projeto. São não-negociáveis na ausência de aprovação explícita do Fundador.

**R1 — Event before state:**
Toda mudança de estado começa com `INSERT INTO events`. Nunca `UPDATE` direto em tabela de domínio sem evento correspondente.

**R2 — Projection read-only:**
Frontend lê apenas das 13 projections de doc 11 §21. Nunca acessa tabelas de domínio diretamente. Nunca recalcula estado localmente.

**R3 — No direct provider call from frontend:**
Frontend nunca chama OpenAI, Anthropic, Perplexity ou qualquer provedor diretamente. Toda chamada de IA vai para `POST /api/intent` ou `POST /api/collectors/run` → runtime.

**R4 — No token in DB:**
`secret_refs` apenas. Nenhum token, chave de API ou segredo em tabelas normais. Violation é P0 de segurança imediata.

**R5 — RLS everywhere:**
Toda tabela de domínio tem RLS ativo. `tenant_id` como pré-condição, não pós-filtro. Novo table sem RLS → bloqueio de merge.

**R6 — Vector search namespace-first:**
Busca semântica sempre tem `namespace = tenant_id + workspace_id` como `WHERE` clause antes do cálculo de distância. Nunca como filtro pós-query.

**R7 — Agent cannot self-escalate:**
Nenhum agente pode criar, alterar ou revogar policies, roles ou approval thresholds que afetem ele mesmo. Tentativa é blocked + audit entry + alert Metacognik.

**R8 — Product System projeta, não inventa:**
Docs 14–16 (Dashboard, Command Center, Canvas) projetam e manipulam objetos do Runtime. Não criam lógica própria fora do Runtime. Se um widget ou comando precisa de lógica que não existe no Runtime, é um patch no Runtime, não um workaround no produto.

**R9 — Scope lock antes de execução:**
Toda sessão de implementação começa com scope lock explícito: o que será implementado, o que não será. Item fora do scope → `out_of_scope_recommendation`, nunca execução silenciosa.

**R10 — Rollback before merge:**
Nenhuma migration ou mudança estrutural de schema vai para merge sem rollback documentado e testado.

**R11 — Metacognik eval em todo agent run:**
Todo run de agente em produção produz entry em `evals`. Run sem eval entry é incompleto, não válido.

**R12 — Cost reserve before execute:**
Antes de qualquer agent run, `credit_reservations` registra custo estimado. Previne saldo negativo em runs concorrentes. Se reserva falha → run não inicia, não é silenciado.

**R13 — Immutable audit trail:**
`audit_log` e `events` são append-only com constraint de banco. Nenhuma aplicação, agente ou migration pode fazer UPDATE ou DELETE nessas tabelas.

---

# 24. Modos de falha e mitigações

Catálogo dos modos de falha conhecidos na implementação de sistemas event-sourced + CQRS como o CKOS. Cada item foi observado em sistemas similares ou é derivado de riscos explícitos nos docs 10–16.

| # | Modo de falha | Sintoma | Mitigação |
|---|---------------|---------|-----------|
| F1 | Implementar UI antes do event bus | Widgets sem dados reais; estado local não sincronizado com backend | Gate B + C obrigatórios antes de Fase 8+ |
| F2 | Frontend recalculando estado | Dados divergem entre usuários; bug impossível de reproduzir | R2: frontend lê apenas projections; teste cross-user |
| F3 | RLS ausente em nova tabela | Cross-tenant data leak | R5 + code review com checklist de RLS |
| F4 | Vector search sem namespace | Usuário A vê dados de Tenant B em busca semântica | R6 + teste de isolamento de tenant em todo vetor query |
| F5 | Agente auto-escalando permissão | Agente executa ações fora de seu scope autorizado | R7 + Gate D + Metacognik alert |
| F6 | Token em tabela normal | Vazamento de credencial via SQL injection ou log | R4 + scan de segredo antes de commit |
| F7 | Manus tratado como infra CKOS | Dependência de ferramenta temporária vira dívida estrutural | Posicionamento formal em doc 18 + roadmap de substituição |
| F8 | Gate pulado sob pressão de prazo | Fase inicia sem fundação sólida → retrabalho maior | Gate com verificador humano obrigatório; gate não é auto-aprovado |
| F9 | Scope silenciosamente expandido | Feature não planejada entra em PR sem revisão | R9 + scope lock em toda sessão |
| F10 | Billing implementado antes do doc | Schema inconsistente com futura arquitetura de créditos | §22: Billing bloqueado até `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md` aprovado |
| F11 | Migration sem rollback | Rollback de emergência impossível ou destrói dados | R10 + Gate B require rollback testado |
| F12 | Projection sem permission filter | Usuário vê dados de projeto que não tem acesso | Pre-condition filter em toda projection; teste com usuário sem permissão |
| F13 | Event replay não testado | Rebuild de projection após falha impossível ou incorreto | Gate C require replay test |
| F14 | Agent run sem eval entry | Runs sem rastreabilidade; custo invisível; qualidade sem baseline | R11 + Gate F require eval entry em todos os test runs |
| F15 | Approval gate bypassado | Ação sensível executada sem revisão humana | R7 + policy engine testa todos os approval_threshold params |
| F16 | Self-evolving ativa sem gate | Agente altera prompt/policy de produção sem aprovação | Fase 12 começa só após Gate I + J; self-evolution = suggest only |
| F17 | dashboard_preferences permitindo ocultar widget fixed_required | Widget obrigatório some da UI | Constraint de banco: `hidden_widgets NOT INTERSECT fixed_required_set` |
| F18 | context_pack com dados de outro tenant | Agente recebe contexto errado; outputs incorretos | `context_pack_builder` sempre filtra por `tenant_id + project_id` |
| F19 | SSE sem scope de project_id | Usuário recebe updates de projeto de outro usuário/projeto | SSE channel key = `project_id:user_id`; never broadcast |
| F20 | Projection rebuilt sem permission recheck | Após rebuild, dados sem filtro de permissão chegam ao cliente | Rebuild sempre aplica permission filter antes de push |

---

# 25. Rollback e simulação

**Princípio:** Toda fase tem rollback definido antes de começar. "Não planejamos precisar" não é rollback plan.

**Camadas de rollback:**

| Camada | Método | Responsável |
|--------|--------|-------------|
| Schema/migration | Migration reversa testada em ambiente de teste | Technical |
| Event store | Event store é append-only — rollback não apaga eventos; aplica compensating events | Technical |
| Projection | Projection rebuild a partir de eventos (event replay) | Technical |
| Agent run | Run cancelado emite `AgentRunCancelled` event; estado reverte via compensating event | PMO_CKOS |
| Feature flag | Feature desativada por flag — sem rollback de código necessário | Technical |
| Release | Tag de release anterior + rollback de migration se houver | Technical + Founder |

**Compensating events:**
Para operações que não podem ser desfeitas (ex: email enviado, webhook disparado), o sistema emite um compensating event que registra a ação compensatória. O estado não volta no tempo — o log registra o que aconteceu e o que foi feito em resposta.

**Simulação antes de produção:**
- Toda fase nova deve ser testada em namespace isolado antes de qualquer ambiente compartilhado
- Testes de dois namespaces concorrentes para verificar isolamento de tenant
- Load test de projections SSE antes de Gate G (verificar que push não degrada com 50+ projetos ativos)

---

# 26. Checkpoint — Aprovação do Fundador

O Fundador é o ponto de aprovação final para decisões que afetam direção de produto, escopo, launch e qualquer mudança estrutural que não pode ser revertida facilmente.

**Quando aprovação do Fundador é obrigatória:**

| Situação | Gate |
|----------|------|
| Início de qualquer implementação de produção | Gate A |
| Mudança de schema que altera contrato de API existente | Gate B |
| Qualquer mudança em RBAC ou approval policies | Gate D |
| Início de implementação de domínio novo (ROI, Billing, etc.) | Pré-implementação |
| Launch de novo agente com autonomy_level > 2 | Gate F |
| Go/no-go para launch de produto | Gate J |
| Qualquer decisão de preço ou plano | Fora de gates |
| Scope expansion maior que 20% do planejado | Qualquer fase |

**Formato de checkpoint:**

```
FOUNDER CHECKPOINT — [Gate/Fase] — [Data]
Decisão: [o que está sendo aprovado]
Escopo aprovado: [lista]
Fora do escopo: [lista]
Riscos registrados: [lista]
Próxima revisão em: [condição ou data]
Aprovado por: [Fundador — assinatura ou registro]
```

---

# 27. Checkpoint — Aprovação Técnica

O Technical Lead verifica que decisões de implementação respeitam os contratos de arquitetura definidos nos docs 10–16 e que gates de engenharia foram efetivamente cumpridos.

**Quando aprovação técnica é obrigatória:**

| Situação | Gate |
|----------|------|
| Schema finalizado antes da Fase 2 | Gate B |
| Event bus rodando antes da Fase 3 | Gate C |
| Policy engine antes da Fase 4 | Gate D |
| Agent layer antes da Fase 7 | Gate F |
| Projections antes do Product Layer | Gate G |
| Security audit antes do launch | Gate J |
| Qualquer mudança em `packages/contracts` equivalente do CKOS | Any |

**Checklist técnico por gate:**
- Schema: RLS ativo, constraints corretas, rollback testado
- Events: event replay funcional, consumer registry documentado
- Policies: deny-by-default verificado com teste negativo
- Projections: permission filter testado com usuário sem acesso

---

# 28. Checkpoint — Revisão Metacognik

Metacognik audita a qualidade técnica, os riscos de agente, a coerência entre docs e a saúde dos evals durante e após implementação.

**Quando revisão Metacognik é obrigatória:**

| Situação | Tipo de revisão |
|----------|-----------------|
| Novo agente adicionado ao registry | Capability audit + permissions check |
| Prompt de produção alterado | Quality + regression eval |
| Novo workflow blueprint criado | Logic consistency + edge case check |
| Eval score abaixo de threshold em 3+ runs consecutivos | Root cause analysis |
| Custo de run acima de 2x baseline | Anomaly investigation |
| Agent run com `approval_status = bypassed` | Alert + escala para Fundador |
| Gate F (Agent Layer) | Full agent audit |
| Gate I (QA) | Full eval audit |

**Metacognik não aprova ações críticas sozinho.** Metacognik audita, sinaliza e escalona. Aprovação de ação de alto risco sempre inclui humano.

---

# 29. Roadmap de 7 ondas

As ondas mapeiam as fases de implementação à linha do tempo. As durações são estimativas — gates são as âncoras reais, não calendário.

| Onda | Fases | Duração estimada | Entrega principal |
|------|-------|------------------|-------------------|
| Onda 1 — Fundação | Fase 0 + Fase 1 | Meses 1–2 | Docs aprovados, schema vivo, RLS ativo, event store operacional |
| Onda 2 — Core Runtime | Fases 2–4 | Meses 2–4 | Event bus, policy engine, workflow engine funcionando |
| Onda 3 — Agent Layer | Fases 5–6 | Meses 4–6 | Agentes rodando, context/memory, evals operacionais |
| Onda 4 — Projections | Fase 7 | Meses 6–7 | 13 projections live, SSE ativo, permission filtering verificado |
| Onda 5 — Product Layer | Fases 8–10 | Meses 7–10 | Command Center, Node Canvas, Project Dashboard operacionais (MVP P0) |
| Onda 6 — QA + Domains | Fase 11 + docs 21–24 | Meses 10–14 | QA Gate, custo operacional, docs 21_ROI/22_Feedback/23_Support/24_Billing aprovados e P1 iniciando |
| Onda 7 — Self-Evolving | Fase 12 | Meses 14+ | Feedback loops, Metacognik improvement cycle, launch gate |

**Nota sobre Onda 1:**
A Onda 1 inclui a Fase 0 (Documentation Gate). Significa que o início de qualquer código de produção pressupõe que os docs 10–16 já foram finalizados e aprovados. Este documento (doc 17) faz parte da condição de entrada da Onda 1.

**Paralelismo inter-ondas:**
- A partir da Onda 3, um track de observabilidade pode rodar em paralelo (logs estruturados, cost instrumentation básica).
- A partir da Onda 4, design system e componentes de UI podem ser preparados sem esperar o Product Gate.
- Os docs de Business Systems (21_ROI, 22_Feedback, 23_Support, 24_Billing) devem ser escritos durante as Ondas 3–5 para não bloquear a Onda 6.

---

# 30. Documentos futuros obrigatórios

Estes documentos ainda não existem e bloqueiam implementação dos domínios correspondentes. Devem ser criados e aprovados antes de qualquer trabalho de implementação nesses domínios.

**Sequência canônica do Implementation System (05):**

Os docs 18, 19 e 20 já existem e fazem parte do baseline de implementação atual:

| Doc | Título | Status |
|-----|--------|--------|
| `18_RESEARCH_PROTOCOL.md` | Research Protocol (Manus + futuros collectors) | ✅ Existe |
| `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md` | Claude Codex + Antigravity Execution Protocol | ✅ Existe |
| `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md` | QA and Founder Approval Protocol | ✅ Existe |

Os documentos abaixo ainda não existem. Devem ser escritos e aprovados antes da implementação de seus respectivos domínios:

**Business Systems (docs 21–24) — Alta urgência:**

| # | Doc | Domínio | Urgência | Depende de |
|---|-----|---------|----------|------------|
| 21 | `21_ROI_ARCHITECTURE.md` | Modelo de ROI, tipos, projeções, hipóteses | Alta — bloqueia `/roi` command completo, widget ROI Snapshot, node type ROI/Cost | Docs 11, 14, 15 |
| 22 | `22_FEEDBACK_SYSTEM_ARCHITECTURE.md` | Feedback items, threads, decisions, workflows de melhoria | Alta — bloqueia widget Feedback Loop, node types Feedback | Docs 11, 14 |
| 23 | `23_SUPPORT_SYSTEM_ARCHITECTURE.md` | Support tickets, categorias, SLA, friction signals | Média — bloqueia widget Support & Friction, node types Support | Docs 11, 14 |
| 24 | `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md` | Planos, créditos, wallets, faturamento, quota | Alta — bloqueia `/credits` command completo, billing nodes, credit_reservations | Docs 11, 13 |

**Sistemas complementares (docs 25+) — Média/baixa urgência:**

| # | Doc | Domínio | Urgência | Depende de |
|---|-----|---------|----------|------------|
| 25 | `25_WHITELABEL_SYSTEM.md` | Multi-brand, design tokens, tenant branding, white-label deploy | Média — bloqueia whitelabel features mencionadas em docs 14–16 | Docs 12, 14, 15, 16 |
| 26 | `26_COLLECTOR_REGISTRY.md` | Registry de collectors externos, Apify, PubMed, Perplexity, RAG privado | Média — bloqueia node type Collector completo, pesquisa especializada | Docs 10, 15, 16 |
| 27 | `27_AGENT_MARKETPLACE.md` | Marketplace de agentes, publish/install, versionamento, revenue share | Baixa — Fase 12+ | Docs 03, 05, 10 |
| 28 | `28_NOTIFICATION_SYSTEM.md` | Push, email, in-app, digest, routing de notificações | Média — bloqueia approval notifications completas | Docs 10, 12 |
| 29 | `29_EXTERNAL_API.md` | API pública, auth external, webhooks, rate limiting | Baixa — pós-launch | Docs 10, 12 |

**Responsável por priorização:** PMO_CKOS propõe ordem; Fundador aprova.

**Próximo documento a ser escrito:** `18_RESEARCH_PROTOCOL.md` — revisão e expansão do protocolo existente para cobrir roadmap de collectors além de Manus.

**Documentos 22–25 são os mais urgentes** e devem ser escritos durante as Ondas 3–4 para não bloquear a Onda 6.

---

# 31. Agentes, squads e skills

**Agentes envolvidos neste protocolo:**

| Agente | Papel neste protocolo |
|--------|-----------------------|
| PMO_CKOS | Orchestração de implementação, scope lock, dependências, gates |
| Cognik | Executor principal de tarefas de implementação |
| Metacognik | Auditoria de qualidade, evals, risco de agente, escalação |
| Builder Lead | Coordenação de Builder Subagents |
| Builder Subagents | Implementação técnica por domínio |
| QA Lead | Validação independente de cada gate |
| Founder | Aprovação de gates críticos e decisões de direção |
| Technical | Aprovação de gates de engenharia |

**Skills necessárias:**

```
implementation-planning
scope-locking
event-sourcing
cqrs-projections
rbac-implementation
workflow-engine
agent-registry
cost-tracking
rollback-planning
documentation-update
decision-logging
qa-gate
```

---

# 32. Métricas de sucesso

| Métrica | Definição | Target |
|---------|-----------|--------|
| Gate pass rate | % de gates passados na primeira verificação | > 80% |
| Scope creep rate | % de PRs com itens fora do scope lock original | < 10% |
| Rollback rate | % de fases que precisaram de rollback | < 15% |
| Eval coverage | % de agent runs com entry em `evals` | 100% P0 |
| RLS violations | Cross-tenant data leak incidents | 0 |
| Time from gate to gate | Duração média de cada fase | Baseline da Onda 1 |
| Retrabalho pós-gate | Features reimplementadas após gate passar | < 5% |
| Doc → implementation lag | Dias entre doc aprovado e implementação iniciada | < 30 dias por fase |

---

# 33. Edge cases

| # | Situação | Comportamento esperado |
|---|----------|------------------------|
| EC01 | Doc aprovado mas com gap explícito → implementação começa | Gap bloqueia apenas o domínio do gap, não a fase inteira. Gap registrado em §5 deste doc e no ARCHITECTURE_PATCH_REPORT. |
| EC02 | Gate verificado e passado, mas nova inconsistência descoberta durante implementação | Gate pode ser re-aberto por PMO_CKOS. Implementação pausa até resolução. |
| EC03 | Agente sugere feature fora do scope | Feature vai para `out_of_scope_recommendation`. Não é implementada. Agente não decide escopo. |
| EC04 | Dois agentes escrevem no mesmo `project_id` concorrentemente | Event store serializa via `sequence_number`. Último evento consistente. Nenhum dado perdido — auditável. |
| EC05 | SSE desconecta durante update crítico | Frontend marca projection como `is_stale`. Re-conecta e solicita snapshot. Não perde estado — recalcula da última snapshot. |
| EC06 | Metacognik sinaliza que Cognik tem baixa qualidade em 5 runs consecutivos | Cognik é pausado para novos runs no domínio afetado. PMO_CKOS inicia root cause. Runs existentes completam. |
| EC07 | Migration em produção falha no meio | Rollback automático da migration. `events` e `audit_log` não são afetados (append-only). Estado anterior restaurado. |
| EC08 | Fundador não disponível para gate crítico (Gate J) | Launch bloqueado. Não existe aprovação delegada para Gate J. |
| EC09 | Manus usado para task que deveria ser CKOS nativo | Registrado como bootstrap temporário. Output importado como evidence_item. Não vira dependência estrutural. |
| EC10 | Projection rebuild demora mais de 5 minutos | Projection marcada como `rebuilding`. UI mostra badge "reconstruindo". Dados do snapshot anterior servidos com `is_stale = true`. |
| EC11 | novo node type necessário não está nos 20 definidos | Registrado como patch sugerido para doc 16. Não implementado sem doc aprovado. |
| EC12 | Widget de dashboard precisa de dado não coberto por projection existente | Registrado como patch sugerido para doc 11 §21. Nova projection adicionada ao backlog. Widget não implementado sem projection. |
| EC13 | Agent run excede `cost_budget` do projeto | Run pausado. `CostThresholdExceeded` emitido. Usuário notificado. Run não cancelado silenciosamente — fica em `waiting_approval` para decisão. |
| EC14 | Approval expirada antes de decisão do usuário | `ApprovalExpired` event. Node volta para estado anterior. Audit entry. Notificação ao responsável. |
| EC15 | Dois usuários aprovam/rejeitam o mesmo approval concorrentemente | Primeiro evento ganha. Segundo evento emite `ApprovalConflict` e é logado. Metacognik notificado. |
| EC16 | Frontend tenta POST /api/* sem JWT válido | 401. Nenhum dado é processado. Audit entry com `actor_id = unauthenticated`. |
| EC17 | Agente tenta criar policy para si mesmo | `PolicyMutationDenied` event. Run bloqueado. Metacognik recebe alert. Founder notificado se reincidente. |
| EC18 | Rollback de schema necessário em produção com dados em tabela | Rollback de schema sem perda de dados requer migration compensatória (não DROP). Se não possível: snapshot + restore + replay de events pós-snapshot. |
| EC19 | Domínio sem doc (ex: Billing) começa a ser implementado sem aprovação | PRs bloqueados em code review via checklist. Gate A re-aberto. Implementação removida. |
| EC20 | SSE tem mais de 10.000 conexões simultâneas | Sistema de back-pressure: projections menos críticas passam para polling. SSE mantido apenas para projections P0. Load test requerido antes de Gate G. |
| EC21 | Evidência contraditória encontrada após node já aprovado | `ContradictionDetected` event. Node recebe flag `contradiction_present`. Metacognik sugere revisão. Node não é automaticamente invalidado. |
| EC22 | Processo de self-evolving altera workflow blueprint em produção sem aprovação | Fase 12: Metacognik só **sugere**. Toda alteração de blueprint de produção exige `approved_by: [human_actor]` no event. Deploy automático de blueprint é impossível por design. |

---

# 34. Related notes

- [[10_SYSTEM_RUNTIME_ARCHITECTURE]] v1.1.1 — event bus, canonical flow, SSE/projection streaming
- [[11_DATA_MODEL_AND_PERSISTENCE]] v1.2.0 — schema completo, patches P11-1 a P11-8, 13 projections
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]] v1.1.0 — RBAC, ABAC, RLS, secret isolation
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]] v1.1.0 — eval_runner, cost_ledger, Metacognik
- [[14_PROJECT_DASHBOARD_ARCHITECTURE]] v1.2.0 — 10 widgets, presets, profile views
- [[15_COMMAND_CENTER_ARCHITECTURE]] v1.2.1 — Intent Taxonomy, 22 slash commands
- [[16_NODE_CANVAS_ARCHITECTURE]] v1.2.0 — 20 node types, 14 edge types, 3 state machines
- [[18_RESEARCH_PROTOCOL]] — protocolo de pesquisa externa (Manus + roadmap de collectors)
- [[19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL]] — protocolo de execução de código assistida por IA
- [[20_QA_AND_FOUNDER_APPROVAL_PROTOCOL]] — protocolo de QA e aprovação do Fundador
- [[25_SELF_EVOLVING_SYSTEM_ARCHITECTURE]] — Fase 12 em detalhe
- [[ARCHITECTURE_PATCH_REPORT]] v1.2.0 — registro completo de patches P10-1 + P11-1 a P11-8
- [[QA_DOCUMENTATION_CHECKLIST]] — checklist de qualidade de documentação

---

## Patch 1.2.0 — Reescrita estrutural completa

Doc 17 reescrito de v1.1.0 (16 seções, 164 linhas) para v1.2.0 (34 seções, engineer-ready).

**O que mudou:**
- Estrutura expandida de 16 para 34 seções cobrindo fases 0–12, gates A–J, regras de engenharia, checkpoints, roadmap de 7 ondas e documentos futuros obrigatórios.
- Frase central obrigatória formalizada: "CKOS implementation must start from runtime foundations, not from UI screens."
- Manus explicitamente posicionado como ferramenta de bootstrap temporária (não infra CKOS) na Fase 5 §12.
- 22 edge cases documentados com comportamento esperado.
- 13 regras de engenharia derivadas dos docs 10–16 (não-negociáveis).
- 20 modos de falha catalogados com sintomas e mitigações.
- Rollback e simulação formalizados por camada.
- 3 checkpoints separados: Fundador, Técnico, Metacognik.
- 7-wave roadmap com paralelismo permitido entre ondas.
- Documentos futuros obrigatórios com urgência e dependências.

## Patch 1.2.1 — Micro-patch de governança

**O que mudou:**
- §30 Documentos futuros: sequência canônica corrigida. Docs 18, 19, 20 reconhecidos como existentes. Business Systems renumerados para 21–24 (`21_ROI_ARCHITECTURE`, `22_FEEDBACK_SYSTEM_ARCHITECTURE`, `23_SUPPORT_SYSTEM_ARCHITECTURE`, `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE`). Sistemas complementares ajustados para 25–29.
- §22 Explicitamente fora do P0: referências a doc numbers corrigidas (21–26 em vez de 22–27).
- §24 Failure mode F10: referência ao doc de billing corrigida para `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`.
- §29 Roadmap Onda 6: referência a docs futuros corrigida para numeração 21–24.
- §7 Fase 0: linguagem corrigida — "saída esperada" em vez de "saída", deixando claro que aprovação formal é necessária para liberar implementação.
- §20 Gate A: critério expandido com nota explícita: "O Gate A pode ser submetido para aprovação formal. A implementação continua bloqueada até aprovação registrada por Founder + Technical + Metacognik." Gate A aprovado não é autorização automática de implementação.
- YAML related_notes: doc 18 adicionado; doc 19 renomeado para `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`.
- §34 Related notes: docs 18 e 19 com nomes canônicos corretos.
