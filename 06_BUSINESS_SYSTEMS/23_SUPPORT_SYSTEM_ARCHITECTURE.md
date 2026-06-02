---
title: Support System Architecture
file: 23_SUPPORT_SYSTEM_ARCHITECTURE.md
phase: 06_BUSINESS_SYSTEMS
category: business_architecture
version: 1.0.0
status: draft
owner: PMO_CKOS
responsible_agent: cognik
reviewers:
  - metacognik
  - qa_lead
approval_required:
  - founder
  - technical
  - metacognik
inputs: >
  System Runtime Architecture (10 v1.1.1);
  Data Model and Persistence (11 v1.2.0);
  Security, Permissions and Data Governance (12 v1.1.0);
  Evals, Observability and Cost Control (13 v1.1.0);
  Implementation Protocol (17 v1.2.1);
  QA and Founder Approval Protocol (20 v1.2.0);
  ROI Architecture (21 v1.0.0);
  Feedback System Architecture (22 v1.0.0)
related_notes:
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - ../04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md
  - ../04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md
  - ../04_PRODUCT_SYSTEM/16_NODE_CANVAS_ARCHITECTURE.md
  - ../05_IMPLEMENTATION_SYSTEM/17_IMPLEMENTATION_PROTOCOL.md
  - ../05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md
  - 21_ROI_ARCHITECTURE.md
  - 22_FEEDBACK_SYSTEM_ARCHITECTURE.md
  - 24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md
  - ../ARCHITECTURE_PATCH_REPORT.md
  - ../QA_DOCUMENTATION_CHECKLIST.md
outputs: >
  Support System definition (10 support types);
  Support Object Model (12 objects with SQL schemas);
  Support Classification Engine;
  Support SLA Policies (4 priority tiers);
  13-state Support State Machine;
  16 Support Events mapped to event bus;
  Human Escalation Protocol;
  Knowledge Base System;
  Incident Management protocol;
  Friction Signal detection;
  MVP P0 scope;
  20 Failure Modes;
  6 patches suggested for docs 10/11 (not applied)
---

> **Tese central do Support System:**  
> "Support in CKOS is not a helpdesk. It is a governed resolution system that captures operational friction, routes it to the right owner, tracks resolution with SLAs, escalates when needed, and feeds every unresolved issue back into the learning loop."

> **Princípio central:**  
> "No support ticket should be closed without a resolution summary, a root cause classification, and a decision about whether the issue informs the product, the workflow, or the knowledge base."

---

# 1. Propósito

O Support System da CKOS resolve um problema crítico de qualidade operacional: toda plataforma de AI que gera outputs, executa workflows e toma decisões **cria fricção operacional** — comportamentos inesperados, erros de execução, dúvidas de clientes, falhas de billing, incidentes de segurança. Sem um sistema de suporte governado, essa fricção se acumula invisível, não-rastreável e não-aprendível.

O Support System define:

- **Como capturar** tickets de suporte de múltiplas origens (Command Center, Feedback, sistema, cliente, admin)
- **Como classificar** por tipo, prioridade, SLA e categoria
- **Como rotear** para o owner correto (humano ou agente)
- **Como resolver** com rastreabilidade de root cause e knowledge base
- **Como escalar** quando SLA é violado ou human handoff é necessário
- **Como fechar o loop** — cada ticket resolvido alimenta a Knowledge Base, o Feedback System e o ROI System
- **Como detectar padrão** — friction signals agregam tickets em padrões de produto a serem endereçados

O Support System **não é** um canal de comunicação livre. É uma estrutura de resolução com governança, SLAs, rastreabilidade e aprendizado sistêmico.

---

# 2. O que é / O que NÃO é o Support System

## O que é

| É | Descrição |
|---|-----------|
| **Sistema de resolução governado** | Todo ticket tem owner, SLA, status, root cause e decision sobre aprendizado |
| **Detector de fricção operacional** | `friction_signals` agregam padrões invisíveis em uma ou poucos tickets |
| **Integrador de aprendizado** | Tickets resolvidos alimentam Knowledge Base, Feedback System, ROI e Evals |
| **Protocolo de escalação** | SLA breach → escalation_level++; N tentativas de agente → human handoff |
| **Componente do Business Operating System** | Suporte, ROI, Feedback e Billing são os 4 pilares do Business Systems layer |
| **Superfície de Node Canvas** | Support nodes representam tickets vivos no canvas do projeto |

## O que NÃO é

| Não é | Por quê |
|-------|---------|
| **Helpdesk genérico** | Cada ticket tem tipo, classificação, routing e SLA específicos por contexto CKOS |
| **Chatbot de atendimento** | O Command Center pode ser entrada, mas o sistema de resolução é próprio |
| **Repositório de reclamações** | Todo ticket deve fechar com resolution_summary + root_cause_category |
| **Sistema paralelo ao Feedback** | Support e Feedback são complementares — ticket pode originar de feedback e vice-versa |
| **Mecanismo de auto-resolução por agente** | Agente pode tentar resolver; human handoff é obrigatório quando agente falha N vezes |
| **Repositório de billing** | Billing support usa doc 24 como referência; Support System é a camada de resolução acima |

---

# 3. Princípio Central

> **"No support ticket should be closed without a resolution summary, a root cause classification, and a decision about whether the issue informs the product, the workflow, or the knowledge base."**

Esta frase define a diferença entre suporte como canal de descarte e suporte como sistema de aprendizado. No CKOS, o closure de um ticket não é o fim — é o início do registro de conhecimento.

---

# 4. Filosofia do Support System

1. **Resolução com rastreabilidade.** Todo ticket tem audit trail completo: reporter, classificação, assignee, tentativas de resolução, escalações e closure.
2. **SLA como contrato, não como aspiração.** SLA breach dispara evento formal (`SupportSlaBreached`) e incrementa `escalation_level` — não é silencioso.
3. **Agente como primeiro respondente, humano como fallback garantido.** Agente pode resolver tickets; human handoff é ativado automaticamente quando agente falha ou SLA está em risco.
4. **Root cause é obrigatório.** Ticket não pode ser fechado sem `root_cause_category` preenchido — isso alimenta friction signals e knowledge base.
5. **Conhecimento é produto do suporte.** Cada ticket resolvido é candidato a knowledge article — não por automação, mas por sugestão com aprovação humana.
6. **Friction signals são a camada de pattern recognition.** Um único ticket é incidente; N tickets do mesmo tipo são sinal de produto.
7. **Privacidade por design.** `is_client_visible DEFAULT false`; `has_pii` dispara redação obrigatória; notas internas nunca expostas sem autorização explícita.
8. **Incidentes têm protocolo próprio.** Tickets P0 com `is_incident=true` seguem Incident Management (§21) — SLA diferente, war room, post-mortem obrigatório.
9. **Suporte alimenta ROI.** Custo de suporte por projeto/cliente é dado de ROI operacional; tickets não resolvidos impactam retention_roi e efficiency_roi.
10. **Suporte alimenta Feedback.** Ticket resolvido com padrão recorrente pode gerar `feedback_learning_signal` — mas nunca automaticamente; aprovação humana obrigatória.
11. **Tenant isolation absoluta.** `tenant_id` em todas as tabelas; cross-tenant structurally impossible.
12. **Auditabilidade completa.** Toda transição de estado emite evento no event bus; `support_ticket_events` é append-only.

---

# 5. Support Types

Todo ticket pertence a exatamente um `ticket_type`. O tipo determina categoria padrão, SLA padrão, routing inicial e reviewer esperado.

## 5.1 `client_support`

| Campo | Valor |
|---|---|
| **Definição** | Dúvidas, solicitações ou reclamações de clientes sobre outputs, proposals, artifacts e escopo entregue |
| **Origem típica** | Client Portal, Command Center (cliente), email, Feedback do tipo `client_feedback` |
| **Prioridade padrão** | P2 (urgente se contrato em risco: P1) |
| **Reviewer obrigatório** | project_lead ou founder |
| **SLA resposta** | ≤ 4 h (P2) |
| **Human handoff** | Sempre que cliente insatisfeito após 1 tentativa de agente |
| **Exemplos** | "O relatório entregue não cobre o que foi briefado"; "A proposta tem dados incorretos"; "O artifact de campanha não reflete nossa marca" |

## 5.2 `admin_support`

| Campo | Valor |
|---|---|
| **Definição** | Problemas de configuração de workspace, gestão de usuários, permissões e integrações |
| **Origem típica** | Admin panel, Command Center (/support), Feedback do tipo `user_feedback` |
| **Prioridade padrão** | P2 |
| **Reviewer obrigatório** | admin ou technical |
| **SLA resposta** | ≤ 4 h |
| **Human handoff** | Quando problema envolve permissões de segurança (escalar para technical) |
| **Exemplos** | "Usuário X não consegue acessar o projeto Y"; "Integração com Google não está sincronizando"; "Workspace não consegue adicionar novo membro" |

## 5.3 `agent_support`

| Campo | Valor |
|---|---|
| **Definição** | Comportamento inesperado de agente: output incorreto, loop, timeout, recusa inesperada, qualidade abaixo do threshold |
| **Origem típica** | Eval system (eval_score abaixo do threshold), Feedback do tipo `agent_feedback`, Command Center |
| **Prioridade padrão** | P2 (loop ou P0 incidente: P1) |
| **Reviewer obrigatório** | technical + metacognik |
| **SLA resposta** | ≤ 4 h |
| **Human handoff** | Após 2 tentativas de re-run sem melhora; após qualquer loop detectado |
| **Exemplos** | "Cognik gerou output com dados inventados"; "Nick entrou em loop de clarificação"; "Agente de coleta falhou 3x sem notificar" |

