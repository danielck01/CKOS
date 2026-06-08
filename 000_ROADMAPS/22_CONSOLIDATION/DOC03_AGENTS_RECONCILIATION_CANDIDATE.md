---
title: Doc 03 Agents Reconciliation Candidate
file: DOC03_AGENTS_RECONCILIATION_CANDIDATE.md
layer: auxiliary
doc_type: pmo_patch_candidate
phase: 000_ROADMAPS
category: consolidation
status: awaiting_founder_approval
version: 0.1.0
created_at: 2026-06-02
owner: pmo_ckos
responsible_agent: claude_opus_4_8
session_id: S-P1-CONSOL-L3-CLAUDE-20260602-009
companion_of: 04_CONSOLIDATION_EXECUTION_PLAN.md
target_canonical: 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md
inventory_source: 000_UPGRADE/03_AGENT_CIVILIZATION (65 arq) lidos @ 2026-06-02
reviewers:
  - founder
  - metacognik
approval_required:
  - founder
  - metacognik
non_authority_boundary: >
  Patch candidate. PROPÕE, não aplica. Não edita 03_AGENT_OPERATING_MODEL.md nem
  qualquer canônico 01-28. Não move/arquiva/deleta o UPGRADE/03. Tocar o Doc 03 é P1
  e exige sessão canonical_patch separada com aprovação Founder + Metacognik. Os nomes
  de agente listados aqui são CANDIDATOS de catálogo, não agentes ativos.
tags: [consolidation, agents, doc03, patch-candidate, reconciliation, pmo]
---

# Doc 03 — Reconciliação de Agentes (Patch Candidate)

> **L3 da consolidação (D4 = promoção agressiva).** Compara o 2º sistema de agentes paralelo
> — `000_UPGRADE/03_AGENT_CIVILIZATION/` (65 arq) — contra o canônico
> `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md`, e propõe o que promover.
> **Modo:** `patch_candidate`. Nada é aplicado no Doc 03 por este texto.

---

## 0. Veredito em uma linha (PMO, direto)

**A `UPGRADE/03` é um scaffold gerado por template, raso. O canônico Doc 03 é mais rico em quase tudo.**
O valor real a promover é **estrutural** (1 padrão: o *I/O Contract* por agente) e **um punhado de nomes net-new** de catálogo — não conteúdo. O grande output desta sessão **não é uma promoção**, é a **exposição de um conflito de taxonomia** (superagents-persona vs "commanders" funcionais) que só o Founder + Metacognik resolvem.

⚠️ **Alerta de constituição:** o Doc 03 §1 proíbe "nomes bonitos sem skill contratada". A `UPGRADE/03` é literalmente uma pilha de 28 nomes com prompts genéricos e **zero skill contratada**. Promover o catálogo em massa **violaria o próprio §1**. Por isso a recomendação abaixo é cirúrgica, não atacadista — mesmo sob D4.

---

## 1. Método

- Lidos: README + amostra densa dos 3 níveis (6 superagents × {profile, prompt, policies}, 12 agents × {profile, prompt, io_contract}, 10 subagents). Confirmada **uniformidade total** por nível: os arquivos são o **mesmo template** com a linha "Função" / o nome trocados.
- Sinal real por arquivo = **(nome) + (função de 1 linha) + (shape do io_contract)**. Todo o resto (responsabilidades, inputs, outputs, prompt, policies) é boilerplate idêntico entre instâncias.
- Comparação contra o roster e os schemas do Doc 03 canônico (§5.1–§5.7).

### 1.1 Prova da uniformidade (por que o conteúdo não promove)

| Nível | Arquivos | O que varia entre instâncias | O que é idêntico |
|---|---|---|---|
| superagents | 6 × (profile+prompt+policies) | só a linha **Função** do profile e do prompt | responsabilidades, inputs, outputs, policies (5 regras), estrutura do prompt |
| agents | 12 × (profile+prompt+io_contract) | só a linha **Função** | "Quando acionar", inputs, outputs, prompt, **io_contract** (JSON idêntico, só troca `"agent"`) |
| subagents | 10 × 1 arquivo | **só o título** (nome do arquivo) | a própria "Função" é genérica idêntica: *"Executar uma microtarefa especializada"* |

