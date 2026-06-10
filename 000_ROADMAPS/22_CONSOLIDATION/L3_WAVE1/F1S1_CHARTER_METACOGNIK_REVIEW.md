---
title: F1 Sprint 1 Charter — Metacognik Completeness Review (read-only)
file: F1S1_CHARTER_METACOGNIK_REVIEW.md
layer: auxiliary
doc_type: pmo_metacognik_completeness_review
phase: 000_ROADMAPS
category: consolidation
status: released
version: 0.1.0
created_at: 2026-06-10
owner: pmo_ckos
reviewer: claude_fresh_session
session_id: S-F1S1-CHARTER-METAREV-CLAUDE-20260610-001
review_of: F1_SPRINT1_CHARTER.md
author_session: S-F1S1-CHARTER-CLAUDE-20260610-001  # claude_opus_4_7 — separação de papéis preservada (autor ≠ reviewer)
two_key_context: >
  Esta NÃO é uma 2ª chave de canonical_patch. PATCH 2 + 2.5 já estão aplicados ao canônico
  (commits `5d1d969`, `79d66e1`). Esta sessão = audit de COMPLETENESS de um planning artifact
  (charter PMO). Veredito orienta se o charter está pronto para virar dispatch de implementação.
target_dispatch_session: S-F1S1-IMPLEMENTATION-DISPATCH-20260610-001  # sessão futura (PMO escreve o dispatch — SEPARADA desta e da autora)
tags: [metacognik, completeness-audit, review, f1, sprint-1, intent-ingress, charter, planning, post-patch-2-5, post-gate-5, released]
---

# F1 Sprint 1 Charter — Metacognik Completeness Review

> **Veredito:** **APROVA-COM-AJUSTES** (charter sólido na espinha, 4 ajustes obrigatórios antes do dispatch)
> **Data:** 2026-06-10
> **Sessão:** S-F1S1-CHARTER-METAREV-CLAUDE-20260610-001 (Claude Code fresh, separado do autor `claude_opus_4_7` da sessão `S-F1S1-CHARTER-CLAUDE-20260610-001`)
> **Executor escolhido:** Claude Code fresh (per [[feedback-metacognik-executor]] — audit em Claude; Windsurf reservado para APPLY mecânico)
> **Natureza desta sessão:** completeness audit de planning artifact. NÃO é 2ª chave de canonical_patch (não há texto canônico nesta sessão). NÃO autoriza implementação.

---

## 1. Veredito

**APROVA-COM-AJUSTES** — O charter está estruturalmente sólido:

- Todas as 5 precondições documentais conferem (PATCH 2 commit `5d1d969`, PATCH 2.5 commit `79d66e1`, GATE 5 = GO 2026-06-09, F1 candidate fan-in publicado, decisões técnicas GATE 5 §7 alinhadas).
- Os 7 anchors canônicos do charter foram verificados RO contra o estado atual pós-PATCH 2/2.5 (Doc 02 §5.2 PROMOTE-U1, Doc 05 §5.6.1 PROMOTE-U2, Doc 10 §5.2/§5.3, Doc 11 §4/§7/§12.1, Doc 12 §5.6/§5.15, Doc 15 §5.1 PL-01, Taxonomy §7.4).
- Escopo cirúrgico (6 deliverables IN, ~11 itens OUT com motivo, 5 itens PROIBIDO).
- Tech stack do §4 bate 1:1 com GATE 5 §7-§8 (pg-boss + OpenRouter Claude 4.7 Opus + GPT-5.5 + Supabase Vault).
- Founder decisions §9 (AQ-S1-01/02/03) registradas com implicações operacionais.
- Plano de dispatch §7 em 6 etapas com Metacognik audit antes do executor (esta sessão é a etapa 2).

**MAS 4 ajustes obrigatórios** precisam ser acoplados ao charter (ou ao próximo dispatch artifact `S-F1S1-IMPLEMENTATION-DISPATCH.md`) antes do executor arrancar. Sem eles, o exit criterion §5 não tem como ser composto, o implementer não saberá quais entidades persistir nem como mapear envelope conceitual → físico, e a operacionalização de `git init` do `CKOS_RUNTIME` fica órfã.

**Sem AJUSTES 01-04, REPROVO** como base para dispatch direto.
**Com AJUSTES 01-04 acoplados, APROVO** (com 4 observações não-bloqueantes def-01..def-04).

---

## 2. Tabela de findings por checagem (1–8)

