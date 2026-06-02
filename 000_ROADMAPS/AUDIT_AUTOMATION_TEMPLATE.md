---
title: Audit Automation Template
system_id: audit_template_v1_0
layer: auxiliary
phase: 000_ROADMAPS
category: audit_template
status: template
version: 1.0.0
owner: pmo_ckos
created_at: 2026-06-01
purpose: Template para geração automática de notas de auditoria com comandos para Codex e Cascade
---

# Audit Automation Template

## Uso

Este template deve ser usado pelo Claude/Cascade sempre que realizar uma auditoria. Substitua os campos entre `[ ]` com os valores reais da auditoria.

---

# AUDITORIA AUTOMÁTICA — [NOME_DA_AUDITORIA]

## Metadados

- **Data:** [YYYY-MM-DD]
- **Sessão:** [SESSION_ID]
- **Agente:** [Claude/Cascade/Codex]
- **Modo:** [READ-ONLY/AUDIT/PATCH]
- **Escopo:** [ESCOPO_AUDITADO]
- **Veredito:** [VEREDITO_FINAL]

---

## 1. VEREDITO

[RESUMO_DO_VEREDITO_EM_1-2_PARÁGRAFOS]

---

## 2. ARQUIVOS LIDOS

| Arquivo | Status | Observações |
|---|---|---|
| [ARQUIVO_1] | [OK/ERRO] | [OBSERVAÇÃO] |
| [ARQUIVO_2] | [OK/ERRO] | [OBSERVAÇÃO] |
| [ARQUIVO_N] | [OK/ERRO] | [OBSERVAÇÃO] |

---

## 3. ACHADOS CRÍTICOS

### AC-[NUMERO] — [TÍTULO_DO_ACHADO]
**Severidade:** [Alta/Média/Baixa]

[DESCRIÇÃO_DETALHADA_DO_ACHADO]

---

## 4. PATCHES OBRIGATÓRIOS

| ID | Patch | Arquivo(s) | Por que bloqueia |
|---|---|---|---|
| [M-1] | [DESCRIÇÃO] | [ARQUIVOS] | [JUSTIFICATIVA] |
| [M-2] | [DESCRIÇÃO] | [ARQUIVOS] | [JUSTIFICATIVA] |

---

## 5. PATCHES LEVES (RECOMENDADOS)

| ID | Patch | Arquivo(s) | Prioridade |
|---|---|---|---|
| [L-1] | [DESCRIÇÃO] | [ARQUIVOS] | [Alta/Média/Baixa] |
| [L-2] | [DESCRIÇÃO] | [ARQUIVOS] | [Alta/Média/Baixa] |

---

## 6. RISCOS IDENTIFICADOS

| ID | Risco | Severidade | Mitigação |
|---|---|---|---|
| [R-1] | [DESCRIÇÃO] | [Alta/Média/Baixa] | [MITIGAÇÃO] |
| [R-2] | [DESCRIÇÃO] | [Alta/Média/Baixa] | [MITIGAÇÃO] |

---

## 7. BRA PACKET PARA CODEX

```yaml
bra_id: BRA-[AGENT]-CODEX-[DATE]-[SEQUENCE]
timestamp: [TIMESTAMP]
origin_session: [SESSION_ID]
target_session: [TARGET_SESSION]
scope:
  allowed:
    - [PERMISSÃO_1]
    - [PERMISSÃO_2]
  forbidden:
    - [RESTRIÇÃO_1]
    - [RESTRIÇÃO_2]
mode: [MODE]
checkout_lock_ref: [LOCK_REF]
intelligence_level: [high/highest]
files_read:
  - [ARQUIVO_1]
  - [ARQUIVO_2]
files_created: []
files_changed: []
findings:
  - [ACHADO_1]
  - [ACHADO_2]
mandatory_patches:
  - [M-1]
  - [M-2]
light_patches:
  - [L-1]
  - [L-2]
open_questions:
  - [PERGUNTA_1]
  - [PERGUNTA_2]
risks:
  - [RISCO_1]
  - [RISCO_2]
blocked_by:
  type: [BLOCK_TYPE]
  detail: [DETAIL]
handoff_request: [REQUEST]
expiry: [EXPIRY_DATE]
recommended_next_action: [ACTION]
founder_decision_required: [true/false]
roi_impact: [IMPACT]
```

