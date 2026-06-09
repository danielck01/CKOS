---
title: Folder Memory Policy
file: FOLDER_MEMORY_POLICY.md
layer: auxiliary
doc_type: pmo_governance_note
phase: 000_ROADMAPS
category: governance
status: active
version: 1.0.0
created_at: 2026-06-09
owner: pmo_ckos
responsible_agent: claude_opus_4_7
session_id: S-GOV-FOLDMEM-CLAUDE-20260609-001
reviewers:
  - founder
  - pmo_ckos
approval_required:
  - founder
  - pmo_ckos
non_authority_boundary: >
  Nota de governança PMO auxiliar. NÃO é canônica. NÃO autoriza canonical_patch.
  Formaliza a prática já consolidada desde P1.7.1 (2026-05-28) e confirma
  o padrão escolhido pelo Founder em 2026-06-09 na migração da pasta
  000_STUDY_NOTES/02_RESEARCH_SYNTHESIS/.
related_notes:
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 00_SYSTEM_GOVERNANCE/00_TAXONOMY_AND_NAMING.md
tags: [governance, folder-memory, ck-memory, policy, pmo, anti-destructive]
---

# Folder Memory Policy

> **Origem:** prática consolidada desde P1.7.1 (Codex, 2026-05-28) e reconfirmada pelo Founder em 2026-06-09 ao migrar `000_STUDY_NOTES/02_RESEARCH_SYNTHESIS/`.
> **Função desta nota:** formalizar a política em um único lugar consultável; reduzir ambiguidade futura sobre quando migrar, quando preservar e quando NÃO bulk-deletar.

## 1. Standard atual

**`ck_memory.md`** — memória ativa por pasta. Estrutura mínima:
- Frontmatter YAML com `title`, `file`, `layer`, `phase`, `category`, `status`, `version`, `owner`, `responsible_agent`, `confidence`, `provenance_status`, `created_at`, `tags`, `related_notes`
- Conteúdo: estado vivo da pasta, decisões em andamento, próximo audit, owner ativo

Exemplos existentes (5 pastas, em 2026-06-09):
- `000_STUDY_NOTES/12_SESSION_GATES/ck_memory.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/ck_memory.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md`
- `000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/ck_memory.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/00_GOVERNANCE/ck_memory.md`
- `000_STUDY_NOTES/02_RESEARCH_SYNTHESIS/ck_memory.md` (criada 2026-06-09)

## 2. Legacy

**`_folder_memory.md`** — formato anterior (P1.7 e antes). **Preservado como historical context.**

Em 2026-06-09 existem 32 arquivos `_folder_memory.md` no vault (após a deleção explícita em `02_RESEARCH_SYNTHESIS/`). Muitos contêm:
- Histórico operacional de atualizações datadas
- Regras de fronteira (layer, entrada, saída)
- Travas (anti-implementation, anti-canonical)
- Notice de preservação explícito (ex.: `12_SESSION_GATES/_folder_memory.md` linha 38: *"Do not delete this file; keep it as historical context."*)

## 3. Coexistência

Cada pasta pode ter:

| Configuração | Significado |
|---|---|
| Só `_folder_memory.md` | Pasta inativa ou em modo legacy. Sem necessidade de migrar agora. |
| Só `ck_memory.md` | Pasta criada após P1.7.1 ou migrada explicitamente. |
| Ambos | Pasta migrada com `_folder_memory.md` preservado para histórico. |

## 4. Quando criar `ck_memory.md`

- Pasta nova precisa de memória ativa
- Pasta legacy entra em uso ativo (estudo recorrente, patch candidate em andamento, sessão multi-turn)
- Migração explícita autorizada pelo owner da pasta

## 5. Quando NÃO bulk-deletar `_folder_memory.md`

**Regra dura:** não fazer bulk-delete de `_folder_memory.md` em sweep automatizado. Razões:

1. **Conteúdo operacional real** — muitos arquivos têm histórico, regras e travas que se perdem com delete
2. **Notice explícito de preservação** — vários arquivos pedem explicitamente para não deletar
3. **Provenance** — `_folder_memory.md` registra a evolução da pasta ao longo de gates anteriores (P1.7, P1.11, etc.); apagar = perder traceability
4. **Princípio anti-destrutivo** (sistema CKOS) — operações destrutivas exigem autorização explícita escopo-a-escopo

**Exceção autorizada:** delete pontual quando:
- O arquivo é boilerplate genérico (sem histórico real)
- O Founder/owner aprovou explicitamente para aquela pasta específica
- Existe um `ck_memory.md` substituto criado na mesma sessão

Exemplo da única exceção até hoje (2026-06-09): `000_STUDY_NOTES/02_RESEARCH_SYNTHESIS/_folder_memory.md` — boilerplate de 314 bytes, sem histórico; substituído por `ck_memory.md` rico na mesma sessão `S-USER-PMO-CLAUDE-20260609-001`.

## 6. Quando migrar uma pasta inteira

Migração explícita de `_folder_memory.md` → `ck_memory.md` deve seguir:

1. **Sessão dedicada** (`governance_cleanup` ou similar)
2. **Ler conteúdo** do `_folder_memory.md` da pasta
3. **Criar `ck_memory.md`** trazendo o histórico relevante + estado atual + próximo audit
4. **Decidir destino do legado**:
   - **a)** preservar `_folder_memory.md` intacto (default — recomendado)
   - **b)** adicionar header "## Legacy/Superseded Notice" no `_folder_memory.md` apontando para `ck_memory.md` (precedente: `12_SESSION_GATES/_folder_memory.md` linha 36-38)
   - **c)** delete (somente se conteúdo for boilerplate genérico — exceção, com autorização explícita)
5. **Registrar a sessão** no `SESSION_REGISTRY.md` com lock + release

## 7. NÃO criar `ck_memory.md` de improviso

Criar `ck_memory.md` em pasta inativa/dormente = ruído. A criação deve responder a uma necessidade operacional real (estudo em curso, patch em andamento, próximo audit registrável).

## 8. Estado em 2026-06-09 (snapshot)

| Métrica | Valor |
|---|---|
| Pastas com `_folder_memory.md` | 32 |
| Pastas com `ck_memory.md` | 6 (5 anteriores + 1 nova) |
| Pastas com ambos | 4 (12_SESSION_GATES, 10_UIUX_STUDIES, 13_AI_FIRST..., DNA/00_GOVERNANCE) — após P1.7.1 |
| Pastas migradas com delete legado | 1 (02_RESEARCH_SYNTHESIS) |

## 9. Cross-references

- Política original P1.7.1 (Codex): `SESSION_REGISTRY.md` linha 84 (`S-P1-7-1-CODEX-20260528-001`)
- Notice de preservação modelo: `000_STUDY_NOTES/12_SESSION_GATES/_folder_memory.md` linha 36-38
- Migração de referência (delete + substituição): commit `c3786c2` (2026-06-09)
- Padrão de frontmatter `ck_memory.md`: `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md`
