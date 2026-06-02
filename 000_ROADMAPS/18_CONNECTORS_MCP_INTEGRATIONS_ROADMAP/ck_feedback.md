---
title: "Connectors MCP Integrations Roadmap - Feedback"
system_id: roadmap_18_connectors_mcp_integrations_ck_feedback
layer: auxiliary
phase: 000_ROADMAPS
category: roadmap
status: draft
version: 1.0.0
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
created_at: 2026-05-28
purpose: "Collect feedback, decisions, rejections and pending adjustments for the connectors MCP integrations roadmap."
inputs:
  - "000_ROADMAPS/README.md"
  - "000_ROADMAPS/ck_memory.md"
  - "000_ROADMAPS/ck_tasks.md"
  - "000_ROADMAPS/ck_risks.md"
  - "000_ROADMAPS/ck_agent_handoffs.md"
  - "../ck_agent_handoffs.md"
  - "../04_CONNECTORS_MCP_INTEGRATIONS_ROADMAP/README.md"
  - "../../02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md"
outputs:
  - "governed auxiliary roadmap for connectors MCP integrations"
  - "approval-ready tasks"
  - "risk and ROI traceability"
  - "handoff-ready context pack"
framework:
  - "Intent -> Question -> Plan -> Execution"
  - "SPCCAE"
  - "one agent writes and another audits"
  - "Security / Governance / Cost / Approval Impact"
edge_cases:
  - "roadmap treated as canonical authority"
  - "agent starts implementation from study material"
  - "duplicate scope with earlier roadmap folders"
  - "context pack grows beyond task need"
  - "approval bypass"
integrations:
  - "MCP (planning only)"
  - "connectors (planning only)"
  - "APIs (planning only)"
  - "webhooks (planning only)"
  - "Apify (planning only)"
  - "Perplexity or OpenRouter (planning only)"
  - "PubMed (planning only)"
  - "Google Drive (planning only)"
  - "GitHub (planning only)"
  - "Stripe (planning only)"
  - "Calendar (planning only)"
  - "n8n as prototype only (planning only)"
prompts:
  - "Read README.md and ck_memory.md before action."
  - "Ask Founder approval before any patch outside this folder."
  - "Show ROI, risk, cost and consequence for every major question."
metrics:
  - "all seven root controls exist"
  - "0 canonical docs changed"
  - "0 implementation files changed"
  - "YAML valid"
  - "handoff rules visible"
related_notes:
  - "../README.md"
  - "../ck_memory.md"
  - "../ck_agent_handoffs.md"
  - "../04_CONNECTORS_MCP_INTEGRATIONS_ROADMAP/README.md"
  - "../../02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md"
tags:
  - "roadmap"
  - "auxiliary"
  - "p1_missing_roadmaps"
  - "18_connectors_mcp_integrations"
  - "ck_feedback"
---
# Connectors MCP Integrations Roadmap - Feedback

## Founder

- P1 creation authorized as auxiliary roadmap completion only.
- Future expansion requires explicit approval.

## PMO_CKOS

- Pending review: reconcile overlap with existing 00-13 roadmap folders.
- Pending review: validate task sizing and risk register before P2.

## Metacognik

- Pending review: check for duplicated concepts, premature implementation language and context cost creep.

## QA

- Pending review: YAML validity, file existence and no forbidden changes.

## Agent Executors

- Executors may only act on a checkout-locked, Founder-approved task pack.

## Decisions Approved

- Auxiliary layer only.
- No canonical authority.
- No implementation.
- Minimum context before agent action.

## Rejections

- Antigravity execution remains rejected for this phase.
- UI implementation remains rejected for this phase.
- Backend, API, database, connector and real agent work remain rejected.

## Pending Adjustments

- Add detailed milestones only after PMO review.
- Link acceptance criteria only after overlap reconciliation.
