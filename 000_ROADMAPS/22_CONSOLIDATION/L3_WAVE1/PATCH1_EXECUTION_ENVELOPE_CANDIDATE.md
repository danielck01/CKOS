---
title: PATCH 1 — Execution Envelope (canonical_patch candidate, apply-ready)
file: PATCH1_EXECUTION_ENVELOPE_CANDIDATE.md
layer: auxiliary
doc_type: pmo_canonical_patch_candidate
phase: 000_ROADMAPS
category: consolidation
status: awaiting_metacognik_apply_gate
version: 0.1.0
created_at: 2026-06-04
owner: pmo_ckos
responsible_agent: claude_opus_4_8
session_id: S-P1-L3-PATCH1-CLAUDE-20260604-001
companion_of: WAVE1_FANIN_AUDIT_FOR_FOUNDER.md
derives_from:
  - WAVE1_FANIN_AUDIT_FOR_FOUNDER.md   # GO items #1 (S1+T1) e #2 (S2); resolve AQ-W1-ENVELOPE
  - DOC06_SKILLS_RECONCILIATION_CANDIDATE.md      # PROMOTE-S1, PROMOTE-S2
  - DOC09_TRANSFORMERS_RECONCILIATION_CANDIDATE.md # PROMOTE-T1
target_canonical:
  - 02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md          # PATCH A, PATCH B (obrigatório)
  - 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md # PATCH C (obrigatório)
  - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md      # PATCH D (companion opcional, +1 campo)
founder_approval: granted (2026-06-04, triagem go/hold do fan-in audit)
metacognik_approval: PENDING (gate de aplicação sobre este texto específico)
reviewers:
  - founder
  - metacognik
approval_required:
  - founder
  - metacognik
non_authority_boundary: >
  Patch candidate APPLY-READY. PROPÕE o texto exato; NÃO aplica. Esta sessão NÃO edita
  canônico 01-28. A aplicação é uma sessão canonical_patch SEPARADA, sob a regra de duas
  chaves do sistema (Founder ✅ + Metacognik ⏳) e separação de papéis (a sessão-auditora
  não aplica o próprio patch). Só os itens GO (S1+T1+S2) entram; itens HOLD do audit ficam de fora.
tags: [consolidation, canonical-patch-candidate, execution-envelope, doc06, doc09, doc03, l3, apply-ready, pmo]
---

# PATCH 1 — Execution Envelope (apply-ready)

> **O que é:** o texto **exato e pronto-para-colar** que materializa os 2 itens GO aprovados no
> fan-in audit — `S1`+`T1` (Execution Envelope) e `S2` (critério de utilidade downstream) — e
> **resolve `AQ-W1-ENVELOPE`** com uma proposta concreta.
> **O que não é:** não aplica nada. É o artefato que o **Metacognik** revisa para virar a 2ª chave;
> depois disso, uma sessão `canonical_patch` separada cola estes blocos.

---

## 0. Estado das duas chaves (regra do sistema)

A constituição (repetida em todo candidate): *"Aplicação exige sessão canonical_patch separada com aprovação Founder + Metacognik."*

| Chave | Quem | Estado | Sobre o quê |
|---|---|---|---|
| 1ª | **Founder** | ✅ **dada** (2026-06-04) | a **triagem** go/hold do fan-in audit (promover S1/T1/S2; segurar o resto; não promover policies) |
| 2ª | **Metacognik** | ⏳ **pendente** | o **texto específico** abaixo (PATCH A-D) e a resolução proposta de AQ-W1-ENVELOPE |

> Por isso esta sessão **não** edita o canônico: falta a 2ª chave, e a separação de papéis impede a sessão-auditora de aplicar o próprio patch. Entrego o texto pronto; um "go" do Metacognik destrava a aplicação mecânica.

---

## 1. Escopo (só o GO; nada do HOLD)

**Entra:** `PROMOTE-S1` (Skill I/O Contract), `PROMOTE-T1` (Transformer Spec Card + robustez), `PROMOTE-S2` (critério downstream). Mais a **forma de saída comum** que S1 e T1 compartilham.

**NÃO entra** (HOLD no audit, não tocar nesta aplicação): T2 `briefing_to_task`, S3a/S3b intent/context, clusters ROI/learning/context, catálogo F2, as 11 policies. Ver `WAVE1_FANIN_AUDIT_FOR_FOUNDER.md §3/§5`.

---

## 2. Resolução proposta de AQ-W1-ENVELOPE (o ponto que o Metacognik decide)

**Pergunta:** existe UM envelope de I/O canônico para toda unidade executável?

**Proposta (não-fragmentadora):** **sim — e ele já existe quase inteiro no `Agent Run` (Doc 03 §5.5).** Não criar formato novo; **nomear** o que já está lá e reusá-lo.

