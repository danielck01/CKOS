---
title: CKOS Master Expansion Roadmap
file: CKOS_MASTER_EXPANSION_ROADMAP.md
layer: auxiliary
doc_type: pmo_roadmap
phase: 000_ROADMAPS
category: consolidation
status: draft
version: 0.2.0
created_at: 2026-06-01
updated_at: 2026-06-02
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - founder
  - metacognik
approval_required:
  - founder
  - pmo_ckos
confidence: medium
provenance_status: pmo_synthesis_unverified
source_tool: claude_opus_4_8
purpose: Roadmap mestre de expansão do CKOS como sistema AI-first, das fases de convergência documental até autonomia, negócio e marketplace, com dependências, gates e critérios de saída. Companion do board CKOS_EXPANSION_KANBAN.md.
intelligence_level: highest
non_authority_boundary: >
  Roadmap auxiliar/PMO. Sequencia e recomenda; nao governa, nao canoniza, nao implementa.
  Cada fase exige seus proprios gates/checkouts. Nenhuma implementacao (backend/UI/API)
  e autorizada por este documento.
related_notes:
  - 00_CKOS_CONSOLIDATION_MAP_AND_GAP_AUDIT.md
  - 01_MULTI_SESSION_CONTROL_ROOM_RUNBOOK.md
  - 02_DNA_SYSTEM_COMPARISON_AND_INTEGRATION_MAP.md
  - CKOS_EXPANSION_KANBAN.md
tags: [roadmap, expansion, ai-first, phases, architecture, master]
---

# CKOS — Roadmap Mestre de Expansão (AI-First)

> **Os 5 gates são apenas a Fase 0.** Este documento mostra o arco completo: de
> convergência documental até CKOS operando como organismo que cresce, decide,
> aprende e gera ROI com mínima intervenção do Founder.
> **Companion:** o board navegável vive em [CKOS_EXPANSION_KANBAN.md](CKOS_EXPANSION_KANBAN.md).

---

## Princípios de arquitetura (regem todas as fases)

1. **Documentação antes de runtime; runtime antes de UI.** Nunca inverter.
2. **Fonte de verdade única = canônico 01-28** (GATE 0 declarou 01-27; Doc 28 somado via GATE 3). Fronteira autoritativa: `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`.
3. **Thin slice antes de civilização.** 1 intenção → 4 agentes → 1 decisão → 1 evidência → 1 memória. Escala depois.
4. **Autonomia gated, nunca presumida.** Cognik propõe, Metacognik audita, Founder aprova risco/custo acima do teto.
5. **Tudo vira evento + memória + ROI.** Sem event log, é chat bonito. Sem memória, aluciná. Sem ROI, é caro e cego.
6. **Proativo, não só reativo.** Research real (OpenRouter/Perplexity/Apify), não só conhecimento de LLM.
7. **O DNA cresce por uso, não por wizard.** Cada interação é depósito no DNA do usuário.

---

## Mapa de fases (visão de 1 página)

```txt
F0 Convergência Documental      ── os 5 gates + docs 28-34 + cleanup        [AGORA]
F1 Runtime Cognitivo MVP        ── thin slice: intent→run→evento→memória→ROI
F2 Civilização de Agentes&Skills ── 4 agentes → catálogo; skills sênior; model router; research
F3 Motor de DNA                 ── Creative DNA vivo, bootstrapping, calibração
F4 Superfícies de Produto       ── Project Pulse, Command Center, Node Canvas
F5 Conectores & Integrações     ── MCP, OAuth, Apify actors, n8n como acelerador
F6 Autonomia & Auto-Evolução    ── níveis de autonomia, Builder Subagents, heartbeat
F7 Negócio & Escala             ── ROI, créditos/billing, suporte, Creator Mode, Marketplace
FX Governança & Segurança       ── transversal, contínua (12 Security, 13 Evals/Cost, QA)
```

Dependências macro: **F0 → F1 → (F2 ∥ F3) → F4 → (F5 ∥ F6) → F7**, com **FX** correndo em paralelo o tempo todo.

---

## F0 — Convergência Documental `[AGORA]`

**Meta:** uma spec, um backlog, zero ambiguidade. Mata a confusão antes de construir.

| Gate | Entrega | Status |
|---|---|---|
| GATE 0 | Canônico 01-27 declarado fonte única | ✅ |
| GATE 1 | Patches A+B+C — dups 18/19 + ordinal 21 | ✅ 2026-06-02 |
| GATE 2 | Comparação DNA + integração (2 sistemas) | ✅ |
| GATE 3 | **Doc 28** — Notes/RAG/Knowledge canônico | ✅ 2026-06-02 (fan-in Claude) |
| GATE 4 | Control Room Runbook v1.1 | ✅ 2026-06-02 (fan-in Claude) |
| GATE 5 | Backend MVP thin-slice spec (arquivo 03) | ✅ spec criada + fan-in Claude; ⏳ aguarda aprovação Founder |
| +Docs | Docs 29-34 | ⚠️ paralelo com F1 — não bloqueia GATE 5 |
| +Promo | Joias do DNA (DNA-PC-1..7) | paralelo com Doc 28 |

