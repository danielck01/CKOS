---
title: Command Center Architecture
file: 15_COMMAND_CENTER_ARCHITECTURE.md
phase: 04_PRODUCT_SYSTEM
category: product_architecture
version: 1.3.0
status: draft
owner: PMO_CKOS
responsible_agent: Nick
reviewers:
  - Metacognik
  - QA_Lead
approval_required:
  - founder
  - metacognik
purpose: >
  Definir o Command Center como camada de intenção, aprovação, acompanhamento e explicação do CKOS.
  Emite eventos para o runtime (10), lê de ui_projections (11 §21), nunca escreve estado diretamente.
  Não é chat. Não é input bonito. Não chama agente diretamente.
inputs: >
  Runtime Architecture (10 v1.1.0) — ingress, engines, event bus, fluxo canônico §5.2, approval gate §5.8;
  Data Model (11 v1.1.2) — ui_projections §21, cost_ledger §18, approvals §16, audit_logs §16.1;
  Security (12 v1.1.0) — RBAC, ABAC, policy_engine, data classification, model privacy policy;
  Evals/Observability (13 v1.1.0) — cost guard, eval scores, model router policy;
  Architecture Patch Report (v1.1.0) — gaps de produto/negócio §12.1–12.4.
outputs: >
  Intent Taxonomy com 10 famílias;
  Modos do Command Center (Ask / Action / Approval / Explain / Support / Cost / Feedback);
  22 slash commands com intent pattern completo;
  Relação com Nick como interface conversacional do CKOS;
  16 estados vivos mapeados a eventos de runtime;
  Leitura das 7 ui_projections;
  Eventos emitidos;
  Integração de gaps ROI / Feedback / Suporte / Créditos;
  Tabela command_history (patch pendente para doc 11);
  MVP P0 e exclusões;
  Edge cases.
framework: >
  Intenção → intent_router → context_pack_builder → policy_engine → workflow_engine →
  agent_router → model_router → approval_gate → ui_projection_engine → Command Center mostra estado.
edge_cases: >
  Comando ambíguo; usuário sem permissão; custo acima do limite; agente indisponível;
  RAG sem fonte suficiente; aprovação expirada; workflow travado; output com baixa confiança;
  ação irreversível; cross-project access attempt; capability não ativada;
  suporte acionado durante ação crítica; projeção stale.
integrations: >
  Emite eventos para Runtime (10);
  Lê ui_projections via SSE/WebSocket (11 §21);
  Respeita policy_engine (12) — deny-by-default;
  Consome cost_projection + budget_alerts (11 §18);
  Encaminha approvals para approval_gate (10 §5.8);
  Audit_logs via runtime (11 §16.1) — toda ação do usuário registrada automaticamente.
prompts: >
  Classificar intenção e modo (intent_type, confidence, mode_detected);
  Converter slash command em evento estruturado;
  Nick: traduzir estado de runtime para linguagem do papel do usuário;
  Nick: pedir aprovação com contexto de risco, custo e reversibilidade;
  Nick: explicar bloqueio com política, evidência e sugestão de caminho alternativo.
metrics: >
  Taxa de interpretação correta de intenção;
  % de approvals bem encaminhadas antes da expiração;
  Tempo intenção→primeiro evento de runtime;
  % comandos resolvidos sem retrabalho;
  % estados vivos exibidos corretamente e dentro do SLA de projeção;
  Uso recorrente de slash commands;
  Satisfação de Feedback Mode simples;
  Taxa de PermissionDenied com explicação satisfatória.
related_notes:
  - ../01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - 14_PROJECT_DASHBOARD_ARCHITECTURE.md
  - 16_NODE_CANVAS_ARCHITECTURE.md
  - ../ARCHITECTURE_PATCH_REPORT.md
tags: [product, command_center, intent, routing, ingress, nick, intent_taxonomy, modes, slash_commands, ui_projections, approvals, feedback, support, cost, gaps]
---

> **Regra fundamental:**
> O Command Center **não é chat**. Não é input bonito. Não chama agente diretamente. Não escreve estado diretamente.
> O Command Center é a **camada de intenção, aprovação, acompanhamento e explicação do CKOS**.
> Toda ação começa como evento — e o estado exibido ao usuário é sempre lido de `ui_projections` (doc 11 §21), nunca inventado ou consultado diretamente em tabelas de domínio.

# 1. Propósito

Definir o **Command Center** como o ingress primário do CKOS: a superfície pela qual o usuário expressa intenção, recebe explicações contextuais de Nick, acompanha execuções em tempo real, aprova ações, consulta custos e reporta problemas.

O Command Center responde à pergunta central de doc 10 §5.2: **como uma intenção vira execução rastreável?** É o passo 1 desse fluxo — emite `IntentSubmitted` para o runtime — e é também o último — exibe ao usuário cada etapa subsequente via projeções (doc 11 §21).

**O Command Center não executa.** Captura intenção, mostra estado e facilita decisões humanas. Quem executa é o runtime (10).

# 2. Função dentro do CKOS

O Command Center é a **boca e os olhos do runtime para o usuário**:

- **Boca**: transforma linguagem natural, slash commands, mentions e formulários em eventos estruturados para o runtime.
- **Olhos**: exibe o estado vivo de runs, nodes, approvals, custos e riscos lidos de `ui_projections` — nunca via queries diretas a tabelas de estado.

Exemplos de intenção que o Command Center captura — cobrindo as 10 famílias da Intent Taxonomy (§5.3):

```txt
"Diagnostique o momento atual deste projeto"         → Ask Mode / Action Mode      [Strategy]
"Quais hipóteses o Cognik identificou?"              → Ask Mode / Explain Mode     [Strategy]
"Comece um briefing inteligente"                     → Action Mode                 [Briefing]
"Pesquise referências de mercado para este projeto"  → Action Mode                 [Research]
"Qual node está travando o workflow?"                → Ask Mode / Explain Mode     [Nodes]
"Monte um squad para este problema"                  → Ask Mode / Action Mode      [Agents]
"Gere uma proposta inicial"                          → Action Mode                 [Production]
"Aprovar este workflow"                              → Approval Mode               [Decisions]
"Qual ROI esperado?"                                 → Ask Mode / Cost Mode        [ROI/Cost]
"Esse output não está bom, peça revisão"             → Feedback Mode               [Feedback]
"Abrir suporte"                                      → Support Mode                [Support]
"Quais memórias foram usadas nessa resposta?"        → Explain Mode                [Memory]
```

# 3. Inputs

- Texto livre em linguagem natural (pt-BR, en, zh-CN)
- Slash commands (`/briefing`, `/approve`, `/support` — ver §5.4)
- Mentions de agentes e roles (`@nick`, `@metacognik`, `@pmo_ckos` — ver §5.5)
- Arquivos, imagens, links (injetados como contexto pelo `context_pack_builder`)
- Projeto ativo, workspace, seção atual (propagados automaticamente pelo contexto de sessão)
- Permissões do usuário no escopo atual (avaliadas em tempo real pelo `policy_engine` — doc 12)
- Estado de `ui_projections` (consumido assincronamente via SSE/WebSocket — ver §9)
- Histórico de comandos do usuário no projeto (via `command_history` — ver §13)

