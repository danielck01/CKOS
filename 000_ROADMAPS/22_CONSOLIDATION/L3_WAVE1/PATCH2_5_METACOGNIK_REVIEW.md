---
title: PATCH 2.5 — Metacognik Review (2ª chave do apply-gate)
file: PATCH2_5_METACOGNIK_REVIEW.md
layer: auxiliary
doc_type: pmo_metacognik_review
phase: 000_ROADMAPS
category: consolidation
status: released
version: 0.1.0
created_at: 2026-06-09
owner: pmo_ckos
reviewer: claude_fresh_session
session_id: S-P25-L3-METAREV-CLAUDE-20260609-001
review_of: PATCH2_5_INTENT_SUBMITTED_RECONCILIATION_CANDIDATE.md
author_session: S-F1S1-PMO-PATCH25-CLAUDE-20260609-001  # claude_opus_4_7 — separação de papéis preservada (autor ≠ reviewer)
two_key_context: "Founder = 1ª chave ✅ (GATE 5 = GO + AQ-IO-1 = `user`, 2026-06-09). Esta revisão = 2ª chave sobre o TEXTO."
target_application_session: S-APPLY2_5-FRESH-20260609-001  # sessão canonical_patch separada (NÃO esta, NÃO a autora)
tags: [metacognik, apply-gate, review, patch25, intent-submitted, doc10, l3-wave1, two-key, post-gate-5, post-patch-2, released]
---

# PATCH 2.5 — Metacognik Review (2ª chave do apply-gate)

> **Veredito:** **APROVA-COM-PATCHES-LEVES** (2ª chave condicional)
> **Data:** 2026-06-09
> **Sessão:** S-P25-L3-METAREV-CLAUDE-20260609-001 (Claude Code fresh, separado do autor `claude_opus_4_7` da sessão `S-F1S1-PMO-PATCH25-CLAUDE-20260609-001`)
> **Executor escolhido:** Claude Code fresh (per [[feedback-metacognik-executor]] — audit em Claude; Windsurf reservado para APPLY mecânico)

---

## 1. Veredito

**APROVA-COM-PATCHES-LEVES** — PATCH E (1 substituição + 1 inserção em Doc 10 §5.2) está semanticamente correto e apply-ready, MAS a aplicação como descrita criaria uma inconsistência canônica entre Doc 10 e Doc 15 (Command Center Architecture).

**Um patch-leve OBRIGATÓRIO** precisa ser adicionado à mesma sessão `canonical_patch` de aplicação:

- **PL-01** — Reconciliar Doc 15 linha 153 (`04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md §5.1` "Mapeamento direto a doc 10 §5.2") com a nova forma de `IntentSubmitted`. Detalhes em §3 abaixo.

**Três observações não-bloqueantes** (defer para PATCH 3 / não impedem APPLY):

- **F-01** — `§5.1` de Doc 10 lista 5 fontes de ingress (`CommandBar / API / Agent / Scheduler / Webhook`); E.1 lista 3 (`CommandBar | backend API | webhook`). Agent/Scheduler omitidos do exemplo. Coerente com foco user-first do patch (Agent/Scheduler são ingress de sistema, não humano), mas merece clarificação futura.
- **F-02** — Política RLS para eventos com `project_id IS NULL` (caso novo destravado pelo PATCH 2.5) precisa cláusula explícita em Doc 12 §5.6. Defer PATCH 3 (Doc 11/12 update).
- **F-03** — `project_id` aparece tanto em envelope §5.3 quanto em payload (`project_id?`). Duplicação **herdada** do canônico atual (linha 78 original já tinha) — PATCH 2.5 não regride, só preserva. Consolidação futura.

**Sem PL-01, REPROVO.** Com PL-01 adicionado à sessão de APPLY, **APROVO** (2ª chave dada).

---

## 2. Tabela de findings por checagem (1–8)

