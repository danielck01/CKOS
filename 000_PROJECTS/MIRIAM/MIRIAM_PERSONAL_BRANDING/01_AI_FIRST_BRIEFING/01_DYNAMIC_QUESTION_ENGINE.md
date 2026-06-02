# Dynamic Question Engine

Status: active_protocol

## Funcao

Selecionar a proxima pergunta minima que reduz risco ou destrava decisao. O motor nao deve despejar questionario completo.

## Prioridade de perguntas

1. Perguntas que reduzem risco etico/OAB.
2. Perguntas que eliminam ambiguidade estrategica.
3. Perguntas que distinguem fato de hipotese.
4. Perguntas que permitem escolher artifact parcial.
5. Perguntas de refinamento estetico ou editorial somente depois.

## Algoritmo simulado

```yaml
input:
  - context_state
  - current_gaps
  - risk_level
  - previous_answers
  - blocked_outputs
process:
  - classify_gap
  - rank_by_risk_reduction
  - pick_one_question
  - define_expected_answer_type
  - define_next_artifact_if_answered
output:
  question: single_next_best_question
  reason: why_this_question_now
  artifact_unlocked: optional
```

## Anti-padrao

Nao perguntar "qual tom de voz voce quer?" antes de entender objetivo, risco, fontes, publico e limites profissionais.
