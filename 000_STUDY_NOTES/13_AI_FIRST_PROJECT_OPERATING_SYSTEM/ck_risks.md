---
title: AI-first Project Operating System Risks
file: ck_risks.md
layer: study
phase: 000_STUDY_NOTES
category: ai_first_project_operating_system_risks
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
purpose: Register risks for the AI-first project operating system study layer.
inputs:
  - README.md
  - 03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
outputs:
  - study risk register
framework:
  - identify
  - classify
  - mitigate
  - audit
edge_cases:
  - premature implementation
  - self-approval by executor
  - cross-session conflict
integrations:
  - PMO_CKOS
  - Metacognik
prompts:
  - Treat every future runtime idea as candidate-only.
metrics:
  - zero forbidden files modified
  - zero canonical docs created
related_notes:
  - 14_ACCEPTANCE_CRITERIA_FOR_DOC27.md
tags:
  - risks
  - governance
  - study
---

# Risk Register

| Risk | Severity | Control |
|---|---|---|
| Generic task-list drift | high | Require every task concept to include intent, question, context, risk, cost, ROI, approval, evidence, feedback and learning. |
| Premature Doc 27 creation | high | Keep candidates in note 13; require PMO/Metacognik audit first. |
| Agent pack created too early | high | Study roles only; do not create real agent folders or runtime agents. |
| Antigravity activation from study language | high | Antigravity remains blocked until separate Founder-approved gate. |
| Windsurf registered as `specialist_unregistered` | high | Windsurf pode ser usado como leitura, brainstorming ou suporte auxiliar, mas não como executor governado sem gate equivalente ao Antigravity. |
| Implementation leakage | high | No UI, backend, API, database, migrations, MCP server, n8n JSON or automation. |
| Notes become ungoverned memory | medium | Require YAML, source references, confidence and provenance on every note. |
| Questions become conversation noise | medium | Require why, decision, risk, ROI and consequence for every intelligent question. |
| ROI treated only as money | medium | Use operational ROI: entropy, context cost, traceability, reuse, learning and decision quality. |
| Parallel sessions conflict | medium | Apply one writer, checkout lock, release log and auditor session. |
| Canonical candidates too broad | medium | Separate Doc 27 candidates from deferred Docs 28-30 candidates. |

## Residual Risk

This layer is intentionally broad. Its value depends on external audit narrowing what becomes Doc 27.
