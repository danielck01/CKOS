---
title: Execution System — README
file: 00_README_EXECUTION_SYSTEM.md
phase: 02_EXECUTION_SYSTEM
category: skills
version: 1.1.0
status: active
owner: PMO_CKOS
responsible_agent: PMO_CKOS
reviewers:
  - Metacognik
approval_required:
  - none
purpose: README auxiliar de navegação da fase 02.
inputs: Docs canônicos 06-09.
outputs: Guia de leitura do Execution System.
framework: Documento auxiliar.
edge_cases: Não aplicável.
integrations: Não aplicável.
prompts: Não aplicável.
metrics: Não aplicável.
related_notes:
  - 06_SKILLS_REGISTRY.md
tags: [execution, readme, auxiliary]
---

# 02_EXECUTION_SYSTEM

Define a **capacidade** do CKOS: o que sabe fazer (skills), como encadeia (workflows), com quais prompts (library) e como traduz bruto em objeto (transformers). É o "verbo" entre o conceito (Thinking) e a execução física (Runtime).

> Documento **auxiliar**, não canônico numerado.

## Conteúdo canônico

1. `06_SKILLS_REGISTRY.md` — capacidades reutilizáveis (skill ≠ prompt).
2. `07_WORKFLOW_BLUEPRINTS.md` — fluxos adaptativos com estados, eventos e approval gates.
3. `08_PROMPT_LIBRARY.md` — prompts conectados a skills/workflows/executores.
4. `09_TRANSFORMERS_AND_PIPELINES.md` — pipeline mestre canônico (fonte única).

## Correções da v2

- Naming freeze aplicado: `PMO_CKOS` (era "PMO Agent"), `QA Lead` (era "QA Agent"), `Research Subagent` (era "Research Agent"), `Metacognik` em todos. "Product Architect" e "Prompt Engineer Agent" viraram skills (`product-strategy`, `prompt-library-curation`).
- Todos os 4 docs reestruturados no template v2 de 16 seções (antes abandonavam o template).
- Pipeline mestre agora tem fonte única em `09`; `07` e `15` apenas referenciam.

## Próxima leitura

`03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md`
