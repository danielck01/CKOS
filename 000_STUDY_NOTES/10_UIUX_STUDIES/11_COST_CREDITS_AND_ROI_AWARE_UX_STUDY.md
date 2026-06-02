---
title: "11 Cost, Credits and ROI-Aware UX Study"
system_id: study_notes_cost_credits_roi_aware_ux_study_20260528
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
  - "06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md"
tags:
  - uiux
  - study
  - billing
  - credits
  - roi
  - neurodesign
---

# 11 Cost, Credits and ROI-Aware UX Study

## 1. Propósito

Esta nota de estudo especifica os padrões de design UI/UX e neurodesign para a experiência do usuário orientada a **Custos, Créditos e Retorno sobre Investimento (ROI)** no CKOS. Ela define como traduzir a arquitetura comercial de faturamento e o consumo de créditos de runtime em elementos de interface transparentes, mitigando a fricção de cobranças surpresa e comprovando o valor operacional gerado pelo sistema operacional de agentes.

## 2. O Que Este Padrão Resolve

* **Opacidade Financeira**: Elimina a falta de clareza sobre o consumo de tokens e custos de infraestrutura em plataformas AI-first.
* **Estouro Acidental de Orçamento**: Previne gastos excessivos sob processamento concorrente através de representações visuais claras do padrão de pré-reserva de créditos.
* **Justificativa de Valor (ROI)**: Comprova visualmente se as execuções de subagentes e ferramentas comerciais geraram economia real de tempo e recursos operacionais em relação aos métodos de trabalho manuais tradicionais.

## 3. O Que Não Pode Virar

* **Dashboard de Checkout Comercial Tradicional**: Não pode se comportar como um carrinho de e-commerce decorativo ou popups invasivos de upsell que interrompem o fluxo de trabalho técnico.
* **Visualizador Passivo de Relatórios Mensais**: Não deve ser uma página estática de extratos em PDF gerada pós-fato sem feedback imediato durante as execuções ativas.
* **Indicador Desconectado do Runtime**: Não pode inventar ou recalcular saldos locais de créditos ignorando as projeções oficiais baseadas no CQRS do runtime.

## 4. Relação com Runtime / Dashboard / Command Center / Node Canvas

* **Fontes de Dados de Runtime**: A UI do CKOS consome dados exclusivamente das projeções e tabelas oficiais do runtime, sendo proibido tratar arquivos markdown de documentação (como `ck_memory.md`) como fonte viva. A interface lê dados de:
  - `roi_snapshot_projection` e `cost_projection` (para métricas e snapshots atualizados);
  - `roi_hypotheses`, `roi_outcomes`, `roi_evidence_links` e `evidence_items` (para dados e links de ROI/evidências);
  - `cost_ledger` (para custos internos de runtime, restritos a administradores);
  - `credit_wallets`, `credit_reservations` e `credit_transactions` (para o fluxo de créditos do cliente);
  - `usage_events` e `billing_events` (para eventos de consumo e faturamento real).
* **Runtime (Cost Guard & Quota Engine)**: A interface monitora de forma síncrona a `cost_projection` e o estado das wallets. O `quota_engine` bloqueia preventivamente execuções na UI se o saldo disponível for insuficiente.
* **Command Center**: Apresenta no canto superior direito uma pílula flutuante estilizada contendo o status de consumo do projeto atual (`Est. Custo: $0.15 CKC`).
* **Node Canvas**: Cada nó de execução ou subagente em progresso renderiza um micro-badge dinâmico contendo o consumo em tempo real daquela run específica.
* **Project Dashboard**: Consolida os gráficos de ROI histórico e eficiência acumulada (comparando horas salvas e custos de infraestrutura).

## 5. Estados Visuais

