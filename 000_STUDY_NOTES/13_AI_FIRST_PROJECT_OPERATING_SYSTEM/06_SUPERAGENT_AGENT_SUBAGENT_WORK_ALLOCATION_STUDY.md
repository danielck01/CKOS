---
title: Superagent Agent Subagent Work Allocation Study
file: 06_SUPERAGENT_AGENT_SUBAGENT_WORK_ALLOCATION_STUDY.md
layer: study
phase: 000_STUDY_NOTES
category: agent_work_allocation
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
purpose: Study work allocation between superagents, agents and subagents without creating real agents or packs.
inputs:
  - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md
  - 02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
outputs:
  - role allocation study
  - future agent pack candidate constraints
framework:
  - decide -> plan -> execute -> audit -> approve -> learn
edge_cases:
  - role study mistaken for agent creation
  - subagent receives authority without policy
integrations:
  - future agentRegistry
  - future squadRegistry
prompts:
  - Study responsibilities before creating any real agent pack.
metrics:
  - no real agents created
  - handoff boundaries clear
related_notes:
  - ck_agent_handoffs.md
tags:
  - agents
  - superagents
  - subagents
---

# Superagent / Agent / Subagent Work Allocation

## PMO Decision

Do not create a complete agent pack now. First study who decides, who plans, who executes, who audits, who approves, who learns and who updates memory.

## Allocation Questions

| Question | Why it matters |
|---|---|
| Who owns the project intention? | Prevents execution without strategic context. |
| Who converts questions into briefing? | Prevents scattered context. |
| Who decomposes tasks? | Prevents arbitrary task splitting. |
| Who executes? | Requires skill, tool and permission boundaries. |
| Who audits? | Prevents self-approval. |
| Who approves? | Preserves decision rights. |
| Who writes memory? | Prevents untrusted memory writes. |

## Future Pack Candidate

If approved later, a future auxiliary pack may study:

```txt
CEO_AGENT/
PMO_CKOS/
METACOGNIK/
BUILDER_LEAD/
DESIGN_LEAD/
SECURITY_LEAD/
DATA_LEAD/
RESEARCH_LEAD/
QA_LEAD/
SUBAGENTS/
```

This folder does not create that pack.

## Candidate For Doc 27

Doc 27 should include agent work allocation as part of task orchestration, but must keep real agent creation behind separate policy, registry and approval gates.
