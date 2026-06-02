---
title: MCP Connectors Roadmap
file: 01_MCP_CONNECTORS_ROADMAP.md
phase: 000_ROADMAPS
category: integration_roadmap
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
tags: [mcp, connectors, integrations]
---

# MCP, Connectors and Integrations Roadmap

## Objetivo

Definir como o CKOS conecta ferramentas externas sem criar bypass de segurança, custo, approval e auditoria.

## Categorias

1. MCP servers
2. APIs diretas
3. Webhooks
4. OAuth connectors
5. Apify actors
6. n8n prototypes
7. RAG connectors
8. Storage connectors
9. Calendar/email/connectors pessoais
10. Payment/billing connectors

## Regras

- Nenhum conector acessa dado sem tenant isolation.
- Nenhum secret em arquivo markdown.
- Todo conector deve passar por `tool_router`, `policy_engine`, `approval_gate`, `cost_guard` e `audit_logs`.
- n8n é protótipo/acelerador, não core runtime.
- Manus é bootstrap/manual, não infraestrutura oficial.

## Próximo doc canônico sugerido

`26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`