# 4. Outputs

O Command Center pode retornar ao usuário:

- Resposta textual contextual de Nick
- Sugestão de próximo passo (lida de `command_center_suggestions`)
- Status de execução em tempo real (de `agent_activity_projection`, `node_status_projection`)
- Pedido de aprovação com contexto de risco, custo e reversibilidade (de `approval_projection`)
- Resumo de run concluído (de `agent_activity_projection`)
- Artefato gerado ou link para node (via `artifact_pipeline` → `artifact_versions`)
- Alerta de custo (de `cost_projection` + `budget_alerts`)
- Alerta de risco (de `risk_projection`)
- Pedido de suporte (evento `SupportRequested` — tabela pendente, ver §12.3)
- Feedback request (evento `FeedbackRequested` — tabela pendente, ver §12.2)
- Decisão registrada (confirmação de `DecisionRegistered` no event log)
- Mensagem de bloqueio com explicação de política (de `audit_logs` + `policy_engine`)

# 5. Framework operacional

## 5.1 Fluxo canônico: da intenção ao estado vivo

Mapeamento direto a doc 10 §5.2. O Command Center é responsável pelos passos marcados com `[CC]`:

```txt
[CC]  1.  Usuário expressa intenção → Command Center emite
              IntentSubmitted{intent_text, user_id, project_id?, context_ref?, section?, mode?, slash_command?, mentioned_agent?}

       2.  intent_router classifica (transformer: intent_to_object)
              → IntentResolved{intent_type, object_candidates, confidence, mode_detected}

       3.  context_pack_builder monta Context Packet (memória curta/média/longa — doc 11)
              → ContextAssembled{pack_id, sources, token_count, budget_remaining}

       4.  policy_engine valida usuário×workspace×projeto×ação (doc 12 — deny-by-default)
              → PermissionGranted | PermissionDenied{policy_id, reason}

       5.  workflow_engine instancia Workflow Run (blueprint — doc 07)
              → WorkflowStarted{workflow_id, run_id}

       6.  Cada passo → RunScheduled → RunStarted{run_id, idempotency_key, trace_id}

       7.  agent_router escolhe agente; model_router escolhe modelo; tool_router habilita tools

       8.  Worker executa skill → PartialOutputProduced (streaming)

       9.  Node State Machine transiciona node(s) afetado(s)

      10.  Metacognik audita → MetacognikReviewed{confidence, risk, recommendation}

      11.  approval_gate: se autonomia/risco exige → ApprovalRequested → [pausa]
[CC]        Command Center exibe approval request com contexto completo
            → usuário emite ApprovalSubmitted{decision: approved|rejected|changes_requested}

      12.  Artifact Pipeline materializa → ArtifactGenerated

      13.  Memory Writer grava decisões/aprendizados → MemoryUpdated

[CC]  14.  ui_projection_engine projeta → Command Center lê e exibe estado ao usuário
```

O Command Center nunca pula nenhum passo desse fluxo. Não existe atalho de "chamar agente diretamente".

## 5.2 Modos do Command Center

Sete modos definem como o Command Center interpreta a intenção e como Nick responde. O modo pode ser detectado automaticamente pelo `intent_router` (`mode_detected`) ou selecionado explicitamente pelo usuário via slash command.

### A. Ask Mode

**Descrição:** Usuário faz pergunta e recebe resposta contextual sem instanciar workflow.

**Exemplos:** "O que está impedindo a proposta?", "Quais nodes estão ativos?", "O Cognik encontrou algo relevante?", "Qual o status do briefing?", "Qual o risco mais crítico agora?"

**Fluxo:** `IntentSubmitted{mode: ask}` → `intent_router` classifica como `intent_type: query.*` → `context_pack_builder` reúne contexto relevante → Nick responde a partir de `ui_projections` + memória autorizada → nenhum workflow instanciado.

**Regra:** Nick responde apenas com o que está nas projeções, memória autorizada e event log. Nunca inventa estado.

---

### B. Action Mode

**Descrição:** Usuário pede uma ação concreta. Runtime cria workflow/run.

**Exemplos:** "Crie um briefing", "Analise os concorrentes", "Monte a proposta", "Gere o moodboard", "Execute a campanha X", "Rode a pesquisa de mercado".

**Fluxo:** `IntentSubmitted{mode: action}` → `intent_router` classifica como `intent_type: action.*` → fluxo canônico completo (§5.1) → Command Center exibe estados vivos (§8) em tempo real.

**Regra:** Uma ação sempre gera pelo menos um evento de runtime e um `workflow_run`. Nunca executar sem trace.

---

### C. Approval Mode

**Descrição:** Usuário aprova, rejeita ou solicita revisão de um item pendente.

**Exemplos:** "Aprovar este workflow", "Rejeitar essa proposta", "Pedir revisão desse output", "Escalonar para o Founder".

**Fluxo:** Command Center exibe `approval_projection{status: requested, expires_at, risk_level, cost_estimate, reversible}` → usuário emite `ApprovalSubmitted{approval_id, decision: approved|rejected|changes_requested, note?}` → `approval_gate` resume workflow parado.

**Regra:** Aprovação nunca é escrita diretamente no banco — é sempre um evento `ApprovalSubmitted` que o `approval_gate` consome. O Command Center não altera `approvals` diretamente.

---

### D. Explain Mode

**Descrição:** Nick explica o que está acontecendo, por que algo foi bloqueado, qual evidência existe, qual custo foi previsto.

**Exemplos:** "Por que o workflow foi bloqueado?", "Qual evidência o Cognik usou?", "Por que a permissão foi negada?", "O que o Metacognik sinalizou?", "Quais riscos foram detectados?"

**Fluxo:** `IntentSubmitted{mode: explain}` → `context_pack_builder` reúne `audit_logs` + `risk_projection` + `agent_decisions` + `evidence_items` autorizados → Nick traduz para linguagem do papel do usuário.

**Regra:** Nick nunca revela dados sensíveis de outro projeto ou usuário em modo Explain. `policy_engine` filtra o que pode ser exibido. Se não há evidência acessível, Nick explica o bloqueio sem revelar o motivo sensível.

---

### E. Support Mode

**Descrição:** Usuário reporta problema, abre ticket ou solicita ajuda humana.

**Exemplos:** "Abrir suporte", "O agente está em loop", "Cobranças erradas", "Preciso falar com alguém".

**Fluxo:** `IntentSubmitted{mode: support}` → `intent_router` classifica como `intent_type: support.*` → runtime emite `SupportRequested{category, description, run_id?, severity}` → Command Center confirma abertura com referência de correlação.

**Dependência de gap:** Tabela `support_tickets` + gestão de ticket são pendências registradas (ARCH_PATCH_REPORT §12.3). MVP P0 usa evento `SupportRequested` no event log; acompanhamento de ticket é deferred (doc 17 ou doc 11 v2.x).

---

### F. Cost Mode

**Descrição:** Usuário consulta créditos, custo estimado, consumo por run, alertas e limites.

**Exemplos:** "Quanto isso vai custar?", "Quantos créditos restam?", "Qual o custo do último run?", "Estou próximo do limite?", "Aprovar custo extra".

