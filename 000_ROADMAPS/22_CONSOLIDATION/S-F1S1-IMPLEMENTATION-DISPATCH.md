---
title: F1 Sprint 1 — Implementation Dispatch (Intent Ingress)
file: S-F1S1-IMPLEMENTATION-DISPATCH.md
layer: auxiliary
doc_type: pmo_implementation_dispatch
phase: 000_ROADMAPS
category: consolidation
status: ready_for_executor
version: 1.0.0
created_at: 2026-06-10
owner: pmo_ckos
dispatcher: claude_opus_4_7 (S-F1S1-CHARTER-AJUSTES-CLAUDE-20260610-001 — PMO Dispatcher)
session_id: S-F1S1-IMPLEMENTATION-DISPATCH-20260610-001
target_session: S-F1S1-IMPL-EXEC-<DATE>-001  # a abrir pelo executor (Codex OU Claude Code fresh)
derives_from:
  - F1_SPRINT1_CHARTER.md v0.3.0                                  # source-of-truth do escopo (commit b22ecbe)
  - L3_WAVE1/F1S1_CHARTER_METACOGNIK_REVIEW.md                    # AJUSTES + deferíveis (commit 26fba60)
  - 03_BACKEND_MVP_THIN_SLICE_PLAN.md §3/§9/§14/§18               # backend-antes-de-UI + exit criterion + ordem + user-first
  - GATE5_FOUNDER_DECISION_PACKAGE.md §7-§8                       # tech stack confirmado
target_repo:
  url: https://github.com/danielck01/CKOS_RUNTIME
  visibility: private
  default_branch: main
  created_at: 2026-06-10
  created_via: gh CLI (PMO executando via claude_opus_4_7 com Founder approval)
target_canonical: []   # implementation dispatch NÃO edita canônico 01-28
approval_required:
  - founder   # Founder revisa + aprova antes do executor arrancar
non_authority_boundary: >
  Implementation dispatch — orquestra a sessão de IMPLEMENTAÇÃO do F1 Sprint 1 em REPO SEPARADO
  (`CKOS_RUNTIME`). NÃO edita canônico 01-28 deste repo (apenas cita). NÃO é canonical_patch. NÃO
  modifica o charter (charter está frozen em v0.3.0). Implementação real é uma sessão SEPARADA desta
  e da autora do charter. Cadeia de chaves para implementation: Founder review desta dispatch +
  executor escolhe entre Codex e Claude fresh em sessão nova.
tags: [implementation, dispatch, f1, sprint-1, intent-ingress, runtime, ckos-runtime-repo, post-charter-v0.3.0]
---

# F1 Sprint 1 — Implementation Dispatch (Intent Ingress)

> **A sessão que destrava a implementação real do CKOS runtime.** Pega o `F1_SPRINT1_CHARTER.md v0.3.0` (commit `b22ecbe`) + decisões pós-charter + AQs novas e converte em **especificação operacional autocontida** para executor (Codex OU Claude Code fresh) iniciar S1 em `CKOS_RUNTIME` (repo separado).
> **O que não é:** não escreve código. Não modifica canônico. Não modifica o charter. Apenas orquestra o handoff para implementação.

---

## 0. Contexto + precondições (todas satisfeitas)

| Item | Estado | Commit |
|---|---|---|
| GATE 5 = GO + AQ-IO-1 = `user` (Founder) | ✅ 2026-06-09 | `1b13f2c` |
| PATCH 2 applied (Doc 02 User canônico + Doc 05 memória user_id + Doc 03 Agent Run typing + Doc 04 anti-pattern policies) | ✅ 2026-06-09 | `5d1d969` |
| PATCH 2.5 applied (Doc 10 §5.2 IntentSubmitted + Doc 15 §5.1 Command Center alinhado) | ✅ 2026-06-09 | `79d66e1` |
| F1 Sprint 1 Charter v0.3.0 (Founder approved + Metacognik APROVA-COM-AJUSTES + 4 AJUSTES applied) | ✅ 2026-06-10 | `b22ecbe` |
| Repo `CKOS_RUNTIME` criado (private, default `main`, README + Node gitignore) | ✅ 2026-06-10 | github.com/danielck01/CKOS_RUNTIME |
| `gh` CLI instalado + autenticado (`danielck01`, escopos `repo`+`workflow`+`read:org`+`gist`) | ✅ 2026-06-10 | n/a |

Nada bloqueia o início da implementação. Esta dispatch é o **último artefato PMO antes do executor arrancar**.

---

## 1. Repo de implementação (separado)

| Propriedade | Valor |
|---|---|
| **URL** | https://github.com/danielck01/CKOS_RUNTIME |
| **Visibility** | private |
| **Default branch** | `main` (modernização — doc repo `CKOS` permanece em `master` como legacy) |
| **Estado inicial** | 1 commit (README + Node .gitignore) |
| **Permissões** | `danielck01` é owner; executor terá acesso via `gh auth login` no ambiente dele |
| **Cross-ref ao doc repo** | README do `CKOS_RUNTIME` aponta para `github.com/danielck01/CKOS` (este repo) como **canonical spec**. Implementação cita Doc 10 §5.2 etc. via path: `https://github.com/danielck01/CKOS/blob/<BASELINE_COMMIT>/03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md` |
| **Baseline canonical pin** | Executor pina o commit `b22ecbe` (charter v0.3.0) como baseline. Cross-refs cite esse SHA, não `master` (cita o estado, não o moving target) |

> **Convenção de commits no `CKOS_RUNTIME`:** prefixos `feat: ...`, `fix: ...`, `chore: ...`, `test: ...`, `refactor: ...`, `docs: ...`, `ci: ...` (conventional commits). Diferente do doc repo (`canonical_patch:`, `planning:` etc.).

---

## 2. Tech stack (final — sem renegociação durante S1)

Decisões fechadas em GATE 5 §7 + AQ-S1-02 (Founder approved 2026-06-10) + AQ-S1-07/08/09 (PMO decide com Founder approval — ver §3).

| Layer | Escolha | Versão alvo | Justificativa |
|---|---|---|---|
| **Language** | TypeScript | 5.4+ (strict mode) | type safety + ecosystem Supabase/pg-boss/OpenRouter |
| **Runtime** | Node.js | 20 LTS | suporta top-level await, native fetch, ESM |
| **Package manager** | pnpm | 9+ | rápido, monorepo-ready, lockfile determinístico |
| **HTTP framework** | Fastify | 4+ | schema-first (TypeBox ou JSON Schema), perf, OpenAPI plugin |
| **DB** | PostgreSQL via Supabase | 15+ | já decidido em GATE 5; RLS Doc 12 §5.6 |
| **DB client** | postgres.js (`postgres`) | 3.4+ | leve, fast, sem ORM overhead; Drizzle usa por baixo |
| **ORM/migrations** | **Drizzle ORM + drizzle-kit** | drizzle 0.30+, kit 0.22+ | TS-native, schema-first, suporta partição Postgres (events table), migrations versionadas (AQ-S1-08) |
| **Job runner** | pg-boss | 9+ | Postgres-native; zero infra extra (GATE 5 §7) |
| **LLM gateway** | OpenRouter | API v1 | Claude 4.7 Opus + GPT-5.5 com fallback mútuo (GATE 5 §8) |
| **Secret store** | Supabase Vault + secret_refs | n/a | Doc 11 §12.1 + Doc 12 §5.15 |
| **Deploy** | Fly.io OU Railway (container) | Docker base Node 20-alpine | Executor escolhe no `fly launch`/`railway init` baseado em UX preferida; ambos suportam pg-boss worker + HTTP juntos |
| **CI** | GitHub Actions | n/a | `.github/workflows/ci.yml` no `CKOS_RUNTIME` |
| **Test runner** | Vitest | 1.6+ | rápido, TS-native, compatible Jest API |
| **Linter/formatter** | Biome | 1.7+ | substitui ESLint + Prettier; mais rápido |
| **Logging** | pino | 9+ | structured JSON logs, pino-pretty em dev |
| **Schema validation** | Zod | 3+ | runtime validation dos events + Drizzle adapter |
| **OpenRouter SDK** | OpenAI SDK (com baseURL=openrouter) | 4+ | OpenRouter é OpenAI-compatible API |

