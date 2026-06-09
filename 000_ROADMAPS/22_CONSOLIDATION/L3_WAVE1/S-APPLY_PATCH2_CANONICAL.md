---
title: APPLY PATCH 2 — User-in + Response-out (canonical_patch, pré-montada)
file: S-APPLY_PATCH2_CANONICAL.md
layer: auxiliary
doc_type: pmo_session_task
phase: 000_ROADMAPS
category: consolidation
status: blocked_on_metacognik_2nd_key
version: 0.1.0
created_at: 2026-06-09
owner: pmo_ckos
dispatcher: claude_opus_4_7 (S-USER-PMO-CLAUDE-20260609-001)
session_id: S-USER-APPLY2-FRESH-20260609-001
role: canonical_patch_executor
applies: PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md
gated_on: Metacognik review = APROVA (2ª chave) sobre o texto do PATCH 2
target_canonical:
  - 01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md          # PATCH A
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md # PATCH B
  - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md          # PATCH C
  - 01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md         # PATCH D
non_authority_boundary: >
  Sessão canonical_patch — a ÚNICA que pode editar canônico nesta cadeia, e SÓ depois das duas chaves
  (Founder ✅ GATE 5 = GO em 2026-06-09 + Metacognik ⏳). Executor fresco: NÃO pode ser a sessão-autora
  do PATCH 2 (S-USER-PMO-CLAUDE-20260609-001 = claude_opus_4_7) nem a sessão-auditora Metacognik.
  Cola SÓ os blocos exatos do PATCH 2; nada de conteúdo novo, nada de U3/U4/U5/R3/R4/R5 (defer PATCH 3),
  nada de mover/arquivar UPGRADE, nada de SQL/UI/backend.
tags: [session-task, canonical-patch, user-system, response-engine, doc02, doc03, doc04, doc05, apply, two-key, l3-wave1, post-gate-5]
---

# APPLY PATCH 2 — User-in + Response-out (canonical_patch)

> **Esta sessão APLICA o canônico.** É a 4ª etapa da cadeia PATCH 2 (Founder GATE 5 GO ✅ → Candidate ✅ → Metacognik ⏳ → APPLY). Ela só existe pronta para que, no instante em que a 2ª chave virar, a aplicação seja **mecânica e rastreável** — sem reabrir decisão.

---

## ⛔ PRÉ-CONDIÇÃO (a 2ª chave) — não rode antes disto

Esta sessão **só roda** se a revisão Metacognik do PATCH 2 voltou **`APROVA`**. Decida pelo veredito:

| Veredito Metacognik | O que fazer |
|---|---|
| **APROVA** | Rode esta sessão. Aplique A, B, C, D. |
| **APROVA-COM-PATCHES-LEVES** | **NÃO rode ainda.** O Dispatcher ajusta o `PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md` com os patches leves; só então esta sessão roda sobre o texto corrigido. |
| **REPROVA** | **NÃO rode.** Volta pro Dispatcher re-trabalhar o PATCH 2. |

> Duas chaves: **Founder ✅** (GATE 5 = GO + AQ-IO-1 = `user`, 2026-06-09, registrado em `GATE5_FOUNDER_DECISION_PACKAGE.md §8`) + **Metacognik ⏳** (este texto). Sem as duas, nada de canônico.

---

## A. PROMPT PARA COLAR (canonical_patch — executor fresco)

```txt
You are a CKOS session under MULTI_SESSION_EXECUTION_POLICY.
- Esta é uma sessão canonical_patch AUTORIZADA: pode editar APENAS os canônicos listados em ALLOWED,
  e SOMENTE colando os blocos exatos do PATCH 2. Zero conteúdo novo. Zero reinterpretação.
- PRÉ-CONDIÇÃO: a revisão Metacognik do PATCH 2 = APROVA. Se não for APROVA, PARE e devolva ao Dispatcher.
- Você NÃO é a sessão-autora do PATCH 2 (S-USER-PMO-CLAUDE-20260609-001) nem a sessão-auditora Metacognik.
- NÃO toque U3/U4/U5/R3/R4/R5 (defer PATCH 3), NÃO crie `/CKOS_USER_SYSTEM/`, NÃO mova/arquive UPGRADE,
  NÃO crie SQL/UI/backend, NÃO edite outro canônico.

ROLE: canonical_patch executor (fresco). SESSION: S-USER-APPLY2-FRESH-20260609-001.

READ FIRST (nesta ordem):
  1. L3_WAVE1/PATCH2_METACOGNIK_REVIEW.md  → confirmar veredito = APROVA
  2. L3_WAVE1/PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md  → §3 tem os blocos EXATOS (PATCH A/B/C/D) e §4 as instruções
  3. as 4 seções-alvo, para casar os anchors:
     - 01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md (§5.1 linha 54; §5.2 após Workspace, antes Project)
     - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md (§5.6 bloco YAML; nova §5.6.1)
     - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md (§5.5 Agent Run YAML, entre `output:` e `confidence:`)
     - 01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md (§5.8 fim + nova §5.9 antes de `# 6. Agente responsável`)

ALLOWED TO WRITE:
  - 01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md            (PATCH A)
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md  (PATCH B)
  - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md            (PATCH C)
  - 01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md           (PATCH D)
  - ARCHITECTURE_PATCH_REPORT.md  (registrar como §31)
  - 000_ROADMAPS/SESSION_REGISTRY.md  (1 sessão + 1 lock + release)

