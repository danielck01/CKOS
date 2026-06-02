---
title: Connectors, MCP and Integrations Architecture
file: 26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md
system_id: connectors_mcp_and_integrations_architecture
display_name: Connectors, MCP and Integrations Architecture
doc_type: canonical_doc
category: evolution_system
layer: canonical
status: draft
version: 1.0.4
created_at: 2026-05-29
updated_at: 2026-05-31
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - metacognik
  - technical
  - qa_lead
approval_required:
  - founder
  - technical
  - metacognik
source_type: canonical_creation_from_authorized_microgate
source_path: 000_ROADMAPS/18_CONNECTORS_MCP_INTEGRATIONS_ROADMAP/
source_tool: codex
provenance_status: verified
version_note: "v1.0.4 - Light governance patch PL-01, PL-02, PL-04, PL-05 after external audit."
project: ckos
related_docs:
  - 00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md
  - 00_SYSTEM_GOVERNANCE/00_DOCUMENT_TEMPLATE.md
  - 00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - 03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - 03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - 05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL.md
  - 05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md
  - 06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md
  - 07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md
risk_level: high
confidence: high
tags:
  - connectors
  - mcp
  - integrations
  - external_tools
  - policy_engine
  - tool_router
  - approval_gate
  - secret_refs
  - audit_logs
  - cost_guard
---

# 26 - Connectors, MCP and Integrations Architecture

## 1. Purpose

This document defines how CKOS governs connectors, MCP servers, integrations, webhooks, collectors, API providers, external tools and execution boundaries.

It exists to prevent external access from becoming an uncontrolled side channel. Connectors are useful only when they are policy-controlled, tenant-scoped, cost-aware, auditable and reversible where possible.

## 2. What This Document Is

This is the canonical architecture for external access surfaces in CKOS.

It defines:

- connector concepts and taxonomy;
- when to use MCP, native APIs, collectors, webhooks, research connectors and private RAG;
- execution boundaries for tools and external providers;
- policy, approval, cost, secret, audit and evidence requirements;
- registry schema proposals for future patches;
- failure modes, risk model and MVP P0 scope.

## 3. What This Document Is Not

This document is not:

- implementation permission;
- a backend service;
- an API specification for production endpoints;
- a migration plan;
- a real MCP server;
- a UI design;
- a vendor selection mandate;
- a grant to call external providers;
- a promotion of n8n, Manus, Apify, Perplexity, OpenRouter or any provider to CKOS core runtime.

## 4. Core Thesis

Connectors, MCP servers, APIs, collectors, webhooks and external tools are not autonomous sources of truth. They are governed access surfaces controlled by `policy_engine`, `tool_router`, `approval_gate`, `cost_guard`, `audit_logs`, tenant isolation and `secret_refs`.

In Portuguese:

> Conectores nao sao atalhos livres para o mundo externo. Eles sao portas governadas. Toda chamada precisa ter permissao, custo estimado, escopo, rastreabilidade, isolamento por tenant, politica de segredo e possibilidade de auditoria.

## 5. Definitions

| Term | Definition |
|---|---|
| `connector` | Governed CKOS abstraction that exposes an external capability to runtime through policy, routing, cost, secrets and audit. |
| `MCP server` | External or internal Model Context Protocol server exposing tools/resources through a standard protocol. It is a transport and capability surface, not an authority layer. |
| `tool` | Executable action available to an agent or workflow through `tool_router`. It may be local or connector-backed. |
| `collector` | Connector specialized in gathering external or internal data and normalizing it into evidence, context packs, artifacts or records. |
| `integration` | Longer-lived relationship with an external system, usually requiring credentials, sync policy and data egress controls. |
| `webhook` | Inbound or outbound event bridge between CKOS and an external system. |
| `API provider` | External service offering an API that may back a connector, collector or integration. |
| `skill` | CKOS execution capability from the Skills Registry. A skill may request tools but does not bypass policies. |
| `secret_ref` | Pointer to a vault-managed secret. It never contains the secret value. |

## 6. Connector Taxonomy

| Class | Examples | Primary use | Authority level |
|---|---|---|---|
| Native API connector | Stripe, GitHub, Google APIs | Structured provider operation | Governed access surface |
| MCP connector | MCP server exposing tools/resources | Standardized tool/resource access | Governed access surface |
| Collector | Apify actor, academic collector, web parser | Data collection and normalization | Evidence input only |
| Webhook integration | payment event, CRM update, calendar callback | Event ingress/egress | Event source pending validation |
| Research connector | Perplexity, OpenRouter search, PubMed, CrossRef, arXiv | Evidence discovery | Research evidence input |
| Private knowledge connector | upload parser, private RAG, internal artifact retriever | Tenant-private knowledge access | Internal evidence/context input |
| Prototype automation | n8n workflow, manual Zap-like flow | Experiment or acceleration | Prototype only |

