# 02_WORKFLOW_ENGINES

## Objetivo

Estudar opcoes para executar workflows do CKOS com `workflow_run`, `workflow_cards`, state machines, retries, cancellation e deteccao de stalled run.

Esta nota nao define backend final. Ela prepara uma recomendacao tecnica preliminar para o CKOS Runtime.

## Opcoes analisadas

1. Workflow engine leve, proprio do CKOS

- State machines declarativas em registry.
- Estado atual como projection; verdade em eventos.
- Jobs executam passos atomicos.
- Alta aderencia ao modelo CKOS: workflow cards, approvals, QA, ROI, memory writer e cost guard.
- Exige disciplina para nao virar um engine informal cheio de `if/else`.

2. Temporal

- Excelente para durable execution, retries, timeouts, heartbeats, replay e workflows longos.
- Workflows precisam ser deterministicos; chamadas externas ficam em Activities.
- Custo de adocao alto para MVP local: servidor, SDK, conceitos, deploy e modelagem.

3. BullMQ flows

- Forte para jobs, retries, prioridades e dependencias parent-child.
- Baseado em Redis.
- Bom para execucao de jobs, mas nao e por si so um modelo de dominio para workflow cards, approvals e audit trail CKOS.

4. pg-boss + state machine em Postgres

- Jobs confiaveis usando Postgres, menos infraestrutura.
- Bom encaixe com event store e Supabase/Postgres.
- Nao fornece workflow semantics completas; o CKOS ainda precisa modelar estado, cards, approvals e cancellation.

5. XState/statecharts para modelagem

- Excelente para explicitar estados, transicoes e guards.
- Pode rodar em JS/TS e ajudar a testar transicoes puras.
- Nao substitui storage duravel, queue, retries e audit trail.

## Recomendacao para CKOS MVP

Recomendacao preliminar: criar um workflow engine leve do CKOS, event-sourced, com state machines declarativas e jobs atomicos em uma fila Postgres-based. Usar Temporal apenas como opcao futura para workflows longos/criticos quando a complexidade operacional justificar.

Separacao sugerida:

- `workflow_run`: instancia executavel de um blueprint.
- `workflow_step_run`: execucao atomica de etapa.
- `workflow_card`: projection operacional para humano/agente ver proximo passo, status, bloqueio, approval ou QA.
- `workflow_state`: projection reconstruivel a partir dos eventos.

Estados minimos:

```txt
draft
ready
running
waiting_user_input
waiting_agent
waiting_approval
blocked
cancelling
cancelled
completed
failed
timed_out
archived
```

Eventos minimos:

```txt
workflow_started
workflow_step_scheduled
workflow_step_started
workflow_step_completed
workflow_step_failed
workflow_waiting_input
approval_requested
approval_granted
approval_denied
workflow_blocked
workflow_cancel_requested
workflow_cancelled
workflow_timed_out
workflow_completed
```

## Por que essa recomendacao

O CKOS precisa de controle fino sobre intencao, contexto, perguntas, planner, workflow cards, approvals, QA, ROI e memory writer. Um engine generico resolve durabilidade, mas nao resolve sozinho o modelo operacional do CKOS.

Para MVP, o menor caminho implementavel e:

- event store como fonte de verdade
- state machine explicita por tipo de workflow
- jobs atomicos e idempotentes
- workflow cards como projection, nao como fonte de verdade
- stalled detector varrendo runs sem heartbeat/atividade dentro do SLA

Temporal deve continuar no radar, especialmente porque sua documentacao formaliza bem durabilidade, replay, timeouts, retries e heartbeats. Mas adotar Temporal antes do dominio CKOS estabilizar pode cristalizar decisoes cedo demais.

## Trade-offs

- Proprio CKOS: mais aderente e barato no MVP, mas exige maturidade de implementacao.
- Temporal: mais resiliente para workflows longos, mas mais caro de aprender, operar e encaixar.
- BullMQ/pg-boss: otimos para jobs; nao devem ser confundidos com workflow engine completa.
- XState: otimo para state machine pura; nao entrega persistencia duravel sozinho.

## Riscos

- Misturar `workflow_card` com source of truth e criar divergencia.
- Retry em nivel errado duplicar efeitos externos.
- Cancellation incompleta deixar agent/tool calls rodando sem dono.
- Stalled run ser tratado apenas como estado visual, sem evento e sem acao de recuperacao.
- State machines nao versionadas quebrarem runs antigos.

## Como implementar depois

1. Definir `workflow_blueprints` e `state_machine_definitions` versionados.
2. Criar `workflow_runs`, `workflow_step_runs` e projections `workflow_cards`.
3. Cada transicao valida deve emitir evento e atualizar projection em consumidor idempotente.
4. Retries devem ocorrer em `workflow_step_run`, com backoff e classificacao de erro.
5. Cancellation deve emitir `workflow_cancel_requested`, impedir novos steps e sinalizar workers ativos.
6. Stalled detector deve procurar steps em `running` sem heartbeat recente e emitir `workflow_step_stalled`.
7. Testar state machines com tabela de transicoes validas e invalidas.

## Dependencias

- Event store append-only.
- Background job runner.
- Agent runtime com heartbeat.
- Approval system.
- Cost guard.
- QA/eval runner.
- Fontes primarias consultadas:
  - Temporal workflow execution: https://docs.temporal.io/workflow-execution
  - Temporal deterministic constraints: https://docs.temporal.io/workflow-definition
  - BullMQ stalled jobs: https://docs.bullmq.io/guide/jobs/stalled
  - XState docs: https://stately.ai/docs

## O que nao fazer agora

- Nao implementar Temporal no MVP sem aprovacao especifica.
- Nao usar workflow cards como tabela editavel de verdade operacional.
- Nao permitir transicoes implicitas fora da state machine.
- Nao fazer retry de um workflow inteiro quando apenas um step falhou.
- Nao criar frontend de workflow cards nesta fase.
