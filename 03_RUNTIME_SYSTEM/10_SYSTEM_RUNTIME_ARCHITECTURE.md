---
title: System Runtime Architecture
file: 10_SYSTEM_RUNTIME_ARCHITECTURE.md
phase: 03_RUNTIME_SYSTEM
category: runtime
version: 1.1.1
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
purpose: Definir o runtime executável do CKOS — registries, engines, state machines, protocolo de eventos entre agentes, capabilities, collectors, context pack, schemas, evidence, decision rights, cost guard, evals, replay, sandbox e learning loop.
inputs: Object Model (02); Agent Model (03); Autonomy (04); Memory (05); Skills (06); Workflows (07); Transformers (09).
outputs: Modelo de execução; 23 registries; 20 engines; protocolo de eventos de agente; capability system; collector runtime; context pack; schemas; evidence trail; decision rights; cost guard; eval hooks; state machines; run replay; sandbox; learning loop; recorte MVP P0.
framework: Event-sourced + CQRS + worker pool; registries (dados) + engines (comportamento); ingress → resolver → policy → workflow → run → audit → approval → artifact → memory → projection.
edge_cases: Evento duplicado; run órfão; modelo indisponível; tool timeout; approval expirado; projeção atrasada; loop de agentes.
integrations: Postgres/event store (11); Redis/queue; OpenRouter (model router); tools externas; permission engine (12); tracing (13).
prompts: Não aplicável (documento de arquitetura).
metrics: Latência intenção→primeiro evento; throughput de runs; taxa de retry; runs órfãos; lag de projeção; custo/run.
related_notes:
  - ../01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md
  - ../01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md
  - 11_DATA_MODEL_AND_PERSISTENCE.md
  - 12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - 13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
tags: [runtime, event_bus, workflow_engine, scheduler, cqrs, registries, engines, state_machines, capability, collector, context_pack, evals, cost_guard, run_replay, sandbox, learning_loop]
---

# 1. Propósito

Definir o runtime executável do CKOS: a camada que faz os objetos (02), agentes (03), autonomia (04), memória (05), skills (06), workflows (07) e transformers (09) **acontecerem** de forma rastreável, concorrente, resiliente e auditável.

Este documento responde à pergunta central: **como uma intenção digitada na CommandBar vira execução rastreável no CKOS?** (ver §5.2).

# 2. Função dentro do CKOS

O Runtime é a fonte de verdade de execução. Product (04) é projeção dele; Implementation (05) constrói sobre ele. Princípio arquitetural: **event-sourced + CQRS**. Toda mudança de estado é um evento imutável no event log; o estado atual é uma projeção derivada. Isso dá rastreabilidade total, replay, rollback e diagnóstico vivo "de graça".

# 3. Inputs

Object Model (02), Agent Operating Model (03), Autonomy (04), Memory (05), Skills (06), Workflow Blueprints (07), Transformers (09).

# 4. Outputs

Modelo de execução; especificação de event bus/log, workflow engine, agent/model/tool routers, node state machine, run scheduler/queue, approval gate runtime, artifact pipeline, HITL, projeção em tempo real, rollback e failure modes.

# 5. Framework operacional

## 5.1 Componentes do runtime

```txt
┌─────────────────────────────────────────────────────────────────┐
│ INGRESS (CommandBar / API / Agent / Scheduler / Webhook)          │
│   → Intent Resolver  → Context Assembler  → Policy/Permission     │
├─────────────────────────────────────────────────────────────────┤
│ EVENT BUS  (pub/sub)        ↔   EVENT LOG (append-only, fonte)    │
├─────────────────────────────────────────────────────────────────┤
│ WORKFLOW ENGINE (máquinas de estado)                              │
│   → Run Scheduler → Queue (Redis) → Worker Pool                   │
│        → Agent Router → Model Router → Tool Router                │
│   → Node State Machine                                            │
├─────────────────────────────────────────────────────────────────┤
│ METACOGNIK AUDIT  →  APPROVAL GATE  →  ARTIFACT PIPELINE          │
├─────────────────────────────────────────────────────────────────┤
│ PROJECTORS (CQRS read models) → UI Projection (SSE/WebSocket)     │
│ MEMORY WRITER → (11 Data Model)   ·   TRACER → (13 Evals)         │
└─────────────────────────────────────────────────────────────────┘
```

## 5.2 Fluxo canônico: da intenção à execução rastreável