> Os subagents são o caso extremo: **nem função própria têm** — o único dado é o nome do arquivo.

---

## 2. Inventário comparativo

### 2.1 Superagents

| Canônico Doc 03 (§5.2) | UPGRADE/03 "commanders" |
|---|---|
| Nick, Cognik, Metacognik, PMO_CKOS, Builder Lead, QA Lead, Datta, Ops, Campaign (+Branddock pendente) | genesis_orchestrator, research_commander, execution_commander, governance_commander, knowledge_commander, roi_commander |
| **Modelo:** persona/papel (interface, cognição, metacognição) + leads funcionais + superagents de domínio | **Modelo:** orquestradores por **função/domínio** ("commander" de cada área) |

→ **Taxonomias diferentes, não 1:1.** Ver Conflitos §5 (AQ-A03-1/2/4).

### 2.2 Agents

| UPGRADE/03 agent | Função declarada (1 linha) | Mapeia para canônico? |
|---|---|---|
| financial_roi_analyst | custo, valor, payback, margem, CAC, LTV | ✅ ROI (agent) + ROI Calculator (subagent) |
| rag_curator | busca/organiza/valida memória/docs internos | ✅ RAG Builder Subagent + Datta + Doc 05/28 |
| apify_operator | seleciona e aciona atores Apify | ✅ Research Subagent + Doc 26 (Apify) |
| proposal_architect | proposta: escopo, fases, entregáveis, riscos, ROI | ✅ Proposal Builder (subagent) — UPGRADE sobe p/ agent |
| prompt_engineer | normaliza intenção → comando operacional | ✅ Prompt Refiner (subagent) + Doc 08 |
| reels_director | conduz briefing/execução de Reels/TikTok | ✅ Media/Visual (agent) + Reels Collector (subagent) |
| campaign_strategist | campanhas: narrativa, canais, criativos, orçamento | ✅ Campaign (superagent) — UPGRADE **rebaixa** p/ agent |
| metacognition_critic | clareza, coerência, evidência, risco, prontidão | ⚠️ É **Metacognik** em outro nível → conflito (AQ-A03-3) |
| **product_architect** | intenção → produto, módulos, jornada, requisitos, MVP | 🆕 **sem equivalente canônico** |
| **question_architect** | perguntas adaptativas por lacuna/risco | 🆕 quase sem equivalente (Briefing Parser só parseia) |
| **context_engineer** | respostas/fontes → contexto estruturado | 🆕 existe como "Context Assembler" no Doc 10 (runtime), não como agent |
| ux_strategist | experiência, fluxo, interface, comportamento | 〜 parcial: Visual (agent) + Docs 14/15/16 |

### 2.3 Subagents

| UPGRADE/03 subagent | Mapeia para canônico? |
|---|---|
| gap_detector | ✅ Gap Detector |
| quality_checker | ✅ QA Regression Checker |
| approval_gate_writer | ✅ Approval Manager |
| **source_validator** | 🆕 sem equivalente (valida fontes/evidência) |
| **briefing_score_calculator** | 🆕 sem equivalente (score de clareza do briefing) |
| **summary_compressor** | 🆕 sem equivalente (compressão de contexto) |
| **learning_event_logger** | 🆕 sem equivalente (loga eventos de aprendizado) |
| **task_card_writer** | 🆕 sem equivalente (escreve task cards) |
| **contradiction_detector** | 🆕 sem equivalente (detecta contradições) |
| yaml_writer | 〜 utilitário (escreve YAML frontmatter) |

---

## 3. A PROMOVER

> Sob D4 (agressivo), mas respeitando o §1 do Doc 03. Promoção = entra no patch candidate p/ o Doc 03; **aplicação é sessão separada.**

### 3.1 Estrutural (o valor real)

