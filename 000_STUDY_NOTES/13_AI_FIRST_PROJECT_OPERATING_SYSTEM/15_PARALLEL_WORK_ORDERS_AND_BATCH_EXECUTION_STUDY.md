---
title: Parallel Work Orders And Batch Execution Study
file: 15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md
layer: study
phase: 000_STUDY_NOTES
category: parallel_work_orders_batch_execution
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
intelligence_level: high
purpose: Study Work Orders and Batch Execution as non-canonical preparation for a future Doc 27.
inputs:
  - CKOS_VAULT_MAP_REFRESH_REPORT.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/README.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_tasks.md
  - 000_ROADMAPS/ck_memory.md
  - 000_ROADMAPS/ck_tasks.md
  - 000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
  - 000_ROADMAPS/ROADMAP_ROUTING_MATRIX.md
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - 02_EXECUTION_SYSTEM/07_WORKFLOW_BLUEPRINTS.md
  - 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md
outputs:
  - work order study model
  - batch execution study model
  - fan-out fan-in audit model
  - Doc 27 candidate sections
framework:
  - intent -> questions -> briefing -> work order -> tasks -> batch -> fan-out -> fan-in -> audit -> release -> memory
edge_cases:
  - work order mistaken for canonical schema
  - batch approval hides high-risk task
  - agent conflict during parallel execution
  - checkout lock treated as optional
  - study note treated as Doc 27 authority
integrations:
  - PMO_CKOS
  - Cognik
  - Metacognik
  - Founder approval
  - Multi-Session Execution Policy
  - future Doc 27
prompts:
  - Treat Work Order as study-only until Founder/PMO/Metacognik approve canonical scope.
metrics:
  - no canonical docs created
  - no implementation started
  - no real agents created
  - work order boundaries clarified before Doc 27
related_notes:
  - 05_TASK_AI_FIRST_SYSTEM_STUDY.md
  - 07_PARALLEL_EXECUTION_AND_CHECKOUT_LOCK_STUDY.md
  - 08_FOUNDER_APPROVAL_BATCH_CONTROL_STUDY.md
  - 09_ROI_AWARE_TASKS_NOTES_AND_QUESTIONS_STUDY.md
  - 13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md
  - 14_ACCEPTANCE_CRITERIA_FOR_DOC27.md
tags:
  - study
  - work_orders
  - batch_execution
  - checkout_lock
  - doc27_candidate
---

# Parallel Work Orders And Batch Execution Study

## Non-Authority Boundary

This is a non-canonical Study Layer note. It does not create Doc 27, does not alter docs 01-26, does not authorize UI, backend, API, database, migrations, MCP server, n8n JSONs, runtime automations, real agents or production schemas.

`Work Order` in this note is a proposed operating concept only. It is not a database table, not an API contract, not a UI object and not a permission grant.

Identifier and schema warning: all fields in this note, including `approval_id`, `task_id`, `work_order_id`, `lock_id` and `release_id`, are study placeholders or references only. They do not create canonical Doc 11 tables, fields, migrations, RLS rules or API contracts. Any future canonical use requires a separate approved Doc 11 patch.

## 1. Proposito

This note studies how CKOS should coordinate multiple AI-first tasks through a governed Work Order and Batch Execution layer before any future Doc 27 is written.

The goal is to prevent Doc 27 from becoming a generic task-list document. A CKOS Work Order should preserve intention, briefing, questions, context, risk, ROI, approval, checkout lock, agent allocation, execution evidence, fan-in audit, release and memory.

The central thesis:

```txt
Task = atomic work candidate.
Work Order = governed executable package.
Batch = approved group of Work Orders or tasks executed under shared limits.
Release = audited closure with evidence, risks and next step.
```

Mandatory distinction: a `task` is the atomic unit of work. A `Work Order` is the governed envelope that can group one or more tasks with scope, approval, lock, context, risk, ROI, evidence and release requirements. A local schema using `task_id` must not be read as a Work Order identifier unless it explicitly says it is a study placeholder.

## 2. Por Que Work Order E Necessario

