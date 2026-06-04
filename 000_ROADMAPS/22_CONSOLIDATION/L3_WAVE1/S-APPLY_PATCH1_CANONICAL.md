---
title: APPLY PATCH 1 — Execution Envelope (canonical_patch, pré-montada)
file: S-APPLY_PATCH1_CANONICAL.md
layer: auxiliary
doc_type: pmo_session_task
phase: 000_ROADMAPS
category: consolidation
status: blocked_on_metacognik_2nd_key
version: 0.1.0
created_at: 2026-06-04
owner: pmo_ckos
dispatcher: claude_opus_4_8 (S-P1-L3DISPATCH-CLAUDE-20260604-001)
session_id: S-P1-L3-APPLY1-CODEX-20260604-001
role: canonical_patch_executor
applies: PATCH1_EXECUTION_ENVELOPE_CANDIDATE.md
gated_on: Metacognik review = APROVA (2ª chave) sobre o texto do PATCH 1
target_canonical:
  - 02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md          # PATCH A + B
  - 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md # PATCH C
  - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md      # PATCH D (só se Metacognik aprovar D)
non_authority_boundary: >
  Sessão canonical_patch — a ÚNICA que pode editar canônico nesta cadeia, e SÓ depois das
  duas chaves (Founder ✅ + Metacognik). Executor fresco: NÃO pode ser a sessão-autora do
  PATCH 1 nem a sessão-auditora (separação de papéis). Cola SÓ os blocos exatos do PATCH 1;
  nada de conteúdo novo, nada de item HOLD, nada de mover/arquivar UPGRADE.
tags: [session-task, canonical-patch, execution-envelope, doc06, doc09, doc03, apply, two-key, l3]
---

# APPLY PATCH 1 — Execution Envelope (canonical_patch)

> **Esta sessão APLICA o canônico.** É a 4ª etapa da cadeia. Ela só existe pronta para que,
> no instante em que a 2ª chave virar, a aplicação seja **mecânica e rastreável** — sem reabrir decisão.

---

## ⛔ PRÉ-CONDIÇÃO (a 2ª chave) — não rode antes disto

Esta sessão **só roda** se a revisão do Metacognik ([S-METACOGNIK_PATCH1_REVIEW.md](S-METACOGNIK_PATCH1_REVIEW.md)) voltou **`APROVA`**. Decida pelo veredito:

| Veredito Metacognik | O que fazer |
|---|---|
| **APROVA** | Rode esta sessão. Aplique A, B, C (e D **se** o Metacognik aprovou D). |
| **APROVA-COM-PATCHES-LEVES** | **NÃO rode ainda.** O Dispatcher ajusta o `PATCH1_EXECUTION_ENVELOPE_CANDIDATE.md` com os patches leves; só então esta sessão roda sobre o texto corrigido. |
| **REPROVA** | **NÃO rode.** Volta pro Dispatcher re-trabalhar o PATCH 1. |

> Duas chaves: **Founder ✅** (triagem go/hold, 2026-06-04) + **Metacognik ⏳** (este texto). Sem as duas, nada de canônico.

---

## A. PROMPT PARA COLAR (canonical_patch — executor fresco)

