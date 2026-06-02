---
title: Node Canvas Architecture
file: 16_NODE_CANVAS_ARCHITECTURE.md
phase: 04_PRODUCT_SYSTEM
category: product_architecture
version: 1.2.0
status: draft
owner: PMO_CKOS
responsible_agent: Cognik
reviewers:
  - Metacognik
  - QA_Lead
approval_required:
  - founder
  - metacognik
purpose: >
  Definir o Node Canvas como superfície visual operacional do CKOS — projeção interativa
  de objetos, eventos, workflows, estados e aprovações do Runtime. Não é ferramenta de
  desenho, não é fonte da verdade, não escreve estado diretamente.
inputs: >
  Runtime Architecture (10 v1.1.0); Data Model (11 v1.1.2); Security (12 v1.1.0);
  Evals (13 v1.1.0); Command Center (15 v1.2.1); Object Model (02); Workflow Blueprints (07)
outputs: >
  Definição completa de node types (20 famílias); edge schema; canvas events;
  state machines visíveis; relação com ui_projections; MVP P0; gaps registrados.
framework: >
  Canvas exibe projeção de objetos do Runtime. Todo estado nasce no Runtime via evento.
  Canvas emite intenções para o Command Center; nunca escreve estado diretamente.
edge_cases: >
  Canvas sobrecarregado; node duplicado por agente; edge incompatível; state machine
  em conflito com projeção; node de outro tenant; approval sem permissão; node orfão.
integrations: >
  Lê de ui_projections (11 §21); emite intenções via Command Center (15);
  consome event bus (10 §5.3); permissões via Security (12); evals via Metacognik (13).
prompts: Sugerir nodes; conectar nodes; audit de canvas; diagnóstico de lacunas.
metrics: >
  Nodes úteis criados; % nodes com evidência; % nodes com owner; tempo node→workflow;
  nº de decisões por canvas; nº de approvals completados; redução de redundância.
related_notes:
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../03_RUNTIME_SYSTEM/13_EVALS_QUALITY_CONFIDENCE.md
  - 14_PROJECT_DASHBOARD_ARCHITECTURE.md
  - 15_COMMAND_CENTER_ARCHITECTURE.md
  - ../01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md
  - ../02_EXECUTION_SYSTEM/07_WORKFLOW_BLUEPRINTS.md
  - ../ARCHITECTURE_PATCH_REPORT.md
  - ../QA_DOCUMENTATION_CHECKLIST.md
tags: [product, canvas, nodes, graph, realtime, projections, state-machine]
---

> **Node Canvas não é a fonte da verdade. Node Canvas é a superfície visual operacional para objetos, eventos, workflows, estados e aprovações do Runtime.**
>
> O Canvas renderiza projeções. O estado vive no Runtime (doc 10). A persistência vive no Data Model (doc 11). A segurança é imposta pelo policy engine (doc 12). A qualidade é auditada pelos Evals (doc 13).
>
> Toda ação no Canvas é uma intenção — emitida para o Command Center (doc 15) ou diretamente como evento de intenção para o Runtime. Nenhuma ação no Canvas escreve estado diretamente em tabelas de domínio.

# 1. Propósito

O **Node Canvas** é a superfície visual operacional do CKOS onde usuários e agentes interagem com o grafo de objetos vivos de um projeto. Não é um quadro de notas adesivas, não é um editor de fluxos decorativo, não é uma ferramenta de brainstorm. É a **interface de operação do projeto em tempo real**.

O Node Canvas deve permitir:

- Visualizar todos os objetos operacionais de um projeto (nodes) e suas relações (edges) como grafo vivo.
- Criar nodes manualmente ou aceitar sugestões de agentes, ancorados em objetos reais do Runtime.
- Conectar nodes com edges tipadas que representam relações causais, dependências, evidências e aprovações.
- Visualizar o estado atual de cada node via state machine (sugerido, ativo, bloqueado, aprovado, etc.).
- Acompanhar execução de workflows em tempo real — ver quais nodes estão rodando, qual agente está ativo, qual passo está pendente.
- Acionar aprovações e registrar decisões diretamente no contexto do node.
- Ver evidências, hipóteses, confidence scores, gaps e riscos associados a cada node.
- Auditar quem criou, modificou, executou e aprovou cada node (lineage completo).
- Visualizar custos estimados, uso de créditos e impacto de ROI associados a nodes e workflows.
- Interagir com agentes (ver qual agente está atuando em qual node; ver estado do agente).
- Receber sugestões contextuais de novos nodes, conexões, diagnósticos e alertas.
- Exportar o canvas como artefato de comunicação (snapshot, PDF, apresentação).
- Navegar por versões anteriores do canvas (replay de eventos).
- Filtrar e buscar nodes por tipo, estado, agente, data, confiança, risco, aprovação.

O Canvas **não** cria lógica de negócio. O Canvas **não** executa agentes diretamente. O Canvas **não** resolve workflows. O Canvas é a superfície — o cérebro é o Runtime.

# 2. Função dentro do CKOS

O Node Canvas ocupa uma camada específica dentro da arquitetura, com relações bem definidas com cada componente do sistema:

| Componente | Relação com o Canvas |
|---|---|
| **Command Center (15)** | Entrada de intenção textual e slash commands. Canvas recebe projeções do CC; CC recebe intenções do Canvas quando o usuário aciona ação via node. |
| **Node Canvas (este doc)** | Superfície visual operacional. Renderiza projeções. Emite intenções. |
| **Project Dashboard (14)** | Visão executiva longitudinal — KPIs, tendências, resumos. Canvas é operacional (objeto a objeto); Dashboard é gerencial (projeto como todo). |
| **Runtime (10)** | Fonte da verdade de estado, eventos e execução. Canvas nunca escreve no Runtime diretamente — emite eventos de intenção que o Runtime processa. |
| **Data Model (11)** | Persistência de nodes, edges, events, projections, approvals. Canvas lê de `ui_projections` (11 §21), nunca de tabelas de domínio direto. |
| **Security (12)** | RBAC + ABAC + RLS + tenant isolation. Canvas respeita permissões — não renderiza o que o usuário não pode ver; mostra versão redigida quando permitido. |
| **Evals / Metacognik (13)** | Confiança, qualidade e auditoria. Canvas exibe `confidence_score`, warnings de Metacognik, e estados de auditoria sem executar julgamento próprio. |