```txt
1.  CommandBar emite IntentSubmitted{text, project_id, user_id, section}
2.  Intent Resolver classifica (usa transformer intent_to_object) → IntentResolved{intent, object_candidates, confidence}
3.  Context Assembler monta Context Packet (memória curta/média/longa via 11) → ContextAssembled
4.  Policy/Permission Engine (12) valida usuário×workspace×projeto×ação → PermissionGranted | PermissionDenied
5.  Workflow Engine instancia Workflow Run a partir do blueprint (07) → WorkflowStarted{workflow_id, run_id}
6.  Cada passo vira um Run agendado: RunScheduled → RunStarted{run_id, idempotency_key, trace_id}
7.  Agent Router escolhe agente; Model Router escolhe modelo (política 13); Tool Router habilita tools permitidas (12)
8.  Worker executa a skill (06); emite partial outputs → PartialOutputProduced (streaming, §5.9)
9.  Node State Machine transiciona o(s) node(s) afetado(s) (§5.7)
10. Metacognik audita → MetacognikReviewed{confidence, risk, recommendation}
11. Approval Gate: se autonomia/risco exigir (04/12) → ApprovalRequested → [pausa] → ApprovalGranted|Denied
12. Artifact Pipeline materializa outputs → ArtifactGenerated (binário em storage, metadado em 11)
13. Memory Writer grava decisões/aprendizados → MemoryUpdated
14. Projectors atualizam read models → UI recebe NextBestAction via SSE
```

Cada seta acima é **um evento no event log**. Logo, qualquer execução é reconstruível, auditável e reproduzível (run replay — ver `13`).

## 5.3 Event Bus e Event Log

- **Event Log**: tabela append-only `event` (schema em `11`). Fonte de verdade. Nunca se faz UPDATE/DELETE — apenas append. Cada evento: `event_id (uuid v7), workspace_id, project_id, type, payload (jsonb), actor (user/agent/system), causation_id, correlation_id, occurred_at`.
- **Event Bus**: pub/sub que distribui eventos aos consumidores (workflow engine, projectors, memory writer, tracer). MVP: Postgres `LISTEN/NOTIFY` + outbox; escala: Redis Streams / NATS.
- **Ordering & causation**: `correlation_id` agrupa tudo de uma intenção; `causation_id` aponta o evento que causou este. Permite reconstruir a árvore causal de uma execução.

## 5.4 Workflow Engine

- Instancia blueprints (07) como **máquinas de estado** dirigidas por eventos.
- Estados de workflow: `draft·ready·running·waiting_user_input·waiting_agent·waiting_approval·blocked·completed·failed·rolled_back·archived`.
- Cada transição consome e produz eventos. O engine é **stateless**; o estado vive no event log + projeção `workflow_state`.
- Suporta sub-workflows e fan-out/fan-in (sequencial, concorrente, handoff — padrões da pesquisa Manus/Azure).

## 5.5 Routers

- **Agent Router**: mapeia intenção/skill → agente (03), respeitando permissões de agente (12). Resolve handoffs.
- **Model Router**: escolhe o modelo (via OpenRouter) por política de custo/qualidade (`13 §model policy`): tarefa barata → modelo barato; tarefa crítica → modelo forte; com fallback automático.

> **Nota estratégica — Posicionamento CKOS sobre modelos de linguagem (MVP e além):**
> CKOS does not own or train a foundation model at MVP stage. CKOS owns the **model orchestration layer**: model registry, model router, context pack, memory, prompts, instructions, policies, evals, fallbacks, cost guard and learning loop. External LLMs (e.g., OpenAI, Anthropic, Google, open-source via OpenRouter) are **replaceable cognitive engines** — selected per task by risk level, privacy classification, budget envelope, latency requirement and quality threshold. This is an intentional architectural constraint: the value of CKOS is in the orchestration, memory, reasoning structure, approval gates and learning loop — not in any single underlying model. Model substitution must never require architecture changes; only model registry and routing policy updates.

- **Tool Router**: habilita apenas as `allowed_tools` da skill (06) E permitidas ao agente/projeto (12). Deny-by-default.

## 5.6 Run Scheduler, Queue, Retry, Timeout, Idempotency

```txt
Run = unidade atômica de execução de agente/skill/tool.
- Queue: Redis (filas por prioridade e por tenant para isolamento de carga).
- Worker Pool: workers consomem runs; concorrência limitada por workspace (cota — ver 12/13).
- Idempotency: cada run tem idempotency_key = hash(correlation_id + step + input_digest).
    Reexecução com a mesma key não duplica efeito (consulta event log antes de aplicar).
- Retry: backoff exponencial com jitter; máximo configurável; só para falhas transitórias.
- Timeout: por run e por workflow; timeout emite RunTimedOut → política de retry/fallback/escalonamento.
- Dead-letter: runs que esgotam retries vão para DLQ + incidente (13).
```

