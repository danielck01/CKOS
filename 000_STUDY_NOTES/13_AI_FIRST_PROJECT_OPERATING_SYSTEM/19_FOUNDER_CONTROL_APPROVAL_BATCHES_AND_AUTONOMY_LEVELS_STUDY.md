---
title: Founder Control Approval Batches And Autonomy Levels Study
file: 19_FOUNDER_CONTROL_APPROVAL_BATCHES_AND_AUTONOMY_LEVELS_STUDY.md
layer: study
phase: 000_STUDY_NOTES
category: founder_control_approval_batches_autonomy_levels
version: 0.1.0
status: draft
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers: [founder, metacognik, pmo_ckos]
approval_required: [founder]
confidence: unverified
provenance_status: unverified
source_tool: codex
related_notes:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/08_FOUNDER_APPROVAL_BATCH_CONTROL_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/16_SMART_QUESTIONS_AND_CONTEXTUAL_INTERVENTION_STUDY.md
  - 01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md
tags: [study, founder_control, approval_batches, autonomy_levels, doc27_candidate]
---

# Founder Control Approval Batches And Autonomy Levels Study

## Non-Authority Boundary

This note is study-only. It does not change CKOS autonomy policy, does not create real agents, does not start runtime automation, and does not authorize implementation or canonical changes.

## 1. Proposito

Study how Founder can control AI-first work at the right level: not approving every tiny action, and not granting blind autonomy.

The purpose is to prepare future Doc 27 candidates for approval batches, Work Order control and autonomy boundaries.

## 2. Problema que resolve

CKOS needs speed without losing Founder control.

This note addresses:

- too many approval interruptions;
- vague "go ahead" approvals;
- batch approvals that hide risk;
- agent autonomy rising without explicit decision;
- parallel sessions proceeding beyond approved scope;
- completion claimed without release evidence.

## 3. O que e

It is a study model for Founder control through explicit approval envelopes.

Approval envelope:

**ESTUDO APENAS — schema conceitual, não DDL, não runtime, não migração, não contrato de API.**

```yaml
approval_id:
approved_scope:
forbidden_scope:
included_tasks:
included_work_orders:
batch_size:
risk_ceiling:
cost_ceiling:
autonomy_level:
expires_at:
stop_conditions:
fan_in_audit_required:
release_required:
```

Nota inline: O campo `approval_id` neste Approval Envelope identifica a aprovação de Work Order/Batch Approval Envelope. Ele não redefine nem substitui o `approval_id` canônico do Doc 11, relacionado à tabela de approvals. Qualquer alinhamento real entre esses identificadores precisa ser resolvido em documentação canônica futura.

Aviso de identificadores de estudo: `approval_id`, `task_id`, `work_order_id`, `lock_id` e `release_id`, quando citados nesta camada, sao identificadores conceituais ou referencias operacionais de estudo. Eles nao criam tabela, campo, indice, RLS, migration, API ou schema canonico. Qualquer promocao real desses IDs depende de patch futuro e explicitamente aprovado em Doc 11.

This is a candidate pattern only.

## 4. O que nao e

It is not:

- a new approval policy;
- an autonomy upgrade;
- a runtime permission system;
- an agent execution protocol;
- a replacement for checkout lock;
- a way to skip Metacognik audit;
- a way to approve hidden implementation.

## 5. Relacao com intencao minima do Founder

Founder may say:

```txt
pode seguir com as proximas tarefas
```

CKOS should translate that into a bounded approval question:

```txt
Should this mean next 5 low-risk study tasks, one Work Order,
or a batch with explicit risk/cost ceiling?
```

Founder control is strongest when the system converts broad intent into a clear approval envelope.

## 6. Relacao com Cognik

Cognik supports Founder control by preparing the context needed for a clean approval decision.

Study responsibilities:

- summarize the next tasks;
- identify dependencies;
- identify duplicate or stale work;
- show missing context;
- connect tasks to briefing and memory;
- propose smallest safe approval batch.

Cognik should not infer approval from context.

## 7. Relacao com Metacognik

Metacognik audits whether approval is safe.

Study responsibilities:

- detect hidden high-risk tasks inside a batch;
- challenge vague approval language;
- require explicit stop conditions;
- detect autonomy creep;
- audit whether cost/risk ceilings are clear;
- block self-approval or post-hoc approval claims.

Metacognik should treat vague autonomy as a risk.

## 8. Relacao com briefing inteligente

Briefing should prepare Founder approval by making decisions explicit.

Briefing-to-approval flow:

```txt
intent
  -> briefing gaps
  -> smart questions
  -> task candidates
  -> Work Order proposal
  -> approval envelope
  -> execution only inside lock
```

