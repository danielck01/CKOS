---
title: "Operational UI/UX Grammar for CKOS"
file: "02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md"
phase: 000_STUDY_NOTES
category: study_note
status: draft
version: 1.0.0
owner: pmo_ckos
responsible_agent: antigravity_design_study
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - founder
confidence: unverified
provenance_status: unverified
source_tool: antigravity
purpose: "Mapear a gramática visual extraída das referências para as superfícies e fluxos operacionais de runtime do CKOS."
inputs:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md"
  - "04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md"
  - "04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md"
  - "04_PRODUCT_SYSTEM/16_NODE_CANVAS_ARCHITECTURE.md"
outputs:
  - "02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md"
framework: "Sentir -> Pensar -> Criar -> Conectar -> Avaliar -> Elevar"
edge_cases:
  - "Desenho de cartões sem conexão clara com o estado do banco de dados ou do runtime"
  - "Poluição visual gerada por grafos sem agrupamento lógico contextual"
integrations:
  - "antigravity_design_study"
prompts:
  - "Mapear superfícies de visualização do CKOS com base em padrões de design operacionais."
metrics:
  - "Zero de código implementado"
  - "11/11 perguntas estratégicas respondidas através de elementos visuais precisos"
related_notes:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md"
tags:
  - "grammar"
  - "runtime_ui"
  - "components"
  - "design_study"
---

# Operational UI/UX Grammar for CKOS

Esta nota de estudo estabelece como os componentes de interface do CKOS devem projetar visualmente o estado operacional ativo do sistema operacional de agentes, convertendo elementos estéticos em gramáticas funcionais de runtime.

---

## 1. As 11 Perguntas Estratégicas e Suas Projeções Visuais

A interface do CKOS não deve ser um dashboard decorativo passivo. Ela deve responder de forma síncrona e visual a 11 perguntas fundamentais:

```
+-----------------------------------------------------------------------------+
|                                COMMAND CENTER                               |
| 1. Intent: [ "Criar landing page de vendas..." ]                            |
| 2. Understanding: (AI Parsing: Marketing Jurídico, Regulação OAB, Copywriting) |
+-----------------------------------------------------------------------------+
|    EXECUTION PLAN WIDGET    |                    NODE CANVAS                |
| 3. Context: [Files Loaded]  | 8. Running:                                   |
| 4. Capabilities: [n8n, git] |    - Codex Agent [Writing page.tsx...]        |
| 5. Cost: $0.45 CKC          |    - QA Agent [Testing routes...]             |
| 6. Risks: High (OAB rule 4) |    - Connected by smooth bezier curves        |
| 7. Approvals: Awaiting CEO  |                                               |
+-----------------------------+-----------------------------------------------+
|    EVIDENCE MAP             |               ROI & LEARNINGS                 |
| 9. Evidence: [OAB Code v2]  | 10. Artifacts: [src/App/page.tsx]             |
|                             | 11. ROI: +82% Confidence \| Memory registered  |
+-----------------------------------------------------------------------------+
```

### 1. O que o usuário quer? (Intent)
* **Solução de Design**: O *Command Center* principal atua como a superfície de entrada. O input de texto do usuário apresenta um campo com tipografia geométrica proeminente e cantos arredondados, que se ilumina com um backlight pulsante assim que o usuário inicia a digitação.

### 2. O que o sistema entendeu? (Understanding)
* **Solução de Design**: Abaixo da commandbar, são renderizados chips translúcidos contextuais e dinâmicos de classificação semântica (ex: `Tipo: Código`, `Domínio: Financeiro`, `Nível de Risco: Médio`). O sistema traduz a intenção bruta em tokens de escopo visual antes de montar o plano de ação.

### 3. Qual contexto será lido? (Context Pack)
* **Solução de Design**: Exibição de uma gaveta flutuante ou "shelf" de documentos acoplada à commandbar contendo cartões arredondados e minimalistas que representam os arquivos, fontes e memórias históricas que serão injetados na sessão do agente (ex: mini-cards de `.pdf`, `.tsx` ou links externos).

### 4. Quais capabilities serão ativadas? (Capabilities)
* **Solução de Design**: Chips de ferramentas na base do cartão de tarefas exibem ícones lineares discretos (como Git, UV, ChEMBL, n8n) acendendo-se em azul operacional para demonstrar quais APIs e subsistemas de execução estão mapeados para aquela tarefa específica.

### 5. Quanto pode custar? (Cost Guard)
* **Solução de Design**: No canto superior direito do widget de execução ou da commandbar, um contador de créditos minimalista exibe a estimativa em dólares CKC (ex: `$0.12 CKC / 1.5M tokens`). Se a estimativa exceder o teto estipulado pela policy, a cor do texto muda de branco suave para laranja ou vermelho, bloqueando a ação física.

