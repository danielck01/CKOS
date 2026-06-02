---
title: Credits, Plans and Billing Architecture
file: 24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md
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
  Feedback System Architecture (22 v1.0.0);
  Support System Architecture (23 v1.0.0)
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
  - 23_SUPPORT_SYSTEM_ARCHITECTURE.md
  - ../ARCHITECTURE_PATCH_REPORT.md
  - ../QA_DOCUMENTATION_CHECKLIST.md
outputs: >
  Credits, Plans and Billing System definition;
  4 plan tiers with feature gates and limits;
  Credit consumption model with reservation pattern;
  Quota enforcement (soft + hard limits);
  Billing Object Model (13 objects with SQL schemas);
  Internal cost vs. external billing distinction;
  Subscription State Machine (6 states);
  Invoice State Machine (7 states);
  16 Billing Events mapped to event bus;
  Overage and upgrade flows;
  Invoice generation protocol;
  Billing Disputes;
  Whitelabel billing model;
  MVP P0 scope;
  20 Failure Modes;
  6 patches suggested for docs 10/11 (not applied)
---

> **Tese central do Credits, Plans and Billing System:**  
> "Billing in CKOS is not a payment gateway integration. It is a governed monetization layer that translates runtime consumption into customer-facing value exchanges — with credit pre-reservation, quota enforcement, transparent invoicing, and a clean separation between what CKOS spends internally and what the customer is charged."

> **Princípio central:**  
> "Internal runtime cost and external customer billing are distinct systems that must never be confused: cost_ledger tracks what CKOS spends; billing_events track what customers owe. Only explicit billing events — not cost_ledger entries — generate charges."

---

# 1. Propósito

O Credits, Plans and Billing System da CKOS resolve um problema estrutural de operação comercial: toda plataforma de AI-first que executa agents, workflows, collectors e artifact generators **consome recursos com custo real** — e essa relação de consumo precisa ser governada tanto internamente (cost_ledger do runtime) quanto externamente (o que o cliente paga).

Sem uma arquitetura de billing governada:
- Consumo de créditos pode causar saldo negativo em condições de concorrência
- A distinção entre custo interno de runtime e valor cobrado do cliente colapsa
- Quotas e limites de plano não são enforced de forma consistente
- Overages podem ocorrer sem notificação ou aprovação
- Invoicing não tem rastreabilidade de usage events
- Whitelabel billing não tem isolamento de tenant

O Credits, Plans and Billing System define:

- **Plans** — tiers de funcionalidade e limites de consumo por org/workspace
- **Credits** — unidade universal de consumo com pré-reserva atômica
- **Quota Enforcement** — limites soft (warn) e hard (block) por recurso
- **Billing Events** — source of truth de cobranças (distintos do cost_ledger)
- **Invoicing** — geração de faturas a partir de usage_events e billing_events
- **Overage flows** — o que acontece quando o cliente excede o plano
- **Upgrade/Downgrade** — fluxos de mudança de plano com aprovação e proratização
- **Disputes** — gestão de disputas de cobrança com rastreabilidade
- **Whitelabel Billing** — billing separado por tenant para clientes whitelabel

---

# 2. O que é / O que NÃO é o Credits, Plans and Billing System

## O que é

| É | Descrição |
|---|-----------|
| **Camada de monetização governada** | Traduz consumo de runtime em valor cobrado do cliente com rastreabilidade |
| **Sistema de créditos com reserva atômica** | `credit_reservations` previnem saldo negativo em condições de concorrência |
| **Enforcement de quotas por plano** | Limites soft (warn) e hard (block) por resource_type, por plano |
| **Source of truth de cobranças** | `billing_events` — não `cost_ledger` — são a origem de faturas |
| **Integrador de Business Systems** | Conecta com ROI (custo vs. valor), Support (billing_support), Feedback (friction billing) |
| **Base de Whitelabel** | Billing separado por tenant permite operação comercial multi-brand |

## O que NÃO é

| Não é | Por quê |
|-------|---------|
| **O cost_ledger** | `cost_ledger` (doc 11 §18) é custo interno de runtime — tokens, tools, models. Billing é o que o cliente paga. São sistemas distintos que interagem mas não são equivalentes |
| **Gateway de pagamento** | Este doc define a arquitetura de billing; a integração com Stripe/Paddle/etc. é uma dependência de implementação — não definida aqui |
| **Sistema de preços hardcoded** | Preços, credit rates e exchange rates ficam em tabelas configuráveis — nunca hardcoded em código |
| **Apenas para SaaS** | O billing model suporta SaaS, whitelabel e enterprise com quotas e estruturas distintas |
| **Transparente para agentes** | Agentes não têm acesso direto a billing_events ou credit_wallets — somente via APIs com permissão explícita |

---

# 3. Princípio Central

> **"Internal runtime cost and external customer billing are distinct systems that must never be confused: cost_ledger tracks what CKOS spends; billing_events track what customers owe. Only explicit billing events — not cost_ledger entries — generate charges."**

Esta separação é a invariante arquitetural mais crítica do sistema de billing:
- Um `model_call` gera entrada no `cost_ledger` (custo interno) e pode gerar `usage_event` (cobrança ao cliente) — mas estas são entidades distintas com tabelas distintas
- A conversão de custo interno para cobrança ao cliente é mediada por `credit_rate_config` e nunca é automática
- Um `cost_ledger` entry sem `usage_event` correspondente não gera cobrança

---

# 4. Filosofia do Credits, Plans and Billing System

1. **Transparência de consumo.** Todo cliente pode ver seu consumo em tempo real — créditos usados, reservados, disponíveis — sem atraso de mais de 30 segundos.
2. **Pré-reserva obrigatória.** Nenhuma operação que consome créditos inicia sem `CreditReserved` bem-sucedido — previne saldo negativo sob concorrência.
3. **Billing events como source of truth.** Faturas são geradas exclusivamente de `usage_events` e `billing_events` — jamais diretamente de `cost_ledger`, `model_calls` ou `agent_runs`.
4. **Quota enforcement consistente.** Limites de plano são validados no `quota_engine` antes de cada operação — não apenas em batch ou post-hoc.
5. **Separação custo/billing.** `cost_ledger` e `billing_events` são sistemas distintos com tabelas distintas. A taxa de conversão é configurável por plano e nunca hardcoded.
6. **Notificação proativa.** Warning em 80% da quota (soft_limit); block em 100% (hard_limit); notificação de overage antes de cobrar.
7. **Aprovação humana para overages.** Consumo acima do plano requer aprovação explícita (founder ou admin) — nunca automático.
8. **Invoices auditáveis.** Toda invoice tem `usage_event_ids[]` — linha de itens rastreável até o evento que gerou a cobrança.
9. **Whitelabel isolation.** Billing de tenants whitelabel é totalmente isolado — `tenant_id` em todas as tabelas; cross-tenant impossível estruturalmente.
10. **Disputas com rastreabilidade.** Toda disputa tem razão documentada, audit trail e resolução formal — nunca silenciosa.
11. **Secrets em vault.** Tokens de gateway de pagamento (Stripe secret key, etc.) nunca em tabelas normais — apenas `secret_ref` apontando para vault externo.
12. **Planos como feature gates.** Um plano não é apenas um preço — é uma coleção de features habilitadas, limites de recursos e políticas de overage.

---

# 5. Plans Architecture

## 5.1 Plan Tiers

O CKOS opera com 4 planos padrão, configuráveis por tenant. Valores são exemplificativos — preços reais ficam em `plans.price_config`.

| Plan | Código | Modelo | Credits/mês | Agent Runs | Workspaces | Projetos ativos |
|------|--------|--------|:-----------:|:----------:|:----------:|:---------------:|
| Free | `free` | Gratuito | 500 | 50 | 1 | 2 |
| Starter | `starter` | Mensal/Anual | 5.000 | 500 | 3 | 10 |
| Professional | `professional` | Mensal/Anual | 25.000 | ilimitado* | 10 | ilimitado |
| Enterprise | `enterprise` | Customizado | Configurável | Configurável | Configurável | Configurável |

*"ilimitado" = sem quota rígida; soft_limit ativa notificação.

## 5.2 Feature gates por plano

| Feature | Free | Starter | Professional | Enterprise |
|---------|:----:|:-------:|:------------:|:----------:|
| Agentes básicos (Nick, Cognik) | ✅ | ✅ | ✅ | ✅ |
| Node Canvas | ✅ | ✅ | ✅ | ✅ |
| Command Center | ✅ | ✅ | ✅ | ✅ |
| Collectors externos (Apify, etc.) | — | ✅ | ✅ | ✅ |
| ROI Architecture completo | — | Básico | ✅ | ✅ |
| Metacognik (audit completo) | — | — | ✅ | ✅ |
| Whitelabel | — | — | Básico | Completo |
| Suporte dedicado | — | — | — | ✅ |
| SLA customizado | — | — | — | ✅ |
| Billing separado por cliente | — | — | — | ✅ |
| Custom agent_registry | — | — | ✅ | ✅ |
| Admin financeiro (invoices, analytics) | — | Limitado | ✅ | ✅ |

