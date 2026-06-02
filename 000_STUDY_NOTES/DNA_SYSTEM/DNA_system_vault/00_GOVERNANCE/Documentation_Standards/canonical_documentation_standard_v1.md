---
title: Canonical Documentation Standard v1
file: canonical_documentation_standard_v1.md
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
purpose: Define as camadas documentais do CKOS, sua autoridade, permissões e regras de promoção.
inputs:
  - estudo em 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/
outputs:
  - padrão canônico de camadas documentais
related_notes:
  - yaml_frontmatter_standard_v1.md
  - study_vs_canonical_policy_v1.md
  - migration_strategy_v1.md
tags: [ckos, canonical, governance, documentation, standards]
---

# Canonical Documentation Standard v1

## 1. Purpose

Definir o padrão geral de documentos CKOS. Especificar as camadas documentais, sua autoridade, permissões, quem pode editar, quando pode ser promovido e quando pode gerar migration ou alterar runtime.

## 2. Regra Crítica

> **Somente CANONICAL pode ser usado como fonte de implementação final.**
> STUDY pode recomendar, nunca governar.
> ROADMAP orienta sequência, mas não substitui spec.
> PATCH_REPORT registra mudança, mas não é arquitetura.
> MEMORY registra contexto, mas não é policy.

Nenhum agente deve implementar backend, schema ou runtime com base em documentos STUDY, ROADMAP ou MEMORY sem uma spec CANONICAL aprovada.

## 3. Camadas Documentais

### 3.1 RAW

| Campo | Valor |
|---|---|
| Autoridade | Evidência apenas — não governa nada |
| Status permitido | `raw`, `received`, `archived` |
| Quem pode editar | Agentes de intake, PMO |
| Uso por Codex como spec | **Proibido** |
| Pode gerar migration | **Não** |
| Pode alterar runtime | **Não** |
| Pode ser promovido | Sim, para STUDY após revisão de fonte |
| Condição de promoção | Fonte identificada e revisada |

### 3.2 STUDY

| Campo | Valor |
|---|---|
| Autoridade | Análise não-canônica — pode recomendar |
| Status permitido | `study`, `draft`, `unverified`, `archived` |
| Quem pode editar | Agentes de pesquisa, PMO |
| Uso por Codex como spec | **Proibido** |
| Pode gerar migration | **Não** |
| Pode alterar runtime | **Não** |
| Pode ser promovido | Sim, para candidato canônico após revisão |
| Condição de promoção | Confiança não-baixa, risco avaliado, PMO e Metacognik revisados |

### 3.3 CANONICAL

| Campo | Valor |
|---|---|
| Autoridade | Autoridade máxima do sistema |
| Status permitido | `draft`, `active`, `deprecated`, `archived` |
| Quem pode editar | Apenas owner aprovado com patch report |
| Uso por Codex como spec | **Permitido** |
| Pode gerar migration | **Sim, com patch report e aprovação** |
| Pode alterar runtime | **Sim, com aprovação** |
| Pode ser promovido | Já é canônico |
| Condição de promoção | N/A |

### 3.4 ROADMAP

| Campo | Valor |
|---|---|
| Autoridade | Planejamento auxiliar — não é spec |
| Status permitido | `draft`, `active`, `blocked`, `done`, `archived` |
| Quem pode editar | PMO, agente de roadmap |
| Uso por Codex como spec | **Proibido sem spec canônica correspondente** |
| Pode gerar migration | **Não diretamente** |
| Pode alterar runtime | **Não** |
| Pode ser promovido | Pode informar spec canônica após gate |
| Condição de promoção | Não contradiz spec canônica existente |

### 3.5 PATCH_REPORT

| Campo | Valor |
|---|---|
| Autoridade | Rastreabilidade de mudança |
| Status permitido | `draft`, `active`, `archived` |
| Quem pode editar | PMO, auditor |
| Uso por Codex como spec | **Não** |
| Pode gerar migration | **Não** — suporta migration aprovada |
| Pode alterar runtime | **Não** |
| Pode ser promovido | Pode suportar atualização canônica |
| Condição de promoção | Validação completa |

### 3.6 HANDOFF