## 5.7 Node State Machine

Aplica as transições de `02 §5.4-5.5`. Transições válidas são explícitas (qualquer outra é rejeitada e logada como `invalid_transition`):

```txt
suggested → draft → pending_approval → active → running → (completed | blocked | failed)
running → waiting_input → running
completed → archived | reopened
qualquer → blocked (por Metacognik/permissão); blocked → active (após resolução)
```

## 5.8 Approval Gate (runtime)

- Materializa `04` em tempo de execução. Quando um passo requer aprovação (por nível de autonomia, risco, custo, reversibilidade, dados sensíveis), o workflow entra em `waiting_approval` e emite `ApprovalRequested` com o approval object (04 §5.6).
- O run **não** prossegue até `ApprovalGranted`. `ApprovalDenied` → `changes_requested` ou rollback. `expires_at` → escalonamento (04 §5.8).
- Auto-approval (04 §5.3) é avaliado pelo Policy Engine (12) — se permitido, emite `AutoApproved` e segue.

## 5.9 Streaming de diagnóstico vivo

O diagnóstico não espera o fim. Cada `PartialOutputProduced`, `HypothesisCreated`, `GapDetected`, `RiskDetected`, `ConfidenceChanged` é publicado no bus e projetado para a UI via SSE/WebSocket em tempo real. É isto que torna o "diagnóstico vivo" (Constituição P2) um mecanismo, não uma promessa.

## 5.10 Artifact Generation Pipeline

`ArtifactRequested → render/compose → validate (QA Lead/eval) → store binary (storage) → register metadata (11) → ArtifactGenerated`. Artifacts versionados; nunca sobrescritos (nova versão + lineage em 11).

## 5.11 Human-in-the-Loop (HITL)

Pontos de intervenção: aprovar/editar/rejeitar nodes; responder perguntas do briefing; aprovar gates; pausar/abortar workflow; override de decisão de agente. Todo HITL vira evento (rastreável e auditável).

## 5.12 Real-time UI Projection (CQRS)

Projectors consomem o event log e mantêm read models otimizados para leitura. A UI (Product 14–16) lê projeções — **nunca** escreve estado diretamente; ela emite intenções/eventos. Ver schemas completos das 13 projeções em `11_DATA_MODEL §21`.

### 5.12.1 Live Projection Streaming — SSE e Polling *(Patch 1.1.1 — P10-1)*

O `ui_projection_engine` entrega atualizações de projeção para a UI via dois canais:

**SSE (Server-Sent Events)** — push em tempo real para projeções que mudam com alta frequência e são críticas para experiência do usuário:

```txt
Fluxo canônico de atualização de projeção:

Event emitido no event_bus
  → ui_projection_engine recebe evento
  → atualiza tabela de projeção tipada (11 §21)
  → verifica permissão do ator conectado (policy_engine)
  → se autorizado: envia SSE update para conexões abertas daquele project_id
  → se não autorizado: filtra silenciosamente (permission_filtered)
  → frontend recebe delta e re-renderiza widget afetado
  → frontend NUNCA recalcula source-of-truth — apenas renderiza a projeção
```

**Projeções com delivery SSE** (alta frequência, críticas para UX):

| Projeção | Trigger de push | Justificativa |
|---|---|---|
| `project_pulse_projection` | Qualquer mudança de estado de agente, node ou workflow | Home operacional — deve refletir realidade em <2s |
| `agent_activity_projection` | `AgentRunStarted | AgentRunCompleted | AgentBlocked` | Agentes rodando em tempo real |
| `node_health_projection` | `NodeStateChanged | RiskDetected | ApprovalRequested` | Bloqueios devem aparecer imediatamente |
| `decision_queue_projection` | `ApprovalRequested | ApprovalExpired | ApprovalEscalated` | Decisões urgentes não devem esperar polling |
| `approval_projection` | `ApprovalRequested | ApprovalSubmitted | ApprovalEscalated` | Gate de workflow — crítico |
| `canvas_graph_projection` | `NodeCreated | NodeEdgeCreated | NodeStateChanged` | Canvas visual — latência perceptível inaceitável |
| `command_center_context_projection` | `IntentSubmitted | AgentRunCompleted | RiskDetected` | Sugestões contextuais devem refletir estado atual |

**Projeções com delivery Polling** (baixa frequência, não críticas para loop imediato):

