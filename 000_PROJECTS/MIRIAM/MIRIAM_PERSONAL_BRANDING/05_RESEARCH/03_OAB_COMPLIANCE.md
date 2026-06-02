# OAB Compliance

Status: draft_risk_layer

## Funcao

Registrar limites juridicos e eticos a validar antes de qualquer saida publica.

## Pontos de atencao

- publicidade juridica deve ser informativa e discreta;
- evitar mercantilizacao;
- evitar promessa de resultado;
- evitar captacao indevida;
- evitar comparacao, autopromocao agressiva ou sensacionalismo;
- revisar qualquer conteudo que trate de crime, vitima, acusado, flagrante ou prisao.

## Politica do projeto

```yaml
legal_compliance_claim: forbidden_without_human_review
legal_review_required: true
allowed_now:
  - internal_risk_mapping
  - language_boundaries
  - questions_for_review
blocked_now:
  - final_public_copy
  - sales_promises
  - definitive_compliance_statement
```

## Nota

Este documento nao substitui advogado especialista em etica/OAB.
