---
title: Migration Strategy v1
file: migration_strategy_v1.md
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
purpose: Definir a estratégia segura de migração documental em quatro fases para o vault CKOS.
inputs:
  - estudo em 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/14_migration_strategy.md
  - estudo em 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/15_risk_register.md
outputs:
  - estratégia de migração por fases com gates de aprovação
related_notes:
  - canonical_documentation_standard_v1.md
  - study_vs_canonical_policy_v1.md
  - yaml_frontmatter_standard_v1.md
tags: [ckos, canonical, migration, governance, documentation, risk]
---

# Migration Strategy v1

## 1. Purpose

Definir a estratégia segura para normalizar documentação do vault CKOS em quatro fases. Cada fase tem escopo limitado, regras explícitas e gate de aprovação antes de avançar.

## 2. Princípio Fundamental

> Automação pode assistir inventário e validação.
> Automação não deve decidir autoridade, aprovação, confiança, promoção canônica ou significado semântico.

## 3. Phase 1 — Inventory

**Objetivo:** Ler, classificar e gerar relatório. Nenhum arquivo é alterado.

**Regras:**

- Não alterar nenhum arquivo.
- Detectar presença de frontmatter YAML.
- Classificar `layer` e `doc_type` de cada arquivo.
- Detectar arquivos sem `tags`.
- Detectar `_folder_memory.md` legado.
- Detectar possíveis candidatos canônicos.
- Identificar arquivos com ambiguidade de risco.

**Outputs esperados:**

- Relatório de inventário (Markdown ou CSV).
- Relatório de classificação por camada.
- Lista de riscos identificados.

**Gate de aprovação:** PMO_CKOS revisa inventário antes de Phase 2.

## 4. Phase 2 — Safe Patch

**Objetivo:** Adicionar frontmatter mínimo apenas em arquivos sem YAML, sem alterar corpo.

**Regras:**

- Apenas pastas de baixo risco.
- Nenhum documento canônico sem revisão.
- Nenhuma reescrita de conteúdo.
- Preservar título e corpo originais.
- Adicionar `provenance_status: unverified` quando fonte não revisada.
- `confidence` deve ser `unverified` por padrão se não verificada.

**Outputs esperados:**

- Patch report.
- Relatório de validação YAML.
- Lista de arquivos alterados.

**Gate de aprovação:** PMO_CKOS aprova lista de arquivos antes de aplicar. Founder se qualquer pasta de risco médio ou alto.

## 5. Phase 3 — Standard Alignment

**Objetivo:** Normalizar campos divergentes em documentos de baixo risco.

**Regras:**

- Normalizar tags apenas a partir de mapeamento aprovado.
- Normalizar `owner`/`responsible_agent` apenas quando mapeamento é certo.
- Evitar mudanças semânticas.
- Registrar casos incertos como deferred.
- Não tocar documentos canônicos de risco alto.

**Outputs esperados:**

- Relatório before/after.
- Lista deferred com justificativa.
- Atualização do risk register.

**Gate de aprovação:** PMO_CKOS e Metacognik revisam antes de Phase 4.

## 6. Phase 4 — Canonical Review

**Objetivo:** Documentos canônicos passam por revisão humana antes de qualquer patch.

**Regras:**

- Aprovação de Founder/PMO/técnico conforme `approval_required`.
- Revisar diffs manualmente.
- Validar YAML.
- Verificar links.
- Verificar SemVer.
- Atualizar patch report.

**Outputs esperados:**

- Patch canônico aprovado.
- Patch report atualizado.
- Release note.

**Gate de aprovação:** Todos os aprovadores em `approval_required` do documento alvo.

## 7. O Que Não Automatizar Nunca

As seguintes ações **nunca** devem ser executadas por automação sem aprovação humana explícita:

- Promoção canônica de qualquer documento STUDY.
- Replacement de `_folder_memory.md` por `ck_memory.md`.
- Normalização de `approval_required` onde a base de aprovação é incerta.
- Normalização de `owner` onde o source é ambíguo.
- Renames de arquivos.
- Deletes de arquivos.
- Tag deletion.
- Sweep em documentos canônicos.
- Migrations sem inventário completo aprovado.
- Inferência de aprovação a partir de status ou tags.

## 8. Registro de Riscos de Migration

| risk_id | Risco | Nível | Mitigação |
|---|---|---|---|
| RISK_001 | Quebra de links | high | Sem rename/delete em Phase 1 e 2 |
| RISK_002 | Perda de contexto legado | high | Inventariar antes de qualquer ação |
| RISK_003 | STUDY promovido como CANONICAL por erro | critical | Exigir `layer` e `canonical_candidate` |
| RISK_004 | YAML inválido gerado | medium | Validação antes e depois |
| RISK_005 | Owner normalizado incorretamente | high | Usar mapeamento aprovado apenas |
| RISK_006 | Campo `approval_required` enfraquecido | critical | Revisão manual para canônicos |
| RISK_007 | Tags perdem sinal de retrieval RAG | medium | Preservar tags desconhecidas em relatório |
| RISK_008 | Roadmap tratado como canônico | high | Exigir campo `layer` em todos os docs |
| RISK_009 | Backend implicado por documentação | high | Relação backend deve ser explícita |
| RISK_010 | Automação altera corpo de texto | high | Phase 2 adiciona apenas YAML mínimo |
| RISK_011 | Conteúdo sensível exposto | medium | Revisar `source_path` antes de copiar |
| RISK_012 | Confiança inflada | high | Default `unverified` para docs incertos |

## 9. Status Atual

**Phase 1 (Inventory) não foi executada ainda.** Nenhuma migration foi aplicada. Esta estratégia é o baseline canônico para orientar futuras execuções.