Fluxo canônico de intenção via Canvas:

```txt
Usuário aciona ação no Canvas
  → IntentSubmitted (ou NodeActionTriggered)
  → Command Center (15) / intent_router (10)
  → context_pack_builder → policy_engine
  → workflow_engine → agent_router → model_router
  → approval_gate (se necessário)
  → eval_runner / Metacognik
  → ui_projection_engine
  → Canvas atualiza projeção
```

# 3. Princípios do Node Canvas

1. **ui-projection-not-source-of-truth** — Canvas lê de `ui_projections` (doc 11 §21). Nunca lê diretamente de tabelas de domínio. Nunca calcula estado próprio.
2. **object-first** — Todo node é um objeto real do sistema (doc 02/11). Nodes decorativos sem objeto correspondente no Runtime são bloqueados.
3. **event-driven** — Toda mudança visível no Canvas é consequência de um evento no bus (doc 10 §5.3). Canvas não cria estado — exibe eventos.
4. **policy-controlled** — Toda ação do Canvas passa pelo `policy_engine` (doc 10 §5.5). Nenhuma ação contorna política de permissão.
5. **state-machine-aware** — Canvas exibe e respeita as state machines de node, workflow e approval (doc 10 §5.7). Não exibe transições impossíveis como disponíveis.
6. **approval-aware** — Canvas exibe `approval_status` em cada node que exige aprovação. Acionar execução sem aprovação é bloqueado visualmente e por política.
7. **cost-aware** — Canvas exibe `cost_estimate` e consumo de créditos por node e por workflow quando disponível. Não bloqueia por custo — apenas informa.
8. **evidence-aware** — Todo node deve ter pelo menos uma evidência vinculada ou um `confidence_score` visível. Nodes sem evidência exibem badge de alerta.
9. **agent-visible** — Canvas exibe qual agente está ativo em cada node, em qual estado (working, blocked, awaiting_approval, completed, audited).
10. **whitelabel-ready** — Canvas usa tokens de design do `design_system` ativo (branddock). Layout, cores e tipografia são parametrizados por tenant.
11. **mobile-readable** — Canvas MVP exibe nodes em modo read-only em mobile. Criação e edição em mobile são funcionalidades futuras (pós-MVP).
12. **manual-and-ai-created** — Nodes podem ser criados pelo usuário manualmente ou sugeridos/gerados por agentes. Ambas as origens são rastreadas.
13. **tenant-isolated** — Canvas nunca exibe nodes de outro tenant. RLS no nível de projeção garante isolamento (doc 12 §5.2).
14. **replay-capable** — Canvas deve permitir navegar por estados passados via replay de eventos. Isso requer event store append-only (doc 11 §4).

# 4. O que é um Node

Um **node** é um objeto vivo do CKOS — representa uma unidade de pensamento, execução, evidência, decisão ou produto dentro de um projeto. Não é um card estático. É uma entidade com estado, história, owner, evidências, custos, aprovações e conexões.

Todo node persiste na tabela `nodes` (doc 11 §4) e tem o seguinte schema:

```txt
id                   uuid           identificador único (PK)
node_type            enum           tipo do node (ver §5)
title                text           nome legível
description          text           descrição operacional (não decorativa)
status               enum           estado atual na state machine (ver §9)
state_machine        jsonb          snapshot da state machine atual
owner                uuid → users   quem é responsável por este node
project_id           uuid → projetos projeto ao qual pertence
workspace_id         uuid → workspaces workspace (tenant isolation)
tenant_id            uuid           tenant owner (RLS anchor)
created_by           uuid → users   quem criou (usuário ou agente)
source_type          enum           manual | ai_suggested | ai_generated | workflow_generated
source_event_id      uuid → events  evento que originou este node
related_workflow_id  uuid → workflows workflow que executa ou consome este node
related_agent_run_id uuid → agent_runs execução de agente que gerou/atuou neste node
related_artifact_id  uuid → artifacts artefato gerado por este node
risk_level           enum           low | medium | high | critical
confidence_score     float [0,1]    score de confiança do Evals (13)
evidence_links       uuid[]         array de evidências vinculadas
cost_estimate        jsonb          {credits_estimated, credits_consumed, currency}
approval_status      enum           not_required | requested | approved | rejected | expired
permissions_scope    jsonb          quem pode ver, editar, aprovar este node
last_updated         timestamp      última atualização (event-sourced)
```

> **Patch sugerido para doc 11 v1.2.x:** confirmar que a tabela `nodes` inclui todos os campos acima, especialmente `tenant_id` como coluna de RLS, `source_event_id` para rastreabilidade e `cost_estimate` jsonb. O schema atual de doc 11 §4 pode precisar de atualização antes da implementação.

# 5. Node Types

O Canvas organiza nodes em **20 famílias de tipo**. Cada família representa uma classe de objeto operacional com comportamento, criadores, eventos e permissões específicos.

## 5.1 Strategy

**Quando aparece:** diagnóstico inicial, planejamento estratégico, revisão de direção.
**Quem cria:** usuário (lead+) ou Cognik (sugerido).
**Eventos emitidos:** `NodeCreated{strategy}`, `StrategyDraftUpdated`, `StrategyApproved`.
**Agents/squads:** Cognik (análise), Metacognik (auditoria).
**Projections alimentadas:** `node_status_projection`, `project_pulse_projection`.
**Approvals exigidos:** lead ou founder para transição `draft → active`.

## 5.2 Briefing

**Quando aparece:** kickoff do projeto, onboarding de contexto, briefing vivo.
**Quem cria:** usuário (contributor+) ou Nick (via `/briefing`).
**Eventos emitidos:** `NodeCreated{briefing}`, `BriefingUpdated`, `BriefingApproved`.
**Agents/squads:** Nick (contextualização), Cognik (estruturação).
**Projections alimentadas:** `node_status_projection`, `command_center_suggestions`.
**Approvals exigidos:** lead para briefing formal.