| # | Checagem | Resultado | Detalhe |
|---|---|---|---|
| 1 | **ESCOPO IN — 6 deliverables suficientes para exit criterion?** | ⚠️ **PASS-COM-AJUSTE (AJUSTE-02)** | Os 6 deliverables cobrem o "intent → 3 events + 1 output" cirúrgico do §9 do backend plan. MAS faltam **3 deliverables implícitos** que o exit criterion presume sem nomear: (a) **DB migrations** para `events` (Doc 11 §7 linhas 217-232) + `users` (Doc 11 §4 linhas 139-143) + `user_profiles` (Doc 11 §4 linhas 145-147) + `context_packs` (Doc 11 §13 linha 439) — §2.3 PROIBIDO diz "schemas SQL fora do que `11_DATA_MODEL` já define", autorizando esses 4, mas não os enumera como entrega; (b) **healthcheck endpoint** (`/health` ou `/healthz`) — Fly.io e Railway ambos exigem para roteamento de tráfego, sem ele o deploy não roda; (c) **error handling mínimo do Intent Resolver** — chamada OpenRouter pode falhar (timeout, 429, 5xx); sem evento `IntentResolutionFailed{correlation_id}` o trace replay (Doc 10 §5.26 citado no §5 quality gate) quebra silenciosamente em falha de modelo. Não bloqueiam estruturalmente, mas implementer arranca às cegas. |
| 2 | **ESCOPO OUT — defer correto? Nada que devesse ser IN?** | ✅ **PASS** | Os ~11 itens defer estão corretos: UI defer F4 (alinha §3 do backend plan), Approval Gate defer S3 (§14), Question Engine defer S2, Work Order/Agent Run defer S5, memória longa/feedback/ROI defer S6, `ProjectInferred` defer S2 (§18.2 backend plan: Cognik decide), Doc 11 `users` enrichment defer PATCH 3 (§31 ARCHITECTURE_PATCH_REPORT.md), F-01/F-02/F-03 defer PATCH 3 (PATCH 2.5 review §5), U3/U4/U5/R3/R4/R5 defer PATCH 3, Cognitive Atmosphere defer F4. **Nenhum item OUT é precondição técnica de S1.** Observação leve: `PolicyChecked` (Doc 10 §5.2 passo 4) e `RunStarted` (passo 6) ficam implicitamente skipados pelo escopo "3 eventos + 1 output", mas o charter não nomeia. Não é gap — exit criterion não exige —, mas explicitar em §2.2 evitaria confusão do implementer. |
| 3 | **COERÊNCIA com canônico pós-PATCH 2/2.5 — anchors batem?** | ⚠️ **PASS-COM-AJUSTE (AJUSTE-03)** | Anchors verificados RO: **Doc 02 §5.2 linha 62** = `User` 1ª classe PROMOTE-U1 ✅; **Doc 05 §5.6.1 linha 115** = "Escopo de memória: project, workspace, user (PROMOTE-U2)" ✅; **Doc 10 §5.2 linha 78** = `IntentSubmitted{intent_text, user_id, project_id?, context_ref?, section?}` PATCH 2.5 ✅; **Doc 10 §5.3 linha 100** = envelope `event_id, workspace_id, project_id, type, payload, actor, causation_id, correlation_id, occurred_at` ✅; **Doc 15 §5.1 linha 153** = `IntentSubmitted{intent_text, user_id, project_id?, ...}` PL-01 ✅. **Anomalia 1 (cosmética):** charter §3 escreve `project_id?` (opcional) ao citar o envelope; Doc 10 §5.3 linha 100 literal escreve `project_id` (sem `?`). Coerente com a forma user-first do PATCH 2.5 (F-03 deferred) mas não é citação literal. Não bloqueia. **Anomalia 2 (estrutural — AJUSTE-03):** envelope **conceitual** Doc 10 §5.3 ≠ envelope **físico** Doc 11 §7. Divergências de nome: `event_id` (Doc 10) vs `id` (Doc 11 §7 linha 218); `type` vs `event_type` (linha 219); `actor` vs `actor_type` + `actor_id` (linhas 223-224); `occurred_at` vs `created_at` (linha 231); + Doc 11 §7 tem **6 campos extras** não no Doc 10 §5.3 (`idempotency_key, metadata, risk_level, aggregate_type, aggregate_id, tenant_id`). Charter §3 cita só Doc 10 §5.3 e omite a reconciliação — implementer terá que escolher qual mapeamento usar sem orientação. |
| 4 | **REALISMO DO EXIT CRITERION — binário e testável?** | ⚠️ **PASS-COM-AJUSTE (AJUSTE-01)** | Exit criterion §5 é binário e testável **modulo um gap interno**: §5 passo 1 diz **"POST `/intent` ... autenticado"**, mas auth é AQ-S1-05 classificada como "🟡 Não-trava — decidir durante S1 ou logo após". Sem auth definida no charter, **passo 1 do exit criterion é incompossível** — o implementer não tem como compor a request. Internamente inconsistente. Promover AQ-S1-05 a trava-início OU adicionar uma decisão Founder explícita ("mock JWT bearer literal serve para o teste S1") resolve. **Custo do teste e2e:** cada execução chama LLM via OpenRouter (Intent Resolver) → custo monetário real por run de CI/teste (~$0.01-0.05/call). Quality gate §5 não menciona orçamento. Não bloqueia o sprint mas merece flag no dispatch artifact. **Output "não-genérico" (quality gate):** alinhado com tipagem PATCH 2 PROMOTE-R1 (response_type/depth_level/reasoning_mode em Doc 03 §5.5) — implementer pode usar esses campos como guard ("se response_type vazio, fail"). |
| 5 | **TECH STACK — bate com GATE 5 §7?** | ✅ **PASS (com nota leve def-01)** | **pg-boss** (GATE5 §8.1 AQ-G5-02 = ✅) ✅; **OpenRouter único Claude 4.7 Opus + GPT-5.5 fallback** (GATE5 §8.1 AQ-G5-05 = ✅) ✅; **Supabase Vault + secret_refs** (GATE5 §8.1 AQ-G5-09 = ✅; Doc 11 §12.1 linhas 407-426; Doc 12 §5.15 linhas 404-446) ✅; **Supabase Postgres** implícito por Vault + pg-boss ✅. Charter §4 inclui corretamente o caso "chave OpenRouter via `secret_ref` em runtime, nunca no log/payload" — consistente com Doc 12 §5.15 (proibido em produção: API key em event log/trace/response/prompt/config versionado). **Nota leve def-01:** `secret_refs.owner_type` (Doc 11 §12.1 linha 415) enum é `integration|collector|tool|actor|provider`. OpenRouter como model gateway não tem fit limpo; melhor encaixe semântico = `provider` (a API externa é o "provedor de modelo"). Implementer pode decidir, mas dispatch deveria fixar para evitar criatividade desnecessária. Não bloqueia. |
| 6 | **AQ COVERAGE — as 5 AQs cobrem tudo? Gaps não nomeados?** | ⚠️ **PASS-COM-AJUSTES (AJUSTE-01 promove AQ-S1-05; AJUSTE-04 ownership do `git init`)** | AQs cobrem o essencial: AQ-S1-01 (repo) ✅ respondida; AQ-S1-02 (stack) ✅ respondida; AQ-S1-03 (executor) ✅ respondida; AQ-S1-04 (janela temporal) e AQ-S1-05 (auth) abertas; AQ-S1-06 (Doc 11 patch findings emergenciais) abertas. **Gaps não nomeados encontrados:** (a) **AQ-S1-05 mal classificada** — auth é trava-início de fato porque exit criterion §5 step 1 a exige; ver §AJUSTE-01; (b) **AQ-S1-07 ausente**: orçamento de custo OpenRouter para S1 e2e (depende de §4 mas charter não estima); (c) **AQ-S1-08 ausente**: ferramental de migrations no novo repo `CKOS_RUNTIME` — Drizzle/Prisma/Kysely/raw SQL/Supabase migrations? Cada um tem implicações de schema (Doc 11 §7 events com partição por aggregate_type + range por created_at — partição não é trivial em Prisma); (d) **AQ-S1-09 ausente**: ownership operacional do `git init` do `CKOS_RUNTIME` — per memória `[[reference_github_repo]]` gh CLI não está instalado nesta máquina; Founder precisa criar repo manual via github.com web UI antes do executor poder clonar. Charter §7 step 3 não nomeia quem faz isso; ver §AJUSTE-04. |
| 7 | **FOUNDER DECISIONS §9 — completas? PMO follow-up?** | ✅ **PASS (com nota AJUSTE-04 acoplada à check 6)** | As 3 decisões trava-início estão registradas com implicações operacionais explícitas: AQ-S1-01 deixa nome final do repo para o momento do `git init` (Founder), AQ-S1-02 deixa Fly.io vs Railway para o `fly launch`/`railway init` do executor, AQ-S1-03 deixa Codex vs Claude Code fresh para o momento do dispatch. **PMO follow-up pendente:** quem cria o repo `CKOS_RUNTIME` (ou nome final escolhido pelo Founder)? Decisões AQ-S1-01/02 deixam isso para "o momento do dispatch / implementação", mas dispatch é o que vamos escrever na próxima sessão — precisa nominar. Ver AJUSTE-04. |
| 8 | **PLANO DE DISPATCH §7 — 6 passos realistas? Salto perigoso?** | ⚠️ **PASS-COM-AJUSTE (AJUSTE-04 — ownership steps 3-5)** | Steps 1-2 (charter publicado + Metacognik audit) executados conforme. Step 3 (PMO escreve `S-F1S1-IMPLEMENTATION-DISPATCH.md`) **a executar em sessão SEPARADA** desta e da autora — confirmar separação no dispatch artifact. Step 4 (executor roda S1) **separação garantida** pela escolha "Codex OU Claude fresh" do AQ-S1-03 (Founder explicitamente exclui Windsurf). **Salto identificado:** entre step 3 e step 4 há handoff implícito de criação do repo — sem step 3.5 "Founder cria repo CKOS_RUNTIME no GitHub" o executor não tem onde clonar. Step 5 (verificação exit criterion) sem dono nomeado: implementer self-verifica? PMO checa? Founder assina? §5 quality gate lista 4 condições mas não diz quem confirma. Sugiro nominar PMO (lê trace replay + 3 eventos + 1 output) + Founder (assina Sprint Done). Step 6 (Sprint Done → S4 ou S2) coerente com §14 do backend plan. Nenhum salto pula Metacognik audit; loop de feedback aceitável. |

