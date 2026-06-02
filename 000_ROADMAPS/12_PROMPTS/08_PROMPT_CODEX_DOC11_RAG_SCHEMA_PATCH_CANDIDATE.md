---
title: Prompt Codex — Doc 11 RAG/Knowledge Schema Patch Candidate
file: 08_PROMPT_CODEX_DOC11_RAG_SCHEMA_PATCH_CANDIDATE.md
phase: 000_ROADMAPS
category: prompts
status: ready_for_use — USAR SOMENTE APÓS arquivo 03 (GATE 5) existir
owner: pmo_ckos
created_at: 2026-06-02
session_origin: S-P1-GATE34-CLAUDE-20260602-003
depends_on: 000_ROADMAPS/22_CONSOLIDATION/03_BACKEND_MVP_THIN_SLICE_PLAN.md (GATE 5)
purpose: Produzir o patch CANDIDATE (proposta, não aplicação) de refinamento do schema RAG/knowledge do Doc 11, derivado do Doc 28 §18 e filtrado pelo que o thin-slice realmente usa.
---

> ⚠️ **PRÉ-CONDIÇÃO:** o arquivo 03 (`03_BACKEND_MVP_THIN_SLICE_PLAN.md`) precisa existir.
> Sem ele não há como saber o subconjunto mínimo de schema do MVP — e este patch viraria
> over-engineering. Não rodar antes do GATE 5.

> ⚠️ **ESTE É UM PATCH CANDIDATE, NÃO UMA APLICAÇÃO.** Mexer no Doc 11 é P1 (schema crítico)
> e exige aprovação Founder + Technical. Esta sessão PROPÕE o diff; não edita o Doc 11.

---

## EXECUTION HANDOFF — DOC11-RAG-SCHEMA-PATCH-CANDIDATE — 2026-06-02

### Objetivo
Produzir `000_ROADMAPS/22_CONSOLIDATION/DOC11_RAG_SCHEMA_PATCH_CANDIDATE.md` — a proposta de
diff mínimo ao schema do Doc 11 §14 (Memory + RAG + Embeddings), derivada das sugestões do
Doc 28 §18, **filtrada pelo que o thin-slice (arquivo 03) realmente usa**.

### Modo de execução
`patch_candidate` — propõe diff e racional; NÃO edita o Doc 11. Segue o padrão de
`GATE1_STRUCTURAL_PATCH_PLAN.md` (vive em 22_CONSOLIDATION).

### Ferramenta
Codex (qualquer um livre)

### Inteligência exigida
`high` — cruza 3 fontes e produz diff cirúrgico; decisões estruturais viram ARCHITECTURE_QUESTION.

---

## Contexto crítico (ler com atenção — economiza retrabalho)

**O Doc 11 §14 JÁ TEM as tabelas.** O fan-in do Doc 28 (Claude, 2026-06-02) confirmou que
o Doc 11 §14 já define: `memories`, `memory_write_events`, `documents`, `document_chunks`,
`embeddings`, `rag_queries`, `rag_results`, `retrieval_logs`, `vector_collections` — com
namespace+tenant como pré-condição de busca.

Portanto os "7 patches sugeridos" do Doc 28 §18 são **refinamentos de campos**, NÃO criação
de tabelas. Vários campos sugeridos talvez já existam (ex: `documents.classification`,
`document_chunks.chunk_strategy`, `embeddings.namespace`, `memories.confidence/valid_until`).

**Sua tarefa é o DIFF REAL, não recopiar sugestões.**

---

## Leitura obrigatória (nesta ordem)

1. `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md` §14 (Memory + RAG + Embeddings) — **o que JÁ EXISTE** (campo a campo)
2. `07_EVOLUTION_SYSTEM/28_NOTES_RAG_AND_KNOWLEDGE_ARCHITECTURE.md` §18 (patches sugeridos) + §19 (10 AQs)
3. `000_ROADMAPS/22_CONSOLIDATION/03_BACKEND_MVP_THIN_SLICE_PLAN.md` — **o que o MVP realmente usa** (seções de modelo de dados e Evidência→Memória)
4. `01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md` §5.4-5.5 — para não contradizer a hierarquia de memória

---

## Regra do diff mínimo

Um campo só entra na proposta se passar nos TRÊS filtros:

```txt
(Doc 28 §18 sugere)  ∩  (arquivo 03 indica que o MVP usa)  ∩  (NÃO existe hoje no Doc 11 §14)
```

- Campo que o Doc 28 sugere mas o MVP não usa → registrar como "pós-P0 / backlog", não no diff ativo.
- Campo que o Doc 28 sugere mas já existe no Doc 11 → marcar "já existe, sem ação".
- Campo estrutural ambíguo (ex: materialização de notas) → ARCHITECTURE_QUESTION, não decidir sozinho.

