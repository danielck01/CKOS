---
title: checkout-release
file: checkout-release.md
phase: 02_EXECUTION_SYSTEM
category: skill_note
status: active_draft
skill_id: checkout-release
skill_family: operations
owner_agent: PMO_CKOS
review_agent: Metacognik
runtime_authority: false
implementation_authorized: false
source_skill: C:/Users/GustavoBxx/.codex/skills/checkout-release/SKILL.md
---

# checkout-release

Fecha uma tarefa, Work Order, audit ou patch CKOS com registro auditavel. Release registra o que aconteceu; nao e approval.

# Quando Usar

- No fim de patch, auditoria, Work Order, lote ou sessao documental.
- Quando e preciso registrar arquivos criados/alterados, escopo intocado, validacao e riscos.
- Quando o proximo passo precisa ficar explicito.

# Quando Nao Usar

- Para fabricar session, lock ou release IDs.
- Para implicar runtime, schema ou canonical approval sem autorizacao.
- Para esconder validacao falha ou nao executada.

# Entradas

- task_or_work_order_ref
- session_ref
- lock_ref
- release_ref
- files_created
- files_changed
- files_read_only
- validation_evidence
- risks_remaining
- next_step
- memory_update_recommendation

# Workflow

1. Identificar task, scope e status.
2. Listar criados, alterados e explicitamente intocados.
3. Resumir resultado em termos concretos.
4. Registrar validacao real.
5. Registrar riscos, perguntas abertas e audit needs.
6. Definir memory update recommendation.
7. Encerrar com um proximo passo.

# Saida Verificavel

Um `CHECKOUT RELEASE` contendo:

- identity;
- files created;
- files changed;
- explicitly not touched;
- summary;
- validation;
- risks remaining;
- memory update;
- next step.

# Guardrails

- Se novo ID for exigido no vault, procurar `SESSION_REGISTRY.md` antes.
- Claims de release precisam bater com evidencia.
- Forbidden scope deve aparecer quando relevante.
- Approval e release continuam separados.
