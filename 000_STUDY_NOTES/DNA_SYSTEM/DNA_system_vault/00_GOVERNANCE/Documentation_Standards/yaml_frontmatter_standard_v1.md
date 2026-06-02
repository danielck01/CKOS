---
title: YAML Frontmatter Standard v1
file: yaml_frontmatter_standard_v1.md
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
purpose: Definir o YAML frontmatter obrigatório e opcional por tipo de documento CKOS.
inputs:
  - estudo em 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/02_yaml_standard_proposal.md
outputs:
  - template YAML por camada documental
related_notes:
  - canonical_documentation_standard_v1.md
  - naming_enums_tags_standard_v1.md
tags: [ckos, canonical, yaml, governance, documentation]
---

# YAML Frontmatter Standard v1

## 1. Purpose

Definir o frontmatter YAML obrigatório e opcional para cada camada documental CKOS. Este padrão vale para novos documentos. Não aplica normalização retroativa automaticamente.

## 2. YAML Base Obrigatório — Documentos Canônicos

```yaml
---
title:
file:
doc_type:
layer: canonical
phase:
category:
version:
status:
owner:
responsible_agent:
reviewers:
approval_required:
purpose:
inputs:
outputs:
related_notes:
tags:
created_at:
updated_at:
---
```

## 3. Campos Opcionais Canônicos

```yaml
framework:
edge_cases:
integrations:
prompts:
metrics:
risks:
dependencies:
backend_refs:
api_refs:
schema_refs:
roi_refs:
memory_refs:
```

## 4. YAML Obrigatório — Documentos RAW/STUDY

```yaml
---
title:
file:
doc_type:
layer:
source_type:
source_path:
source_tool:
provenance_status:
confidence:
risk_level:
canonical_candidate:
owner:
responsible_agent:
related_notes:
tags:
created_at:
updated_at:
---
```

## 5. YAML para Roadmap

```yaml
---
title:
file:
doc_type: roadmap
status:
owner:
phase:
scope:
dependencies: []
risks: []
roi_relevance:
related_notes: []
tags: []
---
```

## 6. YAML para Patch Report

```yaml
---
title:
file:
doc_type: patch_report
trigger:
objective:
files_created: []
files_changed: []
files_not_touched: []
patches_applied: []
patches_deferred: []
validation:
risks_remaining: []
gate:
confidence:
provenance_status:
tags: []
---
```

## 7. Enums Controlados

### doc_type

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

### layer

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

### status

Documentos canônicos usam apenas:

```txt
draft
active
deprecated
archived
```

Documentos RAW/STUDY podem usar adicionalmente:

```txt
raw
received
unverified
study
```

Documentos de tarefa/execução usam:

```txt
backlog
ready
in_progress
review
done
blocked
```

### phase

```txt
ROOT
000_ROADMAPS
000_STUDY_NOTES
000_UPLOADS
00_SYSTEM_GOVERNANCE
01_THINKING_SYSTEM
02_EXECUTION_SYSTEM
03_RUNTIME_SYSTEM
04_PRODUCT_SYSTEM
05_IMPLEMENTATION_SYSTEM
06_BUSINESS_SYSTEMS
07_EVOLUTION_SYSTEM
99_RESEARCH_LAB
```

### category

```txt
governance
template
taxonomy
architecture
runtime
runtime_data
runtime_observability
security
workflow
memory
approval
cost_control
roi
feedback
roadmap
study
patch_report
handoff
release
task
lock
folder_memory
readme
```

### owner

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

### responsible_agent

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

### approval_required

Sempre como lista, mesmo com um único item:

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

### confidence

```txt
unverified
low
medium
high
verified
```

### risk_level

```txt
low
medium
high
critical
```

### provenance_status

```txt
unverified
source_identified
source_reviewed
verified
redacted
```

## 8. Regras de Validação YAML

- YAML deve parsear sem erros.
- Listas devem ser listas YAML, não strings separadas por vírgula.
- Datas usam formato `YYYY-MM-DD`.
- Nomes em YAML usam system IDs (snake_case).
- Tags usam lowercase snake_case.
- Máximo 8 tags por arquivo.
- `confidence` e `provenance_status` são obrigatórios para RAW/STUDY.
- `layer` é obrigatório para todo documento.
- `approval_required` deve ser lista mesmo com um item.

## 9. O Que Não Fazer

- Não adicionar YAML retroativamente em documentos canônicos sem revisão.
- Não inferir campos que requerem julgamento humano.
- Não usar `confidence: high` sem evidência verificada.
- Não omitir `layer` e `doc_type` em novos documentos.
