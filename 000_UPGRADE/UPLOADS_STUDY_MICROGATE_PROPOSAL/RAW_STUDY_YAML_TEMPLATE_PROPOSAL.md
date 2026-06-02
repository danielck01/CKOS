---
title: RAW/STUDY YAML Template Proposal
file: RAW_STUDY_YAML_TEMPLATE_PROPOSAL.md
system_id: raw_study_yaml_template_proposal
display_name: RAW/STUDY YAML Template Proposal
doc_type: template_proposal
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
  - metacognik
source_type: template_review
source_path: 00_SYSTEM_GOVERNANCE/00_DOCUMENT_TEMPLATE.md
source_tool: codex
provenance_status: verified
project: ckos
related_docs:
  - 00_SYSTEM_GOVERNANCE/00_DOCUMENT_TEMPLATE.md
  - 00_SYSTEM_GOVERNANCE/00_TAXONOMY_AND_NAMING.md
related_notes: []
tags: [yaml, template, raw, study, governance]
risk_level: medium
confidence: medium
canonical_change: false
---

# RAW/STUDY YAML Template Proposal

## 1. Executive lock

This is a template proposal only. It does not patch `00_DOCUMENT_TEMPLATE.md`.

## 2. Current template gap

The current `00_DOCUMENT_TEMPLATE.md` is strong for canonical architecture documents, but RAW/STUDY needs extra metadata:

- layer;
- source provenance;
- source tool;
- confidence;
- risk;
- source path;
- project;
- doc type;
- created/updated dates.

Without these fields, RAW/STUDY notes become difficult to filter, unsafe for RAG, and ambiguous for agents.

## 3. Proposed YAML

```yaml
---
title:
file:
system_id:
display_name:
doc_type: study_note
category:
layer: study
status: draft
version: 0.1.0
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - metacognik
approval_required:
  - founder
source_type:
source_path:
source_tool:
provenance_status: unverified
project: ckos
related_docs: []
related_notes: []
tags: []
risk_level: medium
confidence: unverified
---
```

## 4. Proposed enums

```txt
layer:
- raw
- study
- canonical

doc_type:
- upload_note
- study_note
- source_manifest
- patch_candidate
- decision_log
- canonical_doc

confidence:
- unverified
- low
- medium
- high

risk_level:
- low
- medium
- high
- critical

provenance_status:
- unverified
- partial
- verified
- disputed
- expired
```

## 5. Compatibility with current template

Compatible fields:

```txt
title, file, category, status, version, owner, responsible_agent,
reviewers, approval_required, related_notes, tags
```

New fields required:

```txt
system_id, display_name, doc_type, layer, created_at, updated_at,
source_type, source_path, source_tool, provenance_status, project,
related_docs, risk_level, confidence
```

## 6. Dangerous fields

| Field | Risk | Rule |
|---|---|---|
| `confidence` | AI output overtrusted | AI output defaults to `unverified` |
| `source_tool` | Tool confused with source | Tool is not source of truth |
| `provenance_status` | Premature verification | `verified` requires review |
| `layer` | Study confused with canonical | Only canonical docs are official |
| `approval_required` | Approval implied too early | Approval must be explicit and logged |

## 7. Fields that belong in body, not YAML

Keep these as body sections:

- long summary;
- detailed evidence;
- risks;
- open questions;
- decision alternatives;
- PMO recommendation;
- next action;
- proposed patch details.

YAML should stay indexable and concise.

## 8. RAG impact

Positive impact:

- agents can filter by `layer`;
- RAW can be excluded from canonical retrieval;
- confidence-aware retrieval becomes possible;
- provenance-aware synthesis becomes possible;
- patch candidates can be separated from official docs.

Required RAG rule:

```txt
canonical > approved study note > study note > raw note > raw file
```

## 9. Agent impact

Agents must treat:

- `layer: raw` as material only;
- `confidence: unverified` as non-factual;
- `source_tool: manus/chatgpt/claude/codex/antigravity` as generation source, not truth source;
- `doc_type: patch_candidate` as proposal, not permission.

## 10. Recommended patch to canonical template

After Founder approval, patch `00_DOCUMENT_TEMPLATE.md` with:

- a new section for RAW/STUDY note templates;
- enum additions;
- RAG hierarchy rule;
- QA checklist for RAW/STUDY notes.

Do not alter canonical document requirements for docs 00-24 in the same patch unless explicitly approved.
