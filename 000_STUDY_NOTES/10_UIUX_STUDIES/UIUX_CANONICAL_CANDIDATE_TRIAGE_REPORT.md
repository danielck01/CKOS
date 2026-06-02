---
title: "UI/UX Canonical Candidate Triage Report"
system_id: study_notes_uiux_canonical_candidate_triage_report_20260529
layer: auxiliary
phase: 000_STUDY_NOTES
category: triage_report
status: study_not_canonical
version: 2.0.0
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - founder
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
  - metacognik
confidence: unverified
provenance_status: unverified
source_tool: antigravity
created_at: 2026-05-28
updated_at: 2026-05-29
version_note: "v2.0.0 — Comprehensive rewrite with deep canonical cross-referencing. Supersedes v1.0.0 (session 009)."
purpose: "Relatório de triage dos 14 candidatos a patches canônicos de UI/UX, com cross-referencing profundo contra os documentos canônicos, classificando elegibilidade de promoção com evidências documentais."
tags:
  - uiux_studies
  - triage
  - auxiliary
  - cross_referencing
---

# UI/UX Canonical Candidate Triage Report — v2.0.0

> [!WARNING]
> Este relatório pertence à **camada de estudos auxiliares** (auxiliary study folder) do CKOS. Ele não constitui documentação canônica, não altera as regras oficiais do sistema e não autoriza qualquer implementação de código física (React, HTML, CSS, JS, APIs, banco de dados ou migrações).

> [!IMPORTANT]
> **v2.0.0** — Esta versão substitui integralmente o relatório v1.0.0 (sessão 009). A versão anterior era estruturalmente correta mas rasa: não incluía cross-referencing detalhado com seções e linhas canônicas. Esta versão corrige essa lacuna com evidências documentais precisas para cada candidato.

---

## 1. Contexto e Autorização

Este documento apresenta a **Triage Oficial Revisada** dos Candidatos Canônicos de UI/UX mapeados no arquivo [23_UIUX_CANONICAL_PATCH_CANDIDATES.md](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/000_STUDY_NOTES/10_UIUX_STUDIES/23_UIUX_CANONICAL_PATCH_CANDIDATES.md).

**Sessão:** `S-P1-19-ANTIGRAVITY-20260529-010`
**Lock:** `LOCK-P1-19-ANTIGRAVITY-20260529-010`
**Supersede:** Sessão 009 (`UIUX_CANONICAL_CANDIDATE_TRIAGE_20260528`)

---

## 2. Metodologia de Triage

Cada um dos 14 candidatos foi triado com base nos seguintes critérios:

1. **Cross-referencing canônico profundo**: Leitura e busca textual direta nos documentos canônicos alvo para verificar se a entidade proposta (tabela, evento, projeção, state machine) já existe, é parcialmente coberta ou está ausente.
2. **Conformidade de nomenclatura**: Detecção de conflitos entre nomes usados no estudo e nomes canônicos consolidados nos schemas oficiais.
3. **Integridade epistêmica**: Alinhamento com a arquitetura CQRS (Event Bus e Projeções) do runtime do CKOS.
4. **Necessidade de evidência empírica**: Identificação de propostas que exigem validação prática (testes de usabilidade, Evals de estresse cognitivo, medições de latência de RLS) antes de canonização.
5. **Destino de governança**: Encaminhamento para o bucket correto: promoção, estudo, evidência adicional, documento futuro ou rejeição.

---

## 3. Tabela Completa de Triage (14 Candidatos)

| ID | Nome do Candidato | Target Canônico Alvo | Classificação | Urgência |
|---|---|---|---|---|
| 1 | Matriz de 19 Estados de Execução | Doc 16 §9 | `NEEDS_MORE_EVIDENCE` | Média |
| 2 | 12 Elementos do Approval Gate | Doc 14 §11 + Doc 10 (Approval Gate Engine) | `APPROVE_FOR_CANONICAL_PATCH` | Alta |
| 3 | Tripla Estrutura Epistêmica | Doc 15, Doc 13 (Evals), Doc 18 (Metacognik) | `NEEDS_MORE_EVIDENCE` | Média |
| 4 | Regras WCAG no Runtime | Futuro manual de acessibilidade | `MOVE_TO_FUTURE_DOC` | Baixa |
| 5 | Tabela de Preferências de Densidade (RBAC/ABAC) | Doc 11 §34 (`dashboard_preferences`) | `NEEDS_MORE_EVIDENCE` | Média |
| 6 | Tabelas de Governança CKStore | Doc 21 (futuro) | `MOVE_TO_FUTURE_DOC` | Baixa |
| 7 | Persistência do Histórico do Command Center | Doc 11 (patch pendente) + Doc 15 §13 | `APPROVE_FOR_CANONICAL_PATCH` | Crítica |
| 8 | Registro de Feedback no Learning | Doc 11 (gap P11-3) + Doc 14 §16 | `KEEP_AS_STUDY` | Baixa |
| 9 | Modelagem Financeira Credits/Wallets | Doc 24 (já canônico) | `KEEP_AS_STUDY` | Baixa |
| 10 | Evento `AgentLoopDetected` | Doc 15 §Erros (L882) | `NEEDS_MORE_EVIDENCE` | Média |
| 11 | Mentions Oficiais do Ingress | Doc 15 §5.5 | `KEEP_AS_STUDY` | Baixa |
| 12 | Evento `LayoutPreferenceUpdated` | Doc 14 §28 + Doc 11 §34 | `KEEP_AS_STUDY` | Baixa |
| 13 | Standardização Dashboard Projection | Doc 11 §21, Doc 14, Doc 15, Doc 16 | `REJECT` | Alta |
| 14 | Approved Memory Projection | Doc 11 (ausente) | `NEEDS_MORE_EVIDENCE` | Média |

