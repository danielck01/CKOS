---
title: Project Dashboard Architecture
file: 14_PROJECT_DASHBOARD_ARCHITECTURE.md
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
  Definir o Project Dashboard como projeção executiva do estado vivo do runtime de um projeto
  específico — não página estática de analytics, não cockpit genérico, não fonte de verdade.
inputs: >
  Runtime Architecture (10 v1.1.0); Data Model (11 v1.1.2); Security (12 v1.1.0);
  Evals (13 v1.1.0); Command Center (15 v1.2.1); Node Canvas (16 v1.2.0); Object Model (02)
outputs: >
  Dashboard adaptativo com 10 widgets obrigatórios; widget system modular; views por perfil
  (admin, founder, client, stakeholder); comandos contextuais via CommandBar; MVP P0 definido.
framework: >
  Projeção CQRS de ui_projections (11 §21). Lê de nodes, events, agents, approvals, costs,
  evidence, feedback, decisions. Emite intents. Nunca escreve estado diretamente.
edge_cases: >
  Projeto sem nodes; dados insuficientes; ROI não financeiro; usuário sem permissão de custo;
  projection stale; agent run falhou; layout customizado perdeu widget crítico; projeto muda tipo.
integrations: >
  Lê de ui_projections (11 §21); emite intenções via Command Center (15); consome event bus
  (10 §5.3); permissões via Security (12); evals/custos via doc 13; Node Canvas (16) para drill-down.
prompts: >
  Project Pulse executivo; sugestão de capabilities; diagnóstico contextual; widget suggestions.
metrics: >
  Tempo até entender o estado do projeto (<30s); decisões críticas visíveis sem busca;
  % de widgets com dados de projeção válida; nº de actions tomadas a partir do dashboard;
  nº de nodes com evidência; nº de approvals completados via dashboard.
related_notes:
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - 15_COMMAND_CENTER_ARCHITECTURE.md
  - 16_NODE_CANVAS_ARCHITECTURE.md
  - ../01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md
  - ../ARCHITECTURE_PATCH_REPORT.md
  - ../QA_DOCUMENTATION_CHECKLIST.md
tags: [product, dashboard, adaptive, projection, cockpit, widgets, executive-view]
---

> **Project Dashboard is not a static analytics page. It is the executive projection of the project runtime state, generated from nodes, events, agents, approvals, costs, evidence, feedback and decisions.**
>
> O dashboard do projeto não é um painel fixo. Ele é a leitura executiva do que o sistema está pensando, fazendo, esperando, custando, arriscando e aprendendo naquele projeto.
>
> O Project Dashboard nunca armazena verdade própria. Lê de `ui_projections`. Emite intenções. O Runtime é a fonte da verdade.

# 1. Propósito

O **Project Dashboard** é a home operacional de um projeto específico no CKOS. É onde o usuário — em qualquer perfil — chega ao projeto e entende em segundos:

- O que está acontecendo agora neste projeto?
- O que mudou desde a última visita?
- O que precisa da minha decisão?
- Quais agentes estão trabalhando e em quê?
- Quais nodes estão críticos, bloqueados ou aguardando?
- Quais riscos e lacunas surgiram?
- Quanto este projeto está custando?
- O que os feedbacks indicam?
- Qual é o estado atual do ROI?
- O que o sistema recomenda como próxima ação?

O Project Dashboard responde a essas perguntas como **projeção executiva** do Runtime — não como painel fixo de analytics. O conteúdo é derivado de eventos, nodes, agentes, approvals, custos, evidências, feedbacks e decisões do projeto. É adaptativo por tipo de projeto, perfil de usuário e estado atual do Runtime.

**O que o Project Dashboard não é:**

- Não é página estática de métricas.
- Não é fonte de verdade — a verdade vive no Runtime (doc 10) e no Data Model (doc 11).
- Não é substituto do Node Canvas (doc 16) — Canvas é a superfície visual de trabalho; Dashboard é a leitura executiva.
- Não é substituto do Command Center (doc 15) — CC captura intenção; Dashboard apresenta estado.
- Não é CKOS Home — CKOS Home é visão global de todos os projetos do usuário; este Dashboard é de um único projeto.
- Não calcula ROI, não processa billing, não executa agentes — emite intenções ao Runtime.
- Não escreve estado diretamente em tabelas de domínio.

# 2. O que é / o que não é o Project Dashboard

## 2.1 É

| É | Razão |
|---|-------|
| Projeção executiva do runtime de um projeto | Lê de `ui_projections` e event bus — estado derivado, não armazenado |
| Home operacional de um projeto específico | Responde às 10 perguntas do §1 em <30s |
| Superfície de tomada de decisão | Exibe approval queues, decision nodes, risks, gaps e next actions |
| Ponto de entrada para Node Canvas e Command Center | Drill-down direto do widget para o Canvas; intenção via CommandBar |
| Superfície adaptativa por tipo de projeto e perfil | Widgets aparecem porque o Runtime, nodes ativos ou permissões justificam |
| Interface de monitoramento de agentes | Exibe agent_activity_projection em tempo real |
| Cockpit de custo e ROI | Cost summary e ROI snapshot sempre visíveis para quem tem permissão |

## 2.2 Não é

| Não é | Por quê |
|-------|---------|
| Fonte de verdade | Estado vive no Runtime; Dashboard lê projeções |
| Node Canvas | Canvas é workspace visual de trabalho — Dashboard é leitura executiva |
| Command Center | CC captura intenção; Dashboard apresenta estado |
| CKOS Home | CKOS Home é visão multi-projeto; este doc é single-project |
| Ferramenta de BI/analytics | Não é Metabase, Looker nem Grafana. É cockpit operacional de projeto |
| Sistema de billing | Projeta custos e créditos; não gerencia planos, cobranças ou invoices |
| Calculadora de ROI | Exibe ROI de nodes/projections; não calcula nem modela ROI próprio |

# 3. Separação: CKOS Home vs. Project Dashboard vs. Command Center vs. Node Canvas

Esta separação é estrutural — cada superfície tem responsabilidade única e não se substitui.

