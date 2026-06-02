---
title: Prompt Pack For Multi-Session Claude Audits Study
file: 20_PROMPT_PACK_FOR_MULTI_SESSION_CLAUDE_AUDITS_STUDY.md
layer: study
doc_type: study_note
phase: 000_STUDY_NOTES
category: ai_first_project_operating_system
status: draft
version: 0.1.0
created_at: 2026-05-31
updated_at: 2026-05-31
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
  - metacognik
source_type: user_request
source_path: Codex session - Prompt Pack Generator for Claude Audits
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: high
project: ckos
related_docs:
  - 07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/README.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md
related_notes:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/14_ACCEPTANCE_CRITERIA_FOR_DOC27.md
  - 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/README.md
tags:
  - ckos
  - study
  - prompt_pack
  - claude
  - audit
  - pmo
  - doc27
---

# Prompt Pack For Multi-Session Claude Audits Study

## Non-Authority Boundary

This file is study-only. It creates prompts for future Claude audit sessions. It does not authorize edits to canonical docs, docs 27-34, backend, UI, API, database, migrations, n8n JSONs, runtime agents or real automations.

All prompts below must preserve:

- RAW -> STUDY -> CANONICAL flow.
- Study Layer 13 as non-canonical.
- Doc 27 as not open unless a later Founder/PMO/Metacognik gate explicitly approves it.
- One session, one scope, one checkout release.

## Global Claude Session Guardrail

Use this preface before every prompt in this pack.

```txt
You are Claude acting as PMO_CKOS + Metacognik auditor for CKOS.

Mode discipline:
- Do not edit canonical docs.
- Do not create docs 27-34.
- Do not update ARCHITECTURE_PATCH_REPORT.md.
- Do not edit 00_SYSTEM_GOVERNANCE/*.
- Do not create backend, UI, API, database, migrations, n8n JSONs, runtime agents or real automations.
- If mode is read-only, produce findings only.
- If mode is patch, patch only the explicitly allowed study output file and emit CHECKOUT RELEASE.

Authority discipline:
- Study material can recommend, never govern.
- Roadmaps can sequence, never replace canonical specs.
- Memory can preserve context, never authorize implementation.
- canonical_candidate means candidate, not approval.
```

## 1. Prompt - Audit Doc 26

### Session Recommended

`claude_doc26_audit_readonly`

### Intelligence Level Recommended

High.

### Mode

Read-only.

### Files To Read

- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`
- `00_SYSTEM_GOVERNANCE/00_DOCUMENT_TEMPLATE.md`
- `00_SYSTEM_GOVERNANCE/00_TAXONOMY_AND_NAMING.md`
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md`
- `07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`
- `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md`
- `03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`
- `03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`

### Files Forbidden

- All files for editing.
- Docs 27-34.
- `ARCHITECTURE_PATCH_REPORT.md`.
- Backend, UI, API, database, migrations, n8n JSONs and runtime agent files.

### Prompt

```txt
Audit Doc 26 as read-only.

Goal:
Check whether Doc 26 is internally coherent and aligned with CKOS governance, runtime, data, security, evals, cost guard and RAW/STUDY rules.

Audit questions:
1. Does Doc 26 preserve connector/MCP as governed integration, not core bypass?
2. Does every connector path pass through policy_engine, tool_router, approval_gate, cost_guard, audit logs, tenant isolation and secret_refs?
3. Are collector, actor and provider boundaries clear?
4. Are proposed schemas marked as proposals when not canonicalized in Doc 11?
5. Are required patches to Docs 10/11/12/13/18/24 clearly deferred rather than silently applied?
6. Are ghost tables, ghost services, ghost events or ghost projections implied?
7. Does Doc 26 accidentally authorize implementation?

Return findings ordered by severity:
- Critical blockers.
- High-risk inconsistencies.
- Medium gaps.
- Low editorial issues.
- Patch candidates, without applying patches.
```

### Acceptance Criteria

- Findings cite exact file names and section numbers.
- No file is edited.
- Any proposed change is labeled `patch_candidate`, not applied.
- Implementation remains blocked.

### Expected Output

Markdown audit report with: verdict, findings table, open questions, deferred patches and release.

### Risks

- Treating schema proposals as implemented schema.
- Treating MCP server registry as runtime infrastructure already approved.
- Missing security/cost hooks.