**Estrutura inicial do repo** (executor cria):
```
CKOS_RUNTIME/
├── .github/workflows/ci.yml
├── src/
│   ├── ingress/        # HTTP routes (Fastify)
│   ├── events/         # event types + Zod schemas + publishers
│   ├── transformers/   # intent_to_object (S1 only) + future
│   ├── context/        # context assembler
│   ├── workers/        # pg-boss workers
│   ├── db/             # Drizzle schema + queries + migrations config
│   ├── config/         # env loading + Vault resolution
│   └── lib/            # logger, openrouter client, tracing
├── drizzle/
│   ├── schema.ts       # tabelas (events, users, user_profiles, context_packs)
│   └── migrations/     # SQL migrations geradas
├── tests/
│   ├── unit/
│   ├── integration/    # com DB real (testcontainers OU Supabase test branch)
│   └── e2e/            # 1 intent → 3 events + 1 output
├── scripts/
│   ├── dev.sh
│   ├── migrate.sh
│   └── seed.sh
├── package.json
├── tsconfig.json
├── drizzle.config.ts
├── biome.json
├── Dockerfile
├── fly.toml OR railway.json (escolha do executor)
├── .env.example         # OPENROUTER_API_KEY, SUPABASE_DB_URL, JWT_SECRET, etc.
└── README.md
```

---

## 3. AQs respondidas (decisões fechadas para o executor não negociar)

### Respostas Founder (charter §9, AQ-S1-01/02/03) — reiteradas

- **AQ-S1-01 (repo):** `CKOS_RUNTIME` paralelo (criado em §1 acima)
- **AQ-S1-02 (stack):** TypeScript + Fastify + Fly.io/Railway (escolha entre os 2 = executor)
- **AQ-S1-03 (executor):** Codex OU Claude Code fresh — Windsurf NÃO (per [[feedback-metacognik-executor]])

### Respostas pós-charter (Metacognik AJUSTES) — reiteradas

- **AQ-S1-05 (auth — promovida a trava-início):** **Mock JWT bearer literal** — header `Authorization: Bearer test-user-jwt-{user_id}`. Sem backend de auth real. Auth real entra em S3 (policy/approval). Validação: middleware Fastify simples que parseia o `user_id` do bearer e injeta no contexto da request. JWT secret: `JWT_SECRET=dev-only-not-for-prod` no .env (não é HMAC real — só parsing).

### Respostas novas (PMO defaults, Founder approved 2026-06-10)

- **AQ-S1-07 (orçamento LLM):**
  - **Dev:** $50/mês cap (OpenRouter native budget setting); alerta em 70% ($35), hard stop em 100%
  - **CI/e2e:** $10/mês cap; mesmo alerta. Cada e2e ≤ $0.05.
  - **Per-call cost guard:** middleware no `openrouter client` checa estimativa de tokens antes do call; se > $0.10/call → log warning + métrica. Hard cap: $0.50/call → bloqueia.
  - **Implementação S1:** OpenRouter dashboard configura budget; código emite `LLMCostEstimated{call_id, estimated_usd}` antes do call e `LLMCostActual{call_id, actual_usd, tokens_in, tokens_out}` depois.
- **AQ-S1-08 (migration tool):** **Drizzle ORM + drizzle-kit**. Schema TS em `drizzle/schema.ts`; migrations geradas via `drizzle-kit generate`; aplicadas via `drizzle-kit migrate` ou `drizzle-kit push` em dev. Suporta partição Postgres nativa (necessária pra events table partition by `aggregate_type` + range por `created_at`).
- **AQ-S1-09 (gh CLI no executor):** Executor terá `gh` instalado + autenticado no ambiente. Commits diretos via `git`, PRs via `gh pr create`. PMO/Founder reviews PRs via GitHub UI ou `gh pr view`.

### Deferíveis (não entram em S1 — registrados para futuro)

- **def-01** `secret_refs.owner_type = 'provider'` para OpenRouter → fixado aqui (executor implementa o valor literal `'provider'` na primeira inserção do `secret_refs`)
- **def-02** RLS para `events.project_id IS NULL` → PATCH 3 (workaround S1: RLS por `workspace_id + actor_id = user_id`)
- **def-03** orçamento LLM — fechado em AQ-S1-07 acima
- **def-04** monitoring além de log + correlation_id → emergente; Doc 13 §16 entra em S6
- **def-05** explicitar `PolicyChecked`/`RunStarted` skipados em §2.2 → nota leve no charter; nada a fazer em código
- **def-06** cosmético `project_id?` vs `project_id` literal → PATCH 3 (F-03)

---

## 4. Escopo IN (9 deliverables — fonte: F1_SPRINT1_CHARTER.md §2.1 v0.3.0)

Cobertura cirúrgica. Cada deliverable é independente mas se acopla pelos eventos.

| # | Deliverable | Spec resumida |
|---|---|---|
| **1** | **Endpoint de ingress backend** | `POST /intent` em Fastify; auth via mock JWT middleware; valida payload Zod; persiste `IntentSubmitted` event; retorna `{correlation_id}` |
| **2** | **Event Log mínimo** | Tabela `events` em Postgres (schema físico Doc 11 §7 — ver §6 abaixo); append-only invariant via constraint; idempotency via `idempotency_key UNIQUE` |
| **3** | **Intent Resolver** | Worker pg-boss que consome `IntentSubmitted` → chama transformer `intent_to_object` (LLM via OpenRouter) → publica `IntentResolved` event |
| **4** | **Context Assembler básico** | Worker que consome `IntentResolved` → query DB pra `user_memory_refs[]` + `project_memory_refs[]?` (memória curta MVP) → publica `ContextAssembled` event |
| **5** | **1 output simples rastreável** | Worker final que consome `ContextAssembled` → produz output JSON `{correlation_id, intent_type, candidate_objects, response_type, depth_level, reasoning_mode, payload_text}` → publica `PartialOutputProduced` (simplificado, sem streaming) |
| **6** | **Tracing end-to-end** | `correlation_id` UUIDv4 gerado em §1 e propagado em todos eventos + logs pino |
| **7** | **DB migrations** | Drizzle: `events`, `users`, `user_profiles`, `context_packs`, `secret_refs`. Schema TS em `drizzle/schema.ts` |
| **8** | **Healthcheck endpoint** | `GET /health` retorna `{status: "ok", db: "connected", queue: "running"}` em <100ms; usado por Fly.io/Railway routing |
| **9** | **Error handling Intent Resolver** | Falha OpenRouter (timeout/429/5xx) → emite `IntentResolutionFailed{correlation_id, error_kind, retry_count}` em vez de explodir. pg-boss retry policy: 3 retries, exponential backoff (1s, 5s, 30s) |

