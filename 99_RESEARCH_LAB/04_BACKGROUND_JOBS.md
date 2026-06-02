# 04_BACKGROUND_JOBS

## Objetivo

Comparar BullMQ, pg-boss, Supabase table polling e Temporal para jobs de background do CKOS Runtime, considerando simplicidade, custo, debug e escalabilidade.

## Opcoes analisadas

1. BullMQ

- Biblioteca Node.js robusta, baseada em Redis.
- Suporta retries, backoff, prioridades, repeatable jobs, concorrencia, parent-child dependencies e recuperacao de crashes.
- Bom quando Redis ja e parte central da stack.
- Para CKOS MVP local, adiciona dependencia operacional extra.

2. pg-boss

- Job queue em Node.js sobre PostgreSQL.
- Usa Postgres como mecanismo de fila, com recursos como automatic retries, exponential backoff, cron, priority e dead letter queues.
- Bom quando o sistema ja depende de Postgres/Supabase e quer menos moving parts.
- Throughput tende a ser menor que Redis, mas suficiente para MVP.

3. Supabase table polling manual

- Tabela `jobs` custom, workers fazem polling com locks.
- Muito simples de entender e debugar.
- Alto risco de reinventar retry, lease, dead letter, concorrencia, backoff e stuck job cleanup.

4. Supabase Queues / PGMQ

- Fila Postgres-native gerenciada pela plataforma Supabase.
- Promete delivery duravel, visibility window, archival, auth/RLS e monitoramento no Dashboard.
- Boa opcao se o projeto quiser ficar estritamente dentro do ecossistema Supabase.
- Precisa validar maturidade, disponibilidade no plano usado e ergonomia local.

5. Temporal

- Durable execution e workflow orchestration completos.
- Forte para processos longos, retries, replay, timeouts e heartbeats.
- Mais pesado que o necessario para MVP local inicial.

## Recomendacao para CKOS MVP

Recomendacao preliminar para MVP local: usar pg-boss como job runner primario, encapsulado por uma interface `JobQueueAdapter`, mantendo BullMQ e Temporal como substituiveis no futuro.

Criterios:

| Criterio | BullMQ | pg-boss | Supabase polling | Temporal |
|---|---|---|---|---|
| Simplicidade local | Media, exige Redis | Alta, usa Postgres | Alta no inicio | Baixa |
| Custo operacional | Redis extra | Baixo | Baixo, mas caro em manutencao | Alto |
| Debug | Redis tooling | SQL direto | SQL direto | UI e CLI proprios |
| Escalabilidade | Alta | Media | Baixa/media | Alta |
| Fit CKOS MVP | Bom, mas cedo | Melhor equilibrio | Apenas spike | Futuro |

Usar jobs apenas para execucao atomica. A fila nao deve ser a fonte de verdade do workflow; ela agenda trabalho. A verdade continua em `events`, `workflow_runs`, `agent_runs` e projections.

## Por que essa recomendacao

O CKOS ja tende a Postgres/Supabase para event store, state, cost ledger, approvals, memory e projections. pg-boss evita adicionar Redis no MVP e preserva debug por SQL.

BullMQ e mais forte para throughput e ecossistema de jobs em Redis. Temporal e mais forte para durable workflows complexos. Mas no momento, o custo de operar e modelar essas ferramentas parece maior que o ganho para MVP local.

## Trade-offs

- pg-boss reduz infraestrutura, mas usa o mesmo banco que o dominio; jobs intensos podem competir com queries de runtime.
- BullMQ escala melhor em throughput, mas adiciona Redis e uma superficie nova de monitoramento.
- Supabase table polling parece simples, mas tende a acumular bugs de lease e retry.
- Temporal resolveria muito, mas exige aprender e respeitar determinismo, Activities e deploy proprio/cloud.

## Riscos

- A fila virar source of truth de estado.
- Jobs nao idempotentes causarem efeitos duplicados em retry.
- Dead letter queue nao ser monitorada.
- Jobs longos ficarem sem heartbeat ou timeout.
- Misturar jobs de baixa prioridade com approvals/cost guard criticos na mesma fila.

## Como implementar depois

1. Definir interface `enqueue`, `schedule`, `cancel`, `mark_complete`, `mark_failed`, `retry`, `dead_letter`.
2. Criar filas por tipo: `workflow_steps`, `agent_runs`, `provider_calls`, `projectors`, `memory_writer`, `watchdogs`.
3. Cada job deve carregar apenas IDs e contexto minimo, nunca payload grande.
4. Worker sempre reidrata estado a partir do banco/event store.
5. Configurar retry limit, backoff, timeout e DLQ por tipo de job.
6. Criar dashboard/debug SQL para jobs ativos, falhos e DLQ.
7. Medir quando a troca para BullMQ/Temporal faz sentido.

## Dependencias

- Postgres/Supabase local.
- Adapter de queue.
- Worker monitor.
- Event store e idempotency.
- Fontes primarias consultadas:
  - pg-boss GitHub: https://github.com/timgit/pg-boss
  - BullMQ docs: https://docs.bullmq.io/
  - BullMQ idempotent jobs: https://docs.bullmq.io/patterns/idempotent-jobs
  - Supabase Queues: https://supabase.com/docs/guides/queues
  - Temporal docs: https://docs.temporal.io/workflow-execution

## O que nao fazer agora

- Nao implementar BullMQ e pg-boss ao mesmo tempo.
- Nao criar polling manual como solucao permanente.
- Nao deixar job payload carregar contexto grande, prompts completos ou arquivos.
- Nao usar Temporal antes de aprovar custo operacional.
- Nao implementar backend ainda.
