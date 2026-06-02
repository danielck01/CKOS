---
title: README Standard v1
file: readme_standard_v1.md
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
purpose: Definir o padrão de README para pastas do vault CKOS.
inputs:
  - estudo em 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/03_readme_standard_proposal.md
outputs:
  - template de README de pasta
related_notes:
  - canonical_documentation_standard_v1.md
  - ck_memory_standard_v1.md
tags: [ckos, canonical, readme, governance, documentation]
---

# README Standard v1

## 1. Purpose

Definir o padrão de README para pastas do vault CKOS. O README orienta navegação para humanos e agentes. Não é spec técnica profunda.

## 2. Regra Central

> README de pasta deve orientar navegação.
> README não deve conter spec técnica profunda.
> README não substitui `architecture.md`, `schema.md` ou `api.md`.

## 3. Estrutura Obrigatória

Todo README de pasta deve conter as seguintes seções nesta ordem:

```md
# [Folder Name]

## Operational Status

## Authority

## Purpose

## What This Folder Contains

## What This Folder Must Not Contain

## Reading Order

## Required Files

## Backend Relationship

## ROI Relationship

## Memory Relationship

## Active Blockers

## Next Step
```

## 4. Guia de Seções

| Seção | Conteúdo esperado |
|---|---|
| `Operational Status` | `active`, `draft`, `study-only`, `canonical`, `archived` + uma linha de contexto |
| `Authority` | Se a pasta é `canonical`, `auxiliary`, `raw`, `study` ou `operational` |
| `Purpose` | Uma a três frases descrevendo o objetivo da pasta |
| `What This Folder Contains` | Tabela de arquivos e propósito de cada um |
| `What This Folder Must Not Contain` | Lista explícita de material proibido |
| `Reading Order` | Ordem mínima para evitar sobrecarga de contexto |
| `Required Files` | Arquivos que devem sempre existir nesta pasta |
| `Backend Relationship` | `not_applicable`, `study_only`, `blocked`, `allowed_after_approval` ou `active` |
| `ROI Relationship` | Se ROI é aplicável e onde é rastreado |
| `Memory Relationship` | Se a pasta usa `ck_memory.md` ou memória legada |
| `Active Blockers` | Locks ativos ou decisões bloqueadas |
| `Next Step` | Próxima ação recomendada para humano ou agente |

## 5. YAML Recomendado para README de Pasta

```yaml
---
title:
file: README.md
layer:
doc_type: readme
status:
version:
created_at:
updated_at:
owner:
responsible_agent:
reviewers: []
approval_required: []
authority:
tags: []
---
```

## 6. Regras

- README declara regras da pasta — não sobrescreve governança canônica silenciosamente.
- README deve ser curto o suficiente para agentes lerem antes de trabalhar.
- README deve referenciar `ck_memory.md` para estado local atual.
- README deve referenciar `ck_tasks.md` apenas quando a pasta tem trabalho ativo.
- `Backend Relationship` deve ser explícito — nunca omitido.

## 7. O Que Não Fazer

- Não adicionar YAML de README em lote sem revisão.
- Não reescrever corpos de README existentes automaticamente.
- Não usar README para promover material de estudo a canônico.
- Não colocar spec técnica profunda no README — use arquivos dedicados.
