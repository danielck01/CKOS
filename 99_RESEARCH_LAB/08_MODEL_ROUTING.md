# 08_MODEL_ROUTING

## Objetivo

Estudar model routing para o CKOS: uso de OpenRouter, model registry, reasoning level, fallback models e estimativa de custo.

## Opcoes analisadas

1. Chamar providers diretamente

- Controle maximo por provider.
- Mais SDKs, billing, formatos e fallbacks para manter.

2. OpenRouter como gateway

- Um endpoint para muitos modelos/providers.
- API semelhante a OpenAI Chat Completions.
- Models API retorna metadados como context length, pricing, architecture e supported parameters.
- Fallbacks e provider routing ajudam disponibilidade e custo.

3. Model registry proprio do CKOS

- CKOS nao depende de provider como fonte de politica.
- Guarda capabilities aprovadas, risco, custo, privacidade, defaults e fallback chain.
- Precisa sync/atualizacao periodica.

4. Router interno sem gateway

- Poderoso no longo prazo.
- Cedo demais para MVP, especialmente com muitos modelos mudando rapido.

## Recomendacao para CKOS MVP

Recomendacao preliminar: usar OpenRouter como provider gateway inicial, mas manter `model_registry` e `model_router_policy` dentro do CKOS. OpenRouter deve ser adaptador, nao arquitetura.

Campos sugeridos para `model_registry`:

```txt
model_key
provider_model_id
provider
context_length
input_modalities
output_modalities
supported_parameters
supports_tools
supports_structured_output
supports_reasoning
default_reasoning_effort
pricing_prompt
pricing_completion
pricing_request
privacy_tier
quality_tier
latency_tier
status
last_synced_at
```

Roteamento por policy:

- `task_type`: classify, plan, write, code, QA, RAG, extraction, reasoning.
- `risk_level`: low, medium, high.
- `privacy_level`: public, internal, sensitive, restricted.
- `budget_level`: cheap, balanced, premium.
- `reasoning_effort`: none, minimal, low, medium, high, xhigh quando suportado.
- `fallback_chain`: modelos em ordem de preferencia.

Estimativa de custo:

- Preflight usa tokens estimados + pricing snapshot.
- Pos-call usa usage real e generation stats quando disponivel.
- Fallback deve registrar modelo efetivamente usado.

## Por que essa recomendacao

O CKOS deve possuir a orquestracao: prompts, policies, memory, evals, approvals, cost guard e roteamento. Modelos externos sao motores substituiveis.

OpenRouter reduz friccao no MVP e permite consultar modelos, parametros suportados, pricing e fallbacks. Mas se regras ficarem hardcoded no OpenRouter request, o CKOS perde governanca. O registry proprio preserva independencia.

## Trade-offs

- OpenRouter acelera integracao, mas adiciona dependencia de gateway.
- Registry proprio exige sync e revisao periodica.
- Fallback aumenta disponibilidade, mas pode mudar qualidade, custo e privacidade.
- Reasoning effort melhora tarefas complexas, mas aumenta tokens/custo quando suportado.

## Riscos

- Modelo fallback nao suportar tools ou structured output.
- Pricing mudar e estimativa ficar desatualizada.
- Provider routing escolher endpoint incompatibilidade com politica de dados.
- Reasoning tokens elevarem custo sem aparecer claramente ao usuario.
- Prompt/model pair nao ser avaliado por task type.

## Como implementar depois

1. Criar `model_registry` e `model_registry_snapshots`.
2. Criar sync manual/periodico da OpenRouter Models API.
3. Criar `model_router.select(task_context)` que retorna modelo, parametros, fallback chain e custo estimado.
4. Criar `provider_calls` com request/response metadata higienizada.
5. Criar evals por model/task type.
6. Criar allowlist por privacy tier.
7. Criar fallback policy que valida capabilities antes da chamada.

## Dependencias

- OpenRouter API key.
- Cost guard.
- Eval runner.
- Provider call logger.
- Privacy/data classification.
- Prompt registry.
- Fontes primarias consultadas:
  - OpenRouter Models API: https://openrouter.ai/docs/guides/overview/models
  - OpenRouter model fallbacks: https://openrouter.ai/docs/guides/routing/model-fallbacks
  - OpenRouter API reference/cost stats: https://openrouter.ai/docs/api/reference/overview/
  - OpenRouter parameters/reasoning effort: https://openrouter.ai/docs/api/reference/parameters

## O que nao fazer agora

- Nao hardcodar um unico modelo como arquitetura.
- Nao delegar policy de custo/risco ao provider.
- Nao usar fallback sem validar capabilities.
- Nao estimar custo apenas depois da chamada.
- Nao tomar decisao final de modelos nesta pesquisa.
