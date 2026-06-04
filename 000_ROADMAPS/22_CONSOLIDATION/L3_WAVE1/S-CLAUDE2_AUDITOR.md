---
title: Claude #2 — Auditor (ordena × audita pro Founder)
file: S-CLAUDE2_AUDITOR.md
layer: auxiliary
doc_type: pmo_session_task
phase: 000_ROADMAPS
category: consolidation
status: awaiting_founder_batch_approval
version: 0.1.0
created_at: 2026-06-04
owner: pmo_ckos
dispatcher: claude_opus_4_8 (S-P1-L3DISPATCH-CLAUDE-20260604-001)
session_id: S-P1-L3-CLAUDE2-20260604-001
role: auditor
depends_on: [S-P1-L3-CODEX1, S-P1-L3-CODEX2, S-P1-L3-WINDSURF]  # os 3 releases
companion_of: 00_WAVE1_DISPATCH_AND_PROTOCOL.md
non_authority_boundary: >
  Sessão de auditoria read-only. Retorna findings/veredito; NÃO aplica patch, NÃO edita
  canônico 01-28 nem os 3 candidates, NÃO aprova (Founder decide). Produz síntese Founder-facing.
tags: [session-task, claude, auditor, fan-in, slot2, l3]
---

# Claude #2 — Auditor · ordena × audita pro Founder (Slot 2 do Runbook)

> **A sessão que você pediu:** "ele ordena × audita pro Founder". Lê os 3 candidates produzidos
> pelos escritores, **ordena** o que promover por severidade/força, **audita** canonical-readiness,
> **agrega** as ARCHITECTURE_QUESTIONS, e entrega **um** pacote pro Founder decidir.
> Roda **depois** dos 3 releases (rolling: pode auditar cada candidate assim que pousa).

---

## A. PROMPT PARA COLAR (engenharia de prompt padrão CKOS — template auditor 5b)

```txt
You are a CKOS session under MULTI_SESSION_EXECUTION_POLICY.
- Fonte de verdade = canônico 01-28. Você NÃO edita canônico, NÃO edita os 3 candidates, NÃO aplica patch.
- read-only = só findings + síntese. Study/UPGRADE/canônico = leitura.

ROLE: Claude Code auditor (read-only). SESSION: S-P1-L3-CLAUDE2-20260604-001.
READ:
  - L3_WAVE1/DOC06_SKILLS_RECONCILIATION_CANDIDATE.md       (Codex#1)
  - L3_WAVE1/DOC09_TRANSFORMERS_RECONCILIATION_CANDIDATE.md (Codex#2)
  - L3_WAVE1/DOC12_POLICIES_RECONCILIATION_CANDIDATE.md     (Windsurf)
  - canônico-alvo p/ readiness (RO): Doc 06, Doc 09, Doc 12, Doc 04
  - F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md (cruzar net-new que já mapeei)
AUDIT GOAL: ordenar × auditar para o Founder.
  1. CONSOLIDAR: lista única de A-PROMOVER das 3 trilhas, deduplicada.
  2. ORDENAR: por força (ALTA/MÉDIA/BAIXA) × utilidade no F1 × risco. Top promotions primeiro.
  3. CANONICAL-READINESS: cada promoção respeita o §1 do doc-alvo? viola constituição? fura GATE 5?
  4. AGREGAR: todas as ARCHITECTURE_QUESTIONS (AQ-S06/AQ-T09/AQ-P12) num bloco, sem decidir.
  5. CRUZAR com F1_RUNTIME_IO (evitar promover 2x o mesmo net-new que já está lá).
RETURN: veredito; tabela ordenada A-PROMOVER (id, doc-alvo, força, readiness); AQs agregadas;
  o que está pronto p/ canonical_patch vs o que espera GATE 5; recomendação pro Founder (go/hold por item).
CLOSE WITH: criar L3_WAVE1/WAVE1_FANIN_AUDIT_FOR_FOUNDER.md + CHECKOUT RELEASE (files_changed: esse 1; status: released).
```

## B. PERGUNTAS DO PMO → (o auditor deve responder na síntese)

1. **Dedup cross-track:** algum item aparece em 2 trilhas (ex.: uma policy que também é skill)? Consolide.
2. **Anti-bloat:** algum escritor despejou boilerplate como "promoção"? Recuse, cite.
3. **Constituição:** alguma promoção cria "nome bonito sem skill/teste" (§1 Doc 03/06)? Sinalize.
4. **GATE 5:** algo aqui depende do backend não-decidido? Marque como hold-GATE-5 (não promover já).
5. **Ordem pro Founder:** qual a sequência ótima de aplicação (qual canonical_patch primeiro)?
6. **Windsurf = modelo grátis (baixa confiança):** RE-VERIFIQUE cada item do candidate de Policies (TR-POLICY) contra `000_UPGRADE/07_POLICIES/` + Doc 12/04. Trate como rascunho; só promova o que você confirmar na fonte. Você é o dono do julgamento de Policies, não o Windsurf.

## C. ← PERGUNTAS PARA O PMO/FOUNDER (BRA) · Claude#2 preenche
```yaml
bra_id: BRA-AUDIT-20260604-01
from_session: S-P1-L3-CLAUDE2-20260604-001
to: PMO/Dispatcher + Founder
open_questions: [ (preencher) ]
blockers: [ "depende dos 3 releases dos escritores" ]
recommended_next: [ (preencher: ordem de canonical_patch) ]
```

## D. CHECKOUT RELEASE · Claude#2 preenche
```txt
CHECKOUT RELEASE — S-P1-L3-CLAUDE2-20260604-001
files_created: L3_WAVE1/WAVE1_FANIN_AUDIT_FOR_FOUNDER.md
files_changed: SESSION_REGISTRY.md (1 sessão + 1 lock)
files_not_touched: os 3 candidates (RO); canônico Doc 06/09/12/04 (RO)
validation: nada aplicado; síntese ordenada + AQs agregadas + readiness por item
next_step: Founder decide go/hold por promoção → sessões canonical_patch separadas
status: released
```