| Projeção | Intervalo | Justificativa |
|---|---|---|
| `cost_credit_projection` | 60s | Custo não muda a cada segundo; polling suficiente |
| `roi_snapshot_projection` | 60s | Calculado por agente; atualizações são raras |
| `feedback_loop_projection` | 30s | Feedback não é tempo-real |
| `support_friction_projection` | 120s | Tickets não mudam em segundos |
| `artifact_feed_projection` | 30s | Artifacts gerados têm latência de workflow |
| `risk_gap_evidence_projection` | 30s | Risks detectados por diagnóstico periódico |

**Estados internos de projeção** (gerenciados pelo `ui_projection_engine`):

```txt
projection_created      -- projeção inicializada (projeto novo)
projection_updated      -- evento processado; projeção atualizada
projection_stale        -- projeção não foi atualizada dentro do TTL esperado
projection_permission_filtered -- dado calculado mas filtrado por permissão do ator
projection_failed       -- erro ao processar evento; projeção em estado anterior
projection_rebuilt      -- reconstrução completa a partir do event store (após falha ou migração)
```

**Regras obrigatórias do projection engine:**

1. **Permissão é pré-condição, não pós-filtro.** A projeção é calculada completa pelo engine; o filtro por permissão ocorre *antes* do envio via SSE/response — o ator nunca recebe dado que o policy_engine nega.
2. **Staleness é exposta, não silenciada.** `ui_projections.is_stale = true` aparece na UI como timestamp "última atualização: N min atrás" — nunca apresentado como dado atual sem sinalização.
3. **Frontend não recalcula verdade.** Toda projeção recebida é terminal — frontend não deve derivar estado a partir de outros campos da projeção.
4. **Rebuild é transparente.** `projection_rebuilt` pode ser disparado manualmente (admin) ou automaticamente após falha; durante rebuild, UI recebe projeção do estado anterior com `is_stale=true`.
5. **SSE connections são por project_id + user_id.** Não há SSE global; cada conexão é escopada ao projeto e ao ator autenticado, com token efêmero de projeto (12 §5.6).
6. **Disconnect gracioso.** Se SSE cai, frontend volta para polling até reconectar. Nenhuma divergência de estado possível — projeção é sempre reconstruível do event store.

## 5.13 Rollback

Como o sistema é event-sourced, rollback é **compensação**, não DELETE: emite-se eventos compensatórios (`NodeReverted`, `ArtifactSuperseded`, `DecisionRetracted`) que projetam o estado de volta, preservando o histórico. Ações externas irreversíveis (envio, pagamento, deploy) **não** entram em fluxo automático sem approval (por isso o gate em §5.8).

## 5.14 Runtime Registries

Registries são catálogos versionados e auditáveis que o runtime consulta para resolver "o que existe e como usar". São **dados de configuração**, não código: o runtime carrega o registry, valida contra schema (5.20) e injeta no engine correspondente. Toda entrada de registry tem `id`, `version`, `status`, `owner` e `eval_ref` quando aplicável.

| Registry | Função | Input | Output | Relação com runtime |
|---|---|---|---|---|
| `agentRegistry` | catálogo de agentes/superagents (03) | agent_id | definição: papel, capacidades, memória, permissões | consultado pelo `agent_router` |
| `squadRegistry` | composições de agentes para objetivos recorrentes | squad_id | conjunto de agentes + ordem/handoffs | usado por `workflow_engine` |
| `skillRegistry` | skills (06) | skill_id | inputs/outputs/tools/autonomia/eval_ref | resolve execução de skill |
| `skillChainRegistry` | sequências reutilizáveis de skills | chain_id | cadeia ordenada + gates | usado por `workflow_engine` |
| `toolRegistry` | tools internas/externas | tool_id | contrato, custo, permissão | `tool_router` |
| `collectorRegistry` | collectors (5.18) | collector_type | provider+actor+normalizer refs | `collector_runner` |
| `providerRegistry` | APIs externas | provider_id | endpoints, limites, auth ref | nunca exposto ao frontend |
| `actorRegistry` | executores técnicos internos (5.18) | actor_id | credencial ref, escopo | resolvido server-side |
| `promptRegistry` | prompts (08) | prompt_id | template + slots + critérios | injeta no `model_router` |
| `instructionRegistry` | instruções persistentes de comportamento | instruction_id | regra + escopo | aplicado ao context pack |
| `transformerRegistry` | transformers (09) | transformer_id | input_object→output_object | `workflow_engine` |
| `modelRegistry` | modelos disponíveis | model_id | capacidade, preço, limites | `model_router` |
| `workflowRegistry` | blueprints (07) | workflow_id | máquina de estado + gates | `workflow_engine` |
| `nodeTypeRegistry` | tipos de node (16) | node_type | schema, lifecycle, owner | `state_machine_engine` + Canvas |
| `capabilityRegistry` | capabilities (5.17) | capability_id | o que habilita + gates | `policy_engine` + dashboard |
| `policyRegistry` | políticas de autorização/operação | policy_id | regra `pode(ator,ação,recurso,ctx)` | `policy_engine` |
| `approvalPolicyRegistry` | quando exigir aprovação (04) | action/risk | gate + aprovadores | `approval_gate` |
| `memoryPolicyRegistry` | gravação/expiração/permissão de memória (05) | memory_type | regra de write/retain/filter | `memory_retriever` |
| `evalRegistry` | golden sets e rubricas (13) | eval_id | critérios + baseline | `eval_runner` |
| `schemaRegistry` | contratos de output (5.20) | schema_id | JSON schema | valida outputs de agente |
| `artifactRegistry` | tipos de artifact | artifact_type | template, versão, storage policy | `artifact_pipeline` |
| `costPolicyRegistry` | orçamentos e limites (5.23) | scope | limites + ações | `cost_guard` |
| `stateMachineRegistry` | máquinas de estado (5.25) | machine_id | estados + transições válidas | `state_machine_engine` |

