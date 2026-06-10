---
title: APPLY PATCH 2.5 — IntentSubmitted reconciliation (canonical_patch, pré-montada)
file: S-APPLY_PATCH2_5_CANONICAL.md
layer: auxiliary
doc_type: pmo_session_task
phase: 000_ROADMAPS
category: consolidation
status: ready_to_run
version: 0.1.0
created_at: 2026-06-09
owner: pmo_ckos
dispatcher: claude_opus_4_7 (S-F1S1-PMO-PATCH25-CLAUDE-20260609-001)
session_id: S-APPLY2_5-FRESH-20260609-001
role: canonical_patch_executor
applies:
  - PATCH2_5_INTENT_SUBMITTED_RECONCILIATION_CANDIDATE.md   # PATCH E.1 + E.2 (Doc 10 §5.2)
  - PATCH2_5_METACOGNIK_REVIEW.md §3                         # PL-01 obrigatório (Doc 15 linha 153)
gated_on: Metacognik 2ª chave ✅ = APROVA-COM-PATCHES-LEVES (commit `87bb035`, 2026-06-09) — PL-01 acoplado obrigatoriamente
target_canonical:
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md       # E.1 (linha 78) + E.2 (após linha 92)
  - 04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md       # PL-01 (linha 153)
executor_recommendation: Windsurf fresh (APPLY mecânico, per [[feedback-metacognik-executor]] — Windsurf reservado pra tarefas de menor risco; audit fica em Claude)
non_authority_boundary: >
  Sessão canonical_patch — a ÚNICA que pode editar canônico nesta cadeia, e SÓ depois das duas chaves
  (Founder ✅ GATE 5 = GO em 2026-06-09 + Metacognik ✅ APROVA-COM-PATCHES-LEVES com PL-01 obrigatório,
  commit `87bb035`, 2026-06-09). Executor fresco: NÃO pode ser a sessão-autora do candidate
  (S-F1S1-PMO-PATCH25-CLAUDE-20260609-001 = claude_opus_4_7) nem a sessão-auditora Metacognik
  (S-P25-L3-METAREV-CLAUDE-20260609-001 = Claude fresh). Cola SÓ os 3 blocos exatos (E.1 + E.2 + PL-01);
  nada de conteúdo novo, nada de F-01/F-02/F-03 (defer PATCH 3), nada de mover/arquivar UPGRADE, nada de
  SQL/UI/backend, nada de Doc 11 `users` enrichment (defer PATCH 3).
tags: [session-task, canonical-patch, intent-ingress, runtime, command-center, doc10, doc15, apply, two-key, l3-wave1, post-patch-2, f1-s1-prereq]
---

# APPLY PATCH 2.5 — IntentSubmitted reconciliation (canonical_patch)

> **Esta sessão APLICA o canônico.** É a 3ª etapa da cadeia PATCH 2.5 (Founder GATE 5 GO ✅ → Candidate ✅ → Metacognik APROVA-COM-PL-01 ✅ → APPLY). Aplica 3 blocos mecânicos: **E.1 + E.2** (Doc 10 §5.2) **+ PL-01** (Doc 15 linha 153), simultaneamente.

---

## ⛔ PRÉ-CONDIÇÃO — verificar antes de rodar

Esta sessão **só roda** se:

1. **Founder 1ª chave ✅** — GATE 5 = GO + AQ-IO-1 = `user` + §18 user-first reframe (2026-06-09, `GATE5_FOUNDER_DECISION_PACKAGE.md §8`)
2. **Metacognik 2ª chave ✅** — APROVA-COM-PATCHES-LEVES (2026-06-09, `L3_WAVE1/PATCH2_5_METACOGNIK_REVIEW.md`, commit `87bb035`); PL-01 acoplado é **obrigatório** (sem PL-01 = REPROVA)
3. **PATCH 2 já aplicado** — commit `5d1d969` (Doc 02 §5.2 + Doc 05 §5.6.1 referenciados pela nota E.2)

| Estado | O que fazer |
|---|---|
| ✅ Tudo OK acima | **Rode esta sessão.** Aplique E.1 + E.2 + PL-01 simultaneamente. |
| ❌ PATCH 2.5 candidate foi ajustado (ex: nota E.2 reformulada) | Re-conferir texto literal contra candidate **antes** de rodar |
| ❌ PL-01 NÃO está no escopo | **PARE.** Sem PL-01, PATCH 2.5 cria a fragmentação que se propõe a fechar. Devolva ao Dispatcher. |

