---
title: Consolidation Execution Plan
file: 04_CONSOLIDATION_EXECUTION_PLAN.md
phase: 000_ROADMAPS
category: consolidation
status: awaiting_founder_approval
owner: pmo_ckos
created_at: 2026-06-02
session_id: S-P1-CONSOL-CLAUDE-20260602-007
companion_of: 00_CKOS_CONSOLIDATION_MAP_AND_GAP_AUDIT.md
inventory_source: git ls-files @ 2026-06-02 (baseline b3fc69f)
non_authority_boundary: >
  Plano operacional auxiliar. Nada é movido/arquivado/renomeado por este documento.
  Cada lote exige checkout lock + aprovação Founder. git dá rollback. Não deleta nada.
---

# Plano de Execução da Consolidação

> **Diagnóstico (00_MAP) → Execução (este doc).** Inventário real revelou que a fragmentação
> não é "1 arquitetura documentada 35×" — são **3 naturezas distintas** misturadas na mesma gaveta.

## 1. Inventário real (2026-06-02)

| Camada | Arq | Natureza |
|---|---|---|
| **Canônico 00-07** | **~42** | **VERDADE de arquitetura** |
| 000_ROADMAPS | 174 | Processo/governança (este pacote) |
| 000_UPGRADE | 454 | Misto: espelho-arquitetura + operacional + referência |
| 000_STUDY_NOTES/DNA_SYSTEM | 436 | Espelho-arquitetura (271 vault) + projeto visual (158) |
| 000_STUDY_NOTES/Brain | 410 | **Knowledge base de domínio** (NÃO é arquitetura) |
| 000_STUDY_NOTES (outros) | ~145 | Study de arquitetura + dups |
| 99_RESEARCH_LAB | 30 | Referência de implementação |
| 000_UPLOADS | 41 | Uploads brutos |

**Sinal vs ruído: 42 canônico : ~1.450 resto = 1:35.** Mas só **~470 são espelho-arquitetura real**; o resto é knowledge base + operacional na pasta errada.

## 2. Princípios de execução

1. **Canônico 01-28 = única verdade de arquitetura.** Conflito → canônico vence.
2. **Não deletar.** Mover para `99_ARCHIVE/[bloco]/` com README-pointer. git dá rollback.
3. **Por lote, com lock + aprovação Founder.** Um bloco por vez.
4. **3 naturezas, 3 tratamentos:** espelho-arquitetura = reconciliar; knowledge base = segregar; operacional = manter.
5. **Promoção nunca direto no canônico** — vira patch candidate + fan-in (P1).

## 3. Classificação por bloco → destino

| Bloco | Arq | Destino | Mecanismo |
|---|---|---|---|
| Canônico 00-07 | 42 | **MANTER** | — (é a verdade) |
| 000_ROADMAPS | 174 | **MANTER** | processo/governança |
| UPGRADE/03_AGENT_CIVILIZATION | 65 | **RECONCILIAR** vs Doc 03 | promover joia → patch; arquivar resto |
| UPGRADE/04_SKILLS·08_TRANSFORMERS·11_DATA_MODELS·07_POLICIES | ~48 | **RECONCILIAR** vs Docs 06/09/11/12 | idem |
| UPGRADE/05_TOOLS·06_CONNECTORS·10_WORKFLOWS·09_LEARNING·01_CORE | ~50 | **RECONCILIAR** vs Docs 26/07/10/25 | idem |
| UPGRADE/CKOS_CREATOR_MODE_PACK | 30 | **MANTER** | operacional (modo de operação) |
| UPGRADE/MIRIAM_*  | 100 | **MOVER → projetos** | projeto de cliente, não doc de sistema (D3) |
| UPGRADE/ckos_digitalocean_n8n_pack | 56 | **REFERÊNCIA** | acelerador; não core (Doc 26 R) |
| UPGRADE/deep_research·BRIEFING_TYPES·Codex_Continuation | ~70 | **ARQUIVAR** (extrair joia se houver) | já coberto por Docs 18/08/19 |
| DNA_SYSTEM/DNA_system_vault | 271 | **MINA DE PROMOÇÃO** | extrair DNA-PC-1..7 → patch; arquivar vault |
| DNA_SYSTEM/SUPERAGENT_Director_Visual | 158 | **BENCHMARK EXTERNO** (academia IA, não nosso) | extrair técnica/skills/formato (como paperclip); migrar estudo do DNA; não versionar como nosso |
| STUDY/Brain | 410 | **KB de PRIMEIRA CLASSE** (tesouro: psicologia, metodologia) | `000_KNOWLEDGE_BASE/` preservando estrutura; alimenta RAG/Doc 28 |
| STUDY/04_UI_UX_STUDY + 10_UIUX_STUDIES | 62 | **MERGE + renomear** | resolver dup de nome (refs vs estudos) |
| STUDY/13_AI_FIRST·14_PAPERCLIP·outros | ~70 | **ARQUIVAR** após extrair candidatos | study já consumido pelos gates |
| 99_RESEARCH_LAB | 30 | **MANTER como referência** | insumo backend, marcado |
| 000_UPLOADS | 41 | **SEGREGAR** | uploads brutos → KB ou archive |

