---
title: Metacognik — Revisão de Apply-Gate do PATCH 2 (2ª chave)
file: S-METACOGNIK_PATCH2_REVIEW.md
layer: auxiliary
doc_type: pmo_session_task
phase: 000_ROADMAPS
category: consolidation
status: awaiting_run
version: 0.1.0
created_at: 2026-06-09
owner: pmo_ckos
dispatcher: claude_opus_4_7 (S-USER-PMO-CLAUDE-20260609-001 → atuando como Dispatcher do PATCH 2)
session_id: S-P2-L3-METAREV-FRESH-20260609-001
role: metacognik_reviewer
depends_on: [S-USER-PMO-CLAUDE-20260609-001]   # o candidate apply-ready do PATCH 2
companion_of: PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md
two_key_context: "Founder = 1ª chave ✅ (GATE 5 = GO + AQ-IO-1 = `user`, 2026-06-09). Esta sessão decide a 2ª chave (Metacognik) sobre o TEXTO."
separation_of_duties: >
  Sessão SEPARADA e independente. O autor do PATCH 2 (claude_opus_4_7, S-USER-PMO-CLAUDE-20260609-001)
  NÃO revisa o próprio patch. Esta sessão deve rodar em **executor diferente** (Windsurf é a opção
  natural — Claude Code aqui está em quota crítica), com contexto fresco (chat novo, sem memória da
  sessão autora). Nota: o gateway OpenRouter é do RUNTIME CKOS (onde agents/skills rodam), não dos
  executores de doc-building. Windsurf usa seu próprio modelo (Claude/GPT/etc.) — não importa qual,
  desde que seja sessão fresh fora do claude_opus_4_7 autor. Read-only: NÃO aplica, NÃO edita canônico
  01-28, NÃO edita o PATCH 2 candidate nem o F1 candidate. Retorna veredito + findings.
tags: [session-task, metacognik, apply-gate, review, patch2, user-system, response-engine, l3-wave1, two-key, post-gate-5]
---

# Metacognik — Revisão de Apply-Gate do PATCH 2 (2ª chave)

> **A sessão que destrava a aplicação do PATCH 2:** "dispare a sessão de revisão do Metacognik sobre o PATCH 2".
> Revisa o **texto exato** do `PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md` (blocos A/B/C/D) e a resolução proposta de `AQ-IO-2` e `AQ-IO-3`.
> Devolve a **2ª chave**: APROVA / APROVA-COM-PATCHES-LEVES / REPROVA.
> **Não aplica.** Se aprovar, a aplicação é **outra** sessão `canonical_patch` separada (`S-USER-APPLY2-FRESH-20260609-001`, já pré-montada em `S-APPLY_PATCH2_CANONICAL.md`).
> **Rode com contexto fresco — você não é o autor do patch.**

---

## A. PROMPT PARA COLAR (template auditor 5b — Metacognik apply-gate)

