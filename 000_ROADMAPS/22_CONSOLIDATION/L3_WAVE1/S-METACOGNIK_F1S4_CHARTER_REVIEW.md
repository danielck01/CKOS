---
title: Metacognik — Completeness Audit do F1 Sprint 4 Charter (Event Log Hardening)
file: S-METACOGNIK_F1S4_CHARTER_REVIEW.md
layer: auxiliary
doc_type: pmo_session_task
phase: 000_ROADMAPS
category: consolidation
status: awaiting_run
version: 0.1.0
created_at: 2026-06-11
owner: pmo_ckos
dispatcher: claude (S-F1S4-CHARTER-CLAUDE-20260611-001 → atuando como Dispatcher do charter audit)
session_id: S-F1S4-CHARTER-METAREV-CLAUDE-20260611-001
role: metacognik_completeness_auditor
depends_on:
  - S-F1S4-CHARTER-CLAUDE-20260611-001            # charter v0.2.0 publicado (commit ed0be72)
  - S-F1S1-PMO-VERIFY-CLAUDE-20260611-001         # S1 production validado (sprint-done 4ed637d) — precondition
companion_of: F1_SPRINT4_CHARTER.md
audit_context: >
  Esta NÃO é uma 2ª chave de canonical_patch. O F1 Sprint 4 Charter é um planning artifact (não
  modifica canônico 01-28). Esta sessão faz completeness/coherence audit: o charter cobre o necessário
  para o Event Log hardening destravar S2/S3/S5/S6? As decisões Founder (§9) são suficientes? O exit
  criterion (5 checks) é binário, testável e factível no stack production atual (Fly shared-cpu-1x +
  Supabase free tier pooler)? A partition migration em produção tem plano de segurança adequado?
  Veredito: APROVA / APROVA-COM-AJUSTES / REPROVA — libera (ou trava) o PMO escrever o dispatch de
  implementação.
separation_of_duties: >
  Sessão SEPARADA e independente. O autor do charter (claude, S-F1S4-CHARTER-CLAUDE-20260611-001)
  NÃO revisa o próprio charter. Esta sessão DEVE rodar em **Claude Code em chat fresh** (instância
  separada, contexto novo, sem memória da sessão autora). **Windsurf NÃO é o executor recomendado** —
  audit de completeness exige raciocínio (avaliar riscos de migration em produção, factibilidade de
  performance targets, gaps de escopo), fora do nicho APPLY mecânico. Read-only: NÃO aplica, NÃO edita
  canônico, NÃO edita o charter nem qualquer companion. Retorna veredito + findings.
tags: [session-task, metacognik, completeness-audit, charter, f1, sprint-4, event-log, hardening, l3-wave1, post-sprint-1-done]
---

# Metacognik — Completeness Audit do F1 Sprint 4 Charter

> **A sessão que libera o PMO a escrever o dispatch de implementação do S4:** "dispare a sessão de completeness audit do charter F1 Sprint 4".
> Audita o **F1_SPRINT4_CHARTER.md v0.2.0** (commit `ed0be72`) — escopo IN/OUT, coerência com canônico, realismo do exit criterion (5 checks), riscos da partition migration em produção, Founder decisions (§9), plano de dispatch.
> Devolve veredito: **APROVA / APROVA-COM-AJUSTES / REPROVA**.
> **Não aplica nada.** Se aprovar, PMO escreve `S-F1S4-IMPLEMENTATION-DISPATCH.md` (sessão separada) que orquestra o executor em `CKOS_RUNTIME` (mesmo repo de S1, branch base `main` @ `1171384`).
> **Rode com contexto fresco em Claude Code — você não é o autor do charter, e Windsurf não faz audit.**

---

## A. PROMPT PARA COLAR (template auditor — completeness audit)

