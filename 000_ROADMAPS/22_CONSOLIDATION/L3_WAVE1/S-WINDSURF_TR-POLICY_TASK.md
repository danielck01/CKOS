---
title: TR-POLICY Task — Windsurf (Policies Reconciliation Candidate)
file: S-WINDSURF_TR-POLICY_TASK.md
layer: auxiliary
doc_type: pmo_session_task
phase: 000_ROADMAPS
category: consolidation
status: awaiting_founder_batch_approval
version: 0.1.0
created_at: 2026-06-04
owner: pmo_ckos
dispatcher: claude_opus_4_8 (S-P1-L3DISPATCH-CLAUDE-20260604-001)
session_id: S-P1-L3-WINDSURF-20260604-001
track: TR-POLICY
companion_of: 00_WAVE1_DISPATCH_AND_PROTOCOL.md
non_authority_boundary: >
  Autoriza SÓ a criação do candidate de Policies em L3_WAVE1/ + registry. Windsurf faz
  inventário + rascunho; o julgamento final (promover/cobrir) é do fan-in (Claude#2). NÃO edita
  Doc 12/04 nem canônico 01-28. NÃO move/arquiva UPGRADE/07. PROPÕE; aplicação = sessão separada.
tags: [session-task, windsurf, policies, doc12, doc04, patch-candidate, l3]
---

# TR-POLICY — Windsurf · Policies Reconciliation Candidate

> Roda **em paralelo** com TR-SKILLS (Codex#1) e TR-TRANSF (Codex#2) — arquivos disjuntos.
> ⚠️ **BAIXA CONFIANÇA (modelo grátis):** todo output aqui é **hipótese**. Faça **inventário + rascunho marcado**;
> **NÃO decida promoção** — o julgamento de mérito é do Claude#2, que **re-verifica cada item contra a fonte**
> antes de qualquer promoção. Inteligência: **medium** (verificamos, não confiamos). Conflito → AQ, não resolva.

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

ROLE: Windsurf PMO-suporte (patch_candidate, inventário+rascunho). SESSION: S-P1-L3-WINDSURF-20260604-001. TRACK: TR-POLICY.

READ FIRST (nesta ordem):
  1. 000_ROADMAPS/22_CONSOLIDATION/DOC03_AGENTS_RECONCILIATION_CANDIDATE.md   ← TEMPLATE de saída
  2. 03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md         ← canônico-alvo (read-only)
  3. 01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md                          ← canônico-alvo 2 (read-only)
  4. 000_UPGRADE/07_POLICIES/  (11 arquivos)                                  ← espelho a reconciliar (read-only)
  5. 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/00_WAVE1_DISPATCH_AND_PROTOCOL.md ← protocolo BRA/Q&A

ALLOWED TO WRITE (somente):
  - 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/DOC12_POLICIES_RECONCILIATION_CANDIDATE.md  (criar)
  - 000_ROADMAPS/SESSION_REGISTRY.md  (1 linha de sessão + 1 lock, status released)

FORBIDDEN:
  - editar Doc 12 / Doc 04 ou qualquer canônico 01-28
  - mover/renomear/arquivar/deletar 000_UPGRADE/07_POLICIES/ (read-only)
  - tocar o arquivo-alvo de outra sessão (Skills/Transformers), governance, patch report, SQL, UI
  - DECIDIR promoção contestável — registra como AQ, deixa pro fan-in

TASK:
  Comparar 000_UPGRADE/07_POLICIES (11 arq) vs Doc 12 (+ Doc 04), e produzir
  DOC12_POLICIES_RECONCILIATION_CANDIDATE.md espelhando a estrutura do candidate do Doc 03:
    §0 Veredito · §1 Método + prova de uniformidade · §2 Inventário comparativo (cada policy → Doc 12? Doc 04? net-new?)
    §3 A PROMOVER (IDs PROMOTE-P*, com o quê / por que / seção-alvo Doc 12 ou Doc 04 / força)
    §4 JÁ COBERTO · §5 CONFLITOS → ARCHITECTURE_QUESTIONS (AQ-P12-*) · §6 Risco P1
  Marcar claramente o que é rascunho/baixa-confiança para o fan-in revisar.

CLOSE WITH: CHECKOUT RELEASE + BRA Packet (open_questions = suas AQs).
```

---

## B. PERGUNTAS DO PMO → (responda dentro do candidate)

1. **Boilerplate vs real:** os 11 policies têm regra real (condição→ação→enforcement) ou é template? **Prove com diff**.
2. **Dois donos canônicos:** mapeie cada policy → **Doc 12** (security/permissões/data governance/RLS/secrets) **ou** **Doc 04** (autonomy levels, approval, batches). Onde cada uma pertence?
3. **Net-new:** quais policies **não existem** em Doc 12 nem Doc 04? Cruze com minha nota `F1_RUNTIME_IO` (PROMOTE-R2: do_not_over_ask, do_not_over_explain, no_fake_certainty, assumption_transparency, depth_fit). Não promova 2x.
4. **Já coberto:** autonomy levels 1-5 já estão no Doc 04? budget gates no Doc 24? memory validation no Doc 05? Não duplicar.
5. **Conflito de camada:** policy de runtime/segurança (Doc 12) vs policy cognitiva/comportamento (Doc 04) — onde mora cada tipo? → AQ.

---

## C. ← PERGUNTAS PARA O PMO (BRA) · Windsurf preenche
```yaml
bra_id: BRA-POLICY-20260604-01
from_session: S-P1-L3-WINDSURF-20260604-001
to: PMO/Dispatcher
open_questions: [ (preencher — esp. dúvidas Doc 12 vs Doc 04) ]
blockers: [ (preencher, ou "none") ]
recommended_next: [ (preencher) ]
```

## D. CHECKOUT RELEASE · Windsurf preenche
```txt
CHECKOUT RELEASE — S-P1-L3-WINDSURF-20260604-001
files_created: L3_WAVE1/DOC12_POLICIES_RECONCILIATION_CANDIDATE.md
files_changed: SESSION_REGISTRY.md (1 sessão + 1 lock)
files_not_touched: Doc 12 / Doc 04 (RO); 000_UPGRADE/07_POLICIES/ (RO)
validation: estrutura espelha DOC03 candidate; itens baixa-confiança marcados p/ fan-in
risks_remaining: (preencher)
next_step: fan-in (Claude#2 Auditor) faz o julgamento final + consolida com TR-SKILLS + TR-TRANSF
status: released_with_required_external_audit
```
