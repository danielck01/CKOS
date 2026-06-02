---
title: Proposed 000 Uploads Structure
file: PROPOSED_000_UPLOADS_STRUCTURE.md
system_id: proposed_000_uploads_structure
display_name: Proposed 000_UPLOADS Structure
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
  - 00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md
  - 00_SYSTEM_GOVERNANCE/00_DOCUMENT_TEMPLATE.md
  - 00_SYSTEM_GOVERNANCE/00_TAXONOMY_AND_NAMING.md
  - CKOS_FOLDER_MEMORY.md
related_notes: []
tags: [uploads, raw_layer, governance, provenance, pmo]
risk_level: medium
confidence: medium
canonical_change: false
---

# Proposed 000_UPLOADS Structure

## 1. Executive lock

This file is a proposal only. It does not create `000_UPLOADS/`, does not move files, does not promote uploads to canonical documentation, and does not authorize implementation.

## 2. Purpose

Define the future RAW layer for CKOS knowledge intake.

RAW receives material. RAW does not interpret, decide, approve, or canonize.

## 3. Proposed tree

```txt
000_UPLOADS/
|-- README.md
|-- _folder_memory.md
|-- 00_INBOX_RAW/
|-- 01_SOURCE_DOCUMENTS/
|-- 02_RESEARCH_AND_BENCHMARKS/
|-- 03_TECH_REFERENCES/
|-- 04_BUSINESS_LEGAL_REFERENCES/
|-- 05_UI_UX_REFERENCES/
|-- 06_AI_TOOL_OUTPUTS/
|   |-- chatgpt/
|   |-- claude/
|   |-- codex/
|   |-- manus/
|   |-- antigravity/
|   `-- other/
|-- 07_CLIENT_PROJECT_INPUTS/
|-- 08_MEDIA_AND_TRANSCRIPTS/
|-- 09_DATASETS_AND_TABLES/
|-- 10_CONNECTOR_EXPORTS/
|-- 90_READY_FOR_STUDY/
`-- 99_ARCHIVE/
```

## 4. Global rules

- Every folder must contain `README.md` and `_folder_memory.md`.
- RAW files are not source of truth.
- Every RAW item needs provenance.
- Every RAW item with PII must be classified before analysis.
- AI outputs enter with `confidence: unverified` by default.
- Connector exports must be checked for tokens, provider ids, actor ids, PII, and tenant leakage.
- Nothing moves to CANONICAL from RAW.
- RAW can only move to STUDY.

## 5. Naming rule

```txt
YYYYMMDD_source-tool_topic_owner_status.ext
```

Example:

```txt
20260527_manus_mcp-connectors-research_pmo_ckos_raw.md
```

Allowed status suffixes:

```txt
raw | triaged | ready_for_study | archived | rejected
```

## 6. Folder policy matrix

| Folder | Function | Allowed | Prohibited | Main risk | Move to STUDY when | Archive when | Owner | Related docs |
|---|---|---|---|---|---|---|---|---|
| `00_INBOX_RAW` | Temporary intake | Unsorted uploads | Long-term storage | Infinite junk drawer | Source and category identified | Duplicate/invalid | pmo_ckos | docs 00, 18 |
| `01_SOURCE_DOCUMENTS` | Original docs | PDF, DOCX, MD, notes | Edited derivatives | Missing provenance | Source manifest exists | Superseded or irrelevant | pmo_ckos | docs 05, 18 |
| `02_RESEARCH_AND_BENCHMARKS` | Research material | Reports, benchmarks | Unsourced claims as fact | Opinion becomes truth | Evidence map exists | Low relevance | pmo_ckos | docs 18, 21 |
| `03_TECH_REFERENCES` | Technical references | Official docs, specs | Production code | Copying external architecture | Technical summary exists | Outdated standard | technical | docs 10-13 |
| `04_BUSINESS_LEGAL_REFERENCES` | Business/legal refs | Pricing, legal, policy | Legal advice as final | Compliance error | Legal/business risk classified | Expired regulation | pmo_ckos | docs 12, 24 |
| `05_UI_UX_REFERENCES` | Visual refs | Screens, flows, moodboards | UI implementation | UI starts too early | Design study note created | Off-brand/stale | pmo_ckos | docs 14-16, future 32-33 |
| `06_AI_TOOL_OUTPUTS` | AI outputs | ChatGPT, Claude, Codex, Manus, Antigravity outputs | Treating AI as source | AI hallucination | Human study note exists | Contradicted/unusable | pmo_ckos | docs 18, 19 |
| `07_CLIENT_PROJECT_INPUTS` | Client inputs | Briefings, assets, docs | Public sharing | PII/client leakage | PII classified and summarized | Consent missing | pmo_ckos | docs 12, 20 |
| `08_MEDIA_AND_TRANSCRIPTS` | Media sources | Audio/video transcripts, screenshots | Copyright misuse | Inaccurate transcript | Transcript reviewed | Bad source/no rights | pmo_ckos | docs 18 |
| `09_DATASETS_AND_TABLES` | Data inputs | CSV, XLSX, exports | Production DB dumps | Dirty data | Schema/data note exists | Unusable/unsafe | datta | docs 11, 13 |
| `10_CONNECTOR_EXPORTS` | Raw connector outputs | API exports, collector dumps | Secrets, tokens, actor ids | Credential leak | Redaction + source manifest done | Unsafe or stale | technical | docs 10, 12, future 26-27 |
| `90_READY_FOR_STUDY` | Staging for study | Triaged items | Canonical docs | Promotion shortcut | Study note assigned | Idle > review window | pmo_ckos | future 28-29 |
| `99_ARCHIVE` | Frozen material | Rejected/stale/duplicates | Active material | Old material returns | Not applicable | Already archived | pmo_ckos | CKOS_FOLDER_MEMORY |

## 7. PII policy

PII must be classified as one of:

```txt
none | possible | confirmed | sensitive
```

Files with `possible`, `confirmed`, or `sensitive` PII cannot be sent to external tools without explicit policy approval.

## 8. Provenance policy

Every uploaded item must answer:

- who/what produced it;
- when it was produced;
- where it came from;
- whether it is original, copied, generated, exported, or transformed;
- whether commercial/project use is permitted;
- whether a source can be rechecked later.

## 9. Required folder README fields

Each `README.md` should include:

- function;
- what can enter;
- what cannot enter;
- naming rule;
- when to move to STUDY;
- when to archive;
- main risk;
- PII policy;
- provenance policy;
- owner;
- related docs.

## 10. Approval status

Pending Founder approval. No folder should be created in canonical root until this proposal is approved.