**Fluxo:** `IntentSubmitted{mode: cost}` → Command Center lê `cost_projection{project_id, spent_usd, limit_usd, state}` + `budget_alerts` + `run_costs` → Nick apresenta estado financeiro atual.

**Aprovação de custo extra:** se `project_budgets.state = needs_approval` → Command Center aciona Approval Mode com contexto de custo.

**Dependência de gap:** Créditos, planos e billing (wallet, invoices, upgrade) são pendências registradas (ARCH_PATCH_REPORT §12.4). MVP usa `cost_projection` como proxy de consumo; a camada de billing real é deferred.

---

### G. Feedback Mode

**Descrição:** Usuário avalia output, agente, artifact, proposta, workflow ou decisão.

**Exemplos:** "Esse briefing está bom", "O output do Datta está incorreto", "O workflow foi eficiente?", "Avaliar proposta aprovada".

**Fluxo:** `IntentSubmitted{mode: feedback}` → Command Center apresenta objeto de feedback → usuário emite `FeedbackSubmitted{target_type, target_id, rating, comment?, is_implicit: false}` → runtime registra como sinal de eval + learning loop.

**Dependência de gap:** Tabela `feedback_entries` + eventos `FeedbackSubmitted`/`FeedbackImplicit` são pendências registradas (ARCH_PATCH_REPORT §12.2). MVP P0 usa `eval_results` como proxy; feedback explícito com persistência própria é deferred.

---

## 5.3 Intent Taxonomy

> **Todo comando é um evento de intenção, não uma chamada direta de execução.**
> *Every command is an intent event, not a direct execution call.*

O `intent_router` (doc 10 §5.15) classifica toda intenção dentro desta taxonomia antes de roteá-la para o fluxo canônico (§5.1). Slash commands são atalhos — não chamadas diretas — que mapeiam para as mesmas famílias abaixo.

```txt
Intent Taxonomy
├── 1. Strategy & Diagnosis
├── 2. Briefing & Context
├── 3. Research & Collection
├── 4. Nodes & Workflows
├── 5. Agents & Squads
├── 6. Production & Artifacts
├── 7. Decisions & Approvals
├── 8. ROI, Cost & Usage        ← família #8 de 10; importante, mas não o centro
├── 9. Feedback & Support
└── 10. Memory, Evidence & Explainability
```

### 5.3.1 Strategy & Diagnosis

**Propósito:** Diagnosticar o estado atual do projeto, identificar lacunas estratégicas, mapear hipóteses e surfaçar riscos ocultos.

```txt
"Diagnostique o momento atual deste projeto."
"Quais são as maiores lacunas estratégicas?"
"Quais hipóteses o Cognik identificou?"
"O que o Metacognik está questionando?"
"Compare o briefing com os dados coletados."
"Mostre os riscos ocultos deste projeto."
```

| Campo | Valor |
|---|---|
| `intent_type` | `query.strategy.*` \| `action.strategy.diagnose` |
| Eventos | `IntentSubmitted` → `IntentResolved` → Nick responde (Ask) \| `WorkflowStarted` (Action) |
| Projections | `project_pulse_projection`, `risk_projection`, `node_status_projection` |
| Permissões | project_member (any) |
| Outputs | análise contextual, risk summary, gap list, hipóteses priorizadas |

### 5.3.2 Briefing & Context

**Propósito:** Iniciar, expandir ou revisar o briefing do projeto; montar e auditar o context pack.

```txt
"Comece um briefing inteligente."
"Continue o briefing de onde paramos."
"Quais respostas ainda estão fracas?"
"Transforme este briefing em mapa de nodes."
"Mostre as contradições do briefing."
"Monte um context pack para este projeto."
```

| Campo | Valor |
|---|---|
| `intent_type` | `action.briefing.*` \| `query.briefing.*` |
| Eventos | `IntentSubmitted` → `WorkflowStarted{briefing_workflow}` → `NodeCreated` |
| Projections | `node_status_projection`, `project_pulse_projection` |
| Permissões | project_member (contributor+) |
| Outputs | briefing node, context pack, perguntas para o cliente, mapa de nodes |

### 5.3.3 Research & Collection

**Propósito:** Coletar dados externos via collectors (Perplexity, Apify, PubMed, APIs de mercado, RAG privado); alimentar o sistema de evidências.

```txt
"Pesquise referências de mercado para este projeto."
"Colete dados dos concorrentes no Instagram."
"Busque estudos científicos sobre esse comportamento."
"Compare este posicionamento com benchmarks."
"Verifique fontes confiáveis para esta hipótese."
"Colete sinais externos antes de gerar proposta."
```

| Campo | Valor |
|---|---|
| `intent_type` | `action.research.*` \| `action.collect.*` |
| Eventos | `IntentSubmitted` → `WorkflowStarted` → `CollectorRunStarted` |
| Projections | `agent_activity_projection`, `node_status_projection` |
| Permissões | project_member (contributor+); technical (dados sensíveis) |
| Outputs | research pack, evidence nodes, collector output, artifact |

### 5.3.4 Nodes & Workflows

**Propósito:** Criar, visualizar, conectar e arquivar nodes; instanciar, consultar e gerenciar workflows operacionais.

```txt
"Crie nodes a partir deste diagnóstico."
"Mostre quais nodes estão ativos."
"Qual node está travando o workflow?"
"Crie um workflow para campanha de lançamento."
"Transforme essa ideia em fluxo operacional."
"Conecte este node ao briefing e à proposta."
```

| Campo | Valor |
|---|---|
| `intent_type` | `action.nodes.*` \| `query.nodes.*` \| `action.workflow.*` \| `query.workflow.*` |
| Eventos | `IntentSubmitted` → `NodeCreationRequested` \| `WorkflowStarted` |
| Projections | `node_status_projection`, `agent_activity_projection` |
| Permissões | project_member (any para query; contributor+ para criação/conexão) |
| Outputs | node criado, edge criada, workflow instanciado, status de nodes |

### 5.3.5 Agents & Squads

**Propósito:** Consultar agentes ativos, entender roteamento, montar squads, acionar agente específico via mention.

```txt
"Qual agente deve analisar isso?"
"Monte um squad para este problema."
"Peça ao Metacognik para auditar essa resposta."
"Acione o agente de pesquisa."
"Quais agentes estão trabalhando agora?"
"Explique por que esse agente foi escolhido."
```

| Campo | Valor |
|---|---|
| `intent_type` | `query.agents.*` \| `action.agents.assign` |
| Eventos | `IntentSubmitted{mentioned_agent?}` → `agent_router` resolve → `IntentResolved` |
| Projections | `agent_activity_projection` |
| Permissões | project_member (any) |
| Outputs | agente selecionado, squad montado, explicação de roteamento, activity status |

### 5.3.6 Production & Artifacts

**Propósito:** Gerar, revisar, versionar e aprovar artefatos de produção (propostas, roteiros, moodboards, relatórios, prompt packs).

```txt
"Gere uma proposta inicial."
"Crie um prompt pack visual."
"Monte um roteiro para campanha."
"Transforme essa análise em relatório."
"Gere uma versão executiva deste diagnóstico."
"Atualize o artifact com as novas evidências."
```