O sistema de créditos e billing projeta visualmente as restrições orçamentárias e de planos do runtime, reforçando visualmente os seguintes elementos:
* **Créditos Disponíveis**: O saldo operacional disponível do cliente (`balance_available` da `credit_wallets`).
* **Créditos Reservados**: Parcela temporariamente retida para workflows ativos rodando em segundo plano (`balance_reserved` de `credit_reservations`), sinalizando indisponibilidade para novas ações.
* **Créditos Consumidos**: Histórico de consumo debitado via `usage_events` e transações registradas.
* **Custo Estimado**: Projeção de gastos pré-execução obtida de `CostEstimateRequested`.
* **Custo Real**: O valor final debitado após a conclusão e aprovação da atividade.
* **Custos Granulares**: Detalhamento do custo por agente (`agent_costs`), custo por modelo de IA (`model_costs`) e custo por collector (`collector_costs`).
* **Métricas de ROI**: Indicação de ROI estimado vs. realizado, score de confiança (`confidence`), hipóteses assumidas (`assumptions`), restrições operacionais (`limitations`) e nível de cobertura de evidências (`evidence_coverage`).

O comportamento dos estados visuais segue as restrições de planos e quotas do runtime:
* **Active Balance (Saldo Operacional)**: A pílula de créditos exibe o saldo com tipografia limpa em verde ou cinza claro (`balance_available`).
* **Overage Warning (Aviso de Limite - Soft Limit)**: Quando o consumo atinge 80% da quota do plano (`soft_limit_percent`), a pílula assume uma tonalidade laranja pulsante suave. O placeholder do Command Center ativa o chip sugestivo "/billing".
* **Quota Blocked (Bloqueio de Saldo - Hard Limit)**: A pílula de créditos muda para vermelho sólido. Todas as ações de execução são desabilitadas na UI. O widget do plano de execução exibe o status de erro `Blocked by Cost` e um botão destacado "Upgrade Plan" ou "Aprove Extra Budget".
* **Credit Reservation Active (Reserva de Créditos)**: No extrato do projeto, a parcela de créditos vinculada a workflows ativos rodando em segundo plano é colorida com uma máscara azul-cobre translúcida (`balance_reserved`), sinalizando visualmente que aqueles créditos estão retidos temporariamente e indisponíveis para novas ações.

## 6. Inputs

* **Credit Wallet Projections**: Dados do modelo `credit_wallets` contendo os campos `balance_available` e `balance_reserved`, e projeções de `roi_snapshot_projection`.
* **Rate Configurations**: O valor em créditos por unidade de recurso lido de `credit_rate_config` (ex: créditos por run de subagente ou chamada de API).
* **Quota Metrics**: Status de limites mensais de storage, collector runs e chamadas de modelos permitidos para o plano ativo da organização.
* **Database Ledger Tables**: Registros de `cost_ledger`, `credit_transactions`, `usage_events` e `billing_events`.

## 7. Outputs

* **Budget Authorization Requests**: Eventos do tipo `CostEstimateRequested` disparados antes de execuções de alto impacto financeiro.
* **Dispute Registrations**: Formulários estruturados de abertura de disputas emitindo eventos `BillingDisputeOpened` associados a `usage_events` rastreáveis.

## 8. Riscos

* **Estresse Cognitivo por Controle Excessivo**: A exibição agressiva de custos em centavos de dólares a cada segundo de digitação pode inibir a criatividade do usuário e induzir à paralisia de decisão.
  * *Mitigação*: Agrupar e consolidar pequenas transações de models calls pequenas em pílulas discretas atualizadas com debounce de 30 segundos, exibindo contadores proeminentes apenas para tarefas P0 caras.
* **Falta de Sincronização de Saldos**: Exibir créditos desatualizados devido a latência de rede ou latência de eventos da projeção.
  * *Mitigação*: Exibir sinal visual "Sincronizando..." se `ui_projections.last_event_id` estiver defasado em relação ao bus principal.

## 9. Regras de ROI

> **Regra Rígida**: Nenhuma melhoria de ROI ou eficiência alegada pela IA pode ser renderizada na interface do CKOS sem estar vinculada a evidências de auditoria de economia operacional comprovada e lida a partir das tabelas oficiais de runtime (`roi_snapshot_projection`, `roi_outcomes`, `roi_evidence_links`). O arquivo `ck_memory.md` é estritamente uma memória documental e não deve ser lido ou parseado pelo runtime ou interface da aplicação.