## 5.3 Limites por plano (`plan_limits`)

| Resource Type | Free | Starter | Professional | Enterprise |
|---------------|:----:|:-------:|:------------:|:----------:|
| `credit_quota_monthly` | 500 | 5.000 | 25.000 | Configurável |
| `agent_runs_monthly` | 50 | 500 | Sem hard limit | Configurável |
| `storage_gb` | 1 | 10 | 100 | Configurável |
| `collector_runs_daily` | 5 | 50 | 500 | Configurável |
| `artifact_generations_monthly` | 10 | 100 | Sem hard limit | Configurável |
| `active_projects` | 2 | 10 | Sem hard limit | Configurável |
| `workspace_members` | 3 | 10 | 50 | Configurável |
| `model_calls_per_minute` | 10 | 30 | 100 | Configurável |

## 5.4 Overage policies por plano

| Plan | Overage policy | Notificação | Aprovação |
|------|---------------|-------------|-----------|
| Free | `hard_block` — sem overage | 80% + 95% | — |
| Starter | `warn_then_block` — notifica; bloqueia se não aprovado | 80% | Admin |
| Professional | `warn_then_charge` — notifica; cobra se aprovado | 80% | Admin ou Founder |
| Enterprise | `custom` — definido no contrato | Configurável | Configurável |

---

# 6. Credits Architecture

## 6.1 O que é um crédito

Um crédito é a **unidade universal de consumo** do CKOS. É a abstração entre o custo real de runtime (tokens, compute, APIs) e o valor cobrado do cliente. A taxa de conversão custo→crédito é configurável via `credit_rate_config` e nunca hardcoded.

**Propriedades de um crédito:**
- É indivisível na camada de billing (integer ou com precisão de 0.01)
- É escopo-específico: créditos de um org/workspace não são transferíveis para outro
- Tem TTL configurável: créditos comprados podem ter data de expiração
- É auditável: toda movimentação tem entrada em `credit_transactions`

## 6.2 Tipos de consumo de crédito

| Resource Type | Unidade | Taxa exemplo (configurável) | Quem consome |
|---------------|---------|:---------------------------:|-------------|
| `agent_run` | por run | 1–10 créditos | Agente |
| `model_call_small` | por chamada | 0.1 crédito | Runtime |
| `model_call_large` | por chamada | 1–5 créditos | Runtime |
| `model_call_vision` | por chamada | 2–8 créditos | Runtime |
| `collector_run` | por execução | 2 créditos | Collector |
| `artifact_generation` | por artifact | 5 créditos | Artifact engine |
| `storage_gb_month` | por GB/mês | 10 créditos | Storage |
| `rag_query` | por query | 0.5 crédito | RAG engine |
| `research_run` | por run | 5–20 créditos | Research pipeline |
| `export` | por export | 1 crédito | Data layer |

**Nota:** Taxas acima são exemplificativas. Os valores reais ficam exclusivamente em `credit_rate_config` — nunca em código-fonte. Toda mudança de taxa requer Founder approval + versão da config.

## 6.3 Ciclo de vida de créditos

```
Estado de créditos em credit_wallets:
  balance_available   — créditos disponíveis para uso
  balance_reserved    — créditos pré-reservados (em uso em runs ativas)
  balance_total       = balance_available + balance_reserved
  balance_lifetime    — total de créditos adquiridos (histórico)
  
Regra fundamental:
  balance_available NUNCA pode ser negativo
  balance_reserved NUNCA pode exceder balance_total
  
Tentativa de consumo sem reserva prévia → bloqueada
Tentativa de reservar mais do que balance_available → bloqueada
```

---

# 7. Credit Reservation Pattern

O credit reservation pattern é o mecanismo que previne saldo negativo sob operações concorrentes.

## 7.1 Fluxo de reserva e consumo

```
1. RESERVA (antes de iniciar o run)
   → quota_engine verifica: balance_available >= estimated_cost
   → Se NÃO: QuotaHardLimitReached → run bloqueado
   → Se SIM: CreditReserved emitido
              credit_reservations criada (id, wallet_id, amount, run_id, expires_at)
              balance_available -= amount
              balance_reserved += amount

2. EXECUÇÃO (run em progresso)
   → credit_reservation ativa até o run terminar ou TTL expirar
   → Se TTL expira: CreditReservationExpired → balance_reserved -= amount; balance_available += amount

3. CONSUMO (run concluído com sucesso)
   → actual_cost calculado (pode diferir do estimated_cost)
   → CreditConsumed emitido
   → credit_transactions criada (tipo: consumption; amount: actual_cost)
   → balance_reserved -= reservation_amount
   → balance_available += (reservation_amount - actual_cost)  [devolve diferença]
   → credit_reservations.status = consumed

4. LIBERAÇÃO (run falhou ou cancelado)
   → CreditReservationReleased emitido
   → balance_reserved -= reservation_amount
   → balance_available += reservation_amount
   → credit_reservations.status = released
   → Charge parcial possível se partial_consumption_allowed na policy

5. EXPIRAÇÃO (TTL atingido sem conclusão)
   → CreditReservationExpired emitido
   → balance_reserved -= reservation_amount
   → balance_available += reservation_amount
   → credit_reservations.status = expired
   → run_id associado → support ticket automático (tipo: execution_support)
```

## 7.2 Regras obrigatórias do reservation pattern

1. **Nenhum run inicia sem `CreditReserved` bem-sucedido** — não há exceção
2. **`credit_reservations` é a única fonte de `balance_reserved`** — nunca calculado ad-hoc
3. **`actual_cost` pode ser menor mas nunca maior que `reservation_amount`** sem nova reserva incremental
4. **TTL obrigatório** em toda reserva — sem TTL, reserva fica presa se run nunca completar
5. **Deduplication key** em `credit_transactions` — `idempotency_key` previne double-charge
6. **`balance_available` é NEVER negative** — constraint de banco de dados + validação na camada de aplicação

---

# 8. Quota Architecture

## 8.1 Quota types

| Quota Type | Enforcement | Comportamento no limite | Reset |
|------------|:-----------:|------------------------|-------|
| `monthly_credits` | Hard limit | Bloqueia; notify founder/admin | Todo mês |
| `daily_agent_runs` | Soft + Hard | 80%: warn; 100%: block | Todo dia |
| `monthly_storage_gb` | Soft | 80%: warn; 100%: alert + block uploads | Todo mês |
| `per_minute_model_calls` | Hard (rate limit) | 429; backoff; queue se permitido | Por minuto |
| `daily_collector_runs` | Soft + Hard | 80%: warn; 100%: block | Todo dia |
| `monthly_artifacts` | Soft | 80%: warn; sem hard block (Professional+) | Todo mês |

## 8.2 Quota enforcement flow

```
Antes de qualquer operação consumidora:
  → quota_engine.check(org_id, workspace_id, resource_type, estimated_amount)
  → Busca: quota_policies para o plano ativo + subscriptions + credit_wallets
  → Cálculo: consumed_this_period + balance_reserved + estimated_amount

  → consumed < soft_limit_percent * limit → ALLOW (sem notificação)
  → consumed >= soft_limit_percent * limit → ALLOW + QuotaWarningThresholdReached
  → consumed >= hard_limit → DENY → QuotaHardLimitReached
                                   → run bloqueado antes de iniciar
                                   → CreditReservationReleased (se reserva foi feita)

  → QuotaHardLimitReached + overage_policy = warn_then_charge → notifica founder/admin
    → founder/admin aprova overage explicitamente → overage_authorized → run libera
    → timeout sem aprovação → run bloqueado permanentemente até créditos disponíveis
```

## 8.3 `quota_policies` — resolução por plano

```sql
quota_policies
  id                  uuid    PRIMARY KEY
  tenant_id           uuid    NOT NULL    -- RLS
  plan_id             uuid    REFERENCES plans(id)
  resource_type       text    NOT NULL
  period              text    NOT NULL    -- daily | monthly | per_minute | lifetime
  soft_limit          bigint              -- NULL = sem soft limit
  hard_limit          bigint              -- NULL = sem hard limit (enterprise ilimitado)
  soft_limit_percent  numeric DEFAULT 0.80
  overage_policy      text    DEFAULT 'hard_block'
                              -- hard_block | warn_then_block | warn_then_charge | custom
  overage_charge_rate numeric             -- créditos por unidade excedente (se warn_then_charge)
  created_at          timestamptz DEFAULT now()
  updated_at          timestamptz DEFAULT now()
```

