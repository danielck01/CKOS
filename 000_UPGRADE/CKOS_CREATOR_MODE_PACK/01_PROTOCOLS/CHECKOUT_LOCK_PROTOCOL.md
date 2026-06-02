---
title: Checkout Lock Protocol
system_id: checkout_lock_protocol
category: creator_mode_protocol
status: active
version: 1.0.0
owner: pmo_ckos
reviewers:
  - founder
  - ceo_agent
created_for: CKOS_CREATOR_MODE_PACK
---

# Checkout Lock Protocol

## Proposito

Evitar caos de multiplos chats editando o mesmo vault, projeto ou pack.

## Quando usar

Usar antes de qualquer agente mexer em uma pasta, criar pack, editar filetree, gerar documentos de projeto ou atualizar memoria.

## CHECKOUT LOCK

```md
# CHECKOUT LOCK

task_id:
agent:
role:
folder_scope:
files_allowed:
files_forbidden:
started_at:
expected_output:
approval_required:
risk_level:
status: locked
```

## CHECKOUT RELEASE

```md
# CHECKOUT RELEASE

task_id:
agent:
files_changed:
summary:
risks:
next_step:
status: released
```

## Regras

- Um lock deve ter escopo de pasta claro.
- `files_forbidden` deve incluir docs canonicos quando o trabalho for auxiliar.
- Nenhum lock autoriza renomear, deletar ou mover arquivos.
- Ao finalizar, release deve listar arquivos alterados.
- Se o trabalho parar no meio, status vira `blocked`, nao `released`.

## Exemplo

```md
# CHECKOUT LOCK

task_id: CKOS-CREATOR-MODE-001
agent: CEO_AGENT_CKOS
role: creator_mode_pack_builder
folder_scope: 000_UPGRADE/CKOS_CREATOR_MODE_PACK/
files_allowed:
  - 000_UPGRADE/CKOS_CREATOR_MODE_PACK/**
  - 000_UPGRADE/CKOS_UPGRADE_INDEX.md
  - 000_UPGRADE/CKOS_CONTINUATION_PLAN.md
files_forbidden:
  - 00_SYSTEM_GOVERNANCE/**
  - 01_THINKING_SYSTEM/**
  - 02_EXECUTION_SYSTEM/**
  - 03_RUNTIME_SYSTEM/**
  - 04_PRODUCT_SYSTEM/**
  - 05_IMPLEMENTATION_SYSTEM/**
  - 06_BUSINESS_SYSTEMS/**
started_at: 2026-05-26
expected_output: Creator Mode Pack auxiliar
approval_required: founder
risk_level: medium
status: locked
```