## 5.3 Research

**Quando aparece:** fase de pesquisa, coleta de mercado, benchmarks.
**Quem cria:** usuário ou agente collector (via `/research`).
**Eventos emitidos:** `NodeCreated{research}`, `CollectorRunStarted`, `ResearchCompleted`.
**Agents/squads:** Research Subagent, Datta (validação).
**Projections alimentadas:** `node_status_projection`, `risk_projection`.
**Approvals exigidos:** não obrigatório; Metacognik pode sinalizar fontes não confiáveis.

## 5.4 Evidence

**Quando aparece:** toda vez que uma fonte, dado, resultado ou observação suporta outro node.
**Quem cria:** usuário, agente collector, ou automaticamente por collector run.
**Eventos emitidos:** `EvidenceAdded`, `EvidenceLinked`, `EvidenceContradicted`.
**Agents/squads:** Datta (validação), Metacognik (confiabilidade).
**Projections alimentadas:** `node_status_projection`, `risk_projection`.
**Approvals exigidos:** nenhum; Metacognik emite warning se confiança < threshold.

## 5.5 Hypothesis

**Quando aparece:** quando uma suposição precisa ser registrada, testada e confirmada ou refutada.
**Quem cria:** usuário ou Cognik (sugerido via análise de gaps).
**Eventos emitidos:** `HypothesisCreated`, `HypothesisTested`, `HypothesisConfirmed`, `HypothesisRefuted`.
**Agents/squads:** Cognik (geração), Metacognik (validação).
**Projections alimentadas:** `node_status_projection`, `risk_projection`.
**Approvals exigidos:** nenhum automático; hipóteses críticas podem exigir lead.

## 5.6 Risk

**Quando aparece:** identificação de ameaças, dependências críticas, lacunas de segurança ou viabilidade.
**Quem cria:** usuário, Metacognik (automático), ou Cognik (diagnóstico).
**Eventos emitidos:** `RiskDetected`, `RiskMitigated`, `RiskEscalated`.
**Agents/squads:** Metacognik (detecção automática), Cognik (análise).
**Projections alimentadas:** `risk_projection`, `project_pulse_projection`.
**Approvals exigidos:** risks `critical` exigem acknowledge explícito de lead+.

## 5.7 Gap

**Quando aparece:** quando o sistema ou usuário detecta informação ausente, capacidade não coberta, ou dependência não resolvida.
**Quem cria:** Cognik (automático via diagnóstico), Metacognik, ou usuário.
**Eventos emitidos:** `GapDetected`, `GapAddressed`, `GapPersists`.
**Agents/squads:** Cognik, Metacognik.
**Projections alimentadas:** `risk_projection`, `node_status_projection`.
**Approvals exigidos:** nenhum; gaps persistentes viram risks.

## 5.8 Workflow

**Quando aparece:** quando uma sequência de ações precisa ser orquestrada pelo workflow engine.
**Quem cria:** usuário (via `/workflow`) ou Runtime (automático ao conectar nodes dependentes).
**Eventos emitidos:** `WorkflowCreated`, `WorkflowStarted`, `WorkflowCompleted`, `WorkflowFailed`.
**Agents/squads:** Ops (orquestração), Agent Router (execução).
**Projections alimentadas:** `node_status_projection`, `agent_activity_projection`.
**Approvals exigidos:** workflows com impacto externo ou alto custo exigem approval antes de `queued → running`.

## 5.9 Agent

**Quando aparece:** quando um agente específico é atribuído a um node ou workflow.
**Quem cria:** agent_router (automático) ou usuário (atribuição manual).
**Eventos emitidos:** `AgentAssigned`, `AgentRunStarted`, `AgentRunCompleted`, `AgentBlocked`.
**Agents/squads:** qualquer agente do registry; Metacognik audita.
**Projections alimentadas:** `agent_activity_projection`.
**Approvals exigidos:** nenhum automático; alguns agentes têm approval_gate por policy (doc 12).

## 5.10 Collector

**Quando aparece:** quando uma coleta estruturada de dados externos é necessária (crawl, scrape, API call, etc.).
**Quem cria:** usuário (via `/research`, `/competitors`) ou Research Subagent.
**Eventos emitidos:** `CollectorRunStarted`, `CollectorRunCompleted`, `CollectorRunFailed`.
**Agents/squads:** Research Subagent, Datta.
**Projections alimentadas:** `node_status_projection`.
**Approvals exigidos:** collectors com acesso a dados sensíveis exigem lead+ approval.

## 5.11 Artifact

**Quando aparece:** quando um output concreto é gerado (proposta, relatório, imagem, vídeo, código, deck).
**Quem cria:** agente (via workflow) ou usuário (via `/artifact`).
**Eventos emitidos:** `ArtifactGenerated`, `ArtifactRevised`, `ArtifactApproved`, `ArtifactRejected`.
**Agents/squads:** Production Squad, Branddock (para brand artifacts).
**Projections alimentadas:** `node_status_projection`, `project_pulse_projection`.
**Approvals exigidos:** artifacts formais (propostas, publicações) exigem approval de lead+ ou cliente.

## 5.12 Approval

**Quando aparece:** quando uma decisão, workflow ou artefato requer autorização humana explícita.
**Quem cria:** approval_gate (automático via Runtime) ou usuário (manual).
**Eventos emitidos:** `ApprovalRequested`, `ApprovalSubmitted`, `ApprovalApproved`, `ApprovalRejected`, `ApprovalExpired`.
**Agents/squads:** nenhum executa — humano aprova; Metacognik pode bloquear.
**Projections alimentadas:** `approval_projection`.
**Approvals exigidos:** o próprio node é o mecanismo de approval.

## 5.13 Decision

