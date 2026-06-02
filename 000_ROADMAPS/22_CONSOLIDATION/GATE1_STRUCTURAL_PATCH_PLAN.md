---
title: GATE 1 Structural Patch Plan
file: GATE1_STRUCTURAL_PATCH_PLAN.md
layer: auxiliary
doc_type: pmo_patch_plan
phase: 000_ROADMAPS
category: consolidation
status: draft
version: 0.1.0
created_at: 2026-06-01
updated_at: 2026-06-01
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - founder
  - metacognik
  - technical
approval_required:
  - founder
  - pmo_ckos
  - metacognik
confidence: high
provenance_status: pmo_synthesis_grounded
source_tool: claude_opus_4_8
purpose: Plano de patch estrutural do GATE 1 — fechar a migração Self-Evolving (21→25) já decidida, resolver duplicatas 18/19, repontar referências e registrar, com dispatch por capacidade (Windsurf/Codex/Claude). Proposta gated; nada aplicado aqui.
intelligence_level: highest
non_authority_boundary: >
  Plano auxiliar/PMO. NÃO renomeia, move, deleta ou edita doc canônico. NÃO executa o
  patch. Apenas propõe. A execução exige checkout canônico separado + aprovação
  Founder/PMO/Metacognik/Technical. Reaproveita a decisão prévia 2026-05-27 (Opção A).
related_notes:
  - 00_CKOS_CONSOLIDATION_MAP_AND_GAP_AUDIT.md
  - 01_MULTI_SESSION_CONTROL_ROOM_RUNBOOK.md
  - ../../000_STUDY_NOTES/08_DECISION_LOGS/20260527_decision_self-evolving-conflict-resolution_pmo_ckos_draft.md
  - ../../000_UPGRADE/UPLOADS_STUDY_MICROGATE_PROPOSAL/SELF_EVOLVING_RENUMBERING_RISK_REPORT.md
tags: [gate1, patch-plan, structural, renumbering, self-evolving, dispatch]
---

# GATE 1 — Patch Plan Estrutural (proposta gated)

> **Achado de PMO:** este problema já foi decidido em 2026-05-27. Não re-decidimos —
> **fechamos o loop**. O [decision log](../../000_STUDY_NOTES/08_DECISION_LOGS/20260527_decision_self-evolving-conflict-resolution_pmo_ckos_draft.md)
> aprovou **Opção A** e o [risk report](../../000_UPGRADE/UPLOADS_STUDY_MICROGATE_PROPOSAL/SELF_EVOLVING_RENUMBERING_RISK_REPORT.md)
> travou o rename até patch plan + gate Founder. Este é esse patch plan.

---

## 1. Fronteira de autoridade

Plano auxiliar. Não aplica nada. A execução = checkout canônico separado, em **uma janela controlada**, por Codex, após aprovação do Founder. Reaproveita a decisão e o scan prévios.

---

## 2. Estado real vs. estado em 2026-05-27 (o que mudou)

| | 2026-05-27 (decision log) | **2026-06-01 (agora)** |
|---|---|---|
| Docs canônicos | iam até 24 | até **27** |
| `07_EVOLUTION_SYSTEM/` | não existia (proposta) | **existe** (25, 26, 27) |
| `25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` | a criar | **já criado** (v1.0.0, canonical_doc) |
| `05/21_SELF_EVOLVING_SYSTEM.md` | a superseder | **ainda ativo, sem banner** |
| Referências 21→25 | a repontar | **~212 ocorrências em 39 arquivos ainda apontam para 21** |

**Conclusão:** Opção A foi **parcialmente executada** (doc 25 nasceu) mas a migração ficou aberta. GATE 1 = terminar.

---

## 3. Os 3 defeitos e a resolução

### Defeito 1 — Colisão ordinal 21 + Self-Evolving duplicado (G-01/G-02)
- **Canônico vence:** `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` (schema novo `doc_type: canonical_doc`).
- **Superseded:** `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` → banner no topo apontando p/ doc 25; **não deletar** (decisão prévia §8.4).
- **ROI fica dono único do 21:** `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md` inalterado.
- **Decisão pendente do Founder:** manter o arquivo antigo em `05/21...` com banner (rota aprovada, baixo risco) **ou** de-numerar/mover para arquivo (`_SUPERSEDED_...` ou pasta de arquivo) — remove fisicamente a colisão de filename. Ver §7.

### Defeito 2 — Duplicata 18 (Research Protocol)
- **Canônico:** `18_RESEARCH_PROTOCOL.md` (genérico).
- **Auxiliar/vendor:** `18_RESEARCH_PROTOCOL_FOR_MANUS.md` → de-numerar (Manus é ferramenta temporária, não infra; `CKOS_UPGRADE_INDEX` já afirma isso). Renomear p/ `RESEARCH_PROTOCOL_FOR_MANUS_AUXILIARY.md` ou mover para auxiliar. Libera o ordinal 18 para um doc só.

### Defeito 3 — Duplicata 19 (Execution Protocol) ⚠️ precisa de diff
- Candidatos: `19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md` (v1.1.0) vs `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md` (v1.0.0, schema novo).
- **Sinal de governança:** o decision log §4.9 cita a versão **ANTIGRAVITY** como dependência canônica → provável canônico.
- **Ação obrigatória antes de executar:** **diff de conteúdo read-only** (Claude) para confirmar que o canônico é superset e que nenhum conteúdo único se perde. Só então de-numerar o perdedor.

---

## 4. Tabela de substituição de referências (reaproveitada do decision log §8.2)

