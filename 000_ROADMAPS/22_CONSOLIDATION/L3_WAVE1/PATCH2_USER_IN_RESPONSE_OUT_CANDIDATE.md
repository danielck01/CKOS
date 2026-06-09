---
title: PATCH 2 — User-in + Response-out (canonical_patch candidate, apply-ready)
file: PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md
layer: auxiliary
doc_type: pmo_canonical_patch_candidate
phase: 000_ROADMAPS
category: consolidation
status: awaiting_metacognik_apply_gate
version: 0.1.0
created_at: 2026-06-09
owner: pmo_ckos
responsible_agent: claude_opus_4_7
session_id: S-USER-PMO-CLAUDE-20260609-001
companion_of: F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md
derives_from:
  - F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md   # PROMOTE-U1/U2/R1/R2 (ALTA)
  - GATE5_FOUNDER_DECISION_PACKAGE.md                      # §8 decisão Founder 2026-06-09
  - 000_STUDY_NOTES/02_RESEARCH_SYNTHESIS/ck_memory.md     # triagem PMO de 8 DRs + SYSTEM_RESPONSE
target_canonical:
  - 01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md         # PATCH A (User como objeto 1ª classe)
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md # PATCH B (memória escopada user_id)
  - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md         # PATCH C (response_type/depth_level/reasoning_mode no Agent Run)
  - 01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md        # PATCH D (5 anti-pattern Response Behavior Policies)
founder_approval: granted (2026-06-09, GATE 5 = GO + AQ-IO-1 = user + 3 AQs técnicas)
metacognik_approval: PENDING (apply-gate sobre este texto específico)
reviewers:
  - founder
  - metacognik
approval_required:
  - founder
  - metacognik
non_authority_boundary: >
  Patch candidate APPLY-READY. PROPÕE o texto exato; NÃO aplica. Esta sessão NÃO edita canônico 01-28.
  A aplicação é uma sessão canonical_patch SEPARADA, sob a regra de duas chaves do sistema (Founder ✅
  + Metacognik ⏳) e separação de papéis (a sessão-autora não aplica o próprio patch). Só os itens
  ALTA do F1 candidate (U1/U2/R1/R2) entram; U3/U4/U5/R3/R4/R5 ficam para PATCH 3 conforme
  F1-Sprints 2-3 revelarem necessidade.
tags: [consolidation, canonical-patch-candidate, user-system, response-engine, doc02, doc03, doc04, doc05, l3-wave1, apply-ready, pmo, post-gate-5]
---

# PATCH 2 — User-in + Response-out (apply-ready)

> **O que é:** o texto **exato e pronto-para-colar** que materializa os 4 itens ALTA do F1 candidate (U1/U2/R1/R2) em Doc 02/03/04/05. Resolve AQ-IO-2 (User é objeto novo) e AQ-IO-3 (memória `user_id` é nova camada de escopo no Doc 05).
> **O que não é:** não aplica nada. É o artefato que o **Metacognik** revisa para virar a 2ª chave; depois disso, uma sessão `canonical_patch` separada cola estes blocos.

---

## 0. Estado das duas chaves (regra do sistema)

A constituição (repetida em todo candidate): *"Aplicação exige sessão canonical_patch separada com aprovação Founder + Metacognik."*

| Chave | Quem | Estado | Sobre o quê |
|---|---|---|---|
| 1ª | **Founder** | ✅ **dada** (2026-06-09) | autorização **GATE 5 = GO** + **AQ-IO-1 = `user`** + 3 AQs técnicas. Ver `GATE5_FOUNDER_DECISION_PACKAGE.md §8` |
| 2ª | **Metacognik** | ⏳ **pendente** | o **texto específico** abaixo (PATCH A-D) e a resolução proposta de AQ-IO-2/3 |

> Por isso esta sessão **não** edita o canônico: falta a 2ª chave, e a separação de papéis impede a sessão-autora de aplicar o próprio patch. Entrego o texto pronto; um "APROVA" do Metacognik destrava a aplicação mecânica.

---

## 1. Escopo (só ALTA; defer MÉDIA para PATCH 3)