---

## 8. BRA PACKET PARA CASCADE

```yaml
bra_id: BRA-[AGENT]-CASCADE-[DATE]-[SEQUENCE]
timestamp: [TIMESTAMP]
origin_session: [SESSION_ID]
target_session: cascade_implementation
scope:
  allowed:
    - [PERMISSÃO_1]
    - [PERMISSÃO_2]
  forbidden:
    - [RESTRIÇÃO_1]
    - [RESTRIÇÃO_2]
mode: [MODE]
checkout_lock_ref: [LOCK_REF]
intelligence_level: [high/highest]
files_read:
  - [ARQUIVO_1]
  - [ARQUIVO_2]
files_created: []
files_changed: []
findings:
  - [ACHADO_1]
  - [ACHADO_2]
mandatory_patches:
  - [M-1]
  - [M-2]
light_patches:
  - [L-1]
  - [L-2]
open_questions:
  - [PERGUNTA_1]
  - [PERGUNTA_2]
risks:
  - [RISCO_1]
  - [RISCO_2]
blocked_by:
  type: [BLOCK_TYPE]
  detail: [DETAIL]
handoff_request: [REQUEST]
expiry: [EXPIRY_DATE]
recommended_next_action: [ACTION]
founder_decision_required: [true/false]
roi_impact: [IMPACT]
cascade_specific_instructions:
  - [INSTRUÇÃO_ESPECÍFICA_PARA_CASCADE]
  - [INSTRUÇÃO_ESPECÍFICA_PARA_CASCADE]
```

---

## 9. CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: [SESSION_ID]
mode: [MODE]
allowed_scope:
  - [PERMISSÃO_1]
  - [PERMISSÃO_2]
files_created:
  - [ARQUIVO_CRIADO_1]
  - [ARQUIVO_CRIADO_2]
files_changed:
  - [ARQUIVO_MODIFICADO_1]
  - [ARQUIVO_MODIFICADO_2]
files_not_touched:
  - [ARQUIVO_NÃO_TOCADO_1]
  - [ARQUIVO_NÃO_TOCADO_2]
validation:
  - [VALIDAÇÃO_1]
  - [VALIDAÇÃO_2]
verdict: [VEREDITO]
mandatory_patches: [M-1, M-2]
light_patches: [L-1, L-2]
risks_remaining:
  - [RISCO_1]
  - [RISCO_2]
next_step:
  - [PRÓXIMO_PASSO_1]
  - [PRÓXIMO_PASSO_2]
status: [STATUS]
SESSÃO FINALIZADA
```

---

## 10. RESUMO EXECUTIVO

**Uma linha:** [RESUMO_EM_UMA_LINHA]

**Próximos passos:**
1. [PASSO_1]
2. [PASSO_2]
3. [PASSO_3]

**Decisão requerida:** [SIM/NÃO]
**Responsável:** [RESPONSÁVEL]
**Prazo:** [PRAZO]

---

## INSTRUÇÕES PARA O AGENTE

Quando este template for usado:

1. **Substitua todos os campos entre `[ ]`** com os valores reais
2. **Mantenha a estrutura YAML** para BRA Packets
3. **Gere automaticamente** os BRA Packets para Codex e Cascade
4. **Registre no SESSION_REGISTRY** após completar a auditoria
5. **Crie nota no Kanban** para tracking visual
6. **Atualize dependências** se houver bloqueios

---

## INTEGRAÇÃO COM KANBAN

Após gerar a auditoria, o agente deve:

1. Adicionar tarefa ao Kanban em `000_ROADMAPS/TASK_KANBAN.md`
2. Categoria: `Auditoria`
3. Status inicial: `Em Progresso`
4. Adicionar tags: `#audit`, `#[AGENTE]`, `#[ESCOPO]`
5. Linkar para esta nota de auditoria
