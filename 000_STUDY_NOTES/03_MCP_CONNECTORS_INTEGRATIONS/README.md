# 03_MCP_CONNECTORS_INTEGRATIONS

## Funcao da pasta

Estudar MCP, conectores, APIs, collectors, webhooks, n8n, integracoes nativas e ingestion privada.

## O que pode entrar

Notas tecnicas, matrizes de risco, manifests de exports, comparativos e patch candidates futuros.

## O que nao pode entrar

Tokens, secrets, integracao real, endpoint ativo, n8n runtime ou MCP tratado como core autonomo.

## Naming obrigatorio

`YYYYMMDD_source-tool_topic_owner_status.md`

## Regra de saida

Gerar patch candidate para futuros docs 26-28, se aprovado.

## Quando mover para CANONICAL

Nunca direto. Exige patch plan e aprovacao Founder.

## Quando arquivar

Quando referencia tecnica for insegura, vencida ou contraria a policy CKOS.

## Risco principal

Bypass de policy_engine, tool_router, approval_gate, cost_guard, audit_logs, tenant isolation ou secret_refs.

## Politica de PII

Nao persistir payloads com dados de tenant sem sanitizacao.

## Politica de provenance

Registrar provider, source_tool, data, escopo, tenant e metodo de coleta.