---

## 4. Fichas Detalhadas por Candidato

---

### 4.1 Candidato 1 — Matriz de 19 Estados de Execução de Workflows

**Classificação:** `NEEDS_MORE_EVIDENCE`
**Escopo Alvo:** [16_NODE_CANVAS_ARCHITECTURE.md §9](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/04_PRODUCT_SYSTEM/16_NODE_CANVAS_ARCHITECTURE.md)
**Nota de Estudo Fonte:** Nota 03 (`WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK`)

**Base Canônica Consultada:**
- Doc 16 §9.1 — State machine de Node: **9 estados** (`suggested → draft → pending_approval → active → running → waiting_input → waiting_approval → completed → archived → blocked`). Linhas 456–468.
- Doc 16 §9.2 — State machine de Workflow: **10 estados** (`created → planned → queued → running → waiting_agent → waiting_tool → waiting_approval → completed → failed → cancelled → rolled_back`). Linhas 474–486.
- Doc 16 §9.3 — State machine de Approval: **6 estados** (`requested → approved → rejected → expired → revoked → escalated`). Linhas 492–499.
- Doc 16 §10 — Estados de agente visíveis: 6 estados adicionais (`working, suggested, blocked, awaiting_approval, audited, completed`). Linhas 521–530.

**Resumo da Proposta:** Integrar uma matriz conceitual de 19 estados de execução triando-a contra as state machines oficiais.

**Cross-referencing:**
O Doc 16 §9 já define formalmente **3 state machines distintas** com um total combinado de 25+ estados (9 Node + 10 Workflow + 6 Approval). A proposta de "19 estados" do estudo não especifica se é uma união, intersecção ou reorganização destas máquinas. Há risco de conflito se a UI renderizar um subconjunto arbitrário que misture estados de máquinas distintas.

**Condições para Promoção:**
1. Mapear explicitamente cada um dos 19 estados propostos para a state machine canônica correspondente (Node, Workflow ou Approval).
2. Demonstrar empiricamente que a unificação visual não confunde o operador sobre qual máquina está sendo representada.
3. Eliminar quaisquer estados inexistentes nas 3 state machines canônicas ou propor formalmente sua criação no Doc 10/16.

**Inconsistências Registradas:** Nenhuma inconsistência canônica direta — o problema é de especificação insuficiente do mapeamento.

---

### 4.2 Candidato 2 — 12 Elementos Obrigatórios do Approval Gate

**Classificação:** `APPROVE_FOR_CANONICAL_PATCH`
**Escopo Alvo:** [14_PROJECT_DASHBOARD_ARCHITECTURE.md §11](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md) + [10_SYSTEM_RUNTIME_ARCHITECTURE.md](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md) (Approval Gate Engine)
**Nota de Estudo Fonte:** Nota 12 (`APPROVAL_GATE_AND_REVERSIBILITY_UX_STUDY`) §11

**Base Canônica Consultada:**
- Doc 14 §11 (L320–342): Widget "What Needs Decision" define approvals pendentes com título, tipo, quem pediu, tempo, prazo e impacto estimado. Ações inline: aprovar/rejeitar/delegar. Evento: `ApprovalSubmittedFromDashboard`.
- Doc 14 §27.3 (L762–764): State machine de Approval visível no Dashboard (estados de Doc 16 §9.3).
- Doc 14 §28 evento #2 (L773): `ApprovalSubmittedFromDashboard` → `approval_gate → Runtime`.
- Doc 16 §9.3 (L490–499): State machine de Approval: 6 estados.

**Resumo da Proposta:** Canonizar regra rígida de que nenhum portão de aprovação visual pode ser renderizado sem exibir obrigatoriamente os 12 elementos de contexto definidos na Nota 12 §11: (1) Ação Solicitada, (2) Motivo, (3) Risco, (4) Custo, (5) Dados Afetados, (6) Arquivos/Objetos Impactados, (7) Rollback Disponível, (8) Quem Pediu, (9) Quem Aprova, (10) Prazo, (11) Consequência de Aprovar, (12) Consequência de Rejeitar.

**Cross-referencing:**
O Doc 14 §11 define os elementos do widget "What Needs Decision" mas de forma resumida (título, tipo, quem pediu, tempo, prazo, impacto). A Nota 12 é significativamente mais completa com 12 campos obrigatórios, incluindo diff de arquivos, custo, rollback, e consequências de ambas as decisões. A proposta **estende** o Doc 14 sem contradizê-lo. A Nota 12 §5.1 também define 7 tipos distintos de reversão que não existem no canônico.

**Justificativa de Aprovação:**
A lacuna entre os 6 campos do Doc 14 e os 12 campos da Nota 12 é um risco real de segurança: sem exibir consequências de aprovar/rejeitar, custo, diff e rollback, o operador aprova às cegas. A Nota 12 resolve isso com checklist rígida ancorada em eventos canônicos (`ApprovalSubmitted`, `RollbackWorkflowRequested`, `CompensationActionRequested`).

