---
title: Founder Approval Batch Control Study
file: 08_FOUNDER_APPROVAL_BATCH_CONTROL_STUDY.md
layer: study
phase: 000_STUDY_NOTES
category: founder_approval_batch_control
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
purpose: Study how Founder can approve controlled batches of AI-first work without losing risk, cost or governance visibility.
inputs:
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
outputs:
  - batch approval modes
  - risk and cost boundaries
framework:
  - batch proposal -> limits -> approval -> execution window -> release
edge_cases:
  - batch approval hides high-risk task
  - cost limit exceeded mid-batch
integrations:
  - approval_gate
  - cost_guard
  - SESSION_REGISTRY.md
prompts:
  - Approve a batch only when risk, scope, cost and rollback boundaries are explicit.
metrics:
  - fewer interruptions
  - no hidden high-risk tasks
related_notes:
  - 05_TASK_AI_FIRST_SYSTEM_STUDY.md
tags:
  - approval
  - founder
  - batch_control
---

# Founder Approval Batch Control

## Purpose

Founder should be able to approve meaningful work without approving every small action manually, while still preserving governance.

## Candidate Modes

```txt
approve_one_task
approve_next_3_tasks
approve_next_5_tasks
approve_next_10_tasks
approve_batch_with_cost_limit
approve_batch_with_risk_limit
approve_only_study
approve_only_memory_update
reject_and_request_replan
```

## Batch Guardrails

| Guardrail | Required |
|---|---|
| Scope | Allowed and forbidden files/actions declared. |
| Risk ceiling | Batch stops if a task exceeds approved risk. |
| Cost ceiling | Batch stops or asks again if cost estimate is exceeded. |
| Approval expiry | Approval is time-bound or session-bound. |
| Audit trail | Every task in the batch points to the batch approval. |
| Release | Batch closes with checkout release and memory update. |

## Candidate For Doc 27

Doc 27 should include batch approval as a task orchestration primitive, not as a UI convenience. Batch approval never bypasses risk, cost or policy.
