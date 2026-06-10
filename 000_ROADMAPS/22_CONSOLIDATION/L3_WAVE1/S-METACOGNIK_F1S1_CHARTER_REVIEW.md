---
title: Metacognik — Completeness Audit do F1 Sprint 1 Charter
file: S-METACOGNIK_F1S1_CHARTER_REVIEW.md
layer: auxiliary
doc_type: pmo_session_task
phase: 000_ROADMAPS
category: consolidation
status: awaiting_run
version: 0.1.0
created_at: 2026-06-10
owner: pmo_ckos
dispatcher: claude_opus_4_7 (S-F1S1-CHARTER-CLAUDE-20260610-001 → atuando como Dispatcher do charter audit)
session_id: S-F1S1-CHARTER-METAREV-CLAUDE-20260610-001
role: metacognik_completeness_auditor
depends_on:
  - S-F1S1-CHARTER-CLAUDE-20260610-001            # charter publicado (commit 3548821)
  - S-USER-APPLY2-FRESH-20260609-001              # PATCH 2 aplicado (commit 5d1d969) — precondition
  - S-APPLY2_5-FRESH-20260609-001                 # PATCH 2.5 aplicado (commit 79d66e1) — precondition
companion_of: F1_SPRINT1_CHARTER.md
audit_context: >
  Esta NÃO é uma 2ª chave de canonical_patch. O F1 Sprint 1 Charter é um **planning artifact**
  (não modifica canônico 01-28). Esta sessão faz **completeness/coherence audit**: o charter cobre
  todo o necessário para destravar implementação? As decisões Founder (§9) são suficientes? O exit
  criterion é binário e realista? Há gaps de escopo (algo IN faltando, ou algo OUT que deveria estar IN)?
  Veredito: APROVA / APROVA-COM-AJUSTES / REPROVA — NÃO virar 2ª chave de PATCH, virar liberação para
  PMO escrever o dispatch de implementação.
separation_of_duties: >
  Sessão SEPARADA e independente. O autor do charter (claude_opus_4_7,
  S-F1S1-CHARTER-CLAUDE-20260610-001) NÃO revisa o próprio charter. Esta sessão DEVE rodar em
  **Claude Code em chat fresh** (instância separada, contexto novo, sem memória da sessão autora).
  **Windsurf NÃO é o executor recomendado** — audit de completeness exige raciocínio (avaliar gaps,
  realismo, coerência cross-doc), está fora do nicho APPLY mecânico. Read-only: NÃO aplica, NÃO edita
  canônico, NÃO edita o charter nem qualquer companion. Retorna veredito + findings.
tags: [session-task, metacognik, completeness-audit, charter, f1, sprint-1, intent-ingress, l3-wave1, post-patch-2-5, post-gate-5]
---

# Metacognik — Completeness Audit do F1 Sprint 1 Charter

> **A sessão que libera o PMO a escrever o dispatch de implementação:** "dispare a sessão de completeness audit do charter F1 Sprint 1".
> Audita o **F1_SPRINT1_CHARTER.md** (commit `3548821`) — escopo IN/OUT, coerência com canônico pós-PATCH 2/2.5, realismo do exit criterion, cobertura das AQs, registro das Founder decisions (§9), plano de dispatch.
> Devolve veredito: **APROVA / APROVA-COM-AJUSTES / REPROVA**.
> **Não aplica nada.** Se aprovar, PMO escreve `S-F1S1-IMPLEMENTATION-DISPATCH.md` (sessão separada) que orquestra o executor (Codex OU Claude fresh) em repo `CKOS_RUNTIME` separado.
> **Rode com contexto fresco em Claude Code — você não é o autor do charter, e Windsurf não faz audit.**

---

## A. PROMPT PARA COLAR (template auditor — completeness audit)