| Superfície | Escopo | Responsabilidade principal |
|---|---|---|
| **CKOS Home** | Todos os projetos do usuário / admin | Visão global: todos os projetos, alertas globais, approvals globais, custos globais, plano/créditos, suporte geral, convites, últimas atividades, onboarding |
| **Project Dashboard** (este doc) | Um único projeto | Status do projeto; agentes ativos; nodes críticos; decisões pendentes; ROI; custos; riscos; gaps; artifacts; feedbacks; tickets; approvals; atividades recentes |
| **Command Center (15)** | Intenção e acompanhamento dentro de um projeto | Captura intenção; conversa com Nick; acompanha execução; mostra status de agentes; não executa diretamente; não apresenta estado executivo |
| **Node Canvas (16)** | Grafo de objetos e workflows de um projeto | Superfície visual de trabalho: nodes, edges, workflows, operações; não é fonte de verdade; não é dashboard executivo |

**Regra de navegação:**

```txt
CKOS Home → seleciona projeto → Project Dashboard (home operacional)
Project Dashboard → clica em "abrir canvas" → Node Canvas
Project Dashboard → digita comando → Command Center / CommandBar
Node Canvas → emite intenção → Command Center
Command Center → atualiza projeção → Project Dashboard (via ui_projection)
```

# 4. Relação com Runtime, Data Model, Security e Evals

| Componente | Relação com o Dashboard |
|---|---|
| **Runtime (10)** | Fonte de estado via `ui_projection_engine`. Dashboard nunca chama Runtime diretamente — consome projeções. |
| **Data Model (11)** | Persistência. Dashboard lê das `ui_projections` (§21 de doc 11), que são derivadas das tabelas de domínio. |
| **Security (12)** | Toda renderização é filtrada por RBAC + ABAC + RLS. Dashboard não exibe o que o ator não pode ver. |
| **Evals / Metacognik (13)** | Dashboard exibe `confidence_score`, `eval_results`, quality gates, warnings e estado de auditoria do Metacognik. |
| **Command Center (15)** | Dashboard hospeda o CommandBar (§25). Toda intenção do Dashboard passa pelo intent_router do CC. |
| **Node Canvas (16)** | Dashboard exibe Node Health widget baseado em `node_status_projection`. Drill-down abre o Canvas no node específico. |

# 5. Princípios do Project Dashboard

1. **projection-not-source-of-truth** — Dashboard lê de `ui_projections`. Nunca calcula estado próprio, nunca escreve em tabelas de domínio.
2. **adaptive-by-runtime** — Widgets aparecem porque o Runtime, o tipo de projeto, os nodes ativos ou as permissões justificam — não por configuração padrão.
3. **executive-first** — O usuário deve entender o estado do projeto em menos de 30 segundos sem precisar navegar para outras superfícies.
4. **intent-not-execution** — Dashboard emite intenções (via CommandBar ou ações em widgets). Nunca executa agentes, workflows ou mutations diretamente.
5. **decision-surface** — Decisions, approvals e risk acknowledgments devem ser ações de primeiro nível — visíveis e acionáveis sem drill-down profundo.
6. **cost-always-visible** — Custo e consumo de créditos do projeto são sempre exibidos para quem tem permissão (`lead+`). Não são seções escondidas.
7. **evidence-anchored** — Dados exibidos no dashboard (ROI, risk, confidence) devem ter evidências rastreáveis. Dashboard não inventa estado.
8. **whitelabel-adaptive** — Layout, cores e tipografia são parametrizados pelo `design_system` ativo (branddock). Dashboard não tem identidade visual própria fixada.
9. **never-cross-tenant** — RLS na camada de projeção garante que nunca aparecem dados de outro tenant, mesmo por bug de projeção.
10. **mobile-reads** — Dashboard MVP tem leitura em mobile. Criação e edição são pós-MVP em mobile.
11. **projection-freshness** — Dashboard exibe timestamp de última atualização da projeção. Se projeção está stale, exibe aviso sem bloquear a leitura.
12. **persona-agnostic** — Dashboard não hardcoda tipo de projeto (e-commerce, branding, influencer). Nasce neutro e adapta widgets por contexto.

# 6. Data Sources

O Project Dashboard lê exclusivamente destas fontes:

```txt
ui_projections (11 §21)       → base principal de todos os widgets
  ├── node_status_projection
  ├── agent_activity_projection
  ├── approval_projection
  ├── cost_projection
  ├── risk_projection
  ├── project_pulse_projection
  └── command_center_suggestions

events (10 §5.3)               → feed de atividades recentes
workflow_runs (11 §6)          → estado de workflows em execução
agent_runs (11 §7)             → execuções de agentes
nodes (11 §4)                  → via node_status_projection
approvals (11 §13)             → via approval_projection
artifacts (11 §10)             → artifacts gerados no projeto
decisions (node type §5.13)    → decisions registradas
risks (node type §5.6)         → risks detectados
gaps (node type §5.7)          → gaps identificados
hypotheses (node type §5.5)    → hipóteses ativas
evidence_items (11 §14)        → evidências vinculadas a nodes
cost_ledger (11 §18)           → custos via cost_projection
eval_results (11 §15)          → confidence scores
support_tickets (gap §12.3)    → tickets abertos (gap — ver §31)
feedback_items (gap §12.2)     → feedbacks recebidos (gap — ver §31)
project_settings               → configurações do projeto
stakeholders (11)              → perfis e roles do projeto
memory_summaries (11 §20)      → quando permitido por policy (12 §5.9)
```

**Regra:** Dashboard não lê de tabelas de domínio diretamente. Toda leitura passa por `ui_projections` ou pelo event feed. Se uma projeção não existe, o widget correspondente exibe estado neutro — não inventa dados.

# 7. Modelo de UI Projections

Dashboard consome as 7 `ui_projections` de doc 11 §21. Cada widget tem projeção(ões) responsável(is):

| Widget | Projeções consumidas |
|---|---|
| Project Pulse | `project_pulse_projection` |
| What Needs Decision | `approval_projection`, `node_status_projection` |
| AI Activity | `agent_activity_projection` |
| Node Health | `node_status_projection` |
| ROI Snapshot | `cost_projection`, `node_status_projection` |
| Cost & Credits | `cost_projection` |
| Feedback Loop | `node_status_projection` (feedback nodes) |
| Support & Friction | `node_status_projection` (support nodes) |
| Artifacts Generated | `node_status_projection` (artifact nodes) |
| Risk, Gap & Evidence Monitor | `risk_projection`, `node_status_projection` |
| CommandBar suggestions | `command_center_suggestions` |
| Header / Pulse indicator | `project_pulse_projection` |

**Atualização das projeções:** streaming em tempo real via SSE (doc 10 §5.9) para widgets de AI Activity e Project Pulse. Polling periódico para widgets de custo e ROI. Widgets exibem timestamp de última atualização.

