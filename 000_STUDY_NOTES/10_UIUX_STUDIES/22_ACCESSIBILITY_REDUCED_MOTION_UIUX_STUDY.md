---
title: "22 Accessibility and Reduced Motion UI/UX Study"
system_id: study_notes_accessibility_reduced_motion_uiux_study_20260528
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
  - "000_STUDY_NOTES/10_UIUX_STUDIES/05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/20_DESIGN_SYSTEM_THEME_GOVERNANCE_UIUX_STUDY.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/21_MOTION_STATE_FEEDBACK_UIUX_STUDY.md"
tags:
  - uiux
  - study
  - accessibility
  - reduced_motion
  - wcag
  - keyboard_navigation
  - neurodesign
---

# 22 Accessibility and Reduced Motion UI/UX Study

## 1. Propósito

Esta nota de estudo especifica as diretrizes de **Acessibilidade e Redução de Movimento (Accessibility and Reduced Motion)** para o CKOS. O objetivo é estabelecer parâmetros rígidos para assegurar a inclusão de usuários com restrições motoras, visuais e cognitivas, definindo como simplificar o comportamento do canvas de grafos, timelines de agentes e commandbar de acordo com as normas internacionais WCAG 2.1.

## 2. O Que Este Padrão Resolve

* **Bloqueio de Uso para Usuários de Leitores de Tela**: Resolve a impossibilidade de leitores de tela interpretarem o Node Canvas 2D espacial por meio do desenvolvimento de uma estrutura alternativa semântica.
* **Sobrecarga Cognitiva e Crises de Ansiedade**: Impede que animações pulsantes ou flashes de tela (flicker) desencadeiem problemas de fadiga ou distúrbios vestibulares em usuários sensíveis.
* **Barreira de Uso Sem Mouse**: Permite operar todo o sistema operacional de IA (incluindo a manipulação e criação de conexões entre nós) usando exclusivamente o teclado.

## 3. O Que Não Pode Virar

* **Checkbox Estético de Acessibilidade Sem Ação**: Não pode ser um botão de enfeite que apenas altera a cor do site sem reestruturar a semântica da DOM.
* **Layout Quebrado em Alto Contraste**: As regras de contraste elevado ou ampliação de fontes não devem desalinhamento de botões de aprovação ou esconder informações de custo no rodapé.
* **Modo de Uso Degradado**: O usuário de acessibilidade não deve receber uma interface com menos recursos lógicos; a alternativa visual deve expor exatamente o mesmo nível de controle e dados que a original.

## 4. Relação com Runtime / Dashboard / Command Center / Node Canvas

* **Preferences Service**: A interface lê as diretrizes de acessibilidade do navegador/sistema operacional (`@media (prefers-reduced-motion)`, `@media (forced-colors)`) e ajusta os estilos na inicialização.
* **Command Center**: Suporta atalhos abrangentes e leitores de tela em todas as sugestões do autocompleter.
* **Node Canvas**: O grafo 2D é mapeado para um fallback de árvore hierárquica legível e acessível via teclado.

## 5. Diretrizes de Acessibilidade no Node Canvas

* **Navegação Bidimensional por Teclado (Tab Navigation)**:
  - Pressionar a tecla `Tab` move o foco sequencialmente de nó em nó seguindo a ordem de execução do workflow.
  - O foco ativo em um nó é destacado por um anel reflexivo duplo (double focus ring) com espessura de 3px e cor contrastante.
  - As setas direcionais permitem navegar pelas conexões (arestas de dependência) para auditar a linhagem de dados.
* **Fallback Estrutural Semântico**:
  - Usuários de leitores de tela (ex: NVDA, VoiceOver) podem alternar para a **Visualização em Árvore Estruturada**, que renderiza a topologia do grafo em tags `<nav>` e `<ul>`/`<li>` padrão, fornecendo a leitura correta das relações pai-filho e estados dos nós de execução.

## 6. Governança de Redução de Movimento e Alto Contraste

* **Comportamento sob `prefers-reduced-motion: reduce`**:
  - Desativação de todas as animações de pulso de backlight de estado (substituídas por bordas pontilhadas ou badges estáticos).
  - Remoção de efeitos de deslocamento e scroll suave (instant jump).
  - Suspensão de efeitos de shimmer em skeletons de carregamento (substituídos por fundos cinzas estáticos de opacidade fixa).
* **Comportamento sob Alto Contraste**:
  - Bordas de caixas de chat, widgets e commandbar mudam para 2px de espessura com cores de contraste máximo (branco/preto puro).
  - Remoção de backdrops translúcidos calmos de baixa visibilidade (glassmorphism) em favor de fundos sólidos opacos.

## 7. Relação com Dimensões CKOS

* **Context**: Adapta o layout dinamicamente às capacidades de exibição do hardware e preferências do usuário.
* **Learning**: Reduz a barreira de aprendizado e a exaustão neurológica sob uso prolongado do sistema operacional de IA.

## 8. Comportamento Web vs. Mobile

* **Web**:
  - Suporte completo a leitores de tela ARIA attributes (`aria-live="polite"` para streaming de logs de agentes e outputs).
  - Foco em atalhos de teclado rápidos.
* **Mobile**:
  - Adaptação às ferramentas nativas de acessibilidade (TalkBack no Android, VoiceOver no iOS).
  - Targets de toque ampliados para no mínimo `48px x 48px` para todas as ações cruciais de controle e aprovação.

## 9. Anti-Patterns

* **Logs em Streaming sem ARIA Live**: Impedir que usuários cegos saibam se subagentes estão escrevendo arquivos em tempo real por falta de tags `aria-live`.
* **Uso Exclusivo de Cores para Indicar Status**: Exibir um nó apenas em verde ou vermelho para indicar sucesso ou erro sem incluir texto ou ícones explicativos adicionais.

## 10. Acceptance Criteria

* O sistema operacional deve respeitar as diretrizes de acessibilidade nativas do usuário (Reduced Motion e High Contrast) sem necessidade de acionamento manual de botões dentro do aplicativo.
* Toda ação de alteração de estado no Node Canvas ou no Approval Gate deve ser operável via teclado.
* A pontuação mínima de acessibilidade medida por ferramentas automatizadas (ex: Lighthouse A11y) nas superfícies estruturadas deve ser superior a **95**.
