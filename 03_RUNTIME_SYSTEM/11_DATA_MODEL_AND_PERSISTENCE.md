---
title: Data Model and Persistence
file: 11_DATA_MODEL_AND_PERSISTENCE.md
phase: 03_RUNTIME_SYSTEM
category: runtime_data
version: 1.2.0
status: draft
owner: PMO_CKOS
responsible_agent: Builder Lead
reviewers:
  - metacognik
  - qa_lead
approval_required:
  - founder
  - technical
  - metacognik
purpose: >
  Definir o modelo de dados executável do CKOS — como objetos, eventos, agentes, workflows,
  memória, RAG, approvals, artifacts, collectors, evals, costs, registries e projections são
  persistidos, versionados, auditados e reproduzidos. É o gêmeo persistido do Object Model (02)
  + Runtime (10). Versão 1.2.0 adiciona suporte completo ao Product System (docs 14–16):
  node_edges, ROI, Feedback, Support, Credits/Billing, ui_projections expandidas,
  dashboard_preferences e project_activity_feed.
inputs: >
  Object Model (02); Memory (05); Transformers (09); Runtime v1.1.1 (10);
  Security (12 v1.1.0); Evals (13 v1.1.0); Command Center (15 v1.2.1);
  Node Canvas (16 v1.2.0); Project Dashboard (14 v1.2.0).
outputs: >
  Estratégia de persistência por store; ~180 tabelas concretas com colunas/FKs/índices/tenant-scope;
  node_edges schema completo; ROI/Feedback/Support/Billing data models; 13 ui_projections com
  trigger/cache/permission spec; dashboard_preferences; project_activity_feed; recorte MVP P0 atualizado.
framework: Postgres (verdade relacional + event store append-only) + Redis (efêmero/filas) + Vector (RAG) + Object Storage (binários) + Projections (CQRS read models).
edge_cases: Evento duplicado; run órfão; tool timeout; collector parcial; vetor cross-tenant; memória stale; projeção atrasada; approval expirado; conflito de versão de artifact; custo acima do limite; migration quebra run antigo; retry duplicando; agente lê sem permissão.
integrations: Supabase/Postgres; Redis; pgvector/vector store; object storage; consumido por 10 (runtime), 12 (security), 13 (evals); projeta para 14-16.
prompts: Não aplicável (documento de arquitetura de dados).
metrics: % runs com trace completo; % outputs com evidence; latência write→projection; retrieval accuracy; cost/run e /projeto; orphan run rate; duplicate event rate; RLS violation attempts; artifact version conflicts.
related_notes:
  - ../01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md
  - ../01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - ../02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md
  - 10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - 12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - 13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - ../04_PRODUCT_SYSTEM/16_NODE_CANVAS_ARCHITECTURE.md
tags: [runtime, data_model, persistence, multi_tenant, event_sourcing, registries, rag, cost_ledger, schema]
---

# Convenção de notação (ler antes das tabelas)

- PK padrão: `id uuid` (UUID v7, ordenável por tempo).
- Colunas de tenant: `org_id`, `workspace_id`, `project_id` (presentes onde o escopo se aplica). **Toda** tabela de domínio carrega pelo menos `org_id`.
- Timestamps: `created_at timestamptz`, `updated_at timestamptz`. Tabelas append-only não têm `updated_at`.
- `[APPEND-ONLY]` = sem UPDATE/DELETE; correção por evento compensatório.
- `[VEC]` = vetorial (vector store). `[REDIS]` = efêmero. `[STORAGE]` = binário em object storage. Sem marca = Postgres relacional.
- `fk→tabela` indica foreign key. `[idx: …]` indica índice sugerido.
- Tipos: `uuid, text, jsonb, int, bigint, numeric, timestamptz, bool, enum`.
- Versionamento: objetos versionáveis usam `version int` + `supersedes_id uuid` (nova versão, nunca overwrite).

---

# 1. Propósito

O doc 11 é o **gêmeo persistido** do Object Model (02) e do Runtime (10): transforma conceitos e mecanismos em tabelas, índices, stores e contratos de persistência. Ele responde, de forma executável:

- quais objetos existem e **onde** são armazenados (Postgres? vetor? cache? storage?);
- como se relacionam (FKs, tabelas de ligação);
- como são versionados (version + supersedes_id);
- como viram **evento** (event store append-only);
- como entram em **memória** (curta/média/longa) e **RAG** (chunks + embeddings);
- como alimentam a **UI** (projection tables);
- como são **auditados** (audit_logs, event log);
- como podem ser **reproduzidos** via run replay.

Critério de aprovação: forte o suficiente para um engenheiro escrever migrations do Supabase **sem inventar arquitetura**.

# 2. Função dentro do CKOS

```txt
02_AI_FIRST_OBJECT_MODEL      = modelo conceitual (o que existe)
10_SYSTEM_RUNTIME_ARCHITECTURE = motor de execução (como roda)
11_DATA_MODEL_AND_PERSISTENCE  = persistência executável (onde mora e como dura)  ← este doc
12_SECURITY                    = depende de 11 (RLS, classificação, tenancy)
13_EVALS                       = depende de 11 (eval tables, cost ledger, traces)
```

Regra: o runtime (10) lê/escreve aqui; a segurança (12) governa o acesso a estas tabelas; os evals (13) leem destas tabelas.

# 3. Persistence Strategy

Roteamento de store — a decisão central. **Nada de blob em Postgres; nada de verdade transacional só em vetor.**

| Store | O que guarda |
|---|---|
| 3.1 **Postgres/Supabase** | entidades relacionais, **event store** (append-only), runs, approvals, decisions, states, registries (config-as-data), cost ledger, evals, metadata de artifact, projections |
| 3.2 **Redis** `[REDIS]` | filas de run, locks, leases, ephemeral run state, rate limits, stream buffer, heartbeats, memória curta (sessão), context cache quente |
| 3.3 **Vector Store** `[VEC]` | embeddings, RAG, memórias semânticas, document_chunks, artifacts indexados; namespace por tenant/projeto |
| 3.4 **Object/File Storage** `[STORAGE]` | imagens, vídeos, PDFs, contratos, decks, prompt packs, screenshots, arquivos de referência; path com `org/workspace/project/` |
| 3.5 **Event Store** | inicialmente tabela Postgres `events` **append-only** e particionada por `aggregate_type`/tempo; todo evento crítico imutável |
| 3.6 **Projection Tables** | tabelas derivadas (CQRS) para UI/dashboard/command center/node canvas; **descartáveis e reconstruíveis** a partir do event store |

# 4. Core Entity Model

Tabelas centrais (tratamento completo, conforme exigido):

### organizations
- **Propósito**: tenant raiz (a CKCompany e, no whitelabel, cada org cliente).
- **Campos**: `id, name text, plan enum, status enum, created_at`.
- **Relações**: 1—N workspaces.
- **Índices**: `[idx: status]`.
- **Owner**: PMO_CKOS. **Tenant_scope**: raiz (define o tenant).
- **Segurança (12)**: nível mais alto de isolamento; tudo abaixo herda `org_id`.

### workspaces
- **Propósito**: container de operação dentro da org; carrega a skin whitelabel.
- **Campos**: `id, org_id fk→organizations, name, theme_tokens jsonb, locale text, status, created_at`.
- **Relações**: N—1 org; 1—N projects, members.
- **Índices**: `[idx: org_id]`.
- **Tenant_scope**: org+workspace. **Segurança**: `theme_tokens` é skin; isolamento é estrutural (RLS), não cosmético.

### projects
- **Propósito**: unidade operacional (branding, campanha, pesquisa, e-commerce…).
- **Campos**: `id, org_id, workspace_id fk, name, type enum, status enum, briefing jsonb, created_by fk→users, created_at, updated_at`.
- **Relações**: N—1 workspace; 1—N nodes, runs, decisions, artifacts, capabilities.
- **Índices**: `[idx: workspace_id, status]`.
- **Tenant_scope**: org+workspace+project. **Segurança**: chave de filtro RLS dominante.

### project_members
- **Propósito**: associa users a projects com papel (RBAC).
- **Campos**: `id, project_id fk, user_id fk, role enum(founder|org_admin|workspace_owner|operator|reviewer|client|agent_service), invited_by, created_at`.
- **Índices**: `[idx: project_id, user_id unique]`.
- **Segurança**: base do RBAC de 12.

### stakeholders
- **Propósito**: pessoas/grupos com papel no projeto (inclui externos/cliente).
- **Campos**: `id, org_id, workspace_id, project_id, role enum, identity_ref, display_name, contact jsonb, created_at`.
- **Índices**: `[idx: project_id]`.
- **Segurança**: `contact` pode conter PII → classificação em 12.

### users
- **Propósito**: identidade autenticável (humano ou `agent_service`).
- **Campos**: `id, org_id, kind enum(human|agent_service), auth_ref, email citext, status, created_at`.
- **Índices**: `[idx: auth_ref unique, email]`.
- **Segurança**: `email` = PII; `agent_service` users recebem token efêmero por run (12 §5.6).

### user_profiles
- **Propósito**: dados não-críticos de perfil/preferência.
- **Campos**: `user_id fk pk, display_name, avatar_uri [STORAGE], preferences jsonb, updated_at`.

### project_settings
- **Propósito**: configuração por projeto (autonomy default, budget, capabilities habilitadas, model policy).
- **Campos**: `project_id fk pk, default_autonomy_level int, budget_profile jsonb, model_policy_ref, enabled_capabilities jsonb, updated_at`.

## 4.1 RBAC Permission Tables *(Patch 1.1.1 — Security Data Support)*

Complementam o enum `role` de `project_members` com papéis dinâmicos, hierárquicos e avaliáveis pelo `policy_engine` (12 §5.3). `project_members.role` continua sendo o mecanismo primário para scoping rápido em projeto; estas tabelas suportam permissões cross-scope, roles custom e avaliação ABAC dinâmica.

### rbac_roles
- **Propósito**: catálogo de papéis disponíveis por org; suporte a papéis custom além dos system_roles (que espelham o enum de `project_members`).
- **Campos**: `id, org_id fk→organizations [RLS], role_key text, display_name, scope_level enum(org|workspace|project|run), description, is_system_role bool, status enum(active|deprecated), created_at`.
- **Relações**: 1—N `role_permissions`; N—N `users` via `user_role_assignments`.
- **Índices**: `[idx: org_id, role_key unique per org]`.
- **Tenant_scope**: org. **Segurança (12 §5.3)**: `is_system_role = true` → imutável em runtime; alteração exige PR aprovado + registro em `registry_change_logs`.

### role_permissions
- **Propósito**: matrix de permissões por papel — o que cada `rbac_role` pode fazer em qual recurso e escopo; base da avaliação RBAC no `policy_engine`.
- **Campos**: `id, role_id fk→rbac_roles, scope_level enum(org|workspace|project|object|field), resource_type text, action text, effect enum(allow|deny), conditions jsonb, priority int`.
- **Relações**: N—1 `rbac_roles`.
- **Índices**: `[idx: role_id, resource_type, action]`.
- **Tenant_scope**: herdado do role (org). **Segurança (12 §5.3)**: carregado em cache Redis para latência de authz ≤ 5 ms; invalidado quando role é modificado.

