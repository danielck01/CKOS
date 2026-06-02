---
title: Runtime & Backend Roadmap — ck_risks
file: ck_risks.md
phase: 000_ROADMAPS
category: risk_register
version: 1.0.0
status: active
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
tags: [risks, governance, 02_runtime_backend_roadmap]
---

# ck_risks — Runtime & Backend Roadmap

| ID | Risco | Severidade | Sinal | Mitigação | Status |
|---|---|---:|---|---|---|
| R-02_RUNTIME_BACKEND_ROADMAP-001 | Criar documentação duplicada | Alta | Novo doc sem consultar mapa | Ler CKOS_FILETREE_MAP e ck_memory | aberto |
| R-02_RUNTIME_BACKEND_ROADMAP-002 | Implementar antes da hora | Alta | Pedido visual vira código | Aplicar prompt DO_NOT_IMPLEMENT | aberto |
| R-02_RUNTIME_BACKEND_ROADMAP-003 | Perder governança de versões | Média | YAML inconsistente | Usar template CKOS | aberto |
| R-02_RUNTIME_BACKEND_ROADMAP-004 | Agentes editarem mesmo arquivo | Alta | Dois chats na mesma pasta | CHECKOUT_LOCK + handoff | aberto |
| R-02_RUNTIME_BACKEND_ROADMAP-005 | Confundir estudo com canônico | Alta | Study note vira regra final | RAW → STUDY → CANONICAL | aberto |

## Política de risco

Qualquer risco alto exige PMO audit antes de execução. Qualquer risco crítico exige Founder approval.