* O widget de ROI exibe gráficos comparativos densos estruturados em colunas curtas, apresentando:
  1. Horas manuais economizadas (calculadas pelo feedback do usuário e histórico do workflow).
  2. Custo operacional direto do runtime (consumo real de créditos).
  3. Taxa de acerto de entregas sem necessidade de retrabalho manual.
  4. Métricas detalhadas de ROI estimado vs. realizado, nível de confiança (`confidence`), premissas (`assumptions`), limitações e cobertura de evidências (`evidence_coverage`).

## 10. Regras de Custo/Créditos

* **Diferenciação Estrita (Custo vs. Preço)**: A interface deve diferenciar com clareza o custo interno do runtime de computação (`cost_ledger` em USD, visível apenas para admins técnicos/internos do CKOS) das cobranças faturadas ao cliente (`credit_transactions` e `usage_events` em créditos CKC) e do faturamento de cobrança real/billing do cartão/fatura (`billing_events` e faturas reais). Custo interno de runtime nunca é exibido diretamente para usuários clientes.
* **Estimativa vs. Cobrança**: Exibir claramente a estimativa de custos antes da execução (fase de planejamento) e a cobrança/consumo real de créditos efetuada apenas após a aprovação e término do fluxo.
* **Rastreabilidade**: Todo cartão de cobrança de fatura no painel financeiro deve conter a listagem em acordeão dos IDs de eventos de uso que a geraram, permitindo ao usuário abrir o run exato ou artefato correspondente para fins de auditoria.

## 11. Regras de Aprovação Humana

* Transições para o estado `Blocked by Cost` devido ao estouro de limites requerem o acionamento de um portão de aprovação de orçamento extra, liberando a fila de workflows apenas após o evento `ApprovalSubmitted` assinado pelo Founder ou administrador financeiro cadastrado no projeto.

## 12. Regras de Evidência

* As faturas geradas de faturamento e os usage_events vinculados no painel financeiro devem conter as chaves de correlação física (`correlation_id` e `idempotency_key`) para certificar que não existem duplicidades de cobrança por falhas na camada de concorrência.

## 13. Mobile Behavior

* **Push Notifications de Alerta**: Notificações instantâneas ergonômicas no topo da tela do celular são disparadas se o saldo de créditos atingir o limite crítico.
* **Upgrade Rápido**: O widget mobile exibe um botão de ação proeminente na metade inferior para recarga rápida de créditos via um fluxo simplificado de pagamento associado à assinatura existente.
* **Visualização Compacta**: O status de faturamento reduz o extrato a um gráfico de linha minimalista do consumo diário do workspace.

## 14. Web Behavior

* **Painel Financeiro Denso (Analytical Dashboard)**: Desktop exibe tabelas interativas completas permitindo filtros por subagentes, por projetos ativos e por data de transação. Gráficos de barras de eficiência mostram o ROI acumulado por workflow.

## 15. Anti-Patterns

* **Misturar Cost Ledger com Invoicing**: Exibir o consumo em dólares brutos do custo da API da OpenAI na fatura do cliente, induzindo à confusão epistemológica sobre o modelo de negócio do CKOS.
* **Ausência de Trava Física**: Permitir que workflows concorrentes continuem a rodar no backend mesmo com a interface mobile exibindo saldo de créditos esgotado ou devedor (falha do reservation pattern).

## 16. Acceptance Criteria

* O saldo visual disponível exibido na UI deve ser alimentado de forma exclusiva pela projeção `cost_projection` e `credit_wallets` CQRS.
* O widget de ROI deve exibir os dados de retorno com base estritamente em `roi_snapshot_projection` e tabelas de evidência oficiais do banco de dados, e nunca em parseamento de arquivos markdown como `ck_memory.md`.
* O botão de início de workflow complexo deve ser desativado imediatamente na UI se o custo estimado do pre-check exceder os créditos disponíveis na wallet correspondente.

## 17. Próximas Perguntas para Founder/PMO

* Devemos implementar uma funcionalidade de "auto-recarga" de créditos configurável por projeto para evitar que workflows automáticos travem em momentos críticos de produção devido a quotas esgotadas?
* Qual o SLA tolerado para a exibição de estornos de créditos na UI após a rejeição ou falha de uma tarefa de subagente?
