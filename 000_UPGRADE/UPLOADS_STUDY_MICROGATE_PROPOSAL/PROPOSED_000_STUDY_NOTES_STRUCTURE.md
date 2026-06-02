---
title: Proposed 000 Study Notes Structure
file: PROPOSED_000_STUDY_NOTES_STRUCTURE.md
system_id: proposed_000_study_notes_structure
display_name: Proposed 000_STUDY_NOTES Structure
doc_type: structure_proposal
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
  - metacognik
approval_required:
  - founder
source_type: governance_review
source_path: CKOS_DOCUMENTATION_REVIEWED
source_tool: codex
provenance_status: verified
project: ckos
related_docs:
  - 00_SYSTEM_GOVERNANCE/00_DOCUMENT_TEMPLATE.md
  - 00_SYSTEM_GOVERNANCE/00_TAXONOMY_AND_NAMING.md
  - 05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL.md
  - 05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md
related_notes: []
tags: [study_notes, working_notes, governance, pmo]
risk_level: medium
confidence: medium
canonical_change: false
---

# Proposed 000_STUDY_NOTES Structure

## 1. Executive lock

This file is a proposal only. It does not create `000_STUDY_NOTES/`, does not promote content, and does not modify canonical docs.

## 2. Purpose

Define the STUDY layer: the interpretation layer between RAW uploads and CANONICAL documentation.

STUDY transforms material into structured notes with evidence, risks, gaps, hypotheses, confidence, and PMO recommendation.

## 3. Proposed tree

```txt
000_STUDY_NOTES/
|-- README.md
|-- _folder_memory.md
|-- 00_INBOX_FOR_REVIEW/
|-- 01_UPLOAD_STUDY_NOTES/
|-- 02_RESEARCH_SYNTHESIS/
|-- 03_MCP_CONNECTORS_INTEGRATIONS/
|-- 04_UI_UX_STUDY/
|-- 05_BUSINESS_SYSTEMS_STUDY/
|-- 06_CLIENT_PROJECT_STUDY/
|-- 07_CANONICAL_PATCH_CANDIDATES/
|-- 08_DECISION_LOGS/
|-- 09_APPROVED_FOR_CANONICAL_PATCH/
`-- 99_ARCHIVE/
```

## 4. Hard rule

`09_APPROVED_FOR_CANONICAL_PATCH/` does not mean canonical.

It means ready for patch plan.

## 5. Required flow

```txt
raw upload
-> triage
-> source manifest
-> study note YAML
-> PMO review
-> Metacognik/Technical/Legal review when applicable
-> patch candidate
-> patch plan
-> Founder approval
-> canonical doc patch
-> QA documentation check
-> Architecture Patch Report entry
```

## 6. Folder policy matrix

| Folder | Function | Allowed | Prohibited | Main risk | Exit rule | Owner |
|---|---|---|---|---|---|---|
| `00_INBOX_FOR_REVIEW` | Incoming study work | Assigned raw items | Long-term storage | Study backlog rot | Move to specific folder after triage | pmo_ckos |
| `01_UPLOAD_STUDY_NOTES` | Study notes from uploads | RAW interpretation notes | Canonical patches | Weak provenance | Promote to synthesis or archive | pmo_ckos |
| `02_RESEARCH_SYNTHESIS` | Cross-source synthesis | Multi-source research notes | Single-source truth claims | Overconfidence | Move to patch candidate if actionable | pmo_ckos |
| `03_MCP_CONNECTORS_INTEGRATIONS` | MCP/connectors study | Protocol and integration notes | Runtime implementation | Tool bypass | Future docs 26-27 candidate | technical |
| `04_UI_UX_STUDY` | Visual/product study | References, patterns, principles | UI implementation | Premature UI | Future docs 32-33 candidate | pmo_ckos |
| `05_BUSINESS_SYSTEMS_STUDY` | Business systems study | ROI, feedback, support, billing notes | Rewriting docs 21-24 | Recreating completed docs | Patch candidate only if gap found | pmo_ckos |
| `06_CLIENT_PROJECT_STUDY` | Client/project study | Briefing interpretation, risks | Client-facing final docs | PII leakage | Project pack after approval | pmo_ckos |
| `07_CANONICAL_PATCH_CANDIDATES` | Candidate changes | Proposed canonical changes | Direct edits | Patch without approval | Move to approved queue after review | pmo_ckos |
| `08_DECISION_LOGS` | Decision tracking | PMO/Founder decisions | Informal chat dumps | Missing decision rights | Reference in patch plan | pmo_ckos |
| `09_APPROVED_FOR_CANONICAL_PATCH` | Ready for patch plan | Reviewed candidates | Canonical source | Misread as official | Patch plan required | pmo_ckos |
| `99_ARCHIVE` | Closed notes | Rejected/stale notes | Active notes | Old claims returning | Not applicable | pmo_ckos |

## 7. Standard body sections

Every study note should include:

- Purpose;
- Context;
- Source analyzed;
- What this material reveals;
- What this changes in CKOS;
- Possible decisions;
- Risks;
- Open questions;
- PMO recommendation;
- Next action;
- Related notes.

## 8. Promotion criteria

A study note can become a patch candidate only if it has:

- valid YAML;
- provenance;
- confidence level;
- risk level;
- related canonical docs;
- explicit PMO recommendation;
- clear proposed destination;
- review requirement.

## 9. Rejection criteria

Reject or archive when:

- source cannot be identified;
- PII is unsafe;
- claim is contradicted by canonical docs;
- material is implementation disguised as documentation;
- material pushes UI/backend before gates;
- output of AI lacks supporting source.

## 10. Approval status

Pending Founder approval. No STUDY folder should be created in the canonical root until this proposal is approved.