---

# 9. Billing Object Model

Todos os objetos abaixo são documentação arquitetural. Patches sugeridos para doc 11 estão em §27.

## 9.1 `plans` — Definição de planos

```sql
plans
  id                  uuid    PRIMARY KEY DEFAULT gen_random_uuid()
  code                text    NOT NULL UNIQUE   -- free | starter | professional | enterprise
  display_name        text    NOT NULL
  description         text
  billing_model       text    NOT NULL          -- free | monthly | annual | custom
  price_config        jsonb   NOT NULL          -- {monthly_usd, annual_usd, currency, ...}
                                                -- NUNCA hardcoded em código
  credit_quota_monthly bigint DEFAULT 0         -- 0 = ilimitado (enterprise)
  is_active           boolean DEFAULT true
  is_public           boolean DEFAULT true
  sort_order          integer DEFAULT 0
  metadata            jsonb
  created_at          timestamptz DEFAULT now()
  updated_at          timestamptz DEFAULT now()
```

---

## 9.2 `plan_features` — Features por plano

```sql
plan_features
  id                  uuid    PRIMARY KEY DEFAULT gen_random_uuid()
  plan_id             uuid    NOT NULL REFERENCES plans(id)
  feature_key         text    NOT NULL          -- string de feature gate
  is_enabled          boolean DEFAULT false
  config              jsonb                     -- configurações específicas da feature
  created_at          timestamptz DEFAULT now()

UNIQUE (plan_id, feature_key)
```

---

## 9.3 `subscriptions` — Assinatura de org a um plano

```sql
subscriptions
  id                    uuid    PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id             uuid    NOT NULL    -- RLS
  org_id                uuid    NOT NULL
  plan_id               uuid    NOT NULL REFERENCES plans(id)
  status                text    NOT NULL DEFAULT 'active'
                                -- active | trialing | past_due | suspended | cancelled | expired
  billing_cycle         text    NOT NULL   -- monthly | annual | custom
  current_period_start  timestamptz NOT NULL
  current_period_end    timestamptz NOT NULL
  trial_ends_at         timestamptz
  cancelled_at          timestamptz
  cancellation_reason   text
  external_subscription_id text            -- ID no gateway (Stripe, etc.)
  payment_method_ref    text               -- secret_ref → vault (NUNCA dados de cartão aqui)
  auto_renew            boolean DEFAULT true
  overage_approved_by   uuid               -- human UUID; null se sem overage ativo
  overage_approved_at   timestamptz
  metadata              jsonb
  created_at            timestamptz DEFAULT now()
  updated_at            timestamptz DEFAULT now()
```

---

## 9.4 `credit_wallets` — Saldo de créditos por org/workspace

```sql
credit_wallets
  id                  uuid    PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id           uuid    NOT NULL    -- RLS
  org_id              uuid    NOT NULL
  workspace_id        uuid                -- NULL = wallet de org; NOT NULL = wallet de workspace
  wallet_type         text    DEFAULT 'primary'  -- primary | workspace | bonus | trial
  balance_available   bigint  NOT NULL DEFAULT 0 CHECK (balance_available >= 0)
  balance_reserved    bigint  NOT NULL DEFAULT 0 CHECK (balance_reserved >= 0)
  balance_lifetime    bigint  NOT NULL DEFAULT 0
  currency_credits    text    DEFAULT 'CKC'      -- código interno de crédito CKOS
  expires_at          timestamptz                 -- NULL = sem expiração
  is_active           boolean DEFAULT true
  created_at          timestamptz DEFAULT now()
  updated_at          timestamptz DEFAULT now()

-- Constraint derivada (verificada na application layer + trigger):
-- balance_available + balance_reserved = balance_total (computed)
-- balance_available NEVER negative (CHECK constraint acima)
```

---

## 9.5 `credit_transactions` — Movimentações de crédito (append-only)

```sql
credit_transactions
  id                  uuid    PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id           uuid    NOT NULL    -- RLS
  wallet_id           uuid    NOT NULL REFERENCES credit_wallets(id)
  transaction_type    text    NOT NULL
                              -- purchase | consumption | refund | adjustment |
                              -- bonus | transfer_in | transfer_out | expiration
  amount              bigint  NOT NULL    -- positivo = crédito; negativo = débito
  balance_after       bigint  NOT NULL    -- saldo após esta transação (snapshot)
  description         text    NOT NULL
  run_id              uuid                -- run que originou (se consumption)
  reservation_id      uuid    REFERENCES credit_reservations(id)
  usage_event_id      uuid    REFERENCES usage_events(id)
  idempotency_key     text    UNIQUE      -- previne double-charge
  approved_by         uuid                -- human UUID; obrigatório para adjustments
  metadata            jsonb
  created_at          timestamptz DEFAULT now()

-- append-only: sem UPDATE ou DELETE
```

---

## 9.6 `credit_reservations` — Pré-reserva atômica

```sql
credit_reservations
  id                  uuid    PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id           uuid    NOT NULL    -- RLS
  wallet_id           uuid    NOT NULL REFERENCES credit_wallets(id)
  run_id              uuid    NOT NULL    -- agent_run, collector_run, etc.
  run_type            text    NOT NULL    -- agent_run | collector_run | research_run | export
  amount_reserved     bigint  NOT NULL CHECK (amount_reserved > 0)
  amount_consumed     bigint              -- preenchido em consumption
  status              text    NOT NULL DEFAULT 'active'
                              -- active | consumed | released | expired
  expires_at          timestamptz NOT NULL  -- obrigatório; previne reserva presa
  consumed_at         timestamptz
  released_at         timestamptz
  expired_at          timestamptz
  created_at          timestamptz DEFAULT now()
```

---

## 9.7 `usage_events` — Source of truth de consumo (append-only)

```sql
usage_events
  id                  uuid    PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id           uuid    NOT NULL    -- RLS
  org_id              uuid    NOT NULL
  workspace_id        uuid
  project_id          uuid
  resource_type       text    NOT NULL    -- agent_run | model_call | collector_run | artifact | storage | rag_query
  resource_id         uuid                -- ID do recurso consumido (run_id, artifact_id, etc.)
  quantity            numeric NOT NULL    -- quantidade consumida (ex: tokens, GB, runs)
  credits_consumed    bigint  NOT NULL    -- créditos consumidos
  cost_internal_usd   numeric             -- custo interno CKOS (do cost_ledger — apenas referência)
  billing_period_start timestamptz NOT NULL
  billing_period_end  timestamptz NOT NULL
  subscription_id     uuid    REFERENCES subscriptions(id)
  reservation_id      uuid    REFERENCES credit_reservations(id)
  idempotency_key     text    UNIQUE
  is_billable         boolean DEFAULT true
  is_invoiced         boolean DEFAULT false
  invoice_id          uuid                -- preenchido quando invoice gerada
  metadata            jsonb
  created_at          timestamptz DEFAULT now()

-- append-only: sem UPDATE em campos de consumo; só is_invoiced e invoice_id atualizáveis
```

---

## 9.8 `billing_events` — Eventos de cobrança (append-only)

```sql
billing_events
  id                  uuid    PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id           uuid    NOT NULL    -- RLS
  org_id              uuid    NOT NULL
  subscription_id     uuid    REFERENCES subscriptions(id)
  event_type          text    NOT NULL
                              -- charge | refund | credit_added | overage_charge |
                              -- plan_change | dispute_opened | dispute_resolved |
                              -- subscription_renewed | subscription_cancelled
  amount_credits      bigint              -- valor em créditos
  amount_usd          numeric             -- valor em USD (se aplicável)
  currency            char(3) DEFAULT 'USD'
  description         text    NOT NULL
  usage_event_ids     uuid[]              -- usage_events que originaram este billing_event
  external_charge_id  text               -- ID no gateway de pagamento
  approved_by         uuid               -- human UUID; obrigatório para overages e refunds
  status              text    DEFAULT 'pending'
                              -- pending | processed | failed | refunded | disputed
  idempotency_key     text    UNIQUE
  metadata            jsonb
  created_at          timestamptz DEFAULT now()

-- append-only: sem UPDATE em campos financeiros
```

---

## 9.9 `invoice_records` — Faturas geradas

