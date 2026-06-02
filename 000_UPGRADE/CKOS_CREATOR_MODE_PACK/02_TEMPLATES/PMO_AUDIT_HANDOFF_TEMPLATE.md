---
title: PMO Audit Handoff Template
system_id: pmo_audit_handoff_template
category: creator_mode_template
status: active
version: 1.1.0
updated_at: 2026-05-26
owner: pmo_ckos
created_for: CKOS_CREATOR_MODE_PACK
---

# PMO_AUDIT_HANDOFF

## Pedido ao PMO

```txt
PMO, revise este plano antes de execucao.
```

## Metadados

```txt
task_id:
project_name:
project_type:
category:
subcategory:
requested_by:
ceo_agent:
date:
risk_level:
estimated_credits:
approval_status:
```

## Plano enviado pelo CEO

```txt
Intent detected:

Intencao refinada:

Objetivo:

Escopo:

Nao escopo:

Saida recomendada:
```

## Escopo a auditar

```txt
Allowed actions:

Forbidden actions:

Files/folders to read:

Files/folders to create or update:

Files/folders forbidden:
```

## Custo estimado

```txt
Local reading:
Planning:
PMO audit:
External research:
Artifact generation:
Delivery audit:
Total estimated range:
Alternatives cheaper than current plan:
```

## Riscos conhecidos

```txt
Legal risk:
Reputational risk:
Technical risk:
Documentation risk:
Cost risk:
Duplication risk:
Canonical conflict risk:
```

## Arquivos permitidos

## Arquivos proibidos

## Policies aplicadas

```txt
POLICY_PLANNER_FIRST:
POLICY_CONTEXT_PACK_REQUIRED:
POLICY_COST_VISIBILITY_REQUIRED:
POLICY_PMO_AUDIT_FOR_MEDIUM_HIGH_RISK:
POLICY_FOUNDER_APPROVAL_BEFORE_EXECUTION:
POLICY_CHECKOUT_LOCK_REQUIRED:
POLICY_CANONICAL_DOC_PROTECTION:
POLICY_NO_IMPLEMENTATION_IN_DOCUMENTAL_PHASE:
```

## Checkout lock proposto

```txt
# CHECKOUT LOCK

task_id:
agent:
role:
folder_scope:
files_allowed:
files_forbidden:
started_at:
expected_output:
approval_required:
risk_level:
status: locked
```

## Decisao solicitada

```txt
PMO_AUDIT_REPORT

Verdict:
approved | approved_with_required_patches | blocked

Reason:

Scope check:

Risk check:

Cost check:

Documentation check:

Filetree check:

Missing context:

Required patches:
1.
2.
3.

Forbidden actions:

Approved next action:

Founder decision required:
yes/no

Recommended response to CEO Agent:
```

## Bloqueios automaticos do PMO

Bloquear se o CEO tentar:

- gerar estrategia final sem briefing;
- criar UI/UX antes da fase autorizada;
- criar backend, migration, API ou agente real;
- renumerar docs sem busca de referencias;
- recriar docs ja existentes;
- ignorar custo estimado;
- ignorar risco juridico ou reputacional;
- tratar pesquisa externa como verdade canonica;
- promover Manus, n8n ou Apify como core runtime;
- executar sem Founder approval.

## Checkout release apos entrega

```txt
# CHECKOUT RELEASE

task_id:
agent:
files_changed:
summary:
risks:
next_step:
status: released
```
