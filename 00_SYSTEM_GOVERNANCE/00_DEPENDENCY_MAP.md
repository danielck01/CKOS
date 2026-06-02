---
title: Dependency Map
file: 00_DEPENDENCY_MAP.md
phase: 00_SYSTEM_GOVERNANCE
category: dependency_map
version: 2.5.0
status: active
owner: PMO_CKOS
responsible_agent: PMO_CKOS
reviewers:
  - metacognik
approval_required:
  - founder
purpose: Mapa de dependências do CKOS com a fase Runtime — impede que produto, prompts, dashboards, agentes e skills sejam criados antes da base correta.
inputs: Master Map v2; taxonomia; template; nova fase Runtime.
outputs: Matriz de dependências; ordem segura; bloqueios; riscos de antecipação.
framework: 4 níveis de dependência — conceito, objeto, operacional, runtime/implementação.
edge_cases: Urgência de demo; cliente quer ver algo; tool entrega fora da hierarquia; executor ignora dependency check.
integrations: Governa a ordem de execução de toda a árvore.
prompts: Prompt de verificação de dependência; prompt de bloqueio de antecipação.
metrics: Menos implementações descartadas; menos docs duplicados; mais decisões registradas.
related_notes:
  - 00_MASTER_MAP.md
  - 00_DOCUMENT_TEMPLATE.md
  - 00_TAXONOMY_AND_NAMING.md
tags: [governance, dependency_map, sequencing, blockers, runtime]
---

# 1. Propósito

Definir o mapa de dependências do CKOS para impedir que implementação, prompts, dashboards, agentes e skills sejam criados antes da base conceitual e de runtime existir. Dependência não é burocracia — é redução de erro.

# 2. Função dentro do CKOS

Responde o que precisa existir antes de cada documento, interface, skill, workflow, approval e implementação. A mudança central da v2: **Product e Implementation agora dependem explicitamente de Runtime.**

# 3. Inputs

- Master Map v2; taxonomia; template; estrutura de 6 fases; visão AI First.

# 4. Outputs

- matriz de dependências; ordem segura; bloqueios; riscos de antecipação; regras de implementação.

# 5. Níveis de dependência

```txt
Level 1 — Concept: a ideia precisa estar definida (Thinking).
Level 2 — Object: o objeto precisa existir no Object Model (02) e ter materialização no Data Model (11).
Level 3 — Operational: workflow, skill, prompt ou approval precisa existir (Execution).
Level 4 — Runtime/Implementation: runtime, dados, segurança e evals existem (03) antes de interface (04) e construção (05).
```

# 6. Cadeia macro de fases

Fluxo de conhecimento antes de qualquer novo documento canonico:

```txt
000_UPLOADS
  -> 000_STUDY_NOTES
    -> patch plan aprovado
      -> CANONICAL docs
```

```txt
00_SYSTEM_GOVERNANCE
  → 01_THINKING_SYSTEM
    → 02_EXECUTION_SYSTEM
      → 03_RUNTIME_SYSTEM
        → 04_PRODUCT_SYSTEM
          → 05_IMPLEMENTATION_SYSTEM
            → 06_BUSINESS_SYSTEMS
              → 07_EVOLUTION_SYSTEM
```

# 7. Dependências por documento

```txt
01_CONSTITUTION         └── 00 completo
02_OBJECT_MODEL         └── 01, 00_TAXONOMY
03_AGENT_OPERATING      └── 01, 02
04_AUTONOMY_APPROVALS   └── 02, 03
05_MEMORY_CONTEXT       └── 02, 03, 04

06_SKILLS_REGISTRY      └── 02, 03, 04
07_WORKFLOW_BLUEPRINTS  └── 06, 04, 05
08_PROMPT_LIBRARY       └── 06, 07
09_TRANSFORMERS         └── 02, 05, 06, 07

10_RUNTIME_ARCH         └── 02, 03, 04, 05, 06, 07, 09   (materializa o que esses descrevem)
11_DATA_MODEL           └── 02, 05
12_SECURITY             └── 02, 04, 11
13_EVALS                └── 03(agentes), 06, 10

14_DASHBOARD            └── 11, 12, 10            (Data Model + Permissions + UI Projection)
15_COMMAND_CENTER       └── 10, 12, 06, 08        (Runtime + Agent Router + Approval Gate)
16_NODE_CANVAS          └── 02, 10, 07            (Object Model + Runtime + Workflow Engine)

17_IMPLEMENTATION       └── 10, 12, 13, 04
18_RESEARCH_PROTOCOL    └── 06, 17 (18_RESEARCH_PROTOCOL_FOR_MANUS.md: superseded/historical)
19_CLAUDE_CODEX         └── 17, 12
20_QA_FOUNDER           └── 04, 13, 17
21_ROI_ARCHITECTURE     └── 11, 13, 17, 20
22_FEEDBACK_SYSTEM      └── 11, 13, 17, 20, 21
23_SUPPORT_SYSTEM       └── 11, 12, 13, 17, 20, 22
24_CREDITS_BILLING      └── 11, 12, 13, 17, 20, 21, 23
25_SELF_EVOLVING        └── 10, 11, 12, 13, 04, 17, 20, 21-24   (Runtime + Data + Security + Evals + Business Signals + Approval + Sandbox)
26_CONNECTORS_MCP       └── 10, 11, 12, 13, 18, 19, 24, 25   (Runtime + Data + Security + Evals + Research + Execution Protocol + Credits + Evolution)
27_WORK_ORDERS_MULTI_SESSION └── 26, 11, 12, 13, 24, MULTI_SESSION_EXECUTION_POLICY, 28   (Work Orders + Multi-Session Orchestration; documentation-only; no runtime/schema)
28_NOTES_RAG_KNOWLEDGE  └── 05, 10, 11, 12, 13, 18, 26, 27   (Notes + RAG + Knowledge; ingestion/retrieval policy; Doc 11 suggestions only)
```

