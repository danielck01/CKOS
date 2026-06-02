---
title: "Mobile Command-First Ergonomics"
file: "04_MOBILE_COMMAND_FIRST_ERGONOMICS.md"
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
purpose: "Definir as diretrizes de ergonomia física e layout mobile baseado no padrão command-first para o CKOS."
inputs:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md"
  - "000_ROADMAPS/19_UIUX_STUDY_ROADMAP/README.md"
outputs:
  - "04_MOBILE_COMMAND_FIRST_ERGONOMICS.md"
framework: "Sentir -> Pensar -> Criar -> Conectar -> Avaliar -> Elevar"
edge_cases:
  - "Redução de tabelas densas de desktop resultando em colunas ilegíveis e espremidas"
  - "Botões de aprovação críticos localizados na zona morta superior do polegar"
integrations:
  - "antigravity_design_study"
prompts:
  - "Mapear padrões ergonômicos de uso móvel com foco na metade inferior e navegação rápida."
metrics:
  - "Zero de código implementado"
  - "100% dos controles críticos acessíveis na zona ergonômica verde do polegar"
related_notes:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md"
tags:
  - "mobile"
  - "ergonomics"
  - "command_first"
  - "design_study"
---

# Mobile Command-First Ergonomics

Esta nota de estudo estabelece os padrões ergonômicos de interface para a visualização móvel do CKOS, garantindo que o controle de processos densos de agentes de IA seja natural, rápido e adaptado ao uso de toque com uma única mão.

---

## 1. Mapeamento Ergonômico de Toque e Zonas de Acessibilidade

Para evitar fadiga e erros de toque em ações críticas de governança, o design mobile do CKOS segmenta a tela do dispositivo móvel vertical em três zonas ergonômicas de alcance do polegar:

```
+------------------------------------+
|  ZONA VERMELHA (Alcance Difícil)   |
|  - Status do sistema global        |
|  - Ícones de configurações passivas|
+------------------------------------+
|  ZONA AMARELA (Alcance Médio)      |
|  - Leitura de logs compactos       |
|  - Visualização de grafos simples  |
+------------------------------------+
|  ZONA VERDE (Alcance Fácil)        |
|  - COMMAND BAR / Input de texto    |
|  - Botões de aprovação de gates    |
|  - Docks flutuantes e abas         |
+------------------------------------+
```

### A. Zona Verde (Metade Inferior - Acesso Rápido)
* **Elementos**: O input principal de intenções (*Command Center*), botões de ação e botões de aprovação crítica de planos de execução.
* **Comportamento**: A commandbar móvel flutua logo acima do teclado virtual. As pílulas de sugestão dinâmicas e chips contextuais são renderizados em carrosséis horizontais deslizando logo acima do input de texto, facilitando o toque com o polegar.

### B. Zona Amarela (Centro da Tela - Visualização Principal)
* **Elementos**: Widgets ativos de progresso de agentes, visualizadores de timelines e mini-painéis de status de tarefas.
* **Comportamento**: Informações dinâmicas que exigem leitura atenta e rolagem vertical suave.

### C. Zona Vermelha (Metade Superior - Leitura Passiva)
* **Elementos**: Status global de conexão do CKOS, indicador macro de consumo de créditos e atalhos para configurações passivas do usuário.
* **Comportamento**: Elementos informativos que não exigem interação constante. Qualquer botão inserido nesta área deve ser estritamente secundário e protegido contra toques acidentais.

---

## 2. Prevenção de "Mobile Espremido" (Data Compression Rules)

Um erro comum em interfaces móveis de IA é a tentativa de reduzir layouts densos de desktop diretamente para telas móveis. O CKOS define regras rígidas de adaptação ergonômica:

### A. Grafo de Agentes (Node Canvas)
* **Desktop**: Exibição em canvas infinito com arrastar e zoom bidimensional.
* **Mobile**: O canvas complexo é ocultado por padrão. Em seu lugar, é renderizado um fluxo linear vertical simplificado de dependências (comportamento de lista aninhada). Se o usuário fizer o gesto de pinça para expandir, o sistema abre uma folha inferior (*bottom sheet*) contendo o modo paisagem forçado para visualização espacial do grafo.

### B. Tabelas Médicas e Financeiras de Evidências (Evidence Map & Billing)
* **Desktop**: Múltiplas colunas de dados estruturados lado a lado (ex: fonte, validade, autor, ROI, risco).
* **Mobile**: As colunas são convertidas em cartões verticais individuais empilháveis (*stacked cards*). O cartão expõe apenas a métrica principal (ex: ROI) e o nome do arquivo. Detalhes secundários de auditoria de risco e validade são ocultados sob um acordeão expansível de toque suave.