### user_role_assignments
- **Propósito**: vínculo entre usuário e papel em um escopo específico (org, workspace ou project); suporta expiração e revogação imediata.
- **Campos**: `id, org_id fk [RLS], user_id fk→users, role_id fk→rbac_roles, scope_level enum, scope_ref text, granted_by fk→users, granted_at, expires_at, revoked_at`.
- **Relações**: N—1 `users`; N—1 `rbac_roles`.
- **Índices**: `[idx: org_id, user_id]` `[idx: org_id, scope_ref, role_id]`.
- **Tenant_scope**: org. **Segurança (12 §5.3)**: revogação efetiva na próxima request (`revoked_at` não-null = inativo); `policy_engine` invalida cache na revogação.

# 5. Object Registry Tables

Camada genérica de objetos vivos (complementa as tabelas tipadas; permite tratar qualquer objeto de forma uniforme para versionamento, relações e transições).

```txt
object_types(id, key text unique, schema_ref fk→ (schemaRegistry item), lifecycle_ref fk→state_machines, owner_agent, version) 
objects(id, org_id, workspace_id, project_id, object_type fk→object_types, status, payload jsonb, current_version int, created_by, created_at, updated_at) [idx: project_id, object_type, status]
object_versions(id, object_id fk, version int, payload jsonb, change_reason, created_by, created_at) [APPEND-ONLY] [idx: object_id, version unique]
object_relationships(id, project_id, from_object fk, to_object fk, rel_type enum(depends_on|supports|contradicts|evidences|blocks|triggers|derived_from|approval_for|owned_by|learned_from), weight numeric) [idx: from_object, to_object]
object_state_transitions(id, object_id fk, machine_id, from_state, to_state, event_id fk→events, actor_type, actor_id, occurred_at) [APPEND-ONLY]
```

**Objetos oficiais** (cada um tem tabela tipada própria nas seções seguintes E uma linha-espelho em `objects` para uniformidade de grafo/versão): Project, Workspace, Stakeholder, Node, Workflow, Run, Event, Decision, Approval, Artifact, Memory, Evidence, Hypothesis, Risk, Gap, Insight, CollectorRun, AgentRun, ToolCall, Proposal, Contract, Task.

> Decisão de design: tabelas tipadas são a fonte para queries operacionais e índices; `objects`/`object_versions`/`object_relationships` dão o grafo genérico para o Node Canvas (16) e o versionamento uniforme. As duas se mantêm em sincronia via runtime (10).

# 6. Registry Persistence (config-as-data híbrido)

Estratégia recomendada (**híbrido — Opção C**):
1. **Fonte canônica inicial** = arquivos versionados no repo (`/registries/*.yaml`), revisáveis por PR.
2. **Carregamento** para tabelas de registry no boot/deploy (seed).
3. **Versionamento em banco** (cada item tem histórico).
4. **Audit log** de toda mudança.
5. **Approval** para alteração crítica (agentes, policies, model, approval, cost) via 04/12.

```txt
registries(id, key text unique, kind enum, source enum(file|db|hybrid), canonical_path text, version, status) 
registry_items(id, registry_id fk, item_key text, definition jsonb, current_version int, status enum(draft|active|deprecated|archived), owner, updated_at) [idx: registry_id, item_key unique]
registry_item_versions(id, registry_item_id fk, version int, definition jsonb, change_reason, created_by, created_at) [APPEND-ONLY] [idx: registry_item_id, version unique]
registry_change_logs(id, registry_item_id fk, action enum(create|update|deprecate|activate), before jsonb, after jsonb, actor, approval_id fk→approvals, occurred_at) [APPEND-ONLY]
```

Os **23 registries do doc 10** (`agentRegistry, squadRegistry, skillRegistry, skillChainRegistry, toolRegistry, collectorRegistry, providerRegistry, actorRegistry, promptRegistry, instructionRegistry, transformerRegistry, modelRegistry, workflowRegistry, nodeTypeRegistry, capabilityRegistry, policyRegistry, approvalPolicyRegistry, memoryPolicyRegistry, evalRegistry, schemaRegistry, artifactRegistry, costPolicyRegistry, stateMachineRegistry`) são linhas em `registries`; suas entradas vivem em `registry_items`. Alguns têm também tabela tipada dedicada quando precisam de relações ricas (ex.: `agents`, `nodes/node_types`, `capabilities`, `state_machines`, `collectors`) — nesse caso a tabela tipada é a fonte e o registry item referencia.

# 7. Event Model

Modelo recomendado: **uma tabela `events` append-only particionada** por `aggregate_type` (+ tempo), com **views/streams tipados** para os 12 fluxos lógicos do doc 10 (5.16). Isto evita 12 esquemas divergentes e mantém ordenação/causalidade globais.

```txt
events [APPEND-ONLY] [partição por aggregate_type, range por created_at]
( id uuid(v7),
  event_type text,            -- ex.: node_created, approval_requested, run_completed
  aggregate_type enum(system|agent|workflow|node|approval|artifact|collector|tool|decision|memory|cost|eval),
  aggregate_id uuid,
  project_id, workspace_id, tenant_id,   -- tenant_id = org_id; mantido explícito p/ RLS
  actor_type enum(user|agent|system),
  actor_id uuid,
  causation_id uuid,          -- evento que causou este
  correlation_id uuid,        -- agrupa toda a intenção/run
  idempotency_key text,
  payload jsonb,
  metadata jsonb,
  risk_level enum(low|medium|high),
  created_at timestamptz )
[idx: correlation_id] [idx: aggregate_type, aggregate_id] [idx: project_id, created_at] [idx: idempotency_key unique]
```

Streams lógicos (views sobre `events` filtrando `aggregate_type`/`event_type`): `system_events, agent_events, workflow_events, node_events, approval_events, artifact_events, collector_events, tool_events, decision_events, memory_events, cost_events, eval_events`.

**Regras**: append-only; nunca deletar evento; correção por **evento compensatório**; todo run tem `correlation_id`; todo handoff tem `causation_id`; `idempotency_key` único impede duplicidade (§27).

# 8. Runtime Run Tables

```txt
workflow_runs(id, org_id, workspace_id, project_id, workflow_id fk→workflows, workflow_version, state enum, autonomy_level int, correlation_id, context_pack_id fk→context_packs, started_at, ended_at, timeout_at, cost_usd numeric, approval_status, error_id fk→run_errors) [idx: project_id, state]
agent_runs(id, org_id, workspace_id, project_id, workflow_run_id fk, agent_id fk→agents, agent_version, skill_id, state enum, input jsonb, output jsonb, context_pack_id fk, model_id, confidence numeric, cost_usd, idempotency_key, trace_id, started_at, ended_at, timeout_at, approval_status, error_id) [idx: workflow_run_id] [idx: idempotency_key unique]
tool_calls(id, agent_run_id fk, tool_id fk→ tool registry item, input jsonb, output jsonb, status, cost_usd, latency_ms, started_at, ended_at) [idx: agent_run_id]
collector_runs(id, org_id, workspace_id, project_id, collector_type, actor_id, provider_id, state enum, input jsonb, normalized_count int, cost_usd, started_at, ended_at)  -- ver §12
model_calls(id, agent_run_id fk, model_id, prompt_id, tokens_in int, tokens_out int, cost_usd, latency_ms, fallback_of uuid, created_at) [idx: agent_run_id]
run_steps(id, run_id, run_kind enum(workflow|agent), step_index int, name, status, started_at, ended_at)
run_state_transitions(id, run_id, run_kind, from_state, to_state, event_id fk→events, occurred_at) [APPEND-ONLY]
run_errors(id, run_id, run_kind, code, message, stack jsonb, is_transient bool, occurred_at) [APPEND-ONLY]
run_retries(id, run_id, run_kind, attempt int, reason, backoff_ms, scheduled_at)
run_heartbeats(id, run_id, run_kind, worker_id, lease_until timestamptz, beat_at) [REDIS]  -- detecção de órfão
```

Todo run guarda: `input, context_pack_id, output, status, started_at, ended_at, timeout_at, cost, model, tool (via tool_calls), approval_status, error, trace_id`.

# 9. Agent Persistence

```txt
agents(id, system_id text unique, display_name, mention text, level enum(superagent|agent|subagent), squad_id fk→ squadRegistry item, owner_superagent, autonomy_level int, risk_level enum, approval_policy_ref, model_policy_ref, fallback_model, eval_policy_ref, timeout_policy jsonb, retry_policy jsonb, rate_limit jsonb, data_access_scope jsonb, tenant_scope enum, allowed_object_types jsonb, forbidden_actions jsonb, logging_level enum, status, current_version int)
agent_versions(id, agent_id fk, version int, definition jsonb, change_reason, created_by, created_at) [APPEND-ONLY]
agent_skills(agent_id fk, skill_id fk)            -- N:N
agent_prompts(agent_id fk, prompt_id fk)
agent_tools(agent_id fk, tool_id fk)
agent_collectors(agent_id fk, collector_type)
agent_permissions(id, agent_id fk, scope enum(org|workspace|project|object|field), resource, action, effect enum(allow|deny))  -- alimenta 12
agent_handoffs(id, from_agent fk, to_agent fk, project_id, node_id, reason, context_summary, required_inputs jsonb, expected_output jsonb, risk_level, approval_required, memory_refs jsonb, event_id fk→events, created_at)
agent_outputs(id, agent_run_id fk, schema_id fk→ schemaRegistry, payload jsonb, valid bool, created_at)  -- validado por contrato (5.20)
agent_decisions(id, agent_run_id fk, decision_id fk→decisions, created_at)
agent_context_reads(id, agent_run_id fk, context_pack_id fk, source_type, source_ref, tokens int, created_at)  -- auditoria de RAG/contexto
agent_memory_reads(id, agent_run_id fk, memory_id fk→memories, created_at)
agent_memory_writes(id, agent_run_id fk, memory_id fk→memories, write_type, created_at)
agent_eval_results(id, agent_run_id fk, eval_id fk→evals, score numeric, passed bool, detail jsonb, created_at)  -- base p/ 13
agent_costs(id, agent_run_id fk, cost_usd, tokens_in, tokens_out, tool_cost_usd, created_at)
agent_errors(id, agent_run_id fk, code, message, occurred_at) [APPEND-ONLY]
agent_approval_requests(id, agent_run_id fk, approval_id fk→approvals, created_at)
agent_state_transitions(id, agent_run_id fk, from_state, to_state, event_id fk, occurred_at) [APPEND-ONLY]
```

# 10. Node and Workflow Persistence

