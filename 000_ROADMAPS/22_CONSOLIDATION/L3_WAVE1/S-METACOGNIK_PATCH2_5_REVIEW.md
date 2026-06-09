---
title: Metacognik — Revisão de Apply-Gate do PATCH 2.5 (2ª chave)
file: S-METACOGNIK_PATCH2_5_REVIEW.md
layer: auxiliary
doc_type: pmo_session_task
phase: 000_ROADMAPS
category: consolidation
status: awaiting_run
version: 0.1.0
created_at: 2026-06-09
owner: pmo_ckos
dispatcher: claude_opus_4_7 (S-F1S1-PMO-PATCH25-CLAUDE-20260609-001 → atuando como Dispatcher do PATCH 2.5)
session_id: S-P25-L3-METAREV-CLAUDE-20260609-001
role: metacognik_reviewer
depends_on:
  - S-F1S1-PMO-PATCH25-CLAUDE-20260609-001     # o candidate apply-ready do PATCH 2.5 (commit 724bfb9)
  - S-USER-APPLY2-FRESH-20260609-001            # PATCH 2 já aplicado (5d1d969) — precondition
companion_of: PATCH2_5_INTENT_SUBMITTED_RECONCILIATION_CANDIDATE.md
two_key_context: "Founder = 1ª chave ✅ (GATE 5 = GO + AQ-IO-1 = `user` + §18 user-first reframe no backend MVP plan, 2026-06-09). Esta sessão decide a 2ª chave (Metacognik) sobre o TEXTO do PATCH E."
separation_of_duties: >
  Sessão SEPARADA e independente. O autor do PATCH 2.5 (claude_opus_4_7,
  S-F1S1-PMO-PATCH25-CLAUDE-20260609-001) NÃO revisa o próprio patch. Esta sessão DEVE rodar em
  **Claude Code em chat fresh** (instância separada), com contexto novo (sem memória da sessão
  autora). **Windsurf NÃO é o executor recomendado para audit** — Windsurf fica reservado para tarefas
  de menor risco (ex: APPLY mecânico pós-2ª chave). Audit de canonical_patch tem risco de decisão
  mais alto e requer raciocínio mais forte. Read-only: NÃO aplica, NÃO edita canônico 01-28, NÃO
  edita o PATCH 2.5 candidate nem qualquer companion. Retorna veredito + findings.
tags: [session-task, metacognik, apply-gate, review, patch2-5, intent-ingress, runtime, doc10, l3-wave1, two-key, f1-s1-prereq, post-patch-2]
---

# Metacognik — Revisão de Apply-Gate do PATCH 2.5 (2ª chave)

> **A sessão que destrava a aplicação do PATCH 2.5:** "dispare a sessão de revisão do Metacognik sobre o PATCH 2.5".
> Revisa o **texto exato** do `PATCH2_5_INTENT_SUBMITTED_RECONCILIATION_CANDIDATE.md` (PATCH E = 1 substituição em linha 78 + 1 nota explicativa pós-fluxo).
> Devolve a **2ª chave**: APROVA / APROVA-COM-PATCHES-LEVES / REPROVA.
> **Não aplica.** Se aprovar, a aplicação é **outra** sessão `canonical_patch` separada (a ser nomeada `S-APPLY2_5-FRESH-20260609-001`).
> **Rode com contexto fresco em Claude Code — você não é o autor do patch, e Windsurf não faz audit.**

---

## A. PROMPT PARA COLAR (template auditor 5b — Metacognik apply-gate)

