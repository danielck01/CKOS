---
title: "Visual Reference Taxonomy - Canvas OS"
file: "01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md"
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
purpose: "Classificar as referências visuais de design em famílias conceituais e operacionais para a interface do CKOS."
inputs:
  - "000_STUDY_NOTES/04_UI_UX_STUDY/10_Referências_Design"
  - "000_ROADMAPS/19_UIUX_STUDY_ROADMAP/README.md"
outputs:
  - "01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md"
framework: "Sentir -> Pensar -> Criar -> Conectar -> Avaliar -> Elevar"
edge_cases:
  - "Mistura indesejada de famílias contrastantes na mesma tela"
  - "Aplicação de transparências excessivas prejudicando acessibilidade"
integrations:
  - "antigravity_design_study"
prompts:
  - "Traduzir referências visuais em gramáticas de runtime funcionais de IA."
metrics:
  - "Zero linhas de código geradas"
  - "100% de cobertura das imagens de referência em taxonomias claras"
related_notes:
  - "000_STUDY_NOTES/04_UI_UX_STUDY/README.md"
  - "000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md"
tags:
  - "taxonomy"
  - "canvas_os"
  - "visual_references"
  - "design_study"
---

# Visual Reference Taxonomy: Canvas OS & AI OS for Designers

Esta nota de estudo analisa as referências visuais disponibilizadas na pasta `000_STUDY_NOTES/04_UI_UX_STUDY/10_Referências_Design` e as organiza em uma taxonomia operacional direcionada ao CKOS, garantindo que o design final não seja meramente decorativo, mas sim uma projeção síncrona do runtime do sistema operacional de agentes.

---

## 1. Classificação das Referências em Famílias Visuais

### A. Calm Glass / Ambient Interface
* **Caracterização**: Widgets construídos com vidro fosco de alta refração física (desfoque de fundo de `20px` a `30px`), cantos hiper-arredondados (*squircles* de `24px` a `32px`), sombras internas finas imitando bordas de vidro polido e fundos naturais com gradientes suaves e orgânicos (dunas de areia ao amanhecer, céus crepusculares roxos/rosas).
* **Sensação Cognitiva (Sentir)**: Serenidade, redução do estresse técnico, colaboração fluida, acolhimento e clareza intelectual.
* **Problemas que Resolve**: Suaviza a complexidade de interações autônomas complexas com IA, evitando a sensação de "terminal industrial de comandos" para usuários corporativos ou finais.
* **Riscos Operacionais**: Baixo contraste sob certas imagens de fundo, perda de legibilidade de texto fino, excesso de decoração visual (*skeuomorfismo do vidro*) que esconde a falta de processamento real.
* **Aplicação no CKOS**: Workspace colaborativo, visualizadores de memórias de longo prazo, telas de onboarding de clientes e painéis de ROI macro.
* **Não Aplicável a**: Console de desenvolvimento em tempo real, logs brutas de processamento ou depuração profunda de subagentes.

### B. Operational Control Plane (Spatial Canvas)
* **Caracterização**: Grade pontilhada ortogonal de fundo, cartões opacos flutuando sobre uma base semitransparente colorida por gradientes quentes e escuros (ex: cobre, preto absoluto e vermelho sutil), conectores dinâmicos curvos interligando nós e cartões de agentes com fotos reais de personas ou documentos de entrada/saída anexados na própria malha.
* **Sensação Cognitiva (Sentir)**: Controle absoluto de processos distribuídos, orientação espacial das capacidades ativas e tangibilidade das decisões da IA.
* **Problemas que Resolve**: Torna visível e rastreável onde cada subagente está trabalhando, quais arquivos estão abertos e qual a hierarquia lógica de interdependência das tarefas.
* **Riscos Operacionais**: Entropia visual ("efeito teia de aranha" ou espaguete) ao exibir conexões de dezenas de agentes sem filtragem dinâmica ou agrupamento contextual.
* **Aplicação no CKOS**: *Node Canvas*, orquestrador de subagentes, mapeador físico da filetree alterada e fluxogramas de auditoria lógica do PMO.
* **Não Aplicável a**: Telas mobile de visualização rápida, telas de transações financeiras estritamente tabulares ou formulários estáticos de configurações.

