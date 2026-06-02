---
title: "Neurodesign and Cognitive Load Rules"
file: "05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md"
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
purpose: "Estabelecer regras de neurodesign e gerenciamento de carga cognitiva aplicadas à interface do CKOS."
inputs:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md"
  - "000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md"
outputs:
  - "05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md"
framework: "Sentir -> Pensar -> Criar -> Conectar -> Avaliar -> Elevar"
edge_cases:
  - "Fadiga visual por excesso de brilho em interfaces escuras em ambientes de baixa iluminação"
  - "Interrupções visuais excessivas gerando frustração cognitiva no usuário"
integrations:
  - "antigravity_design_study"
prompts:
  - "Descrever princípios neurocognitivos de interface com base no comportamento de tomada de decisão do usuário."
metrics:
  - "Zero de código implementado"
  - "10 princípios pragmáticos de neurodesign aplicados aos fluxos de processamento de IA"
related_notes:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md"
tags:
  - "neurodesign"
  - "cognitive_load"
  - "visual_hierarchy"
  - "design_study"
---

# Neurodesign and Cognitive Load Rules

Esta nota de estudo documenta os princípios biológicos e cognitivos que devem orientar o design da interface do CKOS, minimizando o cansaço intelectual e maximizando a confiança e a clareza de ação do usuário humano.

---

## 1. Princípios Neurocognitivos de Interface (Neurodesign Rules)

O cérebro humano processa interfaces de software com base em rotas neurais evolutivas de detecção de ameaças, recompensa e economia de energia. A interface do CKOS deve respeitar os seguintes 10 princípios pragmáticos:

### A. Hick’s Law (Lei de Hick)
* **Princípio**: O tempo para tomar uma decisão aumenta com o número e a complexidade das opções apresentadas.
* **Regra no CKOS**: O Command Center nunca apresenta uma lista longa de ferramentas ou opções na inicialização. Na barra de comandos, o usuário vê apenas o campo de prompt e no máximo 3 pílulas de atalhos sugeridas dinamicamente pela relevância context-aware. Opções avançadas ou capabilities extras são ocultadas até que o usuário inicie a digitação ou chame o menu de ferramentas via barra `/`.

### B. Miller’s Law (Lei de Miller)
* **Princípio**: O cérebro humano médio consegue manter apenas cerca de 7 (mais ou menos 2) itens em sua memória de trabalho de curto prazo.
* **Regra no CKOS**: No Agent Activity Stream ou no Node Canvas, o número máximo de subagentes ou tarefas ativos sendo executados visivelmente em paralelo é limitado a 5. Se o workflow envolver mais agentes (ex: 15 subagentes em execução paralela), a interface agrupa-os visualmente em "Task Force Clusters" consolidados, exibindo apenas o progresso agregado. O usuário pode clicar no cluster para expandir se necessário.

### C. Progressive Disclosure (Divulgação Progressiva)
* **Princípio**: Apresentar informações de forma faseada, mostrando apenas os detalhes essenciais no primeiro nível e revelando dados complexos somente sob demanda.
* **Regra no CKOS**: No Evidence Map e nas timelines de execução, o sistema exibe apenas o status geral do nó (Sucesso/Erro) e o arquivo de saída gerado. A listagem de logs brutos de backend, tokens consumidos, lineage de dados e justificativas cognitivas do PMO Auditor permanecem colapsadas. O usuário as revela clicando na aba de expansão ("View Audit Trails"), evitando sobrecarregar a tela com dados secundários.

### D. Typographic Hierarchy (Hierarquia Tipográfica)
* **Princípio**: A variação de peso, tamanho e estilo da tipografia organiza visualmente a prioridade de leitura de informações complexas.
* **Regra no CKOS**: O CKOS utiliza duas famílias tipográficas contrastantes: a geométrica neo-grotesca (Inter/Outfit) em pesos Bold e Medium para títulos, comandos e métricas quantitativas de alta precisão (ROI, custos); e uma fonte serifada elegante de alta legibilidade (ex: Lora ou Playfair Display) para o ROI & Learning Panel e memórias aprendidas, sinalizando ao cérebro o estado de "leitura reflexiva" e reduzindo o estresse cognitivo da depuração técnica de código.

### E. Trust Signals for AI (Sinais de Confiança na IA)
* **Princípio**: O usuário precisa compreender os limites de confiabilidade da IA para confiar em suas decisões autônomas, reduzindo a ansiedade do uso de sistemas pretos.
* **Regra no CKOS**: Todo cartão de plano ou nó sugerido exibe um "Confidence Score" (de 0% a 100%) calculado dinamicamente com base em testes anteriores e conformidade regulatória. Se o score for menor que 80%, a UI adiciona um sinal visual estável e o botão de Approval Gate passa a exigir dupla confirmação explicativa (co-auditoria).

