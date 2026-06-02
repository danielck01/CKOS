---
title: PMO Audit Simulation Skill
system_id: pmo_audit_simulation_skill
category: creator_mode_skill
status: active
version: 1.0.0
owner: pmo_ckos
created_for: CKOS_CREATOR_MODE_PACK
---

# PMO Audit Simulation Skill

## Funcao

Auditar plano do CEO Agent antes de execucao documental.

## Verificacoes

- Escopo.
- Custo.
- Risco.
- Filetree.
- Duplicidade.
- Ordem documental.
- Conflito com docs canonicos.
- Uso indevido de ferramentas externas.
- Necessidade de aprovacao Founder.

## Output obrigatorio

Usar `02_TEMPLATES/PMO_AUDIT_HANDOFF_TEMPLATE.md`.

## Bloqueios automaticos

- Criar estrategia final sem briefing.
- Criar pack antes de filetree.
- Criar UI/backend/migrations/agentes reais.
- Recriar docs 21-24.
- Criar docs 25-30.
- Renumerar arquivos.
- Ignorar custo.
- Ignorar risco juridico/reputacional.

## Veredito

```txt
approved
approved_with_required_patches
blocked
```