```sql
invoice_records
  id                    uuid    PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id             uuid    NOT NULL    -- RLS
  org_id                uuid    NOT NULL
  subscription_id       uuid    REFERENCES subscriptions(id)
  invoice_number        text    NOT NULL UNIQUE
  status                text    NOT NULL DEFAULT 'draft'
                                -- draft | finalized | sent | paid | overdue | disputed | void | refunded
  billing_period_start  timestamptz NOT NULL
  billing_period_end    timestamptz NOT NULL
  subtotal_credits      bigint  NOT NULL DEFAULT 0
  subtotal_usd          numeric NOT NULL DEFAULT 0.00
  tax_usd               numeric NOT NULL DEFAULT 0.00
  total_usd             numeric NOT NULL DEFAULT 0.00
  currency              char(3) DEFAULT 'USD'
  line_items            jsonb   NOT NULL   -- [{description, quantity, unit_price, total, usage_event_ids}]
  usage_event_ids       uuid[]  NOT NULL   -- todos os usage_events incluídos
  billing_event_ids     uuid[]             -- billing_events relacionados
  due_date              timestamptz
  paid_at               timestamptz
  external_invoice_id   text               -- ID no gateway (Stripe Invoice ID, etc.)
  pdf_url               text
  notes                 text
  created_at            timestamptz DEFAULT now()
  updated_at            timestamptz DEFAULT now()
```

---

## 9.10 `plan_limits` — Limites por plano por resource type

```sql
plan_limits
  id                  uuid    PRIMARY KEY DEFAULT gen_random_uuid()
  plan_id             uuid    NOT NULL REFERENCES plans(id)
  resource_type       text    NOT NULL
  period              text    NOT NULL    -- daily | monthly | per_minute | lifetime
  soft_limit          bigint              -- NULL = sem soft limit
  hard_limit          bigint              -- NULL = sem hard limit
  soft_limit_percent  numeric DEFAULT 0.80
  created_at          timestamptz DEFAULT now()
  updated_at          timestamptz DEFAULT now()

UNIQUE (plan_id, resource_type, period)
```

---

## 9.11 `credit_rate_config` — Taxas de conversão (configuráveis, nunca hardcoded)

```sql
credit_rate_config
  id                  uuid    PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id           uuid                -- NULL = configuração global; NOT NULL = override por tenant
  resource_type       text    NOT NULL
  credits_per_unit    numeric NOT NULL    -- créditos por unidade de consumo
  unit_description    text               -- ex: "per agent_run", "per 1000 tokens"
  effective_from      timestamptz NOT NULL DEFAULT now()
  effective_until     timestamptz         -- NULL = indefinido
  approved_by         uuid    NOT NULL    -- founder obrigatório para mudanças de taxa
  version             integer NOT NULL DEFAULT 1
  created_at          timestamptz DEFAULT now()
```

**Regras:**
- Toda mudança de taxa é uma nova linha (versão incremental) — histórico preservado
- Aprovação do Founder obrigatória para mudança de taxa
- `effective_from` e `effective_until` permitem transições suaves entre taxas
- Taxas retroativas nunca se aplicam a `credit_transactions` já gravadas

---

## 9.12 `billing_disputes` — Disputas de cobrança

```sql
billing_disputes
  id                  uuid    PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id           uuid    NOT NULL    -- RLS
  org_id              uuid    NOT NULL
  invoice_id          uuid    REFERENCES invoice_records(id)
  billing_event_id    uuid    REFERENCES billing_events(id)
  dispute_type        text    NOT NULL
                              -- incorrect_charge | duplicate_charge | unauthorized |
                              -- service_not_rendered | credit_not_applied | other
  description         text    NOT NULL
  amount_disputed_usd numeric NOT NULL
  status              text    NOT NULL DEFAULT 'open'
                              -- open | under_review | resolved_approved | resolved_rejected | escalated
  opened_by           uuid    NOT NULL   -- human UUID
  reviewed_by         uuid               -- human UUID (founder ou admin financeiro)
  resolution_note     text               -- obrigatório antes de resolved_*
  resolution_amount_usd numeric          -- valor ajustado/reembolsado
  resolved_at         timestamptz
  created_at          timestamptz DEFAULT now()
  updated_at          timestamptz DEFAULT now()
```

---

## 9.13 `billing_alerts` — Configuração de alertas de billing

```sql
billing_alerts
  id                  uuid    PRIMARY KEY DEFAULT gen_random_uuid()
  tenant_id           uuid    NOT NULL    -- RLS
  org_id              uuid    NOT NULL
  workspace_id        uuid                -- NULL = alerta de org
  alert_type          text    NOT NULL
                              -- quota_warning | quota_hard_limit | credit_low |
                              -- overage_pending | invoice_due | invoice_overdue | dispute_opened
  threshold_percent   numeric             -- para quota alerts
  threshold_credits   bigint              -- para credit_low alerts
  notify_roles        text[]  NOT NULL    -- admin | founder | project_lead
  channel             text[]  NOT NULL    -- email | command_center | slack
  is_active           boolean DEFAULT true
  created_at          timestamptz DEFAULT now()
```

---

# 10. Distinção Crítica: Cost Ledger vs. Billing

Esta distinção é a invariante mais importante do sistema de billing.

## 10.1 Tabela de distinção

| Aspecto | `cost_ledger` (doc 11 §18) | `usage_events` + `billing_events` |
|---------|---------------------------|-----------------------------------|
| **O que mede** | Custo real de runtime CKOS | Consumo cobrado ao cliente |
| **Quem popula** | Runtime engine (automático) | Billing layer (controlled) |
| **Moeda** | USD (custo de tokens, APIs) | Créditos CKOS + USD |
| **Visível ao cliente** | Não (interno) | Sim (via invoice + dashboard) |
| **Gera cobrança** | Nunca diretamente | Sempre (via billing_events) |
| **Relação** | Insumo para cálculo de taxa de conversão | Resultado do cálculo com `credit_rate_config` |
| **Exemplo** | 1 model_call = $0.002 (custo OpenAI) | 1 model_call = 0.5 créditos (taxa CKOS para cliente) |

## 10.2 Fluxo de conversão

```
Runtime executa model_call
  → cost_ledger.entry criada (custo interno: $0.002)
  → credit_rate_config consultada (resource_type: model_call_small → 0.1 crédito/call)
  → usage_event criada (credits_consumed: 0.1; cost_internal_usd: 0.002)
  → credit_reservation consumida (0.1 crédito debitado do wallet)
  
Ao final do período de billing:
  → usage_events do período → billing_event → invoice_record
  → invoice tem line_items com usage_event_ids rastreáveis
  → cost_ledger NÃO aparece na invoice — apenas usage_events
```

---

# 11. Billing State Machines

## 11.1 Subscription State Machine

| # | Estado | Descrição |
|---|--------|-----------|
| 1 | `active` | Assinatura ativa; consumo normal; SLA aplicável |
| 2 | `trialing` | Período de trial; sem cobrança; limites reduzidos |
| 3 | `past_due` | Pagamento vencido; notificações ativas; funcionalidade mantida por grace period |
| 4 | `suspended` | Grace period expirado; funcionalidade suspensa; dados preservados |
| 5 | `cancelled` | Cancelamento solicitado; funcionalidade até fim do período |
| 6 | `expired` | Período encerrado; sem renovação; somente leitura |

**Transições:**

| De | Para | Trigger |
|----|------|---------|
| `trialing` | `active` | Trial expirado com pagamento configurado |
| `trialing` | `expired` | Trial expirado sem pagamento |
| `active` | `past_due` | Pagamento falhou; `PlanPaymentFailed` |
| `active` | `cancelled` | Admin/Founder solicita cancelamento |
| `past_due` | `active` | Pagamento recebido; `InvoicePaymentReceived` |
| `past_due` | `suspended` | Grace period expirado sem pagamento |
| `suspended` | `active` | Pagamento recebido + reativação aprovada por Founder |
| `cancelled` | `expired` | Fim do período pago |
| `cancelled` | `active` | Reativação antes do fim do período |
| `expired` | `active` | Nova assinatura criada (`PlanActivated`) |

## 11.2 Invoice State Machine

| # | Estado | Descrição |
|---|--------|-----------|
| 1 | `draft` | Invoice em composição; usage_events sendo agregados |
| 2 | `finalized` | Invoice finalizada; valores confirmados; não editável |
| 3 | `sent` | Invoice enviada ao cliente |
| 4 | `paid` | Pagamento confirmado |
| 5 | `overdue` | Data de vencimento passada sem pagamento |
| 6 | `disputed` | Disputa aberta pelo cliente |
| 7 | `void` | Invoice cancelada (duplicata ou erro) |
| 8 | `refunded` | Valor reembolsado total ou parcialmente |

**Transições:**

| De | Para | Trigger | Ação |
|----|------|---------|------|
| `draft` | `finalized` | Fim do período de billing | Valores travados; `InvoiceGenerated` |
| `finalized` | `sent` | Sistema ou manual | `InvoiceSent` event |
| `sent` | `paid` | Gateway confirma pagamento | `InvoicePaymentReceived` |
| `sent` | `overdue` | `due_date` passou | `InvoiceOverdue` + notificação |
| `overdue` | `paid` | Pagamento tardio | Subscription reativa se `past_due` |
| `paid` | `disputed` | Cliente abre disputa | `BillingDisputeOpened` |
| `finalized` | `void` | Founder/Admin cancela invoice | Estorno se já cobrado |
| `paid` | `refunded` | Disputa aprovada ou erro | `BillingEventRefund` |
| `disputed` | `paid` | Disputa rejeitada | — |
| `disputed` | `refunded` | Disputa aprovada | Valor devolvido |

