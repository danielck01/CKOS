# 03_TECH_REFERENCES

## Funcao da pasta

Guardar referencias tecnicas brutas para runtime, protocolos, conectores, seguranca, dados e infraestrutura.

## O que pode entrar

Documentacao tecnica, specs de API, referencias MCP, security docs, exemplos de arquitetura e notas de fornecedor.

## O que nao pode entrar

Codigo de producao, migrations, chaves, tokens ou implementacao direta.

## Naming obrigatorio

`YYYYMMDD_source-tool_topic_owner_status.ext`

## Regra de saida

Gerar estudo tecnico antes de qualquer patch em docs runtime ou futuros docs 25-29.

## Quando mover para STUDY

Quando impactar MCP, collectors, security, cost guard, audit, data model ou policies.

## Quando arquivar

Quando a referencia estiver obsoleta, insegura ou fora do escopo CKOS.

## Risco principal

Introduzir dependencia tecnica antes da governanca.

## Politica de PII

Evitar logs reais, tokens, payloads pessoais ou dados de tenant.

## Politica de provenance

Registrar fornecedor, versao, URL/origem e data de consulta.