```txt
node_types(id, key text unique, schema_ref, lifecycle_ref fk→state_machines, category enum(core|capability|execution|intelligence), owner_agent, version)  -- fonte: nodeTypeRegistry
nodes(
  id uuid pk,
  org_id fk→organizations [RLS],
  workspace_id fk, project_id fk,
  node_type fk→node_types,
  status enum(suggested|draft|pending_approval|active|running|waiting_input|waiting_approval|completed|archived|blocked),
  origin enum(manual|nick_suggested|cognik_generated|metacognik_required|agent_generated|workflow_generated),
  owner_agent fk→agents,
  payload jsonb,
  current_version int,
  created_by fk→users,
  source_event_id fk→events,      -- evento que originou este node (P11-1)
  cost_estimate jsonb,             -- {credits_estimated, credits_consumed, currency} (P11-1)
  created_at, updated_at
) [idx: project_id, node_type, status]
node_versions(id, node_id fk, version int, payload jsonb, change_reason, created_at) [APPEND-ONLY]

-- P11-1: node_edges schema completo (suporta Node Canvas 16 §7)
node_edges(
  id              uuid pk,
  tenant_id       uuid,                  -- = org_id; explícito para RLS e partição
  org_id          fk→organizations [RLS],
  workspace_id    fk→workspaces,
  project_id      fk→projects,
  source_node_id  fk→nodes,             -- nó de origem
  target_node_id  fk→nodes,             -- nó de destino
  edge_type       enum(
                    dependency,          -- A não pode acontecer sem B
                    sequence,            -- A dispara B na sequência
                    evidence,            -- A é evidência de / suporta B
                    risk,                -- A representa risco de B
                    approval,            -- A é o aprovador formal de B
                    handoff,             -- A transfere execução para B
                    cost,                -- A é estimativa de custo de B
                    roi,                 -- A é nó de ROI de B
                    feedback,            -- A é feedback sobre B
                    support,             -- A é ticket de suporte de B
                    artifact,            -- A gera/é artifact de B
                    memory,              -- A é entrada de memória derivada de B
                    collector,           -- A é run de coleta que alimenta B
                    blocked_by           -- A está bloqueado por B
                  ),
  label           text,                  -- descrição legível da relação (opcional)
  direction       enum(directed|bidirectional) default 'directed',
  weight          numeric default 1.0,   -- relevância da relação [0,1]
  status          enum(active|inactive|invalidated) default 'active',
  created_by_type enum(user|agent|system),
  created_by_id   uuid,
  source_event_id fk→events,            -- evento que originou esta edge
  workflow_run_id fk→workflow_runs,      -- workflow que criou esta relação (se aplicável)
  evidence_id     fk→evidence_items,    -- evidência que fundamenta esta edge (se evidence)
  approval_id     fk→approvals,         -- approval associado (se approval)
  metadata        jsonb,                 -- dados extras por edge_type
  created_at      timestamptz,
  updated_at      timestamptz,
  archived_at     timestamptz            -- soft-delete; null = ativa
)
[idx: project_id, source_node_id, target_node_id]
[idx: org_id, edge_type, status]
[idx: source_node_id, edge_type]        -- queries "quais edges saem deste node?"
[idx: target_node_id, edge_type]        -- queries "quais edges chegam neste node?"

node_inputs(id, node_id fk, key, value jsonb, source_ref)
node_outputs(id, node_id fk, key, value jsonb, artifact_id fk→artifacts)
node_states(id, node_id fk, state, since timestamptz)         -- estado corrente projetado
node_events(id, node_id fk, event_id fk→events)               -- liga node ao event store
workflows(id, key text unique, current_version int, owner_agent, status)  -- fonte: workflowRegistry
workflow_versions(id, workflow_id fk, version int, definition jsonb, state_machine_id fk, created_at) [APPEND-ONLY]
workflow_steps(id, workflow_version_id fk, step_index int, kind enum(skill|agent|transformer|approval|collector), ref_id, gate jsonb)
workflow_edges(id, workflow_version_id fk, from_step, to_step, condition jsonb)
workflow_run_links(workflow_run_id fk, node_id fk)            -- quais nodes um run tocou
```

Reforço: Node Canvas (16) **não é UI solta** — cada node é objeto persistido; cada edge tem significado operacional; cada node_type vem do `nodeTypeRegistry`; cada workflow depende de uma state machine (§20).

# 11. Capability System Persistence

```txt
capabilities(id, capability_id text unique, display_name, when_to_activate jsonb, required_inputs jsonb, optional_inputs jsonb, approval_required, cost_profile jsonb, risk_level, current_version int, status)  -- fonte: capabilityRegistry
capability_versions(id, capability_fk, version int, definition jsonb, created_at) [APPEND-ONLY]
project_capabilities(id, project_id fk, capability_fk, state enum(suggested|active|archived), activated_by, activation_event_id fk→events, activated_at) [idx: project_id]
capability_activation_rules(id, capability_fk, rule jsonb, priority int)
capability_nodes(capability_fk, node_type fk)
capability_agents(capability_fk, agent_id fk)
capability_skills(capability_fk, skill_id fk)
capability_tools(capability_fk, tool_id fk)
capability_collectors(capability_fk, collector_type)
capability_dashboards(capability_fk, dashboard_key)           -- projeções sugeridas (14)

-- Patch 1.1.1: capability grants com approval e revogação (12 §5.11)
capability_grants(id, org_id fk [RLS], workspace_id fk, project_id fk,
                  capability_id fk→capabilities,
                  granted_to_type enum(project|workspace|org),
                  granted_to_id uuid,
                  granted_by fk→users, granted_at,
                  expires_at, revoked_at,
                  status enum(active|revoked|expired),
                  approval_ref fk→approvals,
                  metadata jsonb)
[idx: project_id, capability_id, status] [idx: org_id, capability_id, status]
```

Reforço: e-commerce, ads e CRM **não nascem default**. `project_capabilities` começa vazio/`suggested`; ativação exige contexto, briefing, decisão, coleta ou aprovação (registrada em `activation_event_id`).

# 12. Collector Persistence

```txt
collectors(id, collector_type text unique, display_name, provider_id fk→ providerRegistry, default_actor_strategy, normalizer_ref, policy_ref, cost_profile jsonb, status)  -- abstração CKOS
collector_runs(id, org_id, workspace_id, project_id, collector_type fk, actor_id, provider_run_id, state enum(requested|authorized|queued|running|waiting_provider|normalizing|completed|failed|rate_limited|cancelled), input jsonb, started_at, ended_at)
collector_inputs(id, collector_run_id fk, params jsonb)        -- params NÃO sensíveis
collector_outputs(id, collector_run_id fk, raw_ref [STORAGE], record_count int)
collector_normalized_records(id, collector_run_id fk, schema_id fk→schemaRegistry, record jsonb, node_id fk→nodes, evidence_id fk→evidence_items)  -- CollectorNormalizedOutput
collector_provider_runs(id, collector_run_id fk, provider_id, external_run_ref, status, cost_usd)
collector_errors(id, collector_run_id fk, code, message, occurred_at) [APPEND-ONLY]
collector_costs(id, collector_run_id fk, cost_usd, units int, created_at)
```

Separação obrigatória (taxonomia §10.2): **Collector** (abstração CKOS, visível ao produto) ≠ **Actor** (executor técnico interno) ≠ **Provider** (API externa). **Tokens/segredos NUNCA em tabela normal** — vão para secret manager/env seguro; `actorRegistry`/`providerRegistry` guardam apenas `secret_ref`. Detalhe de isolamento em 12.

## 12.1 Secret References *(Patch 1.1.1 — Security Data Support)*

Tabela de ponteiros seguros para credenciais. **Nunca armazena o segredo real** — armazena apenas o caminho no vault externo. Usada por collector actors, integrations, tools e qualquer componente que precise de credencial externa.

```txt
secret_refs(
  id              uuid primary key,
  org_id          fk→organizations [RLS],
  workspace_id    fk→workspaces,
  project_id      fk→projects,
  ref_key         text,               -- identificador semântico (ex.: "meta_ads_api_key")
  vault_path      text,               -- caminho no vault externo (ex.: "vault/ckos/org_123/meta_ads")
  secret_type     enum(api_key|oauth_token|service_account|webhook_secret|database_url|custom),
  owner_type      enum(integration|collector|tool|actor|provider),
  owner_ref       text,               -- id do owner (integration_id, collector_type, etc.)
  status          enum(active|rotating|revoked|expired),
  expires_at      timestamptz,
  last_rotated_at timestamptz,
  created_by      fk→users,
  created_at      timestamptz
)
[idx: org_id, ref_key unique per org]
[idx: owner_type, owner_ref]
[APPEND-ONLY de versões via audit_log — revogação por status=revoked, não DELETE]
```

**Regras de segurança obrigatórias:**
- `vault_path` nunca aparece em response body, log, trace ou event payload — redação automática.
- Toda resolução de `secret_ref` (vault lookup) emite evento `SecretAccessed` → `audit_logs`.
- Toda tentativa de exibir `vault_path` em log é interceptada e substituída por `[SECRET_REF_REDACTED]`.
- Rotação: vault-managed com janela de sobreposição; `last_rotated_at` atualizado; status permanece `active`.
- RLS ativo: admin de um tenant nunca vê `secret_refs` de outro tenant.
- `secret_refs` de projetos revogados transitam para `status=revoked` automaticamente na revogação do projeto.

# 13. Context Pack Persistence

```txt
context_packs(id, org_id, workspace_id, project_id, agent_run_id fk, intent text, active_node_id, workflow_state, permissions_snapshot jsonb, risk_level, budget jsonb, output_schema_id fk, forbidden_actions jsonb, final_token_count int, created_at)
context_sources(id, context_pack_id fk, source_type enum(project|node|workflow|event|memory|rag|instruction), source_ref, included bool, tokens int, priority int)
context_retrieval_logs(id, context_pack_id fk, query text, retriever enum(memory|rag), top_k int, latency_ms, created_at)  -- auditoria de recuperação
context_budget_logs(id, context_pack_id fk, max_tokens int, used_tokens int, excluded_sources jsonb, compression_strategy enum(truncate|summarize|hierarchical))
context_compressions(id, context_pack_id fk, source_ref, original_tokens int, compressed_tokens int, method)
context_snapshots(id, context_pack_id fk, snapshot jsonb [STORAGE-opcional])  -- para run replay (§22)
```

Cada `context_pack` guarda: project context, user intent, active node, workflow state, recent events, relevant memories, RAG results, permissions, budget constraints, output schema, forbidden actions, final token count, sources used/excluded.

# 14. Memory + RAG + Embeddings

```txt
memories(id, org_id, workspace_id, project_id, scope enum(short_term|mid_term|long_term), type, source_object_ref, content text, summary text, confidence numeric, permission_level enum, reliability numeric, freshness_at timestamptz, valid_until timestamptz, created_by, reviewed_by) [idx: project_id, scope]
memory_versions(id, memory_id fk, version int, content, created_at) [APPEND-ONLY]
memory_scopes(id, memory_id fk, scope_kind enum(session|project|workspace|org|brand), scope_ref)
memory_links(id, memory_id fk, related_node fk, related_decision fk, link_type)
memory_write_events(id, memory_id fk, agent_run_id fk, event_id fk→events, write_type, created_at) [APPEND-ONLY]
documents(id, org_id, workspace_id, project_id, kind, title, storage_uri [STORAGE], source_lineage jsonb, classification enum(public|internal|confidential|pii), created_at)
document_chunks(id, document_id fk, chunk_index int, text, token_count int, chunk_strategy enum(fixed|semantic|recursive), metadata jsonb) [idx: document_id]
embeddings [VEC] (id, chunk_id fk→document_chunks | memory_id fk→memories, vector vector(N), model_id, namespace text, org_id, workspace_id, project_id, created_at)  -- namespace + tenant = pré-condição de busca
rag_queries(id, project_id, agent_run_id fk, query text, top_k int, filters jsonb, created_at)
rag_results(id, rag_query_id fk, chunk_id|memory_id, score numeric, rank int, used bool)
retrieval_logs(id, rag_query_id fk, candidates int, returned int, permission_filtered int, latency_ms)
vector_collections(id, namespace text unique, tenant_scope, embedding_model, dims int, created_at)
```

Camadas (05): **short_term** = sessão/run (Redis + memories.scope); **mid_term** = projeto/workspace; **long_term** = organização/brand/knowledge. Definir por entrada: **chunking strategy**, **embedding metadata** (model, dims, namespace), **freshness**, **reliability**, **access scope**, **tenant isolation** (namespace por tenant/projeto), **source lineage**. Hierarquia de confiança (05 §5.5) aplicada na recuperação: dado estruturado/decision > embedding.

# 15. Evidence, Hypothesis, Risk and Gap Persistence

