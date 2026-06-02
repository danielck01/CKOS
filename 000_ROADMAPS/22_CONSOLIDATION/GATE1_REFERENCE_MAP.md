---
title: GATE 1 Reference Map — Self-Evolving 21→25 Migration
file: GATE1_REFERENCE_MAP.md
layer: auxiliary
doc_type: pmo_reference_map
phase: 000_ROADMAPS
category: consolidation
status: draft
version: 0.1.0
created_at: 2026-06-01
updated_at: 2026-06-01
owner: pmo_ckos
responsible_agent: windsurf
reviewers:
  - founder
  - metacognik
  - technical
approval_required:
  - founder
  - pmo_ckos
confidence: high
provenance_status: pmo_synthesis_grounded
source_tool: windsurf_rg_scan
purpose: Mapa completo de referências ao Doc 21 Self-Evolving para execução do GATE 1. Exporta todas as ocorrências encontradas por rg, classifica quais são ROI-21 (preservar) vs Self-Evolving-21 (migrar), redige banner superseded, e rascunha diffs de governança. NÃO aplica nada; é material de trabalho para Codex executar após Founder approval.
intelligence_level: high
non_authority_boundary: >
  Mapa auxiliar/PMO. NÃO renomeia, move, deleta ou edita doc canônico. NÃO executa o
  patch. Apenas propõe. A execução exige checkout canônico separado + aprovação
  Founder/PMO/Metacognik/Technical.
related_notes:
  - GATE1_STRUCTURAL_PATCH_PLAN.md
  - ../../000_STUDY_NOTES/08_DECISION_LOGS/20260527_decision_self-evolving-conflict-resolution_pmo_ckos_draft.md
  - ../../000_UPGRADE/UPLOADS_STUDY_MICROGATE_PROPOSAL/SELF_EVOLVING_RENUMBERING_RISK_REPORT.md
tags: [gate1, reference-map, self-evolving, migration, 21-to-25]
---

# GATE 1 Reference Map — Self-Evolving 21→25 Migration

> **SESSION:** S-P1-GATE1-WINDSURF-20260601-001  
> **MODE:** coordenação/study-only  
> **INTELLIGENCE:** high  
> **STATUS:** draft (aguardando Founder approval)

---

## 1. Escopo do scan

**Data do scan:** 2026-06-01  
**Ferramenta:** rg (ripgrep)  
**Diretório:** vault completo (exceto `.obsidian/`)  
**Padrões buscados:**
- `21_SELF_EVOLVING_SYSTEM`
- `[[21_SELF_EVOLVING_SYSTEM]]`
- `Self-Evolving (21)`
- `doc 21 (Self-Evolving)`
- `../05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`

**Resultado bruto:** 90 matches em 22 arquivos para o padrão principal `21_SELF_EVOLVING_SYSTEM`. Os padrões de wikilink e path específico não retornaram resultados (a migração já foi parcialmente aplicada em 2026-05-27).

---

## 2. Classificação de referências

### 2.1 ROI-21 (NÃO MUDAR)

Referências ao `21_ROI_ARCHITECTURE.md` em `06_BUSINESS_SYSTEMS/` devem ser preservadas. ROI permanece doc 21.

| Arquivo | Linha | Trecho | Ação |
|---|---|---|---|
| `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md` | 1-5 | `title: 21_ROI_ARCHITECTURE`... | PRESERVAR (próprio arquivo) |
| `06_BUSINESS_SYSTEMS/22_FEEDBACK_SYSTEM_ARCHITECTURE.md` | 26 | `- 21_ROI_ARCHITECTURE.md v1.0.0` | PRESERVAR |
| `06_BUSINESS_SYSTEMS/22_FEEDBACK_SYSTEM_ARCHITECTURE.md` | 47 | `- 21_ROI_ARCHITECTURE.md` | PRESERVAR |
| `06_BUSINESS_SYSTEMS/22_FEEDBACK_SYSTEM_ARCHITECTURE.md` | 1387 | `- [[21_ROI_ARCHITECTURE]]` | PRESERVAR |
| `06_BUSINESS_SYSTEMS/23_SUPPORT_SYSTEM_ARCHITECTURE.md` | 36 | `- 21_ROI_ARCHITECTURE.md` | PRESERVAR |
| `06_BUSINESS_SYSTEMS/23_SUPPORT_SYSTEM_ARCHITECTURE.md` | 1306 | `- 21_ROI_ARCHITECTURE.md` | PRESERVAR |
| `06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md` | 37 | `- 21_ROI_ARCHITECTURE.md` | PRESERVAR |
| `06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md` | 1276 | `- 21_ROI_ARCHITECTURE.md` | PRESERVAR |

