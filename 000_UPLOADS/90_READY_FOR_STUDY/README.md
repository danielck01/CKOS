# 90_READY_FOR_STUDY

## Funcao da pasta

Fila de material RAW triado e pronto para virar source manifest ou study note.

## O que pode entrar

Arquivos com origem minima, owner, risco e destino de estudo definidos.

## O que nao pode entrar

Material sem triagem, secrets, PII nao classificada ou arquivos ja estudados.

## Naming obrigatorio

`YYYYMMDD_source-tool_topic_owner_status.ext`

## Regra de saida

Criar nota em `../000_STUDY_NOTES/` e manter referencia ao arquivo bruto.

## Quando mover para STUDY

Assim que PMO confirmar que ha contexto suficiente para interpretacao.

## Quando arquivar

Quando a triagem posterior reprovar o material.

## Risco principal

Virar segunda inbox sem SLA.

## Politica de PII

PII deve estar classificada antes de entrar aqui.

## Politica de provenance

Provenance minima obrigatoria: fonte, ferramenta, data e owner.