**Entra (4 patches, escopo cirúrgico):**
- **PATCH A** — `PROMOTE-U1`: `User` como objeto de 1ª classe (Doc 02 §5.1/5.2)
- **PATCH B** — `PROMOTE-U2`: memória escopada `user_id` (Doc 05 §5.6)
- **PATCH C** — `PROMOTE-R1`: tipagem da resposta (`response_type`/`depth_level`/`reasoning_mode`) no Agent Run (Doc 03 §5.5)
- **PATCH D** — `PROMOTE-R2`: 5 Response Behavior Policies anti-padrão (Doc 04 nova §5.9)

**NÃO entra (defer para PATCH 3 conforme F1-Sprints revelarem necessidade):**
- **U3** (aprendizado 4 níveis declarado→observado→inferido→validado) → refinamento de Doc 05 §5.5, depende de telemetria que ainda não existe
- **U4** (tribos como modos dinâmicos `f(comportamento, intenção, projeto, feedback)`) → derivada, não wizard; F1-S6 (memória) é pré-requisito
- **U5** (onboarding engine adaptativa) → abstrato, ancorar quando F1-S1/S2 estiverem rodando
- **R3** (gate de lacuna em 3 níveis) → refina Question Engine (Doc 03), entra com F1-S2
- **R4** (Response Contract V1 — 9 pontos) → enriquecimento de qualidade, pode entrar em Doc 13/20 quando evals existirem
- **R5** (User Mode vs Audit Mode) → princípio agora; UI difere em F4

**NÃO entra de jeito nenhum:**
- `/CKOS_USER_SYSTEM/` pasta de sistema (fragmentação 1:35)
- Smart Response Engine docs 01-07 (duplica Doc 10 §5.2)
- Schemas SQL (Doc 11 gated)
- Cognitive Atmosphere / glass / wallpaper (F4)

---

## 2. Resolução proposta de AQ-IO-2 e AQ-IO-3 (Metacognik decide junto com o texto)

### AQ-IO-2 — `User` é objeto novo de 1ª classe ou promoção/extensão do `Stakeholder`?

**Proposta (PATCH A):** **objeto novo**, com relação explícita a `Stakeholder`.

Justificativa: `Stakeholder` (Doc 02 §5.2) tem semântica de **papel projeto-escopado** (founder, owner, sponsor, reviewer, operator, client, external partner, agent group). Um mesmo `User` pode ser múltiplos `Stakeholder` em projetos diferentes (founder no Projeto A, reviewer no Projeto B). Tratar `User` como extensão do `Stakeholder` confunde identidade (persistente entre projetos) com papel (projeto-escopado). Solução: `User` é o objeto de identidade operacional vivo; `Stakeholder.user_id` referencia o `User` em cada projeto.

### AQ-IO-3 — Memória `user_id` é nova camada de escopo no Doc 05, ou identity store separado?

**Proposta (PATCH B):** **nova camada de escopo no Doc 05** (campo `user_id` no `memory_object` ao lado de `project_id`/`workspace_id`).

Justificativa: Doc 05 já tem 3 escopos (project, workspace + curta/média/longa). Adicionar `user_id` como 4ª dimensão de escopo é mecânico, não estrutural. Criar identity store separado refabricaria fragmentação (1:35 risk). Princípio #5 — nomear o que falta, não criar sistema novo.

---

## 3. Os patches exatos (apply-ready)

> Convenção: **ANCHOR** = onde inserir; **INSERIR/SUBSTITUIR** = texto literal. A sessão de aplicação cola sem reinterpretar.

### PATCH A — Doc 02 §5.1 + §5.2 · `User` como objeto de 1ª classe

**Arquivo:** `01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md`

**A.1 — §5.1 (linha 54).**
**SUBSTITUIR:**
> `Workspace · Project · Stakeholder · Briefing · Signal · Node · Capability · Agent · Skill`
**POR:**
> `User · Workspace · Project · Stakeholder · Briefing · Signal · Node · Capability · Agent · Skill`

**A.2 — §5.2 (após a linha `- **Workspace**: container de organização/cliente/operação.`, antes de `- **Project**: unidade operacional ...`).**
**INSERIR:**

