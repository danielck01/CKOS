---
title: Prompt Codex — GATE 3 · Criação Doc 28
file: 06_PROMPT_CODEX_GATE3_DOC28_CREATION.md
phase: 000_ROADMAPS
category: prompts
status: ready_for_use — USAR SOMENTE APÓS GATE 1 ✅
owner: pmo_ckos
created_at: 2026-06-02
session_origin: S-P1-GATE1-CLAUDE-20260602-002
depends_on: GATE 1 liberado (patches A+B+C aplicados pelo Codex)
purpose: Prompt pronto para sessão canonical_patch Codex criar Doc 28 Notes/RAG/Knowledge Architecture.
---

> ⚠️ **PRÉ-CONDIÇÃO:** Este prompt só roda após GATE 1 ser declarado ✅ no kanban
> pelo fan-in de Claude. Não abrir antes disso.

---

## EXECUTION HANDOFF — GATE3-DOC28-CREATION — 2026-06-02

### Objetivo
Criar `07_EVOLUTION_SYSTEM/28_NOTES_RAG_AND_KNOWLEDGE_ARCHITECTURE.md` — o documento canônico que define como o CKOS estrutura, ingere, indexa e recupera conhecimento (notas, documentos, embeddings, RAG). Este doc é a Lacuna Real L-01 do mapa de consolidação.

### Modo de execução
`canonical_patch` — documentação arquitetural apenas. Sem código, sem backend, sem UI, sem migrations reais. Schema suggestions vão em seção "Patches sugeridos ao Doc 11".

### Ferramenta
Codex

### Inteligência exigida
`highest` — decisões arquiteturais de longo prazo; qualquer ambiguidade deve virar `ARCHITECTURE_QUESTION`, não suposição.

---

## Leitura obrigatória ANTES de escrever (ler nesta ordem)

**Para entender o que NÃO duplicar:**
1. `01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md` — Doc 05 cobre memory assembly e context packet em runtime. Doc 28 NÃO recria isso.
2. `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL.md` §9 (Evidence Object Model) — Doc 18 cobre coleta e scoring de evidências. Doc 28 cobre como evidências são indexadas no RAG privado após aprovadas.

**Para entender o que Doc 28 DEVE cobrir (fontes primárias):**
3. `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/` — ler TODOS os 14 arquivos. Este é o core técnico do Doc 28.
4. `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/04_NOTES_AS_OPERATIONAL_MEMORY_STUDY.md`
5. `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/12_RAG_METADATA_AND_VECTOR_CATEGORY_STUDY.md`
6. `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/18_AI_FIRST_PROJECT_NOTE_SYSTEM_AND_RAG_GOVERNANCE_STUDY.md`

**Para entender o formato e padrão de doc canônico esperado:**
7. `07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md` — doc mais recente no mesmo folder; siga o estilo de frontmatter e estrutura de seções.

**Para checar schema já existente antes de sugerir patches:**
8. `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md` — tabelas que já existem (documents, embeddings, memory_updates etc.)

---

## Arquivos permitidos para modificação

- `07_EVOLUTION_SYSTEM/28_NOTES_RAG_AND_KNOWLEDGE_ARCHITECTURE.md` — **CRIAR** (não existe)
- `000_ROADMAPS/SESSION_REGISTRY.md` — registrar sessão + lock + release
- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md` — adicionar Doc 28 à lista canônica
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md` — adicionar dependências do Doc 28
- `ARCHITECTURE_PATCH_REPORT.md` — registrar criação do Doc 28

## Arquivos proibidos (não tocar)

- Qualquer doc canônico 01-27 (conteúdo) — apenas referência/leitura
- `01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md` — não alterar
- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL.md` — não alterar
- `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md` — não alterar (sugestões de patch vão dentro do Doc 28, não nele)
- Qualquer arquivo de UI, backend real, API, migrations, runtime workers
- `000_STUDY_NOTES/` — apenas leitura

---

## Frontmatter obrigatório do Doc 28

```yaml
---
title: 28 — Notes, RAG and Knowledge Architecture
file: 28_NOTES_RAG_AND_KNOWLEDGE_ARCHITECTURE.md
system_id: notes_rag_knowledge_architecture
phase: 07_EVOLUTION_SYSTEM
category: knowledge_system
version: 1.0.0
status: draft
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - founder
  - technical
  - metacognik
approval_required:
  - founder
  - technical
  - metacognik
inputs:
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - 03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - 03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - 05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL.md
  - ARCHITECTURE_PATCH_REPORT.md
outputs:
  - note_object_model
  - knowledge_asset_taxonomy
  - ingestion_pipeline_spec
  - embedding_strategy
  - chunking_policy
  - rag_query_policy
  - retrieval_quality_framework
  - rag_cost_policy
  - knowledge_lifecycle_spec
  - doc_11_patch_suggestions
related_notes:
  - ../01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - ../05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL.md
  - 26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md
  - 27_AI_FIRST_WORK_ORDERS_AND_MULTI_SESSION_ORCHESTRATION_ARCHITECTURE.md
  - 25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md
tags:
  - knowledge
  - rag
  - notes
  - embeddings
  - ingestion
  - chunking
  - retrieval
  - governance
---
```

---

## Estrutura de seções obrigatória

O Doc 28 deve ter no mínimo estas seções — expanda onde o material das fontes justificar:

```
# 1. Propósito
# 2. O que é este documento / O que NÃO é
   (Incluir tabela explícita: o que Doc 28 cobre vs o que fica em Doc 05, Doc 18, Doc 11)
# 3. Princípio central
# 4. Note como objeto CKOS
   ## 4.1 Taxonomia de tipos de nota
   ## 4.2 Schema de metadados obrigatórios
   ## 4.3 Memory role de cada tipo
   ## 4.4 Lifecycle: RAW → STUDY → CANONICAL
   ## 4.5 Proveniência e confiança
