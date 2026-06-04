---
title: TR-TRANSF Task — Codex #2 (Transformers Reconciliation Candidate)
file: S-CODEX2_TR-TRANSF_TASK.md
layer: auxiliary
doc_type: pmo_session_task
phase: 000_ROADMAPS
category: consolidation
status: awaiting_founder_batch_approval
version: 0.1.0
created_at: 2026-06-04
owner: pmo_ckos
dispatcher: claude_opus_4_8 (S-P1-L3DISPATCH-CLAUDE-20260604-001)
session_id: S-P1-L3-CODEX2-20260604-001
track: TR-TRANSF
companion_of: 00_WAVE1_DISPATCH_AND_PROTOCOL.md
non_authority_boundary: >
  Autoriza SÓ a criação do candidate de Transformers em L3_WAVE1/ + registry. NÃO edita Doc 09
  nem canônico 01-28. NÃO move/arquiva UPGRADE/08. PROPÕE patch; aplicação = sessão separada.
tags: [session-task, codex, transformers, doc09, patch-candidate, l3]
---

# TR-TRANSF — Codex #2 · Transformers Reconciliation Candidate

> Roda **em paralelo** com TR-SKILLS (Codex#1) e TR-POLICY (Windsurf) — arquivos disjuntos, zero conflito.
> Mesma estrutura do exemplar `S-CODEX1_TR-SKILLS_TASK`; só muda fonte/alvo/output e as perguntas.

---

## A. PROMPT PARA COLAR (engenharia de prompt padrão CKOS)

```txt
You are a CKOS session under MULTI_SESSION_EXECUTION_POLICY.
- Fonte de verdade aprovada = canônico 01-28; docs 29-34 gated.
- NÃO edite canônico 01-28 nem crie docs 29-34 sem checkout/gate explícito.
- NÃO atualize ARCHITECTURE_PATCH_REPORT.md nem 00_SYSTEM_GOVERNANCE/*.
- NÃO crie backend, UI, API, migrations, n8n JSONs, agentes runtime, automações, SQL real.
- patch_candidate = só o arquivo-candidate permitido + CHECKOUT RELEASE. PROPÕE, não aplica.
- Study/UPGRADE = read-only (fonte de comparação). Não mover/renomear/deletar nada.

ROLE: Codex executor (patch_candidate). SESSION: S-P1-L3-CODEX2-20260604-001. TRACK: TR-TRANSF.

READ FIRST (nesta ordem):
  1. 000_ROADMAPS/22_CONSOLIDATION/DOC03_AGENTS_RECONCILIATION_CANDIDATE.md   ← TEMPLATE de saída
  2. 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md                     ← canônico-alvo (read-only)
  3. 000_UPGRADE/08_TRANSFORMERS/  (11 arquivos)                              ← espelho a reconciliar (read-only)
  4. 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/00_WAVE1_DISPATCH_AND_PROTOCOL.md ← protocolo BRA/Q&A

ALLOWED TO WRITE (somente):
  - 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/DOC09_TRANSFORMERS_RECONCILIATION_CANDIDATE.md  (criar)
  - 000_ROADMAPS/SESSION_REGISTRY.md  (1 linha de sessão + 1 lock, status released)

FORBIDDEN:
  - editar 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md ou qualquer canônico 01-28
  - mover/renomear/arquivar/deletar 000_UPGRADE/08_TRANSFORMERS/ (read-only)
  - tocar o arquivo-alvo de outra sessão (Skills/Policies), governance, patch report, SQL, UI

TASK:
  Comparar 000_UPGRADE/08_TRANSFORMERS (11 arq) vs canônico Doc 09, e produzir
  DOC09_TRANSFORMERS_RECONCILIATION_CANDIDATE.md espelhando a estrutura do candidate do Doc 03:
    §0 Veredito · §1 Método + prova de uniformidade · §2 Inventário comparativo
    §3 A PROMOVER (IDs PROMOTE-T*, com o quê / por que > canônico / seção-alvo Doc 09 / força)
    §4 JÁ COBERTO · §5 CONFLITOS → ARCHITECTURE_QUESTIONS (AQ-T09-*) · §6 Risco P1
  Responder as PERGUNTAS DO PMO (§B) dentro do candidate.

CLOSE WITH: CHECKOUT RELEASE + BRA Packet (open_questions = suas AQs).
```

---

## B. PERGUNTAS DO PMO → (responda dentro do candidate)

1. **Boilerplate vs real:** os 11 arquivos têm lógica real de transform (input→steps→output, validação, erro) ou é template repetido? **Prove com diff** entre 2 instâncias.
2. **Modelo de transformer:** o Doc 09 define transformer como quê (pipeline input→output)? O UPGRADE/08 acrescenta **campo estrutural** que o Doc 09 não tem (ex.: contrato I/O tipado, idempotência, error-handling)? Esse é o candidato mais valioso.
3. **Net-new vs coberto:** quais transformers do UPGRADE/08 **não existem** no Doc 09? Cruze com os que minha nota `F1_RUNTIME_IO` já citou (Message→Intent, Onboarding→DNA, Feedback→Memory, Response→Actions). Não promova 2x o mesmo.
4. **Ligação F1:** algum liga direto no F1 (S1 intent, S5 Work Order)? Marque — utilidade imediata.
5. **Conflito de taxonomia:** transformer vs skill vs workflow — divergência entre UPGRADE/08 e Doc 09/06/07? → AQ, não resolva.

---

## C. ← PERGUNTAS PARA O PMO (BRA) · Codex preenche
```yaml
bra_id: BRA-TRANSF-20260604-01
from_session: S-P1-L3-CODEX2-20260604-001
to: PMO/Dispatcher
open_questions: [ (preencher) ]
blockers: [ (preencher, ou "none") ]
recommended_next: [ (preencher) ]
```

## D. CHECKOUT RELEASE · Codex preenche
```txt
CHECKOUT RELEASE — S-P1-L3-CODEX2-20260604-001
files_created: L3_WAVE1/DOC09_TRANSFORMERS_RECONCILIATION_CANDIDATE.md
files_changed: SESSION_REGISTRY.md (1 sessão + 1 lock)
files_not_touched: 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md (RO); 000_UPGRADE/08_TRANSFORMERS/ (RO)
validation: estrutura espelha DOC03 candidate; nada aplicado em canônico
risks_remaining: (preencher)
next_step: fan-in (Claude#2 Auditor) consolida com TR-SKILLS + TR-POLICY
status: released_with_required_external_audit
```