# 8. Dashboard Adaptativo

O Project Dashboard **nasce neutro** — não tem widgets de e-commerce, campanha, financeiro ou qualquer capability específica por padrão. Widgets contextuais aparecem quando o Runtime, os nodes ativos, o tipo de projeto configurado ou as permissões justificam.

**Lógica de ativação de widgets contextuais:**

```txt
node_type presente no projeto → widget correspondente ativado
  campaign nodes ativos → Campaigns widget sugerido
  roi nodes com dados → ROI Snapshot widget sugerido
  feedback nodes ativos → Feedback Loop widget ativado
  support nodes ativos → Support & Friction widget ativado
  billing nodes → Cost & Credits widget (sempre visível para lead+)
```

**4 exemplos de perfil adaptativo:**

### Branding institucional
Widgets prioritários: Briefing, Posicionamento (Strategy nodes), Stakeholders, Concorrentes (Research nodes), Persona/Brand nodes, Proposta (Artifact), Artifacts aprovados, ROI estratégico.  
Widgets ausentes: Commerce, Conversão, Estoque, Campanhas pagas.

### E-commerce
Widgets prioritários: Produtos (Campaign/Artifact nodes), Conversão (ROI node), Ticket médio, Competidores (Research), Campanhas (Campaign nodes), ROI financeiro.  
Widgets contextuais: Estoque (se integração ativa), Ads (se collector configurado).

### Influencer / personal brand
Widgets prioritários: Persona nodes, Conteúdo (Artifact), Comunidade (Research), Audiência (Evidence), Narrativa (Briefing), Calendário de conteúdo (Workflow), Feedback Loop, ROI de crescimento.  
Widgets ausentes: Commerce, B2B, Financeiro complexo.

### Projeto interno CKOS
Widgets prioritários: Sprints (Workflow nodes), Issues (Gap/Risk nodes), Agent Runs (AI Activity), Custos de modelo (Cost & Credits), QA (Eval nodes), Decisões técnicas (Decision nodes).  
Widgets contextuais: Deploy (System nodes, se configurado).

> **Regra anti-hardcode:** nenhum destes perfis é configuração padrão permanente. O dashboard deriva perfil por contexto, nodes ativos e configuração de projeto — nunca assume e-commerce como padrão.

# 9. Widget System Architecture

## 9.1 Tipos de widget

| Tipo | Comportamento |
|---|---|
| `fixed_required` | Sempre presente; não pode ser ocultado ou removido pelo usuário |
| `runtime_suggested` | Sugerido pelo sistema quando o Runtime ou nodes justificam; usuário pode aceitar, recusar ou adiar |
| `node_generated` | Aparece automaticamente quando um node type específico está ativo no projeto |
| `user_pinned` | Usuário fixou manualmente; persiste no layout até ser removido |
| `admin_locked` | Admin travou o widget em posição e visibilidade; usuário não pode mover ou ocultar |
| `plan_locked` | Widget disponível apenas em planos específicos; exibe teaser em planos inferiores |
| `experimental` | Feature flag ativo; visível apenas para usuários beta |

## 9.2 Widgets obrigatórios (fixed_required)

Todo Project Dashboard deve ter estes 10 widgets. Podem ser minimizados mas nunca removidos:

| # | Widget | Tipo | Projeção base |
|---|---|---|---|
| 1 | Project Pulse | `fixed_required` | `project_pulse_projection` |
| 2 | What Needs Decision | `fixed_required` | `approval_projection` |
| 3 | AI Activity | `fixed_required` | `agent_activity_projection` |
| 4 | Node Health | `fixed_required` | `node_status_projection` |
| 5 | ROI Snapshot | `fixed_required` | `cost_projection` |
| 6 | Cost & Credits | `fixed_required` | `cost_projection` |
| 7 | Feedback Loop | `fixed_required` | `node_status_projection` |
| 8 | Support & Friction | `fixed_required` | `node_status_projection` |
| 9 | Artifacts Generated | `fixed_required` | `node_status_projection` |
| 10 | Risk, Gap & Evidence Monitor | `fixed_required` | `risk_projection` |

## 9.3 Hierarquia de renderização

```txt
1. Verificar permissão do ator (RBAC + ABAC + RLS)
2. Verificar projeção disponível (freshness check)
3. Verificar se widget_type permite renderização no plano atual
4. Renderizar com dados ou em estado neutro (sem inventar)
5. Exibir timestamp de última atualização da projeção
```

## 9.4 Widget em estado neutro

Quando a projeção não tem dados suficientes (projeto novo, dados ausentes, projeção stale), o widget:
- Exibe título e ícone normalmente.
- Exibe mensagem de estado neutro: "Nenhum dado disponível ainda" ou "Aguardando execução de agente".
- Não exibe dados fictícios ou placeholders enganosos.
- Exibe botão de ação contextual quando aplicável: "Criar briefing", "Iniciar diagnóstico", etc.

# 10. Widget: Project Pulse

**Tipo:** `fixed_required`  
**Projeção:** `project_pulse_projection`  
**Permissão mínima:** `project_member`

O Project Pulse é o **resumo executivo do estado atual do projeto** — gerado pelo Runtime a partir de nodes, events, agent runs, approvals, costs e evidence. É a primeira coisa que o usuário vê.

**Conteúdo do Project Pulse:**

- Estado geral do projeto: `on_track | at_risk | blocked | waiting_decision | idle`
- Última atividade significativa: qual agente atuou, qual node foi criado, qual decision foi registrada.
- Nodes críticos: quantos nodes em estado `blocked` ou `pending_approval`.
- Agentes ativos: quantos rodando agora, qual tarefa.
- Alertas de risco: N risks em estado `active`.
- Próxima ação recomendada: gerada pela `command_center_suggestions` projection.
- Confidence geral do projeto: média ponderada dos `confidence_scores` dos nodes ativos.

**O Project Pulse não é gerado pelo Dashboard.** É gerado pelo `ui_projection_engine` a partir de eventos do Runtime. Dashboard apenas renderiza a projeção.

# 11. Widget: What Needs Decision

**Tipo:** `fixed_required`  
**Projeção:** `approval_projection`, `node_status_projection`  
**Permissão mínima:** `contributor`

Exibe todos os itens que requerem ação humana explícita **neste projeto** — ordenados por urgência e impacto.

**Conteúdo:**