---

## A. PROMPT PARA COLAR (canonical_patch — executor Windsurf fresco)

```txt
You are a CKOS session under MULTI_SESSION_EXECUTION_POLICY.
- Esta é uma sessão canonical_patch AUTORIZADA: pode editar APENAS os canônicos listados em ALLOWED,
  e SOMENTE colando os 3 blocos exatos (E.1 + E.2 + PL-01). Zero conteúdo novo. Zero reinterpretação.
- PRÉ-CONDIÇÃO: Metacognik review do PATCH 2.5 = APROVA-COM-PATCHES-LEVES (commit 87bb035, 2026-06-09).
  PL-01 é OBRIGATÓRIO — não aplique E.1/E.2 sem PL-01 na mesma sessão.
- Você NÃO é a sessão-autora do candidate (S-F1S1-PMO-PATCH25-CLAUDE-20260609-001 = claude_opus_4_7) nem
  a sessão-auditora Metacognik (S-P25-L3-METAREV-CLAUDE-20260609-001 = Claude fresh).
- NÃO toque F-01/F-02/F-03 (defer PATCH 3), NÃO toque Doc 11 `users` enrichment (defer PATCH 3),
  NÃO crie SQL/UI/backend, NÃO edite outro canônico além de Doc 10 + Doc 15.

ROLE: canonical_patch executor (Windsurf fresco). SESSION: S-APPLY2_5-FRESH-20260609-001.

READ FIRST (nesta ordem):
  1. L3_WAVE1/PATCH2_5_METACOGNIK_REVIEW.md  → confirmar veredito = APROVA-COM-PATCHES-LEVES + PL-01 §3
  2. L3_WAVE1/PATCH2_5_INTENT_SUBMITTED_RECONCILIATION_CANDIDATE.md §2  → E.1 e E.2 literais
  3. as 2 seções-alvo, para casar os anchors:
     - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md §5.2 (linha 78 + linha 92-94 contexto da nota E.2)
     - 04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md §5.1 (linha 153 dentro de bloco ```txt iniciado em 151)

ALLOWED TO WRITE:
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md  (E.1 + E.2 + bump version)
  - 04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md   (PL-01 + bump version)
  - ARCHITECTURE_PATCH_REPORT.md                          (registrar como §32 + bump version)
  - 000_ROADMAPS/SESSION_REGISTRY.md                      (1 sessão + 1 lock + release)

