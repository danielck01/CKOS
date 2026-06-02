---
title: Master Roadmap 2026
file: 01_MASTER_ROADMAP_2026.md
phase: 000_ROADMAPS
category: master_roadmap
version: 1.0.0
status: draft
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
  - metacognik
purpose: Planejar, governar e sincronizar a evolução documental e operacional do CKOS sem gerar implementação prematura.
inputs:
  - 00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md
  - CKOS_FOLDER_MEMORY.md
  - CKOS_FILETREE_MAP.md
  - ARCHITECTURE_PATCH_REPORT.md
outputs:
  - plano rastreável
  - tarefas auditáveis
  - riscos abertos
  - critérios de aceite
framework: Sentir, Pensar, Criar, Conectar, Avaliar, Elevar
edge_cases: Roadmap treated as canonical source; agent reads excessive context; implementation starts from planning material.
integrations: codex, claude, antigravity, ceo_agent, pmo_auditor and founder review sessions.
prompts: Read README and ck_memory before task-specific planning, patching or handoff.
metrics: YAML valid; 0 canonical docs created; 0 implementation changes; handoff logged when sessions change.
confidence: unverified
provenance_status: unverified
source_tool: chatgpt
related_notes:
  - README.md
tags: [master-roadmap, spccae]
---

# Master Roadmap 2026

## Fase 0 — Estabilizar governança viva

Objetivo: impedir que o vault vire um conjunto de documentos brilhantes, porém desconectados.

Entregas:
- `000_ROADMAPS/` validado.
- `README.md` + `ck_memory.md` em pastas críticas.
- Padrão de `CHECKOUT_LOCK` e `CHECKOUT_RELEASE` aplicado.
- Separação clara entre RAW, STUDY, UPGRADE, CANONICAL e ROADMAP.

Critério de aceite:
- Qualquer agente recebe apenas endereço de pasta e sabe onde ler contexto, memória, tarefas, riscos, ROI e handoff.

## Fase 1 — Fechar docs 26–31 antes de UI/UX

Sequência recomendada:

1. `26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`
2. `27_COLLECTOR_REGISTRY_AND_RESEARCH_ACTORS_ARCHITECTURE.md`
3. `28_KNOWLEDGE_INGESTION_UPLOADS_AND_SOURCE_GOVERNANCE_ARCHITECTURE.md`
4. `29_STUDY_NOTES_AND_LEARNING_MODE_ARCHITECTURE.md`
5. `30_CLIENT_PROJECT_PLANNER_AND_SELF_DOCUMENTING_PROJECTS_ARCHITECTURE.md`
6. `31_SKILLS_TOOLS_CAPABILITY_AND_CKSTORE_ARCHITECTURE.md`

Bloqueio: não iniciar docs canônicos de UI/UX antes de 26–31, exceto estudos em `000_STUDY_NOTES`.

## Fase 2 — UI/UX como gramática operacional

Docs futuros:

7. `32_UIUX_FOUNDATION_AND_OPERATIONAL_INTERFACE_ARCHITECTURE.md`
8. `33_MOTION_INTERACTION_AND_STATE_FEEDBACK_ARCHITECTURE.md`
9. `34_WEB_MOBILE_WHITELABEL_AND_IMPLEMENTATION_READINESS_GATE.md`

Regra: UI não é estética. UI é projeção do runtime, dos estados, das permissões, dos custos, dos riscos e das decisões.

## Fase 3 — Implementação controlada

Somente depois de:
- docs 26–34 aprovados;
- roadmap de implementação validado;
- UI/UX acceptance criteria fechado;
- Security lane aprovada;
- cost guard e approval gates especificados.

## Lanes permanentes

- Governance
- Security
- Cost/Credits
- ROI
- Memory/Context
- UI/UX
- Runtime
- Agents
- QA/Metacognik
