---
title: Documentation Standards — CKOS v1
file: README.md
layer: canonical
doc_type: readme
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
authority: canonical
tags: [ckos, canonical, governance, documentation, standards]
---

# Documentation Standards

## Operational Status

**Active — canonical.** Esta pasta é a fonte de verdade para o padrão documental CKOS v1.

## Authority

Esta pasta é **canônica**. Os arquivos aqui definem o padrão documental oficial do CKOS.

Regras de autoridade:

- Nenhum arquivo fora desta pasta pode sobrescrever ou contradizer estes padrões sem um patch report aprovado.
- Padrões aqui valem para todos os novos documentos criados no vault.
- Documentos legados existentes **não são alterados automaticamente** por estes padrões.
- Qualquer sweep futuro depende de patch report e aprovação explícita.

## Purpose

Esta pasta define o padrão documental mínimo e seguro do CKOS v1. Não executa migration. Não substitui arquivos legados ainda. Serve como fonte de verdade para novos documentos e como referência para futuras migrações controladas.

## What This Folder Contains

| Arquivo | Propósito |
|---|---|
| `README.md` | Este arquivo — declara autoridade e ordem de leitura |
| `canonical_documentation_standard_v1.md` | Padrão geral de documentos CKOS e matriz de camadas |
| `yaml_frontmatter_standard_v1.md` | YAML obrigatório e opcional por tipo de documento |
| `readme_standard_v1.md` | Padrão de README para pastas |
| `ck_memory_standard_v1.md` | Padrão de `ck_memory.md` |
| `ck_tasks_standard_v1.md` | Padrão de `ck_tasks.md` com Kanban |
| `study_vs_canonical_policy_v1.md` | Política entre documentos STUDY e CANONICAL |
| `naming_enums_tags_standard_v1.md` | Normalização de nomes, enums e tags |
| `migration_strategy_v1.md` | Estratégia de migração em quatro fases |
| `PATCH_REPORT_documentation_standard_v1.md` | Registro desta promoção canônica |

## What This Folder Must Not Contain

- Documentos de estudo ou drafts não aprovados.
- Especificações de backend ou schema sem aprovação técnica.
- Qualquer arquivo que não tenha passado pelo processo de promoção canônica.
- Resultados de sweep automático.

## Reading Order

1. `canonical_documentation_standard_v1.md` — entenda as camadas e autoridade
2. `yaml_frontmatter_standard_v1.md` — aprenda o YAML obrigatório
3. `study_vs_canonical_policy_v1.md` — entenda quando STUDY pode virar CANONICAL
4. `migration_strategy_v1.md` — entenda como migrar com segurança

Depois, conforme necessidade:

- `readme_standard_v1.md`
- `ck_memory_standard_v1.md`
- `ck_tasks_standard_v1.md`
- `naming_enums_tags_standard_v1.md`

## Required Files

- `README.md` (este arquivo)
- `canonical_documentation_standard_v1.md`
- `yaml_frontmatter_standard_v1.md`
- `PATCH_REPORT_documentation_standard_v1.md`

## Backend Relationship

`not_applicable` — esta pasta contém apenas padrões documentais. Nenhum backend é implementado aqui.

## ROI Relationship

Indireto. Padrões documentais reduzem retrabalho, melhoram qualidade de retrieval RAG e reduzem erros de interpretação por agentes.

## Memory Relationship

Esta pasta não usa `ck_memory.md` por enquanto. O estado desta pasta é registrado no `PATCH_REPORT_documentation_standard_v1.md`.

## Active Blockers

Nenhum bloqueio ativo. Migration, sweep e aplicação a documentos legados requerem aprovação futura antes de execução.

## Next Step

1. PMO_CKOS revisa e aprova o conteúdo v1.
2. Founder aprova a promoção canônica formal.
3. Qualquer extensão futura deste padrão requer novo patch report.
4. Migration somente após Phase 1 (Inventory) e aprovação explícita.
