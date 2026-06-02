---
title: Docs 25-34 Sequence Proposal
file: DOCS_25_34_SEQUENCE_PROPOSAL.md
system_id: docs_25_34_sequence_proposal
display_name: Docs 25-34 Sequence Proposal
doc_type: sequence_proposal
category: governance_proposal
layer: study
status: draft
version: 0.1.0
created_at: 2026-05-27
updated_at: 2026-05-27
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - founder
  - technical
  - metacognik
approval_required:
  - founder
  - technical
  - metacognik
source_type: governance_review
source_path: CKOS_DOCUMENTATION_REVIEWED
source_tool: codex
provenance_status: verified
project: ckos
related_docs:
  - 00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md
  - 00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md
  - CKOS_FOLDER_MEMORY.md
  - ARCHITECTURE_PATCH_REPORT.md
related_notes: []
tags: [docs_25_34, roadmap, governance, pmo]
risk_level: high
confidence: medium
canonical_change: false
---

# Docs 25-34 Sequence Proposal

## 1. Executive lock

This file proposes sequence only. It does not create docs 25-34, does not rename Self-Evolving, and does not patch canonical docs.

## 2. Current state

- Docs 00-24 exist.
- Business Systems docs 21-24 exist in `06_BUSINESS_SYSTEMS/`.
- Gate I is documentally complete.
- Implementation remains blocked.
- UI/UX remains blocked.
- Self-Evolving has numbering conflict and must not be renamed yet.

## 3. Recommended sequence

```txt
25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md
26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md
27_COLLECTOR_REGISTRY_AND_RESEARCH_ACTORS_ARCHITECTURE.md
28_KNOWLEDGE_INGESTION_UPLOADS_AND_SOURCE_GOVERNANCE_ARCHITECTURE.md
29_STUDY_NOTES_AND_LEARNING_MODE_ARCHITECTURE.md
30_CLIENT_PROJECT_PLANNER_AND_SELF_DOCUMENTING_PROJECTS_ARCHITECTURE.md
31_CK_STORE_AND_CAPABILITY_MARKETPLACE_ARCHITECTURE.md
32_UI_UX_SYSTEM_ARCHITECTURE.md
33_DESIGN_SYSTEM_MOTION_AND_VISUAL_PIPELINE_ARCHITECTURE.md
34_FINAL_IMPLEMENTATION_READINESS_GATE.md
```

## 4. Rationale

UI/UX should wait until docs 32-33 because earlier docs define:

- source intake;
- evidence governance;
- MCP and connector safety;
- collector registry;
- study notes;
- project self-documentation;
- capability marketplace;
- approval and readiness gate.

Creating UI before these decisions risks building screens that call the wrong tools, expose unsafe data, imply unapproved capabilities, or turn visual references into product decisions.

## 5. Doc-by-doc scope

| Doc | Scope | Why before UI |
|---|---|---|
| 25 Self-Evolving | Controlled evolution, sandbox, evals, approval | Prevents autonomy theater |
| 26 Connectors/MCP/Integrations | Integration decision matrix and safety rules | UI cannot expose unsafe actions |
| 27 Collector Registry | Collector/Actor/Provider, reliability, cost | UI must not expose provider/actor |
| 28 Knowledge Ingestion/Uploads | RAW layer, provenance, PII, source governance | UI upload flows depend on this |
| 29 Study Notes/Learning Mode | STUDY layer, learning, canonical promotion | UI learning surfaces depend on this |
| 30 Client Project Planner | Self-documenting projects, briefing, plans | Project UX depends on object flow |
| 31 CK Store/Marketplace | Capabilities, add-ons, credits | UI needs capability gating |
| 32 UI/UX System | Surfaces, widgets, command center, cockpit | Can now project governed runtime |
| 33 Design/Motion/Visual Pipeline | Design system, motion, visual prompts | Visual layer after UX architecture |
| 34 Final Readiness Gate | Final pre-implementation gate | Prevents premature build |

## 6. Dependency proposal

```txt
25 depends on 10, 12, 13, 04, 17, 20
26 depends on 10, 11, 12, 13, 18, 19
27 depends on 10, 11, 12, 13, 18, 26
28 depends on 05, 10, 11, 12, 18, 26, 27
29 depends on 05, 08, 13, 18, 28
30 depends on 07, 10, 15, 18, 20, 21-24, 29
31 depends on 10, 12, 13, 24, 26, 27, 30
32 depends on 14, 15, 16, 26-31
33 depends on 32 and visual study notes
34 depends on 25-33
```

## 7. Taxonomy question

Founder must decide where docs 25-34 live:

- Option A: create a new `07_GOVERNED_KNOWLEDGE_AND_CAPABILITIES/` layer;
- Option B: distribute across existing phases;
- Option C: create `07_NEXT_PHASE_SYSTEMS/` as temporary canonical phase.

PMO recommendation: Option A is cleaner if the Founder approves a new canonical phase. Until then, keep proposals in `000_UPGRADE`.

## 8. Approval status

Pending Founder approval. No docs 25-34 should be created until this sequence is approved.