If briefing is incomplete, approval should be limited to study or context-gathering.

## 9. Relacao com sistema de perguntas inteligentes

Smart questions should reduce approval load.

Approval question template:

```yaml
question:
approval_scope:
recommended_batch_size:
risk_ceiling:
cost_ceiling:
autonomy_level:
stop_conditions:
why_this_matters:
consequence_if_unanswered:
```

A good approval question gives Founder a real decision, not a vague yes/no.

## 10. Relacao com tasks, work orders e lotes paralelos

Founder approval can operate at several levels:

| Level | Use |
|---|---|
| task approval | high-risk or isolated atomic task |
| Work Order approval | coherent governed execution envelope for one or more tasks |
| next 5 tasks | small, low/medium risk work |
| next 10 tasks | low-risk or study-only work with stable scope |
| batch approval | multiple Work Orders under shared ceiling |

Rule: task = unidade atomica de trabalho. Work Order = envelope governado de execucao com scope, approval, lock, risk, ROI, context and release. Founder approval of tasks does not automatically approve a Work Order unless the envelope is explicit.

Parallel batches require:

- checkout lock;
- non-overlapping write scopes;
- risk/cost ceiling;
- fan-in audit;
- release note;
- stop on scope or autonomy drift.

## 11. Relacao com memoria curta, media e longa

Approval state should be memory-routed:

| Memory layer | Approval memory |
|---|---|
| short | active approval for current session, lock and stop conditions |
| medium | pending Work Orders, active batch, unresolved approvals |
| long | approved decisions, stable Founder preferences, final release records |

Vague approval should not become long memory. Only explicit, auditable approval should persist as a strong decision.

## 12. Relacao com RAG, notes e metadados

Approval decisions should be retrievable with clear metadata.

Candidate metadata:

```yaml
approval_ref:
approved_by:
scope:
risk_ceiling:
cost_ceiling:
autonomy_level:
related_tasks:
related_work_orders:
valid_until:
release_ref:
canonical_status:
confidence:
```

This is a future candidate only, not a canonical schema.

## 13. Relacao com ROI por task/projeto/decisao

Founder control has ROI when it reduces decision fatigue without increasing risk.

ROI dimensions:

- fewer interruptions;
- faster low-risk execution;
- clearer stop conditions;
- less rework from vague approval;
- better audit trail;
- safer autonomy;
- more precise cost control;
- better release confidence.

Every approval batch should state why batching is better than one-by-one approval.

## 14. Regras de approval e autonomia

Candidate autonomy levels for study only:

| Level | Meaning | Allowed in this study layer |
|---|---|---|
| L0 manual | ask before every action | yes, as concept |
| L1 assisted | ask before write or external effect | yes, as concept |
| L2 bounded batch | execute approved low-risk batch within lock | yes, as concept |
| L3 audited autonomy | proceed within broader policy and post-audit | candidate only, not authorized |
| L4 self-directed | agent chooses goals and executes | not authorized |

Approval rules:

- no autonomy increase without explicit Founder approval;
- no batch approval without risk/cost ceiling;
- no implementation inside study approval;
- no canonical change inside study approval;
- no agent self-approval;
- Metacognik audit required for risk escalation.

## 15. Antipadroes

- "Pode seguir" interpreted as unlimited approval.
- Next 10 tasks approved without seeing scope.
- Batch approval used to hide high-risk work.
- Autonomy level inferred from repeated approvals.
- Founder approval stored without expiry or context.
- Metacognik audit skipped because Founder is busy.
- Release omitted after batch completion.
- Study-only approval used for implementation.

## 16. Candidatos para futuro Doc 27

Candidate Doc 27 sections:

- Founder approval envelope.
- Next 5/10 task approval model.
- Work Order approval model.
- Batch risk/cost ceilings.
- Autonomy level boundaries for task orchestration.
- Stop conditions and expiry.
- Fan-in audit after approved batch.
- Approval memory and release traceability.

These are not canonical until approved in a future checkout.

## 17. Acceptance criteria

- Note remains study-only.
- No autonomy policy is changed.
- No real agent or automation is created.
- Founder approval remains explicit.
- Next 5/10 task approval includes risk/cost/scope limits.
- Metacognik audit is required for risk or autonomy escalation.
- RAG/metadata are candidate-only.
- No Doc 27 or docs 28-34 are created.

## 18. Related notes

- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/08_FOUNDER_APPROVAL_BATCH_CONTROL_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/16_SMART_QUESTIONS_AND_CONTEXTUAL_INTERVENTION_STUDY.md`
- `01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md`