| Campo | Valor |
|---|---|
| Autoridade | Continuidade de sessão |
| Status permitido | `draft`, `active`, `completed`, `blocked` |
| Quem pode editar | Agente remetente, agente receptor |
| Uso por Codex como spec | **Não** |
| Pode gerar migration | **Não** |
| Pode alterar runtime | **Não** |
| Pode ser promovido | Pode virar evidência de release |
| Condição de promoção | Escopo não ambíguo |

### 3.7 RELEASE

| Campo | Valor |
|---|---|
| Autoridade | Sumário de mudança aplicada |
| Status permitido | `draft`, `released`, `rolled_back`, `archived` |
| Quem pode editar | Release owner, PMO |
| Uso por Codex como spec | **Não** |
| Pode gerar migration | **Não** |
| Pode alterar runtime | **Não** |
| Pode ser promovido | Suporta auditoria canônica |
| Condição de promoção | Validação presente |

### 3.8 TASK

| Campo | Valor |
|---|---|
| Autoridade | Controle de execução |
| Status permitido | `backlog`, `ready`, `in_progress`, `review`, `done`, `blocked` |
| Quem pode editar | PMO, owner designado |
| Uso por Codex como spec | **Não** |
| Pode gerar migration | **Não** |
| Pode alterar runtime | **Não** |
| Pode ser promovido | Pode produzir handoff ou release |
| Condição de promoção | Escopo declarado |

### 3.9 MEMORY

| Campo | Valor |
|---|---|
| Autoridade | Memória local da pasta |
| Status permitido | `draft`, `active`, `stale`, `archived` |
| Quem pode editar | Folder owner, PMO |
| Uso por Codex como spec | **Não** |
| Pode gerar migration | **Não** |
| Pode alterar runtime | **Não** |
| Pode ser promovido | Pode informar README ou canônico após revisão |
| Condição de promoção | Não é apenas memória local |

### 3.10 FEEDBACK

| Campo | Valor |
|---|---|
| Autoridade | Input de revisão |
| Status permitido | `open`, `triaged`, `resolved`, `archived` |
| Quem pode editar | Revisores, PMO |
| Uso por Codex como spec | **Não** |
| Pode gerar migration | **Não** |
| Pode alterar runtime | **Não** |
| Pode ser promovido | Pode virar task ou patch candidate |
| Condição de promoção | Não duplicado, verificado |

### 3.11 LOCK

| Campo | Valor |
|---|---|
| Autoridade | Controle de edição |
| Status permitido | `active`, `released`, `expired`, `cancelled` |
| Quem pode editar | PMO, session owner |
| Uso por Codex como spec | **Não** |
| Pode gerar migration | **Não** |
| Pode alterar runtime | **Não** |
| Pode ser promovido | Pode virar evidência de release |
| Condição de promoção | Lock liberado, escopo sem conflito |

## 4. Requisitos de Documento Canônico

Todo documento na camada `canonical` deve incluir:

- SemVer (`1.x.x` para aprovado, `0.x.x` para draft).
- Aprovação formal registrada no YAML (`approval_required`).
- Enums controlados (ver `yaml_frontmatter_standard_v1.md`).
- Corpo numerado.
- Exemplos implementáveis quando aplicável.
- Relação com backend, ROI e memória quando aplicável.
- Failure modes.
- Critérios de aprovação e rejeição.

## 5. Estrutura de Corpo Canônico

```md
# 1. Purpose

# 2. Function Inside CKOS

# 3. Inputs

# 4. Outputs

# 5. Operational Framework

# 6. Responsible Agent

# 7. Agents Involved

# 8. Skills Required

# 9. Prompts Related

# 10. Integrations

# 11. Memory And Context

# 12. Backend Relation

# 13. ROI Relation

# 14. Failure Modes

# 15. Test Plan

# 16. Approval Criteria

# 17. Rejection Criteria

# 18. Related Notes
```

## 6. Regras de Versão

- `0.x.x`: proposta ou draft — não é baseline.
- `1.x.x`: baseline aprovado.
- Minor version: expansão compatível.
- Patch version: correção sem mudança semântica.
- Major version: mudança de contrato ou conceito.

## 7. O Que Não Automatizar

- Promoção canônica.
- Edição de documentos canônicos sem patch report.
- Inferência de aprovação.
- Sweep automático em documentos de qualquer camada.
