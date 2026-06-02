# codex

## Funcao da pasta

Guardar outputs brutos do Codex quando forem pesquisa, auditoria ou proposta documental.

## O que pode entrar

Relatorios, diffs planejados, auditorias e propostas geradas por Codex.

## O que nao pode entrar

Codigo de producao, migrations, backend, UI, secrets ou alteracao canonica sem patch plan.

## Naming obrigatorio

`YYYYMMDD_codex_topic_owner_status.ext`

## Regra de saida

Gerar study note ou patch candidate somente apos revisao PMO.

## Quando mover para STUDY

Quando o output Codex precisar virar evidencia, decisao ou patch candidate.

## Quando arquivar

Quando for log temporario, duplicado ou superado.

## Risco principal

Confundir capacidade de execucao com autorizacao de implementacao.

## Politica de PII

Nao persistir dados sensiveis de repos, clientes ou prompts sem controle.

## Politica de provenance

Registrar tarefa, data, contexto e arquivos lidos quando relevante.

