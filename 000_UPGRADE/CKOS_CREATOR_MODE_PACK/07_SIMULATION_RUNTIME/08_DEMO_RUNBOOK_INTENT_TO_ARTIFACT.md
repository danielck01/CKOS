---
title: Demo Runbook Intent To Artifact
system_id: demo_runbook_intent_to_artifact
category: creator_mode_simulation_runtime
status: active
version: 1.0.0
owner: ceo_agent
reviewers:
  - founder
  - pmo_ckos
created_for: CKOS_CREATOR_MODE_PACK
created_at: 2026-05-26
---

# Demo Runbook Intent To Artifact

## Proposito

Roteiro para demonstrar o CKOS funcionando no Codex como ambiente de execucao documental com backend/API/conectores simulados.

Este runbook nao implementa nada.

## Pre-condicoes

- Creator Mode Pack ativo.
- Simulation Runtime Layer lida.
- Founder fornece intencao minima.
- CEO Agent opera em Planner Mode.
- PMO Auditor disponivel como papel simulado ou chat separado.
- Checkout lock usado antes de escrita documental.

## Demo flow

### 1. Founder envia intencao

```txt
Criar projeto para [objetivo minimo].
```

Evento:

```txt
IntentSubmitted
```

### 2. CEO interpreta

Simular:

```txt
POST /intent/interpret
```

CEO responde:

```txt
CEO_AGENT_INTERPRETATION

Intent detected:
Project type:
Category:
Subcategory:
Risk level:
Required context:
Recommended first action:
Estimated CKOS credits:
Blocked actions:
Needs PMO audit?
Founder approval needed?
Suggested output:
Question to Founder:
```

Eventos:

```txt
IntentResolved
ProjectTypeClassified
RiskClassified
```

### 3. CEO monta Context Pack

Simular:

```txt
POST /context-pack/build
```

Declarar:

- arquivos locais a ler;
- uploads esperados;
- fontes externas possiveis;
- docs canonicos relevantes;
- gaps;
- riscos;
- evidence map necessario.

Evento:

```txt
ContextPackBuilt
```

### 4. Policy engine avalia

Simular:

```txt
POST /policy/evaluate
```

Resultado possivel:

```txt
approved_for_planning_only
approved_with_pmo_audit
blocked_by_policy
blocked_by_cost
blocked_by_missing_context
```

Evento:

```txt
PolicyEvaluated
```

### 5. Credits service estima custo

Simular:

```txt
POST /credits/estimate
```

Formato:

```txt
SIMULACAO DE CREDITOS CKOS

Local reading:
Planning:
PMO audit:
External research:
Artifact generation:
Delivery audit:
Total estimated range:
Cheaper alternative:
Approval required:
```

Evento:

```txt
CreditsEstimated
```

### 6. CEO envia PMO handoff

Simular:

```txt
POST /pmo/audit-request
```

PMO responde:

```txt
PMO_AUDIT_REPORT

Verdict:
Reason:
Scope check:
Risk check:
Cost check:
Documentation check:
Filetree check:
Missing context:
Required patches:
Forbidden actions:
Approved next action:
Founder decision required:
Recommended response to CEO Agent:
```

Eventos:

```txt
PMOAuditRequested
PMOAuditCompleted
```

### 7. Founder decide

Simular:

```txt
POST /approvals/founder/request
POST /approvals/founder/decision
```

Decisoes:

- aprovado;
- aprovado com limite;
- ajustar plano;
- bloquear;
- aprovar apenas filetree;
- aprovar pack depois da filetree.

Evento:

```txt
FounderDecisionRecorded
```

### 8. Checkout lock

Simular:

```txt
POST /checkout/lock
```

Registrar:

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

Evento:

```txt
CheckoutLocked
```

### 9. CEO gera artifacts aprovados

Simular:

```txt
POST /artifacts/generate
```

Possiveis artifacts:

- `PROJECT_INTENT_ANALYSIS.md`
- `PROJECT_FILETREE_PROPOSAL.md`
- `PROJECT_EXECUTION_PLAN.md`
- `PMO_REVIEW_REQUEST.md`
- `FOUNDER_APPROVAL_CHECKLIST.md`
- `SOURCE_INDEX.md`
- `EVIDENCE_MAP.md`
- `RISK_AND_COMPLIANCE_MATRIX.md`

Eventos:

```txt
ArtifactGenerationStarted
ArtifactGenerated
```

### 10. Checkout release

Simular:

```txt
POST /checkout/release
```

Registrar:

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

Evento:

```txt
CheckoutReleased
```

### 11. PMO audita entrega

Simular:

```txt
POST /pmo/audit-result
```

PMO verifica:

- escopo cumprido;
- arquivos corretos;
- nenhum forbidden action executado;
- custos coerentes;
- riscos registrados;
- proximo passo claro.

Evento:

```txt
DeliveryAudited
```

### 12. CEO recomenda proxima acao

CEO fecha com:

```txt
Resumo:
Arquivos criados:
Arquivos atualizados:
Eventos simulados:
Custos:
Riscos:
Bloqueios:
Proxima acao recomendada:
```

Evento:

```txt
ProjectNextActionRecommended
```

## Demo minimal output

Para o primeiro teste real, gerar apenas:

```txt
PROJECT_INTENT_ANALYSIS.md
PROJECT_FILETREE_PROPOSAL.md
PROJECT_EXECUTION_PLAN.md
PMO_REVIEW_REQUEST.md
FOUNDER_APPROVAL_CHECKLIST.md
```

Pack de notas vem depois de filetree aprovada.

## Projeto Miriam

O Projeto Miriam pode ser usado como primeiro case real, mas somente com approval especifico para iniciar o scenario.

Classificacao esperada:

```yaml
project_type: personal_branding_legal
category: personal_branding
subcategory: regulated_legal_marketing
risk_level: high
pmo_required: true
founder_approval_required: true
```

Bloqueios:

- nao criar tom de voz definitivo;
- nao criar pilares definitivos;
- nao criar plano de conteudo final;
- nao criar identidade visual;
- nao afirmar conformidade juridica sem fonte e revisao humana.