```txt
You are a CKOS session under MULTI_SESSION_EXECUTION_POLICY.
- Fonte de verdade aprovada = canônico 01-28 (pós-PATCH 2 e 2.5); docs 29-34 gated.
- NÃO edite canônico 01-28 nem o charter F1_SPRINT4_CHARTER.md. NÃO atualize ARCHITECTURE_PATCH_REPORT.md
  nem 00_SYSTEM_GOVERNANCE/*.
- NÃO crie backend, UI, API, migrations, SQL, agentes runtime. read-only = só findings + veredito.
- Esta NÃO é uma 2ª chave de canonical_patch — é audit de completeness de um planning artifact.

ROLE: Metacognik completeness auditor (read-only) do F1 Sprint 4 Charter.
SESSION: S-F1S4-CHARTER-METAREV-CLAUDE-20260611-001.
CONTEXT: S1 (Intent Ingress) DONE em produção (sprint-done commit 4ed637d, 2026-06-11) — runtime live em
         https://ckos-runtime.fly.dev (Fly GRU shared-cpu-1x 512MB + Supabase free tier via Session Pooler
         aws-1-sa-east-1, ~60 conexões max). 8 eventos S1 reais no DB (correlation_id b75238fd-...).
         Founder respondeu AQ-S4-01/02/03 do charter (2026-06-11, §9): partition LIST+RANGE, idempotency
         window 24h, perf targets P95 <100ms + ≥50 events/s.
         Você decide se o charter está completo para PMO escrever o dispatch de implementação.
SEPARATION: o autor do charter = claude (S-F1S4-CHARTER-CLAUDE-20260611-001). Você NÃO é ele.
            Executor recomendado: **Claude Code em chat fresh** (NÃO Windsurf — audit precisa de raciocínio).

READ (nesta ordem):
  - 000_ROADMAPS/22_CONSOLIDATION/F1_SPRINT4_CHARTER.md          (o alvo — v0.2.0, escopo + AQs + §9 decisions)
  - 000_ROADMAPS/22_CONSOLIDATION/F1_SPRINT1_CHARTER.md          (pattern + AJUSTE-03 tabela envelope conceitual↔físico)
  - 000_ROADMAPS/22_CONSOLIDATION/S-F1S1-IMPLEMENTATION-DISPATCH.md §17  (production_deploy block — baseline real: healthcheck 8ms, e2e 22s, 8 eventos)
  - 000_ROADMAPS/22_CONSOLIDATION/03_BACKEND_MVP_THIN_SLICE_PLAN.md §14  (ordem dos sprints: S1 → S4 → S2/S3 → S5 → S6)
  - 000_ROADMAPS/22_CONSOLIDATION/CKOS_EXPANSION_KANBAN.md       (S1 ✅ + S4 como #blocker lane F1)
  - canônico cross-ref (RO, confirmar coerência):
      03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md §5.3 (Event Bus e Event Log — append-only, envelope, ordering/causation)
      03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md §5.6 (Run Scheduler, Queue, Retry, Timeout, Idempotency)
      03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md §5.26 (Run Replay)
      03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md §7 (events table físico — linhas 217-235, especialmente línea 235 partition hint)
      03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md §16 (quality gates — telemetria/baseline)
      03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md §5.6 (RLS — pra avaliar exposição do /metrics)

AUDIT GOAL: dar veredito sobre completeness do charter.
  1. ESCOPO IN — os 9 deliverables são SUFICIENTES e CORRETOS pro exit criterion (5 checks §5)? Falta algo
     crítico (ex: backward-compat do GET /trace existente após partition? rollback plan se migration falhar
     em produção? estratégia de downtime/zero-downtime durante o swap da tabela)?
  2. ESCOPO OUT — algum defer é DE FATO precondição técnica de S4? Algum IN que poderia ser defer sem quebrar
     o exit criterion (over-scope)? Em particular: outbox pattern defer S5 está correto, ou particionar SEM
     outbox cria retrabalho em S5?
  3. COERÊNCIA com canônico — anchors batem? Doc 11 §7 línea 235 realmente diz "partição por aggregate_type
     + range por created_at"? Doc 10 §5.26 Run Replay é coerente com replay causal via causation_id chain?
     A tabela ingress_idempotency (extensão não-canônica §3.1) viola algum princípio (anti-fragmentação,
     "schemas SQL fora do Doc 11" do PROIBIDO §2.3)? O charter justifica adequadamente a exceção?
  4. REALISMO DO EXIT CRITERION — os 5 checks são binários e testáveis? P95 <100ms + 50 events/s é factível
     em Fly shared-cpu-1x 512MB + Supabase free tier pooler (~60 conns)? O check 5 (partition migration sem
     perda dos 8 eventos S1) tem verificação objetiva? O stress test (bench:events 1000 events + 100 workers)
     pode esgotar o pooler de 60 conexões ou derrubar o app em produção?
  5. PARTITION MIGRATION RISK — o plano (criar events_partitioned → copiar → swap rename + view backward-compat)
     é seguro? Gaps: (a) o que acontece com pg-boss workers durante o swap? (b) Drizzle schema.ts precisa
     refletir a partição ou o ORM é agnóstico? (c) a view backward-compat mantém os triggers append-only?
     (d) janela de downtime aceitável ou zero-downtime obrigatório? (e) FKs de context_packs ou outras tabelas
     apontando pra events quebram no rename?
  6. AQ COVERAGE — as 6 AQs cobrem o que falta? Gaps não nomeados: (a) auth do GET /metrics (exposto público
     vaza info operacional? Doc 12 §5.6 exige?); (b) onde o counter de telemetria persiste (Postgres table vs
     in-memory que reseta no restart do Fly machine auto_stop)?; (c) request_hash do idempotency — o que entra
     no hash (intent_text + user_id + workspace_id? project_id?) e colisões; (d) replay causal quando
     causation_id é NULL (root) ou quando LLMCost events formam side-chain fora da cadeia linear workflow;
     (e) bench:events roda contra produção ou DB separado (custo/risco free tier)?
  7. FOUNDER DECISIONS §9 — as 3 respostas (LIST+RANGE, 24h, P95 <100ms + 50 ev/s) estão registradas com
     implicações? AQ-S4-04/05/06 médias têm dono claro (executor vs Met vs PMO)?
  8. PLANO DE DISPATCH §7 — os 7 passos são realistas? Slices propostos (a-i) cobrem os 9 deliverables?
     Verificação (step 6) nomeia executor self-test + PMO valida + Founder assina — coerente com pattern S1?

RETURN: veredito (APROVA / APROVA-COM-AJUSTES / REPROVA);
  tabela de findings por checagem 1-8;
  go/no-go explícito do charter como base para o dispatch de implementação;
  lista de AJUSTES obrigatórios (se APROVA-COM-AJUSTES) — citar §, linha, texto exato (diff-ready, Forma A);
  lista de gaps não-bloqueantes (defer pro dispatch ou pra durante S4);
  confirmação de que a próxima sessão (PMO escreve S-F1S4-IMPLEMENTATION-DISPATCH.md) é SEPARADA desta
  e da autora do charter.

CLOSE WITH: criar L3_WAVE1/F1S4_CHARTER_METACOGNIK_REVIEW.md + CHECKOUT RELEASE
  (files_created: esse 1; files_changed: SESSION_REGISTRY 1 sessão + 1 lock + release; status: released).
  NÃO commitar — commits/pushes só com aprovação explícita do Founder (feedback-commit-approval).
```

