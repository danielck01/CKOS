---
title: Credits Estimation Skill
system_id: credits_estimation_skill
category: creator_mode_skill
status: active
version: 1.0.0
owner: pmo_ckos
created_for: CKOS_CREATOR_MODE_PACK
---

# Credits Estimation Skill

## Funcao

Estimar creditos CKOS simulados antes de qualquer execucao.

## Inputs

- Tipo de acao.
- Quantidade de arquivos.
- Uso de web/deep research.
- Risco.
- Necessidade de PMO/Metacognik.
- Tamanho do pack.

## Formula simples

```txt
custo_total =
  leitura_local
  + analise
  + filetree
  + pmo_audit
  + pesquisa_externa
  + risco_sensivel
```

## Saida

```txt
SIMULACAO DE CREDITOS CKOS

Local read:
Analysis:
Filetree:
PMO:
External research:
Sensitive domain premium:
Total range:
Approval:
```

## Regras

- Sempre apresentar alternativas mais baratas.
- Sempre separar local de externo.
- Dominio sensivel aumenta risco e exige approval.
