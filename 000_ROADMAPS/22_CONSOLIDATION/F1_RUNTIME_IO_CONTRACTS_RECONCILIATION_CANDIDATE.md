---
title: F1 Runtime I/O Contracts Reconciliation Candidate (User-in + Response-out)
file: F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md
layer: auxiliary
doc_type: pmo_patch_candidate
phase: 000_ROADMAPS
category: consolidation
status: awaiting_founder_approval
version: 0.1.0
created_at: 2026-06-04
owner: pmo_ckos
responsible_agent: claude_opus_4_8
session_id: S-P1-F1IO-CLAUDE-20260604-001
companion_of: 04_CONSOLIDATION_EXECUTION_PLAN.md
source_proposals:
  - "Founder msg 2026-06-03: User System / User Operating DNA"
  - "Founder msg 2026-06-03: Smart / Cognitive Response Engine"
target_canonical:
  - 01_THINKING_SYSTEM/02_AI_FIRST_OBJECT_MODEL.md
  - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md
  - 01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
reviewers:
  - founder
  - metacognik
approval_required:
  - founder
  - metacognik
gate_dependency: GATE 5 (arquivo 03 BACKEND_MVP_THIN_SLICE) — bloqueante
non_authority_boundary: >
  Patch candidate. PROPÕE, não aplica. Não edita nenhum canônico 01-28. Não cria
  pasta de sistema (/CKOS_USER_SYSTEM/, Response Engine docs), não cria schema SQL,
  não cria agente real, não toca UI. Aplicação = sessão canonical_patch separada,
  pós-GATE 5, com aprovação Founder + Metacognik. Os nomes/campos aqui são CANDIDATOS,
  não specs ativas.
tags: [consolidation, runtime, user-system, response-engine, io-contract, patch-candidate, reconciliation, pmo, gate5]
---

# F1 Runtime — Contratos de Entrada e Saída (Patch Candidate)

> **Reconciliação de duas propostas do Founder (2026-06-03)** — "User System / User Operating DNA"
> e "Smart / Cognitive Response Engine" — contra o canônico existente.
> **Tese central desta nota:** as duas propostas **não são dois sistemas**. São o **contrato de
> entrada** (User-in: identidade → intenção) e o **contrato de saída** (Response-out: output tipado
> → ação) **do mesmo runtime da F1** (`Doc 10`). Tratá-las como sistemas separados refabrica o 1:35.
> **Modo:** `patch_candidate`. Nada é aplicado em canônico por este texto.

---

## 0. Veredito em uma linha (PMO, direto)

**~75% das duas propostas já é canônico** — sobretudo o pipeline de 9 camadas do Response Engine, que é o **fluxo §5.2 do Doc 10 quase verbatim**. O valor net-new é **pequeno, denso e diferenciador**: um punhado de campos/políticas que se encaixam em Doc 02/03/04/05/10 como patch — **não** um sistema novo, **não** 20 docs, **não** SQL agora. Tudo é **GATE-5-blocked** (refina o runtime que o GATE 5 ainda vai definir). O entregável mais valioso é **AQ-IO-1**: *o thin-slice começa no usuário ou no projeto?* — pergunta que vai direto ao pacote do GATE 5.

---

## 1. Método e enquadramento

- **Lido @ 2026-06-04 (read-only):** Doc 02 §5.1–5.6, Doc 03 §5.1–5.6, Doc 05 §5.1–5.7, Doc 10 §5.1–5.8. Grep de cobertura em `0X_*/` para `onboarding|tribe|user dna|wallpaper|glassmorphism`.
- **Sinal real por proposta** = o resíduo depois de subtrair (a) o que já tem casa canônica e (b) o que é UI da F4.
- **As duas propostas são uma fatia só.** Visualização:

```txt
User-in (identidade → INTENÇÃO ENTRA)        Response-out (OUTPUT tipado → AÇÃO SAI)
        │                                                    │
        └──────────────  Doc 10 §5.2  (runtime F1)  ─────────┘
   passo 1-3: Intent Resolver + Context     passo 8-14: Worker + Artifact + Memory + Projector
```

### 1.1 Achados de cobertura (a prova de que não é sistema novo)

