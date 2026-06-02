---
title: Smart Questions And Contextual Intervention Study
file: 16_SMART_QUESTIONS_AND_CONTEXTUAL_INTERVENTION_STUDY.md
layer: study
phase: 000_STUDY_NOTES
category: smart_questions_contextual_intervention
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
  - 000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/02_INTELLIGENT_QUESTION_SYSTEM_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/03_BRIEFING_TO_TASKS_TRANSFORMER_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md
tags: [study, smart_questions, contextual_intervention, doc27_candidate]
---

# Smart Questions And Contextual Intervention Study

## Non-Authority Boundary

This note is study-only. It does not create Doc 27, does not update canonical docs, does not implement UI/backend/API/database/migrations, does not create real agents, and does not create runtime automation.

## 1. Proposito

Study how CKOS should ask smart questions and intervene contextually before, during and after task orchestration.

The purpose is to make questions operational: each question must change a decision, reduce risk, improve ROI, lower context cost, protect approval gates or improve memory.

## 2. Problema que resolve

Without contextual intervention, CKOS can either ask too many generic questions or execute too fast.

This note addresses:

- questions asked without consequence;
- execution continuing after context changes;
- Founder being interrupted for low-value decisions;
- high-risk work hidden inside tasks or batches;
- agents proceeding with stale memory or weak evidence;
- plans created before intent, risk or ROI are clear.

## 3. O que e

Smart Question and Contextual Intervention is a study pattern for deciding when CKOS must pause, ask, route, replan or request approval.

Candidate intervention triggers:

| Trigger | Intervention |
|---|---|
| missing intent | ask clarification question |
| missing source | request evidence or mark confidence low |
| risk increase | pause and route to Metacognik/PMO |
| cost increase | ask for budget approval |
| scope drift | stop and re-lock scope |
| memory conflict | ask which source prevails |
| batch ambiguity | reduce batch size or replan |
| weak ROI | ask whether to continue, defer or cancel |

## 4. O que nao e

It is not:

- a chat UX pattern by itself;
- a mandatory questionnaire;
- a production question engine;
- a runtime rule table;
- a UI component;
- a database schema;
- permission for agents to interrupt forever;
- permission to bypass Founder approval.

## 5. Relacao com intencao minima do Founder

Founder may express a minimal intention such as:

```txt
criar um projeto para isso
```

CKOS should not immediately create tasks. It should identify the first decision that matters.

The first smart questions should clarify:

- desired outcome;
- risk domain;
- expected artifact;
- urgency;
- cost ceiling;
- approval sensitivity;
- whether the next step is briefing, study, planning or execution.

The minimum rule:

```txt
Minimal intention creates minimal questions, not maximal bureaucracy.
```

## 6. Relacao com Cognik

Cognik is the candidate context organizer for smart questions.

Study responsibilities:

- detect missing context;
- classify intent;
- compare current request against memory;
- propose next best question candidates;
- identify whether the answer should update briefing, task, work order, ROI or memory;
- avoid duplicate questions when memory already has a reliable answer.

Cognik should prefer fewer, sharper questions.

## 7. Relacao com Metacognik

Metacognik audits whether the question is necessary and safe.

Metacognik should challenge:

- questions that create noise;
- questions that hide a recommendation;
- questions that lead to premature execution;
- questions based on weak or stale memory;
- questions that should have been approval gates;
- questions that ignore risk, evidence, confidence or autonomy boundaries.

Metacognik may require a pause before a task, Work Order or batch proceeds.

## 8. Relacao com briefing inteligente

Smart questions are the living mechanism of intelligent briefing.

Briefing flow:

```txt
minimal intent
  -> gap detection
  -> smart question
  -> answer
  -> live briefing update
  -> decision or next gap
```

A briefing question is valid only when it changes:

- project direction;
- task decomposition;
- work order scope;
- approval mode;
- risk classification;
- context packet;
- ROI hypothesis;
- memory routing.

## 9. Relacao com sistema de perguntas inteligentes

This note extends the intelligent question system by defining when questions should interrupt execution.

Candidate question contract:

