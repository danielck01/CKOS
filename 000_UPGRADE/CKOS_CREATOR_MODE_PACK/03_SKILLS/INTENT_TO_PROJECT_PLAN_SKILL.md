---
title: Intent To Project Plan Skill
system_id: intent_to_project_plan_skill
category: creator_mode_skill
status: active
version: 1.0.0
owner: ceo_agent
created_for: CKOS_CREATOR_MODE_PACK
---

# Intent To Project Plan Skill

## Funcao

Converter uma intencao curta em plano inicial auditavel, sem executar a tarefa final.

## Inputs

- Intencao do Founder.
- Memoria do vault.
- Categoria/subcategoria.
- Fontes anexadas ou ausentes.
- Risco estimado.

## Processo

1. Extrair objetivo.
2. Classificar tipo de projeto.
3. Classificar risco.
4. Identificar dependencias.
5. Identificar fontes necessarias.
6. Estimar creditos.
7. Definir outputs possiveis.
8. Pedir PMO audit quando necessario.
9. Perguntar ao Founder antes de criar arquivos.

## Output

`PROJECT_INTENT_ANALYSIS.md` ou resposta inicial `CEO_AGENT_INTERPRETATION`.

## Reprovado se

- gerar estrategia final;
- pular risco;
- ignorar custo;
- criar pack antes de filetree;
- tratar hipotese como decisao.