---

## 3. Go/no-go por componente do charter

| Componente | Go/no-go | Bloqueio |
|---|---|---|
| §0 Veredito 1-linha | ✅ **GO** | nenhum |
| §1 Precondições (5 verified) | ✅ **GO** | nenhum |
| §2.1 Escopo IN (6 deliverables) | ⚠️ **GO-COM-AJUSTE** | AJUSTE-02 (3 deliverables implícitos) |
| §2.2 Escopo OUT (~11 defers) | ✅ **GO** | nenhum (obs leve: explicitar PolicyChecked/RunStarted skipados) |
| §2.3 PROIBIDO | ✅ **GO** | nenhum |
| §3 Contratos de evento | ⚠️ **GO-COM-AJUSTE** | AJUSTE-03 (envelope conceitual vs físico) |
| §4 Tech stack | ✅ **GO** | nenhum (def-01 não-bloqueante) |
| §5 Exit criterion | ⚠️ **GO-COM-AJUSTE** | AJUSTE-01 (auth indefinida + custo LLM) |
| §6 AQs | ⚠️ **GO-COM-AJUSTE** | AJUSTE-01 promove AQ-S1-05 + AQ-S1-07/08/09 ausentes |
| §7 Plano de dispatch | ⚠️ **GO-COM-AJUSTE** | AJUSTE-04 (ownership steps 3.5 + 5) |
| §8 BRA Packet + CHECKOUT RELEASE | ✅ **GO** | nenhum |
| §9 Founder Decision Log | ✅ **GO** | nenhum (AJUSTE-04 acoplado em §7) |