## 5.4 `billing_support`

| Campo | Valor |
|---|---|
| **Definição** | Problemas relacionados a créditos, consumo inesperado, cobrança errada ou estouro de budget |
| **Origem típica** | Credit wallet alert, Command Center (/credits), Feedback do tipo `user_feedback` |
| **Prioridade padrão** | P1 (suspensão de serviço) ou P2 |
| **Reviewer obrigatório** | admin financeiro ou founder |
| **SLA resposta** | ≤ 1 h (P1); ≤ 4 h (P2) |
| **Human handoff** | Sempre — billing_support nunca resolvido apenas por agente |
| **Referência** | Ver doc 24 (Credits, Plans and Billing Architecture) para detalhes de billing |
| **Exemplos** | "Créditos esgotaram mais rápido do que o esperado"; "Fui cobrado por run que não executei"; "Budget do projeto atingiu limite sem aviso" |

## 5.5 `execution_support`

| Campo | Valor |
|---|---|
| **Definição** | Falhas técnicas de execução: run failed, tool timeout, collector error, workflow stuck |
| **Origem típica** | Runtime error event, eval system, alerting (doc 13 §20) |
| **Prioridade padrão** | P2 (P1 se production-blocking) |
| **Reviewer obrigatório** | technical |
| **SLA resposta** | ≤ 4 h |
| **Human handoff** | Após diagnóstico automático falhar |
| **Exemplos** | "Collector do Apify travou no passo 3"; "Workflow de campanha não completou após 2h"; "Tool timeout em 100% das runs do agente X" |

## 5.6 `security_support`

| Campo | Valor |
|---|---|
| **Definição** | Reportes de incidentes de segurança, violações de policy, acesso indevido ou exposição de dados |
| **Origem típica** | Security event (doc 12 §5.21), user report, audit log alert |
| **Prioridade padrão** | P0 (sempre) |
| **Reviewer obrigatório** | technical + founder |
| **SLA resposta** | ≤ 15 min |
| **Human handoff** | Imediato — nenhum agente trata security_support autonomamente |
| **Escalação especial** | Gera `SupportIncidentDetected` com `is_incident=true`; segue §21 Incident Management |
| **Exemplos** | "Usuário reporta acesso a dados de outro workspace"; "Token exposto em log"; "Comportamento de agente violando privacy policy" |

## 5.7 `incident_support`

| Campo | Valor |
|---|---|
| **Definição** | Incidentes de sistema: indisponibilidade, degradação severa de performance, falha de múltiplos componentes simultâneos |
| **Origem típica** | Alerting (doc 13 §20), monitoring, auto-detection |
| **Prioridade padrão** | P0 ou P1 |
| **Reviewer obrigatório** | technical + founder |
| **SLA resposta** | ≤ 15 min (P0); ≤ 1 h (P1) |
| **Human handoff** | Imediato; war room ativado para P0 |
| **Post-mortem** | Obrigatório para todo P0; recomendado para P1 |
| **Exemplos** | "Plataforma indisponível para workspace X"; "Event bus com backlog crítico"; "Projection engine não atualizando para 3+ projetos" |

## 5.8 `knowledge_support`

| Campo | Valor |
|---|---|
| **Definição** | Dúvidas sobre como usar funcionalidades, falta de documentação, perguntas de how-to |
| **Origem típica** | Command Center, client portal, onboarding flow |
| **Prioridade padrão** | P3 |
| **Reviewer obrigatório** | qa_lead ou support_lead |
| **SLA resposta** | ≤ 24 h |
| **Human handoff** | Quando knowledge base não cobre o caso; oportunidade de novo knowledge article |
| **Exemplos** | "Como configurar um collector de LinkedIn?"; "Quais são os limites do plano Professional?"; "Como adicionar aprovador em um workflow?" |

## 5.9 `onboarding_support`

| Campo | Valor |
|---|---|
| **Definição** | Suporte durante configuração inicial de workspace, integração de sistemas, setup de primeiro projeto |
| **Origem típica** | Onboarding flow, Command Center (novo workspace), admin request |
| **Prioridade padrão** | P2 |
| **Reviewer obrigatório** | admin ou support_lead |
| **SLA resposta** | ≤ 4 h |
| **Human handoff** | Para configurações complexas de whitelabel ou enterprise |
| **Exemplos** | "Como configurar o primeiro projeto com múltiplos workflows?"; "Integração com Slack não está aparecendo para o time"; "Não consigo configurar o branding do workspace" |

## 5.10 `internal_support`

| Campo | Valor |
|---|---|
| **Definição** | Suporte interno da equipe CKOS: builders, ops, QA — problemas de ferramentas internas, pipelines de desenvolvimento, documentação interna |
| **Origem típica** | Equipe interna via Command Center ou formulário interno |
| **Prioridade padrão** | P2 ou P3 |
| **Reviewer obrigatório** | PMO_CKOS ou technical |
| **SLA resposta** | ≤ 4 h (P2); ≤ 24 h (P3) |
| **Human handoff** | Decisão de PMO_CKOS |
| **Exemplos** | "Pipeline de CI está quebrando em todos os PRs"; "Documentação do doc 17 está desatualizada no portal interno"; "Preciso de acesso ao ambiente de staging" |

---

# 6. Support Object Model

Todos os objetos abaixo são documentação arquitetural. Patches sugeridos para doc 11 estão em §27.

## 6.1 `support_tickets` — Tabela principal

```sql
support_tickets
  id                    uuid        PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id             uuid        NOT NULL    -- RLS obrigatório
  org_id                uuid        NOT NULL
  workspace_id          uuid
  project_id            uuid
  ticket_type           text        NOT NULL    -- support_type_enum (§5)
  status                text        NOT NULL DEFAULT 'reported'
                                                -- support_status_enum (§12)
  priority              text        NOT NULL DEFAULT 'p3'
                                                -- p0 | p1 | p2 | p3
  title                 text        NOT NULL
  body                  text        NOT NULL
  body_redacted         text                    -- PII-safe version (obrigatório se has_pii)
  source_channel        text                    -- command_center | feedback | api | email | system | client_portal
  reporter_id           uuid                    -- null para tickets gerados pelo sistema
  reporter_type         text                    -- client | user | admin | agent | system
  owner_id              uuid                    -- human owner atual
  assigned_agent_id     text                    -- agent_id (string do agent_registry)
  category_id           uuid        REFERENCES support_categories(id)
  sla_policy_id         uuid        REFERENCES support_sla_policies(id)
  sla_response_due_at   timestamptz
  sla_resolution_due_at timestamptz
  sla_response_met      boolean
  sla_resolution_met    boolean
  first_response_at     timestamptz
  resolved_at           timestamptz
  closed_at             timestamptz
  resolution_summary    text                    -- obrigatório antes de closed
  root_cause_category   text                    -- obrigatório antes de closed
                                                -- (user_error | config | agent_quality | data_gap |
                                                --  policy | billing | security | system | external | unknown)
  requires_human_handoff boolean   DEFAULT false
  escalation_level      integer   DEFAULT 0
  related_ticket_ids    uuid[]
  related_feedback_id   uuid        REFERENCES feedback_items(id)
  affected_object_type  text                    -- artifact | workflow | node | agent_run | proposal
  affected_object_id    uuid
  is_incident           boolean   DEFAULT false
  incident_severity     text                    -- p0 | p1 | p2 | p3 (só se is_incident)
  is_client_visible     boolean   DEFAULT false -- opt-in explícito obrigatório
  has_pii               boolean   DEFAULT false
  reopened_count        integer   DEFAULT 0
  source_event_id       uuid                    -- evento que criou este ticket
  created_at            timestamptz DEFAULT now()
  updated_at            timestamptz DEFAULT now()
```

**Regras obrigatórias:**
- `tenant_id` + `org_id` obrigatórios em todas as queries (RLS)
- `resolution_summary` e `root_cause_category` obrigatórios antes de `status = closed`
- `is_client_visible DEFAULT false` — nunca exposto ao cliente sem aprovação explícita
- `has_pii = true` → `body_redacted` obrigatório antes de qualquer exibição
- `billing_support` tickets **nunca** resolvidos apenas por agente (requires_human_handoff automático)
- `security_support` e `incident_support` → `is_incident = true` + protocolo §21

---

## 6.2 `support_ticket_events` — Audit trail append-only

```sql
support_ticket_events
  id             uuid        PRIMARY KEY DEFAULT gen_random_uuid()
  ticket_id      uuid        NOT NULL REFERENCES support_tickets(id)
  event_type     text        NOT NULL
                             -- created | classified | assigned | escalated |
                             -- agent_run_started | agent_run_completed |
                             -- human_handoff_required | resolution_proposed |
                             -- resolution_confirmed | resolution_rejected |
                             -- sla_breached | reopened | closed | note_added |
                             -- knowledge_linked | incident_declared
  from_status    text
  to_status      text
  actor_id       uuid                    -- human ou null para sistema
  actor_type     text                    -- human | agent | system
  note           text
  metadata       jsonb
  source_event_id uuid
  created_at     timestamptz DEFAULT now()
```