### Expected CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: claude_doc26_audit_readonly
mode: read-only
files_created: none
files_changed: none
files_not_touched: canonical docs, docs 27-34, ARCHITECTURE_PATCH_REPORT.md, backend, UI, APIs, migrations, database, n8n JSONs
validation: Doc 26 audited against governance/runtime/security/evals constraints
risks_remaining: listed in audit
next_step: PMO_CKOS decides whether to create study-only patch candidate
status: released
```

## 2. Prompt - Audit Study Layer 13

### Session Recommended

`claude_study_layer_13_audit_readonly`

### Intelligence Level Recommended

High.

### Mode

Read-only.

### Files To Read

- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/README.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/01_PROJECT_AI_FIRST_OPERATING_MODEL.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/02_INTELLIGENT_QUESTION_SYSTEM_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/03_BRIEFING_TO_TASKS_TRANSFORMER_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/04_NOTES_AS_OPERATIONAL_MEMORY_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/05_TASK_AI_FIRST_SYSTEM_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/06_SUPERAGENT_AGENT_SUBAGENT_WORK_ALLOCATION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/07_PARALLEL_EXECUTION_AND_CHECKOUT_LOCK_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/08_FOUNDER_APPROVAL_BATCH_CONTROL_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/09_ROI_AWARE_TASKS_NOTES_AND_QUESTIONS_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/10_FEEDBACK_TO_LEARNING_LOOP_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/11_PROJECT_SELF_DOCUMENTATION_SYSTEM_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/12_RAG_METADATA_AND_VECTOR_CATEGORY_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/14_ACCEPTANCE_CRITERIA_FOR_DOC27.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/16_SMART_QUESTIONS_AND_CONTEXTUAL_INTERVENTION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/17_COGNIK_METACOGNIK_TASK_ORCHESTRATION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/18_AI_FIRST_PROJECT_NOTE_SYSTEM_AND_RAG_GOVERNANCE_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/19_FOUNDER_CONTROL_APPROVAL_BATCHES_AND_AUTONOMY_LEVELS_STUDY.md`

### Files Forbidden

- Docs 01-26 for editing.
- Docs 27-34.
- `ARCHITECTURE_PATCH_REPORT.md`.
- `00_SYSTEM_GOVERNANCE/*`.
- Runtime implementation files.

### Prompt

```txt
Audit Study Layer 13 as read-only.

Goal:
Determine whether Study Layer 13 is coherent, non-canonical, useful for future Doc 27 scoping and free from implementation drift.

Check:
1. Does every note preserve non-authority boundary?
2. Are Project, Task, Work Order, Batch, Note, Memory, Smart Question, Cognik and Metacognik distinct?
3. Are candidates for Doc 27 specific enough to avoid a generic task-list doc?
4. Are any backend services, tables, APIs, projections or agents implied before canonical approval?
5. Are ROI, risk, cost, approval and memory hooks present enough for PMO decision?
6. What should remain study-only?
7. What can become patch candidate later?

Return:
- layer verdict;
- duplication map;
- missing decision map;
- Doc 27 readiness estimate;
- blocked items;
- recommended next PMO session.
```

### Acceptance Criteria

- No file changes.
- Clear distinction between useful study and canonical candidate.
- Doc 27 is not opened automatically.

### Expected Output

Study Layer 13 audit report with readiness score and blockers.

### Risks

- Collapsing tasks, work orders and sessions into one generic concept.
- Promoting notes or memory as spec.
- Opening Doc 27 before acceptance criteria are met.

### Expected CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: claude_study_layer_13_audit_readonly
mode: read-only
files_created: none
files_changed: none
files_not_touched: canonical docs, docs 27-34, ARCHITECTURE_PATCH_REPORT.md, backend/UI/runtime assets
validation: Study Layer 13 audited for coherence and non-authority
risks_remaining: listed in audit
next_step: Founder/PMO decides whether to request patch candidate
status: released
```

## 3. Prompt - Audit Documentation Pattern Normalization

### Session Recommended

`claude_documentation_pattern_audit_readonly`

### Intelligence Level Recommended

High.

### Mode

Read-only.

### Files To Read

- `00_SYSTEM_GOVERNANCE/00_DOCUMENT_TEMPLATE.md`
- `00_SYSTEM_GOVERNANCE/00_TAXONOMY_AND_NAMING.md`
- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md`
- `99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/README.md`
- `99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/01_current_patterns_audit.md`
- `99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/02_yaml_standard_proposal.md`
- `99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/10_study_note_standard.md`
- `99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/11_canonical_doc_standard.md`
- `99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/12_naming_and_enums_standard.md`
- `99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/13_tags_taxonomy_proposal.md`
- `99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/14_migration_strategy.md`
- `99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/15_risk_register.md`
- `99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/16_promotion_to_canonical_proposal.md`