---

# 12. Billing Events

Todos os eventos são publicados no event bus de doc 10 §5.3. Nenhum executa diretamente.

| # | Evento | Publisher | Subscribers | Schema mínimo |
|---|--------|-----------|-------------|---------------|
| 1 | `PlanActivated` | billing_engine | subscription_engine, quota_engine, dashboard | org_id, plan_id, subscription_id |
| 2 | `PlanUpgraded` | billing_engine (Founder approval) | quota_engine, feature_gate_engine, dashboard | org_id, from_plan_id, to_plan_id |
| 3 | `PlanDowngraded` | billing_engine (Founder approval) | quota_engine, feature_gate_engine, dashboard | org_id, from_plan_id, to_plan_id, effective_at |
| 4 | `PlanCancelled` | billing_engine (Founder) | subscription_engine, dashboard | org_id, subscription_id, effective_at |
| 5 | `CreditWalletCreated` | billing_engine | dashboard | wallet_id, org_id, initial_balance |
| 6 | `CreditPurchased` | billing_engine | credit_wallet_engine, dashboard | wallet_id, amount, billing_event_id |
| 7 | `CreditReserved` | quota_engine | credit_wallet_engine | reservation_id, wallet_id, amount, run_id |
| 8 | `CreditConsumed` | billing_engine | credit_wallet_engine, usage_ledger | reservation_id, amount_consumed, usage_event_id |
| 9 | `CreditReservationReleased` | billing_engine / runtime | credit_wallet_engine | reservation_id, amount, reason |
| 10 | `CreditReservationExpired` | sla_engine (TTL) | credit_wallet_engine, support_engine | reservation_id, run_id |
| 11 | `QuotaWarningThresholdReached` | quota_engine | notification_engine, dashboard | org_id, resource_type, percent_consumed |
| 12 | `QuotaHardLimitReached` | quota_engine | run_engine (block), dashboard, support_engine | org_id, resource_type, limit |
| 13 | `UsageEventRecorded` | runtime | billing_engine, usage_ledger | usage_event_id, resource_type, credits_consumed |
| 14 | `InvoiceGenerated` | billing_engine | notification_engine, dashboard | invoice_id, org_id, total_usd, period |
| 15 | `InvoicePaymentReceived` | billing_engine (gateway webhook) | subscription_engine, dashboard | invoice_id, amount_paid, paid_at |
| 16 | `BillingDisputeOpened` | billing_engine | support_engine, dashboard, founder (notification) | dispute_id, invoice_id, amount_disputed |

---

# 13. Billing ↔ Support System

## 13.1 Integração bidirecional

| Fluxo | Mecanismo | Regra |
|-------|-----------|-------|
| Quota breach → support ticket | `QuotaHardLimitReached` → support_engine cria `billing_support` ticket | Automático para P1; manual para P2/P3 |
| `billing_support` ticket → billing audit | Ticket com `root_cause_category` resolve ou referencia `billing_events` | Resolution requer cross-reference com `billing_events` |
| Disputa → support ticket | `BillingDisputeOpened` → `billing_support` ticket vinculado | Bidirecional via `support_feedback_links` |
| Friction de billing → product feedback | `friction_signal` tipo `billing_anomaly` → product feedback após aprovação | Aprovação lead+ obrigatória |

## 13.2 Regras de isolamento

1. `billing_support` tickets nunca resolvidos por agente — `requires_human_handoff = true` automático
2. Agente de diagnóstico de billing pode **ler** `credit_transactions` e `usage_events` mas **nunca escrever** ou iniciar reembolsos
3. Reembolso (`billing_events.event_type = refund`) requer aprovação de Founder
4. Estorno de créditos (`credit_transactions.transaction_type = adjustment`) requer aprovação de Founder

---

# 14. Billing ↔ ROI System

## 14.1 Distinção custo/valor no ROI

| Perspectiva | Fonte de dados | ROI Type |
|-------------|---------------|----------|
| Custo interno CKOS | `cost_ledger` (doc 11 §18) | Insumo para `operational_roi` |
| Custo cobrado do cliente | `usage_events` + `credit_transactions` | Insumo para `financial_roi` |
| Valor gerado para o cliente | `roi_outcomes` (doc 21) | Output para todos os ROI types |
| Custo de suporte por projeto | `support_roi_links.cost_attributed` (doc 23) | Insumo para `retention_roi` |

## 14.2 ROI que depende de billing data

| ROI Type | Campo de billing utilizado | Regra |
|----------|---------------------------|-------|
| `financial_roi` | `credit_transactions` total do período | Custo ao cliente vs. valor monetário gerado |
| `operational_roi` | `usage_events` por resource_type | Eficiência de consumo por entrega |
| `efficiency_roi` | Custo de créditos / workflows executados | Custo por unit de output |
| `retention_roi` | Tickets `billing_support` + `credit_transactions` | Custo de fricção de billing em churn risk |

## 14.3 Regras de integração

1. ROI models nunca buscam dados diretamente de `cost_ledger` — usam `usage_events` como proxy de custo ao cliente
2. `roi_models.cost_total` é preenchido por humano ou agente com aprovação — nunca calculado automaticamente de `billing_events`
3. Confidence de ROI financeiro depende de `usage_events` sendo 100% completos para o período

---

# 15. Billing ↔ Node Canvas

## 15.1 Billing Node Types no Canvas

| Node Type | Quando aparece | Visibilidade |
|-----------|---------------|--------------|
| `billing_alert_node` | `QuotaWarningThresholdReached` ou `QuotaHardLimitReached` | admin+ |
| `credit_status_node` | Widget de créditos do projeto | contributor+ |
| `invoice_node` | Invoice gerada; status past_due ou disputed | admin+ |
| `overage_approval_node` | Overage pendente de aprovação | founder + admin |

## 15.2 Comportamento de billing no Canvas

- `credit_status_node` exibe: balance_available, balance_reserved, quota %, período atual
- `billing_alert_node` exibe badge de urgência (warn: amarelo; hard_limit: vermelho)
- `overage_approval_node` exibe ação de aprovação/rejeição diretamente no Canvas para founder/admin
- Nodes de billing **nunca** exibem valores monetários em USD para roles abaixo de `admin`

---

# 16. Billing ↔ Command Center

## 16.1 Intents de billing (Família #8 — ROI, Cost & Usage)

| Intent | Exemplo | intent_type | Evento |
|--------|---------|-------------|--------|
| Ver saldo de créditos | "Quantos créditos restam este mês?" | `query.billing.credit_balance` | — |
| Ver consumo do período | "Qual o consumo de créditos desta semana?" | `query.billing.usage_summary` | — |
| Comprar créditos | "Adicionar 5.000 créditos ao workspace" | `action.billing.purchase_credits` | `CreditPurchased` |
| Aprovar overage | "Autorizar consumo acima do plano para o projeto X" | `action.billing.approve_overage` | `QuotaHardLimitReached → override` |
| Ver invoices | "Mostrar invoices do último trimestre" | `query.billing.list_invoices` | — |
| Ver plano atual | "Qual nosso plano atual e seus limites?" | `query.billing.plan_status` | — |
| Solicitar upgrade | "Solicitar upgrade para Professional" | `action.billing.request_upgrade` | `PlanUpgraded` (após aprovação) |
| Abrir disputa | "Contestar cobrança da invoice #X" | `action.billing.open_dispute` | `BillingDisputeOpened` |
| Ver custo por projeto | "Qual o custo em créditos do projeto de campanha?" | `query.billing.project_cost` | — |
| Ver friction de billing | "Tem alguma anomalia de billing detectada?" | `query.billing.friction_signals` | — |

---

# 17. Billing ↔ Dashboard

## 17.1 Widgets de billing no Project Dashboard

| Widget | Projection base | Conteúdo | Permissão mínima |
|--------|----------------|----------|:----------------:|
| **Credit Balance** | `cost_credit_projection` | Saldo disponível, reservado, % da quota | contributor |
| **Usage This Period** | `cost_credit_projection` | Créditos consumidos por resource_type | contributor |
| **Billing Alerts** | `cost_credit_projection` | Warnings ativos; hard_limits atingidos | admin |
| **Invoice Status** | `cost_credit_projection` | Invoices abertas, vencidas, pagas | admin |
| **Plan Limits** | `cost_credit_projection` | Limites do plano atual com % usado | admin |
| **Cost by Project** | `cost_credit_projection` | Créditos consumidos por projeto (admin view) | admin |

