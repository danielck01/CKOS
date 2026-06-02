---
title: Context Validation
folder: 05_CONTEXT_ENGINE
type: backend_spec
status: implementable
version: 1.0.0
owner: CKOS PMO
backend_module: context_assembler_service
depends_on: [context_assembler_service, policy_engine]
endpoints: [POST /context/:id/validate]
related_files: [context_packet_schema.md, context_assembler.md]
---

# Context Validation

## 1. Purpose (one line)

Decide whether a `ContextPacket` is `valid`, `partial`, or `blocked` — the gate that controls whether the Question Engine, Planner, or a workflow may proceed. Validation is a pure function over a packet + intent type; it never mutates external state (it only writes the verdict back to the packet).

## 2. Validation statuses

```txt
valid    -> all required context present, trust ok, no blocking item, no blocked source needed.
            Planner may run.
partial  -> some optional context missing OR trust in mid band OR too many unvalidated
            assumptions. Question Engine SHOULD run first; Planner may run only for
            steps that do not depend on the missing fields.
blocked  -> a required field is unobtainable (permission/PII/legal), trust below floor,
            or a hard policy/constraint conflict. Planner MUST NOT run. Escalate.
```

## 3. Required vs optional context by intent type

`REQUIRED_BY_INTENT` (seed; tunable in config). A field is "covered" if a `ContextFact` or `ContextConstraint` supplies it.

| intent.type | required (blocking if missing) | optional (partial if missing) |
|---|---|---|
| `campaign` | objective, target_audience, budget_range, channel | tone, launch_date, references |
| `branding` | brand_name, positioning, audience | competitors, moodboard_refs |
| `social` | profile_subject, jurisdiction_or_niche, objective | posting_cadence, tone, references |
| `research` | research_question, scope, source_types | freshness_window, geography |
| `ecommerce` | product, audience, offer, channel | price_point, promo_window |
| `content` | topic, audience, format, objective | seo_keywords, references |
| `other` | objective, audience | constraints, references |

`jurisdiction_or_niche` for `social`/legal subjects is **blocking** because regulatory risk (e.g., OAB rules) must be known before any public-facing plan.

## 4. Validation rules (evaluated in order; first match wins)

```txt
validate(packet, intent):

R1 BLOCKED — hard stops (any => blocked)
   - any required field maps to a source that was excluded(permission)        -> "permission:<field>"
   - a constraint of type "legal" conflicts with the stated objective         -> "legal_conflict"
   - trust_score < 0.40                                                        -> "trust_floor"
   - a high-risk assumption (risk_if_wrong=high) has confidence < 0.30
     AND blocks a required field                                              -> "unsafe_assumption:<field>"
   - cross-tenant source was required                                         -> "tenant_violation"
   => return { status:"blocked", blocking_reasons:[...] }

R2 PARTIAL — proceed with care (any => partial)
   - >=1 required field missing (no covering fact)                            -> "missing:<field>"
   - trust_score in [0.40, 0.60)                                              -> "low_trust"
   - count(assumptions where needs_validation) > 3                            -> "too_many_assumptions"
   - >=1 optional field missing                                              -> "missing_optional:<field>"
   => return { status:"partial", blocking_reasons:[required ones only] }

R3 VALID — all clear
   - all required fields covered
   - trust_score >= 0.60
   - no legal/policy conflict
   - <= 3 unvalidated assumptions
   => return { status:"valid", blocking_reasons:[] }
```

Note: a *required* field missing yields **partial** (not blocked) — because the cure is to ask the user (Question Engine), which is a normal forward path. It becomes **blocked** only when the field is *unobtainable* (permission/legal/tenant), not merely absent.

## 5. Accepted vs blocked sources

**Accepted** source types: `project, briefing, decision, memory, rag, evidence, user_instruction, artifact, workflow, event` — provided they pass the permission filter and namespace check.

**Blocked** (never included, regardless of relevance):
```txt
- any source outside org:workspace:project namespace            (tenant isolation)
- PII-classified source when policy denies for this actor       (Doc 12)
- secrets / tokens / credentials (must never enter a packet)
- web_research with no citation/source metadata                 (fails L-07-style replay rule)
- weak_hypothesis used to satisfy a REQUIRED field              (insufficient trust)
```

## 6. Downstream gating (who reads the verdict)

| Consumer | valid | partial | blocked |
|---|---|---|---|
| Question Engine | optional | **run** (resolve missing) | run only to gather obtainable bits |
| Planner | run | run for non-dependent steps only | **refuse** |
| Workflow start | allow | allow with approval gate on risky steps | deny |
| Cost-bearing step | allow | require confirmation | deny |

## 7. Output contract

```ts
interface ContextValidationResult {
  context_packet_id: string;
  status: "valid" | "partial" | "blocked";
  blocking_reasons: string[];      // machine-readable: "missing:budget_range", "permission:jurisdiction"
  missing_required: string[];
  missing_optional: string[];
  trust_score: number;
  recommended_next: "plan" | "ask_questions" | "escalate";
  validated_at: string;
}
```

`recommended_next`:
```txt
valid   -> "plan"
partial -> "ask_questions"
blocked -> "escalate"   (to human / Metacognik)
```

## 8. Endpoint

```
POST /context/:id/validate   -> 200 ContextValidationResult
```
Re-validates and writes `validation_status` + `blocking_reasons` back onto the packet. Idempotent; safe to call after the user answers questions (re-run to flip partial → valid).

## 9. Failure modes

| Failure | Behavior |
|---|---|
| packet not found / cross-tenant | 404 |
| intent.type unknown | use `other` required set; add assumption "intent type unclassified" |
| trust_score null (no included sources) | treat as 0 → `partial` (fresh draft path), all required → missing |
| legal constraint detected but ambiguous | `blocked` with `legal_conflict`; route to Metacognik |

## 10. Worked examples

```txt
A) Fresh social draft, no briefing yet:
   required {profile_subject, jurisdiction_or_niche, objective} all missing
   -> status: partial, blocking_reasons:["missing:profile_subject","missing:jurisdiction_or_niche","missing:objective"]
   -> recommended_next: ask_questions

B) Campaign, all required present, trust 0.81, 2 assumptions:
   -> status: valid, recommended_next: plan

C) Legal/social subject, jurisdiction source is PII-restricted for this actor:
   -> status: blocked, blocking_reasons:["permission:jurisdiction_or_niche"]
   -> recommended_next: escalate
```

## 11. Codex implementation checklist

```txt
[ ] pure function validate(packet, intent): ContextValidationResult
[ ] REQUIRED_BY_INTENT config table (seed from §3)
[ ] rule order R1->R2->R3, first match wins
[ ] required-missing => partial; required-unobtainable => blocked
[ ] POST /context/:id/validate writes status back to context_packets
[ ] re-validate after question answers flips partial->valid
[ ] tests: each status reachable; legal/permission => blocked; missing => partial
```
