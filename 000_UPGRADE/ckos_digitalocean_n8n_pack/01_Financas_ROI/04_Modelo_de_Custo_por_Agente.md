---
title: "Modelo de Custo por Agente"
tipo: "nota_financeira"
area: "Agentes, Custos, LLMOps"
relacionado:
  - "./02_ROI_Infra_por_Projeto.md"
---

# Modelo de Custo por Agente

## Objetivo

Medir custo por agente, projeto, tarefa e run.

## Campos mínimos

- agent_id;
- project_id;
- model_provider;
- model_name;
- input_tokens;
- output_tokens;
- reasoning_tokens;
- latency_ms;
- estimated_cost_usd;
- status;
- output_type;
- human_review_required.

## Uso

O CKOS deve escolher modelos por função, não por hype.
