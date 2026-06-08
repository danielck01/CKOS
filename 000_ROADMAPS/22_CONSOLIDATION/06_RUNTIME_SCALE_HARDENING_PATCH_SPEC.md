---
title: Runtime Scale Hardening Patch Spec
file: 06_RUNTIME_SCALE_HARDENING_PATCH_SPEC.md
phase: 000_ROADMAPS
category: hardening_patch_spec
status: draft_ready_for_founder_review
owner: pmo_ckos
created_at: 2026-06-02
directive_source: founder_pmo_runtime_scale_hardening
canonical_patch: false
no_runtime_authority: true
implementation_authorized: false
purpose: >
  Registrar tres mudancas P0 para proteger o desenvolvimento CKOS contra
  lacunas de business systems, simulacoes fora do runtime e isolamento fraco
  de tenants em projections/SSE.
source_docs:
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - 03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - 03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - 04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md
  - 04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md
  - 04_PRODUCT_SYSTEM/16_NODE_CANVAS_ARCHITECTURE.md
  - 06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md
  - 06_BUSINESS_SYSTEMS/22_FEEDBACK_SYSTEM_ARCHITECTURE.md
  - 06_BUSINESS_SYSTEMS/23_SUPPORT_SYSTEM_ARCHITECTURE.md
  - 06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md
  - 02_EXECUTION_SYSTEM/skills/ckos-policy-rls-security.md
  - 02_EXECUTION_SYSTEM/skills/ckos-event-runtime-contract.md
  - 02_EXECUTION_SYSTEM/skills/ckos-qa-gate.md
confidence: high
---

# 1. PMO Verdict

As tres mudancas propostas sao aceitas como guardrails P0 de escala:

1. Proteger o desenvolvimento contra lacunas dos Business Systems usando estados degradados amigaveis na UI, sem mascarar ausencia de fundacoes.
2. Manter foco no runtime limitando simulacoes a injecao sintetica no event bus, sem APIs falsas para interface.
3. Blindar seguranca movendo isolamento de tenants de filtros logicos da aplicacao para particionamento estrutural no projection engine e no SSE.

Essas regras nao criam implementacao, migration, API, UI ou runtime. Elas definem criterios que futuras implementacoes devem respeitar.

# 2. Mudanca 1 - Business Systems Com Estado Degradado Explicito

## 2.1 Problema

Quando ROI, Feedback, Support, Credits/Billing ou outros Business Systems ainda nao estao completos, a UI nao pode fingir que a fundacao existe. Placeholder bonito sem boundary vira divida arquitetural e engana o desenvolvimento.

## 2.2 Regra

Toda superficie de produto que dependa de Business System incompleto deve mostrar estado degradado explicito e amigavel:

```txt
available              -> fundacao pronta e projection confiavel
degraded_available     -> dado parcial, com aviso e limite claro
foundation_missing     -> sistema base ausente; widget/node opera read-only ou placeholder
blocked_missing_foundation -> acao bloqueada ate fundacao existir
projection_stale       -> dado antigo; UI mostra timestamp e motivo
not_authorized         -> policy nega; UI nao revela dado sensivel
```

## 2.3 Obrigatorio Na UI

- Mostrar ausencia de fundacao como estado do sistema, nao como erro generico.
- Exibir o que esta disponivel, o que esta indisponivel e qual doc/gap governa a falta.
- Bloquear acoes que dependeriam de Business System nao implementado.
- Permitir visualizacao read-only ou redigida apenas quando policy permitir.
- Nunca inventar ROI, credit balance, support SLA, feedback learning ou billing status.

## 2.4 Reprovado

- Widget mostra zero, vazio ou sucesso quando o dado real nao existe.
- UI usa mock fixo para parecer funcional.
- Business gap e escondido como "em breve" sem source_ref.
- Frontend calcula ROI/cost/billing localmente.
- QA aprova feature porque a tela parece coerente, embora a fundacao esteja ausente.