## 17.2 `cost_credit_projection` — campos de billing

Esta projeção é read-only; alimenta widgets de billing e Canvas. Já definida em doc 11 §21 — campos a expandir via P24-5:

```
cost_credit_projection (campos de billing):
  balance_available           -- créditos disponíveis
  balance_reserved            -- créditos em reserva ativa
  quota_monthly_percent       -- % da quota mensal consumida
  quota_daily_percent         -- % da quota diária consumida
  active_reservations_count   -- reservas ativas
  billing_alerts_active       -- alertas de quota ativos
  invoice_overdue_count       -- invoices vencidas
  invoice_past_due_total_usd  -- valor total vencido
  subscription_status         -- status da assinatura atual
  plan_code                   -- plano ativo
  period_start                -- início do período de billing
  period_end                  -- fim do período de billing
  last_updated_at
```

---

# 18. Overage and Upgrade Flows

## 18.1 Overage flow

```
QuotaHardLimitReached (recurso = X; org_id = Y)
  → run bloqueado antes de iniciar (quota_engine)
  → CreditReservationReleased (se reserva foi criada)
  → overage_approval_node criado no Canvas
  → notificação para founder + admin (via billing_alerts config)
  
Founder/Admin vê notificação:
  → APROVAR: overage_authorized → quota temporariamente elevada → run libera
             billing_event tipo overage_charge criado
             subscriptions.overage_approved_by + overage_approved_at preenchidos
  → REJEITAR: run permanece bloqueado → suporte notificado
  
Ao final do período:
  → usage_events de overage → billing_event → invoice com linha de overage explícita
```

## 18.2 Upgrade/Downgrade flow

```
Upgrade solicitado (via Command Center ou admin panel):
  → PlanUpgrade request criado (requer Founder approval)
  → Founder aprova → PlanUpgraded emitido
  → subscriptions.plan_id atualizado
  → quota_policies atualizadas imediatamente
  → proratização: billing_event para diferença do período atual
  → feature_gate_engine atualiza features disponíveis
  
Downgrade solicitado:
  → PlanDowngrade request criado (requer Founder approval)
  → Founder aprova → PlanDowngraded emitido com effective_at = fim do período atual
  → quota_policies mantidas até effective_at
  → Se consumo atual > novo plano limits → warning ao Founder
  → features excedentes desabilitadas em effective_at
```

---

# 19. Invoice Generation

## 19.1 Ciclo de geração de invoice

```
Fim do período de billing (current_period_end):
  → billing_engine coleta usage_events do período (is_billable=true; is_invoiced=false)
  → Agrupa por resource_type e aplica credit_rate_config
  → Adiciona billing_events de overage, compras e ajustes do período
  → Calcula: subtotal_credits, subtotal_usd, tax_usd, total_usd
  → Cria invoice_record (status: draft)
  → Revisão automática: total > 0? → se não, invoice não gerada (exceto para contratos enterprise)
  → InvoiceGenerated emitido (status: finalized)
  → usage_events marcados is_invoiced = true; invoice_id preenchido
  → Invoice enviada ao cliente (status: sent)
```

## 19.2 Rastreabilidade obrigatória de invoice

Todo `invoice_record` deve ter:
- `usage_event_ids[]` — todos os usage_events incluídos
- `line_items` com `usage_event_ids` por linha
- `billing_event_ids[]` — billing_events associados (overages, compras, etc.)
- `subscription_id` — assinatura ativa no período

**Invariante:** Um cliente deve conseguir chegar de qualquer linha da invoice até o `usage_event` que a gerou, e deste até o `agent_run` ou `model_call` ou `collector_run` que originou o consumo.

## 19.3 Aprovação de invoice

| Tipo | Aprovação |
|------|-----------|
| Invoice padrão (gerada automaticamente) | Nenhuma — automática se total dentro do esperado |
| Invoice com overage | Founder (overage já foi aprovado — referência na invoice) |
| Invoice manual (ajuste) | Founder obrigatório |
| Invoice de enterprise (custom) | Founder + contrato referenciado |

---

# 20. Billing Disputes

## 20.1 Processo de disputa

```
BillingDisputeOpened (cliente ou admin abre disputa)
  → billing_disputes criada (status: open)
  → billing_support ticket automático criado (vinculado à disputa)
  → Founder + admin financeiro notificados
  → Invoice status = disputed
  
Review (founder ou admin financeiro):
  → Verifica usage_events + billing_events referenciados na invoice
  → Documenta review_note
  
APROVADA (cobrou incorretamente):
  → billing_disputes.status = resolved_approved
  → billing_event tipo refund criado (approved_by = founder)
  → credit_transactions.transaction_type = refund (se em créditos)
  → Invoice status = refunded (total ou parcial)
  
REJEITADA (cobrança correta):
  → billing_disputes.status = resolved_rejected
  → resolution_note obrigatório com explicação rastreável
  → Invoice volta ao status anterior (paid ou overdue)
```

## 20.2 Regras de disputas

1. Disputa nunca resolvida por agente — `billing_disputes.reviewed_by` é sempre UUID humano
2. `resolution_note` obrigatório antes de qualquer `resolved_*`
3. Reembolso em USD requer integração com gateway — registrado como `external_charge_id` referência
4. Reembolso em créditos pode ser imediato via `credit_transactions.transaction_type = refund`
5. Disputas de mais de 60 dias são auto-escaladas para Founder com flag de urgência

---

# 21. Whitelabel Billing

O CKOS suporta billing separado por tenant para clientes que operam no modelo whitelabel — onde o cliente do CKOS (a empresa) revende o CKOS para seus próprios clientes.

## 21.1 Modelo de billing whitelabel

```
Tenant A (empresa X, cliente CKOS):
  → Tem subscriptions.plan_id = enterprise
  → Tem credit_wallets para seus workspaces
  → Paga CKOS diretamente (billing_events de tenant A)

Tenants filhos (clientes da empresa X):
  → Cada cliente da empresa X é um sub-tenant com tenant_id próprio
  → credit_wallets por sub-tenant (totalmente isolados)
  → Empresa X define planos para seus clientes (via plans configuráveis por tenant)
  → Empresa X paga CKOS; cobra seus clientes independentemente
  → CKOS não tem acesso aos dados de billing sub-tenant → tenant isolation
```

## 21.2 Regras de whitelabel billing

1. `credit_wallets.tenant_id` é SEMPRE scoped — cross-tenant structurally impossible
2. `plans` configuráveis por tenant — empresa X pode criar planos customizados para seus clientes
3. `credit_rate_config.tenant_id NOT NULL` → override de taxa por tenant (empresa X define sua taxa para clientes)
4. `invoice_records` de sub-tenant nunca acessíveis pelo tenant pai sem permissão explícita
5. `billing_events` de sub-tenant → RLS via `tenant_id` — tenant pai nunca vê
6. Admin financeiro do tenant pai pode ver analytics agregados (sem dados individuais de sub-tenant) apenas em view com aggregation

---

# 22. Billing Permissions

## 22.1 Matriz de permissões por role

| Ação | viewer | project_member | contributor | lead | admin | technical | founder |
|------|:------:|:--------------:|:-----------:|:----:|:-----:|:---------:|:-------:|
| Ver saldo de créditos do projeto | — | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ver consumo do período | — | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ver invoices | — | — | — | — | ✅ | — | ✅ |
| Ver plano e limites | — | — | — | ✅ | ✅ | ✅ | ✅ |
| Aprovar overage | — | — | — | — | ✅ | — | ✅ |
| Comprar créditos | — | — | — | — | ✅ | — | ✅ |
| Solicitar upgrade/downgrade | — | — | — | — | ✅ | — | ✅ |
| Aprovar upgrade/downgrade | — | — | — | — | — | — | ✅ |
| Abrir disputa | — | — | — | — | ✅ | — | ✅ |
| Resolver disputa | — | — | — | — | — | — | ✅ |
| Emitir reembolso | — | — | — | — | — | — | ✅ |
| Alterar credit_rate_config | — | — | — | — | — | — | ✅ |
| Ver billing sub-tenant | — | — | — | — | — | — | ✅ (founder do tenant pai) |

## 22.2 Regras de segurança obrigatórias

1. **RLS em todas as tabelas de billing.** `tenant_id` obrigatório; cross-tenant impossível.
2. **`payment_method_ref` é `secret_ref` apenas.** Dados de cartão/token de gateway nunca em `subscriptions` — somente referência para vault externo.
3. **`credit_rate_config` imutável após effective_from.** Histórico preservado; nova linha para mudanças.
4. **`credit_transactions` append-only.** Sem UPDATE ou DELETE em qualquer campo financeiro.
5. **`usage_events` append-only.** Apenas `is_invoiced` e `invoice_id` atualizáveis após criação.
6. **Reembolsos requerem `approved_by` (Founder UUID).** Agentes bloqueados de criar billing_events de tipo refund.
7. **Overage charges requerem `approved_by`.** `billing_events.event_type = overage_charge` sem `approved_by` humano é inválido.
8. **`credit_wallets.balance_available >= 0`.** CHECK constraint no banco de dados; validação na camada de aplicação.
9. **Disputas revisadas por humano.** `billing_disputes.reviewed_by` é sempre UUID humano.
10. **Taxas de conversão nunca hardcoded.** Toda referência a créditos por recurso vai para `credit_rate_config`.

