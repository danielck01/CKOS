---
title: Thinking System — README
file: 00_README_THINKING_SYSTEM.md
phase: 01_THINKING_SYSTEM
category: constitution
version: 1.1.0
status: active
owner: PMO_CKOS
responsible_agent: PMO_CKOS
reviewers:
  - Metacognik
approval_required:
  - none
purpose: README auxiliar de navegação da fase 01.
inputs: Docs canônicos 01-05.
outputs: Guia de leitura do Thinking System.
framework: Documento auxiliar.
edge_cases: Não aplicável.
integrations: Não aplicável.
prompts: Não aplicável.
metrics: Não aplicável.
related_notes:
  - 01_CKOS_AI_FIRST_CONSTITUTION.md
tags: [thinking, readme, auxiliary]
---

# 01_THINKING_SYSTEM

A camada conceitual do CKOS: o que o sistema é, quais objetos manipula, como agentes operam, como a autonomia é governada e como a memória funciona. É a fonte de verdade conceitual — **materializada** depois em `03_RUNTIME_SYSTEM`.

> Documento **auxiliar**, não canônico numerado.

## Conteúdo canônico

1. `01_CKOS_AI_FIRST_CONSTITUTION.md` — princípios não negociáveis e definição de AI First real.
2. `02_AI_FIRST_OBJECT_MODEL.md` — objetos, relações, estados e lifecycle de node (conceitual).
3. `03_AGENT_OPERATING_MODEL.md` — superagents/agents/subagents, handoffs, runs, hierarquia.
4. `04_AUTONOMY_AND_APPROVALS.md` — 7 níveis de autonomia, approval gates, matriz de risco.
5. `05_MEMORY_AND_CONTEXT_ARCHITECTURE.md` — camadas de memória, RAG, trust hierarchy, context packet.

## Naming (freeze v2 aplicado)

`Metacognik` (grafia única), `PMO_CKOS`, `QA Lead`, `Builder Lead`, `Builder Subagents`. Agents de domínio são catálogo de hipóteses até terem skill contratada.

## Pré-requisito desta fase para as próximas

Os objetos (02), agentes (03), autonomia (04) e memória (05) são **insumos diretos** do `10_SYSTEM_RUNTIME_ARCHITECTURE.md`. Nada de Product/Implementation sem Runtime.

## Próxima leitura

`02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md`
