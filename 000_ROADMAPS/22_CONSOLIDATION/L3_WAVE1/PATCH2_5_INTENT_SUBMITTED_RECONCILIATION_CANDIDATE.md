---
title: PATCH 2.5 — IntentSubmitted reconciliation (canonical_patch candidate, apply-ready)
file: PATCH2_5_INTENT_SUBMITTED_RECONCILIATION_CANDIDATE.md
layer: auxiliary
doc_type: pmo_canonical_patch_candidate
phase: 000_ROADMAPS
category: consolidation
status: awaiting_metacognik_apply_gate
version: 0.1.0
created_at: 2026-06-09
owner: pmo_ckos
responsible_agent: claude_opus_4_7
session_id: S-F1S1-PMO-PATCH25-CLAUDE-20260609-001
companion_of:
  - PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md     # User canônico — precondition (já aplicado em 5d1d969)
  - F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md  # PROMOTE-U1 ingress reframe
derives_from:
  - 03_BACKEND_MVP_THIN_SLICE_PLAN.md            # §18.2 user-first event spec (2026-06-09)
  - PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md     # User como objeto canônico (Doc 02 §5.2)
  - GATE5_FOUNDER_DECISION_PACKAGE.md            # §8 decisão Founder = GO + AQ-IO-1 = user
target_canonical:
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md  # PATCH E (Doc 10 §5.2 linha 78 + nota user-first)
founder_approval: granted (2026-06-09, GATE 5 = GO + AQ-IO-1 = `user` — reframe user-first cobre ingress)
metacognik_approval: PENDING (apply-gate sobre este texto específico)
reviewers:
  - founder
  - metacognik
approval_required:
  - founder
  - metacognik
non_authority_boundary: >
  Patch candidate APPLY-READY. PROPÕE o texto exato; NÃO aplica. Esta sessão NÃO edita canônico 01-28.
  A aplicação é uma sessão canonical_patch SEPARADA, sob a regra de duas chaves (Founder ✅ via GATE 5
  + Metacognik ⏳) e separação de papéis (a sessão-autora não aplica o próprio patch). Escopo cirúrgico:
  1 patch (PATCH E em Doc 10 §5.2 linha 78 + 1 nota explicativa).
tags: [consolidation, canonical-patch-candidate, runtime, intent-ingress, doc10, l3-wave1, apply-ready, pmo, f1-s1-prereq, post-patch-2]
---

# PATCH 2.5 — IntentSubmitted reconciliation (apply-ready)

> **O que é:** o texto **exato e pronto-para-colar** que reconcilia Doc 10 §5.2 linha 78 com o reframe user-first do `03_BACKEND_MVP_THIN_SLICE_PLAN.md §18.2`. Faz `project_id` opcional na 1ª intenção, decopla a origem de `CommandBar` (UI), e adiciona campos opcionais (`context_ref?`) alinhados a §18.2.
> **O que não é:** não aplica nada. É o artefato que o **Metacognik** revisa para virar a 2ª chave; depois disso, uma sessão `canonical_patch` separada cola este bloco.

---

## 0. Estado das duas chaves (regra do sistema)

| Chave | Quem | Estado | Sobre o quê |
|---|---|---|---|
| 1ª | **Founder** | ✅ **dada** (2026-06-09) | autorização **GATE 5 = GO + AQ-IO-1 = `user`** já cobre ingress user-first. Ver `GATE5_FOUNDER_DECISION_PACKAGE.md §8` + `03_BACKEND_MVP_THIN_SLICE_PLAN.md §18` |
| 2ª | **Metacognik** | ⏳ **pendente** | o **texto específico** abaixo (PATCH E) e a coerência cross-doc (Doc 02 §5.2 / Doc 05 §5.6.1 / Doc 10 §5.3 envelope) |

> Esta sessão **não** edita o canônico: falta a 2ª chave, e a separação de papéis impede a sessão-autora de aplicar o próprio patch. Entrego o texto pronto; um "APROVA" do Metacognik destrava a aplicação mecânica.

---

## 1. Escopo (1 patch cirúrgico)

**Entra:**
- **PATCH E** — Reconciliação de `IntentSubmitted` em Doc 10 §5.2 (linha 78) com §18.2 user-first do backend MVP plan.