```txt
You are a CKOS session under MULTI_SESSION_EXECUTION_POLICY.
- Fonte de verdade aprovada = canônico 01-28; docs 29-34 gated.
- NÃO edite canônico 01-28 nem o PATCH 2 candidate. NÃO atualize ARCHITECTURE_PATCH_REPORT.md nem 00_SYSTEM_GOVERNANCE/*.
- NÃO crie backend, UI, API, migrations, SQL, agentes runtime. read-only = só findings + veredito.
- Study/UPGRADE/candidates/canônico = leitura. Não mover/renomear/deletar nada.

ROLE: Metacognik reviewer (read-only), 2ª chave do apply-gate do PATCH 2. SESSION: S-P2-L3-METAREV-FRESH-20260609-001.
CONTEXT: Founder já deu a 1ª chave (GATE 5 = GO + AQ-IO-1 = `user`, 2026-06-09).
         Você decide a 2ª chave sobre o TEXTO do PATCH 2.
SEPARATION: o autor do PATCH 2 = claude_opus_4_7 (S-USER-PMO-CLAUDE-20260609-001). Você NÃO é ele.
         Executor recomendado: Windsurf em chat fresh (Claude Code do autor está em quota crítica).
         OpenRouter é gateway do runtime CKOS, NÃO dos executores de doc-building — ignore.

READ (nesta ordem):
  - L3_WAVE1/PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md            (o alvo — blocos A/B/C/D + resolução de AQ-IO-2/3)
  - F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md          (a fonte da promoção — confirma que A/B/C/D = só os 4 ALTA)
  - GATE5_FOUNDER_DECISION_PACKAGE.md §8                          (a 1ª chave do Founder; confirma escopo e AQs respondidas)
  - canônico-alvo (RO, casar texto exato):
      01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md §5.1 (linha 54) / §5.2 (após Workspace, antes Project)
      01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md §5.6 bloco YAML / fim do §5.6 antes do §5.7
      01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md §5.5 Agent Run (pós-PATCH 1, com next_actions já presente)
      01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md §5.8 fim / transição para §6
  - canônico cross-ref (RO, confirmar coerência):
      02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md §5.3.2 (Execution Output Envelope — para R1 ser coerente)
      02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md §5.5 (envelope no transformer registry — para R1 ser coerente)
      03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md §5.2 passo 1 (IntentSubmitted já carrega user_id desde versão atual)
      03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md §5.6 (RLS multi-tenant — para U2 não criar gap de permission)

REVIEW GOAL: virar (ou não) a 2ª chave sobre o texto exato.
  1. EXATIDÃO: cada ANCHOR e cada OLD→NEW casa LITERALMENTE com o texto atual do canônico? (apply tem de ser mecânico, sem corromper espaços, aspas, numeração)
  2. CONSTITUIÇÃO §1 (anti "nome bonito sem skill"): `User` é identidade operacional real (não nome decorativo)? As 5 `Response Behavior Policies` são critério verificável (não slogan)? Confirme.
  3. ANTI-FRAGMENTAÇÃO: a alegação "User é objeto novo distinto de Stakeholder" é correta? Verifique Doc 02 §5.2: Stakeholder é projeto-escopado (founder/owner/reviewer/client...), User é identidade persistente entre projetos. A relação Stakeholder.user_id → User.user_id refabrica algo, ou é a casa certa?
  4. ESCOPO: só ALTA (U1/U2/R1/R2)? Zero vazamento de MÉDIA (U3 aprendizado 4 níveis, U4 tribos, U5 onboarding engine, R3 gate de lacuna 3 níveis, R4 Response Contract V1, R5 User Mode vs Audit Mode)?
  5. AQ-IO-2 (`User` é objeto novo vs extensão de `Stakeholder`): a resolução proposta (objeto novo de 1ª classe + relação User⇄Stakeholder) é sólida AGORA? Há um caminho mais barato (campo `user_id` em Stakeholder) que faria o mesmo trabalho sem novo objeto?
  6. AQ-IO-3 (`user_id` em memory_object vs identity store separado): adicionar `user_id` como 4ª dimensão de escopo no `memory_object` (junto com `project_id`/`workspace_id`) é a casa certa? Há risco de quebrar RLS multi-tenant do Doc 12 §5.6?
  7. IRRADIAÇÃO P1: adicionar `User` ao Doc 02 + `user_id` ao Doc 05 + 3 campos ao Agent Run em Doc 03 + nova §5.9 em Doc 04 quebra algo downstream (Doc 06/07/08/10/11/12/13/27)? Em particular: Doc 11 §4 tabelas (precisará patch suggestion?), Doc 27 Work Orders (Work Order carrega user_id?), Doc 12 §5.6 RLS (precisa estender com user-level filter?).
  8. MECÂNICA: bump de versão (Doc 02 v1.1→v1.2; Doc 03 v1.2→v1.3; Doc 04 v1.1→v1.2; Doc 05 v1.1→v1.2; ARCHITECTURE_PATCH_REPORT v1.10.3→v1.10.4; §31 nova) descritos corretamente para a sessão de aplicação?

RETURN: veredito (APROVA = 2ª chave / APROVA-COM-PATCHES-LEVES / REPROVA);
  tabela de findings por checagem 1-8;
  go/no-go explícito de cada um dos 4 PATCHES (A/B/C/D) — qualquer um pode ser aprovado/rejeitado independentemente;
  lista de patches-leves se houver (citar linha + texto exato);
  confirmação de que a aplicação é uma sessão canonical_patch SEPARADA (S-USER-APPLY2-FRESH-20260609-001) e não esta.

CLOSE WITH: criar L3_WAVE1/PATCH2_METACOGNIK_REVIEW.md + CHECKOUT RELEASE
  (files_created: esse 1; files_changed: SESSION_REGISTRY 1 sessão + 1 lock; status: released).
```