```txt
You are a CKOS session under MULTI_SESSION_EXECUTION_POLICY.
- Fonte de verdade aprovada = canônico 01-28; docs 29-34 gated.
- NÃO edite canônico 01-28 nem o PATCH 2.5 candidate. NÃO atualize ARCHITECTURE_PATCH_REPORT.md nem 00_SYSTEM_GOVERNANCE/*.
- NÃO crie backend, UI, API, migrations, SQL, agentes runtime. read-only = só findings + veredito.
- Study/UPGRADE/candidates/canônico = leitura. Não mover/renomear/deletar nada.

ROLE: Metacognik reviewer (read-only), 2ª chave do apply-gate do PATCH 2.5. SESSION: S-P25-L3-METAREV-CLAUDE-20260609-001.
CONTEXT: Founder já deu a 1ª chave (GATE 5 = GO + AQ-IO-1 = `user` em 2026-06-09; §18 user-first reframe no backend MVP plan).
         PATCH 2 (User-in + Response-out) já aplicado em 2026-06-09 (commit 5d1d969).
         Você decide a 2ª chave sobre o TEXTO do PATCH E (Doc 10 §5.2 IntentSubmitted reconciliation).
SEPARATION: o autor do PATCH 2.5 = claude_opus_4_7 (S-F1S1-PMO-PATCH25-CLAUDE-20260609-001). Você NÃO é ele.
         Executor recomendado: **Claude Code em chat fresh** (NÃO Windsurf — Windsurf é reservado pra APPLY mecânico,
         audit precisa de raciocínio mais forte). Outra instância de Claude Code, contexto novo.

READ (nesta ordem):
  - L3_WAVE1/PATCH2_5_INTENT_SUBMITTED_RECONCILIATION_CANDIDATE.md  (o alvo — PATCH E completo + resolução)
  - 000_ROADMAPS/22_CONSOLIDATION/03_BACKEND_MVP_THIN_SLICE_PLAN.md §18  (origem do reframe user-first; spec de IntentSubmitted em §18.2)
  - L3_WAVE1/PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md               (PATCH 2 — confirma que User canônico já existe em Doc 02 §5.2)
  - GATE5_FOUNDER_DECISION_PACKAGE.md §8                             (1ª chave Founder; AQ-IO-1 = user resolvida)
  - canônico-alvo (RO, casar texto exato):
      03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md §5.2 (linhas 75-95 — fluxo de 14 passos, especialmente linha 78 IntentSubmitted)
      03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md §5.3 (linha 98 — envelope fields do Event Log)
  - canônico cross-ref (RO, confirmar coerência pós-PATCH 2):
      01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md §5.2 (User como objeto 1ª classe — PATCH 2 PROMOTE-U1)
      01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md §5.6.1 (memória escopada user_id — PATCH 2 PROMOTE-U2)
      03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md linhas 139-148 (users + user_profiles — confirmar que ainda não tem campos PATCH 2; defer PATCH 3 OK)
      03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md §5.6 (RLS multi-tenant — confirmar que ingress decoplado de project_id não quebra escopo)

REVIEW GOAL: virar (ou não) a 2ª chave sobre o texto exato.
  1. EXATIDÃO: o OLD da linha 78 (`1.  CommandBar emite IntentSubmitted{text, project_id, user_id, section}`) casa LITERALMENTE com Doc 10 §5.2 linha 78 atual? Espaços, indentação (`  ` após `1.`), aspas, ordem dos campos no `{}` — tudo bate? E o ANCHOR de E.2 (após fechamento de ` ```txt ` e antes do parágrafo "Cada seta acima é **um evento no event log**") está corretamente localizado?
  2. CONSTITUIÇÃO §1 + ANTI-FRAGMENTAÇÃO: a substituição **amplia** o domínio de `IntentSubmitted` sem remover capacidade (CommandBar continua válido como exemplo; `project_id` continua aceito quando presente)? Ou alguma semântica do canônico atual é silenciosamente perdida?
  3. COERÊNCIA COM §18.2 DO BACKEND PLAN: o payload novo (`{intent_text, user_id, project_id?, context_ref?, section?}`) cobre 100% dos campos REQUIRED/OPTIONAL de §18.2 (linhas 316-324)? §18.2 também menciona `workspace_id REQUIRED, occurred_at REQUIRED, correlation_id REQUIRED` — o candidate justifica não duplicá-los citando Doc 10 §5.3 envelope; essa justificativa é sólida ou cria gap de leitura para quem ler só §5.2?
  4. RENOMEAR `text` → `intent_text`: a mudança de nome quebra alguma referência cruzada existente? Verifique se `text` (como campo de IntentSubmitted) aparece em Doc 06/07/09/11/13/15/16 — se houver, é patch leve ou bloqueador?
  5. CROSS-REF PATCH 2: a nota explicativa (E.2) referencia `Doc 02 §5.2` e `Doc 05 §5.6.1` (PATCH 2 PROMOTE-U1/U2) — os anchors estão corretos pós-PATCH 2 (commit 5d1d969)?
  6. RLS MULTI-TENANT (Doc 12 §5.6): tornar `project_id` opcional na 1ª intenção introduz um buraco de escopo (evento `IntentSubmitted` sem `project_id` ainda tem `workspace_id` REQUIRED via envelope — confirme que RLS continua aplicável só no nível workspace)?
  7. ESCOPO: só PATCH E entra? Zero vazamento de: (a) enriquecimento Doc 11 `users` table (defer PATCH 3); (b) adição de `correlation_id`/`occurred_at`/`workspace_id` no payload (envelope já cobre); (c) `ProjectInferred` event sendo definido aqui (mencionado na nota como cross-ref pra §18.2, mas não definido no PATCH E)?
  8. MECÂNICA: bump de versão (Doc 10 v1.1.1 → v1.2.0; ARCHITECTURE_PATCH_REPORT v1.10.4 → v1.10.5; §32 nova) descritos corretamente para a sessão de aplicação?