Tasks alone are too small to govern parallel AI work. Sessions alone are too operational. Roadmaps are too broad. Releases happen too late. CKOS needs a middle object that can say:

- what work is being authorized;
- why it exists;
- which tasks belong together;
- which agents or sessions may touch it;
- what files, folders, costs and risks are allowed;
- which approval covers it;
- how fan-out is coordinated;
- how fan-in is audited;
- what memory must be updated after completion.

Without Work Orders, CKOS risks:

- approving isolated tasks without seeing dependency chains;
- allowing parallel sessions to write overlapping files;
- hiding high-risk tasks inside a generic batch;
- losing ROI traceability after execution;
- treating agent activity as progress even when no release evidence exists.

Work Order is therefore the proposed PMO bridge between intelligent briefing and controlled execution.

## 3. Diferenca Entre Task, Session, Work Order, Batch, Roadmap E Release

| Object | Study definition | Authority level | Main risk if confused |
|---|---|---|---|
| `task` | Atomic unit of intended work with origin, context, risk, cost, ROI and acceptance. | Study candidate until approved. | Becomes generic Kanban card. |
| `session` | Time-bounded interaction or execution run by one agent or role. | Operational, governed by lock/release. | Session activity mistaken for project progress. |
| `work_order` | Governed package that groups tasks, scope, approval, locks, agents, ROI and release requirements. | Candidate orchestration object. | Treated as canonical schema or permission grant. |
| `batch` | Approved execution window for multiple tasks or Work Orders under shared limits. | Approval envelope, not bypass. | Hides risk, cost or scope changes. |
| `roadmap` | Auxiliary planning lane that orders future workstreams and gates. | Non-canonical unless later promoted. | Roadmap treated as architecture authority. |
| `release` | Closure evidence proving what changed, what did not, validation, residual risk and next step. | Audit output, not automatic approval. | Done status without evidence. |

Short rule:

```txt
task says what.
session says who is acting now.
work_order says what governed package is executable.
batch says how much can proceed together.
roadmap says why this belongs in the bigger sequence.
release says what was actually completed and audited.
```

## 4. Schema Proposto De Work Order

This is a study schema, not a data model.

**ESTUDO APENAS — schema conceitual, não DDL, não runtime, não migração, não contrato de API.**

```yaml
work_order_id:
title:
status: draft | needs_context | needs_questions | ready_for_approval | approved | locked | executing | fan_in_review | released | rejected | archived
origin_intent:
source_questions:
related_briefing:
roadmap_refs:
task_refs:
batch_ref:
owner_role:
planner_role:
executor_roles:
auditor_role:
approver_role:
context_pack:
memory_refs:
evidence_refs:
scope:
  allowed_files:
  allowed_folders:
  allowed_actions:
  forbidden_files:
  forbidden_folders:
  forbidden_actions:
risk:
  level:
  types:
  stop_conditions:
cost:
  estimated_ckc:
  token_budget:
  tool_budget:
  time_budget:
roi:
  hypothesis:
  dimensions:
  evidence_needed:
approval:
  required:
  approved_by:
  approval_mode:
  expires_at:
checkout_lock:
  lock_id:
  lock_required:
  active_holder:
  conflict_policy:
execution:
  fan_out_units:
  dependencies:
  sequence:
  parallel_allowed:
  escalation_rules:
fan_in_audit:
  required:
  auditor:
  checks:
release:
  files_created:
  files_changed:
  files_not_touched:
  validation:
  risks_remaining:
  next_step:
learning:
  feedback_refs:
  memory_update_required:
  patch_candidate_refs:
```

Minimum viable Work Order fields for a future Doc 27 candidate:

```txt
work_order_id
origin_intent
scope_allowed
scope_forbidden
task_refs
risk_level
cost_estimate
roi_hypothesis
approval_required
checkout_lock
release_requirements
```

## 5. Batch Execution Model

Batch Execution is the controlled execution of multiple approved tasks or Work Orders under one explicit envelope.

Proposed flow:

