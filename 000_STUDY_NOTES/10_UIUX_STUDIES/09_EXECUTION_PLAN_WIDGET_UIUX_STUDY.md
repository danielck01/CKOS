---
title: "09 Execution Plan Widget UI/UX Study"
system_id: study_notes_execution_plan_widget_uiux_study_20260528
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
  - "000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md"
  - "04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md"
tags:
  - uiux
  - study
  - execution_plan
  - widget
  - neurodesign
---

# 09 Execution Plan Widget UI/UX Study

## 1. Propósito

Esta nota de estudo especifica os padrões de design UI/UX e neurodesign aplicados ao **Execution Plan Widget** (Widget de Plano de Execução) do CKOS. O objetivo é estabelecer diretrizes rígidas sobre como projetar visualmente a formulação, o acompanhamento, o controle de custos, a análise de riscos e a aprovação de planos de workflows operacionais executados por agentes autônomos, alinhando de forma síncrona a interface com o estado real do runtime no CKOS.

## 2. O Que Este Padrão Resolve

* **Incerteza Operacional**: Evita a ansiedade cognitiva do usuário ("o que a IA está fazendo com meus arquivos?") ao fornecer uma timeline em tempo real de tarefas divididas em etapas lógicas lineares.
* **Execuções Prematuras e Prejuízos**: Impede que agentes rodem tarefas complexas ou ferramentas de alto custo sem antes apresentar um orçamento estimado claro e obter consentimento explícito.
* **Sobrecarga de Informação**: Condensa logs extensos de compiladores ou execuções em micro-feedbacks e status agrupados, permitindo expansão opcional somente sob demanda de depuração.

## 3. O Que Não Pode Virar

* **Painel Decorativo Estático**: Não pode ser um elemento estético de "carregamento" baseado em cronômetros falsos ou animações em loop desconectadas do runtime.
* **Interface de Log Tradicional Incompreensível**: Não deve se tornar uma mera listagem de terminal Unix cinza que assusta o usuário não técnico.
* **Bypass de Validação**: Não pode permitir que uma tarefa progrida sem expor claramente seus riscos, dependências ou exigências de aprovação.

## 4. Relação com Runtime / Dashboard / Command Center / Node Canvas

* **Runtime (Event Bus)**: O widget assina os canais de atualização das tabelas `workflows` e `agent_runs` do runtime. Transições de estados de execução reais refletem no preenchimento visual e na renderização dos nós do widget.
* **Command Center**: O plano de execução surge acoplado abaixo do Command Center assim que uma intenção complexa é parseada e estruturada pelo `intent_router`.
* **Node Canvas**: O widget atua como uma projeção detalhada 1D de um nó de workflow que está rodando espacialmente no Node Canvas 2D.
* **Project Dashboard**: Alimenta a projeção do dashboard (`project_dashboard_projection`) com resumos de progresso histórico e contadores agregados de sucesso/falha de workflows executados.

## 5. Estados Visuais

O widget do plano de execução projeta de forma estrita as transições de estado oficiais controladas pela state machine de workflows do runtime, refletindo os seguintes 19 estados cognitivos e operacionais do CKOS:

