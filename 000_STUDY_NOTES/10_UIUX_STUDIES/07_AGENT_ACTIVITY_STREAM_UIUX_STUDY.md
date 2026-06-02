---
title: "Agent Activity Stream UI/UX Study"
file: "07_AGENT_ACTIVITY_STREAM_UIUX_STUDY.md"
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
purpose: "Especificar os padrões de design UI/UX para o Agent Activity Stream do CKOS, garantindo legibilidade e diferenciação operacional."
inputs:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md"
outputs:
  - "07_AGENT_ACTIVITY_STREAM_UIUX_STUDY.md"
framework: "Sentir -> Pensar -> Criar -> Conectar -> Avaliar -> Elevar"
edge_cases:
  - "Conversão do stream em um chat log genérico poluído sem agrupamento lógico"
  - "Excessiva verbosidade de logs ocultando interrupções ou erros críticos"
integrations:
  - "antigravity_design_study"
prompts:
  - "Projetar a timeline de atividades de agentes inteligentes do CKOS."
metrics:
  - "Zero de código implementado"
  - "100% de alinhamento com os estados de execução e limites de visualização de agentes"
related_notes:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md"
tags:
  - "agent_stream"
  - "activity_stream"
  - "timeline"
  - "design_study"
---

# Agent Activity Stream: UI/UX Study

Este estudo especifica o design da superfície de linha temporal de processamento dos agentes no CKOS, garantindo rastreabilidade epistemológica e eliminando layouts de conversação genéricos.

---

## 1. O que é o Agent Activity Stream?

O **Agent Activity Stream** é a linha do tempo (timeline) cronológica e semântica de eventos de processamento e decisões tomadas pelos agentes em segundo plano. Ela expõe visualmente a história de execução de uma intenção do usuário, traduzindo eventos assíncronos do runtime em blocos de progresso ordenados.

O objetivo do Stream é permitir que o usuário audite, de forma linear e confortável, quem (agente/ferramenta) fez o quê, quando, baseado em qual evidência de entrada, com qual custo financeiro e gerando qual impacto ou artefato de saída.

---

## 2. Diferenciação das Superfícies de Interface

Para evitar confusão cognitiva e sobreposição funcional na área de trabalho do CKOS, a tabela abaixo delimita a responsabilidade de design de cada superfície:

| Superfície Visual | Foco Principal | Dimensão Espacial | Comportamento UI/UX |
| :--- | :--- | :--- | :--- |
| **Agent Activity Stream** | Temporal e de Lineage | 1D (Vertical Linear) | Timeline cronológica estruturada contendo o histórico de passos dos agentes. |
| **Node Canvas** | Estrutural e Topológico | 2D (Canvas Infinito) | Grafo espacial de nós e conexões dinâmicas de arquivos e subagentes. |
| **Project Dashboard** | Gerencial e ROI Macro | Modular (Cards/Grids) | Pipelines de entrega, controle orçamentário geral e portões pendentes. |
| **Execution Plan Widget** | Execução Real-Time | Compacto (Dock/Overlay) | Feedback rápido de progresso de logs imediatos da tarefa rodando agora. |

---

## 3. Estados do Stream e Transições Visuais

O Stream reflete síncronamente os eventos emitidos pelo Event Bus de runtime. Seus estados visuais são:

```
[ idle ] 
   │  (WorkflowStarted / AgentRunStarted)
   ▼
[ streaming ] ──(DecisionRequired / NodeAwaitingApproval)──► [ waiting_approval ]
   │                                                                │
   │◄─────────────────(DecisionRegistered: Approved)────────────────┘
   │
   ├──(AgentRunFailed)─────────────────────────────────────► [ interrupted_error ]
   │
   └──(WorkflowCompleted / RunSucceeded)───────────────────► [ finished ]
```

* **idle**: Timeline em repouso. Os blocos passados são renderizados com opacidade reduzida de `55%` em tema cinza-fosco sem brilho traseiro.
* **streaming**: Eventos de progresso chegam ativamente. O Stream renderiza micro-animações verticais (deslocamentos de `8px` para cima com duração de `150ms`) conforme novas tarefas são iniciadas ou logs curtos são consolidados. A borda esquerda do bloco ativo brilha em tom azul sutil.
* **waiting_approval**: A timeline congela a progressão. A linha conectora vertical brilha em ouro-amarelo e um *Approval Gate Card* surge destacado em Z-index proeminente.
* **paused**: Execução suspensa manualmente pelo usuário. A linha de tempo adota traçado tracejado e as animações de preenchimento são paralisadas.
* **interrupted_error**: O bloco ativo interrompe a timeline com borda vermelha e acende um backlight vermelho difuso de baixa intensidade. Exibe opções de mitigação rápida (`Fix`) e explicação do erro.
* **finished**: Bloco concluído com sucesso. O cabeçalho do bloco brilha em verde-esmeralda por `200ms` antes de assentar, exibindo o ROI gerado, a memória gravada em `ck_memory.md` e o total de créditos consumidos.

---

## 4. Limitação e Agrupamento de Agentes Ativos

Para evitar poluição visual e fadiga de atenção em fluxos de processamento massivamente paralelos, a UI limita estritamente o número de agentes individuais representados de forma explícita:

* **Regra de Visualização Direta**: No máximo **5 avatares de agentes** ou linhas de atividade distintas podem ser renderizados lado a lado ou de forma expandida na timeline ativa em um dado instante.
* **Regra do Cluster Card**: Se a execução envolver mais de 5 agentes em paralelo (ex: 12 subagentes depurando arquivos de código simultaneamente), o Stream agrupa visualmente a atividade sob um cartão consolidado chamado **Cluster Card**.
* **Affordance do Cluster**: O cartão é desenhado em Calm Glass cinza-médio com um badge indicativo (ex: `[+] 12 Agentes Ativos`). Passar o mouse ou tocar no Cluster abre um mini-popover vertical mostrando a lista de avatares secundários e a porcentagem de tarefas concluídas por cada um, sem quebrar a estrutura linear do Stream.

---

## 5. Agrupamento Semântico e Estrutura de Informação

O Stream organiza seus dados em blocos aninhados rígidos, agrupando por contexto lógico e eliminando a rolagem infinita de linhas sem nexo:

1. **Run (Ciclo Geral)**: O contêiner pai. Representa o cumprimento da intenção principal enviada pelo usuário (ex: `Run #04: Refatoração da Camada de Autenticação`). Exibe o custo total e tempo decorrido no cabeçalho.
2. **Tarefa (Task)**: O bloco de execução individual delegado a um subagente. Contém a justificativa cognitiva (ex: `QA Agent: Validando testes de integração de rotas`).
3. **Approval (Decision Gate)**: Inserções na timeline marcando decisões de controle de segurança humana.
4. **Artefato (Artifact)**: Os produtos finais criados. Renderizados em formato de micro-cards contendo o tipo de arquivo, link físico direto (`file:///...`) e a ação executada (`[NEW]`, `[MODIFY]`, `[DELETE]`).

---

## 6. Representação Visual de Eventos Críticos

O design gráfico do Stream utiliza as affordances de cores e contrastes do Neurodesign System para sinalizar eventos operacionais cruciais:

```
+-------------------------------------------------------------+
| RUN #12: Criar novo endpoint de faturamento                 |
| Executor: Codex Agent                                       |
|                                                             |
| [x] Task 1: Analisar banco de dados (Est. $0.05 CKC)        |
| [!] Task 2: Modificar schema.prisma (Est. $0.12 CKC)        |
|     +-------------------------------------------------+     |
|     |  ERRO: Relação "Billing" inexistente no banco.  |     |
|     |  [ Explicar Erro ]        [ Executar Fix / Fix ]|     |
|     +-------------------------------------------------+     |
|                                                             |
| Conector de Handoff: Codex Agent ---> QA Agent              |
| Evidência: [schema.prisma](file:///...) -> [Evidence Map]   |
+-------------------------------------------------------------+
```

### A. Erro
* **Design**: Mensagens de erro são encapsuladas em blocos de alerta internos com fundo vermelho translúcido (`rgba(220, 53, 69, 0.1)`) e contorno vermelho sólido de `1px`.
* **Interação**: Apresenta obrigatoriamente duas opções rápidas: `Explain` (solicita explicação semântica do erro) e `Fix` (sugere e inicia o patch de correção proposto pela IA).

### B. Bloqueio
* **Design**: Quando o fluxo é interrompido por violação de políticas (`policy_engine`) ou falta de créditos, a timeline é graficamente cortada por uma linha horizontal amarela com um padrão listrado de advertência e o badge `Blocked by Policy`.

### C. Custo
* **Design**: Exibido no canto superior direito de cada cartão de Run ou Tarefa na cor branca suave (ex: `$0.04 CKC`). Se o custo estiver próximo do limite pré-estabelecido do orçamento cognitivo, o valor passa a piscar em amarelo; se estourar, fica vermelho sólido e o fluxo transita para `waiting_approval`.

### D. Evidência (Evidence Lineage)
* **Design**: Cada artefato gerado apresenta um ícone discreto de conexão física que exibe uma mini-âncora de link. Clicar nessa âncora abre instantaneamente o *Evidence Map* destacando o grafo de causalidade que levou à geração daquele arquivo específico.

### E. Handoff (Passagem de Bastão)
* **Design**: A transferência de tarefas entre agentes é ilustrada por um conector visual na timeline. O avatar do agente de origem (ex: `Codex`) desvanece suavemente para a esquerda enquanto uma linha conectora em curva suave com uma seta desenha o caminho até o avatar do agente de destino (ex: `QA Agent`), que surge iluminado do lado direito.

---

## 7. Diretrizes para Evitar "Chat Log Genérico" (Anti-Chat Rules)

Para garantir que a interface do CKOS permaneça técnica, precisa e inovadora, o design do Stream é proibido de adotar as seguintes práticas padrão de mercado:

* **Proibido Balões de Fala (Bubble Chat)**: O alinhamento de mensagens alternado (usuário à direita em balão azul, IA à esquerda em balão cinza) é banido. Esse padrão induz a conversações informais, consome espaço lateral precioso na tela e prejudica a leitura de diffs de código.
* **Alinhamento e Estrutura Contínua**: Toda a timeline é estruturada com alinhamento fixo à esquerda. A leitura é feita de cima para baixo como uma árvore de commits de Git enriquecida com metadados.
* **Foco em Mutabilidade e Evidências**: Em vez de mensagens conversacionais longas (ex: *"Olá! Analisei seus arquivos e decidi criar uma função nova..."*), o Stream exibe notificações de estado curtas e baseadas em dados estruturados (ex: `Codex Agent: Gravou 42 linhas no arquivo index.ts (+12.4% otimização)`).
* **Campos de Decisão Integrados**: Respostas e inputs do usuário não são inseridos como balões de chat, mas sim como submissões de dados em formulários focados ou em campos de input textuais contextuais inseridos diretamente na base do cartão que solicitou a resposta.