```txt
briefing/context
  -> task candidates
  -> Work Order proposal
  -> risk/cost/ROI scoring
  -> approval mode selection
  -> checkout lock
  -> fan-out execution
  -> fan-in audit
  -> release
  -> memory and learning update
```

Batch types:

| Batch type | Use | Stop condition |
|---|---|---|
| `study_batch` | Create or audit study notes only. | Any canonical or implementation drift. |
| `memory_batch` | Update governed memory only. | Conflict with higher-trust source. |
| `documentation_batch` | Apply approved auxiliary docs work. | File outside lock. |
| `audit_batch` | Review multiple outputs without editing them. | Auditor starts writing execution changes. |
| `canonical_candidate_batch` | Prepare candidate material only. | Candidate treated as approved canon. |
| `implementation_candidate_batch` | Prepare future implementation plan only after canon. | Any real code/API/UI/runtime creation. |

Batch approval must declare:

- batch size;
- Work Orders or tasks included;
- allowed and forbidden scope;
- risk ceiling;
- cost ceiling;
- approval expiry;
- audit owner;
- release requirements.

## 6. Fan-out / Fan-in Audit

Fan-out means splitting a Work Order or batch into parallel execution units. Fan-in means gathering the results back into one audit and release.

Fan-out is allowed only when:

- each unit has non-overlapping write scope;
- each unit knows the shared Work Order and batch approval;
- dependencies are explicit;
- one file has one active writer;
- risk/cost ceilings apply to every unit;
- escalation rules are known before execution.

Fan-in audit must verify:

| Check | Meaning |
|---|---|
| Scope integrity | No unit touched forbidden files or actions. |
| Dependency integrity | Outputs match the dependency plan. |
| Evidence integrity | Claims are backed by source, test, review or clear reasoning. |
| Conflict integrity | No two outputs contradict each other silently. |
| Cost integrity | Actual cost stayed inside batch ceiling or was re-approved. |
| Risk integrity | New risks were classified before release. |
| Memory integrity | Short, medium and long memory updates are correctly routed. |
| Release integrity | One consolidated release explains the whole batch. |

Fan-in rule:

```txt
No batch is released by counting completed tasks.
A batch is released only after consolidated audit.
```

## 7. Aprovacao De Proximas 5/10 Tarefas

Founder approval can be batched, but never blind.

Proposed approval modes:

```txt
approve_next_5_tasks
approve_next_10_tasks
approve_next_5_low_risk_tasks
approve_next_10_study_only_tasks
approve_next_batch_until_cost_ceiling
approve_next_batch_until_risk_change
approve_one_work_order
approve_work_order_batch
reject_and_request_replan
```

Approval of next 5 tasks should be used when:

- the tasks are small or medium risk;
- dependencies are clear;
- scope is narrow;
- Work Order release can be audited in one pass.

Approval of next 10 tasks should be used only when:

- all tasks are low risk or study-only;
- the file/folder scope is stable;
- no canonical or implementation action is included;
- cost ceiling is explicit;
- any risk escalation stops the batch.

Required language for a future approval:

```txt
Founder approves the next [5/10] tasks only inside Work Order [id],
with allowed scope [scope],
forbidden scope [scope],
risk ceiling [level],
cost ceiling [limit],
expiry [session/date],
and mandatory fan-in audit before release.
```

## 8. ROI Por Work Order

Every Work Order needs an ROI hypothesis before approval.

ROI de Work Order deve referenciar o framework do Doc 21 e não redefinir um sistema paralelo de ROI.

ROI dimensions:

| Dimension | Work Order question |
|---|---|
| Entropy reduction | Does this reduce ambiguity or duplicate paths? |
| Context cost reduction | Will future agents need less context to continue? |
| Decision quality | Does this unlock a better Founder/PMO decision? |
| Traceability | Can outputs be linked to intent, briefing, task and approval? |
| Risk reduction | Does this detect or contain risk earlier? |
| Execution speed | Does batching reduce interruption without hiding risk? |
| Reuse | Can outputs become reusable notes, prompts or context packs? |
| Learning capture | Will feedback improve future Work Orders? |

Proposed ROI block:

```yaml
roi:
  primary_dimension:
  secondary_dimensions:
  value_created:
  cost_to_execute:
  risk_reduced:
  context_saved:
  decision_unlocked:
  evidence_needed:
  after_release_measure:
```

Work Order ROI rule:

```txt
No Work Order should be approved only because tasks are available.
It should be approved because the governed package creates measurable operational value.
```

## 9. Perguntas Inteligentes Antes E Durante Execucao

Before Work Order approval:

| Question | Why it matters |
|---|---|
| What decision does this Work Order unlock? | Blocks execution without PMO value. |
| Which briefing answer or intent created it? | Preserves provenance. |
| What is the smallest safe batch size? | Avoids oversized approvals. |
| Which files or actions are forbidden? | Prevents scope drift. |
| What risk should stop the batch? | Prevents hidden escalation. |
| What cost ceiling applies? | Protects credits/time/tool usage. |
| What evidence proves success? | Prevents status-only release. |
| What memory must be updated? | Keeps learning and continuity alive. |

During execution:

| Question | Trigger |
|---|---|
| Did context change enough to pause? | New source, contradiction or Founder update. |
| Did risk exceed approved ceiling? | Security, legal, canonical, financial or implementation drift. |
| Did a task need a file outside lock? | Checkout conflict. |
| Did another agent produce conflicting output? | Fan-in contradiction. |
| Did cost exceed estimate? | Budget or model/tool usage variance. |
| Should this become learning or patch candidate? | Repeated correction or reusable pattern. |

Quality rule:

```txt
Every Work Order question must declare decision_unlocked, risk_reduced, roi_improved, cost_or_time_impact and consequence_if_unanswered.
```

## 10. Integracao Com Briefing Inteligente

The intelligent briefing should create Work Orders only after it has transformed raw answers into structured operational context.

Suggested transformation:

```txt
minimal intent
  -> Nick detects intent
  -> Cognik structures live briefing and gaps
  -> smart questions reduce ambiguity
  -> Metacognik audits risk/confidence
  -> PMO_CKOS proposes Work Order
  -> Founder approves batch or requests replan
```

Briefing-to-Work-Order rules:

- not every answer becomes a task;
- not every task becomes a Work Order;
- gaps should become questions before tasks;
- high-risk answers should pause for audit before batch creation;
- Work Order must retain source questions and briefing refs;
- approval mode must be chosen after risk/cost/ROI classification.

The Work Order is the executable packaging of a briefing-derived decision, not a replacement for the briefing.

## 11. Integracao Com Cognik E Metacognik

This note does not create real agents. It studies role responsibilities.

| Role | Work Order responsibility |
|---|---|
| `Cognik` | Organizes context, briefing gaps, hypotheses, transformer outputs and memory retrieval candidates. |
| `Metacognik` | Audits assumptions, confidence, evidence, risk, circular logic, self-approval and unsafe autonomy. |
| `PMO_CKOS` | Owns Work Order scope, locks, batch limits, release requirements and roadmap alignment. |
| `Founder` | Approves strategic direction, exceptions, batch size and high-impact decisions. |

Cognik integration:

- assemble minimum context pack;
- connect briefing answers to task candidates;
- identify duplicate tasks from memory;
- classify missing context before execution;
- propose Work Order composition.

Metacognik integration:

- veto or pause weak Work Orders;
- detect risk hidden inside batch approval;
- audit evidence quality at fan-in;
- flag self-approval by executor;
- require rollback or replan when confidence is low;
- classify whether feedback becomes memory, learning or patch candidate.

## 12. Integracao Com Memoria Curta, Media E Longa

Work Orders should route memory by trust and lifespan.

| Memory layer | Work Order use |
|---|---|
| Short memory | Current session state, active lock, running tasks, unresolved questions, transient blockers. |
| Medium memory | Active project briefing, pending decisions, Work Order state, batch progress, hypotheses and review notes. |
| Long memory | Approved decisions, final releases, reusable patterns, validated learning, accepted outputs and strategic preferences. |

Memory write rules:

- active execution state belongs to short memory;
- incomplete Work Orders belong to medium memory;
- released Work Orders may update long memory only when approved and auditable;
- rejected outputs must not become strong memory;
- study notes remain lower trust than canonical docs;
- memory conflicts trigger Metacognik review.

Minimum context packet for a Work Order:

```yaml
work_order_summary:
origin_intent:
briefing_refs:
active_decisions:
constraints:
allowed_scope:
forbidden_scope:
task_refs:
memory_refs:
evidence_refs:
approval_rules:
release_requirements:
```

Boundary with BRA: this Work Order context packet is internal execution state for the governed Work Order. It is not a BRA Packet. BRA Packet is the relay between sessions. BRA does not replace lock, approval or Work Order `context_pack`; Work Order `context_pack` does not replace BRA between sessions.

## 13. Regras De Conflito Entre Agentes

Conflict types:

| Conflict | Rule |
|---|---|
| Same file write | Newer or lower-priority session waits. |
| Scope overlap | PMO narrows scope before execution. |
| Evidence contradiction | Metacognik audits before release. |
| Agent self-approval | Blocked; another role audits. |
| Cost escalation | Pause for re-approval. |
| Risk escalation | Pause for Metacognik/PMO/Founder as needed. |
| Roadmap conflict | Use `ROADMAP_ROUTING_MATRIX.md` before choosing lane. |
| Study vs canon conflict | Canonical docs prevail; study note remains context only. |

Agent priority for conflict resolution:

```txt
Founder explicit decision
  > approved canonical docs
  > PMO checkout lock
  > Metacognik risk veto/pause
  > current Work Order
  > roadmap/study context
  > agent inference
```

Parallelism rule:

```txt
Agents may read in parallel.
Agents may write in parallel only when locked scopes do not overlap.
Agents may not audit their own output as final release authority.
```

## 14. Regras De Checkout Lock

Work Orders inherit the Multi-Session rule:

```txt
Every writing action requires declared scope, forbidden scope, checkout lock and checkout release.
```

Work Order lock candidate:

**ESTUDO APENAS — schema conceitual, não DDL, não runtime, não migração, não contrato de API.**

```yaml
lock_id:
work_order_id:
batch_id:
task_refs:
holder_agent:
session_id:
session_type:
allowed_scope:
forbidden_scope:
expected_outputs:
estimated_cost:
intelligence_level:
approval_basis:
expires_at:
release_required: true
```

Lock rules:

- one file, one active writer;
- one Work Order may have many read-only auditors;
- no hidden writes during audit;
- no broad lock when a narrow lock is enough;
- lock expires at session end unless explicitly extended;
- scope expansion requires re-approval;
- lock release must state what was not touched.

## 15. Release Requirements

Every Work Order or batch release should include:

**ESTUDO APENAS — schema conceitual, não DDL, não runtime, não migração, não contrato de API.**

```yaml
release_id:
work_order_id:
batch_id:
released_by:
audited_by:
files_created:
files_changed:
files_not_touched:
tasks_completed:
tasks_rejected:
tasks_deferred:
validation:
evidence_refs:
cost_actual:
risk_changes:
conflicts_found:
conflicts_resolved:
memory_updates:
learning_updates:
patch_candidates:
risks_remaining:
next_step:
status:
```

Release rules:

- release is not the same as approval;
- release does not canonize study material;
- release must declare forbidden surfaces not touched;
- release must include residual risk;
- release must route learning and memory;
- release must identify whether external audit is required.

Minimum release statement:

```txt
This Work Order is released as study-only/auxiliary/canonical-candidate,
with no forbidden scope touched,
with validation complete,
with residual risks declared,
and with next step identified.
```

## 16. Anti-patterns

- Treating Work Order as a database schema before Doc 27.
- Treating batch approval as permission to skip task-level risk.
- Approving next 10 tasks when risk or scope is unstable.
- Counting completed tasks instead of auditing fan-in quality.
- Allowing executor to self-approve release.
- Creating real agents from role language in a study note.
- Updating long memory from unverified study output.
- Using roadmap priority as canonical authority.
- Expanding checkout scope mid-run without approval.
- Hiding cost escalation inside a batch.
- Asking questions that do not change decision, risk, ROI, cost, scope, evidence or memory.
- Creating UI/backend/API/runtime artifacts from this study.
- Creating Doc 27 from this note without separate Founder/PMO/Metacognik approval.