---

## B. PERGUNTAS DO PMO → (o revisor responde no relatório)

1. **Exatidão literal:** algum bloco OLD→NEW **não** bate com o texto atual (espaço, aspas, numeração de seção, ordering de campos no YAML)? Se sim, cite linha e corrija antes de aprovar — apply mecânico não pode corromper.
2. **Reuso real vs invenção (PATCH A):** `User` realmente preenche um gap real (identidade persistente entre projetos), ou Stakeholder com `user_id` já bastaria? Prove com exemplo concreto onde Stakeholder plano não resolve.
3. **Escopo do `memory_object` (PATCH B):** adicionar `user_id` como 4ª dimensão de escopo (junto de project/workspace + curta/média/longa) viola alguma invariante do Doc 05 §5.5 (trust hierarchy) ou Doc 12 §5.6 (RLS)? Confirme com leitura.
4. **Tipagem do output (PATCH C):** `response_type` (8 valores), `depth_level` (4 valores), `reasoning_mode` (4 valores) — algum valor parece desnecessário ou faltando para cobrir o que o F1-Sprint-2/3 vai usar?
5. **Anti-padrões (PATCH D):** as 5 policies (`do_not_over_ask`, `do_not_over_explain`, `no_fake_certainty`, `assumption_transparency`, `depth_fit`) são todas **verificáveis** via eval (Doc 13)? Ou alguma é só slogan? Se slogan, recomende patch leve.
6. **Risco de pré-empção:** canonizar `User` agora **fecha** indevidamente alguma AQ-mãe ainda em aberto (taxonomia commanders vs personas, layer de policy)? Ou é ortogonal?
7. **Cross-doc consistency:** o envelope tipado (R1) é coerente com o `Execution Output Envelope` de Doc 06 §5.3.2 (PATCH 1)? Skills/transformers vão saber consumir os 3 campos novos do Agent Run?
8. **Defer PATCH 3 (MÉDIA):** algum dos 6 itens MÉDIA (U3/U4/U5/R3/R4/R5) deveria entrar **junto** no PATCH 2 por dependência hard? Argumente caso a caso.

---

## C. ← PERGUNTAS PARA O PMO/FOUNDER (BRA) · Metacognik preenche

```yaml
bra_id: BRA-METAREV-PATCH2-20260609-01
from_session: S-P2-L3-METAREV-FRESH-20260609-001
to: PMO/Dispatcher (claude_opus_4_7) + Founder
open_questions: [ (preencher após review) ]
blockers:
  - "depende do PATCH 2 candidate (já released no commit 1b13f2c)"
  - "depende do GATE 5 = GO (já decidido pelo Founder em 2026-06-09)"
recommended_next:
  - "(preencher: se APROVA → abrir sessão canonical_patch de aplicação S-USER-APPLY2-FRESH-20260609-001)"
  - "(se APROVA-COM-PATCHES-LEVES → Dispatcher ajusta candidate)"
  - "(se REPROVA → volta ao Dispatcher; itens individuais aprovados podem virar PATCH 2.5 reduzido)"
```

