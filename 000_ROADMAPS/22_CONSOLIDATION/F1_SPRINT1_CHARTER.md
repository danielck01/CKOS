---
title: F1 Sprint 1 — Intent Ingress Charter (PMO planning)
file: F1_SPRINT1_CHARTER.md
layer: auxiliary
doc_type: pmo_sprint_charter
phase: 000_ROADMAPS
category: consolidation
status: metacognik_approved_ajustes_applied
version: 0.3.0
created_at: 2026-06-10
founder_decisions_at: 2026-06-10
metacognik_audit_at: 2026-06-10
ajustes_applied_at: 2026-06-10
owner: pmo_ckos
responsible_agent: claude_opus_4_7
session_id: S-F1S1-CHARTER-CLAUDE-20260610-001
derives_from:
  - F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md      # fan-in F1 (PROMOTE-U1/U2/R1/R2 ALTA já aplicados)
  - 03_BACKEND_MVP_THIN_SLICE_PLAN.md                         # §3 backend-antes-de-UI, §9 exit criterion S1, §14 ordem dos sprints, §18 user-first reframe
  - GATE5_FOUNDER_DECISION_PACKAGE.md                         # §7 (pg-boss/OpenRouter/Vault) + §8 (decisão GO + AQ-IO-1 = user)
  - 01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md            # §5.2 User canônico (PATCH 2)
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md  # §5.6.1 memória user_id (PATCH 2)
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md       # §5.2 IntentSubmitted reconciliado (PATCH 2.5)
  - 04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md       # §5.1 Command Center alinhado (PATCH 2.5 PL-01)
companion_of:
  - PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md                  # precondition aplicado (commit 5d1d969)
  - PATCH2_5_INTENT_SUBMITTED_RECONCILIATION_CANDIDATE.md     # precondition aplicado (commit 79d66e1)
target_canonical: []                                          # charter NÃO edita canônico 01-28; é planning artifact
approval_required:
  - founder
  - metacognik
non_authority_boundary: >
  Planning artifact PMO. Define o ESCOPO operacional do Sprint 1 (Intent Ingress). NÃO edita canônico 01-28
  (nada de PATCH); NÃO escreve código; NÃO toca SQL/UI/agentes runtime; NÃO move/arquiva UPGRADE. A
  implementação real é uma sessão SEPARADA (executor a definir conforme AQ-S1-01 — repo de implementação).
  Cadeia de chaves: Founder ✅ via GATE 5 (já dada para a fase F1 em si) + Metacognik (audit de
  completeness/coerência do charter — não 2ª chave de canonical_patch).
tags: [planning, sprint-charter, f1, sprint-1, intent-ingress, runtime, pmo, post-patch-2-5, post-gate-5]
---

# F1 Sprint 1 — Intent Ingress Charter

> **O que é:** charter PMO que define o **escopo executável** do Sprint 1 (Intent Ingress) — primeira fatia operacional do runtime CKOS, agora destravada pelo PATCH 2 + 2.5.
> **O que não é:** não é spec de código, não é canonical_patch, não é dispatch de implementação. É o documento de alinhamento que precede a sessão de implementação.

---

## 0. Veredito em uma linha (PMO, direto)

Sprint 1 entrega **um endpoint de ingress backend que aceita uma intenção, persiste `IntentSubmitted{user_id, intent_text, project_id?, ...}` no event log, resolve a intenção via Intent Resolver, monta Context Packet mínimo, e gera 1 output simples rastreável por `correlation_id` — sem UI**.

---

## 1. Precondições satisfeitas (cadeia documental completa)

| Item | Status | Commit |
|---|---|---|
| GATE 5 = GO + AQ-IO-1 = `user` (Founder) | ✅ 2026-06-09 | `1b13f2c` |
| PATCH 2 aplicado (User canônico + memória user_id + response typing + 5 anti-pattern policies) | ✅ 2026-06-09 | `5d1d969` |
| PATCH 2.5 aplicado (IntentSubmitted reconciliação Doc 10 §5.2 + Doc 15 §5.1) | ✅ 2026-06-09 | `79d66e1` |
| Decisões técnicas GATE 5 (pg-boss + OpenRouter + Supabase Vault) | ✅ | GATE5 §7 |
| F1 candidate fan-in (PROMOTE-U1/U2/R1/R2 todos no canônico) | ✅ | F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md |