## 7. MCP Role In CKOS

MCP is a protocol boundary for exposing tools and resources to model-driven workflows. It can simplify integration, but it does not change CKOS authority.

Mandatory decisions:

1. MCP does not replace `policy_engine`.
2. MCP does not replace `tool_router`.
3. MCP does not replace `approval_gate`.
4. MCP cannot access secrets directly.
5. MCP cannot write to the database directly without the CKOS runtime.
6. MCP cannot execute cross-tenant actions.
7. MCP outputs are not truth until scored, logged and connected to evidence.

When CKOS uses MCP, the runtime must wrap MCP calls in the same event, approval, cost, audit and secret boundaries used for any other tool.

## 8. Connector vs Tool vs Skill vs Collector vs Integration

| Item | What it is | Example | Who authorizes |
|---|---|---|---|
| Connector | Governed access surface | `github_connector` | `policy_engine` + registry |
| Tool | Executable action | `create_issue` | `tool_router` |
| Skill | CKOS capability that may use tools | `research-summary` | skillRegistry + policy |
| Collector | Data-gathering connector | `pubmed_collector` | policy + cost + source rules |
| Integration | Long-lived external relationship | `stripe_billing_integration` | policy + approval + secrets |
| MCP server | Protocol server exposing tools/resources | `docs_mcp_server` | mcp registry + policy |

A skill can request a tool. A tool can be backed by a connector or MCP server. A connector can include collectors or webhook handlers. None of them bypasses runtime governance.

## 9. Integration Boundary Model

All external access follows this boundary:

```txt
intent or workflow step
  -> context_pack_builder
  -> policy_engine
  -> cost_guard reservation or estimate
  -> approval_gate when sensitive
  -> tool_router
  -> connector_adapter or mcp_adapter
  -> external provider
  -> normalization
  -> eval/evidence scoring
  -> event_store + audit_logs
  -> evidence_items/context_packs/artifacts/projections
```

The external provider never becomes the source of truth. The source of truth is the CKOS event store plus governed persisted objects.

Governance note (PL-01): `connector_adapter` and `mcp_adapter` are documentary placeholders pending P26-1 in Doc 10. They do not exist as canonical runtime components until Doc 10 is patched, audited and approved.

## 10. Policy-First Connector Execution

Every connector call must be denied by default and allowed only through explicit grants.

Required preconditions:

- actor has capability grant;
- project/tenant has connector enabled;
- connector status lifecycle permits execution;
- connector risk is allowed by plan and policy;
- data classification permits egress;
- `secret_ref` exists and is active when required;
- cost estimate fits budget or has approval;
- rate limit and retry policy are defined for provider-facing calls;
- idempotency key exists when retry, webhook or external mutation can duplicate effects;
- approval policy is satisfied;
- audit trail can be created.

Missing policy means deny.

## 11. Tool Router Rules

`tool_router` decides whether a tool can run by intersecting:

```txt
skill.allowed_tools
  intersection agent.allowed_tools
  intersection project.allowed_tools
  intersection connector_registry.status=active
  intersection capability_grants
  intersection plan_limits
  intersection policy_engine allow
```

Rules:

- no connector runs without capability grant;
- connector-backed grants are action-scoped; wildcard grants cannot authorize external mutation or data egress;
- no tool runs only because an MCP server exposes it;
- no provider action is callable directly by UI or agent;
- every tool call receives `correlation_id`, `causation_id`, tenant scope and cost context;
- every sensitive or medium+ risk tool call is audit logged.

## 12. Approval Gate Rules

`approval_gate` enters before calls that are sensitive, irreversible, high-cost, externally mutating or privacy-relevant.

Approval is required when:

- connector mutates an external system;
- connector may publish or send data externally;
- connector handles PII or confidential data;
- cost estimate exceeds threshold;
- webhook subscription changes external state;
- connector can create or modify artifacts for client delivery;
- provider terms, legal risk or data egress risk are non-trivial.

Approval must reference the exact connector, action, input scope, estimated cost, data classification, rollback/fallback policy and approver.

Approval for connector execution is not reusable across materially different action, payload scope, data class, provider account, tenant scope or cost envelope.

## 13. Secret Management and `secret_ref`

Secrets never live in connector configs, events, logs, prompts, study notes, UI or database rows as raw values.

Rules:

- connector registry stores `secret_ref`, not token values;
- MCP servers receive scoped runtime credentials only through CKOS runtime mediation;
- secret lookup happens server-side and is logged as `SecretAccessed` without secret value;
- secret rotation changes vault state, not connector architecture;
- missing, expired or revoked secret_ref fails closed;
- logs and outputs must redact detected tokens.

Suggested fields:

```txt
secret_ref
secret_owner_type: connector | mcp_server | provider | actor | webhook
secret_scope: org | workspace | project
status: active | rotating | revoked | expired
expires_at
last_rotated_at
```

Future Doc 11 patch must extend `secret_refs.owner_type` to include at minimum:

```txt
connector
mcp_server
webhook
```

This extension is required so connector credentials, MCP server credentials and webhook signing secrets can all reference vault-managed secrets without overloading `provider`, `actor` or generic integration ownership.

## 14. Tenant Isolation and RLS Requirements

Every connector object and run must carry tenant scope:

```txt
org_id
workspace_id
project_id
actor_id
correlation_id
```

Rules:

- connector data is RLS-scoped by `org_id`;
- private RAG uses namespace as precondition, never post-filter;
- connector credentials are scoped by org/workspace/project;
- webhook ingress must resolve tenant before any processing;
- cross-tenant action is always denied;
- provider account sharing between tenants is forbidden unless explicitly modeled as enterprise-managed shared infrastructure with strict sub-scope isolation.

## 15. PII and Sensitive Data Handling

Before any external call:

1. classify data as `public`, `internal`, `confidential`, `PII` or `sensitive`;
2. minimize payload to the least necessary fields;
3. sanitize PII when external source does not require it;
4. block egress when policy forbids external processing;
5. audit PII access and redaction;
6. prefer private upload/RAG when sensitive information already exists in the vault.

Mandatory decision: upload/private RAG has priority when the needed information is already in the tenant vault.

## 16. Cost Guard and Credit Reservation

Connector execution consumes cost and may consume credits. Cost control follows docs 13 and 24.

Before execution:

- estimate provider cost, model cost and internal processing cost;
- reserve credits for paid connector/tool/collector runs;
- block when wallet or quota is insufficient;
- enforce provider and connector rate limits before external calls;
- require approval for over-threshold costs;
- record actual cost after execution;
- release unused reservation on failure or cancellation.

Cost scopes:

```txt
connector | mcp_server | tool | collector | webhook | provider | run | workflow | project | tenant | day | month
```

## 17. Connector Event Model

Connector activity is event-sourced. Suggested event types:

```txt
ConnectorCallRequested
ConnectorPolicyChecked
ConnectorCapabilityGranted
ConnectorCallApproved
ConnectorCallDenied
ConnectorCallStarted
ConnectorCallSucceeded
ConnectorCallFailed
ConnectorCallTimedOut
ConnectorOutputNormalized
ConnectorEvidenceCreated
ConnectorArtifactCandidateCreated
ConnectorCostReserved
ConnectorCostConsumed
ConnectorSecretAccessed
ConnectorPIIRedacted
ConnectorFallbackSelected
ConnectorDisabled
MCPServerRegistered
MCPToolBindingCreated
WebhookReceived
WebhookValidated
WebhookRejected
```

All events require tenant scope, actor, connector id, action, risk level, cost estimate/actual when applicable, correlation id and causation id.

Governance note (PL-02): the 23 connector event types listed above require P26-8 before any runtime may emit events. Until P26-8 patches the Doc 10 event catalog and is audited and approved, these are proposed types, not canonical events that runtime may emit.

## 18. Audit Logs and Run Replay

Audit logs record security, authorization and governance facts. Event store records execution facts. Both are required.

Audit entries are mandatory for:

- permission grant/deny;
- secret lookup;
- PII redaction;
- connector approval request/resolution;
- external mutation;
- webhook validation failure;
- policy violation;
- provider exposure blocked;
- cost hard limit;
- connector status transition;
- fallback selection;
- retry exhaustion or rate-limit block;
- webhook idempotency collision;
- cross-tenant attempt.

Run replay must reconstruct:

- connector selected;
- policy evaluated;
- approval status;
- context pack used;
- payload after redaction;
- provider response metadata;
- normalized output;
- cost;
- idempotency key, retry count and fallback decision;
- connector status at selection time;
- evidence/artifact links;
- failure and fallback path.

## 19. Research Connectors

Research connectors discover evidence. They do not decide truth.

Examples:

- Perplexity/OpenRouter research;
- PubMed, CrossRef, arXiv;
- public web search APIs;
- industry reports through authorized APIs;
- private RAG and uploads.