# 5. Knowledge Asset Types
# 6. Pipeline de Ingestão
   (upload → parse → chunk → embed → index → link)
# 7. Namespace e Isolamento de Tenant
# 8. Estratégia de Embedding
   ## 8.1 Text embedding
   ## 8.2 Multimodal embedding (imagem, áudio, PDF)
   ## 8.3 Creative DNA indexing
   ## 8.4 Evidence indexing
   ## 8.5 Memory indexing
   ## 8.6 Visual asset indexing
# 9. Chunking Policy
# 10. RAG Query Policy
# 11. Retrieval Quality Scoring
# 12. Cost Policy
# 13. Conexão com objetos do Runtime
   (nodes, evidence_items, memory, DNA, artifacts, Work Orders)
# 14. Security Rules
   (namespace como pré-condição nunca pós-filtro; PII; classificação)
# 15. Testing Rules
# 16. Failure Modes
# 17. MVP P0 Scope
   (o que do Doc 28 vai para o thin-slice do GATE 5)
# 18. Patches sugeridos ao Doc 11
   (tabelas/campos necessários que ainda não existem em 11 — NÃO editar o 11, só registrar)
# 19. ARCHITECTURE_QUESTIONS em aberto
   (ambiguidades que precisam de decisão Founder/Technical antes de implementar)
# 20. Related Notes
## Patch 1.0.0 — Criação do documento
```

---

## Constraints críticos

**O que Doc 28 faz que Doc 05 NÃO faz:**
- Define como documentos e notas são ingeridos, chunkeados e embedados
- Define a política de qualidade de retrieval (o que é "boa" recuperação)
- Define custo de operações RAG e quando usar
- Define quais tipos de conteúdo são indexáveis e como
- Define o ciclo de vida de uma nota: quando promove, quando expira, quando arquiva
- Define proveniência e confiança de notas (study vs canônico vs unverified)

**O que Doc 28 NÃO faz (deixar para outros docs):**
- Não define como o runtime monta o context packet → Doc 05
- Não define como evidências são coletadas → Doc 18
- Não define schema de banco de dados (só sugere patches) → Doc 11
- Não define conectores externos → Doc 26
- Não implementa código → nenhum doc

**Regras de escrita:**
- Toda afirmação técnica tem referência de fonte (doc + seção, ou arquivo DNA/14_RAG + arquivo)
- Ambiguidades viram `ARCHITECTURE_QUESTION` — nunca invenção
- Schema suggestions em §18 não têm `CREATE TABLE` real — são especificações textuais
- Namespace como pré-condição (nunca pós-filtro) é regra não-negociável — derivada de Doc 12 e Doc 18 §17 R1

---

## Não fazer

- Não duplicar o Doc 05 (memory loop, context assembly)
- Não duplicar o Doc 18 (research pipeline, source tiers, confidence scoring de evidências)
- Não criar tabelas reais no Doc 11
- Não implementar qualquer código
- Não criar novos docs além do Doc 28
- Não abrir doc 29+ (gated por GATE 1 — verificar se liberado)
- Não tomar decisões de produto silenciosas (registrar como ARCHITECTURE_QUESTION)

---

## Como declarar a sessão no SESSION_REGISTRY

```
session_id: S-P1-GATE3-CODEX-20260602-001  (ou data real de execução)
task_id: GATE3_DOC28_NOTES_RAG_KNOWLEDGE_CREATION
session_type: canonical_patch
agent: codex
scope: 07_EVOLUTION_SYSTEM/28_NOTES_RAG_AND_KNOWLEDGE_ARCHITECTURE.md (CRIAR);
       ARCHITECTURE_PATCH_REPORT.md; 00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md;
       00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md; SESSION_REGISTRY.md
status: active → released_with_required_external_audit
started_at: [data real]
expected_outputs: Doc 28 criado; maps atualizados; patch report registrado
estimated_cost: medium (doc grande, muitas fontes para ler)
intelligence_level: highest
```

---

## Output esperado do Codex

CHECKOUT RELEASE com:
```
FILES_CREATED: [28_NOTES_RAG_AND_KNOWLEDGE_ARCHITECTURE.md; demais se aplicável]
FILES_CHANGED: [ARCHITECTURE_PATCH_REPORT.md; 00_MASTER_MAP.md; 00_DEPENDENCY_MAP.md; SESSION_REGISTRY.md]
SUMMARY: [o que o doc cobre em 5 linhas]
ARCHITECTURE_QUESTIONS: [lista de ambiguidades que precisam de decisão]
DOC_11_PATCH_SUGGESTIONS: [tabelas/campos sugeridos]
RISKS: [riscos da criação]
NEXT_STEP: "Fan-in Claude: confirmar integridade do Doc 28 e declarar GATE 3 ✅"
```

---

## Nota de fan-in (para o Claude após o Codex terminar)

Quando o Codex entregar o release do Doc 28, o Claude deve verificar:

- [ ] As seções obrigatórias (1-20) estão todas presentes?
- [ ] Doc 28 não duplica Doc 05 nem Doc 18?
- [ ] Namespace como pré-condição (não pós-filtro) está explícito?
- [ ] ARCHITECTURE_QUESTIONS registradas (não resolvidas silenciosamente)?
- [ ] Nenhum schema real foi criado em Doc 11?
- [ ] Frontmatter completo e coerente?
- [ ] ARCHITECTURE_PATCH_REPORT registrado?
- [ ] 00_MASTER_MAP.md atualizado com Doc 28?
- [ ] 00_DEPENDENCY_MAP.md reflete dependências do Doc 28?

Se todos ✅ → declarar GATE 3 ✅ e desbloquear docs 29+.