```txt
You are a CKOS session under MULTI_SESSION_EXECUTION_POLICY.
- Fonte de verdade aprovada = canônico 01-28 (pós-PATCH 2 e 2.5); docs 29-34 gated.
- NÃO edite canônico 01-28 nem o charter F1_SPRINT1_CHARTER.md. NÃO atualize ARCHITECTURE_PATCH_REPORT.md
  nem 00_SYSTEM_GOVERNANCE/*.
- NÃO crie backend, UI, API, migrations, SQL, agentes runtime. read-only = só findings + veredito.
- Esta NÃO é uma 2ª chave de canonical_patch — é audit de completeness de um planning artifact.
  Não há texto canônico sendo aplicado.

ROLE: Metacognik completeness auditor (read-only) do F1 Sprint 1 Charter.
SESSION: S-F1S1-CHARTER-METAREV-CLAUDE-20260610-001.
CONTEXT: Cadeia PATCH 2 + 2.5 100% aplicada (commits 5d1d969, 79d66e1); GATE 5 = GO + AQ-IO-1 = `user`
         (Founder, 2026-06-09); Founder respondeu AQ-S1-01/02/03 do charter (2026-06-10, §9).
         Você decide se o charter está completo para PMO escrever o dispatch de implementação.
SEPARATION: o autor do charter = claude_opus_4_7 (S-F1S1-CHARTER-CLAUDE-20260610-001). Você NÃO é ele.
            Executor recomendado: **Claude Code em chat fresh** (NÃO Windsurf — audit precisa
            de raciocínio; Windsurf é reservado pra APPLY mecânico).

READ (nesta ordem):
  - 000_ROADMAPS/22_CONSOLIDATION/F1_SPRINT1_CHARTER.md         (o alvo — escopo, AQs, tech stack, §9 decisions)
  - 000_ROADMAPS/22_CONSOLIDATION/03_BACKEND_MVP_THIN_SLICE_PLAN.md §3/§9/§14/§18  (origem: backend-antes-de-UI, exit criterion S1, ordem dos sprints, user-first reframe)
  - 000_ROADMAPS/22_CONSOLIDATION/GATE5_FOUNDER_DECISION_PACKAGE.md §7-§8           (tech stack pg-boss/OpenRouter/Vault + decisão GO)
  - 000_ROADMAPS/22_CONSOLIDATION/F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md (fan-in F1 — confirma que PROMOTE-U1/U2/R1/R2 estão no canônico)
  - 000_ROADMAPS/22_CONSOLIDATION/CKOS_EXPANSION_KANBAN.md       (confirmar ordem dos sprints + estado F1)
  - canônico cross-ref (RO, confirmar coerência pós-PATCH 2/2.5):
      01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md §5.2  (User canônico — PATCH 2 PROMOTE-U1)
      01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md §5.6.1  (memória user_id — PATCH 2 PROMOTE-U2)
      03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md §5.2/§5.3  (IntentSubmitted user-first + envelope Event Log — PATCH 2.5)
      03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md §4 (tables events/users/user_profiles/context_packs) + §7 (events linhas 217-232) + §12.1 (secret_refs)
      03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md §5.6 (RLS multi-tenant) + §5.15 (Vault-only para segredos)
      04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md §5.1  (Command Center alinhado — PATCH 2.5 PL-01)
      00_SYSTEM_GOVERNANCE/00_TAXONOMY.md §7.4 (Constituição: nomes bonitos sem skill contratada)
  - L3_WAVE1/PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md           (RO histórico — confirmar defer U3-R5)
  - L3_WAVE1/PATCH2_5_METACOGNIK_REVIEW.md                       (RO histórico — confirmar defer F-01/F-02/F-03)

AUDIT GOAL: dar veredito sobre completeness do charter.
  1. ESCOPO IN — os 6 deliverables (endpoint ingress, event log mínimo, Intent Resolver, Context Assembler básico, 1 output simples, tracing correlation_id) são SUFICIENTES para o exit criterion (1 intent end-to-end com correlation_id, sem UI)? Falta algum componente crítico (auth básica, error handling mínimo, schema migration, healthcheck endpoint)?
  2. ESCOPO OUT — algum item defer é DE FATO precondição técnica de S1 (e foi defer por engano)? Algum item IN que poderia ser defer sem quebrar o exit criterion (over-scope)?
  3. COERÊNCIA com canônico pós-PATCH 2/2.5 — todos os anchors do charter (Doc 02 §5.2, Doc 05 §5.6.1, Doc 10 §5.2/§5.3, Doc 15 §5.1) batem com o estado atual canônico? Algum cite-only ficou apontando pra texto que não existe ou que mudou? Em particular: o envelope §5.3 do Doc 10 (linha 98) tem TODOS os campos que o charter §3 lista (`event_id`, `workspace_id`, `project_id?`, `type`, `payload`, `actor`, `causation_id`, `correlation_id`, `occurred_at`)?
  4. REALISMO DO EXIT CRITERION — "1 intent → 3 events + 1 output rastreado por correlation_id, sem UI" é binário e testável? Há gap implícito (ex: como o teste autentica sem auth setup? como o output é "não-genérico" sem skill registry mínimo? Intent Resolver chama LLM via OpenRouter — quanto custa testar end-to-end?). Quality gates (§5 do charter) são suficientes?
  5. TECH STACK GATE 5 — pg-boss + OpenRouter (Claude 4.7 Opus + GPT-5.5 fallback) + Supabase Vault batem com GATE5 §7? As implicações operacionais (§4 do charter) estão completas? Em particular: `secret_refs` (Doc 11 §12.1) realmente resolve a chave OpenRouter em runtime?
  6. AQ COVERAGE — as 5 AQs (3 trava-início + 2 médias) cobrem tudo o que falta decidir antes da implementação? Algum gap não nomeado (ex: monitoring/observability mínima, error rate budget, runtime cost estimate, schema migration plan para events table, RLS para events `project_id IS NULL` — a F-02 defer)? AQ-S1-05 (auth) é "média" mas pode ser trava-início de fato (sem auth, exit criterion não rodavel).
  7. FOUNDER DECISIONS §9 — as 3 respostas (AQ-S1-01 = novo repo `CKOS_RUNTIME`; AQ-S1-02 = TS+Fastify+Fly/Railway; AQ-S1-03 = Codex OU Claude fresh) estão registradas com implicações operacionais? Algo precisa de PMO follow-up para dispatch?
  8. PLANO DE DISPATCH (§7) — os 6 passos são realistas? Há salto perigoso (ex: pular Metacognik audit pra implementação direto)? Loop de feedback em produção (passo 5 "verificação exit criterion") está bem definido? Quem operacionaliza o `git init` do CKOS_RUNTIME (passo 3) — PMO ou Founder?

RETURN: veredito (APROVA / APROVA-COM-AJUSTES / REPROVA);
  tabela de findings por checagem 1-8;
  go/no-go explícito do charter como base para o dispatch de implementação;
  lista de ajustes obrigatórios (se APROVA-COM-AJUSTES) — citar §, linha, texto exato;
  lista de gaps não-bloqueantes (defer pra dispatch ou pra durante S1);
  confirmação de que a próxima sessão (PMO escreve `S-F1S1-IMPLEMENTATION-DISPATCH.md`) é SEPARADA
  desta e da autora do charter.

CLOSE WITH: criar L3_WAVE1/F1S1_CHARTER_METACOGNIK_REVIEW.md + CHECKOUT RELEASE
  (files_created: esse 1; files_changed: SESSION_REGISTRY 1 sessão + release; status: released).
```

