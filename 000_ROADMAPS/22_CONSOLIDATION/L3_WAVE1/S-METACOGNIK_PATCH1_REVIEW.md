---
title: Metacognik — Revisão de Apply-Gate do PATCH 1 (2ª chave)
file: S-METACOGNIK_PATCH1_REVIEW.md
layer: auxiliary
doc_type: pmo_session_task
phase: 000_ROADMAPS
category: consolidation
status: awaiting_run
version: 0.1.0
created_at: 2026-06-04
owner: pmo_ckos
dispatcher: claude_opus_4_8 (S-P1-L3-PATCH1-CLAUDE-20260604-001 → atuando como Dispatcher)
session_id: S-P1-L3-METAREV-CLAUDE-20260604-001
role: metacognik_reviewer
depends_on: [S-P1-L3-PATCH1-CLAUDE-20260604-001]   # o candidate apply-ready
companion_of: PATCH1_EXECUTION_ENVELOPE_CANDIDATE.md
two_key_context: "Founder = 1ª chave ✅ (triagem, 2026-06-04). Esta sessão decide a 2ª chave (Metacognik) sobre o TEXTO."
separation_of_duties: >
  Sessão SEPARADA e independente. O autor do PATCH 1 (e do fan-in audit) NÃO revisa o próprio patch.
  Esta sessão deve rodar com contexto fresco. Read-only: NÃO aplica, NÃO edita canônico 01-28,
  NÃO edita o PATCH 1 candidate nem os candidates do audit. Retorna veredito + findings.
tags: [session-task, metacognik, apply-gate, review, patch1, execution-envelope, l3, two-key]
---

# Metacognik — Revisão de Apply-Gate do PATCH 1 (2ª chave)

> **A sessão que o Founder pediu:** "dispare a sessão de revisão do Metacognik sobre o PATCH 1".
> Revisa o **texto exato** do `PATCH1_EXECUTION_ENVELOPE_CANDIDATE.md` (blocos A/B/C/D) e a resolução
> proposta de `AQ-W1-ENVELOPE`. Devolve a **2ª chave**: APROVA / APROVA-COM-PATCHES-LEVES / REPROVA.
> **Não aplica.** Se aprovar, a aplicação é **mais uma** sessão `canonical_patch` separada.
> **Rode com contexto fresco — você não é o autor do patch.**

---

## A. PROMPT PARA COLAR (template auditor 5b — Metacognik apply-gate)

```txt
You are a CKOS session under MULTI_SESSION_EXECUTION_POLICY.
- Fonte de verdade aprovada = canônico 01-28; docs 29-34 gated.
- NÃO edite canônico 01-28 nem o PATCH 1 candidate. NÃO atualize ARCHITECTURE_PATCH_REPORT.md nem 00_SYSTEM_GOVERNANCE/*.
- NÃO crie backend, UI, API, migrations, SQL, agentes runtime. read-only = só findings + veredito.
- Study/UPGRADE/candidates/canônico = leitura. Não mover/renomear/deletar nada.

ROLE: Metacognik reviewer (read-only), 2ª chave do apply-gate. SESSION: S-P1-L3-METAREV-CLAUDE-20260604-001.
CONTEXT: Founder já deu a 1ª chave (triagem do fan-in audit). Você decide a 2ª chave sobre o TEXTO do patch.
READ:
  - L3_WAVE1/PATCH1_EXECUTION_ENVELOPE_CANDIDATE.md            (o alvo — blocos A/B/C/D + resolução de AQ-W1-ENVELOPE)
  - L3_WAVE1/WAVE1_FANIN_AUDIT_FOR_FOUNDER.md                  (a triagem aprovada; confirme que só GO entrou)
  - canônico-alvo (RO, casar texto exato):
      02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md §5.3 / §14 / §15
      02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md §5.5 / §14
      01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md §5.5 (Agent Run)
  - fonte da promoção (RO): DOC06_SKILLS_RECONCILIATION_CANDIDATE.md (S1/S2), DOC09_TRANSFORMERS_RECONCILIATION_CANDIDATE.md (T1)
REVIEW GOAL: virar (ou não) a 2ª chave sobre o texto exato.
  1. EXATIDÃO: cada ANCHOR e cada OLD→NEW casa LITERALMENTE com o texto atual do canônico? (apply tem de ser mecânico, sem corromper)
  2. CONSTITUIÇÃO §1: o envelope/contrato cria "nome bonito sem skill/teste"? (não deveria — é forma/critério, não entrada). Confirme.
  3. ANTI-FRAGMENTAÇÃO: a alegação "reusa campos já canônicos" é verdadeira? Verifique você mesmo que Doc 03 §5.5 já tem confidence/risks/gaps/evidence/idempotency_key e que Doc 09 §14 já exige fallback manual.
  4. ESCOPO: só GO (S1+T1+S2)? Zero vazamento de HOLD (T2, S3a/b, ROI/learning/context, catálogo F2, as 11 policies)?
  5. AQ-W1-ENVELOPE: a resolução proposta (1 envelope reusando Agent Run) é sólida AGORA, ou deveria esperar a AQ-mãe de taxonomia? Decida.
  6. PATCH D: incluir `next_actions` no Doc 03 §5.5 junto, ou deixar Doc 03 só como cross-ref? Decida go/no-go de D.
  7. IRRADIAÇÃO P1: adicionar esses campos a Doc 06/09 quebra algo downstream (Docs 03/04/07/08/10/11/13)? Sinalize.
  8. MECÂNICA: bump de versão + traceability (patch report/maps) descritos corretamente para a sessão de aplicação?
RETURN: veredito (APROVA = 2ª chave / APROVA-COM-PATCHES-LEVES / REPROVA);
  tabela de findings por checagem 1-8; go/no-go explícito do PATCH D; lista de patches-leves se houver;
  confirmação de que a aplicação é uma sessão canonical_patch SEPARADA (não esta).
CLOSE WITH: criar L3_WAVE1/PATCH1_METACOGNIK_REVIEW.md + CHECKOUT RELEASE (files_created: esse 1; files_changed: SESSION_REGISTRY 1 sessão + 1 lock; status: released).
```