```txt
evidence_items(id, org_id, workspace_id, project_id, content, source_type enum(approved_decision|contract|db_record|user|artifact|retrieved_doc|agent_inference|web|weak), source_owner, source_ref, last_verified_at, expiration_policy jsonb, created_at)
source_reliability_scores(id, evidence_id fk, score numeric, computed_by, computed_at)
source_freshness_scores(id, evidence_id fk, score numeric, computed_at)
hypotheses(id, project_id, statement, status enum(open|supported|refuted|parked), owner_agent, created_by, decision_id fk→decisions, created_at, updated_at) [idx: project_id, status]
hypothesis_evidence_links(id, hypothesis_id fk, evidence_id fk, link_type enum(supports|contradicts), weight numeric)
confidence_scores(id, hypothesis_id fk, score numeric, computed_by, computed_at)
risks(id, project_id, description, severity enum, likelihood enum, status, owner_agent, created_at)
gaps(id, project_id, description, blocks_decision fk→decisions, status, created_at)
insights(id, project_id, content, evidence_refs jsonb, confidence numeric, created_by, created_at)
```

Toda hipótese precisa: evidências (`hypothesis_evidence_links`), confiança (`confidence_scores`), lacuna (`gaps`), origem (`evidence_items.source_*`), data, responsável (`owner_agent`/`created_by`), status, decisão relacionada (`decision_id`).

# 16. Decisions and Approvals

```txt
decisions(id, org_id, workspace_id, project_id, decision_type, context, chosen jsonb, rejected jsonb, decided_by, decided_at, supersedes_id fk→decisions, status) [idx: project_id]
decision_events(id, decision_id fk, event_id fk→events) [APPEND-ONLY]
decision_rights(id, decision_type text, allowed_approvers jsonb, required_approvers jsonb, auto_approval_allowed bool, risk_level, rollback_required bool, audit_required bool)  -- Decision Rights Matrix (10 §5.22)
decision_evidence_links(id, decision_id fk, evidence_id fk, weight numeric)
approvals(id, org_id, workspace_id, project_id, object_type, object_id, action, risk_level, cost_estimate numeric, reversible bool, status enum(requested|approved|rejected|expired|revoked|escalated|auto_approved), approver, decision_note, expires_at, created_at)
approval_requests(id, approval_id fk, requested_by, recommendation, options jsonb, impact jsonb, rollback jsonb, created_at)
approval_events(id, approval_id fk, event_id fk→events) [APPEND-ONLY]
approval_policies(id, policy_key, action_or_risk, required_approvers jsonb, auto_approval_allowed bool)  -- fonte: approvalPolicyRegistry
approval_expirations(id, approval_id fk, expires_at, action_on_expire enum(block|escalate|auto))
approval_escalations(id, approval_id fk, from_role, to_role, reason, escalated_at)
```

Conectado à Decision Rights Matrix (10 §5.22): Nick sugere · Cognik interpreta · Metacognik bloqueia/audita · PMO_CKOS recomenda · Founder aprova estrutural · Cliente aprova escopo/proposta/contrato · QA Lead aprova qualidade técnica.

## 16.1 Audit Log Persistence *(Patch 1.1.2 — Implementation Readiness)*

Tabela append-only de rastreabilidade de segurança, autorização, decisões e ações de agentes. É a fonte de verdade para incident review, compliance e run replay de incidentes. O schema de política dos 14 eventos obrigatórios está em doc 12 §5.16 — esta seção é a materialização de persistência correspondente em doc 11, necessária para que engenheiros escrevam migrations sem inventar arquitetura.

```txt
audit_logs [APPEND-ONLY] [RLS: org_id]
(
  id                uuid primary key (v7),
  tenant_id         uuid,                         -- = org_id; explícito para partição e RLS
  org_id            fk→organizations [RLS],
  workspace_id      fk→workspaces,
  project_id        fk→projects,
  actor_type        enum(user|agent|system|collector|provider),
  actor_id          text,                          -- user_id ou agent system_id
  action            text,                          -- ex.: permission_denied, approval_requested, secret_redacted
  target_type       text,                          -- tipo do recurso afetado (node, artifact, policy, workflow...)
  target_id         text,                          -- id do recurso afetado
  event_id          fk→events,                     -- evento do event store que originou esta entrada
  run_id            uuid,                          -- agent_run_id ou workflow_run_id contextual
  correlation_id    uuid,                          -- agrupa todas as entradas de uma intenção/run
  causation_id      uuid,                          -- evento que causou esta ação
  risk_level        enum(low|medium|high|critical),
  severity          enum(P0|P1|P2|P3|none),        -- alinhado aos 14 security events de doc 12 §5.21
  effect            enum(allow|deny|block|redact|escalate),
  policy_id         uuid,                          -- policyRegistry item_id avaliado
  approval_id       fk→approvals,                  -- approval relacionado, se aplicável
  ip_hash           text,                          -- hash de IP (nunca o IP real — PII constraint)
  user_agent_hash   text,                          -- hash do user agent
  metadata          jsonb,                         -- contexto: role, tenant, risk, data_classification
  redacted_fields   jsonb,                         -- lista de campos redatados (nunca o valor)
  created_at        timestamptz default now()
)
[APPEND-ONLY — sem UPDATE/DELETE; compensação por novo entry com action='correction_of']
[idx: org_id, project_id, created_at]
[idx: org_id, actor_id, action]
[idx: severity, created_at]      -- incident queries por severidade
[idx: correlation_id]            -- reconstrução de cadeia causal
[idx: run_id]                    -- replay de incidente
```

**Regras obrigatórias:**

1. **Append-only**: nenhuma entrada é modificada ou deletada; correção por nova entrada com `action = correction_of`.
2. **Sem segredo real**: `metadata` e `redacted_fields` nunca carregam token, password ou API key — apenas indicação de que o campo foi redatado.
3. **Sem PII sensível sem mascaramento**: dado PII em `metadata` deve ser mascarado (ex.: email → hash; nome → iniciais).
4. **Retenção mínima de 12 meses** (regulatório) — imutáveis; expiração via archiving, nunca DELETE.
5. **RLS force** — aplica mesmo ao superusuário da aplicação; isolamento de tenant é estrutural.

**14 eventos de segurança que obrigatoriamente geram entradas (doc 12 §5.21):**

```txt
P0: TenantBoundaryViolationAttempted · AgentPolicyModificationAttempt · EmergencyBypassActivated
P1: SecretRedacted · PolicyViolationDetected · ApprovalPolicyChanged · VectorNamespaceViolationAttempted
P2: PIIBlockedFromPrompt · ModelPrivacyPolicyViolation · CollectorProviderExposureBlocked
    CapabilityScopeViolation · AgentPermissionDenied
P3: PIIAccessLogged · PermissionDenied
```

**Ações adicionais que geram entradas:**

```txt
PermissionGranted · ApprovalRequested · ApprovalResolved · ApprovalExpired
AgentToolCallExecuted (risk ≥ medium) · CollectorRunAuthorized · ModelCallWithPII
MemoryWriteWithSensitiveData · DecisionRegistered (risk_level ≥ medium)
RoleAssigned · RoleRevoked · CapabilityGranted · CapabilityRevoked
SecretAccessed (vault lookup) · SecretRotated · DataExpired
```

**Relações com outros componentes:**

- `event_id fk→events` — toda entrada de `audit_logs` corresponde a um evento no event store (§7); camadas complementares: `events` = log de execução; `audit_logs` = log de segurança/authz/governança
- `approval_id fk→approvals` — liga autorização ao approval object para auditar se approval foi respeitado (§16)
- `run_id + correlation_id + causation_id` — cadeia causal reconstruível via `run_replays` (§22) sem logging paralelo
- `policy_id` — identifica qual regra do `policyRegistry` foi avaliada; base de auditoria de RBAC (§4.1)
- **doc 12 §5.16** — define o schema de política dos 14 eventos obrigatórios; este §16.1 é a materialização em tabela
- **doc 13 §13** — consome `audit_logs` para security observability, alertas P0–P3 e SLAs de resposta

# 17. Artifact Persistence

```txt
artifacts(id, org_id, workspace_id, project_id, type enum(briefing|diagnostico|proposta|moodboard|prompt_pack|dashboard|relatorio|campanha|contrato|roteiro|brandbook|...), current_version int, status enum(draft|generated|under_review|approved|rejected|published|archived|versioned), owner_agent, produced_by_run fk→ runs, created_at) [idx: project_id, type, status]
artifact_versions(id, artifact_id fk, version int, storage_uri [STORAGE], checksum, supersedes_id, created_at) [APPEND-ONLY]
artifact_source_runs(artifact_id fk, run_id, run_kind)        -- lineage de geração
artifact_approval_status(artifact_id fk, approval_id fk→approvals, status)
artifact_owners(artifact_id fk, owner_type enum(agent|user), owner_id)
artifact_files(id, artifact_version_id fk, storage_uri [STORAGE], mime, size_bytes, checksum)
artifact_events(id, artifact_id fk, event_id fk→events) [APPEND-ONLY]
```

Artifacts versionados; **nunca sobrescritos** (nova `artifact_versions` + `supersedes_id`).

# 18. Cost Ledger

```txt
cost_ledger [APPEND-ONLY] (id, org_id, workspace_id, project_id, scope enum(project|client|agent|workflow|run|model|tool|collector|day|month), scope_ref, cost_usd numeric, tokens int, units int, source_event_id fk→events, occurred_at) [idx: project_id, scope, occurred_at]
run_costs(run_id, run_kind, cost_usd)         -- view materializada sobre cost_ledger
model_costs(model_id, period, cost_usd)
tool_costs(tool_id, period, cost_usd)
collector_costs(collector_type, period, cost_usd)
project_budgets(id, project_id fk, period enum(day|month|total), limit_usd numeric, soft_limit_usd numeric, state enum(within_budget|approaching_limit|blocked_by_cost|needs_approval))
agent_budgets(id, agent_id fk, project_id, period, limit_usd, state)
budget_alerts(id, budget_ref, level enum(approaching|exceeded), threshold numeric, fired_at) [APPEND-ONLY]
```

Custos por: project, client, agent, workflow, run, model, tool, collector, day, month. `cost_ledger` é a fonte append-only; as demais são agregações. Base do Cost Guard (10 §5.23) e do controle de custo de 13.

# 19. Evals Persistence (base para o 13)

Só **persistência**; o sistema de evals é detalhado em 13.

```txt
evals(id, eval_key, target_kind enum(agent|skill|workflow|output|rag), criteria_ref, baseline jsonb, status)  -- fonte: evalRegistry
eval_criteria(id, eval_id fk, name, weight numeric, type enum(assertion|rubric|metric))
eval_results(id, eval_id fk, target_run_id, target_kind, passed bool, created_at) [idx: target_run_id]
eval_scores(id, eval_result_id fk, metric enum(confidence|hallucination_risk|rag_retrieval_quality|evidence_coverage|uncertainty|contradiction), score numeric)
eval_failures(id, eval_result_id fk, criterion, detail jsonb)
eval_recommendations(id, eval_result_id fk, recommendation text)
quality_regressions(id, target_kind, target_ref, baseline numeric, current numeric, delta numeric, detected_at) [APPEND-ONLY]
hallucination_checks(id, agent_run_id fk, claims int, ungrounded int, risk numeric, created_at)
contradiction_checks(id, agent_run_id fk, contradictions int, detail jsonb, created_at)
evidence_coverage_scores(id, agent_run_id fk, claims int, with_evidence int, coverage numeric, created_at)
```

