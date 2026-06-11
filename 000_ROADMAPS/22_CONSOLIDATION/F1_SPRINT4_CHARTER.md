---
title: F1 Sprint 4 — Event Log Hardening Charter (PMO planning)
file: F1_SPRINT4_CHARTER.md
layer: auxiliary
doc_type: pmo_sprint_charter
phase: 000_ROADMAPS
category: consolidation
status: founder_approved_awaiting_metacognik
version: 0.2.0
created_at: 2026-06-11
founder_decisions_at: 2026-06-11
owner: pmo_ckos
responsible_agent: claude_opus_4_7
session_id: S-F1S4-CHARTER-CLAUDE-20260611-001
derives_from:
  - F1_SPRINT1_CHARTER.md v0.3.0                                  # pattern de charter validado (S1 done em 2026-06-11, commit 4ed637d)
  - S-F1S1-IMPLEMENTATION-DISPATCH.md §17 production_deploy       # baseline performance live em GRU
  - 03_BACKEND_MVP_THIN_SLICE_PLAN.md §14                          # ordem dos sprints: S4 antes de S2/S3
  - CKOS_EXPANSION_KANBAN.md F1 lane                               # "S4 — Event Log (sem ele, vira chat bonito) #F1 #runtime #blocker"
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md §5.3       # Event Bus + Event Log conceitual
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md §5.6       # Run Scheduler, Queue, Retry, Timeout, Idempotency
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md §5.26      # Run Replay
  - 03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md §7          # events table físico + partition hint línea 235
companion_of:
  - F1_SPRINT1_CHARTER.md
  - S-F1S1-IMPLEMENTATION-DISPATCH.md
target_canonical: []                                              # charter NÃO edita canônico 01-28
target_repo: https://github.com/danielck01/CKOS_RUNTIME           # mesmo de S1 (mono-runtime, multi-sprint)
approval_required:
  - founder
  - metacognik
non_authority_boundary: >
  Planning artifact PMO. Define o ESCOPO operacional do Sprint 4 (Event Log hardening) — primeira
  fortificação da fundação que sustenta S2/S3/S5/S6. NÃO edita canônico 01-28 (apenas cita). NÃO
  escreve código. NÃO toca SQL diretamente (executor escreve migrations Drizzle no CKOS_RUNTIME).
  Implementação real é uma sessão SEPARADA desta e da autora.
tags: [planning, sprint-charter, f1, sprint-4, event-log, runtime, hardening, post-sprint-1-done]
---

# F1 Sprint 4 — Event Log Hardening Charter

> **O que é:** charter PMO que define o escopo executável do Sprint 4 — hardening do event log que sustenta tudo que vem depois (S2 Question Engine, S3 Approval Gates, S5 Work Order/Agent Run, S6 Feedback/ROI). Per [`03_BACKEND_MVP_THIN_SLICE_PLAN.md §14`](03_BACKEND_MVP_THIN_SLICE_PLAN.md): "Event Log deve ser estabilizado cedo porque sustenta todos os demais critérios."
> **O que não é:** não é spec de código, não é canonical_patch, não é dispatch de implementação. É o artefato de alinhamento que precede a sessão de dispatch.

---

## 0. Veredito em uma linha (PMO, direto)

Sprint 4 entrega **um event log production-grade**: idempotência fim-a-fim com client_request_id, replay em ordem causal (não temporal), tabela `events` particionada por `aggregate_type` + range por `created_at`, telemetria de write attempts bloqueadas, e baseline de performance documentado (P95 insert + throughput) — sem novos eventos, sem novos endpoints de negócio, sem mexer no fluxo S1.

---

## 1. Precondições satisfeitas

| Item | Estado | Referência |
|---|---|---|
| S1 entregue + production deploy validado | ✅ 2026-06-11 | commit `4ed637d` (sprint-done) |
| Runtime live em GRU + Supabase Pooler sa-east-1 | ✅ | https://ckos-runtime.fly.dev |
| Quality gate S1: 13/13 verdes | ✅ | dispatch §14 + anexo §17 production_deploy |
| Schema canônico Doc 11 §7 implementado integralmente | ✅ | 0 patch findings |
| 4 eventos workflow + 4 LLMCost contratos canônicos no runtime | ✅ | Zod schemas + Drizzle tipados |
| Append-only invariant via Postgres triggers | ✅ | trigger `events_no_update_delete` |
| pg-boss workers consumindo eventos | ✅ | validado em e2e prod |

