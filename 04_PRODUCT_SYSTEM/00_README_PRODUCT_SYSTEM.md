---
title: Product System — README
file: 00_README_PRODUCT_SYSTEM.md
phase: 04_PRODUCT_SYSTEM
category: product_architecture
version: 1.1.0
status: draft
owner: PMO_CKOS
responsible_agent: PMO_CKOS
reviewers:
  - Metacognik
approval_required:
  - none
purpose: README auxiliar de navegação da fase 04.
inputs: Docs canônicos 14-16.
outputs: Guia de leitura do Product System.
framework: Documento auxiliar.
edge_cases: Não aplicável.
integrations: Não aplicável.
prompts: Não aplicável.
metrics: Não aplicável.
related_notes:
  - 14_PROJECT_DASHBOARD_ARCHITECTURE.md
tags: [product, readme, auxiliary]
---

# 04_PRODUCT_SYSTEM

As superfícies que o usuário toca: Dashboard (14), Command Center (15) e Node Canvas (16). **Regra central: Product System não é fonte da verdade — é projeção de objetos, eventos, permissões, memória e runtime.**

> Documento **auxiliar**, não canônico numerado.
>
> Esta fase **depende** de `03_RUNTIME_SYSTEM` (10-13) e está bloqueada para implementação até a fase 03 ser aprovada.

## Conteúdo canônico (renumerado de 10-12 → 14-16)

1. `14_PROJECT_DASHBOARD_ARCHITECTURE.md` — cockpit adaptativo; projeção de read models do runtime.
2. `15_COMMAND_CENTER_ARCHITECTURE.md` — ingress do runtime; intenção → ação estruturada.
3. `16_NODE_CANVAS_ARCHITECTURE.md` — projeção editável do grafo de objetos.

## Correções da v2

- Renumeração 10→14, 11→15, 12→16.
- `Metaconik` → `Metacognik` em todo o pacote (inclui node type "Metacognik Audit", origem `metacognik_required`, mention `@metacognik`).
- Owner "Product Architect" → `PMO_CKOS` + skill `product-strategy`.
- Cada doc agora declara dependência explícita de Runtime (10), Data Model (11), Security (12) e Evals (13).
- Reforço: Dashboard não é página fixa; Command Center não é busca; Node Canvas não é só UI; cada interface reflete o estado vivo do runtime.

## Próxima leitura

`05_IMPLEMENTATION_SYSTEM/17_IMPLEMENTATION_PROTOCOL.md`