**Regras:** append-only; nenhum UPDATE ou DELETE permitido; RLS via ticket_id → tenant_id.

---

## 6.3 `support_categories`

```sql
support_categories
  id                   uuid   PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id            uuid   NOT NULL
  name                 text   NOT NULL
  ticket_type          text   NOT NULL
  description          text
  default_priority     text   DEFAULT 'p3'
  default_sla_policy_id uuid  REFERENCES support_sla_policies(id)
  routing_rule         jsonb  -- {owner_role, agent_id, escalation_path}
  created_at           timestamptz DEFAULT now()
  updated_at           timestamptz DEFAULT now()
```

---

## 6.4 `support_sla_policies`

```sql
support_sla_policies
  id                        uuid   PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id                 uuid   NOT NULL
  name                      text   NOT NULL
  priority                  text   NOT NULL  -- p0 | p1 | p2 | p3
  response_time_minutes     integer NOT NULL  -- P0:15 | P1:60 | P2:240 | P3:1440
  resolution_time_hours     integer NOT NULL  -- P0:4  | P1:24  | P2:72  | P3:168
  escalation_at_minutes     integer NOT NULL  -- P0:10 | P1:45  | P2:180 | P3:1200
  warning_at_percent        integer DEFAULT 80 -- % do SLA para warning notification
  notify_channels           text[]            -- email | slack | command_center | pager
  auto_escalate             boolean DEFAULT true
  created_at                timestamptz DEFAULT now()
```

**SLA padrão por prioridade:**

| Prioridade | Nome | Resposta | Resolução | Escalação em | Warning em |
|:----------:|------|:--------:|:---------:|:------------:|:----------:|
| P0 | Critical / Incident | ≤ 15 min | ≤ 4 h | 10 min | 80% (12 min) |
| P1 | High | ≤ 1 h | ≤ 24 h | 45 min | 80% (48 min) |
| P2 | Medium | ≤ 4 h | ≤ 72 h | 3 h | 80% (3 h 12 min) |
| P3 | Low | ≤ 24 h | ≤ 7 d | 20 h | 80% (19 h 12 min) |

---

## 6.5 `support_agent_links`

```sql
support_agent_links
  id                    uuid   PRIMARY KEY DEFAULT gen_random_uuid()
  ticket_id             uuid   NOT NULL REFERENCES support_tickets(id)
  agent_run_id          uuid   NOT NULL
  agent_id              text   NOT NULL
  action_taken          text   NOT NULL  -- description of attempted resolution
  action_type           text             -- diagnose | resolve | escalate | knowledge_lookup | handoff
  resolution_attempted  boolean DEFAULT false
  resolution_succeeded  boolean
  escalation_triggered  boolean DEFAULT false
  eval_score            numeric(3,2)     -- 0.00–1.00
  handoff_reason        text             -- reason for human handoff if triggered
  metacognik_flagged    boolean DEFAULT false
  created_at            timestamptz DEFAULT now()
```

---

## 6.6 `support_resolution_notes`

```sql
support_resolution_notes
  id               uuid   PRIMARY KEY DEFAULT gen_random_uuid()
  ticket_id        uuid   NOT NULL REFERENCES support_tickets(id)
  author_id        uuid   NOT NULL
  author_type      text   NOT NULL  -- human | agent
  body             text   NOT NULL
  body_redacted    text              -- obrigatório se has_pii
  is_internal      boolean DEFAULT true
  is_client_visible boolean DEFAULT false
  note_type        text             -- diagnosis | resolution_attempt | resolution | followup | escalation
  created_at       timestamptz DEFAULT now()
```

---

## 6.7 `friction_signals`

```sql
friction_signals
  id                  uuid   PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id           uuid   NOT NULL
  org_id              uuid   NOT NULL
  workspace_id        uuid
  project_id          uuid
  signal_type         text   NOT NULL
                             -- repeated_ticket_same_type | agent_quality_degradation |
                             -- sla_breach_pattern | billing_anomaly | workflow_stuck_pattern |
                             -- collector_failure_pattern | knowledge_gap |
                             -- client_dissatisfaction_pattern | security_alert_pattern |
                             -- onboarding_friction
  detected_by         text   NOT NULL   -- agent_id ou 'system'
  source_object_type  text              -- artifact | workflow | agent | collector | node
  source_object_id    uuid
  severity            text   DEFAULT 'medium'  -- low | medium | high | critical
  description         text
  pattern_count       integer DEFAULT 1        -- quantos tickets compõem o padrão
  pattern_window_days integer DEFAULT 7        -- janela de tempo do padrão
  last_seen_at        timestamptz DEFAULT now()
  ticket_ids          uuid[]                   -- tickets que compõem o sinal
  feedback_ids        uuid[]                   -- feedbacks relacionados
  status              text   DEFAULT 'detected'
                             -- detected | acknowledged | escalated | converted_to_product_gap |
                             -- resolved | ignored
  acknowledged_by     uuid
  resolution_note     text
  created_at          timestamptz DEFAULT now()
  updated_at          timestamptz DEFAULT now()
```

**Regras de friction_signal:**
- Criado automaticamente quando `pattern_count >= 3` tickets do mesmo tipo em `pattern_window_days`
- Emite evento `SupportFrictionSignalDetected` no event bus
- Status `converted_to_product_gap` → cria feedback_item do tipo `product_feedback` (via aprovação humana)
- Nunca `ignored` sem `resolution_note`

---

## 6.8 `support_knowledge_articles`

```sql
support_knowledge_articles
  id                  uuid   PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id           uuid   NOT NULL
  title               text   NOT NULL
  body                text   NOT NULL
  article_type        text   NOT NULL
                             -- howto | troubleshoot | reference | policy | faq
  ticket_types        text[]            -- tipos de suporte cobertos por este artigo
  tags                text[]
  author_id           uuid   NOT NULL
  status              text   DEFAULT 'draft'
                             -- draft | published | archived
  source_ticket_ids   uuid[]            -- tickets que originaram este artigo
  view_count          integer DEFAULT 0
  helpful_count       integer DEFAULT 0
  not_helpful_count   integer DEFAULT 0
  last_helpful_ratio  numeric(3,2)      -- helpful / (helpful + not_helpful)
  created_at          timestamptz DEFAULT now()
  updated_at          timestamptz DEFAULT now()
```

---

## 6.9 `support_escalation_records`

```sql
support_escalation_records
  id                  uuid   PRIMARY KEY DEFAULT gen_random_uuid()
  ticket_id           uuid   NOT NULL REFERENCES support_tickets(id)
  escalation_level    integer NOT NULL
  escalated_by        uuid               -- actor (human or system)
  escalated_by_type   text               -- human | system
  escalated_to        uuid               -- novo owner (human)
  reason              text   NOT NULL
  trigger             text   NOT NULL    -- sla_breach | agent_failure | manual | policy
  sla_breach_at       timestamptz        -- quando o SLA foi violado (se trigger=sla_breach)
  resolved_at         timestamptz
  created_at          timestamptz DEFAULT now()
```

---

## 6.10 `support_incident_reports`

```sql
support_incident_reports
  id                  uuid   PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id           uuid   NOT NULL
  org_id              uuid   NOT NULL
  ticket_id           uuid   REFERENCES support_tickets(id)   -- pode ser null (auto-detected)
  severity            text   NOT NULL  -- p0 | p1 | p2 | p3
  title               text   NOT NULL
  description         text   NOT NULL
  root_cause          text
  timeline            jsonb              -- [{time, event, actor}] ordered list
  affected_systems    text[]
  affected_project_ids uuid[]
  status              text   DEFAULT 'detected'
                             -- detected | investigating | mitigating | resolved | post_mortem | closed
  detected_at         timestamptz NOT NULL DEFAULT now()
  resolved_at         timestamptz
  post_mortem_doc_url text              -- link para post-mortem (obrigatório para P0)
  lessons_learned     text              -- obrigatório antes de closed
  created_at          timestamptz DEFAULT now()
  updated_at          timestamptz DEFAULT now()
```

---

## 6.11 `support_feedback_links`

```sql
support_feedback_links
  id               uuid   PRIMARY KEY DEFAULT gen_random_uuid()
  ticket_id        uuid   NOT NULL REFERENCES support_tickets(id)
  feedback_item_id uuid   NOT NULL REFERENCES feedback_items(id)
  link_type        text   NOT NULL
                          -- originated_from_feedback | generated_feedback |
                          -- corroborates | escalated_from | resolved_together
  created_by       uuid   NOT NULL
  created_at       timestamptz DEFAULT now()
```

---

## 6.12 `support_roi_links`

```sql
support_roi_links
  id               uuid   PRIMARY KEY DEFAULT gen_random_uuid()
  ticket_id        uuid   NOT NULL REFERENCES support_tickets(id)
  roi_model_id     uuid   NOT NULL REFERENCES roi_models(id)
  link_type        text   NOT NULL
                          -- impacts_efficiency_roi | impacts_retention_roi |
                          -- adds_support_cost | reduces_quality_metric |
                          -- incident_cost | knowledge_investment
  cost_attributed  numeric(12,2)     -- custo de suporte atribuído ao modelo de ROI
  currency         char(3) DEFAULT 'USD'
  note             text
  created_by       uuid   NOT NULL
  created_at       timestamptz DEFAULT now()
```