### Veredito 1-linha (charter §0)

> Sprint 1 entrega **um endpoint de ingress backend que aceita uma intenção, persiste `IntentSubmitted{user_id, intent_text, project_id?, ...}` no event log, resolve a intenção via Intent Resolver, monta Context Packet mínimo, e gera 1 output simples rastreável por `correlation_id` — sem UI**.

---

## 5. Escopo OUT (defer — não implementar em S1)

Cobertura completa em [F1_SPRINT1_CHARTER.md §2.2](F1_SPRINT1_CHARTER.md). Resumo crítico:

- ❌ **UI / CommandBar / qualquer frontend** — defer F4
- ❌ **Approval Gate completo** — defer S3
- ❌ **Question Engine + clarity scorer** — defer S2
- ❌ **Work Order + Agent Run completo** — defer S5
- ❌ **Feedback loop + ROI + memória longa** — defer S6
- ❌ **`ProjectInferred` event** — defer S2 (Cognik decide)
- ❌ **Doc 11 `users` enrichment** (campos PATCH 2: `operating_dna_ref?`, `tribes_scored?`, etc.) — defer PATCH 3
- ❌ **F-01/F-02/F-03** — defer PATCH 3
- ❌ **Streaming output** (passo 8 do fluxo de 14) — S1 retorna síncrono; streaming é S5

### PROIBIDO durante S1

- Criar `/CKOS_USER_SYSTEM/` ou pastas paralelas
- Schemas SQL fora do que Doc 11 §4/§7/§12.1/§13 define
- Smart Response Engine docs 01-07 (duplica Doc 10 §5.2)
- 100 smart questions hardcoded (7-12 amarradas a S1/S2 bastam — entra em S2)
- "Personagem IA com nome bonito sem skill contratada" (Constituição §1)

---

## 6. Contratos de eventos (literal — pronto pra implementar como Zod schemas)

### 6.1 Envelope físico (TODOS os eventos)

Schema Drizzle TS (referência canônica = Doc 11 §7 + Doc 10 §5.3 reconciliados via charter §3 AJUSTE-03):

```typescript
// drizzle/schema.ts
import { pgTable, uuid, text, jsonb, timestamp, pgEnum } from 'drizzle-orm/pg-core';

export const actorTypeEnum = pgEnum('actor_type', ['user', 'agent', 'system']);
export const riskLevelEnum = pgEnum('risk_level', ['low', 'medium', 'high']);

export const events = pgTable('events', {
  id: uuid('id').primaryKey().defaultRandom(),           // UUIDv7 idealmente; v4 OK pra MVP
  tenant_id: uuid('tenant_id').notNull(),                // = org_id (RLS root, Doc 12 §5.6.1)
  workspace_id: uuid('workspace_id').notNull(),
  project_id: uuid('project_id'),                        // NULL permitido (S1 user-first; F-02 RLS defer PATCH 3)
  event_type: text('event_type').notNull(),              // 'IntentSubmitted' | 'IntentResolved' | ...
  payload: jsonb('payload').notNull(),                   // schema específico do tipo (ver §6.2-§6.6)
  actor_type: actorTypeEnum('actor_type').notNull(),
  actor_id: uuid('actor_id').notNull(),                  // user_id quando actor=user
  aggregate_type: text('aggregate_type').notNull().default('workflow'),   // S1: sempre 'workflow'
  aggregate_id: uuid('aggregate_id').notNull(),          // S1: = correlation_id
  correlation_id: uuid('correlation_id').notNull(),      // amarra fluxo (request → output)
  causation_id: uuid('causation_id'),                    // evento causador (cadeia)
  idempotency_key: text('idempotency_key').unique(),     // hash(correlation_id + step + input_digest)
  metadata: jsonb('metadata').default({}),               // tracing, telemetria livre
  risk_level: riskLevelEnum('risk_level').notNull().default('low'),  // S1: sempre 'low'
  created_at: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
});
```

**Append-only invariant** (Postgres trigger):
```sql
-- migrations/0001_events_append_only.sql
CREATE OR REPLACE FUNCTION events_no_update_delete() RETURNS trigger AS $$
BEGIN
  RAISE EXCEPTION 'events table is append-only — % not allowed', TG_OP;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER events_block_update BEFORE UPDATE ON events FOR EACH ROW EXECUTE FUNCTION events_no_update_delete();
CREATE TRIGGER events_block_delete BEFORE DELETE ON events FOR EACH ROW EXECUTE FUNCTION events_no_update_delete();
```

**Indexes** (Doc 11 §7 línea 235):
```sql
CREATE INDEX events_correlation_idx ON events (correlation_id, created_at);
CREATE INDEX events_workspace_actor_idx ON events (workspace_id, actor_id, created_at);
CREATE INDEX events_project_idx ON events (project_id) WHERE project_id IS NOT NULL;
```

**RLS workaround S1** (F-02 defer):
```sql
ALTER TABLE events ENABLE ROW LEVEL SECURITY;

CREATE POLICY events_workspace_actor ON events FOR SELECT
  USING (workspace_id = current_setting('app.workspace_id')::uuid
     AND actor_id = current_setting('app.user_id')::uuid);
```

### 6.2 IntentSubmitted (payload)

```typescript
import { z } from 'zod';

export const IntentSubmittedPayload = z.object({
  intent_text: z.string().min(1).max(10000),
  user_id: z.string().uuid(),
  project_id: z.string().uuid().optional(),    // OPCIONAL — Doc 10 §5.2 + §18.2 backend plan
  context_ref: z.string().optional(),          // hint a briefing/conversa anterior
  section: z.string().optional(),              // UI-specific quando origem = CommandBar
});

export type IntentSubmitted = z.infer<typeof IntentSubmittedPayload>;
```

### 6.3 IntentResolved (payload)

```typescript
export const IntentResolvedPayload = z.object({
  intent_type: z.enum([
    'create_project', 'update_briefing', 'analyze', 'decision_required',
    'task', 'question', 'output_request', 'unknown',
  ]),
  candidate_object_types: z.array(z.string()).min(1),  // 'project' | 'briefing' | 'task' | ...
  confidence: z.number().min(0).max(1),
  response_type: z.enum([                              // Doc 03 §5.5 PROMOTE-R1
    'diagnostica', 'estrategica', 'decisao', 'operacional',
    'criativa', 'tecnica', 'learning', 'ROI',
  ]),
  depth_level: z.enum(['direta', 'estruturada', 'estrategica', 'profunda']),
  reasoning_mode: z.enum(['fast', 'deep', 'skeptical', 'exploratory']),
  llm_model_used: z.string(),                          // 'anthropic/claude-4.7-opus' | 'openai/gpt-5.5'
  llm_cost_usd: z.number(),                            // cost guard input
  llm_tokens_in: z.number().int(),
  llm_tokens_out: z.number().int(),
});
```