---

## B. PERGUNTAS DO PMO → (o revisor responde no relatório)

1. **Backward-compat do `/trace`:** S1 production tem `GET /trace/:correlation_id` funcionando (validado com 8 eventos reais). Após partition swap + view, esse endpoint continua retornando os mesmos 8 eventos byte-idênticos? O charter §5 check 5 cobre só `SELECT * FROM events WHERE workspace_id` — devia cobrir o endpoint HTTP também?

2. **Triggers na tabela particionada:** Postgres triggers `BEFORE UPDATE/DELETE FOR EACH ROW` em tabelas particionadas têm semântica diferente (precisam estar na partição ou na parent conforme versão PG15). O charter assume que o trigger append-only "já implementado em S1" sobrevive à migration — verifique se isso é assumption ou precisa ser deliverable explícito.

3. **Esgotamento do pooler no stress test:** bench:events com 100 workers paralelos contra Supabase free tier (pooler ~60 conns no Session mode). O postgres.js client do runtime tem `max` connections configurado? Stress test vai enfileirar ou estourar? Recomende config explícita pro dispatch (ex: `max: 20` no client + workers enfileiram).

4. **Counter de telemetria — persistência:** `events_append_attempts_blocked_total` — se for in-memory no Fastify process, reseta a cada deploy/restart (e Fly auto_stop_machines para a machine em idle!). Postgres table de counters resolve mas adiciona write por increment. Qual a recomendação certa pro S4 (e é AJUSTE ou decisão de dispatch)?