**Nenhuma precondição pendente.** Sprint 4 destrava-se assim que Founder + Metacognik aprovarem charter + dispatch.

---

## 2. Escopo do Sprint 4

### 2.1 ENTRA (cirúrgico — escopo de hardening, não novas features)

| # | Deliverable | Anchor canônico |
|---|---|---|
| 1 | **Idempotência no ingress** — header `X-Idempotency-Key` (UUID v4) no `POST /intent`: 2ª chamada com mesmo key + mesmo workspace dentro de janela (AQ-S4-02) retorna 200 com `correlation_id` original, NÃO cria evento duplicado | Doc 10 §5.6 (Idempotency) |
| 2 | **Idempotency table** dedicada `ingress_idempotency(key, workspace_id, correlation_id, request_hash, created_at)` com índice unique + cleanup job pg-boss | Doc 11 §7 (eventos invariants) — extensão operacional |
| 3 | **Replay endpoint robusto** `GET /events/replay/:correlation_id?ordering=causal\|temporal` — `causal` percorre `causation_id` chain (topological); `temporal` mantém comportamento atual de S1 | Doc 10 §5.26 (Run Replay) |
| 4 | **Partição da tabela `events`** — `PARTITION BY LIST (aggregate_type)` + sub-partição `RANGE (created_at)` mensal. Migração: criar tabela nova `events_partitioned`, copiar dados S1 (poucos), swap via rename + view backward-compat | Doc 11 §7 línea 235 |
| 5 | **Telemetria append-only** — counter Postgres `events_append_attempts_blocked_total{op}` exposto via endpoint `GET /metrics` (Prometheus text format); incrementa toda vez que trigger bloqueia UPDATE/DELETE | Doc 13 §16 quality gates — preparação |
| 6 | **Performance baseline test** — script `pnpm bench:events` insere 1000 eventos concorrentes (100 workers × 10 events), mede P50/P95/P99 insert latency + throughput events/s. Documentado em `docs/EVENT_LOG.md` | Doc 13 §16 — baseline pra alertar regressão |
| 7 | **Concorrência tests** — `tests/integration/idempotency_concurrent.test.ts`: 50 POSTs paralelos com mesmo idempotency_key → exatamente 1 event publicado; sem deadlock | Doc 10 §5.6 + Doc 13 §16 |
| 8 | **`docs/EVENT_LOG.md`** no CKOS_RUNTIME — invariantes (append-only, idempotency, ordering, partition), schema com 6 campos extras explicados, replay semantics, performance baseline, troubleshooting | self-documentação operacional |
| 9 | **Migration safety net** — testar migration de partição em branch separada do Supabase (`pnpm db:migrate:dry-run` simula EXPLAIN), documentar rollback no `docs/MIGRATIONS.md` | Doc 11 §7 + Doc 12 §5.X (data governance) |

### 2.2 NÃO ENTRA (defer — motivos explícitos)

| Item | Defer para | Motivo |
|---|---|---|
| Outbox pattern + Event Bus pub/sub real | **S5** | Doc 10 §5.3 Event Bus é a 5ª etapa do thin-slice; S4 foca em PERSISTÊNCIA hardening, S5 cobre PROPAGAÇÃO |
| Novos tipos de evento (PolicyChecked, RunStarted) | **S3/S5** | Charter S1 §2.2 listou esses como skipados em S1; entram com os sprints que precisam |
| Memória longa / cross-projeto | **S6** | Doc 05 §5.1 — entra com feedback/ROI |
| Real-time projections (CQRS read models) | **S5/F4** | Doc 10 §5.12 — depende de Event Bus (S5) + UI (F4) |
| Multi-tenant RLS forçada via Supabase roles | **S3** | Auth real entra em S3 (charter S1 §6 AQ-S1-05 promovida); até lá, RLS app-side |
| Event compaction / cold storage | **F6/F7** | Doc 21 — operacional, não funcional |
| Audit log compliance (LGPD/SOC2) | **F7** | Doc 12 §5.15 + Doc 24 — compliance é fase de negócio |
| Multi-region replication | **F6** | Single Supabase project basta pra MVP; replicação é autonomia (Doc 21) |
| OpenTelemetry traces distribuídos | **S6** | Pino structured logs + correlation_id basta pra S4; OTEL entra com observability completa |
| F-01 / F-02 / F-03 (Metacognik flags PATCH 2.5) | **PATCH 3** | Inalterado — herdado |
| Doc 11 `users` enrichment (PATCH 2 fields) | **PATCH 3** | Inalterado — herdado |