# 3. Mudanca 2 - Simulacao Somente Por Injecao Sintetica No Event Bus

## 3.1 Problema

Simulacao pode virar um segundo runtime se criarmos APIs falsas para alimentar interface. Isso quebra SDD, mascara backend ausente e cria contrato paralelo que depois precisa ser desfeito.

## 3.2 Regra

Toda simulacao P0 deve entrar pelo mesmo trilho conceitual do runtime:

```txt
SyntheticEventInjected
  -> event_bus
  -> event_store
  -> workflow/projection handlers
  -> ui_projection_engine
  -> Dashboard / Command Center / Canvas
```

A simulacao injeta eventos sinteticos, marcados e auditaveis. Ela nao cria API falsa de produto.

## 3.3 Envelope Minimo De Evento Sintetico

```yaml
event_type:
synthetic: true
simulation_id:
tenant_id:
workspace_id:
project_id:
actor_type: simulation
correlation_id:
causation_id:
source_ref:
payload:
expires_at:
```

## 3.4 Obrigatorio

- Todo dado sintetico deve carregar `synthetic: true`.
- Todo evento sintetico deve ter tenant/project scope.
- Projections derivadas de simulacao devem preservar `synthetic_source_ref`.
- UI deve poder exibir "dados simulados" quando isso for relevante.
- Simulacao nao usa segredo real, provider real ou side effect externo.

## 3.5 Reprovado

- Criar endpoint fake para a interface consumir.
- Criar mock API que nao passa pelo event bus.
- Criar estado de UI que nao seja reconstruivel por evento.
- Usar simulacao para contornar policy, approval, cost ou tenant isolation.
- Deixar dado sintetico indistinguivel de dado real.

# 4. Mudanca 3 - Isolamento Estrutural De Tenants Em Projection/SSE

## 4.1 Problema

Filtrar tenant tarde na aplicacao e insuficiente em escala. Um bug em query, controller, websocket, cache ou payload pode vazar dados cross-tenant. RLS continua necessario, mas nao pode ser o unico cinto de seguranca quando projection/SSE entram em tempo real.

## 4.2 Regra

O isolamento de tenants deve existir estruturalmente em quatro camadas:

```txt
event ingestion partition
  -> projection build partition
  -> projection storage partition
  -> SSE/channel partition
```

O projection engine nunca deve calcular uma projecao global e filtrar depois para o usuario. Ele deve construir, armazenar e distribuir projections ja particionadas por tenant/project.

## 4.3 Projection Engine

Obrigatorio:

- Projection job sempre recebe `tenant_id`, `workspace_id`, `project_id` como pre-condicao.
- Projection storage tem chave composta por `tenant_id/project_id/projection_key`.
- Rebuild de projection roda por tenant/project, nao global por default.
- Payload nao autorizado nunca entra no snapshot enviado ao frontend.
- Dados redigidos devem ser materializados como payload redigido, nao removidos pelo frontend.

## 4.4 SSE

Obrigatorio:

- Nenhum canal SSE global.
- Canal minimo: `tenant_id:project_id:user_id`.
- Token SSE efemero com tenant/project/user scope.
- Reconexao revalida policy.
- Broadcast por tenant/project, nunca broadcast global com filtro no cliente.
- Eventos cross-tenant devem ser impossiveis por topico/canal, nao apenas por `if`.

## 4.5 Reprovado

- Projection global filtrada na aplicacao.
- SSE global com payload de multiplos tenants.
- Frontend recebe dado e decide esconder.
- Cache compartilhado sem tenant namespace.
- Query de projection sem tenant/project como parametro obrigatorio.
- Bug de projection depende do frontend para nao renderizar dado de outro tenant.

# 5. Efeito No SDD

Todo Work Order tecnico que toque Product, Runtime, Data Model ou Security deve anexar estes tres checks no implementation brief:

```txt
Business foundation check:
  - Esta feature depende de ROI/Feedback/Support/Billing?
  - Se sim, existe fundacao? Se nao, qual estado degradado aparece?

Simulation check:
  - O teste/simulacao entra por evento sintetico no event bus?
  - Existe qualquer fake API para UI? Se sim, reprovar.

Projection isolation check:
  - Projection e SSE sao particionados por tenant/project/user?
  - Existe filtro tardio no frontend/app como seguranca primaria? Se sim, reprovar.
```

# 6. Patches Canonicos Sugeridos

| Target | Patch sugerido |
|---|---|
| Doc 10 Runtime | Adicionar regra: simulacao P0 = synthetic event injection only; projection/SSE particionados por tenant/project/user. |
| Doc 11 Data Model | Fortalecer `ui_projections` com partition key obrigatoria e `synthetic_source_ref` quando aplicavel. |
| Doc 12 Security | Elevar projection/SSE partitioning a criterio de aprovacao; filtro logico de aplicacao nao e isolamento suficiente. |
| Doc 13 Evals | Adicionar eval de projection leak, stale projection, synthetic/real confusion e degraded foundation masking. |
| Doc 14 Dashboard | Adicionar estados degradados obrigatorios para Business Systems incompletos. |
| Doc 15 Command Center | Proibir fake APIs de interface; explain mode deve expor fundacao ausente sem revelar dados sensiveis. |
| Doc 16 Canvas | Trocar placeholders silenciosos por `foundation_missing`/`blocked_missing_foundation` com source_ref. |
| Docs 21-24 Business | Exigir projection readiness e degraded-state contract por sistema. |

# 7. Acceptance Criteria

Uma futura implementacao passa se:

- UI mostra fundacao ausente como estado claro e amigavel.
- Nenhum Business System incompleto e mascarado como funcional.
- Toda simulacao e evento sintetico auditavel no event bus.
- Nao existe fake API para alimentar UI.
- Projection engine particiona por tenant/project antes de materializar payload.
- SSE usa canais escopados e token efemero por tenant/project/user.
- Frontend nunca e camada primaria de seguranca.
- QA gate verifica os tres checks antes de release.

# 8. Stop Conditions

Parar o desenvolvimento se:

- A tela exige dado de Business System inexistente sem degraded state.
- Um mock/fake API aparece para desbloquear UI.
- Projection/SSE usam canal global ou projection global.
- Tenant isolation depende de filtro logico depois que payload ja foi montado.
- Simulacao mistura dado real e sintetico sem marca clara.

# 9. Architecture Questions

| ID | Pergunta | Dono | Impacto |
|---|---|---|---|
| AQ-RSH-01 | `ui_projections` deve ser fisicamente particionada por tabela/partition ou por chave composta + RLS/FORCE RLS no MVP? | Technical + Security | Define migration futura do Doc 11. |
| AQ-RSH-02 | Qual evento canonico representa simulacao: `SyntheticEventInjected`, evento real com `synthetic=true`, ou ambos? | Runtime + PMO | Define contrato de event bus. |
| AQ-RSH-03 | Quais degraded states entram em Doc 14/15/16 como lista canonica? | Product + PMO | Evita UI inventar labels. |
| AQ-RSH-04 | Quais Business Systems exigem degraded state P0 antes de implementacao de UI: ROI, Feedback, Support, Billing, todos? | PMO + Founder | Define gating de produto. |
| AQ-RSH-05 | SSE token sera emitido por auth service, projection engine ou gateway? | Security + Technical | Define enforcement real. |

# 10. Proximo Passo PMO

Antes de qualquer UI/runtime real, criar Work Order de hardening documental para aplicar patches nos docs alvo em ordem:

```txt
1. Doc 10 + Doc 12: runtime/security guardrails
2. Doc 11: projection data contract
3. Doc 14/15/16: degraded UI states e no fake APIs
4. Doc 13: evals/QA checks
5. Docs 21-24: business system readiness/degraded contracts
```

Este arquivo e patch-spec auxiliar. Nao e aprovacao de implementacao.