| Campo | Valor |
|---|---|
| `intent_type` | `action.artifact.*` \| `action.produce.*` |
| Eventos | `IntentSubmitted` → `WorkflowStarted` → `ArtifactGenerated` |
| Projections | `node_status_projection`, `agent_activity_projection` |
| Permissões | project_member (contributor+) |
| Outputs | artifact, artifact_version, link para node, prompt pack, relatório |

### 5.3.7 Decisions & Approvals

**Propósito:** Consultar decisões pendentes, aprovar/rejeitar ações, escalonar aprovações, registrar decisões formais.

```txt
"Quais decisões estão pendentes?"
"Aprovar este workflow."
"Rejeitar e pedir revisão."
"Explique o que estou aprovando."
"Qual o risco desta aprovação?"
"Registre esta decisão."
```

| Campo | Valor |
|---|---|
| `intent_type` | `approval.submit` \| `query.approvals.*` \| `action.decisions.*` |
| Eventos | `ApprovalSubmitted` \| `IntentSubmitted{mode: approval}` \| `DecisionRegistered` |
| Projections | `approval_projection`, `project_pulse_projection` |
| Permissões | role com `approval_required` atendido |
| Outputs | approval_projection atualizado, workflow resumido, decisão registrada |

### 5.3.8 ROI, Cost & Usage

**Propósito:** Consultar ROI esperado, custo por run/workflow/agente, consumo de créditos e alertas de orçamento.

```txt
"Qual ROI esperado?"
"Quanto este workflow já custou?"
"Qual agente está consumindo mais?"
"Este projeto está dentro do orçamento?"
"Vale a pena rodar esse collector agora?"
"Mostre custo versus valor gerado."
```

| Campo | Valor |
|---|---|
| `intent_type` | `query.roi.*` \| `query.cost.*` \| `query.credits.*` |
| Eventos | `IntentSubmitted{mode: cost}` → `CostEstimateRequested` |
| Projections | `cost_projection`, `project_pulse_projection` |
| Permissões | project_member (any) |
| Outputs | cost_projection, estimativa de custo, alerta de budget |

> **Nota:** ROI, Cost & Usage é **família #8 de 10**. É um domínio importante, mas representa uma parte do espectro de intenções do Command Center — não o seu centro de gravidade. Os gaps de implementação desta família estão registrados em ARCH_PATCH_REPORT §12.1 e §12.4.

### 5.3.9 Feedback & Support

**Propósito:** Registrar feedback explícito sobre outputs e agentes; acionar suporte para erros ou pedidos de ajuda humana.

```txt
"Registrar feedback sobre esta resposta."
"Esse output não está bom, peça revisão."
"Abra um suporte para este erro."
"Preciso de ajuda humana."
"Reportar problema no workflow."
"Marcar esta resposta como útil."
```

| Campo | Valor |
|---|---|
| `intent_type` | `feedback.submit` \| `support.open` |
| Eventos | `FeedbackSubmitted` \| `SupportRequested` |
| Projections | `agent_activity_projection` (para estado de suporte) |
| Permissões | project_member (any) |
| Outputs | feedback registrado, correlation_id de suporte, escalação |

> **Nota:** Feedback & Support é **família #9 de 10**. Os gaps de implementação estão registrados em ARCH_PATCH_REPORT §12.2 e §12.3.

### 5.3.10 Memory, Evidence & Explainability

**Propósito:** Consultar memórias usadas pelo sistema, explorar evidências de decisões, reproduzir runs e entender bloqueios.

```txt
"O que você sabe sobre este projeto?"
"Quais memórias foram usadas?"
"Quais fontes sustentam essa resposta?"
"Mostre o caminho desta decisão."
"Reproduza o run anterior."
"Por que esse comando foi bloqueado?"
"Quais dados estão faltando?"
```

| Campo | Valor |
|---|---|
| `intent_type` | `query.memory.*` \| `query.evidence.*` \| `query.explain.*` \| `query.replay.*` |
| Eventos | `IntentSubmitted{mode: explain}` → `ContextAssembled` → Nick responde |
| Projections | `project_pulse_projection`, `agent_activity_projection`, `risk_projection` |
| Permissões | project_member (any); evidence filtrada por `data_classification` |
| Outputs | memórias usadas, fontes citadas, run replay, explicação de bloqueio |

---

## 5.4 Slash commands e intent patterns

Os slash commands são atalhos das 10 famílias da Intent Taxonomy (§5.3). Todo slash command resulta em `IntentSubmitted` para o runtime — nunca em chamada direta a agente, tool, provider, model ou collector.

| Comando | `intent_type` | `required_context` | `emitted_event` | `runtime_dependency` | `permissions_required` | `projected_response` |
|---|---|---|---|---|---|---|
| `/briefing` | `action.briefing.create` | project_id, stakeholders, objectives | `IntentSubmitted` → `WorkflowStarted` | workflow_engine, briefing_workflow | project_member (contributor+) | `node_status_projection`, artifact preview |
| `/diagnosis` | `query.strategy.diagnose` | project_id | `IntentSubmitted{mode: ask}` | intent_router, context_pack_builder | project_member (any) | `project_pulse_projection`, `risk_projection` |
| `/research` | `action.research.run` | project_id, objective, sources? | `IntentSubmitted` → `WorkflowStarted` → `CollectorRunStarted` | workflow_engine, collector_runner | project_member (contributor+) | `agent_activity_projection`, collector status |
| `/competitors` | `action.research.competitors` | project_id, market_scope? | `IntentSubmitted` → `WorkflowStarted` → `CollectorRunStarted` | workflow_engine, collector_runner | project_member (contributor+) | `node_status_projection`, collector output |
| `/nodes` | `query.nodes` | project_id | `IntentSubmitted{mode: ask}` | intent_router | project_member (any) | `node_status_projection` |
| `/workflow` | `action.workflow.create` | project_id, objective, nodes? | `IntentSubmitted` → `WorkflowStarted` | workflow_engine | project_member (contributor+) | workflow status, `node_status_projection` |
| `/agents` | `query.agents` | project_id | `IntentSubmitted{mode: ask}` | intent_router | project_member (any) | `agent_activity_projection` |
| `/audit` | `query.explain.audit` | project_id, run_id? | `IntentSubmitted{mode: explain}` | context_pack_builder, audit_logs | project_member (any) | Metacognik warnings, audit summary |
| `/proposal` | `action.artifact.create.proposal` | project_id, briefing_id, scope_nodes | `IntentSubmitted` → `WorkflowStarted` | workflow_engine, artifact_pipeline | project_member (lead+) | `approval_projection`, artifact link |
| `/artifact` | `action.artifact.create` | project_id, artifact_type, source_nodes? | `IntentSubmitted` → `WorkflowStarted` | workflow_engine, artifact_pipeline | project_member (contributor+) | artifact preview, `node_status_projection` |
| `/approve` | `approval.submit` | approval_id, decision | `ApprovalSubmitted` | approval_gate | role com `approval_required` atendido | `approval_projection` atualizado |
| `/roi` | `query.roi` | project_id, period?, scope? | `IntentSubmitted{mode: cost}` | cost_guard, cost_projection | project_member (any) | `cost_projection` + `roi_projection` *(gap §12.1)* |
| `/cost` | `query.cost` | project_id, scope?, period? | `IntentSubmitted{mode: cost}` → `CostEstimateRequested` | cost_guard | project_member (any) | `cost_projection`, `run_costs` |
| `/credits` | `query.credits` | workspace_id | `IntentSubmitted{mode: cost}` | cost_projection | workspace_member (any) | `cost_projection` + credits_balance *(gap §12.4)* |
| `/feedback` | `feedback.submit` | target_type, target_id | `FeedbackSubmitted` *(gap §12.2)* | eval_runner | project_member (any) | confirmação |
| `/support` | `support.open` | description, category, run_id? | `SupportRequested` *(gap §12.3)* | event_store | authenticated_user | correlation_id como referência |
| `/explain` | `query.explain` | target_type?, target_id?, run_id? | `IntentSubmitted{mode: explain}` | context_pack_builder, audit_logs, evidence_items | project_member (any) | explicação via `audit_logs` + `evidence_items` autorizados |
| `/memory` | `query.memory` | project_id | `IntentSubmitted{mode: explain}` | memory_retriever, context_pack_builder | project_member (any) | memórias usadas, freshness |
| `/evidence` | `query.evidence` | project_id, node_id?, run_id? | `IntentSubmitted{mode: explain}` | rag_retriever, evidence_items | project_member (any) | `evidence_items` autorizados |
| `/replay` | `query.replay` | run_id | `IntentSubmitted{mode: explain}` | run_replays, event_store | project_member (lead+) | run replay: input, contexto, agente, custo, output |
| `/admin` | `admin.ops` | org_id, action_type | `IntentSubmitted{mode: action}` | policy_engine, workflow_engine | admin / founder | workflow status, audit_logs |
| `/billing` | `query.billing` | org_id, period? | `IntentSubmitted{mode: cost}` | cost_projection | admin / founder | `billing_projection` *(gap §12.4)* |

