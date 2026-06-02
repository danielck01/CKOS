# Metacognik - Claim Validation

Status: active_policy

## Funcao

Validar afirmacoes antes que virem texto publico, recomendacao estrategica ou artifact final.

## Tipos de claim

- claim juridico;
- claim de algoritmo;
- claim de reputacao;
- claim de benchmark;
- claim comercial;
- claim de autoridade profissional.

## Processo

```yaml
claim:
source:
source_type:
confidence:
risk:
needs_human_review:
allowed_use:
  - internal_analysis
  - draft
  - public_after_review
blocked_use:
```

## Regra

Nao afirmar conformidade juridica. Registrar apenas que a recomendacao parece alinhada a fontes e requer revisao humana.