---

# 7. Support Classification Engine

O Support Classification Engine é o componente de runtime responsável por classificar e enriquecer tickets recém-criados antes do roteamento.

## 7.1 Dimensões de classificação

| Dimensão | Campo | Valores | Quem classifica |
|----------|-------|---------|-----------------|
| Tipo | `ticket_type` | 10 tipos (§5) | Agente (sugere) → human confirma para P0/P1 |
| Prioridade | `priority` | p0/p1/p2/p3 | Agente (baseado em type + keywords + context) |
| Categoria | `category_id` | `support_categories` | Agente (lookup por type + context) |
| SLA Policy | `sla_policy_id` | `support_sla_policies` | Sistema (derivado de priority) |
| PII detection | `has_pii` | bool | Agente de análise de PII (automático) |
| Incidente | `is_incident` | bool | Sistema (p0 security/incident → true automático) |
| Objeto afetado | `affected_object_type/id` | ref | Agente (extração de contexto) |

## 7.2 Regras obrigatórias de classificação

1. `ticket_type` e `priority` são obrigatórios antes de `SupportTicketClassified` ser emitido
2. `security_support` → `priority = p0` + `is_incident = true` automático
3. `incident_support` → `priority = p0` ou `p1` + `is_incident = true` automático
4. `has_pii = true` → `body_redacted` gerado automaticamente antes de qualquer log ou display
5. Classificação de agente para P0/P1 deve ser confirmada por humano antes do SLA iniciar
6. `billing_support` → `requires_human_handoff = true` automático

## 7.3 Fluxo de classificação

```
SupportTicketCreated (event bus)
  → support_classification_agent analisa body + type + context
  → sugere: ticket_type, priority, category_id, affected_object
  → detecta PII → gera body_redacted se has_pii
  → P0/P1: emite SupportTicketCreated com flag pending_human_confirmation
  → P2/P3: classifica diretamente, emite SupportTicketClassified
  → SLA clock inicia em SupportTicketClassified (não em SupportTicketCreated)
```

---

# 8. Support Routing Rules

Após classificação, o ticket é roteado para o owner e/ou agente responsável.

| Tipo | Roteamento padrão | Agente permitido | Human obrigatório | Escalação padrão |
|------|-------------------|:----------------:|:-----------------:|-----------------|
| `client_support` | project_lead | Sim (1ª tentativa) | Sim (após 1 falha) | founder |
| `admin_support` | admin | Sim | Não obrigatório | technical |
| `agent_support` | technical | Sim (diagnóstico) | Após 2 falhas | metacognik |
| `billing_support` | admin financeiro | Não | Sempre | founder |
| `execution_support` | technical | Sim | Após diagnóstico | technical lead |
| `security_support` | technical + founder | Não | Sempre | founder |
| `incident_support` | technical + founder | Não | Sempre | P0: war room |
| `knowledge_support` | support_lead | Sim | Para novos artigos | qa_lead |
| `onboarding_support` | admin | Sim | Para enterprise | support_lead |
| `internal_support` | PMO_CKOS | Sim | Decisão PMO | PMO_CKOS |

**Regras de roteamento:**
1. Se `owner_id` não pode ser determinado pela categoria → emite `SupportTicketAssigned` com `owner_id = null` + alerta para PMO_CKOS
2. Se `assigned_agent_id` não disponível → rota direto para owner humano
3. Se `requires_human_handoff = true` → rota direto para owner humano (agente não inicia)
4. Se `priority = p0` → PMO_CKOS e founder notificados imediatamente independente do tipo

---

# 9. Support SLA Policies

## 9.1 SLA lifecycle

```
SupportTicketClassified
  → sla_response_due_at = classified_at + response_time_minutes
  → sla_resolution_due_at = classified_at + resolution_time_hours * 60
  → warning_at = sla_response_due_at * warning_at_percent / 100
  
Polling do SLA engine (doc 10):
  → now() > warning_at AND NOT first_response_at → emite warning notification
  → now() > sla_response_due_at AND NOT first_response_at → SlaBreached (response)
  → now() > sla_resolution_due_at AND status NOT IN (resolved, closed) → SlaBreached (resolution)
  → SlaBreached → escalation_level++ → SupportTicketEscalated → cria support_escalation_record
```

## 9.2 SLA breach consequences

| Breach | Ação automática | Ação humana requerida |
|--------|-----------------|----------------------|
| Response time warning (80%) | Notificação ao owner | Owner deve responder |
| Response time breached | `SlaBreached` event; escalation_level++ | PMO_CKOS acionado |
| Resolution time at 50% sem progresso | Warning ao owner + lead | Lead deve intervir |
| Resolution time breached | `SlaBreached` event; escalation_level += 2 | Founder notificado para P0/P1 |
| escalation_level >= 3 | Founder e Technical notificados | War room para P0 |

---

# 10. Support ↔ Feedback System

Support e Feedback são sistemas complementares — cada um tem papel distinto mas trocam informação de forma bidirecional.

## 10.1 Fluxos de integração

| Fluxo | Direção | Mecanismo | Regra |
|-------|---------|-----------|-------|
| Feedback gera ticket | Feedback → Support | `feedback_support_links.link_type = originated_from_feedback` | Quando `feedback_items.support_required = true` |
| Ticket gera feedback | Support → Feedback | `support_feedback_links.link_type = generated_feedback` | Quando ticket resolvido revela padrão de produto |
| Friction signal gera feedback | Support → Feedback | `friction_signals.status = converted_to_product_gap` → `feedback_items` | Aprovação humana obrigatória |
| Ticket e feedback corroboram | Bidirecional | `link_type = corroborates` | Mesma issue reportada por dois canais |

## 10.2 Regras de integração

1. Um ticket pode originar de um feedback, mas **nunca** substituí-lo — o feedback item permanece independente
2. A criação de feedback a partir de ticket resolvido é **sugerida** pelo sistema, não automática — requer aprovação do support_lead
3. `friction_signals` → `feedback_items` requer aprovação humana E `feedback_items.decision_required = true`
4. O closure de um ticket **não** fecha automaticamente o feedback relacionado

---

# 11. Support ↔ ROI System

Suporte tem custo. Cada ticket cria custo de operação que impacta o ROI do projeto e do cliente.

## 11.1 Tipos de impacto em ROI

| ROI Type afetado | Mecanismo | Quando |
|-----------------|-----------|--------|
| `efficiency_roi` | Custo de suporte / hora humana | Todo ticket com owner humano |
| `retention_roi` | Client_support não resolvido no SLA → churn risk | `client_support` com SLA breached |
| `operational_roi` | Execution_support recorrente → ineficiência de workflow | `friction_signals` de tipo `workflow_stuck_pattern` |
| `decision_quality_roi` | Agent_support recorrente → qualidade de decisão de agente | `friction_signals` de tipo `agent_quality_degradation` |
| `risk_reduction_roi` | Security_support resolvido → risco evitado | `security_support` com root_cause resolvido |

## 11.2 `support_roi_links` — quando criar

- Ao resolver ticket com custo de human hours > threshold → criar `support_roi_link` com `cost_attributed`
- Ao detectar `friction_signal` de tipo `client_dissatisfaction_pattern` → vincular a `retention_roi`
- Ao resolver `incident_support` P0 → vincular custo de incidente a `risk_reduction_roi`
- Criação de `support_roi_link` é sempre feita por humano ou com confirmação humana — não automático

---

# 12. Support State Machine

O Support State Machine governa o ciclo de vida de cada ticket. Canvas exibe e respeita — não controla.

## 12.1 Estados

| # | Estado | Descrição |
|---|--------|-----------|
| 1 | `reported` | Ticket criado; aguardando classificação |
| 2 | `triaged` | Classificado (type, priority, SLA); aguardando assignment |
| 3 | `assigned` | Owner e/ou agente designados; SLA clock ativo |
| 4 | `in_progress` | Resolução sendo trabalhada ativamente |
| 5 | `awaiting_client` | Aguardando resposta ou informação do cliente/reporter |
| 6 | `awaiting_agent` | Agente executando tentativa de resolução |
| 7 | `pending_knowledge` | Artigo de knowledge base encontrado; aguardando confirmação |
| 8 | `escalated` | Escalado para nível superior (owner ou prioridade) |
| 9 | `pending_review` | Resolução proposta; aguardando confirmação do reporter ou QA |
| 10 | `resolved` | Resolução confirmada com `resolution_summary` e `root_cause_category` |
| 11 | `closed` | Ticket formalmente encerrado após período de confirmação |
| 12 | `reopened` | Reporter ou sistema rejeitou a resolução |
| 13 | `archived` | Estado final após TTL (closed_at + 90 dias default) |

## 12.2 Transições

