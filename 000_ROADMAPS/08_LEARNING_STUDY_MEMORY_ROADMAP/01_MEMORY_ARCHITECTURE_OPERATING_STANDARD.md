---
title: Memory Architecture Operating Standard
file: 01_MEMORY_ARCHITECTURE_OPERATING_STANDARD.md
phase: 000_ROADMAPS
category: memory_roadmap
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
tags: [memory, learning, rag]
---

# Memory Architecture Operating Standard

## Memória curta

Contexto imediato da tarefa, chat, intenção, plano atual, checkout lock e arquivos em edição.

## Memória média

Projeto ativo, roadmaps, decisões recentes, study notes, feedbacks, runs, handoffs e tarefas abertas.

## Memória longa

Docs canônicos, decisões aprovadas, arquitetura, vault validado, embeddings, histórico auditado e source manifests.

## Padrão por pasta

Obrigatório:
- `README.md`
- `ck_memory.md`

Condicional:
- `ck_learning.md` quando a pasta acumula aprendizado.
- `ck_tasks.md` quando a pasta tem execução contínua.
- `ck_prompts.md` quando a pasta contém prompts reutilizáveis.
- `ck_feedback.md` quando a pasta recebe revisão contínua.
- `ck_roi.md` quando há custo, valor, performance ou decisão de investimento.
- `ck_risks.md` quando há risco operacional, técnico, legal, financeiro ou reputacional.

## Regra RAG

Notas padrão devem ser escritas para vetorização: títulos claros, YAML consistente, seções curtas, decisões explícitas, links relacionados e separação entre hipótese, decisão e evidência.