**Nenhuma precondição pendente.** Sprint 1 pode arrancar tecnicamente assim que executor + repo forem definidos (AQ-S1-01/02 em §6).

---

## 2. Escopo do Sprint 1

### 2.1 ENTRA (cirúrgico — não negocie durante implementação)

| # | Deliverable | Anchor canônico |
|---|---|---|
| 1 | **Endpoint de ingress backend** (HTTP/queue) que aceita 1 intenção autenticada | Doc 10 §5.2 passo 1 (`Ingress (CommandBar \| backend API \| webhook)`) |
| 2 | **Event Log mínimo** (tabela `event` append-only, schema canônico) capaz de persistir `IntentSubmitted` com envelope completo (`workspace_id`, `correlation_id`, `occurred_at`, `actor`) | Doc 10 §5.3 linha 98 |
| 3 | **Intent Resolver** (classifica intent → `candidate_object_types[]` + confidence) usando 1 transformer `intent_to_object` via LLM | Doc 10 §5.2 passo 2 + §18.2 do backend plan |
| 4 | **Context Assembler básico** (monta `ContextAssembled{user_id, user_memory_refs[], project_memory_refs[]?}`) — só memória curta MVP | Doc 10 §5.2 passo 3 + Doc 05 §5.6.1 (escopo user_id já canônico) |
| 5 | **1 output simples rastreável** (resposta texto, sem render UI; só JSON com `correlation_id` + payload) | Doc 10 §5.2 passo 8 (`PartialOutputProduced`) — modo simplificado |
| 6 | **Tracing end-to-end** por `correlation_id` único da intenção até o output | Doc 10 §5.3 + §13 EVALS observability |
| 7 | **DB migrations** para `events`, `users`, `user_profiles`, `context_packs` (schemas conforme Doc 11 §4/§7/§13) — *deliverable operacional que sustenta os 6 cognitivos acima* | Doc 11 §4 (`users`/`user_profiles` linhas 139-148), §7 (`events` linhas 217-232), §13 (`context_packs` linha 439) |
| 8 | **Healthcheck endpoint** `GET /health` (200 OK + DB ping) — exigido por Fly.io/Railway para roteamento | implícito do tech stack §4 (Fly.io/Railway) |
| 9 | **Error handling mínimo do Intent Resolver** — falha OpenRouter (timeout/429/5xx) emite evento `IntentResolutionFailed{correlation_id, error_kind, retry_count}` ao invés de explodir; trace replay (Doc 10 §5.26) continua coerente em modo falha | Doc 10 §5.6 (Run Scheduler retry/timeout/dead-letter) — modo simplificado para S1 |

