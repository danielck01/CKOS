---
title: Handoff Standard
file: 07_handoff_standard.md
layer: study
doc_type: standard_proposal
status: draft
version: 0.1.0
created_at: 2026-05-31
updated_at: 2026-05-31
owner: pmo_ckos
responsible_agent: codex
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - pmo_ckos
source_type: local_vault_audit
source_path: handoff patterns
source_tool: codex
provenance_status: unverified
confidence: medium
risk_level: medium
canonical_candidate: true
tags: [ckos, handoff, governance, agents]
---

# Handoff Standard

## Objective

Define a handoff standard between Claude, Codex, PMO, Founder and other CKOS agents.

## Required Fields

```txt
from
to
scope
done
not_done
files_touched
files_not_touched
risks
blockers
next_action
status
approval_needed
```

## Proposed Template

```md
# Handoff - [scope]

## From

## To

## Scope

## Done

## Not Done

## Files Touched

## Files Not Touched

## Risks

## Blockers

## Next Action

## Status

## Approval Needed
```

## Status Enum

```txt
draft
ready_for_review
accepted
rejected
blocked
completed
```

## Rules

- Handoff must distinguish completed work from suggested work.
- Handoff must list files not touched when scope constraints matter.
- Handoff must state whether approval is required before next action.
- Handoff cannot silently promote study output to canonical.

## What Not To Do Now

- Do not use chat summary as the only handoff for critical work.
- Do not omit risks because work is "documentation only".
- Do not pass backend work through a study handoff without explicit approval.