**Condições para Promoção:**
1. Redigir diff de patch aplicável ao Doc 14 §11 expandindo os campos do widget.
2. Confirmar que os eventos de reversão (§5.1 da Nota 12) são compatíveis com o event bus do Doc 10.
3. Testar em mobile que os 12 elementos são exibíveis sem sobrecarga visual.

**Inconsistências Registradas:** Nenhuma. A proposta estende corretamente o canônico.

---

### 4.3 Candidato 3 — Tripla Estrutura Epistêmica de Respostas

**Classificação:** `NEEDS_MORE_EVIDENCE`
**Escopo Alvo:** [15_COMMAND_CENTER_ARCHITECTURE.md](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md)
**Nota de Estudo Fonte:** Nota 13 (`EVIDENCE_TRUST_AND_DECISION_UIUX_STUDY`) §12

**Base Canônica Consultada:**
- Doc 15 L175: Metacognik audita → `MetacognikReviewed{confidence, risk, recommendation}`.
- Doc 15 L236: `context_pack_builder` reúne `audit_logs` + `risk_projection` + `agent_decisions` + `evidence_items` autorizados → Nick traduz.
- Doc 15 L540–542: Comandos `/explain` e `/evidence` usam `evidence_items` autorizados.
- Doc 15 L594: Traduzir complexidade técnica (confidence scores, risk levels) em implicações práticas.
- Doc 15 L598: Mostrar evidências quando disponíveis (`evidence_items` + `agent_decisions`).
- Doc 15 L873: `ContextAssembled{confidence: low}` → Nick indica limitação de contexto.
- Doc 15 L876: `MetacognikReviewed.confidence < threshold` → Nick apresenta score + recomendação.
- Doc 13 (Evals) L65: Todo output estratégico passa por eval de `evidence coverage`, hallucination check, contradiction check.
- Doc 13 (Evals) L118: Evidence coverage score.
- Doc 13 (Evals) L126–127: Confidence scoring + Uncertainty scoring.
- Doc 13 (Evals) L406–408: Baixa confiança e evidência insuficiente como triggers.

**Resumo da Proposta:** Forçar toda resposta do Command Center / Nick a ser estruturalmente dividida em 3 blocos epistêmicos: (1) Nível de Confiança (Confidence Score), (2) Links de Evidência (`evidence_items` + `roi_evidence_links`), (3) Declaração de Limitações.

**Cross-referencing:**
O Doc 15 já contém referências distribuídas a confidence, evidence e limitações, mas **não como regra rígida estrutural unificada**. A tripla epistêmica é um padrão emergente nos canônicos que a Nota 13 formaliza. O Doc 13 (Evals) define os mecanismos de scoring e coverage que alimentariam os dados. Porém, a Nota 13 §12 impõe exibição compulsória em **toda** resposta, o que pode sobrecarregar respostas simples (ex: `/help`, `/status`).

**Condições para Promoção:**
1. Cross-reading aprofundado de Doc 13 (Evals), Doc 15, Doc 14 §19 (Risk, Gap & Evidence) e Doc 18 (se existir Metacognik doc separado) para mapear exatamente quais responses modes (`ask`, `explain`, `execute`) devem exibir a tripla.
2. Testes de usabilidade mobile para avaliar se exibição compulsória em tela pequena causa fadiga de informação.
3. Definir threshold: respostas triviais (ex: `/status`, `/help`) ficam isentas da tripla.

**Inconsistências Registradas:** A nota propõe a tripla para "toda" resposta, mas o canônico diferencia `ask mode`, `explain mode` e `execute mode` com níveis de detalhe distintos.

---

### 4.4 Candidato 4 — Regras de Validação WCAG no Runtime

**Classificação:** `MOVE_TO_FUTURE_DOC`
**Escopo Alvo:** Futuro manual de governança do Design System / Acessibilidade Digital
**Nota de Estudo Fonte:** Notas 08 (`WHITELABEL_TOKEN_SYSTEM`) e 22 (`ACCESSIBILITY_REDUCED_MOTION`)

**Base Canônica Consultada:**
- Nenhum documento canônico 01–25 atualmente possui seção dedicada a WCAG ou acessibilidade digital.
- Doc 14 §5.8: `whitelabel-adaptive` — tokens parametrizados por tenant. Sem referência a validação WCAG.
- Doc 14 §32 (Visual Direction): direção visual sem implementação — sem menção a contraste.

**Resumo da Proposta:** Tornar obrigatória a validação matemática em tempo real de taxas de contraste (4.5:1 mínimo) no serviço de temas antes de persistir customizações whitelabel.

**Cross-referencing:**
Não há âncora canônica para esta proposta nos documentos 01–25 atuais. A proposta é tecnicamente válida e importante, mas seu escopo (design system governance + whitelabel compliance) excede qualquer documento existente. Deve ser alocada em documento futuro dedicado.

**Condições para Promoção:**
1. Criação de documento canônico dedicado (ex: Doc 27 ou similar) para Design System Governance.
2. Especificação formal de quais tokens são sujeitos a validação WCAG e quais são isentos.

