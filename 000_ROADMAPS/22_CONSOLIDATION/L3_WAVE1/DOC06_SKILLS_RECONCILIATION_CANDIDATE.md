---
title: Doc 06 Skills Reconciliation Candidate
file: DOC06_SKILLS_RECONCILIATION_CANDIDATE.md
layer: auxiliary
doc_type: pmo_patch_candidate
phase: 000_ROADMAPS
category: consolidation
status: awaiting_founder_approval
version: 0.1.0
created_at: 2026-06-04
owner: pmo_ckos
responsible_agent: codex_1
session_id: S-P1-L3-CODEX1-20260604-001
track: TR-SKILLS
companion_of: 00_WAVE1_DISPATCH_AND_PROTOCOL.md
target_canonical: 02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md
inventory_source: 000_UPGRADE/04_SKILLS_REGISTRY (15 arq: README + 14 skill files) lidos @ 2026-06-04
reviewers:
  - founder
  - metacognik
approval_required:
  - founder
  - metacognik
non_authority_boundary: >
  Patch candidate. PROPOE, nao aplica. Nao edita 02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md
  nem qualquer canonico 01-28. Nao move/renomeia/arquiva/deleta o UPGRADE/04.
  Tocar o Doc 06 e P1 e exige sessao canonical_patch separada com aprovacao Founder +
  Metacognik. Os nomes de skill listados aqui sao candidatos de catalogo, nao skills
  ativadas em runtime.
tags: [consolidation, skills, doc06, patch-candidate, reconciliation, l3, pmo]
---

# Doc 06 - Reconciliacao de Skills (Patch Candidate)

> **L3 da consolidacao (TR-SKILLS).** Compara `000_UPGRADE/04_SKILLS_REGISTRY/`
> (15 arquivos) contra o canonico `02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md`, e
> propoe o que promover. **Modo:** `patch_candidate`. Nada e aplicado no Doc 06 por este texto.

---

## 0. Veredito em uma linha (PMO, direto)

**A `UPGRADE/04` e um scaffold curto e repetitivo: mais estruturado que prompt solto, mas muito menos governado que o Doc 06.**
O valor real a promover nao e a doutrina de cada skill; e **um envelope minimo de I/O executavel** e um pequeno conjunto de **nomes granulares** que o Doc 06 cobre so parcialmente ou de modo implicito.

Alerta de constituicao: o Doc 06 exige owner, quando nao usar, risco, workflow, prompts base e `eval_ref`. A `UPGRADE/04` tem entrada, saida e criterio de sucesso, mas nao tem owner, allowed_tools, autonomia, metricas, edge cases, prompts base ou eval. Promover tudo em massa criaria "skills bonitas" sem contrato completo.

---

## 1. Metodo

- Lidos: `README.md` + 14 arquivos em `skills/`.
- Comparado contra o Doc 06 canonico v1.1.0: proposito, taxonomia, template oficial, skills MVP, autonomia, edge cases, metricas e criterios de aprovacao/reprovacao.
- Sinal real por arquivo UPGRADE = **nome + definicao de 1 linha + shape comum de Input/Output + criterio de sucesso comum**.
- Tudo que envolver aplicacao no Doc 06, runtime, SQL, backend, UI, agentes reais ou move/archive do UPGRADE fica fora desta sessao.

### 1.1 Prova da uniformidade (por que o conteudo por skill quase nao promove)

Comparacao direta entre `adaptive_questioning.md` e `workflow_design.md` mostrou que variam apenas:

| Campo | Varia? | Evidencia |
|---|---|---|
| Titulo | sim | `# Skill - adaptive_questioning` vs `# Skill - workflow_design` |
| Definicao | sim | pergunta adaptativa vs workflows/sprints |
| `Output.skill` | sim | valor do identificador da skill |
| Quando usar | nao | frase identica: usar quando intencao/briefing/agente exigir a capacidade |
| Input JSON | nao | `context_state`, `goal`, `constraints`, `evidence` |
| Output JSON | nao | `skill`, `result`, `confidence`, `risks`, `next_actions` |
| Criterio de sucesso | nao | resultado operacional que alimenta agente, tarefa, proposta, workflow ou decisao |

Logo, a `UPGRADE/04` nao contem anti-padroes, rubricas, testes, score 0-10, discipline-master, metricas por skill ou policy por skill. Ela contem um **contrato minimo repetido**.