5. **request_hash spec:** o charter §3.1 diz `sha256(intent_text + user_id + ...)` — o `...` é gap. O que entra exatamente? Se `project_id?` opcional entra, requests iguais com/sem project_id geram hashes diferentes (correto?). Recomende a fórmula fechada pro dispatch.

6. **Replay causal — side-chains:** os 8 eventos S1 incluem 4 LLMCost que NÃO estão na cadeia causal linear do workflow (IntentSubmitted → IntentResolved → ContextAssembled → PartialOutputProduced). No ordering=causal, LLMCost aparecem onde? (filhos do evento que os causou? excluídos? flag separada?) O charter §3.2 não especifica — AJUSTE ou dispatch detail?

7. **`/metrics` auth:** Prometheus text format exposto público em https://ckos-runtime.fly.dev/metrics vaza contagens operacionais (quantos eventos, quantas tentativas bloqueadas). Doc 12 §5.6 deny-by-default sugere proteger. Mock JWT (mesmo do /intent) ou IP allowlist ou deixar público em S4 (risco aceito)? Recomende.

8. **Zero-downtime vs janela:** o app em produção tem auto_stop_machines (para quando idle). A migration de partição pode rodar com o app parado (janela trivial, zero tráfego real ainda) — o charter §2.1 #4 fala em "swap via rename" mas não explicita a janela. Para S4 com 1 usuário (Founder), janela de minutos é aceitável? Confirme que zero-downtime NÃO é requisito de S4 (over-engineering) ou argumente o contrário.

---

## C. ← PERGUNTAS PARA O PMO/FOUNDER (BRA) · Metacognik preenche

```yaml
bra_id: BRA-METAREV-F1S4-CHARTER-20260611-01
from_session: S-F1S4-CHARTER-METAREV-CLAUDE-20260611-001
to: PMO/Dispatcher (claude) + Founder
open_questions: [ (preencher após audit) ]
blockers:
  - "depende do charter F1_SPRINT4_CHARTER.md v0.2.0 (já publicado no commit ed0be72)"
  - "depende do S1 sprint-done (commit 4ed637d) — confirmar runtime live antes de auditar targets"
  - "depende das Founder decisions §9 (já registradas em 2026-06-11)"
recommended_next:
  - "(preencher: se APROVA → PMO escreve S-F1S4-IMPLEMENTATION-DISPATCH.md em sessão separada)"
  - "(se APROVA-COM-AJUSTES → Dispatcher aplica AJUSTES Forma A no charter v0.2.0→v0.3.0; depois dispatch)"
  - "(se REPROVA → volta ao Dispatcher para re-trabalhar charter)"
```

---

## D. CHECKOUT RELEASE · Metacognik preenche