```yaml
question:
trigger:
decision_unlocked:
risk_reduced:
roi_improved:
cost_or_time_impact:
consequence_if_unanswered:
recommended_default:
fallback_if_unanswered:
memory_update_needed:
```

Questions without trigger and consequence should be removed.

## 10. Relacao com tasks, work orders e lotes paralelos

Smart questions can appear at each orchestration layer:

| Layer | Intervention question |
|---|---|
| task | Is this task ready, blocked or premature? |
| work order | Does this package have enough context, ROI and approval? |
| batch | Is the batch size safe under risk/cost ceiling? |
| session | Is this session still inside lock? |
| fan-in audit | Did parallel work create contradictions? |

During parallel batches, smart questions should not be asked by every executor independently. PMO should consolidate them so Founder receives fewer, higher-value decisions.

## 11. Relacao com memoria curta, media e longa

Smart questions use memory differently by layer:

| Memory | Use |
|---|---|
| short | current session state, active lock, latest answer, active blocker |
| medium | live briefing, pending decisions, Work Order status, hypotheses |
| long | approved decisions, stable preferences, validated learning, final releases |

Rules:

- if short memory conflicts with long memory, pause for review;
- if medium memory has a hypothesis only, mark confidence;
- if long memory answers the question, do not ask again unless context changed;
- rejected answers should not become strong memory.

## 12. Relacao com RAG, notes e metadados

RAG should support questions, not replace judgment.

Before asking, CKOS should know:

- which notes were retrieved;
- their layer and canonical status;
- confidence and provenance;
- freshness;
- permission boundary;
- whether the retrieved material is evidence or study context.

Candidate metadata for a question:

```yaml
question_ref:
retrieved_notes:
memory_type:
confidence:
provenance_status:
risk_level:
roi_scope:
canonical_status:
```

## 13. Relacao com ROI por task/projeto/decisao

Each smart question should have ROI.

ROI types:

- avoids wrong task;
- reduces batch rework;
- prevents low-confidence output;
- lowers context cost;
- prevents approval churn;
- improves future memory;
- blocks unsafe autonomy;
- preserves Founder focus.

If a question does not improve at least one ROI dimension, it should become silent internal reasoning or be removed.

## 14. Regras de approval e autonomia

Smart questions must escalate to approval when:

- cost ceiling may be exceeded;
- risk level changes;
- scope expands;
- canonical material could be affected;
- implementation could start;
- batch size increases;
- agent autonomy would rise;
- Founder preference or strategic direction is ambiguous.

Candidate autonomy posture:

| Autonomy level | Question behavior |
|---|---|
| L0 | ask before any action |
| L1 | ask before write |
| L2 | ask before risk/cost/scope change |
| L3 | ask only at approved gates, with audit |
| L4 | not authorized by this study layer |

This is only a study candidate, not an approved autonomy model.

## 15. Antipadroes

- Asking generic questions to look careful.
- Asking after execution what should have been asked before.
- Asking Founder for decisions that memory already answers.
- Hiding approval decisions as clarification questions.
- Letting every parallel session ask separately.
- Treating RAG similarity as enough evidence to skip a question.
- Asking for preference when risk or compliance is the real issue.
- Continuing execution after a question reveals scope drift.

## 16. Candidatos para futuro Doc 27

Candidate Doc 27 sections:

- Smart Question lifecycle.
- Contextual intervention triggers.
- Question-to-task readiness rules.
- Question-to-Work-Order readiness rules.
- Batch pause and escalation rules.
- Founder interruption minimization.
- Metacognik question audit.
- RAG-backed question provenance.

All candidates require future PMO/Founder/Metacognik approval.

## 17. Acceptance criteria

- Note remains study-only.
- No Doc 27 or docs 28-34 are created.
- No canonical docs are modified.
- No runtime implementation is defined.
- Smart questions are tied to decision, risk, ROI, cost, approval or memory.
- Contextual intervention is tied to tasks, Work Orders and batches.
- RAG and metadata are described as support only.
- Autonomy levels are marked as study candidates only.

## 18. Related notes

- `000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/02_INTELLIGENT_QUESTION_SYSTEM_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/03_BRIEFING_TO_TASKS_TRANSFORMER_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md`