| De | Para |
|---|---|
| `21_SELF_EVOLVING_SYSTEM.md` | `25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` |
| `[[21_SELF_EVOLVING_SYSTEM]]` | `[[25_SELF_EVOLVING_SYSTEM_ARCHITECTURE]]` |
| `Self-Evolving (21)` / `doc 21 (Self-Evolving)` | `Self-Evolving (25)` / `doc 25 (Self-Evolving)` |
| `../05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` | `../07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` |
| **PRESERVAR** `21_ROI_ARCHITECTURE.md` e `doc 21` quando = ROI | (não tocar) |

**Alto impacto (repontar com cuidado):** Master Map (15 hits), Patch Report (19), Dependency Map, Docs 03/10/11/12/13/17/20, Constitution. **Mapas auxiliares** (FILETREE/FOLDER/VAULT_REFRESH) também.

---

## 5. Arquivos do patch (do decision log §8.1, atualizado)

**Governança/mapas:** `00_MASTER_MAP.md`, `00_DEPENDENCY_MAP.md`, `ARCHITECTURE_PATCH_REPORT.md`, `CKOS_FILETREE_MAP.md`, `CKOS_FOLDER_MEMORY.md`, `CKOS_VAULT_MAP_REFRESH_REPORT.md`.
**Docs canônicos com refs diretas:** 01 Constitution, 03 Agent Model, 10/11/12/13 Runtime, 17 Impl, 18 (Manus), 20 QA, README Impl.
**Novos a tocar (vs 05-27):** `07_EVOLUTION_SYSTEM/00_README` + `25` (confirmar related_notes), `26` (refs).
**NÃO tocar:** `06/21_ROI_ARCHITECTURE.md`, docs não relacionados, `.obsidian/`, `Memória GPT.md`, n8n, qualquer backend/UI/API.

---

## 6. Dispatch por capacidade (Control Room em ação)

Contexto operacional: **Codex volta 00:05 · Claude 55% (conservar) · Windsurf com folga.**

| Quando | Sessão | Tarefa | Modo | Escreve? |
|---|---|---|---|---|
| **Agora** | **Windsurf** (PMO local) | Exportar `rg` completo das 212 refs; montar tabela de substituição exata por arquivo; redigir o banner de superseded; rascunhar entradas de registry/patch-report e diffs de Master/Dependency Map | coordenação / study-only | só arquivos de controle (este plano, BRA, registry-draft) |
| **Agora** | **Claude** (leve) | **1 diff read-only** do par 19 (e confirmar que 18_Manus não tem conteúdo canônico único) → veredito de qual é canônico | read-only audit | não |
| **Você** | **Founder** | Aprovar: (a) tabela de substituição; (b) destino do `05/21` (banner-in-place vs de-numerar); (c) vencedor do 19 | decisão | autoridade |
| **00:05** | **Codex** (escritor) | Executar **em 1 checkout canônico**: banner no `05/21`; repontar 21→25 em todos os arquivos; de-numerar 18_Manus e o 19-perdedor; atualizar Master Map, Dependency Map, Patch Report, mapas auxiliares | canonical_patch | sim, no lock |
| **Pós** | **Claude** (leve) | Auditoria read-only de fan-in: 0 links quebrados, ROI=21 íntegro, doc 25 íntegro | read-only audit | não |

Regra: Codex só escreve **depois** do diff do 19 (Claude) e do OK do Founder. Um arquivo, um escritor; release ao final (Runbook §7).

---

## 7. Decisão que preciso de você (Founder)

1. **Destino do `05/21_SELF_EVOLVING_SYSTEM.md`:**
   - **(A) Banner-in-place** (rota aprovada 05-27): mantém o arquivo, adiciona aviso "superseded → doc 25". Risco baixo. Colisão de *filename* 21 persiste mas resolvida semanticamente.
   - **(B) De-numerar/arquivar**: renomeia p/ `_SUPERSEDED_SELF_EVOLVING_SYSTEM.md` ou move p/ pasta de arquivo. Remove a colisão de filename de vez. Risco um pouco maior (mais um caminho a repontar).
   - *Recomendação PMO:* **B** — você quer a árvore limpa para a expansão; a colisão de filename volta a confundir agentes futuros. Mas A é o caminho já pré-aprovado.
2. **Vencedor do 19:** aceitar a recomendação (ANTIGRAVITY como canônico) **após** o diff do Claude confirmar.

---

## 8. Risco & rollback

- **Risco principal:** links quebrados (212 refs). Mitigação: tabela exata por arquivo (Windsurf) + execução atômica (Codex) + fan-in (Claude).
- **Rollback:** patch em 1 checkout → reverter = restaurar os arquivos do checkout. Nenhuma deleção (só banner/rename reversível).
- **Não criar docs 28-34 neste patch** (decision log §8.10). GATE 1 é só estrutural.

---

## 9. Critérios de aprovação (do decision log §12, mantidos)

- ROI permanece doc 21 sem ambiguidade.
- Self-Evolving = doc 25 sem link quebrado.
- Arquivo antigo claramente superseded.
- 18 e 19 com um único dono canônico cada.
- Nada de docs 28-34 neste patch.
- Tudo registrado no `ARCHITECTURE_PATCH_REPORT.md`.

---

## 10. Próxima ação

Disparar **agora** as duas sessões paralelas (Windsurf prep + Claude diff do 19). Quando o Founder aprovar §7 e o Codex voltar (00:05), executar o patch em uma janela. Eu (PMO) gero os prompts prontos do Runbook para cada sessão sob seu OK.