* **`intent_received` (Intenção Recebida)**: O widget registra o recebimento do comando bruto do usuário e inicia a animação de ingress na interface.
* **`interpreting_intent` (Interpretando Intenção)**: O `intent_router` realiza o parsing e classificação taxonômica da intenção. Exibe um backlight pulsante roxo sutil na Commandbar.
* **`building_context_pack` (Construindo Pacote de Contexto)**: O `context_pack_builder` compila as referências necessárias do vault, indicando visualmente a indexação temporária dos nós de contexto.
* **`estimating_cost` (Estimando Custo)**: O `cost_guard` calcula o orçamento estimado em créditos CKC. Apresenta o indicador "Calculando despesas...".
* **`waiting_approval` (Aguardando Aprovação)**: O widget congela, a borda externa muda para um amarelo-ouro contínuo de alta intensidade, o backdrop blur do fundo adensa para 30px, e um botão de ação destacado é exibido para o Approval Gate.
* **`routing_agents` (Roteando Agentes)**: O planejador distribui subtarefas entre agentes especializados, indicando as linhas de transmissão (handoffs) entre avatares.
* **`running_agent_steps` (Executando Etapas do Agente)**: A execução ativa das tarefas pelo agente. A barra de progresso horizontal preenche-se suavemente com um gradiente azul-verde e logs mono-espaçados fluem na base com opacidade de 90%.
* **`waiting_tool` (Aguardando Ferramenta)**: O chip da ferramenta ativa (ex: Git, n8n, ChEMBL) acende na base em azul operacional brilhante para mostrar a latência externa de processamento da API/Tool.
* **`waiting_external_source` (Aguardando Fonte Externa)**: Pausa temporária aguardando retorno de coletores de terceiros ou inputs adicionais fora do sistema.
* **`metacognik_audit_running` (Auditoria Metacognik em Execução)**: O auditor de conformidade analisa em tempo real a segurança das ações executadas. O widget exibe um anel concêntrico azul-cobre pulsante ao redor do status.
* **`partial_success` (Sucesso Parcial)**: Algumas etapas do plano foram concluídas, mas outras falharam de forma contornável ou aguardam mitigação. O widget sinaliza com listras verdes e amarelas diagonais sutis.
* **`blocked_by_cost` (Bloqueado por Custo)**: O widget muda a pílula de saldo para vermelho sólido e desabilita o início/continuação do plano, exibindo o aviso de limite de créditos excedido.
* **`blocked_by_permission` (Bloqueado por Permissão)**: Ação suspensa por restrição de políticas RBAC/ABAC do usuário ativo, exibindo um badge vermelho de acesso negado.
* **`blocked_by_missing_context` (Bloqueado por Contexto)**: Interrupção visual por ausência de dados vitais de briefing. O widget destaca o nó de dados faltante com uma borda amarela pontilhada.
* **`completed_with_warnings` (Concluído com Avisos)**: O workflow finalizou, mas a auditoria de IA reportou desvios secundários. Exibe um badge amarelo "Completed with Warnings".
* **`ready_for_review` (Pronto para Revisão)**: O workflow gerou o output final e aguarda homologação humana. O botão "Review Artifacts" brilha em Calma Glass verde-azul.
* **`rollback_available` (Reversão Disponível)**: O plano foi executado com sucesso e o runtime registrou pontos de restauração. Um botão destacado de "Rollback" fica disponível.
* **`failed_recoverable` (Falha Recuperável)**: O widget exibe o erro e apresenta opções para re-execução, mitigação ou modificação de parâmetros de entrada.
* **`failed_critical` (Falha Crítica)**: Interrompe o workflow imediatamente. O widget exibe a borda em vermelho sólido, travando a timeline e expondo o trace detalhado de erro.

O Execution Plan Widget é projetado para agregar e expor de forma holística: o plano detalhado, as etapas lineares e não-lineares, os agentes responsáveis pelas tarefas, as linhas de handoffs (passagens de controle), o custo estimado da run, os créditos reservados no saldo, a matriz de riscos identificados, as âncoras de evidências justificadoras, os approvals gates necessários, os outputs parciais/finais e os comandos de rollback/reversibilidade quando disponíveis.

## 6. Inputs

* **Workflow Blueprint**: O JSON estruturado do workflow gerado pelo `workflow_engine`, contendo o grafo de tarefas, subagentes responsáveis e dependências físicas.
* **Estimated Cost Configuration**: Os metadados de créditos estimados (`cost_estimate`) derivados do pre-check do `cost_guard`.
* **Metacognik Risk Audit**: Os avisos textuais e nível de risco preliminar computados para as tarefas ativas do plano.
* **Active Execution Events**: Fluxo de streaming de eventos de progresso e tokens consumidos vindos do runtime (`PartialOutputProduced`).

## 7. Outputs

* **Execution Status (Projeção Visual)**: A representação visual síncrona da timeline de tarefas ativas e barras de progresso.
* **Budget Metrics**: Exibição em tempo real do custo estimado vs créditos consumidos acumulados da execução atual.
* **Action Command Triggers**: Eventos de interação humana emitidos pelo usuário a partir do widget, tais como solicitações de pausa, aprovação ou reversão.
* **Error Log Context**: Contexto de erro detalhado enviado ao painel de explicação ou ao formulário de suporte caso ocorra falha.

## 8. Riscos

* **Entropia de Interface (Flickering)**: Mudanças de estado rápidas em subsegundos podem causar piscar de luzes na tela, gerando estresse cognitivo.
  * *Mitigação*: Implementar transições de opacidade e cores com interpolação suave (mínimo de 150ms) e debounce lógico para estados intermediários curtos.
* **Desconexão de Execução Assíncrona**: O usuário fechar o widget de execução achando que a ação foi cancelada no backend.
  * *Mitigação*: Manter um indicador visual discreto na barra de status persistente do sistema caso haja workflows ativos rodando em segundo plano.

## 9. Regras de ROI