**Sem AJUSTES 01-04 aplicados ao charter (ou ao próximo dispatch artifact), REPROVA** como base para dispatch direto.
**Com AJUSTES 01-04 aplicados, APROVA** (def-01..def-04 são deferíveis durante S1 ou para PATCH 3).

---

## 4. AJUSTES OBRIGATÓRIOS (§, linha, texto exato)

Os ajustes podem ser aplicados de duas formas:
- **Forma A (preferida):** patch leve no charter §2.1/§3/§6/§7/§9 antes do dispatch — mantém o charter auto-contido e único ponto de verdade.
- **Forma B (aceitável):** ajustes virarem cláusulas explícitas no `S-F1S1-IMPLEMENTATION-DISPATCH.md` que PMO escreverá em sessão separada — charter fica "frozen" como referência histórica.

PMO decide em §1 da sessão de dispatch.

### AJUSTE-01 — Auth do ingress: promover AQ-S1-05 a trava-início

**Arquivo:** `000_ROADMAPS/22_CONSOLIDATION/F1_SPRINT1_CHARTER.md`

**§6 linha 210 — alterar status da AQ-S1-05:**

DE:
```
**AQ-S1-05 — Auth do endpoint de ingress:** Supabase Auth (JWT)? OAuth? API key? Mínimo viável pra S1.
```

PARA (sub §🔴 Trava-início):
```
**AQ-S1-05 — Auth do endpoint de ingress (TRAVA-INÍCIO — promovida 2026-06-10 por Metacognik audit):**

Exit criterion §5 step 1 diz "POST `/intent` ... **autenticado**". Sem auth definida, o teste do exit
criterion é incompossível. Decidir antes do dispatch.

| Opção | Recomendação PMO | Implicação S1 |
|---|---|---|
| (a) **Mock JWT bearer literal** (header `Authorization: Bearer test-user-jwt-{user_id}`) — sem backend de auth real | **(recomendação PMO)** | Mais simples; e2e roda via `curl`; auth real fica S2/S3 |
| (b) Supabase Auth JWT real (signup mínimo + token) | mais completo mas adiciona setup | bate em compliance/PII (Doc 12) cedo demais |
| (c) API key estática por workspace | meio-termo | precisa de gerenciamento secret — vault desnecessário em S1 |

**Recomendação PMO:** (a) mock JWT — alinhado ao princípio backend-antes-de-UI e ao escopo cirúrgico do
S1; auth real entra com S3 (policy/approval) quando Doc 12 §5.6.1 RLS começar a importar de fato.
```

