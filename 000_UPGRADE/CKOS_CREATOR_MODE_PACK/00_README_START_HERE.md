---
title: CKOS Creator Mode Pack
system_id: ckos_creator_mode_pack
category: upgrade_pack
status: active
version: 1.1.0
updated_at: 2026-05-26
owner: ceo_agent
reviewers:
  - founder
  - pmo_ckos
  - metacognik
created_for: CKOS_DOCUMENTATION_REVIEWED
---

# CKOS Creator Mode Pack

## Proposito

Este pack define como simular, no Codex, o modo de criacao de projetos do CKOS a partir de uma intencao minima do Founder.

Ele transforma o Codex em ambiente de execucao documental:

```txt
Founder escreve intencao
CEO interpreta
CEO monta Context Pack
PMO audita
Founder aprova
CEO gera artefatos
PMO valida
Founder decide
```

## Status

Auxiliar. Este pack nao e canonico e nao cria docs 25-30.

## Ordem de leitura

1. `01_PROTOCOLS/CEO_AGENT_PLANNER_PROTOCOL.md`
2. `01_PROTOCOLS/PROJECT_CREATION_FROM_INTENT_PROTOCOL.md`
3. `01_PROTOCOLS/SIMULATED_CREDITS_POLICY_FOR_PLANNING.md`
4. `01_PROTOCOLS/CHECKOUT_LOCK_PROTOCOL.md`
5. `02_TEMPLATES/PROJECT_INTENT_ANALYSIS_TEMPLATE.md`
6. `02_TEMPLATES/PROJECT_FILETREE_PROPOSAL_TEMPLATE.md`
7. `02_TEMPLATES/PROJECT_EXECUTION_PLAN_TEMPLATE.md`
8. `02_TEMPLATES/PMO_AUDIT_HANDOFF_TEMPLATE.md`
9. `02_TEMPLATES/FOUNDER_APPROVAL_CHECKLIST_TEMPLATE.md`
10. `04_CATEGORIES/PROJECT_CATEGORY_TAXONOMY.md`
11. `07_SIMULATION_RUNTIME/00_SIMULATION_RUNTIME_INDEX.md`

## Regra central

O CEO Agent nao comeca executando documento. Ele comeca transformando intencao minima em plano auditavel com custo estimado, dependencias, riscos, opcoes de saida e aprovacao Founder.

## Saidas permitidas

- Documento de analise.
- Plano de execucao.
- Proposta de filetree.
- Checklist de aprovacao.
- Handoff para PMO.
- Pack de notas, somente depois de filetree aprovada.
- Relatorio auditavel.
- Prompt pack.
- Research plan.
- Simulation runtime plan.

## Acoes proibidas

- Nao implementar UI.
- Nao criar backend.
- Nao criar migrations.
- Nao criar APIs.
- Nao criar agentes reais.
- Nao criar automacoes runtime.
- Nao recriar docs 21-24.
- Nao criar docs 25-30.
- Nao renumerar documentos.
- Nao promover n8n ou Manus a core CKOS.
- Nao gerar estrategia final de branding sem briefing, pesquisa e aprovacao.

## Simulation Runtime Layer

A pasta `07_SIMULATION_RUNTIME/` permite testar projetos como se houvesse backend, API, conectores, policy engine, credit engine, PMO audit e event log.

Essa camada e apenas documental:

- endpoints sao simulados;
- servicos sao contratos narrativos;
- schemas sao mocks;
- conectores nao executam chamadas reais;
- creditos sao estimativas CKOS demonstrativas;
- n8n continua sendo acelerador/prototipo, nao core;
- Manus continua sendo bootstrap/manual, nao infraestrutura definitiva.

## Checkout lock obrigatorio

Todo projeto, pack ou pasta nova deve iniciar com `CHECKOUT LOCK` antes de qualquer escrita documental e terminar com `CHECKOUT RELEASE`.

## Projeto Miriam

O exemplo em `05_EXAMPLES/EXAMPLE_MIRIAM_PLANNING_ONLY.md` deve ser usado apenas como case de planejamento. Ele nao autoriza estrategia final, campanha, tom de voz ou plano de conteudo.