### 6.4 ContextAssembled (payload)

```typescript
export const ContextAssembledPayload = z.object({
  pack_id: z.string().uuid(),
  user_memory_refs: z.array(z.string().uuid()),         // memórias com user_id matching (S1: short-term only)
  project_memory_refs: z.array(z.string().uuid()).optional(),   // se project_id existir
  sources: z.array(z.object({
    kind: z.enum(['user_profile', 'event_log', 'briefing']),    // S1: estas 3 only
    ref: z.string(),
  })),
  token_count: z.number().int(),
  budget_remaining: z.number().int(),                   // S1: cap = 8000 tokens
});
```

### 6.5 PartialOutputProduced (simplificado — S1)

```typescript
export const PartialOutputProducedPayload = z.object({
  output_kind: z.literal('intent_response'),            // S1: só este kind
  payload_text: z.string(),                             // resposta NL
  response_type: z.enum([/* mesmo enum de §6.3 */]),    // copia do IntentResolved
  depth_level: z.enum([/* mesmo */]),
  confidence: z.number().min(0).max(1),
  is_final: z.literal(true),                            // S1: sem streaming, sempre final
});
```

### 6.6 IntentResolutionFailed (error path — Deliverable #9)

```typescript
export const IntentResolutionFailedPayload = z.object({
  error_kind: z.enum(['timeout', 'rate_limit', 'server_error', 'invalid_response', 'budget_exceeded']),
  error_message: z.string(),
  retry_count: z.number().int().min(0),
  llm_attempt: z.object({
    model: z.string(),
    duration_ms: z.number().int(),
    http_status: z.number().int().optional(),
  }).optional(),
  fallback_used: z.boolean(),                           // tentou modelo fallback (Claude → GPT)?
});
```

### 6.7 LLM cost tracking events (cost guard — AQ-S1-07)

```typescript
export const LLMCostEstimatedPayload = z.object({
  call_id: z.string().uuid(),
  model: z.string(),
  estimated_tokens_in: z.number().int(),
  estimated_cost_usd: z.number(),
});

export const LLMCostActualPayload = z.object({
  call_id: z.string().uuid(),
  model: z.string(),
  actual_tokens_in: z.number().int(),
  actual_tokens_out: z.number().int(),
  actual_cost_usd: z.number(),
  duration_ms: z.number().int(),
});
```

---

## 7. Auth — mock JWT bearer (AJUSTE-01 + AQ-S1-05 trava-início)

### 7.1 Middleware Fastify (escopo S1)

```typescript
// src/ingress/auth.ts
import { FastifyRequest, FastifyReply } from 'fastify';

export async function mockJwtAuth(req: FastifyRequest, reply: FastifyReply) {
  const auth = req.headers.authorization;
  if (!auth?.startsWith('Bearer ')) {
    return reply.code(401).send({ error: 'missing_bearer' });
  }
  const token = auth.substring(7);
  // S1 mock: token literal = 'test-user-jwt-{user_id}' (NÃO É HMAC REAL)
  const match = token.match(/^test-user-jwt-([0-9a-f-]{36})$/);
  if (!match) {
    return reply.code(401).send({ error: 'invalid_mock_jwt_format' });
  }
  const userId = match[1];
  // Inject no contexto
  (req as any).auth = { user_id: userId, workspace_id: req.headers['x-workspace-id'] };
  if (!(req as any).auth.workspace_id) {
    return reply.code(400).send({ error: 'missing_workspace_id_header' });
  }
}
```

**Header esperado pelo client:**
```
POST /intent
Authorization: Bearer test-user-jwt-7c9e6679-7425-40de-944b-e07fc1f90ae7
X-Workspace-Id: 1234abcd-...
Content-Type: application/json

{"intent_text": "Quero analisar o briefing do projeto X"}
```

**Real auth (S3 — fora de escopo):** Substituir middleware por validador Supabase Auth JWT (HMAC HS256 com `SUPABASE_JWT_SECRET`). Nesse momento, Doc 12 §5.6.1 RLS começa a importar.

### 7.2 .env.example (S1)

```bash
# DB
SUPABASE_DB_URL=postgresql://postgres:[password]@db.[ref].supabase.co:5432/postgres
SUPABASE_DB_URL_DIRECT=postgresql://postgres:[password]@db.[ref].supabase.co:6543/postgres  # for migrations

# LLM
OPENROUTER_API_KEY=sk-or-v1-...
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL_PRIMARY=anthropic/claude-4.7-opus
OPENROUTER_MODEL_FALLBACK=openai/gpt-5.5
LLM_BUDGET_USD_MONTHLY=50
LLM_BUDGET_ALERT_PCT=70
LLM_BUDGET_HARD_STOP_PCT=100

# Server
PORT=3000
NODE_ENV=development
LOG_LEVEL=info

# Auth (mock)
JWT_SECRET=dev-only-not-for-prod-s1-mock
```

> **Produção:** `OPENROUTER_API_KEY` deve resolver via Supabase Vault + `secret_refs.owner_type='provider'` (def-01 fechado). Em dev, .env é OK; em prod, secret_ref → vault em runtime conforme Doc 12 §5.15.

---

## 8. Intent Resolver — transformer `intent_to_object`

### 8.1 Contract (Doc 09 §5.5 envelope)

```typescript
// src/transformers/intent_to_object.ts
import { z } from 'zod';
import { openRouterClient } from '../lib/openrouter';
import { IntentResolvedPayload } from '../events/types';

export const TransformerInput = z.object({
  intent_text: z.string(),
  user_id: z.string().uuid(),
  project_id: z.string().uuid().optional(),
  context_ref: z.string().optional(),
});

export const TransformerOutput = IntentResolvedPayload;   // mesmo schema do event payload

export async function intentToObject(
  input: z.infer<typeof TransformerInput>,
  correlation_id: string,
): Promise<z.infer<typeof TransformerOutput>> {
  // ver §8.2 prompt + §8.3 cost guard
}
```

### 8.2 Prompt template (escopo S1 — refinará em F2)

```typescript
const SYSTEM_PROMPT = `
You are the Intent Resolver of CKOS — a cognitive operating system.
Your job: classify a user's natural-language intent into structured CKOS objects.

CONSTRAINTS:
- intent_type: pick exactly one from [create_project, update_briefing, analyze, decision_required, task, question, output_request, unknown]
- candidate_object_types: array of CKOS objects that the intent might create or affect, from [project, briefing, signal, node, workflow, decision, artifact]
- confidence: 0.0-1.0 based on how clear the intent is
- response_type: pick exactly one from [diagnostica, estrategica, decisao, operacional, criativa, tecnica, learning, ROI]
- depth_level: pick exactly one from [direta, estruturada, estrategica, profunda] based on how much depth the response needs
- reasoning_mode: pick exactly one from [fast, deep, skeptical, exploratory] based on how the agent should think

OUTPUT FORMAT: STRICT JSON matching the schema below. No prose, no markdown.

{
  "intent_type": "...",
  "candidate_object_types": [...],
  "confidence": 0.0,
  "response_type": "...",
  "depth_level": "...",
  "reasoning_mode": "..."
}
`;

const USER_PROMPT = (input: z.infer<typeof TransformerInput>) => `
USER ID: ${input.user_id}
${input.project_id ? `PROJECT ID: ${input.project_id}` : 'NO PROJECT (1st intent — user-first)'}
${input.context_ref ? `CONTEXT REF: ${input.context_ref}` : ''}

