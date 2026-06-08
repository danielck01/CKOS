---
title: ckos-data-model-migration
file: ckos-data-model-migration.md
phase: 02_EXECUTION_SYSTEM
category: skill_note
status: p0_draft
skill_id: ckos-data-model-migration
skill_family: development_hardening
owner_agent: Builder Lead
review_agent: QA Lead
runtime_authority: false
implementation_authorized: false
source_refs:
  - ../../000_ROADMAPS/22_CONSOLIDATION/05_P0_DEV_HARDENING_SKILL_PACK_ARCHITECTURE.md
  - ../../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
---

# ckos-data-model-migration

Blinda modelagem de dados, schema, migration, seed e persistencia contra improviso, drift canonico e falhas multi-tenant.

# Quando Usar

- Antes de criar ou alterar tabela, coluna, indice, enum, view, projection, migration ou seed.
- Quando um executor sugerir schema derivado de prompt, estudo ou conveniencia.
- Quando o trabalho toca events, workflow_runs, agent_runs, context_packs, audit_logs, cost_ledger, approvals, documents, memories, embeddings ou billing.

# Quando Nao Usar

- Para decidir produto ou UX.
- Para inventar schema fisico de Work Orders sem decisao canonica.
- Para criar migrations reais em fase documental.

# Entradas Minimas

- mudanca pretendida;
- Doc 11 ou patch/AQ que autoriza a superficie;
- tenant/org/workspace/project scope;
- RLS requirement;
- migration direction;
- rollback/compensation;
- impacto em dados existentes.

# Workflow

1. Mapear a mudanca ao Doc 11.
2. Identificar tenant scope.
3. Verificar se a superficie e append-only.
4. Definir constraints, indices e idempotency.
5. Verificar RLS/FORCE RLS.
6. Definir migration validation e rollback/fallback.
7. Gerar AQ quando a autoridade nao existir.

# Saida Verificavel

Proposta ou checklist de dados com:

- mapping para Doc 11;
- tabelas/colunas/indices afetados;
- `org_id`, `workspace_id`, `project_id` quando aplicavel;
- RLS/FORCE RLS;
- append-only ou compensating model;
- idempotency e uniqueness constraints;
- migration validation;
- AQs.

# Guardrails

- Ausencia de tenant scope em tabela de dominio e falha P0.
- `events`, `audit_logs`, billing events e cost ledger sao append-only.
- Vector namespace e pre-condicao, nao pos-filtro.
- Secret real nunca entra em tabela; apenas `secret_ref`.

# Proxima Skill

- [[ckos-policy-rls-security]] para RLS/security.
- [[ckos-event-runtime-contract]] para eventos/projections.
- [[ckos-qa-gate]] para validar entrega.