> **Nota AJUSTE-02 (Metacognik audit 2026-06-10):** deliverables 7-9 são **operacionais** — sustentam os 6 cognitivos acima sem alterar o veredito §0 ("intent → 3 events + 1 output"). DB migrations materializam o event log (#2), healthcheck atende ao deploy stack (#1), error handling preserva o tracing (#6) em modo de falha LLM. Sem eles, o exit criterion §5 não é composivel.

### 2.2 NÃO ENTRA (motivos explícitos — defer para sprints posteriores)

| Item | Defer para | Motivo |
|---|---|---|
| UI / CommandBar | F4 (Product System rollout) | `§3` backend-antes-de-UI; `§9` exit criterion explicitamente diz "sem UI" |
| Approval Gate / Policy Engine completo | **S3** | §14 ordem dos sprints; S3 = Registry agentes/skills + policy + approval gates |
| Question Engine / score de clareza | **S2** | Kanban F1 |
| Work Order + Agent Run end-to-end | **S5** | AQ-G5-01/04 ainda abertas; Work Order modeling depende delas |
| Feedback + Memória longa + ROI | **S6** | AQ-G5-06/07/08 abertas; memória longa precisa de telemetria |
| Os 4 agentes MVP (Cognik / PM / Risk / ROI) completos | **S5/S6** | Sprint 1 usa um workflow mínimo, não orquestração completa |
| `ProjectInferred{user_id, project_id, source_intent_id}` event | **S2** | §18.2 backend plan: "Cognik decide se output desta intenção JUSTIFICA criar project_id"; S2 com Question Engine pode decidir |
| Doc 11 `users` enrichment (PATCH 2 fields: `operating_dna_ref?`, `tribes_scored?`, etc.) | **PATCH 3** | §31 PATCH_REPORT explícito; S1 roda com `users.id` + `user_profiles.preferences` |
| F-01 / F-02 / F-03 (Doc 10/12 cleanups) | **PATCH 3** | Metacognik review PATCH 2.5 §1 defer; nenhum bloqueia S1 |
| Multi-tenant RLS para events com `project_id IS NULL` (F-02) | **PATCH 3** | Doc 11 §7 já comporta `project_id NULL`; policy escrita defer |
| U3/U4/U5/R3/R4/R5 (MÉDIA do F1 candidate) | **PATCH 3 / sprints 2-3** | F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md §3 + PATCH 2 candidate §1 |
| Cognitive Atmosphere / glass / wallpaper / brand whitelabel | **F4** | F1 candidate §5 |

### 2.3 PROIBIDO (durante Sprint 1)

- Criar `/CKOS_USER_SYSTEM/` ou qualquer pasta de sistema nova
- Schemas SQL fora do que `11_DATA_MODEL` já define (tabelas: `events`, `users`, `user_profiles`, `workspaces`, `projects`, `context_packs`)
- Smart Response Engine docs 01-07 (duplica Doc 10 §5.2)
- Banco de 100 smart questions (7-12 amarradas ao S1/S2 bastam)
- Qualquer "personagem IA com nome bonito sem skill contratada" (Constituição §1, `00_TAXONOMY §7.4`)

---

## 3. Contratos de eventos (cite, não duplique)

**Fonte canônica única (pós-PATCH 2.5):** `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md §5.2`

S1 implementa **apenas os 3 primeiros eventos** do fluxo de 14 passos:

```
1. IntentSubmitted     → Doc 10 §5.2 (Ingress multi-source; user_id REQUIRED; project_id?)
2. IntentResolved      → Doc 10 §5.2 (transformer intent_to_object)
3. ContextAssembled    → Doc 10 §5.2 (Context Packet mínimo, memória curta + user_id refs)
```

**+ 1 output simples** (passo 8 do fluxo de 14, em modo simplificado):

```
PartialOutputProduced (simplificado)  → texto/JSON com correlation_id; sem streaming completo
```

**Envelope obrigatório de TODOS os eventos** (Doc 10 §5.3 linha 98):
- `event_id` (uuid v7), `workspace_id`, `project_id?`, `type`, `payload jsonb`, `actor`, `causation_id`, `correlation_id`, `occurred_at`

> **NÃO repita** os campos do envelope dentro do payload de cada evento (PATCH 2.5 fechou essa divergência). Implementação que escrever `correlation_id` dentro do `payload jsonb` regride o PATCH 2.5.

> **Reconciliação envelope conceitual ↔ físico (AJUSTE-03, Metacognik audit 2026-06-10):** Doc 10 §5.3 define o envelope **conceitual** com nomes legíveis; Doc 11 §7 (linhas 217-232) define o schema **físico** da tabela `events` com nomes ligeiramente diferentes + 6 campos operacionais extras. Mapeamento:
>
> | Conceitual (Doc 10 §5.3) | Físico (Doc 11 §7) | Notas |
> |---|---|---|
> | `event_id` | `id uuid(v7)` | rename + tipo explícito |
> | `type` | `event_type text` | rename |
> | `actor` | `actor_type enum(user\|agent\|system)` + `actor_id uuid` | desnormalizado |
> | `occurred_at` | `created_at timestamptz` | rename (semântica: momento do append) |
> | `workspace_id` | `workspace_id` | idem |
> | `project_id?` | `project_id` (NULL permitido) | nullable; F-02 RLS defer PATCH 3 |
> | `causation_id` | `causation_id uuid` | idem |
> | `correlation_id` | `correlation_id uuid` | idem |
> | `payload` | `payload jsonb` | idem |
> | (n/a) | `tenant_id` (= `org_id`) | extra — exigido por RLS Doc 12 §5.6.1 |
> | (n/a) | `aggregate_type` + `aggregate_id` | extra — partição + streams lógicos Doc 11 §7 linha 235 |
> | (n/a) | `idempotency_key text unique` | extra — Doc 11 §7 linha 232 + Doc 10 §5.6 |
> | (n/a) | `metadata jsonb` | extra — campo livre para telemetria/tracing |
> | (n/a) | `risk_level enum(low\|medium\|high)` | extra — usado por approval gate (defer S3) |
>
> S1 implementa o schema **físico** (Doc 11 §7) com todos os campos; `risk_level` e `aggregate_*` ficam com valores default (`"low"` + `aggregate_type='workflow'` + `aggregate_id = correlation_id`) até S3/S5 ativarem o uso real. `idempotency_key = hash(correlation_id + step + input_digest)` per Doc 10 §5.6.

**Detalhamento da forma user-first** (cobertura adicional):
- `03_BACKEND_MVP_THIN_SLICE_PLAN.md §18.2` — schema com REQUIRED/OPTIONAL explícito; é a referência para o reviewer/implementador entender intent

---

## 4. Tech stack — confirmado em GATE 5 §7

| Componente | Decisão GATE 5 | Implicação S1 |
|---|---|---|
| Job runner / queue | **pg-boss** (Postgres-native; zero infra extra) | Worker que processa `IntentSubmitted` consome via pg-boss; mesmo DB do event log |
| Model gateway | **OpenRouter único** (Claude 4.7 Opus + GPT-5.5 com fallback mútuo) | Intent Resolver chama LLM via OpenRouter; `model_router` (Doc 10) aponta pra endpoint único |
| Secret store | **Supabase Vault** + `secret_refs` (Doc 11 §12.1 + Doc 12 §5.15) | Chave OpenRouter resolvida via `secret_ref` em runtime, nunca no log/payload |
| Database / persistence | **Supabase Postgres** (implícito por Vault + pg-boss escolhas) | `events`, `users`, `user_profiles`, `context_packs` em Supabase; RLS workspace-level via Doc 12 §5.6 |
| Telemetria | mínimo viável (S1) — log estruturado + `correlation_id` propagado | Doc 13 EVALS_OBSERVABILITY_AND_COST_CONTROL — só o essencial pra S1; expansão em S6 |

**Não decidido em GATE 5** (decidir antes ou durante S1):
- Runtime language/framework (Node/TS? Python? Go?) — depende de AQ-S1-02
- Deployment target (Supabase Edge Functions? Container? Vercel?) — depende de AQ-S1-02

---

## 5. Exit criterion (binário)

> **Uma intenção entra sem UI e gera trace com `correlation_id`** — `03_BACKEND_MVP_THIN_SLICE_PLAN.md §9` (S1).

Testável por:
1. POST `/intent` (ou push a queue) com `{intent_text, user_id, workspace_id}` autenticado
2. Inspeção do event log: 3 events com mesmo `correlation_id` (IntentSubmitted → IntentResolved → ContextAssembled)
3. Recebimento de 1 output JSON com `{correlation_id, payload}` na resposta da request (síncrono OK pra S1 — streaming fica pra S5)
4. **Zero UI envolvida** — teste roda via `curl`/Postman/pgcli

**Quality gate (Sprint Done):**
- 3 eventos persistidos com envelope completo
- Output não-genérico (não pode ser "ok" — tem que conter resolução real do Intent Resolver)
- `user_id` rastreado fim-a-fim
- Trace replay (Doc 10 §5.26) funciona pra essa intenção

---

## 6. Architecture Questions abertas — Founder/PMO decidem antes ou durante S1

### 🔴 Trava-início (decidir ANTES do dispatch de implementação)

**AQ-S1-01 — Repo de implementação**

Este projeto (`CKOS_DOCUMENTATION_REVIEWED`) é **doc-only**. Onde S1 vai morar?

| Opção | Prós | Contras |
|---|---|---|
| (a) Novo repo paralelo `CKOS_RUNTIME` (ou nome similar) | Separação limpa doc ↔ código; doc repo permanece estável | 2 repos pra sincronizar; cross-refs git ficam manuais |
| (b) Branch deste repo com pasta `runtime/` no root | Mono-repo; cross-refs via paths relativos | Histórico misturado; CI/CD doc ↔ código convive |
| (c) Outro caminho (sub-pasta `implementation/`? worktree separada? monorepo Nx/Turborepo?) | — | depende da resposta Founder |

**Recomendação PMO:** (a) novo repo `CKOS_RUNTIME` — preserva o estado documental rastreável deste repo (cadeia PATCH 1/2/2.5/3...) e isola velocidade de código sem poluir o doc history.

**AQ-S1-02 — Runtime stack (language/framework + deployment)**

Não foi decidido em GATE 5 (que cobriu queue/LLM/vault). Precisa decidir antes do dispatch.

| Componente | Opções | Recomendação PMO |
|---|---|---|
| Language | Node/TypeScript / Python / Go / Rust | **TypeScript** (Node 20+) — ecosystem Supabase + pg-boss + OpenRouter SDKs maduros; compartilha types com futuro UI |
| HTTP framework | Fastify / Express / Hono / Bun | **Fastify** — schema-first, performance, OpenAPI-friendly |
| Deployment | Supabase Edge Functions / Fly.io container / Vercel / Railway | **Fly.io** ou **Railway** (container) — Edge Functions limitam pg-boss worker; container roda worker + HTTP juntos |

**AQ-S1-03 — Executor de implementação (sessão dispatch)**

Quem implementa S1? Padrão de cadeia de dispatch (per [[feedback-dispatch-chain-mode]]):

| Opção | Notas |
|---|---|
| (a) Codex (precedente: Codex2 escreveu `03_BACKEND_MVP_THIN_SLICE_PLAN.md`) | Codex tem contexto do thin-slice plan; bom pra continuidade |
| (b) Windsurf fresh | Padrão APPLY mecânico até agora; tarefas de código mais complexas que APPLY |
| (c) Claude Code (outra instância) | Per [[feedback-metacognik-executor]] — Claude pra tarefas de maior risco/raciocínio |

**Recomendação PMO:** (a) Codex ou (c) Claude Code — implementação de runtime é tarefa de raciocínio (não-trivial) — fora do nicho "APPLY mecânico" do Windsurf.

**AQ-S1-05 — Auth do endpoint de ingress (TRAVA-INÍCIO — promovida 2026-06-10 por Metacognik audit AJUSTE-01)**

Exit criterion §5 step 1 diz "POST `/intent` ... **autenticado**". Sem auth definida, o teste do exit criterion é incompossível. Decidir antes do dispatch.

| Opção | Recomendação PMO | Implicação S1 |
|---|---|---|
| (a) **Mock JWT bearer literal** (header `Authorization: Bearer test-user-jwt-{user_id}`) — sem backend de auth real | **(recomendação PMO)** | Mais simples; e2e roda via `curl`; auth real fica S2/S3 |
| (b) Supabase Auth JWT real (signup mínimo + token) | mais completo mas adiciona setup | bate em compliance/PII (Doc 12) cedo demais |
| (c) API key estática por workspace | meio-termo | precisa de gerenciamento secret — vault desnecessário em S1 |

**Recomendação PMO:** (a) mock JWT — alinhado ao princípio backend-antes-de-UI e ao escopo cirúrgico do S1; auth real entra com S3 (policy/approval) quando Doc 12 §5.6.1 RLS começar a importar de fato.

### 🟡 Não-trava — decidir durante S1 ou logo após

**AQ-S1-04 — Janela temporal:** S1 tem deadline? Em quantos dias/semanas? Vai serializado com S2/S3 ou paralelizado?

**AQ-S1-06 — Doc 11 patch suggestion S1 emergencial:** S1 vai descobrir gaps reais em Doc 11 (ex: `events.correlation_id` index, `context_packs.intent_id` FK)? Se sim, registramos como `F1S1_DOC11_PATCH_FINDINGS.md` durante o sprint para virar PATCH 3 candidate depois.

### 🟢 Defer (PATCH 3 ou sprints 2-3)

Já listadas em §2.2 — repetidas aqui apenas pra reforço: F-01/F-02/F-03 (PATCH 2.5 review), Doc 11 `users` enrichment, U3/U4/U5/R3/R4/R5, ProjectInferred event, Approval Gate completo, memória longa, ROI/evals.

---

## 7. Plano de dispatch (próximas sessões)

```txt
1. (AGORA) Este charter publicado e revisado pelo Founder
       → Founder responde AQ-S1-01/02/03 e flagga ajustes de escopo se necessário

2. Metacognik completeness audit (Claude fresh, mesmo pattern PATCH 2.5)
       → Sessão `S-F1S1-CHARTER-METAREV-CLAUDE-20260610-001`
       → Verifica: completeness do escopo, coerência com canônico pós-PATCH 2.5,
         realismo do exit criterion, suficiência das AQs respondidas
       → Veredito: APROVA / APROVA-COM-AJUSTES / REPROVA
       → NÃO é 2ª chave de canonical_patch (não há texto canônico nesta sessão)

3. Após Founder responder AQ-S1-01/02/03 + Metacognik APROVA-COM-AJUSTES + AJUSTES aplicados:
       → PMO escreve dispatch de implementação em SESSÃO SEPARADA desta e da autora
         (arquivo `S-F1S1-IMPLEMENTATION-DISPATCH.md`)
       → Especifica: repo, executor, stack, eventos a implementar, tests, exit criterion,
         decisão final de auth (AQ-S1-05 promovida — mock JWT bearer recomendado),
         orçamento LLM (AQ-S1-07 nova — fixar limite mensal/teste),
         ferramental de migrations (AQ-S1-08 nova — Drizzle/Prisma/raw decidir),
         `secret_refs.owner_type` para OpenRouter (def-01 — fixar `provider`)

3.5. (NOVO, AJUSTE-04 atualizado pós-`gh` install 2026-06-10) Criação do repo `CKOS_RUNTIME`
       → Founder confirma parâmetros (nome final, visibility private/public, descrição)
       → PMO executa `gh repo create danielck01/<NAME> --<VISIBILITY> --description "..." --add-readme`
         (gh CLI instalado e autenticado em 2026-06-10 — per [[reference-github-repo]])
       → PMO reporta URL do repo criado + branch default ao Founder para validação
       → URL é registrada no `S-F1S1-IMPLEMENTATION-DISPATCH.md` como `runtime_repo_url`

4. Executor (Codex OU Claude fresh — per AQ-S1-03) roda S1
       → Em sessão separada e em repo separado (clona `CKOS_RUNTIME` do step 3.5)
       → Reporta progresso via commits no `CKOS_RUNTIME` + relatórios de PR (GitHub)
       → Doc 11 patch findings emergem aqui (registrados em
         `000_ROADMAPS/22_CONSOLIDATION/F1S1_DOC11_PATCH_FINDINGS.md` no doc repo,
         per AQ-S1-06)

5. Verificação de exit criterion
       → Executor self-test: roda os 4 passos do §5 deste charter + reporta output JSON
         no `S-F1S1-IMPLEMENTATION-DISPATCH.md` (anexo)
       → PMO valida: lê trace replay (3 eventos com mesmo correlation_id + 1 output
         não-genérico) + confirma quality gate §5
       → Founder assina Sprint Done (atualiza Kanban: S1 → ✅)

6. Sprint Done → atualizar kanban → iniciar S4 (Event Log hardening) ou S2 (Question Engine)
       conforme §14 do backend plan
```

---

## 8. BRA Packet + CHECKOUT RELEASE

```yaml
bra_id: BRA-F1S1-CHARTER-20260610-01
from_session: S-F1S1-CHARTER-CLAUDE-20260610-001
to: Founder + Metacognik
context_summary:
  - "Cadeia PATCH 2 + 2.5 100% aplicada (commits 5d1d969, 79d66e1) — todas precondições documentais satisfeitas"
  - "Doc 10 §5.2 + Doc 15 §5.1 reconciliados como contrato canônico único de IntentSubmitted (user-first)"
  - "GATE 5 §7 fixou pg-boss + OpenRouter + Supabase Vault como tech stack"
  - "Exit criterion S1 do backend plan §9 = 1 intent end-to-end com correlation_id, sem UI"
  - "S1 escopo limitado aos 3 primeiros eventos do fluxo de 14 passos + 1 output simplificado"
outputs:
  - "F1_SPRINT1_CHARTER.md (este): escopo + tech stack + exit criterion + AQs abertas + plano de dispatch"
open_questions:
  - "AQ-S1-01 (Repo de implementação): novo repo CKOS_RUNTIME / branch / outro?"
  - "AQ-S1-02 (Stack): TS+Fastify+Fly.io é a recomendação PMO — Founder confirma?"
  - "AQ-S1-03 (Executor): Codex / Claude fresh / Windsurf — Founder escolhe?"
  - "AQ-S1-04 (Janela temporal): deadline + serializado vs paralelizado com S2/S3?"
  - "AQ-S1-05 (Auth ingress): Supabase Auth JWT é suficiente pra S1?"
blockers:
  - "AQ-S1-01/02/03 são trava-início para o dispatch de implementação. Charter destravado por GATE 5 + PATCHES 2/2.5."
risk_flags:
  - "P1 (Runtime core): mitigado por escopo cirúrgico (3 eventos + 1 output simples), reuso máximo de docs 02/05/10/11/12 já reconciliados, exit criterion binário"
recommended_next:
  - "Founder lê este charter → flagga ajustes + responde AQ-S1-01/02/03 → commit + push"
  - "Em paralelo: Metacognik completeness audit (sessão fresca, Claude Code, mesmo pattern PATCH 2.5)"
  - "Após Founder responder + Metacognik APROVA: PMO escreve S-F1S1-IMPLEMENTATION-DISPATCH.md"
```

---

## 9. Founder Decision Log (2026-06-10)

Founder revisou o charter em 2026-06-10 e respondeu **"Aceito todas as recomendações"** às 3 AQs trava-início. Decisões registradas:

### AQ-S1-01 — Repo de implementação: **(a) Novo repo `CKOS_RUNTIME` paralelo**

- Doc repo (`CKOS_DOCUMENTATION_REVIEWED`) permanece estável
- Novo repo `CKOS_RUNTIME` (nome provisório; Founder pode renomear no momento do `git init`) será criado para hospedar S1 e sprints subsequentes
- Cross-refs entre repos via path absoluto/URL nos commits

### AQ-S1-02 — Stack: **TypeScript + Fastify + Fly.io/Railway**

- **Language:** TypeScript (Node 20+ LTS)
- **HTTP framework:** Fastify (schema-first, OpenAPI-friendly, performance)
- **Deployment:** Fly.io **ou** Railway (container) — decisão final fica para o executor de implementação no momento do `fly launch` / `railway init` (ambos suportam pg-boss worker + HTTP juntos)
- Justificativa preservada do charter §4 + §6 AQ-S1-02

### AQ-S1-03 — Executor de implementação: **Codex OU Claude Code fresh**

- Implementação de runtime é tarefa de raciocínio (não-trivial) — fora do nicho "APPLY mecânico" do Windsurf
- Escolha final entre Codex e Claude Code fresh fica para o momento do dispatch de implementação (per §7 etapa 3), conforme disponibilidade/preferência operacional
- Mantém [[feedback-metacognik-executor]] — Windsurf reservado para tarefas mecânicas

### AQs médias (não-trava — decidir durante S1)

- **AQ-S1-04** (janela temporal) e **AQ-S1-05** (auth ingress) permanecem abertas; serão decididas no dispatch de implementação ou durante o sprint conforme a forma do trabalho se materializar.

### Próximo passo confirmado

Charter agora vai para **Metacognik completeness audit** (Claude fresh, mesmo pattern PATCH 2.5) — sessão `S-F1S1-CHARTER-METAREV-CLAUDE-20260610-001`. Após APROVA, PMO escreve `S-F1S1-IMPLEMENTATION-DISPATCH.md` (já com AQs trava-início respondidas, conforme acima).

---

## 9.5 Metacognik Audit + AJUSTES Applied (2026-06-10, charter v0.3.0)

Metacognik completeness audit (Claude fresh, sessão `S-F1S1-CHARTER-METAREV-CLAUDE-20260610-001`) executou 8 checks contra o charter v0.2.0 (commit `3548821`) e emitiu **APROVA-COM-AJUSTES** (commit `26fba60`). Forma A escolhida pelo PMO: 4 AJUSTES obrigatórios aplicados in-place no charter (v0.2.0 → v0.3.0). Charter agora é fonte-de-verdade auto-contida para dispatch de implementação.

### AJUSTES aplicados

| Ajuste | § afetado | Resumo |
|---|---|---|
| **AJUSTE-01** | §6 | AQ-S1-05 (auth) promovida de 🟡 não-trava para 🔴 trava-início com 3 opções + recomendação PMO = mock JWT bearer literal |
| **AJUSTE-02** | §2.1 | +3 deliverables operacionais (#7 DB migrations, #8 healthcheck `/health`, #9 error handling Intent Resolver com `IntentResolutionFailed` event) — sustentam os 6 cognitivos sem alterar veredito §0 |
| **AJUSTE-03** | §3 | Tabela de reconciliação envelope **conceitual** (Doc 10 §5.3) ↔ **físico** (Doc 11 §7) com 9 campos canônicos + 6 extras (tenant_id, aggregate_*, idempotency_key, metadata, risk_level) — orienta implementer a usar schema físico de Doc 11 §7 |
| **AJUSTE-04** | §7 | Steps 3-5 reescritos com **step 3.5 NOVO** (criação do repo `CKOS_RUNTIME` via `gh` CLI — atualizado pós-install em 2026-06-10) + step 5 explicita verificadores (PMO valida trace + Founder assina Sprint Done) |

### Modificação operacional vs review original

AJUSTE-04 do review especificava "Founder cria repo CKOS_RUNTIME via web UI (gh CLI ausente)". Em **2026-06-10 durante esta sessão**, o `gh` CLI foi instalado e autenticado (Founder rodou `gh auth login` como `danielck01`, escopos `repo`+`workflow`+`read:org`+`gist`). O step 3.5 foi atualizado para refletir essa nova capacidade: Founder confirma parâmetros (nome, visibility, descrição), PMO executa `gh repo create` — preserva o **espírito** do AJUSTE-04 (Founder ownership das decisões) sem a fricção da web UI. Memória [[reference-github-repo]] atualizada.

### 6 deferíveis não-bloqueantes (do review §5)

Não aplicados nesta revisão; entram no dispatch de implementação OU em PATCH 3:

- **def-01** (`secret_refs.owner_type='provider'` para OpenRouter) → fixar no dispatch
- **def-02** (RLS policy `events.project_id IS NULL`) → PATCH 3 (Doc 12 §5.6 update; herdado de F-02 PATCH 2.5)
- **def-03** (orçamento custo LLM CI/e2e) → fixar no dispatch como nova AQ-S1-07
- **def-04** (monitoring além de log + correlation_id) → emergente durante S1
- **def-05** (explicitar `PolicyChecked`/`RunStarted` skipados em §2.2) → nota leve em §2.2 OU no dispatch
- **def-06** (cosmético `project_id?` vs `project_id` literal) → PATCH 3 (F-03)

### AQs novas surgidas do audit (para o dispatch incorporar)

- **AQ-S1-07** — Orçamento LLM (limite mensal de OpenRouter em CI/dev/e2e)
- **AQ-S1-08** — Ferramental de migrations (Drizzle, Prisma, Kysely, raw SQL, Supabase migrations) — Doc 11 §7 `events` tem partição por `aggregate_type` + range por `created_at`, não trivial em alguns ORMs
- **AQ-S1-09** — gh CLI ownership do executor da implementação (executor terá `gh` no ambiente dele ou usa GitHub web nos PRs? — não-bloqueante mas vale fixar)

### Próximo passo (pós-AJUSTES aplicados)

1. **PMO escreve `S-F1S1-IMPLEMENTATION-DISPATCH.md`** (sessão SEPARADA desta e da autora-original do charter) — orquestra Codex OU Claude fresh em `CKOS_RUNTIME`
2. **Em paralelo:** Founder confirma nome/visibility do repo → PMO executa `gh repo create`
3. **Executor inicia S1** após dispatch + repo prontos

---

```txt
CHECKOUT RELEASE — S-F1S1-CHARTER-CLAUDE-20260610-001
files_created: 000_ROADMAPS/22_CONSOLIDATION/F1_SPRINT1_CHARTER.md (este)
files_changed: 000_ROADMAPS/SESSION_REGISTRY.md (1 sessão; planejado)
files_not_touched: canônico 01-28 (RO — só lidas seções referenciadas: Doc 10 §5.2/§5.3, Doc 02 §5.2, Doc 05 §5.6.1, Doc 15 §5.1); demais candidates (RO histórico); ARCHITECTURE_PATCH_REPORT.md (não há nova §; charter não é canonical_patch); UPGRADE/*; 00_SYSTEM_GOVERNANCE/*; SQL/UI/backend
validation:
  - todas as precondições documentais verificadas e citadas com commit hash
  - escopo IN (6 deliverables) + OUT (~11 itens com motivo de defer cada) + PROIBIDO explícito
  - contratos de eventos cite-only (não duplica Doc 10 §5.2)
  - tech stack alinhado com decisões GATE 5 §7
  - exit criterion binário e testável
  - 5 AQs abertas claramente flagadas (3 trava-início + 2 médias)
  - plano de dispatch em 6 etapas com sessão Metacognik antes do executor
risks_remaining: P1 mitigado por escopo cirúrgico + reuso de canônico já reconciliado; principal risco residual = AQ-S1-01 (repo) não respondida bloqueia dispatch
next_step: Founder review → responde AQs → Metacognik completeness audit → dispatch implementação
status: released
```