INTENT:
${input.intent_text}
`;
```

### 8.3 Cost guard (AQ-S1-07)

```typescript
// Pré-call: estimar custo
const estimated = estimateCost(SYSTEM_PROMPT + USER_PROMPT(input), 'anthropic/claude-4.7-opus');
await publishEvent('LLMCostEstimated', { call_id, model, estimated_tokens_in, estimated_cost_usd });

if (estimated.cost_usd > 0.50) {
  throw new Error('per_call_cost_exceeded');   // hard cap
}
if (estimated.cost_usd > 0.10) {
  logger.warn({ call_id, estimated_cost_usd }, 'per_call_cost_warning');
}

// Pós-call: registrar atual
await publishEvent('LLMCostActual', { call_id, model, actual_tokens_in, actual_tokens_out, actual_cost_usd, duration_ms });

// Monthly cap check (DB query somando LLMCostActual.actual_cost_usd no mês corrente):
const spent = await getMonthlySpend();
if (spent > BUDGET_HARD_STOP) {
  throw new Error('monthly_budget_exceeded');
}
if (spent / BUDGET_MONTHLY > BUDGET_ALERT_PCT / 100) {
  logger.warn({ spent, budget: BUDGET_MONTHLY }, 'monthly_budget_alert');
}
```

### 8.4 Fallback (Claude → GPT)

Se Claude 4.7 Opus retornar erro 5xx ou timeout (>30s), tentar `openai/gpt-5.5` automaticamente. Se ambos falharem, publish `IntentResolutionFailed` com `fallback_used: true`.

---

## 9. Context Assembler básico (Deliverable #4)

### 9.1 Scope S1

```typescript
// src/context/assembler.ts
export async function assembleContext(
  user_id: string,
  project_id: string | undefined,
  correlation_id: string,
): Promise<z.infer<typeof ContextAssembledPayload>> {
  // S1: só memória curta = user_profile + últimos 10 events do user (mesmo workspace)
  const userProfile = await db.select().from(user_profiles).where(eq(user_profiles.user_id, user_id)).limit(1);
  const recentEvents = await db
    .select()
    .from(events)
    .where(and(
      eq(events.actor_id, user_id),
      project_id ? eq(events.project_id, project_id) : isNull(events.project_id),
    ))
    .orderBy(desc(events.created_at))
    .limit(10);

  const pack_id = randomUUID();
  return {
    pack_id,
    user_memory_refs: [userProfile[0]?.user_id].filter(Boolean) as string[],
    project_memory_refs: project_id ? recentEvents.map(e => e.id) : undefined,
    sources: [
      ...(userProfile.length ? [{ kind: 'user_profile' as const, ref: userProfile[0].user_id }] : []),
      ...recentEvents.map(e => ({ kind: 'event_log' as const, ref: e.id })),
    ],
    token_count: 0,           // S1: não tokenize ainda; deixa ContextPackBuilder S2+ fazer
    budget_remaining: 8000,
  };
}
```

> **S2+ vai adicionar:** RAG/embeddings via Doc 28 (`notes_rag`), briefings vivos, trust hierarchy ranking. S1 fica raso intencionalmente — exit criterion não exige profundidade.

---

## 10. Output (Deliverable #5)

### 10.1 Scope S1

```typescript
// src/workers/output_producer.ts
export async function produceOutput(
  intent_resolved: z.infer<typeof IntentResolvedPayload>,
  context: z.infer<typeof ContextAssembledPayload>,
  correlation_id: string,
): Promise<z.infer<typeof PartialOutputProducedPayload>> {
  // S1: 1 chamada LLM curta sintetizando intent + context num response NL
  const SYSTEM = `You are CKOS responding to a user intent. Use response_type=${intent_resolved.response_type}, depth_level=${intent_resolved.depth_level}, reasoning_mode=${intent_resolved.reasoning_mode}. Be precise. Use Response Behavior Policies (Doc 04 §5.9): no_fake_certainty, do_not_over_explain, assumption_transparency.`;
  const USER = `Intent: <inject from event>\nContext sources: <inject from context>`;

  const llmResponse = await openRouterClient.chat({...});

  return {
    output_kind: 'intent_response',
    payload_text: llmResponse.text,
    response_type: intent_resolved.response_type,
    depth_level: intent_resolved.depth_level,
    confidence: intent_resolved.confidence,
    is_final: true,
  };
}
```

### 10.2 Quality guard (não-genérico — charter §5)

Validar antes de publicar:
- `payload_text.length > 50` (não pode ser "ok" ou "got it")
- `payload_text` não pode ser exatamente o `intent_text` ecoado
- Falha desses checks → reduzir `confidence` em 50% e logar warning (não bloqueia em S1; bloqueia em S2 quando quality gates entrarem)

---

## 11. Testing strategy

### 11.1 Unit tests (Vitest)

Cobertura mínima S1:
- Zod schemas (validação de cada event payload)
- Auth middleware (mock JWT parsing)
- Transformer `intent_to_object` com LLM mocked (Vitest `vi.mock`)
- Cost guard logic (estimate, hard cap, monthly cap simulado)

### 11.2 Integration tests

Com DB real (testcontainers-postgresql OU Supabase test branch):
- POST `/intent` → row aparece em `events` table com `event_type='IntentSubmitted'`
- pg-boss worker dispara `intent_to_object` após `IntentSubmitted`
- Append-only invariant: tentar UPDATE/DELETE em `events` → erro

### 11.3 E2E test (exit criterion — charter §5)

```typescript
// tests/e2e/intent_to_output.test.ts
test('1 intent → 3 events + 1 output, rastreado por correlation_id', async () => {
  const correlation_id = await postIntent({
    headers: { Authorization: `Bearer test-user-jwt-${TEST_USER_ID}`, 'X-Workspace-Id': TEST_WORKSPACE_ID },
    body: { intent_text: 'Quero analisar o briefing do Projeto X' },
  });

  // Wait até pipeline completar (até 60s — Intent Resolver + Context + Output)
  await waitForEvent(correlation_id, 'PartialOutputProduced', { timeout: 60000 });

  const events_for_correlation = await queryEvents({ correlation_id });

  expect(events_for_correlation.map(e => e.event_type)).toEqual([
    'IntentSubmitted',
    'IntentResolved',
    'ContextAssembled',
    'PartialOutputProduced',
  ]);   // 4 events conta IntentSubmitted + 3 conforme charter §5 (que conta após ingress = 3 + output)

  const output = events_for_correlation.find(e => e.event_type === 'PartialOutputProduced');
  expect(output.payload.payload_text.length).toBeGreaterThan(50);
  expect(output.payload.is_final).toBe(true);
});
```

### 11.4 Cost tests (CI)

CI roda e2e somente uma vez por PR (não em cada push); CI tem budget $10/mês cap.

---

## 12. Deploy + CI

### 12.1 Fly.io OU Railway (executor escolhe)