**Quando aparece:** quando uma escolha irreversível ou de alto impacto é registrada para auditoria futura.
**Quem cria:** usuário (lead+) — decisões não podem ser criadas por agentes sozinhos.
**Eventos emitidos:** `DecisionRegistered`, `DecisionReversed` (raro, com justificativa).
**Agents/squads:** Nick (contextualiza a decisão), Metacognik (registra no audit log).
**Projections alimentadas:** `node_status_projection`, `project_pulse_projection`.
**Approvals exigidos:** decisões críticas exigem co-aprovação de founder.

## 5.14 ROI / Cost

**Quando aparece:** quando uma estimativa de retorno, custo ou impacto financeiro é calculada ou registrada.
**Quem cria:** usuário ou Cognik (estimativa automática baseada em workflow cost).
**Eventos emitidos:** `ROIEstimateCreated`, `CostUpdated`, `ROIRealized`.
**Agents/squads:** Cognik (cálculo), Datta (validação de premissas).
**Projections alimentadas:** `cost_projection`, `project_pulse_projection`.
**Approvals exigidos:** nenhum para estimativa; ROI realizado exige confirmação de lead+.

> **Gap §20.1:** Arquitetura de ROI não está definida — este node type é placeholder. Ver `ARCHITECTURE_PATCH_REPORT.md §12.1`.

## 5.15 Feedback

**Quando aparece:** quando um usuário, cliente ou agente registra avaliação qualitativa de um output ou processo.
**Quem cria:** usuário (via `/feedback`) ou Nick (ao detectar insatisfação em conversa).
**Eventos emitidos:** `FeedbackSubmitted`, `FeedbackProcessed`, `FeedbackLinkedToImprovement`.
**Agents/squads:** Nick (captura), Metacognik (categorização).
**Projections alimentadas:** `node_status_projection`.
**Approvals exigidos:** nenhum.

> **Gap §20.2:** Feedback System não está definido — ver `ARCHITECTURE_PATCH_REPORT.md §12.2`.

## 5.16 Support

**Quando aparece:** quando um usuário reporta um problema, dúvida ou bloqueio que requer intervenção.
**Quem cria:** usuário (via `/support`) ou Nick (ao detectar bloqueio em conversa).
**Eventos emitidos:** `SupportRequested`, `SupportAssigned`, `SupportResolved`.
**Agents/squads:** Nick (triagem), Ops (roteamento).
**Projections alimentadas:** `node_status_projection`.
**Approvals exigidos:** nenhum; escalamentos exigem lead.

> **Gap §20.3:** Support System não está definido — ver `ARCHITECTURE_PATCH_REPORT.md §12.3`.

## 5.17 Billing / Credits

**Quando aparece:** quando o consumo de créditos, plano, cobrança ou upgrade é relevante para o contexto do projeto.
**Quem cria:** sistema (automático via billing engine) — não criado por usuário nem agente diretamente.
**Eventos emitidos:** `CreditsConsumed`, `PlanLimitReached`, `BillingEventRegistered`.
**Agents/squads:** sistema de billing (externo ao Canvas).
**Projections alimentadas:** `cost_projection`.
**Approvals exigidos:** upgrades de plano exigem confirmação do usuário.

> **Gap §20.4:** Credits, Plans & Billing Architecture não está definida — ver `ARCHITECTURE_PATCH_REPORT.md §12.4`.

## 5.18 Campaign

**Quando aparece:** quando um esforço coordenado de marketing, vendas ou comunicação é planejado ou executado.
**Quem cria:** usuário (contributor+) ou agente de campanha (via workflow).
**Eventos emitidos:** `CampaignCreated`, `CampaignLaunched`, `CampaignCompleted`.
**Agents/squads:** Production Squad, Branddock, Research Subagent.
**Projections alimentadas:** `node_status_projection`, `project_pulse_projection`.
**Approvals exigidos:** lançamento de campanha exige approval de lead+.

## 5.19 Persona / Brand

**Quando aparece:** quando um público-alvo, buyer persona, arquétipo de marca ou identidade visual precisa ser registrado como objeto operacional.
**Quem cria:** usuário (contributor+) ou Branddock (geração a partir de briefing).
**Eventos emitidos:** `PersonaCreated`, `BrandTokenUpdated`, `PersonaValidated`.
**Agents/squads:** Branddock, Cognik.
**Projections alimentadas:** `node_status_projection`.
**Approvals exigidos:** personas formais exigem approval de lead.

## 5.20 System

**Quando aparece:** nodes especiais que representam o próprio sistema — integrações externas, configurações, capacidades habilitadas, limites de API.
**Quem cria:** sistema (automático) ou admin.
**Eventos emitidos:** `SystemNodeCreated`, `IntegrationConnected`, `CapabilityEnabled`.
**Agents/squads:** nenhum agente de conteúdo — apenas sistema e admin.
**Projections alimentadas:** `node_status_projection`.
**Approvals exigidos:** habilitação de novas capacidades exige admin.

# 6. Como Nodes são Criados

## 6.1 AI-created (agente gera node)

```txt
Usuário emite intenção (comando, conversa, contexto)
  → IntentSubmitted → intent_router
  → context_pack_builder monta o contexto do projeto
  → policy_engine valida (permissão, tenant, rate limit)
  → workflow_engine seleciona workflow adequado
  → agent_router seleciona agente
  → agente processa → emite NodeCreated{type, schema, source_event_id}
  → event bus persiste evento (doc 11 §4)
  → ui_projection_engine atualiza node_status_projection
  → Canvas recebe projeção atualizada → exibe novo node
```

Node criado por agente tem `source_type = ai_generated` ou `ai_suggested`. Se `ai_suggested`, o node aparece no Canvas em estado `suggested` — usuário precisa confirmar para `draft`.

## 6.2 Manual (usuário cria node)

```txt
Usuário abre painel "Novo node" no Canvas
  → seleciona node_type → preenche schema mínimo obrigatório
  → Canvas envia NodeCreateRequested ao Command Center
  → policy_engine valida (permissão de criação para este node_type)
  → Runtime persiste evento NodeCreated{source_type: manual}
  → state_machine inicializa em `draft`
  → audit_log registra criação com actor_id e timestamp
  → ui_projection_engine atualiza projeção → Canvas exibe
```

