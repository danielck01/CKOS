---
title: "Widget State Matrix and Execution Feedback"
file: "03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md"
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
purpose: "Definir a matriz de estados visuais dos widgets e componentes com base nas referências de design do Canvas OS."
inputs:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md"
  - "000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md"
outputs:
  - "03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md"
framework: "Sentir -> Pensar -> Criar -> Conectar -> Avaliar -> Elevar"
edge_cases:
  - "Flickering visual quando o estado muda rapidamente"
  - "Indicação de erro sem fornecer alternativa imediata de correção (botão Fix)"
integrations:
  - "antigravity_design_study"
prompts:
  - "Mapear estados de widgets baseando-se em eventos de execução reais."
metrics:
  - "Zero de código implementado"
  - "Matriz detalhada com 11 estados de IA com correspondentes visuais exatos"
related_notes:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md"
tags:
  - "state_matrix"
  - "feedback"
  - "execution"
  - "design_study"
---

# Widget State Matrix and Execution Feedback

Esta nota de estudo documenta como os widgets e componentes visuais do CKOS devem alterar seus estados estéticos para representar de forma transparente o ciclo de vida de processamento de tarefas executadas por agentes autônomos.

---

## 1. Alinhamento de State Machines do Runtime e Projeções Visuais

Os estados visuais dos widgets do CKOS projetam de forma síncrona as transições de estado oficiais controladas pelo runtime (conforme definido no doc 16 §9). Nenhuma transição visual é gerada de forma ad-hoc na UI. A interface mapeia cada estado canônico a aliases visuais, comportamentos ergonômicos e pistas estéticas:

### A. Máquina de Estados de Node (Runtime doc 16 §9.1)

Esta tabela mapeia o ciclo de vida atômico de um nó de informação ou execução no Node Canvas e nos painéis laterais:

| Estado do Runtime | Categoria / Natureza | Alias / Percepção Visual (Sentir) | Comportamento do Widget (Criar / Conectar) | Pista Visual & Estilo (Pensar / Avaliar) |
| :--- | :--- | :--- | :--- | :--- |
| `suggested` | Inicial (IA) | *Suggested AI Node* | Widget flutua com opacidade de 70% e contorno pontilhado. Exibe botões "Accept" e "Dismiss". | Contorno pontilhado roxo/azul sutil. Backlight traseiro difuso e sem brilho metálico de borda. |
| `draft` | Inicial (Usuário) | *Draft / Uncommitted* | Permite edição textual e atalhos manuais de conexão de dependências. | Fundo em vidro escuro fosco (`rgba(255,255,255,0.05)`) com contorno cinza estável. Sem backlight. |
| `pending_approval` | Gate de Controle | *Awaiting Gate Approval* | Widget é projetado à frente (Z-index elevado). Ações de alteração de conteúdo são bloqueadas. | Borda externa pulsa suavemente em tom amarelo-ouro. Backdrop blur do fundo é adensado para 30px. |
| `active` | Operacional Neutro | *Active / Operational* | Pronto para ser consumido em workflows ou lido por subagentes. | Contorno cinza sólido fino. Estética Calm Glass limpa com legibilidade máxima. |
| `running` | Execução Ativa | *Processing Runtime* | Exibe logs atômicos rápidos em fonte mono-espaçada de alta legibilidade. | Anel do avatar do agente gira em loop azul contínuo. Gráficos de barra de eficiência movem-se dinamicamente. |
| `waiting_input` | Bloqueio Recuperável | *User Input Requested* | Abre um campo de input textual no rodapé do cartão para interação direta. | Um backlight azul estável acende atrás do widget para atrair a atenção seletiva. |
| `waiting_approval` | Bloqueio / Gate | *Paused for Approval* | Congela a execução interna e exibe link imediato para o Approval Gate ativo. | Borda amarela contínua e Z-index ligeiramente elevado. |
| `completed` | Sucesso / Histórico | *Execution Succeeded* | Reduz sua opacidade para 60% e apaga backlights para retirar o foco cognitivo. | Uma piscada rápida em verde-esmeralda (150ms) nas bordas antes de assentar em cinza neutro. Ícone de check sutil no topo. |
| `archived` | Histórico Passivo | *Archived Node* | Ocultado por padrão no Node Canvas. Apenas pesquisável via logs de auditoria históricos. | Cinza escuro fosco e sem relevos visuais. |
| `blocked` | Bloqueio Estrito | *Blocked / Intercepted* | Desabilita todas as edições. Exibe log de erro condensado e botão destacado "Explain/Mitigate". | Contorno vermelho pulsante lento. Backlight vermelho difuso. |

### B. Máquina de Estados de Workflow (Runtime doc 16 §9.2)

Mapeia a progressão lógica e temporal de múltiplos agentes e tarefas agrupados em pipelines de entrega:

