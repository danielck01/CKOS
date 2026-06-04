---
title: TR-SKILLS Task — Codex #1 (Skills Reconciliation Candidate)
file: S-CODEX1_TR-SKILLS_TASK.md
layer: auxiliary
doc_type: pmo_session_task
phase: 000_ROADMAPS
category: consolidation
status: awaiting_founder_batch_approval
version: 0.1.0
created_at: 2026-06-04
owner: pmo_ckos
dispatcher: claude_opus_4_8 (S-P1-L3DISPATCH-CLAUDE-20260604-001)
session_id: S-P1-L3-CODEX1-20260604-001
track: TR-SKILLS
companion_of: 00_WAVE1_DISPATCH_AND_PROTOCOL.md
non_authority_boundary: >
  Nota de tarefa para 1 sessão Codex. Autoriza SÓ a criação do candidate de Skills em
  L3_WAVE1/ + registry. NÃO edita Doc 06 nem qualquer canônico 01-28. NÃO move/arquiva
  o UPGRADE/04. PROPÕE patch; aplicação = sessão canonical_patch separada pós-Founder.
tags: [session-task, codex, skills, doc06, patch-candidate, l3]
---

# TR-SKILLS — Codex #1 · Skills Reconciliation Candidate

> **Cole o bloco da §A numa sessão Codex.** Ele se basta. Devolva preenchidas as §C (perguntas pro PMO) e §D (release).
> Roda **em paralelo** com TR-TRANSF (Codex#2) e TR-POLICY (Windsurf) — arquivos disjuntos, sem conflito.

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

ROLE: Codex executor (patch_candidate). SESSION: S-P1-L3-CODEX1-20260604-001. TRACK: TR-SKILLS.

READ FIRST (nesta ordem):
  1. 000_ROADMAPS/22_CONSOLIDATION/DOC03_AGENTS_RECONCILIATION_CANDIDATE.md   ← TEMPLATE de saída (espelhe a estrutura)
  2. 02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md                                ← canônico-alvo (read-only)
  3. 000_UPGRADE/04_SKILLS_REGISTRY/  (15 arquivos)                           ← espelho a reconciliar (read-only)
  4. 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/00_WAVE1_DISPATCH_AND_PROTOCOL.md ← protocolo BRA/Q&A

ALLOWED TO WRITE (somente):
  - 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/DOC06_SKILLS_RECONCILIATION_CANDIDATE.md  (criar)
  - 000_ROADMAPS/SESSION_REGISTRY.md  (1 linha de sessão + 1 lock, status released)

FORBIDDEN:
  - editar 02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md ou qualquer canônico 01-28
  - mover/renomear/arquivar/deletar 000_UPGRADE/04_SKILLS_REGISTRY/ (read-only)
  - tocar o arquivo-alvo de outra sessão (Transformers/Policies), governance, patch report, SQL, UI

TASK:
  Comparar 000_UPGRADE/04_SKILLS_REGISTRY (15 arq) vs canônico Doc 06, e produzir
  DOC06_SKILLS_RECONCILIATION_CANDIDATE.md espelhando a estrutura do candidate do Doc 03:
    §0 Veredito em 1 linha (PMO, direto)
    §1 Método + prova de uniformidade (o UPGRADE é template-boilerplate ou conteúdo real? mostre)
    §2 Inventário comparativo (cada skill UPGRADE → mapeia pro Doc 06? net-new? 〜parcial?)
    §3 A PROMOVER (IDs PROMOTE-S*, com: o quê, por que > canônico, seção-alvo no Doc 06, força ALTA/MÉDIA/BAIXA)
    §4 JÁ COBERTO (arquivar, sem ação)
    §5 CONFLITOS → ARCHITECTURE_QUESTIONS (AQ-S06-*) — não decidir, levantar
    §6 Risco P1 + nota de aplicação (P1 = sessão canonical_patch separada com Founder)
  Respeitar o §1 do canônico (sem "nomes/skills bonitas sem skill contratada/sem teste").
  Responder as PERGUNTAS DO PMO (§B desta nota) dentro do candidate.

CLOSE WITH: CHECKOUT RELEASE (files_created, files_changed, files_not_touched, validation,
  risks_remaining, next_step, status) + BRA Packet (open_questions = suas AQs).
```

---

## B. PERGUNTAS DO PMO → (responda dentro do candidate)

1. **Boilerplate vs real:** os 15 arquivos são template repetido (como o UPGRADE/03 era) ou há doutrina/anti-padrões/score/testes reais por skill? **Prove com diff** entre 2 instâncias.
2. **Modelo de skill:** o Doc 06 trata skill como quê (registry + allowed_tools + contrato)? O UPGRADE/04 acrescenta algum **campo estrutural** que o Doc 06 não tem (ex.: score 0-10, anti-padrões, testes, discipline-master)? Isso é o candidato mais valioso (igual o I/O Contract foi no Doc 03).
3. **Net-new vs coberto:** quais skills do UPGRADE/04 **não existem** no Doc 06 (net-new) e quais são duplicata? Liste nominalmente.
4. **Ligação F1/F2:** algum item liga direto no F1 (S3 registry de skills + policy checker)? Marque, é o de maior utilidade imediata.
5. **Conflito de taxonomia:** há divergência skill vs capability vs tool entre UPGRADE/04 e Doc 06/02/26? Se sim → AQ, não resolva.

---

## C. ← PERGUNTAS PARA O PMO (BRA) · Codex preenche

> Dúvidas de escopo/arquitetura que você devolve. Não espere resposta item-a-item: registre, siga com hipótese marcada, eu resolvo no fan-in.

```yaml
bra_id: BRA-SKILLS-20260604-01
from_session: S-P1-L3-CODEX1-20260604-001
to: PMO/Dispatcher
open_questions:
  - (Codex preenche)
blockers:
  - (Codex preenche, ou "none")
recommended_next:
  - (Codex preenche)
```

---

## D. CHECKOUT RELEASE · Codex preenche ao terminar

```txt
CHECKOUT RELEASE — S-P1-L3-CODEX1-20260604-001
files_created: 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/DOC06_SKILLS_RECONCILIATION_CANDIDATE.md
files_changed: 000_ROADMAPS/SESSION_REGISTRY.md (1 sessão + 1 lock)
files_not_touched: 02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md (canônico, read-only); 000_UPGRADE/04_SKILLS_REGISTRY/ (read-only)
validation: estrutura espelha DOC03 candidate; §1 do Doc 06 respeitado; nada aplicado em canônico
risks_remaining: (preencher)
next_step: fan-in PMO (Claude) consolida com TR-TRANSF + TR-POLICY
status: released_with_required_external_audit
```