# 20. State Machines Persistence

```txt
state_machines(id, machine_id text unique, applies_to enum(agent_run|node|workflow_run|approval|artifact|collector_run), version, status)  -- fonte: stateMachineRegistry
state_machine_states(id, machine_id fk, state text, is_initial bool, is_terminal bool)
state_machine_transitions(id, machine_id fk, from_state, to_state, guard jsonb, on_event text)
state_transition_logs(id, machine_id, aggregate_type, aggregate_id, from_state, to_state, event_id fk→events, actor, occurred_at) [APPEND-ONLY] [idx: aggregate_type, aggregate_id]
```

Cobre as 6 máquinas do doc 10 §5.25 (agent_run, node, workflow_run, approval, artifact, collector_run). Transição inválida → rejeitada e logada como `invalid_transition` em `state_transition_logs`.

# 21. UI Projection Persistence (CQRS read models)

Tabelas **derivadas e reconstruíveis** a partir do event store. UI lê daqui; **UI não é fonte da verdade**. Versão 1.2.0 expande de 7 para 13 projeções para suportar docs 14–16.

**Tabela raiz genérica (metadado de projeção):**
```txt
ui_projections(
  id              uuid pk,
  projection_key  text,              -- ex.: 'project_pulse', 'node_health'
  org_id          fk [RLS],
  workspace_id    fk,
  project_id      fk,
  payload         jsonb,             -- dados da projeção (para projeções não-tipadas)
  last_event_id   fk→events,        -- último evento que atualizou esta projeção
  is_stale        bool default false,
  stale_reason    text,
  rebuilt_at      timestamptz,       -- última reconstrução completa
  updated_at      timestamptz
)
[idx: projection_key, project_id]
```

**13 projeções tipadas (P11-6 — Product System Support):**

| # | Projeção | Superfície consumidora | Delivery |
|---|---|---|---|
| 1 | `project_pulse_projection` | Dashboard §10, CC §5.3 | SSE |
| 2 | `agent_activity_projection` | Dashboard §12, CC, Canvas | SSE |
| 3 | `node_health_projection` | Dashboard §13, Canvas §9 | SSE |
| 4 | `decision_queue_projection` | Dashboard §11, CC §5.3 | SSE |
| 5 | `approval_projection` | Dashboard §11, Canvas §9.3 | SSE |
| 6 | `cost_credit_projection` | Dashboard §15, CC `/cost` | polling 60s |
| 7 | `roi_snapshot_projection` | Dashboard §14 | polling 60s |
| 8 | `feedback_loop_projection` | Dashboard §16 | polling 30s |
| 9 | `support_friction_projection` | Dashboard §17 | polling 120s |
| 10 | `artifact_feed_projection` | Dashboard §18, Canvas §5.11 | polling 30s |
| 11 | `risk_gap_evidence_projection` | Dashboard §19, Canvas §12 | polling 30s |
| 12 | `canvas_graph_projection` | Canvas §16 | SSE |
| 13 | `command_center_context_projection` | CC §5.3, Dashboard CommandBar | SSE |

---

### 1. project_pulse_projection
```txt
project_pulse_projection(
  project_id pk fk→projects,
  org_id [RLS],
  state          enum(empty_state|briefing_live|diagnosis_active|proposal_building|
                       approval_pending|operation_active|learning_loop),
  pulse          jsonb,   -- {headline, last_activity, confidence_avg, active_agents,
                          --  blocked_nodes, pending_approvals, next_action_suggestion}
  last_event_id  fk→events,
  updated_at     timestamptz
)
```
**Source tables:** `nodes, agent_runs, workflow_runs, approvals, risks, evidence_items`  
**Update trigger:** `NodeCreated | NodeStateChanged | AgentRunStarted | AgentRunCompleted | ApprovalRequested | RiskDetected | WorkflowStarted | WorkflowCompleted`  
**Cache strategy:** SSE push após cada trigger. Cache Redis 60s; rebuild do zero semanalmente.  
**Tenant scope:** `org_id` (RLS). **Permission filtering:** state + headline visíveis para `project_member+`; `next_action_suggestion` visível para `contributor+`.

---

### 2. agent_activity_projection
```txt
agent_activity_projection(
  id pk, project_id fk, org_id [RLS],
  agent_id       fk→agents,
  state          enum(idle|working|waiting_tool|waiting_approval|blocked|completed|audited),
  current_node_id fk→nodes,
  last_run_id    fk→agent_runs,
  last_run_started_at timestamptz,
  cost_current_session numeric,
  updated_at
)
[idx: project_id, state]
```
**Source tables:** `agent_runs, agent_state_transitions, tool_calls, approvals`  
**Update trigger:** `AgentRunStarted | AgentRunCompleted | AgentBlocked | ApprovalRequested | MetacognikReviewed`  
**Cache:** SSE; invalidate por `agent_id + project_id`. **Permission:** `project_member+` vê estado; custo visível para `lead+`.

---

### 3. node_health_projection
```txt
node_health_projection(
  id pk, project_id fk, org_id [RLS],
  node_id        fk→nodes,
  node_type      text,
  status         enum(same as node state machine),
  risk_level     enum(low|medium|high|critical),
  confidence_score numeric,
  has_evidence   bool,
  pending_approval bool,
  blocked_reason text,
  assigned_agent_id fk→agents,
  updated_at
)
[idx: project_id, status, risk_level]
```
**Source tables:** `nodes, node_states, risks, evidence_items, approvals, agent_runs`  
**Update trigger:** `NodeStateChanged | EvidenceLinked | RiskDetected | ApprovalRequested | AgentAssigned`  
**Cache:** SSE; rebuild ao `NodeCreated`. **Permission:** `project_member+`; `risk_level=critical` sempre visível para `lead+`.

---

### 4. decision_queue_projection
```txt
decision_queue_projection(
  id pk, project_id fk, org_id [RLS],
  decision_type  text,
  object_type    text,
  object_id      uuid,
  title          text,
  urgency        enum(low|medium|high|critical),
  requestor_type enum(user|agent|system),
  requestor_id   uuid,
  required_role  enum,
  age_hours      numeric,        -- calculado: now() - created_at
  expires_at     timestamptz,
  updated_at
)
[idx: project_id, urgency, required_role]
```
**Source tables:** `approvals, decisions, nodes (pending_approval), workflow_runs (waiting_approval)`  
**Update trigger:** `ApprovalRequested | NodeStateChanged | WorkflowWaitingApproval | ApprovalExpired`  
**Cache:** SSE; TTL 30s. **Permission:** cada entrada visível apenas para o `required_role` e `lead+`/`founder`.

---

### 5. approval_projection
```txt
approval_projection(
  id pk, project_id fk, org_id [RLS],
  approval_id    fk→approvals,
  status         enum(requested|approved|rejected|expired|revoked|escalated),
  object_type    text,
  object_id      uuid,
  summary        text,
  expires_at     timestamptz,
  approver_id    fk→users,
  updated_at
)
```
**Source tables:** `approvals, approval_events, approval_escalations`  
**Update trigger:** `ApprovalRequested | ApprovalSubmitted | ApprovalExpired | ApprovalEscalated`  
**Cache:** SSE. **Permission:** visível apenas ao approver designado e `lead+`.

---

### 6. cost_credit_projection
```txt
cost_credit_projection(
  project_id pk fk, org_id [RLS],
  period         enum(today|week|month|total),
  credits_consumed numeric,
  credits_reserved numeric,
  credits_available numeric,
  cost_usd       numeric,
  budget_limit_usd numeric,
  budget_state   enum(within|approaching|exceeded|blocked),
  top_consumers  jsonb,   -- [{type, ref_id, cost_usd}] top 5
  forecast_7d    numeric, -- projeção de consumo dos próximos 7 dias
  updated_at
)
```
**Source tables:** `cost_ledger, project_budgets, credit_wallets, credit_transactions`  
**Update trigger:** `CostLedgerEntryAdded | BudgetAlertFired | CreditConsumed | CreditReserved`  
**Cache:** polling 60s; push imediato em `budget_state=exceeded`. **Permission:** `lead+` apenas.

---

### 7. roi_snapshot_projection
```txt
roi_snapshot_projection(
  project_id pk fk, org_id [RLS],
  roi_type       enum(financial|strategic|operational|brand|content|
                       acquisition|retention|efficiency|learning),
  estimated_value numeric,
  realized_value  numeric,
  confidence_score numeric,
  gaps_count      int,
  evidence_count  int,
  cost_accumulated numeric,
  payback_est_days int,
  risk_impact     numeric,
  last_snapshot_at timestamptz,
  updated_at
)
[idx: project_id, roi_type]
```
**Source tables:** `roi_models, roi_snapshots, roi_hypotheses, roi_evidence_links, cost_ledger`  
**Update trigger:** `ROISnapshotCreated | ROIMetricUpdated | CostLedgerEntryAdded`  
**Cache:** polling 60s. **Permission:** `lead+`.

---

### 8. feedback_loop_projection
```txt
feedback_loop_projection(
  id pk, project_id fk, org_id [RLS],
  feedback_id    fk→feedback_items,
  source_type    enum(client|stakeholder|internal|agent|qa),
  status         enum(received|processing|analyzed|converted|rejected|archived),
  sentiment      enum(positive|negative|neutral|mixed),
  converted_to   text,   -- 'node:uuid' | 'task:uuid' | null
  priority       enum,
  updated_at
)
[idx: project_id, status, sentiment]
```
**Source tables:** `feedback_items, feedback_decisions, feedback_node_links`  
**Update trigger:** `FeedbackSubmitted | FeedbackProcessed | FeedbackConverted | FeedbackRejected`  
**Cache:** polling 30s. **Permission:** `contributor+`; source_type=client visible para `lead+`.

---

### 9. support_friction_projection
```txt
support_friction_projection(
  id pk, project_id fk, org_id [RLS],
  ticket_id      fk→support_tickets,
  title          text,
  priority       enum(low|medium|high|critical),
  status         enum(open|assigned|in_progress|waiting_user|escalated|resolved|closed),
  age_hours      numeric,
  assignee_id    uuid,
  sla_breached   bool,
  impact_scope   enum,
  updated_at
)
[idx: project_id, status, priority]
```
**Source tables:** `support_tickets, support_ticket_events, friction_signals`  
**Update trigger:** `SupportTicketCreated | TicketStatusChanged | SLABreached | FrictionSignalDetected`  
**Cache:** polling 120s; push imediato em `priority=critical` ou `sla_breached=true`. **Permission:** `contributor+`.

---

### 10. artifact_feed_projection
```txt
artifact_feed_projection(
  id pk, project_id fk, org_id [RLS],
  artifact_id    fk→artifacts,
  artifact_type  text,
  title          text,
  status         enum(draft|generated|under_review|approved|rejected|published|archived),
  approval_status enum,
  confidence_score numeric,
  produced_by_run fk→workflow_runs,
  version        int,
  updated_at
)
[idx: project_id, status, artifact_type]
```
**Source tables:** `artifacts, artifact_versions, artifact_approval_status, eval_results`  
**Update trigger:** `ArtifactGenerated | ArtifactApproved | ArtifactRejected | ArtifactRevised`  
**Cache:** polling 30s. **Permission:** `project_member+`; `client` vê apenas artifacts com `visibility_scope=client`.

---