| # | Checagem | Resultado | Detalhe |
|---|---|---|---|
| 1 | EXATIDÃO (OLD literal + anchor E.2) | ✅ **PASS** | Linha 78 verificada por Read direta: casa LITERAL (`1.  CommandBar emite IntentSubmitted{text, project_id, user_id, section}` — incluindo dois espaços após `1.`). Anchor E.2: linha 92 = closing ` ``` `; linha 93 = vazia; linha 94 = `Cada seta acima é **um evento no event log**`. Anchors corretos. |
| 2 | CONSTITUIÇÃO + ANTI-FRAGMENTAÇÃO | ✅ **PASS** | Substituição **aditiva**: CommandBar continua exemplo válido (1º item da lista); `project_id` continua aceito (apenas opcional); `text` → `intent_text` é rename, não remoção. Coerente com Doc 10 §5.1 INGRESS que já lista múltiplas origens. P4 (CommandBar centro operacional) não é violada — nota E.2 explicita que CommandBar permanece origem canônica via Doc 14-16. |
| 3 | COERÊNCIA COM §18.2 (linhas 316-324) | ✅ **PASS** | Payload `{intent_text, user_id, project_id?, context_ref?, section?}` cobre 100% dos REQUIRED + OPTIONAL do §18.2 que pertencem ao payload. `workspace_id`/`occurred_at`/`correlation_id` corretamente NÃO duplicados — envelope §5.3 (linha 98) é fonte literal: `event_id, workspace_id, project_id, type, payload, actor, causation_id, correlation_id, occurred_at`. Justificativa do candidate sólida + nota E.2 explicita "Envelope fields seguem §5.3 — não precisam ser repetidos" → gap de leitura coberto. |
| 4 | RENAME `text` → `intent_text` cross-refs | ⚠️ **PATCH-LEVE OBRIGATÓRIO (PL-01)** | Grep `IntentSubmitted\{` no canônico encontrou **Doc 15 linha 153** com schema literal: `IntentSubmitted{text, project_id, user_id, section, mode?, slash_command?, mentioned_agent?}` — explicitamente "Mapeamento direto a doc 10 §5.2" (Doc 15 §5.1, linha 149). Sem patch em Doc 15, fica `text` (Doc 15) vs `intent_text` (Doc 10) — fragmentação. Demais ocorrências em Docs 11/14/16/17/18/21 são references soltas (não schemas literais) — não bloqueiam. Lista de matches em §4 abaixo. |
| 5 | CROSS-REF PATCH 2 (anchors E.2) | ✅ **PASS** | Doc 02 §5.2 linha 62 = `User` PROMOTE-U1 confirmado pós-PATCH 2 (commit `5d1d969`). Doc 05 §5.6.1 linha 115 = "Escopo de memória: project, workspace, user (PROMOTE-U2)" confirmado. Ambos anchors da nota E.2 corretos. |
| 6 | RLS multi-tenant (Doc 12 §5.6) | ✅ **PASS (com flag F-02 deferred)** | `workspace_id` REQUIRED no envelope §5.3 → RLS workspace-level intacta. Doc 11 §7 (linha 217-232) **não força** `project_id NOT NULL` na tabela `events` → inserções com `project_id = NULL` são fisicamente possíveis. Token de sessão (Doc 12 linha 95) carrega `org_id + workspace_id + project_id` mínimo — `project_id` NULL é caso novo que merece cláusula RLS explícita ("eventos sem project_id visíveis a actor=user"), defer PATCH 3 (não bloqueia 2.5). |
| 7 | ESCOPO (zero vazamento) | ✅ **PASS** | (a) Doc 11 `users` (linhas 139-143) e `user_profiles` (145-147) confirmados SEM campos PATCH 2 (`operating_dna_ref?`, `tribes_scored?`, etc.) → defer PATCH 3 respeitado. (b) Payload E.1 NÃO inclui `correlation_id/occurred_at/workspace_id` → envelope-only respeitado. (c) `ProjectInferred` aparece na nota E.2 só como cross-ref textual a §18.2 do backend plan; NÃO é definido como evento novo em Doc 10. Escopo cirúrgico confirmado. |
| 8 | MECÂNICA (versões + relatórios) | ✅ **PASS** | Doc 10 atual `version: 1.1.1` (linha 6) → v1.2.0 (minor bump, semântica de "novo campo opcional" → minor). `ARCHITECTURE_PATCH_REPORT.md` atual `version: 1.10.4` (linha 6) → v1.10.5. §31 = PATCH 2 (linha 2245, registrada). §32 nova = PATCH 2.5, slot livre. `released_with_required_external_audit` é o status correto (preserva passo de validação). |

---

## 3. PL-01 (Patch-leve OBRIGATÓRIO) — Reconciliação Doc 15 linha 153

**Justificativa:** Doc 15 §5.1 linha 149 declara textualmente "Mapeamento direto a doc 10 §5.2". Sem PL-01, PATCH 2.5 cria a fragmentação que ele próprio se propõe a eliminar (Princípio anti-fragmentação citado no BRA do candidate, linha 131).

**Arquivo:** `04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md`

**Linha 153 (dentro do bloco ` ```txt ` que começa na linha 151).**

