---
title: 12 Session Gates - README
system_id: study_notes_session_gates_readme_20260528
layer: auxiliary
phase: 000_STUDY_NOTES
category: folder_readme
status: auxiliary
version: 0.1.0
owner: pmo_ckos
responsible_agent: codex
reviewers:
  - founder
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
confidence: unverified
provenance_status: unverified
source_tool: codex
created_at: 2026-05-28
purpose: Govern formal gates for specialized sessions without granting canonical or implementation authority.
inputs:
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
  - 000_ROADMAPS/SESSION_REGISTRY.md
outputs:
  - session gate notes
  - approval conditions
  - blocked/allowed output boundaries
tags:
  - session_gates
  - study
  - auxiliary
---

# 12 Session Gates

## Purpose

This folder stores auxiliary formal gates for specialized sessions. It is not canonical and does not authorize implementation.

## Current Gates

| file | purpose | status |
|---|---|---|
| `01_ANTIGRAVITY_STUDY_MODE_GATE.md` | Define the required gate before Antigravity may operate in Design Study Session. | created; activation requires explicit Founder approval |
| `ck_memory.md` | Active folder memory for session gates. | active |
| `_folder_memory.md` | Legacy/superseded folder memory preserved from P1.7. | legacy |

## Rules

- Gates in this folder are study/governance controls, not canonical approvals by themselves.
- No gate here may create docs 26-34.
- No gate here may start UI/UX implementation, backend, API, database, migrations, JSONs n8n or real agents.
- Antigravity remains blocked until the specific gate is approved for activation by Founder.

## Minimum Reading Order

1. `000_ROADMAPS/SESSION_REGISTRY.md`
2. `000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md`
3. This `README.md`
4. `ck_memory.md`
5. The specific gate note

`_folder_memory.md` is preserved only as legacy/superseded history.
