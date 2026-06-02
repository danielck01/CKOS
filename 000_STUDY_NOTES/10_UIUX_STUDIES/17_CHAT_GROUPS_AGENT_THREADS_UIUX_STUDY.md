---
title: "17 Chat, Groups and Agent Threads UI/UX Study"
system_id: study_notes_chat_groups_agent_threads_uiux_study_20260528
phase: 000_STUDY_NOTES
category: uiux_study
status: draft
confidence: unverified
provenance_status: unverified
source_tool: antigravity
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers: [pmo_ckos, metacognik]
approval_required: [founder, pmo_ckos, metacognik]
related_notes:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/ck_memory.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/07_AGENT_ACTIVITY_STREAM_UIUX_STUDY.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/11_COST_CREDITS_AND_ROI_AWARE_UX_STUDY.md"
tags:
  - uiux
  - study
  - chat
  - agent_threads
  - communication
  - neurodesign
---

# 17 Chat, Groups and Agent Threads UI/UX Study

## 1. Propósito

Esta nota de estudo especifica os padrões de design UI/UX e neurodesign para **Chat, Grupos e Linhas de Comunicação de Agentes (Agent Threads)** no CKOS. O objetivo é estabelecer diretrizes conceituais sobre como formatar visualmente a colaboração entre usuários humanos e agentes autônomos, eliminando as interfaces de chat tradicionais de consumo em favor de timelines técnicas orientadas a ações e modificações de estado estruturadas.

## 2. O Que Este Padrão Resolve

* **Bate-papo Sem Fim e Inútil**: Previne a proliferação de conversas casuais na interface que não geram entregas reais ou logs operacionais auditáveis.
* **Falta de Delimitação de Contexto**: Esclarece visualmente quais arquivos do vault e referências do projeto estão acessíveis para leitura/escrita em cada canal de discussão ativo.
* **Consumo Fantasma de Recursos**: Exibe de forma contínua o custo acumulado em créditos da linha de conversa ativa, alertando se o loop de iterações de IA estiver saindo do controle.

## 3. O Que Não Pode Virar

* **Clone de WhatsApp/ChatGPT**: Não pode exibir balões de mensagens alternadas centralizados nas laterais sem conexões técnicas diretas de lineage ou atalhos de ferramentas.
* **Caixa Preta de Decisão**: A conversa entre subagentes em segundo plano não pode ser invisível; o usuário deve poder colapsar e auditar os diálogos internos e handoffs ocorridos durante a execução da tarefa.
* **Canal Sem Vinculação de Tarefa**: Toda conversa ou grupo criado na interface deve estar atrelado a um nó ou objetivo de workflow explícito do projeto.

## 4. Relação com Runtime / Dashboard / Command Center / Node Canvas

* **Event Bus de Execução**: A timeline de chat exibe mensagens geradas a partir de eventos `AgentOutputProduced` e logs do runtime.
* **Node Canvas**: Cada grupo ou canal ativo corresponde a um nó de equipe ou conjunto de arestas de handoff que operam concorrentemente no Canvas 2D.
* **Command Center**: O usuário abre threads de agentes específicos digitando comandos contextuais (ex: `/chat agent_coder`).

## 5. Linhas de Discussão Técnica (Technical Threads)

* **Alinhamento Unilateral à Esquerda**: Diferente de chats de consumo (balões à esquerda e à direita), todas as interações e mensagens de agentes alinham-se em uma timeline linear técnica vertical na esquerda.
* **Exposição de Handoffs de Agentes**: Quando o controle da conversa passa de um agente a outro (ex: Coder para Auditor), a interface renderiza uma linha curva sutil com o avatar dos agentes envolvidos indicando a transição.
* **Micro-Diffs Integrados**: Mensagens de agentes que alteram código ou documentos mostram um comparador visual de texto (Diff de adições e deleções) compacto de forma nativa no fluxo da conversa.

## 6. Delimitação Visual de Limites de Contexto (Context Boundaries)

* **Badge de Escopo Ativo**: O cabeçalho da conversa exibe o chip indicando a pasta ou arquivos sob controle de escrita da thread (ex: `Escopo: @/docs/briefing/`).
* **Visualizador de Context Pack**: Um popover expansível no topo lista as chaves de contexto e memórias lidas pelos agentes presentes na thread técnica, garantindo conformidade de isolamento.

## 7. Monitoramento de Créditos e Custos da Linha de Conversa

* **Indicador de Orçamento Flutuante**: O painel exibe a despesa acumulada da thread no formato: `Custo da Conversa: $0.04 CKC`.
* **Aviso de Model Loop**: Se a conversa entre subagentes gerar mais de 5 iterações consecutivas sem input humano, a borda da caixa de chat pulsa em laranja e exibe um botão "Pausar Loop".

## 8. Comportamento Web vs. Mobile

* **Web**:
  - Organização em painel lateral de split-screen permitindo visualizar a conversa técnica ao lado do editor de arquivos alterados.
* **Mobile**:
  - O fluxo da conversa ocupa a totalidade da tela, com atalhos de deslizar para exibir o diff completo ou aprovar portões decisórios propostos.

## 9. Anti-Patterns

* **Mensagens Sem Metadados de Auditoria**: Exibir texto de IA sem os indicadores de confidence score, referências documentais ou tempo de processamento.
* **Interface Textual Pura**: Omitir representações gráficas de status de processamento (loading skeleton) durante latências de resposta prolongadas.

## 10. Acceptance Criteria

* Toda thread de comunicação deve possuir um link físico para o respectivo nó de workflow do grafo do canvas.
* As interações de IA devem listar explicitamente os arquivos lidos e escritos no respectivo turno da conversa.
* O encerramento da tarefa associada deve arquivar e congelar a thread, impedindo novos inputs de texto no chat desativado.