Nodes manuais têm `source_type = manual`. O Canvas nunca grava diretamente na tabela `nodes` — toda criação manual passa pelo mesmo fluxo de eventos.

# 7. Edges e Conexões

Edges representam relações tipadas entre nodes. Não são conexões decorativas — cada edge tem semântica, confiança e rastreabilidade.

## 7.1 Tipos de edge (14)

| Edge type | Semântica | Exemplo |
|---|---|---|
| `depends_on` | A não pode acontecer sem B | Workflow depende de Briefing aprovado |
| `informs` | A fornece contexto para B | Evidence informa Strategy |
| `blocks` | A impede B de avançar | Risk bloqueia Campaign launch |
| `generates` | A produz B como output | Workflow gera Artifact |
| `approves` | A é o aprovador formal de B | Approval node aprova Decision |
| `contradicts` | A contraria ou invalida B | Evidence contradiz Hypothesis |
| `supports` | A fortalece ou valida B | Evidence suporta Hypothesis |
| `replaces` | A substitui B (B é arquivado) | Nova Strategy substitui Strategy anterior |
| `triggers` | A dispara B automaticamente | Decision aciona Workflow |
| `belongs_to_workflow` | A faz parte do fluxo B | Task pertence a Workflow |
| `evidence_for` | A é evidência específica de B | Research é evidência de Strategy |
| `risk_for` | A representa risco de B | Risk está associado a Campaign |
| `cost_for` | A representa custo/estimativa de B | ROI/Cost node estima Workflow |
| `feedback_for` | A é feedback sobre B | Feedback está associado a Artifact |

## 7.2 Edge schema

```txt
source_node_id   uuid → nodes   node de origem
target_node_id   uuid → nodes   node de destino
edge_type        enum           tipo da conexão (tabela acima)
confidence       float [0,1]    confiança nesta conexão (calculado por Evals ou manual)
created_by       uuid           actor que criou a edge (usuário ou agente)
source_event_id  uuid → events  evento que originou esta edge
status           enum           active | inactive | invalidated
metadata         jsonb          dados adicionais específicos do tipo de edge
```

> **Patch sugerido para doc 11 v1.2.x:** a tabela `node_edges` com o schema acima precisa ser adicionada formalmente ao doc 11. O doc 11 §11 menciona `node_edge` implicitamente mas sem schema formal. Este patch deve ser aplicado antes da implementação do Canvas.

# 8. Canvas Events

O Canvas opera inteiramente via eventos do bus (doc 10 §5.3). Nenhum evento do Canvas executa diretamente — todos passam pelo Runtime.

| # | Evento | Origem | Destino no runtime |
|---|---|---|---|
| 1 | `NodeCreatedOnCanvas` | Usuário (manual) | `NodeCreateRequested → Runtime → NodeCreated` |
| 2 | `NodeUpdatedOnCanvas` | Usuário (edição) | `NodeUpdateRequested → Runtime → NodeUpdated` |
| 3 | `NodeDeletedOnCanvas` | Usuário (exclusão) | `NodeDeleteRequested → Runtime → policy → NodeArchived` |
| 4 | `EdgeCreatedOnCanvas` | Usuário (conexão manual) | `EdgeCreateRequested → Runtime → EdgeCreated` |
| 5 | `EdgeDeletedOnCanvas` | Usuário (remoção) | `EdgeDeleteRequested → Runtime → EdgeInvalidated` |
| 6 | `NodeActionTriggered` | Usuário (ação em node) | `IntentSubmitted → intent_router → workflow_engine` |
| 7 | `WorkflowStartedFromCanvas` | Usuário (via `/workflow` ou UI) | `WorkflowStartRequested → workflow_engine → WorkflowStarted` |
| 8 | `ApprovalRequestedFromCanvas` | Sistema (approval_gate) | `ApprovalRequested → approval_projection` |
| 9 | `ApprovalSubmittedFromCanvas` | Usuário (approve/reject) | `ApprovalSubmitted → approval_gate → ApprovalResolved` |
| 10 | `AgentAssignedFromCanvas` | Usuário (atribuição manual) | `AgentAssignRequested → agent_router → AgentAssigned` |
| 11 | `EvidenceLinkedOnCanvas` | Usuário (link manual) | `EvidenceLinkRequested → Runtime → EvidenceLinked` |
| 12 | `CanvasFilterApplied` | Usuário (filtro UI) | `ui_projection query params atualizados — sem evento de domínio` |
| 13 | `CanvasViewportChanged` | Usuário (navegação) | `estado local do Canvas — sem evento de domínio` |
| 14 | `NodeInspectorOpened` | Usuário (clique em node) | `leitura de projeção — sem evento de domínio` |
| 15 | `ManualNodeCreateRequested` | Usuário (painel de criação) | `NodeCreatedOnCanvas → fluxo §6.2` |
| 16 | `CanvasExportRequested` | Usuário (exportar canvas) | `ArtifactCreateRequested → workflow → snapshot gerado` |

Eventos 12, 13 e 14 são estado local de UI — não criam eventos de domínio. Todos os demais criam eventos persistidos no event store (doc 11 §4).

# 9. State Machines no Canvas

O Canvas exibe e respeita state machines — nunca as controla. Transições inválidas não são expostas como ações disponíveis.

## 9.1 State machine de Node

```txt
suggested
  → (usuário confirma) → draft
  → (submetido para aprovação) → pending_approval
    → (aprovado) → active
    → (rejeitado) → draft
  → (execução iniciada) → running
  → (aguarda input) → waiting_input
  → (aguarda aprovação em execução) → waiting_approval
  → (execução concluída) → completed
  → (arquivado) → archived
  → (bloqueado por risk/policy/Metacognik) → blocked
```

No Canvas: cada estado tem uma representação visual distinta (cor, badge, ícone). Transições disponíveis são exibidas como ações no inspector do node — apenas transições válidas pela state machine.

## 9.2 State machine de Workflow