| De | Para | Evento | Condição |
|----|------|--------|----------|
| `reported` | `triaged` | `SupportTicketClassified` | type, priority, SLA atribuídos |
| `triaged` | `assigned` | `SupportTicketAssigned` | owner_id ou assigned_agent_id definidos |
| `assigned` | `in_progress` | actor inicia trabalho | — |
| `assigned` | `awaiting_agent` | `SupportAgentRunStarted` | agente iniciou run de resolução |
| `in_progress` | `awaiting_client` | owner aguarda info | ticket em espera de resposta |
| `in_progress` | `awaiting_agent` | `SupportAgentRunStarted` | — |
| `in_progress` | `escalated` | `SupportTicketEscalated` | SLA breach ou manual |
| `awaiting_agent` | `in_progress` | `SupportAgentRunCompleted` success=false | agente falhou; retorna a owner humano |
| `awaiting_agent` | `pending_review` | `SupportResolutionProposed` | agente propôs resolução |
| `awaiting_agent` | `in_progress` | `SupportHumanHandoffRequired` | agente atingiu limite de tentativas |
| `pending_knowledge` | `resolved` | reporter confirma | artigo resolve o problema |
| `pending_knowledge` | `in_progress` | reporter rejeita | artigo não resolve; continua |
| `pending_review` | `resolved` | `SupportResolutionConfirmed` | reporter ou QA confirma |
| `pending_review` | `in_progress` | `SupportResolutionRejected` | reporter ou QA rejeita |
| `awaiting_client` | `in_progress` | reporter responde | — |
| `awaiting_client` | `closed` | sem resposta em TTL | timeout policy (ex: 14 dias sem resposta) |
| `escalated` | `assigned` | novo owner designado | — |
| `escalated` | `in_progress` | trabalho retomado com urgência | — |
| `resolved` | `closed` | período de confirmação passa | default: 48h sem reabrir |
| `resolved` | `reopened` | `SupportTicketReopened` | reporter rejeita resolução |
| `closed` | `reopened` | reporter reabre | dentro de TTL de reabertura |
| `reopened` | `triaged` | reclassificação | reinicia fluxo com contexto original |
| `closed` | `archived` | TTL expirado | após 90 dias |
| `any` | `escalated` | `SupportSlaBreached` | SLA violation automática |

## 12.3 Regras da state machine

1. `closed` requer `resolution_summary` NOT NULL + `root_cause_category` NOT NULL
2. `closed` → `archived` é automático após TTL; não pode ser revertido
3. `archived` é estado final — nenhuma transição possível
4. `reopened` incrementa `reopened_count` e emite `SupportTicketReopened`
5. `escalated` incrementa `escalation_level` e cria `support_escalation_record`
6. Toda transição de estado cria entrada em `support_ticket_events`

---

# 13. Support Events

Todos os eventos são publicados no event bus de doc 10 §5.3. Nenhum executa diretamente.

| # | Evento | Publisher | Subscribers | Schema mínimo |
|---|--------|-----------|-------------|---------------|
| 1 | `SupportTicketCreated` | Command Center / Feedback / System | support_classification_agent, alerting | ticket_id, ticket_type, priority, tenant_id |
| 2 | `SupportTicketClassified` | support_classification_agent | support_routing_engine, sla_engine | ticket_id, ticket_type, priority, sla_policy_id |
| 3 | `SupportTicketAssigned` | support_routing_engine | owner (notification), agent_runner | ticket_id, owner_id, assigned_agent_id |
| 4 | `SupportAgentRunStarted` | agent_runner | canvas, dashboard | ticket_id, agent_id, agent_run_id |
| 5 | `SupportAgentRunCompleted` | agent_runner | support_routing_engine, evals | ticket_id, agent_run_id, success, eval_score |
| 6 | `SupportHumanHandoffRequired` | agent_runner / sla_engine | owner (P0 notification), canvas | ticket_id, reason, escalation_level |
| 7 | `SupportResolutionProposed` | agent or human | owner, reporter (notification) | ticket_id, resolution_note_id |
| 8 | `SupportResolutionConfirmed` | reporter / QA / system | projection engine, knowledge_engine | ticket_id, resolved_by, resolution_summary |
| 9 | `SupportResolutionRejected` | reporter / QA | support_routing_engine | ticket_id, rejection_reason |
| 10 | `SupportTicketReopened` | reporter / system | support_routing_engine, canvas | ticket_id, reopened_by, reason |
| 11 | `SupportTicketClosed` | system (after TTL) | projection engine, knowledge_engine | ticket_id, closed_at, root_cause_category |
| 12 | `SupportSlaBreached` | sla_engine | escalation_engine, alerting, founder (P0/P1) | ticket_id, breach_type, escalation_level |
| 13 | `SupportTicketEscalated` | escalation_engine | new owner, canvas | ticket_id, escalation_level, escalated_to |
| 14 | `SupportIncidentDeclared` | system / human | war_room, founder, technical, canvas | ticket_id, incident_id, severity |
| 15 | `SupportFrictionSignalDetected` | friction_detection_engine | canvas, dashboard, feedback_routing_engine | signal_id, signal_type, pattern_count, severity |
| 16 | `SupportKnowledgeArticleLinked` | knowledge_engine | canvas, dashboard | ticket_id, article_id |

---

# 14. Support ↔ Node Canvas

## 14.1 Support Node Types

| Node Type | Quando aparece | Quem pode criar | Agents |
|-----------|---------------|-----------------|--------|
| `support_ticket_node` | Ticket relevante ao projeto (agent_support, execution_support, client_support) | Sistema (ao criar ticket) ou manual | cognik, support_agent |
| `friction_signal_node` | friction_signal com `severity >= medium` | Sistema (automático por friction_detection_engine) | metacognik |
| `incident_node` | `is_incident = true` | Sistema (P0/P1 automático) | — (human only) |
| `knowledge_gap_node` | `ticket_type = knowledge_support` sem artigo | Sistema (sugestão) | cognik |
| `resolution_node` | Resolução proposta para ticket complexo | Agente ou humano | cognik |

## 14.2 Support Edge Types no Canvas

| Edge Type | Significado |
|-----------|-------------|
| `support_for` | support_ticket_node → affected_object_node |
| `originated_from` | support_ticket_node → feedback_node |
| `escalated_to` | support_ticket_node → owner_node |
| `resolved_by` | support_ticket_node → resolution_node |
| `pattern_of` | friction_signal_node → [support_ticket_node, ...] |
| `generates_knowledge` | support_ticket_node → knowledge_gap_node |
| `impacts_roi` | support_ticket_node → roi_node |
| `part_of_incident` | support_ticket_node → incident_node |

## 14.3 Comportamento no Canvas

- Canvas exibe badges de SLA em support_ticket_nodes: verde (no SLA), amarelo (warning), vermelho (breached)
- friction_signal_node exibe `pattern_count` e `severity`
- incident_node exibe status atual e severity com badge P0/P1/P2/P3
- Nenhum node de suporte é excluído do Canvas — apenas arquivado com `archived_at`

---

# 15. Support ↔ Command Center

## 15.1 Intents de suporte (Família #9 — Support & Friction)

| Intent | Exemplo de comando | intent_type | Evento emitido |
|--------|-------------------|-------------|----------------|
| Criar ticket | "Reportar problema com o artifact de campanha" | `action.support.create_ticket` | `SupportTicketCreated` |
| Ver tickets abertos | "Quais suportes estão abertos no projeto?" | `query.support.list_open` | — (consulta projeção) |
| Verificar SLA | "O ticket de suporte do cliente está dentro do SLA?" | `query.support.check_sla` | — |
| Escalar ticket | "Escalar o ticket #X para o Technical Lead" | `action.support.escalate` | `SupportTicketEscalated` |
| Ver fricções | "Quais são os padrões de fricção detectados este mês?" | `query.support.friction_signals` | — |
| Criar knowledge | "Criar artigo de knowledge base a partir do ticket #X" | `action.support.create_knowledge` | `SupportKnowledgeArticleLinked` |
| Declarar incidente | "Declarar incidente P0 — plataforma indisponível" | `action.support.declare_incident` | `SupportIncidentDeclared` |
| Verificar incidente | "Qual o status do incidente declarado?" | `query.support.incident_status` | — |
| Fechar ticket | "Fechar ticket #X com root cause: config error" | `action.support.close_ticket` | `SupportTicketClosed` |
| Ver custo de suporte | "Qual o custo de suporte do projeto este mês?" | `query.support.cost_summary` | — |

---

# 16. Support ↔ Dashboard

## 16.1 Widgets de suporte no Project Dashboard

| Widget | Projection base | Conteúdo | Permissão |
|--------|----------------|----------|-----------|
| **Open Tickets** | `support_friction_projection` | Tickets abertos por tipo e prioridade | project_member any |
| **SLA Status** | `support_friction_projection` | % tickets dentro do SLA; breach count | contributor+ |
| **Friction Signals** | `support_friction_projection` | Sinais detectados; severity; padrão_count | lead+ |
| **Support Cost** | `cost_credit_projection` | Custo de horas humanas de suporte por período | lead+ |
| **Incident Status** | `support_friction_projection` | Incidentes ativos; severity; tempo aberto | admin+ |
| **Agent Resolution Rate** | `support_friction_projection` | % tickets resolvidos por agente sem handoff | technical |

## 16.2 `support_friction_projection` — campos principais

Esta projeção é read-only; alimenta widgets do Dashboard e do Canvas.

