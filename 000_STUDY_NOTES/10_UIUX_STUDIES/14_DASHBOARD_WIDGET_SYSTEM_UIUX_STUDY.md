---
title: "14 Dashboard Widget System UI/UX Study"
system_id: study_notes_dashboard_widget_system_uiux_study_20260528
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
  - "000_STUDY_NOTES/10_UIUX_STUDIES/03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/11_COST_CREDITS_AND_ROI_AWARE_UX_STUDY.md"
tags:
  - uiux
  - study
  - dashboard
  - widgets
  - neurodesign
---

# 14 Dashboard Widget System UI/UX Study

## 1. Propósito

Esta nota de estudo especifica os padrões de design UI/UX e neurodesign para o **Dashboard Widget System** (Sistema de Widgets do Dashboard) do CKOS. O objetivo é estabelecer diretrizes conceituais sobre como estruturar a exibição modular de métricas operacionais, saldos de créditos, status de execução e históricos de auditoria, garantindo que a disposição visual de cada elemento apoie diretamente a tomada de decisão ágil e sem sobrecarga cognitiva.

## 2. O Que Este Padrão Resolve

* **Disposição Caótica de Informação**: Define um sistema rígido de posicionamento e proporção para os cartões de informação, evitando layouts desordenados.
* **Falta de Contexto Financeiro e Técnico**: Garante que cada widget exponha seu custo e seu impacto em ROI de forma unificada e visível.
* **Perda de Rastreabilidade Operacional**: Permite que o usuário trace a origem dos dados exibidos no widget até as tabelas reais do banco de dados (`cost_projection`, `roi_snapshot_projection`, etc.).

## 3. O Que Não Pode Virar

* **Mosaico Estático Decorativo**: Não pode ser composto por cartões meramente estéticos que mostram gráficos fictícios ou de carregamento sem conexão de rede.
* **Gargalo de Performance**: O carregamento de múltiplos widgets na tela não deve travar a thread de processamento da UI; o consumo de dados deve ser assíncrono e colapsado sob demanda.
* **Bypass de Regras de Negócios**: Os widgets não podem contornar as restrições de RBAC/ABAC; dados confidenciais de faturamento (`cost_ledger`) só devem ser acessados por usuários com permissões de administrador.

## 4. Relação com Runtime / Dashboard / Command Center / Node Canvas

* **Projeções do Runtime**: Os widgets assinam canais de CQRS e renderizam exclusivamente dados lidos das tabelas `credit_wallets`, `roi_snapshot_projection` e `cost_projection`.
* **Command Center**: O usuário pode ativar, desativar ou reordenar widgets digitando comandos de layout específicos (ex: `/dashboard hide cost`).
* **Node Canvas**: Qualquer nó de execução ativa no canvas 2D pode ser "fixado" no dashboard como um widget temporário de acompanhamento 1D.

## 5. Estrutura e Layout do Sistema de Widgets

* **Grelha Dinâmica (Grid)**: Organização dos widgets em uma estrutura de colunas flexíveis (1 a 4 colunas dependendo do dispositivo).
* **Estados de Colapso (Micro-views vs. Expanded)**:
  - *Micro-view*: Exibe apenas o status em formato de ícone, o título e a métrica principal (ex: saldo atual).
  - *Expanded view*: Abre um modal ou expande o cartão para baixo, revelando logs de execução, Diffs de arquivos, ou a lista de referências documentais associadas.
* **Carrossel de Widgets de Projetos**: Permite alternar entre diferentes painéis de workspaces sem perder o contexto operacional ativo.

## 6. Regras de Neurodesign e Carga Cognitiva

* **Hick's Law Aplicada**: Limitar a no máximo 6 o número de widgets ativos por página de dashboard principal.
* **Divulgação Progressiva**: Informações de latência profunda e traces de erro permanecem ocultos por padrão, exigindo um clique explícito em "Ver Logs Técnicos" para visualização.
* **Codificação de Cores Epistêmica**: Alinhamento estrito com os níveis de confiança (verde-azul para alta confiança, vermelho-laranja para falha ou baixa confiança).

## 7. Relação com Dimensões CKOS

* **Execution**: Os widgets refletem instantaneamente transições da máquina de estados do runtime (como `running_agent_steps`, `waiting_approval`).
* **Cost**: O widget de créditos exibe a divisão clara entre créditos disponíveis (`balance_available`) e reservados (`balance_reserved`).
* **ROI**: O widget de ROI exibe gráficos simplificados de economia de tempo baseados em `roi_snapshot_projection`.
* **Learning**: O widget de histórico registra os aprendizados das últimas runs executadas, permitindo a retroalimentação semântica do projeto.

## 8. Comportamento Web vs. Mobile

* **Web**:
  - Exibição em grade multi-colunas paralela.
  - Hover states revelam atalhos de configuração rápidos no canto superior de cada widget.
* **Mobile**:
  - Layout vertical de coluna única com scroll suave.
  - Tamanho mínimo de toque ergonômico para ações internas (`48px x 48px`).
  - Swiping lateral para rotacionar entre widgets de diferentes categorias.

## 9. Anti-Patterns

* **Métricas Desconexas**: Exibir valores de uso que não podem ser auditados ou rastreados até os registros físicos correspondentes.
* **Falta de Estado de Latência**: Deixar o widget em branco ou estático sem exibir um skeleton de carregamento se o tempo de resposta da API exceder 300ms.

## 10. Acceptance Criteria

* O sistema de widgets deve consumir dados exclusivamente de projeções ativas no banco de dados e bus de eventos.
* Todos os widgets devem exibir seus respectivos estados de erro de forma limpa, fornecendo opções de re-tentativa e atalhos para os logs técnicos correspondentes.
* Alterações de ordenação na UI devem disparar eventos de layout persistidos nas preferências do usuário.