> **BORDA DURA DA F0 (PMO 2026-06-02):** F0 = GATEs 0-5 + reconciliação + Doc 11 candidate. **Nada mais entra.**
> **Saída:** GATE 5 aprovado pelo Founder fecha a F0 e abre a F1 (data-alvo 2026-06-09, confirmar).
> **Fora da F0** (paralelo com F1, nunca antes): Docs 29-34, joias DNA, Vault Loop, Fan-In recorrente.
> **Versionamento:** `git init` no core feito 2026-06-02 (baseline commitado; paperclip_study e node_modules ignorados).
> Batch-writing de docs canônicos em sessão única **não recomendado** (degrada qualidade e fan-in). Paralelismo correto = Codex1 ≠ Codex2 em frentes diferentes.

**Saída:** spec única + backlog único + Doc 28 + GATE 5 desbloqueado.

---

## F1 — Runtime Cognitivo MVP

**Meta:** o "AI-first de verdade" rodando como espinha fina. Base: `000_UPGRADE/13_MVP_FUNCTIONAL/sprints.md`.

**Slice vertical:**
```txt
Intenção (Doc 15) → Intent Resolver + Cognik (Doc 03/10) → Metacognik approval (Doc 04)
→ Work Order (Doc 27) → Agent Run (Doc 03) → Event Log (Doc 10/11/13)
→ Evidência → Memória (Doc 05) → ROI (Doc 21)
```

| Sprint | Entrega | Doc dono |
|---|---|---|
| S1 | Intent Resolver + Context State + 1 output | 10 |
| S2 | Question Engine + score de clareza + lacunas/risco | 03 |
| S3 | Registry de agentes/skills + policy checker + approval gates | 03/04/06 |
| S4 | Event Log (sem ele, vira chat) | 10/11/13 |
| S5 | Work Order + Agent Run end-to-end | 27 |
| S6 | Feedback pós-output + memória + ROI | 05/21/22 |

**Agentes do MVP (4):** Cognik (governa) · PM/Builder (planeja) · Risk=Metacognik (audita) · ROI (calcula).
**Saída:** uma intenção real percorre o pipeline inteiro e deixa rastro auditável.

---

## F2 — Civilização de Agentes & Skills

**Meta:** sair de 4 agentes para um ecossistema; skills de nível sênior; inteligência proativa multi-modelo.

- **Catálogo de agentes** (Doc 03): superagents (Nick, Cognik, Metacognik, PMO, Builder Lead, QA Lead, Datta, Ops, Campaign) + agents de domínio (ativam só com skill contratada) + subagents.
- **Skills como discipline-master docs** (Doc 06 + metodologia Human Academy): doutrina + anti-padrões + score 0-10 + testes. (DNA-PC-3)
- **Skill Selector** — agente que escolhe/ranqueia skills no momento da tarefa (lacuna L-02).
- **Skill request / learning loop** — agente pede skill a outro; modo aprendizado recebe e registra (lacuna L-03, liga em F6).
- **Model Router** (Doc 26/10): OpenRouter multi-modelo; reasoning alto só com decisão/risco/custo/arquitetura.
- **Research proativo** (Doc 18/26): Perplexity, deep research, Apify, dados reais — não só LLM.

**Saída:** agentes com capacidades reais, selecionáveis, com pesquisa proativa e roteamento de custo.

---

## F3 — Motor de DNA `(pode correr ∥ F2)`

**Meta:** o DNA do usuário cresce sozinho. Base: arquivo 02 (DNA-PC-1..7).

- **Creative DNA** como objeto vivo (Doc 02) com estados `DNA-0 → DNA-vivo`.
- **Entrada por contexto:** criação de projeto, briefing, missão sem DNA (**bootstrapping just-in-time**).
- **Crescimento:** briefing/perguntas/notas/research/feedback como depósitos automáticos (Doc 05).
- **Calibração:** feedback→learning + DNA-consistency como métrica de ROI/QA (Doc 21/13/22).

**Saída:** todo projeto tem DNA que enriquece a cada interação, sem wizard manual.

---

## F4 — Superfícies de Produto

**Meta:** o usuário vê o sistema pensar, fazer, esperar, custar, arriscar e aprender.

