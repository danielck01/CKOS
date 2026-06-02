---
title: Learning, Study & Memory Roadmap — ck_agent_handoffs
file: ck_agent_handoffs.md
phase: 000_ROADMAPS
category: agent_handoff
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
tags: [handoff, agents, 08_learning_study_memory_roadmap]
---

# ck_agent_handoffs — Learning, Study & Memory Roadmap

## Handoff atual

Nenhum handoff ativo.

## Modelo de handoff

```txt
# CHECKOUT LOCK
folder: 000_ROADMAPS/08_LEARNING_STUDY_MEMORY_ROADMAP
agent: <Codex | Claude | Antigravity | ChatGPT | CEO_AGENT | PMO_CKOS>
task: <descrição>
allowed_files:
  - <arquivo>
forbidden_files:
  - docs canonicos sem microgate
risk_level: <low | medium | high | critical>
estimated_credits: <CKC estimado>
```

```txt
# CHECKOUT RELEASE
folder: 000_ROADMAPS/08_LEARNING_STUDY_MEMORY_ROADMAP
agent: <agente>
files_changed:
  - <arquivo>
summary: <o que mudou>
open_risks:
  - <risco>
next_step: <próxima ação>
status: released
```

## Regra

Quando trocar de modelo, chat ou ferramenta, registrar handoff. Antigravity não deve editar docs canônicos sem patch plan. Claude/Codex não devem assumir que UI study é implementação.
