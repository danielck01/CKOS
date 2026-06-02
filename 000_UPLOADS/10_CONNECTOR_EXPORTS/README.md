# 10_CONNECTOR_EXPORTS

## Funcao da pasta

Guardar exports brutos vindos de conectores, APIs, webhooks, n8n, MCP, browser-use ou importacoes manuais.

## O que pode entrar

Exports JSON/CSV/MD, payloads sanitizados, logs de coleta e amostras de retorno de ferramenta.

## O que nao pode entrar

Tokens, secrets, refresh tokens, credenciais, dumps de tenant ou chamadas nao auditadas como regra canonica.

## Naming obrigatorio

`YYYYMMDD_source-tool_topic_owner_status.ext`

## Regra de saida

Gerar source manifest com provider, metodo, actor, tenant, policy, custo e risco.

## Quando mover para STUDY

Quando o export informar arquitetura de MCP, collector, API, webhook, n8n ou integracao nativa.

## Quando arquivar

Quando contiver secrets, PII nao sanitizada, payload incompleto ou origem incerta.

## Risco principal

Bypass de policy_engine, tool_router, cost_guard, audit_logs ou tenant isolation.

## Politica de PII

Sanitizar payloads e registrar tenant/contexto sem expor dados desnecessarios.

## Politica de provenance

Registrar provider, ferramenta, data, metodo, escopo, tenant e owner.

