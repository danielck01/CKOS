---
title: Paperclip Governance Approvals And Budgets Study
file: 04_PAPERCLIP_GOVERNANCE_APPROVALS_AND_BUDGETS_STUDY.md
layer: study
study_layer: 14_PAPERCLIP_AGENT_OPERATING_MODEL
doc_type: study_note
phase: 000_STUDY_NOTES
category: paperclip_agent_operating_model
status: draft
version: 0.1.1
created_at: 2026-06-01
updated_at: 2026-06-01
owner: pmo_ckos
responsible_agent: codex
reviewers:
  - claude
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
  - metacognik
source_type: paperclip_benchmark_study
source_tool: codex
provenance_status: unverified
confidence: unverified
risk_level: high
purpose: Study Paperclip governance, approval and budget patterns as non-authoritative future CKOS reference material.
---

# 04_PAPERCLIP_GOVERNANCE_APPROVALS_AND_BUDGETS_STUDY.md

**Study Layer**: 14_PAPERCLIP_AGENT_OPERATING_MODEL  
**Note**: 04  
**Status**: Study-only, non-canonical  
**Created**: 2026-06-01  
**Purpose**: Analyze Paperclip's governance, approval workflows, and budget control mechanisms

## Non-Authority Boundary

This file is study-only, draft and unverified. It is not canonical.

It does not authorize Doc 27. It does not create Doc 27. It does not authorize backend, UI, API, database, migrations, real agents, runtime automations, n8n JSONs, MCP servers, webhooks or production schemas.

It may coordinate future sessions as a non-canonical operating note. It may not override `SESSION_REGISTRY.md`, `MULTI_SESSION_EXECUTION_POLICY.md`, canonical docs, Founder approval or PMO/Metacognik audit.

## Overview

Paperclip implements sophisticated governance mechanisms including approval workflows, budget policies with hard stops, cost tracking, activity logging, and multi-user board access. These mechanisms ensure that autonomous agent work remains under human control with clear audit trails and cost containment.

## Approval System

### Approvals Table

```typescript
approvals: pgTable("approvals", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  type: text (not null)
  requestedByAgentId: uuid (foreign key to agents)
  requestedByUserId: text
  status: text (not null, default "pending")
  payload: jsonb (not null)
  decisionNote: text
  decidedByUserId: text
  decidedAt: timestamp
  createdAt: timestamp
  updatedAt: timestamp
})
```

### Approval Comments

```typescript
approvalComments: pgTable("approval_comments", {
  id: uuid (primary key)
  approvalId: uuid (foreign key to approvals)
  authorUserId: text
  content: text
  createdAt: timestamp
})
```

### Approval Workflow

**Request Phase**
- Agent or user requests approval via `approvals` table
- `type` specifies approval type (e.g., "agent_hire", "budget_increase", "routine_create")
- `payload` contains approval-specific data
- `status` set to "pending"

**Review Phase**
- Board users review pending approvals
- Comments added via `approvalComments` table
- Discussion and clarification

**Decision Phase**
- Board user approves or rejects
- `status` updated to "approved" or "rejected"
- `decisionNote` records reasoning
- `decidedByUserId` tracks who decided
- `decidedAt` timestamps the decision

### Approval Types

Paperclip supports multiple approval types:
- Agent hiring and configuration changes
- Budget increases and policy changes
- Routine creation and modification
- Sensitive operations requiring board approval

### Indexes for Approval Queries

```typescript
companyStatusTypeIdx: index on (companyId, status, type)
```

This supports efficient queries for:
- Finding all pending approvals for a company
- Filtering by approval type
- Status-based filtering

## Budget System

### Budget Policies Table

```typescript
budgetPolicies: pgTable("budget_policies", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  scopeType: text (not null)
  scopeId: uuid (not null)
  metric: text (not null, default "billed_cents")
  windowKind: text (not null)
  amount: integer (not null, default 0)
  warnPercent: integer (not null, default 80)
  hardStopEnabled: boolean (not null, default true)
  notifyEnabled: boolean (not null, default true)
  isActive: boolean (not null, default true)
  createdByUserId: text
  updatedByUserId: text
  createdAt: timestamp
  updatedAt: timestamp
})
```

### Budget Incidents Table

```typescript
budgetIncidents: pgTable("budget_incidents", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  budgetPolicyId: uuid (foreign key to budget_policies)
  scopeType: text
  scopeId: uuid
  incidentKind: text
  metricValue: integer
  thresholdValue: integer
  resolvedAt: timestamp
  createdAt: timestamp
})
```

### Budget Policy Structure

**Scope**
- `scopeType`: What the budget applies to (e.g., "agent", "project", "company")
- `scopeId`: Specific entity ID within the scope type