**Notas:**
- Todos os campos de `required_context` são preenchidos automaticamente pelo `context_pack_builder` quando disponíveis no projeto ativo.
- Se `required_context` estiver incompleto, Nick solicita o dado faltante antes de emitir o evento — nunca assume.
- Comandos marcados com *(gap pendente)* emitem evento e exibem estado parcial até que a tabela/projeção correspondente esteja disponível.

## 5.5 Mentions oficiais

Mentions chamam um agente específico no contexto do comando atual. O `intent_router` injeta a mention como `mentioned_agent` no `IntentSubmitted`.

```txt
@nick          → Nick (interface conversacional; sempre disponível)
@cognik        → Cognik (diagnóstico, análise, evidência)
@metacognik    → Metacognik (auditoria, bloqueio, risco — NÃO executa a pedido direto do usuário)
@pmo_ckos      → PMO_CKOS (planejamento, timeline, decisão estrutural)
@qa_lead       → QA Lead (aprovação de qualidade técnica)
@builder_lead  → Builder Lead (implementação, arquitetura técnica)
@datta         → Datta (dados, métricas, cost ledger)
@ops           → Ops (operações, deploys, collectors)
@campaign      → Campaign Agent (campanhas, conteúdo, distribuição)
```

**Regra `@metacognik`:** Não executa ações a pedido direto do usuário — só audita runs e emite `MetacognikReviewed`. Mencionar `@metacognik` ativa Explain Mode mostrando os últimos sinais de auditoria do projeto.

**Regra de capabilities:** Mentions de agents de domínio (ex.: `@branddock`) só são resolvidos se a capability correspondente estiver ativa no projeto (`capabilityRegistry` + `policy_engine`). Se não ativada, Nick informa e sugere ativação quando o usuário tem permissão.

## 5.6 Sugestões contextuais

O `command_center_suggestions` (doc 11 §21) é atualizado pelo `ui_projection_engine` com base no estado atual do projeto. O Command Center exibe as sugestões de maior `priority` como chips contextuais no placeholder do input.

Exemplos por seção:

```txt
Seção briefing ativo:    "O que falta para fechar o diagnóstico?"  |  "/diagnosis"
Seção Canvas:            "Crie um node a partir dessa hipótese."   |  "/nodes"
Seção proposta:          "Quais riscos antes de aprovar?"           |  "/audit"
Seção cost:              "Qual métrica prova que funcionou?"        |  "/roi"
Seção approval pending:  "Há 2 aprovações aguardando sua decisão." |  "/approve"
Seção pós-run:           "Datta registrou nova métrica relevante." |  "/agents"
```

# 6. Nick — interface conversacional do CKOS

Nick é a **interface conversacional do CKOS**, não um chatbot genérico. Nick não gera texto livre sobre qualquer assunto — Nick traduz o estado do runtime para a linguagem do usuário, facilita decisões humanas e mantém o usuário informado sobre execuções, riscos e custos.

**O que Nick deve fazer:**

- Explicar estados do runtime em linguagem acessível ao papel do usuário (founder vs. cliente vs. ops)
- Traduzir complexidade técnica (event log, confidence scores, risk levels) em implicações práticas
- Sugerir próximos passos a partir de `command_center_suggestions` + contexto ativo
- Solicitar aprovação quando `approval_gate` emite `ApprovalRequested` — com contexto de risco, custo, reversibilidade e prazo (`expires_at`)
- Apontar riscos detectados por Metacognik ou `risk_projection`
- Mostrar evidências quando disponíveis e autorizadas (`evidence_items` + `agent_decisions`)
- Explicar custo estimado de uma ação antes de executar (via `cost_guard` pre-check)
- Acionar Support Mode quando detecta erro de sistema ou solicitação explícita do usuário
- Coletar feedback simples após runs concluídos (Feedback Mode)
- **Nunca fingir execução sem evento real de runtime**
- **Nunca revelar dados sensíveis de outro tenant, projeto ou usuário**
- **Nunca inventar estado** — o que Nick exibe deve ter origem em `ui_projections` ou `audit_logs`

**O que Nick não é:**

- Não é buscador de informação pública
- Não é copilot de código genérico sem contexto de projeto
- Não é canal de comunicação externa (e-mail, Slack, WhatsApp)
- Não é interface de billing direto (encaminha para Cost Mode + operador)
- Não é executor — nunca age sem evento de runtime correspondente

**Persona de Nick por papel:**

| Papel | Tom de Nick |
|---|---|
| Founder | Direto, estratégico, com risco e custo sempre visíveis |
| PMO_CKOS | Operacional, focado em bloqueios, timelines e aprovações pendentes |
| Cliente | Claro, sem jargão técnico, focado em outputs e decisões de escopo |
| Ops / Builder | Técnico, com trace_id, run_id e referências a tabelas quando relevante |
| QA Lead | Focado em evidência, confidence score e conformidade com critérios |

# 7. Relação com agentes e routers

O Command Center não escolhe agente manualmente. O processo é sempre mediado pelo runtime:

