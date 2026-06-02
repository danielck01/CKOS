---
title: Mock Data Schemas
system_id: mock_data_schemas
category: creator_mode_simulation_runtime
status: active
version: 1.0.0
owner: ceo_agent
reviewers:
  - founder
  - pmo_ckos
created_for: CKOS_CREATOR_MODE_PACK
created_at: 2026-05-26
---

# Mock Data Schemas

## Proposito

Definir schemas falsos para simular objetos do CKOS durante testes no Codex.

Estes schemas nao sao tabelas, migrations, DTOs de API real ou modelos de backend. Sao estruturas documentais para raciocinio e auditoria.

## Regras

- Todo objeto deve conter `simulation_only: true`.
- Nenhum objeto deve conter token, segredo ou credencial.
- Nenhum objeto deve ser tratado como persistencia real.
- IDs podem ser simbolicos.

## Intent

```yaml
intent_id:
simulation_only: true
submitted_by:
submitted_at:
raw_text:
language:
project_hint:
attachments_declared:
source_mode:
  attached_sources:
  deep_research_requested:
  exploratory_no_sources:
status:
```

## IntentAnalysis

```yaml
intent_analysis_id:
simulation_only: true
intent_id:
intent_detected:
intent_refined:
project_type:
category:
subcategory:
risk_level:
regulated_domain:
sensitive_data_possible:
recommended_first_action:
suggested_output:
blocked_actions:
needs_pmo_audit:
founder_approval_needed:
```

## Project

```yaml
project_id:
simulation_only: true
name:
slug:
project_type:
category:
subcategory:
owner:
status:
risk_level:
source_mode:
current_gate:
approved_filetree:
approved_by:
created_at:
```

## ContextPack

```yaml
context_pack_id:
simulation_only: true
project_id:
local_docs:
uploaded_sources:
external_sources_requested:
canonical_docs:
memory_files:
policies:
known_conflicts:
missing_context:
evidence_map_required:
confidence_level:
```

## PolicyDecision

```yaml
policy_decision_id:
simulation_only: true
task_id:
action_requested:
policies_evaluated:
decision:
  approved:
  approved_with_patches:
  blocked:
reason:
required_approvals:
blocked_actions:
conditions:
expires_at:
```

## CreditEstimate

```yaml
credit_estimate_id:
simulation_only: true
task_id:
project_id:
phase:
local_reading_cost:
planning_cost:
pmo_cost:
external_research_cost:
artifact_generation_cost:
delivery_audit_cost:
total_estimated_range:
cost_gate:
cheaper_alternatives:
approval_required:
```

## ConnectorRunSimulation

```yaml
connector_run_id:
simulation_only: true
connector:
real_execution: false
requested_by:
input_scope:
data_classification:
expected_output:
cost_estimate:
risk_level:
policies:
approval_required:
status:
blocked_reason:
source_refs:
```

## PMOAudit

```yaml
pmo_audit_id:
simulation_only: true
task_id:
project_id:
verdict:
  approved:
  approved_with_required_patches:
  blocked:
reason:
scope_check:
risk_check:
cost_check:
documentation_check:
filetree_check:
missing_context:
required_patches:
forbidden_actions:
approved_next_action:
founder_decision_required:
```

## Artifact

```yaml
artifact_id:
simulation_only: true
project_id:
artifact_type:
path_proposed:
status:
created_by:
requires_pmo_audit:
requires_founder_approval:
source_refs:
policies_applied:
```

## ArtifactSet

```yaml
artifact_set_id:
simulation_only: true
project_id:
task_id:
artifacts:
files_created:
files_updated:
files_forbidden:
checkout_lock_ref:
checkout_release_ref:
delivery_audit_required:
```

## CheckoutLock

```yaml
checkout_lock_id:
simulation_only: true
task_id:
agent:
role:
folder_scope:
files_allowed:
files_forbidden:
started_at:
expected_output:
approval_required:
risk_level:
status: locked
```

## CheckoutRelease

```yaml
checkout_release_id:
simulation_only: true
task_id:
agent:
files_changed:
summary:
risks:
next_step:
status: released
```

## FounderApproval

```yaml
approval_id:
simulation_only: true
task_id:
project_id:
requested_decision:
options:
decision:
approved_scope:
blocked_scope:
conditions:
approved_by:
approved_at:
status:
```

## EventLogEntry

```yaml
event_id:
simulation_only: true
event_type:
task_id:
project_id:
actor:
occurred_at:
payload_ref:
policies_applied:
credit_estimate_ref:
approval_ref:
append_only: true
```