**Metric**
- `metric`: What to measure (e.g., "billed_cents", "token_count", "request_count")
- `windowKind`: Time window (e.g., "monthly", "weekly", "daily")

**Limits**
- `amount`: Budget limit amount
- `warnPercent`: Warning threshold percentage (default 80%)
- `hardStopEnabled`: Whether hard stop is enabled (default true)
- `notifyEnabled`: Whether notifications are enabled (default true)

### Budget Enforcement

**Warning Phase**
- When spend reaches `warnPercent` of budget
- Notification sent to board users
- Agent continues working

**Hard Stop Phase**
- When spend reaches 100% of budget and `hardStopEnabled` is true
- Agent status set to "paused"
- `pauseReason` set to "budget_exceeded"
- Queued work for this agent is cancelled
- New work assignments are rejected

**Incident Tracking**
- Budget incidents recorded in `budgetIncidents` table
- Tracks when thresholds were crossed
- Records resolution timestamp

### Indexes for Budget Queries

```typescript
companyScopeActiveIdx: index on (companyId, scopeType, scopeId, isActive)
companyWindowIdx: index on (companyId, windowKind, metric)
companyScopeMetricUniqueIdx: uniqueIndex on (companyId, scopeType, scopeId, metric, windowKind)
```

These support efficient queries for:
- Finding active budget policies for a scope
- Budget calculations by time window
- Preventing duplicate budget policies

## Cost Tracking

### Cost Events Table

```typescript
costEvents: pgTable("cost_events", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  agentId: uuid (foreign key to agents)
  projectId: uuid (foreign key to projects)
  goalId: uuid (foreign key to goals)
  issueId: uuid (foreign key to issues)
  provider: text
  model: text
  metric: text
  amount: integer
  billedCents: integer
  createdAt: timestamp
})
```

### Finance Events Table

```typescript
financeEvents: pgTable("finance_events", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  eventType: text
  amount: integer
  currency: text
  description: text
  createdAt: timestamp
})
```

### Cost Tracking Model

Paperclip tracks costs at multiple levels:
- **Company**: Total company spend
- **Agent**: Per-agent spend (via `budgetMonthlyCents` and `spentMonthlyCents`)
- **Project**: Per-project spend
- **Goal**: Per-goal spend
- **Issue**: Per-issue spend
- **Provider**: Per-provider spend (e.g., Anthropic, OpenAI)
- **Model**: Per-model spend (e.g., Claude 3.5 Sonnet, GPT-4)

### Budget Per Agent

Each agent has budget fields:
- `budgetMonthlyCents`: Monthly budget limit
- `spentMonthlyCents`: Current monthly spend

When an agent exceeds its budget:
1. Agent status set to "paused"
2. `pauseReason` set to "budget_exceeded"
3. `pausedAt` timestamp set
4. Queued work cancelled
5. New assignments rejected

## Activity Logging

### Activity Log Table

```typescript
activityLog: pgTable("activity_log", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  actorType: text
  actorId: text
  action: text
  entityType: text
  entityId: uuid
  changes: jsonb
  metadata: jsonb
  createdAt: timestamp
})
```

### Activity Logging Model

Every mutating action is logged:
- **Actor**: Who performed the action (agent or user)
- **Action**: What was done (e.g., "issue_created", "agent_updated", "approval_granted")
- **Entity**: What was affected (e.g., "issue", "agent", "approval")
- **Changes**: What changed (before/after state)
- **Metadata**: Additional context

### Audit Trail

Activity log provides:
- Complete audit trail of all mutations
- Actor attribution for every change
- Change history for entities
- Debugging and compliance support

## Multi-User Board Access

### Board Users

Paperclip supports multiple human board users:
- Shared board access
- Company memberships
- Role-based permissions
- Sidebar preferences

### Company Memberships

```typescript
companyMemberships: pgTable("company_memberships", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  userId: text
  role: text
  state: text
  createdAt: timestamp
  updatedAt: timestamp
})
```

### Instance User Roles

```typescript
instanceUserRoles: pgTable("instance_user_roles", {
  id: uuid (primary key)
  userId: text
  role: text
  createdAt: timestamp
})
```

### Permission Model

**Instance-level roles**
- Admin: Full control over instance
- Board: Board access to companies
- User: Limited access

**Company-level roles**
- Owner: Full control over company
- Admin: Administrative access
- Member: Standard access
- Viewer: Read-only access

## Agent API Keys

### Agent API Keys Table

```typescript
agentApiKeys: pgTable("agent_api_keys", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  agentId: uuid (foreign key to agents)
  keyHash: text (not null)
  name: text
  lastUsedAt: timestamp
  expiresAt: timestamp
  createdAt: timestamp
})
```

