---
title: 03 Prompt Claude Architecture Review
file: 03_PROMPT_CLAUDE_ARCHITECTURE_REVIEW.md
phase: 000_ROADMAPS
category: prompt
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
tags: [prompt, agents, roadmap]
---
# Prompt — Claude Architecture Review

Atue como arquiteto crítico do CKOS. Revise roadmaps, dependências, riscos e sequência canônica. Não implemente. Não reescreva tudo sem necessidade. Aponte conflitos, duplicidades e lacunas.

Leia:
- `000_ROADMAPS/README.md`
- `000_ROADMAPS/01_DOCUMENTATION_ROADMAP/01_DOCS_26_TO_34_CANONICAL_SEQUENCE.md`
- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`
- `CKOS_FILETREE_MAP.md`
- `CKOS_FOLDER_MEMORY.md`
- `ARCHITECTURE_PATCH_REPORT.md`

Entrega:
- diagnóstico;
- riscos;
- decisões pendentes;
- patch candidates;
- recomendação de microgate;
- checklist de aceite.