### 1.2 Respostas as perguntas do PMO

| Pergunta | Resposta |
|---|---|
| Boilerplate vs real | Boilerplate com valor estrutural leve. Os 14 arquivos repetem o mesmo corpo; so nome, definicao e `Output.skill` mudam. |
| Modelo de skill | Doc 06 = registry governado, taxonomia, template, owner/review, autonomy, approvals, allowed_tools, inputs/outputs, triggers, edge cases, metrics, workflow, transformers e eval_ref. UPGRADE/04 = cartao minimo com Input/Output JSON e criterio de sucesso. |
| Campo estrutural novo | Sim: envelope comum `Input -> Output` com `confidence`, `risks` e `next_actions`. Doc 06 lista `required_inputs`/`outputs`, mas nao exemplifica o shape minimo comum. |
| Net-new vs coberto | Net-new forte: `intent_classification`, `context_engineering`, `roi_modeling`, `learning_extraction`. Parcial/especializado: `deep_research_synthesis`, `apify_scraping_planning`, `visual_briefing`, `reels_storytelling`. Coberto: `proposal_generation`, `quality_assurance`, `adaptive_questioning`, `task_decomposition`, `workflow_design`, `metacognitive_review`. |
| Ligacao F1/F2 | F1 direto: I/O contract, `intent_classification`, `context_engineering`, `quality_assurance`/`qa-gate`, `metacognitive_review` como avaliacao. F2/catalogo: especializacoes criativas e research/tool planning. |
| Conflito de taxonomia | Sim: UPGRADE usa snake_case e micro-skills; Doc 06 usa kebab-case, familias e skills mais amplas. Apify tambem cruza boundary skill vs tool/connector Doc 26. |

---

## 2. Inventario comparativo

### 2.1 Estrutura do registry

| Superficie | Doc 06 canonico | UPGRADE/04 |
|---|---|---|
| Definicao de skill | capacidade modular, versionada, auditavel, que transforma intencao em acao controlada | capacidade reutilizavel; agentes selecionam skills registradas |
| Taxonomia | 7 familias: Strategy, Research, Creative, Product/UX, Development, Operations, Metacognitive | nenhuma taxonomia explicita |
| Template | `skill_id`, category, owner/review, autonomy, approvals, allowed_tools, inputs/outputs, triggers, edge cases, metrics, workflow, transformers, eval_ref | markdown curto: definicao, quando usar, input JSON, output JSON, criterio de sucesso |
| Aprovacao | exige output verificavel, owner, quando nao usar, risco, workflow, prompts base, eval_ref | criterio generico: alimentar agente/tarefa/proposta/workflow/decisao |
| Runtime | executada por 10_RUNTIME, logada em runs, avaliada em 13_EVALS | nao especifica runtime; so shape operacional |

### 2.2 Skills UPGRADE/04 vs Doc 06

| UPGRADE/04 skill | Definicao declarada | Mapeia para Doc 06? | Leitura PMO |
|---|---|---|---|
| `adaptive_questioning` | perguntas por lacunas, risco e contexto | sim, via `briefing-intelligence` (perguntas adaptativas) | Ja coberto; pode virar alias/subskill se Doc 06 detalhar briefing. |
| `apify_scraping_planning` | planejar coleta com atores Apify | parcial, via `research-pack-generation` + Doc 26 | Candidato, mas com AQ skill vs tool/connector. |
| `context_engineering` | dados brutos -> contexto operacional | parcial; Doc 06 usa contexto como input, nao como skill explicita | Candidato forte, ligado a F1 Context State e implementation-brief. |
| `deep_research_synthesis` | sintetizar pesquisas com evidencia e acao | parcial, via `research-pack-generation` | Candidato como especializacao de Research, nao MVP separado ainda. |
| `intent_classification` | classificar intencao e tipo de execucao | parcial; intencao e input do Doc 06, nao skill registrada | Candidato forte, ligado a intent resolver/F1. |
| `learning_extraction` | extrair aprendizado de resultados e feedback | parcial; Doc 06 diz que execucoes alimentam memoria | Candidato medio para memoria/evals/self-evolution. |
| `metacognitive_review` | criticar clareza, coerencia, risco e evidencia | sim, via Metacognitive: hypothesis-audit, confidence-scoring, gap-detection, decision-quality-review, agent-output-evaluation | Ja coberto; nome pode virar alias. |
| `proposal_generation` | criar proposta estrategica e comercial | sim, MVP `proposal-generation` | Ja coberto quase 1:1. |
| `quality_assurance` | validar output contra criterios e policies | sim, MVP `qa-gate` + criterios de QA | Ja coberto; nao duplicar. |
| `reels_storytelling` | roteiro, gancho, takes e CTA para Reels | parcial, via Creative: video-shot-planning, brand-storytelling, copywriting-system | Candidato baixo, especializacao de dominio. |
| `roi_modeling` | modelar impacto economico e operacional | parcial; aparece em metricas/ROI arquitetural, nao como skill explicita | Candidato medio, ligado a ROI proxy. |
| `task_decomposition` | quebrar execucao em tarefas e subtarefas | sim, `task-breakdown` em Operations | Ja coberto; normalizar naming. |
| `visual_briefing` | direcao visual e briefing de producao | parcial, via visual-direction e reference-moodboard-research | Candidato baixo/medio como especializacao Creative/Product. |
| `workflow_design` | criar workflows e sprints | sim, `workflow-orchestration` + workflow blueprints | Ja coberto; normalizar naming. |