**Por que existe agora:** PATCH 2 (commit `5d1d969`, 2026-06-09) adicionou `User` como objeto de 1ª classe (Doc 02 §5.2) e memória escopada `user_id` (Doc 05 §5.6.1). O reframe user-first do GATE 5 (Founder, 2026-06-09) tornou `project_id` OPCIONAL na 1ª intenção. Mas Doc 10 §5.2 linha 78 ainda diz literalmente `CommandBar emite IntentSubmitted{text, project_id, user_id, section}` — `project_id` posicional/obrigatório + origem atrelada a UI (`CommandBar`). Isso diverge de §18.2 e bloqueia F1 Sprint 1 (S1 implementaria backend ingress fora do canônico → viola Princípio #5 anti-fragmentação).

**NÃO entra:**
- Enriquecimento de `users` table em Doc 11 (campos PATCH 2: `operating_dna_ref?`, `tribes_scored?`, `autonomy_preferences`, `response_preferences`, `confidence`, etc.) — defer para **PATCH 3** (Doc 11 patch candidate) conforme §31 do `ARCHITECTURE_PATCH_REPORT.md`: *"Materialização física especificada em Doc 11 como patch candidate posterior — esta seção define apenas a política."*
- Adicionar `correlation_id`/`occurred_at`/`workspace_id` ao payload de `IntentSubmitted` — esses já existem como **envelope fields** de todo evento via Doc 10 §5.3 (linha 98). §18.2 lista-os explicitamente para legibilidade do leitor, mas duplicá-los no payload do IntentSubmitted seria redundância.
- Reescrita estrutural de Doc 10 §5.2 — preserva o fluxo de 14 passos intacto.

---

## 2. O patch exato (apply-ready)

> Convenção: **ANCHOR** = onde inserir/substituir; **SUBSTITUIR/INSERIR** = texto literal. A sessão de aplicação cola sem reinterpretar.

### PATCH E — Doc 10 §5.2 · IntentSubmitted user-first reframe

**Arquivo:** `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md`

**E.1 — §5.2 linha 78 (dentro do bloco ` ```txt `).**
**SUBSTITUIR:**
```
1.  CommandBar emite IntentSubmitted{text, project_id, user_id, section}
```
**POR:**
```
1.  Ingress (CommandBar | backend API | webhook) emite IntentSubmitted{intent_text, user_id, project_id?, context_ref?, section?}
```

**E.2 — Após o fechamento do bloco ` ```txt ` (atual linha 92) e antes do parágrafo que começa com `Cada seta acima é **um evento no event log**` (atual linha 94).**
**INSERIR (nova nota explicativa, parágrafo único):**

```markdown
> **Nota — user-first ingress (PATCH 2.5, post-GATE 5):** `user_id` é REQUIRED (PATCH 2 PROMOTE-U1 — ver `01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md §5.2`); `project_id` é OPCIONAL na 1ª intenção do usuário e pode ser inferido a posteriori via `ProjectInferred{user_id, project_id, source_intent_id}` quando a intenção justificar (ver `000_ROADMAPS/22_CONSOLIDATION/03_BACKEND_MVP_THIN_SLICE_PLAN.md §18.2`). `intent_text` (renomeado de `text` para clareza); `context_ref?` aponta para briefing/conversa anterior se existir. **Source não é exclusivo de UI:** CommandBar permanece a origem canônica via Doc 14-16 (Product System), mas backend ingress (API, webhook, scheduled trigger) é igualmente válido — aderente a `§3` backend-antes-de-UI e ao F1-Sprint 1. Envelope fields (`workspace_id`, `correlation_id`, `occurred_at`, `actor`) seguem `§5.3` Event Log — não precisam ser repetidos no payload.
```

---

## 3. Instruções para a sessão de aplicação (pós-Metacognik)

1. **Abrir sessão `canonical_patch` separada** (não esta) + checkout lock escopado **apenas** a: Doc 10, `ARCHITECTURE_PATCH_REPORT.md`, `SESSION_REGISTRY.md`.
2. **Colar PATCH E** (E.1 + E.2). Nada além disso. Conteúdo literal.
3. **Bump de versão (minor):** Doc 10 v1.1.1 → v1.2.0
4. **Registrar em `ARCHITECTURE_PATCH_REPORT.md`** como nova §32 (v1.10.4 → v1.10.5).
5. **Marcar `released_with_required_external_audit`** — preserva o passo de validação.
6. **Não tocar** Doc 11 (enriquecimento defer PATCH 3), nem Doc 02/03/04/05 (já em v1.2.0/1.3.0 via PATCH 2), nem §5.3 envelope (intocado).

---

## 4. Risco + reversibilidade

- **Risco P1 controlado:** Doc 10 é Runtime Architecture (core). Mudança é **1 linha substituída + 1 parágrafo inserido**. Ambos aditivos do ponto de vista semântico:
  - PATCH E.1 amplia o domínio de `IntentSubmitted` (origens válidas + opcionalidade de `project_id`) sem remover capacidade — `CommandBar` continua sendo origem válida; `project_id` continua sendo aceito quando presente.
  - PATCH E.2 é nota explicativa cross-ref; não altera comportamento.
- **Baixa controvérsia:** o reframe user-first já tem chave Founder (GATE 5 = GO + AQ-IO-1 = `user`); §18.2 do backend plan já documenta o reframe; PATCH 2 já tornou User canônico. PATCH 2.5 só fecha o último loop entre essas decisões e o Doc 10.
- **Reversível:** git baseline `5d1d969` (PATCH 2 aplicado); o PATCH é bloco isolado; rollback trivial via `git revert` ou restauração da linha 78 anterior.
- **Anti-bloat respeitado:** zero campo novo no payload (envelope é §5.3); zero objeto novo; zero pasta nova; zero SQL.
- **Cross-doc coerência:** após PATCH E, o trio { Doc 02 §5.2 (User canônico) + Doc 05 §5.6.1 (memória user_id) + Doc 10 §5.2 (IntentSubmitted user-first) } fica self-consistent. Doc 11 (persistência) entra em PATCH 3 sem urgência.

---

## 5. BRA Packet

```yaml
bra_id: BRA-PATCH25-20260609-01
from_session: S-F1S1-PMO-PATCH25-CLAUDE-20260609-001
to: Metacognik + Founder
context_summary:
  - "PATCH 2 (User-in + Response-out) aplicado em 2026-06-09 (commit 5d1d969); Doc 02 §5.2 + Doc 05 §5.6.1 + Doc 03 §5.5 + Doc 04 §5.9 atualizados."
  - "F1 Sprint 1 (Intent Ingress) destravado tecnicamente, mas Doc 10 §5.2 linha 78 ainda diverge de §18.2 user-first do backend MVP plan."
  - "Divergência: `IntentSubmitted{text, project_id, user_id, section}` (canônico) vs `IntentSubmitted{intent_text, user_id, project_id?, context_ref?, ...}` (§18.2 user-first)."
  - "Sem PATCH 2.5, S1 implementaria backend ingress fora do canônico → Princípio #5 anti-fragmentação violado."
outputs:
  - "PATCH2_5_INTENT_SUBMITTED_RECONCILIATION_CANDIDATE.md (este): PATCH E apply-ready em 1 substituição + 1 inserção."
open_questions:
  - "Metacognik: aceita renomear `text` → `intent_text` (alinha §18.2 e melhora searchability)? Alternativa: manter `text` mas anotar alias."
  - "Metacognik: aceita decoplar 'CommandBar' como única origem? (CommandBar continua válido; só não é mais o único exemplo nomeado.)"
  - "Metacognik: aceita `section?` ficar opcional (era UI-specific, só aplica quando CommandBar é origem)?"
  - "Metacognik: aceita nota explicativa pós-fluxo (§5.2 após linha 92) ou prefere footnote inline?"
blockers:
  - "Aplicação bloqueada até a 2ª chave (Metacognik) sobre este texto. F1 Sprint 1 charter aguarda este patch ser aplicado."
risk_flags:
  - "P1 (Doc 10 Runtime core) — mitigado por escopo cirúrgico (1 linha substituída + 1 parágrafo inserido), pleno aditivo semântico, zero remoção de capacidade, git rollback baseline 5d1d969."
recommended_next:
  - "Metacognik revisa PATCH E → 'APROVA' → sessão canonical_patch separada cola e marca released_with_required_external_audit (Doc 10 → v1.2.0; ARCHITECTURE_PATCH_REPORT §32 v1.10.5)."
  - "Após APPLY: F1 Sprint 1 charter pode ser escrito como artefato standalone, citando Doc 10 §5.2 (já reconciliado) como fonte canônica única do contrato `IntentSubmitted`."
```

---

## 6. CHECKOUT RELEASE

```txt
CHECKOUT RELEASE — S-F1S1-PMO-PATCH25-CLAUDE-20260609-001
files_created: 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/PATCH2_5_INTENT_SUBMITTED_RECONCILIATION_CANDIDATE.md (este)
files_changed: nenhum (esta sessão é só candidate; SESSION_REGISTRY entry virá quando user aprovar o commit)
files_not_touched: canônico Doc 10 (RO — só lidas linhas 1-15 header + 75-99 §5.2-§5.3); Doc 11 (RO — só lidas linhas 139-148 users); demais docs 01-09, 12-28; ARCHITECTURE_PATCH_REPORT.md;
  00_SYSTEM_GOVERNANCE/*; PATCH2 candidate (RO histórico)
validation: texto apply-ready casado à seção real (Doc 10 §5.2 linha 78 verificada via Read em 2026-06-09); divergência §18.2 ↔ canônico documentada com fonte (backend plan §18.2:313-336); resolução por reuso (envelope fields §5.3 não duplicados); só ALTA, nada de HOLD; nada aplicado
risks_remaining: aplicação aguarda 2ª chave (Metacognik); P1 mitigado por escopo + reuso + rollback
next_step: Metacognik revisa PATCH E → sessão canonical_patch separada aplica → F1 Sprint 1 charter
status: released
```