```
support_friction_projection:
  open_tickets_count          -- total de tickets em status != closed/archived
  open_by_type                -- {client_support: N, agent_support: N, ...}
  open_by_priority            -- {p0: N, p1: N, p2: N, p3: N}
  sla_compliance_rate         -- % tickets respondidos dentro do SLA (últimos 30d)
  sla_breach_count            -- tickets com breach ativo
  avg_resolution_hours        -- média de resolução por tipo
  friction_signals_active     -- friction_signals em status detected/acknowledged
  friction_signals_by_type    -- {repeated_ticket: N, agent_quality: N, ...}
  incident_count_active       -- incidentes em status != closed
  agent_resolution_rate       -- % tickets com resolution_succeeded = true
  human_handoff_rate          -- % tickets que exigiram human handoff
  reopened_count_30d          -- tickets reabertos nos últimos 30 dias
  knowledge_gap_count         -- knowledge_support sem artigo vinculado
  last_updated_at
```

---

# 17. Support ↔ Billing e Credits

Support tickets do tipo `billing_support` são a interface entre o Support System e o sistema de Credits, Plans and Billing (doc 24).

## 17.1 Regras de integração

1. `billing_support` tickets têm `requires_human_handoff = true` automático — nunca resolvidos apenas por agente
2. O Support System **não acessa** `credit_wallets` ou `billing_events` diretamente — consulta via projeção `cost_credit_projection`
3. Diagnóstico de billing_support requer cross-reference com `credit_transactions` (doc 24) — feito por humano ou agente com permissão `billing_read`
4. Resolution de billing_support pode exigir estorno de crédito (doc 24) — aprovação founder obrigatória
5. `billing_support` com `priority = p1` → notificação imediata ao admin financeiro e founder

## 17.2 Friction signals de billing

| signal_type | Trigger | Ação |
|-------------|---------|------|
| `billing_anomaly` | ≥ 3 billing_support tickets do mesmo workspace em 7 dias | friction_signal → review obrigatório por admin financeiro |
| `credit_exhaustion_pattern` | workspace atinge limite de crédito ≥ 2x em 30 dias | friction_signal → review de plano com founder |
| `unexpected_charge_pattern` | ≥ 2 tickets de cobrança inesperada no mesmo projeto | friction_signal → audit de cost_ledger |

---

# 18. Support ↔ Agents e Evals

## 18.1 Agentes no Support System

| Agente | Papel | Limite |
|--------|-------|--------|
| `support_classification_agent` | Classifica tickets (type, priority, PII, affected_object) | Não pode modificar `sla_policy_id` — apenas sugerir |
| `support_routing_agent` | Determina owner e assigned_agent baseado em routing_rules | Não pode criar owners fora do `user_role_assignments` |
| `support_resolution_agent` | Tenta resolver tickets de `knowledge_support`, `execution_support` | Máximo 2 tentativas antes de `HumanHandoffRequired` |
| `friction_detection_engine` | Detecta padrões em tickets e cria friction_signals | Nunca auto-converte friction_signal para product_gap |
| `knowledge_suggestion_agent` | Sugere artigos de knowledge base ao criar ticket | Sugestão apenas; humano decide criar novo artigo |

## 18.2 Eval targets para agentes de suporte

| Eval Target | Threshold | Fonte |
|-------------|:---------:|-------|
| Classificação correta (type + priority) | ≥ 0.90 accuracy | `support_agent_links.eval_score` comparado com classificação humana |
| Taxa de resolução autônoma | ≥ 0.60 (knowledge/execution) | `support_agent_links.resolution_succeeded` |
| Falsos negativos de PII | = 0 | `has_pii` detectado vs. review humano |
| Human handoff desnecessário | ≤ 0.10 | Tickets com handoff mas resolvíveis por agente |
| Friction signal precision | ≥ 0.80 | Sinais convertidos para product_gap aprovados vs. rejeitados |

## 18.3 Metacognik no Support System

| Situação | Ação do Metacognik |
|----------|-------------------|
| `agent_support` com `eval_score < 0.50` | Flag para revisão de qualidade do agente |
| `friction_signal` de `agent_quality_degradation` | Revisão obrigatória de agent_eval_links relacionados |
| Tentativa de agente resolver `security_support` | Bloqueio imediato + `PolicyViolationDetected` |
| `support_resolution_agent` com > 30% handoff rate | Alert para Technical Lead |

---

# 19. Human Escalation Protocol

## 19.1 Triggers de escalação obrigatória

| Trigger | Condição | Ação |
|---------|----------|------|
| SLA breach (response) | `now() > sla_response_due_at AND NOT first_response_at` | `SlaBreached` + escalation_level++ + notificação owner |
| SLA breach (resolution) | `now() > sla_resolution_due_at AND status NOT IN (resolved, closed)` | `SlaBreached` + escalation_level += 2 + notificação lead |
| Agent failure limit | `support_agent_links.count(ticket_id) >= 2 AND resolution_succeeded = false` | `HumanHandoffRequired` + status = in_progress |
| Security ticket | `ticket_type = security_support` | Imediato: human_handoff + priority = p0 + notificação founder + technical |
| Incident P0 | `is_incident = true AND incident_severity = p0` | War room: notificação founder + technical + PMO_CKOS |
| escalation_level >= 3 | Qualquer ticket | Founder + Technical notificados; PMO_CKOS revisão de protocolo |

## 19.2 Escalation flow

```
SLA breach detectado (sla_engine)
  → escalation_engine acionado
  → cria support_escalation_record
  → incrementa escalation_level
  → SupportTicketEscalated emitido
  → novo owner designado (próximo nível na hierarquia)
  → notificação enviada ao novo owner + ao owner anterior
  → status = escalated
  → se escalation_level >= 3 → founder notificado
```

## 19.3 Human handoff format obrigatório

Quando `HumanHandoffRequired` é emitido, o agente deve registrar em `support_resolution_notes`:

```
HANDOFF REPORT
Ticket ID: {ticket_id}
Tipo: {ticket_type}
Tentativas: {N}
Ações tomadas:
  1. {action_1}
  2. {action_2}
Razão do handoff: {reason}
Diagnóstico atual: {diagnosis}
Próximos passos sugeridos: {suggestions}
Evidências coletadas: {evidence_refs}
```

---

# 20. Knowledge Base System

## 20.1 O que é a Knowledge Base

A Knowledge Base do Support System é um repositório de artigos criados a partir de tickets resolvidos, friction_signals e autoria direta. Não é uma wiki estática — é um sistema vivo alimentado por resolução de tickets.

## 20.2 Ciclo de vida de um knowledge article

```
Ticket resolvido (SupportTicketClosed)
  → knowledge_suggestion_agent verifica: artigo existente cobre este root cause?
  → Se NÃO: sugere criação de artigo → notification ao support_lead
  → support_lead aprova → knowledge article criado (status: draft)
  → knowledge_lead revisa → status: published
  → article vinculado aos tickets de origem (source_ticket_ids)

Novo ticket criado
  → knowledge_suggestion_agent busca artigos por tipo + tags + keywords
  → Se encontrar: SupportKnowledgeArticleLinked emitido
  → status = pending_knowledge se article_type = troubleshoot
  → Reporter confirma resolução → ticket resolved sem human handoff
```

## 20.3 Métricas de qualidade de knowledge articles

| Métrica | Campo | Meta |
|---------|-------|------|
| Helpfulness ratio | `helpful_count / (helpful_count + not_helpful_count)` | ≥ 0.75 |
| Defect rate | Tickets reabertos após artigo vinculado | ≤ 0.15 |
| Coverage | % de `knowledge_support` tickets com artigo vinculado | ≥ 0.60 (MVP P0) |
| Staleness | Artigos com `last_updated > 90d` sem review | 0 (alerta automático) |

## 20.4 Regras de governança da Knowledge Base

1. Artigos **não são gerados automaticamente** — agente sugere, humano aprova e edita
2. Todo artigo publicado tem `author_id` humano obrigatório
3. `source_ticket_ids` deve ter pelo menos 1 ticket de origem
4. Artigos com `last_helpful_ratio < 0.50` por 30 dias → alerta para revisão ou archive
5. Artigos nunca deletados — apenas arquivados (`status: archived`)
6. Cross-reference com `root_cause_category` dos tickets permite agrupar artigos por causa

---

# 21. Incident Management

## 21.1 Definição de incidente

Um incidente é qualquer evento de sistema com impacto real ou potencial em:
- Disponibilidade da plataforma para ≥ 1 workspace/org
- Integridade de dados de clientes
- Segurança (qualquer violação de tenant isolation ou exposição de dados)
- SLA de múltiplos tickets simultâneos (≥ 3 tickets P1 abertos ao mesmo tempo)

## 21.2 Severity levels

| Severity | Critério | SLA resolução | Post-mortem |
|:--------:|----------|:-------------:|:-----------:|
| P0 | Indisponibilidade total ou violação de segurança | ≤ 4 h | Obrigatório |
| P1 | Degradação severa ou ≥ 1 workspace afetado | ≤ 24 h | Recomendado |
| P2 | Degradação parcial; workaround disponível | ≤ 72 h | Opcional |
| P3 | Impacto mínimo; workaround trivial | ≤ 7 d | Não |

## 21.3 Incident lifecycle

```
Detecção (auto ou manual)
  → SupportIncidentDeclared emitido
  → support_incident_report criado
  → founder + technical notificados imediatamente
  → War room ativado (P0/P1)
  
Investigação
  → root_cause identificado
  → affected_systems mapeados
  → timeline atualizada continuamente

Mitigação
  → ação imediata para reduzir impacto
  → status = mitigating

Resolução
  → status = resolved
  → resolved_at preenchido
  → SupportResolutionConfirmed emitido

Post-mortem (P0 obrigatório)
  → root_cause documentado
  → lessons_learned preenchido
  → actions_for_prevention registradas
  → post_mortem_doc_url preenchido
  → status = closed
```