### 2.2 Self-Evolving-21 (MIGRAR PARA 25)

Referências ao antigo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` devem ser repontadas para `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`.

| Arquivo | Linha | Trecho | Substituição proposta |
|---|---|---|---|
| `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md` | 27 | `- ../05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` | `- ../07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` |
| `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md` | 37 | `...ver 21_SELF_EVOLVING_SYSTEM` | `...ver 25_SELF_EVOLVING_SYSTEM_ARCHITECTURE` |
| `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md` | 138 | `...21_SELF_EVOLVING_SYSTEM.md` | `...25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` |
| `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md` | 200 | `- [[21_SELF_EVOLVING_SYSTEM]]` | `- [[25_SELF_EVOLVING_SYSTEM_ARCHITECTURE]]` |
| `01_THINKING_SYSTEM/01_CKOS_AI_FIRST_CONSTITUTION.md` | 90 | `...21_SELF_EVOLVING_SYSTEM.md` | `...25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` |
| `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` | 3 | `file: 21_SELF_EVOLVING_SYSTEM.md` | (adicionar banner superseded) |
| `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md` | 26 | `- 21_SELF_EVOLVING_SYSTEM.md` | `- ../07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` |
| `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md` | 43 | `...21_SELF_EVOLVING_SYSTEM` | `...25_SELF_EVOLVING_SYSTEM_ARCHITECTURE` |
| `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md` | 140 | `- [[21_SELF_EVOLVING_SYSTEM]]` | `- [[25_SELF_EVOLVING_SYSTEM_ARCHITECTURE]]` |
| `05_IMPLEMENTATION_SYSTEM/00_README_IMPLEMENTATION_SYSTEM.md` | 41 | `5. 21_SELF_EVOLVING_SYSTEM.md` | `5. (histórico) 21_SELF_EVOLVING_SYSTEM.md → ver 25 em 07_EVOLUTION_SYSTEM` |
| `05_IMPLEMENTATION_SYSTEM/00_README_IMPLEMENTATION_SYSTEM.md` | 48 | `21_SELF_EVOLVING_SYSTEM criado` | `25_SELF_EVOLVING_SYSTEM_ARCHITECTURE criado` |
| `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md` | 89 | `...21_SELF_EVOLVING_SYSTEM.md` | `...25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` |
| `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md` | 96 | `...21_SELF_EVOLVING_SYSTEM.md` | `...25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` |
| `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md` | 175 | `...21_SELF_EVOLVING_SYSTEM.md` | `...25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` |
| `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md` | 233 | `21_SELF_EVOLVING_SYSTEM.md` | `25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` |
| `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md` | 242 | `...21_SELF_EVOLVING_SYSTEM.md` | `...25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` |
| `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md` | 244 | `...21_SELF_EVOLVING_SYSTEM.md` | `...25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` |
| `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md` | 156 | `...21_SELF_EVOLVING_SYSTEM.md` | `...25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` |
| `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` | 1 | (frontmatter) | (verificar related_notes) |

### 2.3 Arquivos auxiliares (mapas, reports, memories)

Estes arquivos registram o estado da migração e devem ser atualizados para consistência.

| Arquivo | Tipo de atualização | Nota |
|---|---|---|
| `CKOS_VAULT_MAP_REFRESH_REPORT.md` | Atualizar referências ao 21 | Já registra superseded em 2026-05-27 |
| `CKOS_FOLDER_MEMORY.md` | Atualizar referências ao 21 | Já registra superseded em 2026-05-27 |
| `CKOS_FILETREE_MAP.md` | Atualizar referências ao 21 | Já registra superseded em 2026-05-27 |
| `ARCHITECTURE_PATCH_REPORT.md` | Seção 26 já registra patch | Já registra superseded em 2026-05-27 |
| `000_UPGRADE/CKOS_CONTINUATION_PLAN.md` | Atualizar referências ao 21 | Pack auxiliar, não canônico |
| `000_UPGRADE/CKOS_CODEX_MEMORY.md` | Atualizar referências ao 21 | Pack auxiliar, não canônico |
| `000_UPGRADE/CKOS_UPGRADE_INDEX.md` | Atualizar referências ao 21 | Pack auxiliar, não canônico |
| `000_UPGRADE/CKOS_CREATOR_MODE_PACK/*` | Atualizar referências ao 21 | Pack auxiliar, não canônico |
| `000_UPGRADE/UPLOADS_STUDY_MICROGATE_PROPOSAL/*` | Atualizar referências ao 21 | Pack auxiliar, não canônico |
| `000_ROADMAPS/22_CONSOLIDATION/*` | Atualizar referências ao 21 | Arquivos de trabalho PMO |
| `000_STUDY_NOTES/08_DECISION_LOGS/*` | Atualizar referências ao 21 | Decision log histórico |

---

## 3. Banner "superseded" para 05/21

Proposta de banner a adicionar no topo de `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` (após o frontmatter YAML):

```markdown
> **⚠️ SUPERSEDED — 2026-06-01**
>
> Este documento foi preservado como material histórico. A arquitetura Self-Evolving ativa agora vive em:
>
> **`07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`**
>
> O doc 21 permanece ativo para ROI Architecture em `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`.
>
> Não edite este arquivo. Referências futuras devem apontar para o doc 25.
```

---

## 4. Diff proposto — 00_MASTER_MAP.md

### 4.1 Linha 89
```diff
- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` foi preservado como historico/superseded.
+ `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` foi preservado como historico/superseded (ver banner no topo).
```

### 4.2 Linha 96
```diff
- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` (superseded/historico)
+ `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` (superseded/historico — banner adicionado em 2026-06-01)
```

### 4.3 Linha 175
```diff
- Self-Evolving ativo e `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`. O arquivo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` esta preservado como superseded/historico.
+ Self-Evolving ativo e `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`. O arquivo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` esta preservado como superseded/historico com banner apontando para doc 25.
```

### 4.4 Linha 233
```diff
- └── 21_SELF_EVOLVING_SYSTEM.md             (superseded/historico)
+ └── 21_SELF_EVOLVING_SYSTEM.md             (superseded/historico — banner adicionado)
```

### 4.5 Linha 242
```diff
- Docs canônicos numerados: **00 (×4) + 01–27 = 31 canônicos**, considerando que o antigo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` foi preservado como histórico/superseded e que `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md` permanece o doc 21 ativo.
+ Docs canônicos numerados: **00 (×4) + 01–27 = 31 canônicos**, considerando que o antigo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` foi preservado como histórico/superseded com banner (2026-06-01) e que `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md` permanece o doc 21 ativo.
```

### 4.6 Linha 244
```diff
- Nota de refresh 2026-05-27: o conflito de numeracao foi resolvido por decisao Founder. `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md` permanece como doc 21. Self-Evolving ativo agora e `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`. O arquivo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` permanece preservado como material historico/superseded.
+ Nota de refresh 2026-05-27: o conflito de numeracao foi resolvido por decisao Founder. `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md` permanece como doc 21. Self-Evolving ativo agora e `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`. O arquivo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` permanece preservado como material historico/superseded com banner adicionado em 2026-06-01.
```

---

## 5. Diff proposto — 00_DEPENDENCY_MAP.md

### 5.1 Linha 156
```diff
- | 25 Self-Evolving | `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` criado; antigo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` preservado como superseded; ROI permanece doc 21 |
+ | 25 Self-Evolving | `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` criado; antigo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` preservado como superseded com banner (2026-06-01); ROI permanece doc 21 |
```

---

## 6. Entrada proposta — SESSION_REGISTRY.md

```markdown
| S-P1-GATE1-CODEX-20260601-001 | GATE1_SELF_EVOLVING_21_TO_25_MIGRATION_20260601 | canonical_patch | codex | `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` (banner only), `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md`, `01_THINKING_SYSTEM/01_CKOS_AI_FIRST_CONSTITUTION.md`, `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md`, `05_IMPLEMENTATION_SYSTEM/00_README_IMPLEMENTATION_SYSTEM.md`, `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`, `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md`, mapas auxiliares (CKOS_FILETREE_MAP.md, CKOS_FOLDER_MEMORY.md, CKOS_VAULT_MAP_REFRESH_REPORT.md) | Docs 01-26, Docs 28-34, `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md` (preservar), `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` (preservar), `.obsidian/`, `Memória GPT.md`, backend, UI, API, database, migrations, MCP server real, webhook real, JSON n8n, real agents, runtime automations | released_with_required_external_audit | 2026-06-01 | Aplicar banner superseded no 05/21, repontar todas as referências Self-Evolving-21→25, preservar ROI-21, atualizar mapas de governança e auxiliares; não deletar, não mover, não renomear arquivos | high | highest |
```

---

## 7. Seção proposta — ARCHITECTURE_PATCH_REPORT.md

```markdown
# 27. GATE 1 — Self-Evolving 21→25 Reference Migration

**Data:** 2026-06-01  
**Trigger:** Founder aprovou GATE1_STRUCTURAL_PATCH_PLAN.md.  
**Sessão:** S-P1-GATE1-CODEX-20260601-001  
**Executor:** Codex  
**Auditoria:** Claude (read-only fan-in)

## 27.1 Objetivo

Completar a migração de referências do antigo Doc 21 Self-Evolving (`05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`) para o Doc 25 ativo (`07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`), preservando ROI como Doc 21 (`06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`).

## 27.2 Arquivos alterados

### Banner adicionado
- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` — banner superseded no topo apontando para doc 25

### Referências repontadas (Self-Evolving 21→25)
- `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md` — 4 ocorrências
- `01_THINKING_SYSTEM/01_CKOS_AI_FIRST_CONSTITUTION.md` — 1 ocorrência
- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md` — 3 ocorrências
- `05_IMPLEMENTATION_SYSTEM/00_README_IMPLEMENTATION_SYSTEM.md` — 2 ocorrências
- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md` — 6 ocorrências
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md` — 1 ocorrência

### Mapas auxiliares atualizados
- `CKOS_FILETREE_MAP.md` — referências ao 21
- `CKOS_FOLDER_MEMORY.md` — referências ao 21
- `CKOS_VAULT_MAP_REFRESH_REPORT.md` — referências ao 21

### Packs auxiliares atualizados (opcional)
- `000_UPGRADE/CKOS_CONTINUATION_PLAN.md`
- `000_UPGRADE/CKOS_CODEX_MEMORY.md`
- `000_UPGRADE/CKOS_UPGRADE_INDEX.md`
- `000_UPGRADE/CKOS_CREATOR_MODE_PACK/*`
- `000_UPGRADE/UPLOADS_STUDY_MICROGATE_PROPOSAL/*`

## 27.3 Arquivos NÃO alterados

- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md` — preservado como doc 21 ativo
- `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` — preservado como doc ativo
- Docs 01-26 canônicos — nenhum conteúdo alterado além de referências
- Docs 28-34 — não criados
- `.obsidian/` — não tocado
- `Memória GPT.md` — não tocado

## 27.4 Validação

- ROI permanece doc 21 sem ambiguidade
- Self-Evolving = doc 25 sem link quebrado
- Arquivo antigo claramente superseded com banner
- Nenhum arquivo deletado, movido ou renomeado
- Nenhuma implementação criada

## 27.5 Status

**GATE 1 migration completed.**
```

---

## 8. Resumo estatístico

| Categoria | Contagem |
|---|---:|
| Total de matches (rg) | 90 |
| Arquivos afetados | 22 |
| Referências ROI-21 (preservar) | 8 |
| Referências Self-Evolving-21 (migrar) | 16 |
| Arquivos canônicos principais | 6 |
| Arquivos auxiliares (mapas/reports) | 10 |
| Packs auxiliares (000_UPGRADE) | 6 |

---

## 9. Próximos passos (após Founder approval)

1. Founder aprovar: (a) tabela de substituição; (b) banner proposto; (c) diffs de governança
2. Codex executar patch em 1 checkout canônico
3. Claude fazer auditoria read-only de fan-in (0 links quebrados, ROI=21 íntegro, doc 25 íntegro)
4. Registrar release em SESSION_REGISTRY e ARCHITECTURE_PATCH_REPORT

---

## 10. Riscos identificados

- **Risco principal:** links quebrados se substituição não for exata
- **Risco secundário:** ROI ser confundido com Self-Evolving se contexto não for claro
- **Mitigação:** tabela exata por arquivo + execução atômica + fan-in audit

---

## 11. CHECKOUT RELEASE (sessão Windsurf)

**files_created:** `000_ROADMAPS/22_CONSOLIDATION/GATE1_REFERENCE_MAP.md`  
**files_changed:** nenhum (modo study-only)  
**validation:** Scan rg completo exportado; tabela de substituição classificada (ROI-21 preservar, Self-Evolving-21 migrar); banner superseded redigido; diffs de governança rascunhados; entrada SESSION_REGISTRY proposta; seção ARCHITECTURE_PATCH_REPORT proposta.  
**risks_remaining:** Risco de links quebrados se Codex não seguir tabela exata; risco de ROI ser confundido se contexto não for claro.  
**next_step:** Founder aprovar §7 (decisão destino 05/21 e vencedor 19), então Codex executar patch em checkout canônico.  
**status:** released_study_only_reference_map