**SUBSTITUIR:**
```
              IntentSubmitted{text, project_id, user_id, section, mode?, slash_command?, mentioned_agent?}
```
**POR:**
```
              IntentSubmitted{intent_text, user_id, project_id?, context_ref?, section?, mode?, slash_command?, mentioned_agent?}
```

**Justificativa do shape escolhido:**
- Base alinhada com Doc 10 §5.2 pós-PATCH E.1 (mesma ordem, mesmas opcionalidades para os 5 primeiros campos)
- 3 campos UI-specific do Command Center preservados como sufixo (`mode?`, `slash_command?`, `mentioned_agent?`) — essas são extensões legítimas da camada Product (Doc 14-16), não conflito com o contrato runtime
- Zero remoção de capacidade

**Demais linhas de Doc 15** (lines 200, 212, 236, 248, 260, 274, 401, 443, 464, 511, 525-545, 739) usam padrão shorthand `IntentSubmitted{mode: X}` — só citam o campo `mode` como discriminador de dispatch. Essas linhas NÃO precisam patch (não escrevem `text` literal).

**Bump de versão necessário em Doc 15:** verificar e bumpar como `minor` (alinhamento com Doc 10 v1.2.0).

**Outras docs verificadas — SEM patch necessário:**
- Doc 11 (Data Model) — `IntentSubmitted` mencionado em update trigger (linha 948); nenhum schema literal com `text`
- Doc 14 (Project Dashboard) — `IntentSubmitted (com project_id e context_snapshot)` (linha 662) é descrição contextual de happy-path Dashboard, não schema; coerente com `project_id?` (presente quando vem do Dashboard)
- Doc 16 (Node Canvas) — só refs por nome
- Docs 17/18/21 — só refs por nome ou shorthand de evento

---

## 4. Go/no-go explícito do PATCH E

| Componente | Status |
|---|---|
| **PATCH E.1** (Doc 10 §5.2 linha 78 — substituição) | ✅ **GO** (com PL-01 acoplado) |
| **PATCH E.2** (Doc 10 §5.2 nota explicativa após linha 92) | ✅ **GO** |
| **PL-01** (Doc 15 linha 153 — patch-leve obrigatório) | ✅ **GO + obrigatório acoplar à sessão APPLY** |

**Sem PL-01:** REPROVA — PATCH 2.5 cria inconsistência canônica que viola seu próprio princípio anti-fragmentação.
**Com PL-01:** APROVA — escopo cirúrgico preservado, aditivo semântico, reversível por `git revert`, zero remoção de capacidade.

---

## 5. Patches-leves consolidados (uma única tabela para a sessão APPLY)

| ID | Tipo | Arquivo | Linha alvo | Ação | Bloqueante? |
|---|---|---|---|---|---|
| E.1 | core | `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md` | 78 | SUBSTITUIR (texto literal em §2 do candidate) | sim — é o patch principal |
| E.2 | core | `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md` | após 92, antes 94 | INSERIR nota explicativa | sim — é o patch principal |
| PL-01 | patch-leve | `04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md` | 153 | SUBSTITUIR (texto em §3 desta review) | **sim — obrigatório acoplar à mesma sessão** |
| (futuro) | F-01 | `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md` | E.1 nota | Considerar listar Agent/Scheduler como ingress + esclarecer contrato system-originated | não — defer PATCH 3 |
| (futuro) | F-02 | `03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md` | §5.6 | Cláusula RLS explícita para events com `project_id IS NULL` | não — defer PATCH 3 |
| (futuro) | F-03 | `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md` | §5.3 + §5.2 | Consolidar duplicação `project_id` envelope vs payload | não — defer (herança do canônico anterior) |

---

## 6. Confirmação de aplicação em sessão SEPARADA

A aplicação deste patch **NÃO é esta sessão** (S-P25-L3-METAREV-CLAUDE-20260609-001 = read-only Metacognik review) e **NÃO é a sessão autora** (S-F1S1-PMO-PATCH25-CLAUDE-20260609-001 = `claude_opus_4_7` que escreveu o candidate).

