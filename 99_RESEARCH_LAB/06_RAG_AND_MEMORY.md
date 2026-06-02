# 06_RAG_AND_MEMORY

## Objetivo

Estudar padroes para RAG e memoria do CKOS: pgvector, `memory_updates`, regras de promocao, retrieval policies e decay policy.

## Opcoes analisadas

1. pgvector em Supabase/Postgres

- Vetores ficam no mesmo Postgres do dominio.
- Permite RLS e filtros relacionais junto da busca semantica.
- Bom para MVP, debug e multi-tenancy.

2. Vector DB externo

- Pode escalar melhor para volume alto e recursos avancados.
- Adiciona custo, sync e risco de vazamento cross-tenant se namespaces forem mal geridos.

3. RAG hibrido: keyword + vector + filtros relacionais

- Melhor controle de precisao.
- Exige mais tuning e evals.

4. Memory writer direto em memoria canonica

- Rapido.
- Alto risco de poluir memoria com outputs nao verificados.

5. Memory updates em staging

- `memory_updates` recebe candidatos.
- Promocao depende de fonte, evidencia, confianca, QA/aprovacao e politica de validade.
- Mais seguro para CKOS.

## Recomendacao para CKOS MVP

Recomendacao preliminar: usar pgvector em Supabase/Postgres no MVP, com `memory_updates` append-only como staging antes de promover para memoria operacional.

Modelo conceitual:

```txt
memory_updates
- id
- source_type
- source_ref
- project_id
- proposed_memory_type
- content
- evidence_refs
- confidence
- risk_level
- status
- proposed_by_agent
- reviewed_by
- created_at
```

Promocao sugerida:

- `proposed`: agente sugeriu memoria.
- `validated`: schema/evidence check passou.
- `approved`: humano ou policy aprovou quando necessario.
- `promoted`: entrou em `memories`.
- `rejected`: nao deve ser recuperada.
- `expired`: nao deve ser recuperada por padrao.

Retrieval policy:

- Sempre filtrar por `org_id`, `workspace_id`, `project_id` quando aplicavel.
- Aplicar RLS e permissao antes de retornar conteudo ao agente/modelo.
- Misturar similaridade vetorial com filtros de tipo, freshness, confidence, source reliability e approval status.
- Registrar `rag_query`, `rag_results` e quais memorias entraram no context packet.

Decay policy:

- Nao apagar memoria automaticamente no MVP.
- Usar `freshness_score`, `valid_until`, `last_used_at`, `decay_reason`.
- Memoria antiga pode continuar auditavel, mas perde prioridade de retrieval.

## Por que essa recomendacao

O CKOS depende de memoria confiavel para contexto, perguntas, planner, QA, ROI e feedback. Gravar tudo direto em memoria canonica cria poluicao semantica. O staging em `memory_updates` cria um funil auditavel.

Supabase/pgvector e suficiente para MVP porque combina vetor, relacional, RLS, migrations e debug SQL. A documentacao de Supabase mostra que pgvector e uma extensao Postgres e que RAG pode respeitar RLS, o que e central para multi-tenancy do CKOS.

## Trade-offs

- pgvector simplifica a stack, mas pode exigir tuning de indices e particionamento com volume alto.
- Staging reduz risco de memoria ruim, mas adiciona latencia no learning loop.
- Decay por score e validade e mais seguro que delete, mas exige bom criterio de retrieval.
- RLS em busca vetorial protege acesso, mas pode afetar performance se as policies forem pesadas.

## Riscos

- Cross-tenant leakage por filtro ausente.
- Memoria de baixa confianca ser recuperada como verdade.
- Embedding antigo ficar incompatibile com novo modelo.
- Decay mal calibrado esconder informacao ainda relevante.
- Guardar dados sensiveis em chunk sem classificacao.

## Como implementar depois

1. Habilitar `pgvector` via migration controlada.
2. Criar tabelas `documents`, `document_chunks`, `memories`, `memory_updates`, `rag_queries`, `rag_results`.
3. Criar colunas relacionais para tenant, projeto, tipo, status, confidence e freshness.
4. Criar embeddings com dimensao fixa por `embedding_model_id`.
5. Criar policies de RLS para chunks e memories.
6. Criar memory writer que gera candidatos, nao promove direto.
7. Criar evals de retrieval relevance, freshness e leakage.

## Dependencias

- Supabase/Postgres.
- pgvector.
- Embedding provider.
- RLS/policy engine.
- Memory policy registry.
- QA/eval runner.
- Fontes primarias consultadas:
  - Supabase vector columns/pgvector: https://supabase.com/docs/guides/ai/vector-columns
  - Supabase RAG with permissions: https://supabase.com/docs/guides/ai/rag-with-permissions
  - Supabase RLS: https://supabase.com/docs/guides/database/postgres/row-level-security

## O que nao fazer agora

- Nao usar vector DB externo antes do MVP provar volume/necessidade.
- Nao promover memoria sem evidencia minima.
- Nao recuperar memoria sem filtro de tenant/projeto.
- Nao deletar memoria automaticamente como substituto de decay.
- Nao criar memory writer backend agora.