```txt
Usuário expressa intenção
→ intent_router classifica (intent_type, object_candidates, confidence)
→ policy_engine valida (pode o usuário executar essa ação nesse projeto?)
→ agent_router escolhe agente/squad (agentRegistry + squadRegistry)
→ model_router escolhe modelo (por custo×qualidade×privacidade — doc 13)
→ tool_router habilita tools (interseção skill∩agente∩projeto — doc 12)
→ runtime executa
→ ui_projection_engine projeta
→ Command Center exibe estado ao usuário
```

**Regras:**

- O Command Center nunca passa `agent_id` hardcoded para o runtime. Passa apenas `intent_type` + contexto.
- Se o usuário menciona `@cognik`, o Command Center injeta `mentioned_agent: cognik` no evento — mas o `agent_router` ainda valida se Cognik é o agente correto para a intenção e se tem permissão no projeto.
- Handoffs entre agentes são eventos do runtime (`AgentHandoff`) — o Command Center não orquestra handoffs.
- A Decision Rights Matrix (doc 10 §5.22) define quem pode decidir o quê: Nick sugere · Cognik interpreta · Metacognik bloqueia/audita · PMO_CKOS recomenda · Founder aprova estrutural · Cliente aprova escopo.

# 8. Estados vivos

O Command Center exibe os estados abaixo em tempo real, consumindo SSE/WebSocket da `ui_projection_engine`. Cada estado mapeia a eventos específicos de doc 10 §5.2.

| Estado visível ao usuário | Evento(s) de runtime correspondente(s) |
|---|---|
| Recebendo pedido | `IntentSubmitted` |
| Interpretando intenção | `IntentResolved` |
| Montando contexto | `ContextAssembled` |
| Consultando memória | (interno ao `context_pack_builder` — `ContextAssembled` quando completo) |
| Validando permissões | `PermissionGranted` \| `PermissionDenied` |
| Escolhendo agentes | `RunScheduled` (após agent_router resolver) |
| Estimando custo | `CostEstimateProduced` (de `cost_guard` pre-check) |
| Aguardando aprovação | `ApprovalRequested` |
| Executando workflow | `RunStarted` → `PartialOutputProduced` (streaming) |
| Gerando artefato | `ArtifactRequested` → `ArtifactGenerated` |
| Auditando com Metacognik | `MetacognikReviewed` |
| Enviando para QA Lead | `ApprovalRequested{approver: qa_lead}` |
| Atualizando node | `NodeTransitioned` (via `state_machine_engine`) |
| Registrando decisão | `DecisionRegistered` |
| Erro controlado | `RunFailed` \| `WorkflowFailed` (com `error_category` e sugestão de recovery) |
| Suporte necessário | `SupportRequested` (manual ou por escalação automática de DLQ) |

**Regra de projeção stale:** se `ui_projections.last_event_id` < último evento no event log, o Command Center exibe "Sincronizando..." para campos críticos (aprovação, custo, bloqueio). Nunca age sobre dado defasado (doc 11 §27).

# 9. Leitura de ui_projections

O Command Center lê **exclusivamente** das projeções CQRS — nunca de tabelas de estado diretamente. As sete projeções relevantes para o Command Center (doc 11 §21):

| Projeção | Conteúdo | Modo(s) que consome |
|---|---|---|
| `command_center_suggestions` | Sugestões contextuais por section + priority | Ask, Action (placeholder chips) |
| `agent_activity_projection` | Estado de cada agente: state, last_run_id | Ask, Action, Explain |
| `approval_projection` | Approvals pendentes: status, expires_at, risk_level, cost_estimate | Approval |
| `cost_projection` | Consumo por período: spent_usd, limit_usd, state | Cost, Action (pre-check) |
| `risk_projection` | Riscos ativos: severity, status | Ask, Explain, Action (pre-check) |
| `node_status_projection` | Estado de nodes: status, summary | Ask, Action, Explain |
| `project_pulse_projection` | Pulso geral do projeto: gaps, hipóteses ativas, última decisão | Ask, Explain |

**Regra de atualidade:** O Command Center verifica `last_event_id` antes de exibir estado crítico (aprovação, custo, bloqueio). Se stale, exibe indicador de sincronização e não age sobre dado defasado.

# 10. Eventos emitidos pelo Command Center

O Command Center emite os eventos abaixo para o runtime. Todos incluem `{project_id, user_id, correlation_id, occurred_at}` como campos base (doc 10 §5.3).

| Evento | Quando | Payload relevante |
|---|---|---|
| `IntentSubmitted` | Todo input do usuário | `{text, mode?, slash_command?, mentioned_agent?, section, project_id}` |
| `ApprovalSubmitted` | Usuário decide sobre approval | `{approval_id, decision: approved\|rejected\|changes_requested, note?}` |
| `FeedbackSubmitted` | Usuário avalia output/artifact/workflow *(gap pendente §12.2)* | `{target_type, target_id, rating, comment?, is_implicit: false}` |
| `SupportRequested` | Usuário abre suporte *(gap pendente §12.3)* | `{category, description, run_id?, severity_estimate}` |
| `CostEstimateRequested` | Cost Mode pre-check antes de ação | `{action_type, workflow_id?, context_summary}` |
| `CommandCancelled` | Usuário cancela ação em andamento | `{run_id, reason?}` |

**Regra:** O Command Center nunca emite eventos que deveriam ser gerados por agentes ou pelo runtime (ex.: `AgentHandoff`, `ArtifactGenerated`, `MetacognikReviewed`). Esses são exclusivos do runtime.

# 11. Permissões e governança

O Command Center respeita integralmente o modelo de segurança de doc 12. As regras abaixo são aplicadas pelo `policy_engine` — o Command Center não as implementa internamente; apenas apresenta o resultado da avaliação.

**RBAC:** Toda ação do Command Center é validada contra `role_permissions` do usuário no workspace/projeto. Se `PermissionDenied`, Nick explica o limite e sugere pedido de aprovação quando aplicável.

**ABAC — 7 atributos contextuais (doc 12):** `data_classification`, `risk_level`, `reversibility`, `cost_estimate`, `tenant_id`, `project_scope`, `stakeholder_visibility`. O Command Center injeta esses atributos no `IntentSubmitted` via `context_pack_builder`.

**Tenant isolation:** O Command Center nunca exibe dados de outro tenant ou projeto fora do escopo ativo. Tentativa registrada em `audit_logs` como `TenantBoundaryViolationAttempted` (doc 11 §16.1).

**Data classification:** Artefatos e outputs com `classified: confidential | restricted` não aparecem em resposta de Nick a usuários sem permissão — nem em Explain Mode.

**Model privacy policy (doc 12):** Nick não menciona qual modelo foi usado quando `model_privacy_policy` do projeto bloqueia essa informação.

**Cost policy:** Se uma ação estaria acima de `project_budgets.soft_limit_usd`, Nick mostra estimativa e solicita confirmação antes de emitir `IntentSubmitted`. Se acima de `limit_usd`, exige `ApprovalSubmitted` antes de prosseguir.

**Agents cannot alter policy:** O Command Center nunca permite que um agente ou usuário modifique `policyRegistry` ou `approvalPolicyRegistry` via comando — agentes não têm permissão de escrita nessas tabelas.