* **Indicador de ROI Previsto**: O widget deve apresentar no planejamento a estimativa de tempo e esforço manual economizados ao rodar o workflow de agentes (ex: `ROI Estimado: +85% Eficiência | -4h de Trabalho`).
* **Validação de ROI de Execução**: Após a conclusão bem-sucedida, o widget exibe os aprendizados e resultados de ROI extraídos exclusivamente de projeções e tabelas de banco de dados do runtime (tais como `roi_snapshot_projection`, `roi_outcomes`, `roi_evidence_links` e `evidence_items`), comprovando o valor retido. O arquivo `ck_memory.md` serve unicamente como documentação e memória de apoio conceitual de projeto, nunca sendo lido ou parseado pelo runtime ou pela interface visual em produção.

## 10. Regras de Custo/Créditos

> **Regra Rígida**: Nenhum plano de execução pode aparecer na tela ou iniciar sem apresentar explicitamente o custo estimado acumulado, o limite de créditos do projeto e o saldo atual disponível.

* O widget exibe de forma proeminente o indicador de custos no formato: `Est. Custo: $0.15 CKC` (ou créditos correspondentes).
* Se o custo de runtime estimado pelo planejador exceder o teto estipulado pela política orçamentária do projeto (`project_budgets.soft_limit_usd`), o texto do contador de créditos muda para laranja, notificando a restrição.
* Se ultrapassar o teto rígido (`limit_usd`), a cor do texto muda para vermelho sólido e desabilita fisicamente o botão de início, forçando o acionamento do portão de aprovação de orçamento extra.

## 11. Regras de Aprovação Humana

* Se qualquer tarefa no plano contiver um nível de risco avaliado pelo Metacognik como `High` ou envolver ações com reversibilidade marcada como `False` (irreversível), o widget exibe obrigatoriamente um ícone de cadeado dourado ao lado da tarefa.
* A progressão do workflow é congelada visualmente antes da execução daquela tarefa de risco, forçando o estado visual do widget a transitar para `Waiting Approval` até que o evento `ApprovalSubmitted` correspondente seja registrado.

## 12. Regras de Evidência

* Toda tarefa listada na timeline do plano de execução deve conter um atalho do tipo âncora ("link de evidência") para o contexto de briefing ou documentação que sustenta a sua necessidade (ex: `Baseado em: OAB_Rule_4.pdf`).
* O widget impede visualmente que tarefas flutuem "sem base justificável" na timeline do projeto.

## 13. Mobile Behavior

* **Layout de Coluna Única**: A timeline de tarefas é renderizada verticalmente, ocupando a metade inferior da tela do dispositivo móvel para facilitar o toque de controle ergonômico com o polegar.
* **Gestos**:
  * Deslizar lateralmente (swipe) em um cartão de tarefa ativa expande os logs mono-espaçados condensados correspondentes da execução.
  * Toques em botões de controle (Pause/Play) possuem tamanho mínimo de `48px x 48px` para evitar toques acidentais em áreas vizinhas.
* **Safe Areas**: O rodapé do widget respeita a área segura do teclado virtual do celular para prevenir sobreposições durante inputs de texto adicionais.

## 14. Web Behavior

* **Layout Multi-Coluna Split**: Exibe a timeline densa na lateral esquerda, o visualizador do editor de código ou diff de arquivos no painel central, e o terminal com streaming de logs do agente atômico ativo na lateral direita.
* **Hover State**: Passar o cursor sobre uma tarefa do plano ilumina as curvas de dependência associadas a ela no Node Canvas espacial.

## 15. Anti-Patterns

* **Progresso Linear Cosmético**: Utilizar uma barra de progresso fictícia que se move sozinha sem mapeamento direto de eventos do bus de runtime (Ex: barras que sobem até 99% e travam por falta de resposta real).
* **Logs Escondidos permanentemente**: Impedir que o usuário acesse os logs técnicos de erro caso ocorra falha (ex: exibir apenas uma mensagem genérica "Ocorreu um erro" sem o trace).
* **Ausência de Indicador de Custo**: Permitir que o usuário inicie um plano sem apresentar a estimativa financeira preventiva de tokens consumidos.

## 16. Acceptance Criteria

* O widget deve ler e projetar exclusivamente os estados agregados das projeções oficiais `agent_activity_projection` e `node_status_projection`.
* A estimativa de custo de créditos e a classificação de risco devem ser exibidas de forma clara e legível no planejamento do widget antes da liberação do acionamento físico de execução.
* A transição visual para o estado de pausa e congelamento em `Waiting Approval` deve ocorrer imediatamente após o recebimento do evento `ApprovalRequested` de runtime.

## 17. Próximas Perguntas para Founder/PMO

* Devemos permitir a edição dinâmica de etapas do plano de execução (adicionar ou remover tarefas manuais) diretamente no widget enquanto a execução está em andamento, ou qualquer alteração de plano exige abortar a run atual e formular um novo workflow?
* Qual deve ser o nível de granularidade dos logs de agentes exibidos no widget mobile para não prejudicar o desempenho de renderização e memória sob conexões de dados limitadas?