Rules:

- every research output must become `evidence_items` or `context_packs` with source metadata;
- source metadata must include source ref, retrieved_at, freshness policy, license or terms posture when known and confidence;
- no synthesis without evidence ids;
- source reliability, freshness and confidence are required;
- research connector output cannot become a final artifact without eval and approval when required.

## 20. Apify Actor Governance

Apify actors are governed collectors, not free agents.

Use Apify when:

- a source needs structured public collection;
- native API is unavailable, insufficient or commercially impractical;
- terms and legal posture allow collection;
- output can be normalized and scored;
- actor is registered and approved.

Do not use Apify when:

- native API provides safer official access;
- source includes sensitive tenant data;
- robots/terms/legal posture prohibit collection;
- actor requires uncontrolled credentials;
- output cannot be audited or normalized.

Apify actors require `collector_registry`, `provider_registry`, `actor_registry`, `secret_ref`, rate limit, cost profile, PII risk and fallback policy.

## 21. Perplexity/OpenRouter Research Connector Governance

Perplexity/OpenRouter may be used as research connectors, not final sources of truth.

Use them when:

- the task needs current web discovery;
- citations or source links are returned;
- data sent outward is public or sanitized;
- cost is within budget;
- outputs are normalized into evidence.

Do not use them when:

- tenant-private data is enough in RAG;
- query contains unredacted PII;
- decision requires primary academic/legal source;
- output cannot be cited or verified.

OpenRouter may route model/research calls, but CKOS owns model orchestration and policy. No model/provider is core.

## 22. Academic Source Connectors

Use academic connectors for scientific, medical, technical, regulatory or evidence-sensitive questions.

Priority sources:

- PubMed for biomedical and behavioral science;
- CrossRef for DOI metadata;
- arXiv for technical preprints;
- SSRN when relevant;
- institutional repositories;
- official government or standards databases when applicable.

Rules:

- distinguish peer-reviewed research from preprints;
- extract scope and limitations;
- never extrapolate beyond the study;
- cite DOI/source ref when available;
- prefer primary source over secondary summary;
- use freshness policies by domain.

## 23. Upload/RAG/Private Knowledge Connectors

Private knowledge connectors access tenant-owned files, artifacts, memories and vector indexes.

Use private upload/RAG when:

- information is already in the vault;
- source contains confidential or PII data;
- external search would leak context;
- tenant-specific decision history matters;
- evidence provenance is internal and approved.

Private RAG rules:

- namespace is mandatory;
- permission filter is precondition;
- context pack records reads;
- stale content is flagged;
- retrieved items are evidence/context, not automatic truth.

## 24. Webhooks and External Automation

Webhooks are event bridges. They are not trusted just because they are received.

Inbound webhook flow:

```txt
receive
  -> verify signature
  -> resolve tenant and connector
  -> validate event schema
  -> policy check
  -> dedupe by idempotency key
  -> emit WebhookValidated or WebhookRejected
  -> append event
  -> route to workflow only if allowed
```

Outbound webhook flow:

```txt
workflow event
  -> policy check
  -> approval if sensitive
  -> cost/rate check
  -> payload minimization
  -> signed delivery
  -> delivery event + audit log
```

Webhook retry must be idempotent, bounded and observable.

Webhook registration must declare tenant resolution policy, allowed event types, signing secret reference, idempotency key source, retry bounds and disabled/revoked behavior. Missing webhook policy means reject before route.

## 25. n8n Positioning

n8n is a prototype and accelerator, not CKOS core runtime.

Allowed:

- early workflow exploration;
- proof-of-concept for connector value;
- manual testing with fake/sanitized data;
- temporary bridge for understanding provider behavior.

Forbidden:

- production source of truth;
- permanent event bus;
- direct bypass of `policy_engine`;
- storage of real secrets outside vault;
- tenant data processing without CKOS isolation;
- JSON workflows treated as canonical architecture.

Any n8n learning that matters must be converted into CKOS docs, registries or study notes before canonical implementation.

## 26. MCP Server Registry

MCP servers must be registered before use.

Registry fields proposed:

```txt
mcp_server_id
display_name
owner
transport_type
endpoint_ref
tenant_scope
allowed_projects
tool_names
resource_names
secret_ref
risk_level
cost_profile
approval_policy_ref
data_egress_policy
pii_policy
status
fallback_policy
audit_required
last_eval_at
```

Registration does not authorize execution. Execution still requires capability grant, policy allow, cost approval and tool routing.

## 27. Connector Registry Schema Proposal