```markdown
- **User**: pessoa que opera ou consome o CKOS — objeto de 1ª classe, vivo e versionado. **Campos canônicos:** `user_id, display_name, role, workspace_ids[], primary_stakeholder_id?, operating_dna_ref?, tribes_scored?, autonomy_preferences, response_preferences, confidence, created_at, updated_at`. **Distinção:** `User` é a **identidade operacional persistente entre projetos**; `Stakeholder` é o **papel projeto-escopado** (founder, owner, reviewer, client...) que um `User` pode assumir. Um `User` pode ser múltiplos `Stakeholders` em projetos diferentes. **Relação:** `Stakeholder.user_id → User.user_id` (referência). (PROMOTE-U1, AQ-IO-2 resolvida: `User` é objeto novo de 1ª classe, não extensão do `Stakeholder`.)
```

### PATCH B — Doc 05 §5.6 Memory object · adicionar escopo `user_id` + §5.6.1 explicativo

**Arquivo:** `01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md`

**B.1 — §5.6 bloco YAML, após a linha `project_id:` e antes de `workspace_id:`.**
**INSERIR (1 linha):**

```yaml
user_id:           # novo — PROMOTE-U2: memória escopada por usuário, persistente entre projetos (AQ-IO-3 resolvida)
```

**B.2 — Após o fechamento do fence `\`\`\`` do bloco YAML de §5.6 e antes de `## 5.7 Context packet`, inserir nova subseção §5.6.1.**
**INSERIR:**

```markdown
### 5.6.1 Escopo de memória: project, workspace, user (PROMOTE-U2)

A partir do PATCH 2, o `memory_object` admite **três dimensões de escopo simultâneas**, cada uma opcional dependendo do tipo da memória:

| Campo | Quando preencher | Lifecycle |
|---|---|---|
| `project_id` | memória ligada a um projeto específico (briefing vivo, decisões do projeto, artifacts) | dura enquanto o projeto está ativo + retenção pós-arquivamento conforme `12_SECURITY` |
| `workspace_id` | memória organizacional (políticas do workspace, identidade da marca, stakeholders comuns) | dura enquanto o workspace existir |
| `user_id` | memória do usuário **entre projetos** (preferências de resposta, autonomy preferences, tribos scored, User Operating DNA refs, padrões de decisão observados) | dura enquanto o User existir; sobrevive ao arquivamento de projetos |

**Regras de combinação:**
- Memória pode ter **um, dois ou os três escopos** preenchidos. Exemplos:
  - `{project_id, workspace_id}` — memória clássica de projeto (comportamento atual antes do PATCH 2)
  - `{user_id, workspace_id}` — preferências do usuário dentro de uma organização
  - `{user_id}` — preferência cross-workspace do usuário (rara; geralmente Founder-only)
- **Permission filter (`12_SECURITY`)** continua sendo aplicado: um usuário não enxerga memória `user_id` de outro usuário, mesmo no mesmo workspace, salvo se `permission_level` autorizar (default: deny).
- **Trust hierarchy (§5.5)** permanece: memória escopada `user_id` não tem prioridade especial — segue a mesma ordem (approved decision > signed contract > structured DB > etc.).
- **Esquecimento e expiração (§5.8)**: memória `user_id` tem retenção independente do ciclo de vida de projetos. Limpeza por solicitação explícita do usuário (LGPD) ou por `valid_until`.

Materialização física (índices `user_id`, RLS, namespace de vetor) é especificada em `11_DATA_MODEL` como patch candidate posterior — esta seção define apenas a **política**.
```

### PATCH C — Doc 03 §5.5 Agent Run · tipagem da resposta (PROMOTE-R1)

**Arquivo:** `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md`

**ANCHOR:** bloco YAML de `## 5.5 Agent Run`, entre a linha `output:` e a linha `confidence:`.
**INSERIR (3 linhas):**

```yaml
response_type:     # novo — PROMOTE-R1: diagnóstica | estratégica | decisão | operacional | criativa | técnica | learning | ROI
depth_level:       # novo — PROMOTE-R1: direta | estruturada | estratégica | profunda
reasoning_mode:    # novo — PROMOTE-R1: fast | deep | skeptical | exploratory
```

> Nota de aplicação: estes 3 campos **tipam a forma do output**, não substituem o output em si. Cumprem o que o F1 candidate chamou de "o gem" — o runtime executa runs mas não classifica a forma da resposta. Doc 06 §5.3.2 Execution Output Envelope (PATCH 1) referencia esta tipagem como parte do envelope.

### PATCH D — Doc 04 · nova §5.9 Response Behavior Policies (PROMOTE-R2)

