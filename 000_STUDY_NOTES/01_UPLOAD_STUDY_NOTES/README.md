# 01_UPLOAD_STUDY_NOTES

## Funcao da pasta

Guardar notas de estudo geradas a partir de uploads brutos.

## O que pode entrar

Notas que resumem fonte, evidencia, risco, confidence, lacunas e destino possivel.

## O que nao pode entrar

Arquivo RAW original, doc canonico, patch aplicado ou decisao sem evidencia.

## Naming obrigatorio

`YYYYMMDD_source-tool_topic_owner_status.md`

## Regra de saida

Mover para synthesis, patch candidate, decision log ou archive.

## Quando mover para CANONICAL

Nunca diretamente. A nota pode informar patch plan.

## Quando arquivar

Quando for superada, rejeitada ou sem confidence suficiente.

## Risco principal

Resumo virar verdade canonica sem QA.

## Politica de PII

Usar referencias sanitizadas e evitar copiar dados sensiveis.

## Politica de provenance

Obrigatorio linkar o upload bruto em `source_path`.

