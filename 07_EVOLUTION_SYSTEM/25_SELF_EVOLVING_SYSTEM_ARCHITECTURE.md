---
title: Self-Evolving System Architecture
file: 25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md
system_id: self_evolving_system_architecture
display_name: Self-Evolving System Architecture
doc_type: canonical_doc
category: evolution_system
layer: canonical
status: draft
version: 1.0.0
created_at: 2026-05-27
updated_at: 2026-05-27
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - metacognik
  - technical
  - qa_lead
approval_required:
  - founder
  - technical
  - metacognik
source_type: rewritten_from_superseded_doc
source_path: 05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md
source_tool: codex
provenance_status: verified
project: ckos
related_docs:
  - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md
  - 01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - 03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - 03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - 05_IMPLEMENTATION_SYSTEM/17_IMPLEMENTATION_PROTOCOL.md
  - 05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md
  - 06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md
  - 06_BUSINESS_SYSTEMS/22_FEEDBACK_SYSTEM_ARCHITECTURE.md
  - 06_BUSINESS_SYSTEMS/23_SUPPORT_SYSTEM_ARCHITECTURE.md
  - 06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md
risk_level: high
confidence: high
---

# 25 - Self-Evolving System Architecture

## 1. Proposito

The Self-Evolving System defines how CKOS learns from its own operation, proposes improvements, tests changes, measures impact and evolves with human approval.

It is not an implementation permission. It is the canonical architecture for governed evolution: learning signals, improvement proposals, sandbox simulation, evals, approval gates, rollback and audit logs.

## 2. O que e / O que nao e

It is:

- a governed learning system;
- a continuous improvement layer;
- a mechanism for system evolution proposals;
- a performance evaluation system for agents, prompts, workflows, nodes, skills, capabilities and costs;
- a sandbox and rollback governance layer.

It is not:

- AI changing production by itself;
- an agent with unrestricted permissions;
- auto-deploy;
- a replacement for the Founder;
- a replacement for QA;
- a bypass of policy, security, cost guard or approval.

## 3. Principio central

"The CKOS may propose its own evolution, but it must never silently mutate its own production behavior without policy, evidence, evaluation, approval and rollback."

## 4. Relacao com o Founder

The Founder stops being a prompt operator and becomes the strategic approver of critical evolution.

CKOS may recommend improvements, organize evidence and prepare a controlled change package. Metacognik audits the reasoning. Technical validates feasibility and safety. QA Lead validates regression and release criteria. The Founder approves, rejects or asks for revision.

The Founder remains the highest strategic authority for:

- autonomy level changes;
- production behavior changes;
- pricing, billing and legal policy changes;
- security-sensitive changes;
- irreversible or high-risk changes.

## 5. Relacao com Metacognik

Metacognik is the autonomy risk auditor.

Metacognik must:

- detect risk;
- audit assumptions;
- evaluate evidence;
- block dangerous autonomy;
- require rollback;
- veto changes without adequate confidence;
- detect circular evaluation, where the system changes the standards used to judge itself;
- flag claims that lack provenance or measurable outcomes.

Metacognik can veto even when Founder interest exists. A veto does not override the Founder as authority; it forces explicit review before action.

## 6. Relacao com Runtime

Self-Evolving depends on the Runtime layer. It cannot operate as a parallel execution system.

Required runtime components:

- `event_bus`;
- state machines;
- `workflow_engine`;
- `policy_engine`;
- `approval_gate`;
- `model_router`;
- `cost_guard`;
- `eval_runner`;
- `sandbox_runner`;
- `rollback_manager`;
- `audit_logs`.

Every evolution action must be represented as events. Every sensitive action must pass through policy and approval. Every experiment must be traceable.

## 7. Relacao com Data Model

The Self-Evolving System requires data objects that may be added as future patches to the Data Model:

- `system_improvement_proposals`;
- `evolution_runs`;
- `evolution_experiments`;
- `agent_performance_records`;
- `prompt_performance_records`;
- `workflow_performance_records`;
- `node_performance_records`;
- `skill_performance_records`;
- `capability_change_requests`;
- `rollback_records`;
- `evolution_eval_results`;
- `evolution_approval_requests`.

These objects must include tenant scope, source events, approval references, confidence, risk level, cost estimate, rollback status and audit metadata.