**Arquivo:** `01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md`

**ANCHOR:** após o fechamento do bloco `\`\`\`txt` de `## 5.8 Escalonamento` e antes de `# 6. Agente responsável`.
**INSERIR (nova subseção completa):**

```markdown
## 5.9 Response Behavior Policies (anti-padrões de saída — PROMOTE-R2)

Cinco policies anti-padrão que governam **como** o agente responde (não apenas se pode agir). Compõem o Execution Output Envelope (Doc 06 §5.3.2) com critérios de comportamento e tipam-se via Doc 03 §5.5 (`response_type`, `depth_level`, `reasoning_mode`).

| Policy ID | Regra | Quando dispara |
|---|---|---|
| `do_not_over_ask` | Não fazer pergunta sem ganho informacional esperado (EVIG > custo cognitivo). Preferir hipótese declarada quando `confidence ≥ threshold`. | Question Engine antes de emitir `QuestionAsked` |
| `do_not_over_explain` | Não inflar resposta com material irrelevante. *"Profundidade não é tamanho, é precisão operacional."* | Composer de output, Metacognik review |
| `no_fake_certainty` | Toda afirmação sem `evidence` forte vai com `confidence` explícito e flag `assumption_transparency`. | Worker emite `PartialOutputProduced` |
| `assumption_transparency` | Pressupostos do raciocínio aparecem como campo separado do output, nunca embutidos como fato. | Composer + Metacognik |
| `depth_fit` | Profundidade da resposta deve casar com `depth_level` declarado no Agent Run (Doc 03 §5.5) e com `response_preferences` do User (Doc 02 §5.2). | Composer antes de finalizar artifact |

**Princípio que governa as 5:** *profundidade não é tamanho, é precisão operacional* — uma resposta direta com 1 frase pode ter mais valor que um relatório de 3 páginas se a precisão for maior.

**Enforcement:**
- As 5 policies são verificáveis em `13_EVALS` (Doc 13) como eval kinds.
- O Metacognik review (Doc 03 §5.5) usa-as como critério.
- Violação registrada em `audit_logs` e reduz `confidence` do run.
- **Não bloqueiam** a execução por default — geram alerta + reduzem `confidence`. Apenas `depth_fit` extremo (resposta totalmente fora da forma esperada) pode acionar `ApprovalRequested`.

**Cross-ref:**
- `response_type`, `depth_level`, `reasoning_mode` no Agent Run → `Doc 03 §5.5`
- Quality gates → `Doc 13 §16`
- User Mode vs Audit Mode (princípio de verbosidade controlada) → registrado aqui; UI difere em F4 (Doc 14/15/16)
- User `response_preferences` → `Doc 02 §5.2` (objeto User, PROMOTE-U1)
```

---

## 4. Instruções para a sessão de aplicação (pós-Metacognik)

1. **Abrir sessão `canonical_patch` separada** (não esta, não a auditora) + checkout lock escopado **apenas** a: Doc 02, Doc 03, Doc 04, Doc 05, `ARCHITECTURE_PATCH_REPORT.md`, `SESSION_REGISTRY.md`.
2. **Colar A, B, C, D** (4 patches). Nada além disso. Conteúdo literal.
3. **Bump de versão (minor):**
   - Doc 02 v1.1.0 → v1.2.0
   - Doc 03 v1.2.0 → v1.3.0 (acabou de subir para 1.2.0 no PATCH 1)
   - Doc 04 v1.1.0 → v1.2.0
   - Doc 05 v1.1.0 → v1.2.0
4. **Registrar em `ARCHITECTURE_PATCH_REPORT.md`** como nova §31 (v1.10.3 → v1.10.4).
5. **Marcar `released_with_required_external_audit`** — preserva o passo de validação.
6. **Não tocar** Doc 11 (schema gated), nem criar `/CKOS_USER_SYSTEM/`, nem U3/U4/U5/R3/R4/R5 (defer PATCH 3).

---

## 5. Risco + reversibilidade