### 11. risk_gap_evidence_projection
```txt
risk_gap_evidence_projection(
  id pk, project_id fk, org_id [RLS],
  object_type    enum(risk|gap|evidence|hypothesis),
  object_id      uuid,
  title          text,
  severity       enum(low|medium|high|critical),
  status         text,
  confidence_score numeric,
  has_contradiction bool,
  metacognik_warning bool,
  related_node_id fk→nodes,
  updated_at
)
[idx: project_id, object_type, severity]
```
**Source tables:** `risks, gaps, evidence_items, hypotheses, contradiction_checks, confidence_scores`  
**Update trigger:** `RiskDetected | GapDetected | EvidenceAdded | HypothesisCreated | MetacognikReviewed`  
**Cache:** polling 30s. **Permission:** `project_member+`.

---

### 12. canvas_graph_projection
```txt
canvas_graph_projection(
  project_id pk fk, org_id [RLS],
  nodes_snapshot jsonb,  -- array de {node_id, type, status, position_hint, agent_active}
  edges_snapshot jsonb,  -- array de {edge_id, source, target, edge_type, status}
  layout_version int,
  last_event_id  fk→events,
  updated_at
)
```
**Source tables:** `nodes, node_states, node_edges, agent_activity_projection`  
**Update trigger:** `NodeCreated | NodeStateChanged | NodeEdgeCreated | NodeEdgeInvalidated | AgentAssigned`  
**Cache:** SSE (graph updates em tempo real); snapshot completo a cada 300s ou por demand. **Permission:** `project_member+`; nodes `restricted` omitidos por RLS.

---

### 13. command_center_context_projection
```txt
command_center_context_projection(
  project_id pk fk, org_id [RLS],
  section        text,
  suggestions    jsonb,  -- array de {intent, label, slash_command, priority, context_trigger}
  active_intents jsonb,  -- intenções em execução deste projeto
  last_command   jsonb,  -- {text, intent_type, outcome, at}
  updated_at
)
[idx: project_id, section]
```
**Source tables:** `command_history (P11-2), agent_activity_projection, approval_projection, risk_gap_evidence_projection`  
**Update trigger:** `IntentSubmitted | IntentResolved | AgentRunCompleted | ApprovalRequested | RiskDetected`  
**Cache:** SSE; suggestions re-geradas a cada mudança de estado de projeto. **Permission:** `contributor+`.

# 22. Run Replay Persistence

```txt
run_replays(id, run_id, run_kind, requested_by, created_at)
run_replay_events(id, run_replay_id fk, event_id fk→events, ordinal int)     -- cadeia causal reconstruída
run_replay_snapshots(id, run_replay_id fk, context_pack_id fk, snapshot jsonb [STORAGE-opcional])
run_replay_artifacts(id, run_replay_id fk, artifact_id fk→artifacts)
```

Reconstrói: input, contexto (context_pack), agente, modelo (model_calls), tool (tool_calls), custo (cost_ledger), output, approval, error, cadeia causal (events.causation_id). Possível porque tudo é event-sourced — sem logging paralelo.

# 23. Sandbox / Simulation Persistence

```txt
simulations(id, project_id, target_action jsonb, risk_level, requested_by, created_at)
simulation_runs(id, simulation_id fk, isolated_env_ref, predicted_output jsonb, predicted_cost_usd, state enum(draft|simulation|pending_approval|approved|executed|rolled_back))
simulation_outputs(id, simulation_run_id fk, output jsonb, diff jsonb)
sandbox_changes(id, simulation_run_id fk, change_type, before jsonb, after jsonb)
rollback_plans(id, target_run_id, run_kind, steps jsonb, created_at)
compensating_actions(id, target_event_id fk→events, action_type, payload jsonb, applied_event_id fk→events, applied_at) [APPEND-ONLY]
```

Ação sensível (por `risk_level`) deve ter: simulação → approval → rollback plan → compensating action disponível antes de `executed`.

# 24. Learning Loop Persistence

```txt
lessons_learned(id, project_id, context, lesson, source_run_id, created_at)
decision_outcomes(id, decision_id fk→decisions, outcome enum(positive|negative|mixed|unknown), measured_at, detail jsonb)
workflow_performance(id, workflow_id, period, success_rate numeric, avg_cost_usd, avg_retries numeric)
agent_performance(id, agent_id, period, avg_quality numeric, reproval_rate numeric, avg_cost_usd)
prompt_performance(id, prompt_id, period, approval_rate numeric, avg_quality numeric)
skill_performance(id, skill_id, period, rework_rate numeric, success_rate numeric)
node_performance(id, node_type, period, usefulness numeric, redundancy_rate numeric)
```

Liga causa→efeito (decisão→resultado, prompt→qualidade, skill→retrabalho); ajusta thresholds/políticas (13) e roteamento. Substrato do Self-Evolving (25).

# 25. Multi-tenancy and Data Isolation Notes (preparação para 12)

Sem aprofundar segurança (é o 12), mas o schema já prepara:

- `tenant_id` (= `org_id`) **obrigatório** em toda tabela de domínio; `workspace_id`/`project_id` onde aplicável.
- `created_by` em todas; `visibility_scope` e `access_scope` em objetos expostos a cliente.
- **RLS futuro**: toda tabela de domínio entra sob Row-Level Security por `org_id`/`workspace_id` (12). O schema já carrega as colunas para isso funcionar sem refactor.
- **Storage**: path com `org/workspace/project/...` + URLs assinadas.
- **Vector namespace** por `tenant/project` (`vector_collections.namespace`); filtro de tenant é **pré-condição** da busca, não pós-filtro.
- Segredos (tokens de provider/actor) **fora** das tabelas → secret manager; tabelas guardam só `secret_ref`.

# 26. MVP P0 Data Model

**Entra no MVP P0** (mínimo para o runtime rodar ponta a ponta e ser auditável):

```txt
organizations · workspaces · projects · stakeholders · users · project_members
nodes · workflows · workflow_runs · agent_runs · agent_events · tool_calls · collector_runs
approvals · artifacts · memories · documents · document_chunks · embeddings · context_packs
evidence_items · hypotheses · risks · gaps · decisions · cost_ledger · eval_results
audit_logs · state_transition_logs · ui_projections
```

(`events` append-only é implícito e obrigatório no P0 — é a fonte de `agent_events`/`state_transition_logs`/`audit_logs`.)

**Adições P0 do Patch 1.1.1 (Security Data Support):** `rbac_roles · role_permissions · user_role_assignments · secret_refs`. `capability_grants` entra no P0 quando `capability_system` for ativado; pode ser deferred para P1 se as capabilities forem gerenciadas por `project_settings.enabled_capabilities`.

**Adições P0 do Patch 1.2.0 (Product System Data Support):**
```txt
node_edges          -- schema completo (§10); suporta Node Canvas MVP
project_activity_feed -- feed append-only para Recent Events no Dashboard (§35)
dashboard_preferences -- personalização de layout por usuário/projeto (§34)
```
*(13 ui_projections tipadas (§21) são reconstruíveis — não entram como "tabelas P0" mas como projeções ativas desde o MVP)*

**Fica fora do MVP P0** (evolução): self-evolving avançado; registry UI; sandbox/simulation avançado; run replay visual completo; model router sofisticado; capability marketplace; full cost analytics; squad/skill-chain registries; learning loop completo; ROI System (§30 — aguarda ROI Architecture doc); Feedback System completo (§31 — aguarda Feedback Architecture doc); Support System completo (§32 — aguarda Support Architecture doc); Credits/Billing completo (§33 — aguarda Billing Architecture doc).

## Patch 1.1.1 — Security Data Support

Aplicado para suportar as políticas definidas em `12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md v1.1.0`. Não altera tabelas existentes — apenas adições.

| Tabela | Seção | Propósito |
|---|---|---|
| `rbac_roles` | §4.1 | Catálogo de papéis dinâmicos por org; complementa `project_members.role` |
| `role_permissions` | §4.1 | Matrix de permissões por papel; base da avaliação RBAC no `policy_engine` |
| `user_role_assignments` | §4.1 | Vínculos usuário↔papel com escopo, expiração e revogação imediata |
| `capability_grants` | §11 | Permissão de capability por project/workspace/org com approval e revogação |
| `secret_refs` | §12.1 | Ponteiros seguros para vault; nunca armazenam segredo real |

**Dependências satisfeitas para doc 12:**
- `policy_engine` (10) agora tem tabelas de RBAC para consultar em authz.
- `tool_router` e `agent_router` podem resolver `role_permissions` para enforcement de capability scope.
- `collector_runner` resolve `secret_refs` server-side sem expor `vault_path`.
- `approval_gate` pode ligar `capability_grants.approval_ref` a approvals de capabilities de alto risco.
- `audit_logs` recebe `SecretAccessed`, `RoleAssigned`, `RoleRevoked`, `CapabilityGranted`, `CapabilityRevoked`.

**Dependências ainda abertas (para validação antes de aprovação de 12):**
- `policy_rules` físico (RBAC+ABAC policy store) está coberto pelos registries genéricos (`registry_items`/`registry_item_versions`) via `policyRegistry`. Nenhuma tabela adicional necessária.
- `audit_logs` já existe no P0 e cobre todos os novos eventos de segurança. O schema completo foi adicionado em `§16.1` como Patch 1.1.2.

## Patch 1.1.2 — audit_logs Schema for Implementation Readiness

Aplicado após o **Runtime Approval Gate** identificar que `audit_logs` constava na lista MVP P0 (§26) mas sem seção dedicada com schema derivável. Um engenheiro lendo doc 11 isoladamente não conseguia derivar o schema — violando o critério de aprovação do próprio documento. O schema estava apenas em doc 12 §5.16.

| Tabela | Seção | Propósito |
|---|---|---|
| `audit_logs` | §16.1 | Rastreabilidade append-only de segurança, autorização, decisões e ações de agentes; fonte de verdade para incident review, compliance e run replay de incidentes de segurança |

**Dependências satisfeitas:**
- Engenheiro deriva migrations de `audit_logs` inteiramente de doc 11 §16.1, sem necessidade de cruzar com doc 12.
- Cross-reference de doc 12 §5.16 complementa esta seção com a especificação de política dos 14 eventos — a tabela está em doc 11, a política dos eventos está em doc 12.
- `audit_logs` no MVP P0 (§26) agora tem seção dedicada e schema completo.
- Adições ao MVP P0 do Patch 1.1.2: `audit_logs` (com schema completo).

**Nada alterado nas tabelas existentes** — apenas adição de §16.1.

## Patch 1.2.0 — Product System Data Support

Aplicado para suportar os docs 14 (Project Dashboard), 15 (Command Center) e 16 (Node Canvas) v1.2.x. Adiciona 8 patches documentais de coerência sem alterar tabelas existentes.

| Patch | Tabelas adicionadas / expandidas | Seção | Doc origem |
|---|---|---|---|
| P11-1 | `node_edges` (schema completo); `nodes` (+source_event_id, +cost_estimate) | §10 | Doc 16 §7 |
| P11-2 | `roi_models, roi_metrics, roi_snapshots, roi_hypotheses, roi_evidence_links, roi_assumptions, roi_outcomes` | §30 | Doc 14 §14, Doc 15 `/roi` |
| P11-3 | `feedback_items, feedback_threads, feedback_sources, feedback_decisions, feedback_node_links, feedback_artifact_links, feedback_status_transitions` | §31 | Doc 14 §16, Doc 15 `/feedback` |
| P11-4 | `support_tickets, support_ticket_events, support_categories, support_sla_policies, support_agent_links, support_resolution_notes, friction_signals` | §32 | Doc 14 §17, Doc 15 `/support` |
| P11-5 | `plans, plan_features, subscriptions, credit_wallets, credit_transactions, credit_reservations, usage_events, billing_events, invoice_records, plan_limits, quota_policies` | §33 | Doc 14 §15 |
| P11-6 | `ui_projections` expandidas: 7 → 13 projeções tipadas com spec completa | §21 | Docs 14–16 |
| P11-7 | `dashboard_preferences` | §34 | Doc 14 §24 |
| P11-8 | `project_activity_feed` | §35 | Doc 14 §29 |

