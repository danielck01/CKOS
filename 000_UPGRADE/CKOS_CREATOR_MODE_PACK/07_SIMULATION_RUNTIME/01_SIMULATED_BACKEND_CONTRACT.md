---
title: Simulated Backend Contract
system_id: simulated_backend_contract
category: creator_mode_simulation_runtime
status: active
version: 1.0.0
owner: ceo_agent
reviewers:
  - founder
  - pmo_ckos
  - metacognik
created_for: CKOS_CREATOR_MODE_PACK
created_at: 2026-05-26
---

# Simulated Backend Contract

## Proposito

Nomear os servicos internos que o CEO Agent pode referenciar durante uma simulacao de projeto.

Este documento nao implementa backend. Ele define contratos narrativos e estruturas esperadas para testes documentais.

## Flags obrigatorias

```yaml
simulation_only: true
runtime_execution: false
backend_created: false
api_created: false
database_created: false
migrations_created: false
real_connectors_executed: false
```

## Servicos simulados

| Service | Funcao | Entrada | Saida | Policy minima |
|---|---|---|---|---|
| `IntentService` | Interpretar intencao minima | `Intent` | `IntentAnalysis` | `POLICY_PLANNER_FIRST` |
| `ProjectService` | Propor projeto e filetree | `IntentAnalysis` | `ProjectProposal` | `POLICY_FOUNDER_APPROVAL_BEFORE_EXECUTION` |
| `ContextPackService` | Montar contexto consultavel | `ProjectProposal` | `ContextPack` | `POLICY_CONTEXT_PACK_REQUIRED` |
| `PolicyEngineService` | Avaliar risco, permissao e bloqueios | `ActionRequest` | `PolicyDecision` | `POLICY_CANONICAL_DOC_PROTECTION` |
| `CreditsService` | Estimar custo CKOS simulado | `ActionPlan` | `CreditEstimate` | `POLICY_COST_VISIBILITY_REQUIRED` |
| `ConnectorService` | Declarar conectores simulados | `ConnectorRequest` | `ConnectorRunSimulation` | `POLICY_CONNECTOR_SCOPE_LIMIT_REQUIRED` |
| `PMOAuditService` | Auditar escopo, custo, risco e ordem | `PMOHandoff` | `PMOAudit` | `POLICY_PMO_AUDIT_FOR_MEDIUM_HIGH_RISK` |
| `ArtifactService` | Gerar artefatos documentais aprovados | `ApprovedExecutionPlan` | `ArtifactSet` | `POLICY_CHECKOUT_LOCK_REQUIRED` |
| `EventLogService` | Registrar trilha auditavel | `EventLogEntry` | `EventLogAppendResult` | `POLICY_APPEND_ONLY_AUDIT_LOG` |
| `ApprovalService` | Registrar decisao Founder | `ApprovalRequest` | `FounderApproval` | `POLICY_HUMAN_APPROVAL_REQUIRED` |

## Contrato de execucao simulada

Todo servico simulado deve responder neste formato:

```yaml
service:
operation:
simulation_only: true
input_ref:
output_ref:
policies_applied:
credit_estimate:
risk_level:
approval_required:
status:
notes:
```

## Operacoes permitidas por servico

### IntentService

- `interpret_intent`
- `classify_project_type`
- `detect_risk_domain`
- `suggest_first_output`

Nao pode:

- criar artefato final;
- aprovar sozinho;
- iniciar pack de notas.

### ProjectService

- `propose_project`
- `propose_filetree`
- `list_required_artifacts`
- `identify_dependencies`

Nao pode:

- criar pasta oficial sem Founder approval;
- transformar proposta em arquitetura canonica;
- iniciar docs 25-30.

### ContextPackService

- `list_local_sources`
- `list_uploaded_sources`
- `map_missing_context`
- `build_context_pack_manifest`

Nao pode:

- executar deep research sem approval;
- tratar output de IA anterior como source-of-truth;
- enviar PII para fonte externa.

### PolicyEngineService

- `evaluate_action`
- `evaluate_connector`
- `evaluate_cost_gate`
- `evaluate_sensitive_domain`
- `block_action`

Nao pode:

- relaxar policy por conveniencia;
- ignorar documentos canonicos;
- permitir implementacao na fase documental.

### CreditsService

- `estimate_action_cost`
- `estimate_connector_cost`
- `estimate_pack_cost`
- `suggest_cheaper_option`

Nao pode:

- cobrar creditos reais;
- esconder custo de PMO;
- executar reserva real de creditos.

### ConnectorService

- `declare_connector`
- `simulate_connector_run`
- `simulate_connector_block`
- `record_source_reference`

Nao pode:

- chamar API externa;
- abrir OAuth real;
- salvar token;
- tratar n8n como core;
- tratar Manus como source runtime.

### PMOAuditService

- `review_plan`
- `block_plan`
- `approve_with_patches`
- `approve_next_action`

Nao pode:

- substituir Founder;
- aprovar strategy final em dominio sensivel sem fontes;
- ignorar custo ou risco.

### ArtifactService

- `generate_analysis_doc`
- `generate_filetree_proposal`
- `generate_execution_plan`
- `generate_pmo_request`
- `generate_approval_checklist`
- `generate_note_pack_after_approval`

Nao pode:

- gerar artefato fora do escopo aprovado;
- criar estrategia final sem briefing;
- alterar canonicos sem patch plan.

## Saida esperada

O objetivo deste contrato e dar ao CEO Agent uma linguagem comum:

```txt
Simulated service: ContextPackService
Operation: build_context_pack_manifest
Endpoint simulated: POST /context-pack/build
Policies: POLICY_CONTEXT_PACK_REQUIRED, POLICY_SOURCE_INDEX_REQUIRED
Result: approved_for_planning_only
```