### Files Forbidden

- All files for editing.
- Nested or parallel `00_GOVERNANCE/Documentation_Standards/` material as canonical authority unless PMO explicitly scopes it as imported study evidence.

### Prompt

```txt
Audit Documentation Pattern Normalization as read-only.

Goal:
Compare the research lab study with official CKOS governance without canonizing it.

Check:
1. Which patterns already exist officially?
2. Which study-only patterns are useful?
3. Which fields conflict with 00_DOCUMENT_TEMPLATE?
4. Which names conflict with 00_TAXONOMY_AND_NAMING?
5. Which enum expansions are safe as auxiliary only?
6. Which proposed automations must remain blocked?
7. Is there any parallel canonical claim outside the CKOS root governance?

Return:
- verdict: aprove / partially aprove / block;
- table of pattern, source, maturity, risk, action;
- conflicts;
- patch candidates;
- prohibited automation list;
- next PMO session recommendation.
```

### Acceptance Criteria

- No canonical promotion.
- No template rewrite.
- No enum rewrite.
- Parallel governance folders are treated as imported study context unless rooted in official CKOS governance.

### Expected Output

Documentation governance audit report.

### Risks

- Accidentally treating study proposal as official standard.
- Normalizing owners, approvals or tags without human review.
- Weakening RAW -> STUDY -> CANONICAL.