---

## B. PERGUNTAS DO PMO → (o revisor responde no relatório)

1. **Cobertura mínima de auth (AQ-S1-05 = "média"):** dado que o exit criterion requer "1 intent autenticado entra", AQ-S1-05 (auth do ingress) é DE FATO trava-início e foi mal classificada? Justifique com base no exit criterion §5 do charter.

2. **Schema migration plan ausente:** charter §2.3 (proibido) diz "schemas SQL fora do que `11_DATA_MODEL` já define". Mas Doc 11 §4 tabelas (`events`, `users`, etc.) são *modeladas*, não materializadas. O dispatch de implementação precisa de uma sub-AQ sobre quem escreve as migrations iniciais (Supabase migrations? Drizzle? Prisma?) e onde elas vivem (CKOS_RUNTIME repo ou parte canônica?). Confirme se é gap ou se está adequadamente coberto.

3. **Observability/monitoring gap:** charter §4 menciona "telemetria mínima viável (S1) — log estruturado + correlation_id propagado", e §13 EVALS é defer pra S6. Mas se Intent Resolver via OpenRouter falhar, qual o circuito de feedback no S1? Quality gate §5 inclui error handling testável? (Verifique se Doc 13 §16 quality gates é referenciado adequadamente.)

4. **Cost estimate ausente:** OpenRouter é pay-per-token. S1 testando end-to-end com Claude 4.7 Opus + GPT-5.5 vai gerar custo. Charter NÃO menciona budget/cost guard pra S1. Pode ser gap a registrar como AQ-S1-06 (defer durante S1 ou trava se Founder quiser orçamento explícito).