- Approvals pendentes: lista de nodes em `pending_approval` com: título, tipo, quem pediu, há quanto tempo, prazo (se configurado), impacto estimado.
- Decisions sem aprovação de segundo nível (quando policy exige co-aprovação).
- Workflows pausados em `waiting_approval`.
- Nodes `blocked` que exigem intervenção humana (não apenas agente).
- Escalamentos de aprovação expirada.

**Ações disponíveis direto no widget:**

- Aprovar / rejeitar inline (para approvals simples de primeiro nível).
- "Ver detalhes" → abre Node Inspector no Canvas.
- "Delegar para [pessoa]" → emite `ApprovalDelegated` → Runtime.

Nenhuma ação escreve estado diretamente — tudo via `ApprovalSubmittedFromDashboard → Runtime`.

# 12. Widget: AI Activity

**Tipo:** `fixed_required`  
**Projeção:** `agent_activity_projection`  
**Permissão mínima:** `project_member`

Exibe o que os agentes estão fazendo no projeto **em tempo real**.

**Conteúdo:**

- Agentes rodando agora: nome do agente, node onde está atuando, estado (`working | waiting_tool | waiting_approval | blocked`), tempo de execução.
- Últimas execuções concluídas: agente, node, output gerado, `confidence_score`.
- Execuções com erro ou bloqueio: agente, motivo, node afetado, ação disponível.
- Metacognik warnings: se Metacognik emitiu auditoria ou bloqueio, aparece como alerta de topo.
- Custo acumulado de runs na sessão: créditos consumidos por agente (para `lead+`).

**Atualização:** streaming em tempo real via SSE (doc 10 §5.9). Badge de "vivo" quando há agentes ativos.

# 13. Widget: Node Health

**Tipo:** `fixed_required`  
**Projeção:** `node_status_projection`  
**Permissão mínima:** `project_member`

Exibe o **estado de saúde dos nodes críticos** do projeto — não todos os nodes, mas os que precisam de atenção.

**Conteúdo:**

- Nodes `blocked`: lista com motivo, node_type, owner, quanto tempo bloqueado.
- Nodes `pending_approval`: aguardando decisão.
- Nodes `suggested` sem confirmação (há N dias): sugestões pendentes de agentes.
- Nodes sem evidência vinculada: nodes em estado `active` sem `evidence_links`.
- Nodes com `confidence_score` abaixo do threshold.
- Nodes com `risk_level = critical`.

**Ações:**

- "Ver no Canvas" → abre o Canvas no node específico.
- "Confirmar sugestão" inline para `ai_suggested` nodes simples.

# 14. Widget: ROI Snapshot

**Tipo:** `fixed_required`  
**Projeção:** `cost_projection`, `node_status_projection`  
**Permissão mínima:** `lead`

**O dashboard não calcula ROI.** Exibe o que está nos ROI nodes, evidence_items, hypotheses e cost_ledger — derivado de `cost_projection` e dos nodes do tipo ROI/Cost.

**Tipos de ROI suportados:**

| Tipo | Descrição |
|---|---|
| `financial_roi` | Retorno financeiro direto (receita, conversão, ticket médio) |
| `strategic_roi` | Posicionamento, market share, diferenciação |
| `operational_roi` | Eficiência de processos, redução de retrabalho |
| `brand_roi` | Reconhecimento, autoridade, share of voice |
| `content_roi` | Alcance, engajamento, conversão por conteúdo |
| `acquisition_roi` | Custo de aquisição de clientes, CAC |
| `retention_roi` | Redução de churn, LTV |
| `efficiency_roi` | Tempo economizado, automação bem-sucedida |
| `learning_roi` | Hipóteses confirmadas, decisões melhores, aprendizado documentado |

**Conteúdo do ROI Snapshot:**

- ROI estimado (por tipo ativo no projeto).
- ROI realizado quando disponível (evidence_items ligados ao ROI node).
- Hipóteses de retorno ativas.
- Evidências usadas e `confidence` por hipótese.
- Lacunas de dados que impedem cálculo (gaps detectados).
- Custo acumulado do projeto até agora.
- Payback estimado.
- Risks que afetam ROI.

> **Gap registrado:** ROI Architecture completa aguarda doc dedicado (ARCH_PATCH_REPORT §12.1). ROI Snapshot exibe dados disponíveis via projeção — sem garantia de completude até ROI Architecture ser definida.

# 15. Widget: Cost & Credits

**Tipo:** `fixed_required`  
**Projeção:** `cost_projection`  
**Permissão mínima:** `lead`

**Conteúdo:**

- Créditos consumidos neste projeto até hoje.
- Créditos previstos para execuções planejadas / workflows queued.
- Custo por run (média dos últimos N runs).
- Custo por agente (breakdown por agente ativo no projeto).
- Custo por modelo (breakdown por LLM chamado).
- Custo por coletor (se collectors ativos).
- Custo por workflow (mais caro dos últimos N).
- Alertas de orçamento: aviso quando projeto atinge 70%, 90% e 100% do budget configurado.
- Ações bloqueadas por custo: lista de execuções pausadas por `cost_guard` (doc 13 §11).
- Projeção de consumo nos próximos 7 dias (baseada em ritmo atual).
- Recomendação de upgrade quando projeção excede plano (texto neutro, não pressão de vendas).

**Regra:** Cost & Credits projeta — não cobra, não processa pagamento, não gerencia plano. Esses são sistemas externos.

> **Gap registrado:** Credits, Plans & Billing precisam de doc dedicado (ARCH_PATCH_REPORT §12.4). Widget exibe dados de `cost_projection` e `cost_ledger` — sem billing completo até o sistema ser definido.

# 16. Widget: Feedback Loop

**Tipo:** `fixed_required`  
**Projeção:** `node_status_projection` (feedback nodes)  
**Permissão mínima:** `contributor`

Feedback **não é comentário solto**. Feedback é objeto operacional que pode alterar o projeto via Runtime — convertido em node, task, gap, improvement ou decision.

**Conteúdo:**

- Feedbacks recebidos: lista com tipo, fonte, data, status (`pending | processing | resolved | rejected`).
- Feedbacks pendentes de análise.
- Feedbacks analisados por agentes (com confidence e recomendação).
- Feedbacks convertidos em nodes (link para o node gerado).
- Feedbacks convertidos em tasks (link para o workflow).
- Feedbacks rejeitados com justificativa registrada.
- Feedbacks que alteraram uma decisão já registrada.
- Feedbacks que afetaram ROI, proposta, campanha ou escopo.

**Fluxo operacional:**

