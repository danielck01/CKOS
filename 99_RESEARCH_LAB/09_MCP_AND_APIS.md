# 09_MCP_AND_APIS

## Objetivo

Estudar opcoes de integracao MCP e APIs para o CKOS: contratos, tools registry e integracao com CLI local.

## Opcoes analisadas

1. API interna CKOS-first

- Contratos de dominio controlados: intent, project, context, workflow, run, approval, cost, memory.
- Mais previsivel para runtime.
- Requer adaptadores para tools externas.

2. MCP stdio para ferramentas locais

- Cliente lanca servidor MCP como subprocesso.
- Bom para CLIs locais, filesystem controlado e ferramentas dev.
- Exige cuidado para stdout conter apenas mensagens MCP validas.

3. MCP Streamable HTTP

- Bom para servidores remotos, multiplas conexoes e notificacoes.
- Precisa auth, validacao de Origin e seguranca de rede.

4. Chamada direta de CLI sem MCP

- Simples para MVP interno.
- Menos padronizada; input/output e erros podem virar parsing fragil.

5. Tools registry CKOS

- Catalogo interno de tools permitidas, schemas, scopes, timeout, cost class e approval policy.
- Essencial para deny-by-default.

## Recomendacao para CKOS MVP

Recomendacao preliminar: definir contratos internos CKOS primeiro e criar uma camada de adapters. Usar MCP para ferramentas locais e externas quando o contrato MCP trouxer valor, mas nao fazer MCP ser a fonte de verdade do runtime.

Arquitetura sugerida:

```txt
CKOS Runtime
  -> tools_registry
  -> tool_router
  -> adapter:
       - internal_api
       - mcp_stdio
       - mcp_http
       - local_cli
       - provider_api
```

Tool registry minimo:

```txt
tool_key
adapter_type
input_schema
output_schema
allowed_agents
required_scopes
risk_level
approval_required
timeout_ms
max_cost
secrets_ref
status
```

API contracts prioritarios:

- `POST /intents`
- `POST /workflow-runs`
- `POST /workflow-runs/{id}/cancel`
- `POST /approvals/{id}/decision`
- `POST /agent-runs`
- `POST /tools/{tool_key}/invoke`
- `GET /runs/{id}/events`
- `GET /correlations/{correlation_id}/timeline`

## Por que essa recomendacao

MCP padroniza descoberta e chamada de tools, resources e prompts. A especificacao usa JSON-RPC, capability negotiation e transportes como stdio e Streamable HTTP. Isso e excelente para integrar ferramentas, mas o CKOS precisa manter ownership do dominio: approvals, cost guard, policies, audit trail e memory writer.

Para CLI local, MCP stdio e uma boa opcao quando houver servidor MCP confiavel. Quando nao houver, um adapter `local_cli` com schema, timeout e logging pode ser suficiente no MVP.

## Trade-offs

- API interna da controle, mas exige adapters.
- MCP reduz integracao custom, mas aumenta superficie de seguranca.
- CLI direto e rapido, mas parsing de texto e fragil.
- Tools registry adiciona governanca, mas exige manutencao de schemas.

## Riscos

- Tool poisoning ou prompt injection via descricao de tool/resource.
- Servidor MCP local exposto em interface de rede errada.
- Segredos vazarem por env, stdout, logs ou payload.
- Tool ser chamada fora de approval/cost guard.
- Falha de CLI virar output ambiguo sem codigo de erro estruturado.

## Como implementar depois

1. Definir `tools_registry` deny-by-default.
2. Criar `tool_router.invoke(tool_key, input, run_context)`.
3. Validar input/output por JSON Schema.
4. Envolver toda chamada em event logging, timeout, approval check e cost guard.
5. Para MCP stdio, capturar stderr como log e exigir stdout MCP valido.
6. Para MCP HTTP, exigir auth, allowlist de host e validacao de Origin.
7. Criar tool call replay/debug com `correlation_id`.

## Dependencias

- Tools registry.
- Policy engine.
- Approval/cost guard.
- Secrets manager.
- Event store.
- Observability.
- Fontes primarias consultadas:
  - MCP architecture: https://modelcontextprotocol.io/docs/learn/architecture
  - MCP server concepts/tools/resources/prompts: https://modelcontextprotocol.io/docs/learn/server-concepts
  - MCP transports: https://modelcontextprotocol.io/specification/2025-06-18/basic/transports
  - MCP authorization: https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization

## O que nao fazer agora

- Nao expor tools sem registry e policy.
- Nao deixar MCP decidir autorizacao de dominio do CKOS.
- Nao executar CLI com argumentos livres gerados por LLM sem schema/allowlist.
- Nao logar secrets.
- Nao criar frontend ou backend nesta fase.
