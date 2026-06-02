---
title: Event Log Simulation
system_id: event_log_simulation
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

# Event Log Simulation

## Proposito

Definir uma trilha de eventos simulada para projetos CKOS rodados no Codex.

Este log nao e banco de dados. Ele e um modelo documental append-only para auditoria de decisoes e entregas.

## Regras

- Eventos sao conceituais.
- Eventos nao executam codigo.
- Eventos nao disparam automacoes reais.
- Eventos nao escrevem em banco real.
- Eventos devem ser citados em relatorios e artifacts quando relevantes.

## Sequencia padrao

```txt
IntentSubmitted
IntentResolved
ProjectTypeClassified
RiskClassified
ContextRequiredMapped
ContextPackBuilt
PolicyEvaluated
CreditsEstimated
PMOAuditRequested
PMOAuditCompleted
FounderApprovalRequested
FounderDecisionRecorded
CheckoutLocked
ArtifactGenerationStarted
ArtifactGenerated
CheckoutReleased
DeliveryAuditRequested
DeliveryAudited
ProjectNextActionRecommended
```

## Eventos

| Evento | Emitido por | Quando | Payload minimo |
|---|---|---|---|
| `IntentSubmitted` | Founder | Intencao curta recebida | `intent_id`, `raw_text` |
| `IntentResolved` | CEO Agent | Intencao interpretada | `intent_analysis_id` |
| `ProjectTypeClassified` | CEO Agent | Tipo/categoria definidos | `project_type`, `category`, `subcategory` |
| `RiskClassified` | CEO Agent | Risco estimado | `risk_level`, `risk_reason` |
| `ContextRequiredMapped` | ContextPackService | Contexto necessario listado | `required_docs`, `missing_context` |
| `ContextPackBuilt` | ContextPackService | Manifest de contexto pronto | `context_pack_id` |
| `PolicyEvaluated` | PolicyEngineService | Acao avaliada | `policy_decision_id` |
| `CreditsEstimated` | CreditsService | Custo simulado calculado | `credit_estimate_id` |
| `PMOAuditRequested` | CEO Agent | Plano enviado ao PMO | `pmo_request_id` |
| `PMOAuditCompleted` | PMO Auditor | PMO aprovou/bloqueou | `pmo_audit_id`, `verdict` |
| `FounderApprovalRequested` | CEO Agent | Decisao humana solicitada | `approval_request_id` |
| `FounderDecisionRecorded` | Founder | Founder decidiu | `approval_id`, `decision` |
| `CheckoutLocked` | CEO/Doc Architect | Escopo travado | `checkout_lock_id` |
| `ArtifactGenerationStarted` | ArtifactService | Criacao documental iniciada | `artifact_set_id` |
| `ArtifactGenerated` | ArtifactService | Artefato gerado | `artifact_id`, `path` |
| `CheckoutReleased` | CEO/Doc Architect | Escopo liberado | `checkout_release_id` |
| `DeliveryAuditRequested` | CEO Agent | Entrega enviada ao PMO | `delivery_audit_request_id` |
| `DeliveryAudited` | PMO Auditor | Entrega validada | `delivery_audit_id`, `verdict` |
| `ProjectNextActionRecommended` | CEO Agent | Proximo passo proposto | `recommendation` |

## Eventos de bloqueio

| Evento | Motivo |
|---|---|
| `ActionBlockedByPolicy` | Policy nao permite a acao |
| `ActionBlockedByCost` | Custo exige aprovacao ou e alto demais |
| `ActionBlockedByMissingContext` | Faltam fontes, briefing ou memoria |
| `ActionBlockedByPMO` | PMO bloqueou ou pediu patches |
| `ActionBlockedByFounder` | Founder nao aprovou |
| `ActionBlockedByCanonicalConflict` | Conflito com docs canonicos |
| `ActionBlockedByDocumentalPhase` | Tentativa de implementacao em fase documental |

## Template de evento

```yaml
event_id:
simulation_only: true
event_type:
task_id:
project_id:
actor:
role:
occurred_at:
payload:
policies_applied:
credit_estimate_ref:
approval_ref:
append_only: true
notes:
```

## Exemplo

```yaml
event_id: evt_sim_001
simulation_only: true
event_type: PolicyEvaluated
task_id: CKOS-PROJECT-TEST-001
project_id: project_miriam_planning
actor: PolicyEngineService
role: simulated_backend_service
occurred_at: 2026-05-26
payload:
  action_requested: create_project_filetree_proposal
  decision: approved_with_pmo_audit
policies_applied:
  - POLICY_PLANNER_FIRST
  - POLICY_PMO_AUDIT_FOR_MEDIUM_HIGH_RISK
credit_estimate_ref: ckc_estimate_001
approval_ref: null
append_only: true
notes: "Simulated event only; no runtime call performed."
```

