---
title: F1 Sprint 4 — Implementation Dispatch (Event Log Hardening)
file: S-F1S4-IMPLEMENTATION-DISPATCH.md
layer: auxiliary
doc_type: pmo_implementation_dispatch
phase: 000_ROADMAPS
category: consolidation
status: ready_for_executor
version: 1.0.0
created_at: 2026-06-12
owner: pmo_ckos
responsible_agent: claude_fable_5 (pmo dispatcher)
session_id: S-F1S4-IMPLEMENTATION-DISPATCH-20260612-001
derives_from:
  - F1_SPRINT4_CHARTER.md v0.3.0 (commit 966e8c3)                      # fonte-de-verdade do escopo
  - L3_WAVE1/F1S4_CHARTER_METACOGNIK_REVIEW.md (commit 947cefa)        # APROVA-COM-AJUSTES + def-01..def-07
  - S-F1S1-IMPLEMENTATION-DISPATCH.md §17 production_deploy            # baseline S1 live
target_repo: https://github.com/danielck01/CKOS_RUNTIME                # branch base main @ 1171384
target_canonical: []                                                   # dispatch NÃO edita canônico 01-28
approval_required:
  - founder
non_authority_boundary: >
  Dispatch autocontido para o executor implementar o Sprint 4 no repo CKOS_RUNTIME. NÃO edita canônico
  01-28. NÃO escreve código nesta sessão (executor faz em sessão SEPARADA). Todas as decisões estão
  fechadas — o executor NÃO renegocia escopo; ambiguidade real = PARAR e perguntar ao PMO.
tags: [dispatch, implementation, f1, sprint-4, event-log, hardening, runtime, executor-ready]
---

# F1 Sprint 4 — Implementation Dispatch (Event Log Hardening)

> **Para o executor:** este arquivo é a spec completa. Charter v0.3.0 é a referência de escopo; este dispatch fecha TODAS as decisões + contratos técnicos. Se algo aqui contradisser o charter, **este dispatch prevalece** (foi escrito depois, com os AJUSTES do Metacognik embutidos).

---

## 0. Contexto + precondições (todas satisfeitas)

| Item | Estado | Referência |
|---|---|---|
| S1 entregue + production validado | ✅ 2026-06-11 | doc repo commit `4ed637d` (sprint-done: S1) |
| Runtime live | ✅ | https://ckos-runtime.fly.dev (Fly app `ckos-runtime`, org `its-ckcompany`, região `gru`, machine `2876d1dc699028`, auto_stop ativo) |
| Supabase produção | ✅ | projeto `dplcbmwsfrsphsxrfkav`, Session Pooler `aws-1-sa-east-1.pooler.supabase.com:5432` (Direct host é IPv6-only no free tier — NÃO usar), role `postgres.dplcbmwsfrsphsxrfkav` |
| 8 eventos S1 reais em produção | ✅ | correlation_id `b75238fd-0a41-4d1e-8c3f-300fb342723f` (4 workflow + 4 LLMCost) |
| CKOS_RUNTIME main | ✅ | sha `1171384` (12 PRs, 52/52 testes) |
| Charter S4 v0.3.0 (Founder + Metacognik) | ✅ | doc repo commit `966e8c3`; AJUSTES 01-05 aplicados; review em `947cefa` |
| Founder decisions AQ-S4-01/02/03 | ✅ | charter §9 |

**Custo LLM do S4: $0.** Nenhum deliverable chama LLM. Cost guard S1 permanece intocado.

---

## 1. Repo + branch discipline

