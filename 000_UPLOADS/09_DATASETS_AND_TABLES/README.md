# 09_DATASETS_AND_TABLES

## Funcao da pasta

Guardar datasets, CSVs, planilhas e tabelas brutas.

## O que pode entrar

CSV, XLSX, TSV, exports tabulares, listas e dados de benchmark.

## O que nao pode entrar

Secrets, dados pessoais sem classificacao, dump de banco, credenciais ou schema de producao.

## Naming obrigatorio

`YYYYMMDD_source-tool_topic_owner_status.ext`

## Regra de saida

Gerar manifest com origem, campos, risco e destino de estudo.

## Quando mover para STUDY

Quando a tabela for usada para analise, benchmark, ROI, billing, support ou ingestion.

## Quando arquivar

Quando for duplicada, corrompida, sem origem ou sem licenca/consentimento.

## Risco principal

Vazar dados sensiveis ou interpretar dado bruto sem contexto.

## Politica de PII

Classificar campos pessoais antes de qualquer processamento.

## Politica de provenance

Registrar origem, ferramenta, data, schema aproximado e owner.