## 5.15 Runtime Engines

Engines são os processos ativos que consomem registries + eventos e executam. Diferem de registries (dados) por terem comportamento.

| Engine | Responsabilidade |
|---|---|
| `intent_router` | classifica a intenção de entrada e roteia para workflow/skill/agente |
| `event_bus` | pub/sub que distribui eventos aos consumidores (§5.3) |
| `event_store` | persistência append-only dos eventos (fonte de verdade) |
| `workflow_engine` | instancia e conduz workflows como máquinas de estado (§5.4) |
| `agent_router` | resolve agente a partir de intenção/skill, respeitando permissões |
| `model_router` | escolhe modelo por custo×qualidade com fallback (§5.5, 13) |
| `tool_router` | habilita interseção de tools permitidas (skill∩agente∩projeto) |
| `collector_runner` | executa collectors server-side (5.18) |
| `context_pack_builder` | monta o context packet antes de cada chamada de IA (5.19) |
| `memory_retriever` | recupera memória curta/média/longa sob política (05/12) |
| `rag_retriever` | recuperação semântica com filtro de permissão e ranking (05) |
| `policy_engine` | avalia `pode(ator,ação,recurso,ctx)` (12) — deny-by-default |
| `approval_gate` | pausa execução aguardando aprovação (04/§5.8) |
| `eval_runner` | roda evals/scores em runs e outputs (13) |
| `cost_guard` | contabiliza custo e aplica throttle/budget (5.23) |
| `loop_detector` | detecta ciclos de agentes via causation_id + profundidade (§5.12) |
| `state_machine_engine` | aplica transições válidas de node/run/workflow/approval/artifact/collector (5.25) |
| `artifact_pipeline` | renderiza→valida→armazena→registra artifacts (§5.10) |
| `ui_projection_engine` | mantém read models e faz streaming para a UI (§5.12) |
| `learning_loop_engine` | agrega outcomes em aprendizado (5.28) |

## 5.16 Agent Event Communication Protocol

**Agentes não conversam apenas por texto livre — conversam por eventos estruturados.** Texto é payload de um evento, não o canal. Isso garante rastreabilidade, validação por policy, auditoria por Metacognik e replay (5.26).

Tabelas/streams de evento de agente (todas com `org_id`, `workspace_id`, `project_id`, `correlation_id`, `causation_id`, `occurred_at` — ver 11):

| Stream/tabela | Registra |
|---|---|
| `agent_events` | todo evento emitido/consumido por um agente |
| `agent_runs` | execução do agente (espelha `run` de 11/03) |
| `agent_handoffs` | transferência entre agentes (handoff protocol 03 §5.4) |
| `agent_outputs` | outputs estruturados validados por schema (5.20) |
| `agent_decisions` | decisões registradas com evidência |
| `agent_tool_calls` | chamadas de tool com input/output/custo |
| `agent_errors` | falhas, exceções, timeouts |
| `agent_costs` | custo por run/modelo/tool (5.23) |
| `agent_context_reads` | o que foi lido do context pack/memória (auditoria de RAG) |
| `agent_memory_writes` | gravações de memória (05/11) |
| `agent_eval_results` | scores de qualidade (13) |
| `agent_approval_requests` | pedidos de aprovação emitidos (04) |
| `agent_state_transitions` | mudanças no `agent_run` state machine (5.25) |

Fluxo estruturado:

```txt
agent emits event
→ policy_engine valida (pode emitir? pode chamar este alvo/tool?) (12)
→ event_bus roteia
→ target agent recebe payload ESTRUTURADO (não texto solto) validado por schema (5.20)
→ output / decision / handoff (também eventos estruturados)
→ Metacognik audita (confiança, evidência, risco) (13)
→ Nick traduz/explica ao usuário
```

## 5.17 Capability Activation System

Nem todo projeto começa com e-commerce, ads, CRM, eventos ou social intelligence (Constituição P1). Capabilities são módulos **ativáveis por contexto**, não páginas default. O runtime nunca ativa capability por default — só via lógica de ativação (02 §5.6) e `policy_engine`.

Schema de capability (no `capabilityRegistry`):

```yaml
capability_id:
display_name:
when_to_activate:        # condições/gatilhos
required_inputs:
optional_inputs:
node_types_enabled:      # do nodeTypeRegistry
agents_enabled:          # do agentRegistry
skills_enabled:          # do skillRegistry
tools_enabled:           # do toolRegistry
collectors_enabled:      # do collectorRegistry
default_dashboards:      # projeções sugeridas (14)
approval_required:       # enum (04/12)
cost_profile:            # perfil de custo esperado (5.23)
risk_level:              # baixo/médio/alto
```

Ativar uma capability emite `CapabilityActivated`, habilita seus node types/agents/skills/tools/collectors e sugere dashboards — tudo sob approval quando `approval_required`/`risk_level` exigir.

## 5.18 Collector Runtime Architecture

Distinção obrigatória:

- **Collector** = abstração CKOS, visível para o produto. "Quero coletar comentários do Instagram." É o que a UI conhece.
- **Actor** = executor técnico interno (conta/credencial/sessão) que realiza a coleta. Invisível ao frontend.
- **Provider** = fornecedor/API externa (Apify, plataforma social, etc.).

Regras duras de segurança (12):

```txt
Frontend NUNCA chama provider direto.
Frontend NUNCA expõe token/segredo.
Frontend NUNCA expõe actor id.
Frontend chama APENAS: POST /api/collectors/run  { collector_type, params }
```

Fluxo:

```txt
collector_type
→ collectorRegistry (resolve definição)
→ policy check (12: pode este projeto/usuário usar este collector?)
→ providerRegistry (resolve API externa)
→ actorRegistry (resolve executor/credencial, server-side, via vault)
→ collectorRunner (executa)
→ normalizer (CollectorNormalizedOutput, schema 5.20)
→ persistence (11)
→ event emitted (collector_run.* + node/evidence)
→ UI projection (§5.12)
```

Arquivos futuros recomendados (referência de implementação, **não criar agora**):

```txt
src/server/collectors/collectorRegistry.ts
src/server/collectors/actorRegistry.ts
src/server/collectors/providerRegistry.ts
src/server/collectors/collectorRunner.ts
src/server/collectors/collectorNormalizer.ts
src/server/collectors/collectorSchemas.ts
src/server/collectors/collectorPolicies.ts
src/server/collectors/collectorTypes.ts
```

## 5.19 Context Pack Builder

Antes de **qualquer** chamada de IA, o `context_pack_builder` (engine) monta um pacote mínimo suficiente (materializa 05 §5.7). Conteúdo:

```txt
project context · user intent · active node · active workflow · recent events
· relevant memories · RAG results · permissions (12) · risk level · budget constraints (5.23)
· agent instructions (instructionRegistry) · output schema (5.20) · forbidden actions
```

Context budgeting (evita estouro de janela e custo):

```yaml
max_tokens:
priority_sources:        # ordem de inclusão sob escassez
excluded_sources:
freshness_window:        # idade máxima de evidência/memória
memory_depth:            # curta/média/longa a incluir
rag_top_k:
compression_strategy:    # truncate | summarize | hierarchical
summary_required:        # bool
```

O context pack é logado em `agent_context_reads` (5.16) para auditoria e replay.

## 5.20 Schema / Contract Registry

Todo output importante tem **contrato** (JSON schema no `schemaRegistry`). Output que não valida contra o schema é rejeitado pelo runtime antes de virar evento/decisão. Contratos mínimos:

```txt
HypothesisOutput · RiskOutput · GapOutput · NodeCreationOutput
ProposalSectionOutput · DecisionOutput · ApprovalRequestOutput · CollectorNormalizedOutput
```

Cada contrato define campos obrigatórios, tipos, e referências (ex.: `HypothesisOutput` exige `confidence`, `evidence_refs`, `gaps`, `source`). Validação de schema é um quality gate barato e determinístico antes dos evals semânticos (13).