# 8. Dependências críticas (regras duras)

- **Product System depende de Runtime.** Nenhum doc 14–16 é aprovável sem 10 e 11 existirem.
- **Runtime depende de** Object Model (02), Agent Model (03), Autonomy (04), Memory (05), Workflows (07) e Transformers (09).
- **Implementation depende de Runtime + Product.**
- **Self-Evolving (25) depende de** Runtime (10) + Data Model (11) + Security (12) + Evals (13) + Approval (04/20) + Business Systems (21-24).
- **Connectors/MCP (26) depende de** Runtime (10) + Data Model (11) + Security (12) + Evals (13) + Research Protocol (18) + Execution Protocol (19) + Credits/Billing (24) + Self-Evolving (25).
- **Node Canvas depende de** Object Model (02) + Runtime (10) + Workflow Engine (parte de 10).
- **Command Center depende de** Runtime (10) + Agent Router (parte de 10) + Approval Gate (10/04).
- **Dashboard depende de** Data Model (11) + Permissions (12) + UI Projection (10).

## 8.1 Dependências de componentes de runtime (v2.1)

Após a expansão do `10_SYSTEM_RUNTIME_ARCHITECTURE` (registries, engines, state machines):

- **Capability System** depende de 02 (Object Model), 06 (Skills), 07 (Workflows), 10 (Runtime), 11 (Data Model), 12 (Security).
- **Collector System** depende de 10 (Runtime), 11 (Data Model), 12 (Security), 13 (Evals), 09 (Transformers/normalização).
- **Context Pack Builder** depende de 05 (Memory), 09 (Transformers), 10 (Runtime), 11 (Data Model), 12 (Permissions), 13 (budget/eval hooks).
- **Self-Evolving (25)** depende — além de 10/11/12/13/04/17/20/21-24 — de **Run Replay, Sandbox/Simulation, Cost Guard, Eval Hooks, Decision Rights Matrix, rollback, audit logs e business learning signals**.
- **Product System (14-16)** depende de **UI Projection Engine, State Machine Registry e Data Model** (10/11).
- **Command Center (15)** depende de **Context Pack Builder, Intent Router, Agent Router, Policy Engine e Approval Gate** (10).
- **Node Canvas (16)** depende de **Node Type Registry, State Machine Engine, Workflow Engine e Event Store** (10).

## 8.2 Dependencia RAW/STUDY para docs futuros 25-34

Nenhum novo doc canonico 25-34 deve ser criado a partir de material externo sem passar por:

```txt
RAW source
  -> source manifest ou upload note
    -> study note
      -> patch candidate
        -> aprovacao Founder/PMO/Metacognik/Technical quando aplicavel
          -> canonical patch
```

Essa regra vale para material de pesquisa, PDFs, prints, CSVs, benchmarks, outputs de IA, exports de conectores, transcricoes, referencias visuais, `000_UPGRADE/` e qualquer ferramenta externa.

## 8.3 Dependencias futuras antes de UI/UX docs 32-33

Docs de UI/UX e visual system so podem ser iniciados depois da sequencia de governanca de conhecimento e capabilities:

