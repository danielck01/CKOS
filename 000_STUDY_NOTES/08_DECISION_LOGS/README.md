# 08_DECISION_LOGS

## Funcao da pasta

Registrar decisoes PMO/Founder sobre estudo, promocao, rejeicao ou arquivamento.

## O que pode entrar

Decision logs com contexto, opcoes, decisao, responsavel, risco e proxima acao.

## O que nao pode entrar

Decisao informal sem owner, patch aplicado ou ata com PII desnecessaria.

## Naming obrigatorio

`YYYYMMDD_source-tool_topic_owner_status.md`

## Regra de saida

Decision log permanece como trilha; pode apontar para patch candidate ou archive.

## Quando mover para CANONICAL

Nunca direto. Pode ser citado em patch plan.

## Quando arquivar

Quando decisao for substituida e houver novo log referenciado.

## Risco principal

Perder rastreabilidade de aprovacao.

## Politica de PII

Registrar decisao sem expor dados desnecessarios.

## Politica de provenance

Referenciar notas, fontes e aprovadores.

