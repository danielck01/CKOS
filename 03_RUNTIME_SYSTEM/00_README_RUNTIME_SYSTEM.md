---
title: Runtime System — README
file: 00_README_RUNTIME_SYSTEM.md
phase: 03_RUNTIME_SYSTEM
category: runtime
version: 1.0.0
status: draft
owner: PMO_CKOS
responsible_agent: Builder Lead
reviewers:
  - Metacognik
approval_required:
  - none
purpose: README auxiliar de navegação da fase 03 (nova).
inputs: Docs canônicos 10-13.
outputs: Guia de leitura do Runtime System.
framework: Documento auxiliar.
edge_cases: Não aplicável.
integrations: Não aplicável.
prompts: Não aplicável.
metrics: Não aplicável.
related_notes:
  - 10_SYSTEM_RUNTIME_ARCHITECTURE.md
tags: [runtime, readme, auxiliary]
---

# 03_RUNTIME_SYSTEM (nova fase — gate atual do programa)

A camada que estava **ausente** na auditoria. Faz o conceito (01) e a capacidade (02) **acontecerem** de forma rastreável, segura e mensurável. Product (04) e Implementation (05) dependem desta fase.

> Documento **auxiliar**, não canônico numerado.
>
> **Status do programa**: a implementação de produto/backend está **bloqueada** até esta fase ser revisada e aprovada pelo Founder (`00_MASTER_MAP §9`).

## Conteúdo canônico

1. `10_SYSTEM_RUNTIME_ARCHITECTURE.md` — event bus/log, workflow engine, routers, state machine, scheduler, approval gate, projeção em tempo real, rollback. Responde: *como uma intenção vira execução rastreável?*
2. `11_DATA_MODEL_AND_PERSISTENCE.md` — o que vai para Postgres, event log, Redis, vector, storage; multi-tenant; lineage. Responde: *o que vai para cada store?*
3. `12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md` — RBAC/ABAC, RLS, PII, secrets, permissões de agente/tool, whitelabel. Responde: *como impedir acesso/execução indevidos?*
4. `13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md` — evals, scores, tracing, custo, regressão. Responde: *como saber se a IA funciona/erra/gasta/piora?*

## Por que esta fase existe

A auditoria classificou "arquitetura bonita sem runtime" como risco realizado. Esta fase converte princípios em mecanismos: event-sourcing + CQRS (10), persistência multi-tenant (11), deny-by-default (12) e qualidade/custo mensuráveis (13).

## Próxima leitura

`04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md` (que agora depende explicitamente desta fase).