---

# 23. Billing QA Checklist

## 23.1 Checklist de qualidade (BL1–BL16)

| # | Item | Critério |
|---|------|---------|
| BL1 | Distinção cost/billing | `cost_ledger` e `usage_events` são entidades distintas; invoice nunca gerada de `cost_ledger` |
| BL2 | Credit reservation pattern | Toda operação consumidora tem `CreditReserved` antes de iniciar |
| BL3 | Negative balance prevention | `balance_available >= 0` CHECK constraint + validação application layer |
| BL4 | Quota enforcement | `quota_engine.check()` antes de toda operação; hard_limit bloqueia antes de reservar |
| BL5 | Plan feature gates | `plan_features` consultado antes de expor funcionalidade |
| BL6 | Billing state machines | Subscription (6 estados) + Invoice (8 estados) completos com transições |
| BL7 | Events | 16 eventos com publisher, subscriber e schema mínimo |
| BL8 | Invoice rastreabilidade | `line_items` com `usage_event_ids`; path até agent_run rastreável |
| BL9 | Overage approval | Overage requer `approved_by` humano; sem auto-charge |
| BL10 | Secrets em vault | `payment_method_ref` é `secret_ref`; nenhum token financeiro em tabelas normais |
| BL11 | RLS | `tenant_id` em todas as tabelas; cross-tenant impossível |
| BL12 | Whitelabel isolation | Billing de sub-tenants completamente isolado do tenant pai |
| BL13 | Append-only tables | `credit_transactions` e `usage_events` sem UPDATE/DELETE em campos financeiros |
| BL14 | Credit_rate_config imutável | Nova linha para cada mudança de taxa; `approved_by` Founder obrigatório |
| BL15 | Dispute rastreabilidade | `resolution_note` obrigatório; `reviewed_by` sempre humano |
| BL16 | Idempotency | `idempotency_key` em `credit_transactions`, `usage_events`, `billing_events` |

## 23.2 Critérios de rejeição automática

1. `billing_events` de tipo `refund` ou `overage_charge` sem `approved_by` humano
2. `credit_wallets` sem CHECK constraint em `balance_available >= 0`
3. `payment_method_ref` contendo dados de cartão em texto plano
4. `usage_events` gerando charges sem `idempotency_key`
5. Upgrade/Downgrade sem Founder approval registrado

---

# 24. MVP P0

## 24.1 O que entra no MVP P0

| Componente | Escopo P0 |
|-----------|-----------|
| Plans | `free` e `starter` (Professional configurado mas não exposto) |
| Credit wallets | Por org (workspace wallet deferido para P1) |
| Credit reservation pattern | **Obrigatório desde P0** — sem exceção |
| Quota enforcement | Hard limit para `monthly_credits` e `daily_agent_runs`; soft limit com warning |
| Usage events | Todos os `resource_type` básicos (agent_run, model_call, collector_run) |
| Billing events | `charge`, `credit_added`, `subscription_renewed` |
| Invoices | Draft → finalized → sent → paid (manual gateway P0) |
| Credit rate config | Configuração inicial; mudanças por Founder apenas |
| Dashboard widgets | Credit Balance + Usage This Period |
| Command Center | `/credits` e `/plan` básicos |
| Node Canvas | `credit_status_node` + `billing_alert_node` |
| Billing alerts | `quota_warning` e `quota_hard_limit` |
| Billing support | Via doc 23 (Support System) com `requires_human_handoff = true` |

## 24.2 O que fica fora do MVP P0

| Componente | Motivo do deferral | Urgência |
|-----------|--------------------|----------|
| Payment gateway integration (Stripe/Paddle) | Implementação de integração externa — fora do escopo deste doc | P1 |
| `annual` billing cycle | Complexidade de proratização | P1 |
| `enterprise` plan | Custom contracts; SLA customizado | P1 |
| Workspace-level wallets | Complejidade de hierarquia de créditos | P1 |
| `billing_disputes` | Requer gateway integrado | P1 |
| Whitelabel billing | Requer tenant hierarchy completo + doc 25 | P1 |
| Overage auto-charge (`warn_then_charge`) | Requer gateway; P0 usa `warn_then_block` | P1 |
| Credit transfer entre workspaces | Complexidade; risco de inconsistência | P2 |
| `trial` subscription status | Deferido para go-to-market | P1 |
| Invoice PDF generation | Requer template engine | P1 |
| `billing_alerts` custom (Slack, email) | Requer notification_engine (doc 28) | P1 |
| Admin financeiro analytics | Dashboard financeiro completo | P1 |

---

# 25. Failure Modes

| # | Failure Mode | Sintoma | Mitigação |
|---|---|---|---|
| FM-B1 | Reserva de crédito não liberada após falha de run | `balance_reserved` cresce indefinidamente | TTL obrigatório em `credit_reservations.expires_at`; `CreditReservationExpired` automático |
| FM-B2 | Double-charge por retry de request | Mesmo usage_event contabilizado duas vezes | `idempotency_key UNIQUE` em `credit_transactions` + `usage_events` |
| FM-B3 | `balance_available` negativo sob concorrência | Créditos negativos inconsistentes | `CHECK (balance_available >= 0)` + operações atômicas de UPDATE |
| FM-B4 | Cost_ledger confundido com billing | Invoice gerada de `model_calls` diretamente | Billing engine consulta APENAS `usage_events` — nunca `cost_ledger` ou `model_calls` |
| FM-B5 | `credit_rate_config` hardcoded em código | Mudança de taxa requer deploy | Toda taxa via `credit_rate_config`; nenhuma constante financeira em código-fonte |
| FM-B6 | Token de gateway em tabela de subscriptions | Exposição de credentials de pagamento | `payment_method_ref` = `secret_ref` APENAS; vault validation obrigatória |
| FM-B7 | Quota hard_limit não enforced | Consumo acima do plano sem bloqueio | `quota_engine.check()` antes de CADA reserva; não apenas batch |
| FM-B8 | Overage cobrado sem aprovação | Cliente cobrado automaticamente sem consentimento | `overage_charge` billing_event bloqueado sem `approved_by` humano |
| FM-B9 | Invoice sem rastreabilidade de usage_events | Linha de invoice não pode ser auditada | `line_items[].usage_event_ids` obrigatório; invoice rejeitada se vazia |
| FM-B10 | Upgrade de plano sem proratização | Cliente cobrado pelo mês cheio em upgrade no meio do mês | `billing_event` de proratização criado no momento do upgrade |
| FM-B11 | Cross-tenant billing leak | Créditos de tenant A deduzidos de tenant B | `tenant_id` em todas as operações; `credit_wallets` scoped por tenant |
| FM-B12 | `credit_transactions` com UPDATE em campos financeiros | Audit trail adulterado | Tabela append-only; `UPDATE` bloqueado via trigger ou policy |
| FM-B13 | Disputa resolvida por agente | Reembolso sem supervisão humana | `billing_disputes.reviewed_by` = UUID humano; agentes bloqueados de `resolved_*` |
| FM-B14 | Subscription não cancela ao fim do período | Cobrança após cancelamento | `cancelled_at` + `effective_at` enforced; trigger de `expired` ao fim do período |
| FM-B15 | `plan_features` consultado apenas no login | Feature gate bypass por cache stale | Feature gate verificado a cada request; cache TTL máximo 60s |
| FM-B16 | `credit_rate_config` com dois registros ativos | Ambiguidade qual taxa aplicar | `effective_from/until` com constraint de não sobreposição por `resource_type` |
| FM-B17 | Invoice gerada sem `is_billable = true` events | Invoice inclui consumo interno (logs, debug) | `is_billable DEFAULT true` só para eventos de produto; `is_billable = false` para internal |
| FM-B18 | Reservation TTL muito curto | Run legítimo expira antes de completar | TTL = `max_run_duration + buffer`; configurável por `resource_type` |
| FM-B19 | Downgrade com consumo acima do novo limite | Run bloqueado inesperadamente no dia do downgrade | Warning ao Founder 7 dias antes; consumo atual vs. novo limite comparado |
| FM-B20 | Whitelabel sub-tenant credit com acesso de tenant pai | Cross-tenant read de dados financeiros | RLS por `tenant_id`; tenant pai acessa APENAS aggregates — sem dados individuais |