| Futuro doc | Dependencia obrigatoria antes de UI/UX |
|---|---|
| 25 Self-Evolving | `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` criado; antigo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` preservado como superseded; ROI permanece doc 21 |
| 26 Connectors/MCP | `07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md` criado; matriz MCP/API/collector/webhook/n8n/nativo definida; vendors permanecem substituiveis |
| 27 Work Orders/Multi-Session Orchestration | `07_EVOLUTION_SYSTEM/27_AI_FIRST_WORK_ORDERS_AND_MULTI_SESSION_ORCHESTRATION_ARCHITECTURE.md` criado como arquitetura documental; sem backend, UI, schema, runtime, agentes reais ou automacao |
| 28 Notes/RAG/Knowledge Architecture | `07_EVOLUTION_SYSTEM/28_NOTES_RAG_AND_KNOWLEDGE_ARCHITECTURE.md` criado como owner de Notes/RAG, metadata, vector categories, embeddings, chunking, retrieval governance e Doc 11 patch suggestions |
| 29 Study Notes/Learning Mode | notas estudaveis, confidence, patch candidates e learning mode definidos |
| 30 Client Project Planner | projetos autodocumentados, planner, briefing, artefatos e decisoes definidos |
| 31 CK Store/Capability Marketplace | capabilities, add-ons, planos, creditos e marketplace definidos |

Conclusao: UI/UX docs 32-33 continuam bloqueados ate docs 25-31 serem resolvidos e aprovados.

## 8.4 MCP, conectores e integracoes: invariantes de runtime

MCP, conectores e integracoes nao podem bypassar:

- `policy_engine`
- `tool_router`
- `approval_gate`
- `cost_guard`
- `audit_logs`
- tenant isolation
- `secret_refs`

Todo output de integracao vira source/evidence apenas via RAW/STUDY, com source manifest, provenance, confidence e auditabilidade.

# 9. O que não pode ser feito antes da hora

- Não criar dashboards fixos por canal.
- Não criar dezenas de agentes antes do Agent Operating Model + skill contratada.
- Não criar Prompt Library antes do Skills Registry.
- Não criar automação sem Approval Gate.
- Não criar RAG sem Memory Architecture (05) + Data Model (11).
- Não criar Node Canvas sem Object Model + Runtime.
- **Não iniciar produto/backend sem Runtime (10–13) aprovado.**

# 10. Matriz de risco por antecipação

| Ação antecipada | Risco | Consequência |
|---|---:|---|
| Criar UI antes do Runtime/Data Model | Alto | Interface bonita sem lógica nem persistência |
| Criar agents antes da taxonomia/skill | Alto | Teatro de agentes |
| Criar Prompt Library antes das skills | Médio/Alto | Prompt solto sem reuso |
| Criar dashboards fixos | Alto | Plataforma não whitelabel |
| Criar auto-approval sem gate de runtime | Alto | Risco jurídico e operacional |
| Criar RAG sem memory policy + data model | Alto | Recuperação errada ou vazamento entre tenants |
| Criar self-evolving sem sandbox/evals | Crítico | Agente altera o sistema sem controle |

# 11. Edge cases

- Urgência de demo: protótipo `prototype_only`, sem backend real.
- Cliente precisa ver algo: Proposal Experience, não CKOS Core.
- Tool externa entrega fora da hierarquia: converter para docs oficiais.
- Claude/Codex implementa sem dependency check: isolar em lab/branch até aprovação (ver 19).

# 12. Prompts relacionados

```txt
Antes de executar esta tarefa, verifique as dependências obrigatórias (conceito, objeto, operacional, runtime). Classifique o risco de executar agora (baixo/médio/alto). Se faltar dependência, proponha a menor ação para destravar sem criar entropia.
```

```txt
Avalie se esta implementação está sendo pedida antes de Runtime (10), Data Model (11), Security (12) ou Evals (13). Se sim, não implemente; gere recomendação PMO_CKOS de sequência correta.
```

# 13. Métricas de sucesso

- menos implementações descartadas; menos docs duplicados; menos agentes sem função; menos dashboards fixos; mais decisões registradas; clareza entre visão, runtime e execução.

# 14. Critérios de aprovação

Aprovado se a cadeia de fases, as dependências por documento e as regras duras forem consistentes com `00_MASTER_MAP` e impedirem produto antes de runtime.

# 15. Critérios de reprovação

Reprovado se permitir Product/Implementation sem Runtime, ou se omitir a dependência Runtime→(02,03,04,05,07,09).

# 16. Related notes

- [[00_MASTER_MAP]]
- [[00_DOCUMENT_TEMPLATE]]
- [[00_TAXONOMY_AND_NAMING]]
- [[10_SYSTEM_RUNTIME_ARCHITECTURE]]
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]]