- **Execution Output Envelope** = `{ result, confidence, risks, gaps, next_actions }`.
- `confidence`, `risks`, `gaps` **já são campos do Agent Run** (Doc 03 §5.5). O único acréscimo é `next_actions` (que os dois UPGRADE-fontes já usavam como "próximas ações").
- Skills (Doc 06) e transformers (Doc 09) **referenciam** este envelope em vez de redefinir. Skills enfatizam `risks`; transformers enfatizam `gaps`; ambos emitem `confidence` + `next_actions`.
- Robustez (`validation`, `error_policy`, `fallback_manual`, `idempotency_semantics`) entra **só no registry de transformer** (Doc 09), porque o §14 do Doc 09 **já exige** "fallback manual" e é onde falta forma — não como conteúdo herdado do UPGRADE (que não tinha nada disso), mas como **lacuna obrigatória** do patch.

> Resultado: 1 envelope, 3 docs alinhados (03/06/09), **zero formato paralelo**. É a tese anti-1:35 aplicada ao contrato de saída.

---

## 3. Os patches exatos (apply-ready)

> Convenção: **ANCHOR** = onde inserir; **INSERIR/SUBSTITUIR** = texto literal. A sessão de aplicação cola sem reinterpretar.

### PATCH A — Doc 06 §5.3 · adicionar o contrato de I/O + nomear o envelope
**Arquivo:** `02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md`
**ANCHOR:** logo após o fence YAML que fecha `## 5.3 Template de skill` (a linha ` ``` ` antes de `## 5.4 Skills prioritárias para MVP`).
**INSERIR:**

```markdown
### 5.3.1 Contrato mínimo de execução (Skill Execution I/O Contract)

O template acima nomeia `required_inputs`/`outputs`; este contrato dá a **forma** mínima deles. Toda skill declara:

​```yaml
input:
  context_state:   # contexto corrente (ver Doc 05 Context Packet)
  goal:            # objetivo da invocação
  constraints:     # limites/policies aplicáveis (ver Doc 04 + Doc 12)
  evidence:        # evidência/fontes disponíveis (ver Doc 18)
output:            # Execution Output Envelope — ver §5.3.2
​```

### 5.3.2 Execution Output Envelope (forma de saída canônica)

Envelope de saída **único**, compartilhado por skills, transformers (Doc 09 §5.5) e runs (Doc 03 §5.5):

`{ result, confidence, risks, gaps, next_actions }`

- `confidence`, `risks`, `gaps` são a mesma família dos campos do **Agent Run** (Doc 03 §5.5); `next_actions` é o acréscimo.
- Toda unidade executável emite este envelope. Skills enfatizam `risks`; transformers enfatizam `gaps`; ambos sempre `confidence` + `next_actions`.
- Não substitui o template (§5.3); é a **forma** que `outputs` nomeia. Proíbe formatos de saída paralelos.
```

### PATCH B — Doc 06 §14/§15 · adicionar critério de utilidade downstream (S2)
**Arquivo:** `02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md`

**B.1 — §14 (linha 171).**
**SUBSTITUIR:**
> `Skill aprovada se tem output verificável, owner, "quando não usar", risco definido, conexão a workflow, prompts base e eval_ref.`
**POR:**
> `Skill aprovada se tem output verificável, owner, "quando não usar", risco definido, conexão a workflow, prompts base, eval_ref e **resultado que alimenta um consumidor downstream** (agente, tarefa, proposta, workflow ou decisão).`

**B.2 — §15 (linha 175).**
**SUBSTITUIR:**
> `Reprovada se: sem output verificável; depende de prompt genérico; sem owner; sem "quando não usar"; sem risco; sem workflow; sem registro de aprendizado.`
**POR:**
> `Reprovada se: sem output verificável; depende de prompt genérico; sem owner; sem "quando não usar"; sem risco; sem workflow; sem registro de aprendizado; **ou cujo output não alimenta nenhum consumidor downstream (relatório morto).**`

### PATCH C — Doc 09 §5.5 · robustez obrigatória + envelope (T1)
**Arquivo:** `02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md`
**ANCHOR:** dentro do bloco YAML de `## 5.5 Transformer registry`, após a linha `metrics:` e antes do fechamento do fence.
**INSERIR (novos campos obrigatórios):**

```yaml
output_envelope:        # { confidence, gaps, next_actions } — ver Doc 06 §5.3.2 Execution Output Envelope
validation:             # como valida input e output (obrigatório — ausente no MVP atual)
error_policy:           # comportamento em erro (obrigatório — ausente no MVP atual)
fallback_manual:        # caminho manual quando falha (já exigido pelo §14 — agora explícito no registry)
idempotency_semantics:  # chave/semântica de idempotência (alinha Doc 03 idempotency_key + Doc 10)
```

> Nota de aplicação: estes 4 campos de robustez são **lacuna obrigatória** (o UPGRADE/08 não os tinha). `fallback_manual` apenas torna o registry coerente com o §14, que já o exige.

### PATCH D — Doc 03 §5.5 Agent Run · alinhamento do envelope (COMPANION OPCIONAL, +1 campo)
**Arquivo:** `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md`
**ANCHOR:** bloco YAML de `## 5.5 Agent Run`, após a linha `gaps:` (linha 109).
**INSERIR:**

```yaml
next_actions:      # novo — alinha o Execution Output Envelope (Doc 06 §5.3.2)
```

> Por que opcional: o Agent Run já tem `confidence`/`risks`/`gaps`/`evidence`/`idempotency_key`. Só falta `next_actions` para o envelope ser idêntico nos 3 docs. **Recomendo incluir** (alinhamento total, +1 campo, risco ~zero), mas é a única parte que toca o Thinking System core — fica à decisão do Metacognik aceitar D junto, ou deixar Doc 03 como cross-ref apenas.

---

## 4. Instruções para a sessão de aplicação (pós-Metacognik)

1. **Abrir sessão `canonical_patch` separada** (não esta, não a auditora) + checkout lock escopado **apenas** a: Doc 06, Doc 09, (Doc 03 se D aceito), `ARCHITECTURE_PATCH_REPORT.md`, maps permitidos, `SESSION_REGISTRY.md`.
2. **Colar A, B, C** (e D se aprovado). Nada além disso.
3. **Bump de versão (minor):** Doc 06 (v1.1.0 → v1.2.0), Doc 09 (próximo minor), Doc 03 (próximo minor, só se D). Registrar em `ARCHITECTURE_PATCH_REPORT.md`.
4. **Marcar `released_with_required_external_audit`** — preserva o passo de validação; não declarar sign-off final.
5. **Não tocar** nenhum item HOLD nem mover/arquivar UPGRADE/04|08 (arquivamento é pós-aprovação, sessão própria).

---

## 5. Risco + reversibilidade

- **Risco P1 controlado:** Doc 06/09 são core do Execution System; por isso o escopo é cirúrgico (4 blocos, 1 envelope, alinhado ao que já existe) e o resto fica HOLD.
- **Baixa controvérsia:** o envelope harmoniza campos que **já são canônicos** no Agent Run — não é aposta de arquitetura nova.
- **Reversível:** git baseline `b3fc69f`; cada patch é um bloco isolado; rollback trivial.
- **Anti-bloat respeitado:** nenhum nome de catálogo, nenhuma "skill bonita sem owner/eval" entra. Só contrato/forma/critério.

---

## 6. BRA Packet

```yaml
bra_id: BRA-PATCH1-20260604-01
from_session: S-P1-L3-PATCH1-CLAUDE-20260604-001
to: Metacognik + Founder
context_summary:
  - "Founder aprovou a triagem do fan-in audit; este é o texto exato dos itens GO (S1+T1+S2)."
  - "Verifiquei a fonte canônica: Doc 03 Agent Run já tem confidence/risks/gaps/evidence/idempotency_key; Doc 09 §14 já exige fallback manual."
  - "Envelope proposto reusa o que existe; só acrescenta next_actions (e +1 campo opcional em Doc 03)."
outputs:
  - "PATCH1_EXECUTION_ENVELOPE_CANDIDATE.md (este): PATCH A-D apply-ready + resolução de AQ-W1-ENVELOPE."
open_questions:
  - "Metacognik: aceita a resolução de AQ-W1-ENVELOPE (1 envelope reusando Agent Run)?"
  - "Metacognik: PATCH D (next_actions no Doc 03) entra junto, ou Doc 03 fica como cross-ref?"
blockers:
  - "Aplicação bloqueada até a 2ª chave (Metacognik) sobre este texto."
risk_flags:
  - "P1 (core Execution System) — mitigado por escopo cirúrgico + reuso de campos canônicos + git rollback."
recommended_next:
  - "Metacognik revisa A-D → 'go' → sessão canonical_patch separada cola e marca released_with_required_external_audit."
  - "Em paralelo (decisão Founder+Metacognik, não bloqueia PATCH 1): as 2 AQs-mãe (taxonomia, camada-policy) e AQ-IO-1→GATE 5."
```

---

## 7. CHECKOUT RELEASE

```txt
CHECKOUT RELEASE — S-P1-L3-PATCH1-CLAUDE-20260604-001
files_created: 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/PATCH1_EXECUTION_ENVELOPE_CANDIDATE.md
files_changed: 000_ROADMAPS/SESSION_REGISTRY.md (1 sessão + 1 lock)
files_not_touched: canônico Doc 06/09/03 (RO — só lidas as seções-alvo p/ casar o texto); docs 01-28;
  docs 29-34; ARCHITECTURE_PATCH_REPORT.md; 00_SYSTEM_GOVERNANCE/*; os candidates do audit (RO)
validation: texto apply-ready casado às seções reais (Doc 06 §5.3/§14/§15; Doc 09 §5.5/§14; Doc 03 §5.5);
  AQ-W1-ENVELOPE resolvida por reuso de campos já canônicos; só itens GO; nada aplicado
risks_remaining: aplicação aguarda 2ª chave (Metacognik); P1 mitigado por escopo + reuso + rollback
next_step: Metacognik aprova A-D → sessão canonical_patch separada aplica
status: released
```