```txt
CHECKOUT RELEASE — S-F1S4-CHARTER-METAREV-CLAUDE-20260611-001
files_created: L3_WAVE1/F1S4_CHARTER_METACOGNIK_REVIEW.md
files_changed: SESSION_REGISTRY.md (1 sessão + 1 lock + release)
files_not_touched: charter F1_SPRINT4_CHARTER.md (RO — auditado, não editado); canônico 01-28 (RO);
  S1 charter/dispatch (RO — pattern + baseline); CKOS_RUNTIME (não tocado); backend MVP plan / kanban (RO);
  ARCHITECTURE_PATCH_REPORT.md (audit de planning não gera entry)
validation: 8 checks executados — completeness IN/OUT, coerência canônico, realismo exit criterion +
  partition migration risk, AQ coverage, Founder decisions §9, plano de dispatch; veredito + findings +
  AJUSTES (se houver, diff-ready) + gaps não-bloqueantes
risks_remaining: dispatch de implementação pode descobrir gaps reais durante S4 (Doc 11 partition findings,
  trigger semantics em particionada) que viram PATCH 3 — charter AQ-S4-04 já prevê esse caminho
next_step:
  - APROVA → PMO escreve S-F1S4-IMPLEMENTATION-DISPATCH.md (sessão separada)
  - APROVA-COM-AJUSTES → Dispatcher aplica Forma A (charter v0.2.0→v0.3.0); commit; depois dispatch
  - REPROVA → volta ao Dispatcher
status: released
```

---

## E. Entrada de SESSION_REGISTRY proposta (Dispatcher registra como `planned`)

```txt
S-F1S4-CHARTER-METAREV-CLAUDE-20260611-001 | F1S4_CHARTER_COMPLETENESS_AUDIT_20260611 | audit | metacognik (claude fresh) |
  scope: read F1_SPRINT4_CHARTER.md v0.2.0 + F1_SPRINT1_CHARTER.md (pattern) + S1 dispatch §17 (baseline prod)
  + backend plan §14 + kanban + canônico Doc 10 §5.3/§5.6/§5.26, Doc 11 §7, Doc 13 §16, Doc 12 §5.6;
  write L3_WAVE1/F1S4_CHARTER_METACOGNIK_REVIEW.md + registry | planned (depende do charter, commit ed0be72)
forbidden: aplicar/editar canônico 01-28; editar o charter; tocar CKOS_RUNTIME; `00_SYSTEM_GOVERNANCE/`;
  `ARCHITECTURE_PATCH_REPORT.md`; SQL/UI/backend; move/rename/delete; rodar implementação (sessão separada);
  decidir AQ-S4-04/05/06 (médias — só RECOMENDAR); commitar (aprovação explícita do Founder requerida)
separation: NÃO pode ser a sessão autora (S-F1S4-CHARTER-CLAUDE-20260611-001); DEVE ser Claude Code fresh
  (NÃO Windsurf — audit em Claude per feedback-metacognik-executor)
```

---

## F. Fluxo da completeness audit

```txt
1. Founder cola a seção A num chat **fresh em Claude Code** (instância separada do autor; NÃO Windsurf)
2. Metacognik roda → produz L3_WAVE1/F1S4_CHARTER_METACOGNIK_REVIEW.md com:
   - veredito (APROVA / APROVA-COM-AJUSTES / REPROVA)
   - findings 1-8 + respostas às 8 perguntas PMO (seção B)
   - AJUSTES obrigatórios diff-ready (se houver)
   - gaps não-bloqueantes (defer pro dispatch ou durante S4)
3. Founder volta à sessão PMO (Dispatcher) e cola o veredito
4. Se APROVA → PMO escreve S-F1S4-IMPLEMENTATION-DISPATCH.md
5. Se APROVA-COM-AJUSTES → PMO aplica Forma A (charter v0.2.0→v0.3.0), commit, depois dispatch
6. Se REPROVA → PMO re-trabalha charter (raro — escopo cirúrgico limita risco)
```

> **Importante:** mesmo se Metacognik aprovar, **nenhum código é escrito nesta sessão nem na próxima**. A próxima
> sessão (PMO) só escreve o dispatch. A implementação real é etapa posterior, no `CKOS_RUNTIME` (executor
> Codex OU Claude fresh, branch base `main` @ `1171384`).

> **Precedent S1:** o audit do charter S1 produziu APROVA-COM-AJUSTES com 4 AJUSTES de alta qualidade
> (auth trava-início, deliverables implícitos, envelope reconciliation, ownership git init) — todos
> confirmados valiosos na implementação. Esperar findings do mesmo calibre aqui, provavelmente sobre:
> partition migration safety, telemetria persistence, pooler exhaustion no stress test, /metrics auth.