## B. PERGUNTAS DO PMO → (o revisor responde no relatório)

1. **Exatidão literal:** algum bloco OLD→NEW **não** bate com o texto atual (espaço, aspas, numeração de seção)? Se sim, cite linha e corrija antes de aprovar — apply mecânico não pode corromper.
2. **Reuso real vs invenção:** o envelope realmente só **renomeia** o que o Agent Run já tem + `next_actions`, ou está introduzindo formato novo disfarçado? Prove com o YAML do Doc 03 §5.5.
3. **Robustez (Doc 09):** `validation/error_policy/fallback_manual/idempotency_semantics` entram como **lacuna obrigatória** (correto) e não como conteúdo herdado do UPGRADE/08 (que não tinha nada disso)? Confirme.
4. **Risco de pré-empção:** canonizar o envelope agora **fecha** indevidamente a AQ-W1-TAXONOMIA (skill vs transformer vs Work Order)? Ou é ortogonal (forma de saída ≠ onde a capacidade mora)? Julgue.
5. **D no Thinking core:** vale tocar o Doc 03 (core do Thinking System) por +1 campo agora, ou o alinhamento total pode esperar?

## C. ← PERGUNTAS PARA O PMO/FOUNDER (BRA) · Metacognik preenche

```yaml
bra_id: BRA-METAREV-20260604-01
from_session: S-P1-L3-METAREV-CLAUDE-20260604-001
to: PMO/Dispatcher + Founder
open_questions: [ (preencher) ]
blockers: [ "depende do PATCH 1 candidate (já released)" ]
recommended_next: [ (preencher: se APROVA → abrir sessão canonical_patch de aplicação) ]
```

## D. CHECKOUT RELEASE · Metacognik preenche

```txt
CHECKOUT RELEASE — S-P1-L3-METAREV-CLAUDE-20260604-001
files_created: L3_WAVE1/PATCH1_METACOGNIK_REVIEW.md
files_changed: SESSION_REGISTRY.md (1 sessão + 1 lock)
files_not_touched: PATCH 1 candidate (RO); canônico Doc 06/09/03 (RO); candidates do audit (RO)
validation: veredito da 2ª chave + findings por checagem 1-8 + go/no-go de D; nada aplicado
next_step: se APROVA → sessão canonical_patch separada aplica A/B/C(/D); se REPROVA/PATCHES → volta ao autor
status: released
```

---

## E. Entrada de SESSION_REGISTRY proposta (o Dispatcher já registrou como `planned`)

```txt
S-P1-L3-METAREV-CLAUDE-20260604-001 | PATCH1_METACOGNIK_APPLY_GATE_REVIEW_20260604 | audit | metacognik (claude) |
  scope: read PATCH 1 candidate + fan-in audit + canônico Doc 06 §5.3/§14/§15, Doc 09 §5.5/§14, Doc 03 §5.5 (RO) + 2 source candidates (RO);
  write L3_WAVE1/PATCH1_METACOGNIK_REVIEW.md + registry | planned (depende do PATCH 1 candidate, já released)
forbidden: aplicar/editar canônico 01-28, editar o PATCH 1 candidate ou os candidates do audit, governance, patch report, SQL/UI/backend, move/rename/delete, itens HOLD
```

> **Fluxo:** Founder cola a seção **A** numa sessão fresca → Metacognik roda → devolve `PATCH1_METACOGNIK_REVIEW.md` + veredito. Se **APROVA**, o Dispatcher abre a sessão `canonical_patch` de aplicação (3ª e última etapa). Se **REPROVA/PATCHES-LEVES**, volta ao autor do PATCH 1.