---

## 3. A PROMOVER

> Promocao aqui = entra no patch candidate para o Doc 06. Aplicacao exige sessao `canonical_patch` separada. Nenhuma skill abaixo fica ativa por este arquivo.

### 3.1 Estrutural (o valor real)

| ID | Item a promover | Por que e melhor que o canonico | Secao-alvo no Doc 06 | Forca |
|---|---|---|---|---|
| **PROMOTE-S1** | **Skill Execution I/O Contract** - envelope minimo: `input{context_state, goal, constraints, evidence}` -> `output{skill, result, confidence, risks, next_actions}` | O Doc 06 tem template com `required_inputs` e `outputs`, mas nao define shape comum. Este envelope operacionaliza confidence/risks/next_actions e liga direto ao S3 registry + policy checker do F1 sem criar schema fisico. | novo subitem em **5.3 Template de skill**: "Contrato minimo de execucao" | **ALTA** |
| **PROMOTE-S2** | **Criterio operacional de downstream** - toda skill deve produzir resultado que alimente agente, tarefa, proposta, workflow ou decisao | O Doc 06 exige output verificavel, mas o UPGRADE explicita a prova de utilidade operacional. Isso fortalece criterios de aprovacao/reprovacao sem inflar o catalogo. | **14. Criterios de aprovacao** e **15. Criterios de reprovacao** | **MEDIA** |

### 3.2 Catalogo - candidatos granulares (nao specs completas)

| ID | Candidato | Leitura proposta | Secao-alvo no Doc 06 | Forca |
|---|---|---|---|---|
| **PROMOTE-S3a** | `intent-classification` | Skill candidata para classificar intencao e tipo de execucao antes de workflow/agent run. Utilidade F1 direta. | Taxonomia Strategy/Operations + possivel MVP futuro | **ALTA** |
| **PROMOTE-S3b** | `context-engineering` | Skill candidata para transformar fontes/respostas em contexto operacional. Deve alinhar com Doc 05/10/28 e nao virar RAG interno. | Operations/Metacognitive ou Development, pendente AQ | **ALTA** |
| **PROMOTE-S3c** | `roi-modeling` | Skill candidata para modelar impacto economico/operacional; liga ao ROI proxy e ao Business System. | Strategy/Operations; cross-ref ROI architecture | **MEDIA** |
| **PROMOTE-S3d** | `learning-extraction` | Skill candidata para extrair aprendizado de resultados e feedback, alimentando memoria/evals sem criar automacao runtime. | Metacognitive/Operations | **MEDIA** |
| **PROMOTE-S3e** | `deep-research-synthesis` | Especializacao de `research-pack-generation`: sintese com evidencia e acao. | Research, como subskill/alias governado | **MEDIA** |
| **PROMOTE-S3f** | `apify-scraping-planning` | Skill candidata de planejamento, nao execucao de connector; deve apontar para allowed_tools/Doc 26. | Research + `allowed_tools`, pendente AQ | **BAIXA-MEDIA** |
| **PROMOTE-S3g** | `visual-briefing` | Especializacao Creative/Product: direcao visual + briefing de producao. | Creative/Product/UX, como candidato F2 | **BAIXA** |
| **PROMOTE-S3h** | `reels-storytelling` | Especializacao Creative de roteiro curto; util para catalogo de dominio, nao core MVP. | Creative, como candidato F2 | **BAIXA** |

