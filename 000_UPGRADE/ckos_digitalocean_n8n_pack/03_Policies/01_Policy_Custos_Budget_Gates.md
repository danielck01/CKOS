---
title: "Policy — Custos e Budget Gates"
tipo: "policy"
area: "Governança, Finanças"
---

# Policy — Custos e Budget Gates

## Regra

Nenhum agente, workflow ou serviço pode executar ação com impacto financeiro sem budget gate.

## Gatilhos de aprovação

Exigir aprovação humana quando:

- criar novo serviço pago;
- escalar VPS;
- ativar scraper com alto volume;
- enviar campanha;
- consumir modelo caro;
- executar workflow em massa;
- acessar conector sensível;
- alterar plano/crédito de usuário.

## Saída esperada

Toda execução deve registrar:

```json
{
  "decision": "approved_or_blocked",
  "reason": "motivo",
  "estimated_cost_usd": 0,
  "approved_by": "human_or_policy",
  "timestamp": "ISO-8601"
}
```
