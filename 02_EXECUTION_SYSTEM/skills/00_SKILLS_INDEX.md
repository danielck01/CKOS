---
title: CKOS Skills Index
file: 00_SKILLS_INDEX.md
phase: 02_EXECUTION_SYSTEM
category: skills_index
status: active_draft
owner: PMO_CKOS
created_at: 2026-06-02
canonical_patch: false
runtime_authority: false
implementation_authorized: false
purpose: Indice operacional das notas de skills CKOS no vault real.
source_refs:
  - ../06_SKILLS_REGISTRY.md
  - ../../000_ROADMAPS/22_CONSOLIDATION/05_P0_DEV_HARDENING_SKILL_PACK_ARCHITECTURE.md
---

# CKOS Skills Index

Esta pasta centraliza notas de skills em `02_EXECUTION_SYSTEM/skills/`.

Decisao de organizacao: skills ficam em uma subpasta propria do Execution System, nao espalhadas pelas pastas de cada sistema. Cada skill pode referenciar docs de Thinking, Runtime, Product, Business ou Evolution, mas a capacidade em si pertence a camada de execucao.

Nomear cada nota com o proprio `skill_id` ajuda agentes e humanos a encontrar a skill por busca textual, wikilink ou roteamento: `[[ckos-qa-gate]]`, `rg "ckos-qa-gate"`, ou lookup por nome exato.

Estas notas sao biblioteca documental. Elas nao criam runtime, nao instalam agente real, nao alteram Doc 06 e nao autorizam backend, banco, API, UI, migrations, MCP, webhook, n8n ou automacao.

# Ordem Recomendada

```txt
project-intake
  -> briefing-builder
  -> note-normalizer/document-ingestion
  -> context-pack-builder
  -> work-order-draft
  -> risk-gap-review
  -> ckos-implementation-brief
  -> guardas P0 quando aplicavel
  -> ckos-qa-gate
  -> checkout-release
```

# Skills Operacionais Base

| Skill | Usar quando |
|---|---|
| [[project-intake]] | Uma intencao precisa virar projeto governado. |
| [[briefing-builder]] | Contexto solto precisa virar briefing. |
| [[note-normalizer]] | Uma nota bruta precisa virar conhecimento governado. |
| [[document-ingestion]] | Documento/upload precisa de plano de ingestao e RAG readiness. |
| [[context-pack-builder]] | Uma execucao precisa de contexto minimo suficiente. |
| [[work-order-draft]] | Trabalho precisa virar envelope governado. |
| [[risk-gap-review]] | Artefato precisa de auditoria de riscos/lacunas. |
| [[checkout-release]] | Uma entrega precisa de fechamento auditavel. |

# Skills P0 De Desenvolvimento

| Skill | Usar quando |
|---|---|
| [[ckos-implementation-brief]] | Work Order/context pack precisa virar briefing tecnico para executor. |
| [[ckos-backend-thin-slice]] | O trabalho toca backend P0/F1/GATE5. |
| [[ckos-data-model-migration]] | O trabalho toca schema, migration, tabela, indice, seed ou projection. |
| [[ckos-policy-rls-security]] | O trabalho toca auth, policy, RLS, secrets, PII, tool/model access ou tenant isolation. |
| [[ckos-event-runtime-contract]] | O trabalho toca evento, run, workflow, state machine, projection ou rollback. |
| [[ckos-qa-gate]] | Uma entrega tecnica precisa ser validada antes de release. |

# Roteamento Rapido

| Sinal no pedido | Skill inicial |
|---|---|
| "Tenho uma ideia/projeto" | [[project-intake]] |
| "Organize esse contexto" | [[briefing-builder]] |
| "Transforme essas notas" | [[note-normalizer]] |
| "Indexar/ingerir documento" | [[document-ingestion]] |
| "Monte contexto para executar" | [[context-pack-builder]] |
| "Crie Work Order" | [[work-order-draft]] |
| "Revise riscos/lacunas" | [[risk-gap-review]] |
| "Prepare para Codex/Claude/Windsurf" | [[ckos-implementation-brief]] |
| "Backend puro" | [[ckos-backend-thin-slice]] |
| "Banco/migration/schema" | [[ckos-data-model-migration]] |
| "RLS/policies/seguranca" | [[ckos-policy-rls-security]] |
| "Eventos/runtime/projections" | [[ckos-event-runtime-contract]] |
| "Validar entrega" | [[ckos-qa-gate]] |
| "Fechar sessao/release" | [[checkout-release]] |

# Regras De Boundary

- Nota de skill nao e canonical patch.
- Nota de skill nao e runtime skill instalada.
- Qualquer promocao ao Doc 06 exige sessao separada e aprovacao.
- Qualquer implementacao exige Work Order, implementation brief e QA gate.
- Qualquer lacuna de schema, policy ou runtime vira `ARCHITECTURE_QUESTION`.