5. **Repo cross-ref realismo (AQ-S1-01 resposta):** Founder decidiu novo repo `CKOS_RUNTIME`. Mas o charter cita anchors do tipo `Doc 10 §5.2` — quando S1 implementar, como vai garantir que essas citações continuam válidas (cross-repo)? Sugestão de patch leve no charter: amarrar "snapshot canônico em `5d1d969` + `79d66e1`" como baseline para o CKOS_RUNTIME.

6. **Plano de dispatch passo 3 (PMO escreve `S-F1S1-IMPLEMENTATION-DISPATCH.md`):** quem cria o repo `CKOS_RUNTIME` e qual é o conteúdo inicial? PMO inclui no dispatch um README mínimo? Ou Founder operacionaliza fora da cadeia?

7. **Sprint Done quality gate (§5 do charter):** "Output não-genérico (não pode ser 'ok')". Métrica de "não-genérico" é subjetiva. Há eval objetivo (Doc 13) que pode ser ancorado em S1 mesmo em modo mínimo? Ou aceita-se inspeção humana no Sprint Done?

8. **Defer F-02 (RLS `project_id IS NULL`) — risco real em S1?** Charter defer para PATCH 3. Mas S1 com `project_id?` opcional vai gerar events com `project_id NULL` no DEV. Se outro user/projeto compartilhar o mesmo workspace, há risco de leak? Mitigação adequada (workspace-level RLS via Doc 12 §5.6 é suficiente para DEV/MVP)?

---

## C. ← PERGUNTAS PARA O PMO/FOUNDER (BRA) · Metacognik preenche

```yaml
bra_id: BRA-METAREV-F1S1-CHARTER-20260610-01
from_session: S-F1S1-CHARTER-METAREV-CLAUDE-20260610-001
to: PMO/Dispatcher (claude_opus_4_7) + Founder
open_questions: [ (preencher após audit) ]
blockers:
  - "depende do charter F1_SPRINT1_CHARTER.md (já publicado no commit 3548821)"
  - "depende do PATCH 2/2.5 aplicados (commits 5d1d969, 79d66e1) — confirmar canônico antes de auditar"
  - "depende das Founder decisions §9 do charter (já registradas em 2026-06-10)"
recommended_next:
  - "(preencher: se APROVA → PMO escreve `S-F1S1-IMPLEMENTATION-DISPATCH.md` em sessão separada)"
  - "(se APROVA-COM-AJUSTES → Dispatcher edita F1_SPRINT1_CHARTER.md com ajustes; após commit, PMO escreve dispatch de implementação)"
  - "(se REPROVA → volta ao Dispatcher para re-trabalhar charter; em casos extremos, voltar ao Founder para re-respond AQs)"
```

---

## D. CHECKOUT RELEASE · Metacognik preenche

```txt
CHECKOUT RELEASE — S-F1S1-CHARTER-METAREV-CLAUDE-20260610-001
files_created: L3_WAVE1/F1S1_CHARTER_METACOGNIK_REVIEW.md
files_changed: SESSION_REGISTRY.md (1 sessão + release)
files_not_touched: charter F1_SPRINT1_CHARTER.md (RO — auditado, não editado); canônico 01-28 (RO — leituras conforme READ list); backend MVP plan / GATE5 / F1 candidate / kanban (RO); PATCH 2/2.5 candidates + reviews (RO histórico); ARCHITECTURE_PATCH_REPORT.md (não há nova § — audit não é canonical_patch)
validation: 8 checks executados — completeness IN/OUT, coerência canônico pós-PATCH 2/2.5, realismo exit criterion, tech stack GATE 5, AQ coverage, Founder decisions §9, plano de dispatch; veredito APROVA / APROVA-COM-AJUSTES / REPROVA + tabela de findings + lista de ajustes obrigatórios (se houver) + lista de gaps não-bloqueantes (defer)
risks_remaining: charter NÃO é canonical_patch — risco residual = dispatch de implementação pode descobrir gaps reais durante S1 (Doc 11 patches, schema migration, monitoring) que viram PATCH 3 ou follow-ups; mitigação = charter §6 AQ-S1-06 (Doc 11 patch findings emergenciais) já prevê esse caminho
next_step:
  - APROVA → PMO escreve `S-F1S1-IMPLEMENTATION-DISPATCH.md` (executor: Codex OU Claude fresh; repo: CKOS_RUNTIME; sessão fresca, não-autora claude_opus_4_7, não-auditora deste audit)
  - APROVA-COM-AJUSTES → Dispatcher edita F1_SPRINT1_CHARTER.md com ajustes; commit + push; depois PMO escreve dispatch
  - REPROVA → volta ao Dispatcher
status: released
```