---

# 26. Business Systems Gate — Status Final

Com a criação deste documento, os quatro documentos do `06_BUSINESS_SYSTEMS/` estão completos.

| Doc | Título | Versão | Status | Gate I requirement |
|-----|--------|:------:|--------|:-----------------:|
| 21 | ROI Architecture | v1.0.0 ✅ | draft | ✅ presente |
| 22 | Feedback System Architecture | v1.0.0 ✅ | draft | ✅ presente |
| 23 | Support System Architecture | v1.0.0 ✅ | draft | ✅ presente |
| 24 | Credits, Plans and Billing Architecture | v1.0.0 ✅ | draft | ✅ presente |

**Gate I (Business Systems Gate) pode ser submetido para aprovação formal.**

Todos os quatro documentos existem, estão versionados e são mutuamente referenciáveis. Cada documento:
- Define a arquitetura do sistema sem implementar backend, frontend, migrations ou agentes
- Registra patches sugeridos para docs 10 e 11 sem aplicá-los
- Conecta explicitamente ao Runtime (10–13), Product System (14–16), Implementation System (17–20) e aos outros Business Systems (21–24)

**Aprovação requerida (Gate I):** Founder + Technical + Metacognik, conforme doc 20 §7 Gate I.

---

# 27. Patches Sugeridos para Outros Docs

Os patches abaixo foram identificados durante a criação deste documento. Estão **registrados como sugestões** — não aplicados. Requerem aprovação Technical + PMO_CKOS antes de aplicar.

| Patch | Doc alvo | Descrição | Urgência |
|-------|----------|-----------|----------|
| **P24-1** | Doc 11 v1.3.x | Tabela `credit_rate_config` — schema completo com `tenant_id` (override), `effective_from/until`, `approved_by` (Founder), versioning | Antes de Billing MVP |
| **P24-2** | Doc 11 v1.3.x | Tabela `billing_disputes` — schema completo com `dispute_type`, `resolution_note` obrigatório, `reviewed_by` (human) | Antes de Dispute flow P1 |
| **P24-3** | Doc 11 v1.3.x | Tabela `billing_alerts` — schema completo com `threshold_percent`, `threshold_credits`, `notify_roles`, `channel` | Antes de Alerts MVP |
| **P24-4** | Doc 11 v1.3.x | Adicionar `idempotency_key` em `credit_transactions`, `usage_events` e `billing_events` se não presentes em §33 | Antes de qualquer billing em produção |
| **P24-5** | Doc 11 v1.3.x | Expandir `cost_credit_projection` em §21 com campos de billing: `balance_available`, `quota_monthly_percent`, `billing_alerts_active`, `invoice_overdue_count`, `subscription_status`, `plan_code` | Antes de Gate F |
| **P24-6** | Doc 10 v1.2.x | Registrar `quota_engine`, `billing_engine`, `credit_wallet_engine` e `feature_gate_engine` como componentes nomeados do runtime no §5.2 (flow) e §5.4 (component registry) | Antes de Gate I |

> Patches P24-1 a P24-6 registrados. Não aplicar sem aprovação formal Technical + PMO_CKOS e versão incremental nos docs afetados.

---

# 28. Edge Cases

| # | Caso | Comportamento esperado |
|---|------|----------------------|
| EC-B1 | `credit_reservations` orphan (run_id inválido) | TTL expiração automática; `CreditReservationExpired`; alerta para technical |
| EC-B2 | Dois requests simultâneos tentando reservar os últimos créditos | Operação atômica (SELECT FOR UPDATE ou serializable transaction); apenas um bem-sucedido |
| EC-B3 | Mudança de `credit_rate_config` durante run ativo | Run usa a taxa vigente na criação da reserva; nova taxa aplica apenas a reservas futuras |
| EC-B4 | Downgrade no dia da geração da invoice | Invoice gerada com plano atual; downgrade effectua no próximo período |
| EC-B5 | `billing_disputes` aberto em invoice já `paid` | Invoice status = disputed; pagamento registrado mas em hold; Founder notificado |
| EC-B6 | Overage aprovado mas gateway falha no charge | `billing_event` status = failed; notificação ao admin; retry com `idempotency_key` |
| EC-B7 | `subscription` expires durante run ativo | Run completa; `CreditReservationReleased`; sem nova reserva após subscription.status = expired |
| EC-B8 | Créditos comprados com `expires_at` no passado | Compra bloqueada na criação; `expires_at` validado antes de `CreditPurchased` |
| EC-B9 | Reembolso em créditos maior que o consumo original | Permitido se Founder aprova explicitamente (bonus); `transaction_type = adjustment` com nota |
| EC-B10 | Tenant whitelabel com sub-tenant sem wallet | Sub-tenant sem wallet não pode executar operações; wallet criado ao ativar subscription |
| EC-B11 | `invoice_records` com `total_usd = 0` | Invoice não enviada se total = 0 (exceto enterprise com invoice obrigatória por contrato) |
| EC-B12 | `quota_engine` indisponível | Fail-open para plano Professional+; fail-closed para Free/Starter (operação bloqueada) |
| EC-B13 | Mudança de `credit_rate_config` retroativa solicitada | Bloqueada — taxas retroativas não se aplicam a `credit_transactions` já gravadas |
| EC-B14 | `plan_features` ausente para um feature_key | Feature gate retorna `is_enabled = false` (deny-by-default) |

---

# 29. Related Notes

- `../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md` — Event bus, component registry; engines de billing referenciados
- `../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md` — §33 Credits/Plans/Billing Data Model (tabelas base: plans, plan_features, subscriptions, credit_wallets, credit_transactions, credit_reservations, usage_events, billing_events, invoice_records, plan_limits, quota_policies); §18 cost_ledger (custo interno — distinto de billing); §21 projeções (cost_credit_projection)
- `../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md` — RLS, tenant isolation, vault-only secrets, deny-by-default
- `../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md` — cost_guard (doc 13 §11); cost_ledger como base de custo interno; alerting (§20)
- `../04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md` — Dashboard widgets de billing; projeções
- `../04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md` — `/credits`, `/plan` — Família #8 de intenções
- `../04_PRODUCT_SYSTEM/16_NODE_CANVAS_ARCHITECTURE.md` — billing_alert_node, credit_status_node, overage_approval_node
- `../05_IMPLEMENTATION_SYSTEM/17_IMPLEMENTATION_PROTOCOL.md` — Gate I (Business Systems); billing como dependência de MVP comercial
- `../05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md` — CQ1–CQ10 + BL1–BL16 checklists; approval actors
- `21_ROI_ARCHITECTURE.md` — billing como insumo para financial_roi e efficiency_roi; distinção custo/billing na perspectiva ROI
- `22_FEEDBACK_SYSTEM_ARCHITECTURE.md` — feedback de billing; friction de cobrança → product gap
- `23_SUPPORT_SYSTEM_ARCHITECTURE.md` — billing_support (integração principal); SLA de billing tickets; disputes via support
- `../ARCHITECTURE_PATCH_REPORT.md` — §24: registro de conclusão deste documento; patches P24-1 a P24-6; Gate I status final
- `../QA_DOCUMENTATION_CHECKLIST.md` — Checklist BL1–BL16 aplicado a este documento

---

## Patch 1.0.0 — Criação

**Data:** 2026-05-25  
**Autor:** PMO_CKOS + Cognik (doc owner)  
**Revisores:** Metacognik, QA Lead  
**Status:** draft — aguarda aprovação Founder + Technical + Metacognik

**O que este documento cobre:**
- Credits, Plans and Billing System como quarto e último documento do Business Systems layer (06_BUSINESS_SYSTEMS/)
- Distinção fundamental: `cost_ledger` (custo interno runtime) vs. `billing_events` (cobrança ao cliente)
- 4 planos (Free, Starter, Professional, Enterprise) com feature gates e limites
- Credit consumption model com reservation pattern atômico
- Quota enforcement soft + hard com overage approval flow
- 13 objetos com schemas SQL completos
- Subscription State Machine (6 estados) + Invoice State Machine (8 estados)
- 16 billing events conectados ao event bus de doc 10
- Whitelabel billing com isolamento completo de sub-tenant
- Invoice generation com rastreabilidade obrigatória até usage_event
- Billing disputes com aprovação humana obrigatória
- 6 patches sugeridos para docs 10 e 11 (não aplicados)

**Gate I — Business Systems Gate:**
Este documento é o quarto e último dos documentos obrigatórios para Gate I (Business Systems Gate) conforme doc 20 §7 Gate I e doc 17 §30. Com este documento, todos os quatro Business Systems (21–24) existem e estão versionados. **Gate I pode ser submetido para aprovação formal.**

**Aprovação requerida:** Founder + Technical + Metacognik.
