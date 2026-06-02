---
title: Paperclip Work Task And Ticket System Study
file: 03_PAPERCLIP_WORK_TASK_AND_TICKET_SYSTEM_STUDY.md
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
purpose: Study Paperclip issue, task, ticket and workspace patterns as non-authoritative future CKOS reference material.
---

# 03_PAPERCLIP_WORK_TASK_AND_TICKET_SYSTEM_STUDY.md

**Study Layer**: 14_PAPERCLIP_AGENT_OPERATING_MODEL  
**Note**: 03  
**Status**: Study-only, non-canonical  
**Created**: 2026-06-01  
**Purpose**: Analyze Paperclip's issue model, work tracking, and ticket system

## Non-Authority Boundary

This file is study-only, draft and unverified. It is not canonical.

It does not authorize Doc 27. It does not create Doc 27. It does not authorize backend, UI, API, database, migrations, real agents, runtime automations, n8n JSONs, MCP servers, webhooks or production schemas.

It may coordinate future sessions as a non-canonical operating note. It may not override `SESSION_REGISTRY.md`, `MULTI_SESSION_EXECUTION_POLICY.md`, canonical docs, Founder approval or PMO/Metacognik audit.

## Overview

Paperclip's work and task system is built around a rich issue model that supports goal hierarchy, parent/sub-issue structure, blocker dependencies, execution policies, workspace isolation, and full audit trails. Issues carry company/project/goal context, support both agent and human assignees, and include sophisticated execution semantics.

## Issue Schema Analysis

### Core Issue Table (`issues`)

```typescript
{
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  projectId: uuid (foreign key to projects)
  projectWorkspaceId: uuid (foreign key to project_workspaces)
  goalId: uuid (foreign key to goals)
  parentId: uuid (foreign key to issues.id - self-reference)
  title: text (not null)
  description: text
  status: text (not null, default "backlog")
  workMode: text (not null, default "standard")
  priority: text (not null, default "medium")
  assigneeAgentId: uuid (foreign key to agents)
  assigneeUserId: text
  checkoutRunId: uuid (foreign key to heartbeat_runs)
  executionRunId: uuid (foreign key to heartbeat_runs)
  executionAgentNameKey: text
  executionLockedAt: timestamp
  createdByAgentId: uuid (foreign key to agents)
  createdByUserId: text
  issueNumber: integer
  identifier: text
  originKind: text (not null, default "manual")
  originId: text
  originRunId: text
  originFingerprint: text (not null, default "default")
  requestDepth: integer (not null, default 0)
  billingCode: text
  assigneeAdapterOverrides: jsonb
  executionPolicy: jsonb
  executionState: jsonb
  monitorNextCheckAt: timestamp
  monitorWakeRequestedAt: timestamp
  monitorLastTriggeredAt: timestamp
  monitorAttemptCount: integer (not null, default 0)
  monitorNotes: text
  monitorScheduledBy: text
  executionWorkspaceId: uuid (foreign key to execution_workspaces)
  executionWorkspacePreference: text
  executionWorkspaceSettings: jsonb
  startedAt: timestamp
  completedAt: timestamp
  cancelledAt: timestamp
  hiddenAt: timestamp
  createdAt: timestamp
  updatedAt: timestamp
}
```

### Key Fields Explained

**Context and Hierarchy**
- `companyId`: Company scope (all issues are company-scoped)
- `projectId`: Project membership
- `projectWorkspaceId`: Project workspace context
- `goalId`: Goal hierarchy membership
- `parentId`: Parent issue for work breakdown structure

**Identity and Tracking**
- `title`: Issue title
- `description`: Issue description
- `status`: Current status (backlog, todo, in_progress, blocked, in_review, done, cancelled)
- `workMode`: Work mode (standard, etc.)
- `priority`: Priority level (low, medium, high)
- `issueNumber`: Sequential issue number within company
- `identifier`: Human-readable identifier (e.g., "COMP-123")

**Assignment and Execution**
- `assigneeAgentId`: Agent assignee
- `assigneeUserId`: Human assignee
- `checkoutRunId`: Current checkout lock
- `executionRunId`: Current live execution
- `executionAgentNameKey`: Execution agent name key
- `executionLockedAt`: When execution was locked

