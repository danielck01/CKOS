---
title: "Connectors MCP Integrations Roadmap - Memory"
system_id: roadmap_18_connectors_mcp_integrations_ck_memory
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
purpose: "Maintain live operational memory for the connectors MCP integrations auxiliary roadmap."
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
  - "ck_memory"
---
# Connectors MCP Integrations Roadmap - Memory

## Current State

This roadmap was created during P1 Missing Roadmaps Completion as a draft auxiliary planning lane. It is ready for PMO review and later Founder-approved expansion.

## Approved Decisions

- Keep this roadmap auxiliary, not canonical.
- Keep implementation blocked until a future explicit gate.
- Use minimum context before asking agents to act.
- Require checkout lock before any write operation.

## Files Created

- README.md
- ck_memory.md
- ck_tasks.md
- ck_risks.md
- ck_roi.md
- ck_feedback.md
- ck_agent_handoffs.md

## Dependencies

- MCP
- connectors
- APIs
- webhooks
- Apify
- Perplexity or OpenRouter
- PubMed
- Google Drive
- GitHub
- Stripe
- Calendar
- n8n as prototype only

## Do Not Do

- connector implementation
- API credential use
- webhook creation
- n8n production workflow
- external account mutation
- secret storage

## Risks Remaining

- Duplicate scope may exist with earlier roadmap folders.
- Future sessions may over-read context instead of using targeted packs.
- Study language may be mistaken for implementation approval.

## Next Recommended Action

PMO review should reconcile this roadmap with existing 00-13 roadmap folders, then propose P2 expansion only where useful.