### Agent Authentication

Agents authenticate via API keys:
- Keys are hashed at rest
- Company-scoped (cannot access other companies)
- Tracked in activity log
- Can be revoked

### Board API Keys

```typescript
boardApiKeys: pgTable("board_api_keys", {
  id: uuid (primary key)
  userId: text
  keyHash: text (not null)
  name: text
  lastUsedAt: timestamp
  expiresAt: timestamp
  createdAt: timestamp
})
```

## Comparison with CKOS Study Layer 13

### CKOS Concepts (Study Layer 13)
- Founder approval batch control
- ROI-aware tasks, notes, and questions
- Intelligent question system
- Briefing-to-tasks transformation

### Paperclip Model
- Approval workflows with typed approvals
- Budget policies with hard stops
- Cost tracking at multiple levels
- Activity logging for all mutations
- Multi-user board access with roles
- Agent API keys for authentication

### Key Differences

| Aspect | Paperclip | CKOS (Study Layer 13) |
|--------|-----------|----------------------|
| Approvals | Typed approval workflows with comments | Founder approval batch control |
| Budget | Per-agent monthly budgets with hard stops | ROI-aware tasks and questions |
| Cost tracking | Multi-level cost tracking (company, agent, project, goal, issue) | Not specified |
| Audit trail | Activity log for all mutations | Not specified |
| Multi-user | Multi-user board access with roles | Not specified |
| Authentication | Agent API keys hashed at rest | Not specified |

## Adoption Candidates for CKOS

### Strong Candidates

1. **Approval workflows**: Typed approvals with request/review/decision phases
2. **Budget policies with hard stops**: Prevent runaway costs
3. **Cost tracking at multiple levels**: Company, agent, project, goal, issue
4. **Activity logging**: Complete audit trail for all mutations
5. **Multi-user board access**: Shared access with role-based permissions
6. **Agent API keys**: Hashed at rest, company-scoped authentication

### Moderate Candidates

1. **Budget incidents table**: Track when thresholds were crossed
2. **Approval comments**: Discussion and clarification during review
3. **Company memberships**: Track user access to companies
4. **Instance user roles**: Instance-level permission model
5. **Budget warning thresholds**: Notify before hard stop

### Weak Candidates

1. **Finance events table**: May not align with CKOS's ROI model
2. **Budget per agent**: CKOS may prefer ROI-aware task budgets instead
3. **Hard stop enabled flag**: May be too rigid for CKOS's needs

## Risks and Considerations

### Risks

1. **Complexity**: Approval and budget systems add significant complexity
2. **Over-engineering**: CKOS may not need all of Paperclip's governance features
3. **Rigidity**: Hard stops may be too rigid for some use cases
4. **Operational overhead**: Multi-user access and role management add complexity

### Considerations

1. **CKOS scope**: Does CKOS need multi-user access or is it single-user?
2. **Budget model**: Should CKOS use per-agent budgets or ROI-aware task budgets?
3. **Approval needs**: Does CKOS need typed approval workflows or simpler approval?
4. **Audit requirements**: What level of audit trail does CKOS need?

## Open Questions for PMO

1. Should future CKOS canon evaluate typed approval workflows like Paperclip?
2. Should CKOS use per-agent budgets with hard stops or ROI-aware task budgets?
3. Should future CKOS canon evaluate multi-level cost tracking?
4. Should future CKOS canon evaluate activity logging for all mutations?
5. Should CKOS support multi-user board access with roles?
6. Should CKOS use agent API keys for authentication?
7. What is CKOS's target governance model: lightweight or comprehensive?

## CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: Codex — Paperclip Benchmarking
mode: study-only
files_created:
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/04_PAPERCLIP_GOVERNANCE_APPROVALS_AND_BUDGETS_STUDY.md
files_changed:
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/ck_memory.md (to be updated)
files_not_touched:
  - docs 01-26
  - docs 27-34
  - 00_SYSTEM_GOVERNANCE/*
  - ARCHITECTURE_PATCH_REPORT.md
  - backend/UI/API/banco/migrations
  - JSONs n8n
  - agentes reais
  - automações runtime
validation:
  - Paperclip approval system analyzed
  - Budget policies and enforcement documented
  - Cost tracking model documented
  - Activity logging documented
  - Multi-user board access documented
  - Agent API keys documented
  - Comparison with CKOS Study Layer 13 completed
  - Adoption candidates identified
risks_remaining:
  - Approval and budget systems add significant complexity
  - CKOS governance model not yet defined
  - Multi-user needs not yet defined
next_step:
  - Create note 05: CKOS Differentiation from Paperclip Study
status: released_as_study_note_only
```
