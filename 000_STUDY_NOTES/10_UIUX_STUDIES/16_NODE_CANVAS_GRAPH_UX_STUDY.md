---
title: "16 Node Canvas Graph UX Study"
system_id: study_notes_node_canvas_graph_ux_study_20260528
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
  - "000_STUDY_NOTES/10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/09_EXECUTION_PLAN_WIDGET_UIUX_STUDY.md"
tags:
  - uiux
  - study
  - node_canvas
  - graph
  - spatial_ux
  - neurodesign
---

# 16 Node Canvas Graph UX Study

## 1. Propósito

Esta nota de estudo especifica os padrões de design UI/UX e neurodesign para o **Node Canvas** (Canvas de Nós) do CKOS. O objetivo é orientar a concepção tridimensional e espacial da interface de grafos, detalhando como visualizar a topologia de tarefas de agentes, handoffs, lineages de arquivos e dependências técnicas no espaço 2D infinito do sistema operacional.

## 2. O Que Este Padrão Resolve

* **Incompreensão de Fluxos Complexos**: Representa de forma espacial o fluxo de dependências entre tarefas que timelines lineares 1D não conseguem expressar de forma satisfatória.
* **Perda de Rastreabilidade de Origem**: Desenha explicitamente as linhas de linhagem que ligam artefatos finais aos arquivos originais de briefing e referências.
* **Falta de Interação em Execuções Concorrentes**: Permite pausar, ajustar parâmetros ou reiniciar caminhos específicos do workflow manipulando diretamente os nós visuais no grafo.

## 3. O Que Não Pode Virar

* **Fluxograma Estático Cosmético**: Não pode ser um desenho inativo sem impacto no runtime; a exclusão de uma linha ou nó no canvas deve alterar o plano de execução no backend.
* **Interface Pesada Irresponsiva**: O renderizador do grafo (Canvas/WebGL) deve sustentar centenas de nós com taxa estável de 60fps em dispositivos normais, utilizando renderização condicional para nós fora do viewport.
* **Visualizador de Logs Genérico**: Não deve ser usado para exibir logs de texto longos dentro dos nós; logs pertencem a gavetas laterais de detalhes sob demanda.

## 4. Relação com Runtime / Dashboard / Command Center / Node Canvas

* **Event Bus do Runtime**: O canvas assina atualizações de status de nós via `node_status_projection`. Mudanças no runtime (ex: nó atinge erro) atualizam instantaneamente a borda e o backlight do nó no canvas.
* **Command Center**: Atalhos da Commandbar podem focar, selecionar ou criar nós espacialmente (ex: `/canvas focus NodeA`).
* **Dashboard**: Projeta agregados de progresso de workflows do canvas nas telas de sumário financeiro e ROI.

## 5. Regras Espaciais de Interação e Navegação no Grafo 2D

* **Zoom e Pan Intuitivos**: Controles ergonômicos usando roda do mouse, gestos de pinça (pinch-to-zoom) no trackpad/tela móvel, e atalhos rápidos de teclado (`+` / `-` / `0` para reset).
* **Alinhamento Automático de Nós (Auto-Layout)**: Algoritmo de distribuição baseado em forças direcionadas com opção de travamento manual para preservar a personalização espacial do usuário.
* **Conectores Curvos Dinâmicos**: As linhas que ligam os nós são representadas por curvas de Bézier suaves, cuja cor e padrão de animação indicam o fluxo de controle:
  - *Gradiente em movimento*: Fluxo de execução em progresso ativo.
  - *Vermelho estático*: Link onde ocorreu interrupção por erro ou conflito.
  - *Tracejado amarelo*: Relação especulativa ou hipótese em auditoria.

## 6. Visualização de Linhagem (Lineage) e Evidências

* **Linhas de Evidência**: Ao selecionar um nó de artefato produzido, a interface ilumina exclusivamente as conexões que levam às fontes originais de dados (`roi_evidence_links` e `evidence_items`), esmaecendo os nós não relacionados.
* **Visualização de Contradições de Evidências**: Conflitos ou contradições detectados pela auditoria do Metacognik conectam os dois nós divergentes com um elo vermelho pulsante de alerta.

## 7. Relação com Dimensões CKOS

* **Context**: Nós específicos representam pastas do vault, briefing de projetos ou diretórios de código mapeados como insumos.
* **Evidence**: Representa as âncoras epistemológicas justificadoras.
* **Approval**: Nós especiais em formato de portão (cadados ouro) que travam o progresso da execução até a assinatura digital do stakeholder.
* **Execution**: Representa a topologia viva do pipeline ativo de agentes autônomos.

## 8. Comportamento Web vs. Mobile

* **Web**:
  - Área de visualização espacial em tela inteira (Full-canvas mode).
  - Seleção em massa de nós, arrastar e soltar (drag and drop), e menu de contexto rico de clique direito.
* **Mobile**:
  - Fallback ergonômico para uma lista de árvore hierárquica colapsável se o usuário preferir evitar manipulação tátil complexa de grafos.
  - Modo pan simplificado com guias visuais de ancoragem nas bordas para localizar nós fora da área visível.

## 9. Anti-Patterns

* **Cruzar Linhas Sem Orientação**: Cruzar conexões de forma desordenada criando o efeito visual "cabelo de anjo" (spaghetti lines).
* **Nós Flutuantes Sem Relação**: Permitir nós de tarefas na execução sem conexões de dependência explícitas com o restante do workflow.

## 10. Acceptance Criteria

* O estado e posicionamento dos nós no canvas devem ser mantidos persistentes no workspace do usuário.
* Selecionar qualquer nó de execução deve carregar o diff de arquivos alterados e logs técnicos na gaveta de detalhes lateral em menos de 150ms.
* O canvas deve refletir de forma síncrona o bloqueio físico por aprovação, indicando visualmente o nó congelado com o backlight do portão correspondente.
