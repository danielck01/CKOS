---
title: "15 Command Center Operational UX Study"
system_id: study_notes_command_center_operational_ux_study_20260528
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
  - "000_STUDY_NOTES/10_UIUX_STUDIES/02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/10_INTENT_CLARIFIER_AND_SMART_QUESTIONS_UIUX_STUDY.md"
  - "04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md"
tags:
  - uiux
  - study
  - command_center
  - commandbar
  - neurodesign
---

# 15 Command Center Operational UX Study

## 1. Propósito

Esta nota de estudo especifica os padrões de design UI/UX e neurodesign para o **Command Center** (Centro de Comando) do CKOS. O objetivo é definir as regras conceituais de digitação, autocomplete de comandos, sugestões preditivas e o fluxo de refinamento tátil, permitindo que a Commandbar atue como o principal ponto de controle operacional de intenções do usuário.

## 2. O Que Este Padrão Resolve

* **Complexidade de Navegação**: Substitui múltiplos menus e botões escondidos por uma Commandbar central acessível por atalhos rápidos (`Ctrl + K` ou `Cmd + K`).
* **Ambiguidade de Sintaxe**: Orienta o usuário em tempo real na formulação de comandos estruturados por meio de sugestões de taxonomia claras.
* **Fricção de Disparo**: Permite disparar workflows de múltiplos subagentes e consultas em menos de 3 segundos usando prefixos padrão de atalhos.

## 3. O Que Não Pode Virar

* **Chat de Conversa Comum**: Não deve se comportar como um clone de chat web onde o usuário digita longos textos e aguarda parágrafos informativos inúteis.
* **Barra de Pesquisa Simples**: Não pode ser limitada a buscar apenas termos no vault de documentos sem capacidade de disparar ações de runtime.
* **Painel Poluído**: Evita exibir dezenas de sugestões irrelevantes que cobrem a área central da interface de trabalho ativa.

## 4. Relação com Runtime / Dashboard / Command Center / Node Canvas

* **Command Center Architecture**: Alinha-se diretamente com as especificações do documento canônico 15. A interface atua como a projeção visual da Commandbar.
* **Runtime Event Bus**: Toda digitação finalizada emite eventos `IntentSubmitted` direcionados ao `intent_router` do runtime.
* **Node Canvas**: Comandos digitados na Commandbar (como `/canvas link NodeA NodeB`) interagem espacialmente com o Node Canvas 2D.

## 5. Padrões Operacionais de Entrada (Commandbar UX)

* **Prefixo de Comando `/` (Slash Commands)**: A Commandbar suporta atalhos específicos mapeados para a taxonomia de intenções do CKOS, divididos em 22 comandos operacionais:
  * *Strategy & Diagnosis*: `/diagnosis` (efetua diagnóstico estratégico do projeto).
  * *Briefing & Context*: `/briefing` (cria ou edita o briefing e context pack).
  * *Research & Collection*: `/research` (inicia pesquisas de dados externos) e `/competitors` (varre concorrentes e benchmarks).
  * *Nodes & Workflows*: `/nodes` (exibe status e foca nós no canvas) e `/workflow` (instancia planos de execução).
  * *Agents & Squads*: `/agents` (lista e gerencia subagentes em execução).
  * *Production & Artifacts*: `/proposal` (gera proposta de projeto) e `/artifact` (materializa entregáveis ou prompt packs).
  * *Decisions & Approvals*: `/approve` (decide sobre approvals pendentes).
  * *ROI, Cost & Usage*: `/roi` (relatórios de ROI e eficácia), `/cost` (consome orçamentos de run) e `/credits` (saldo de créditos do workspace).
  * *Feedback & Support*: `/feedback` (envia avaliações de outputs) e `/support` (abre tickets de suporte).
  * *Memory, Evidence & Explainability*: `/explain` (detalha decisões e erros), `/audit` (exibe logs de Metacognik), `/memory` (chama freshness de memórias do RAG), `/evidence` (explora fontes de dados do RAG) e `/replay` (reproduz runs anteriores).
  * *System & Billing Ops*: `/admin` (tarefas de governança de sistema) e `/billing` (faturamento corporativo).
* **Context Anchors (`@` para Ficheiros e Contexto)**: Permite referenciar arquivos ou objetos específicos diretamente na commandbar (ex: `/explain @src/auth.ts` ou `/artifact create proposal @briefing_v2`).
* **Autocomplete Dinâmico e Tolerante a Falhas**: Heurística preditiva que antecipa o próximo argumento com base na seção ativa do usuário e no histórico do projeto, sugerindo o preenchimento automático em menos de 50ms.