### 6. Que riscos existem? (Risk Matrix)
* **Solução de Design**: Um indicador de risco compacto composto por uma barra de gradiente colorido (verde-amarelo-vermelho) ou por um círculo concêntrico no topo da commandbar. Ao expandir, exibe chips de alerta textuais (ex: `Risco Reputacional`, `Mudança Irreversível de Arquivo`).

### 7. Quem precisa aprovar? (Approval Gates)
* **Solução de Design**: Um cartão de aprovação (*Approval Gate Card*) destacado, que flutua no Z-index mais elevado, contendo o avatar tridimensional do stakeholder responsável ou a indicação de nível hierárquico exigido (ex: `Aprovação de Founder pendente`). Os botões de decisão possuem luzes de status internas brilhantes.

### 8. O que está rodando agora? (Active Runtime)
* **Solução de Design**: O *Node Canvas* espacial e o *Agent Activity Stream* mostram os avatares dos agentes piscando suavemente no centro do canvas, com conectores curvilíneos curvos ativos pulsando dados (micro-linhas brilhantes correndo pelo conector) até os cartões dos arquivos que estão sendo modificados em tempo real.

### 9. Qual evidência sustenta a saída? (Evidence Map)
* **Solução de Design**: O *Evidence Map* funciona como uma malha conectiva espacial (*Spatial Canvas*) onde o usuário pode clicar em qualquer saída produzida pela IA e rastrear, através de caminhos de conexão física, as fontes exatas, notas de estudo e decisões passadas que influenciaram o resultado.

### 10. Qual artefato foi produzido? (Artifacts)
* **Solução de Design**: Cartões de arquivo de saída renderizados na tela com representações visuais ricas de seu conteúdo (trechos de código formatados com syntax highlighting dentro do próprio widget, ou miniaturas visuais de alta definição no caso de imagens e designs).

### 11. Qual ROI ou aprendizado foi gerado? (ROI & Learning)
* **Solução de Design**: Widgets circulares concêntricos que exibem a porcentagem de melhoria de eficiência operacional (ex: `ROI: +40%`) e cartões editoriais elegantes com fontes serifadas e fundo de vidro fosco suave, simbolizando a cristalização do aprendizado que foi gravado permanentemente no repositório de decisões de runtime (mapeado em `roi_evidence_links` e no repositório de memórias validadas, a ser especificado como projeção canônica futura. Antes de qualquer uso em UI, essa projeção precisa ser formalizada como patch candidate no [23_UIUX_CANONICAL_PATCH_CANDIDATES.md](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/000_STUDY_NOTES/10_UIUX_STUDIES/23_UIUX_CANONICAL_PATCH_CANDIDATES.md)).

---

## 2. Anatomia das Superfícies Visuais e Mapeamento de Fontes Operacionais

A interface do CKOS projeta dados operacionais síncronos a partir de fontes de verdade bem delineadas no runtime. Abaixo está o mapeamento detalhado de cada superfície visual chave para as suas fontes operacionais subjacentes:

### A. Command Center (Editorial + Command Surface)
* **Descrição Física**: Caixa flutuante centralizada com desfoque de fundo de 25px (`Calm Glass`), contorno reflexivo sutil e chips suspensos dinâmicos de intenção.
* **Mapeamento de Fontes de Dados**:
  * **Event Bus / Runtime Event**: Emite eventos `IntentSubmitted` e escuta `CommandCenterSuggestionsUpdated` para auto-complete dinâmico.
  * **Projection / Read Model**: Lê de `command_center_suggestions` (sugestões de comandos baseadas no contexto e histórico de navegação).
  * **Approval State**: Não possui estados de aprovação diretos no input, mas a indicação visual de bloqueio preventivo acende se o usuário tentar um comando proibido por políticas do `policy_engine`.
  * **Cost / Credit Source**: Exibe em formato de pílula flutuante o custo máximo estimado da intenção baseando-se no modelo semântico parseado (estimativa preliminar via LLM parser do runtime).
  * **Evidence Source**: Apresenta chips indicando a confiabilidade das memórias históricas ou briefings recuperados para subsidiar a intenção ativa.

### B. Project Dashboard Projection (Data-Dense Minimal)
* **Descrição Física**: Painel estruturado exposto em colunas limpas de tarefas (pipelines), timelines verticais com nós luminosos de status e resumos de saúde geral do projeto. O antigo conceito de "Project Pulse" foi descontinuado e substituído pela projeção do dashboard de modo a não se tornar um componente de código rígido.
* **Mapeamento de Fontes de Dados**:
  * **Event Bus / Runtime Event**: Escuta eventos `WorkflowCreated`, `WorkflowCompleted`, `WorkflowFailed` e `DecisionRegistered`.
  * **Projection / Read Model**: Consome `project_dashboard_projection` (read model agregado contendo o resumo consolidado de saúde dos processos, prazos e prioridades).
  * **Approval State**: Renderiza contadores de portões de aprovação ativos pendentes na raiz do projeto (dados agregados de `approval_projection`).
  * **Cost / Credit Source**: Consome dados agregados da `cost_projection` para exibir o orçamento geral consumido versus o budget máximo configurado para o projeto.
  * **Evidence Source**: Exibe o badge de nível de risco acumulado (`risk_level`) e o indicador de confiança epistemológica global da entrega.

