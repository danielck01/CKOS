# 07_CANONICAL_PATCH_CANDIDATES

## Funcao da pasta

Guardar propostas estudadas que podem virar patch canonico.

## O que pode entrar

Patch candidates com evidencia, related docs, risco, confidence, decisao PMO e aprovadores esperados.

## O que nao pode entrar

Patch aplicado, diff final sem approval, doc canonico completo ou sugestao sem estudo.

## Naming obrigatorio

`YYYYMMDD_source-tool_topic_owner_status.md`

## Regra de saida

Mover para `09_APPROVED_FOR_CANONICAL_PATCH/` apenas apos revisao, ou arquivar.

## Quando mover para CANONICAL

Nunca como movimento de arquivo. Somente conteudo aprovado pode informar patch no doc oficial.

## Quando arquivar

Quando rejeitado, superado, sem evidence ou sem fit taxonomico.

## Risco principal

Aplicar patch antes de approval.

## Politica de PII

Patch candidates nao devem carregar PII bruta.

## Politica de provenance

Referenciar study notes e sources que sustentam a proposta.