## 21.4 Regras de post-mortem

1. Post-mortem P0 deve ser concluído em ≤ 5 dias após resolução
2. `lessons_learned` obrigatório antes de `closed` para P0/P1
3. Post-mortem gera ≥ 1 action item formal (pode ser friction_signal ou feedback_item)
4. Incident report nunca deletado — apenas `closed` + `archived` após TTL

---

# 22. Support Permissions

## 22.1 Matriz de permissões por role

| Ação | viewer | project_member | contributor | lead | admin | technical | founder |
|------|:------:|:--------------:|:-----------:|:----:|:-----:|:---------:|:-------:|
| Ver tickets próprios | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Criar ticket | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ver todos os tickets do projeto | — | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| Atribuir owner | — | — | — | ✅ | ✅ | ✅ | ✅ |
| Resolver ticket | — | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| Escalar ticket | — | — | — | ✅ | ✅ | ✅ | ✅ |
| Ver friction_signals | — | — | — | ✅ | ✅ | ✅ | ✅ |
| Declarar incidente | — | — | — | — | ✅ | ✅ | ✅ |
| Ver security_support | — | — | — | — | — | ✅ | ✅ |
| Aprovar knowledge article | — | — | — | ✅ | ✅ | ✅ | ✅ |
| Ver custo de suporte | — | — | — | ✅ | ✅ | ✅ | ✅ |
| Aprovar friction → product_gap | — | — | — | — | ✅ | ✅ | ✅ |

## 22.2 Regras de segurança obrigatórias

1. **RLS em todas as tabelas.** `tenant_id` obrigatório; cross-tenant structurally impossible.
2. **`is_client_visible DEFAULT false`.** Tickets e notas nunca expostos ao cliente sem aprovação explícita.
3. **`is_internal DEFAULT true`** em `support_resolution_notes`. Notes internas nunca expostas sem autorização.
4. **`has_pii = true`** → `body_redacted` obrigatório antes de qualquer display ou log.
5. **`security_support` restrito a technical + founder.** Outros roles recebem versão redigida.
6. **Agentes não acessam `support_incident_reports`.** Apenas componentes técnicos de diagnóstico.
7. **`billing_support` requer `billing_read` permission** para agentes de diagnóstico.
8. **Toda escalação cria `support_escalation_record`** — auditabilidade obrigatória.

---

# 23. Support QA Checklist

## 23.1 Checklist de qualidade (SU1–SU14)

| # | Item | Critério |
|---|------|---------|
| SU1 | Cobertura de tipos | Todos os 10 support types cobertos com routing e SLA |
| SU2 | SLA policies | 4 prioridades com response, resolution e escalation times definidos |
| SU3 | State machine | 13 estados com transições completas e regras de bloqueio |
| SU4 | Events | 16 eventos com publisher, subscriber e schema mínimo |
| SU5 | Human handoff | Protocolo definido com trigger automático + format obrigatório |
| SU6 | Incident management | Severity levels, SLA, war room, post-mortem obrigatório para P0 |
| SU7 | Knowledge base | Ciclo de vida de artigos, métricas, governança definidos |
| SU8 | Friction signals | Detecção automática, pattern_count threshold, status lifecycle |
| SU9 | RLS | `tenant_id` em todas as tabelas; regras de segurança completas |
| SU10 | PII handling | `has_pii` → `body_redacted` obrigatório; validado no schema |
| SU11 | Client visibility | `is_client_visible DEFAULT false` em tickets e notas |
| SU12 | ROI integration | `support_roi_links` com cost_attributed; impactos por roi_type |
| SU13 | Feedback integration | `support_feedback_links` bidirecionais; friction → product_gap com aprovação |
| SU14 | Agent eval targets | 5 eval targets com thresholds para agentes de suporte |

## 23.2 Critérios de rejeição automática

1. Tabela principal sem `tenant_id` (RLS violation)
2. `billing_support` sem `requires_human_handoff = true` automático
3. `security_support` com agente como único resolver
4. `closed` permitido sem `resolution_summary` + `root_cause_category`
5. `approved_for_application` em `feedback_learning_signals` sem aprovação humana explícita

---

# 24. MVP P0

## 24.1 O que entra no MVP P0

| Componente | Escopo P0 |
|-----------|-----------|
| Support types | `client_support`, `admin_support`, `agent_support`, `execution_support` |
| State machine | Todos os 13 estados (mas `incident_*` simplificado) |
| SLA policies | P1, P2, P3 (P0/incident: protocolo manual no MVP) |
| Human handoff | Protocolo completo + format obrigatório |
| Friction signals | Detecção automática para `repeated_ticket_same_type` e `agent_quality_degradation` |
| Eventos | `SupportTicketCreated`, `SupportTicketClassified`, `SupportTicketAssigned`, `SupportAgentRunStarted/Completed`, `SupportHumanHandoffRequired`, `SupportResolutionConfirmed`, `SupportTicketClosed`, `SupportSlaBreached`, `SupportFrictionSignalDetected` |
| Command Center | `/support` — criar, ver, escalar tickets |
| Dashboard widget | Open Tickets + SLA Status |
| Node Canvas | `support_ticket_node` + `friction_signal_node` |
| Knowledge Base | Estrutura criada; artigos manuais apenas (sem auto-suggestion no P0) |
| Objects | `support_tickets`, `support_ticket_events`, `support_sla_policies`, `support_categories`, `support_resolution_notes`, `friction_signals`, `support_agent_links` |

## 24.2 O que fica fora do MVP P0

| Componente | Motivo do deferral | Urgência |
|-----------|--------------------|----------|
| `billing_support` | Requer doc 24 completo | P1 — após doc 24 |
| `security_support` avançado | Requer protocolo de incident management completo | P1 |
| `incident_support` completo | War room, post-mortem formal, `support_incident_reports` | P1 |
| Knowledge Base auto-suggestion | Requer knowledge_suggestion_agent treinado com base de tickets | P1 |
| Support ↔ ROI links | Requer doc 21 integrado + cost_attribution logic | P1 |
| Friction → product_gap conversão | Requer integração Feedback System | P1 |
| `knowledge_support` e `onboarding_support` | P3 tickets — não bloqueiam P0 | P2 |
| `internal_support` | Uso interno apenas — não bloqueia produto | P2 |
| `support_escalation_records` | Escalação P0 é manual no MVP | P1 |
| `support_incident_reports` | Post-mortem formal | P1 |

---

# 25. Failure Modes

| # | Failure Mode | Sintoma | Mitigação |
|---|---|---|---|
| FM-S1 | Ticket criado sem classificação | `ticket_type` null → SLA não inicia | `SupportTicketCreated` bloqueia se `ticket_type` ausente |
| FM-S2 | SLA policy ausente para a prioridade | SLA clock não inicia → breach silencioso | `sla_policy_id` obrigatório antes de `SupportTicketClassified` |
| FM-S3 | Agente em loop de resolução | Tentativas infinitas sem handoff | `support_agent_links.count(ticket_id) >= 2` → `HumanHandoffRequired` automático |
| FM-S4 | PII no ticket exposto em log | `body` com dados sensíveis no audit trail | `has_pii = true` → `body_redacted` obrigatório antes de qualquer write em `support_ticket_events` |
| FM-S5 | Ticket fechado sem root cause | Knowledge base não alimentado; padrão invisível | `closed` bloqueado se `root_cause_category = null` |
| FM-S6 | Escalação sem novo owner | Ticket orphan com `escalation_level++` mas sem responsável | `support_escalation_record.escalated_to` obrigatório; se null → notificação PMO_CKOS |
| FM-S7 | Incident P0 não declarado | `security_support` tratado como P2 | `ticket_type = security_support` → `is_incident = true` e `priority = p0` automático |
| FM-S8 | Friction signal sem tickets vinculados | Sinal sem evidência → falso positivo invisível | `friction_signals.ticket_ids` mínimo 1 item obrigatório |
| FM-S9 | `support_resolution_note` com `is_client_visible = true` sem aprovação | Dados internos expostos ao cliente | `is_client_visible = true` requer `lead+` permission; auditado |
| FM-S10 | `billing_support` resolvido por agente | Estorno ou ajuste financeiro sem autorização humana | `billing_support` → `requires_human_handoff = true` automático; agente bloqueado de `resolution_confirmed` |
| FM-S11 | Knowledge article auto-publicado | Informação incorreta na KB sem revisão | `status: published` requer `author_id` humano + review; agente só cria `draft` |
| FM-S12 | Ticket reaberto sem contexto | Owner perde histórico; resolução duplicada | `reopened` → copia contexto original em `support_resolution_notes` automaticamente |
| FM-S13 | `friction_signal` convertido para product_gap sem aprovação | Feedback_item criado sem owner | `friction_signals.status = converted_to_product_gap` requer aprovação humana (lead+) |
| FM-S14 | Ticket de `security_support` visível para contributor | Dados sensíveis de incidente expostos | RLS por role + `security_support` → filtro de visibilidade em todas as projeções |
| FM-S15 | Post-mortem P0 não concluído em 5 dias | Lições não documentadas; risco repetido | Alert automático ao founder após 5 dias sem `post_mortem_doc_url` |
| FM-S16 | `support_roi_links` criados sem `cost_attributed` | ROI de suporte invisível | `cost_attributed` NOT NULL com DEFAULT 0.00 obrigatório; alert se 0.00 após 24h |
| FM-S17 | SLA breach silencioso | `sla_resolution_due_at` passa sem evento | SLA engine (doc 10) deve polling a cada 5 min para tickets em status aberto |
| FM-S18 | Human handoff sem handoff report | Owner não tem contexto | `HumanHandoffRequired` bloqueia se `support_resolution_notes` sem nota do tipo `diagnosis` |
| FM-S19 | Incident sem `affected_systems` | Post-mortem incompleto | `support_incident_reports.affected_systems` mínimo 1 item para P0 |
| FM-S20 | Tenant cross-reference em friction_signal | Padrão de um tenant afeta análise de outro | `friction_signals` sempre scoped por `tenant_id`; analytics cross-tenant apenas em admin role global |

