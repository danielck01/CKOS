---
title: ckos-event-runtime-contract
file: ckos-event-runtime-contract.md
phase: 02_EXECUTION_SYSTEM
category: skill_note
status: p0_draft
skill_id: ckos-event-runtime-contract
skill_family: development_hardening
owner_agent: Builder Lead
review_agent: Metacognik
runtime_authority: false
implementation_authorized: false
source_refs:
  - ../../000_ROADMAPS/22_CONSOLIDATION/05_P0_DEV_HARDENING_SKILL_PACK_ARCHITECTURE.md
  - ../../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
---

# ckos-event-runtime-contract

Garante que runtime, workflows, agents, projections e rollback sigam contrato event-sourced/CQRS do CKOS.

# Quando Usar

- Ao criar fluxo, worker, run, state machine, projection, event handler, replay, rollback, approval pause ou artifact pipeline.
- Ao revisar qualquer implementacao que muda estado operacional.

# Quando Nao Usar

- Para logs observacionais que nao sao fonte causal.
- Para substituir Data Model ou Security.
- Para justificar event sourcing quando o trabalho e apenas documental.

# Entradas Minimas

- estado que muda;
- evento que causa a mudanca;
- actor;
- correlation_id;
- causation_id;
- idempotency_key;
- state machine afetada;
- projection/read model afetado;
- rollback/compensation esperado.

# Workflow

1. Identificar source-of-truth.
2. Definir eventos emitidos/consumidos.
3. Definir payload minimo.
4. Validar causation/correlation.
5. Validar idempotency.
6. Validar state transitions.
7. Definir projection update.
8. Definir retry/timeout/DLQ.
9. Definir compensating events e replay evidence.

# Saida Verificavel

Runtime event contract com:

- eventos emitidos/consumidos;
- payload minimo;
- causation/correlation;
- idempotency;
- valid state transitions;
- projection update;
- retry/timeout/DLQ;
- compensating events;
- replay evidence.

# Guardrails

- UPDATE/DELETE nao substitui evento causal.
- Rollback e compensacao, nao apagamento de historico.
- Workflow engine e stateless; estado vive em event log + projection.
- UI/projection nao escreve source-of-truth.
- Approval pendente pausa run.

# Proxima Skill

- [[ckos-data-model-migration]] se eventos exigirem schema.
- [[ckos-policy-rls-security]] se eventos envolvem auth/audit.
- [[ckos-qa-gate]] para validar replay e scope.