**Inconsistências Registradas:** Nenhuma — a proposta é coerente, mas sem destino canônico imediato.

---

### 4.5 Candidato 5 — Tabela de Preferências de Densidade Visual (RBAC/ABAC)

**Classificação:** `NEEDS_MORE_EVIDENCE`
**Escopo Alvo:** [11_DATA_MODEL_AND_PERSISTENCE.md §34](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md)
**Nota de Estudo Fonte:** Nota 11 (`COST_CREDITS_AND_ROI_AWARE_UX_STUDY`)

**Base Canônica Consultada:**
- Doc 11 §34 (L1559–1588): Tabela `dashboard_preferences` já existe canônicamente (Patch 1.2.0, P11-7). Inclui campo `density enum(compact|default|expanded) default 'default'` na L1575.
- Doc 11 L147: Tabela `users` já contém campo `preferences jsonb`.
- Doc 14 §24 (L617–652): Widget personalization: density, presets, save/restore layout.

**Resumo da Proposta:** Criar tabela `preferences` com RLS por role e evento `UserPreferenceUpdated`.

**Cross-referencing:**
A proposta é **parcialmente redundante**. O Doc 11 §34 já define `dashboard_preferences` com campo `density` e o Doc 11 L147 define `users.preferences jsonb`. A proposta do estudo pede uma tabela `preferences` separada, mas isso conflita com o schema existente. O que falta no canônico é: (a) RLS policies específicas para preferências por role, (b) evento `UserPreferenceUpdated` formal no event bus.

**Condições para Promoção:**
1. Redefinir a proposta como **patch ao `dashboard_preferences` existente (§34)** e não como tabela nova.
2. Especificar as RLS policies necessárias por role sem conflitar com o modelo RBAC do Doc 12.
3. Avaliar impacto de latência de consulta de preferências ao renderizar layouts dinâmicos.

**Inconsistências Registradas:**
- **INC-05**: A proposta usa o nome `preferences` (tabela genérica) enquanto o canônico já define `dashboard_preferences` (tabela específica com `density`). Proposta deve ser redirecionada para extensão da tabela existente.

---

### 4.6 Candidato 6 — Tabelas de Governança da CKStore

**Classificação:** `MOVE_TO_FUTURE_DOC`
**Escopo Alvo:** Futuro documento de CKStore / Marketplace Architecture
**Nota de Estudo Fonte:** Nota 19 (`CKSTORE_CAPABILITY_MARKETPLACE_UIUX_STUDY`)

**Base Canônica Consultada:**
- Não existe documento canônico formal para CKStore/Marketplace nas pastas `04_PRODUCT_SYSTEM/` ou `05_IMPLEMENTATION_SYSTEM/`.
- Doc 15 L570: Mentions de agents de domínio só são resolvidos se a capability correspondente estiver ativa (`capabilityRegistry` + `policy_engine`). Referência indireta a capabilities mas sem schema de tabela.

**Resumo da Proposta:** Criar tabelas `available_capabilities` e `installed_capabilities` para registrar habilidades e subagentes instalados com estimativas de quotas e assinaturas de segurança.

**Cross-referencing:**
Nenhuma destas tabelas existe nos documentos canônicos atuais. O Doc 15 menciona `capabilityRegistry` como conceito mas sem definição de schema. A CKStore é uma feature comercial futura que necessita de documento canônico dedicado antes de propor tabelas de persistência.

**Condições para Promoção:**
1. Criação de documento canônico dedicado para CKStore Architecture.
2. Definição formal do schema de capabilities compatível com o `policy_engine` do Doc 12.

**Inconsistências Registradas:** Nenhuma — proposta coerente, mas prematura.

---

### 4.7 Candidato 7 — Persistência do Histórico do Command Center (`command_history`)

**Classificação:** `APPROVE_FOR_CANONICAL_PATCH`
**Escopo Alvo:** [11_DATA_MODEL_AND_PERSISTENCE.md](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md)
**Nota de Estudo Fonte:** Nota 15 (`COMMAND_CENTER_OPERATIONAL_UX_STUDY`)

**Base Canônica Consultada:**
- Doc 11 L947: `command_history (P11-2)` listada como source table para projeção, **marcada com `(P11-2)` indicando patch pendente**.
- Doc 15 L35: `Tabela command_history (patch pendente para doc 11)` — **declaração explícita de patch pendente**.
- Doc 15 L126: `Histórico de comandos do usuário no projeto (via command_history - ver §13)`.
- Doc 15 L803: `command_history [APPEND-ONLY]` — schema declarado no Doc 15 como especificação de dados necessária.
- Doc 15 L839: `Histórico de comandos via command_history (patch doc 11 v1.2.x)` — **referência explícita ao patch futuro para Doc 11 v1.2.x**.

**Resumo da Proposta:** Implementar formalmente a tabela `command_history` no Doc 11 para gerenciar o histórico de atalhos e intents enviados pelo usuário.

**Cross-referencing:**
Esta é uma **inconsistência canônica confirmada (INC-01)**. O Doc 15 referencia `command_history` em pelo menos 5 pontos distintos (L35, L126, L803, L839, L947 do Doc 11), declarando-a explicitamente como "patch pendente para doc 11". O Doc 11 lista `command_history (P11-2)` como source table mas **não contém a especificação DDL da tabela**. O schema inline do Doc 15 L803 declara `[APPEND-ONLY]` como constraint.