**Origin and Provenance**
- `originKind`: Origin type (manual, routine_execution, harness_liveness_escalation, etc.)
- `originId`: Origin identifier
- `originRunId`: Origin run identifier
- `originFingerprint`: Origin fingerprint for deduplication
- `requestDepth`: Depth of nested requests
- `createdByAgentId`: Agent that created the issue
- `createdByUserId`: Human that created the issue

**Execution Policy and State**
- `executionPolicy`: JSONB field for execution rules
- `executionState`: JSONB field for runtime state
- `assigneeAdapterOverrides`: Adapter-specific overrides

**Monitor Support**
- `monitorNextCheckAt`: When monitor should fire
- `monitorWakeRequestedAt`: When monitor wake was requested
- `monitorLastTriggeredAt`: When monitor last fired
- `monitorAttemptCount`: Number of monitor attempts
- `monitorNotes`: Non-secret monitor instructions
- `monitorScheduledBy`: Who scheduled the monitor

**Workspace Isolation**
- `executionWorkspaceId`: Execution workspace context
- `executionWorkspacePreference`: Preferred workspace type
- `executionWorkspaceSettings`: Workspace-specific settings

**Lifecycle**
- `startedAt`: When work started
- `completedAt`: When work completed
- `cancelledAt`: When work was cancelled
- `hiddenAt`: When issue was hidden (soft delete)

## Goal Hierarchy

Paperclip implements a goal hierarchy: company → team → agent → task

**Goal Tables**
- `projectGoals`: Project-level goals
- `goals`: General goals table

**Issue-Goal Relationship**
- `goalId` field links issue to a goal
- Goals provide the "why" for the work
- Agents see full goal ancestry in their context

This ensures goal alignment: every task traces back to the company mission. Agents know what to do and why.

## Parent/Sub-Issue Structure

### Structural Hierarchy

Parent/sub-issue relationships are structural, not dependency-based:

**Use parent/sub-issues for:**
- Work breakdown
- Rollup context
- Explaining why a child issue exists
- Waking the parent assignee when all direct children become terminal

**Do not treat `parentId` as execution dependency by itself**

### Self-Reference

The `parentId` field is a self-reference to `issues.id`, enabling arbitrary nesting depth.

### Indexes for Parent/Child Queries

```typescript
parentIdx: index on (companyId, parentId)
```

This index supports efficient queries for:
- Finding all children of a parent
- Traversing the issue tree
- Rollup calculations

## Blocker Dependencies

### Dependency Semantics

Blocker relationships (`blockedByIssueIds`) are separate from parent/sub-issue structure:

**Use blockers for:**
- "This issue cannot continue until that issue changes state"
- Explicit waiting relationships
- Automatic wakeups when all blockers resolve

**Blocked issues should stay idle while blockers remain unresolved**

### Blocker Table

```typescript
issueRelations: pgTable("issue_relations", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  sourceIssueId: uuid (foreign key to issues)
  targetIssueId: uuid (foreign key to issues)
  relationType: text (e.g., "blocks")
  createdAt: timestamp
})
```

### Automatic Wakeups

When all blockers resolve:
- Paperclip queues an `issue_blockers_resolved` wake
- The blocked issue can proceed with real work
- No manual intervention required

## Execution Policy

### Policy Structure

`executionPolicy` is a JSONB field that contains execution rules:

```typescript
{
  participants?: Array<{
    participantType: "agent" | "user"
    participantId: string
    role: string
  }>
  monitor?: {
    nextCheckAt: timestamp
    notes: string
    serviceName?: string
    externalRef?: string
    timeoutAt?: timestamp
    maxAttempts?: number
    recoveryPolicy?: "wake_owner" | "create_recovery_issue" | "escalate_to_board"
  }
  // ... other policy fields
}
```

### Participant Model

Execution policies can specify participants for multi-step workflows:
- Review participants
- Approval participants
- Handoff participants

### Monitor Policy

Monitor policy configures one-shot deferred actions for async checks (detailed in note 02).