```txt
created
  → planned
  → queued
  → running
    → waiting_agent    (aguarda agente disponível)
    → waiting_tool     (aguarda resultado de tool/collector)
    → waiting_approval (approval_gate acionado)
  → completed
  → failed
  → cancelled
  → rolled_back
```

Canvas exibe o estado atual do workflow no node de Workflow e nos nodes pertencentes a ele (via edge `belongs_to_workflow`).

## 9.3 State machine de Approval

```txt
requested
  → approved
  → rejected
  → expired    (timeout configurado por policy)
  → revoked    (cancelado pelo aprovador antes da decisão)
  → escalated  (sem resposta → próximo approver na hierarquia)
```

Canvas exibe approval nodes com contador de tempo restante quando configurado. `escalated` aciona notificação para o próximo approver registrado.

# 10. Relação com Agentes

O Canvas é a superfície onde a atividade de agentes se torna visível para o usuário.

**Fluxo de ação de agente no Canvas:**

```txt
Usuário aciona ação em node (ou evento automático dispara)
  → NodeActionTriggered → intent_router
  → agent_router seleciona agente adequado
  → agent_run criado → estado: working
  → Canvas exibe "Agente X trabalhando neste node"
  → agente conclui → emite output event
  → eval_runner / Metacognik avalia output
  → ui_projection_engine atualiza agent_activity_projection
  → Canvas exibe estado final: completed | blocked | audited
```

**Estados de agente visíveis no Canvas:**

| Estado | Significado visual |
|---|---|
| `working` | badge animado no node — agente está processando |
| `suggested` | node ou edge em estado de sugestão — aguarda confirmação |
| `blocked` | agente bloqueado por policy, risk ou dependência ausente |
| `awaiting_approval` | agente parou para aguardar decisão humana |
| `audited` | Metacognik emitiu avaliação — resultado visível no inspector |
| `completed` | agente concluiu — output disponível no node |

O Canvas nunca chama um agente diretamente. Todo `AgentAssignedFromCanvas` ou `NodeActionTriggered` passa pelo `agent_router` no Runtime.

# 11. Relação com Workflows

O Canvas é onde workflows se tornam visíveis como clusters de nodes conectados.

Canvas **sugere** — Runtime **cria**. Quando o usuário agrupa nodes e clica em "iniciar workflow", o Canvas emite `WorkflowStartRequested`. O workflow_engine valida, cria e executa. O Canvas exibe o resultado via projeção.

**7 exemplos de transformação de cluster → workflow:**

| Cluster de nodes | Workflow type |
|---|---|
| Strategy + Research + Evidence → Briefing | `briefing_generation_workflow` |
| Briefing + Persona + Campaign → Artifact | `campaign_production_workflow` |
| Risk + Gap + Hypothesis → Decision | `strategic_diagnosis_workflow` |
| Collector + Evidence + Hypothesis → Research | `competitive_research_workflow` |
| Artifact + Approval → Published | `artifact_approval_workflow` |
| Feedback + Support → Gap → Improvement | `feedback_to_improvement_workflow` |
| Strategy + ROI/Cost + Decision → Plan | `roi_planning_workflow` (gap §20.1) |

O Workflow node no Canvas exibe: estado atual, % de conclusão, nodes dependentes, agente ativo, tempo estimado, custo acumulado.

# 12. Relação com Evidências e Hipóteses

O Canvas expõe um **side panel de evidências** ao inspecionar qualquer node que suporte rastreabilidade epistêmica.

**Conteúdo do side panel de evidência:**

- Lista de Evidence nodes vinculados (edge `evidence_for`)
- `confidence_score` atual e histórico
- `source_reliability` por evidence (validado por Datta)
- `freshness` da evidência (data da coleta vs. hoje)
- Gaps identificados por Metacognik (evidência ausente para suportar claim)
- Contradições ativas (edges `contradicts` com outros nodes)
- Hipóteses suportadas ou refutadas por esta evidência
- Warnings de Metacognik (ex: "evidência única sem corroboração")

Um node sem evidência vinculada exibe badge amarelo no Canvas. Um node com `confidence_score < 0.5` exibe badge laranja. Um node bloqueado por Metacognik exibe badge vermelho com ícone de auditoria.

# 13. Relação com ROI, Custo, Créditos e Billing

O Canvas exibe informações de custo e ROI como **contexto operacional** — não como sistema financeiro.

**9 tipos de informação de custo/ROI previstos no Canvas:**

1. `cost_estimate` por node (jsonb no schema do node)
2. Custo acumulado de um workflow em execução
3. Créditos consumidos por agent_run (visível no node de Agent)
4. Estimativa de créditos para um novo workflow (antes de iniciar)
5. ROI/Cost node como objeto formal (família §5.14)
6. Budget threshold — alerta visual quando workflow excede orçamento
7. Comparação entre estimativa e custo real (pós-execução)
8. Histórico de consumo de créditos por projeto (via `cost_projection`)
9. Link para painel de billing (redireciona para Billing/Credits node ou Dashboard)

O Canvas **não resolve** a arquitetura financeira do CKOS. Não calcula ROI, não processa cobranças, não armazena dados de pagamento. Estes são sistemas externos que precisam de documentação própria.

> **Gap §20.1:** ROI Architecture, Billing e Credits precisam de documento dedicado. Enquanto não existirem, o Canvas exibe dados disponíveis via `cost_projection` sem garantia de completude.

# 14. Relação com Feedback e Support

O Canvas exibe Feedback e Support como nodes operacionais — não como caixas de texto genéricas.

**5 tipos de node de Feedback e Support no Canvas:**

1. **FeedbackNode** — avaliação qualitativa de um Artifact ou Workflow; aparece vinculado via edge `feedback_for`
2. **SupportNode** — bloqueio ou dúvida do usuário; aparece com badge de urgência e assignee
3. **ImprovementNode** — gap gerado a partir de feedback recorrente; conectado via edge `generates`
4. **QANode** — resultado de avaliação formal de qualidade (Metacognik ou humano); conectado ao Artifact auditado
5. **LearningNode** — entrada de memória gerada a partir de feedback processado; alimenta o RAG (doc 11 §21)