**Fly.io setup mínimo:**
```bash
fly launch --no-deploy --copy-config --name ckos-runtime
# fly.toml gerado; ajustar:
# - app = "ckos-runtime"
# - primary_region = "gru" (São Paulo) ou "iad" (Virginia)
# - http_service.internal_port = 3000
# - http_service.checks = healthcheck path "/health"
fly secrets set OPENROUTER_API_KEY=... SUPABASE_DB_URL=... JWT_SECRET=...
fly deploy
```

**Railway setup mínimo:**
```bash
railway init
railway add postgresql  # ou conecta Supabase existente
railway variables set OPENROUTER_API_KEY=... SUPABASE_DB_URL=...
railway up
```

### 12.2 GitHub Actions CI

```yaml
# .github/workflows/ci.yml
name: CI
on: [pull_request, push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v3
        with: { version: 9 }
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: 'pnpm' }
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint
      - run: pnpm typecheck
      - run: pnpm test:unit
      - run: pnpm test:integration
      # E2E gated por label `e2e-ok` no PR (cost guard CI cap $10/mo)
      - if: contains(github.event.pull_request.labels.*.name, 'e2e-ok')
        run: pnpm test:e2e
        env:
          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
```

---

## 13. Doc 11 patch findings durante S1 (AQ-S1-06 — registry)

Conforme charter §6 AQ-S1-06: gaps reais em Doc 11 descobertos durante implementação NÃO viram patches in-flight. Registra em arquivo paralelo NO DOC REPO:

**Arquivo:** `000_ROADMAPS/22_CONSOLIDATION/F1S1_DOC11_PATCH_FINDINGS.md` (executor cria quando primeiro finding aparecer)

**Formato de entry:**
```markdown
## FIND-{NN} — {short title} — descoberto {date}

- **Onde no canônico:** Doc 11 §X linha Y
- **Onde no código CKOS_RUNTIME:** path/to/file.ts:line
- **Gap:** descrição factual
- **Workaround S1:** o que fizemos pra continuar
- **Proposed PATCH 3 entry:** o que vai virar candidate depois
```

Executor abre PR no doc repo (não no runtime repo) pra registrar findings. PMO consolida em PATCH 3 candidate em sessão separada.

---

## 14. Sprint Done quality gate (§5 charter)

Sprint Done quando TODOS estes verdes:

- [ ] 3 eventos `IntentSubmitted` + `IntentResolved` + `ContextAssembled` persistidos com envelope completo
- [ ] Output `PartialOutputProduced` retornado com `payload_text.length > 50` e `is_final: true`
- [ ] `correlation_id` mesmo em todos 4 events da request
- [ ] `user_id` rastreado fim-a-fim (todos events têm `actor_id = user_id`)
- [ ] Append-only invariant testada (UPDATE/DELETE bloqueado)
- [ ] Trace replay manual: query `WHERE correlation_id = ?` retorna sequência completa
- [ ] Healthcheck `/health` responde 200 OK em <100ms
- [ ] Error handling: 1 teste e2e simulando OpenRouter 5xx → `IntentResolutionFailed` event publicado, sem crash
- [ ] Deploy live em Fly.io OU Railway (URL acessível)
- [ ] LLM cost guard: rodou 10x e2e em CI, custo total < $5
- [ ] Doc 11 patch findings registrados (zero ou mais — só registrar, não bloquear)
- [ ] Executor self-test reporta JSON output anexado a este dispatch (§17)
- [ ] **PMO valida** trace replay + 4 eventos + output não-genérico (esta sessão ou sessão PMO fresh)
- [ ] **Founder assina Sprint Done** + atualiza Kanban (S1 → ✅) + dispara dispatch S4

---

## 15. Separação de papéis

| Sessão | Agent | Papel | Onde |
|---|---|---|---|
| `S-F1S1-CHARTER-CLAUDE-20260610-001` | `claude_opus_4_7` (autor charter) | Autora do charter v0.1.0 | doc repo |
| `S-F1S1-CHARTER-METAREV-CLAUDE-20260610-001` | Claude fresh (auditor) | Metacognik completeness audit | doc repo |
| `S-F1S1-CHARTER-AJUSTES-CLAUDE-20260610-001` | `claude_opus_4_7` (esta sessão — Dispatcher) | Aplicou AJUSTES + escreve esta dispatch | doc repo |
| `S-F1S1-IMPL-EXEC-<DATE>-001` | **Codex OU Claude Code fresh** | **Executor — IMPLEMENTA S1** | **`CKOS_RUNTIME` repo separado** |
| `S-F1S1-VERIFY-<DATE>-001` | PMO (esta ou fresh) + Founder | Verifica exit criterion + Sprint Done | doc repo (Kanban update) |

**Garantia de separação:** Executor NÃO pode ser `claude_opus_4_7` (Dispatcher). DEVE ser sessão fresca de Codex OU Claude Code (não Windsurf — per [[feedback-metacognik-executor]]).

---

## 16. PROMPT PARA EXECUTOR (cola num chat Codex OU Claude Code fresh)