| Tema | Menções no canônico inteiro | Leitura |
|---|---|---|
| `onboarding` | 8 (periférico, 3 arquivos) | **gap real** — não modelado |
| `user dna / user identity / perfil do usuário` | 3 (Doc 11, Doc 12) | **gap real** — User não é objeto |
| `tribe / persona / user mode` | 21 (mas "persona" = agente/marca, não segmento de usuário) | **net-new** |
| `wallpaper / glassmorphism / cognitive atmosphere` | 6 (node canvas, exec protocol) | **F4 (UI)** — não é sistema cognitivo |
| pipeline de resposta (intent→context→route→compose→memory) | Doc 10 §5.2 inteiro | **duplicata** — já é o runtime |

---

## 2. Inventário comparativo

### 2.1 User-in — proposta "User Operating DNA" vs canônico

| Peça da proposta | Casa canônica | Veredito |
|---|---|---|
| `User` como modelo cognitivo-operacional vivo | Doc 02 §5.2 só tem **`Stakeholder`** (papel plano: founder/owner/reviewer…) | 🆕 **PROMOVER** (U1) |
| Memória do usuário entre projetos | Doc 05 §5.6 `memory_object` é escopado `project_id`+`workspace_id` — **não há `user_id` persistente** | 🆕 **PROMOVER** (U2) |
| Aprendizado declarado→observado→inferido→validado | Doc 05 tem trust hierarchy (§5.5) mas não o eixo de preferência do usuário | 🆕 **PROMOVER** (U3) |
| Tribos como modos dinâmicos | sem equivalente (persona canônica = agente/marca) | 🆕 **PROMOVER** (U4) — derivada, não wizard |
| Onboarding como engine adaptativa | `onboarding` = 8 menções periféricas; é a 1ª captura de intenção (F1-S1) | 🆕 **PROMOVER** (U5) |
| Memory taxonomy (project/agent/visual/ROI…) | Doc 05 §5.1–5.2 já tem camadas + tipos + memory object | ✅ **JÁ COBERTO** |
| Policies (autonomy 1-5, budget, approval) | Doc 04 + Doc 12 | ✅ **JÁ COBERTO** |
| Transformers (Briefing→Proposal…) | Doc 09 | ✅ **JÁ COBERTO** |
| ROI em camadas + fórmulas | Doc 21 | ✅ **JÁ COBERTO** |
| Smart questions com metadados | Doc 03 Question Engine + Study 13 nota 16 + F1-S2 | ✅ **JÁ COBERTO** |
| Cognitive Atmosphere / glass / wallpaper / widgets | — (é UI) | ⛔ **F4 — NÃO ENTRA** (§5) |
| `/CKOS_USER_SYSTEM/` 13 subpastas + SQL | — | ⛔ **fragmentação / Doc 11 gated** (§5) |

### 2.2 Response-out — proposta "Cognitive Response Engine" vs canônico

| Camada da proposta | Casa canônica (Doc 10 §5.2) | Veredito |
|---|---|---|
| Intent Interpreter | passo 2 — Intent Resolver `IntentResolved{intent, confidence}` | ✅ **JÁ COBERTO** |
| Context Reader | passo 3 — Context Assembler + Doc 05 Context Packet | ✅ **JÁ COBERTO** |
| Missing Info Detector | passo 10 — Metacognik `{confidence, risk}` + F1-S2 | ✅ coberto; **refinar** (R3) |
| Policy & Safety Layer | passo 4+11 — Policy/Permission Engine + Approval Gate (Doc 04/12) | ✅ **JÁ COBERTO** |
| Skill/Agent Router | passo 7 — Agent + Model + Tool Router | ✅ **JÁ COBERTO** |
| Response Composer | passo 8 — Worker executa skill + partial outputs | ✅ coberto; **tipar** (R1) |
| Action Extractor | passo 12 — Artifact Pipeline + lifecycle Doc 02 + Doc 27 | ✅ **JÁ COBERTO** |
| Memory Updater | passo 13 — Memory Writer `MemoryUpdated` | ✅ **JÁ COBERTO** |
| Metric Tracker | passo 14 — Projectors + Doc 13 Tracer / Doc 21 | ✅ **JÁ COBERTO** |
| `response_object` (JSON) | Doc 03 §5.5 **Agent Run** já tem input/output/confidence/risks/gaps/evidence/cost/model/status | ✅ coberto; **enriquecer** (R1) |
| `response_type` + `depth_level` + `reasoning_mode` | sem equivalente — runtime **executa** runs mas não **tipa** a forma do output | 🆕 **PROMOVER** (R1) — o gem |
| Policies anti-padrão (over-ask/over-explain/fake-certainty/depth-fit) | sem equivalente explícito | 🆕 **PROMOVER** (R2) |
| Response Contract V1 (9 pontos) | sem equivalente (qualidade de output) | 🆕 **PROMOVER** (R4) |
| User Mode vs Audit Mode | sem equivalente | 🆕 **PROMOVER** (R5) — princípio agora, UI F4 |
| Response metrics / utility score | Doc 13 (evals) + Doc 21 (ROI) | ✅ **JÁ COBERTO** |
| Response UI / botões (Sprint 7) | — (é UI) | ⛔ **F4 — NÃO ENTRA** |
| docs 01-07 + 4 tabelas SQL como sistema | — | ⛔ **fragmentação / Doc 11 gated** |