---

# 30. ROI System Data Model *(Patch 1.2.0 — P11-2)*

> **Gap registrado:** ROI Architecture completa aguarda doc dedicado (ARCH_PATCH_REPORT §12.1). Este modelo de dados é a base de persistência necessária para suportar o ROI Snapshot widget (doc 14 §14) e os ROI nodes (doc 16 §5.14). Não define a lógica de cálculo — apenas a estrutura de armazenamento.

```txt
roi_models(
  id uuid pk,
  org_id fk [RLS], workspace_id fk, project_id fk,
  roi_type       enum(financial|strategic|operational|brand|content|
                       acquisition|retention|efficiency|learning),
  name           text,
  description    text,
  calculation_method enum(formula|inference|manual|hybrid),
  formula        jsonb,                  -- ex.: {expression, variables, units}
  confidence_score numeric,
  status         enum(draft|active|archived),
  created_by     fk→users,
  created_at, updated_at
)
[idx: project_id, roi_type, status]

roi_metrics(
  id uuid pk,
  roi_model_id   fk→roi_models,
  metric_name    text,
  unit           text,                   -- ex.: 'BRL', 'leads', '%', 'hours'
  current_value  numeric,
  baseline_value numeric,
  target_value   numeric,
  measurement_method text,
  source_type    enum(manual|agent_inference|collector|artifact|decision),
  source_ref     uuid,
  period         enum(current|30d|90d|12m|total),
  measured_at    timestamptz,
  created_at
)
[idx: roi_model_id]

roi_snapshots(
  id uuid pk,
  org_id fk [RLS], project_id fk,
  roi_model_id   fk→roi_models,
  snapshot_type  enum(estimated|realized|projected),
  roi_value      numeric,
  confidence_score numeric,
  evidence_quality enum(low|medium|high),
  gaps           jsonb,                  -- [{description, impact}]
  cost_accumulated numeric,
  payback_estimated_days int,
  period_start   timestamptz,
  period_end     timestamptz,
  created_by_run fk→agent_runs,
  created_at
) [APPEND-ONLY] [idx: project_id, roi_model_id, created_at]

roi_hypotheses(
  id uuid pk,
  project_id fk,
  roi_model_id   fk→roi_models,
  statement      text,
  expected_roi   numeric,
  expected_roi_type text,
  timeframe_days int,
  status         enum(open|validated|refuted|parked),
  confidence_score numeric,
  created_by     fk→users,
  created_at, updated_at
)
[idx: project_id, status]

roi_evidence_links(
  id uuid pk,
  roi_model_id   fk→roi_models,
  roi_hypothesis_id fk→roi_hypotheses,
  evidence_id    fk→evidence_items,
  link_type      enum(supports|contradicts|validates|undermines),
  weight         numeric,
  created_at
)
[idx: roi_model_id]

roi_assumptions(
  id uuid pk,
  roi_model_id   fk→roi_models,
  assumption     text,
  confidence     numeric,
  validated      bool default false,
  validated_by   fk→users,
  evidence_id    fk→evidence_items,
  risk_if_wrong  enum(low|medium|high|critical),
  created_at
)

roi_outcomes(
  id uuid pk,
  roi_model_id   fk→roi_models,
  outcome_type   enum(revenue|savings|time_saved|market_share|brand_lift|
                       retention|acquisition|other),
  value          numeric,
  unit           text,
  period         text,
  measured_at    timestamptz,
  validated_by   fk→users,
  evidence_id    fk→evidence_items,
  created_at
) [APPEND-ONLY]
```