**Fluxo de permissão negada:**
1. Nick explica o limite em linguagem do papel do usuário (sem revelar detalhes da política interna)
2. Nick sugere o caminho correto (pedir aprovação, escalonar para role com permissão)
3. Evento registrado em `audit_logs` com `effect: deny`
4. Nenhum dado sensível é revelado

# 12. Gaps de produto/negócio integrados

Os quatro gaps registrados em ARCHITECTURE_PATCH_REPORT §12 impactam o Command Center. Este documento não resolve os gaps — garante apenas que o Command Center os considere e reserve as superfícies necessárias.

## 12.1 ROI (ARCH_PATCH_REPORT §12.1)

**Impacto no Command Center:** `/roi` deve existir como comando. Nick deve ser capaz de responder perguntas de ROI contextual.

**Disponível agora:** `cost_projection` (spent_usd vs. limit_usd por projeto/período). Base de dados em `cost_ledger` + learning tables (doc 11 §18 + §24).

**Pendente (deferred):** `roi_projection` — projeção de ROI multi-dimensão (por projeto, workflow, agente, artifact, campanha). Deve ser adicionada a doc 11 §21 antes de implementação.

**Comportamento no MVP P0:** `/roi` mapeia para `query.roi` → emite `IntentSubmitted{mode: cost}` → Nick responde com `cost_projection` como proxy até `roi_projection` estar disponível.

## 12.2 Feedback (ARCH_PATCH_REPORT §12.2)

**Impacto no Command Center:** Feedback Mode (§5.2.G) e `/feedback` dependem de `feedback_entries` + eventos `FeedbackSubmitted`/`FeedbackImplicit`.

**Disponível agora:** `eval_results` + `decision_outcomes` (doc 11 §24) como proxy de feedback implícito.

**Pendente (deferred):** Tabela `feedback_entries`, eventos `FeedbackSubmitted`, `FeedbackImplicit`, `FeedbackRequested`. Deve ser adicionado a doc 11 v2.x.

**Comportamento no MVP P0:** Feedback Mode existe. Nick coleta avaliação simples (👍/👎 + comentário). Persistência formal é deferred; sinal enviado para `eval_runner` via `eval_results`.

## 12.3 Suporte (ARCH_PATCH_REPORT §12.3)

**Impacto no Command Center:** Support Mode (§5.2.E) e `/support` dependem de `support_tickets` + infraestrutura de ticket.

**Disponível agora:** `SupportRequested` como evento no event log. `run_id`, `trace_id` e `correlation_id` disponíveis para diagnóstico.

**Pendente (deferred):** Tabelas `support_tickets`, `ticket_events`, `incident_reports`. Handoff para operador humano. Help center interno. Deve ser adicionado a doc 11 v2.x ou doc 17.

**Comportamento no MVP P0:** Support Mode existe. Nick coleta descrição e emite `SupportRequested` para o event log. Acompanhamento manual por operador até sistema de tickets estar disponível.

## 12.4 Créditos, Planos e Billing (ARCH_PATCH_REPORT §12.4)

**Impacto no Command Center:** `/credits` e `/billing` dependem de camada de billing (wallet, planos, invoices) que não está em doc 11.

**Disponível agora:** `cost_projection` (consumo de runtime em USD). `project_budgets.state` para detectar aproximação/excesso de limite. `budget_alerts` para notificações.

**Pendente (deferred):** Tabelas `org_wallets`, `plan_subscriptions`, `billing_events`, `invoices`, `credit_ledger`. Projeção `billing_projection`. Fluxos de upgrade/downgrade + approval de custo extra.

**Comportamento no MVP P0:** `/credits` e `/billing` exibem `cost_projection` como estado de consumo. Nick informa quando `project_budgets.state ≠ within_budget`. Gestão financeira real é deferred.

> **Regra geral dos gaps:** O Command Center nunca expõe ao usuário a ausência de uma tabela como erro — exibe o melhor estado disponível via projeções existentes e indica quando a informação está parcialmente disponível.

# 13. Tabelas e projeções relacionadas

O Command Center referencia as seguintes tabelas de doc 11. Não as acessa diretamente — acessa via projeções ou recebe via eventos do runtime.

**Lidas via ui_projections (doc 11 §21):**
- `command_center_suggestions`
- `agent_activity_projection`
- `approval_projection`
- `cost_projection`
- `risk_projection`
- `node_status_projection`
- `project_pulse_projection`

**Escritas via eventos (Command Center emite → runtime escreve):**
- `events` — todo `IntentSubmitted`, `ApprovalSubmitted`, etc. (doc 11 §7)
- `approvals` — via `ApprovalSubmitted` → `approval_gate` (doc 11 §16)
- `audit_logs` — toda ação do usuário registrada automaticamente (doc 11 §16.1)
- `context_packs` — criados pelo `context_pack_builder` em cada intent (doc 11 §13)

**Referenciadas via runtime (Command Center não acessa; runtime comunica via projeção):**
- `workflow_runs` (doc 11 §8)
- `agent_runs` (doc 11 §9)
- `artifacts` + `artifact_versions` (doc 11 §17)
- `decisions` + `decision_events` (doc 11 §16)
- `cost_ledger` + `project_budgets` + `budget_alerts` (doc 11 §18)
- `eval_results` (doc 11 §19)

**Tabela de histórico de comandos — pendência de patch para doc 11 v1.2.x:**

```txt
command_history [APPEND-ONLY]
(
  id               uuid primary key (v7),
  org_id           fk→organizations [RLS],
  workspace_id     fk→workspaces,
  project_id       fk→projects,
  user_id          fk→users,
  mode             enum(ask|action|approval|explain|support|cost|feedback),
  slash_command    text,
  intent_text      text,
  intent_type      text,
  correlation_id   uuid,
  run_id           uuid,
  outcome          enum(completed|failed|cancelled|blocked|pending_approval),
  created_at       timestamptz default now()
)
[idx: project_id, user_id, created_at]
[idx: correlation_id]
```

Esta tabela é necessária para: histórico de comandos no MVP P0, sugestões contextuais baseadas em padrão de uso e aprendizado de intenção via `learning_loop_engine`.

# 14. MVP P0 do Command Center

**Entra no MVP P0** (mínimo para o Command Center funcionar ponta a ponta):

```txt
Input de intenção em linguagem natural
Nick respondendo com contexto (Ask Mode + Action Mode)
Status de execução em tempo real — 16 estados vivos (§8)
Approval requests com contexto completo (Approval Mode)
Leitura das 7 ui_projections (§9)
Sugestões contextuais via command_center_suggestions
Estimativa de custo básica via cost_projection (Cost Mode parcial)
Feedback simples 👍/👎 + comentário (Feedback Mode parcial — sem feedback_entries)
Support Mode: emissão de SupportRequested (sem gestão de ticket)
Histórico de comandos via command_history (patch doc 11 v1.2.x)
Audit log automático de todas as ações do usuário via runtime
Slash commands MVP: /briefing /diagnosis /research /nodes /workflow /agents /audit /proposal /artifact /approve /cost /explain /memory /evidence
```

**Fica fora do MVP P0 (evolução):**