### AJUSTE-02 — Deliverables implícitos enumerados

**Arquivo:** `000_ROADMAPS/22_CONSOLIDATION/F1_SPRINT1_CHARTER.md`

**§2.1 — adicionar 3 linhas à tabela ENTRA (após linha 77, após linha 6 "Tracing"):**

INSERIR:
```
| 7 | **DB migrations** para `events`, `users`, `user_profiles`, `context_packs` (schemas conforme Doc 11 §4/§7/§13) | Doc 11 §4 (`users`/`user_profiles` linhas 139-148), §7 (`events` linhas 217-232), §13 (`context_packs` linha 439) |
| 8 | **Healthcheck endpoint** `GET /health` (200 OK + DB ping) — exigido por Fly.io/Railway para roteamento | implícito do tech stack §4 (Fly.io/Railway) |
| 9 | **Error handling mínimo do Intent Resolver** — falha OpenRouter (timeout/429/5xx) emite evento `IntentResolutionFailed{correlation_id, error_kind, retry_count}` ao invés de explodir; trace replay (Doc 10 §5.26) continua coerente em modo falha | Doc 10 §5.6 (Run Scheduler retry/timeout/dead-letter) — modo simplificado para S1 |
```

E ajustar §0 (veredito 1-linha) para refletir os 9 deliverables, OU mantê-lo como está e tratar 7-9 como "deliverables operacionais que sustentam os 6 cognitivos".

### AJUSTE-03 — Reconciliação envelope conceitual (Doc 10 §5.3) ↔ físico (Doc 11 §7)

**Arquivo:** `000_ROADMAPS/22_CONSOLIDATION/F1_SPRINT1_CHARTER.md`

**§3 — adicionar nota após linha 127 (após "Implementação que escrever `correlation_id` dentro do `payload jsonb` regride o PATCH 2.5"):**

INSERIR:
```
> **Reconciliação envelope conceitual ↔ físico (orientação ao implementer):** Doc 10 §5.3 define o
> envelope **conceitual** com nomes legíveis; Doc 11 §7 (linhas 217-232) define o schema **físico**
> da tabela `events` com nomes ligeiramente diferentes + 6 campos operacionais extras. Mapeamento:
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
> S1 implementa o schema **físico** (Doc 11 §7) com todos os campos; `risk_level` e `aggregate_*` ficam
> com valores default ("low" + `aggregate_type='workflow'` + `aggregate_id = correlation_id`) até S3/S5
> ativarem o uso real. `idempotency_key = hash(correlation_id + step + input_digest)` per Doc 10 §5.6.
```

### AJUSTE-04 — Ownership de `git init` + verificação do exit criterion

**Arquivo:** `000_ROADMAPS/22_CONSOLIDATION/F1_SPRINT1_CHARTER.md`

**§7 — alterar linhas 233-244 (steps 3-5 do plano de dispatch):**

DE (atual):
```
3. Após Founder responder AQ-S1-01/02/03 + Metacognik APROVA:
       → PMO escreve dispatch de implementação
         (arquivo `S-F1S1-IMPLEMENTATION-DISPATCH.md` ou similar)
       → Especifica: repo, executor, stack, eventos a implementar, tests, exit criterion

4. Executor (Codex ou Claude fresh) roda S1
       → Em sessão separada e em repo separado (per AQ-S1-01 resposta)
       → Reporta progresso via commits + relatórios de PR
       → Doc 11 patch findings emergem aqui (registrados em arquivo paralelo)

5. Verificação de exit criterion
       → Testes end-to-end demonstram 1 intent → 3 events + 1 output, rastreado por correlation_id
       → Quality gate Sprint Done passa
```

