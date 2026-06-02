# Response Memory

Status: waiting_for_real_answers

## Como registrar

Cada resposta da Miriam deve ser registrada como uma unidade de memoria:

```yaml
response_id:
date:
question:
raw_answer:
classified_as:
  - fact
  - hypothesis
  - validation_needed
  - decision
impact:
  - context
  - risk
  - strategy
  - artifact
source:
  - miriam_answer
approval_status:
next_question:
```

## Respostas registradas

Nenhuma resposta real de Miriam foi registrada nesta pasta ate esta versao.

## Regra

Nao preencher com suposicoes do agente. Hipoteses devem ficar em `../00_CONTEXT/03_ASSUMPTIONS_AND_GAPS.md`.
