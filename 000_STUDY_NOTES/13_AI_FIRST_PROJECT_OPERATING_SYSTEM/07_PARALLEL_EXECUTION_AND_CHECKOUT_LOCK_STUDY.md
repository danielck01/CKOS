---
title: Parallel Execution And Checkout Lock Study
file: 07_PARALLEL_EXECUTION_AND_CHECKOUT_LOCK_STUDY.md
layer: study
phase: 000_STUDY_NOTES
category: parallel_execution_checkout_lock
status: draft
version: 0.1.0
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
  - metacognik
confidence: unverified
provenance_status: unverified
source_tool: codex
purpose: Study how parallel Codex, Claude, Antigravity and PMO sessions can coordinate without file conflicts or authority drift.
inputs:
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
outputs:
  - parallel execution rules
  - checkout lock study model
framework:
  - one writer
  - one auditor
  - lock before write
  - release after write
edge_cases:
  - two sessions write same file
  - auditor edits while auditing
  - design study becomes implementation
integrations:
  - SESSION_REGISTRY.md
  - future task orchestration
prompts:
  - Declare allowed and forbidden scope before writing.
metrics:
  - zero overlapping active write locks
related_notes:
  - ck_tasks.md
tags:
  - checkout_lock
  - parallel_sessions
  - study
---

# Parallel Execution And Checkout Lock

## Core Rules

```txt
one_writer_one_auditor
no_parallel_write_same_file
session_registry_required
checkout_lock_required
checkout_release_required
handoff_required_when_context_changes
audit_before_next_gate
```

## Session Modes

| Mode | Study meaning |
|---|---|
| `planner_session` | Scope, risks, cost and sequence. |
| `executor_session` | Writes only locked files. |
| `auditor_session` | Reads and reports findings; does not edit. |
| `design_study_session` | Studies visual/product direction only. |
| `research_session` | Gathers evidence; does not canonize. |
| `canonical_patch_session` | Separate approved canonical checkout only. |
| `memory_refresh_session` | Updates maps and memory only. |

## Lock Candidate Fields

```yaml
task_id:
session_id:
session_type:
agent:
allowed_scope:
forbidden_scope:
expected_outputs:
estimated_cost:
intelligence_level:
approval_basis:
release_required:
```

## Candidate For Doc 27

Doc 27 should make checkout locks part of task orchestration. Parallel AI work without locks is not CKOS-grade execution.
