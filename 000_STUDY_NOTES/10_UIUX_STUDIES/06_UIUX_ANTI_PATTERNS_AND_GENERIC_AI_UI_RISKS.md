---
title: "UI/UX Anti-Patterns and Generic AI UI Risks"
file: "06_UIUX_ANTI_PATTERNS_AND_GENERIC_AI_UI_RISKS.md"
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
purpose: "Mapear os principais anti-padrões e riscos visuais na interface do CKOS para evitar layouts corporativos genéricos."
inputs:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md"
  - "000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md"
outputs:
  - "06_UIUX_ANTI_PATTERNS_AND_GENERIC_AI_UI_RISKS.md"
framework: "Sentir -> Pensar -> Criar -> Conectar -> Avaliar -> Elevar"
edge_cases:
  - "Ocultação de logs reais em prol de uma interface excessivamente polida e sem dados de verdade"
  - "Uso de cores de status sem consistência semântica com o runtime subjacente"
integrations:
  - "antigravity_design_study"
prompts:
  - "Listar desvios de design e anti-padrões em sistemas operacionais de IA."
metrics:
  - "Zero de código implementado"
  - "10 anti-padrões documentados com alternativas corretivas claras"
related_notes:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md"
tags:
  - "anti_patterns"
  - "risks"
  - "generic_saas"
  - "design_study"
---

# UI/UX Anti-Patterns and Generic AI UI Risks

Esta nota de estudo cataloga as práticas de design visual e de interação que o CKOS deve evitar a todo custo para prevenir a regressão a layouts SaaS corporativos genéricos de mercado, que mascaram a complexidade técnica e pecam na transparência do processamento de agentes de IA.

---

## 1. Catálogo de Anti-padrões de Interface

### A. O Dashboard Fake (Painel Decorativo Estático)
* **O que é**: Painéis com gráficos genéricos ou contadores estatísticos estáticos que não possuem atualização real, não mapeiam ações atômicas do runtime dos agentes e não permitem que o usuário clique em um dado para auditar a evidência lógica que o gerou.
* **Alternativa CKOS**: Todos os cartões de status e métricas devem ser interativos. Ao clicar em um indicador de progresso de tarefa, a interface expõe as ações exatas executadas no backend e os arquivos envolvidos no *Evidence Map*.

### B. Glassmorphism Excessivo / Decorativo
* **O que é**: Aplicação indiscriminada de transparências, blur e contornos brilhantes em todos os elementos da tela apenas por apelo estético, sem critério de hierarquia ou Z-index. Isso destrói o contraste visual e gera fadiga ocular rápida.
* **Alternativa CKOS**: A transparência de vidro é usada apenas em camadas de background inativas ou em commandbars sobrepostas temporariamente. Cartões operacionais ativos de dados permanecem sólidos e legíveis.

### C. A IA Invisível / Caixa-Preta
* **O que é**: Deixar o usuário esperando em uma tela com um spinner de carregamento genérico enquanto a IA processa o prompt em segundo plano por dezenas de segundos sem demonstrar o andamento da tarefa.
* **Alternativa CKOS**: Utilizar o *Execution Plan Widget* para exibir a linha exata de processamento (logs rápidos formatados de forma condensada, arquivos criados e tempo decorrido), fornecendo transparência total da atividade.

### D. Invisibilidade Financeira e Operacional (Omissão de Custo e ROI)
* **O que é**: Esconder os custos de tokens e o consumo de créditos de execução em sub-páginas escondidas de configurações. Isso induz a gastos inesperados.
* **Alternativa CKOS**: A exibição dos créditos consumidos e do ROI de eficiência é um elemento nativo de cabeçalho e rodapé em todos os widgets operacionais que iniciam o processamento de agentes.

### E. O "Mobile Espremido"
* **O que é**: Reduzir grids densos de desktop diretamente para a largura de telas móveis verticalmente, resultando em letras minúsculas, tabelas com colunas ilegíveis e botões espremidos nas extremidades.
* **Alternativa CKOS**: Compressão e transposição ergonômica de layouts. Tabelas viram pilhas verticais de cartões de toque e grafos de canvas complexos convertem-se em fluxogramas de lista lineares.

### F. Motion Cosmética Excessiva (Animações Sem Função)
* **O que é**: Inserir animações complexas tridimensionais, transições longas ou rotações de elementos apenas para chamar atenção do usuário, atrasando a velocidade de navegação técnica e sobrecarregando a CPU do dispositivo.
* **Alternativa CKOS**: As animações devem durar no máximo `150ms` e devem servir estritamente como feedback de mudança de estado físico (affordance) ou orientação espacial.

### G. Aprovação Cega (Approval sem Contexto)
* **O que é**: Apresentar um botão "Aprovar" em modais de pop-up isolados que cobrem toda a tela sem permitir que o usuário revise o código gerado, os custos estimados ou os riscos potenciais associados de forma contígua.
* **Alternativa CKOS**: Os *Approval Gates* são contêineres acoplados à área de trabalho, permitindo a exibição lado a lado do código candidado a modificação e do painel de riscos e ROI do PMO Auditor.

### H. Perda de Acessibilidade sob Temas Personalizados
* **O que é**: Adoção de paletas de cores decorativas que não respeitam a taxa mínima de contraste exigida pela WCAG para leitura de textos em interfaces profissionais.
* **Alternativa CKOS**: Todo tema personalizado (*whitelabel*) deve ser submetido a um validador automático de contraste de cor no design system antes de ser aplicado na interface de trabalho.

### I. Empty State Decorativo
* **O que é**: Telas vazias sem atividades ativas que exibem apenas uma ilustração bonitinha 3D ou frase poética inspiradora, sem fornecer nenhuma ação imediata, atalhos contextuais ou histórico de atividades recentes para que o usuário saiba como progredir.
* **Alternativa CKOS**: Todo *Empty State* no CKOS deve ser uma superfície ativa de sugestões. Ele exibe um prompt-input minimalista e uma lista dinâmica de atalhos rápidos das últimas ações executadas, sugestões de intents baseadas na fase do projeto ou links diretos para carregar arquivos de contexto.

### J. Aprovação Sem Consequência Clara
* **O que é**: Solicitar que o usuário aprove um plano ou etapa de execução do agente através de uma mensagem curta como "Você aprova a execução do plano?", sem detalhar de forma clara e visível quais arquivos serão gravados/excluídos fisicamente no disco, qual será o impacto financeiro exato (créditos) e se a ação é reversível ou irreversível.
* **Alternativa CKOS**: Todo portão de decisão (*Approval Gate*) deve conter a seção "Impactos do Commit". Nela são listados os caminhos exatos dos arquivos marcados como `[NEW]`, `[MODIFY]` ou `[DELETE]` com diffs coloridos, o custo máximo do token commit e um badge de indicação de reversibilidade (`reversible` ou `destructive/irreversible`).
