---
title: Cognik Metacognik Task Orchestration Study
file: 17_COGNIK_METACOGNIK_TASK_ORCHESTRATION_STUDY.md
layer: study
phase: 000_STUDY_NOTES
category: cognik_metacognik_task_orchestration
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
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/06_SUPERAGENT_AGENT_SUBAGENT_WORK_ALLOCATION_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/16_SMART_QUESTIONS_AND_CONTEXTUAL_INTERVENTION_STUDY.md
  - 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md
tags: [study, cognik, metacognik, task_orchestration, doc27_candidate]
---

# Cognik Metacognik Task Orchestration Study

## Non-Authority Boundary

This note is study-only and studies orchestration responsibilities only. It does not create real agents, agent directories, services, events, projections, APIs, tables, UI, runtime automation or canonical authority.

## 1. Proposito

Study how Cognik and Metacognik should participate in AI-first task orchestration before a future Doc 27.

The goal is to keep two different functions separate:

```txt
Cognik organizes context and proposes work.
Metacognik audits risk, confidence and reasoning.
```

## 2. Problema que resolve

Task orchestration fails when the same reasoning loop both proposes and approves work.

This note addresses:

- context assembly without audit;
- agent self-approval;
- tasks created from weak hypotheses;
- missing confidence and provenance checks;
- risk hidden behind productivity language;
- parallel sessions without one accountable fan-in audit.

## 3. O que e

This is a study model for splitting task orchestration into complementary responsibilities.

| Responsibility | Candidate owner |
|---|---|
| intent interpretation support | Cognik |
| context packet assembly | Cognik |
| briefing gap detection | Cognik |
| task candidate shaping | Cognik |
| Work Order composition support | Cognik + PMO_CKOS |
| risk/confidence audit | Metacognik |
| evidence contradiction audit | Metacognik |
| self-approval detection | Metacognik |
| release confidence audit | Metacognik + PMO_CKOS |

## 4. O que nao e

It is not:

- a real agent registry;
- an agent pack;
- an implementation contract;
- a workflow engine;
- a production permission model;
- a substitute for Founder approval;
- permission for Cognik or Metacognik to autonomously change canon.

## 5. Relacao com intencao minima do Founder

Founder may provide only a short intent. Cognik should expand it into a context-aware interpretation, while Metacognik checks whether the interpretation is safe enough to plan around.

Example:

```txt
Founder intent -> Cognik interpretation -> Metacognik confidence/risk audit -> PMO plan
```

If confidence is low, the next output should be a smart question, not a task.

## 6. Relacao com Cognik

Cognik is the candidate context and transformation layer.

Study responsibilities:

- retrieve relevant memory;
- identify briefing gaps;
- suggest task candidates;
- detect duplicate work;
- classify likely output type;
- propose task-to-Work-Order grouping;
- prepare context packets with minimum sufficient evidence.

Cognik should not be final approver of its own interpretation.

## 7. Relacao com Metacognik

Metacognik is the candidate risk, confidence and reasoning auditor.

Study responsibilities:

- audit assumptions;
- detect circular reasoning;
- detect evidence mismatch;
- detect hidden implementation drift;
- block unsafe autonomy;
- require rollback or replan when confidence is low;
- audit whether the question, task or Work Order should exist.

Metacognik can pause orchestration, but this study does not grant runtime veto implementation.

## 8. Relacao com briefing inteligente

In briefing, Cognik structures answers and hypotheses. Metacognik checks whether the briefing is strong enough to become tasks or Work Orders.

Briefing readiness check:

```txt
briefing answer
  -> Cognik gap/context classification
  -> Metacognik risk/confidence audit
  -> task candidate or smart question
```

If briefing is incomplete, orchestration remains in study/planning mode.

## 9. Relacao com sistema de perguntas inteligentes

Cognik may propose the next best question. Metacognik audits whether it is the right question.

Question audit checks:

- Does it unlock a decision?
- Does it reduce real risk?
- Does it improve ROI?
- Is it answerable from existing memory?
- Is it actually an approval request?
- Does it protect Founder focus?

## 10. Relacao com tasks, work orders e lotes paralelos

Cognik helps prepare task candidates. PMO_CKOS packages them into Work Orders. Metacognik audits the package before or during fan-in.

Parallel batch posture:

| Phase | Cognik | Metacognik |
|---|---|---|
| before fan-out | context packet and dependency clues | risk/confidence readiness |
| during execution | context refresh if needed | pause on contradiction or scope drift |
| fan-in | organize outputs and memory refs | audit contradictions, evidence and self-approval |

No executor should be the final auditor of its own Work Order.

## 11. Relacao com memoria curta, media e longa

Cognik retrieves and organizes memory. Metacognik audits memory trust.

| Memory layer | Cognik role | Metacognik role |
|---|---|---|
| short | summarize active session state | detect stale or conflicting active state |
| medium | assemble live project context | audit unresolved hypotheses |
| long | retrieve approved decisions and learning | verify hierarchy of trust |

Memory conflict should create an audit pause, not silent overwrite.

## 12. Relacao com RAG, notes e metadados

Cognik can use RAG to assemble relevant notes. Metacognik checks the reliability of retrieved context.

Candidate metadata checks:

```yaml
note_ref:
layer:
status:
confidence:
provenance_status:
canonical_status:
freshness:
permission_scope:
used_for:
```

RAG output should be input to reasoning, not final authority.

## 13. Relacao com ROI por task/projeto/decisao

Cognik estimates what context or task may create value. Metacognik audits whether the ROI claim is justified.

ROI audit questions:

- Is the value operational or merely activity?
- Does this reduce context cost?
- Does this prevent rework?
- Does this improve decision quality?
- Is evidence strong enough for the ROI claim?
- Is cost proportionate to expected value?

## 14. Regras de approval e autonomia

Approval remains with Founder or authorized governance roles.

Candidate autonomy boundaries:

| Action | Cognik | Metacognik |
|---|---|---|
| suggest context | allowed as study concept | audit if high risk |
| create task candidate | allowed as study concept | audit if risk/cost/scope changes |
| approve Work Order | not allowed | not allowed |
| approve batch | not allowed | may recommend pause |
| change canon | not allowed | not allowed |
| start implementation | not allowed | block as study violation |

No autonomy level is promoted by this note.

## 15. Antipadroes

- Cognik creates tasks from every briefing answer.
- Metacognik becomes decorative and never blocks.
- Same agent proposes, executes and approves.
- RAG retrieval is treated as verified truth.
- Context pack becomes huge and lowers ROI.
- Batch execution starts before confidence audit.
- Founder approval is inferred from silence.
- Work Order is treated as an implementation object.

## 16. Candidatos para futuro Doc 27

Candidate Doc 27 sections:

- Cognik role in task readiness.
- Metacognik role in risk/confidence audit.
- Separation of proposer, executor, auditor and approver.
- Fan-in audit responsibilities.
- Memory trust audit before task creation.
- ROI claim audit.
- Self-approval prevention.

These are candidates only.

## 17. Acceptance criteria

- Note remains non-canonical study.
- No real agent is created.
- Cognik and Metacognik responsibilities are separated.
- Founder approval remains explicit.
- Metacognik audit is tied to risk, confidence, evidence and autonomy.
- Cognik is tied to context, briefing and task candidate preparation.
- No implementation or schema is authorized.

## 18. Related notes

- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/06_SUPERAGENT_AGENT_SUBAGENT_WORK_ALLOCATION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/16_SMART_QUESTIONS_AND_CONTEXTUAL_INTERVENTION_STUDY.md`
- `02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md`