```txt
Feedback recebido → FeedbackSubmitted
  → Runtime → node_status_projection atualizada
  → Dashboard exibe no widget
  → Agente (opcional) analisa → emite FeedbackAnalyzed
  → Usuário decide: converter em node / task / rejeitar
  → Dashboard emite intent → Runtime processa
```

> **Gap registrado:** Feedback System completo aguarda doc dedicado (ARCH_PATCH_REPORT §12.2).

# 17. Widget: Support & Friction

**Tipo:** `fixed_required`  
**Projeção:** `node_status_projection` (support nodes)  
**Permissão mínima:** `contributor`

**Conteúdo:**

- Tickets abertos neste projeto: prioridade, status, assignee, há quanto tempo aberto.
- Dúvidas recorrentes (padrão detectado por Nick entre sessões do mesmo projeto).
- Bloqueios do usuário: nodes em `waiting_input` há mais de N horas.
- Erros controlados: runs com status `failed` que não bloquearam o projeto mas precisam de atenção.
- Fricções detectadas: ações tentadas repetidamente sem sucesso (feedback implícito).
- Tempo médio de resposta por tipo de suporte.
- Impacto no projeto: tickets que bloqueiam workflow ou approval ativo.
- Ações disponíveis: converter ticket em node, task, approval ou artifact.

**Escalamento:**

Suporte pode escalar para incidente quando: impacto estimado é `high` ou `critical`, tempo sem resolução excede threshold configurado, ou Metacognik emite warning de bloqueio sistêmico.

> **Gap registrado:** Support System completo aguarda doc dedicado (ARCH_PATCH_REPORT §12.3).

# 18. Widget: Artifacts Generated

**Tipo:** `fixed_required`  
**Projeção:** `node_status_projection` (artifact nodes)  
**Permissão mínima:** `project_member`

**Conteúdo:**

- Artifacts gerados: lista com tipo, título, data de criação, `approval_status`, agente responsável, `confidence_score`.
- Artifacts aguardando aprovação.
- Artifacts aprovados (disponíveis para download/entrega).
- Artifacts rejeitados com motivo.
- Artifacts em revisão.
- Última versão de cada artifact.
- Custo de geração por artifact (para `lead+`).

**Ações:**

- "Ver artifact" → abre visualização.
- "Aprovar / rejeitar" inline para lead+.
- "Gerar nova versão" → emite intent → Runtime.
- "Enviar para cliente" → emite intent → Runtime → gera link de compartilhamento com policy de acesso.

# 19. Widget: Risk, Gap & Evidence Monitor

**Tipo:** `fixed_required`  
**Projeção:** `risk_projection`, `node_status_projection`  
**Permissão mínima:** `project_member`

**Conteúdo:**

- Risks ativos: `risk_level`, descrição, nó afetado, há quanto tempo ativo, status de mitigação.
- Risks críticos: badge de alerta de topo — sempre visível independente de filtro.
- Gaps detectados: lacunas de informação, capacidade ou dependência não resolvida.
- Hypotheses ativas: hipóteses sem confirmação, com confidence e evidence links.
- Evidence summary: quantidade de evidence nodes, % com `confidence > threshold`, evidências contraditórias ativas.
- Warnings do Metacognik: se Metacognik emitiu auditoria de confiança baixa ou contradição de evidências.

**Ações:**

- "Mitigar risco" → emite intent → Runtime → cria Risk node de mitigação.
- "Preencher lacuna" → emite intent → Research workflow.
- "Testar hipótese" → emite intent → Hypothesis workflow.
- "Ver evidências" → drill-down para Node Inspector no Canvas.

# 20. Stakeholder View

**Quem acessa:** roles com escopo definido por `permissions_scope` do projeto — parceiros, consultores, times externos com acesso restrito.

**O que vê:**

- Apenas blocos relacionados ao seu papel e escopo.
- Nodes que o têm como `owner` ou que estão no `permissions_scope` do seu role.
- Approvals que requerem sua ação.
- Artifacts compartilhados com seu perfil.
- Nenhum dado de custo, crédito ou billing — a menos que explicitamente configurado.
- Nenhum dado de outro tenant ou outro projeto.

**O que não vê:**

- Dados internos de custo e modelo.
- Nodes `data_classification: confidential` ou `restricted`.
- Configurações de workspace ou org.
- Agent activity details (vê apenas resultados, não runs internos).

# 21. Client View

**Quem acessa:** cliente do projeto — não é usuário interno do CKOS; acessa via link compartilhado ou role `client`.

**O que vê:**

- Progresso do projeto em linguagem simples (Project Pulse simplificado).
- Decisões solicitadas ao cliente: approvals de artifact, aprovação de proposta, confirmação de escopo.
- Artifacts disponíveis para download / revisão.
- Próximos passos: o que o projeto precisa do cliente para avançar.
- Tickets de suporte abertos pelo próprio cliente.
- Feedbacks que o cliente enviou e seu status de processamento.

**O que não vê:**

- Custos internos, créditos, modelo usado.
- Nodes internos de diagnóstico, risco técnico, hipóteses internas.
- Detalhes de agentes e runs.
- Dados de outros clientes ou projetos.

**Renderização para cliente:** versão redigida de qualquer node com `data_classification: internal` ou superior. Conteúdo não-redissível (só para o role atual) é omitido, não exibido com [REDACTED].

# 22. Admin View

**Quem acessa:** admin da organização — tem visão privilegiada de runtime.

**O que vê (além da view padrão):**

- Custos detalhados: por agente, por modelo, por coletor, por workflow, por usuário.
- Agent runs: todas as execuções, incluindo as que falharam, com logs.
- Permissões: quem tem qual acesso neste projeto.
- Configurações: project_settings, capability grants, integrations.
- Support tickets: todos os tickets, incluindo internos.
- Audit trail: log de ações no projeto (doc 12 §7).
- Run replay: acessar `run_replay` de qualquer execução passada (doc 13 §14).
- Nodes de sistema: nodes do tipo `System` visíveis.

# 23. Founder / Internal CK View

**Quem acessa:** founder da organização e equipe interna da CK Company no contexto de projeto interno.

**O que vê (além do admin):**

- Decisões registradas no projeto: com evidências, conflitos e histórico de mudança.
- ROI executivo: todas as dimensões de ROI com confidence e gaps.
- Riscos críticos: com estimativa de impacto e recomendação de mitigação.
- Custos e créditos: breakdown completo com projeção.
- Approvals pendentes de nível founder.
- Visão comparativa: projeto no contexto de outros projetos da org (via CKOS Home, não via este dashboard).
- Metacognik audit history: todas as auditorias realizadas neste projeto.
- Learning loop status: hipóteses confirmadas, decisões aprendidas (doc 13 §21).

