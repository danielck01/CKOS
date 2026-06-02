---
title: Project Test Scenario Template
system_id: project_test_scenario_template
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

# Project Test Scenario Template

## Proposito

Fornecer um template para testar projetos no Codex usando o Creator Mode e a Simulation Runtime Layer.

Use este template antes de criar qualquer pack de notas.

## Metadados

```yaml
scenario_id:
simulation_only: true
project_name:
raw_founder_intent:
project_type:
category:
subcategory:
risk_level:
source_mode:
  attached_sources:
  deep_research_requested:
  exploratory_no_sources:
estimated_credits:
pmo_required:
founder_approval_required:
status:
```

## CHECKOUT LOCK

```txt
# CHECKOUT LOCK

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

## Etapa 1 - Interpretacao

```txt
SIMULATED CALL:
POST /intent/interpret

Output:
- Intent detected
- Intent refined
- Project type
- Category
- Subcategory
- Risk level
- Suggested output
```

## Etapa 2 - Context Pack

```txt
SIMULATED CALL:
POST /context-pack/build

Output:
- docs to read
- uploads to inspect
- canonical references
- missing context
- source mode
- evidence map requirement
```

## Etapa 3 - Policy evaluation

```txt
SIMULATED CALL:
POST /policy/evaluate

Output:
- policies applied
- allowed actions
- blocked actions
- required approvals
- risk notes
```

## Etapa 4 - Credits estimate

```txt
SIMULATED CALL:
POST /credits/estimate

Output:
- local reading cost
- planning cost
- PMO cost
- external research cost
- artifact generation cost
- total range
- cheaper alternatives
```

## Etapa 5 - PMO handoff

```txt
SIMULATED CALL:
POST /pmo/audit-request

Output:
- PMO_AUDIT_REPORT
- verdict
- required patches
- approved next action
```

## Etapa 6 - Founder approval

```txt
SIMULATED CALL:
POST /approvals/founder/request

Decision options:
- approve planning artifact
- request patches
- block execution
- approve filetree only
- approve pack creation after filetree
```

## Etapa 7 - Artifact generation

```txt
SIMULATED CALL:
POST /artifacts/generate

Allowed only after approval.

Possible outputs:
- PROJECT_INTENT_ANALYSIS.md
- PROJECT_FILETREE_PROPOSAL.md
- PROJECT_EXECUTION_PLAN.md
- PMO_REVIEW_REQUEST.md
- FOUNDER_APPROVAL_CHECKLIST.md
```

## Etapa 8 - Delivery audit

```txt
SIMULATED CALL:
POST /pmo/audit-result

Output:
- delivery status
- gaps
- risks
- next action
```

## Event log esperado

```txt
IntentSubmitted
IntentResolved
ContextPackBuilt
PolicyEvaluated
CreditsEstimated
PMOAuditRequested
PMOAuditCompleted
FounderApprovalRequested
FounderDecisionRecorded
CheckoutLocked
ArtifactGenerated
CheckoutReleased
DeliveryAudited
ProjectNextActionRecommended
```

## CHECKOUT RELEASE

```txt
# CHECKOUT RELEASE

task_id:
agent:
files_changed:
summary:
risks:
next_step:
status: released
```

## Cenografias de teste

### Scenario A - Fontes anexadas

Usar quando Founder anexou documentos.

Output inicial recomendado:

- `PROJECT_INTENT_ANALYSIS.md`
- `SOURCE_INDEX.md`
- `EVIDENCE_MAP.md`

### Scenario B - Sem fontes

Usar quando Founder trouxe apenas intencao.

Output inicial recomendado:

- `PROJECT_INTENT_ANALYSIS.md`
- `GAPS_AND_QUESTIONS.md`
- `RESEARCH_PLAN.md`

### Scenario C - Deep research autorizado

Usar quando contexto externo e necessario.

Output inicial recomendado:

- `DEEP_RESEARCH_SCOPE.md`
- `CREDIT_ESTIMATE.md`
- `PMO_REVIEW_REQUEST.md`

### Scenario D - Dominio regulado

Usar para direito, saude, financas, criancas, dados sensiveis ou reputacao publica.

Output inicial recomendado:

- `RISK_AND_COMPLIANCE_MATRIX.md`
- `SOURCE_REQUIREMENTS.md`
- `HUMAN_REVIEW_REQUIRED.md`

