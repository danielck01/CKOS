---
title: Agent Civilization Roadmap
file: 01_AGENT_CIVILIZATION_ROADMAP.md
phase: 000_ROADMAPS
category: agent_roadmap
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
tags: [agents, superagents, subagents]
---

# Agent Civilization Roadmap

## Hierarquia operacional

1. Founder humano
2. CEO Agent
3. PMO_CKOS
4. Metacognik
5. Domain Leads
6. Specialist Agents
7. Subagents
8. Tools/Skills/Collectors

## Regra

O CEO Agent interpreta intenção, contrata agentes, propõe plano, estima risco/custo e pede aprovação. Ele não substitui Founder. PMO audita. Metacognik veta inconsistência. Especialistas executam dentro de scope.

## Handoffs obrigatórios

- CEO → PMO: plano precisa auditoria.
- PMO → Founder: risco, custo ou patch canônico.
- CEO → Specialist: tarefa aprovada com scope.
- Specialist → PMO: entrega precisa QA.
- PMO → Memory: atualização de `ck_memory.md`.

## Cuidado

Enquanto agentes reais não existem no runtime, tudo isso é simulação documental. Não escrever como se o backend já executasse agentes autonomamente.