---

# 26. Support como Aprendizado Sistêmico

O Support System não é um endpoint de resolução — é um ponto de entrada de aprendizado contínuo.

## 26.1 Fluxos de aprendizado saindo do suporte

| Saída | Destino | Mecanismo | Aprovação |
|-------|---------|-----------|-----------|
| Root cause patterns → knowledge articles | Knowledge Base | `knowledge_suggestion_agent` sugere; humano aprova | support_lead |
| Friction signals → product_gap | Feedback System (`feedback_items`) | `friction_signals.status = converted_to_product_gap` | lead+ |
| Agent resolution failures → eval scores | Evals (doc 13) | `support_agent_links.eval_score` alimenta `eval_results` | automático |
| Incident lessons → architecture improvements | Architecture process | Post-mortem → ticket interno → doc update | technical + founder |
| SLA breach patterns → SLA policy review | Support SLA Policies | friction_signal `sla_breach_pattern` → review de policy | admin |
| Client dissatisfaction pattern → ROI impact | ROI System | `support_roi_links` → `retention_roi` impact | lead+ |

## 26.2 Invariante de fechamento de loop

> Todo ticket fechado deve ter pelo menos um de: knowledge article criado, friction_signal incrementado, feedback_item gerado, ou `root_cause_category` documentado como `no_pattern_detected`.

Esta invariante garante que suporte nunca é um black hole de informação.

---

# 27. Patches Sugeridos para Outros Docs

Os patches abaixo foram identificados durante a criação deste documento. Estão **registrados como sugestões** — não aplicados. Requerem aprovação Technical + PMO_CKOS antes de aplicar.

| Patch | Doc alvo | Descrição | Urgência |
|-------|----------|-----------|----------|
| **P23-1** | Doc 11 v1.3.x | Tabela `support_knowledge_articles` — schema completo com `source_ticket_ids`, `helpful_count`, `last_helpful_ratio`, RLS por `tenant_id` | Antes de Knowledge Base MVP |
| **P23-2** | Doc 11 v1.3.x | Tabela `support_escalation_records` — schema completo com `escalation_level`, `escalated_by_type`, `sla_breach_at` | Antes de Escalation Protocol MVP |
| **P23-3** | Doc 11 v1.3.x | Tabela `support_incident_reports` — schema completo com `timeline jsonb`, `affected_systems text[]`, `post_mortem_doc_url`, `lessons_learned` | Antes de Incident Management P1 |
| **P23-4** | Doc 11 v1.3.x | Tabela `support_feedback_links` — schema completo (bidirectional: ticket → feedback e feedback → ticket) | Antes de Gate I |
| **P23-5** | Doc 11 v1.3.x | Expandir `support_friction_projection` em §21 com campos: `agent_resolution_rate`, `human_handoff_rate`, `knowledge_gap_count`, `sla_compliance_rate`, `avg_resolution_hours_by_type` | Antes de Gate F |
| **P23-6** | Doc 10 v1.2.x | Registrar `support_classification_agent`, `friction_detection_engine`, `support_routing_engine` e `sla_engine` como componentes nomeados do runtime no §5.2 (flow) e §5.4 (component registry) | Antes de Gate G |

> Patches P23-1 a P23-6 registrados. Não aplicar sem aprovação formal Technical + PMO_CKOS e versão incremental nos docs afetados.

---

# 28. Edge Cases

| # | Caso | Comportamento esperado |
|---|------|----------------------|
| EC-S1 | Ticket criado por agente sem `reporter_type = agent` | `reporter_type` validado no schema; agent-created tickets têm `reporter_id = null` + `reporter_type = agent` |
| EC-S2 | SLA policy não definida para a prioridade | Ticket criado com `sla_policy_id = null`; alerta para PMO_CKOS; SLA clock suspenso |
| EC-S3 | Owner designado sem `support_read` permission | Routing engine rejeita; alerta; ticket volta para `triaged` |
| EC-S4 | Ticket `security_support` criado por usuário sem `security_read` | Ticket criado; conteúdo redigido para o reporter; visível apenas a technical + founder |
| EC-S5 | Agente tenta `closed` sem `resolution_summary` | Bloqueado por policy; `PolicyViolationDetected` emitido |
| EC-S6 | friction_signal com `pattern_count = 1` | Não gera sinal; apenas registra primeiro ticket; threshold = 3 para signal criação |
| EC-S7 | Ticket `billing_support` com agente como único assignee | `requires_human_handoff = true` ativado automaticamente; agente pode fazer diagnóstico mas não pode `resolved` |
| EC-S8 | Incident P0 sem `affected_systems` preenchido | `post_mortem` bloqueado até `affected_systems` ter ≥ 1 item |
| EC-S9 | Reporter não responde em `awaiting_client` por 14 dias | Auto-close com `root_cause_category = user_no_response`; knowledge_suggestion_agent não cria artigo |
| EC-S10 | Knowledge article com `last_helpful_ratio < 0.50` por 30 dias | Alert para support_lead; auto-status = `archived` se não revisado em mais 15 dias |
| EC-S11 | `support_roi_links` criado com `cost_attributed = 0.00` | Aceito com warning; alert ao lead após 24h para completar o custo atribuído |
| EC-S12 | Ticket reaberto após `archived` | Bloqueado — `archived` é estado final; novo ticket deve ser criado com `related_ticket_ids` apontando para o arquivado |
| EC-S13 | friction_signal criado em tenant sem lead | Sinal criado; notificação para PMO_CKOS; `acknowledged_by` fica null até PMO_CKOS designar owner |
| EC-S14 | Dois incidentes P0 simultâneos no mesmo tenant | Dois `support_incident_reports` independentes; war rooms separados; `affected_systems` podem se sobrepor — rastreado explicitamente |

---

# 29. Related Notes

- `../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md` — Event bus, component registry, state machine registry
- `../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md` — §32 Support System Data Model (tabelas base: support_tickets, support_ticket_events, support_categories, support_sla_policies, support_agent_links, support_resolution_notes, friction_signals); §21 projeções (support_friction_projection)
- `../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md` — RLS, tenant isolation, security events, deny-by-default
- `../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md` — Eval targets para agentes de suporte; alerting (§20); cost guard
- `../04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md` — Dashboard widgets de suporte; projeções
- `../04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md` — `/support` command; Família #9 de intenções
- `../04_PRODUCT_SYSTEM/16_NODE_CANVAS_ARCHITECTURE.md` — support_ticket_node, friction_signal_node, incident_node
- `../05_IMPLEMENTATION_SYSTEM/17_IMPLEMENTATION_PROTOCOL.md` — Gate I (Business Systems); ondas de implementação
- `../05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md` — SU1–SU7 checklist; veto Metacognik; approval actors
- `21_ROI_ARCHITECTURE.md` — ROI types impactados por suporte; support_roi_links
- `22_FEEDBACK_SYSTEM_ARCHITECTURE.md` — Feedback ↔ Support links; friction → product_gap; feedback_support_links
- `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md` — billing_support integration; credit_wallet; billing_events
- `../ARCHITECTURE_PATCH_REPORT.md` — §23: registro de conclusão deste documento; patches P23-1 a P23-6
- `../QA_DOCUMENTATION_CHECKLIST.md` — Checklist SU1–SU14 aplicado a este documento

---

## Patch 1.0.0 — Criação

**Data:** 2026-05-25  
**Autor:** PMO_CKOS + Cognik (doc owner)  
**Revisores:** Metacognik, QA Lead  
**Status:** draft — aguarda aprovação Founder + Technical + Metacognik

**O que este documento cobre:**
- Support System como terceiro documento do Business Systems layer (06_BUSINESS_SYSTEMS/)
- 10 support types com especificação completa por tipo
- 12 objetos com schemas SQL completos
- 4-tier SLA policy com response/resolution/escalation times
- 13-state support state machine com transições completas
- 16 eventos conectados ao event bus de doc 10
- Human Escalation Protocol com triggers automáticos e format obrigatório
- Knowledge Base System com governança e métricas de qualidade
- Incident Management com severity levels e post-mortem obrigatório para P0
- Friction Signal detection com pattern_count threshold e lifecycle
- 6 patches sugeridos para docs 10 e 11 (não aplicados)

**Dependência de Gate I:**
Este documento é o terceiro dos quatro documentos obrigatórios para Gate I (Business Systems Gate) conforme doc 20 §7 Gate I e doc 17 §30. Restante: `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`.