FORBIDDEN:
  - qualquer outro canônico; qualquer item HOLD do fan-in (T2, S3a/S3b, clusters, catálogo F2, 11 policies);
    qualquer item MÉDIA do F1 candidate (U3, U4, U5, R3, R4, R5)
  - mover/renomear/arquivar/deletar UPGRADE/*; SQL/UI/backend/migrations; texto fora dos blocos do PATCH 2
  - criar `/CKOS_USER_SYSTEM/` ou pastas similares
  - criar Cognitive Atmosphere / Glass / wallpaper (F4)

TASK:
  1. Confirmar veredito APROVA (senão PARAR).
  2. Colar PATCH A em Doc 02 (A.1 §5.1 linha 54 substituir; A.2 §5.2 inserir definição User após Workspace).
  3. Colar PATCH B em Doc 05 (B.1 §5.6 YAML inserir `user_id:` após `project_id:`; B.2 inserir nova §5.6.1).
  4. Colar PATCH C em Doc 03 (§5.5 inserir 3 linhas entre `output:` e `confidence:`).
  5. Colar PATCH D em Doc 04 (nova §5.9 antes de `# 6. Agente responsável`).
  6. Bump de versão minor:
       - Doc 02 v1.1.0 → v1.2.0
       - Doc 03 v1.2.0 → v1.3.0  (subiu para 1.2.0 no PATCH 1)
       - Doc 04 v1.1.0 → v1.2.0
       - Doc 05 v1.1.0 → v1.2.0
  7. Registrar em ARCHITECTURE_PATCH_REPORT.md: §31 nova; bump v1.10.3 → v1.10.4.
  8. Emitir CHECKOUT RELEASE com status = released_with_required_external_audit.

CLOSE WITH: CHECKOUT RELEASE (files_changed exatos, versões, validation, status).
```

---

## B. Decisão de escopo

PATCH 2 = **somente os 4 itens ALTA** (U1 + U2 + R1 + R2). Regra:

| Item | Status | Razão |
|---|---|---|
| U1 (User 1ª classe) | ✅ inclui | ALTA — PATCH A |
| U2 (memória user_id) | ✅ inclui | ALTA — PATCH B |
| R1 (response_type/depth_level/reasoning_mode) | ✅ inclui | ALTA — PATCH C |
| R2 (5 Response Behavior Policies) | ✅ inclui | ALTA — PATCH D |
| U3 (4-level learning) | ⛔ defer PATCH 3 | precisa telemetria que ainda não existe |
| U4 (tribos dinâmicas) | ⛔ defer PATCH 3 | depende de F1-S6 (memória rodando) |
| U5 (onboarding engine) | ⛔ defer PATCH 3 | abstrato sem F1-S1/S2 rodando |
| R3 (gap gate 3 níveis) | ⛔ defer PATCH 3 | entra com Question Engine de F1-S2 |
| R4 (Response Contract V1) | ⛔ defer PATCH 3 | precisa evals existentes (Doc 13) |
| R5 (User/Audit Mode) | ⛔ defer F4 | UI distinction |

> **Não negocie escopo durante a aplicação.** Se Metacognik aprovar item adicional, isso volta ao Dispatcher para virar PATCH 3 candidate em sessão separada.

---

## C. Checklist de traceability (caprichado — não pular)

- [ ] Veredito Metacognik = APROVA confirmado e citado no release.
- [ ] PATCH A/B/C/D colados **literais** (diff = só os blocos do PATCH 2 §3).
- [ ] Versões bumpadas e registradas no `ARCHITECTURE_PATCH_REPORT.md` §31.
- [ ] Nenhum item MÉDIA tocado (U3/U4/U5/R3/R4/R5 intactos).
- [ ] Nenhum item HOLD tocado (T2, S3a/S3b, clusters, catálogo F2, policies).
- [ ] UPGRADE/* intacto (arquivamento é sessão própria).
- [ ] `/CKOS_USER_SYSTEM/` **não** criado.
- [ ] `git status` mostra só os arquivos de ALLOWED.

---

## D. CHECKOUT RELEASE · executor preenche

```txt
CHECKOUT RELEASE — S-USER-APPLY2-FRESH-20260609-001
precondition: Founder GATE 5 = GO + AQ-IO-1 = `user` (2026-06-09, GATE5_FOUNDER_DECISION_PACKAGE.md §8);
              Metacognik review PATCH 2 = APROVA (citar data/arquivo)
files_changed:
  - 01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md (v1.1.0 → v1.2.0):
      PATCH A — §5.1 +User; §5.2 +definição User
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md (v1.1.0 → v1.2.0):
      PATCH B — §5.6 +user_id no memory_object; §5.6.1 nova explicação dos 3 escopos
  - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md (v1.2.0 → v1.3.0):
      PATCH C — §5.5 Agent Run +response_type +depth_level +reasoning_mode
  - 01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md (v1.1.0 → v1.2.0):
      PATCH D — §5.9 nova Response Behavior Policies (5 anti-padrões)
  - ARCHITECTURE_PATCH_REPORT.md (v1.10.3 → v1.10.4): §31 registrada
  - SESSION_REGISTRY.md
files_not_touched: itens MÉDIA do F1 candidate (U3/U4/U5/R3/R4/R5); itens HOLD; UPGRADE/*;
  demais canônicos; SQL/UI/backend/migrations; `/CKOS_USER_SYSTEM/` não criado
validation: blocos colados literais do PATCH 2 §3; AQ-IO-2/3 resolvidas; envelope tipado consistente com
  Doc 06 §5.3.2 (PATCH 1); memória user_id consistente com 3 dimensões de escopo
risks_remaining: P1 mitigado (escopo cirúrgico + reuso + git rollback baseline c3786c2)
next_step: fan-in final / sign-off Founder+Metacognik; libera F1 Sprint 1 (S1 carrega user_id + IntentReceived)
status: released_with_required_external_audit
```