**Total a promover:** 2 estruturais + 8 candidatos de catalogo. **Nao promover:** os markdowns como specs completas; faltam owner, tools, autonomia, riscos, edge cases, prompts base e eval_ref.

---

## 4. JA COBERTO (arquivar, sem acao no canonico)

- `proposal_generation` -> ja existe como MVP `proposal-generation`.
- `quality_assurance` -> ja existe como MVP `qa-gate` e criterios de QA.
- `adaptive_questioning` -> ja aparece em `briefing-intelligence` como perguntas adaptativas; tambem conversa com smart questions, mas nao precisa duplicar skill core.
- `task_decomposition` -> ja coberto por `task-breakdown`.
- `workflow_design` -> ja coberto por `workflow-orchestration` e `07_WORKFLOW_BLUEPRINTS`.
- `metacognitive_review` -> ja coberto pela familia Metacognitive (`hypothesis-audit`, `confidence-scoring`, `gap-detection`, `decision-quality-review`, `agent-output-evaluation`).
- Todo o boilerplate repetido de "Quando usar", Input, Output e criterio de sucesso generico -> promover apenas como padrao estrutural, nao como texto por skill.

---

## 5. CONFLITOS -> ARCHITECTURE_QUESTIONS (nao decidir aqui)

| ID | Conflito | Pergunta para Founder + Metacognik |
|---|---|---|
| **AQ-S06-1** | **Contrato de I/O de skill.** Doc 06 tem template abstrato; UPGRADE/04 tem JSON minimo. | O Doc 06 deve canonizar um `Skill Execution I/O Contract` comum, ou isso pertence ao Doc 10/11 como runtime/schema futuro? |
| **AQ-S06-2** | **Granularidade do catalogo.** UPGRADE/04 cria micro-skills; Doc 06 prefere familias e skills amplas. | Promover micro-skills como entradas independentes, aliases/subskills sob skills maiores, ou manter so na camada F2 futura? |
| **AQ-S06-3** | **Skill vs tool/connector.** `apify_scraping_planning` cruza skill de pesquisa, planejamento de coleta e Doc 26 connector/tool. | Apify deve aparecer no Doc 06 como skill planejadora com `allowed_tools`, ou ficar somente em Doc 26/Research Protocol? |
| **AQ-S06-4** | **Naming convention.** UPGRADE usa `snake_case`; Doc 06 usa `kebab-case`. | Qual convencao canonica para `skill_id`: manter kebab-case do Doc 06, aceitar aliases snake_case, ou registrar ambos com regra de normalizacao? |
| **AQ-S06-5** | **F1 vs F2.** `intent-classification` e `context-engineering` parecem uteis ao F1; especializacoes criativas parecem F2. | Quais skills entram no F1 minimo e quais ficam como catalogo expandido pos-GATE/fan-in? |

---

## 6. Risco P1 + nota de aplicacao

- **P1:** o Doc 06 e registro mestre de execucao. Alterar template, taxonomia ou MVP irradia para Docs 03/04/07/08/10/11/13 e policy checker. Este texto nao aplica nada.
- **Aplicacao:** sessao `canonical_patch` separada, com Founder + Metacognik, escopo explicitamente limitado ao Doc 06 e eventuais registros permitidos pelo checkout.
- **Guarda anti-bloat:** nao despejar 14 nomes no MVP. A maioria e alias, subskill ou especializacao F2. Promover todos sem owner/tools/eval violaria os criterios do proprio Doc 06.
- **Dependencia F1:** PROMOTE-S1, PROMOTE-S3a e PROMOTE-S3b sao os unicos com utilidade imediata mais forte para F1. Mesmo assim, devem permanecer como contrato/documentacao ate existir aprovacao runtime separada.
- **UPGRADE/04:** nao mover, renomear, arquivar ou deletar nesta sessao. Qualquer arquivamento so depois de aprovacao do candidate + canonical_patch separado.
