---
title: Simulated API Endpoint Map
system_id: simulated_api_endpoint_map
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

# Simulated API Endpoint Map

## Proposito

Definir endpoints falsos para testes documentais do CKOS no Codex.

Nenhum endpoint abaixo existe em runtime. Eles sao nomes de referencia para simular backend e API sem implementar nada.

## Regra de uso

Sempre declarar:

```yaml
endpoint_is_simulated: true
network_call_performed: false
backend_required: false
implementation_allowed: false
```

## Endpoints simulados

| Metodo | Endpoint simulado | Service | Funcao | Output esperado |
|---|---|---|---|---|
| POST | `/intent/interpret` | `IntentService` | Interpretar intencao curta | `IntentAnalysis` |
| POST | `/projects/propose` | `ProjectService` | Propor projeto | `ProjectProposal` |
| POST | `/projects/filetree/propose` | `ProjectService` | Propor filetree | `FiletreeProposal` |
| POST | `/context-pack/build` | `ContextPackService` | Montar manifest de contexto | `ContextPack` |
| POST | `/policy/evaluate` | `PolicyEngineService` | Avaliar acao | `PolicyDecision` |
| POST | `/credits/estimate` | `CreditsService` | Estimar custo | `CreditEstimate` |
| POST | `/connectors/declare` | `ConnectorService` | Declarar conector | `ConnectorDeclaration` |
| POST | `/connectors/simulate-run` | `ConnectorService` | Simular run sem executar | `ConnectorRunSimulation` |
| POST | `/pmo/audit-request` | `PMOAuditService` | Enviar plano para PMO | `PMOAuditRequest` |
| POST | `/pmo/audit-result` | `PMOAuditService` | Registrar decisao PMO | `PMOAudit` |
| POST | `/approvals/founder/request` | `ApprovalService` | Pedir aprovacao | `FounderApprovalRequest` |
| POST | `/approvals/founder/decision` | `ApprovalService` | Registrar decisao | `FounderApproval` |
| POST | `/checkout/lock` | `ArtifactService` | Bloquear escopo documental | `CheckoutLock` |
| POST | `/artifacts/generate` | `ArtifactService` | Gerar artefatos aprovados | `ArtifactSet` |
| POST | `/checkout/release` | `ArtifactService` | Liberar escopo documental | `CheckoutRelease` |
| POST | `/events/append` | `EventLogService` | Registrar evento | `EventLogAppendResult` |
| GET | `/simulation/status` | `EventLogService` | Ver estado da demo | `SimulationStatus` |

## Request envelope

Todo endpoint simulado usa envelope comum:

```yaml
request_id:
task_id:
actor:
role:
workspace:
project_id:
simulation_only: true
payload:
policies_requested:
credit_estimate_required:
pmo_audit_required:
founder_approval_required:
```

## Response envelope

```yaml
request_id:
task_id:
endpoint:
service:
simulation_only: true
status:
result_ref:
events_emitted:
policies_applied:
credit_estimate:
approvals_required:
blocked_reason:
next_recommended_action:
```

## Exemplo de simulacao

```yaml
endpoint: POST /intent/interpret
service: IntentService
simulation_only: true
request:
  intent_text: "Criar projeto para perfil no Instagram para recem advogada penal feminina no Brasil."
response:
  project_type: personal_branding_legal
  category: personal_branding
  subcategory: regulated_legal_marketing
  risk_level: high
  suggested_output: analysis_doc
  pmo_audit_required: true
  founder_approval_required: true
  events_emitted:
    - IntentSubmitted
    - IntentResolved
```

## Endpoints bloqueados nesta fase

Os seguintes endpoints nao devem ser simulados como executaveis:

```txt
POST /runtime/agent/run
POST /database/migrate
POST /ui/render
POST /oauth/connect/live
POST /billing/charge
POST /credits/reserve/live
POST /n8n/workflows/execute
POST /external-api/call/live
```

Se aparecerem em um plano, PMO deve bloquear ou rebaixar para planejamento documental.

