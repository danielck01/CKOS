---
title: MCP Connectors Integrations Pre Architecture
file: MCP_CONNECTORS_INTEGRATIONS_PRE_ARCHITECTURE.md
system_id: mcp_connectors_integrations_pre_architecture
display_name: MCP, Connectors and Integrations Pre-Architecture
doc_type: pre_architecture_note
category: integrations
layer: study
status: draft
version: 0.1.0
created_at: 2026-05-27
updated_at: 2026-05-27
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - founder
  - technical
  - metacognik
approval_required:
  - founder
  - technical
  - metacognik
source_type: governance_review
source_path: 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md;03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
source_tool: codex
provenance_status: verified
project: ckos
related_docs:
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - 03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - 03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - 05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL.md
related_notes: []
tags: [mcp, connectors, integrations, policy_engine, tool_router, audit_logs]
risk_level: high
confidence: medium
canonical_change: false
---

# MCP, Connectors and Integrations Pre-Architecture

## 1. Executive lock

This is a pre-architecture note only. It does not create doc 26 and does not implement MCP, connectors, APIs, webhooks, n8n, RAG, agents, or tools.

## 2. Positioning

MCP is not CKOS core runtime.

In CKOS, MCP should be evaluated as a governed adapter/protocol for connecting models or agents to tools, files, APIs, databases, and external context.

MCP is allowed only if it passes through CKOS governance.

## 3. Non-bypass invariants

No integration can bypass:

- `policy_engine`;
- `tool_router`;
- `approval_gate`;
- `cost_guard`;
- `audit_logs`;
- tenant isolation;
- `secret_refs`;
- source manifest;
- evidence validation when it affects knowledge.

## 4. MCP cannot

- bypass runtime;
- expose tokens in frontend;
- write directly to canonical docs;
- replace Collector Registry;
- replace Approval Gate;
- operate without audit logs;
- become source of truth by itself;
- bypass tenant boundaries;
- run with unscoped secrets.

## 5. Comparative matrix

| Type | Use when | Do not use when | Main risks | Minimum approval | Policy relation | Cost relation | Audit relation | Source manifest relation |
|---|---|---|---|---|---|---|---|---|
| MCP server | External tool/context has a useful MCP contract and can be scoped | Core sensitive flow, payment, uncontrolled secrets | Tool overreach, hidden actions, token leakage | technical + pmo_ckos | Must be registered as allowed tool/capability | Cost profile required | Every call logged | Output becomes RAW/STUDY source only |
| Own API | Flow is core, recurring, sensitive, high-volume, or financial | Experiment/prototype | Premature build, wrong contract | founder + technical | Native policy enforcement | Full cost and rate policy | Full event/audit trail | API output can become evidence after validation |
| Collector | Goal is collection, research, benchmark, evidence | Needs to mutate external system | Provider leak, scraping risk, weak evidence | pmo_ckos + technical | Collector policy + provider allowlist | Collector cost profile | Collector run logged | Normalized output gets source manifest |
| Webhook | External event must enter CKOS | Payload unsigned or untrusted | Spoofing, replay, injection | technical | Ingress policy required | Cost if triggers run | Webhook received + decision logged | Payload saved as raw source |
| n8n | Prototype, backoffice, temporary non-critical automation | Core runtime, payments, credits, sensitive data | Tool dependency, shadow runtime | pmo_ckos; founder if high risk | Must call CKOS API, not bypass it | Budget gate required | Logs mirrored to CKOS | n8n output is unverified RAW |
| Native integration | Strategic integration requiring long-term reliability | Demand unclear | Overbuilding, vendor lock | founder + technical | Native capability/policy | Productized cost model | Full audit/event model | Can become governed source |
| Export/import manual | Bootstrap, migration, one-off analysis | Real-time or recurring need | Human error, stale data | pmo_ckos | Manual review required | Low/direct cost | Import logged | Requires source manifest |
| Browser/computer-use | Supervised inspection or manual UI operation | Critical autonomous operation | Non-determinism, ToS risk | pmo_ckos + technical if sensitive | Allowed action scope required | Session budget | Screen/action log required | Screens/results as RAW only |
| RAG/private ingestion | Private docs with tenant namespace and policy | PII unclassified or rights unclear | Cross-tenant leak, polluted memory | technical; legal if PII | Memory policy + RLS | Embedding/storage cost | Ingestion and retrieval logged | Each doc gets manifest |

## 6. Secret policy

- Secrets live only in vault/secret manager.
- CKOS stores only `secret_ref`.
- Frontend never receives provider token, actor id, provider endpoint secret, OAuth refresh token, or webhook secret.
- Secret access emits audit event.
- Connector output must be redacted before study.

## 7. Cost policy

Every connector or MCP server must have:

- cost profile;
- rate limit;
- quota;
- failure cost behavior;
- cancellation behavior;
- approval threshold.

High-cost deep research and high-volume collection require approval before run.

## 8. Evidence policy

External integration output is not evidence until:

- provenance exists;
- source type is known;
- reliability is scored;
- confidence is assigned;
- contradictions are checked;
- PMO or Metacognik review is complete when risk is high.

## 9. Recommended canonical destination

This note should feed future:

- `26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`;
- `27_COLLECTOR_REGISTRY_AND_RESEARCH_ACTORS_ARCHITECTURE.md`;
- `28_KNOWLEDGE_INGESTION_UPLOADS_AND_SOURCE_GOVERNANCE_ARCHITECTURE.md`.

## 10. Open questions for Founder

- Should MCP be allowed in P0 only as manual/dev adapter?
- Which providers are approved for first study: Google Drive, Apify, Perplexity/OpenRouter, YouTube transcripts?
- Should browser/computer-use be documented as a separate governed mode in doc 26?