### C. Folhas Inferiores Deslizantes (Bottom Sheets) para Decisões
* **Comportamento**: Toda vez que o sistema operacional de IA exigir um Approval Gate ou uma resposta a perguntas inteligentes, o CKOS aciona uma *Bottom Sheet* que desliza de baixo para cima na tela, preenchendo no máximo `70%` da altura total.
* **Affordance**: Apresenta uma barra superior centralizada arredondada indicando que o usuário pode arrastar para fechar ou colapsar a folha, mantendo a sensação de controle espacial e físico.
* **Layout**: Os botões de tomada de decisão (ex: `Aprovar Plano`, `Rejeitar / Alterar`) ocupam toda a largura da parte inferior da folha ergonômica, facilitando a confirmação de segurança.

---

## 3. Especificações Técnicas Mobile e Ergonomia de Toque

### A. Breakpoints Responsivos
* **Mobile Compacto (SM)**: `320px` a `479px` (foco em celulares pequenos em portrait).
* **Mobile Padrão (MD)**: `480px` a `767px` (celulares de tela grande e phablets).
* **Tablet (LG)**: `768px` a `1023px` (início do layout adaptativo híbrido).
* A partir de `1024px`, o sistema operacional transiciona automaticamente para o layout Desktop Completo.

### B. Área Mínima de Toque (Touch Targets)
* **Controles Críticos (Aprovação/Ações)**: Mínimo de `48px` x `48px` físicos (ou `48dp`).
* **Micro-ações/Chips**: Mínimo de `32px` x `32px`, mas sempre acompanhados de espaçamento de segurança (padding) de no mínimo `8px` entre os elementos vizinhos para evitar toques acidentais (misclicks).

### C. Zonas de Segurança (Safe Areas)
* **Barra de Status (Superior)**: Reservar espaço mínimo de `44px` no iOS e `24px` no Android para o notch e informações de sistema (relógio, bateria).
* **Indicador de Home (Inferior)**: Toda UI flutuante ou botão fixado na base deve manter uma margem inferior mínima de `34px` para não conflitar com a barra de navegação/gesto de home nativa do sistema operacional do smartphone (evitando que o usuário feche a aplicação sem querer).

### D. Interação com o Teclado Virtual (Soft Keyboard Handling)
* Quando o teclado virtual é ativado, a Command Bar se desloca dinamicamente para o topo do teclado (`anchored input`).
* A viewport operacional útil diminui. Nesse estado, o conteúdo principal da tela realiza scroll vertical livre com um fade de transparência no topo e na base para indicar continuidade espacial.

### E. Bottom Dock (Dock de Navegação Inferior)
* Um dock flutuante de vidro de `56px` a `64px` de altura fica fixado na base da tela (respeitando a Safe Area).
* Ele abriga os 4 principais atalhos da sessão ativa: `Command Center` (Centralizado), `Project Dashboard` (Lista rápida), `Agent Activity Stream` (Timeline compacta) e `Evidence Map` (Atalhos).

### F. Folhas Inferiores (Bottom Sheets)
* **Bottom Sheet Compacta (Peek)**: Ocupa até `35%` da tela. Usada para exibir status rápidos de subagentes ou estimativas de custos.
* **Bottom Sheet Expandida (Full)**: Ocupa até `85%` da tela. Usada para Approval Gates completos, com visualizador de diffs e logs detalhados. Nunca deve ocupar 100% da tela para que o usuário saiba que ainda está no mesmo contexto espacial (affordance de dismiss clicando fora).

### G. Orientação Portrait/Landscape
* **Portrait (Padrão)**: Foco em comando, leitura rápida de timelines, aprovações de portões e interações textuais.
* **Landscape (Forçado)**: Ativado exclusivamente quando o usuário rotaciona o aparelho ou expande o `Node Canvas`. Nesse modo, a grade de agentes é exibida em modo de visualização livre tridimensional com suporte a gestos espaciais.

### H. Gestos Permitidos e Proibidos
* **Gestos Permitidos**:
  * **Swipe Down (Bottom Sheets)**: Colapsar ou fechar o portão/folha ativa.
  * **Pinch-to-Zoom**: Ampliar ou reduzir o grafo no modo Landscape do Node Canvas.
  * **Horizontal Swipe**: Navegar entre chips de sugestões na Command Bar.
* **Gestos Proibidos**:
  * **Swipe Left/Right (Global)**: Proibido para transicionar entre telas principais, pois conflita com a navegação lateral nativa do iOS (gesto de voltar).
  * **Double Tap (Crítico)**: Proibido para ações de aprovação ou execução. Decisões críticas de governança exigiriam toque único e pressionamento contínuo sutil para evitar disparos acidentais.
