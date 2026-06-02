# Artifacts During Conversation

Status: active_protocol

## Funcao

Definir quais artefatos podem nascer durante o briefing sem virar estrategia final prematura.

## Artefatos permitidos durante conversa

- `ASSUMPTIONS_AND_GAPS_UPDATE`
- `SOURCE_EVIDENCE_MAP_DRAFT`
- `ETHICAL_RISK_MATRIX_DRAFT`
- `DECISION_LOG_ENTRY`
- `PROFILE_DECISION_OPTIONS`
- `QUESTION_TRACE`
- `PMO_REVIEW_REQUEST`

## Artefatos bloqueados ate aprovacao

- posicionamento final
- tom de voz final
- pilares definitivos
- calendario editorial
- promessa comercial
- bio final
- roteiro de vendas
- HTML final

## Regra de maturidade

Um artefato parcial deve indicar:

```yaml
status: draft
based_on:
  - source
  - answer
  - hypothesis
needs_validation: true
approval_gate: founder_or_pmo
```