**Invariantes:**
- `roi_snapshots` é append-only — novos snapshots não sobrescrevem; histórico preservado.
- `roi_type` alinha com os 9 tipos definidos em doc 14 §14 e doc 15 Intent Taxonomy família #8.
- `calculation_method = inference` significa que o snapshot foi gerado por agente — `created_by_run` obrigatório neste caso.
- Dashboard e Canvas **não calculam ROI** — lêem de `roi_snapshot_projection` (§21 #7).

---

# 31. Feedback System Data Model *(Patch 1.2.0 — P11-3)*

> **Gap registrado:** Feedback System completo aguarda doc dedicado (ARCH_PATCH_REPORT §12.2). Este modelo sustenta o Feedback Loop widget (doc 14 §16) e os Feedback nodes (doc 16 §5.15).

```txt
feedback_items(
  id uuid pk,
  org_id fk [RLS], workspace_id fk, project_id fk,
  source_type    enum(client|stakeholder|internal|agent|qa),
  source_id      uuid,               -- fk→users ou fk→stakeholders (polimórfico)
  feedback_type  enum(explicit|implicit),
  channel        enum(command_center|dashboard|canvas|api|webhook|email|other),
  content        text,
  sentiment      enum(positive|negative|neutral|mixed),
  status         enum(received|processing|analyzed|converted|rejected|archived),
  priority       enum(low|medium|high|critical),
  correlation_id uuid,               -- liga ao intent/run que gerou o feedback
  created_at, updated_at
)
[idx: project_id, source_type, status]
[idx: project_id, sentiment, created_at]

feedback_threads(
  id uuid pk,
  org_id fk, project_id fk,
  root_feedback_id fk→feedback_items,
  subject        text,
  status         enum(open|resolved|archived),
  created_at, updated_at
)
[idx: project_id]

feedback_sources(
  id uuid pk,
  org_id fk, project_id fk,
  source_type    text,
  source_ref     uuid,
  display_name   text,
  trust_level    enum(low|medium|high),
  created_at
)

feedback_decisions(
  id uuid pk,
  org_id fk, project_id fk,
  feedback_id    fk→feedback_items,
  decision_action enum(convert_to_node|create_task|reject|archive|escalate),
  decided_by     fk→users,
  decision_note  text,
  related_node_id fk→nodes,
  related_artifact_id fk→artifacts,
  decided_at     timestamptz
)
[idx: project_id, feedback_id]

feedback_node_links(
  id uuid pk,
  feedback_id    fk→feedback_items,
  node_id        fk→nodes,
  link_type      enum(generated|influenced|addressed|rejected_by),
  created_at
)

feedback_artifact_links(
  id uuid pk,
  feedback_id    fk→feedback_items,
  artifact_id    fk→artifacts,
  link_type      enum(about|generated_by|influenced),
  created_at
)

feedback_status_transitions(
  id uuid pk,
  feedback_id    fk→feedback_items,
  from_status    text,
  to_status      text,
  actor_id       uuid,
  actor_type     enum(user|agent|system),
  event_id       fk→events,
  occurred_at    timestamptz
) [APPEND-ONLY]
```

**Invariantes:**
- `feedback_type = implicit` = feedback inferido por comportamento (repetição de ação, rejeição de sugestão, etc.). Não requer interação explícita do usuário.
- Todo feedback convertido gera entrada em `feedback_decisions` + link em `feedback_node_links` ou `feedback_artifact_links`.
- `feedback_status_transitions` é append-only — rastreabilidade completa do ciclo de vida do feedback.
- `content` com PII potencial → classificação `internal` mínima; mascarado nos audit logs.

---

# 32. Support System Data Model *(Patch 1.2.0 — P11-4)*

> **Gap registrado:** Support System completo aguarda doc dedicado (ARCH_PATCH_REPORT §12.3). Este modelo sustenta o Support & Friction widget (doc 14 §17) e os Support nodes (doc 16 §5.16).

```txt
support_tickets(
  id uuid pk,
  org_id fk [RLS], workspace_id fk, project_id fk,
  reporter_id    uuid,               -- fk→users ou fk→stakeholders
  reporter_type  enum(client|stakeholder|internal),
  title          text,
  description    text,
  category_id    fk→support_categories,
  priority       enum(low|medium|high|critical),
  status         enum(open|assigned|in_progress|waiting_user|escalated|resolved|closed),
  assignee_id    uuid,               -- fk→users ou fk→agents
  assignee_type  enum(agent|human),
  impact_scope   enum(project|workflow|node|artifact|billing|access|system),
  related_node_id fk→nodes,
  related_run_id  uuid,
  correlation_id  uuid,
  sla_deadline   timestamptz,
  resolved_at    timestamptz,
  created_at, updated_at
)
[idx: project_id, status, priority]
[idx: org_id, created_at]

support_ticket_events(
  id uuid pk,
  ticket_id      fk→support_tickets,
  event_type     enum(created|assigned|escalated|commented|status_changed|resolved|reopened|closed),
  actor_id       uuid,
  actor_type     enum(user|agent|system),
  payload        jsonb,
  event_id       fk→events,
  occurred_at    timestamptz
) [APPEND-ONLY] [idx: ticket_id]

support_categories(
  id uuid pk,
  org_id fk,
  key            text,
  display_name   text,
  description    text,
  default_sla_hours int,
  default_priority enum(low|medium|high|critical),
  is_system      bool default false,
  created_at
)

support_sla_policies(
  id uuid pk,
  org_id fk,
  category_id    fk→support_categories,
  priority       enum,
  response_sla_hours int,
  resolution_sla_hours int,
  escalation_after_hours int,
  escalate_to_role enum,
  active         bool default true
)

support_agent_links(
  id uuid pk,
  ticket_id      fk→support_tickets,
  agent_id       fk→agents,
  assignment_type enum(auto|manual),
  assigned_at    timestamptz,
  unassigned_at  timestamptz
)

support_resolution_notes(
  id uuid pk,
  ticket_id      fk→support_tickets,
  content        text,
  author_id      uuid,
  author_type    enum(user|agent),
  is_internal    bool default false,  -- não visível para reporter externo
  created_at     timestamptz
) [APPEND-ONLY]

friction_signals(
  id uuid pk,
  org_id fk [RLS], workspace_id fk, project_id fk,
  user_id        fk→users,
  signal_type    enum(repeated_action|error_retry|abandoned_flow|failed_intent|
                       blocked_node|stale_approval|unresolved_ticket_pattern),
  context        jsonb,              -- detalhes do sinal (node_id, intent_type, etc.)
  session_id     uuid,
  created_at     timestamptz
) [APPEND-ONLY] [idx: project_id, signal_type, created_at]
```

**Invariantes:**
- `support_ticket_events` é append-only — histórico completo de cada ticket.
- `support_resolution_notes` com `is_internal=true` nunca visível para `reporter_type=client`.
- `friction_signals` é sinal de produto — alimenta o learning loop (§24) e a `support_friction_projection` (§21 #9).
- SLA breach gera entrada em `audit_logs` e push imediato na projeção.
- `priority=critical` tickets disparam notificação imediata para `admin`/`founder`.

---

# 33. Credits, Plans and Billing Data Model *(Patch 1.2.0 — P11-5)*

> **Gap registrado:** Credits, Plans & Billing Architecture aguarda doc dedicado (ARCH_PATCH_REPORT §12.4). Este modelo define a base de persistência para suportar o Cost & Credits widget (doc 14 §15). Não define a lógica de cobrança externa — apenas a estrutura de dados interna do CKOS.

> **Separação obrigatória:** `cost_ledger` (§18) = custo interno de runtime (tokens, tools, collectors). `credit_wallets` + `credit_transactions` = sistema de créditos do usuário/org. `billing_events` + `invoice_records` = sistema de faturamento. São camadas separadas — não confundir.

```txt
plans(
  id uuid pk,
  key            text unique,         -- ex.: 'free', 'starter', 'professional', 'enterprise'
  display_name   text,
  description    text,
  tier           enum(free|starter|professional|enterprise|custom),
  status         enum(active|deprecated|hidden),
  version        int,
  created_at
)

plan_features(
  id uuid pk,
  plan_id        fk→plans,
  feature_key    text,                -- ex.: 'max_projects', 'canvas_access', 'custom_agents'
  display_name   text,
  enabled        bool,
  limit_value    numeric,             -- null = ilimitado
  limit_unit     text,
  metadata       jsonb
)
[idx: plan_id, feature_key]

subscriptions(
  id uuid pk,
  org_id         fk→organizations [RLS],
  plan_id        fk→plans,
  status         enum(trial|active|past_due|cancelled|expired),
  billing_cycle  enum(monthly|annual|usage_based),
  current_period_start timestamptz,
  current_period_end   timestamptz,
  trial_ends_at  timestamptz,
  cancelled_at   timestamptz,
  external_subscription_ref text,    -- ref no sistema de billing externo (ex.: Stripe)
  created_at, updated_at
)
[idx: org_id, status]

credit_wallets(
  id uuid pk,
  org_id         fk→organizations [RLS],
  workspace_id   fk→workspaces,
  scope          enum(org|workspace|project),
  scope_ref      uuid,               -- id do escopo (org_id, workspace_id ou project_id)
  balance        numeric default 0,  -- créditos disponíveis
  reserved       numeric default 0,  -- créditos reservados para runs em execução
  currency       text default 'credits',
  updated_at     timestamptz
)
[idx: org_id, scope, scope_ref]

credit_transactions(
  id uuid pk,
  org_id         fk [RLS],
  wallet_id      fk→credit_wallets,
  transaction_type enum(purchase|grant|consumption|refund|expiry|reservation|release),
  amount         numeric,            -- positivo = crédito; negativo = débito
  balance_before numeric,
  balance_after  numeric,
  source_type    enum(run|workflow|tool|collector|manual|billing_event),
  source_ref     uuid,               -- id do run/workflow/billing_event
  description    text,
  created_at     timestamptz
) [APPEND-ONLY] [idx: wallet_id, created_at]

credit_reservations(
  id uuid pk,
  org_id         fk [RLS],
  wallet_id      fk→credit_wallets,
  amount         numeric,
  reserved_for_type enum(workflow_run|agent_run|collector_run),
  reserved_for_id   uuid,
  status         enum(active|released|consumed|expired),
  expires_at     timestamptz,
  created_at     timestamptz
)
[idx: wallet_id, status]

usage_events(
  id uuid pk,
  org_id         fk [RLS],
  workspace_id   fk, project_id fk,
  event_type     enum(model_call|tool_call|collector_run|storage_write|
                       api_call|workflow_step|custom),
  resource_ref   uuid,               -- id do model_call, tool_call, etc.
  units_consumed numeric,
  unit_type      text,               -- ex.: 'tokens', 'calls', 'mb', 'steps'
  cost_usd       numeric,
  correlation_id uuid,
  source_event_id fk→events,
  occurred_at    timestamptz
) [APPEND-ONLY] [idx: org_id, project_id, occurred_at]

billing_events(
  id uuid pk,
  org_id         fk [RLS],
  subscription_id fk→subscriptions,
  event_type     enum(invoice_generated|payment_succeeded|payment_failed|
                       plan_changed|trial_ended|subscription_cancelled|credit_purchased),
  amount         numeric,
  currency       text,
  metadata       jsonb,
  external_ref   text,
  occurred_at    timestamptz
) [APPEND-ONLY]

invoice_records(
  id uuid pk,
  org_id         fk [RLS],
  subscription_id fk→subscriptions,
  billing_period_start timestamptz,
  billing_period_end   timestamptz,
  subtotal       numeric,
  tax            numeric,
  total          numeric,
  status         enum(draft|open|paid|void|uncollectible),
  line_items     jsonb,              -- [{description, quantity, unit_price, amount}]
  external_invoice_id text,
  issued_at      timestamptz,
  due_at         timestamptz,
  paid_at        timestamptz
)
[idx: org_id, status]

plan_limits(
  id uuid pk,
  plan_id        fk→plans,
  limit_key      text,               -- ex.: 'runs_per_month', 'storage_gb'
  limit_value    numeric,
  limit_unit     text,
  hard_limit     bool default false, -- false = warn; true = block
  block_on_exceed bool default false,
  approval_required_on_exceed bool default false
)
[idx: plan_id, limit_key]

quota_policies(
  id uuid pk,
  org_id         fk [RLS],
  scope          enum(org|workspace|project),
  scope_ref      uuid,
  policy_key     text,
  quota_value    numeric,
  quota_unit     text,
  reset_period   enum(daily|monthly|never),
  overage_action enum(block|warn|approve|charge),
  created_at     timestamptz
)
[idx: org_id, scope, scope_ref]
```

**Invariantes:**
- `credit_transactions` é append-only. Saldo calculado como `SUM(amount)` ou via `balance_after` da última entrada.
- `credit_reservations` garante que créditos prometidos para um run em execução não sejam consumidos por outro run concorrente.
- `quota_policies.overage_action = approve` → o custo não bloqueia imediatamente; emite `ApprovalRequested` para o `approval_gate`.
- Tokens/segredos de sistemas de pagamento externos **nunca** nesta tabela — somente `external_subscription_ref` e `external_invoice_id` como referências opacas.
- O `cost_guard` (doc 10 §5.23) consulta `credit_wallets`, `plan_limits` e `quota_policies` antes de cada run de custo significativo.

---

# 34. Dashboard Preferences *(Patch 1.2.0 — P11-7)*

> Sustenta a personalização de layout do Project Dashboard (doc 14 §24).

```txt
dashboard_preferences(
  id uuid pk,
  org_id         fk→organizations [RLS],
  workspace_id   fk→workspaces,
  project_id     fk→projects,
  user_id        fk→users,
  layout_preset  text,               -- ex.: 'executive', 'operations', 'founder'
  pinned_widgets jsonb,              -- array de widget_keys
  hidden_widgets jsonb,              -- array de widget_keys (fixo_obrigatórios não entram)
  widget_order   jsonb,              -- array ordenado de widget_keys
  widget_sizes   jsonb,              -- {widget_key: 'compact|default|expanded'}
  density        enum(compact|default|expanded) default 'default',
  theme_overrides jsonb,             -- tokens de tema locais (override do design_system)
  created_at     timestamptz,
  updated_at     timestamptz,
  CONSTRAINT uq_user_project UNIQUE (user_id, project_id)
)
[idx: project_id, user_id]
```

**Invariantes:**
- Um usuário tem no máximo uma preferência por projeto (UNIQUE constraint).
- `hidden_widgets` nunca pode incluir widgets `fixed_required` (validação na camada de aplicação + policy_engine).
- `theme_overrides` não altera a `design_system` do projeto — apenas override local do usuário.
- `admin_locked` widgets são gerenciados via `project_settings` (§4), não por `dashboard_preferences`.
- `plan_locked` widgets são validados pelo `policy_engine` consultando `plan_features` (§33).

---

# 35. Project Activity Feed *(Patch 1.2.0 — P11-8)*

> Feed append-only de atividades visíveis do projeto — alimenta "Recent Events" no Dashboard (doc 14 §29), CKOS Home, stakeholder updates, run replay e auditoria de suporte.

```txt
project_activity_feed(
  id             uuid pk,
  org_id         fk→organizations [RLS],
  workspace_id   fk→workspaces,
  project_id     fk→projects,
  event_id       fk→events,         -- evento do event store que originou esta atividade
  actor_type     enum(user|agent|system|collector),
  actor_id       text,               -- user_id ou agent system_id
  activity_type  text,               -- ex.: 'node_created', 'artifact_approved', 'risk_detected'
  title          text,               -- título legível (ex.: "Briefing aprovado por Ana")
  summary        text,               -- descrição de 1–2 linhas
  target_type    text,               -- tipo do objeto afetado (node, artifact, workflow, etc.)
  target_id      uuid,               -- id do objeto afetado
  severity       enum(info|warning|error|critical) default 'info',
  visibility_scope enum(internal|lead|admin|founder|client|public) default 'internal',
  created_at     timestamptz
) [APPEND-ONLY]
[idx: project_id, created_at]
[idx: org_id, project_id, visibility_scope, created_at]
[idx: event_id]
```

**Invariantes:**
- Append-only — nunca atualizar ou deletar entradas; dados de auditoria/histórico.
- `visibility_scope` determina quem vê a atividade: `client` vê apenas entradas com `visibility_scope IN ('client', 'public')`; `admin` vê tudo.
- `event_id fk→events` garante rastreabilidade bidirecional: event store → activity feed.
- Alimentado pelo `ui_projection_engine` e pelo `memory_writer` ao processar eventos do bus.
- Não deve armazenar PII sensível em `title`/`summary` — usar referências por id quando possível.

---

# 27. Edge Cases

- **Evento duplicado** → `events.idempotency_key unique` + dedupe por `id`.
- **Run órfão** → `run_heartbeats.lease_until` expira → re-enqueue idempotente (idempotency_key).
- **Tool timeout** → `tool_calls.status=timeout` → retry/backoff (`run_retries`) → DLQ.
- **Collector parcial** → `collector_runs.state=failed` com `normalized_count` parcial; registros salvos são válidos; reprocessar resto.
- **Vector search cross-tenant** → namespace+tenant como pré-condição; tentativa logada (12).
- **Memória desatualizada** → `memories.valid_until`/`freshness_at`; job de expiração (05 §5.8).
- **Projeção atrasada** → `ui_projections.last_event_id` < último evento → UI mostra "sincronizando"; nunca tratar projeção stale como verdade.
- **Approval expirado** → `approval_expirations.action_on_expire` (block|escalate|auto).
- **Artifact version conflict** → resolver por `supersedes_id` + Metacognik (hierarquia de confiança).
- **Custo acima do limite** → `project_budgets.state=blocked_by_cost` → `needs_approval`.
- **Migration quebra run antigo** → eventos são imutáveis e versionados por `payload` schema_version; replay usa o schema da época.
- **Retry duplicando** → idempotency_key no run e no evento impede efeito duplo.
- **Agente lê dado sem permissão** → bloqueado por `agent_permissions`/RLS (12); tentativa logada em `events`/`audit_logs`.

# 28. Metrics

% runs com trace completo · % outputs com evidence · latência write→projection · retrieval accuracy · cost per run · cost per project · event replay success · orphan run rate · duplicate event rate · RLS violation attempts · artifact version conflicts · vector retrieval confidence.

# 29. Related Notes

- [[02_AI_FIRST_OBJECT_MODEL]]
- [[05_MEMORY_AND_CONTEXT_ARCHITECTURE]]
- [[09_TRANSFORMERS_AND_PIPELINES]]
- [[10_SYSTEM_RUNTIME_ARCHITECTURE]]
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]]
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]]
- [[14_PROJECT_DASHBOARD_ARCHITECTURE]]
- [[15_COMMAND_CENTER_ARCHITECTURE]]
- [[16_NODE_CANVAS_ARCHITECTURE]]
- [[25_SELF_EVOLVING_SYSTEM_ARCHITECTURE]]
- [[ARCHITECTURE_PATCH_REPORT]]