## 8. Relacao com Business Systems

Business Systems docs 21-24 feed the Evolution System with real operating signals.

ROI contributes:

- real outcomes;
- confidence;
- return by workflow;
- cost vs. value.

Feedback contributes:

- explicit feedback;
- implicit feedback;
- complaints;
- suggestions;
- friction signals.

Support contributes:

- recurring tickets;
- root causes;
- escalations;
- knowledge gaps.

Billing/Credits contributes:

- cost by capability;
- plans blocking usage;
- overage;
- abnormal consumption;
- profitability by client/project.

These signals do not auto-apply changes. They generate hypotheses and improvement proposals.

## 9. Learning Signals

Learning signals include:

- approval outcomes;
- rejected outputs;
- corrected outputs;
- support tickets;
- feedback loops;
- ROI outcomes;
- cost anomalies;
- eval failures;
- security incidents;
- workflow delays;
- tool failures;
- model regressions;
- user behavior.

Each signal needs source, timestamp, tenant/project scope, confidence and risk classification.

## 10. Evolution Loop

The canonical loop:

1. observe signals;
2. detect pattern;
3. generate hypothesis;
4. collect evidence;
5. create improvement proposal;
6. simulate in sandbox;
7. evaluate;
8. request approval;
9. apply controlled change;
10. monitor regression;
11. record learning;
12. allow rollback.

Any step can stop the loop. A stopped loop must record why: insufficient evidence, policy block, cost block, eval failure, approval rejection, rollback unavailable or risk too high.

## 11. State Machines

Improvement proposal state machine:

```txt
detected
  -> drafted
    -> evidence_collecting
      -> simulated
        -> eval_pending
          -> approval_requested
            -> approved
            -> rejected
approved
  -> applied
    -> monitoring
      -> archived
      -> rolled_back
```

Allowed states:

- `detected`
- `drafted`
- `evidence_collecting`
- `simulated`
- `eval_pending`
- `approval_requested`
- `approved`
- `rejected`
- `applied`
- `monitoring`
- `rolled_back`
- `archived`

No proposal can jump from `drafted` to `applied`.

## 12. Approval Gates

Required gates:

- Founder approval for strategic, production, billing, security, legal or autonomy-level changes;
- Technical approval for runtime, data, deployment, rollback, security or integration changes;
- Metacognik veto for weak evidence, unsafe autonomy, low confidence or circular logic;
- QA validation for regression, acceptance criteria and release readiness;
- emergency freeze when the system detects self-escalation, policy bypass, tenant leakage, rollback failure or cost loop.

Approval must be explicit, logged and tied to the exact proposal version.

## 13. Sandbox and Simulation

No sensitive change goes directly to production.

Sandbox must simulate:

- cost;
- risk;
- UX impact;
- security impact;
- data impact;
- tenant impact;
- regression;
- rollback path.

Sandbox outputs are not production. Sandbox can produce evidence, diffs, predicted cost, predicted quality and risk reports. It cannot become a hidden production path.

## 14. Rollback

Every change needs a rollback plan.

Rollback must be:

- testable;
- scoped;
- logged;
- tied to the exact applied change;
- available before approval;
- executable without exposing secrets or crossing tenants.

A change without rollback is blocked, unless the Founder explicitly accepts an irreversible strategic decision outside MVP scope.

## 15. Autonomy Ladder

| Level | Name | Allowed behavior |
|---|---|---|
| L0 | Observe only | collect and classify learning signals |
| L1 | Suggest improvements | create non-binding suggestions |
| L2 | Draft patch plan | prepare patch plan for human review |
| L3 | Run sandbox simulation | simulate without production effects |
| L4 | Prepare implementation task | create task package, not execution |
| L5 | Execute reversible low-risk change with approval | execute only after approval and rollback readiness |
| L6 | Execute controlled production change with approval | production change with Founder/Technical/Metacognik gates |
| L7 | Autonomous production mutation is forbidden for MVP | not allowed in MVP |

L7 is explicitly forbidden for MVP.

## 16. Cost and Credits Guardrails

Evolution consumes credits and operational budget.

Rules:

- experiments have estimated cost;
- sandbox runs require budget envelope;
- `cost_guard` can block loops;
- repeated failed experiments are throttled;
- Founder sees estimated cost before approval;
- high-cost evolution requires explicit approval;
- cost savings cannot justify policy or quality regression.