### C. Editorial AI / Command Surfaces
* **Caracterização**: Campos de prompt escuros e translúcidos proeminentes com cantos arredondados, botões contextuais de capacidades embutidos (*Attach*, *Online*), acompanhados de pílulas de sugestões flutuantes que mudam de acordo com o contexto e mini-painéis suspensos exibindo código de backend sendo executado em tempo real com trechos de erro destacados.
* **Sensação Cognitiva (Sentir)**: Coautoria imediata com a IA, prompt-centricity e senso de resposta instantânea e adaptativa.
* **Problemas que Resolve**: Elimina o atraso e a obscuridade das caixas-pretas de IA padrão de mercado. O usuário vê o que o sistema "está pensando" e escrevendo no momento da execução.
* **Riscos Operacionais**: Ansiedade visual se as atualizações de escrita de arquivos ou os códigos piscantes de progresso forem apresentados sem animações de transição suaves ou sem mecanismos de pausa/intervenção do usuário.
* **Aplicação no CKOS**: *Command Center* principal, terminal AI-first da barra de ferramentas global e o widget do plano de execução.
* **Não Aplicável a**: Visualizações agregadas de dados consolidados, históricos de cobrança ou perfis de usuários.

### D. Medical/Data-Dense Minimal
* **Caracterização**: Fundo cinza-claro absoluto com elementos tridimensionais transparentes ou anatômicos (âncoras centrais de atenção), cercados por cartões modulares extremamente limpos de cantos médios (`12px` a `16px`), timelines verticais detalhadas com ícones de atividades médicas e exames em alto contraste de cor cirúrgico.
* **Sensação Cognitiva (Sentir)**: Precisão técnica, rastreabilidade médica/financeira, segurança e credibilidade nos dados exibidos.
* **Problemas que Resolve**: Permite a visualização rápida de uma grande variedade de dados complexos e heterogêneos sem poluição visual ou sobreposição caótica.
* **Riscos Operacionais**: Pode tornar a interface entediante, fria e sem apelo estético se os espaçamentos, tipografia geométrica e micro-contrastes não forem aplicados com extremo rigor.
* **Aplicação no CKOS**: *Evidence Map*, relatórios de auditoria do PMO Auditor, painel financeiro de créditos e detalhamento técnico de logs de erros.
* **Não Aplicável a**: Onboarding inicial poético, áreas de brainstorming e telas de escrita criativa dos agentes.

### E. Floating Widget Ecosystems
* **Caracterização**: Blocos modulares independentes e altamente focados (controles de áudio, temporizadores, gráficos rápidos de barra horizontal, contatos flutuantes, botões circulares concêntricos) que parecem pairar sobre a tela, permitindo recombinação sem exigir grades fixas ou sidebars clássicas de SaaS de mercado.
* **Sensação Cognitiva (Sentir)**: Flexibilidade, controle pessoal da área de trabalho, modularidade e descentralização.
* **Problemas que Resolve**: A rigidez dos painéis laterais clássicos de SaaS que engessam a visualização. Permite que o usuário crie seu próprio cockpit operacional dependendo do tipo de tarefa.
* **Riscos Operacionais**: Desalinhamento visual e confusão de prioridades se o sistema não reordenar os widgets flutuantes de forma automatizada com base no contexto ativo.
* **Aplicação no CKOS**: Micro-status do agente na barra de tarefas, atalhos do *Approval Gate* móvel, controles de chamada/chat ativo e visualizadores rápidos de custos/créditos de token.
* **Não Aplicável a**: Painel de gerenciamento de múltiplos projetos simultâneos de nível corporativo.

---

## 2. Tradução Operacional do Framework CKOS (Lente de Design)

As referências visuais devem ser percebidas sob a seguinte lente de transformação:

* **Sentir**: A transparência física do vidro fosco (*Calm Glass*) deve ser usada para sinalizar a profundidade do sistema (Z-index). Um widget com mais desfoque está "mais profundo" ou em estado de background; um cartão opaco e iluminado está ativo e na vanguarda do processamento, gerando segurança cognitiva imediata.
* **Pensar**: A estrutura de conexões curvas (*Spatial Canvas*) deve refletir a lógica exata de processamento dos agentes. O usuário não deve ver "efeitos visuais" bonitos que não correspondam aos conectores de arquivos reais, promovendo clareza analítica absoluta.
* **Criar**: Os componentes criados devem traduzir elementos visuais em contêineres de capacidades da IA. Um widget flutuante de música na referência vira o contêiner de controle de execução de uma tarefa de agente no CKOS.
* **Conectar**: O layout deve explicitar a conexão entre agentes e humanos. Os avatares de membros do time nas referências são transpostos para avatares ativos de subagentes (como Codex, Claude, PMO Auditor) com indicadores luminosos de status de comunicação.
* **Avaliar**: Os indicadores dinâmicos circulares e gráficos de barra concêntricos das referências serão adaptados para a exibição de ROI financeiro, probabilidade de sucesso e custo de execução de tokens em tempo real.
* **Elevar**: Os fundos com gradientes orgânicos e temas estilizados (*Samurai*, *Nature*) garantem que a interface do CKOS seja customizável e adaptável (*whitelabel*), mudando de tom conforme o perfil da empresa ou o estado emocional configurado pelo usuário para reduzir a fadiga do trabalho.
