---
title: System Governance — README
file: 00_README_SYSTEM_GOVERNANCE.md
phase: 00_SYSTEM_GOVERNANCE
category: governance
version: 2.0.0
status: active
owner: PMO_CKOS
responsible_agent: PMO_CKOS
reviewers:
  - Metacognik
approval_required:
  - none
purpose: README auxiliar de navegação da fase 00.
inputs: Docs canônicos da fase 00.
outputs: Guia de leitura da governança.
framework: Documento auxiliar (não canônico numerado).
edge_cases: Não aplicável.
integrations: Não aplicável.
prompts: Não aplicável.
metrics: Não aplicável.
related_notes:
  - 00_MASTER_MAP.md
tags: [governance, readme, auxiliary]
---

# 00_SYSTEM_GOVERNANCE

Camada de governança documental do CKOS. Existe para impedir entropia: documentos duplicados, nomes conflitantes, agentes sem função, prompts soltos, módulos fixos, dashboards prematuros e implementação sem dependência lógica.

> Documento **auxiliar**. Não é canônico numerado (regra do `00_MASTER_MAP §6`).

## Conteúdo canônico desta fase

1. `00_MASTER_MAP.md` — árvore de 6 fases, docs canônicos/auxiliares, ordem, gates e bloqueio de implementação.
2. `00_DOCUMENT_TEMPLATE.md` — template v2: YAML + enums controlados + estrutura de corpo.
3. `00_TAXONOMY_AND_NAMING.md` — taxonomia + **naming freeze** (Metacognik, PMO_CKOS, QA Lead, Builder Lead/Subagents…).
4. `00_DEPENDENCY_MAP.md` — dependências, com Runtime como pré-requisito de Product/Implementation.

## Regra PMO

Nenhum documento novo nasce fora dessa hierarquia. Antes de criar, classifique: conceito, objeto, runtime, agente, skill, prompt, workflow, interface, memória, integração, capability ou implementação.

## Mudanças da v2 (auditoria 2026-05-24)

- Nova fase `03_RUNTIME_SYSTEM`; Product renumerado para 14–16; Implementation para 17–21 (+21 Self-Evolving).
- Template e enums travados; naming freeze aplicado.
- Implementação de produto **bloqueada** até a fase 03 ser aprovada.

## Próxima leitura

`01_THINKING_SYSTEM/01_CKOS_AI_FIRST_CONSTITUTION.md`