---

## 3. A PROMOVER (o net-new — pequeno e cirúrgico)

> Entra **apenas** no patch candidate. Aplicação = sessão separada pós-GATE 5.

### 3.1 User-in

| ID | Item | Por que é net-new | Alvo canônico | Força |
|---|---|---|---|---|
| **PROMOTE-U1** | `User` como objeto de 1ª classe (vivo, com `confidence`/estado, no padrão do Briefing) | Doc 02 só tem `Stakeholder` plano; runtime começa em Workspace→Project | Doc 02 §5.1/5.2 (+ relação User⇄Stakeholder) | **ALTA** |
| **PROMOTE-U2** | Memória escopada `user_id`, persistente **entre** projetos | `memory_object` é só project/workspace | Doc 05 §5.1/5.6 (nova camada de escopo) | **ALTA** |
| **PROMOTE-U3** | Aprendizado de preferência em 4 níveis (declarado→observado→inferido→validado) + confidence | trust hierarchy existe, eixo de usuário não | Doc 05 (§5.5 + §5.6) | MÉDIA-ALTA |
| **PROMOTE-U4** | Tribos como **modos dinâmicos** `f(comportamento, intenção, projeto, feedback)`, scored por evidência, re-pesados por projeto | net-new; **derivada, não wizard** (Princípio #7) | Doc 02 (projeção) ou Doc 03 | MÉDIA |
| **PROMOTE-U5** | Onboarding = engine adaptativa = **1ª captura de intenção** (semente declarada mínima + crescimento progressivo) | gap real (8 menções); é o front do F1-S1 | Doc 10 §5.2 passo 1 + Doc 15 + F1-S1/S2 | MÉDIA |

### 3.2 Response-out

| ID | Item | Por que é net-new | Alvo canônico | Força |
|---|---|---|---|---|
| **PROMOTE-R1** | **Tipagem da resposta**: `response_type` (diagnóstica/estratégica/decisão/operacional/criativa/técnica/learning/ROI) + `depth_level` (direta/estruturada/estratégica/profunda) + `reasoning_mode` | runtime executa runs mas **não classifica a forma** do output | Doc 03 §5.5 (campo no Agent Run) + Doc 10 §5.2 passo 2/8 | **ALTA** |
| **PROMOTE-R2** | 5 policies anti-padrão: `do_not_over_ask`, `do_not_over_explain`, `no_fake_certainty`, `assumption_transparency`, `depth_fit` + princípio *"profundidade não é tamanho, é precisão operacional"* | sem equivalente; baratíssimo e diferenciador | Doc 04 (comportamento) + Doc 03 | **ALTA** |
| **PROMOTE-R3** | Gate de lacuna em 3 níveis: leve→hipótese / média→responde+sinaliza / crítica→pergunta-antes | refina o Question Engine: define **quando** perguntar vs assumir | F1-S2 + Doc 03 (Metacognik) | MÉDIA-ALTA |
| **PROMOTE-R4** | Response Contract V1 — contrato interno mínimo de toda resposta importante (9 pontos) | artefato de qualidade net-new, alinhado à DNA de governança | Doc 03 (qualidade de output) ou Doc 13/20 | MÉDIA |
| **PROMOTE-R5** | User Mode vs Audit Mode — raciocínio inspecionável sob demanda (não ruído sempre-ligado) | princípio net-new; a parte visível é F4 | princípio em Doc 03/13; UI **deferida F4** | MÉDIA |

**Total net-new:** 10 itens (5 User-in + 5 Response-out). **Os mais fortes:** U1, U2 (ALTA) e R1, R2 (ALTA).

---

## 4. JÁ COBERTO (não criar — usar o que existe)

- **Pipeline de 9 camadas inteiro** → Doc 10 §5.2 (mapa 1:1 em §2.2). Recriar = duplicar o doc executável mais central.
- **Policy/Safety + Memory + Métricas + Routing + Action Extractor + Transformers + Skills** → Docs 04/12, 05, 13/21, 03/10, 02/27, 09, 06.
- **`response_object` JSON** → é o **Agent Run** (Doc 03 §5.5) + campos de R1. Não é objeto novo.
- **Taxonomia de memória + ROI em camadas + smart questions** → Docs 05, 21, 03.

---

## 5. NÃO ENTRA / DEFER-F4 (recusado agora, com motivo)

| Item | Motivo | Destino |
|---|---|---|
| Cognitive Atmosphere, Glass System, wallpaper, widgets, cards, white-label visual | UI — Princípio #1 (doc→runtime→UI). Construir agora = o "Notion bonito com IA" que o próprio Founder alertou (Risco #1) | **F4** (Docs 14/15/16) |
| `/CKOS_USER_SYSTEM/` (13 subpastas) + Response Engine docs 01-07 | refabrica o 1:35 — fragmentação que a F0 existe para colapsar | **recusado** |
| Schemas SQL (`user_profiles`, `response_objects`, `user_memory_events`…) | persistência vive no Doc 11, gated | **Doc 11**, candidate pós-GATE 5 |
| Banco de 100 smart questions | prematuro; 7-12 amarradas ao F1-S1/S2 bastam | **F1** |
| ROI Engine / Policies / Transformers como docs novos | duplicação de Docs 21/04/09 | **recusado** |

> **Princípio a capturar (barato, governa a F4):** *o visual responde a estado (intenção/risco/fase/foco), nunca é tema.* Construir zero agora; só registrar a regra.

---

## 6. CONFLITOS → ARCHITECTURE_QUESTIONS (alimentam o GATE 5, não decidir aqui)

| ID | Pergunta para Founder + Metacognik | Impacto |
|---|---|---|
| **AQ-IO-1** | O thin-slice do MVP (arquivo 03) começa em **`user identity` + 1ª intenção** ou em **`project`**? | **Decisão do GATE 5.** É o entregável central desta nota. |
| **AQ-IO-2** | `User` é objeto novo de 1ª classe, ou **promoção/extensão do `Stakeholder`**? | Taxonomia Doc 02 |
| **AQ-IO-3** | Memória `user_id` é nova **camada de escopo no Doc 05**, ou identity store separado? | Fronteira Doc 05/11 |
| **AQ-IO-4** | Tribo é **objeto**, **score derivado por agente**, ou **projeção de memória**? Quem computa? | Evita a armadilha persona-estática |
| **AQ-IO-5** | Tipagem de resposta (R1) vive **no Agent Run (Doc 03)** ou como **objeto `Response` separado**? | Evita duplicar o Run |

---

## 7. Risco P1 + sequenciamento

- **GATE-5-blocked (duplo):** todo este resíduo refina o runtime cuja espinha o **GATE 5 ainda vai fixar**. Aplicar antes = over-engineering, exatamente como o Doc 11 RAG schema. *(Confirmado pelo Founder 2026-06-03: "GATE 5 primeiro".)*
- **Alimenta o GATE 5:** AQ-IO-1 deve entrar no `GATE5_FOUNDER_DECISION_PACKAGE.md` como 10ª pergunta (sequência user-first do thin-slice).
- **Aplicação = UMA sessão `canonical_patch`** pós-GATE 5 (não dois sistemas), tocando Doc 02 + Doc 05 + Doc 03 + Doc 04 + Doc 10, com Founder + Metacognik. P1, alto impacto (core do Thinking + Runtime).
- **Este texto não aplica nada.** Nenhum canônico, nenhuma pasta, nenhum schema, nenhuma UI.

---

## 8. Resumo para o checkout

- **Net-new a promover:** 10 itens (U1-U5 + R1-R5). Mais fortes: U1/U2 + R1/R2 (ALTA).
- **Já coberto:** o pipeline inteiro (Doc 10 §5.2) + policies/memory/métricas/routing/transformers/skills.
- **Não entra:** visual (F4), folder-trees (fragmentação), SQL (Doc 11 gated), 100 perguntas (prematuro).
- **Conflitos:** 5 AQs (AQ-IO-1..5) — AQ-IO-1 é input do GATE 5.
- **Próximo passo:** fechar **GATE 5** → adicionar AQ-IO-1 ao pacote de decisão → (pós-GATE 5) 1 sessão canonical_patch aplica U/R em Doc 02/05/03/04/10.
