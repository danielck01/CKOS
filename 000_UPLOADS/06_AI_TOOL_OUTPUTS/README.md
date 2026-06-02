# 06_AI_TOOL_OUTPUTS

## Funcao da pasta

Guardar outputs brutos de ferramentas de IA separados por ferramenta.

## O que pode entrar

Respostas de ChatGPT, Claude, Codex, Manus, Antigravity e outras ferramentas, sempre como insumo nao verificado.

## O que nao pode entrar

Fonte canonica, decisao final, secrets, prompt com dados sensiveis sem controle ou output aplicado diretamente.

## Naming obrigatorio

`YYYYMMDD_source-tool_topic_owner_status.ext`

## Regra de saida

Output util deve gerar study note com `confidence: unverified` ate validacao por fonte externa ou decisao humana.

## Quando mover para STUDY

Quando houver insight claro, evidencia verificavel ou pergunta PMO relevante.

## Quando arquivar

Quando for rascunho, alucinacao, duplicado, sem fonte ou sem uso.

## Risco principal

Tratar output de IA como verdade.

## Politica de PII

Nao armazenar prompts/respostas com dados sensiveis sem classificacao e sanitizacao.

## Politica de provenance

Registrar ferramenta, modelo quando conhecido, data, prompt/contexto e owner.