---

## D. CHECKOUT RELEASE · Metacognik preenche

```txt
CHECKOUT RELEASE — S-P2-L3-METAREV-FRESH-20260609-001
files_created: L3_WAVE1/PATCH2_METACOGNIK_REVIEW.md
files_changed: SESSION_REGISTRY.md (1 sessão + 1 lock)
files_not_touched: PATCH 2 candidate (RO); canônico Doc 02/03/04/05 (RO); F1 candidate (RO); GATE5 package (RO); canônico cross-ref (RO)
validation: veredito da 2ª chave + findings por checagem 1-8 + go/no-go por PATCH A/B/C/D + lista de patches-leves; nada aplicado
risks_remaining: aplicação aguarda execução em sessão canonical_patch separada (não esta); P1 mitigado por escopo cirúrgico + reuso + git rollback baseline 3c31c5d
next_step:
  - APROVA → executor fresco roda S-APPLY_PATCH2_CANONICAL.md
  - APROVA-COM-PATCHES-LEVES → Dispatcher ajusta L3_WAVE1/PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md com patches leves
  - REPROVA → volta ao Dispatcher para re-trabalhar
status: released
```

---

## E. Entrada de SESSION_REGISTRY proposta (Dispatcher registra como `planned`)

```txt
S-P2-L3-METAREV-FRESH-20260609-001 | PATCH2_METACOGNIK_APPLY_GATE_REVIEW_20260609 | audit | metacognik (fresh / non-claude_opus_4_7) |
  scope: read PATCH 2 candidate + F1 candidate + GATE5 §8 + canônico Doc 02 §5.1/5.2 (RO), Doc 05 §5.6 (RO), Doc 03 §5.5 pós-PATCH 1 (RO), Doc 04 §5.8/transição §6 (RO) + cross-ref Doc 06/09/10/12 (RO);
  write L3_WAVE1/PATCH2_METACOGNIK_REVIEW.md + registry | planned (depende do PATCH 2 candidate, já released no commit 1b13f2c)
forbidden: aplicar/editar canônico 01-28; editar o PATCH 2 candidate ou F1 candidate; tocar `00_SYSTEM_GOVERNANCE/`; `ARCHITECTURE_PATCH_REPORT.md`; SQL/UI/backend; itens MÉDIA do F1 candidate (U3/U4/U5/R3/R4/R5); move/rename/delete; rodar a aplicação canônica (essa é a próxima sessão, S-USER-APPLY2-FRESH-20260609-001)
separation: NÃO pode ser claude_opus_4_7 (autor do PATCH 2)
```

---

## F. Fluxo da 2ª chave

```txt
1. Founder cola a seção A num chat fresh **em Windsurf** (Claude Code do autor em quota crítica; OpenRouter é runtime, não doc-building)
2. Metacognik roda → produz L3_WAVE1/PATCH2_METACOGNIK_REVIEW.md com:
   - veredito (APROVA / APROVA-COM-PATCHES-LEVES / REPROVA)
   - findings 1-8
   - go/no-go por PATCH A/B/C/D (cada um pode ser independente)
3. Se APROVA total → Dispatcher dispara executor fresco rodando S-APPLY_PATCH2_CANONICAL.md
4. Se APROVA-COM-PATCHES-LEVES → Dispatcher edita PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md com os ajustes,
   depois executor fresco roda S-APPLY_PATCH2_CANONICAL.md sobre o texto corrigido
5. Se REPROVA → volta ao Dispatcher para re-trabalhar (ou abandonar PATCH 2 e propor PATCH 2.5 só com itens aprovados)
```

> **Importante:** mesmo se Metacognik aprovar, **nenhum canônico é tocado nesta sessão**. A aplicação real é a 4ª etapa da cadeia (`S-USER-APPLY2-FRESH-20260609-001`), executada por sessão fresca diferente (separação de papéis: não pode ser nem o autor, nem este auditor).