**Justificativa de Aprovação:**
Urgência Crítica. A tabela é referenciada por um documento canônico oficial (Doc 15) que depende dela para funcionar. A ausência no Doc 11 é uma lacuna formal que deve ser corrigida. O schema já está parcialmente especificado no Doc 15.

**Condições para Promoção:**
1. Redigir diff de patch para Doc 11 criando a seção `command_history` com schema baseado na declaração do Doc 15 L803.
2. Confirmar campos necessários: `id, project_id, user_id, command_text, intent_type, resolved_intent, correlation_id, created_at`.
3. Confirmar constraint `APPEND-ONLY` e RLS por tenant/projeto.

**Inconsistências Registradas:**
- **INC-01 (Crítica)**: Tabela `command_history` referenciada no Doc 15 (5 ocorrências) e no Doc 11 L947 como `(P11-2)` mas sem DDL formal no Doc 11. Lacuna estrutural confirmada.

---

### 4.8 Candidato 8 — Registro de Feedback Explícito no Learning

**Classificação:** `KEEP_AS_STUDY`
**Escopo Alvo:** [11_DATA_MODEL_AND_PERSISTENCE.md](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md) (gap P11-3)
**Nota de Estudo Fonte:** Nota 14 (`DASHBOARD_WIDGET_SYSTEM_UIUX_STUDY`)

**Base Canônica Consultada:**
- Doc 14 §16 (L443–473): Widget "Feedback Loop" — feedback como objeto operacional convertível em node, task, gap, improvement ou decision. Fluxo via `FeedbackSubmitted → Runtime`.
- Doc 14 §31 (L856): `P11-3: feedback_entries — captura de feedback explícito e implícito` — **gap registrado, patch sugerido para Doc 11 v1.2.x**.
- Doc 14 L473: `Gap registrado: Feedback System completo aguarda doc dedicado`.

**Resumo da Proposta:** Criar tabela `feedback_entries` e eventos `FeedbackSubmitted` / `FeedbackImplicit`.

**Cross-referencing:**
O Doc 14 já registra esta necessidade como gap `P11-3` com urgência "Feedback Mode MVP". O gap está catalogado no `ARCHITECTURE_PATCH_REPORT.md §14.4`. A tabela **não existe** no Doc 11 atual. Porém, o Doc 14 declara que o "Feedback System completo aguarda doc dedicado" — o que significa que a criação da tabela isolada sem o sistema completo é prematura.

**Justificativa de Manutenção em Estudo:**
A proposta é válida e alinhada com o gap P11-3, mas deve aguardar a criação do documento de Feedback System Architecture para que a tabela seja definida dentro do contexto correto. Canonizar a tabela isoladamente sem o sistema completo gera risco de schema parcial.

**Condições para Promoção Futura:**
1. Criação do documento canônico de Feedback System Architecture.
2. Definição do schema `feedback_entries` dentro desse contexto.

**Inconsistências Registradas:** Nenhuma — gap reconhecido pelo canônico.

---

### 4.9 Candidato 9 — Modelagem Financeira de Créditos e Wallets

**Classificação:** `KEEP_AS_STUDY`
**Escopo Alvo:** [24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md)
**Nota de Estudo Fonte:** Nota 11 (`COST_CREDITS_AND_ROI_AWARE_UX_STUDY`)

**Base Canônica Consultada:**
- Doc 24 §5.3 (L180): `plan_limits` — canônico.
- Doc 24 §8.3 (L337–340): `quota_policies` — canônico.
- Doc 24 §9.4 (L428–431): `credit_wallets` — canônico, com `balance_available` e `balance_reserved`.
- Doc 24 §9.5 (L453–456): `credit_transactions` — canônico, com `idempotency_key`.
- Doc 24 L102: `credit_reservations` — canônico, previne saldo negativo.
- Doc 24 L65, L86–87: `billing_events` e `usage_events` — canônicos e distintos do `cost_ledger`.
- Doc 24 L112: `cost_ledger` referenciado como Doc 11 §18 — custo interno de runtime.

**Resumo da Proposta:** Utilizar modelagem financeira do Doc 24 para subsidiar exibição de quotas/saldos no Cost Mode, mapeando interfaces para `credit_wallets`, `credit_transactions`, `credit_reservations`, `usage_events`, `billing_events`, `invoice_records`, `plan_limits`, `quota_policies` e `cost_ledger`.

**Cross-referencing:**
**Todas as tabelas mencionadas na proposta já existem canonicamente no Doc 24.** A proposta não pede criação de tabelas novas — pede mapeamento das interfaces UI para as tabelas existentes. Isso é alinhamento de UI/UX study com canônico, não patch canônico. A Nota 11 §4 corretamente referencia todas estas fontes.

**Justificativa de Manutenção em Estudo:**
A proposta não requer alteração canônica — as tabelas já existem e a Nota 11 já as referencia corretamente. O estudo serve como guia de mapeamento para a futura implementação de UI.

**Condições para Promoção Futura:** Nenhuma — não há gap canônico a corrigir.

**Inconsistências Registradas:** Nenhuma. Alinhamento correto com Doc 24.

---

### 4.10 Candidato 10 — Evento de Monitoramento de Loops de IA (`AgentLoopDetected`)