Para projetos internos CKOS: acesso adicional a decisões técnicas, sprints, issues, agentes de desenvolvimento, QA e custos de modelo de desenvolvimento.

# 24. Widget Personalization e Presets

## 24.1 O que o usuário pode fazer

| Ação | Permitida no MVP |
|---|---|
| Pin widget (fixar em posição) | ✅ |
| Hide widget (ocultar temporariamente) | ✅ — exceto `fixed_required` |
| Reorder widget | ✅ |
| Choose density (compact / default / expanded) | ✅ |
| Choose preset | ✅ |
| Save layout | ✅ |
| Restore recommended layout | ✅ |

## 24.2 O que não é permitido

- Remover widgets `fixed_required` (risk, custo, approval) — segurança operacional.
- Criar widgets arbitrários sem `node_type` correspondente.
- Burlar permissões via customização de layout.
- Ver dados cross-tenant por configuração de widget.
- Ocultar alertas críticos de risco ou Metacognik.

## 24.3 Presets disponíveis

| Preset | Foco | Widgets em destaque |
|---|---|---|
| **Executive View** | Decisão rápida, estado geral | Project Pulse, What Needs Decision, ROI Snapshot, Risk Monitor |
| **Creative View** | Artefatos, ideação, marca | Artifacts Generated, Feedback Loop, Node Health (creative nodes), AI Activity |
| **Operations View** | Execução, workflows, agentes | AI Activity, Node Health, Support & Friction, Cost & Credits |
| **Financial View** | Custo, ROI, créditos | ROI Snapshot, Cost & Credits, Risk Monitor (cost risks) |
| **Client View** | Progresso, aprovações, entregáveis | Project Pulse (simplificado), What Needs Decision, Artifacts Generated |
| **Founder View** | Decisão estratégica, riscos, custo | What Needs Decision, ROI Snapshot, Risk Monitor, Cost & Credits |
| **Support View** | Fricções, tickets, bloqueios | Support & Friction, Feedback Loop, Node Health (blocked nodes) |
| **AI Activity View** | Tudo sobre agentes e runs | AI Activity, Node Health, Cost & Credits (por agente) |

Presets são ponto de partida — usuário pode customizar sobre qualquer preset. Preset `recommended` é gerado dinamicamente pelo sistema baseado no estado do Runtime.

# 25. CommandBar no Project Dashboard

O CommandBar aparece dentro do Project Dashboard como o ponto de entrada de intenção no contexto do projeto. **Não executa diretamente** — captura intenção e passa ao Command Center.

## 25.1 Fluxo

```txt
Usuário digita no CommandBar
  → IntentSubmitted (com project_id e context_snapshot)
  → intent_router (doc 15 §5.2)
  → context_pack_builder (com nodes, events, state do projeto)
  → policy_engine → model_router → agent_router / workflow_engine
  → event_bus → state update
  → ui_projection_engine
  → Dashboard refresh (widget correspondente atualiza)
```

## 25.2 Comandos contextuais por projeto

O CommandBar sugere intenções baseadas no estado atual do projeto — não lista genérica. `command_center_suggestions` alimenta as sugestões.

**Exemplos de intenções suportadas:**

```txt
Criar briefing inteligente
Analisar concorrentes
Gerar diagnóstico estratégico
Criar proposta executiva
Criar node de campanha
Revisar evidências ativas
Mostrar riscos ativos do projeto
Explicar por que este node está travado
Estimar ROI do projeto
Simular custo antes de executar
Revisar feedbacks recebidos
Abrir ticket de suporte
Aprovar workflow pendente
Pausar execução por risco
Comparar hipóteses ativas
Pedir auditoria do Metacognik
Gerar artifact para cliente
Ver consumo de créditos deste projeto
Solicitar coleta externa
Criar plano de ação dos próximos 7 dias
Mostrar decisões sem evidência suficiente
Analisar agente com maior custo
Gerar resumo de progresso para o cliente
Listar nodes sem owner definido
```

## 25.3 Restrições do CommandBar

- Comandos genéricos demais (ex: "fazer tudo") são parseados para intenção mais específica por Nick.
- Comandos que exigem permissão maior do que o role atual são bloqueados por `policy_engine`.
- CommandBar nunca chama agente ou workflow diretamente — sempre via `intent_router`.
- CommandBar no Dashboard tem contexto de projeto — diferente do CommandBar global na CKOS Home.

# 26. Permissões, RBAC e ABAC

## 26.1 RBAC no Dashboard

| Role | O que vê e faz no Dashboard |
|---|---|
| `viewer` | Leitura de widgets não-confidenciais. Sem ações. Sem custo, sem billing. |
| `contributor` | Viewer + cria nodes simples via intent. Vê Feedback Loop e Support & Friction. |
| `project_member` | Contributor + vê Node Health completo, AI Activity, Artifacts. Submete approvals simples. |
| `lead` | Project_member + vê Cost & Credits, ROI Snapshot. Aprova workflows e artifacts. Acessa presets avançados. |
| `admin` | Lead + run details, audit trail, permissões, configurações, run replay. |
| `founder` | Admin + decisões estratégicas, ROI executivo, Metacognik audit history, learning loop. |
| `client` | Client View isolado (§21) — sem dados internos. |
| `stakeholder` | Stakeholder View isolado (§20) — escopo limitado. |

## 26.2 ABAC

- `data_classification` do node/artifact determina visibilidade: `public | internal | confidential | restricted`.
- `tenant_id`: RLS garante isolamento. Dashboard nunca mistura projetos de tenants diferentes.
- `approval_status = pending_approval`: visível apenas para o approver designado e para `lead+`.
- `cost_estimate`: visível apenas para `lead+`.

## 26.3 Comportamento sem permissão

- Widget existe mas dados são redacted: exibir título do widget com "Acesso restrito — solicite ao admin".
- Widget inteiro não disponível para o role: ocultar completamente, sem indicação de existência (ex: Cost & Credits para `viewer`).
- Ação não disponível: desabilitar visualmente o botão; não exibir erro de permissão inline para não revelar informação.
- Todo acesso bloqueado gera entrada no `audit_log` (doc 12 §7).

# 27. State Machines Visíveis no Dashboard

O Dashboard exibe estados de 3 máquinas (sem controlar transições — apenas renderiza):

