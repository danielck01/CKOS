---
title: CK Tasks Standard v1
file: ck_tasks_standard_v1.md
layer: canonical
doc_type: canonical_doc
status: active
version: 1.0.0
created_at: 2026-05-31
updated_at: 2026-05-31
owner: pmo_ckos
responsible_agent: metacognik
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - pmo_ckos
purpose: Definir o padrão Kanban de ck_tasks.md para pastas com trabalho ativo no vault CKOS.
inputs:
  - estudo em 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/05_ck_tasks_standard.md
outputs:
  - template e regras de ck_tasks.md
related_notes:
  - canonical_documentation_standard_v1.md
  - ck_memory_standard_v1.md
tags: [ckos, canonical, tasks, kanban, governance, documentation]
---

# CK Tasks Standard v1

## 1. Purpose

Definir o padrão Kanban para `ck_tasks.md` em pastas com trabalho ativo. Estabelecer campos obrigatórios por task e regras de controle de escopo.

## 2. Regra Central

> Nenhum agente deve editar arquivo fora do `allowed_files` declarado na task.
> Tasks não autorizam edições canônicas sem aprovação explícita.
> `ck_tasks.md` é adequado para pastas com trabalho ativo, não para arquivos passivos.

## 3. Colunas Kanban Obrigatórias

```txt
Backlog
Ready
In Progress
Review
Done
Blocked
```

### Definição de Status

| Status | Significado |
|---|---|
| `Backlog` | Não pronto — escopo indefinido ou não aprovado |
| `Ready` | Escopo definido e aprovado para iniciar |
| `In Progress` | Um owner trabalhando ativamente |
| `Review` | Output existe e aguarda revisão |
| `Done` | Critérios de entrega cumpridos |
| `Blocked` | Não pode avançar sem decisão ou input externo |

## 4. Campos Obrigatórios por Task

```txt
task_id
title
scope
allowed_files
forbidden_files
owner
status
approval_required
cost_limit
checkout_lock_required
output_expected
done_criteria
```

## 5. Linha de Task Recomendada

```md
| task_id | title | scope | allowed_files | forbidden_files | owner | status | approval_required | cost_limit | checkout_lock_required | output_expected | done_criteria |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TASK_001 | Exemplo | Apenas estudo | `99_RESEARCH_LAB/...` | vault canônico | pmo_ckos | ready | pmo_ckos | 0 | required | study note | arquivos criados e verificados |
```

## 6. Regra de Checkout

Qualquer task que edite arquivos deve declarar se checkout lock é necessário. Se necessário, o lock deve listar escopo permitido e proibido explicitamente.

## 7. Regra de Custo

Tasks devem declarar `cost_limit` mesmo que seja `0` para trabalho de documentação sem custo de provider.

## 8. Regra de Escopo

- `allowed_files`: lista explícita de arquivos que a task pode editar.
- `forbidden_files`: lista explícita de arquivos que a task não pode tocar.
- Nenhum agente deve inferir permissão de edição que não está em `allowed_files`.

## 9. O Que Não Fazer

- Não converter toda checklist em `ck_tasks.md`.
- Não marcar task como `Done` sem critérios de entrega cumpridos.
- Não deixar tasks autorizarem edições canônicas sem aprovação explícita.
- Não usar `ck_tasks.md` como substituto de roadmap ou spec.