### 2.3 PROIBIDO durante S4

- Editar canônico 01-28 (executor é READ-ONLY no doc repo, mesmo de S1)
- Mudar contratos dos 4 eventos workflow (PATCH 2/2.5 são imutáveis; S4 não toca payloads)
- Criar novos endpoints de negócio (S4 adiciona apenas `/metrics` operacional + extensão de `/events/replay`)
- Aumentar custo LLM por intent (S4 não chama LLM — não toca Intent Resolver nem Output)
- Schemas SQL fora do que Doc 11 §7 define + a `ingress_idempotency` (operacional, justificada em §2.1 #2)
- Skip do test de concorrência (deliverable #7 é crítico — sem ele, idempotência é só promessa)

---

## 3. Contratos (cite — não duplique)

**Fonte canônica única:** já existente, intocada pelo S4.

- **Envelope físico** events table → Doc 11 §7 linhas 217-232 (S1 implementou; S4 adiciona partição preservando schema)
- **Reconciliação envelope conceitual ↔ físico** → `F1_SPRINT1_CHARTER.md §3` (tabela AJUSTE-03)
- **Append-only invariant** → Doc 11 §7 (constraint) + Postgres trigger no CKOS_RUNTIME (já implementado em S1)
- **Idempotency semantics** → Doc 10 §5.6 (Run Scheduler, Queue, Retry, Timeout, Idempotency) — S1 já tem `idempotency_key` no envelope; S4 estende pra ingress
- **Run Replay** → Doc 10 §5.26 — S1 implementou via timestamp; S4 adiciona ordering causal

### 3.1 Nova tabela operacional (extensão, não-canônica)

> **`ingress_idempotency`** — fora do canônico Doc 11 (que cobre só objetos de negócio). É infra operacional do runtime, equivalente a uma cache table.

```sql
CREATE TABLE ingress_idempotency (
  key uuid PRIMARY KEY,                  -- client-provided X-Idempotency-Key
  workspace_id uuid NOT NULL,
  correlation_id uuid NOT NULL,          -- ref ao evento criado na 1ª chamada
  request_hash text NOT NULL,            -- sha256(intent_text + user_id + ...)
  created_at timestamptz NOT NULL DEFAULT now(),
  expires_at timestamptz NOT NULL        -- created_at + AQ-S4-02 janela
);
CREATE INDEX ingress_idempotency_expires_idx ON ingress_idempotency (expires_at);
```

**Conflito resolution rule:** mesmo `key` + mesmo `workspace_id` + mesmo `request_hash` → 200 OK retorna `correlation_id` original (replay-safe). Mesmo `key` + mesmo `workspace_id` + `request_hash` DIFERENTE → 409 Conflict (cliente está reusando key indevidamente).

**Cleanup:** pg-boss job a cada 1h roda `DELETE FROM ingress_idempotency WHERE expires_at < now()`.

### 3.2 Replay endpoint extensão

```
GET /events/replay/:correlation_id?ordering=causal
  → events em ordem topológica do DAG causation_id (root primeiro, depois filhos)
GET /events/replay/:correlation_id?ordering=temporal  (default — backward-compat com S1)
  → events em ordem cronológica created_at ASC
```

Implementação `causal`: query recursive CTE seguindo `causation_id`. Para S4 com `aggregate_id = correlation_id` (charter S1 §3 AJUSTE-03 nota), causação é linear na maior parte; CTE recursivo handles ciclos defensivamente (LIMIT 100 hops).

---

## 4. Tech stack — sem mudanças em relação a S1

S4 NÃO introduz novas dependências. Reusa stack já em produção (charter S1 §4):

- TypeScript 5.4+ + Node 20 LTS + pnpm 9
- Fastify 4 + Zod
- Drizzle ORM + drizzle-kit (migrations de partição)
- pg-boss 9+ (jobs de cleanup idempotency table)
- Supabase Postgres 15+ (suporta `PARTITION BY` nativo)
- Fly.io GRU (mesmo app `ckos-runtime`, redeploy via `fly deploy`)
- Vitest (extensão dos integration tests)
- Pino (structured logs)

**Adições leves:**
- `vitest-concurrent` (já em vitest 1.6+ via `test.concurrent`)
- Endpoint `/metrics` é Fastify route nativa, sem nova lib

---

## 5. Exit criterion (binário)

> **Event log production-grade pode ser stress-testado e replayed em ordem causal sem perder eventos nem criar duplicatas** — testável por 3 checks objetivos:

1. **Idempotência:** `tests/integration/idempotency_concurrent.test.ts` envia 50 POST `/intent` paralelos com mesmo `X-Idempotency-Key` + mesmo `request_hash` → exatamente **1 evento `IntentSubmitted`** persistido, mesma `correlation_id` retornada nas 50 respostas
2. **Replay causal:** dado um `correlation_id` com 8 eventos S1, `GET /events/replay/:correlation_id?ordering=causal` retorna lista em ordem topológica `causation_id` chain (verifica que `event[i].causation_id === event[i-1].id` para `i > 0` quando há cadeia linear)
3. **Performance baseline:** `pnpm bench:events` reporta P95 insert latency < 100ms (target conservador pro free tier Supabase + Fly GRU); throughput ≥ 50 events/s sustentável por 60s (sem timeout, sem deadlock)
4. **Append-only telemetria:** stress test que tenta `UPDATE events SET ... ; DELETE FROM events WHERE ...` 100 vezes → `GET /metrics` mostra `events_append_attempts_blocked_total{op="UPDATE"} = 100, op="DELETE" = 100`
5. **Partition migration:** migration aplicada em produção (Supabase) com S1 events copiados pra partições corretas; query `SELECT * FROM events WHERE workspace_id = ?` retorna mesmos 8 eventos validados em S1 (correlation_id `b75238fd-0a41-4d1e-8c3f-300fb342723f`) — zero perda
6. **`docs/EVENT_LOG.md`** existe no CKOS_RUNTIME documentando invariantes + schema + replay semantics + performance baseline + troubleshooting

**Quality gate Sprint Done:**
- 5 checks acima ✅
- CI verde (extensão dos workflows do S1)
- Deploy live em https://ckos-runtime.fly.dev mantém healthcheck 200 + S1 `/intent` continua funcionando idêntico (regression test)
- Doc 11 patch findings registrados (esperado: 1 — formalizar partition strategy na Doc 11 §7 línea 235)
- PMO valida via execução real de stress test contra deploy
- Founder assina via commit `sprint-done: S4`

---

## 6. Architecture Questions abertas — Founder/PMO decidem antes do dispatch

### 🔴 Trava-início (decidir ANTES do dispatch de implementação)

**AQ-S4-01 — Partition strategy: LIST por `aggregate_type` + RANGE por `created_at` mês, ou apenas RANGE por `created_at`?**

| Opção | Prós | Contras |
|---|---|---|
| (a) **LIST(aggregate_type) + RANGE(created_at month)** — recomendação PMO | Permite drop de partições inteiras (ex: dropar `LLMCost` antigos sem tocar workflow events); planning paralelo nas sub-partições | Mais complexo; precisa CREATE PARTITION pra cada combinação |
| (b) RANGE(created_at month) apenas | Mais simples; suficiente pra MVP | Não isola `LLMCost` de eventos de workflow; archival mais grosseiro |
| (c) Sem partição (deixar table flat) | Zero complexidade | Não escala >1M rows; viola Doc 11 §7 línea 235 |

**Recomendação PMO:** (a) — alinhada com Doc 11 §7 línea 235 "partição por `aggregate_type` + range por `created_at`". Custo inicial baixo (5 partições — uma por tipo); paga em alguns meses quando LLMCost dominar volume.

**AQ-S4-02 — Janela de idempotência: 24h / 7d / 30d / infinito?**

| Opção | Recomendação PMO | Implicação |
|---|---|---|
| (a) **24 horas** ← Rec PMO | Suficiente pra cobrir retries de cliente; cleanup leve | Cliente que reusar key após 24h cria novo intent (não-idempotente cross-day) |
| (b) 7 dias | Mais defensivo | Cleanup pesa mais; raro cliente precisar |
| (c) 30 dias | Compliance-friendly | Tabela cresce; CD demanda mais |
| (d) Infinito | Forte garantia | Não-LGPD-friendly; tabela vira monstro |

**Recomendação PMO:** (a) 24h — cobre casos de retry real (network glitch, deploy restart) sem virar log cross-session. Suficiente pra S4; podemos aumentar em S6 com policy de retenção.

**AQ-S4-03 — Performance targets: quais números são "pass" no exit criterion?**

Recomendação PMO (conservador pro free tier Supabase + Fly shared CPU 512MB):

| Métrica | Target S4 | Target stretch (informativo) |
|---|---|---|
| **P50 insert latency** | < 30ms | < 15ms |
| **P95 insert latency** | < 100ms | < 50ms |
| **P99 insert latency** | < 250ms | < 100ms |
| **Throughput sustentável 60s** | ≥ 50 events/s | ≥ 100 events/s |
| **Concorrência sem deadlock** | 100 workers paralelos | 500 workers |

Justificativa: Fly shared-cpu-1x + Supabase free tier (pooler limit ~60 conexões) impõem teto. Targets de S4 são "demonstrar arquitetura sólida"; otimização entra em F2 quando workload real definir.

### 🟡 Não-trava (decidir durante S4 ou logo após)

**AQ-S4-04 — Doc 11 §7 línea 235 formaliza partition strategy ANTES ou DEPOIS do S4?**

Opção (a): PATCH 3 leve no Doc 11 antes — formaliza canônico, S4 vira aplicação literal.
Opção (b): S4 implementa; descoberta vira PATCH 3 candidate gerado pelo executor (AQ-S1-06 pattern).
Opção (c): Não formalizar agora — Doc 11 §7 línea 235 já tem hint "partição + streams lógicos", suficiente como spec.

Recomendação PMO: (b) — segue o pattern AQ-S1-06 que funcionou em S1 (zero findings); executor reporta se a hint do Doc 11 foi suficiente ou se precisa expansão.

**AQ-S4-05 — Telemetria: `/metrics` em Prometheus text format basta, ou já introduzimos OpenTelemetry?**

Recomendação PMO: **Prometheus text** apenas em S4. OTEL traces distribuídos entram com S6 (Feedback/ROI/observability completa). Prometheus é minimal viable: 1 endpoint, parseável por qualquer scraper futuro.

**AQ-S4-06 — Idempotency cleanup job: pg-boss interno ou cron Fly Machine?**

Recomendação PMO: **pg-boss interno** (mesmo runtime, sem infra extra; consistência operacional com cleanup de outras tables futuras). Cron Fly entra se distribuirmos.

### 🟢 Defer (PATCH 3 ou sprints posteriores)

Já listadas em §2.2 — repetidas pra reforço: outbox pattern (S5), novos event types (S3/S5), memória longa (S6), CQRS projections (S5/F4), RLS forçada Supabase roles (S3), event compaction (F6/F7), audit log compliance (F7), multi-region (F6), OpenTelemetry (S6), F-01/F-02/F-03 (PATCH 3), Doc 11 users enrichment (PATCH 3).

---

## 7. Plano de dispatch (próximas sessões)

```txt
1. (AGORA) Charter publicado → Founder review + responde AQ-S4-01/02/03

2. Metacognik completeness audit (Claude Code fresh, mesmo pattern S1)
       → Sessão `S-F1S4-CHARTER-METAREV-CLAUDE-<DATE>-001`
       → Verifica: completeness escopo, coerência canônico, realismo exit criterion, AQs cobrindo gaps,
         performance targets factíveis no stack S1 production
       → Veredito: APROVA / APROVA-COM-AJUSTES / REPROVA

3. Se APROVA-COM-AJUSTES: Forma A (patch leve no charter v0.1.0→v0.2.0) — preferido per S1 precedent.
   Se APROVA: pular pra step 4.

4. Após Founder responder AQ-S4-01/02/03 + Metacognik APROVA:
       → PMO escreve `S-F1S4-IMPLEMENTATION-DISPATCH.md` em sessão SEPARADA desta
         (autocontido pra executor — pattern S1 dispatch §16 colável)
       → Especifica: partition migration SQL, idempotency endpoint contract, replay causal CTE,
         performance test harness, telemetria metrics format, docs/EVENT_LOG.md outline

5. Executor (Codex OU Claude Code fresh — per AQ-S1-03 inalterada) roda S4
       → Em sessão separada; clone existing CKOS_RUNTIME (não cria novo repo)
       → Branch base: `main` @ sha `1171384` (S1 production state)
       → Slices propostos (~7-9, executor refina):
         a) Migration partition (test em branch Supabase primeiro)
         b) Ingress idempotency table + middleware
         c) Concorrência tests
         d) Replay endpoint causal
         e) Append-only telemetria
         f) Performance baseline + bench script
         g) docs/EVENT_LOG.md
         h) docs/MIGRATIONS.md
         i) CI extension (test:concurrency)
       → Reporta progresso via PRs com label `s4-*` em CKOS_RUNTIME

6. Verificação de exit criterion
       → Executor self-test: roda 5 checks do §5 deste charter contra deploy live
         (ainda https://ckos-runtime.fly.dev — redeploy, não novo app)
       → Reporta JSON output no anexo do dispatch
       → PMO valida: stress test ao vivo + replay causal + telemetria metrics + bench numbers
       → Founder assina via commit `sprint-done: S4` + atualiza Kanban (S4 → ✅)

7. Sprint Done → atualizar kanban → iniciar S2 (Question Engine) OU S3 (Approval Gates)
       conforme §14 do backend plan (S2 e S3 podem rodar paralelos depois de S4 sólido)
```

---

## 8. BRA Packet + CHECKOUT RELEASE

```yaml
bra_id: BRA-F1S4-CHARTER-20260611-01
from_session: S-F1S4-CHARTER-CLAUDE-20260611-001
to: Founder + Metacognik
context_summary:
  - "S1 entregue em production validado fim-a-fim (commit 4ed637d, https://ckos-runtime.fly.dev, e2e $0.0221, 13/13 gates)"
  - "Kanban F1 indica S4 antes de S2/S3 (backend plan §14: Event Log estabilizado cedo)"
  - "Event log production-grade significa idempotência fim-a-fim + replay causal + partição + telemetria + baseline performance"
  - "Stack S1 reusado integralmente (TS + Fastify + Drizzle + pg-boss + Supabase Pooler + Fly GRU) — zero novas deps"
  - "Doc 11 §7 línea 235 já tem hint de partição; AQ-S4-04 decide formalizar antes ou após"
outputs:
  - "F1_SPRINT4_CHARTER.md (este): 9 deliverables IN, ~11 itens OUT, 6 AQs (3 trava-início), exit criterion binário 5 checks"
open_questions:
  - "AQ-S4-01 partition strategy (LIST+RANGE vs RANGE-only vs flat) — Founder confirma rec PMO LIST+RANGE?"
  - "AQ-S4-02 janela idempotência (24h vs 7d vs 30d vs ∞) — Founder confirma rec PMO 24h?"
  - "AQ-S4-03 performance targets — Founder confirma P95 <100ms + 50 events/s como pass?"
  - "AQ-S4-04 Doc 11 patch antes ou depois (Met decide)"
  - "AQ-S4-05 telemetria Prometheus vs OTEL (Met decide)"
  - "AQ-S4-06 cleanup job pg-boss vs cron (executor decide)"
blockers:
  - "AQ-S4-01/02/03 são trava-início pra dispatch. Charter destravado pela entrega S1."
risk_flags:
  - "P1 (Runtime core fortification): mitigado por escopo hardening (não muda contratos S1), reusa stack production validado, exit criterion mensurável via stress test"
  - "Risco operacional médio: partition migration em produção (S1 events serão movidos). Mitigação: migration testada em branch Supabase primeiro (`pnpm db:migrate:dry-run`)"
  - "Risco LLM zero: S4 não chama LLM (cost guard S1 inalterado)"
recommended_next:
  - "Founder lê + responde AQ-S4-01/02/03 (3 perguntas, ~10min)"
  - "Em paralelo: Metacognik completeness audit em Claude fresh"
  - "Após ambos: PMO escreve S-F1S4-IMPLEMENTATION-DISPATCH.md"
```

---

## 9. Founder Decision Log (2026-06-11)

Founder revisou o charter em 2026-06-11 e respondeu **"aceito 3 recs"** às AQs trava-início. Decisões registradas:

### AQ-S4-01 — Partition strategy: **(a) LIST(aggregate_type) + RANGE(created_at month)**

- Alinhada com Doc 11 §7 línea 235 ("partição por `aggregate_type` + range por `created_at`")
- 5 partições iniciais (uma por aggregate_type ativo) + sub-partições mensais
- Permite drop isolado de partições `LLMCost` antigas sem tocar workflow events
- Migration testada em branch Supabase antes de produção (deliverable #9 safety net)

### AQ-S4-02 — Janela de idempotência: **(a) 24 horas**

- Cobre retries reais (network glitch, deploy restart) sem virar log cross-session
- Cleanup leve via pg-boss job horário (`DELETE WHERE expires_at < now()`)
- Extensível em S6 com policy de retenção se necessidade real aparecer

### AQ-S4-03 — Performance targets: **P50 <30ms · P95 <100ms · P99 <250ms · ≥50 events/s sustentado 60s · 100 workers sem deadlock**

- Conservador pro free tier (Supabase pooler ~60 conexões + Fly shared-cpu-1x 512MB)
- Targets demonstram arquitetura sólida; otimização entra em F2 com workload real
- Stretch targets (P95 <50ms, 100 ev/s) ficam informativos no bench report, não gates

### AQs médias (não-trava — fluxo confirmado)

- **AQ-S4-04** (Doc 11 patch timing): opção (b) — executor implementa, findings viram PATCH 3 candidate (pattern AQ-S1-06 validado em S1 com 0 findings)
- **AQ-S4-05** (telemetria): Prometheus text format em S4; OTEL defer S6
- **AQ-S4-06** (cleanup job): pg-boss interno; executor confirma na implementação

### Próximo passo confirmado

Charter vai para **Metacognik completeness audit** (Claude Code fresh, mesmo pattern S1) — sessão `S-F1S4-CHARTER-METAREV-CLAUDE-20260611-001`. Após APROVA (com ou sem AJUSTES), PMO escreve `S-F1S4-IMPLEMENTATION-DISPATCH.md` com decisões acima embutidas.

---

```txt
CHECKOUT RELEASE — S-F1S4-CHARTER-CLAUDE-20260611-001
files_created: 000_ROADMAPS/22_CONSOLIDATION/F1_SPRINT4_CHARTER.md (este)
files_changed: 000_ROADMAPS/SESSION_REGISTRY.md (1 sessão; planejado)
files_not_touched: canônico 01-28 (RO — seções referenciadas: Doc 10 §5.3/§5.6/§5.26, Doc 11 §7, Doc 13 §16);
  S1 charter v0.3.0 (RO — pattern); S1 dispatch + anexo §17 (RO — baseline performance);
  CKOS_RUNTIME (não tocado nesta sessão — executor mexerá em sessão SEPARADA);
  ARCHITECTURE_PATCH_REPORT.md (charter não é canonical_patch); 00_SYSTEM_GOVERNANCE; demais docs
validation:
  - precondições verificadas com commit hashes (S1 done em 4ed637d)
  - escopo IN (9 deliverables hardening) + OUT (~11 defer) + PROIBIDO explícitos
  - contratos cite-only Doc 10 + Doc 11 (zero duplicação canônica)
  - tabela extension `ingress_idempotency` justificada como infra operacional (não-canônica, padrão de cache table)
  - exit criterion binário 5 checks (idempotência, replay causal, perf, telemetria, partition migration)
  - 6 AQs flagadas claramente (3 trava-início com PMO recs)
  - plano de dispatch em 7 etapas com Metacognik audit antes do executor
  - reusa stack S1 production-validated; zero novas deps
risks_remaining: P1 mitigado por escopo hardening + stack production; risco operacional médio (partition migration) com mitigação documentada
next_step: Founder review → responde 3 AQs trava-início → Metacognik completeness audit → dispatch
status: released
```
