# 03_AGENT_RUNTIME

## Objetivo

Estudar como o CKOS Runtime deve representar `agent_run`, heartbeat, handoff, blocked states, timeout e worker monitor.

Esta nota prepara padroes tecnicos para implementacao futura, sem backend agora.

## Opcoes analisadas

1. Agent runtime simples em processo unico

- Facil para prototipo local.
- Pouca protecao contra processo travado, timeout e retomada.
- Dificil auditar handoffs e provider calls com precisao.

2. Workers com queue + `agent_run` persistido

- Cada execucao de agente tem registro proprio.
- Heartbeat e status ficam em tabela/projection.
- Worker monitor detecta stale, timeout e blocked.
- Melhor encaixe com event store, cost guard e QA.

3. Temporal Activities para agent/tool calls

- Heartbeats, retries e cancellation ja sao padroes nativos.
- Mais robusto para atividades longas.
- Custo de adocao alto no MVP.

4. Agents como MCP/tool servers

- Bom para encapsular ferramentas e integracoes.
- Nao substitui run lifecycle; MCP e interface de ferramenta, nao modelo completo de runtime.

## Recomendacao para CKOS MVP

Recomendacao preliminar: modelar o agent runtime como workers idempotentes consumindo jobs atomicos, com `agent_runs` persistidos e heartbeat explicito.

Modelo minimo:

```txt
agent_runs
- id
- workflow_run_id
- workflow_step_run_id
- agent_key
- status
- blocked_reason
- timeout_at
- started_at
- ended_at
- last_heartbeat_at
- correlation_id
- causation_id
- idempotency_key
- input_ref
- output_ref
- error_code
- error_detail
```

Estados sugeridos:

```txt
queued
starting
running
waiting_tool
waiting_model
waiting_human
blocked
handoff_requested
handoff_completed
cancelling
cancelled
completed
failed
timed_out
stalled
```

Heartbeat:

- Deve ser emitido pelo worker/processo, nao pelo LLM.
- Deve registrar progresso operacional: fase, step atual, tokens/custo parcial se disponivel, tool ativa, ultima saida parcial segura.
- Perda de heartbeat nao deve concluir automaticamente que o LLM falhou; deve emitir `agent_run_stalled` e acionar politica de retry/cancel.

## Por que essa recomendacao

O CKOS precisa saber se um agente esta pensando, chamando modelo, aguardando ferramenta, bloqueado por contexto, aguardando approval ou perdido. Logs soltos nao bastam.

Um `agent_run` persistido com heartbeat permite:

- detectar runs orfaos
- pausar por approval sem perder contexto
- auditar handoffs
- atribuir custo por agente/modelo/tool
- montar timeline de debugging
- alimentar QA e memory writer

Temporal mostra uma referencia forte: atividades longas devem heartbeatar, timeouts devem controlar retries, e cancellation so chega de forma confiavel quando a atividade observa sinais/heartbeats. O CKOS pode aplicar essa ideia sem adotar Temporal no MVP.

## Trade-offs

- Heartbeat frequente melhora deteccao, mas aumenta writes.
- Estado rico ajuda debug, mas pode virar complexidade se cada agente criar status proprio.
- Worker monitor simples e barato, mas exige cuidado para nao marcar falso positivo.
- Handoff explicito aumenta burocracia, mas reduz perda de contexto entre agentes.

## Riscos

- Heartbeat feito dentro de chamadas bloqueantes longas nao ser emitido.
- Timeout matar uma etapa que ja causou efeito externo sem idempotency.
- Agente blocked sem `blocked_reason` acionavel.
- Handoff sem resumo de contexto e sem criterio de aceite.
- Worker monitor corrigir estado por `UPDATE` sem emitir evento.

## Como implementar depois

1. Criar `agent_runs` e `agent_run_events`.
2. Cada worker deve registrar `agent_run_started`, heartbeats periodicos e evento terminal.
3. Criar `worker_heartbeats` por processo para separar saude do worker de saude do agent run.
4. Criar `agent_handoffs` com `from_agent`, `to_agent`, `context_summary`, `open_questions`, `required_artifacts`, `acceptance_status`.
5. Criar monitor que emite `agent_run_stalled` quando `last_heartbeat_at` expira.
6. Criar politicas: retry, handoff, escalate to approval, cancel ou mark blocked.
7. Integrar provider call logging e cost ledger por `agent_run_id`.

## Dependencias

- Event store.
- Background job runner.
- Model router.
- Tool registry.
- Cost guard.
- Approval gates.
- Observability/event viewer.
- Fontes primarias consultadas:
  - Temporal Activity Execution: https://docs.temporal.io/activity-execution
  - Temporal Activity Heartbeats: https://docs.temporal.io/encyclopedia/detecting-activity-failures
  - BullMQ stalled jobs: https://docs.bullmq.io/guide/jobs/stalled

## O que nao fazer agora

- Nao executar agentes longos sem heartbeat.
- Nao tratar "blocked" como estado final generico.
- Nao deixar handoff como texto solto em log.
- Nao permitir workers chamarem modelo/tool sem `agent_run_id`.
- Nao implementar backend ainda.