PARA:
```
3. Após Founder responder AQ-S1-01/02/03 + Metacognik APROVA:
       → PMO escreve dispatch de implementação em SESSÃO SEPARADA desta e da autora
         (arquivo `S-F1S1-IMPLEMENTATION-DISPATCH.md`)
       → Especifica: repo, executor, stack, eventos a implementar, tests, exit criterion,
         decisão final de auth (per AQ-S1-05 promovida), orçamento LLM (per AQ-S1-07 nova),
         ferramental de migrations (per AQ-S1-08 nova), secret_refs.owner_type para
         OpenRouter (per def-01)

3.5. (NOVO) Founder cria repo `CKOS_RUNTIME` no GitHub
       → Manual via github.com web UI (gh CLI não está instalado nesta máquina —
         per [[reference_github_repo]])
       → Founder define visibility (private vs public) e nome final
       → Founder reporta URL do repo + branch default ao PMO via commit no
         CKOS_DOCUMENTATION_REVIEWED (ex.: editar `S-F1S1-IMPLEMENTATION-DISPATCH.md`
         adicionando o `runtime_repo_url`)

4. Executor (Codex ou Claude fresh — per AQ-S1-03) roda S1
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
```

**Justificativa:** charter atual deixa a criação do repo órfã entre PMO (escreve dispatch) e Executor (precisa clonar). O step 3.5 nomina Founder por dois motivos: (a) per memória `[[reference_github_repo]]`, gh CLI não está disponível; (b) ownership do repo (visibility/admin) precisa ser do Founder, não do executor. Step 5 nomina PMO + Founder como verificadores para fechar o loop de quality gate.

---

## 5. Gaps não-bloqueantes (defer pra dispatch ou pra durante S1)

| ID | Item | Onde resolver | Notas |
|---|---|---|---|
| def-01 | `secret_refs.owner_type` para OpenRouter (Doc 11 §12.1 enum não tem fit limpo para model gateway) | dispatch (fixar `provider`) | Não bloqueia S1; implementer pode escolher mas explicit > implicit |
| def-02 | RLS policy para `events.project_id IS NULL` (F-02 deferred no PATCH 2.5 review) | PATCH 3 (Doc 12 §5.6 update) | S1 user-first → 1ª intenção sem project_id → linha events com NULL. PATCH 2.5 review §1 já flaggou; mantido aqui. Workaround S1: RLS por `workspace_id + actor_id = user_id` (cobre o caso happy-path) |
| def-03 | Orçamento custo LLM para CI/e2e de S1 (AQ-S1-07 nova sugerida) | dispatch (fixar limite mensal/teste) | OpenRouter Claude 4.7 Opus + GPT-5.5 fallback custa ~$0.01-0.05/call; S1 e2e teste pode rodar 10-50x por iteração de dev → $1-5/dia max |
| def-04 | Monitoring/observability mínima além de log estruturado + correlation_id | durante S1 (emergente) | Charter §4 cita Doc 13 EVALS como referência mas não quantifica; S1 sobrevive com console.log + DB query manual sobre `events` |
| def-05 | Explicitar `PolicyChecked` e `RunStarted` (passos 4 e 6 do fluxo de 14) como skipados em S1 | nota leve no charter §2.2 | Não bloqueia; só evita confusão do implementer |
| def-06 | Cosmético: `project_id?` (charter §3) vs `project_id` literal (Doc 10 §5.3 linha 100) | PATCH 3 (F-03 deferred no PATCH 2.5 review) | Já flaggado; nada novo. |

---

## 6. Confirmação de separação de sessões (Constituição multi-sessão)

| Sessão | Agent | Papel | Estado |
|---|---|---|---|
| `S-F1S1-CHARTER-CLAUDE-20260610-001` | `claude_opus_4_7` | **Autora** do charter | released 2026-06-10 (commit `3548821`) |
| `S-F1S1-CHARTER-METAREV-CLAUDE-20260610-001` | `metacognik (fresh / Claude Code)` | **Esta sessão** — completeness audit | releasing agora |
| `S-F1S1-IMPLEMENTATION-DISPATCH-20260610-001` | a definir (PMO) | **Próxima sessão** — escreve dispatch artifact | a abrir após este release |
| `S-F1S1-IMPL-EXECUTOR-<DATA>-001` | Codex OU Claude fresh (AQ-S1-03) | **Sessão de implementação** | a abrir após dispatch + Founder cria repo CKOS_RUNTIME |

**Garantias:**
- Esta sessão (audit) NÃO é a autora do charter — separação preservada (PMO → Metacognik diferentes).
- A próxima sessão (PMO dispatch) NÃO é esta nem a autora — terceira instância.
- A sessão do executor NÃO é nenhuma das anteriores — quarta instância, em REPO separado (`CKOS_RUNTIME`).
- Esta sessão NÃO edita canônico 01-28 (RO confirmed — só `F1S1_CHARTER_METACOGNIK_REVIEW.md` + `SESSION_REGISTRY.md`).
- Esta sessão NÃO escreve canonical_patch nem texto canônico — é audit de planning artifact.
- Esta sessão NÃO autoriza implementação — só destrava (ou trava) o dispatch.