```txt
/roi com roi_projection real — roi_projection pendente em doc 11 §21
/competitors como workflow dedicado — pode ser coberto por /research no MVP
/billing com billing_projection real — billing_ledger e wallet são deferred
/credits com credit_ledger real — deferred
/feedback com persistência formal — feedback_entries é deferred
/support com gestão de ticket — support_tickets é deferred
/replay completo — run_replays visual avançado é deferred
/admin avançado — deferred para operadores
Marketplace de comandos
Automação financeira completa
Suporte omnichannel
Model router visual avançado
Analytics financeiro avançado
Personalização profunda por cliente
Voice I/O
```

# 15. Edge cases

| Situação | Comportamento esperado |
|---|---|
| Comando ambíguo (confidence < threshold) | Nick pede esclarecimento antes de emitir `IntentSubmitted`; nunca assume intenção com baixa confiança |
| Usuário sem permissão | `PermissionDenied` → Nick explica limite sem revelar política interna; sugere caminho correto; registra `audit_logs{effect: deny}` |
| Custo acima do soft_limit | Nick mostra estimativa e pede confirmação antes de executar |
| Custo acima do hard_limit | Exige `ApprovalSubmitted` antes de prosseguir; workflow não inicia |
| Agente indisponível | `intent_router` retorna fallback_agent sugerido; Nick informa e pergunta se prossegue |
| RAG sem fonte suficiente | `context_pack_builder` retorna `ContextAssembled{confidence: low}`; Nick indica limitação de contexto antes de executar |
| Aprovação expirada | `approval_expirations.action_on_expire` define comportamento; Nick notifica e apresenta opções (renovar, escalonar, cancelar) |
| Workflow travado (state: blocked) | Nick detecta via `node_status_projection`; exibe estado + razão do bloqueio via Explain Mode |
| Output com baixa confiança | `MetacognikReviewed.confidence` < threshold → Nick apresenta score + recomendação antes de exibir resultado |
| Ação irreversível | Qualquer ação com `reversible: false` → `approval_gate` obrigatório; Nick explica irreversibilidade com detalhes |
| Cross-project access attempt | `policy_engine` nega; `audit_logs` registra `TenantBoundaryViolationAttempted`; Nick informa sem revelar dado do outro projeto |
| Capability não ativada | `policy_engine` retorna `CapabilityScopeViolation`; Nick informa que o módulo não está ativo e sugere ativação se o usuário tem permissão |
| Suporte durante ação crítica | Support Mode pode ser invocado em qualquer estado; não cancela workflow ativo; Nick abre suporte em paralelo e mantém status do workflow visível |
| Projeção stale | Command Center exibe "Sincronizando..." para campos críticos; não age sobre dado defasado; aguarda próximo evento de projeção |
| Loop de agente detectado | `loop_detector` emite `AgentLoopDetected`; workflow entra em `state: blocked`; Nick notifica com `trace_id` e sugere `/support` |

# 16. Critérios de aprovação

- Command Center emite eventos para o runtime para toda ação — sem atalhos diretos a agentes, tabelas ou APIs de provider
- Nick mantém contexto do projeto ativo em todas as respostas
- Leitura de estado exclusivamente via `ui_projections` — nunca via queries diretas a tabelas de domínio
- Approval Mode funciona: usuário pode aprovar/rejeitar/pedir revisão e o workflow resume corretamente
- Os 16 estados vivos (§8) têm evento de runtime correspondente e são exibidos sem inventar progresso
- Permissões respeitadas: `PermissionDenied` resulta em explicação, não em execução silenciosa
- Custo estimado exibido antes de ações que impactam orçamento
- Todos os 22 slash commands da tabela §5.4 mapeiam para `intent_type` + `emitted_event`
- Edge cases de permissão, custo e ambiguidade cobertos sem quebrar fluxo
- Gaps §12.1–12.4 têm comportamento definido no MVP P0 (sem dependência de tabelas ainda inexistentes)

# 17. Critérios de reprovação

- Command Center virar chatbot passivo (responde texto sem emitir eventos de runtime)
- Executar ação sem emitir `IntentSubmitted` para o runtime
- Nick inventar estado que não está em `ui_projections` ou `audit_logs`
- Nick revelar dado sensível de outro tenant, projeto ou usuário
- Aprovação ignorada (workflow prossegue sem `ApprovalGranted`)
- Agente escolhido manualmente pelo Command Center (bypassando `agent_router`)
- Command Center escrevendo diretamente em tabelas de domínio (`nodes`, `workflows`, `approvals`)
- Custo ignorado (ação executada mesmo com `project_budgets.state = blocked_by_cost`)
- Slash command sem mapeamento para `emitted_event`
- Projeção stale tratada como estado verdadeiro

# 18. Métricas de sucesso

- Taxa de interpretação correta de intenção (intent confidence ≥ threshold em % dos casos)
- % de approvals bem encaminhadas antes da expiração (`approval_projection.status ≠ expired`)
- Tempo médio intenção→primeiro evento de runtime
- % de comandos resolvidos sem retrabalho (sem re-emissão do mesmo intent em < N minutos)
- % de estados vivos exibidos corretamente e dentro do SLA de projeção
- Uso recorrente de slash commands (adoção por sessão e por usuário ativo)
- Satisfação de Feedback Mode simples (sinal de qualidade de Nick via `eval_results`)
- Taxa de `PermissionDenied` com explicação satisfatória (sem segundo pedido de esclarecimento)
- % de edge cases de custo tratados sem workflow abortado indevido

## Patch 1.1.1 — Intent Taxonomy

Adicionado para ampliar o Command Center além de atalhos de comando e operações de negócio.
ROI, Feedback, Suporte e Créditos reposicionados como famílias **#8–9 de 10** dentro do mapa completo de intenções — sem remover os gaps registrados em ARCH_PATCH_REPORT §12.
Slash commands expandidos de 16 para **22**, mapeando as 10 famílias.
Exemplos em §2 atualizados para cobrir todas as famílias.
Fluxo canônico obrigatório confirmado: `User input → Command Center → IntentSubmitted → intent_router → context_pack_builder → transformer/instruction/prompt layer → policy_engine → workflow_engine → agent_router → model_router → approval_gate → eval_runner / Metacognik → ui_projection_engine → Command Center / Nick`.

# 19. Related notes

- [[03_AGENT_OPERATING_MODEL]] — modelo operacional de Nick e agentes; handoff protocol
- [[10_SYSTEM_RUNTIME_ARCHITECTURE]] — fluxo canônico §5.2; engines §5.15; event protocol §5.16; approval gate §5.8
- [[11_DATA_MODEL_AND_PERSISTENCE]] v1.1.2 — ui_projections §21; cost_ledger §18; approvals §16; audit_logs §16.1
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]] v1.1.0 — RBAC, ABAC, policy_engine, data classification, model privacy
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]] v1.1.0 — cost guard, eval scores, model router policy
- [[14_PROJECT_DASHBOARD_ARCHITECTURE]] — dashboard de projeto; ROI; métricas de performance
- [[16_NODE_CANVAS_ARCHITECTURE]] — Node Canvas; estados de node; transições
- [[ARCHITECTURE_PATCH_REPORT]] v1.1.0 — gaps §12.1–12.4; Manus §13