Future Doc 11 patch should formalize these tables. This document does not apply migrations.

```txt
connector_registry(
  id,
  org_id,
  workspace_id,
  connector_key,
  connector_type,
  provider_key,
  status,
  risk_level,
  cost_profile,
  approval_policy_ref,
  secret_ref,
  tenant_scope,
  data_egress_policy,
  pii_policy,
  rate_limit_policy,
  fallback_policy,
  audit_required,
  created_at,
  updated_at
)

connector_runs(
  id,
  org_id,
  workspace_id,
  project_id,
  connector_id,
  action,
  actor_type,
  actor_id,
  status,
  input_digest,
  output_ref,
  cost_estimate,
  cost_actual,
  approval_id,
  event_id,
  audit_log_id,
  correlation_id,
  causation_id,
  started_at,
  completed_at
)

connector_credentials(
  id,
  org_id,
  connector_id,
  secret_ref,
  credential_scope,
  status,
  expires_at,
  last_rotated_at
)

connector_events(
  id,
  org_id uuid [RLS],
  connector_run_id,
  event_id,
  event_type,
  payload_ref,
  created_at
)

mcp_servers(
  id,
  org_id,
  workspace_id,
  server_key,
  transport_type,
  endpoint_ref,
  secret_ref,
  status,
  risk_level,
  approval_policy_ref,
  cost_profile,
  data_egress_policy,
  audit_required
)

mcp_tool_bindings(
  id uuid primary key,
  org_id uuid [RLS],
  workspace_id uuid,
  mcp_server_id uuid fk->mcp_servers,
  tool_key text,
  connector_id uuid fk->connector_registry,
  required_capability text,
  approval_policy_ref uuid fk->approval_policies,
  cost_profile jsonb,
  risk_level text,
  status text
)

webhook_registrations(
  id uuid primary key,
  org_id uuid [RLS],
  connector_id uuid fk->connector_registry,
  event_type text,
  endpoint_url text,
  secret_ref text,
  signature_algorithm text,
  status text,
  created_at timestamptz,
  updated_at timestamptz
)

webhook_deliveries(
  id uuid primary key,
  org_id uuid [RLS],
  webhook_id uuid fk->webhook_registrations,
  event_id uuid fk->events,
  status text,
  attempt_count integer,
  idempotency_key text,
  delivered_at timestamptz,
  created_at timestamptz
)

collectors_allowlist(
  id uuid primary key,
  org_id uuid [RLS],
  connector_id uuid fk->connector_registry,
  collector_id text,
  rate_limit jsonb,
  pii_risk_level text,
  authorization_level text,
  status text,
  created_at timestamptz,
  updated_at timestamptz
)
```

Field constraints for the future Doc 11 patch:

- `connector_events.org_id uuid [RLS]` is mandatory. Connector events are domain rows linked to tenant-scoped connector runs and must remain RLS-isolated.
- `connector_registry.status` must support a lifecycle equivalent to `requested | active | degraded | disabled | revoked`; only `active` can execute.
- connector-backed capability grants must be action-scoped and must not use wildcard authority for external mutation or data egress.
- `mcp_tool_bindings.org_id uuid [RLS]` is mandatory. Tool bindings are domain rows and must be tenant-isolated.
- `mcp_tool_bindings.workspace_id uuid` is mandatory when the MCP binding is workspace-scoped.
- `connector_registry.approval_policy_ref`, `mcp_servers.approval_policy_ref` and `mcp_tool_bindings.approval_policy_ref` must reference `approval_policies`. Connector policy is not duplicated inline.
- `webhook_registrations.connector_id` is `uuid fk->connector_registry`.
- `webhook_registrations.secret_ref` points to the vault-managed webhook signing secret and never stores the secret value.
- `webhook_registrations` must carry tenant resolution, allowed event type and disabled/revoked behavior as policy fields or policy refs.
- `webhook_deliveries.webhook_id` is `uuid fk->webhook_registrations`.
- `webhook_deliveries.event_id` is `uuid fk->events`.
- `webhook_deliveries.idempotency_key` is mandatory before retry or route.
- `collectors_allowlist.connector_id` is `uuid fk->connector_registry`.
- provider-facing connectors must reference rate-limit and retry policies; missing policy fails closed.
- research and collector normalized outputs must carry source metadata sufficient for evidence replay.

Minimum JSON contract for `cost_profile jsonb`:

```json
{
  "credits_per_call": 0,
  "cost_estimate_usd": 0,
  "budget_hard_limit_usd": 0
}
```

Minimum JSON contract for `data_egress_policy jsonb`:

