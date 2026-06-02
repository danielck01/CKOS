---
title: Context Pack Builder Simulation Skill
system_id: context_pack_builder_simulation_skill
category: creator_mode_skill
status: active
version: 1.0.0
owner: ceo_agent
created_for: CKOS_CREATOR_MODE_PACK
---

# Context Pack Builder Simulation Skill

## Funcao

Simular o Context Pack Builder do CKOS dentro do Codex, organizando memoria, fontes, filetree, riscos e lacunas antes da execucao.

## Inputs

- Intencao.
- Arquivos do vault.
- Uploads do projeto.
- Links/fonte externa autorizada.
- Regras de policy.

## Seções do context pack

```yaml
context_pack_id:
project_id:
intent:
source_mode:
files_read:
sources_attached:
external_sources_needed:
policies_applied:
risk_level:
credit_estimate:
gaps:
allowed_outputs:
blocked_outputs:
```

## Modos

- `attached_sources`
- `external_research_approved`
- `briefing_only_no_sources`

## Regras

- Sem fonte, output e hipotese.
- Com fonte, output pode ser analise.
- Com fonte + PMO + Founder approval, output pode virar plano de execucao.
- Pack de notas so depois de filetree aprovada.