| Estado do Runtime | Categoria / Natureza | Alias Visual | Comportamento do Widget | Pista Visual & Estilo |
| :--- | :--- | :--- | :--- | :--- |
| `created` | Inicialização | *Workflow Initialized* | Widget surge cinza neutro. | Sem animação. |
| `planned` | Planejamento | *Plan Formulated* | Renderiza o checklist ordenado de tarefas pendentes em chips cinzas translúcidos. | Contorno cinza médio. |
| `queued` | Fila de Runtime | *Queued for Dispatch* | Apresenta spinner discreto de carregamento de recursos. | Três pontinhos cinzas piscando ciclicamente no centro. |
| `running` | Execução | *Active Execution* | A barra de progresso horizontal preenche-se suavemente. | Gradiente azul-verde correndo pela barra de preenchimento. |
| `waiting_agent` | Estado Derivado | *Waiting for Agent Slot* | Pausa temporária por fila de concorrência ou limite de rate. | Badge "Waiting for Agent..." em cinza claro piscante. |
| `waiting_tool` | Estado Derivado | *Executing Tool/Collector* | Rastreia a chamada externa ativa (ex: ChEMBL API, n8n crawl). | Ícone da tool ativa brilha em azul na base. |
| `waiting_approval` | Estado Composto | *Human Gate Paused* | Bloqueia a fila temporal até que o portão humano decida. | Timeline do workflow interrompida com um nó amarelo piscante. |
| `completed` | Sucesso | *Workflow Success* | Conclusão bem-sucedida de todas as tarefas da timeline. | O widget brilha em verde-esmeralda por 200ms e depois assenta. |
| `failed` | Falha | *Workflow Failure* | Interrompe o workflow na tarefa exata do erro. Exibe logs e botão de Rollback. | Brilho vermelho sólido na borda da tarefa que falhou. |
| `cancelled` | Cancelado | *Workflow Aborted* | Desativa todas as ações. Risca os títulos das tarefas restantes. | Opacidade cai para 40% com tonalidade acinzentada. |
| `rolled_back` | Reversão / Histórico | *Workflow Reverted* | Exibe logs da transação de desfazer e restaura a filetree anterior. | Badge "Reverted" e bordas cinza-chumbo sólidas. |

### C. Máquina de Estados de Approval (Runtime doc 16 §9.3)

Mapeia o ciclo de vida dos portões decisórios do sistema, críticos para garantir a soberania humana sobre as automações de IA:

| Estado do Runtime | Categoria / Natureza | Alias Visual | Comportamento do Widget | Pista Visual & Estilo |
| :--- | :--- | :--- | :--- | :--- |
| `requested` | Pendência Humana | *Decision Required* | Flutua no topo de todas as camadas. Apresenta botões "Approve" e "Reject". | Borda pulsa em dourado. Avatar do stakeholder com indicador circular brilhante. |
| `approved` | Sucesso de Gate | *Authorized* | Dispara imediatamente o workflow correspondente e fecha a folha/modal. | Transição rápida em verde-esmeralda (200ms) com animação de expansão. |
| `rejected` | Negativa de Gate | *Denied* | Bloqueia a execução, abre formulário obrigatório de feedback para a IA e redefine o node para `draft`. | Brilha em vermelho sólido por 250ms antes de recolher. |
| `expired` | Expirado | *Stale / Expired* | Desabilita todos os botões por estouro de timeout de segurança. | Texto muda para cinza com rótulo "Expired (Timeout)". |
| `revoked` | Cancelamento | *Withdrawn* | Recolhe o portão sem alteração de estado no domínio histórico. | O widget é colapsado suavemente na barra lateral. |
| `escalated` | Alerta de Risco | *Escalated Priority* | Notifica o próximo stakeholder hierárquico na policy por falta de resposta. | Borda pisca duas vezes em vermelho-alaranjado rápido. |

---

## 2. Padrões de Feedback de Execução e Custos (Avaliar)

Para evitar surpresas financeiras e fadiga de espera do usuário, os estados dos widgets incorporam regras de orçamento e tempo:

```
+-------------------------------------------------------+
|  CAPABILITY EXECUTION CARD                            |
|  Agent: Claude 3.5 Sonnet                             |
|                                                       |
|  [|||||||||||||||||||..........] 65% Completed        |
|  Task: Writing database schemas...                    |
|                                                       |
|  Est. Cost: $0.15 CKC   |   Time Elapsed: 12.4s       |
|  Risk: Low              |   Tokens/sec: 140k          |
|                                                       |
|  [ Pause Agent ]                    [ View Code ]     |
+-------------------------------------------------------+
```

1. **Estimador de Overhead de Tokens (Cost Guard)**:
   * Durante o estado `Running`, o widget exibe em tempo real o custo acumulado em tokens/dólares do agente associado.
   * Se o custo ultrapassar o limite pré-aprovado no planejamento, o widget altera dinamicamente seu estado de `Running` para `Awaiting Approval` com o status `Budget Exceeded`, pausando a execução do agente no backend antes que ocorra prejuízo financeiro.
2. **Medidor de Eficiência (Performance Matrix)**:
   * Gráficos em colunas verticais curtas representam a taxa de acertos e o consumo de memória dos agentes em execuções passadas (comportamento "Efficiency" do *Samurai Canvas*).
   * Se o widget indicar baixa eficiência histórica em um agente específico para aquela tarefa, a interface sugere visualmente a substituição do agente executor antes de iniciar o plano.
3. **Mecanismo de Desvanecimento e Foco Dinâmico (Neurodesign)**:
   * Somente o widget no estado `Running` ou `Awaiting Approval` deve emitir luminosidade ativa. Widgets em estado `Completed` ou `Idle` reduzem sua opacidade para `60%` e extinguem seus backlights, permitindo que a atenção seletiva do usuário repouse estritamente no processo ativo.