## 6. As 10 Famílias de Intenção e as Menções a Agentes (Mentions)

Para evitar desvios ou chamadas sem trace no runtime, a interface do Command Center classifica e apresenta de forma estruturada toda entrada em 10 famílias de intenção e gerencia as menções a papéis operacionais:

* **As 10 Famílias de Intenção**:
  1. *Strategy & Diagnosis*: Foco em lacunas e hipóteses (ex: chips de diagnóstico visual).
  2. *Briefing & Context*: Captura de contexto e resolução de gaps.
  3. *Research & Collection*: Coleta em crawlers e bases médicas/científicas.
  4. *Nodes & Workflows*: Criação, visualização e conexão física de grafos 2D.
  5. *Agents & Squads*: Alocação e handoff de subagentes.
  6. *Production & Artifacts*: Geração e versionamento de entregáveis.
  7. *Decisions & Approvals*: Portões de decisão e controle humano.
  8. *ROI, Cost & Usage*: Rastreabilidade de créditos e valor do projeto.
  9. *Feedback & Support*: Sinais de qualidade e chamadas de operador.
  10. *Memory, Evidence & Explainability*: Traces de lineage e fresh de RAG.
* **Sistema de Menções (`@` para Agentes e Roles)**: Permite direcionar comandos ou solicitar explicações de agentes específicos:
  - `@nick`: Interface conversacional primária (sempre disponível para explicações de interface).
  - `@cognik`: Diagnósticos e análises epistêmicas de hipóteses.
  - `@metacognik`: Auditoria e riscos (não executa ações diretas; exibe traces de auditoria ativa).
  - `@pmo_ckos`: Planejamento de timeline, recomendação de tarefas e alocação de squads.
  - `@qa_lead`: Homologação de qualidade técnica de código ou textos.
  - `@builder_lead`: Implementação e controle de arquitetura física de software.
  - `@datta`: Controle do cost ledger e acesso a dados estruturados.
  - `@ops`: Deploys, automações n8n e collectors de APIs externas.
  - `@campaign`: Agenciamento de distribuição e conteúdo.
* **Regra de Handoff Conversacional**: O acionamento de um agente de domínio ativa visualmente o conector de handoff correspondente no Node Canvas, sinalizando graficamente a transição de responsabilidade.

## 7. Fluxo de Clarificação de Intenção e Feedback Visual

* **Backlight Semântico**: A Commandbar altera a tonalidade da sua borda refletindo o estado de processamento:
  - *Roxo pulsante*: Analisando a intenção e coletando dependências.
  - *Azul contínuo*: Aguardando seleção de parâmetros no painel sugestivo.
  - *Verde*: Intenção clara, pronta para execução.
* **Gaveta de Smart Questions**: Quando o clarificador de intenção detecta contradições, expande uma área no terço inferior com as perguntas estruturadas.

## 8. Relação com Dimensões CKOS

* **Intention**: O Command Center captura e mapeia a intenção do usuário para o `intent_router`.
* **Execution**: Dispara pipelines e exibe micro-feedbacks do progresso do agente no rodapé da Commandbar.
* **Cost**: Apresenta preventivamente o orçamento financeiro estimado da run durante a digitação de parâmetros.

## 9. Comportamento Web vs. Mobile

* **Web**:
  - Centralizado no topo da tela com Z-index elevado.
  - Atalhos de teclado amplos para navegação sem mouse.
* **Mobile**:
  - Fixado na base da tela, posicionado ergonomicamente acima do teclado virtual.
  - Carrossel horizontal de comandos rápidos de deslizar com o polegar.

## 10. Anti-Patterns

* **Lançar Ação Sem Confirmação de Custo**: Permitir comandos que executam modelos de IA comerciais de alto custo sem exibir o disclaimer de despesa estimada.
* **Esconder Resultados de Autocomplete**: Não exibir dicas de preenchimento quando o usuário comete pequenos erros de digitação (ausência de tolerância a falhas).

## 11. Acceptance Criteria

* Toda entrada enviada pela Commandbar deve resultar na geração de uma intenção estruturada enviada ao event bus.
* A navegação de sugestões na barra deve ser completamente operável via teclado (teclas direcionais e enter).
* O Command Center deve recolher visualmente quando o usuário clica fora da sua área ativa ou pressiona a tecla `Esc`.