## 5.21 Evidence Trail + Hypothesis System

Toda hipótese deve ter **evidência, confiança, lacuna e origem**. Estruturas (11):

```txt
evidence_items(id, project_id, content, source_type, source_owner,
               source_reliability_score, source_freshness_score, last_verified_at, expiration_policy)
hypothesis_evidence_links(hypothesis_id, evidence_id, link_type, weight)
confidence_scores(hypothesis_id, score, computed_by, computed_at)
```

Campos de qualidade de fonte:

```txt
source_reliability_score   # quão confiável é a origem
source_freshness_score     # quão recente
source_type                # approved_decision | contract | db_record | user | artifact | retrieved_doc | agent_inference | web | weak
source_owner               # quem produziu
last_verified_at
expiration_policy          # quando revalidar/expirar (05 §5.8)
```

Hierarquia de confiança (05 §5.5) decide qual evidência prevalece em conflito; `contradiction` score (13) sinaliza divergências para Metacognik.

## 5.22 Decision Rights Matrix

Quem pode decidir o quê, ligada ao `approvalPolicyRegistry` e a 04/12:

```yaml
decision_type:
allowed_approvers:       # quem pode aprovar
required_approvers:      # quem PRECISA aprovar
auto_approval_allowed:   # bool (só baixo risco/reversível)
risk_level:
rollback_required:       # bool
audit_required:          # bool
```

Papéis (naming freeze):

```txt
Nick        → sugere
Cognik      → interpreta
Metacognik  → bloqueia / audita
PMO_CKOS    → recomenda
Founder     → aprova decisões estruturais (visão, arquitetura, preço, naming, deploy)
Cliente     → aprova escopo / proposta / contrato
QA Lead     → aprova qualidade técnica
```

## 5.23 Cost Guard + Budget Runtime

O `cost_guard` aplica limites do `costPolicyRegistry` por escopo:

```txt
project · client · agent · workflow · run · model · tool · collector · day · month
```

Estados de custo:

```txt
within_budget · approaching_limit · blocked_by_cost · needs_approval
· loop_detected · expensive_model_invoked
```

`approaching_limit` → alerta (13); `blocked_by_cost` → enfileira/pausa não-críticos; ação crítica acima do limite → `needs_approval` (liga em 04: custo > limite → approval). Cotas por tenant evitam que um cliente consuma a capacidade de outro (12).

## 5.24 Eval Hooks + Quality Gates

Hooks de avaliação plugados no `eval_runner` (13), disparados em pontos do fluxo (§5.2):

```txt
agent evals · skill evals · workflow evals · output evals · RAG retrieval evals
· evidence coverage · contradiction detection · hallucination checks
· uncertainty score · quality regression
```

Cada hook produz score persistido em `agent_eval_results` (5.16). Gates: output que falha schema (5.20) ou eval crítico não avança; queda de baseline dispara `quality regression` (13 §5.9) — pré-requisito para liberar autonomia (21).

## 5.25 State Machine Registry

Máquinas de estado registradas no `stateMachineRegistry` e aplicadas pelo `state_machine_engine`. Transições inválidas são rejeitadas e logadas como `invalid_transition`.

```txt
agent_run:
  created · queued · running · waiting_tool · waiting_external_source · waiting_approval
  · paused · retrying · completed · failed · cancelled · expired

node:
  suggested · draft · active · running · waiting_input · waiting_approval · completed · archived · blocked

workflow_run:
  created · planned · queued · running · waiting_agent · waiting_tool · waiting_approval
  · completed · failed · cancelled · rolled_back

approval:
  requested · approved · rejected · expired · revoked · escalated

artifact:
  draft · generated · under_review · approved · rejected · published · archived · versioned

collector_run:
  requested · authorized · queued · running · waiting_provider · normalizing
  · completed · failed · rate_limited · cancelled
```

## 5.26 Run Replay

Todo run deve permitir abrir e inspecionar (reconstruído a partir do event store, §5.3):

```txt
input · contexto usado (context pack, 5.19) · agentes chamados · modelos usados
· custo · ferramentas executadas · outputs · decisões · aprovações · erros · eventos causais
```

Replay serve para debug, auditoria e reavaliação com nova rubrica (13). É possível porque tudo é event-sourced — não exige logging paralelo.

## 5.27 Sandbox / Simulation Mode

Modos de execução de uma ação/run:

```txt
draft · simulation · pending_approval · approved · executed · rolled_back
```