---

## Estrutura do arquivo candidate

```
# 1. Propósito e escopo (proposta, não aplicação)
# 2. Estado atual do Doc 11 §14 (inventário do que já existe)
   (tabela: tabela → campos atuais — provando que NÃO se recria nada)
# 3. Diff mínimo proposto (só o que passou nos 3 filtros)
   (tabela: tabela alvo | campo novo | tipo | por que o MVP precisa | fonte Doc 28 §X)
# 4. Sugestões pós-P0 (Doc 28 pede, MVP não usa ainda — backlog)
# 5. Decisões estruturais que bloqueiam o patch (ARCHITECTURE_QUESTIONS)
   (AQ-01 materialização de notas: documents.kind=note vs tabela dedicada vs object_registry —
    recomendar a mais barata compatível com o que já existe, mas marcar como decisão Founder/Technical)
# 6. AQs do Doc 28 que afetam schema e precisam decisão antes de aplicar
   (AQ-02 embedding model/dims; AQ-03 chunk sizes; AQ-04 multimodal P0/pós-P0; AQ-06 re-embed versioning; AQ-07 negative memory)
# 7. Classificação de risco e fluxo de aprovação
   (P1 schema crítico → Founder + Technical; rollback = reverter o diff de campos)
# 8. Plano de aplicação (a sessão canonical_patch futura)
   (que arquivo, que versão bump 1.2.0 → 1.3.0, que changelog)
```

---

## Arquivos permitidos

- `000_ROADMAPS/22_CONSOLIDATION/DOC11_RAG_SCHEMA_PATCH_CANDIDATE.md` — **CRIAR**
- `000_ROADMAPS/SESSION_REGISTRY.md` — registrar sessão + lock + release

## Arquivos proibidos (não tocar)

- `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md` — **NÃO EDITAR** (é só proposta; aplicação é outra sessão com aprovação Founder)
- `07_EVOLUTION_SYSTEM/28_...` — não editar
- Qualquer doc canônico 01-28
- ARCHITECTURE_PATCH_REPORT.md, 00_SYSTEM_GOVERNANCE/, CKOS_EXPANSION_KANBAN.md, CKOS_MASTER_EXPANSION_ROADMAP.md
- Qualquer migration/DDL/código real

## Não fazer

- Não editar o Doc 11 (proposta apenas)
- Não escrever `CREATE TABLE` / `ALTER TABLE` reais — descrição textual de campos
- Não recriar tabelas que já existem
- Não resolver AQ estrutural sozinho (recomendar + marcar para Founder/Technical)
- Não declarar o patch aprovado — só o Founder aprova P1

---

## Declaração no SESSION_REGISTRY

```
session_id: S-P1-DOC11-CODEX-20260602-001  (ou data real)
task_id: DOC11_RAG_SCHEMA_PATCH_CANDIDATE_20260602
session_type: patch_candidate
agent: codex
scope: 000_ROADMAPS/22_CONSOLIDATION/DOC11_RAG_SCHEMA_PATCH_CANDIDATE.md (CRIAR);
       000_ROADMAPS/SESSION_REGISTRY.md
status: active → released
started_at: [data real]
expected_outputs: patch candidate do Doc 11 (diff mínimo + AQs); Doc 11 NÃO editado
estimated_cost: low
intelligence_level: high
```

---

## Output esperado (CHECKOUT RELEASE)

```
FILES_CREATED: DOC11_RAG_SCHEMA_PATCH_CANDIDATE.md
FILES_CHANGED: SESSION_REGISTRY.md
SUMMARY: [quantos campos no diff ativo vs pós-P0 vs já-existem]
DIFF_SIZE: [N campos novos propostos, em M tabelas]
BLOCKING_AQS: [AQs estruturais que travam a aplicação]
RISKS: [P1 — schema crítico]
NEXT_STEP: "Fan-in Claude → aprovação Founder/Technical → sessão canonical_patch aplica no Doc 11 v1.3.0"
```

---

## Nota de fan-in (Claude, depois)

- [ ] §2 prova o inventário atual (nada recriado)?
- [ ] Diff §3 passou nos 3 filtros (Doc 28 ∩ MVP ∩ não-existe)?
- [ ] Campos pós-P0 separados do diff ativo?
- [ ] AQ estruturais marcadas para Founder, não decididas sozinhas?
- [ ] Doc 11 NÃO foi editado?
- [ ] Risco P1 declarado + rollback?

Se ✅ → vai para aprovação Founder/Technical do schema. Só depois abre a sessão `canonical_patch`.