## 27.1 Estado do projeto (derivado do Runtime)

```txt
empty_state       projeto criado mas sem briefing ou nodes
briefing_live     briefing ativo, projeto em fase de contexto
diagnosis_active  Cognik ou usuário rodando diagnóstico
proposal_building workflow de proposta em execução
approval_pending  approval gate ativo — bloqueia avanço
operation_active  workflows e agentes em execução
learning_loop     projeto em fase de aprendizado — hipóteses sendo testadas
```

Estado derivado da combinação de node_status_projection + agent_activity_projection + approval_projection. Nunca setado manualmente.

## 27.2 State machine de Workflow (doc 16 §9.2)

Visível nos widgets AI Activity e Node Health para workflows associados ao projeto. Dashboard exibe estado atual sem expor transições internas.

## 27.3 State machine de Approval (doc 16 §9.3)

Visível no widget What Needs Decision. Badge de `expired` e `escalated` exibidos com destaque visual distinto.

# 28. Eventos Emitidos pelo Dashboard

O Dashboard emite intenções — não escreve estado. Todos os eventos abaixo passam pelo Runtime.

| # | Evento de intenção | Origem | Processado por |
|---|---|---|---|
| 1 | `DashboardIntentSubmitted` | CommandBar input | `intent_router (15 §5.2)` |
| 2 | `ApprovalSubmittedFromDashboard` | Approve/reject inline em widget | `approval_gate → Runtime` |
| 3 | `WidgetPinned` | Usuário pina widget | `dashboard_preferences (local state)` |
| 4 | `WidgetHidden` | Usuário oculta widget | `dashboard_preferences (local state)` |
| 5 | `LayoutSaved` | Usuário salva layout | `dashboard_preferences → Runtime` |
| 6 | `LayoutRestored` | Usuário restaura layout recommended | `dashboard_preferences → Runtime` |
| 7 | `PresetSelected` | Usuário seleciona preset | `dashboard_preferences → Runtime` |
| 8 | `NodeDrilldownOpened` | Usuário clica "Ver no Canvas" | `CanvasNavigationRequested → Node Canvas` |
| 9 | `RunReplayRequested` | Admin solicita run replay | `RunReplayStarted → eval_runner (13 §14)` |
| 10 | `DashboardExportRequested` | Usuário exporta estado do dashboard | `ArtifactCreateRequested → workflow → snapshot` |
| 11 | `FeedbackAcknowledgedFromDashboard` | Usuário processa feedback no widget | `FeedbackProcessed → Runtime` |
| 12 | `SupportTicketCreatedFromDashboard` | Usuário abre ticket no widget | `SupportRequested → Runtime` |

Eventos 3, 4 são estado local de UI — não criam eventos de domínio. Todos os demais geram eventos persistidos no event store (doc 11 §4).

# 29. MVP P0

## O que entra no MVP P0

- Project Pulse widget (com Project Pulse da `project_pulse_projection`)
- What Needs Decision widget (approval queue básico)
- AI Activity widget (agent_activity_projection)
- Node Health widget (node_status_projection — nodes blocked e pending_approval)
- Cost & Credits widget (summary por projeto — `cost_projection`)
- Risk & Gap Monitor widget (risk_projection)
- Artifacts Generated widget (artifact nodes)
- Recent Events feed (event bus — últimos N eventos do projeto)
- CommandBar contextual (CommandBar com project_id, sugestões básicas via `command_center_suggestions`)
- Basic widget presets: Executive View, Operations View
- RBAC MVP: viewer, contributor, project_member, lead, admin
- ui_projection based rendering (sem cálculo próprio)
- Tenant isolation via RLS
- Estado do projeto derivado (§27.1)
- Mobile read-only (Dashboard leitura em mobile; ações em desktop)

## O que fica fora do MVP P0

- Drag-and-drop avançado de widgets.
- Dashboard marketplace / widget store.
- Full billing management (aguarda Credits/Plans Architecture).
- Advanced ROI forecasting (aguarda ROI Architecture).
- Multi-project dashboard (é CKOS Home — doc separado).
- Fully custom widgets sem node_type.
- Real-time multiplayer editing de layout.
- Complex BI charts (séries temporais longas, forecasting).
- Self-evolving layout optimization (ML de preferências).
- Client View completo (MVP: view simplificada).
- Run replay no dashboard (MVP: apenas no admin/command center).
- Feedback Loop widget completo (aguarda Feedback System Architecture).
- Support & Friction widget completo (aguarda Support System Architecture).
- ROI Snapshot completo (aguarda ROI Architecture).
- Widget presets avançados (MVP: 2 presets).

# 30. Edge Cases

