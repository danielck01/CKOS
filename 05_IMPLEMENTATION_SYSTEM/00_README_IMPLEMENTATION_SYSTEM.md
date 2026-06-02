---
title: Implementation System — README
file: 00_README_IMPLEMENTATION_SYSTEM.md
phase: 05_IMPLEMENTATION_SYSTEM
category: implementation
version: 1.1.0
status: draft
owner: PMO_CKOS
responsible_agent: PMO_CKOS
reviewers:
  - Metacognik
approval_required:
  - none
purpose: README auxiliar de navegação da fase 05.
inputs: Docs canônicos 17-21.
outputs: Guia de leitura do Implementation System.
framework: Documento auxiliar.
edge_cases: Não aplicável.
integrations: Não aplicável.
prompts: Não aplicável.
metrics: Não aplicável.
related_notes:
  - 17_IMPLEMENTATION_PROTOCOL.md
tags: [implementation, readme, auxiliary]
---

# 05_IMPLEMENTATION_SYSTEM

Como o CKOS é construído e evolui: protocolo de implementação (17), pesquisa via Manus (18), execução por Claude/Codex/Antigravity (19), QA + Founder approval (20) e o sistema auto-evolutivo (21).

> Documento **auxiliar**, não canônico numerado.
>
> Depende de `03_RUNTIME_SYSTEM` + `04_PRODUCT_SYSTEM`. Implementação de produto **bloqueada** até a fase 03 ser aprovada.

## Conteúdo canônico (renumerado de 13-16 → 17-20, + 21 novo)

1. `17_IMPLEMENTATION_PROTOCOL.md` — intake, scope lock, impact P0-P4, cortes, QA, founder approval.
2. `18_RESEARCH_PROTOCOL_FOR_MANUS.md` — Manus como Research Subagent temporário.
3. `19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md` — executores de código (Builder Lead + Builder Subagents).
4. `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md` — gates de qualidade e aprovação.
5. `21_SELF_EVOLVING_SYSTEM.md` — **novo**; escada de autonomia controlada (9 níveis) com guardrails.

## Correções da v2

- Renumeração 13→17, 14→18, 15→19, 16→20.
- Naming: `PMO Agent`→`PMO_CKOS`, `QA Agent`→`QA Lead`, `Builder Agent(s)`→`Builder Lead`/`Builder Subagents`, `Research Ops Agent`→`Research Subagent`, `Metaconik`→`Metacognik`.
- Dependências de Runtime/Security/Evals adicionadas.
- `21_SELF_EVOLVING_SYSTEM` criado como documento controlado (não hype), dependente de runtime+security+evals+sandbox+rollback+approval.

## Próxima leitura

Voltar ao `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md` para o status do programa, ou abrir `ARCHITECTURE_PATCH_REPORT.md` na raiz da árvore revisada.