### C. Execution Plan Widget (Editorial + Data-Dense)
* **Descrição Física**: Painel de progresso atômico integrado ao editor de código ou logs da sessão, apresentando barras de gradiente suave e linhas mono-espaçadas de feedback atômico.
* **Mapeamento de Fontes de Dados**:
  * **Event Bus / Runtime Event**: Escuta eventos `WorkflowStarted`, `AgentRunStarted`, `AgentRunCompleted` e `WorkflowFailed`.
  * **Projection / Read Model**: Consome `agent_activity_projection` para rastrear exatamente qual subagente está fazendo qual alteração atômica em qual arquivo.
  * **Approval State**: Bloqueia fisicamente a progressão e brilha em dourado se o estado da máquina de estados do node transitar para `waiting_approval` (necessidade de acionamento do portão humano).
  * **Cost / Credit Source**: Exibe o contador real de tokens consumidos versus estimados da execução em andamento (derivado do campo `cost_estimate` jsonb do nó de Workflow).
  * **Evidence Source**: Links diretos para os arquivos que serviram de briefing de entrada, permitindo ao usuário abrir em tela dividida o documento em que a IA se baseou para a execução.

### D. Node Canvas (Spatial Canvas Interface)
* **Descrição Física**: Fundo infinito pontilhado contendo avatares de agentes dinâmicos envoltos por anéis de progresso coloridos e conectados a arquivos ou outros nós por curvas Bézier cobre e azul.
* **Mapeamento de Fontes de Dados**:
  * **Event Bus / Runtime Event**: Escuta `NodeCreated`, `NodeUpdated`, `NodeArchived`, `EdgeCreated` e `EdgeInvalidated`. Emite intenções via `NodeActionTriggered`.
  * **Projection / Read Model**: Consome diretamente `node_status_projection` e `agent_activity_projection`.
  * **Approval State**: Nodes em estado `pending_approval` exibem um anel dourado sutil e um atalho imediato para o formulário de aprovação.
  * **Cost / Credit Source**: Cada nó do tipo "Workflow" ou "Agent" no canvas renderiza um micro-badge de custo atualizado dinamicamente via `cost_projection`.
  * **Evidence Source**: Exibe em tempo real o indicador de `confidence_score` (0 a 1) avaliado pelos Evals (doc 13) e conexões gráficas do tipo `evidence_for`.

### E. Evidence Map (Epistemic Auditor Panel)
* **Descrição Física**: Janela lateral expansível ou visualizador de conexões que expõe as fontes documentais, confidence scores e contradições epistemológicas.
* **Mapeamento de Fontes de Dados**:
  * **Event Bus / Runtime Event**: Escuta `EvidenceAdded`, `EvidenceLinked` e `EvidenceContradicted` para atualizar as âncoras causais.
  * **Projection / Read Model**: Consome `risk_projection` e `node_status_projection` filtrados por dependências causais.
  * **Approval State**: Se a evidência exige validação formal ou assinatura de co-auditoria, exibe o status de aprovação correspondente da `approval_projection`.
  * **Cost / Credit Source**: Consome os dados de custos das execuções de coleta externa (ex: crawler ou APIs do PubMed/ChEMBL via collector run).
  * **Evidence Source**: A tabela `evidence_links` do schema do nó é a fonte primária de metadados, trazendo a rastreabilidade direta do lineage de dados validada pelo subagente Datta.

### F. ROI & Learning Panel (Editorial Insights)
* **Descrição Física**: Cartões modulares minimalistas com tipografia serifada de alta qualidade, fundos de vidro fosco denso e widgets concêntricos.
* **Mapeamento de Fontes de Dados**:
  * **Event Bus / Runtime Event**: Escuta `DecisionRegistered`, `ROIRealized` e `FeedbackSubmitted`.
  * **Projection / Read Model**: Lê de `project_dashboard_projection` (seção de ROI histórico), `roi_snapshot_projection`, `roi_evidence_links` e repositório de memórias validadas, a ser especificado como projeção canônica futura. Antes de qualquer uso em UI, essa projeção precisa ser formalizada como patch candidate no [23_UIUX_CANONICAL_PATCH_CANDIDATES.md](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/000_STUDY_NOTES/10_UIUX_STUDIES/23_UIUX_CANONICAL_PATCH_CANDIDATES.md).
  * **Approval State**: Decisões e ROIs validados que foram aprovados pelo Founder (dados de `approval_projection` consolidados).
  * **Cost / Credit Source**: Faz o cruzamento analítico entre créditos gastos acumulados no projeto versus valor financeiro gerado (estimativa de ROI calculada pelo Cognik).
  * **Evidence Source**: Mostra links para os artefatos finais e logs de auditoria que validaram o ROI alegado.