**Classificação:** `NEEDS_MORE_EVIDENCE`
**Escopo Alvo:** [10_SYSTEM_RUNTIME_ARCHITECTURE.md](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md) ou Doc 15
**Nota de Estudo Fonte:** Nota 17 (`CHAT_GROUPS_AGENT_THREADS_UIUX_STUDY`)

**Base Canônica Consultada:**
- Doc 15 L882: `Loop de agente detectado | loop_detector emite AgentLoopDetected; workflow entra em state: blocked; Nick notifica com trace_id e sugere /support` — **evento já referenciado no canônico como comportamento de edge case do Command Center**.

**Resumo da Proposta:** Definir formalmente o evento `AgentLoopDetected` disparado pelo runtime quando uma conversa atinge 5 iterações sem intervenção.

**Cross-referencing:**
O evento `AgentLoopDetected` **já existe como referência canônica** no Doc 15 L882, incluindo o comportamento esperado: `loop_detector` emite o evento, workflow entra em `state: blocked`, Nick notifica com `trace_id`. Porém, o evento **não está formalmente definido no Doc 10** (Runtime Architecture) como evento de domínio com schema próprio. A referência no Doc 15 é descritiva (edge case), não especificativa (schema + contract).

**Condições para Promoção:**
1. Definir o schema formal do evento `AgentLoopDetected` no Doc 10 (ou Doc 13 Evals).
2. Validação empírica do threshold (5 iterações) — falsos positivos podem bloquear workflows legítimos.
3. Definir se o `loop_detector` é componente do Doc 10 (Runtime) ou Doc 13 (Evals/Observability).

**Inconsistências Registradas:**
- **INC-10**: Evento referenciado no Doc 15 L882 mas sem definição formal de schema no Doc 10. Similar ao padrão da INC-01 (entity referenciada sem DDL).

---

### 4.11 Candidato 11 — Mentions Oficiais do Ingress

**Classificação:** `KEEP_AS_STUDY`
**Escopo Alvo:** [15_COMMAND_CENTER_ARCHITECTURE.md §5.5](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md)
**Nota de Estudo Fonte:** Nota 15 (`COMMAND_CENTER_OPERATIONAL_UX_STUDY`)

**Base Canônica Consultada:**
- Doc 15 §5.5 (L552–570): **As 9 mentions oficiais já estão canonicamente definidas:**
  - `@nick` (L557) — interface conversacional, sempre disponível
  - `@cognik` (L558) — diagnóstico, análise, evidência
  - `@metacognik` (L559) — auditoria, bloqueio, risco (não executa a pedido direto)
  - `@pmo_ckos` (L560) — planejamento, timeline, decisão estrutural
  - `@qa_lead` (L561) — aprovação de qualidade técnica
  - `@builder_lead` (L562) — implementação, arquitetura técnica
  - `@datta` (L563) — dados, métricas, cost ledger
  - `@ops` (L564) — operações, deploys, collectors
  - `@campaign` (L565) — campanhas, conteúdo, distribuição
- Doc 15 L568: Regra `@metacognik` — não executa ações a pedido direto.
- Doc 15 L570: Regra de capabilities — agents de domínio resolvidos via `capabilityRegistry` + `policy_engine`.

**Resumo da Proposta:** Formalizar suporte na commandbar para as 9 mentions oficiais.

**Cross-referencing:**
**Cobertura 100% canônica confirmada.** O Doc 15 §5.5 define todas as 9 mentions com role, comportamento, regras especiais (`@metacognik` não executa) e regras de capabilities. Não há gap canônico para corrigir.

**Justificativa de Manutenção em Estudo:**
A proposta é inteiramente coberta pelo canônico existente. Manter como estudo de referência de UX para guiar a implementação futura do autocomplete da commandbar.

**Condições para Promoção Futura:** Nenhuma — canônico completo.

**Inconsistências Registradas:** Nenhuma.

---

### 4.12 Candidato 12 — Persistência de Layout de Widgets do Dashboard

**Classificação:** `KEEP_AS_STUDY`
**Escopo Alvo:** [14_PROJECT_DASHBOARD_ARCHITECTURE.md §28](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md) + [11_DATA_MODEL_AND_PERSISTENCE.md §34](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md)
**Nota de Estudo Fonte:** Nota 14 (`DASHBOARD_WIDGET_SYSTEM_UIUX_STUDY`)

