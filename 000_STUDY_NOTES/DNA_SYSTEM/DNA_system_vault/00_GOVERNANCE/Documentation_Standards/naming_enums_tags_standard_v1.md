---
title: Naming, Enums and Tags Standard v1
file: naming_enums_tags_standard_v1.md
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
  - founder
  - pmo_ckos
purpose: Definir normalização de nomes, enums e tags para novos documentos CKOS. Não aplica normalização retroativa.
inputs:
  - estudo em 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/12_naming_and_enums_standard.md
  - estudo em 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/13_tags_taxonomy_proposal.md
outputs:
  - padrão de nomes, enums e tags para novos documentos
related_notes:
  - yaml_frontmatter_standard_v1.md
  - canonical_documentation_standard_v1.md
tags: [ckos, canonical, taxonomy, enums, governance, documentation]
---

# Naming, Enums and Tags Standard v1

## 1. Purpose

Definir a normalização de nomes de agentes, owners, enums de YAML e tags para novos documentos CKOS. Este padrão documenta a convenção — não aplica normalização retroativa em arquivos existentes.

## 2. Regra Central

> YAML usa system IDs em lowercase snake_case.
> Prosa pode usar display names.
> Não renomear arquivos existentes.
> Não normalizar YAML de documentos canônicos sem patch report aprovado.

## 3. Mapeamento de Nomes

| Display Name | System ID (YAML) |
|---|---|
| PMO_CKOS | `pmo_ckos` |
| Cognik | `cognik` |
| Metacognik | `metacognik` |
| Builder Lead | `builder_lead` |
| QA Lead | `qa_lead` |
| Founder | `founder` |
| Technical | `technical` |
| Client | `client` |
| Legal | `legal` |
| Codex | `codex` |
| Claude | `claude` |
| Antigravity | `antigravity` |
| Nick | `nick` |
| Datta | `datta` |
| CEO Agent | `ceo_agent` |

## 4. Enum: owner

```txt
founder
pmo_ckos
technical
qa_lead
builder_lead
metacognik
client
legal
```

## 5. Enum: responsible_agent

```txt
nick
cognik
metacognik
pmo_ckos
qa_lead
builder_lead
datta
codex
claude
antigravity
ceo_agent
```

## 6. Enum: approval_required

Sempre como lista YAML, mesmo com um único item:

```yaml
approval_required:
  - founder
```

Valores permitidos:

```txt
none
founder
pmo_ckos
technical
qa_lead
metacognik
client
legal
```

## 7. Enum: doc_type

```txt
raw_source
study_note
canonical_doc
roadmap
patch_report
handoff
release_note
task_board
folder_memory
feedback_log
checkout_lock
readme
study_index
standard_proposal
audit_note
migration_strategy
risk_register
promotion_proposal
```

## 8. Enum: layer

```txt
raw
study
canonical
roadmap
patch_report
handoff
release
task
memory
feedback
lock
```

## 9. Enum: confidence

```txt
unverified
low
medium
high
verified
```

## 10. Enum: risk_level

```txt
low
medium
high
critical
```

## 11. Regras de Tags

- Sempre minúsculas.
- Sempre snake_case.
- Sem acentos.
- Sem frases longas.
- Máximo 8 tags por arquivo.
- Preferir vocabulário controlado.
- Adicionar nova tag apenas quando nenhuma existente serve.

## 12. Tags Controladas — Core

```txt
ckos
runtime
backend
frontend
branddock
dna
research
study
canonical
roadmap
policy
schema
api
agent
workflow
roi
memory
feedback
qa
approval
cost_guard
supabase
openrouter
mcp
observability
documentation
governance
```

## 13. Tags Controladas — Estendidas

```txt
yaml
template
taxonomy
security
permissions
data_model
event_bus
workflow_engine
agent_runtime
background_jobs
rag
pgvector
model_routing
tools_registry
handoff
release
patch_report
task
lock
readme
folder_memory
audit
risk
migration
```

## 14. Padrão de Seleção de Tags

Ordem recomendada:

```txt
1. projeto/domínio  (ex: ckos)
2. camada           (ex: study, canonical)
3. área do sistema  (ex: runtime, backend)
4. tópico específico (ex: workflow, schema)
5. tópico de controle (ex: approval, cost_guard)
```

Exemplo:

```yaml
tags: [ckos, study, runtime, workflow, approval, cost_guard]
```

## 15. Anti-Padrões de Tags

- Frases longas: `AI First Project Operating System Deep Research`.
- Tags com barra: `runtime/backend/Supabase`.
- Display names: `Metacognik Review Needed`.
- Com acento: `aprovacao`.
- Mais de 8 tags por arquivo.

## 16. O Que Não Fazer

- Não renomear arquivos existentes.
- Não normalizar display names em prosa automaticamente.
- Não reescrever YAML canônico sem aprovação.
- Não deletar tags desconhecidas antes de inventário.
- Não usar strings com espaços como valor de `owner` ou `responsible_agent`.
