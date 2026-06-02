# 05_APPROVAL_AND_COST_GUARD

## Objetivo

Estudar padroes para approval gates, thresholds, cost ledger, budget watchdog e provider call logging no CKOS Runtime.

## Opcoes analisadas

1. Approval como flag em workflow

- Simples.
- Insuficiente para auditoria, expiracao, escalonamento e replay.

2. Approval event-sourced

- `approval_requested`, `approval_granted`, `approval_denied`, `approval_expired`, `approval_escalated`.
- Permite audit trail e bloqueio real de workflow.
- Mais verboso, mas alinhado ao CKOS.

3. Cost guard apenas por provider

- Usa limites externos ou creditos do provedor.
- Nao atribui custo a projeto, workflow, agente, tool ou cliente.

4. Cost ledger interno

- Registra estimativa, reserva, custo real e ajuste por chamada.
- Permite budget watchdog, ROI e auditoria.
- Exige logging consistente em todos os providers/tools.

## Recomendacao para CKOS MVP

Recomendacao preliminar: modelar approval e cost guard como mecanismos de runtime, nao como UI ou convencao de prompt.

Approval gates:

- Gate antes de acoes caras, irreversiveis, externas, sensiveis ou voltadas ao cliente.
- Approval deve ter `scope`, `requested_by`, `required_role`, `risk_level`, `estimated_cost`, `expires_at`, `decision`, `decision_reason`.
- O workflow deve ficar em `waiting_approval` ate evento terminal do approval.

Cost guard:

- Preflight antes de toda model/tool/provider call.
- Ledger append-only para estimativa, reserva e custo real.
- Watchdog por `org`, `workspace`, `project`, `workflow_run`, `agent_run` e `provider`.
- Thresholds em camadas:
  - `info`: registra e segue.
  - `warning`: registra e notifica.
  - `soft_gate`: pede aprovacao.
  - `hard_stop`: bloqueia ate aprovacao humana.

Provider call logging minimo:

```txt
provider_calls
- id
- provider
- model_or_tool
- request_kind
- status
- tokens_in
- tokens_out
- reasoning_tokens
- estimated_cost_usd
- actual_cost_usd
- latency_ms
- agent_run_id
- workflow_run_id
- correlation_id
- causation_id
- idempotency_key
- error_code
```

## Por que essa recomendacao

O CKOS precisa controlar autonomia e custo como parte do runtime. Aprovacao nao e apenas "perguntar ao usuario"; e uma transicao que bloqueia, registra, expira e cria responsabilidade.

O mesmo vale para custo. OpenRouter e outros providers retornam usage/cost e permitem consultar generation stats, mas o CKOS precisa atribuir esse custo a agente, workflow, projeto e ROI. Sem ledger interno, custo vira dado externo disperso.

## Trade-offs

- Preflight aumenta latencia, mas evita surpresa financeira.
- Ledger append-only aumenta volume, mas permite auditoria e ROI.
- Approval gates reduzem autonomia, mas protegem a CKCompany de risco e custo.
- Thresholds muito baixos travam operacao; thresholds altos demais deixam custo escapar.

## Riscos

- Custo estimado diferir do custo real por fallback, caching, reasoning tokens ou provider escolhido.
- Approval concedido para um payload e usado em outro.
- Provider call sem `correlation_id` quebrar rastreabilidade.
- Watchdog agir tarde demais se so rodar em batch.
- Prompt pedir autorizacao mas runtime nao bloquear de fato.

## Como implementar depois

1. Criar `approvals`, `approval_events`, `cost_ledger`, `provider_calls`, `budget_policies`.
2. Criar `cost_guard.check_preflight(scope, estimated_cost, risk_level)`.
3. Criar `cost_guard.record_actual(provider_call_result)`.
4. Criar watchdog que soma custo por janela e emite `budget_threshold_crossed`.
5. Vincular `approval_id` a runs/gates que dependem dele.
6. Criar regra de invalidacao: se input/payload muda, approval anterior nao vale.
7. Registrar todos os provider calls, inclusive falhas e fallbacks.

## Dependencias

- Event store.
- Model router.
- Approval policy registry.
- Cost policy registry.
- Provider/model pricing snapshot.
- Observability.
- Fontes primarias consultadas:
  - OpenRouter API usage/cost stats: https://openrouter.ai/docs/api/reference/overview/
  - OpenRouter model fallbacks: https://openrouter.ai/docs/guides/routing/model-fallbacks
  - OpenRouter provider routing/max price: https://openrouter.ai/docs/guides/routing/provider-selection

## O que nao fazer agora

- Nao confiar apenas no saldo do provider.
- Nao tratar approval como comentario em chat.
- Nao permitir chamada cara sem preflight.
- Nao gravar payload sensivel completo em provider logs.
- Nao criar frontend de approvals agora.