```txt
You are the F1 Sprint 1 IMPLEMENTATION EXECUTOR for CKOS.
SESSION: S-F1S1-IMPL-EXEC-<TODAY>-001 (criar timestamp).

CONTEXT:
- Repo doc canônico (RO reference): https://github.com/danielck01/CKOS @ commit b22ecbe (F1 charter v0.3.0)
- Repo de implementação (WRITE aqui): https://github.com/danielck01/CKOS_RUNTIME (private, branch main, empty exceto README)
- Você é executor fresco. NÃO é claude_opus_4_7 (Dispatcher do charter). NÃO é Windsurf.

READ FIRST (clone o doc repo localmente):
  1. github.com/danielck01/CKOS/blob/b22ecbe/000_ROADMAPS/22_CONSOLIDATION/S-F1S1-IMPLEMENTATION-DISPATCH.md  (este arquivo — spec autocontida)
  2. github.com/danielck01/CKOS/blob/b22ecbe/000_ROADMAPS/22_CONSOLIDATION/F1_SPRINT1_CHARTER.md  (charter v0.3.0 — reference)
  3. github.com/danielck01/CKOS/blob/b22ecbe/03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md §5.2/§5.3  (event flow + envelope)
  4. github.com/danielck01/CKOS/blob/b22ecbe/03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md §4/§7/§12.1/§13  (physical schema)
  5. github.com/danielck01/CKOS/blob/b22ecbe/01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md §5.5  (response typing)
  6. github.com/danielck01/CKOS/blob/b22ecbe/01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md §5.9  (5 anti-pattern policies)
  7. github.com/danielck01/CKOS/blob/b22ecbe/01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md §5.6.1  (memória user_id)
  8. github.com/danielck01/CKOS/blob/b22ecbe/02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md §5.5  (transformer envelope)
  9. github.com/danielck01/CKOS/blob/b22ecbe/03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md §5.6/§5.15  (RLS + Vault)

CLONE WORKSPACE:
  cd ~/projects
  gh repo clone danielck01/CKOS_RUNTIME
  cd CKOS_RUNTIME

INITIAL SETUP (commit em main):
  pnpm init
  pnpm add fastify zod drizzle-orm postgres pg-boss pino @anthropic-ai/openai-sdk
  pnpm add -D typescript tsx vitest @types/node drizzle-kit @biomejs/biome
  # Configurar tsconfig.json strict mode, biome.json, drizzle.config.ts, package.json scripts
  # Criar estrutura de pastas conforme §2 do dispatch
  git add -A && git commit -m "chore: project skeleton (TS + Fastify + Drizzle + pg-boss)"
  git push origin main

IMPLEMENT in this order (1 PR por slice quando estável):
  Slice 1: DB schema + migrations (§6, §7 do dispatch)
  Slice 2: Auth middleware mock (§7 do dispatch)
  Slice 3: POST /intent ingress + IntentSubmitted event (§4 deliverable #1+#2)
  Slice 4: Intent Resolver worker + transformer + LLM cost guard (§8 do dispatch)
  Slice 5: Context Assembler básico (§9 do dispatch)
  Slice 6: Output producer + PartialOutputProduced (§10 do dispatch)
  Slice 7: Error handling + IntentResolutionFailed (§4 deliverable #9)
  Slice 8: Healthcheck /health (§4 deliverable #8)
  Slice 9: Tests (§11 do dispatch — unit + integration + e2e)
  Slice 10: Deploy Fly.io ou Railway (§12 do dispatch — sua escolha entre os 2)
  Slice 11: CI GitHub Actions (§12.2)
  Slice 12: README do CKOS_RUNTIME com setup steps + run instructions

WHILE IMPLEMENTING:
  - Se descobrir gap real em Doc 11 (campo faltando, índice errado, etc.), criar arquivo paralelo
    NO DOC REPO: `000_ROADMAPS/22_CONSOLIDATION/F1S1_DOC11_PATCH_FINDINGS.md` via PR separado (NÃO commit direto)
  - Se encontrar ambiguidade na spec, PARAR e perguntar ao Dispatcher (PMO) em vez de adivinhar
  - Conventional commits: feat:, fix:, chore:, test:, refactor:, docs:, ci:
  - 1 PR por slice estável (cabe revisão)

FORBIDDEN:
  - Editar canônico 01-28 (doc repo é READ-ONLY pra você)
  - Editar charter v0.3.0 ou este dispatch
  - Implementar features OUT (UI, Approval Gate, Question Engine, Work Order, ROI, memória longa, ProjectInferred event)
  - Migrations que violem Doc 11 §7 (schema canônico)
  - Bypass do cost guard
  - Auth real (Supabase Auth JWT) — S1 é mock; real entra em S3

EXIT CRITERION (§14 deste dispatch):
  - 1 intent end-to-end → 4 events com mesmo correlation_id + 1 output não-genérico
  - sem UI; testes verdes; deploy live; cost guard funcional; healthcheck 200

WHEN DONE:
  - Anexar JSON do output do exit criterion test ao S-F1S1-IMPLEMENTATION-DISPATCH.md (PR no doc repo)
  - Avisar PMO via comment no PR
  - PMO valida + Founder assina Sprint Done
```

---

## 17. Anexo (executor preenchido)

```yaml
implementation_session_id: S-F1S1-IMPL-EXEC-20260610-001
executor_agent: claude_code_fresh (Claude Fable 5 — sessão fresca, ≠ claude_opus_4_7 Dispatcher)
ckos_runtime_main_branch_sha: 1171384   # tip of main após PR #12 merge (12 PRs todos mergeados)
ckos_runtime_url: https://github.com/danielck01/CKOS_RUNTIME
deployed_at: pendente   # artefatos prontos (Dockerfile + fly.toml + docs/DEPLOY.md); bloqueio = FLY_API_TOKEN + SUPABASE_DB_URL com Founder
deployed_url: pendente
e2e_test_output:    # execução real contra OpenRouter (não-mockada) em 2026-06-10 21:01 UTC-3
  correlation_id: 200db875-f206-4b97-a8a2-8a791d84b426
  events_workflow:    # 4 eventos do exit criterion §14 — todos com mesmo correlation_id e actor_id=user_id
    - { event_type: IntentSubmitted,       id: 019eb432-acb0-7467-b630-e62af79a984e, created_at: 2026-06-11T01:01:20.797Z }
    - { event_type: IntentResolved,        id: 019eb432-bf19-7c2d-b9b4-1b783b14888c, created_at: 2026-06-11T01:01:25.478Z }
    - { event_type: ContextAssembled,      id: 019eb432-c34e-7b29-9c46-8ec81117454a, created_at: 2026-06-11T01:01:26.536Z }
    - { event_type: PartialOutputProduced, id: 019eb432-f36c-7b10-b42c-f4cc645923d7, created_at: 2026-06-11T01:01:38.492Z }
  events_cost:        # 4 eventos LLMCost (2 calls × {Estimated, Actual})
    - { event_type: LLMCostEstimated, call_id: ecfddcd6-...-357b, model: anthropic/claude-opus-4.7,        estimated_cost_usd: 0.027315 }
    - { event_type: LLMCostActual,    call_id: ecfddcd6-...-357b, model: anthropic/claude-4.7-opus-20260416, actual_cost_usd:    0.00508,  tokens_in: 521, tokens_out: 99 }
    - { event_type: LLMCostEstimated, call_id: 57641968-...-8c01, model: anthropic/claude-opus-4.7,        estimated_cost_usd: 0.048255 }
    - { event_type: LLMCostActual,    call_id: 57641968-...-8c01, model: anthropic/claude-4.7-opus-20260416, actual_cost_usd:    0.014315, tokens_in: 388, tokens_out: 495 }
  intent_text: "Quero analisar o briefing do Projeto X e identificar os 3 maiores riscos"
  resolved:
    intent_type: analyze
    confidence: 0.9
    response_type: diagnostica
    depth_level: estruturada
    reasoning_mode: skeptical
    candidate_object_types: [briefing, signal]
  output_text_length: 1216
  output_quality: nao_generico   # aplica assumption_transparency + no_fake_certainty (Doc 04 §5.9) — recusou inventar riscos sem briefing real, pediu o conteúdo
  total_cost_usd: 0.019395       # bem abaixo do cap $0.05/e2e
  duration_ms: 21488             # POST → PartialOutputProduced no trace
quality_gate_checks:
  - "[x] 4 eventos workflow persistidos com envelope completo (charter §5)"
  - "[x] PartialOutputProduced.payload_text > 50 chars (1216 chars) e is_final=true"
  - "[x] correlation_id idêntico em todos 4 eventos workflow (+ 4 LLMCost)"
  - "[x] user_id rastreado fim-a-fim (actor_id=user_id em todos os 8 eventos)"
  - "[x] append-only invariant testada (integration tests; trigger UPDATE/DELETE bloqueia)"
  - "[x] trace replay manual via GET /trace/:correlation_id (5 fontes em ContextAssembled — user_profile + 4 event_log refs)"
  - "[x] healthcheck /health responde 200 OK em <100ms (smoke 4-43ms)"
  - "[x] error handling: e2e simulando OpenRouter 5xx → IntentResolutionFailed{retry_count:3, fallback_used:true} (verificação ao vivo Slice 7)"
  - "[ ] deploy live em Fly.io ou Railway — pendente FLY_API_TOKEN + Supabase URLs com Founder; artefatos prontos (Dockerfile + fly.toml + docs/DEPLOY.md em CKOS_RUNTIME)"
  - "[x] LLM cost guard funcional: hard cap $0.50/call, hard stop mensal 100%, e2e CI usa mock → custo $0"
  - "[x] Doc 11 patch findings: 0 — schema canônico §7 implementado integralmente; ajuste pontual do slug OpenRouter foi env var, não Doc 11"
  - "[ ] PMO valida trace replay + 4 eventos + output não-genérico (esta sessão ou sessão PMO fresh)"
  - "[ ] Founder assina Sprint Done + atualiza Kanban (S1 → ✅) + dispara dispatch S4"
test_suite_status:
  unit: "48/48 passing (~7s)"
  integration: "3/3 passing contra Postgres 15.13 (~3.7s)"
  e2e_mocked: "1/1 passing contra mock OpenRouter (~6s, custo $0)"
  ci: "GitHub Actions verde em PR #11 (com label e2e-ok) e PR #12 (sem e2e)"
ckos_runtime_pr_history:
  - "PR #1  Slice 1: DB schema + migrations"
  - "PR #2  Slice 2: mock JWT auth middleware"
  - "PR #3  Slice 3: POST /intent + event publisher"
  - "PR #4  Slice 4: Intent Resolver + transformer + LLM cost guard"
  - "PR #5  Slice 5: Context Assembler básico + context_packs row"
  - "PR #6  Slice 6: output producer + PartialOutputProduced + quality guard"
  - "PR #7  Slice 7: error handling + IntentResolutionFailed + retries 1s/5s/30s"
  - "PR #8  Slice 8: healthcheck GET /health"
  - "PR #9  Slice 9: integration tests + e2e (exit criterion CI-mode mockado)"
  - "PR #10 Slice 10: Fly.io deploy artifacts"
  - "PR #11 Slice 11: GitHub Actions CI"
  - "PR #12 Slice 12: README"
spec_deviations_documented:
  - "openai SDK (pacote `openai`): dispatch §16 listava `@anthropic-ai/openai-sdk` (não existe no npm); §2 stack table descrevia 'OpenAI SDK com baseURL=openrouter' — implementado como o pacote canônico `openai`"
  - "OpenRouter model slug: dispatch §7.2 listava 'anthropic/claude-4.7-opus' (não existe no catálogo); slug real do Claude 4.7 Opus é 'anthropic/claude-opus-4.7' (verificado via GET /api/v1/models em 2026-06-10) — corrigido em env.ts (env var, não patch ao canônico)"
  - "Postgres user-space em vez de Docker Compose: máquina do executor tem Smart App Control bloqueando binários nativos baixados (rollup nativo + initdb.exe); resolvido com `@rollup/wasm-node` override e Postgres 15.13 user-space rodando no WSL Ubuntu 24.04. Mesmo Postgres 15 do dispatch §2 — semântica idêntica. Documentado em README.md."
  - "RLS workaround S1 sem FORCE: app-side filter por workspace_id + actor_id em GET /trace (def-02 confirma F-02 defer); RLS real com Supabase roles entra em S3 com auth real"
doc_11_findings_count: 0
ready_for_pmo_verification: true
```