RETURN: veredito (APROVA = 2ª chave / APROVA-COM-PATCHES-LEVES / REPROVA);
  tabela de findings por checagem 1-8;
  go/no-go explícito do PATCH E (único patch — independente);
  lista de patches-leves se houver (citar linha + texto exato);
  confirmação de que a aplicação é uma sessão canonical_patch SEPARADA (nomear `S-APPLY2_5-FRESH-20260609-001`) e não esta.

CLOSE WITH: criar L3_WAVE1/PATCH2_5_METACOGNIK_REVIEW.md + CHECKOUT RELEASE
  (files_created: esse 1; files_changed: SESSION_REGISTRY 1 sessão + 1 lock; status: released).
```

---

## B. PERGUNTAS DO PMO → (o revisor responde no relatório)

1. **Exatidão literal:** o OLD da linha 78 bate **byte-a-byte** com o canônico (indentação `1.  ` com 2 espaços, sem trailing whitespace)? Algum espaço errado no NEW (`Ingress (CommandBar | backend API | webhook)` — pipes com 1 espaço de cada lado)?
2. **Renomear `text` → `intent_text`:** vasculhe `text` em referências cross-doc. Se Doc 11 (`context_packs.intent`), Doc 13 (eval kinds), Doc 15 (CommandBar UX) usarem o nome antigo, isso vira patch leve em PATCH 2.5 ou patch independente? Confirme escopo.
3. **Decoplagem de CommandBar:** Doc 14-16 (Product System) descrevem CommandBar como UX primário. Ao escrever `Ingress (CommandBar | backend API | webhook)`, há risco de leitor entender que API/webhook competem com CommandBar (em vez de complementar)? Sugira fraseado alternativo se for ambíguo.
4. **`section?` agora opcional:** `section` era UI-specific (qual seção da CommandBar emitiu). Mantê-lo opcional é correto, ou deveria sair de `IntentSubmitted` e virar metadado de origem? Justifique.
5. **Envelope vs payload (Doc 10 §5.3):** confirmando que `correlation_id`/`occurred_at`/`workspace_id`/`actor` ficam em `event` table (§5.3 linha 98), o leitor que olha **só** §5.2 entende que esses campos existem implicitamente? Ou a nota E.2 deveria reforçar isso?
6. **AQ-IO-1 = `user` post-condição:** este PATCH 2.5 fecha o último loop do reframe user-first (Doc 02 + Doc 05 já feitos via PATCH 2; Doc 10 agora; Doc 11 defer PATCH 3)? Algo mais ainda fica solto pra Sprint 1 arrancar sem caveat?
7. **Risco F1-S1:** se PATCH 2.5 NÃO for aplicado, o que exatamente vira problema em S1? Vale a pena PATCH 2.5 OU aceitar o gap como caveat documentado em S1 charter?
8. **Defer real:** algum item pendente do reframe user-first (algum cantinho de Doc 06/07/08/12/13/14/15/16/27) deveria entrar **junto** no PATCH 2.5 por dependência hard? Argumente caso a caso (suspeitos: Doc 14/15 CommandBar UX, Doc 27 Work Order carrega user_id?).

---

## C. ← PERGUNTAS PARA O PMO/FOUNDER (BRA) · Metacognik preenche

```yaml
bra_id: BRA-METAREV-PATCH25-20260609-01
from_session: S-P25-L3-METAREV-CLAUDE-20260609-001
to: PMO/Dispatcher (claude_opus_4_7) + Founder
open_questions: [ (preencher após review) ]
blockers:
  - "depende do PATCH 2.5 candidate (já released no commit 724bfb9)"
  - "depende do PATCH 2 aplicado (commit 5d1d969 — User canônico precondition)"
  - "depende do GATE 5 = GO + AQ-IO-1 = user (Founder, 2026-06-09)"
recommended_next:
  - "(preencher: se APROVA → abrir sessão canonical_patch de aplicação S-APPLY2_5-FRESH-20260609-001)"
  - "(se APROVA-COM-PATCHES-LEVES → Dispatcher ajusta candidate)"
  - "(se REPROVA → volta ao Dispatcher; pode virar PATCH 2.5-rev reduzido ou ser absorvido em F1 Sprint 1 charter como caveat)"
