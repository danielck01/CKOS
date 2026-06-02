---
title: "21 Motion and State Feedback UI/UX Study"
system_id: study_notes_motion_state_feedback_uiux_study_20260528
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
  - "000_STUDY_NOTES/10_UIUX_STUDIES/03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md"
tags:
  - uiux
  - study
  - motion
  - animation
  - state_feedback
  - neurodesign
---

# 21 Motion and State Feedback UI/UX Study

## 1. Propósito

Esta nota de estudo especifica as regras de design cinético, transições visuais e micro-feedbacks de animação para os estados operacionais (Motion and State Feedback) no CKOS. O objetivo é estabelecer parâmetros rígidos sobre como animar componentes no ecossistema de interface, assegurando que o movimento de elementos guie a atenção do usuário para as mudanças de estado reais sem causar cansaço ocular ou latências artificiais.

## 2. O Que Este Padrão Resolve

* **Desorientação em Atualizações Síncronas**: Evita o impacto de mudanças abruptas de layout na tela, suavizando a reordenação de tabelas e timelines por meio de interpolação física.
* **Sensação de Lentidão do Sistema**: Utiliza esqueletos de carregamento (skeletons) inteligentes que preveem o formato do output final antes do processamento completo, melhorando o tempo de resposta percebido.
* **Falta de Foco em Processos de Fundo**: Utiliza pulsos de cor e movimentos discretos nas bordas para avisar o usuário sobre execuções em segundo plano sem interromper a digitação.

## 3. O Que Não Pode Virar

* **Interface Poluída de Animações**: Não permite o uso de animações decorativas em loop que não correspondam a transições de estados reais do runtime.
* **Atraso Operacional**: Nenhuma transição visual de entrada ou saída pode durar mais do que 300ms, impedindo que o usuário tenha que "esperar a animação terminar" para interagir com o botão.
* **Causador de Náuseas**: Evita transições espaciais de rotação 3D ou redimensionamentos desproporcionais que induzam à fadiga visual ou sintomas de cinetose.

## 4. Relação com Runtime / Dashboard / Command Center / Node Canvas

* **Event-Driven UI transitions**: As classes de transição de estilo reagem diretamente aos eventos de progresso e finalização de tarefas transmitidos no barramento de eventos.
* **Command Center**: O fechamento da Commandbar realiza um deslizamento para cima (slide-up) limpo com recolhimento de opacidade em 150ms.
* **Node Canvas**: Mover nós no canvas de grafos utiliza curvas com amortecimento físico (spring physics) para simular inércia e gravidade espacial.

## 5. Padrões Cinéticos e Curvas de Animação (Ease & Spring Rules)

* **Limites de Duração Rígidos**:
  - *Transições de micro-badge / Hover states*: **100ms a 150ms**.
  - *Abertura de gavetas laterais / Modais*: **150ms a 250ms**.
  - *Navegação de rotas de página inteira*: **250ms a 300ms**.
* **Curvas de Interpolação**:
  - *Entrada de elementos (Ease-Out)*: `cubic-bezier(0.16, 1, 0.3, 1)` (desaceleração suave para acentuar a precisão).
  - *Saída de elementos (Ease-In)*: `cubic-bezier(0.7, 0, 0.84, 0)` (aceleração rápida de descarte).
  - *Movimento físico de nós (Spring)*: Amortecimento sintonizado sem oscilações repetitivas (no-overshoot spring).

## 6. Mapeamento de Transições para os Estados de Execução

* **Interpreting Intent**: Comando brilha discretamente com backlight pulsante em ciclo senoidal lento (período de 1.5s).
* **Waiting Tool**: O chip correspondente assume uma máscara translúcida pulsante com deslocamento horizontal de brilho (shimmer effect).
* **Audit Running**: O anel concêntrico de Metacognik gira lentamente a 30 RPM com opacidade de 80%.
* **Failed / Blocked State**: O elemento pisca em vermelho sólido por 150ms duas vezes de forma curta para atrair o reflexo de orientação visual e depois fixa-se na cor semântica estável de erro.

## 7. Relação com Dimensões CKOS

* **Execution**: Traduz a atividade das runs em movimentações dinâmicas na tela.
* **Context**: Utiliza direções espaciais coerentes (deslizar da direita para esquerda para detalhes complementares) para consolidar a hierarquia de escopo.
* **Learning**: Sinaliza novos insights ou artefatos gerados por meio de pequenos ingressos luminosos pontuais (glow ingress).

## 8. Comportamento Web vs. Mobile

* **Web**:
  - Interações baseadas no cursor de mouse (hover states rápidos e expansões de acordeão).
* **Mobile**:
  - Transições táteis deslizáveis (swipes) com retorno tátil simulado por animações de rebote (bounce-back) na borda se o limite do contêiner for atingido.

## 9. Anti-Patterns

* **Loading Spinner Tradicional no Centro**: Usar o ícone circular de carregamento genérico em tela cheia que esconde toda a interface ativa sem dar pistas sobre o progresso real.
* **Animações Desconexas de Layout**: Alterar a altura de um contêiner subitamente sem animar a propriedade correspondente, fazendo com que os componentes inferiores saltem de posição de forma brusca (layout shifting).

## 10. Acceptance Criteria

* Toda animação de carregamento deve ser substituída por esqueletos de layout (shimmer skeletons) que respeitem a estrutura do componente que será renderizado.
* Caso as preferências do sistema operacional reportem "Reduced Motion" ativo, todas as transições de deslocamento e escala devem ser removidas, mantendo apenas transições simples de opacidade (fade-in/fade-out).
* Animações de erro ou aviso devem durar o tempo mínimo para atração de foco sem poluir a área visiva do usuário a longo prazo.