**Base Canônica Consultada:**
- Doc 14 §28 (L766–785): Eventos emitidos pelo Dashboard incluem `WidgetPinned` (#3), `WidgetHidden` (#4), `LayoutSaved` (#5), `LayoutRestored` (#6), `PresetSelected` (#7). Eventos #3 e #4 são estado local de UI. Eventos #5, #6, #7 geram eventos persistidos → `dashboard_preferences → Runtime`.
- Doc 11 §34 (L1559–1588): Tabela `dashboard_preferences` com campos para `widget_configs jsonb`, `preset_selected`, `pinned_widgets jsonb`, `density`. P11-7, referenciando Doc 14 §24.

**Resumo da Proposta:** Criar evento `LayoutPreferenceUpdated` para persistir alterações de ordenação e visibilidade.

**Cross-referencing:**
**Já coberto canônicamente.** O Doc 14 §28 define 5 eventos de layout (WidgetPinned, WidgetHidden, LayoutSaved, LayoutRestored, PresetSelected) e o Doc 11 §34 define a tabela `dashboard_preferences` para persistência. O evento proposto `LayoutPreferenceUpdated` é semanticamente equivalente a `LayoutSaved` (Doc 14 evento #5).

**Justificativa de Manutenção em Estudo:**
A necessidade já é atendida pelo canônico. Manter como padrão de estudo de UX flexível para referência de implementação.

**Condições para Promoção Futura:** Nenhuma — canônico completo.

**Inconsistências Registradas:** Nenhuma.

---

### 4.13 Candidato 13 — Standardização de Projeções de Leitura do Dashboard

**Classificação:** `REJECT`
**Escopo Alvo:** [11_DATA_MODEL_AND_PERSISTENCE.md §21](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md)
**Nota de Estudo Fonte:** Nota 23 (`UIUX_CANONICAL_PATCH_CANDIDATES`) §5.13

**Base Canônica Consultada:**
- Doc 11 §21 L661: `project_pulse_projection` — listada como projeção #1.
- Doc 11 L677–679: `### 1. project_pulse_projection` — definição DDL formal.
- Doc 14 L170, L201, L212, L271, L303, L791, L868: **8 referências canônicas** ao nome `project_pulse_projection` no Doc 14.
- Doc 15 L318, L339, L444, L465, L512, L525, L684, L784: **8 referências canônicas** ao nome `project_pulse_projection` no Doc 15.
- Doc 16 L171, L216, L261, L279, L288, L332, L648: **7 referências canônicas** ao nome `project_pulse_projection` no Doc 16.
- Doc 10 L188: `project_pulse_projection` listada como projeção de runtime.
- **Total: 24+ referências canônicas** ao nome `project_pulse_projection` em 4 documentos canônicos.

**Resumo da Proposta:** Banir "Project Pulse" e fixar `project_dashboard_projection` como read model agregado de saúde do projeto.

**Cross-referencing:**
**Proposta rejeitada de forma inequívoca.** O nome `project_pulse_projection` está consolidado em pelo menos **24 ocorrências canônicas** em 4 documentos oficiais (Docs 10, 11, 14, 15, 16). O nome proposto `project_dashboard_projection` **não existe em nenhum documento canônico** — é uma invenção do estudo. Renomear geraria cascata de conflitos em toda a documentação e no runtime.

**Inconsistências Registradas:**
- **INC-13 (Crítica)**: A Nota 23 §5.13 propõe nome `project_dashboard_projection` que conflita com 24+ referências canônicas a `project_pulse_projection`. O termo do estudo é um desvio técnico que deve ser eliminado.

---

### 4.14 Candidato 14 — Validated Memory Projection / Approved Memory Read Model

**Classificação:** `NEEDS_MORE_EVIDENCE`
**Escopo Alvo:** [11_DATA_MODEL_AND_PERSISTENCE.md](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md)
**Nota de Estudo Fonte:** Nota 23 (`UIUX_CANONICAL_PATCH_CANDIDATES`) §5.14

**Base Canônica Consultada:**
- Doc 11: **`approved_memory_projection` não existe** em nenhuma seção do documento canônico atual. Busca textual retornou zero ocorrências em docs canônicos.
- Doc 14 L190: `memory_summaries (11 §20) → quando permitido por policy (12 §5.9)` — referência a memória no Dashboard, mas via `memory_summaries`, não via projeção dedicada.
- Doc 13 (Evals) L396: `Before memory write → eval_runner (confidence + freshness) → write rejeitado se confidence < 0.5` — gate de qualidade para escrita de memória.

**Resumo da Proposta:** Definir read model `approved_memory_projection` no Doc 11 para expor memórias aprovadas, decisões consolidadas, aprendizados validados e feedbacks homologados ao painel de ROI & Aprendizados.

**Cross-referencing:**
A proposta é tecnicamente sólida e alinha-se com o conceito de que memórias devem ser filtradas por qualidade antes de exibição (Doc 13 L396). Porém, a entidade não existe em nenhum doc canônico e exige modelagem complexa envolvendo:
1. RAG pipeline (como a projeção é alimentada?).
2. RLS por tenant (isolamento de memórias por organização).
3. Confidence scoring (gate de qualidade para inclusão na projeção).
4. Diferenciação entre `memory_summaries` (Doc 14 L190) e `approved_memory_projection`.

**Condições para Promoção:**
1. Definir schema formal da projeção com campos, fontes de dados e refresh strategy.
2. Modelar fluxo RAG → projeção → UI, garantindo que memórias com `confidence < 0.5` são excluídas.
3. Confirmar isolamento por tenant via RLS antes de canonizar.
4. Esclarecer relação/distinção com `memory_summaries` do Doc 11 §20.

**Inconsistências Registradas:**
- **INC-14**: Projeção proposta não existe em nenhum doc canônico. Necessita modelagem formal antes de canonização.

---

## 5. Resumo Consolidado por Classificação

### 5.1 APPROVE_FOR_CANONICAL_PATCH (2 candidatos)

| ID | Candidato | Urgência | Condição Principal |
|---|---|---|---|
| 2 | 12 Elementos do Approval Gate | Alta | Diff para Doc 14 §11 expandindo campos do widget |
| 7 | Tabela `command_history` | Crítica | DDL formal no Doc 11 baseado em Doc 15 L803 |

### 5.2 KEEP_AS_STUDY (4 candidatos)

| ID | Candidato | Razão |
|---|---|---|
| 8 | Feedback no Learning | Gap P11-3 reconhecido; aguarda Feedback System Architecture |
| 9 | Modelagem Financeira | Todas tabelas já existem no Doc 24 |
| 11 | Mentions Oficiais | Doc 15 §5.5 cobre 100% das 9 mentions |
| 12 | LayoutPreferenceUpdated | Doc 14 §28 + Doc 11 §34 cobrem completamente |

### 5.3 NEEDS_MORE_EVIDENCE (5 candidatos)

| ID | Candidato | Evidência Necessária |
|---|---|---|
| 1 | Matriz de 19 Estados | Mapeamento explícito para 3 state machines de Doc 16 §9 |
| 3 | Tripla Epistêmica | Testes de usabilidade mobile; definição de threshold por response mode |
| 5 | Preferências de Densidade | Redefinir como patch ao `dashboard_preferences` (§34); avaliar RLS |
| 10 | `AgentLoopDetected` | Schema formal no Doc 10; validação empírica do threshold |
| 14 | Approved Memory Projection | Modelagem RAG → projeção → UI; RLS; relação com `memory_summaries` |

### 5.4 MOVE_TO_FUTURE_DOC (2 candidatos)

| ID | Candidato | Destino |
|---|---|---|
| 4 | Regras WCAG | Futuro doc de Design System Governance / Acessibilidade |
| 6 | Tabelas CKStore | Futuro doc de CKStore & Capability Marketplace Architecture |

### 5.5 REJECT (1 candidato)

| ID | Candidato | Razão |
|---|---|---|
| 13 | Dashboard Projection naming | Nome `project_dashboard_projection` conflita com 24+ refs canônicas a `project_pulse_projection` |

---

## 6. Registro de Inconsistências Canônicas

| INC ID | Candidato | Severidade | Descrição | Docs Afetados |
|---|---|---|---|---|
| INC-01 | #7 | Crítica | Tabela `command_history` referenciada no Doc 15 (5 ocorrências) e Doc 11 L947 como `(P11-2)` mas sem DDL formal | Doc 11, Doc 15 |
| INC-05 | #5 | Média | Proposta usa nome `preferences` (genérico) mas canônico já define `dashboard_preferences` (§34) | Doc 11 |
| INC-10 | #10 | Média | Evento `AgentLoopDetected` referenciado no Doc 15 L882 mas sem schema formal no Doc 10 | Doc 10, Doc 15 |
| INC-13 | #13 | Crítica | Nota 23 §5.13 propõe `project_dashboard_projection` conflitando com 24+ refs canônicas | Docs 10, 11, 14, 15, 16 |
| INC-14 | #14 | Média | `approved_memory_projection` proposta sem existir em nenhum doc canônico | Doc 11 |

---

## 7. Riscos Remanescentes

1. **Risco de Codificação Precoce (P0)**: Subagentes ou desenvolvedores tentarem implementar candidatos aprovados (#2, #7) antes da autorização formal de sessão `canonical_patch` sob lock aprovado pelo Founder.
2. **Inconsistência de Nomenclatura (INC-13)**: O uso de `project_dashboard_projection` em notas de estudo pode vazar para agentes futuros se não for corrigido nas notas fonte.
3. **Complexidade de Portões de Aprovação**: A canonização dos 12 elementos rígidos (#2) sem testes em workflows com efeitos externos pode causar locks se o stakeholder estiver ausente.
4. **Schema Parcial de Feedback**: Canonizar `feedback_entries` (#8) antes do Feedback System Architecture completo geraria tabela órfã.
5. **Threshold de Loop Detector**: Canonizar `AgentLoopDetected` (#10) com threshold de 5 iterações sem validação empírica pode bloquear workflows legítimos de alta complexidade.

---

## 8. Próximo Passo Recomendado

> **Submeter ao PMO/Metacognik para auditoria formal do relatório v2.0.0. Após aprovação do Founder, planejar sessão `canonical_patch` apenas para candidatos aprovados (Candidatos #2 e #7). Não iniciar P1.12 sem esta auditoria.**

---

## 9. Avaliação do Executor (Executor Assessment)

Este relatório foi compilado e estruturado pelo agente `antigravity` na função de executor da sessão de estudos `S-P1-19-ANTIGRAVITY-20260529-010`. Ele representa unicamente a perspectiva do executor (executor assessment) e **não constitui aprovação final, homologação ou validação oficial** pelo PMO, Metacognik ou Founder.

**Diferenças em relação à v1.0.0 (sessão 009):**
- Cross-referencing profundo com linhas e seções canônicas citadas.
- Fichas detalhadas com Base Canônica Consultada, Cross-referencing, Condições para Promoção e Inconsistências por candidato.
- Registro formal de 5 inconsistências canônicas (INC-01, INC-05, INC-10, INC-13, INC-14).
- Candidato 11 corretamente classificado como `KEEP_AS_STUDY` (Doc 15 §5.5 cobre 100%).
- Candidato 5 reclassificado com INC-05 por conflito de nome com `dashboard_preferences`.
