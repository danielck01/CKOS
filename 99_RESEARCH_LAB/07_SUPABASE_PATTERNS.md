# 07_SUPABASE_PATTERNS

## Objetivo

Estudar padroes Supabase/Postgres para migrations, RLS, multi-tenancy, indexes e escolha entre JSONB e campos relacionais no CKOS Runtime.

## Opcoes analisadas

1. Shared schema multi-tenant com RLS

- Uma base/tabelas compartilhadas, com `org_id`, `workspace_id`, `project_id`.
- RLS filtra acesso por usuario/role.
- Melhor custo e simplicidade para MVP.

2. Schema por tenant

- Mais isolamento logico.
- Mais complexo para migrations, analytics e operacao.

3. Database por tenant

- Melhor isolamento forte.
- Custo e operacao altos, inadequado para MVP.

4. JSONB-first

- Rapido para iterar payloads variaveis.
- Pode virar anti-modelo se usado para estado, joins, filtros e relatorios.

5. Relational-first com JSONB nas bordas

- Campos estruturados para identidade, estado, custos, indices, filtros e joins.
- JSONB para payload de eventos, metadata, provider response e configs variaveis.

## Recomendacao para CKOS MVP

Recomendacao preliminar: shared schema multi-tenant com RLS desde a primeira migration, usando campos relacionais para invariantes de runtime e JSONB apenas para payloads variaveis/versionados.

Padrao de colunas:

```txt
id uuid primary key
org_id uuid not null
workspace_id uuid null
project_id uuid null
created_at timestamptz not null
updated_at timestamptz null
status text not null
payload jsonb null
metadata jsonb not null default '{}'
```

Campos relacionais obrigatorios quando forem usados para:

- RLS
- join
- filtro frequente
- ordenacao
- estado de workflow/run
- custo
- approval
- ownership
- retention
- dashboards

JSONB adequado para:

- event payloads versionados
- provider raw metadata higienizada
- tool arguments/result metadata
- configs variaveis de registry
- snapshots de contexto nao consultados frequentemente

## Por que essa recomendacao

Supabase opera sobre Postgres. A propria documentacao recomenda migrations para controlar evolucao de schema, RLS para tabelas expostas, indexes alinhados ao padrao de query e JSONB para dados variaveis, sem exagerar porque o valor relacional vem de query, join e integridade.

O CKOS precisa de multi-tenancy, audit trail e projections. Isso favorece colunas explicitas para escopo e estado, com JSONB apenas onde a variabilidade e real.

## Trade-offs

- Shared schema e barato, mas RLS incorreta vira risco critico.
- Campos relacionais exigem mais migrations, mas melhoram query, custo e type safety.
- JSONB acelera iteracao, mas dificulta constraints e indices se abusado.
- Indexar tudo melhora leitura no curto prazo, mas reduz performance de escrita.

## Riscos

- Tabela criada por SQL sem RLS habilitado.
- Policy permissiva demais permitir vazamento cross-tenant.
- `service_role` usado em rotas comuns e bypassando RLS sem necessidade.
- JSONB esconder campos que deveriam ser auditaveis/indexados.
- Falta de indices compostos em `org_id/project_id/status/created_at` degradar projections.

## Como implementar depois

1. Criar migrations com Supabase CLI, nunca alteracao manual nao rastreada.
2. Toda tabela de dominio deve ter `org_id`; onde aplicavel, `workspace_id` e `project_id`.
3. Habilitar RLS em tabelas expostas e criar policies por papel/escopo.
4. Criar indexes por query real: tenant + status + tempo; aggregate + tempo; correlation_id; event_type.
5. Usar `explain` para validar indices.
6. Criar constraints para status enums ou check constraints.
7. Validar JSONB critico com `pg_jsonschema` quando fizer sentido.

## Dependencias

- Supabase CLI.
- Policy/RBAC model.
- Migration review.
- Query plan review.
- Testes de RLS.
- Fontes primarias consultadas:
  - Supabase database migrations: https://supabase.com/docs/guides/deployment/database-migrations
  - Supabase RLS: https://supabase.com/docs/guides/database/postgres/row-level-security
  - Supabase query optimization: https://supabase.com/docs/guides/database/query-optimization
  - Supabase JSON/JSONB: https://supabase.com/docs/guides/database/json

## O que nao fazer agora

- Nao usar database por tenant no MVP.
- Nao criar tabelas publicas sem RLS.
- Nao colocar estado operacional apenas dentro de JSONB.
- Nao criar indices especulativos sem query alvo.
- Nao editar schema canonico nesta etapa.