### F. Error Recovery Psychology (Psicologia de Recuperação de Erros)
* **Princípio**: Erros geram picos instantâneos de cortisol (estresse técnico). Apresentar um erro sem uma rota clara de ação de correção intensifica a frustração e a fadiga.
* **Regra no CKOS**: Quando uma tarefa de agente falha, o widget exibe o erro condensado em vermelho, mas anexa obrigatoriamente um botão de ação de reparo contextualizado chamado `Fix / Mitigate` no rodapé do cartão. Clicar no botão apresenta imediatamente a solução proposta sugerida pela IA e uma opção de Rollback seguro com um clique, transformando o erro em um fluxo operacional de solução.

### G. Cognitive Load Budget (Orçamento de Carga Cognitiva)
* **Princípio**: O usuário possui um limite diário de energia para processamento e atenção. Exceder esse orçamento visual gera desatenção e cliques acidentais catastróficos.
* **Regra no CKOS**: A interface desativa e desvanece (opacidade de 40%) qualquer componente inativo ou de histórico de logs passados. O uso do efeito de iluminação backlight sutil substitui pop-ups interruptivos e banners intrusivos. Em um mesmo instante temporal, apenas uma zona de atenção seletiva (onde o input é esperado ou o processo está ativamente rodando) emite brilho.

### H. Decision Fatigue Prevention (Prevenção de Fadiga de Decisão)
* **Princípio**: Exigir aprovações e intervenções constantes para micro-tarefas drena rapidamente a capacidade decisória do usuário.
* **Regra no CKOS**: O CKOS adota políticas de delegação segura. Para tarefas de baixo risco ou baixo custo (ex: formatação de arquivo, linting), o sistema executa de forma 100% autônoma e registra o resultado de forma passiva no painel de atividades. O portão de aprovação (*Approval Gate*) é acionado exclusivamente para decisões que envolvam riscos estruturais, custos financeiros altos ou mudanças em arquivos declarados protegidos no RAG.

### I. Fitts’s Law (Ergonomia de Alvos de Toque)
* **Princípio**: O tempo para alcançar um alvo é proporcional à sua distância e inversamente proporcional ao seu tamanho físico.
* **Regra no CKOS**: Todos os botões críticos (como aprovar, rejeitar ou fazer rollback de ações) e atalhos na Commandbar móvel devem possuir uma área mínima de clique/toque de `48px x 48px` para evitar cliques acidentais e reduzir a fricção motora do usuário.

### J. Gestalt Laws of Grouping (Ancoragem Visual de Proximidade)
* **Princípio**: A mente humana agrupa elementos visuais baseando-se em sua proximidade física, semelhança e alinhamento geométrico.
* **Regra no CKOS**: Métricas relacionadas a custos e ROI (créditos disponíveis, reservados e consumidos) são mantidas dentro do mesmo contêiner unificado de Calm Glass, prevenindo buscas oculares dispersas e acelerando a compreensão epistemológica do estado do projeto.

---

## 2. A Teoria do Respiro vs. Densidade (Pensar)

A densidade de dados deve ser adaptativa ao tipo de processamento exigido pelo usuário em cada fase da tarefa:

```
+-------------------------------------------------------------+
| FASE DE REFLEXÃO / IDEIA INICIAL (Respiro Máximo)           |
| [              Command Center / Empty State                ] |
| - Alta margem de respiro                                    |
| - Ausência de dados paralelos                               |
+-------------------------------------------------------------+
| FASE DE EXECUÇÃO / AUDITORIA (Alta Densidade)               |
| [ Grafo de Agentes ] [ Tabela de Custos ] [ Evidências Map ] |
| - Dados compactados próximos                                |
| - Timelines e métricas expressas                            |
+-------------------------------------------------------------+
```

### A. Quando Usar Respiro Máximo (Low Density)
* **Quando**: Na tela inicial de entrada de intenção (*Command Center* em estado *Idle*), onboarding do usuário e exibição de memórias aprendidas (*Learning UI*).
* **Por quê**: O espaço em branco abundante sinaliza ao córtex pré-frontal que não há ameaças ativas, promovendo um estado cognitivo propício para reflexão profunda, entrada de novas intenções e leitura confortável de documentações textuais longas.

### B. Quando Usar Alta Densidade de Dados (High Density)
* **Quando**: No *Node Canvas*, no *Evidence Map* e nas telas de detalhamento do plano de execução do PMO.
* **Por quê**: Quando o usuário está na fase de execução e auditoria, o cérebro precisa estabelecer correlações rápidas de causa e efeito entre o comportamento dos agentes e os artefatos gerados. Ter dados tabulares limpos, timelines estruturadas e gráficos de barras próximos reduz a necessidade do usuário alternar entre janelas (memória de trabalho de curto prazo poupada).
* **Como**: O respiro ainda é mantido internamente através de paddings microscópicos simétricos e grids bem organizados, garantindo que o cérebro agrupe os elementos por proximidade lógica (Leis da Gestalt).
