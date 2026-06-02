# CKOS Runtime Research Lab

## Visao geral

Esta pasta contem notas de pesquisa tecnica para preparar recomendacoes implementaveis do CKOS Runtime sem editar o vault canonico, sem implementar backend e sem tomar decisoes finais.

O objetivo e apoiar as correcoes canonicas em batches do Claude/PMO com estudo isolado sobre arquitetura orientada a eventos, workflow engine, agent runtime, jobs, approvals, cost guard, RAG/memory, Supabase, model routing, MCP/APIs e observabilidade.

Todas as recomendacoes aqui sao preliminares e dependem de aprovacao humana antes de virar canonico.

## Status dos estudos

| Tema | Arquivo | Status |
|---|---|---|
| Event-driven architecture | `01_EVENT_DRIVEN_ARCHITECTURE.md` | Estudo preliminar concluido |
| Workflow engines | `02_WORKFLOW_ENGINES.md` | Estudo preliminar concluido |
| Agent runtime | `03_AGENT_RUNTIME.md` | Estudo preliminar concluido |
| Background jobs | `04_BACKGROUND_JOBS.md` | Estudo preliminar concluido |
| Approval and cost guard | `05_APPROVAL_AND_COST_GUARD.md` | Estudo preliminar concluido |
| RAG and memory | `06_RAG_AND_MEMORY.md` | Estudo preliminar concluido |
| Supabase patterns | `07_SUPABASE_PATTERNS.md` | Estudo preliminar concluido |
| Model routing | `08_MODEL_ROUTING.md` | Estudo preliminar concluido |
| MCP and APIs | `09_MCP_AND_APIS.md` | Estudo preliminar concluido |
| Observability | `10_OBSERVABILITY.md` | Estudo preliminar concluido |

## Recomendacoes principais

- Usar Postgres/Supabase como event store append-only no MVP, com envelope CKOS inspirado em CloudEvents.
- Manter `correlation_id`, `causation_id` e `idempotency_key` como campos obrigatorios nos fluxos criticos.
- Criar workflow engine leve do CKOS, event-sourced, com state machines versionadas e workflow cards como projections.
- Usar jobs atomicos e idempotentes; fila agenda trabalho, mas nao e source of truth.
- Para MVP local, considerar pg-boss como job runner primario por simplicidade e debug SQL.
- Modelar `agent_run` com heartbeat, blocked reason, timeout, handoff e worker monitor.
- Tratar approvals e cost guard como mecanismos de runtime, nao como convencao de prompt.
- Usar pgvector/Supabase para RAG no MVP, com `memory_updates` como staging antes de promocao.
- Usar Supabase shared schema com RLS desde o inicio, campos relacionais para invariantes e JSONB apenas para payloads variaveis.
- Usar OpenRouter como gateway inicial, mas manter model registry e routing policy no CKOS.
- Usar MCP como camada de integracao de tools, nao como fonte de verdade do runtime.
- Combinar event viewer de dominio com OpenTelemetry para traces/logs/metrics tecnicos.

## Decisoes que ainda precisam de aprovacao humana

- Aprovar ou rejeitar Postgres append-only como event store MVP.
- Aprovar formato final do event envelope CKOS.
- Escolher job runner MVP: pg-boss, BullMQ, Supabase Queues ou outro.
- Decidir se Temporal fica fora do MVP ou entra em algum fluxo especifico.
- Aprovar estrategia de multi-tenancy em Supabase.
- Aprovar politica inicial de RLS e uso de `service_role`.
- Aprovar OpenRouter como gateway inicial de modelos.
- Aprovar thresholds iniciais de cost guard e approval gates.
- Aprovar politica de promocao de memoria e decay.
- Aprovar estrategia MCP: stdio local primeiro, HTTP depois, ou ambos.

## Itens que podem virar canonico depois

- Event envelope CKOS.
- Tabelas conceituais de `events`, `workflow_runs`, `workflow_step_runs`, `workflow_cards`, `agent_runs`, `approvals`, `cost_ledger`, `provider_calls`, `memory_updates`, `rag_queries`, `tool_calls`.
- State machines minimas para workflow e agent run.
- Job queue adapter contract.
- Approval gate lifecycle.
- Cost guard lifecycle.
- Model registry schema.
- Tools registry schema.
- Observability IDs e log schema.
- Event viewer/replay requirements.

## Fontes primarias usadas como base

- CloudEvents spec: https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md
- BullMQ docs: https://docs.bullmq.io/
- pg-boss GitHub: https://github.com/timgit/pg-boss
- Temporal docs: https://docs.temporal.io/
- Supabase docs: https://supabase.com/docs/
- OpenRouter docs: https://openrouter.ai/docs/
- Model Context Protocol docs: https://modelcontextprotocol.io/docs/
- OpenTelemetry docs: https://opentelemetry.io/docs/

## Observacao de governanca

Esta pasta e laboratorio de pesquisa. Nada aqui deve ser tratado como verdade canonica ate passar por revisao PMO/tecnica/founder e ser promovido explicitamente.