Nodes de Feedback e Support podem gerar workflows de melhoria, suporte técnico ou QA automaticamente quando o padrão é detectado pelo sistema.

> **Gap §20.2 / §20.3:** Feedback System e Support System precisam de documentação dedicada para definir os fluxos completos.

# 15. Permissões e Segurança

O Canvas respeita integralmente o modelo de segurança do CKOS (doc 12). Toda renderização é filtrada por política antes de chegar ao usuário.

**RBAC no Canvas:**

| Role | Permissões no Canvas |
|---|---|
| `viewer` | Leitura de nodes e edges visíveis para o projeto. Sem ações. |
| `contributor` | Leitura + criação de nodes manuais permitidos para contributor. |
| `project_member` | Contributor + edição de nodes próprios + vinculação de evidências. |
| `lead` | Project_member + aprovações + criação de nodes de decisão + start de workflows. |
| `admin` | Todas as permissões + gerenciamento de nodes de system. |
| `founder` | Admin + aprovação de nodes críticos + acesso a audit log completo. |

**ABAC (atributos dinâmicos):**

- `data_classification` do node: `public | internal | confidential | restricted` — determina quem pode ver o conteúdo.
- `tenant_id`: Canvas nunca mistura nodes de tenants diferentes. RLS aplicado na camada de projeção (doc 11 §21).
- `approval_status`: nodes `pending_approval` só são visíveis para o aprovador designado e para lead+.
- `confidence_score < threshold`: nodes de baixa confiança podem ter visibilidade restrita por política.

**Comportamento quando sem permissão:**

- Se o node existe mas o usuário não tem acesso: exibir versão redigida (title visível, conteúdo oculto) quando policy permitir.
- Se o node é de outro tenant: nunca exibir — nem em versão redigida.
- Se a ação não é permitida pelo RBAC: desabilitar visualmente e emitir `AccessDeniedEvent` no audit log.
- Toda tentativa de ação gera entrada no `audit_log` (doc 12 §7), independente de sucesso.

# 16. Dependência de UI Projections

O Canvas consome as **7 ui_projections** definidas em doc 11 §21. Nunca lê diretamente de tabelas de domínio.

| Projeção | O que Canvas usa |
|---|---|
| `command_center_suggestions` | Sugestões contextuais de nodes e ações exibidas no Canvas quando o usuário está inativo. |
| `agent_activity_projection` | Estado de todos os agentes ativos no projeto — exibido como overlay nos nodes onde agentes estão trabalhando. |
| `approval_projection` | Lista de approvals pendentes — exibida como layer de badges de aprovação nos nodes com `pending_approval`. |
| `cost_projection` | Dados de custo e créditos por node e workflow — exibidos nos badges de custo e no side panel. |
| `risk_projection` | Risks e gaps detectados — exibidos como badges de alerta nos nodes associados. |
| `node_status_projection` | Estado atual de todos os nodes do projeto — base do Canvas. Canvas não recalcula estados. |
| `project_pulse_projection` | Resumo executivo do projeto — usado no header do Canvas (progresso, saúde, alertas críticos). |

Canvas **não recalcula** nenhuma dessas projeções. Se a projeção está desatualizada (lag de event processing), Canvas exibe o estado mais recente disponível com timestamp de última atualização visível para o usuário.

# 17. UX Architecture

Esta seção descreve a arquitetura funcional da UX do Canvas. **Não implementa componentes, não define CSS, não especifica framework de UI.**

**Canvas livre (infinite canvas):**

- Área de trabalho sem bordas fixas — navegável por scroll, zoom, e minimap.
- Clusters automáticos por workflow — nodes pertencentes ao mesmo workflow formam um grupo visual.
- Timeline de eventos — faixa lateral exibindo os últimos N eventos do projeto em tempo real.

**Node inspector (side panel):**

- Abre ao clicar em qualquer node.
- Conteúdo: schema do node, estado atual, histórico de estados, evidências, hipóteses, agente ativo, custo, approval, lineage.
- Ações disponíveis baseadas em permissão e estado atual (só exibe transições válidas).

**Layers sobrepostas:**

- Agent activity layer — overlay que exibe qual agente está ativo em qual node.
- Approval layer — overlay que exibe badges de approval pendente.
- Cost/Risk badges — badges compactos em cada node com dados de custo e risco.

**Filtros e busca:**

- Filtrar por: node_type, status, agente, data, confidence, risk_level, approval_status.
- Busca textual por title e description.
- Filtro "apenas meus nodes" por owner.

**Minimap:**

- Exibido no canto inferior do canvas para navegação em projetos com muitos nodes.
- Destaca clusters por workflow com cores distintas.

**Mobile (MVP: read-only):**

- Canvas exibe nodes em layout compacto — sem drag, sem criação, sem edição.
- Usuário pode inspecionar node, ver estado, ver evidências, aprovar (approval_gate mobile).
- Criação e edição de nodes em mobile são pós-MVP.

**Criação de node (manual):**

- Botão "+" flutuante no canvas → painel de seleção de node_type → form schema mínimo → submit.

**Sugestão de node (AI):**

- Cognik/Nick sugerem nodes como cards "sugeridos" no canvas → usuário confirma ou rejeita.
- Sugestão rejeitada gera `NodeSuggestionRejected` para aprendizado.

**Estética (whitelabel):**

- Tokens de design via `design_system` ativo (branddock). Glassmorphism, border-radius, colors parametrizados por tenant.
- Canvas não tem estética fixa — skin é aplicada por tokens.

# 18. MVP P0

## O que entra no MVP P0

- Renderização de nodes dos tipos: Strategy, Briefing, Research, Evidence, Workflow, Artifact, Approval, Decision.
- Criação manual de nodes com schema básico.
- Exibição de 3 state machines (node, workflow, approval).
- Edges dos tipos: `depends_on`, `informs`, `blocks`, `generates`, `evidence_for`.
- Canvas events: 1–11 (criação, edição, edge, ação, workflow, approval).
- Consumo de `node_status_projection` e `agent_activity_projection`.
- Side panel básico: estado, agente ativo, evidências vinculadas.
- Filtro por node_type e status.
- RBAC MVP: viewer, contributor, lead.
- Tenant isolation via RLS.