FORBIDDEN:
  - qualquer outro canônico (01-09, 11, 12-14, 16-28)
  - itens deferred do Metacognik review: F-01 (Agent/Scheduler ingress em Doc 10), F-02 (RLS cláusula
    project_id NULL em Doc 12), F-03 (consolidar duplicação project_id envelope vs payload em Doc 10)
  - Doc 11 `users` enrichment com campos PATCH 2 (operating_dna_ref?/tribes_scored?/etc.) — defer PATCH 3
  - mover/renomear/arquivar/deletar UPGRADE/*; SQL/UI/backend/migrations; texto fora dos 3 blocos
  - criar pastas novas; ProjectInferred event (mencionado só como cross-ref textual na nota E.2)

TASK (ordem importa — preservar leading whitespace em todos os SUBSTITUIRs):

  1. Confirmar veredito Metacognik = APROVA-COM-PATCHES-LEVES + PL-01 obrigatório acoplado (senão PARAR).

  2. APLICAR PATCH E.1 (Doc 10 §5.2 linha 78):
     ANCHOR: dentro do bloco ```txt de §5.2
     SUBSTITUIR (literal, incluindo dois espaços após `1.`):
       1.  CommandBar emite IntentSubmitted{text, project_id, user_id, section}
     POR (literal, incluindo dois espaços após `1.`):
       1.  Ingress (CommandBar | backend API | webhook) emite IntentSubmitted{intent_text, user_id, project_id?, context_ref?, section?}

  3. APLICAR PATCH E.2 (Doc 10 §5.2 nota explicativa):
     ANCHOR: após o fechamento ``` do bloco txt (atual linha 92, fim do bloco) e ANTES do parágrafo
             "Cada seta acima é **um evento no event log**" (atual linha 94)
     INSERIR (parágrafo único, citação Markdown):
       > **Nota — user-first ingress (PATCH 2.5, post-GATE 5):** `user_id` é REQUIRED (PATCH 2 PROMOTE-U1 — ver `01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md §5.2`); `project_id` é OPCIONAL na 1ª intenção do usuário e pode ser inferido a posteriori via `ProjectInferred{user_id, project_id, source_intent_id}` quando a intenção justificar (ver `000_ROADMAPS/22_CONSOLIDATION/03_BACKEND_MVP_THIN_SLICE_PLAN.md §18.2`). `intent_text` (renomeado de `text` para clareza); `context_ref?` aponta para briefing/conversa anterior se existir. **Source não é exclusivo de UI:** CommandBar permanece a origem canônica via Doc 14-16 (Product System), mas backend ingress (API, webhook, scheduled trigger) é igualmente válido — aderente a `§3` backend-antes-de-UI e ao F1-Sprint 1. Envelope fields (`workspace_id`, `correlation_id`, `occurred_at`, `actor`) seguem `§5.3` Event Log — não precisam ser repetidos no payload.

  4. APLICAR PATCH PL-01 (Doc 15 linha 153, dentro do bloco ```txt iniciado em linha 151):
     ANCHOR: linha 153 com 14 espaços de leading whitespace (preservar alinhamento!)
     SUBSTITUIR (literal, EXATAMENTE 14 espaços de indentação no início):
                   IntentSubmitted{text, project_id, user_id, section, mode?, slash_command?, mentioned_agent?}
     POR (literal, EXATAMENTE 14 espaços de indentação no início):
                   IntentSubmitted{intent_text, user_id, project_id?, context_ref?, section?, mode?, slash_command?, mentioned_agent?}

  5. Bump de versão:
       - Doc 10 v1.1.1 → v1.2.0  (minor — novo shape com campos opcionais)
       - Doc 15 v1.2.1 → v1.3.0  (minor — alinhamento estrutural com Doc 10 reframe)

  6. Registrar §32 em ARCHITECTURE_PATCH_REPORT.md (slot livre após §31 PATCH 2):
       - Bump v1.10.4 → v1.10.5
       - Conteúdo §32 segue mesmo template de §31:
         * Session ID, Task ID, Checkout lock, Checkout release
         * Trigger: 1ª + 2ª chaves citadas (commits 1b13f2c + 87bb035)
         * Escopo: PATCH E.1 + E.2 + PL-01 (acoplado obrigatoriamente)
         * Arquivos alterados (canônico): Doc 10 (E.1+E.2; v1.1.1→v1.2.0), Doc 15 (PL-01; v1.2.1→v1.3.0)
         * Arquivos alterados (governance): este relatório (v1.10.4→v1.10.5; §32), SESSION_REGISTRY
         * Resolução: fecha divergência §18.2 user-first ↔ Doc 10 §5.2 ↔ Doc 15 §5.1
         * Itens fora do escopo: F-01/F-02/F-03 (defer PATCH 3); Doc 11 users enrichment (defer PATCH 3)
         * Risco e rollback: P1 mitigado por escopo cirúrgico (1 substituição Doc 10 + 1 inserção Doc 10 + 1 substituição Doc 15); aditivo semântico; reversibilidade git baseline 5d1d969 (PATCH 2 aplicado) / 724bfb9 (este candidate)
         * Status: released_with_required_external_audit

  7. SESSION_REGISTRY.md: adicionar 1 entry de lock + 1 entry de sessão APPLY (padrão de §31 do PATCH 2)

  8. Emitir CHECKOUT RELEASE com status = released_with_required_external_audit.

CLOSE WITH: CHECKOUT RELEASE (files_changed exatos, versões, validation, status).
```

---

## B. Decisão de escopo (3 blocos — não negocie)

PATCH 2.5 APPLY = **E.1 + E.2 + PL-01 simultaneamente**. Regra:

| Item | Status | Razão |
|---|---|---|
| E.1 (Doc 10 §5.2 linha 78 — substituição) | ✅ aplicar | Patch principal — destrava S1 |
| E.2 (Doc 10 §5.2 nota explicativa) | ✅ aplicar | Patch principal — cross-ref a Doc 02/05 + §18.2 |
| PL-01 (Doc 15 linha 153 — substituição) | ✅ aplicar **obrigatório** | Sem PL-01, PATCH 2.5 cria fragmentação que pretende fechar (Metacognik §3) |
| F-01 (Agent/Scheduler ingress em E.1 nota) | ⛔ defer PATCH 3 | Coerente com foco user-first; clarificação futura sem urgência |
| F-02 (RLS cláusula `project_id IS NULL` em Doc 12 §5.6) | ⛔ defer PATCH 3 | Infra Doc 11 §7 já comporta `project_id NULL`; policy escrita vira PATCH 3 |
| F-03 (duplicação `project_id` envelope §5.3 vs payload) | ⛔ defer | Herança do canônico anterior; PATCH 2.5 não regride; consolidação futura |
| Doc 11 `users` enrichment | ⛔ defer PATCH 3 | §31 PATCH_REPORT explícito: materialização Doc 11 é candidate posterior |

> **Não negocie escopo durante a aplicação.** Se Windsurf executor identificar nova divergência durante a leitura dos canônicos, **PARE** e devolva ao Dispatcher — não tente "consertar tudo" numa sessão APPLY.

---

## C. Checklist de traceability (caprichado — não pular)

- [ ] Veredito Metacognik = APROVA-COM-PATCHES-LEVES confirmado (commit `87bb035` citado no release)
- [ ] PL-01 está incluído no escopo (sem PL-01, PARAR — devolver ao Dispatcher)
- [ ] PATCH 2 já aplicado em `5d1d969` (precondition — Doc 02 §5.2 + Doc 05 §5.6.1 existem como referências da nota E.2)
- [ ] E.1: linha 78 substituída literal (indentação `1.  ` com 2 espaços preservada — verificar `git diff`)
- [ ] E.2: nota explicativa inserida entre o fim do bloco ```txt (linha 92 anterior) e o parágrafo "Cada seta acima" (verificar contexto pré/pós linhas)
- [ ] PL-01: linha 153 substituída literal **com 14 espaços de indentação preservados** (alinhamento dentro do bloco ```txt de §5.1)
- [ ] Bumps feitos: Doc 10 `1.1.1 → 1.2.0` (linha 6 do frontmatter); Doc 15 `1.2.1 → 1.3.0` (linha 6)
- [ ] §32 escrita em ARCHITECTURE_PATCH_REPORT.md; bump `1.10.4 → 1.10.5` (linha 6)
- [ ] Nenhum item F-01/F-02/F-03 tocado (Doc 12 §5.6 intacto; §5.1/§5.3 de Doc 10 não recebem ajustes extras)
- [ ] Doc 11 `users` table intacta (campos PATCH 2 NÃO adicionados aqui)
- [ ] Demais canônicos (01-09, 11, 12-14, 16-28) intactos
- [ ] UPGRADE/* intacto
- [ ] `git status` mostra **apenas**: Doc 10, Doc 15, ARCHITECTURE_PATCH_REPORT.md, SESSION_REGISTRY.md

---

## D. SESSION_REGISTRY entries propostas (executor preenche/ajusta)

```txt
LOCK-APPLY2_5-FRESH-20260609-001 | LOCK_PATCH2_5_APPLICATION_20260609 | checkout_lock | windsurf_fresh |
  03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md, 04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md,
  ARCHITECTURE_PATCH_REPORT.md, 000_ROADMAPS/SESSION_REGISTRY.md |
  released_with_required_external_audit | 2026-06-09 | Lock pra APPLY mecânico do PATCH 2.5 (E.1 + E.2 + PL-01)
  após 2ª chave Metacognik = APROVA-COM-PATCHES-LEVES (commit 87bb035); executor fresco Windsurf
  (separação de papéis: não-autor claude_opus_4_7, não-auditora Claude fresh) | low | highest

S-APPLY2_5-FRESH-20260609-001 | WAVE1_PATCH2_5_INTENT_SUBMITTED_APPLY_20260609 | canonical_patch | windsurf_fresh |
  write: Doc 10 (E.1+E.2; v1.1.1→v1.2.0), Doc 15 (PL-01; v1.2.1→v1.3.0), ARCHITECTURE_PATCH_REPORT (§32; v1.10.4→v1.10.5),
  SESSION_REGISTRY (1 sessão + 1 lock); read-only: candidate + Metacognik review + canônico-alvo + cross-ref Doc 02/05 |
  released_with_required_external_audit | 2026-06-09 | Aplicação literal dos 3 blocos do PATCH 2.5 após 2ª chave
  Metacognik = APROVA-COM-PATCHES-LEVES (commit 87bb035, 2026-06-09): E.1 (Doc 10 §5.2 linha 78 — Ingress
  multi-source + project_id opcional + intent_text), E.2 (Doc 10 §5.2 nota explicativa pós-fluxo cross-ref
  Doc 02/05 + §18.2), PL-01 obrigatório (Doc 15 linha 153 — alinhamento estrutural com Doc 10); §32 registrada
  em ARCHITECTURE_PATCH_REPORT.md; F-01/F-02/F-03 e Doc 11 users enrichment defer PATCH 3; UPGRADE intacto;
  sem backend/UI/SQL/migrations/agentes reais; executor fresco (não-autor, não-auditora) | low | highest
```

---

## E. CHECKOUT RELEASE · executor preenche

```txt
CHECKOUT RELEASE — S-APPLY2_5-FRESH-20260609-001
precondition: Founder GATE 5 = GO + AQ-IO-1 = `user` (2026-06-09, GATE5_FOUNDER_DECISION_PACKAGE.md §8);
              Metacognik review PATCH 2.5 = APROVA-COM-PATCHES-LEVES (2026-06-09, L3_WAVE1/PATCH2_5_METACOGNIK_REVIEW.md, commit 87bb035);
              PATCH 2 aplicado (commit 5d1d969, baseline para Doc 02 §5.2 + Doc 05 §5.6.1 referenciados na nota E.2)
files_changed:
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md (v1.1.1 → v1.2.0):
      E.1 — §5.2 linha 78 substituída (Ingress multi-source, project_id opcional, intent_text)
      E.2 — §5.2 nota explicativa user-first inserida após bloco txt
  - 04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md (v1.2.1 → v1.3.0):
      PL-01 — §5.1 linha 153 substituída (alinhamento estrutural com Doc 10 §5.2)
  - ARCHITECTURE_PATCH_REPORT.md (v1.10.4 → v1.10.5): §32 PATCH 2.5 registrada
  - SESSION_REGISTRY.md (1 lock + 1 sessão APPLY)
files_not_touched: F-01/F-02/F-03 (defer PATCH 3); Doc 11 users enrichment (defer PATCH 3); demais canônicos 01-09, 11, 12-14, 16-28; UPGRADE/*; 00_SYSTEM_GOVERNANCE/*; SQL/UI/backend/migrations; PATCH 2/2.5 candidate (RO)
validation:
  - 3 blocos colados literais do PATCH 2.5 §2 + Metacognik review §3 (PL-01)
  - Indentação preservada: `1.  ` (2 espaços) em Doc 10 linha 78; 14 espaços em Doc 15 linha 153
  - Bumps consistentes: Doc 10 v1.2.0 + Doc 15 v1.3.0 + report v1.10.5
  - Anchor E.2 verificado entre fim do bloco txt e parágrafo "Cada seta acima"
  - Cross-ref Doc 02 §5.2 + Doc 05 §5.6.1 + §18.2 funcionais (PATCH 2 já aplicado em 5d1d969)
risks_remaining: P1 mitigado (escopo cirúrgico + aditivo semântico + git rollback baselines 5d1d969/724bfb9/87bb035)
next_step: F1 Sprint 1 charter (PMO standalone — Doc 10 + Doc 15 alinhados como contrato canônico único)
status: released_with_required_external_audit
```

---

## F. Diferenças vs APPLY PATCH 2 (referência rápida pro executor)

| Aspecto | APPLY PATCH 2 (`S-APPLY_PATCH2_CANONICAL.md`) | APPLY PATCH 2.5 (este) |
|---|---|---|
| Patches | A + B + C + D (4) — Thinking System | E.1 + E.2 + PL-01 (3) — Runtime + Product |
| Docs alvo | Doc 02, 03, 04, 05 | Doc 10, Doc 15 |
| Veredito 2ª chave | APROVA puro | APROVA-COM-PATCHES-LEVES (PL-01 obrigatório) |
| Executor | Windsurf fresh | Windsurf fresh (mesmo padrão — APPLY mecânico) |
| Bumps | Doc 02/04/05 v1.2.0; Doc 03 v1.3.0; report v1.10.4 | Doc 10 v1.2.0; Doc 15 v1.3.0; report v1.10.5 |
| §PATCH_REPORT | §31 | §32 |
| Defer | U3/U4/U5/R3/R4/R5 (MÉDIA) | F-01/F-02/F-03 + Doc 11 users enrichment |
| Risco característico | Indentação YAML preservada | Indentação `1.  ` em Doc 10 + 14 espaços em Doc 15 |

> **Lição PATCH 2:** o executor Windsurf duplicou involuntariamente uma linha no SESSION_REGISTRY (METAREV row). Para PATCH 2.5: **verifique se o session_id da entry sendo adicionada já existe no registry antes de inserir** — se sim, atualize em vez de duplicar. (Esta sessão APPLY adiciona LOCK + APPLY entries; nem METAREV nem outras pré-existem.)