### Expected CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: claude_documentation_pattern_audit_readonly
mode: read-only
files_created: none
files_changed: none
files_not_touched: 00_SYSTEM_GOVERNANCE/*, canonical docs, research lab files
validation: study compared against official governance
risks_remaining: listed in audit
next_step: PMO chooses narrow patch candidate if needed
status: released
```

## 4. Prompt - Decide Whether Doc 27 Can Open

### Session Recommended

`claude_doc27_gate_decision_readonly`

### Intelligence Level Recommended

Highest.

### Mode

Read-only.

### Files To Read

- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md`
- `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`
- `07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/README.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/14_ACCEPTANCE_CRITERIA_FOR_DOC27.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/16_SMART_QUESTIONS_AND_CONTEXTUAL_INTERVENTION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/17_COGNIK_METACOGNIK_TASK_ORCHESTRATION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/18_AI_FIRST_PROJECT_NOTE_SYSTEM_AND_RAG_GOVERNANCE_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/19_FOUNDER_CONTROL_APPROVAL_BATCHES_AND_AUTONOMY_LEVELS_STUDY.md`

### Files Forbidden

- Creating Doc 27.
- Editing any canonical doc.
- Editing `ARCHITECTURE_PATCH_REPORT.md`.
- Editing governance docs.

### Prompt

```txt
Decide if Doc 27 can open, read-only.

Important:
You are not creating Doc 27. You are producing a gate recommendation.

Evaluate:
1. Are Docs 25 and 26 stable enough as dependencies?
2. Has Study Layer 13 answered the key scope question: task system, work order system, project operating system or orchestration architecture?
3. Are acceptance criteria for Doc 27 met?
4. Are required concepts already supported by Docs 02, 05, 06, 07, 09, 10, 11, 12 and 13?
5. Are ghost tables/services/events/projections unresolved?
6. Is the proposed Doc 27 title and purpose narrow enough?
7. What must be blocked before opening?

Return one of:
- OPEN_ALLOWED_WITH_SCOPE
- OPEN_BLOCKED_PENDING_AUDIT
- OPEN_BLOCKED_DEPENDENCY_GAP
- OPEN_BLOCKED_CANONIZATION_RISK

Include:
- exact recommended Doc 27 title if allowed;
- allowed sections;
- forbidden sections;
- required approvals;
- next smallest safe action.
```

### Acceptance Criteria

- Decision is explicit.
- No Doc 27 file is created.
- If blocked, blocker is concrete and actionable.
- If allowed, scope is narrow and non-implementation.

### Expected Output

Gate decision memo.

### Risks

- Opening a generic task doc.
- Hiding unresolved data/runtime dependencies.
- Letting study language become canonical without patch report.

### Expected CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: claude_doc27_gate_decision_readonly
mode: read-only
files_created: none
files_changed: none
files_not_touched: docs 27-34, canonical docs, ARCHITECTURE_PATCH_REPORT.md, backend/UI/runtime assets
validation: Doc 27 gate assessed
risks_remaining: listed in decision memo
next_step: Founder/PMO accepts, blocks or requests patch candidate
status: released
```

## 5. Prompt - Detect Ghost Tables, Services, Events And Projections

### Session Recommended

`claude_ghost_artifact_detection_readonly`

### Intelligence Level Recommended

Highest.

### Mode

Read-only.

### Files To Read

- `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md`
- `03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`
- `03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`
- `07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/16_SMART_QUESTIONS_AND_CONTEXTUAL_INTERVENTION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/17_COGNIK_METACOGNIK_TASK_ORCHESTRATION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/18_AI_FIRST_PROJECT_NOTE_SYSTEM_AND_RAG_GOVERNANCE_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/19_FOUNDER_CONTROL_APPROVAL_BATCHES_AND_AUTONOMY_LEVELS_STUDY.md`

### Files Forbidden

- All edits.
- Any schema/migration creation.
- Any service/API/projection implementation.

### Prompt

```txt
Detect ghost artifacts as read-only.

Definitions:
- Ghost table: a table or store implied by study/canonical text but not defined in Doc 11 or explicitly marked proposal.
- Ghost service: a service/engine/worker/API implied but not defined in Doc 10 or authorized implementation docs.
- Ghost event: an event name or event family implied but not present in canonical event model or marked proposal.
- Ghost projection: a UI/read model/projection implied but not defined in runtime/data docs.

Audit:
1. Extract every implied table, service, event and projection from the files read.
2. Mark each as canonical, proposed, missing, duplicate or forbidden.
3. Identify which document would own the missing definition if it became a patch candidate.
4. State whether each ghost blocks Doc 27.
5. Do not invent schemas.

Return a table:
artifact | type | source | canonical home | status | risk | action.
```

### Acceptance Criteria

- No artifacts are implemented.
- Missing artifacts are classified, not created.
- Doc ownership is suggested only as patch candidate.

### Expected Output

Ghost artifact register.

### Risks

- Turning implied fields into schema.
- Treating study examples as runtime commitments.
- Missing projection/data boundaries.

### Expected CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: claude_ghost_artifact_detection_readonly
mode: read-only
files_created: none
files_changed: none
files_not_touched: docs 01-26, docs 27-34, backend, UI, APIs, migrations, database
validation: ghost artifacts classified
risks_remaining: unresolved ghosts listed
next_step: PMO decides if ghost register becomes study patch candidate
status: released
```

## 6. Prompt - Review ROI By Task And Work Order

### Session Recommended

`claude_roi_work_order_review_readonly`

### Intelligence Level Recommended

High.

### Mode

Read-only.

### Files To Read

- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/09_ROI_AWARE_TASKS_NOTES_AND_QUESTIONS_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/19_FOUNDER_CONTROL_APPROVAL_BATCHES_AND_AUTONOMY_LEVELS_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_roi.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_tasks.md`

### Files Forbidden

- ROI canonical edits.
- Billing/credits edits.
- Task file edits unless a later patch session explicitly allows it.

### Prompt

```txt
Review ROI by task and work order, read-only.

Goal:
Determine whether Study Layer 13 can support ROI-aware task/work order decisions without turning ROI into bureaucracy.

Check:
1. Does every work order require a value hypothesis?
2. Are cost, risk, time, strategic value and reversibility represented?
3. Can Founder approve batches without approving blind execution?
4. Are low-ROI questions filtered out?
5. Are high-risk/high-value tasks escalated?
6. Does this align with Doc 21 ROI architecture?

Return:
- ROI adequacy verdict.
- Required ROI fields for future work orders.
- Anti-patterns.
- Doc 27 candidate language, if useful.
- Items to keep auxiliary.
```

### Acceptance Criteria

- ROI does not become automatic approval.
- No edits are made.
- Recommendations distinguish canonical candidate from auxiliary practice.

### Expected Output

ROI audit memo.

### Risks

- Overfitting every task to financial ROI.
- Ignoring risk/cost/reversibility.
- Treating ROI as permission to implement.

### Expected CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: claude_roi_work_order_review_readonly
mode: read-only
files_created: none
files_changed: none
files_not_touched: Doc 21, billing docs, tasks, canonical docs
validation: ROI-by-work-order model reviewed
risks_remaining: listed in memo
next_step: PMO decides whether ROI fields enter Doc 27 candidate
status: released
```

## 7. Prompt - Review Short, Mid And Long Memory

### Session Recommended

`claude_memory_hierarchy_review_readonly`

### Intelligence Level Recommended

High.

### Mode

Read-only.

### Files To Read

- `01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md`
- `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/04_NOTES_AS_OPERATIONAL_MEMORY_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/11_PROJECT_SELF_DOCUMENTATION_SYSTEM_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/12_RAG_METADATA_AND_VECTOR_CATEGORY_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/18_AI_FIRST_PROJECT_NOTE_SYSTEM_AND_RAG_GOVERNANCE_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md`

### Files Forbidden

- Data model edits.
- RAG implementation.
- Vector schema/migration creation.
- Memory rewrite in canonical docs.

### Prompt

```txt
Review memory hierarchy for Study Layer 13, read-only.

Goal:
Check whether short-term, mid-term and long-term memory are represented correctly across tasks, work orders, project notes and RAG.

Check:
1. What belongs in session memory?
2. What belongs in project/work order memory?
3. What belongs in organization/system memory?
4. What should be stored as note, evidence, decision, feedback or learning?
5. What should be retrievable by RAG and what should not?
6. Are provenance, confidence and tenant boundaries preserved?
7. Does any study text imply unapproved storage tables or vector categories?

Return:
- memory map;
- gaps;
- prohibited memory moves;
- Doc 27 candidate language;
- items requiring Doc 11 patch candidate.
```

### Acceptance Criteria

- Memory is not treated as canonical authority.
- No RAG/storage implementation is implied.
- Short/mid/long distinction is explicit.

### Expected Output

Memory hierarchy review.

### Risks

- Blending local memory with system memory.
- Vectorizing sensitive or unverified material.
- Treating notes as decisions.

### Expected CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: claude_memory_hierarchy_review_readonly
mode: read-only
files_created: none
files_changed: none
files_not_touched: memory canonical docs, data model, RAG/backend assets
validation: memory hierarchy reviewed
risks_remaining: listed in review
next_step: PMO decides whether memory map becomes patch candidate
status: released
```

## 8. Prompt - Review Smart Questions

### Session Recommended

`claude_smart_questions_review_readonly`

### Intelligence Level Recommended

High.

### Mode

Read-only.

### Files To Read

- `01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md`
- `02_EXECUTION_SYSTEM/07_WORKFLOW_BLUEPRINTS.md`
- `000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/02_INTELLIGENT_QUESTION_SYSTEM_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/08_FOUNDER_APPROVAL_BATCH_CONTROL_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/16_SMART_QUESTIONS_AND_CONTEXTUAL_INTERVENTION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/19_FOUNDER_CONTROL_APPROVAL_BATCHES_AND_AUTONOMY_LEVELS_STUDY.md`

### Files Forbidden

- Prompt library edits.
- Workflow edits.
- Approval policy edits.
- Any implementation.

### Prompt

```txt
Review smart questions as read-only.

Goal:
Determine whether CKOS smart questions are precise operational interventions rather than generic chatbot questions.

Check:
1. Does each question declare why it matters?
2. Does it affect ROI, risk, cost, governance, approval, scope, evidence, reversibility or memory?
3. Does it happen at the right time: before task creation, during planning, before approval, during execution or after feedback?
4. Are questions batched to protect Founder attention?
5. Can Claude identify bad questions that should be suppressed?
6. Are autonomy levels respected?

Return:
- smart question taxonomy;
- question quality rubric;
- suppression rules;
- Founder batch mode guidance;
- Doc 27 candidate language.
```

### Acceptance Criteria

- No generic question engine is approved.
- Questions are tied to concrete operational impact.
- Founder attention is protected.

### Expected Output

Smart questions review.

### Risks

- Turning CKOS into a chatbot loop.
- Asking too many low-value questions.
- Asking questions that imply approval.

### Expected CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: claude_smart_questions_review_readonly
mode: read-only
files_created: none
files_changed: none
files_not_touched: workflow docs, prompt library, autonomy docs, implementation files
validation: smart question model reviewed
risks_remaining: listed in review
next_step: PMO decides whether question rubric enters Doc 27 candidate
status: released
```

## 9. Prompt - Review Cognik And Metacognik

### Session Recommended

`claude_cognik_metacognik_review_readonly`

### Intelligence Level Recommended

Highest.

### Mode

Read-only.

### Files To Read

- `00_SYSTEM_GOVERNANCE/00_TAXONOMY_AND_NAMING.md`
- `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md`
- `01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md`
- `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/06_SUPERAGENT_AGENT_SUBAGENT_WORK_ALLOCATION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/17_COGNIK_METACOGNIK_TASK_ORCHESTRATION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/19_FOUNDER_CONTROL_APPROVAL_BATCHES_AND_AUTONOMY_LEVELS_STUDY.md`

### Files Forbidden

- New agent definitions.
- Runtime agent implementation.
- Taxonomy edits.
- Agent registry edits.

### Prompt

```txt
Review Cognik and Metacognik roles in Study Layer 13, read-only.

Goal:
Confirm whether Cognik and Metacognik are used according to official CKOS taxonomy and not expanded into unapproved agents.

Check:
1. Is Cognik limited to context, signal, pattern and briefing interpretation?
2. Is Metacognik limited to risk, confidence, reasoning quality, gap detection and approval pressure?
3. Does either become an executor by mistake?
4. Are PMO_CKOS, Founder, QA Lead and Builder Lead boundaries preserved?
5. Does the study imply new agents without skill, memory, gate and responsibility?
6. Are eval hooks and confidence controls mentioned enough?

Return:
- role integrity verdict;
- boundary violations;
- corrected role language;
- agent-vs-skill decisions;
- Doc 27 candidate language.
```

### Acceptance Criteria

- No new agent is created.
- Taxonomy freeze is respected.
- Cognik/Metacognik remain role-correct.

### Expected Output

Cognik/Metacognik role audit.

### Risks

- Agent theater.
- Metacognik becoming an implementation approver.
- Cognik becoming a hidden orchestrator outside runtime policy.

### Expected CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: claude_cognik_metacognik_review_readonly
mode: read-only
files_created: none
files_changed: none
files_not_touched: taxonomy, agent model, runtime docs, implementation files
validation: Cognik/Metacognik roles reviewed
risks_remaining: listed in audit
next_step: PMO decides whether corrected role language becomes candidate
status: released
```

## 10. Prompt - Generate Final PMO Report

### Session Recommended

`claude_final_pmo_report_patch_study_only`

### Intelligence Level Recommended

Highest.

### Mode

Patch, study-only, only if Founder/PMO explicitly provides an allowed output path inside `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/`.

Recommended output file if approved later:

`000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/21_CLAUDE_FINAL_PMO_AUDIT_REPORT_STUDY.md`

### Files To Read

- All audit outputs produced by prompts 1-9, if available.
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/README.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/14_ACCEPTANCE_CRITERIA_FOR_DOC27.md`
- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md`

### Files Forbidden

- Every file except the explicitly approved study output file.
- Docs 01-26.
- Docs 27-34.
- `ARCHITECTURE_PATCH_REPORT.md`.
- `00_SYSTEM_GOVERNANCE/*`.
- Backend, UI, API, database, migrations, n8n JSONs and runtime agent files.

### Prompt

```txt
Generate final PMO report from Claude audits.

Mode:
Patch only the approved study output file. If no output file is explicitly approved, operate read-only and print the report in chat.

Goal:
Synthesize audit findings from Doc 26, Study Layer 13, documentation pattern normalization, Doc 27 gate, ghost artifacts, ROI, memory, smart questions and Cognik/Metacognik.

Required report sections:
1. Executive verdict.
2. What is safe now.
3. What remains blocked.
4. Doc 27 gate recommendation.
5. Ghost artifact register summary.
6. Candidate patch list.
7. Prohibited automation list.
8. Five-session operating plan for Founder.
9. Open questions requiring Founder/PMO decision.
10. CHECKOUT RELEASE.

Rules:
- Do not create or edit canonical docs.
- Do not open Doc 27.
- Do not claim approval.
- Do not hide uncertainty.
- Every recommendation must be marked: study-only, patch_candidate, blocked or canonical_dependency.
```

### Acceptance Criteria

- Report is study-only.
- Report distinguishes recommendation from approval.
- Report names exact blockers before Doc 27.
- Report includes checkout release.

### Expected Output

One final PMO audit report in the approved study file or chat if no patch permission is given.

### Risks

- Treating synthesis as canonical approval.
- Bundling too many patch candidates into one unsafe patch.
- Letting final report open implementation work.

### Expected CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: claude_final_pmo_report_patch_study_only
mode: patch or read-only fallback
files_created: only approved study output file, if any
files_changed: only approved study output file, if any
files_not_touched: docs 01-26, docs 27-34, ARCHITECTURE_PATCH_REPORT.md, 00_SYSTEM_GOVERNANCE/*, backend, UI, APIs, migrations, database, n8n JSONs
validation: final report generated as study-only synthesis
risks_remaining: listed in report
next_step: Founder/PMO chooses one narrow next session
status: released_with_risks
```

## Como O Founder Deve Operar 5 Sessoes Simultaneas Sem Conflito

### Core Rule

Five simultaneous sessions can run only if each session has a distinct scope, distinct output, distinct forbidden files and a checkout release. No session may infer permission from another session.

### Recommended Five-Session Layout

| Slot | Session | Mode | Output | Conflict Boundary |
|---|---|---|---|---|
| 1 | Doc 26 audit | read-only | audit memo in chat | no edits |
| 2 | Study Layer 13 audit | read-only | study audit memo in chat | no edits |
| 3 | Ghost artifact detection | read-only | ghost register in chat | no schemas or migrations |
| 4 | ROI/memory/questions/Cognik review | read-only | combined review memo in chat | no prompt/workflow/runtime edits |
| 5 | Final PMO synthesis | patch only if approved | one study report file | only approved Study Layer 13 output |

### Founder Operating Steps

1. Assign one session_id per Claude chat.
2. Give each session exactly one prompt from this pack.
3. Require each session to repeat its allowed files and forbidden files before work.
4. Do not allow two sessions to write in the same file.
5. Keep sessions 1-4 read-only by default.
6. Allow session 5 to patch only after sessions 1-4 finish.
7. Reject any answer that asks to edit canonical docs, open Doc 27, create backend, generate migrations or update patch reports.
8. Ask every session to end with CHECKOUT RELEASE.
9. Compare releases before deciding the next PMO action.
10. Approve only one next narrow patch candidate at a time.

### Collision Rules

- If two sessions propose different Doc 27 scopes, do not merge them automatically. Ask PMO_CKOS to classify the conflict.
- If any session finds ghost artifacts, Doc 27 remains blocked until the ghost register is reviewed.
- If any session implies backend/UI/runtime work, mark that output as implementation_drift.
- If any session treats study as canonical, discard the authority claim and preserve only the useful evidence.
- If final synthesis cannot reconcile the audits, next session must be read-only conflict resolution.

### Minimum Founder Decision Template

```txt
Decision:
Approved next action:
Allowed output file:
Forbidden files:
Mode:
Required reviewers:
Reason:
Risks accepted:
Risks rejected:
Expiration:
```

## CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: Codex - Prompt Pack Generator for Claude Audits
mode: patch
allowed_scope:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/20_PROMPT_PACK_FOR_MULTI_SESSION_CLAUDE_AUDITS_STUDY.md
files_created:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/20_PROMPT_PACK_FOR_MULTI_SESSION_CLAUDE_AUDITS_STUDY.md
files_changed: none
files_not_touched:
  - docs 01-26
  - docs 27-34
  - ARCHITECTURE_PATCH_REPORT.md
  - 00_SYSTEM_GOVERNANCE/*
  - backend
  - UI
  - APIs
  - migrations
  - database
  - n8n JSONs
  - real agents
validation:
  - created only the requested study-only prompt pack
  - included 10 Claude audit prompts
  - included session, intelligence level, mode, files to read, forbidden files, acceptance criteria, expected output, risks and CHECKOUT RELEASE for each prompt
  - included Founder five-session operating section
risks_remaining:
  - prompts are operational guidance only and require explicit Founder/PMO scope before use
  - patch-mode final report prompt must not run without approved output file
next_step:
  - Founder selects one Claude prompt/session and runs it with read-only default
status: released
```