- **Repo:** https://github.com/danielck01/CKOS_RUNTIME (mesmo de S1 — mono-runtime, multi-sprint)
- **Branch base:** `main` @ `1171384`
- **PRs:** 1 por slice estável, branch naming `s4-<slice>` (ex: `s4-telemetry`, `s4-partition`), label `s4-*`
- **Doc repo (https://github.com/danielck01/CKOS):** READ-ONLY para o executor. Findings de Doc 11 vão em arquivo novo via PR separado (ver §10)

---

## 2. Tech stack — ZERO novas dependências

Reusa integralmente o stack S1 production-validated:

| Camada | Lib (já no repo) | Uso em S4 |
|---|---|---|
| Runtime | TS 5.4+ / Node 20 / pnpm 9 | inalterado |
| HTTP | Fastify 4 + Zod | rotas novas: `GET /metrics`, `GET /events/replay/:correlation_id` |
| DB | Drizzle ORM + postgres.js | **fixar `max: 20` explícito no client** (def-03 — default era 10 implícito); migrations de partição são **SQL custom** (drizzle-kit não gera DDL de partição; `schema.ts` segue mapeando `events`) |
| Jobs | pg-boss 9+ | job novo: cleanup horário de `ingress_idempotency` |
| Testes | Vitest (`test.concurrent` nativo) | concorrência + bench |
| Logs | Pino | inalterado |
| Deploy | Fly.io (mesmo app, `fly deploy`) | migration roda com app PARADO (ver §8) |

**Proibido adicionar:** Prometheus client lib (o `/metrics` é text format gerado à mão — 1 counter), OTEL, qualquer queue/scheduler novo.

---

## 3. Decisões fechadas (executor NÃO renegocia)

### 3.1 Founder decisions (charter §9)

| AQ | Decisão |
|---|---|
| **AQ-S4-01** | Partição **LIST(`aggregate_type`) + RANGE(`created_at`) mensal** |
| **AQ-S4-02** | Janela de idempotência: **24 horas** |
| **AQ-S4-03** | Targets: **P50 <30ms · P95 <100ms · P99 <250ms · ≥50 events/s sustentado 60s · 100 workers sem deadlock**. Stretch (P95 <50ms, ≥100 ev/s) = informativo no bench report, não gate |

### 3.2 AQs médias (charter §9)

| AQ | Decisão |
|---|---|
| **AQ-S4-04** | Opção (b): executor implementa; descobertas viram findings em `F1S4_DOC11_PATCH_FINDINGS.md` (§10). **2 findings já esperados** — ver §10 |
| **AQ-S4-05** | Prometheus **text format** apenas (sem lib, sem OTEL) |
| **AQ-S4-06** | Cleanup job = **pg-boss interno** (mesmo runtime) |

### 3.3 Defers do Metacognik review (def-01..def-07 — cláusulas vinculantes)

| ID | Cláusula |
|---|---|
| **def-01** | `GET /metrics` protegido pelo **mesmo middleware mock JWT do `/intent`** (`Authorization: Bearer test-user-jwt-{user_id}`). NÃO público, NÃO IP allowlist |
| **def-02** | `request_hash = sha256(canonical_json({ intent_text, user_id, workspace_id, project_id: project_id ?? null }))` — JSON canônico (keys ordenadas, sem whitespace); `project_id` SEMPRE presente com `null` explícito; campos voláteis (timestamps, headers) FORA do hash. Consequência aceita: com/sem `project_id` → hashes diferentes (intents semanticamente distintas) |
| **def-03** | postgres.js client com `max: 20` **explícito**; o bench implementa 100 workers como **concorrência in-process** (Promise pool) enfileirando sobre o pool de conexões — NÃO 100 conexões reais (Session Pooler tem ~60; app + pg-boss já usam ~20). Documentar os 2 pools em `docs/EVENT_LOG.md` |
| **def-04** | Eventos de bench são **permanentes** (append-only, sem DELETE). Bench pleno (1000+ eventos) roda em **Postgres local**; contra produção roda só um **smoke reduzido** (≤100 eventos) com `workspace_id` dedicado `00000000-0000-0000-0000-00000000bench` documentado em `docs/EVENT_LOG.md` |
| **def-05** | ~25 `fk→events` do Doc 11 (tabelas S3/S5+) são impossíveis como FK simples pós-partição → registrar como finding (§10), NÃO resolver em S4 |
| **def-06** | Anchor Doc 13 §16 da telemetria aceito como "preparação" — sem ação |
| **def-07** | Partições LIST iniciais: **enumerar os `aggregate_type` realmente presentes no DB de produção** (`SELECT DISTINCT aggregate_type FROM events`) + **DEFAULT partition obrigatória**. NÃO criar 12 partições vazias do enum completo. (Esperado hoje: `workflow` + possivelmente 1-2 outros — confirmar no DB e reportar no anexo §14) |

---

## 4. Escopo IN — 9 deliverables (charter §2.1 v0.3.0, com AJUSTES embutidos)

| # | Deliverable | Detalhe técnico |
|---|---|---|
| 1 | **Idempotência no ingress** | Header `X-Idempotency-Key` (UUID v4) no `POST /intent`. 2ª chamada com mesmo key+workspace dentro de 24h → 200 com `correlation_id` original, zero evento novo. Sem header → comportamento atual (não-idempotente, backward-compat) |
| 2 | **`ingress_idempotency` table** | SQL em §6.1 + middleware + cleanup pg-boss horário |
| 3 | **Replay endpoint** | `GET /events/replay/:correlation_id?ordering=causal\|temporal` — §6.5. `/trace` de S1 fica INTOCADO |
| 4 | **Partição de `events`** | LIST+RANGE com PK/unique compostas + DEFAULT partition — §6.2. Migration com app parado — §8 |
| 5 | **Telemetria append-only** | Trigger v2 `RETURN NULL` + `RAISE WARNING` + counter persistente `ops_counters` + `GET /metrics` — §6.3/§6.4. **NÃO usar `RAISE EXCEPTION`** (aborta transação e desfaz o increment) |
| 6 | **Performance baseline** | `pnpm bench:events` — §7.3. Resultados em `docs/EVENT_LOG.md` |
| 7 | **Concorrência tests** | 50 POSTs paralelos mesmo key → exatamente 1 evento — §7.1 |
| 8 | **`docs/EVENT_LOG.md`** | Outline em §9 |
| 9 | **Migration safety net** | Ensaio em PG15 local (mesmo ambiente de testes S1); dry-run = `BEGIN … ROLLBACK`; **recriar trigger v2 + índices na nova parent é parte do deliverable**; rollback documentado em `docs/MIGRATIONS.md` |

### Regression obrigatória (não-negociável)

- `POST /intent` SEM o header novo continua funcionando **idêntico** a S1 (e2e mockado de S1 verde)
- `GET /trace/:correlation_id` retorna os 8 eventos S1 **byte-idênticos** pós-migration (dump ordenado por `id` antes/depois do swap)
- Testes S1 que esperavam **exceção** em UPDATE/DELETE passam a esperar **0 rows affected + dados intactos** (consequência do trigger v2 — atualizar esses testes faz parte do slice de telemetria)

---

## 5. Escopo OUT + PROIBIDO

**OUT (defer — charter §2.2):** outbox/Event Bus (S5) · novos event types (S3/S5) · memória longa (S6) · CQRS projections (S5/F4) · RLS Supabase roles (S3) · compaction (F6/F7) · compliance (F7) · multi-region (F6) · OTEL (S6) · F-01/F-02/F-03 + Doc 11 users enrichment (PATCH 3).

**PROIBIDO (charter §2.3):**
- Editar canônico 01-28 (doc repo é READ-ONLY)
- Mudar contratos/payloads dos 4 eventos workflow + 4 LLMCost
- Novos endpoints de negócio (só `/metrics` operacional + `/events/replay`)
- Chamar LLM (custo S4 = $0)
- Schemas SQL fora de: partição de `events` + `ingress_idempotency` + `ops_counters`
- Skip do teste de concorrência
- `RAISE EXCEPTION` no trigger append-only (AJUSTE-01)
- Partição LIST sem DEFAULT (AJUSTE-02)
- Rodar a migration de produção com o app rodando (§8)

---

## 6. Contratos técnicos (literal — pronto pra implementar)

### 6.1 `ingress_idempotency`

```sql
CREATE TABLE ingress_idempotency (
  key uuid PRIMARY KEY,                  -- client-provided X-Idempotency-Key
  workspace_id uuid NOT NULL,
  correlation_id uuid NOT NULL,          -- ref ao evento criado na 1ª chamada
  request_hash text NOT NULL,            -- def-02: sha256(canonical_json({intent_text,user_id,workspace_id,project_id??null}))
  created_at timestamptz NOT NULL DEFAULT now(),
  expires_at timestamptz NOT NULL        -- created_at + interval '24 hours' (AQ-S4-02)
);
CREATE INDEX ingress_idempotency_expires_idx ON ingress_idempotency (expires_at);
```

**Middleware (no `POST /intent`, APÓS auth, ANTES de publicar evento):**

| Cenário | Resposta |
|---|---|
| Sem `X-Idempotency-Key` | fluxo S1 inalterado (202) |
| Key nova | processa normal; grava row com `correlation_id` + `request_hash`; 202 |
| Key existente + mesmo `workspace_id` + mesmo `request_hash` | **200** `{ correlation_id: <original>, idempotent_replay: true }` — zero evento novo |
| Key existente + mesmo `workspace_id` + `request_hash` DIFERENTE | **409 Conflict** `{ error: "idempotency_key_reuse" }` |
| Key existente mas `expires_at < now()` | trata como key nova (sobrescreve a row) |

**Atomicidade:** o INSERT na `ingress_idempotency` e a publicação do evento devem estar na **mesma transação** (ou INSERT ... ON CONFLICT como guard) — 2 requests simultâneos com a mesma key nova não podem AMBOS publicar evento (é exatamente o que o teste §7.1 verifica).

**Cleanup:** pg-boss job horário `DELETE FROM ingress_idempotency WHERE expires_at < now()`.

### 6.2 Partição de `events` (AJUSTE-02 embutido)

```sql
-- Restrição Postgres: PK/UNIQUE em particionada DEVEM incluir as partition keys.
CREATE TABLE events_partitioned (
  -- mesmas colunas da events atual (copiar de schema.ts / Doc 11 §7), MAS:
  PRIMARY KEY (id, aggregate_type, created_at)
) PARTITION BY LIST (aggregate_type);

-- Sub-partição RANGE mensal dentro de cada LIST partition:
CREATE TABLE events_workflow PARTITION OF events_partitioned
  FOR VALUES IN ('workflow') PARTITION BY RANGE (created_at);
CREATE TABLE events_workflow_2026_06 PARTITION OF events_workflow
  FOR VALUES FROM ('2026-06-01') TO ('2026-07-01');
-- (criar a partição do mês corrente + próximo mês; job/nota pra criação futura em docs/MIGRATIONS.md)

-- DEFAULT partition OBRIGATÓRIA (aggregate_types novos de S3/S5 não podem quebrar produção):
CREATE TABLE events_default PARTITION OF events_partitioned DEFAULT;

-- Índice de idempotência vira COMPOSTO (a unicidade global deixa de ser por índice):
CREATE UNIQUE INDEX events_idem_idx ON events_partitioned (idempotency_key, aggregate_type, created_at);
```

**Mitigação da perda de unicidade global** (já canônica — Doc 10 §5.6 "consulta event log antes de aplicar"): o event publisher mantém/ganha guard app-side por `idempotency_key` antes do INSERT; o caminho de ingress já é coberto pela `ingress_idempotency`. Registrar o conflito Doc 11 §7 linha 232 × linhas 214-217 como finding (§10).

**Backward-compat:** após o swap (rename), criar `CREATE VIEW events AS SELECT * FROM events_partitioned` **OU** renomear a particionada para `events` — preferência: **rename direto** (a parent particionada é queryável como tabela normal; view só se o Drizzle reclamar de introspecção). Decidir no ensaio local e documentar a escolha no anexo §14.

**Partições iniciais (def-07):** rodar `SELECT DISTINCT aggregate_type FROM events` em produção; criar LIST partitions só para os valores reais + DEFAULT. Reportar a lista no anexo §14.

### 6.3 Trigger append-only v2 (AJUSTE-01 — substitui o `events_no_update_delete` de S1)

```sql
CREATE OR REPLACE FUNCTION events_block_mutation() RETURNS trigger AS $$
BEGIN
  -- NÃO usar RAISE EXCEPTION: aborta a transação e desfaz o increment abaixo.
  UPDATE ops_counters SET value = value + 1
    WHERE name = 'events_append_attempts_blocked_total{op="' || TG_OP || '"}';
  RAISE WARNING 'append-only violation blocked: % on events (row id %)', TG_OP, OLD.id;
  RETURN NULL;  -- skip silencioso da row — invariante preservado, transação sobrevive
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER events_no_update_delete
  BEFORE UPDATE OR DELETE ON events_partitioned
  FOR EACH ROW EXECUTE FUNCTION events_block_mutation();
-- PG15 clona BEFORE ROW triggers da parent para todas as partições (inclusive futuras).
-- ATENÇÃO: o trigger NÃO migra na cópia — recriar na nova parent é parte do deliverable #9.
```

**Trade-off aceito (AJUSTE-01):** UPDATE/DELETE passam a "succeed" com 0 rows affected em vez de erro. Atualizar os testes S1 que esperavam exceção (ver §4 regression).

### 6.4 `ops_counters` + `GET /metrics`

```sql
CREATE TABLE ops_counters (
  name text PRIMARY KEY,        -- ex: events_append_attempts_blocked_total{op="UPDATE"}
  value bigint NOT NULL DEFAULT 0
);
INSERT INTO ops_counters (name) VALUES
  ('events_append_attempts_blocked_total{op="UPDATE"}'),
  ('events_append_attempts_blocked_total{op="DELETE"}');
```

`GET /metrics` (auth def-01 — mesmo mock JWT do `/intent`) responde `text/plain; version=0.0.4`:

```
# HELP events_append_attempts_blocked_total Mutations blocked by append-only trigger
# TYPE events_append_attempts_blocked_total counter
events_append_attempts_blocked_total{op="UPDATE"} 100
events_append_attempts_blocked_total{op="DELETE"} 100
```

Counter é Postgres (sobrevive a `auto_stop_machines` do Fly) — NÃO memória de processo.

### 6.5 Replay endpoint (AJUSTE-04 embutido)

```
GET /events/replay/:correlation_id?ordering=temporal   (default)
  → created_at ASC (mesma semântica do /trace de S1; /trace permanece intocado)
GET /events/replay/:correlation_id?ordering=causal
  → ordem topológica do DAG
```

**Semântica causal (fechada — não reinterpretar):**
1. Roots = eventos com `causation_id IS NULL`, ordenados por `created_at` ASC
2. Todo evento aparece DEPOIS do seu causador (quando o causador está no mesmo correlation_id)
3. Desempate: `created_at` ASC
4. **Side-chains (os 4 LLMCost de S1) são INCLUÍDOS** como filhos do evento que os causou — não excluídos, não flag separada
5. Implementação: recursive CTE seguindo `causation_id`, `LIMIT 100` hops defensivo contra ciclos
6. **Dado a CONFIRMAR antes de fechar o teste do check 2:** o valor real de `causation_id` dos 4 LLMCost de S1 em produção (NULL? aponta pro IntentSubmitted/IntentResolved?). Rodar `SELECT id, event_type, causation_id FROM events WHERE correlation_id = 'b75238fd-0a41-4d1e-8c3f-300fb342723f' ORDER BY created_at` e **reportar no anexo §14**. O teste valida a invariante topológica genérica (robusta a qualquer forma do DAG), não uma cadeia linear

Auth: mesmo mock JWT de S1.

---

## 7. Testing strategy

### 7.1 Concorrência (deliverable #7 — crítico)

`tests/integration/idempotency_concurrent.test.ts`:
- 50 POSTs `/intent` paralelos (`Promise.all`) com MESMO `X-Idempotency-Key` + mesmo body → exatamente **1 evento `IntentSubmitted`** no DB; as 50 respostas carregam a MESMA `correlation_id`; nenhum deadlock
- 2 POSTs mesma key + body DIFERENTE → 1× sucesso + 1× 409
- Key expirada (mock clock ou `expires_at` manipulado direto no DB de teste) → tratada como nova

### 7.2 Append-only stress (check 4)

100× `UPDATE events SET …` + 100× `DELETE FROM events WHERE …` em **autocommit** → 0 rows alteradas/deletadas (dump byte-idêntico antes/depois) + `GET /metrics` mostra os 2 counters = 100 + counter sobrevive a restart (Postgres).

### 7.3 Bench (deliverable #6, def-03/def-04)

`pnpm bench:events` — script standalone (não Vitest):
- 100 workers **in-process** (Promise pool sobre o postgres.js client `max: 20`) × 10 INSERTs = 1000 eventos
- Mede P50/P95/P99 de INSERT latency + throughput sustentado 60s
- **Local PG15:** bench pleno (1000+ eventos)
- **Produção:** smoke reduzido ≤100 eventos com `workspace_id` de bench (def-04) — eventos ficam pra sempre, são marcados pelo workspace
- Output: tabela markdown pronta pra colar em `docs/EVENT_LOG.md` + JSON pro anexo §14

### 7.4 Regression S1

- e2e mockado de S1 verde sem alteração de comportamento (POST sem header novo)
- `GET /trace/:correlation_id` byte-idêntico pós-migration (check 5)
- Testes de trigger atualizados (exceção → 0 rows)

---

## 8. Migration runbook (deliverable #9 — AJUSTE-03 embutido)

```txt
ENSAIO (local PG15 — mesmo ambiente de testes S1):
  1. Restaurar snapshot do schema de produção (drizzle migrations S1 + seed)
  2. Rodar a migration completa: create partitioned → copy → recriar trigger v2 + índices → swap
  3. pnpm db:migrate:dry-run = BEGIN … ROLLBACK (EXPLAIN não simula DDL)
  4. Verificar: SELECT count(*) idêntico; GET /trace local idêntico; trigger v2 ativo (UPDATE → 0 rows + counter++)
  5. Repetir até o script ser determinístico

PRODUÇÃO (janela de minutos — aceita: 1 usuário, auto_stop já ativo):
  1. Dump de verificação: SELECT * FROM events ORDER BY id → arquivo before.json
  2. fly machine stop 2876d1dc699028        # app PARADO = zero writes concorrentes
  3. Rodar migration via psql/script contra o Pooler
  4. Verificação: count + dump after.json byte-idêntico ao before.json
  5. fly machine start
  6. Smoke: GET /health 200 + GET /trace/b75238fd-... retorna os 8 eventos
  7. Anunciar no PR da migration (janela + duração real)

ROLLBACK (documentar em docs/MIGRATIONS.md):
  - Antes do swap: DROP das tabelas novas, nada mudou
  - Depois do swap: rename reverso (a flat original é preservada como events_flat_backup até Sprint Done)
```

---

## 9. `docs/EVENT_LOG.md` (deliverable #8 — outline)

1. Invariantes (append-only com trigger v2 + semântica 0-rows; idempotência ingress + janela 24h; ordering temporal vs causal; partição LIST+RANGE + DEFAULT)
2. Schema (campos Doc 11 §7 + 6 extras da reconciliação S1; PK/índices compostos pós-partição + por quê)
3. Replay semantics (DAG topológico, side-chains, /trace vs /events/replay)
4. Connection pools (app `max: 20` + pg-boss próprio ~10; Session Pooler ~60 total)
5. Performance baseline (tabela do bench local + smoke produção + data + sha)
6. Bench workspace dedicado (def-04) + por que eventos de bench são permanentes
7. Troubleshooting (counter não incrementa? partição DEFAULT recebendo eventos inesperados? pooler esgotado?)

---

## 10. Doc 11 patch findings (AQ-S4-04 opção b)

Arquivo NO DOC REPO via PR separado: `000_ROADMAPS/22_CONSOLIDATION/F1S4_DOC11_PATCH_FINDINGS.md`.

**2 findings já conhecidos (registrar mesmo que nada novo apareça):**

```md
## FIND-01 — unique(idempotency_key) global impossível em tabela particionada — 2026-06-12
Doc 11 §7 linha 232 (`idx: idempotency_key unique`) × linhas 214-217 (partição LIST+RANGE) são
mutuamente incompatíveis em Postgres (PK/UNIQUE exigem partition keys). Implementado: índice composto
(idempotency_key, aggregate_type, created_at) + guarda app-side (Doc 10 §5.6) + ingress_idempotency.
Sugestão PATCH 3: Doc 11 §7 formalizar partition strategy + índice composto + nota de mitigação.

## FIND-02 — ~25 fk→events do Doc 11 impossíveis como FK simples pós-partição — 2026-06-12
Tabelas S3/S5+ (ex: run_state_transitions linha 248) declaram fk→events. FK para particionada exige
referenciar as partition keys. Opções pro PATCH 3: FK composto OU integridade app-side (padrão comum
em event sourcing). Não bloqueia S4 (nenhuma tabela S1 implementada tem FK→events).
```

- Template para findings novos: `## FIND-{NN} — {título} — {data}` + descrição + sugestão
- NÃO commitar direto no doc repo — PR separado

---

## 11. Sprint Done quality gate (charter §5 v0.3.0 — 6 checks + operacional)

- [ ] **Check 1 — Idempotência:** 50 POSTs paralelos mesmo key → 1 evento, mesma correlation_id nas 50 respostas
- [ ] **Check 2 — Replay causal:** 8 eventos S1 em ordem topológica (roots NULL primeiro; causador antes do causado; desempate created_at ASC); causation_id real dos LLMCost confirmado e reportado
- [ ] **Check 3 — Performance:** P50 <30ms · P95 <100ms · P99 <250ms · ≥50 ev/s por 60s · 100 workers in-process sem deadlock (bench local pleno + smoke produção)
- [ ] **Check 4 — Telemetria:** 100 UPDATE + 100 DELETE autocommit → 0 rows + dump byte-idêntico + `/metrics` mostra 100/100 + counter sobrevive restart
- [ ] **Check 5 — Partition migration:** produção migrada; `SELECT` + `GET /trace` retornam os 8 eventos byte-idênticos (dump before/after) — zero perda, zero mutação
- [ ] **Check 6 — `docs/EVENT_LOG.md`** existe e cobre o outline §9
- [ ] CI verde (workflows S1 + extensão test:concurrency)
- [ ] Regression: `/intent` sem header idêntico a S1; e2e mockado verde; healthcheck 200
- [ ] `F1S4_DOC11_PATCH_FINDINGS.md` com FIND-01/FIND-02 (+ novos se houver) via PR no doc repo
- [ ] Executor self-test: 6 checks rodados contra deploy live; JSON no anexo §14
- [ ] **PMO valida:** stress test ao vivo + replay causal + metrics + bench numbers
- [ ] **Founder assina** via commit `sprint-done: S4` + Kanban (S4 → ✅)

---

## 12. Separação de papéis

| Sessão | Agent | Papel |
|---|---|---|
| `S-F1S4-CHARTER-CLAUDE-20260611-001` | claude_opus_4_7 | Autora do charter |
| `S-F1S4-CHARTER-METAREV-CLAUDE-20260611-001` | Claude fresh | Metacognik audit (APROVA-COM-AJUSTES) |
| `S-F1S4-CHARTER-AJUSTES-CLAUDE-20260612-001` + esta | claude_fable_5 (PMO Dispatcher) | AJUSTES Forma A + este dispatch |
| `S-F1S4-IMPL-EXEC-<DATE>-001` | **Codex OU Claude Code fresh** | **Executor — implementa S4 no CKOS_RUNTIME** |
| `S-F1S4-VERIFY-<DATE>-001` | PMO + Founder | Verifica exit criterion + Sprint Done |

**Executor NÃO pode ser:** a sessão PMO Dispatcher, nem Windsurf (runtime ≠ APPLY mecânico per política de executores).

---

## 13. PROMPT PARA EXECUTOR (cola num chat Codex OU Claude Code fresh)

```txt
You are the F1 Sprint 4 IMPLEMENTATION EXECUTOR for CKOS (Event Log Hardening).
SESSION: S-F1S4-IMPL-EXEC-<TODAY>-001 (criar timestamp).

CONTEXT:
- Repo doc canônico (READ-ONLY): https://github.com/danielck01/CKOS @ commit 966e8c3
- Repo de implementação (WRITE): https://github.com/danielck01/CKOS_RUNTIME — branch base main @ 1171384
  (S1 já entregue: 12 PRs, 52/52 testes, produção live em https://ckos-runtime.fly.dev)
- Você é executor fresco. NÃO é o PMO Dispatcher. NÃO é Windsurf.
- Custo LLM deste sprint: $0 (nenhum deliverable chama LLM).

READ FIRST (no doc repo @ 966e8c3):
  1. 000_ROADMAPS/22_CONSOLIDATION/S-F1S4-IMPLEMENTATION-DISPATCH.md   (este arquivo — spec autocontida; PREVALECE sobre o charter)
  2. 000_ROADMAPS/22_CONSOLIDATION/F1_SPRINT4_CHARTER.md               (charter v0.3.0 — referência de escopo)
  3. 03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md §7             (events físico — linhas 214-237)
  4. 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md §5.3 + §5.6 + §5.26  (event log, idempotency, replay)
E no CKOS_RUNTIME: README + docs/ + src/db/schema.ts + o trigger events_no_update_delete de S1.

DECISÕES FECHADAS (não renegociar — detalhe completo no dispatch §3/§6):
  - Partição LIST(aggregate_type)+RANGE(created_at mensal); PK (id, aggregate_type, created_at);
    índice idem composto; DEFAULT partition OBRIGATÓRIA; partições iniciais = SELECT DISTINCT do DB real
  - Idempotência ingress: header X-Idempotency-Key, janela 24h, tabela ingress_idempotency,
    request_hash = sha256(canonical_json({intent_text,user_id,workspace_id,project_id??null})),
    200 replay / 409 conflict / mesma transação que o publish
  - Trigger append-only v2: RETURN NULL + RAISE WARNING + increment em ops_counters.
    NUNCA RAISE EXCEPTION (desfaz o próprio increment). Testes S1 que esperavam exceção → 0 rows.
  - GET /metrics: Prometheus text à mão, auth = mesmo mock JWT do /intent. Sem lib nova.
  - GET /events/replay/:correlation_id?ordering=causal|temporal — rota NOVA; /trace fica INTOCADO.
    Causal = ordem topológica DAG (roots causation_id NULL primeiro, causador antes, desempate
    created_at ASC, LLMCost INCLUÍDOS como filhos, CTE recursivo LIMIT 100)
  - postgres.js max: 20 explícito; bench = 100 workers IN-PROCESS sobre o pool (não 100 conexões)
  - Bench pleno em PG15 local; produção só smoke ≤100 eventos com workspace de bench
    00000000-0000-0000-0000-00000000bench (eventos são permanentes — append-only)
  - Migration de produção com APP PARADO (fly machine stop) — runbook completo no dispatch §8

IMPLEMENT in this order (1 PR por slice, branch s4-*):
  Slice 1: ops_counters + trigger v2 + GET /metrics (na tabela flat atual) + atualizar testes S1 de trigger
  Slice 2: partition migration — ensaio completo em PG15 local + docs/MIGRATIONS.md (dispatch §6.2 + §8)
  Slice 3: migration EM PRODUÇÃO (app parado, dump before/after byte-idêntico, smoke /trace)
  Slice 4: ingress_idempotency + middleware + cleanup pg-boss + 409 semantics (dispatch §6.1)
  Slice 5: concorrência tests (50 paralelos → 1 evento) (dispatch §7.1)
  Slice 6: GET /events/replay causal/temporal + CONFIRMAR causation_id real dos 4 LLMCost de S1
           (SELECT no DB de produção — reportar no anexo ANTES de fechar o teste do check 2)
  Slice 7: bench:events harness + baseline local + smoke produção (dispatch §7.3)
  Slice 8: docs/EVENT_LOG.md (outline dispatch §9)
  Slice 9: CI extension (test:concurrency) + regression e2e S1 verde

WHILE IMPLEMENTING:
  - Findings de Doc 11 → F1S4_DOC11_PATCH_FINDINGS.md no DOC REPO via PR separado.
    JÁ REGISTRAR FIND-01 (unique×partição) e FIND-02 (fk→events) — texto pronto no dispatch §10
  - Ambiguidade real na spec → PARAR e perguntar ao PMO (não adivinhar)
  - Conventional commits; 1 PR por slice estável

FORBIDDEN:
  - Editar canônico 01-28, charter ou este dispatch
  - Mudar payloads dos eventos S1; novos endpoints de negócio; chamar LLM
  - RAISE EXCEPTION no trigger; partição sem DEFAULT; migration de produção com app rodando
  - Features OUT: outbox, novos event types, memória longa, CQRS, RLS roles, OTEL, compaction

EXIT CRITERION (dispatch §11 — 6 checks):
  idempotência 50-paralelos → 1 evento; replay causal topológico dos 8 eventos S1;
  P95 <100ms + ≥50 ev/s 60s + 100 workers; telemetria 100/100 + counter sobrevive restart;
  migration zero perda (byte-idêntico em SELECT e GET /trace); docs/EVENT_LOG.md completo.

WHEN DONE:
  - Preencher anexo §14 do dispatch (JSON dos 6 checks + causation_id dos LLMCost + lista de
    partições criadas + escolha rename-vs-view + bench numbers) via PR no doc repo
  - Avisar PMO via comment no PR; PMO valida; Founder assina sprint-done: S4
```

---

## 14. Anexo (executor preenche)

```yaml
implementation_session_id: S-F1S4-IMPL-EXEC-<DATE>-001
executor_agent: <preencher>
ckos_runtime_main_branch_sha_before: "1171384"
ckos_runtime_main_branch_sha_after: <preencher>
pr_history: []                      # 1 linha por slice
llmcost_causation_confirmed:        # dado a confirmar ANTES do teste do check 2 (dispatch §6.5 item 6)
  query_output: <SELECT id, event_type, causation_id ... ORDER BY created_at>
  semantics_found: <NULL | aponta pro IntentSubmitted | aponta pro IntentResolved | misto>
partitions_created: []              # def-07: lista real (DISTINCT do DB) + DEFAULT
swap_strategy: <rename | view>      # decisão do ensaio local (dispatch §6.2)
migration_window:
  stopped_at: <ts>
  started_at: <ts>
  duration_min: <n>
  dump_before_sha256: <hash>
  dump_after_sha256: <hash>         # DEVE ser idêntico
exit_criterion_checks:              # 6 checks do §11 com evidência
  check1_idempotency: <pass|fail + evidência>
  check2_replay_causal: <pass|fail + evidência>
  check3_performance: { p50_ms: , p95_ms: , p99_ms: , throughput_eps: , workers: 100, deadlocks: 0, env: local+prod_smoke }
  check4_telemetry: { update_blocked: 100, delete_blocked: 100, rows_mutated: 0, survives_restart: true }
  check5_migration: <pass|fail + byte-idêntico SELECT e /trace>
  check6_docs: <pass|fail>
regression:
  s1_e2e_mocked: <verde|vermelho>
  trace_endpoint_byte_identical: <true|false>
  trigger_tests_updated: <true|false>
doc11_findings_count: <n>           # mínimo 2 (FIND-01 + FIND-02)
spec_deviations: []                 # qualquer desvio operacional, com motivo
ready_for_pmo_verification: <true|false>
```

---

## 15. BRA + CHECKOUT RELEASE

```yaml
bra_id: BRA-F1S4-DISPATCH-20260612-01
from_session: S-F1S4-IMPLEMENTATION-DISPATCH-20260612-001
to: Founder (approval) + Executor (Codex OU Claude fresh — a abrir)
context_summary:
  - "Charter S4 v0.3.0 com AJUSTES 01-05 Metacognik aplicados (commits 947cefa + 966e8c3)"
  - "Stack S1 reusado integral — zero novas deps; custo LLM $0"
  - "6 AQs fechadas (S4-01/02/03 Founder + S4-04/05/06) + 7 defers do review embutidos como cláusulas (def-01..def-07)"
  - "Contratos literais: ingress_idempotency SQL + partition DDL com PK/índices compostos + DEFAULT + trigger v2 RETURN NULL + replay CTE topológico + /metrics text format"
  - "Migration runbook: ensaio PG15 local → produção com app parado → dump byte-idêntico → rollback documentado"
  - "2 Doc 11 findings pré-redigidos (FIND-01 unique×partição; FIND-02 fk→events) — executor registra via PR"
outputs:
  - "S-F1S4-IMPLEMENTATION-DISPATCH.md (este): spec autocontida pro executor arrancar S4"
open_questions: []
blockers: []
risk_flags:
  - "P1 (migration de produção move os 8 eventos S1): mitigado por ensaio local + app parado + dump byte-idêntico + flat preservada como backup até Sprint Done"
  - "Risco zero LLM; risco baixo de pooler (max:20 explícito + workers in-process)"
recommended_next:
  - "Founder aprova commit deste dispatch"
  - "Founder cola §13 num chat executor fresh (Codex OU Claude Code; NÃO Windsurf)"
  - "Executor abre PRs s4-* no CKOS_RUNTIME; PMO acompanha"
  - "Pós Sprint Done: S2 (Question Engine) ∥ S3 (Approval Gates) podem rodar paralelos"
```

```txt
CHECKOUT RELEASE — S-F1S4-IMPLEMENTATION-DISPATCH-20260612-001
files_created: 000_ROADMAPS/22_CONSOLIDATION/S-F1S4-IMPLEMENTATION-DISPATCH.md (este)
files_changed: 000_ROADMAPS/SESSION_REGISTRY.md (1 sessão)
files_not_touched: canônico 01-28 (RO); charter v0.3.0 (RO — fonte de escopo); review Metacognik (RO);
  CKOS_RUNTIME (executor mexerá em sessão SEPARADA); ARCHITECTURE_PATCH_REPORT.md; 00_SYSTEM_GOVERNANCE/*
validation: decisões 100% fechadas (3 Founder + 3 médias + 7 defers como cláusulas); contratos SQL/HTTP
  literais com AJUSTES 01-05 embutidos; runbook de migration com janela + rollback; quality gate 6 checks
  + regression + findings; prompt executor §13 colável; anexo §14 template com dados-a-confirmar
risks_remaining: P1 migration mitigado (ensaio + app parado + backup); causation_id dos LLMCost é dado
  a confirmar pelo executor (check 2 robusto a qualquer forma do DAG)
next_step: Founder aprova commit → cola §13 no executor fresh → S4 roda
status: released
```
