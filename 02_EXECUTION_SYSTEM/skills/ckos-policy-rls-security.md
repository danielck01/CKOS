---
title: ckos-policy-rls-security
file: ckos-policy-rls-security.md
phase: 02_EXECUTION_SYSTEM
category: skill_note
status: p0_draft
skill_id: ckos-policy-rls-security
skill_family: development_hardening
owner_agent: Metacognik
review_agent: QA Lead
runtime_authority: false
implementation_authorized: false
source_refs:
  - ../../000_ROADMAPS/22_CONSOLIDATION/05_P0_DEV_HARDENING_SKILL_PACK_ARCHITECTURE.md
  - ../../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
---

# ckos-policy-rls-security

Aplica o modelo de seguranca CKOS: deny-by-default, RBAC+ABAC, RLS, policyRegistry, approval policies, secrets, tenant isolation, vector/storage isolation e audit trail.

# Quando Usar

- Trabalho toca auth, permissions, roles, RLS, policy, approval, tool/model routing, secrets, PII, vector namespace, storage, billing, support ou dados de cliente.
- Antes de expor dados a agente, modelo, tool externa, projection ou frontend.

# Quando Nao Usar

- Para reduzir seguranca por conveniencia de MVP.
- Para permitir bypass sem registro e approval.
- Para fazer policy hardcoded em controller como fonte de verdade.

# Entradas Minimas

- ator, acao, recurso e contexto;
- classificacao do dado;
- tenant/project scope;
- policies aplicaveis;
- approval requirement;
- secret/model/tool exposure.

# Workflow

1. Avaliar `pode(ator, acao, recurso, contexto)`.
2. Aplicar deny-by-default.
3. Checar RBAC e ABAC.
4. Checar tenant/RLS/vector/storage isolation.
5. Checar PII, secrets e model privacy.
6. Definir approval ou denial.
7. Registrar audit events obrigatorios.

# Saida Verificavel

Security contract com:

- decisao `allow | deny | needs_approval`;
- RBAC+ABAC rationale;
- RLS e tenant isolation checks;
- allowed tools/model constraints;
- secret handling via vault/secret_ref;
- audit events obrigatorios;
- incident/fail-closed behavior.

# Guardrails

- Ausencia de policy equivale a deny.
- Policy engine e unico arbitro.
- Agente nao altera policyRegistry.
- PII/confidential nao entra em context pack/model call sem necessidade, mascara e policy.
- Retry on deny nao e permitido.
- Cross-tenant attempt gera audit/incident P0.

# Proxima Skill

- [[ckos-data-model-migration]] se precisar alterar schema/RLS.
- [[ckos-event-runtime-contract]] se precisar emitir audit/security events.
- [[ckos-qa-gate]] para verificar cobertura.