- **Project Pulse / Dashboard** (Doc 14): projeção viva do runtime.
- **Command Center** (Doc 15): camada de intenção/aprovação; emite eventos, não executa direto.
- **Node Canvas** (Doc 16): objetos vivos do runtime (intenção, hipótese, plano, risco, aprovação, artefato, ROI, memória).
- Frontend como **projeção do runtime** (DNA/15_FRONTEND contracts como referência).

**Saída:** bastidores de um AI-first nascendo, visíveis e operáveis.

---

## F5 — Conectores & Integrações `(pode correr ∥ F6)`

**Meta:** o sistema toca o mundo real, com governança. Base: Doc 26.

- **MCP** (ferramentas controladas), **OAuth** (Google, Meta), **Apify actors** (coleta).
- **n8n como acelerador, não core** — fluxos críticos migram para código próprio.
- Tools Registry real (OpenRouter, Apify) com cost guard.

**Saída:** conectores substituíveis, auditáveis, sem virar dependência de runtime.

---

## F6 — Autonomia & Auto-Evolução

**Meta:** o sistema age proativamente e ajuda a se construir. Base: Docs 04, 21, 25.

- **Níveis de autonomia** + auto-approval para ações reversíveis de baixo risco (Doc 04).
- **Approval batches** — Founder aprova lotes de 5-10, não item a item (Note 19/22).
- **Builder Subagents** (Frontend/Backend/Data/RAG/Automation/QA) sob Builder Lead.
- **Self-Evolving System** (Doc 21/25): sandbox, eval-antes-de-merge, rollback.
- **Heartbeat / proatividade**: sistema acorda, lê contexto, age, audita, atualiza memória.

**Saída:** CKOS reduz a carga do Founder a decisões críticas; começa a expandir-se.

---

## F7 — Negócio & Escala

**Meta:** monetização, suporte e ecossistema. Base: Docs 21-24 + Creator Mode.

- **ROI** operacional (Doc 21) como métrica de produto.
- **Créditos / Planos / Billing** (Doc 24) com budget gates.
- **Suporte IA-humano** (Doc 23).
- **Creator/Client Project Mode** (CKOS_CREATOR_MODE_PACK) — criar projeto por intenção mínima.
- **Marketplace / CKStore** — skills, workflows, agentes, conectores como capacidades distribuíveis.

**Saída:** CKOS como produto/plataforma sustentável e expansível por terceiros.

---

## FX — Governança & Segurança `(transversal, contínua)`

Corre em **todas** as fases:
- **Segurança/Permissões/Data Governance** (Doc 12): secrets, isolamento, RLS.
- **Evals/Observability/Cost** (Doc 13): traces, qualidade, custo por run.
- **QA & Founder Approval** (Doc 20): gates de qualidade.
- **Multi-session policy** + checkout locks + BRA + fan-in (já ativos).
- **Vault Operating Loop** (process layer): cadência daily-intake / fan-in / nightly / weekly que **opera** os boards e registries existentes — não é runtime. É o precursor manual do Heartbeat (F6). Regra: não simular event store em Markdown (Princípios #1 e #5); cada rotina tem dono e condição de morte. Peça de maior ROI imediato = **Session Fan-In recorrente** com output `NEXT_SESSION_PROMPTS` (puxado para a F0). **Não** abrir Study Layer 15 nem ~11 arquivos novos durante a convergência — fragmentação é o problema, não a falta de docs.

**Regra:** nenhuma fase "termina" sem seus controles FX satisfeitos.

---

## Horizontes de tempo (para o board)

| Horizonte | Fases | Foco |
|---|---|---|
| **Agora** | F0 | convergência: 5 gates, Doc 28, cleanup |
| **Curto** | F1 | runtime MVP thin-slice |
| **Médio** | F2, F3 | agentes/skills + DNA |
| **Longo** | F4, F5, F6 | produto, conectores, autonomia |
| **Visão** | F7 | negócio, escala, marketplace |
| **Contínuo** | FX | governança e segurança |

---

## Critérios de saída por fase (resumo)

- **F0:** 1 spec + 1 backlog + Doc 28 aberto + Control Room ativo.
- **F1:** 1 intenção percorre intent→run→evento→memória→ROI com rastro.
- **F2:** skill selecionável + research proativo + model router operando.
- **F3:** projeto com DNA que cresce por uso.
- **F4:** runtime visível e operável na UI.
- **F5:** conectores reais governados e substituíveis.
- **F6:** autonomia por níveis + builder subagents + self-evolving sandbox.
- **F7:** créditos/billing + creator mode + marketplace.

---

## Relação com os boards existentes

- [TASK_KANBAN.md](../TASK_KANBAN.md) = board **operacional documental** (tarefas de doc do dia a dia).
- [CKOS_EXPANSION_KANBAN.md](CKOS_EXPANSION_KANBAN.md) = board **estratégico de expansão** (este roadmap, navegável).
- Este doc = a **narrativa/arquitetura** por trás do board estratégico.