## 17. Acceptance Criteria

This note is acceptable only if:

- it remains in `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/`;
- it does not create or imply Doc 27;
- it does not alter canonical docs;
- it does not implement UI, backend, API, database, migrations, agents, MCP, n8n or automations;
- it defines Work Order as a non-canonical study object;
- it distinguishes task, session, Work Order, batch, roadmap and release;
- it includes a proposed Work Order schema as study-only;
- it includes Batch Execution and Fan-out/Fan-in Audit;
- it includes next 5/10 task approval controls;
- it connects Work Order to ROI, intelligent questions, briefing, Cognik, Metacognik and memory layers;
- it includes conflict, checkout lock and release rules;
- it lists anti-patterns and Doc 27 candidates;
- it closes with CHECKOUT RELEASE.

## 18. Candidatos Para Futuro Doc 27

Candidate sections for future Doc 27, subject to separate audit and approval:

| Candidate section | Why it matters | Suggested posture |
|---|---|---|
| Work Order Object Model | Bridges task and execution governance. | Strong Doc 27 candidate. |
| Work Order Lifecycle | Defines draft through release/archival states. | Strong Doc 27 candidate. |
| Batch Execution Policy | Allows scalable execution without blind approval. | Strong Doc 27 candidate. |
| Fan-out/Fan-in Audit | Makes parallel work auditable. | Strong Doc 27 candidate. |
| Approval Of Next 5/10 Tasks | Reduces Founder interruption while preserving limits. | Candidate with strict guardrails. |
| Work Order ROI | Prevents work packages without value hypothesis. | Strong Doc 27 candidate. |
| Work Order Smart Questions | Ensures questions alter decisions, risk, ROI, cost or memory. | Strong Doc 27 candidate. |
| Briefing-To-Work-Order Transformer | Connects intelligent briefing to executable packages. | Candidate, maybe shared with future briefing doc. |
| Cognik/Metacognik Review Contract | Separates context organization from risk/confidence audit. | Strong Doc 27 candidate. |
| Memory Routing By Work Order | Links execution to short, medium and long memory. | Strong Doc 27 candidate. |
| Checkout Lock Requirements | Embeds multi-session safety. | Strong Doc 27 candidate. |
| Release Requirements | Requires evidence, not status-only closure. | Strong Doc 27 candidate. |

Deferred or separate candidates:

| Candidate | Reason to defer |
|---|---|
| Production database schema for Work Orders | Requires Doc 11 alignment and implementation gate. |
| UI widgets for Work Orders and batches | Requires future Product/UI study and implementation approval. |
| Real agent registry integration | Requires agent policy and runtime approval. |
| Automation runner for batches | Requires backend/runtime architecture and security gates. |

## CHECKOUT RELEASE

files_created:

- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md`

files_changed:

- none

files_not_touched:

- canonical docs 01-26
- docs 27-34
- `ARCHITECTURE_PATCH_REPORT.md`
- `QA_DOCUMENTATION_CHECKLIST.md`
- `000_ROADMAPS/`
- `000_UPLOADS/`
- `000_UPGRADE/`
- UI/backend/API/database/migrations
- MCP server, n8n JSONs, real agents or runtime automations

validation:

- Study-only note created at the Founder-authorized path.
- Work Order and Batch Execution treated as non-canonical candidates only.
- No auxiliary maps or canonical files were intentionally modified.

risks_remaining:

- Future readers may treat Work Order schema as canonical before audit.
- Batch approval still needs PMO/Metacognik narrowing before Doc 27.
- Future Doc 27 scope must decide whether Work Order is central or supporting.

next_step:

- PMO/Metacognik audit this note with existing Study Layer 13 before any Doc 27 checkout.

status: released_as_study_note_only

CHECKOUT RELEASE