| ID | Item a promover | Por que é melhor que o canônico | Seção-alvo no Doc 03 | Força |
|---|---|---|---|---|
| **PROMOTE-1** | **Agent I/O Contract** — envelope tipado por agente: `input{context_state, user_answer, evidence}` → `output{findings, gaps, risks, recommended_actions, artifacts, confidence}` | O canônico §5.5 tem **Agent Run** (metadados de execução: run_id, cost, model, status…) mas **não tem contrato de I/O** do agente. Este envelope formaliza o que o §4 já promete em prosa ("insights, hipóteses, riscos, lacunas, artefatos"). É reutilizável e cai direto no F1 (S3 registry, S5 Agent Run). | **novo §5.8 "Agent I/O Contract"** | **ALTA** |
| **PROMOTE-2** | **Convenção de empacotamento da definição de agente** — bundle `profile / prompt / io_contract / policies` por agente | O canônico descreve agentes em prosa; não tem **formato de registro** para quando o agente vira entrada de catálogo (F2). O bundle é um esqueleto de registro reaproveitável. | nota em §5 + cross-ref Doc 06 (Skills Registry) | MÉDIA |

### 3.2 Catálogo — nomes net-new (candidatos, NÃO specs)

> Entram **apenas** no catálogo de **"agentes-hipótese"** que o §5.1 já prevê (agente só ativa com skill contratada). Cada um carrega só a função de 1 linha como hipótese. **Não** criar persona nem prompt agora — isso violaria o §1.

| ID | Candidato | Função-hipótese | Nível | Seção-alvo | Força |
|---|---|---|---|---|---|
| PROMOTE-3a | product_architect | intenção → produto/módulos/jornada/requisitos/MVP | agent | §5.1 agents | MÉDIA |
| PROMOTE-3b | question_architect | perguntas adaptativas por lacuna/risco (liga em S2 "Question Engine" + Study 13 nota 16) | agent | §5.1 agents | MÉDIA |
| PROMOTE-3c | context_engineer | respostas/fontes → contexto estruturado (liga em S1 "Context State") | agent | §5.1 agents | MÉDIA |
| PROMOTE-3d | ux_strategist | UX/fluxo/comportamento, distinto de Visual | agent | §5.1 agents | BAIXA |
| PROMOTE-3e | source_validator | valida fontes/evidência (liga em Doc 18/28) | subagent | §5.1 subagents | MÉDIA |
| PROMOTE-3f | briefing_score_calculator | score de clareza do briefing (liga em S2) | subagent | §5.1 subagents | MÉDIA |
| PROMOTE-3g | summary_compressor | compressão de contexto (liga em Doc 05) | subagent | §5.1 subagents | MÉDIA |
| PROMOTE-3h | learning_event_logger | loga eventos de aprendizado (liga em Doc 13/21/22) | subagent | §5.1 subagents | MÉDIA |
| PROMOTE-3i | task_card_writer | escreve task cards (liga em PMO + Doc 27 Work Orders) | subagent | §5.1 subagents | BAIXA |
| PROMOTE-3j | contradiction_detector | detecta contradições (liga em Metacognik) | subagent | §5.1 subagents | MÉDIA |
| PROMOTE-3k | yaml_writer | utilitário: escreve YAML frontmatter | subagent | §5.1 subagents (opcional) | BAIXA |

**Total a promover:** 2 estruturais + 11 candidatos de catálogo (4 agents + 7 subagents). **Nenhum conteúdo de prompt/profile/policies** — é boilerplate.

---

## 4. JÁ COBERTO (arquivar, sem ação no canônico)

- **Commanders (conceito):** execution_commander ≈ PMO_CKOS+Builder Lead; governance_commander ≈ Metacognik+Doc 12/04/13. O conteúdo não acrescenta nada; a divergência de naming é o Conflito §5, não promoção.
- **Agents cobertos:** financial_roi_analyst, rag_curator, apify_operator, proposal_architect, prompt_engineer, reels_director, campaign_strategist.
- **Subagents cobertos:** gap_detector, quality_checker, approval_gate_writer.
- **Todo o conteúdo de profile / prompt / policies / io_contract-boilerplate:** valor de promoção zero (templates idênticos).

---

## 5. CONFLITOS → ARCHITECTURE_QUESTIONS (não decidir aqui)

