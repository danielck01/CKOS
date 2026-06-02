---
title: Checkout Lock Template
file: CHECKOUT_LOCK_TEMPLATE.md
phase: 000_ROADMAPS
category: template
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
tags: [template, checkout-lock]
---

# CHECKOUT LOCK TEMPLATE

```txt
# CHECKOUT LOCK
task_id: <ID>
folder: <path>
agent: <agent>
mode: <study | roadmap | patch_plan | execution | audit>
objective: <objective>
allowed_files:
  - <file>
forbidden_files:
  - <file or pattern>
canonical_docs_touched: no
risk_level: <low | medium | high | critical>
estimated_credits: <CKC>
approval_required:
  - Founder
  - PMO_CKOS
```
