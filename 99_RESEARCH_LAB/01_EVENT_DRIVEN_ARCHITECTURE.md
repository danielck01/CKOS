# 01_EVENT_DRIVEN_ARCHITECTURE

## Objetivo

Estudar como o CKOS Runtime deve representar eventos de forma rastreavel, auditavel e idempotente, sem promover uma decisao canonica.

O foco desta nota e preparar uma recomendacao implementavel para:

- event envelope
- eventos append-only
- audit trail
- idempotency
- `correlation_id` e `causation_id`

## Opcoes analisadas

1. Envelope custom CKOS em Postgres

- Cada evento e uma linha em `events`.
- Campos minimos: `id`, `event_type`, `schema_version`, `aggregate_type`, `aggregate_id`, `org_id`, `workspace_id`, `project_id`, `actor_type`, `actor_id`, `correlation_id`, `causation_id`, `idempotency_key`, `occurred_at`, `payload`, `metadata`.
- Simples de consultar, facil de debugar e compativel com Supabase/Postgres.
- Exige disciplina forte de schema, naming e validacao.

2. Envelope inspirado em CloudEvents

- Usa conceitos padronizados como `id`, `source`, `type`, `specversion`, `subject`, `time`, `datacontenttype` e `data`.
- Ajuda interoperabilidade futura com brokers, webhooks e MCP/API events.
- Precisa de extensoes CKOS para tenancy, causation, idempotency, actor e aggregate.

3. Broker-first com Redis Streams, NATS ou Kafka

- Excelente para throughput e distribuicao.
- Adiciona uma camada operacional antes do CKOS precisar dela.
- Pode enfraquecer a visibilidade inicial se o banco nao continuar sendo fonte de verdade.

4. Audit log simples sem event sourcing

- Mais rapido de implementar.
- Insuficiente para replay, projections, causalidade, workflow debugging e memory writer confiavel.

## Recomendacao para CKOS MVP

Recomendacao preliminar: usar Postgres/Supabase como event store append-only, com envelope CKOS inspirado em CloudEvents, mas nao tentar ser CloudEvents puro no MVP.

Envelope sugerido:

```txt
events
- id uuid primary key
- event_type text not null
- schema_version int not null
- source text not null
- aggregate_type text not null
- aggregate_id uuid null
- org_id uuid not null
- workspace_id uuid null
- project_id uuid null
- actor_type text not null
- actor_id text null
- correlation_id uuid not null
- causation_id uuid null
- idempotency_key text null
- occurred_at timestamptz not null default now()
- payload jsonb not null
- metadata jsonb not null default '{}'
```

Regras sugeridas:

- `correlation_id` agrupa tudo que nasceu da mesma intencao, run ou comando raiz.
- `causation_id` aponta para o evento que causou o evento atual.
- `idempotency_key` previne duplicidade por comando, run, provider call ou projection.
- Correcoes devem ser eventos compensatorios, nao `UPDATE` no evento original.
- Projections podem ser reconstruidas a partir de `events`.

## Por que essa recomendacao

O CKOS precisa transformar intencao em projeto, contexto, perguntas, planner, workflow cards, runs, approvals, QA, ROI, feedback e memory writer. Esse fluxo pede causalidade completa, nao apenas logs.

Postgres/Supabase reduz custo operacional no MVP, preserva debug via SQL e combina com a direcao ja existente do vault: event-sourced + CQRS + append-only event log. CloudEvents e util como referencia de envelope porque ja formaliza campos basicos e unicidade por `source` + `id`, mas o CKOS precisa de campos de dominio que CloudEvents nao cobre diretamente.

## Trade-offs

- Simplicidade vs throughput: Postgres e otimo para MVP e auditoria, mas nao substitui Kafka/NATS em escala alta.
- Flexibilidade vs rigor: `payload jsonb` acelera iteracao, mas exige schema registry e validacao.
- Auditabilidade vs volume: append-only cresce rapido e precisa de particionamento/retencao.
- Padrao externo vs dominio CKOS: CloudEvents ajuda, mas nao deve forcar o CKOS a perder `correlation_id`, `causation_id`, tenancy e actor metadata.

## Riscos

- Eventos sem schema versionado virarem blobs dificeis de evoluir.
- Falta de `idempotency_key` causar duplicacao de runs, approvals ou cost ledger.
- Gravar PII ou secrets em `payload`.
- Projections divergirem por consumidores nao idempotentes.
- `correlation_id` gerado tarde demais, quebrando a timeline da intencao.

## Como implementar depois

1. Criar migration `events` com indices por `correlation_id`, `causation_id`, `aggregate_type/aggregate_id`, `project_id/occurred_at` e `event_type/occurred_at`.
2. Criar uma funcao unica `append_event(command_context, event_type, payload, metadata)`.
3. Bloquear `UPDATE` e `DELETE` em `events` para roles de app; permitir somente migrations administrativas aprovadas.
4. Criar registry de eventos com `event_type`, `schema_version`, payload schema e producer autorizado.
5. Criar projector runner idempotente usando `event_id` como checkpoint.
6. Criar event viewer minimo por `correlation_id`.

## Dependencias

- Supabase/Postgres para event store.
- Schema registry para payloads.
- Policy engine para filtrar evento por tenant e permissao.
- Projectors CQRS para workflow cards, cost, approvals, runs e UI/event viewer.
- Fontes primarias consultadas:
  - CloudEvents spec: https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md
  - Supabase JSON/JSONB: https://supabase.com/docs/guides/database/json
  - Supabase query optimization: https://supabase.com/docs/guides/database/query-optimization

## O que nao fazer agora

- Nao introduzir Kafka/NATS como requisito do MVP.
- Nao criar event bus sem event store append-only.
- Nao permitir updates manuais em eventos.
- Nao salvar prompts completos, secrets ou dados sensiveis brutos no event payload.
- Nao promover este envelope para canonico sem aprovacao tecnica/humana.