```txt
You are a CKOS session under MULTI_SESSION_EXECUTION_POLICY.
- Esta é uma sessão canonical_patch AUTORIZADA: pode editar APENAS os canônicos listados em ALLOWED,
  e SOMENTE colando os blocos exatos do PATCH 1. Zero conteúdo novo. Zero reinterpretação.
- PRÉ-CONDIÇÃO: a revisão Metacognik do PATCH 1 = APROVA. Se não for APROVA, PARE e devolva ao Dispatcher.
- Você NÃO é a sessão-autora do PATCH 1 nem a auditora (separação de papéis).
- NÃO toque item HOLD, NÃO mova/arquive UPGRADE, NÃO crie SQL/UI/backend, NÃO edite outro canônico.

ROLE: canonical_patch executor (fresco). SESSION: S-P1-L3-APPLY1-CODEX-20260604-001.

READ FIRST (nesta ordem):
  1. L3_WAVE1/S-METACOGNIK_PATCH1_REVIEW.md  → confirmar veredito = APROVA (+ se PATCH D foi aprovado)
  2. L3_WAVE1/PATCH1_EXECUTION_ENVELOPE_CANDIDATE.md  → §3 tem os blocos EXATOS (PATCH A/B/C/D) e §4 as instruções
  3. as 3 seções-alvo, para casar os anchors:
     - 02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md  (§5.3 fim do template; §14; §15)
     - 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md  (§5.5 transformer registry)
     - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md  (§5.5 Agent Run) — SÓ se D aprovado

ALLOWED TO WRITE:
  - 02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md            (PATCH A + PATCH B)
  - 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md (PATCH C)
  - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md       (PATCH D — SOMENTE se Metacognik aprovou D)
  - ARCHITECTURE_PATCH_REPORT.md  (registrar o patch)
  - 00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md + 00_DEPENDENCY_MAP.md  (só se a mudança exigir traceability)
  - 000_ROADMAPS/SESSION_REGISTRY.md  (1 sessão + 1 lock + release)

FORBIDDEN:
  - qualquer outro canônico; qualquer item HOLD do fan-in (T2, S3a/S3b, clusters, catálogo F2, policies)
  - mover/renomear/arquivar/deletar UPGRADE/04|07|08; SQL/UI/backend/migrations; texto fora dos blocos do PATCH 1

TASK:
  1. Confirmar veredito APROVA (senão PARAR).
  2. Colar PATCH A e PATCH B no Doc 06 (anchors do §3 do PATCH 1, texto literal).
  3. Colar PATCH C no Doc 09 (anchor §5.5, os 5 campos de robustez literais).
  4. Se D aprovado: colar PATCH D no Doc 03 §5.5 (1 campo: next_actions). Se não: NÃO tocar Doc 03.
  5. Bump de versão minor: Doc 06 v1.1.0 → v1.2.0; Doc 09 → próximo minor; Doc 03 → próximo minor (só se D).
  6. Registrar em ARCHITECTURE_PATCH_REPORT.md: o quê, de onde (PATCH 1 / fan-in / 2 chaves), versões.
  7. Emitir CHECKOUT RELEASE com status = released_with_required_external_audit.

CLOSE WITH: CHECKOUT RELEASE (files_changed exatos, versões, validation, status).
```

---

## B. Decisão do PATCH D (companion opcional)

O PATCH D (Doc 03 §5.5 Agent Run: +`next_actions`) **toca o Thinking System core** — por isso é a única parte gated à parte. Regra:
- **Metacognik aprovou D** → inclua Doc 03 no escopo e cole o 1 campo. Envelope fica idêntico nos 3 docs.
- **Metacognik não aprovou D** → **não toque Doc 03**; Doc 06 §5.3.2 já referencia o Agent Run como cross-ref. Funciona sem D.

---

## C. Checklist de traceability (caprichado — não pular)

- [ ] Veredito Metacognik = APROVA confirmado e citado no release.
- [ ] PATCH A/B/C colados **literais** (diff = só os blocos do PATCH 1 §3).
- [ ] PATCH D: aplicado **ou** explicitamente não-aplicado (com motivo) — sem ambiguidade.
- [ ] Versões bumpadas e registradas no `ARCHITECTURE_PATCH_REPORT.md`.
- [ ] Nenhum item HOLD tocado; UPGRADE intacto (arquivamento é sessão própria, pós-decisão de taxonomia/policy).
- [ ] `git status` mostra só os arquivos de ALLOWED.

---

## D. CHECKOUT RELEASE · executor preenche

```txt
CHECKOUT RELEASE — S-P1-L3-APPLY1-CODEX-20260604-001
precondition: Metacognik review = APROVA (citar data/arquivo); PATCH D = [aprovado | não-aprovado]
files_changed:
  - 02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md (v1.1.0 → v1.2.0): PATCH A (§5.3.1/§5.3.2) + PATCH B (§14/§15)
  - 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md (→ minor): PATCH C (§5.5 robustez + envelope ref)
  - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md (→ minor): PATCH D next_actions  [só se aprovado]
  - ARCHITECTURE_PATCH_REPORT.md; SESSION_REGISTRY.md
files_not_touched: itens HOLD; UPGRADE/04|07|08; demais canônicos; SQL/UI/backend
validation: blocos colados literais do PATCH 1 §3; envelope reusa campos canônicos do Agent Run; versões registradas
risks_remaining: P1 mitigado (escopo cirúrgico + reuso + git rollback baseline b3fc69f)
next_step: fan-in final / sign-off Founder+Metacognik se desejado; AQ-W1-ENVELOPE resolvida e aplicada
status: released_with_required_external_audit
```