## Execution State

### State Structure

`executionState` is a JSONB field that contains runtime state:

```typescript
{
  currentParticipant?: {
    participantType: "agent" | "user"
    participantId: string
    role: string
  }
  // ... other state fields
}
```

### Current Participant

The `currentParticipant` field tracks who currently owns the next move in a multi-step workflow.

## Workspace Isolation

### Project Workspaces

- `projectWorkspaceId`: Links issue to a project workspace
- Project workspaces provide project-specific context
- Git worktrees, operator branches, etc.

### Execution Workspaces

- `executionWorkspaceId`: Links issue to an execution workspace
- Execution workspaces are isolated execution environments
- Git worktrees, sandbox environments, etc.

### Workspace Preference

- `executionWorkspacePreference`: Preferred workspace type
- `executionWorkspaceSettings`: Workspace-specific configuration

## Origin Tracking

### Origin Kind

`originKind` tracks how the issue was created:
- `manual`: Manual creation via UI or API
- `routine_execution`: Created by a scheduled routine
- `harness_liveness_escalation`: Created by liveness recovery
- `stale_active_run_evaluation`: Created by watchdog
- `issue_productivity_review`: Created by productivity review
- `stranded_issue_recovery`: Created by stranded work recovery

### Origin Fingerprint

`originFingerprint` provides deduplication:
- Prevents duplicate issue creation
- Used for exact-once guarantees (e.g., accepted-plan decomposition)

### Unique Indexes for Origin Deduplication

```typescript
openRoutineExecutionIdx: uniqueIndex on (companyId, originKind, originId, originFingerprint)
  where originKind = 'routine_execution' and hiddenAt is null and executionRunId is not null and status in ('backlog', 'todo', 'in_progress', 'in_review', 'blocked')
```

This ensures only one open routine execution issue exists per routine run.

## Issue-Related Tables

### Comments

```typescript
issueComments: pgTable("issue_comments", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  issueId: uuid (foreign key to issues)
  authorAgentId: uuid (foreign key to agents)
  authorUserId: text
  content: text
  createdAt: timestamp
  updatedAt: timestamp
})
```

### Documents

```typescript
documents: pgTable("documents", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  title: text
  content: text
  // ... other fields
})

documentRevisions: pgTable("document_revisions", {
  id: uuid (primary key)
  documentId: uuid (foreign key to documents)
  revision: integer
  content: text
  createdAt: timestamp
})

issueDocuments: pgTable("issue_documents", {
  id: uuid (primary key)
  issueId: uuid (foreign key to issues)
  documentId: uuid (foreign key to documents)
  // ... other fields
})
```

### Work Products

```typescript
issueWorkProducts: pgTable("issue_work_products", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  issueId: uuid (foreign key to issues)
  kind: text
  title: text
  description: text
  artifactUrl: text
  // ... other fields
})
```

### Attachments

```typescript
issueAttachments: pgTable("issue_attachments", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  issueId: uuid (foreign key to issues)
  filename: text
  storageKey: text
  mimeType: text
  size: integer
  // ... other fields
})
```

### Labels

```typescript
labels: pgTable("labels", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  name: text
  color: text
  // ... other fields
})

issueLabels: pgTable("issue_labels", {
  id: uuid (primary key)
  issueId: uuid (foreign key to issues)
  labelId: uuid (foreign key to labels)
})
```

## Issue Reference Mentions

Paperclip tracks cross-issue references for context and navigation:

```typescript
issueReferenceMentions: pgTable("issue_reference_mentions", {
  id: uuid (primary key)
  companyId: uuid (foreign key to companies)
  sourceIssueId: uuid (foreign key to issues)
  targetIssueId: uuid (foreign key to issues)
  mentionKind: text
  createdAt: timestamp
})
```

This enables:
- Finding all issues that reference a given issue
- Tracing dependency chains
- Context-aware navigation

## Comparison with CKOS Study Layer 13

### CKOS Concepts (Study Layer 13)
- Briefing-to-tasks transformation
- Notes as operational memory
- Task AI-first system
- Superagent/agent/subagent work allocation
- ROI-aware tasks, notes, and questions

