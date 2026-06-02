# 10_OBSERVABILITY

## Objetivo

Estudar observabilidade para logs, traces, audit trail, event viewer e debugging de runs no CKOS Runtime.

## Opcoes analisadas

1. Logs estruturados apenas

- Barato e rapido.
- Insuficiente para causalidade, replay e debugging de workflows/eventos.

2. Event store + event viewer

- Mostra timeline por `correlation_id`, workflow, agent run e approval.
- Excelente para produto AI-first e auditoria.
- Nao substitui traces tecnicos de API/worker/provider.

3. OpenTelemetry para traces, logs e metrics

- Padrao vendor-neutral.
- Context propagation correlaciona sinais entre servicos/processos.
- Exige instrumentacao e backend/coletor.

4. Observability SaaS desde o inicio

- Dashboards prontos.
- Custo e lock-in antes do dominio estabilizar.

## Recomendacao para CKOS MVP

Recomendacao preliminar: combinar event store/audit trail como observabilidade de dominio com logs estruturados e traces OpenTelemetry para observabilidade tecnica.

Camadas:

1. Domain timeline

- Fonte: `events`.
- Chave: `correlation_id`.
- Mostra intencao, context packet, planner, workflow, agents, approvals, cost, QA, ROI, feedback e memory writer.

2. Technical tracing

- Fonte: OpenTelemetry spans.
- Chaves: `trace_id`, `span_id`, `correlation_id`, `workflow_run_id`, `agent_run_id`.
- Cobre API, queue, worker, model call, tool call, DB query relevante.

3. Structured logs

- JSON logs com nivel, mensagem, error code, IDs e duracao.
- Nunca como unica fonte de verdade de estado.

4. Metrics/watchdogs

- Runs stalled.
- Queue depth.
- Retry rate.
- Cost per project/workflow/agent/model.
- Approval wait time.
- Error rate por provider/tool.

Event viewer minimo:

- Filtro por `correlation_id`.
- Timeline ordenada.
- Visual de causation tree.
- Estados finais e eventos pendentes.
- Links para `workflow_run`, `agent_run`, `approval`, `provider_call`.

## Por que essa recomendacao

O CKOS precisa debugar sistemas agenticos, nao apenas request/response HTTP. Event viewer mostra o que aconteceu no dominio. OpenTelemetry mostra onde a execucao tecnica gastou tempo ou falhou.

OpenTelemetry e adequado porque padroniza instrumentacao, traces, metrics e logs, e context propagation permite correlacionar execucoes distribuidas. O CKOS deve carregar `correlation_id` junto do trace, porque `trace_id` tecnico nem sempre representa a intencao de negocio completa.

## Trade-offs

- Event viewer e muito util, mas precisa de event schema consistente.
- OpenTelemetry melhora diagnostico, mas exige disciplina de spans e cardinalidade.
- Logs estruturados sao baratos, mas podem duplicar dados sensiveis se nao houver policy.
- Metrics agregadas ajudam operacao, mas nao substituem timeline detalhada.

## Riscos

- Alta cardinalidade em metrics usando prompt, user email ou payload como label.
- Logs conterem secrets, PII ou prompts completos.
- Trace sem `correlation_id` ficar separado da timeline CKOS.
- Event viewer mostrar eventos que usuario nao tem permissao para ver.
- Audit trail ser alteravel.

## Como implementar depois

1. Definir log schema minimo: `level`, `msg`, `correlation_id`, `causation_id`, `trace_id`, `workflow_run_id`, `agent_run_id`, `event_id`, `duration_ms`, `error_code`.
2. Instrumentar API, workers, queue adapter, model router, tool router e DB calls criticas.
3. Criar event viewer read-only sobre projections filtradas por permissao.
4. Criar run replay por `correlation_id`.
5. Criar alertas: stalled run, DLQ growth, budget threshold, provider failure spike, approval expiry.
6. Criar redaction policy para logs/events.
7. Definir retention por tipo de sinal.

## Dependencias

- Event store.
- Projection engine.
- Policy engine/RLS.
- OpenTelemetry SDK/coletor ou backend local.
- Structured logger.
- Fontes primarias consultadas:
  - OpenTelemetry docs: https://opentelemetry.io/docs/
  - OpenTelemetry context propagation: https://opentelemetry.io/docs/concepts/context-propagation/
  - OpenTelemetry semantic conventions: https://opentelemetry.io/docs/concepts/semantic-conventions/

## O que nao fazer agora

- Nao depender so de console logs.
- Nao criar dashboards antes de definir eventos e IDs.
- Nao expor event viewer sem filtro de permissao.
- Nao usar prompt completo como log/metric label.
- Nao implementar frontend agora.