```json
{
  "allowed_data_classes": ["public"],
  "pii_allowed": false,
  "redaction_required": true,
  "external_processing_allowed": false,
  "retention_policy": "none"
}
```

Every connector needs `risk_level`, `cost_profile`, `approval_policy_ref`, `secret_ref`, `tenant_scope` and audit trail.

## 28. Failure Modes and Fallbacks

| Failure | Required behavior | Fallback |
|---|---|---|
| Provider timeout | retry with bounded backoff; emit timeout event | alternate provider or queue |
| Provider rate limit | pause connector; respect reset window | lower-volume mode |
| Secret expired | fail closed; audit | rotate secret, then retry |
| Policy denied | block; no retry loop | request capability/approval |
| Missing rate-limit policy | fail closed before provider call | define policy before execution |
| Wildcard grant for external mutation | deny action | request action-scoped grant |
| Cost exceeded | block or approval | cheaper connector/RAG |
| PII detected | redact or block | private RAG |
| Output malformed | reject normalization | alternate parser/source |
| Evidence low quality | mark low confidence | request stronger source |
| Webhook replay | dedupe by idempotency key | no-op + audit |
| MCP server unavailable | mark degraded | native API or queued retry |
| Vendor outage | use adapter fallback | alternate vendor |
| Fallback weakens policy | deny fallback | choose governed equivalent |
| Cross-tenant mismatch | P0 block | incident review |

Fallback must never weaken policy, tenant isolation, secret handling or audit requirements.

## 29. Security Risks

| Risk | Severity | Control |
|---|---|---|
| Secret leakage | P0 | `secret_ref`, vault-only, redaction |
| Cross-tenant data access | P0 | RLS, namespace precondition, tenant-scoped credentials |
| Provider bypass from UI | P0 | server-side only, no provider SDK in UI |
| Unapproved external mutation | P1 | approval gate and audit log |
| PII egress | P1/P0 | classification, redaction, policy block |
| Vendor lock-in | P2 | adapter interface and fallback policy |
| Cost runaway | P1 | credit reservation and cost guard |
| Evidence poisoning | P1 | source scoring and Metacognik review |
| Webhook spoofing | P1 | signature verification and dedupe |
| MCP over-permission | P1 | tool binding grants and deny-by-default |
| Wildcard external authority | P1 | action-scoped grants and approval policy refs |

## 30. MVP P0 Scope

MVP P0 includes documentation and minimal governed architecture only:

- connector taxonomy;
- connector registry design;
- MCP server registry design;
- policy-first execution contract;
- `secret_ref` rules;
- audit/event model;
- cost reservation model;
- risk classification;
- failure/fallback policy;
- research connector governance;
- n8n prototype-only positioning.

MVP P0 does not include:

- real MCP server;
- real API connection;
- migrations;
- backend workers;
- UI;
- n8n production workflow;
- real external automation.

## 31. Out of Scope

Out of scope for this document:

- implementing connectors;
- writing code;
- creating database migrations;
- creating APIs;
- creating UI;
- creating agents;
- storing secrets;
- touching n8n JSONs;
- selecting a permanent vendor;
- creating docs 27-34;
- altering docs 01-25.

## 32. Required Patches to Docs 10/11/12/13/18/24

These are suggestions only. They are not applied by this document.

| Patch | Target doc | Suggested change | Gate |
|---|---|---|---|
| P26-1 | Doc 10 | Formalize `connector_adapter` for native connectors and `mcp_adapter` for MCP servers as subcomponents of `tool_router` or as an adapter layer immediately below it. This avoids ghost components in the boundary model and keeps `tool_router` as the execution authority. | Before connector runtime implementation |
| P26-2 | Doc 11 | Create/expand `connector_registry`, `connector_runs`, `connector_credentials`, `connector_events`, `mcp_servers`, `mcp_tool_bindings`, `webhook_registrations` and `webhook_deliveries`. Webhook persistence must include signed registration, delivery attempts, idempotency keys and event linkage. | Before migrations |
| P26-3 | Doc 12 | Expand policies for connector grants, secret scopes and external data egress. | Before external data processing |
| P26-4 | Doc 13 | Add evals for connector reliability, evidence quality, cost drift and privacy violations. | Before production connectors |
| P26-5 | Doc 18 | Align research connectors with connector registry and MCP/tool taxonomy. | Before research connector implementation |
| P26-6 | Doc 24 | Map credit consumption by connector, tool, collector, webhook and MCP call. | Before paid connector usage |
| P26-7 | Doc 11 v1.3.x | Add `collectors_allowlist` schema: `id uuid primary key`, `org_id uuid [RLS]`, `connector_id uuid fk->connector_registry`, `collector_id text`, `rate_limit jsonb`, `pii_risk_level text`, `authorization_level text`, `status text`, `created_at timestamptz`, `updated_at timestamptz`. This resolves deferred P18-6 from Doc 18 / Architecture Patch Report. | Before any Apify or collector in production |
| P26-8 | Doc 10 | Register the 23 connector event types from Doc 26 section 17 in the Doc 10 event catalog section 5.3 before implementation. Events must receive canonical type definitions before any runtime code emits them. | Before connector event implementation |