1. **Projeto sem nodes ativos:** Dashboard exibe `empty_state`. Project Pulse mostra "Projeto criado, sem atividade". CommandBar sugere "Criar briefing inteligente" como próxima ação. Widgets obrigatórios exibem estado neutro (§9.4).
2. **Projeto sem dados suficientes para widget:** Widget exibe estado neutro com mensagem contextual. Não bloqueia outros widgets. Não exibe dados fictícios.
3. **Projeto com ROI não financeiro:** ROI Snapshot exibe apenas os tipos de ROI com dados disponíveis (ex: `strategic_roi`, `learning_roi`). Campos `financial_roi` ficam em estado neutro se não houver dados.
4. **Usuário sem permissão para custo:** Cost & Credits e ROI Snapshot ficam completamente ocultos (não redacted — omitidos). Sem indicação de que existem para não vazar informação.
5. **Cliente tenta aprovar ação bloqueada por policy:** Dashboard exibe "Aprovação não disponível para este perfil" sem revelar os detalhes da policy. Audit log registra tentativa.
6. **Widget depende de collector indisponível:** Widget exibe dados da última projeção disponível com timestamp. Badge "Coletor indisponível" com link para suporte.
7. **Runtime atrasado (projection lag):** Dashboard exibe timestamp de última atualização em todos os widgets. Banner discreto: "Dados podem estar desatualizados — última sincronização: Xmin atrás". Não bloqueia leitura.
8. **Agent run falhou:** AI Activity widget exibe badge de erro. Motivo visível para `project_member+`. Ação disponível: "Ver detalhes do erro" → run log. Para `admin`: "Abrir run replay".
9. **Dados sensíveis precisam ser mascarados:** `data_classification: confidential` → conteúdo omitido, título visível se `project_member+`. `restricted` → omitido completamente para não-founder.
10. **Feedback contradiz decisão aprovada:** Feedback Loop widget exibe badge "Contradiz decisão [título]". Widget What Needs Decision sugere revisão da decision. Metacognik pode emitir warning automático.
11. **Custo excede orçamento:** Cost & Credits widget exibe alerta vermelho de topo. Workflows não-críticos pausados automaticamente por `cost_guard` (doc 13 §11). Dashboard exibe lista de execuções pausadas com ação de revisão.
12. **Dashboard projection stale:** Exibe timestamp com diferença > N minutos. Botão "Atualizar agora" força re-query das projeções. Não bloqueia leitura dos dados existentes.
13. **Usuário customizou layout e perdeu widget crítico:** Widgets `fixed_required` não podem ser removidos — apenas minimizados. Se minimizados, continuam emitindo alertas críticos como notificações mesmo minimizados.
14. **Projeto muda de tipo no meio do caminho:** Widgets `node_generated` se adaptam automaticamente quando nodes mudam. Widgets `user_pinned` permanecem até o usuário os remover manualmente. Dashboard não remove widget ativo sem confirmação.
15. **Node novo exige widget novo:** Se node_type não tem widget correspondente, o node aparece no Node Health widget genérico. Novo widget só é adicionado via sistema de widget_type definido (não ad-hoc).
16. **Tenant boundary precisa ser preservado:** RLS na camada de projeção bloqueia qualquer query cross-tenant antes de chegar ao Dashboard. Se bug de projeção trouxer dado de outro tenant, Dashboard verifica `tenant_id` antes de renderizar.
17. **Cliente vê apenas versão redigida:** Client View aplica redaction por `data_classification`. Conteúdo omitido (não "[REDACTED]") para não revelar estrutura interna.
18. **Admin precisa abrir run replay:** Dashboard emite `RunReplayRequested` → `eval_runner` (doc 13 §14) processa. Admin visualiza replay no Command Center ou em painel de auditoria dedicado (pós-MVP no dashboard em si).
19. **Suporte vira incidente:** Support & Friction widget detecta ticket com impacto `critical` e sem resolução por N horas. Emite `IncidentEscalated` → notificação para `admin` + `founder`. Dashboard exibe banner de incidente ativo.
20. **ROI fica com baixa confiança:** ROI Snapshot exibe badge laranja "Confiança baixa — N evidências insuficientes". Metacognik pode emitir warning. Dashboard sugere ação: "Coletar mais evidências" → intent → Research workflow.

# 31. Patches Sugeridos para Outros Docs

Os patches abaixo foram identificados durante a revisão do doc 14. Estão **registrados como sugestões** — não aplicados. Requerem decisão de PMO_CKOS antes de aplicar.

## Patches para doc 11 v1.2.x

| # | Tabela / seção | Origem | Urgência |
|---|---|---|---|
| P11-3 | `feedback_entries` — captura de feedback explícito e implícito | §16 (Feedback Loop widget) | Feedback Mode MVP |
| P11-4 | `support_tickets`, `ticket_events` — rastreamento de tickets | §17 (Support & Friction widget) | Support Mode MVP |
| P11-5 | `roi_projection` em §21 (ui_projections) | §14 (ROI Snapshot widget) | ROI Mode MVP |
| P11-7 | `dashboard_preferences` — estado de layout por usuário/projeto (widget_configs, preset_selected, pinned_widgets) | §24 (Widget personalization) | Dashboard MVP |
| P11-8 | Confirmar `project_activity_feed` ou view derivada do event_bus para "recent events" feed | §29 (MVP P0 — Recent Events feed) | MVP P0 |

> Notas: P11-3, P11-4 e P11-5 já estão registrados no `ARCHITECTURE_PATCH_REPORT.md §14.4`. P11-7 e P11-8 são novos — identificados durante esta revisão do doc 14.

## Patch sugerido para doc 10 v1.1.x

| # | Sugestão | Origem | Urgência |
|---|---|---|---|
| P10-1 | Confirmar que `ui_projection_engine` expõe endpoint SSE para `project_pulse_projection` e `agent_activity_projection` (streaming em tempo real para o Dashboard) | §7 (UI projection model), §12 (AI Activity widget) | MVP P0 |

> O doc 10 §5.9 menciona streaming mas não especifica quais projeções têm SSE disponível. O Dashboard depende de SSE para Project Pulse e AI Activity. Este patch confirma (ou adiciona) a especificação.

# 32. Visual Direction (sem implementação)

Esta seção registra a **direção visual** para o Project Dashboard. **Não implementa UI, não define CSS, não especifica framework.**

**Referência de layout:**

- Bento grid: widgets em grid modular com tamanhos variados por relevância.
- Glass widgets: widgets com glassmorphism — backdrop blur, bordas sutis, sombra de profundidade.
- Cards ultra arredondados: border-radius generoso para linguagem visual contemporânea.
- CommandBar central ou bottom: flutuante, sempre acessível, destaque visual sem dominar.
- Fundo: preto ou dark glass como base. Conteúdo tem luminosidade própria por estado.
- Status vivos de agentes: badges animados sutis — working, blocked, completed.
- Alertas discretos: não invasivos; aparecem no contexto, não sobrepõem o conteúdo.
- ROI e custo sempre visíveis: widgets de custo e ROI têm posição privilegiada no grid para `lead+`.
- Layout adaptativo: bento grid re-arranja por número de widgets ativos e preset selecionado.

**Inspiração de experiência:**

- macOS: densidade informacional, foco na tarefa, sem ruído visual.
- Apple Vision Pro: camadas de profundidade, conteúdo flutuante, foco contextual.
- Cockpit cognitivo: informação hierarquizada por urgência, não por beleza.

**Identidade visual:**

- Dashboard é whitelabel. Skin vem do `design_system` ativo (branddock) do projeto ou org.
- Fallback: CK dark / glass (identidade padrão da plataforma).
- Dashboard não tem identidade visual própria fixada — tokens parametrizados por tenant.

# 33. Related Notes

- [[10_SYSTEM_RUNTIME_ARCHITECTURE]]
- [[11_DATA_MODEL_AND_PERSISTENCE]]
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]]
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]]
- [[15_COMMAND_CENTER_ARCHITECTURE]]
- [[16_NODE_CANVAS_ARCHITECTURE]]
- [[02_AI_FIRST_OBJECT_MODEL]]
- [[ARCHITECTURE_PATCH_REPORT]]
- [[QA_DOCUMENTATION_CHECKLIST]]