## 17. Security and Policy Guardrails

Non-negotiable rules:

- no bypass of `policy_engine`;
- no self-elevation of permission;
- no exposed secrets;
- no cross-tenant learning without explicit policy;
- no use of PII in learning without sanitization;
- no change to approval policies by the system itself;
- no direct modification of security policy by an agent;
- no hidden provider/tool tokens in frontend or study notes.

Any attempt at self-escalation triggers security incident handling.

## 18. Evals

Evolution evals include:

- quality regression;
- hallucination;
- evidence coverage;
- cost impact;
- latency impact;
- security impact;
- UX impact;
- ROI impact;
- support impact;
- user trust impact.

Minimum rule: a proposal cannot reach approval if critical evals are missing, stale, failed or contradicted without explanation.

## 19. What Can Evolve

Allowed evolution candidates, with approval:

- prompts;
- instructions;
- skills;
- skill chains;
- workflows;
- node templates;
- dashboard widgets;
- commandbar suggestions;
- collectors;
- model policies;
- support knowledge base;
- research pipelines;
- QA rubrics.

Each candidate type needs its own risk class and approval path.

## 20. What Cannot Evolve Automatically

The system cannot automatically evolve:

- billing rules;
- legal policies;
- security policies;
- tenant access;
- approval policies;
- production secrets;
- pricing;
- deletion policies;
- model privacy policies;
- public client deliverables;
- contracts.

These areas require explicit human approval and may require legal, technical or Founder review.

## 21. UI Projection

Future UI may show:

- evolution proposals;
- risks;
- estimated savings;
- quality before/after;
- pending approvals;
- rollback availability.

This document does not implement UI. UI is a future projection of runtime and evolution state, not a source of truth.

## 22. MVP P0 Scope

MVP P0 includes:

- register learning signals;
- generate improvement proposal;
- simulate in text;
- request approval;
- record decision;
- do not auto-apply production.

P0 is planning and governance, not autonomous mutation.

## 23. Fora do P0

Out of P0:

- auto-deploy;
- self-modifying runtime;
- autonomous marketplace;
- automatic fine-tuning;
- automatic cross-project learning;
- automatic pricing/plan changes;
- automatic security policy changes.

## 24. Edge Cases

| Edge case | Required behavior |
|---|---|
| Improvement reduces cost but worsens quality | block or require explicit tradeoff approval |
| Improvement increases ROI but violates policy | policy wins; block |
| Agent tries to change its own permission | deny, log, security alert |
| Isolated negative feedback | do not overfit; require pattern |
| Contradictory eval | hold for Metacognik review |
| Rollback unavailable | block change |
| Sandbox cost is high | require budget approval |
| Insufficient data | keep proposal in evidence collection |
| Client asks for prohibited change | reject or escalate to Founder/legal |
| Founder approves something vetoed by Metacognik | require explicit override review and audit log |

## 25. Patches sugeridos

Future patches, not applied by this document:

- Doc 11: add `evolution_*` tables and performance records.
- Doc 10: register `evolution_engine`, `sandbox_runner` and `rollback_manager`.
- Doc 12: define self-evolution security policy and anti-self-escalation enforcement.
- Doc 13: define evolution eval targets and regression dashboards.
- Doc 14: add future evolution proposals widget.
- Doc 15: add future commandbar intents for evolution.
- Doc 16: add future evolution proposal nodes.

## 26. Related Notes

- [[03_AGENT_OPERATING_MODEL]]
- [[04_AUTONOMY_AND_APPROVALS]]
- [[05_MEMORY_AND_CONTEXT_ARCHITECTURE]]
- [[10_SYSTEM_RUNTIME_ARCHITECTURE]]
- [[11_DATA_MODEL_AND_PERSISTENCE]]
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]]
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]]
- [[17_IMPLEMENTATION_PROTOCOL]]
- [[20_QA_AND_FOUNDER_APPROVAL_PROTOCOL]]
- [[21_ROI_ARCHITECTURE]]
- [[22_FEEDBACK_SYSTEM_ARCHITECTURE]]
- [[23_SUPPORT_SYSTEM_ARCHITECTURE]]
- [[24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE]]