**Sessão de aplicação recomendada:** `S-APPLY2_5-FRESH-20260609-001`
- **Tipo:** `canonical_patch`
- **Executor recomendado:** Windsurf fresh (APPLY mecânico per [[feedback-metacognik-executor]] — Windsurf é o executor para tarefas mecânicas; Claude reservado para audit)
- **Checkout lock escopado a:**
  - `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md` (PATCH E.1 + E.2)
  - `04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md` (PL-01)
  - `ARCHITECTURE_PATCH_REPORT.md` (§32 nova; v1.10.4 → v1.10.5)
  - `000_ROADMAPS/SESSION_REGISTRY.md` (entry de sessão + lock + release)
- **Bumps de versão:** Doc 10 v1.1.1 → v1.2.0 (minor); Doc 15 minor bump (conferir version atual e incrementar minor); `ARCHITECTURE_PATCH_REPORT.md` v1.10.4 → v1.10.5
- **Status final:** `released_with_required_external_audit`

A separação de papéis das duas chaves é preservada: Founder (chave 1 ✅) ≠ Metacognik (chave 2 ✅ condicional ao PL-01) ≠ Autor do candidate (`claude_opus_4_7`) ≠ Executor da aplicação (Windsurf).

---

## 7. Notas finais

- A divergência Doc 10 ↔ Doc 15 (descoberta nesta revisão) é exatamente o tipo de gap que o PATCH 2.5 existe para fechar. Acoplar PL-01 mantém o patch consistente com sua própria tese (anti-fragmentação).
- A análise RLS (Check 6) revela que o canônico **já permite** eventos com `project_id NULL` (Doc 11 §7 não força NOT NULL) — PATCH 2.5 não introduz brecha nova; só destrava um caso de uso que a infra já comporta. Mas a *policy* RLS para esse caso precisa ser escrita (F-02, defer PATCH 3).
- F1 Sprint 1 fica destravado para arrancar **assim que** PATCH 2.5 (com PL-01) for aplicado em `S-APPLY2_5-FRESH-20260609-001`. O charter standalone do S1 pode então citar Doc 10 §5.2 + Doc 15 §5.1 (já alinhados) como contrato canônico único.

---

## 8. CHECKOUT RELEASE

```txt
CHECKOUT RELEASE — S-P25-L3-METAREV-CLAUDE-20260609-001
files_created: 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/PATCH2_5_METACOGNIK_REVIEW.md (este)
files_changed: 000_ROADMAPS/SESSION_REGISTRY.md (1 sessão + 1 lock + release)
files_not_touched: canônico 01-28 (RO — leituras apenas: Doc 10 §5.2/§5.3, Doc 11 linhas 139-148 + linhas 217-232 events, Doc 12 §5.6, Doc 15 linhas 145-180, Doc 02 §5.2, Doc 05 §5.6.1, Doc 01 §5.4); PATCH 2.5 candidate (RO — não editado); PATCH 2 candidate (RO — referência histórica); 000_STUDY_NOTES/, 000_UPGRADE/, 000_KNOWLEDGE_BASE/; ARCHITECTURE_PATCH_REPORT.md
validation: 8 checks executados — 6 PASS, 1 PASS-com-deferred-flag (Check 6 → F-02), 1 PATCH-LEVE OBRIGATÓRIO (Check 4 → PL-01 Doc 15 linha 153); divergência Doc 10 ↔ Doc 15 documentada com texto exato apply-ready; veredito APROVA-COM-PATCHES-LEVES; PATCH 2.5 NÃO aplicado nesta sessão; separação de papéis preservada (autor ≠ reviewer ≠ executor)
risks_remaining: aplicação aguarda sessão canonical_patch separada (recomendada: S-APPLY2_5-FRESH-20260609-001 / Windsurf) que cola E.1 + E.2 + PL-01 simultaneamente; F-01/F-02/F-03 defer PATCH 3 sem urgência
next_step: sessão S-APPLY2_5-FRESH-20260609-001 aplica E.1 + E.2 + PL-01 mecanicamente → marca released_with_required_external_audit → bumps Doc 10 v1.2.0 + Doc 15 (minor) + ARCHITECTURE_PATCH_REPORT §32 v1.10.5 → F1 Sprint 1 charter standalone
status: released
```