---

## 7. Próximo passo recomendado

1. **PMO lê este review** e decide: aplicar AJUSTES 01-04 no charter (Forma A — patch leve) OU embutir no dispatch artifact (Forma B — cláusulas no `S-F1S1-IMPLEMENTATION-DISPATCH.md`).
2. **Se Forma A:** sessão Claude/Codex fresh aplica AJUSTES 01-04 no charter (escopo: só esse arquivo + SESSION_REGISTRY); bump charter v0.2.0 → v0.3.0.
3. **Se Forma B:** PMO escreve `S-F1S1-IMPLEMENTATION-DISPATCH.md` em sessão SEPARADA com AJUSTES embutidos como cláusulas; charter permanece v0.2.0 freezed.
4. **Founder cria repo `CKOS_RUNTIME`** no GitHub (manual via web UI; gh CLI ausente) — pode acontecer em paralelo com step 3.
5. **Executor (Codex OU Claude fresh) clona `CKOS_RUNTIME` e arranca S1** — sessão separada da autora, da auditora e do dispatcher.

**Após Sprint Done:** atualizar Kanban (S1 → ✅), abrir S4 (Event Log hardening) ou S2 (Question Engine) per §14 backend plan.

---

## 8. BRA Packet + CHECKOUT RELEASE

```yaml
bra_id: BRA-F1S1-CHARTER-METAREV-20260610-01
from_session: S-F1S1-CHARTER-METAREV-CLAUDE-20260610-001
to: PMO_CKOS + Founder
context_summary:
  - "Charter F1 Sprint 1 (commit 3548821) auditado em sessão Claude Code fresh, separada do autor claude_opus_4_7"
  - "Cadeia PATCH 2 + 2.5 100% aplicada confirmada (commits 5d1d969, 79d66e1) — 5 precondições documentais OK"
  - "7 anchors canônicos verificados RO contra estado atual (Doc 02 §5.2, Doc 05 §5.6.1, Doc 10 §5.2/§5.3, Doc 11 §4/§7/§12.1, Doc 12 §5.6/§5.15, Doc 15 §5.1, Taxonomy §7.4) — todos PASS com 1 cosmético"
  - "Tech stack §4 bate 1:1 com GATE 5 §7-§8 (pg-boss + OpenRouter Claude 4.7 Opus + GPT-5.5 fallback + Supabase Vault)"
  - "Founder decisions §9 das 3 AQs trava-início (AQ-S1-01/02/03) registradas com implicações operacionais"
outputs:
  - "F1S1_CHARTER_METACOGNIK_REVIEW.md (este): veredito APROVA-COM-AJUSTES + 8 checks + 4 ajustes + 6 deferíveis + confirmação de separação de sessões"
verdict: APROVA-COM-AJUSTES
ajustes_obrigatorios:
  - "AJUSTE-01 — promover AQ-S1-05 (auth) a trava-início com recomendação PMO = mock JWT bearer literal (charter §6 linha 210)"
  - "AJUSTE-02 — enumerar 3 deliverables implícitos: DB migrations + healthcheck + error handling do Intent Resolver (charter §2.1 após linha 77)"
  - "AJUSTE-03 — adicionar tabela de reconciliação envelope conceitual (Doc 10 §5.3) ↔ físico (Doc 11 §7) (charter §3 após linha 127)"
  - "AJUSTE-04 — nominar Founder como criador do repo CKOS_RUNTIME (step 3.5 novo) + PMO+Founder como verificadores do exit criterion (charter §7 linhas 233-244)"
defers_nao_bloqueantes:
  - "def-01 secret_refs.owner_type para OpenRouter (fixar 'provider' no dispatch)"
  - "def-02 RLS policy events.project_id NULL (PATCH 3 — herdado de F-02 PATCH 2.5 review)"
  - "def-03 orçamento LLM para e2e CI (fixar no dispatch como AQ-S1-07 nova)"
  - "def-04 monitoring mínima além de log estruturado + correlation_id (emergente em S1)"
  - "def-05 explicitar PolicyChecked + RunStarted skipados em S1 (nota leve em §2.2)"
  - "def-06 cosmético: project_id? (charter §3) vs project_id literal (Doc 10 §5.3 linha 100) — F-03 PATCH 3"
blockers:
  - "Sem AJUSTES 01-04 aplicados (Forma A no charter OU Forma B no dispatch), REPROVA como base para dispatch direto"
  - "Específico: §5 step 1 'autenticado' sem auth definida (AJUSTE-01) torna exit criterion incompossível"
risk_flags:
  - "P1 (Runtime core) mitigado por escopo cirúrgico do charter (6 IN + ~11 OUT) + 7 anchors canônicos verificados pós-PATCH 2/2.5"
  - "Risco residual principal pós-AJUSTES = orçamento LLM real do e2e (def-03) — não-bloqueante mas merece flag"
recommended_next:
  - "PMO decide Forma A (patch leve no charter) ou Forma B (cláusulas no dispatch artifact)"
  - "Se Forma A: sessão fresh aplica AJUSTES 01-04 → bump charter v0.2.0→v0.3.0"
  - "Se Forma B: PMO escreve S-F1S1-IMPLEMENTATION-DISPATCH.md em sessão SEPARADA desta e da autora com AJUSTES embutidos"
  - "Em paralelo: Founder cria repo CKOS_RUNTIME no GitHub (web UI; gh CLI ausente)"
  - "Após dispatch + repo: executor (Codex OU Claude fresh per AQ-S1-03) clona CKOS_RUNTIME e arranca S1 em sessão SEPARADA"
session_separation_confirmed:
  - "Esta sessão (auditora) ≠ S-F1S1-CHARTER-CLAUDE-20260610-001 (autora, claude_opus_4_7) ✅"
  - "Próxima sessão (PMO dispatch, a abrir) ≠ esta + ≠ autora ✅"
  - "Sessão de implementação (executor, a abrir) ≠ todas as 3 anteriores + REPO separado (CKOS_RUNTIME) ✅"
  - "Esta sessão NÃO editou canônico 01-28; NÃO escreveu canonical_patch; NÃO autorizou implementação"
```

