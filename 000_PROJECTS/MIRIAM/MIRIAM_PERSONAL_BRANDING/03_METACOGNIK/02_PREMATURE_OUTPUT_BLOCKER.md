# Metacognik - Premature Output Blocker

Status: active_policy

## Funcao

Bloquear saidas que parecem produtivas, mas nascem antes do contexto minimo.

## Saidas bloqueadas agora

- posicionamento final;
- tom de voz final;
- pilares editoriais finais;
- calendario de conteudo;
- bio final;
- plano de lancamento;
- HTML final;
- roteiro de venda;
- promessa de autoridade juridica sem evidencia.

## Condicao de desbloqueio

```yaml
requires:
  - briefing_vivo_answers
  - source_evidence_map
  - ethical_risk_matrix
  - pmo_review
  - founder_approval
  - legal_human_review_when_public_claim
```

## Mensagem padrao

Saida bloqueada: o projeto ainda nao possui contexto, evidencia e aprovacao suficientes para gerar este artefato sem aumentar risco.