## O que fica fora do MVP P0

- Timeline de eventos (pós-MVP).
- Replay de estados passados.
- Nodes de: ROI/Cost, Feedback, Support, Billing/Credits (aguardam docs de sistema dedicado).
- Exportação de canvas como artifact.
- Criação e edição de nodes em mobile.
- Glassmorphism whitelabel (MVP usa tokens padrão, customização é pós-MVP).
- Filtros avançados (busca textual, filtro por confidence, filtro por agente).
- Agent activity overlay completo (MVP: badge simples no node).
- Todos os 14 edge types (MVP: 5 tipos).
- Budget threshold e comparação estimativa vs. real.

# 19. Edge Cases

1. **Canvas com >200 nodes visíveis:** aplicar clustering automático por workflow. Exibir minimap. Filtro de "nodes relevantes" baseado em estado ativo.
2. **Node criado manualmente sem schema válido:** policy_engine rejeita; Canvas exibe erro inline no form; não persiste node incompleto.
3. **Edge criado entre nodes incompatíveis de tipos:** policy valida compatibilidade de tipos de edge. Canvas exibe erro contextual.
4. **Agente gera node duplicado de um existente:** Runtime detecta por matching de title + node_type + project_id; emite `NodeDuplicateDetected`; Canvas exibe alerta de duplicata em vez de criar segundo node.
5. **Usuário tenta aprovar node sem permissão:** Canvas desabilita botão de approval; se tentativa via API direta, policy_engine bloqueia e audit_log registra.
6. **Canvas exibiria node de outro tenant (bug de projeção):** RLS na projeção impede query cruzada; se chegou ao Canvas por bug, Canvas não renderiza node sem `tenant_id` correspondente ao token atual.
7. **State machine de node em conflito com projeção:** Canvas exibe estado da projeção mais recente com timestamp. Conflito é registrado para diagnóstico do sistema.
8. **Workflow já em estado `running`, Canvas sugere recriar:** Canvas detecta workflow ativo via projeção e exibe "workflow em execução" em vez de botão de criação.
9. **Evidence node com `confidence_score < 0.5`:** badge laranja exibido. Side panel exibe warning de Metacognik. Nenhum bloqueio automático — decisão do usuário.
10. **Metacognik emite bloqueio (`blocked`):** node exibe badge vermelho, ações desabilitadas. Side panel exibe justificativa do bloqueio. Somente founder pode override.
11. **Node de Billing/Credits sem sistema financeiro implementado:** Canvas exibe node como placeholder com aviso "sistema de billing pendente — ver Gap §20.4".
12. **Usuário mobile tenta criar node (MVP):** Canvas mobile exibe mensagem "criação de nodes disponível apenas na versão desktop".
13. **UI projection stale (evento emitido mas canvas ainda não atualizou):** Canvas exibe timestamp de última atualização da projeção. Polling/streaming com reconexão automática. Node em estado desconhecido exibe spinner.
14. **Node manualmente deletado (arquivado) mas referenciado em workflow ativo:** Runtime bloqueia arquivamento; Canvas exibe erro "node referenciado em workflow ativo — encerre o workflow antes de arquivar".

# 20. Product / Business Gaps

Os seguintes sistemas são referenciados pelo Node Canvas mas não estão definidos em documentação arquitetural dedicada. Estão registrados como gaps — não como pendências de implementação imediata.

| # | Gap | Impacto no Canvas | Ref |
|---|---|---|---|
| 20.1 | **ROI Architecture** — arquitetura de cálculo, projeção e realização de ROI não definida | Nodes §5.14 e família ROI/Cost são placeholders | `ARCH_PATCH_REPORT §12.1` |
| 20.2 | **Feedback System** — ciclo completo de captura, processamento e aplicação de feedback não documentado | Nodes §5.15 e família Feedback são parciais | `ARCH_PATCH_REPORT §12.2` |
| 20.3 | **Support System** — triagem, roteamento e resolução de suporte não documentados | Nodes §5.16 e família Support são parciais | `ARCH_PATCH_REPORT §12.3` |
| 20.4 | **Credits, Plans & Billing Architecture** — modelo de créditos, planos e cobrança não definido | Nodes §5.17 são placeholders; `cost_projection` incompleta | `ARCH_PATCH_REPORT §12.4` |
| 20.5 | **Campaign Execution Layer** — orquestração completa de campanhas multi-canal não documentada | Nodes §5.18 Campaign carecem de workflow completo | pendente |
| 20.6 | **node_edges schema formal em doc 11** — tabela `node_edges` com schema completo não está em doc 11 v1.1.2 | Implementação do Canvas depende deste patch | patch sugerido para doc 11 v1.2.x |

> **Patches sugeridos para doc 11 v1.2.x** (a serem aplicados antes da implementação do Canvas):
> - `node_edges` table com schema de §7.2 deste documento.
> - `feedback_entries` table para Feedback System (gap 20.2).
> - `support_tickets` table para Support System (gap 20.3).
> - `roi_projection` em §21 para ROI Architecture (gap 20.1).
> - Confirmar campos `tenant_id`, `source_event_id`, `cost_estimate` na tabela `nodes` (§4 deste doc).

# 21. Related notes

- [[10_SYSTEM_RUNTIME_ARCHITECTURE]]
- [[11_DATA_MODEL_AND_PERSISTENCE]]
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]]
- [[13_EVALS_QUALITY_CONFIDENCE]]
- [[14_PROJECT_DASHBOARD_ARCHITECTURE]]
- [[15_COMMAND_CENTER_ARCHITECTURE]]
- [[02_AI_FIRST_OBJECT_MODEL]]
- [[07_WORKFLOW_BLUEPRINTS]]
- [[ARCHITECTURE_PATCH_REPORT]]
- [[QA_DOCUMENTATION_CHECKLIST]]