### 32.1 P26-2 Open Modeling Decisions

P26-2 remains unresolved. The future Doc 11 patch must explicitly decide the following schema modeling questions before migrations:

1. `webhook_deliveries`: decide between append-only event model or mutable status with companion table of attempts.
2. `connector_events`: decide between physical bridge table or view/read model derived from the `events` table.

These decisions are intentionally open in v1.0.3 and must not be treated as implemented, migrated or approved by this document.

### 32.2 v1.0.2 Audit Light Patch Matrix

The following audit corrections are applied in this document only. They do not apply migrations, patch docs 10/11/12/13/18/24, create Doc 27, create APIs, create MCP servers, create webhooks, create agents or start runtime automation.

| Patch | Documentation correction | Status |
|---|---|---|
| L-01 | `connector_events` requires `org_id uuid [RLS]` so connector domain rows remain tenant-isolated. | applied |
| L-02 | Future `secret_refs.owner_type` must include `connector`, `mcp_server` and `webhook`. | applied |
| L-03 | Connector registry execution depends on an explicit lifecycle; only `active` connectors may execute. | applied |
| L-04 | Connector-backed capability grants must be action-scoped; wildcard authority cannot authorize external mutation or data egress. | applied |
| L-05 | Webhook registration and delivery require tenant resolution, signing secret reference, allowed event types and idempotency policy before route. | applied |
| L-06 | Provider-facing connectors require rate-limit and retry policy; missing policy fails closed. | applied |
| L-07 | Research and collector outputs require replayable source metadata before becoming evidence/context. | applied |
| L-08 | Fallbacks cannot weaken policy, tenant isolation, secret handling, approval or audit requirements. | applied |
| L-09 | Runtime activation remains blocked until target docs are patched, externally audited and formally approved. | applied |

## 33. Acceptance Criteria

This document is acceptable when:

- it does not authorize implementation;
- it does not create backend, UI, API, migrations or MCP servers;
- it does not promote any vendor to core;
- it explains MCP, connector, tool, collector, integration and skill;
- it connects execution to `policy_engine`, `tool_router`, `approval_gate`, `audit_logs`, `cost_guard` and `secret_refs`;
- it includes risk model, cost model, failure modes and MVP P0;
- it records suggested patches without applying them;
- it preserves docs 01-25 and does not create docs 27-34.
- v1.0.1 audit patches P1-A to P1-F are incorporated as documentation-only corrections.
- v1.0.2 audit patches L-01 to L-09 are incorporated as documentation-only corrections.
- v1.0.3 reconciles L-03 to L-09 traceability and declares the P26-2 open modeling decisions without resolving or implementing them.
- v1.0.4 applies light governance patches PL-01 and PL-02 after external audit, preserving the block on runtime implementation.

## 34. Related Notes

- [[00_MASTER_MAP]]
- [[00_DOCUMENT_TEMPLATE]]
- [[00_DEPENDENCY_MAP]]
- [[10_SYSTEM_RUNTIME_ARCHITECTURE]]
- [[11_DATA_MODEL_AND_PERSISTENCE]]
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]]
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]]
- [[18_RESEARCH_PROTOCOL]]
- [[19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL]]
- [[24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE]]
- [[25_SELF_EVOLVING_SYSTEM_ARCHITECTURE]]

---

## Patch 1.0.0 - Document creation

**Date:** 2026-05-29; expanded 2026-05-30

**Author:** PMO_CKOS + Documentation Architecture Lead

**Status:** draft; requires Founder + Technical + Metacognik audit.

**Summary:**

- Created the canonical architecture for connectors, MCP and integrations.
- Locked connectors as governed access surfaces, not autonomous truth sources.
- Positioned n8n as prototype only, Apify as governed collector, and Perplexity/OpenRouter as research connectors.
- Defined MCP boundaries, connector registry proposal, failure modes, risk model, cost model and MVP P0.
- Registered suggested patches P26-1 to P26-6 without applying them.

## Patch 1.0.1 - PMO/Metacognik audit light patch