### Paperclip Model
- Rich issue model with goal hierarchy
- Parent/sub-issue structure for work breakdown
- Blocker dependencies for explicit waiting
- Execution policy and state for multi-step workflows
- Workspace isolation for execution environments
- Full audit trail with comments, documents, work products

### Key Differences

| Aspect | Paperclip | CKOS (Study Layer 13) |
|--------|-----------|----------------------|
| Work unit | Issue with rich metadata | Task (less specified) |
| Hierarchy | Goal hierarchy + parent/sub-issues | Superagent/agent/subagent |
| Dependencies | Explicit blocker relationships | Not specified |
| Execution | Execution policy and state | Not specified |
| Workspace | Project and execution workspaces | Not specified |
| Audit trail | Comments, documents, work products, attachments | Notes as memory |

## Adoption Candidates for CKOS

### Strong Candidates

1. **Goal hierarchy**: Company → team → agent → task ensures goal alignment
2. **Parent/sub-issue structure**: Clear work breakdown and rollup context
3. **Blocker dependencies**: Explicit waiting relationships with automatic wakeups
4. **Execution policy**: JSONB field for execution rules and multi-step workflows
5. **Execution state**: JSONB field for runtime state and current participant tracking
6. **Workspace isolation**: Separate project and execution workspaces
7. **Issue reference mentions**: Cross-issue tracking for context and navigation
8. **Company-scoped issues**: Complete data isolation

### Moderate Candidates

1. **Origin tracking**: Origin kind, origin ID, origin fingerprint for provenance
2. **Unique indexes for deduplication**: Prevent duplicate issue creation
3. **Comments**: Threaded comments for discussion
4. **Documents with revisions**: Versioned documents linked to issues
5. **Work products**: First-class outputs linked to issues
6. **Attachments**: File attachments linked to issues
7. **Labels**: Tagging system for organization

### Weak Candidates

1. **Issue number**: Sequential numbering may not align with CKOS needs
2. **Identifier**: Human-readable identifiers may not be needed
3. **Billing code**: May not align with CKOS's ROI model
4. **Assignee adapter overrides**: May be too specific to Paperclip's adapter model

## Risks and Considerations

### Risks

1. **Complexity**: Paperclip's issue model is very rich and complex
2. **Over-engineering**: CKOS may not need all of Paperclip's features
3. **Schema bloat**: Many tables and fields add complexity
4. **Migration overhead**: Rich schema requires careful migration planning

### Considerations

1. **CKOS scope**: Does CKOS need a full issue tracking system or a simpler task model?
2. **Goal hierarchy**: Does CKOS need company-level goals or project-level goals?
3. **Workspace isolation**: Does CKOS need sophisticated workspace management?
4. **Audit trail**: Does CKOS need full audit trail or simpler tracking?

## Open Questions for PMO

1. Should CKOS adopt Paperclip's rich issue model or use a simpler task model?
2. Should future CKOS canon evaluate goal hierarchy like Paperclip?
3. Should CKOS use parent/sub-issue structure for work breakdown?
4. Should future CKOS canon evaluate blocker dependencies with automatic wakeups?
5. Should CKOS use execution policy and state fields?
6. Should future CKOS canon evaluate workspace isolation?
7. What level of audit trail does CKOS need?

## CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: Codex — Paperclip Benchmarking
mode: study-only
files_created:
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/03_PAPERCLIP_WORK_TASK_AND_TICKET_SYSTEM_STUDY.md
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
  - Paperclip issue schema analyzed
  - Goal hierarchy documented
  - Parent/sub-issue structure documented
  - Blocker dependencies documented
  - Execution policy and state documented
  - Workspace isolation documented
  - Issue-related tables documented
  - Comparison with CKOS Study Layer 13 completed
  - Adoption candidates identified
risks_remaining:
  - Paperclip issue model is very rich and complex
  - CKOS scope not yet defined (full issue tracking vs simpler task model)
  - Workspace needs not yet defined
next_step:
  - Create note 04: Paperclip Governance, Approvals and Budgets Study
status: released_as_study_note_only
```
