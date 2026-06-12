---
title: F1 Sprint 4 Charter — Metacognik Completeness Review (read-only)
file: F1S4_CHARTER_METACOGNIK_REVIEW.md
layer: auxiliary
doc_type: pmo_metacognik_completeness_review
phase: 000_ROADMAPS
category: consolidation
status: released
version: 0.1.0
created_at: 2026-06-12
owner: pmo_ckos
reviewer: claude_fresh_session (Claude Fable 5)
session_id: S-F1S4-CHARTER-METAREV-CLAUDE-20260611-001
review_of: F1_SPRINT4_CHARTER.md v0.2.0 (commit ed0be72)
author_session: S-F1S4-CHARTER-CLAUDE-20260611-001  # claude_opus_4_7 — separação de papéis preservada (autor ≠ reviewer)
two_key_context: >
  Esta NÃO é uma 2ª chave de canonical_patch. O F1 Sprint 4 Charter é planning artifact (não modifica
  canônico 01-28). Esta sessão = completeness/coherence audit. Veredito orienta se o charter está
  pronto para virar dispatch de implementação (S-F1S4-IMPLEMENTATION-DISPATCH.md, sessão separada).
target_dispatch_session: S-F1S4-IMPLEMENTATION-DISPATCH-<DATE>-001  # sessão futura (PMO — SEPARADA desta e da autora)
tags: [metacognik, completeness-audit, review, f1, sprint-4, event-log, hardening, charter, planning, post-sprint-1-done, released]
---

# F1 Sprint 4 Charter — Metacognik Completeness Review

> **Veredito:** **APROVA-COM-AJUSTES** (espinha do charter sólida; 5 AJUSTES obrigatórios antes do dispatch — 2 deles corrigem checks do exit criterion que falhariam *por design* como escritos)
> **Data:** 2026-06-12 (dispatch emitido 2026-06-11)
> **Sessão:** S-F1S4-CHARTER-METAREV-CLAUDE-20260611-001 (Claude Code fresh, separado do autor `claude_opus_4_7` da sessão `S-F1S4-CHARTER-CLAUDE-20260611-001`)
> **Executor:** Claude Code fresh (per [[feedback-metacognik-executor]] — audit em Claude; Windsurf reservado para APPLY mecânico)
> **Natureza:** completeness audit de planning artifact. NÃO é 2ª chave de canonical_patch. NÃO autoriza implementação. Read-only — nada foi editado no charter nem no canônico.

---

## 1. Veredito

**APROVA-COM-AJUSTES** — O charter está estruturalmente sólido:

- Precondições §1 conferem: S1 done (commit `4ed637d`), runtime live (https://ckos-runtime.fly.dev, healthcheck 8ms, 8 eventos reais `b75238fd-...`), 13/13 gates, Doc 11 §7 implementado com 0 findings — tudo verificado contra dispatch S1 §17 `production_deploy`.
- Ordem dos sprints correta: backend plan §14 ("S1 ingress → S4 event log hardening → S2/S3 → S5 → S6"; "Event Log deve ser estabilizado cedo") + kanban F1 ("S4 — Event Log (sem ele, vira chat bonito) #blocker"). S4 agora é o passo certo.
- Escopo cirúrgico: 9 deliverables IN, ~11 OUT com motivo, 6 PROIBIDO; zero novas deps (stack S1 production-validated reusado); zero custo LLM.
- Founder decisions §9 (AQ-S4-01/02/03) registradas com implicações; AQs médias com dono claro.
- Plano de dispatch §7 em 7 etapas espelha o pattern S1 validado (slices a-i cobrem os 9 deliverables; verificação com executor self-test + PMO valida + Founder assina).

**MAS 5 AJUSTES obrigatórios** precisam ser aplicados (Forma A, charter v0.2.0→v0.3.0) antes do dispatch. Diferente do audit S1 (onde os ajustes eram lacunas de escopo), aqui **2 ajustes corrigem mecânica quebrada**:

1. **Exit check 4 (telemetria) falha por design como escrito** — um trigger que `RAISE EXCEPTION` aborta a transação e **desfaz o próprio increment do counter**; o counter ficaria 0 para sempre (AJUSTE-01).
2. **Exit check 2 (replay causal) é incompatível com os 8 eventos reais de S1** — 4 dos 8 são LLMCost side-chain; a verificação linear `event[i].causation_id === event[i-1].id` nunca se aplica ao trace real (AJUSTE-04).
3. **Postgres proíbe a unique constraint global do Doc 11 §7 em tabela particionada** — PK(id) e `idempotency_key unique` precisam incluir as partition keys; a garantia anti-duplicidade por índice **deixa de ser global** e o charter não trata (AJUSTE-02).
4. **Deliverable #9 referencia recurso inexistente** — "branch separada do Supabase" é feature paga (Pro+); o free tier do projeto não tem branching (AJUSTE-03).
5. Contagem do exit criterion inconsistente ("3 checks" no §5, "5 checks" no quality gate, 6 itens listados) + anchor "Doc 11 §7 línea 235" errado em ~8 ocorrências (o hint de partição está nas linhas 214-217; a 235 é sobre streams/views) (AJUSTE-05).

**Sem AJUSTES 01-05, REPROVA** como base para dispatch direto (o executor herdaria 2 checks impossíveis e 1 passo de safety net inexecutável).
**Com AJUSTES 01-05 aplicados, APROVA** — GO para o PMO escrever `S-F1S4-IMPLEMENTATION-DISPATCH.md` (com 7 defers não-bloqueantes fixados lá).

---

## 2. Tabela de findings por checagem (1–8)

| # | Checagem | Resultado | Detalhe |
|---|---|---|---|
| 1 | **ESCOPO IN — 9 deliverables suficientes/corretos pro exit criterion?** | ⚠️ **PASS-COM-AJUSTES (01, 02, 03)** | Os 9 deliverables cobrem idempotência + replay + partição + telemetria + baseline + docs — suficientes em extensão. **3 defeitos de mecânica:** (a) **#5 telemetria**: o trigger S1 `events_no_update_delete` bloqueia via exceção; exceção aborta a transação → o increment do counter Postgres na mesma transação é **rolled back** → `events_append_attempts_blocked_total` nunca sai de 0 e o exit check 4 falha por design. Mecanismo correto: trigger BEFORE ROW com `RETURN NULL` (skip silencioso preserva o invariante) + `RAISE WARNING` + increment persistente (AJUSTE-01); (b) **#4 partição**: PK e unique constraints em tabela particionada DEVEM incluir as partition keys (`aggregate_type`, `created_at`) — `unique(idempotency_key)` global do Doc 11 §7 linha 232 é impossível; retry com mesmo hash mas `created_at` diferente **não é mais bloqueado por índice**. Charter silente (AJUSTE-02); (c) **#9 safety net**: Supabase branching é Pro+ — não existe no free tier do projeto; recriação dos triggers na tabela nova é assumption, precisa ser deliverable (AJUSTE-03). **Coerência de endpoint**: S1 expõe `GET /trace/:correlation_id` (dispatch §17); o charter §3.2 trata `GET /events/replay?ordering=temporal` como "comportamento atual de S1" — `/events/replay` é rota NOVA em S4 (`/trace` permanece intocada e precisa de regression test). Esclarecido no AJUSTE-04. |
| 2 | **ESCOPO OUT — algum defer é precondição? over-scope?** | ✅ **PASS** | Nenhum defer é precondição técnica de S4. **Outbox defer S5 está correto**: Doc 10 §5.3 põe outbox no Event Bus (PROPAGAÇÃO); S4 é PERSISTÊNCIA. Particionar sem outbox não cria retrabalho — outbox em S5 é tabela própria (ou consumo via pg-boss já existente); a partição de `events` não interfere no design do outbox. Demais defers (novos event types S3/S5, memória S6, CQRS S5/F4, RLS forçada S3, compaction F6/F7, OTEL S6) batem com backend plan §14 + precedente charter S1 §2.2. **Over-scope avaliado**: particionar com 8 eventos parece YAGNI, mas (i) é hint canônico Doc 11 §7, (ii) kanban marca S4 #blocker, (iii) migrar agora com 8 eventos é o momento de menor risco da história do sistema. Justificado. |
| 3 | **COERÊNCIA com canônico — anchors batem?** | ⚠️ **PASS-COM-AJUSTE (05) + 1 finding canônico** | **Doc 11 §7**: a substância citada existe — "particionada por `aggregate_type` (+ tempo)" (linha 214) e "[partição por aggregate_type, range por created_at]" (linha 217) — **mas o anchor "línea 235" está errado**: a linha 235 lista os streams lógicos (views), não o partition hint. ~8 ocorrências no charter (frontmatter, §2.1 #4, §5, §6, §8, §9) apontam pra linha errada (AJUSTE-05). **Doc 10 §5.26 + §5.3**: replay causal via `causation_id` chain é coerente — §5.3 fala em "reconstruir a **árvore** causal" (DAG, não cadeia linear), o que REFORÇA o AJUSTE-04 (invariante topológica, não linear). **Doc 10 §5.6**: idempotency canônica é de RUN (`hash(correlation_id + step + input_digest)`, "consulta event log antes de aplicar"); a extensão pro ingress com key client-provided é compatível e bem framed ("S1 já tem idempotency_key no envelope; S4 estende pra ingress") — e a cláusula "consulta antes de aplicar" é exatamente a mitigação app-side do AJUSTE-02. **`ingress_idempotency` (extensão não-canônica §3.1)**: NÃO viola o PROIBIDO §2.3 — o próprio §2.3 a excetua com justificativa (infra operacional, padrão cache table); precedente S1: pg-boss criou schema `pgboss.*` sem patch canônico; tem `workspace_id` (app-side scoping igual S1). Aceita. **Finding canônico novo**: Doc 11 §7 linha 232 (`idx: idempotency_key unique`) e linhas 214/217 (partição) são **mutuamente incompatíveis como escritos** em Postgres — finding para PATCH 3 via AQ-S4-04 (pattern AQ-S1-06), além do já esperado no quality gate. |
| 4 | **REALISMO DO EXIT CRITERION — binário, testável, factível?** | ⚠️ **PASS-COM-AJUSTES (01, 04, 05)** | **Inconsistência de contagem**: §5 anuncia "3 checks objetivos", lista 6 itens, quality gate diz "5 checks acima" e o executor self-test (§7 step 6) "roda 5 checks" — qual dos 6 se pula? (AJUSTE-05). **Checks 1, 5, 6 binários e testáveis** ✅. **Check 2 quebrado como escrito**: a verificação linear nunca se aplica ao trace real de S1 (4 LLMCost side-chain) — vira teste vácuo ou falso-negativo (AJUSTE-04). **Check 3 factível**: Fly GRU ↔ Supabase `aws-1-sa-east-1` é intra-região (RTT baixo); INSERT single-row com índices fica em ~5-15ms; P95 <100ms e ≥50 ev/s sustentados são conservadores e realistas no shared-cpu-1x — DESDE QUE o bench não abra 100 conexões reais: postgres.js default `max=10` + pg-boss pool próprio (~10) → ~20 conns de app; 100 workers devem ser concorrência in-process enfileirando sobre o pool, não 100 conexões (senão esgota o Session Pooler ~60 conns — def-03 fixa no dispatch). **Check 4 falha por design** (rollback do increment — AJUSTE-01). **Check 5 verificação objetiva** ✅ — fortalecido pelo AJUSTE-03(d) com regression de `GET /trace` e comparação byte-idêntica. **Custo LLM do exit criterion: $0** (S4 não chama LLM) ✅. **Efeito colateral não tratado**: bench de 1000+ eventos contra produção fica **pra sempre** no event log (append-only, trigger bloqueia DELETE) — usar `workspace_id` dedicado de bench (def-04). |
| 5 | **PARTITION MIGRATION RISK — plano seguro?** | ⚠️ **PASS-COM-AJUSTES (02, 03)** | Plano (criar `events_partitioned` → copiar → swap rename + view backward-compat) é a estratégia certa para 8 eventos. Gaps por sub-pergunta: **(a) pg-boss durante swap**: o queue vive em schema próprio (`pgboss.*`) — não trava com o rename; mas handlers ESCREVEM em `events` → rodar a migration com **app parado** (`fly machine stop`) elimina writes concorrentes; com 1 usuário e auto_stop já ativo, janela de minutos é trivial (AJUSTE-03; confirma B8). **(b) Drizzle**: agnóstico pra DML (INSERT/SELECT na parent funcionam); drizzle-kit NÃO gera DDL de partição — migration é SQL custom; `schema.ts` segue mapeando `events` (view/parent). Detalhe pro dispatch. **(c) View backward-compat + triggers**: view simples é auto-updatable (INSERT/UPDATE/DELETE propagam à base e disparam os triggers da base) — MAS os triggers **não migram na cópia**: recriar `events_no_update_delete` na nova parent (PG15 clona BEFORE ROW triggers da parent pras partições) é deliverable explícito (AJUSTE-03). **(d) Janela**: zero-downtime é over-engineering pra S4 — janela aceita (B8). **(e) FKs**: verificado — nenhuma tabela S1 implementada tem FK → `events` (`context_packs` Doc 11 §13 linha 439 não referencia events); o rename não quebra nada HOJE. **Forward-compat**: Doc 11 tem ~25 `fk→events` em tabelas S3/S5+ (ex.: `run_state_transitions` linha 248) que serão impossíveis como FK simples pós-partição → registrar em F1S4_DOC11_PATCH_FINDINGS (def-05). **LIST sem DEFAULT partition**: INSERT de `aggregate_type` novo (S3/S5) quebraria em produção — DEFAULT partition obrigatória (AJUSTE-02). |
| 6 | **AQ COVERAGE — as 6 AQs cobrem o que falta?** | ⚠️ **PASS-COM-GAPS (5 nomeados → 1 AJUSTE + 4 defers)** | Gaps do dispatch confirmados: **(a) auth do `/metrics`**: público vaza contagens operacionais; Doc 12 é deny-by-default (§5.6 isolamento estrutural; §5.7 deny-by-default) — recomendo **mock JWT, mesmo middleware do `/intent`** (custo ~zero, consistente com S1; IP allowlist é frágil atrás do proxy Fly) → def-01 no dispatch; **(b) persistência do counter**: o charter JÁ diz "counter Postgres" (decisão correta — in-memory reseta no `auto_stop_machines` do Fly) mas o mecanismo precisa do AJUSTE-01 pra não ser desfeito por rollback; **(c) `request_hash`**: o `...` do §3.1 é gap real — fórmula fechada recomendada em B5 (def-02 no dispatch); **(d) replay causal com `causation_id` NULL/side-chains**: é defeito do exit check 2, não detail — AJUSTE-04; **(e) bench produção vs DB separado**: custo LLM $0, mas eventos de bench são **permanentes** no event log de produção — workspace dedicado + decisão explícita no dispatch (def-04). **AQs médias com dono claro** ✅: AQ-S4-04 (b) executor→PATCH 3 candidate; AQ-S4-05 Prometheus (decidido); AQ-S4-06 pg-boss (executor confirma). |
| 7 | **FOUNDER DECISIONS §9 — registradas com implicações?** | ✅ **PASS (1 imprecisão leve)** | AQ-S4-01 = LIST+RANGE com rationale (drop isolado de LLMCost antigos); AQ-S4-02 = 24h com cleanup horário; AQ-S4-03 = P50<30/P95<100/P99<250ms + ≥50 ev/s + 100 workers, com stretch targets informativos — todas com implicações e coerentes com o ambiente (free tier + shared-cpu-1x). **Imprecisão leve**: "5 partições iniciais (uma por aggregate_type ativo)" — S1 só usa `workflow` (default `aggregate_type='workflow'` per charter S1 §3 AJUSTE-03) e eventos LLMCost; a lista exata das partições iniciais + DEFAULT partition ficam pro dispatch (def-07; DEFAULT já exigida no AJUSTE-02). §9 também herda o anchor "línea 235" errado (AJUSTE-05) e a afirmação "Migration testada em branch Supabase" (AJUSTE-03). |
| 8 | **PLANO DE DISPATCH §7 — realista? slices cobrem?** | ✅ **PASS (1 cosmético no AJUSTE-05)** | 7 passos espelham o pattern S1 validado. Slices a-i ↔ deliverables: a→#4+#9, b→#1+#2, c→#7, d→#3, e→#5, f→#6, g→#8, h→#9, i→CI — **9/9 cobertos** ✅. Step 6 nomeia executor self-test + PMO valida (stress test ao vivo) + Founder assina (`sprint-done: S4`) — coerente com S1 §17/quality gate ✅. Branch base `main` @ `1171384` confere com dispatch S1 §17 ✅. **Cosmético**: step 3 diz "patch leve no charter v0.1.0→v0.2.0" — o charter JÁ é v0.2.0 (bump das Founder decisions); AJUSTES = v0.2.0→v0.3.0 (AJUSTE-05). Step 7 (S2 ∥ S3 após S4) coerente com backend plan §14. |

---

## 3. Respostas às 8 perguntas do PMO (seção B do dispatch)

**B1 — Backward-compat do `/trace`:** Sim, o check 5 DEVE cobrir o endpoint HTTP, não só o `SELECT`. A view backward-compat preserva colunas/tipos, então o handler de `GET /trace/:correlation_id` (S1) deve retornar os mesmos 8 eventos byte-idênticos — mas "deve" não é verificação: o swap muda relkind/OID da relação e qualquer dependência sutil (prepared statements, RETURNING, introspecção do Drizzle) só é provada por teste. **AJUSTE-03(d)** adiciona `GET /trace` regression ao check 5. Nota de coerência: `/events/replay` é rota NOVA de S4 (S1 só tem `/trace`); `ordering=temporal` replica a semântica do `/trace`, que permanece intocado.

**B2 — Triggers na particionada:** Em PG15, `CREATE TRIGGER ... BEFORE UPDATE/DELETE FOR EACH ROW` na **parent particionada funciona** e é clonado automaticamente para todas as partições (inclusive criadas depois) — não precisa criar partição por partição. O risco real é outro: **o trigger não migra junto na estratégia copy+swap** — `events_partitioned` nasce sem trigger; é preciso recriá-lo (e re-rodar o teste append-only pós-migration). Hoje o charter trata como assumption ("já implementado em S1", §1) — **AJUSTE-03(a)** promove a deliverable explícito. Atenção acoplada: a recriação deve já usar o mecanismo do AJUSTE-01 (`RETURN NULL` + counter), senão o check 4 falha.

**B3 — Esgotamento do pooler no stress test:** postgres.js tem default `max = 10` conexões; pg-boss mantém pool próprio (~10). Total do app ~20 conns — folga confortável nos ~60 do Session Pooler. O perigo é o bench abrir 100 **conexões** em vez de 100 **workers lógicos**. Recomendação pro dispatch (def-03): (i) fixar `max: 20` explícito no client do runtime (não confiar no default); (ii) `bench:events` implementa os 100 workers como concorrência in-process (Promise pool) sobre o pool de conexões — workers **enfileiram**, não estouram; (iii) documentar os 2 pools (app + pg-boss) em `docs/EVENT_LOG.md`. Com isso o stress test não derruba o app nem esgota o pooler.

**B4 — Counter de telemetria, persistência:** Postgres table (ex.: `ops_counters(name text pk, value bigint)`) — o charter já aponta certo ("counter Postgres"); in-memory é inviável com `auto_stop_machines` (reseta a cada idle). O write por increment é aceitável: bloqueios de UPDATE/DELETE devem ser raros fora de stress test. **MAS é AJUSTE, não decisão de dispatch**, porque o mecanismo como descrito não funciona: se o trigger lança exceção, a transação abortada **desfaz o increment** — counter eternamente 0, exit check 4 impossível. Solução (AJUSTE-01): trigger `RETURN NULL` (skip da row, invariante preservado) + `RAISE WARNING` (visibilidade em log) + increment que sobrevive porque a transação NÃO aborta. Trade-off explícito: UPDATE/DELETE passam a "succeed" com 0 rows affected em vez de erro — testes S1 que esperem exceção são atualizados (regression note no AJUSTE-01).

**B5 — `request_hash` spec:** fórmula fechada recomendada (def-02, fixar no dispatch):
`request_hash = sha256(canonical_json({ intent_text, user_id, workspace_id, project_id: project_id ?? null }))`
— JSON canônico (keys ordenadas, sem whitespace), `project_id` SEMPRE presente com `null` explícito quando ausente. Consequência: requests iguais com/sem `project_id` geram hashes **diferentes — correto**, porque são intents semanticamente distintas (com project scope ≠ sem). Colisões sha256: desprezíveis. Campos voláteis (timestamps, headers) ficam FORA do hash.

**B6 — Replay causal, side-chains:** semântica recomendada (AJUSTE-04): ordem **topológica do DAG** — roots (`causation_id IS NULL`) primeiro por `created_at` ASC; cada evento aparece DEPOIS do seu causador; desempate por `created_at` ASC. **LLMCost são INCLUÍDOS como filhos do evento que os causou** (nem excluídos, nem flag separada) — replay de auditoria de custo precisa deles (Doc 10 §5.26 lista "custo" e "modelos usados" no replay). Ressalva factual: o valor real de `causation_id` dos 4 LLMCost de S1 (NULL? aponta pro IntentSubmitted/IntentResolved?) não é verificável deste repo — o executor reporta o estado real no anexo do dispatch antes de fechar o teste do check 2. Por isso o check 2 reescrito valida a **invariante topológica genérica**, robusta a qualquer forma do DAG real.

**B7 — `/metrics` auth:** **mock JWT — o mesmo middleware do `/intent`** (def-01, fixar no dispatch). Razões: custo ~zero (middleware já existe em S1); consistente com a postura deny-by-default do Doc 12; PMO valida com `curl -H "Authorization: Bearer ..."` sem fricção; IP allowlist é frágil atrás do proxy Fly (IPs de edge variam) e "público com risco aceito" é desnecessário quando a proteção custa 3 linhas. Contagens operacionais (volume de eventos, tentativas bloqueadas) são exatamente o tipo de metadado que o Doc 12 §5.6 trata como estrutural, não cosmético.

**B8 — Zero-downtime vs janela:** **zero-downtime NÃO é requisito de S4 — confirmo que seria over-engineering.** Argumento positivo pela janela: rodar a migration com app **parado** (`fly machine stop`) é a opção *mais segura*, não um compromisso — elimina writes concorrentes durante copy+swap, e o sistema tem 1 usuário (Founder) + `auto_stop_machines` já ativo (a machine passa a maior parte do tempo parada de qualquer forma). Janela de minutos, anunciada no PR da migration. O charter §2.1 #4 não explicita a janela — **AJUSTE-03(c)** fecha isso. Zero-downtime entra no radar quando houver tráfego real (F4+).

---

## 4. Go/no-go por componente do charter

| Componente | Go/no-go | Bloqueio |
|---|---|---|
| §0 Veredito 1-linha | ✅ **GO** | nenhum (herda anchor errado — AJUSTE-05 cosmético) |
| §1 Precondições (7 verificadas) | ✅ **GO** | nenhum — todas conferidas contra dispatch S1 §17 + kanban + commits |
| §2.1 Escopo IN (9 deliverables) | ⚠️ **GO-COM-AJUSTES** | AJUSTE-01 (#5 telemetria), AJUSTE-02 (#4 constraints), AJUSTE-03 (#9 safety net) |
| §2.2 Escopo OUT (~11 defers) | ✅ **GO** | nenhum — outbox defer S5 verificado correto |
| §2.3 PROIBIDO | ✅ **GO** | nenhum — exceção `ingress_idempotency` bem justificada |
| §3 Contratos + §3.1 idempotency table | ⚠️ **GO-COM-DEFER** | def-02 (`request_hash` fórmula no dispatch); tabela em si aceita |
| §3.2 Replay extensão | ⚠️ **GO-COM-AJUSTE** | AJUSTE-04 (semântica side-chains + `/trace` vs `/events/replay`) |
| §4 Tech stack (zero novas deps) | ✅ **GO** | nenhum (def-03 fixa config de pool no dispatch) |
| §5 Exit criterion (6 checks) | ⚠️ **GO-COM-AJUSTES** | AJUSTE-01 (check 4), AJUSTE-04 (check 2), AJUSTE-03d (check 5), AJUSTE-05 (contagem) |
| §6 AQs (3+3) | ✅ **GO** | nenhum — gaps achados viram AJUSTES/defers, não AQs novas trava-início |
| §7 Plano de dispatch (7 steps, slices a-i) | ✅ **GO** | nenhum (versões staled — AJUSTE-05 cosmético) |
| §8 BRA + CHECKOUT | ✅ **GO** | nenhum |
| §9 Founder Decision Log | ✅ **GO** | nenhum (herda "branch Supabase" — corrigida via AJUSTE-03; def-07 lista de partições) |

**Sem AJUSTES 01-05 aplicados: REPROVA** como base para dispatch direto.
**Com AJUSTES 01-05 aplicados (Forma A, v0.2.0→v0.3.0): APROVA** — defers def-01..def-07 são cláusulas do dispatch, não bloqueiam.

---

## 5. AJUSTES OBRIGATÓRIOS (diff-ready, Forma A)

Todos no arquivo `000_ROADMAPS/22_CONSOLIDATION/F1_SPRINT4_CHARTER.md` (v0.2.0 → v0.3.0). Linhas referem-se ao estado do commit `ed0be72`.

### AJUSTE-01 — Telemetria append-only à prova de rollback (deliverable #5 + exit check 4)

**Por quê:** trigger que `RAISE EXCEPTION` aborta a transação inteira — incluindo o increment do counter feito na mesma transação. O counter ficaria 0 para sempre e o exit check 4 nunca passaria. É o tipo de defeito que o executor só descobriria no meio do sprint.

**§2.1 linha 79 — substituir a row do deliverable #5:**

DE:
```
| 5 | **Telemetria append-only** — counter Postgres `events_append_attempts_blocked_total{op}` exposto via endpoint `GET /metrics` (Prometheus text format); incrementa toda vez que trigger bloqueia UPDATE/DELETE | Doc 13 §16 quality gates — preparação |
```

PARA:
```
| 5 | **Telemetria append-only** — counter Postgres persistente (tabela `ops_counters(name text pk, value bigint)`) `events_append_attempts_blocked_total{op}` exposto via `GET /metrics` (Prometheus text format). **Mecanismo obrigatório:** o trigger append-only é reescrito para `RETURN NULL` (skip silencioso da row — invariante preservado) + `RAISE WARNING` + increment do counter. NÃO usar `RAISE EXCEPTION`: exceção aborta a transação e desfaz o próprio increment (counter eternamente 0). Regression: testes S1 que esperem exceção em UPDATE/DELETE passam a esperar 0 rows affected + dados intactos | Doc 13 §16 quality gates — preparação |
```

**§5 linha 181 — substituir o check 4:**

DE:
```
4. **Append-only telemetria:** stress test que tenta `UPDATE events SET ... ; DELETE FROM events WHERE ...` 100 vezes → `GET /metrics` mostra `events_append_attempts_blocked_total{op="UPDATE"} = 100, op="DELETE" = 100`
```

PARA:
```
4. **Append-only telemetria:** stress test que tenta `UPDATE events SET ... ; DELETE FROM events WHERE ...` 100 vezes (autocommit) → 0 rows alteradas/deletadas (dump byte-idêntico antes/depois) E `GET /metrics` mostra `events_append_attempts_blocked_total{op="UPDATE"} = 100, op="DELETE" = 100`; counter sobrevive a restart da Fly machine (tabela Postgres, não memória de processo)
```

### AJUSTE-02 — Unique constraints × partição + DEFAULT partition (§3, nova nota após linha 120)

**Por quê:** Postgres exige que PRIMARY KEY e UNIQUE constraints de tabela particionada incluam **todas** as colunas da partition key. O `[idx: idempotency_key unique]` do Doc 11 §7 linha 232 — implementado globalmente em S1 na tabela flat — é impossível na particionada. A garantia anti-duplicidade ("idempotency_key único impede duplicidade", Doc 11 §7) deixa de ser estrutural e o charter precisa registrar a mitigação, senão o executor descobre no `CREATE TABLE` e improvisa.

**§3 — inserir nota após a linha 120 (após o bullet "Run Replay → Doc 10 §5.26 ..."):**

INSERIR:
```
> **Constraint × partição (restrição Postgres que o S4 DEVE tratar):** PK e UNIQUE em tabela particionada
> precisam incluir as partition keys. Em `events_partitioned` LIST(aggregate_type)+RANGE(created_at):
> PK vira `(id, aggregate_type, created_at)` e o índice único do Doc 11 §7 linha 232 vira
> `(idempotency_key, aggregate_type, created_at)` — a unicidade GLOBAL de `idempotency_key` deixa de ser
> garantida por índice (retry com mesmo hash mas `created_at` distinto NÃO é bloqueado). Mitigação S4:
> (i) guarda app-side no event publisher — "consulta event log antes de aplicar" já é canônica em
> Doc 10 §5.6; (ii) `ingress_idempotency` cobre o caminho de ingress. Este conflito (Doc 11 §7 linha 232
> unique × linhas 214-217 partição) é finding canônico → F1S4_DOC11_PATCH_FINDINGS → PATCH 3 candidate
> (caminho AQ-S4-04, pattern AQ-S1-06).
>
> **DEFAULT partition obrigatória:** a partição LIST DEVE incluir `DEFAULT` — sem ela, INSERT de qualquer
> `aggregate_type` novo (S3/S5 introduzem event types novos) quebra em produção.
```

### AJUSTE-03 — Migration safety net real: sem branch Supabase, triggers recriados, app parado, `/trace` regression (deliverable #9, §9, check 5)

**Por quê:** (a) Supabase branching é feature paga (Pro+) — o free tier do projeto NÃO tem branches; como escrito, o deliverable #9 é inexecutável; (b) triggers não migram na estratégia copy+swap; (c) a janela de migração não está explicitada (B8); (d) o check 5 só cobre SELECT, não o endpoint HTTP validado em produção (B1).

**§2.1 linha 83 — substituir a row do deliverable #9:**

DE:
```
| 9 | **Migration safety net** — testar migration de partição em branch separada do Supabase (`pnpm db:migrate:dry-run` simula EXPLAIN), documentar rollback no `docs/MIGRATIONS.md` | Doc 11 §7 + Doc 12 §5.X (data governance) |
```

PARA:
```
| 9 | **Migration safety net** — Supabase free tier NÃO tem branching (feature Pro+): a migration completa (create partitioned → copy → recriar triggers/índices → swap rename + view) é ensaiada em Postgres 15 local (mesmo ambiente de testes do S1) e/ou em 2º projeto Supabase free descartável; `pnpm db:migrate:dry-run` = transação `BEGIN … ROLLBACK` em ambiente de ensaio (EXPLAIN não simula DDL); **recriar o trigger append-only (mecanismo AJUSTE-01) + índices na nova parent particionada é parte do deliverable** (não migram na cópia; PG15 clona triggers da parent pras partições); em produção a migration roda com **app parado** (`fly machine stop` — janela de minutos aceita: 1 usuário, auto_stop já ativo; zero-downtime é over-engineering em S4); rollback documentado em `docs/MIGRATIONS.md` | Doc 11 §7 + Doc 12 §5.X (data governance) |
```

**§5 linha 182 — estender o check 5:**

DE:
```
5. **Partition migration:** migration aplicada em produção (Supabase) com S1 events copiados pra partições corretas; query `SELECT * FROM events WHERE workspace_id = ?` retorna mesmos 8 eventos validados em S1 (correlation_id `b75238fd-0a41-4d1e-8c3f-300fb342723f`) — zero perda
```

PARA:
```
5. **Partition migration:** migration aplicada em produção (Supabase) com S1 events copiados pra partições corretas; query `SELECT * FROM events WHERE workspace_id = ?` E endpoint S1 `GET /trace/:correlation_id` (HTTP, auth S1) retornam os mesmos 8 eventos validados em S1 (correlation_id `b75238fd-0a41-4d1e-8c3f-300fb342723f`), payload byte-idêntico (comparar dump ordenado por `id` antes/depois do swap) — zero perda, zero mutação
```

**§9 linha 350 — corrigir a implicação registrada da AQ-S4-01:**

DE:
```
- Migration testada em branch Supabase antes de produção (deliverable #9 safety net)
```

PARA:
```
- Migration ensaiada em Postgres 15 local e/ou 2º projeto Supabase free antes de produção (deliverable #9 safety net — free tier não tem branching)
```

### AJUSTE-04 — Replay causal: semântica de side-chains + invariante topológica (§3.2 + exit check 2)

**Por quê:** os 8 eventos reais de S1 incluem 4 LLMCost fora da cadeia linear do workflow. A verificação do check 2 (`event[i].causation_id === event[i-1].id`) nunca se aplica ao trace real — o teste seria vácuo ou falso-negativo. Doc 10 §5.3 fala em **árvore** causal; o critério binário correto é topológico.

**§3.2 — inserir após a linha 151 (após "... CTE recursivo handles ciclos defensivamente (LIMIT 100 hops)."):**

INSERIR:
```
Semântica causal (fechada): roots = eventos com `causation_id IS NULL`, ordenados por `created_at` ASC;
cada evento aparece DEPOIS do seu causador (ordem topológica do DAG — Doc 10 §5.3 "árvore causal");
desempate por `created_at` ASC. Side-chains (ex.: os 4 LLMCost de S1) são INCLUÍDOS como filhos do
evento que os causou — não excluídos, não flag separada (replay de auditoria precisa de custo e modelos,
Doc 10 §5.26). O valor real de `causation_id` dos LLMCost em S1 (NULL? aponta pro causador?) é dado a
CONFIRMAR pelo executor no anexo do dispatch — não assumir.

Nota de rota: `GET /events/replay/:correlation_id` é rota NOVA de S4 (S1 expõe apenas `GET /trace/:correlation_id`,
que permanece intocada — regression no check 5). `ordering=temporal` replica a semântica do `/trace` de S1.
```

**§5 linha 179 — substituir o check 2:**

DE:
```
2. **Replay causal:** dado um `correlation_id` com 8 eventos S1, `GET /events/replay/:correlation_id?ordering=causal` retorna lista em ordem topológica `causation_id` chain (verifica que `event[i].causation_id === event[i-1].id` para `i > 0` quando há cadeia linear)
```

PARA:
```
2. **Replay causal:** dado um `correlation_id` com 8 eventos S1, `GET /events/replay/:correlation_id?ordering=causal` retorna TODOS os eventos do correlation_id em ordem topológica: roots (`causation_id` NULL) primeiro; para todo evento cujo causador está na lista, o causador aparece ANTES dele; desempate `created_at` ASC. (A checagem linear `event[i].causation_id === event[i-1].id` vale apenas pra sub-cadeia workflow de 4 eventos; os 4 LLMCost são side-chain — a invariante topológica é o critério binário.)
```

### AJUSTE-05 — Consistência de contagem do exit criterion + anchors + versões (cosmético-estrutural)

**Por quê:** o exit criterion é o coração do charter e sua contagem está tripla ("3 checks" §5 linha 176, 6 itens listados, "5 checks" quality gate linha 186 e §7 step 6) — o executor self-test não sabe o que rodar. O anchor "línea 235" aponta pra linha errada do Doc 11 em ~8 ocorrências.

- **Linha 176**: "testável por 3 checks objetivos:" → "testável por **6 checks objetivos**:"
- **Linha 186** (quality gate): "5 checks acima ✅" → "**6 checks** acima ✅"
- **§7 step 6** ("roda 5 checks do §5") → "roda os **6 checks** do §5"
- **Anchor**: "Doc 11 §7 **línea 235**" → "Doc 11 §7 **linhas 214-217**" em TODAS as ocorrências (frontmatter `derives_from` linha 23; §2.1 #4 linha 78; §5 quality gate linha 189; §6 AQ-S4-01 linhas 203/207; AQ-S4-04 linha 240; §8 linha 317; §9 linha 347). O hint de partição ("uma tabela `events` append-only particionada por `aggregate_type` (+ tempo)" / "[partição por aggregate_type, range por created_at]") está nas linhas 214 e 217; a linha 235 lista os streams lógicos (views) — conteúdo distinto.
- **Linha 269** (§7 step 3): "patch leve no charter v0.1.0→v0.2.0" → "patch leve no charter **v0.2.0→v0.3.0**" (v0.2.0 já é o estado atual pós-Founder decisions).

---

## 6. Gaps não-bloqueantes (defer pro dispatch ou pra durante S4)

| ID | Item | Onde resolver | Recomendação |
|---|---|---|---|
| def-01 | Auth do `GET /metrics` (B7) | dispatch (cláusula) | **Mock JWT — mesmo middleware do `/intent`**; custo ~zero, deny-by-default Doc 12, PMO valida via curl com header |
| def-02 | `request_hash` fórmula fechada (B5) | dispatch (contrato do middleware) | `sha256(canonical_json({intent_text, user_id, workspace_id, project_id: project_id ?? null}))` — JSON canônico, `project_id` null explícito; com/sem project_id → hashes diferentes (correto) |
| def-03 | Pool de conexões no stress test (B3) | dispatch (config explícita) | `max: 20` no postgres.js client (default 10 — fixar explícito); 100 workers do bench = concorrência in-process enfileirando no pool, NÃO 100 conexões; documentar pool app + pool pg-boss em `docs/EVENT_LOG.md` |
| def-04 | Eventos de bench permanentes em produção | dispatch (decisão registrada) | append-only + trigger sem DELETE = os ~1.2k eventos do stress test ficam pra sempre no event log de produção; usar `workspace_id` dedicado de bench + documentar; alternativa: bench pleno em ambiente local + smoke reduzido em produção (PMO decide) |
| def-05 | Forward-compat: ~25 `fk→events` do Doc 11 (S3/S5+) impossíveis como FK simples pós-partição | F1S4_DOC11_PATCH_FINDINGS → PATCH 3 | FK composto `(event_id, aggregate_type, created_at)` OU integridade app-side (padrão comum em event sourcing); decidir no PATCH 3, não bloqueia S4 |
| def-06 | Anchor Doc 13 §16 da telemetria é framing fraco (gates do §16 são de output/artifact, não infra) | aceitar como "preparação" | refinar quando S6 abrir observability completa; não vale AJUSTE |
| def-07 | Lista exata das partições LIST iniciais ("5 partições" §9 — S1 só usa `workflow` + eventos de custo) | dispatch (SQL da migration) | enumerar `aggregate_type` realmente ativos no DB de produção + DEFAULT partition (AJUSTE-02); não criar 12 partições vazias do enum completo |

---

## 7. Confirmação de separação de sessões (Constituição multi-sessão)

| Sessão | Agent | Papel | Estado |
|---|---|---|---|
| `S-F1S4-CHARTER-CLAUDE-20260611-001` | `claude_opus_4_7` | **Autora** do charter v0.2.0 | released (commit `ed0be72`) |
| `S-F1S4-CHARTER-METAREV-CLAUDE-20260611-001` | `metacognik (fresh / Claude Code — Claude Fable 5)` | **Esta sessão** — completeness audit | releasing agora |
| `S-F1S4-IMPLEMENTATION-DISPATCH-<DATE>-001` | a definir (PMO) | **Próxima sessão** — escreve dispatch | a abrir após este release + AJUSTES |
| `S-F1S4-IMPL-EXEC-<DATE>-001` | Codex OU Claude Code fresh (per AQ-S1-03 inalterada) | **Implementação** em `CKOS_RUNTIME` (branch base `main` @ `1171384`) | etapa posterior |

**Garantias:**
- Esta sessão NÃO é a autora do charter (instância fresh, sem memória da sessão autora) ✅
- A próxima sessão (PMO dispatch) é SEPARADA desta e da autora — terceira instância ✅
- Esta sessão NÃO editou canônico 01-28, NÃO editou o charter, NÃO editou o dispatch task file (placeholders C/D preservados, mesmo pattern do precedente S1), NÃO tocou `CKOS_RUNTIME`, NÃO escreveu SQL/UI/backend ✅
- Esta sessão NÃO decidiu AQ-S4-04/05/06 — apenas RECOMENDOU (donos: executor/Met/PMO per §9) ✅
- Nenhum código é escrito nesta sessão nem na próxima (dispatch) — implementação é etapa posterior ✅
- NÃO commitado — commits/pushes só com aprovação explícita do Founder ([[feedback-commit-approval]]) ✅

---

## 8. Próximo passo recomendado

1. **Founder cola este veredito na sessão PMO (Dispatcher)**.
2. **PMO aplica AJUSTES 01-05 (Forma A)** no charter — v0.2.0→v0.3.0 — em sessão separada desta (precedente: S-F1S1-CHARTER-AJUSTES aplicou os 4 do S1 no mesmo dia). Diffs prontos no §5 acima.
3. **Founder aprova commit** do charter v0.3.0 + este review.
4. **PMO escreve `S-F1S4-IMPLEMENTATION-DISPATCH.md`** (sessão SEPARADA) embutindo: Founder decisions §9 + AJUSTES aplicados + def-01..def-07 como cláusulas (auth /metrics, request_hash, pool config, workspace de bench, lista de partições + DEFAULT).
5. **Executor (Codex OU Claude fresh) roda S4** em `CKOS_RUNTIME` @ `1171384`, slices a-i, PRs `s4-*`.

**Calibre vs precedente S1:** o audit S1 rendeu 4 AJUSTES (auth trava-início, deliverables implícitos, envelope reconciliation, ownership git init) — todos confirmados valiosos na implementação. Os 5 daqui são do mesmo tipo: AJUSTE-01 e AJUSTE-04 salvam 2 exit checks que falhariam por design; AJUSTE-02 evita um `CREATE TABLE` impossível; AJUSTE-03 troca um passo inexecutável (branch Supabase) por um ensaio real.

---

## 9. BRA Packet + CHECKOUT RELEASE

```yaml
bra_id: BRA-METAREV-F1S4-CHARTER-20260611-01
from_session: S-F1S4-CHARTER-METAREV-CLAUDE-20260611-001
to: PMO/Dispatcher (claude) + Founder
context_summary:
  - "Charter F1 Sprint 4 v0.2.0 (commit ed0be72) auditado em Claude Code fresh, separado do autor claude_opus_4_7"
  - "Precondições verificadas: S1 done (4ed637d), runtime live ckos-runtime.fly.dev, 8 eventos b75238fd-..., 13/13 gates, Doc 11 findings 0"
  - "Anchors canônicos verificados RO: Doc 10 §5.3 (linhas 98-102), §5.6 (121-132), §5.26 (536-545); Doc 11 §7 (212-237) + §13 (439); Doc 13 §16 (385-398); Doc 12 §5.6 (176-224)"
  - "Achado central 1: exit check 4 (telemetria) falha por design — RAISE EXCEPTION desfaz o increment do counter na mesma transação"
  - "Achado central 2: exit check 2 (replay causal linear) é incompatível com os 8 eventos reais de S1 (4 LLMCost side-chain)"
  - "Achado central 3: unique(idempotency_key) global do Doc 11 §7 linha 232 é impossível em tabela particionada — finding canônico pra PATCH 3 via AQ-S4-04"
  - "Achado central 4: Supabase free tier não tem branching — deliverable #9 inexecutável como escrito"
outputs:
  - "F1S4_CHARTER_METACOGNIK_REVIEW.md (este): veredito + 8 checks + respostas B1-B8 + 5 AJUSTES diff-ready + 7 defers + separação de sessões"
verdict: APROVA-COM-AJUSTES
go_no_go: "GO como base para S-F1S4-IMPLEMENTATION-DISPATCH.md APÓS AJUSTES 01-05 (Forma A, v0.2.0→v0.3.0); sem eles, NO-GO"
ajustes_obrigatorios:
  - "AJUSTE-01 — telemetria à prova de rollback: trigger RETURN NULL + RAISE WARNING + counter persistente ops_counters (§2.1 #5 linha 79 + check 4 linha 181)"
  - "AJUSTE-02 — constraint × partição: PK/unique compostas + guarda app-side Doc 10 §5.6 + DEFAULT partition + finding Doc 11 pro PATCH 3 (§3 nota nova após linha 120)"
  - "AJUSTE-03 — migration safety real: sem branch Supabase (free tier), ensaio em PG15 local/2º projeto, triggers recriados como deliverable, app parado na janela, GET /trace regression no check 5 (#9 linha 83 + check 5 linha 182 + §9 linha 350)"
  - "AJUSTE-04 — replay causal: semântica topológica DAG com side-chains incluídos + check 2 reescrito + nota /trace vs /events/replay (§3.2 após linha 151 + check 2 linha 179)"
  - "AJUSTE-05 — contagem do exit criterion (3/5/6 → 6) + anchor línea 235 → linhas 214-217 (~8 ocorrências) + versões staled §7 step 3"
defers_nao_bloqueantes:
  - "def-01 /metrics auth = mock JWT mesmo middleware do /intent (dispatch)"
  - "def-02 request_hash = sha256(canonical_json({intent_text, user_id, workspace_id, project_id ?? null})) (dispatch)"
  - "def-03 postgres.js max:20 explícito + bench workers in-process enfileirando (dispatch)"
  - "def-04 eventos de bench permanentes (append-only) → workspace_id dedicado de bench (dispatch)"
  - "def-05 ~25 fk→events do Doc 11 (S3/S5+) impossíveis como FK simples pós-partição → PATCH 3"
  - "def-06 anchor Doc 13 §16 fraco pra telemetria — aceitar como preparação"
  - "def-07 lista das partições LIST iniciais + DEFAULT (dispatch; não criar 12 partições vazias)"
open_questions: []   # nenhuma AQ trava-início nova — gaps viraram AJUSTES diff-ready ou defers com dono
blockers:
  - "AJUSTES 01-05 devem ser aplicados (Forma A) antes do PMO escrever o dispatch"
recommended_next:
  - "Founder cola veredito na sessão PMO → PMO aplica AJUSTES 01-05 Forma A (charter v0.2.0→v0.3.0) em sessão separada"
  - "Founder aprova commit do charter v0.3.0 + este review"
  - "PMO escreve S-F1S4-IMPLEMENTATION-DISPATCH.md em sessão SEPARADA desta e da autora, com def-01..def-07 como cláusulas"
  - "Executor (Codex OU Claude fresh) roda S4 em CKOS_RUNTIME @ 1171384"
session_separation_confirmed:
  - "Esta sessão (auditora, Claude fresh) ≠ S-F1S4-CHARTER-CLAUDE-20260611-001 (autora) ✅"
  - "Próxima sessão (PMO dispatch) ≠ esta ≠ autora ✅"
  - "Esta sessão NÃO editou canônico/charter/dispatch-file; NÃO tocou CKOS_RUNTIME; NÃO decidiu AQs médias (só recomendou); NÃO commitou ✅"
```

```txt
CHECKOUT RELEASE — S-F1S4-CHARTER-METAREV-CLAUDE-20260611-001
files_created: 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/F1S4_CHARTER_METACOGNIK_REVIEW.md (este)
files_changed: 000_ROADMAPS/SESSION_REGISTRY.md (1 sessão + 1 lock + release)
files_not_touched:
  - F1_SPRINT4_CHARTER.md (RO — alvo do audit; AJUSTES serão aplicados pelo Dispatcher em sessão separada)
  - canônico 01-28 (RO — Doc 10 §5.3/§5.6/§5.26, Doc 11 §7/§13, Doc 12 §5.6, Doc 13 §16 só lidos)
  - S-METACOGNIK_F1S4_CHARTER_REVIEW.md (dispatch task file — placeholders C/D preservados, pattern S1)
  - F1_SPRINT1_CHARTER.md + S-F1S1-IMPLEMENTATION-DISPATCH.md (RO — pattern + baseline §17)
  - 03_BACKEND_MVP_THIN_SLICE_PLAN.md + CKOS_EXPANSION_KANBAN.md (RO — ordem sprints + lane F1)
  - ARCHITECTURE_PATCH_REPORT.md (audit de planning não gera entry); 00_SYSTEM_GOVERNANCE/* (RO)
  - CKOS_RUNTIME (não tocado); SQL/UI/backend/migrations (não criados — read-only audit)
validation: 8 checks executados (escopo IN/OUT, coerência canônico com anchors verificados linha a linha,
  realismo exit criterion + factibilidade perf no stack production, partition migration risk a-e,
  AQ coverage a-e, Founder decisions §9, plano de dispatch + slices); 8 perguntas PMO (B1-B8) respondidas;
  veredito APROVA-COM-AJUSTES com 5 AJUSTES diff-ready (Forma A) + 7 defers com dono
risks_remaining: implementação pode revelar gaps adicionais (semântica exata do causation_id dos LLMCost
  em S1 — dado a confirmar pelo executor; comportamento do Drizzle com view backward-compat) — caminho
  previsto: anexo do dispatch + F1S4_DOC11_PATCH_FINDINGS → PATCH 3 (AQ-S4-04)
next_step:
  - PMO aplica AJUSTES 01-05 Forma A (charter v0.2.0→v0.3.0) → Founder aprova commit
  - depois: PMO escreve S-F1S4-IMPLEMENTATION-DISPATCH.md (sessão separada)
status: released
```