Regra: **nenhuma ação sensível entra em `executed` sem passar por `simulation`/`pending_approval` quando `risk_level` exigir.** A simulação roda em ambiente isolado (sem efeito externo, sem segredos reais — 12), produz outputs/custos previstos e alimenta o approval request (04). Base para o Self-Evolving (21 §5.4).

## 5.28 Learning Loop

O `learning_loop_engine` agrega resultados em aprendizado persistente (memória longa, 11):

```txt
lessons_learned · decision_outcomes · workflow_performance · agent_performance
· prompt_performance · skill_performance · node_performance
```

Cada item liga causa→efeito (decisão→resultado, prompt→qualidade, skill→retrabalho) e ajusta thresholds/políticas (13) e prioridades de roteamento. É o substrato que permite o sistema "ficar melhor" — e pré-condição do Self-Evolving (25).

## 5.29 MVP P0 vs Arquitetura Completa

Separação explícita para evitar over-engineering precoce. Esta seção é o **escopo mínimo executável**; o resto é evolução.

**MVP P0 (mínimo para o runtime funcionar de ponta a ponta):**

```txt
intent_router · event_bus (simples) · event_store · agent_router
· workflow_engine (básico) · context_pack_builder · approval_gate
· state_machine_engine · cost_guard (básico) · eval_runner (básico) · ui_projection_engine (básico)
+ registries essenciais: agentRegistry, skillRegistry, toolRegistry, workflowRegistry,
  nodeTypeRegistry, policyRegistry, approvalPolicyRegistry, schemaRegistry, stateMachineRegistry
```

**Depois (arquitetura completa):**

```txt
capabilityRegistry avançado · model_router sofisticado · loop_detector avançado
· self-evolving system (21) · sandbox/simulation avançado · run replay completo
· collector runtime completo · learning_loop_engine · squadRegistry/skillChainRegistry
```

# 6. Agente responsável

Owner documental `PMO_CKOS`; owner técnico `Builder Lead`.

# 7. Superagentes envolvidos

Nick (ingress); Cognik (intent/transformers); Metacognik (audit gate); PMO_CKOS (governança); Builder Lead (implementação do runtime); QA Lead (validação); Datta (consistência de dados/eventos).

# 8. Skills necessárias

intent-routing; agent-routing; run-logging; workflow-orchestration; approval-routing; memory-write; rollback-assessment.

# 9. Prompts relacionados

Não aplicável — documento de arquitetura. Prompts de execução vivem em `08`.

# 10. Integrações

Postgres + event store (11); Redis (queue/cache/locks); OpenRouter (model router); tools externas via Tool Router; permission engine (12); tracer/metrics (13).

# 11. Memória e contexto

O Context Assembler (§5.2 passo 3) monta o Context Packet (05 §5.7) consultando as 3 camadas de memória (11). O Memory Writer (§5.2 passo 13) persiste decisões/aprendizados conforme política de `05`.

# 12. Edge cases

- **Evento duplicado** → idempotency_key + dedupe por `event_id`.
- **Run órfão** (worker morreu) → heartbeat + lease expira → re-enqueue idempotente.
- **Modelo indisponível** → Model Router faz fallback (13); se todos falharem, run → `failed` + incidente.
- **Tool timeout** → retry/backoff; depois DLQ.
- **Approval expirado** → escalonamento (04 §5.8).
- **Projeção atrasada** (lag) → UI mostra "sincronizando"; nunca lê estado obsoleto como verdade.
- **Loop de agentes** (A chama B chama A) → detector de ciclo via `causation_id` + limite de profundidade → `loop_detected` + Metacognik.

# 13. Métricas de sucesso

Latência intenção→primeiro evento; throughput de runs/min; taxa de retry; nº de runs órfãos (meta ~0); lag de projeção (p95); custo/run e custo/projeto (13); % de execuções com trace completo; tempo de rollback.

# 14. Critérios de aprovação

Aprovado quando: o fluxo §5.2 é completo e rastreável; event log é append-only; workflows são máquinas de estado dirigidas por eventos; routers respeitam permissões (12) e política de custo (13); approval gate pausa execução real; rollback é por compensação; projeção alimenta UI em tempo real.

# 15. Critérios de reprovação

Reprovado se: estado vive fora do event log; UI escreve estado direto; runs sem idempotency/trace; approval é cosmético; rollback é DELETE destrutivo; sem isolamento de carga por tenant.

# 16. Related notes

- [[02_AI_FIRST_OBJECT_MODEL]]
- [[03_AGENT_OPERATING_MODEL]]
- [[04_AUTONOMY_AND_APPROVALS]]
- [[11_DATA_MODEL_AND_PERSISTENCE]]
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]]
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]]