- **Risco P1 controlado:** 4 docs do Thinking System core (02/03/04/05) recebem mudanças aditivas. PATCH A adiciona 1 objeto + 1 entrada no índice; PATCH B adiciona 1 campo + 1 sub-seção; PATCH C adiciona 3 campos em bloco YAML; PATCH D adiciona 1 sub-seção. Todos aditivos, todos reversíveis.
- **Baixa controvérsia:**
  - PATCH A nomeia uma identidade que já existia implicitamente (User era inferido de Stakeholder)
  - PATCH B adiciona 1 dimensão de escopo a um modelo já com 3 (project/workspace + curta/média/longa)
  - PATCH C tipifica um output que já existia — não muda comportamento, só classifica
  - PATCH D codifica anti-padrões que o Founder já reconhece (DR 5 + SYSTEM_RESPONSE §16-§17)
- **Reversível:** git baseline `c3786c2` (commit PMO synthesis); cada PATCH é bloco isolado; rollback trivial.
- **Anti-bloat respeitado:** nenhum nome de catálogo, nenhuma "skill bonita sem owner/eval", nenhuma pasta nova de sistema, nenhum SQL.

---

## 6. BRA Packet

```yaml
bra_id: BRA-PATCH2-20260609-01
from_session: S-USER-PMO-CLAUDE-20260609-001
to: Metacognik + Founder
context_summary:
  - "Founder aprovou GATE 5 = GO + AQ-IO-1 = `user` em 2026-06-09; libera PATCH 2."
  - "F1 candidate Jun 4 marcou U1/U2 + R1/R2 como ALTA strength net-new."
  - "Cross-reference com 8 deep researches (Jun 9, sintetizadas em 02_RESEARCH_SYNTHESIS/ck_memory.md) reforça os 4 itens."
  - "Verifiquei as fontes canônicas: Doc 02 §5.1/5.2 (Stakeholder ≠ User), Doc 05 §5.6 (memory_object), Doc 03 §5.5 (Agent Run pós-PATCH 1), Doc 04 §5.8 (Escalonamento) — todas as anchors casam."
outputs:
  - "PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md (este): PATCH A-D apply-ready + resolução de AQ-IO-2/3."
open_questions:
  - "Metacognik: aceita PATCH A (User é objeto novo, não extensão de Stakeholder)?"
  - "Metacognik: aceita PATCH B (user_id como 4ª dimensão de escopo no memory_object, não identity store separado)?"
  - "Metacognik: aceita PATCH C (3 campos no Agent Run para tipar forma do output)?"
  - "Metacognik: aceita PATCH D (§5.9 Response Behavior Policies — 5 anti-padrões com enforcement em 13_EVALS)?"
blockers:
  - "Aplicação bloqueada até a 2ª chave (Metacognik) sobre este texto."
risk_flags:
  - "P1 (Thinking System core 02/03/04/05) — mitigado por escopo cirúrgico (4 patches aditivos, ~10 linhas novas + 2 sub-seções) + reuso de estruturas existentes + git rollback baseline c3786c2."
recommended_next:
  - "Metacognik revisa A-D → 'APROVA' → sessão canonical_patch separada cola e marca released_with_required_external_audit."
  - "Em paralelo (não bloqueia): Sprint 1 só começa após PATCH 2 aplicado ao canônico."
```

---

## 7. CHECKOUT RELEASE

```txt
CHECKOUT RELEASE — S-USER-PMO-CLAUDE-20260609-001 (parte 3/4)
files_created: 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/PATCH2_USER_IN_RESPONSE_OUT_CANDIDATE.md (este)
files_changed: 000_ROADMAPS/SESSION_REGISTRY.md (já contabilizado na sessão principal)
files_not_touched: canônico Doc 02/03/04/05 (RO — só lidas seções-alvo para casar texto); docs 01-28 demais; docs 29-34;
  ARCHITECTURE_PATCH_REPORT.md; 00_SYSTEM_GOVERNANCE/*; F1 candidate (RO); 8 DRs (RO)
validation: texto apply-ready casado às seções reais (Doc 02 §5.1/5.2; Doc 05 §5.6/5.7; Doc 03 §5.5 pós-PATCH 1;
  Doc 04 §5.8/5.9 nova); AQ-IO-2 + AQ-IO-3 resolvidas; só ALTA, nada de HOLD; nada aplicado
risks_remaining: aplicação aguarda 2ª chave (Metacognik); P1 mitigado por escopo + reuso + rollback
next_step: Metacognik revisa A-D → sessão canonical_patch separada (S-APPLY_PATCH2_CANONICAL.md já pré-montada) aplica
status: released
```