```txt
CHECKOUT RELEASE — S-F1S1-CHARTER-METAREV-CLAUDE-20260610-001
files_created: 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/F1S1_CHARTER_METACOGNIK_REVIEW.md (este)
files_changed: 000_ROADMAPS/SESSION_REGISTRY.md (1 sessão + 1 lock + release; planejado)
files_not_touched:
  - canônico 01-28 (RO — só lidas seções referenciadas: Doc 02 §5.2 linha 62, Doc 05 §5.6.1 linha 115, Doc 10 §5.2 linha 78 + §5.3 linha 100, Doc 11 §4 linhas 139-148 + §7 linhas 217-232 + §12.1 linhas 407-426 + §13 linha 439, Doc 12 §5.6 linhas 176-224 + §5.15 linhas 404-446, Doc 15 §5.1 linhas 147-186, Taxonomy §7.4 linha 130)
  - F1_SPRINT1_CHARTER.md (RO — alvo do audit; PMO decide aplicar AJUSTES em Forma A ou B em sessão separada)
  - ARCHITECTURE_PATCH_REPORT.md (não há nova §; audit de planning artifact não gera entry de patch_report)
  - 00_SYSTEM_GOVERNANCE/* (RO)
  - PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md + PATCH2_5_METACOGNIK_REVIEW.md (RO histórico — só consultados para confirmar defers U3-R5 e F-01/F-02/F-03)
  - F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md (RO — confirmou que PROMOTE-U1/U2/R1/R2 estão no canônico via PATCH 2 commit 5d1d969)
  - GATE5_FOUNDER_DECISION_PACKAGE.md (RO — confirmou tech stack §7 e decisão GO §8)
  - CKOS_EXPANSION_KANBAN.md (RO — confirmou estado F1 aberta + ordem dos sprints)
  - 03_BACKEND_MVP_THIN_SLICE_PLAN.md §3/§9/§14/§18 (RO — confirmou backend-antes-de-UI + exit criterion S1 + ordem sprints + user-first reframe)
  - UPGRADE/* (não tocado)
  - SQL / UI / backend / migrations / agentes runtime (não criados — read-only audit)
validation:
  - 8 checks executados conforme prompt; cada um com PASS / PASS-COM-AJUSTE explicitado em §2 + go/no-go por componente em §3
  - 4 AJUSTES obrigatórios com § + linha + texto exato (Forma A — diff-ready) em §4
  - 6 deferíveis não-bloqueantes em §5
  - separação de sessões (autora ≠ auditora ≠ dispatcher ≠ executor) confirmada em §6
  - próximo passo claro (Forma A vs B + ownership do repo CKOS_RUNTIME) em §7
risks_remaining: P1 mitigado por escopo cirúrgico do charter + 7 anchors canônicos verificados; risco residual = aplicação dos AJUSTES 01-04 em sessão separada (Forma A ou B) antes do dispatch
next_step: PMO escolhe Forma A (patch leve charter) ou B (cláusulas no dispatch) → Founder cria repo CKOS_RUNTIME em paralelo → executor arranca S1
status: released
```
