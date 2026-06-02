---
title: Paperclip Org Chart And Agent Model Study
file: 01_PAPERCLIP_ORG_CHART_AND_AGENT_MODEL_STUDY.md
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
purpose: Study Paperclip agent registry and org chart patterns as non-authoritative future CKOS reference material.
---

# 01_PAPERCLIP_ORG_CHART_AND_AGENT_MODEL_STUDY.md

**Study Layer**: 14_PAPERCLIP_AGENT_OPERATING_MODEL  
**Note**: 01  
**Status**: Study-only, non-canonical  
**Created**: 2026-06-01  
**Purpose**: Analyze Paperclip's agent registry, org chart model, and agent lifecycle

## Non-Authority Boundary

This file is study-only, draft and unverified. It is not canonical.

It does not authorize Doc 27. It does not create Doc 27. It does not authorize backend, UI, API, database, migrations, real agents, runtime automations, n8n JSONs, MCP servers, webhooks or production schemas.

It may coordinate future sessions as a non-canonical operating note. It may not override `SESSION_REGISTRY.md`, `MULTI_SESSION_EXECUTION_POLICY.md`, canonical docs, Founder approval or PMO/Metacognik audit.

## Overview

Paperclip models agents as employees in a company with hierarchical org charts, roles, titles, reporting lines, and budgets. The agent model is company-scoped, supports multiple adapter types, and includes runtime configuration for different execution environments.

## Agent Schema Analysis

### Core Agent Table (`agents`)

```typescript
{
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  name: text (not null)
  role: text (not null, default "general")
  title: text
  icon: text
  status: text (not null, default "idle")
  reportsTo: uuid (foreign key to agents.id - self-reference)
  capabilities: text
  adapterType: text (not null, default "process")
  adapterConfig: jsonb (not null, default {})
  runtimeConfig: jsonb (not null, default {})
  defaultEnvironmentId: uuid (foreign key to environments)
  budgetMonthlyCents: integer (not null, default 0)
  spentMonthlyCents: integer (not null, default 0)
  pauseReason: text
  pausedAt: timestamp
  permissions: jsonb (not null, default {})
  lastHeartbeatAt: timestamp
  metadata: jsonb
  createdAt: timestamp
  updatedAt: timestamp
}
```

### Key Fields Explained

**Identity and Organization**
- `name`: Agent name (e.g., "Claude Code", "Codex", "Cursor")
- `role`: Functional role (e.g., "general", "engineer", "designer", "marketer")
- `title`: Job title (e.g., "Senior Engineer", "CTO", "CEO")
- `icon`: Visual icon for UI
- `status`: Current status (idle, active, paused, terminated)
- `reportsTo`: Hierarchical reporting line (self-reference to agents.id)

**Adapter and Runtime**
- `adapterType`: How the agent is invoked (process, http, openclaw, claude-local, codex-local, cursor-local, etc.)
- `adapterConfig`: Adapter-specific configuration (API keys, model settings, etc.)
- `runtimeConfig`: Runtime environment configuration
- `defaultEnvironmentId`: Default execution environment

**Budget and Control**
- `budgetMonthlyCents`: Monthly budget in cents
- `spentMonthlyCents`: Current monthly spend in cents
- `pauseReason`: Reason for pause (budget exceeded, manual, etc.)
- `pausedAt`: When the agent was paused
- `permissions`: Permission grants

**Liveness**
- `lastHeartbeatAt`: Last successful heartbeat timestamp

## Org Chart Model

### Hierarchical Structure

Paperclip uses a self-referential `reportsTo` field to create hierarchical org charts:

```
CEO (reportsTo: null)
├── CTO (reportsTo: CEO.id)
│   ├── Senior Engineer 1 (reportsTo: CTO.id)
│   └── Senior Engineer 2 (reportsTo: CTO.id)
└── CMO (reportsTo: CEO.id)
    └── Marketing Lead (reportsTo: CMO.id)
```

### Indexes for Org Chart Queries

```typescript
companyReportsToIdx: index on (companyId, reportsTo)
```

This index supports efficient queries for:
- Finding all direct reports of a manager
- Traversing up the reporting chain
- Org chart visualization

### Company Scoping

All agents are company-scoped via `companyId`. This ensures:
- Complete data isolation between companies
- One deployment can run multiple companies
- Org charts are per-company, not global

## Adapter Types

### Built-in Adapters

Paperclip supports multiple adapter types out of the box:

**Local CLI/Session Adapters**
- `claude-local`: Claude Code
- `codex-local`: Codex
- `cursor-local`: Cursor
- `cursor-cloud`: Cursor Cloud
- `gemini-local`: Gemini
- `grok-local`: Grok
- `opencode-local`: OpenCode
- `pi-local`: Pi
- `hermes-local`: Hermes (fork-specific)
- `acpx-local`: ACPX

**HTTP/Process Adapters**
- `http`: HTTP webhook/API integrations
- `process`: Command-line process execution

**Gateway Adapters**
- `openclaw-gateway`: OpenClaw-style remote agents

### External Adapter Plugins

Paperclip supports dynamically loaded external adapters via the plugin system:
- Adapters can be installed as npm packages
- Loaded via `~/.paperclip/adapter-plugins.json`
- Zero hardcoded adapter imports in plugin-loader
- Built-in UI adapters can shadow external plugin parsers