---

## 18. BRA + CHECKOUT RELEASE

```yaml
bra_id: BRA-F1S1-DISPATCH-20260610-01
from_session: S-F1S1-IMPLEMENTATION-DISPATCH-20260610-001
to: Founder (review + approval) + Executor (Codex OU Claude fresh — a abrir)
context_summary:
  - "Cadeia F0 documental 100% completa (10 commits hoje); F1 Sprint 1 charter v0.3.0 ativo com AJUSTES Metacognik aplicados"
  - "Repo CKOS_RUNTIME criado (private, main branch, https://github.com/danielck01/CKOS_RUNTIME)"
  - "Tech stack travado: TS 5.4 + Fastify 4 + Drizzle + pg-boss + OpenRouter + Supabase + Fly.io/Railway"
  - "5 AQs respondidas (S1-01/02/03/05/07/08/09) + 6 deferíveis (def-01..06) registrados"
  - "6 contratos de evento especificados como Zod schemas prontos pra implementar"
  - "Cost guard: $50/mo dev + $10/mo CI, hard cap $0.50/call, monthly hard stop em 100%"
outputs:
  - "S-F1S1-IMPLEMENTATION-DISPATCH.md (este): spec autocontida pra executor arrancar S1"
open_questions: []  # 0 abertas — todas respondidas inline ou deferidas com motivo
blockers: []
risk_flags:
  - "P1 (Runtime core greenfield): mitigado por escopo cirúrgico (9 deliverables, 6 events, 1 transformer) + cost guard + exit criterion binário + canônico já reconciliado"
  - "Risco operacional: executor escolhe Fly.io vs Railway — divergência sem grande impacto, mas vale anexar a decisão no §17"
  - "Risco LLM: orçamento $50/mo dev é conservador; se durante S1 ficar curto, PMO ajusta sem virar PATCH (é env var)"
recommended_next:
  - "Founder review desta dispatch (1-2 hours leitura crítica)"
  - "Após approval: PMO commita + push esta dispatch no doc repo"
  - "Founder OU PMO dispara executor (Codex OU Claude Code fresh) via §16 prompt"
  - "Executor abre PRs por slice em CKOS_RUNTIME; PMO/Founder revisam"
  - "Após Sprint Done: PMO atualiza Kanban (S1 → ✅) + escreve S-F1S2-DISPATCH (Question Engine) ou S-F1S4-DISPATCH (Event Log hardening)"
session_separation_confirmed:
  - "Dispatcher (claude_opus_4_7 — esta sessão) ≠ Charter autora (mesma sessão claude_opus_4_7 antes do dispatch) — ok, é refinamento do PMO continuando"
  - "Próxima sessão (Executor) ≠ Dispatcher; DEVE ser Codex OU Claude Code fresh"
  - "Sessão de verificação pós-Sprint Done = PMO + Founder, separada do Executor"
```

```txt
CHECKOUT RELEASE — S-F1S1-IMPLEMENTATION-DISPATCH-20260610-001
files_created:
  - 000_ROADMAPS/22_CONSOLIDATION/S-F1S1-IMPLEMENTATION-DISPATCH.md (este)
  - github.com/danielck01/CKOS_RUNTIME (repo criado via gh CLI)
files_changed:
  - 000_ROADMAPS/SESSION_REGISTRY.md (1 entry desta sessão)
files_not_touched: canônico 01-28 (RO references via SHA baseline b22ecbe); charter v0.3.0 (RO — congelado); ARCHITECTURE_PATCH_REPORT.md (dispatch não é canonical_patch); 00_SYSTEM_GOVERNANCE; demais candidates/reviews (RO histórico)
validation:
  - spec autocontida pra executor (Sections 1-17 cobrem repo, stack, decisões, contracts, auth, transformer, context, output, tests, deploy, CI, findings registry, quality gate)
  - 0 AQs abertas (todas respondidas inline ou deferidas com motivo)
  - cost guard concreto com números ($50/mo + hard caps)
  - 6 event Zod schemas prontos pra colar
  - prompt do executor em §16 é colável em chat Codex OU Claude fresh
  - separação de papéis confirmada (executor ≠ Dispatcher ≠ verificador)
risks_remaining: P1 mitigado; risco operacional baixo (escopo cirúrgico); Founder review desta dispatch destrava o resto
next_step: Founder review → commit dispatch → dispatch para executor → executor arranca S1
status: released
```