**Date:** 2026-05-29

**Author:** PMO_CKOS + Documentation Architect + Security/Data Governance Reviewer

**Status:** draft; requires Founder + Technical + Metacognik audit.

**Summary:**

- P1-A: added `org_id uuid [RLS]` and `workspace_id uuid` to `mcp_tool_bindings`.
- P1-B: added suggested patch P26-7 for `collectors_allowlist`, resolving the deferred P18-6 requirement.
- P1-C: expanded P26-1 to name `connector_adapter` and `mcp_adapter` under or immediately below `tool_router`.
- P1-D: added P26-8 to register the 23 connector event types from section 17 in Doc 10 section 5.3 before implementation.
- P1-E: expanded P26-2 with future `webhook_registrations` and `webhook_deliveries` schemas.
- P1-F: replaced ambiguous `approval_policy` fields with `approval_policy_ref uuid fk->approval_policies` in connector and MCP schemas.
- P2-A: added minimum `cost_profile jsonb` and `data_egress_policy jsonb` contracts.

**Scope confirmation:**

- Documentation only.
- No backend, API, migration, MCP server, n8n JSON, UI or runtime automation created.
- No docs 10, 11, 12, 13, 18 or 24 patched.
- No docs 27-34 created.

## Patch 1.0.2 - PMO/Metacognik audit light patch

**Date:** 2026-05-29

**Author:** PMO_CKOS + Architecture Patch Executor

**Status:** draft; requires Founder + Technical + Metacognik audit.

**Summary:**

- L-01: added `org_id uuid [RLS]` to `connector_events`.
- L-02: explicitly required future extension of `secret_refs.owner_type` to include `connector`, `mcp_server` and `webhook`.
- L-03: added connector lifecycle execution constraint; only `active` connectors may execute.
- L-04: added action-scoped capability grant constraint for connector-backed tools.
- L-05: added webhook tenant resolution, signing, allowed event type and idempotency policy requirements.
- L-06: added rate-limit and retry policy as provider-facing connector preconditions.
- L-07: added replayable source metadata requirement for research and collector evidence.
- L-08: clarified that fallback cannot weaken policy, tenant isolation, secrets, approval or audit.
- L-09: preserved runtime activation block until target docs are patched, audited and approved.

**Scope confirmation:**

- Documentation only.
- No backend, API, migration, MCP server, webhook, n8n JSON, UI, real agent or runtime automation created.
- No docs 10, 11, 12, 13, 18 or 24 patched.
- No docs 27-34 created.

## Patch 1.0.3 - Traceability and open schema decisions patch

**Date:** 2026-05-31

**Author:** PMO_CKOS + Documentation Patch Executor

**Status:** draft; requires Founder + Technical + Metacognik audit.

**Summary:**

- Bumped Doc 26 from `version: 1.0.2` to `version: 1.0.3`.
- Updated `updated_at` to `2026-05-31`.
- Reconciled L-03 to L-09 traceability with `SESSION_REGISTRY.md` and `ARCHITECTURE_PATCH_REPORT.md`.
- Declared two open P26-2 modeling decisions:
  - `webhook_deliveries`: append-only event model or mutable status with companion table of attempts.
  - `connector_events`: physical bridge table or derived view/read model from `events`.

**Scope confirmation:**

- Documentation only.
- No backend, API, migration, MCP server, webhook, n8n JSON, UI, real agent or runtime automation created.
- No docs 10, 11, 12, 13, 18 or 24 patched.
- No docs 01-25 modified.
- No docs 27-34 created.
- P26-1, P26-2, P26-3, P26-4, P26-6 and P26-8 remain unresolved suggested patches.

## Patch 1.0.4 - Light governance patch after external audit

**Date:** 2026-05-31

**Author:** PMO_CKOS + Documentation Patch Executor + Metacognik Compliance Assistant

**Status:** draft; released_with_required_external_audit.

**Summary:**

- Bumped Doc 26 from `version: 1.0.3` to `version: 1.0.4`.
- Updated `version_note` to mention: "Light governance patch PL-01, PL-02, PL-04, PL-05 after external audit."
- PL-01: clarified in section 9 that `connector_adapter` and `mcp_adapter` are documentary placeholders pending P26-1 in Doc 10.
- PL-02: clarified in section 17 that the 23 connector event types require P26-8 before any runtime emits events.

**Scope confirmation:**

- Documentation only.
- No backend, API, migration, MCP server, webhook, n8n JSON, UI, real agent or runtime automation created.
- No docs 01-25 modified.
- No docs 27-34 created.
- Study Layer 13 was not touched.