### Adapter Configuration

Each agent has `adapterConfig` (JSONB) for adapter-specific settings:
- API keys
- Model selection
- Provider settings
- Custom parameters

## Agent Lifecycle

### Creation

Agents are created via board user or agent actions:
- Manual creation via UI
- Programmatic creation via API
- Agent-to-agent delegation (if permissions allow)

### Status Transitions

**idle** → **active**: Agent assigned work or woken for heartbeat
**active** → **idle**: Agent completes work or idle timeout
**active** → **paused**: Manual pause, budget exceeded, or governance action
**paused** → **active**: Manual resume or budget reset
**any** → **terminated**: Permanent termination

### Budget Enforcement

When an agent exceeds its monthly budget:
1. `spentMonthlyCents` reaches `budgetMonthlyCents`
2. Agent status set to `paused`
3. `pauseReason` set to `"budget_exceeded"`
4. `pausedAt` timestamp set
5. Queued work for this agent is cancelled
6. New work assignments are rejected

### Heartbeat Monitoring

- `lastHeartbeatAt` updated on successful heartbeat
- Watchdog monitors for stale agents
- Recovery actions created for silent agents
- Operators can snooze, continue, or dismiss watchdog signals

## Agent Permissions

### Permission Model

Permissions are stored in `permissions` (JSONB) field:
- Granular permission grants
- Company-scoped
- Can be customized per agent

### Permission Grants Table

Separate `principalPermissionGrants` table tracks:
- Principal type (agent or user)
- Principal ID
- Permission type
- Resource scope
- Grant status

## Comparison with CKOS Study Layer 13

### CKOS Concepts (Study Layer 13)
- Superagent/agent/subagent work allocation
- Task AI-first system
- Intelligent question system
- Briefing-to-tasks transformation

### Paperclip Model
- Hierarchical org chart with reporting lines
- Single-assignee task model
- Adapter-based execution
- Budget per agent
- Company-scoped multi-tenancy

### Key Differences

| Aspect | Paperclip | CKOS (Study Layer 13) |
|--------|-----------|----------------------|
| Structure | Hierarchical org chart | Superagent/agent/subagent allocation |
| Focus | Autonomous AI companies | AI-first project operating system |
| Budget | Per-agent monthly budgets | ROI-aware tasks and questions |
| Execution | Adapter-based heartbeats | Briefing-to-tasks transformation |
| Multi-tenancy | Multi-company isolation | Not specified |

## Adoption Candidates for CKOS

### Strong Candidates

1. **Company-scoped agents**: Complete data isolation is valuable for multi-tenant deployments
2. **Adapter-based execution**: "If it can receive a heartbeat, it's hired" is a flexible model
3. **Budget per agent**: Monthly budget tracking prevents runaway costs
4. **Hierarchical reporting lines**: Clear org structure for agent coordination
5. **Last heartbeat tracking**: Liveness monitoring is essential for autonomous systems

### Moderate Candidates

1. **Role/title distinction**: Separates functional role from job title
2. **Status lifecycle**: Clear status transitions (idle, active, paused, terminated)
3. **Pause reason tracking**: Audit trail for why agents were paused
4. **Runtime configuration**: Separates adapter config from runtime config

### Weak Candidates

1. **Self-referential org chart**: CKOS may prefer superagent/agent/subagent model
2. **Built-in adapter types**: CKOS may want a more generic adapter interface
3. **Permissions JSONB**: May prefer a more structured permission model

## Risks and Considerations

### Risks

1. **Org chart complexity**: Hierarchical structures can become complex in large organizations
2. **Budget granularity**: Per-agent budgets may not align with CKOS's ROI-aware model
3. **Adapter lock-in**: Built-in adapters may limit flexibility
4. **Company scoping overhead**: Multi-company isolation adds complexity

### Considerations

1. **CKOS scope**: Is CKOS targeting project operating systems or autonomous companies?
2. **Agent model**: Should CKOS use hierarchical org charts or superagent/agent/subagent?
3. **Budget model**: Should CKOS adopt per-agent budgets or ROI-aware task budgets?
4. **Adapter strategy**: Should CKOS support many built-in adapters or a generic interface?

## Open Questions for PMO

1. Should CKOS adopt Paperclip's hierarchical org chart model?
2. Should future CKOS canon evaluate per-agent budget tracking like Paperclip?
3. Should CKOS support multi-company isolation?
4. Should CKOS adopt Paperclip's adapter-based execution model?
5. What is CKOS's target scope: project operating system or autonomous company control plane?

## CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: Codex — Paperclip Benchmarking
mode: study-only
files_created:
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/01_PAPERCLIP_ORG_CHART_AND_AGENT_MODEL_STUDY.md
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
  - Paperclip agent schema analyzed
  - Org chart model documented
  - Adapter types cataloged
  - Lifecycle model documented
  - Comparison with CKOS Study Layer 13 completed
  - Adoption candidates identified
risks_remaining:
  - CKOS scope not yet defined (project OS vs autonomous company)
  - Agent model decision pending (hierarchical vs superagent/agent/subagent)
  - Budget model decision pending (per-agent vs ROI-aware)
next_step:
  - Create note 02: Paperclip Heartbeat Execution Study
status: released_as_study_note_only
```