## 4. Sequência de lotes

| Lote | Bloco | Risco | Impacto | Pré-req |
|---|---|---|---|---|
| **L1** | Brain → knowledge base | Baixo (não é espelho) | -410 ruído | D1 |
| **L2** | 000_UPGRADE reconciliação | **Alto** (espelho-canônico) | resolve o 2º canônico paralelo | critério de joia (D4) |
| **L3** | DNA_system_vault + SUPERAGENT | Médio | -429 ruído | D2 |
| **L4** | Dups (UI/UX), uploads, study residual | Baixo | limpeza final | — |

Recomendo **L1 primeiro** (quick win visível, baixo risco) e **L2 como o que mais importa** para a futura implementação.

## 5. Protocolo por lote

```txt
1. Checkout lock declarado (escopo = 1 bloco).
2. Identificar joias a promover (→ patch candidate, NÃO aplicar no canônico agora).
3. Mover redundante/segregado para destino + README-pointer no lugar antigo.
4. git commit do lote (rollback disponível).
5. Fan-in Claude + aprovação Founder antes do próximo lote.
```

## 6. Decisões do Founder (RESPONDIDAS 2026-06-02)

- **D1 — Brain → knowledge base de PRIMEIRA CLASSE.** Founder: *"a pasta mais importante do vault são as áreas de expertise, principalmente Psicologia"*. **Não é material a arquivar — é tesouro.** Destino proposto: `000_KNOWLEDGE_BASE/` preservando a estrutura interna (01_AREAS_DE_EXPERTISE/Psicologia, 00_METODOLOGIA etc.), como corpus que alimenta RAG/Doc 28. ⚠️ **Destino exato + mecanismo de move a confirmar** (ver §7 risco de link).
- **D2 — SUPERAGENT_Director_Visual = BENCHMARK EXTERNO, não código nosso.** Founder: é repositório de uma **academia de IA** (vende método de construir agentes Claude p/ campanhas + geração/animação de imagem em lote via Higgsfield). O modelo CLI deles não serve; o CKOS tem runtime/policies/agentes próprios. Interessa só a **técnica/skills/formato**. Tratamento = igual ao paperclip (E5 benchmark): extrair padrões traduzidos, não versionar como nosso. **D2-followup:** já existe estudo de tradução no DNA que precisa migrar — mapear antes de arquivar o material bruto.
- **D3 — Miriam → `000_PROJECTS/`.** ✅ Confirmado. Primeiro projeto de cliente real; lugar próprio, fora do sistema.
- **D4 — Promoção AGRESSIVA.** Founder: promover **tudo que for melhor** que o canônico, mesmo sem necessidade imediata de F1. Implicação: L2/L3 viram **promoção ativa** — comparar cada subsistema espelho vs canônico e puxar o melhor via patch candidate, não só arquivar. (Mais trabalho, canônico mais rico.)

## 7. Riscos

| Risco | Mitigação |
|---|---|
| Mover quebra `[[wikilinks]]` do Obsidian | Mover via Obsidian (atualiza links) OU README-pointer no 99_ARCHIVE; git rollback |
| Promoção apressada reintroduz divergência | patch candidate + fan-in, nunca direto no canônico |
| Arquivar algo ainda útil | git preserva; 99_ARCHIVE é recuperável, não delete |
| node_modules/binários no commit | já cobertos pelo `.gitignore` |

## 8. O que NÃO muda

Canônico 01-28, 000_ROADMAPS (governança), e os gates já fechados. A consolidação **reduz ruído**, não toca a verdade.

---

> **Próximo passo:** Founder responde D1-D4 → executo L1 (Brain) como primeiro lote, com lock e commit.
