---
title: Study vs Canonical Policy v1
file: study_vs_canonical_policy_v1.md
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
purpose: Definir a política que separa documentos STUDY de documentos CANONICAL e as condições de promoção.
inputs:
  - estudo em 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/16_promotion_to_canonical_proposal.md
  - estudo em 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/01_current_patterns_audit.md
outputs:
  - política de promoção canônica
related_notes:
  - canonical_documentation_standard_v1.md
  - migration_strategy_v1.md
tags: [ckos, canonical, policy, governance, study, promotion]
---

# Study vs Canonical Policy v1

## 1. Purpose

Definir com precisão o que STUDY pode e não pode fazer, e as condições exatas para que um documento de estudo seja promovido a canônico.

## 2. Regra Central

> O Research Lab não é canônico.
> Nada dentro de `99_RESEARCH_LAB/` vira regra automaticamente.
> STUDY pode recomendar — nunca governar.

## 3. O Que STUDY Pode Fazer

- Comparar opções e abordagens.
- Propor recomendações com justificativa.
- Registrar riscos e incertezas.
- Sugerir candidatos canônicos com análise de evidência.
- Documentar padrões observados no vault.
- Registrar perguntas abertas.

## 4. O Que STUDY Não Pode Fazer

- Virar regra automaticamente.
- Gerar migration final.
- Autorizar implementação de backend ou runtime.
- Sobrescrever spec canônica.
- Alterar runtime direta ou indiretamente.
- Ser usado por Codex como fonte de implementação.
- Inferir aprovação a partir de status, tags ou nome de pasta.

## 5. Condição de Promoção Canônica

Para que um documento STUDY seja promovido a CANONICAL, todas as etapas abaixo devem ser concluídas na ordem:

| Etapa | Responsável | O que valida |
|---|---|---|
| 1. PMO review | PMO_CKOS | Escopo, risco, maturidade, clareza |
| 2. Metacognik audit | Metacognik | Autoridade, separação de camadas, riscos críticos |
| 3. Patch report criado | PMO_CKOS | Registra o que será criado ou alterado |
| 4. Aprovação explícita | Conforme `approval_required` do doc alvo | Founder se governança, técnico se backend |
| 5. Criação ou atualização em pasta canônica | Agente autorizado | Apenas após aprovação |
| 6. Registro em `ck_memory.md` | Folder owner | Contexto local atualizado |

Nenhuma etapa pode ser pulada.

## 6. Critérios de Rejeição de Promoção

Um documento STUDY não pode ser promovido se:

- `confidence` for `low` ou `unverified` sem justificativa documentada.
- `risk_level` for `critical` sem mitigação aprovada.
- O documento contiver claims sem evidência identificável.
- A aprovação necessária não foi obtida.
- O patch report não existe ou está incompleto.
- O conteúdo contradiz spec canônica existente sem resolução.

## 7. Distinção por Camada

| Camada | Pode recomendar? | Pode governar? | Pode implementar? |
|---|---|---|---|
| RAW | Não | Não | Não |
| STUDY | Sim | Não | Não |
| CANONICAL | Sim | Sim | Sim (com aprovação) |
| ROADMAP | Informa sequência | Não | Não |
| MEMORY | Registra contexto | Não | Não |
| PATCH_REPORT | Registra mudança | Não | Não |

## 8. Casos Que Nunca Automatizar

- Promoção canônica de qualquer documento STUDY.
- Inferência de aprovação a partir de tags ou folder name.
- Replacement de `_folder_memory.md`.
- Normalização de campos `approval_required` em docs canônicos.
- Renames, deletes ou sweeps em documentos de qualquer camada.
- Migration de STUDY para CANONICAL sem patch report.
- Edição de documentos canônicos sem aprovação formal.

## 9. Fluxo de Promoção — Diagrama

```txt
STUDY document
  ↓ PMO_CKOS review (scope, risk, maturity)
  ↓ Metacognik audit (authority, layer separation)
  ↓ Patch report created (what changes, what doesn't)
  ↓ Approval obtained (per approval_required list)
  ↓ Created/updated in canonical folder
  ↓ ck_memory.md updated
CANONICAL document (approved baseline)
```