---

## E. Entrada de SESSION_REGISTRY proposta (Dispatcher registra como `planned`)

```txt
S-F1S1-CHARTER-METAREV-CLAUDE-20260610-001 | F1S1_CHARTER_COMPLETENESS_AUDIT_20260610 | audit | metacognik (claude fresh) |
  scope: read F1_SPRINT1_CHARTER.md + backend MVP plan §3/§9/§14/§18 + GATE5 §7-§8 + F1 candidate + kanban
  + canônico Doc 02 §5.2, Doc 05 §5.6.1, Doc 10 §5.2/§5.3, Doc 11 §4/§7/§12.1, Doc 12 §5.6/§5.15, Doc 15 §5.1
  + PATCH 2/2.5 candidates + reviews (RO histórico) + Constituição (00_TAXONOMY §7.4);
  write L3_WAVE1/F1S1_CHARTER_METACOGNIK_REVIEW.md + registry | planned (depende do charter, já released no commit 3548821)
forbidden: aplicar/editar canônico 01-28; editar o charter; tocar `00_SYSTEM_GOVERNANCE/`; `ARCHITECTURE_PATCH_REPORT.md`;
  SQL/UI/backend; move/rename/delete; rodar implementação (essa é a próxima sessão, separada);
  decidir AQ-S1-04/05 (defer durante S1) — só pode RECOMENDAR
separation: NÃO pode ser claude_opus_4_7 autor (S-F1S1-CHARTER-CLAUDE-20260610-001); DEVE ser Claude Code fresh
  (NÃO Windsurf — audit em Claude per [[feedback-metacognik-executor]])
```

---

## F. Fluxo da completeness audit

```txt
1. Founder cola a seção A num chat **fresh em Claude Code** (instância separada do autor; NÃO Windsurf)
2. Metacognik roda → produz L3_WAVE1/F1S1_CHARTER_METACOGNIK_REVIEW.md com:
   - veredito (APROVA / APROVA-COM-AJUSTES / REPROVA)
   - findings 1-8
   - lista de ajustes obrigatórios (se houver, com § + linha + texto exato)
   - lista de gaps não-bloqueantes (defer pra dispatch ou durante S1)
3. Se APROVA → PMO (volta esta sessão claude_opus_4_7 ou nova instância) escreve `S-F1S1-IMPLEMENTATION-DISPATCH.md`
   incorporando: AQ-S1-01 (repo CKOS_RUNTIME) + AQ-S1-02 (stack) + AQ-S1-03 (executor) + qualquer gap apontado no audit
4. Se APROVA-COM-AJUSTES → Dispatcher edita F1_SPRINT1_CHARTER.md com os ajustes (versão bump 0.2.0 → 0.3.0);
   commit + push; depois PMO escreve dispatch de implementação
5. Se REPROVA → volta ao Dispatcher para re-trabalhar (raro — escopo cirúrgico do charter limita risco)
```

> **Importante:** mesmo se Metacognik aprovar, **nenhum código é escrito nesta sessão nem na próxima**. A próxima sessão (PMO) só **escreve o dispatch**. A implementação real é uma 4ª etapa, em **repo separado** (`CKOS_RUNTIME`) e executor diferente (Codex OU Claude fresh).

> **Diferença vs Metacognik review de canonical_patch:** este audit NÃO vira 2ª chave de PATCH — é um **completeness/coherence audit** de planning. Veredito não controla aplicação ao canônico (nada será aplicado); controla apenas se o PMO pode escrever o próximo dispatch.

> **Lição PATCH 2 e 2.5:** ambos os reviews Metacognik produziram findings concretos (PATCH 2.5 → PL-01 Doc 15 obrigatório). Para o charter audit, esperar findings tipicamente sobre completeness gaps (ex: auth coverage, observability, schema migration plan) — não sobre texto canônico literal.