| ID | Conflito | Pergunta para Founder + Metacognik |
|---|---|---|
| **AQ-A03-1** | **Duas taxonomias de superagent.** Persona (Nick/Cognik/Metacognik/PMO/Builder/QA/Datta/Ops/Campaign) vs "commander" funcional (genesis/research/execution/governance/knowledge/roi). | Adotar uma camada de "commanders" funcionais? Manter só personas? Ou mapear commander→persona como apelido operacional? |
| **AQ-A03-2** | **Desacordo de nível.** UPGRADE eleva Research, Knowledge e ROI a superagent; o canônico os trata como subagent/agent. E **rebaixa Campaign** (superagent canônico) para agent. | Qual é o nível canônico de Research / Knowledge / ROI / Campaign? |
| **AQ-A03-3** | **Duplicação metacognição.** `metacognition_critic` (agent) tem a função de **Metacognik** (superagent). | É a mesma entidade em dois níveis? Consolidar como Metacognik, ou existe um "critic" de agent distinto do superagent? |
| **AQ-A03-4** | **Orquestrador único vs relay.** `genesis_orchestrator` é um "orquestra tudo" de entrada; o canônico distribui em Nick→Cognik→Metacognik. | Há um orquestrador único de entrada, ou o relay distribuído permanece? |

> Estas 4 AQs são o **produto mais valioso** desta sessão. Não são resolvidas por promoção — são decisão de arquitetura.

---

## 6. Plano de arquivamento do UPGRADE/03

**Sequência obrigatória (não inverter):**

1. Founder aprova este candidate (gate).
2. Sessão `canonical_patch` separada aplica PROMOTE-1/2/3 no Doc 03 (com aprovação Founder + Metacognik).
3. **Só então** arquivar: `git mv 000_UPGRADE/03_AGENT_CIVILIZATION/` → `99_ARCHIVE/000_UPGRADE/03_AGENT_CIVILIZATION/` + README-pointer no lugar antigo.

- **Nunca deletar.** `99_ARCHIVE` é recuperável (git rollback). Preserva proveniência do 2º sistema.
- **Por que arquivar e não manter:** é scaffold raso; todo o valor durável (io_contract + nomes candidatos + as 4 AQs) fica capturado neste candidate + no eventual patch do Doc 03. Manter o bruto = manter o "2º canônico paralelo" que a consolidação existe para colapsar.
- **Mecanismo validado:** `git mv` preserva `[[wikilinks]]` (links por nome); commit por lote = reversível.

---

## 7. Risco P1 + nota de aplicação

- **P1:** o Doc 03 é core do Thinking System (`approval_required: founder`). Mexer em §5 (modelo de agentes) é alto impacto — irradia para Docs 04, 10, 21. **Este texto não aplica nada.**
- **Aplicação:** sessão `canonical_patch` separada, com Founder + Metacognik, escopo = só o Doc 03 + maps/patch report.
- **Guarda anti-bloat (Metacognik):** sob D4 a tentação é despejar 28 nomes no §5.1. Recusado. Só 11 candidatos entram, e **como hipóteses gated em skill contratada** (§1). Promover persona/prompt agora seria criar "nomes bonitos sem skill" — exatamente o que o §1 proíbe.
- **Dependência F1:** PROMOTE-1 (I/O Contract) é o único item com utilidade imediata no backend MVP (S3/S5). Os nomes de catálogo são F2 (Catálogo de agentes).

---

## 8. Resumo para o checkout

- **A promover:** 2 estruturais (I/O Contract ALTA, bundle MÉDIA) + 11 candidatos de catálogo (4 agents + 7 subagents).
- **Já coberto / arquivar:** 6 commanders (conceito) + 7 agents + 3 subagents + todo o boilerplate.
- **Conflitos:** 4 ARCHITECTURE_QUESTIONS (AQ-A03-1..4) — o entregável central.
- **Próximo passo:** aprovação Founder → patch no Doc 03 (sessão separada) → arquivar UPGRADE/03 → seguir L3 (Skills/Transformers/Policies/Tools).