```

---

## D. CHECKOUT RELEASE · Metacognik preenche

```txt
CHECKOUT RELEASE — S-P25-L3-METAREV-CLAUDE-20260609-001
files_created: L3_WAVE1/PATCH2_5_METACOGNIK_REVIEW.md
files_changed: SESSION_REGISTRY.md (1 sessão + 1 lock)
files_not_touched: PATCH 2.5 candidate (RO); canônico Doc 10 §5.2/§5.3 (RO); Doc 11 users (RO); §18 backend plan (RO); PATCH 2 candidate (RO histórico); canônico cross-ref Doc 02/05/12 (RO)
validation: veredito da 2ª chave + findings por checagem 1-8 + go/no-go do PATCH E + lista de patches-leves; nada aplicado
risks_remaining: aplicação aguarda execução em sessão canonical_patch separada (não esta); P1 mitigado por escopo cirúrgico (1 linha + 1 parágrafo) + aditivo semântico + git rollback baseline 724bfb9
next_step:
  - APROVA → executor fresco (Windsurf OK aqui — tarefa mecânica de menor risco) roda APPLY de Doc 10 §5.2
  - APROVA-COM-PATCHES-LEVES → Dispatcher ajusta L3_WAVE1/PATCH2_5_INTENT_SUBMITTED_RECONCILIATION_CANDIDATE.md com patches leves
  - REPROVA → volta ao Dispatcher para re-trabalhar (ou aceitar gap como caveat em F1 Sprint 1 charter)
status: released
```

---

## E. Entrada de SESSION_REGISTRY proposta (Dispatcher registra como `planned`)

```txt
S-P25-L3-METAREV-CLAUDE-20260609-001 | PATCH2_5_METACOGNIK_APPLY_GATE_REVIEW_20260609 | audit | metacognik (claude fresh) |
  scope: read PATCH 2.5 candidate + §18 backend plan + PATCH 2 candidate + GATE5 §8 + canônico Doc 10 §5.2/§5.3 (RO),
  cross-ref Doc 02 §5.2/Doc 05 §5.6.1/Doc 11 users/Doc 12 §5.6 (RO);
  write L3_WAVE1/PATCH2_5_METACOGNIK_REVIEW.md + registry | planned (depende do PATCH 2.5 candidate, já released no commit 724bfb9)
forbidden: aplicar/editar canônico 01-28; editar o PATCH 2.5 candidate; tocar `00_SYSTEM_GOVERNANCE/`; `ARCHITECTURE_PATCH_REPORT.md`;
  SQL/UI/backend; bundle de outros patches com este; move/rename/delete; rodar a aplicação canônica (essa é a próxima sessão, S-APPLY2_5-FRESH-20260609-001)
separation: NÃO pode ser claude_opus_4_7 autor (S-F1S1-PMO-PATCH25-CLAUDE-20260609-001); DEVE ser Claude Code fresh (NÃO Windsurf — audit em Claude per feedback_metacognik_executor)
```

---

## F. Fluxo da 2ª chave

```txt
1. Founder cola a seção A num chat **fresh em Claude Code** (instância separada do autor; NÃO Windsurf)
2. Metacognik roda → produz L3_WAVE1/PATCH2_5_METACOGNIK_REVIEW.md com:
   - veredito (APROVA / APROVA-COM-PATCHES-LEVES / REPROVA)
   - findings 1-8
   - go/no-go do PATCH E (único)
3. Se APROVA → Dispatcher dispara executor fresco (Windsurf aceitável aqui — APPLY mecânico de 1 substituição + 1 inserção) rodando o APPLY de Doc 10 §5.2 + bump v1.1.1→v1.2.0 + §32 em ARCHITECTURE_PATCH_REPORT.md (v1.10.4→v1.10.5)
4. Se APROVA-COM-PATCHES-LEVES → Dispatcher edita PATCH2_5_INTENT_SUBMITTED_RECONCILIATION_CANDIDATE.md com os ajustes, depois executor fresco aplica sobre o texto corrigido
5. Se REPROVA → volta ao Dispatcher para re-trabalhar (ou abandonar PATCH 2.5 e absorver o gap como caveat documentado no F1 Sprint 1 charter)
```

> **Importante:** mesmo se Metacognik aprovar, **nenhum canônico é tocado nesta sessão**. A aplicação real é a 3ª etapa da cadeia (`S-APPLY2_5-FRESH-20260609-001`), executada por sessão fresca diferente (separação de papéis: não pode ser nem o autor, nem este auditor).

> **Diferença vs PATCH 2:** o auditor desta vez **deve ser Claude Code fresh, não Windsurf** (per [[feedback-metacognik-executor]] — Windsurf reservado pra tarefas de menor risco como APPLY mecânico; audit precisa de raciocínio mais forte). Windsurf continua aceitável para a etapa 3 (APPLY).
