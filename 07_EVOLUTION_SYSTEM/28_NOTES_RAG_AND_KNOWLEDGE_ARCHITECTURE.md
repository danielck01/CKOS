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

# 1. Propósito

Este documento define como o CKOS estrutura, ingere, classifica, chunka, embeda, indexa e recupera conhecimento privado: notas, documentos, memórias, evidências aprovadas, artifacts, Creative DNA e assets visuais.

Doc 28 existe porque a arquitetura de memória do Doc 05 define a política de contexto e context packet, enquanto o Doc 11 define persistência base e o Doc 18 define pesquisa/evidência. Nenhum deles, sozinho, define a governança completa de ingestão, chunking, embeddings, retrieval quality, custo e lifecycle de notas como objetos de conhecimento. Fonte: Doc 05 §5.3-§5.8; Doc 11 §13-§15 e §25; Doc 18 §3, §6 e §9; Layer 13 Note 04; Layer 13 Note 12; Layer 13 Note 18.

Este documento é documentação arquitetural. Ele não autoriza backend, API, migrations, workers, vector store real, jobs de sync, UI ou agentes reais. Qualquer necessidade de schema entra em §18 como patch sugerido ao Doc 11. Fonte: handoff GATE3-DOC28-CREATION; Doc 26 §2-§4 como padrão de boundary documental.

---

# 2. O que é este documento / O que NÃO é

## 2.1 O que este documento é

| Área | Doc 28 cobre | Fontes |
|---|---|---|
| Notas como objeto CKOS | Tipos de nota, memory role, metadata, lifecycle RAW → STUDY → CANONICAL, confiança e proveniência | Layer 13 Note 04; Layer 13 Note 18 |
| Knowledge assets | Taxonomia de documentos, memórias, evidências, artifacts, Creative DNA e visual assets indexáveis | DNA/14_RAG_VECTOR_SYSTEM README; Doc 11 §14-§15 |
| Ingestão | Pipeline upload → parse → classify → chunk → embed → index → link → audit | Doc 11 §14; Doc 18 §6; DNA/14_RAG `embedding_pipeline.md` |
| Chunking | Política de chunk por tipo de conteúdo, preservando lineage, headings, metadata e lifecycle | DNA/14_RAG `document_chunking_policy.md`; Doc 11 §14 |
| Embeddings | Estratégia textual, multimodal, Creative DNA, evidence, memory e visual asset indexing | DNA/14_RAG thematic files; Doc 05 §5.4 |
| Retrieval | Query policy, namespace, permission precondition, ranking, quality scoring, cost and logs | Doc 05 §5.3; Doc 11 §13-§14; Doc 12 §5.6.2; Doc 13 §9 |
| Patches sugeridos | Lacunas textuais a serem avaliadas para Doc 11 sem DDL real | Doc 11 §14; Layer 13 Note 12 |

## 2.2 O que este documento NÃO é

| Tema | Dono correto | Limite |
|---|---|---|
| Runtime monta context packet | Doc 05 + Doc 10 | Doc 28 define fontes/indexação; não monta prompt final. |
| Pesquisa coleta fontes e pontua evidência | Doc 18 | Doc 28 só define como evidências aprovadas entram no RAG privado. |
| Schema real de banco | Doc 11 | Doc 28 sugere patches; não cria migrations nem DDL. |
| Segurança/RLS/PII | Doc 12 | Doc 28 aplica as regras ao RAG; não redefine a política. |
| Evals/custo observability | Doc 13 | Doc 28 define métricas esperadas para RAG; thresholds canônicos vivem em eval/cost registries. |
| Conectores externos | Doc 26 | Doc 28 não escolhe providers, collectors, MCP ou APIs. |
| Work Orders e fan-in/fan-out | Doc 27 | Doc 28 fornece knowledge sources para Work Orders, sem reger orquestração. |

---

# 3. Princípio central

> Conhecimento recuperado pelo RAG é contexto governado, não verdade automática.

O CKOS deve recuperar conhecimento com namespace, permissão, provenance, confidence, freshness e cost guard antes de usá-lo em decisões, Work Orders ou outputs. Embeddings ajudam a localizar contexto, mas não substituem dados estruturados, decisões aprovadas, evidence IDs ou audit logs. Fonte: Doc 05 §5.4-§5.5; Doc 18 §3; Doc 11 §14; Doc 12 §5.6.2; Doc 13 §9.

Regra dura:

```txt
namespace + permission + classification + provenance
  -> retrieve candidates
  -> score and audit
  -> summarize with source refs
  -> context packet owner decides inclusion
```

Namespace nunca é pós-filtro. Busca vetorial sem namespace explícito é rejeitada antes de consultar o índice. Fonte: Doc 12 §5.6.2; Doc 18 §3 princípio 4; Doc 11 §25.

---

# 4. Note como objeto CKOS

Uma nota CKOS é uma unidade de memória operacional, decisão, contexto, evidência, aprendizado ou handoff. Ela não é apenas um arquivo Markdown. Fonte: Layer 13 Note 04 Core Rule; Layer 13 Note 18 §1-§3.

## 4.1 Taxonomia de tipos de nota

| Tipo | Uso canônico | Trust inicial | Fonte |
|---|---|---:|---|
| `canonical_note` | Source of truth aprovado | high | Layer 13 Note 04 |
| `study_note` | Estudo interpretado, não aprovado como canon | medium/low | Layer 13 Note 04; Note 18 §11 |
| `roadmap_note` | Planejamento e prioridade, sem autoridade arquitetural sozinho | medium | Layer 13 Note 04 |
| `task_note` | Contexto de execução e trace de tarefa | medium | Layer 13 Note 04; Note 18 §10 |
| `work_order_note` | Scope, risk, ROI, approval e release de Work Order | medium | Layer 13 Note 18 §10 |
| `decision_note` | Registro de decisão aprovada ou pendente | high quando aprovado | Layer 13 Note 04 |
| `memory_note` | Sumário ativo de memória curta/média/longa | variável | Doc 05 §5.1; Layer 13 Note 04 |
| `learning_note` | Lição validada por resultado | medium/high após revisão | Layer 13 Note 04; Note 18 §13 |
| `feedback_note` | Feedback classificado para ação/aprendizado | medium | Layer 13 Note 04 |
| `prompt_note` | Padrão de prompt reutilizável candidato | low/medium | Layer 13 Note 04 |
| `risk_note` | Risco governamental, técnico ou operacional | medium/high | Layer 13 Note 04 |
| `roi_note` | Contexto de valor, custo e benefício | medium | Layer 13 Note 04; Note 18 §13 |
| `handoff_note` | Transferência de contexto entre sessões/agentes | medium | Layer 13 Note 04 |
| `patch_candidate_note` | Candidato para patch canônico futuro | low/medium até aprovação | Layer 13 Note 04 |
| `source_manifest_note` | Inventário de fonte/proveniência | medium | Layer 13 Note 04 |
| `release_note` | Evidência de entrega e validação | high quando auditada | Layer 13 Note 18 §10 |

## 4.2 Schema de metadados obrigatórios

Todo objeto-nota indexável deve carregar metadata suficiente para retrieval seguro. Isto é especificação arquitetural; a materialização física depende de patch futuro no Doc 11. Fonte: Layer 13 Note 12; Layer 13 Note 18 §12.

Campos obrigatórios conceituais:

```yaml
note_id:
note_type:
layer:
status:
canonical_status:
source_type:
source_refs:
related_intent:
related_questions:
related_tasks:
related_work_orders:
related_decisions:
related_projects:
confidence:
provenance_status:
risk_level:
roi_scope:
memory_type:
rag_priority:
data_classification:
permission_level:
valid_until:
review_required:
owner:
responsible_agent:
```

Campos mínimos já aparecem como candidatos em Layer 13 Note 12 e Note 18. `data_classification` e `permission_level` são adicionados por exigência do Doc 12 §5.14 e Doc 11 §14.

## 4.3 Memory role de cada tipo

| Memory role | Exemplos | Política |
|---|---|---|
| short_term | lock atual, blocker temporário, estado de sessão | Expira rápido; não vira long memory sem review. |
| mid_term | briefing vivo, hipóteses, task notes, Work Orders pendentes | Requer freshness e provenance em retrieval. |
| long_term | decisões aprovadas, releases finais, learning validado, canon | Requer aprovação/auditoria antes de escrita. |
| negative_memory | outputs rejeitados úteis como anti-padrão | Somente se QA/Metacognik marcar valor preventivo. |

Fonte: Doc 05 §5.1; Layer 13 Note 18 §11 e §15; DNA/14_RAG README §14-§17.

## 4.4 Lifecycle: RAW → STUDY → CANONICAL

```txt
RAW upload / transient note
  -> classified note
  -> study note with provenance
  -> patch candidate or decision candidate
  -> reviewed canonical note / archived note / negative memory
```

Regras:

1. RAW nunca é fonte de verdade.
2. STUDY é contexto, não autoridade.
3. CANONICAL exige approval conforme Doc 20 e governança do arquivo-alvo.
4. Nota rejeitada pode ser arquivada ou virar negative memory se prevenir erro recorrente.
5. Nota obsoleta deve receber `valid_until`, `archived_at` ou freshness warning.

Fonte: Layer 13 Note 04; Layer 13 Note 12 Trust Hierarchy; Layer 13 Note 18 §14-§15; Doc 05 §5.8.

## 4.5 Proveniência e confiança

Trust hierarchy aplicada a notas:

```txt
canonical docs
  > approved decisions
  > structured database records
  > project memory
  > study notes
  > raw uploads
  > unverified AI outputs
```

Conflitos de nota são encaminhados para Metacognik. RAG não resolve conflito sozinho; ele apenas expõe candidatos com score, fonte e freshness. Fonte: Doc 05 §5.5; Layer 13 Note 12; Doc 13 §9.

---

# 5. Knowledge Asset Types

| Asset | Indexável? | Método principal | Restrições |
|---|---:|---|---|
| Canonical docs | sim | chunk por heading + embedding textual | Alta prioridade, mas versionar e citar seção. |
| Study notes | sim | chunk por heading + metadata de confiança | Recuperar como contexto, não verdade. |
| Raw uploads | sim após classificação | parser + chunk + provenance | Baixa confiança até validação. |
| Evidence items aprovados | sim | evidence indexing com `evidence_id` | Só após pipeline do Doc 18. |
| Memories | sim | memory indexing por scope e freshness | Permission level governa retrieval. |
| Decisions | sim, preferir estruturado | structured lookup antes de embedding | Decisão aprovada vence similaridade. |
| Artifacts | sim | artifact metadata + text extraction | Linkar versão/checksum. |
| Creative DNA | sim | creative DNA indexing + tags semânticas | Não confundir referência com regra de marca. |
| Visual assets | sim | caption/OCR/visual descriptors + optional vector | PII/rights/classification antes de indexar. |
| Audio/video | sim, pós-transcrição | transcript chunks + metadata temporal | Multimodal P0 depende de decisão. |
| Feedback | sim quando classificado | feedback note + source refs | Feedback isolado não vira decisão. |
| Source manifests | sim | metadata retrieval | Serve para provenance, não conteúdo final. |

Fonte: Doc 11 §14, §15, §17; Doc 18 §9; DNA/14_RAG `creative_dna_indexing.md`, `evidence_indexing.md`, `memory_indexing.md`, `visual_asset_indexing.md`, `image_to_text_retrieval.md`, `text_to_image_retrieval.md`; Layer 13 Note 04.

---

# 6. Pipeline de Ingestão

Pipeline canônico documental:

```txt
upload/import
  -> source registration
  -> parse/extract
  -> classify data and permissions
  -> normalize metadata
  -> chunk
  -> embed
  -> index by namespace
  -> link to runtime objects
  -> eval retrieval readiness
  -> audit and cost attribution
```

| Etapa | Regra | Fonte |
|---|---|---|
| source registration | Captura source refs, owner, tenant/workspace/project, lineage e checksum quando aplicável | Doc 11 §14; Doc 18 §9 |
| parse/extract | Extrai texto, metadata, headings, OCR/transcript quando autorizado | DNA/14_RAG `embedding_pipeline.md`; `image_to_text_retrieval.md` |
| classify | Define `data_classification`, PII e permission level antes de embedding | Doc 12 §5.14 |
| normalize | Converte para asset/note/evidence/memory com metadata mínima | Layer 13 Note 12; Note 18 §12 |
| chunk | Preserva heading path, source ref, lifecycle e content hash | Doc 11 §14; DNA/14_RAG `document_chunking_policy.md` |
| embed | Usa model/dims/model_id definidos por registry futuro; embeddings não são truth | Doc 05 §5.4; Doc 11 §14 |
| index | Usa namespace como partição/precondição | Doc 12 §5.6.2; Doc 11 §25 |
| link | Conecta a nodes, decisions, evidence, artifacts, Work Orders quando houver relação explícita | Doc 11 §5, §10, §15; Doc 27 |
| eval | Mede relevance, freshness, tenant isolation e context precision | Doc 13 §9 |
| audit/cost | Registra retrieval/embedding cost e audit trail | Doc 13 §14; Doc 11 §16.1 |

Nenhuma ingestão de conteúdo sensível ocorre sem classificação e policy. Fonte: Doc 12 §5.14.

---

# 7. Namespace e Isolamento de Tenant

Namespace é pré-condição de busca, não filtro posterior:

```txt
namespace = org_id + workspace_id + project_id + optional_collection
```

Regras:

1. `rag_retriever` recusa query sem namespace explícito.
2. Vector collection é particionada por namespace de tenant/projeto.
3. Permission level e data classification são avaliados antes de retornar candidatos.
4. Cross-project retrieval dentro do mesmo tenant exige agent scope explícito e audit log.
5. Qualquer tentativa cross-tenant é P0/P1 conforme Doc 12 e Doc 13.

Fonte: Doc 12 §5.6.2, §5.14 e §13; Doc 11 §25; Doc 18 §3 princípio 4; Doc 13 §9 Failure Modes.

---

# 8. Estratégia de Embedding

Embedding é índice auxiliar de recuperação, não fonte de autoridade. Fonte: Doc 05 §5.4.

## 8.1 Text embedding

Text embedding cobre canonical docs, study notes, research packs, evidence summaries, memories, decisions textuais, artifacts parseados e implementation briefs. Cada embedding precisa carregar `model_id`, namespace, source id, chunk id/memory id, language, content hash, confidence/provenance e created_at. Fonte: Doc 11 §14; Layer 13 Note 12.

## 8.2 Multimodal embedding (imagem, áudio, PDF)

Multimodal retrieval deve começar por extração textual controlada: OCR, captions, transcript, PDF text, visual descriptors e metadata. Embedding multimodal direto é candidato futuro, não requisito MVP P0, até definição de model/dims/custo/privacidade. Fonte: DNA/14_RAG `multimodal_embedding_strategy.md`, `image_to_text_retrieval.md`, `text_to_image_retrieval.md`; Doc 12 §5.14; Doc 13 §14.

## 8.3 Creative DNA indexing

Creative DNA é indexado como referência semântica de linguagem visual, tom, padrões, restrições e exemplos. Uma referência visual recuperada não vira regra de marca sem aprovação; ela informa direção criativa e deve preservar source/rights/provenance. Fonte: DNA/14_RAG `creative_dna_indexing.md`; Doc 18 §3 source-aware e citation-required.

## 8.4 Evidence indexing

Evidence indexing só acontece após o pipeline do Doc 18 produzir `evidence_items` aprovados ou verificáveis. Retrieval deve retornar `evidence_id`, claim, confidence, freshness e source tier, não apenas texto similar. Fonte: Doc 18 §3, §6, §9; DNA/14_RAG `evidence_indexing.md`.

## 8.5 Memory indexing

Memories são indexadas com scope (`short_term`, `mid_term`, `long_term`), freshness, reliability, permission level e valid_until. Long memory exige review antes de escrita e retrieval de memória expirada deve gerar warning. Fonte: Doc 05 §5.1, §5.6, §5.8; Doc 11 §14; Doc 13 §16 quality gate before memory write.

## 8.6 Visual asset indexing

Visual assets usam metadata, caption, OCR, tags, rights, checksum, source lineage e optional visual descriptors. Se houver PII, faces, documentos pessoais, conteúdo de cliente ou marca sob NDA, a indexação fica bloqueada até policy explícita. Fonte: DNA/14_RAG `visual_asset_indexing.md`; Doc 12 §5.14.

---

# 9. Chunking Policy

Chunking deve preservar significado, lineage e auditabilidade.

| Conteúdo | Estratégia padrão | Metadata mínima | Fonte |
|---|---|---|---|
| Markdown/canonical docs | heading-aware semantic chunks | heading path, section, file, version, source line refs se disponíveis | Doc 11 §14; DNA `document_chunking_policy.md` |
| Study notes | heading-aware chunks + trust metadata | confidence, provenance, canonical_status, memory_type | Layer 13 Note 12 |
| Raw uploads | parser-specific chunks | source_ref, checksum, page/time range, data_classification | Doc 11 §14; Doc 12 §5.14 |
| Evidence items | claim-level chunks | evidence_id, confidence, source tier, freshness | Doc 18 §9 |
| Memories | memory-object chunks | memory_id, scope, valid_until, permission_level | Doc 05 §5.6; Doc 11 §14 |
| Visual/audio/video | transcript/OCR/descriptor chunks | asset_id, timestamp/region, rights, classification | DNA/14_RAG visual and multimodal files |

Regras:

1. Chunk não pode perder source lineage.
2. Chunk não pode misturar tenants, projects ou permission levels.
3. Chunk de estudo deve carregar que é estudo.
4. Chunk de evidência deve carregar `evidence_id`.
5. Re-chunking cria nova versão; não sobrescreve silenciosamente.
6. Tamanho numérico de chunk é decisão de implementação futura e está em `ARCHITECTURE_QUESTION AQ-03`.

Fonte: Doc 11 §14; Layer 13 Note 12; Doc 18 §9.

---

# 10. RAG Query Policy

Fluxo de query:

```txt
intent
  -> classify need
  -> choose retrieval scopes
  -> enforce namespace and permission
  -> retrieve candidates
  -> rank by relevance + trust + freshness
  -> summarize with source refs
  -> log retrieval
  -> hand off to context packet owner
```

Regras:

1. Private RAG é prioritário quando fresco, relevante e autorizado. Fonte: Doc 18 §3 princípio 12; Doc 18 §6.
2. Dados estruturados e decisões aprovadas vencem embeddings em conflito. Fonte: Doc 05 §5.4-§5.5.
3. Study notes são recuperadas como contexto, não autoridade. Fonte: Layer 13 Note 12; Note 18 §11.
4. Se top results forem stale, low confidence ou unverified, o agente deve reduzir confidence ou pedir melhor contexto. Fonte: Doc 05 §12; Doc 13 §9.
5. Toda síntese que use retrieval deve carregar source refs/evidence refs. Fonte: Doc 18 §3 citation-required; Doc 05 §5.3.

Doc 28 define esta política de retrieval. A montagem final do context packet permanece com Doc 05/Doc 10. Fonte: Doc 05 §5.7.

---

# 11. Retrieval Quality Scoring

Score composto recomendado:

```txt
retrieval_quality =
  relevance_score
  + source_reliability
  + freshness
  + permission_safety
  + provenance_confidence
  + context_precision
  - contradiction_penalty
  - stale_penalty
```

Métricas mínimas:

| Métrica | Uso | Fonte |
|---|---|---|
| Retrieval relevance | top result deve ser relevante para a intent; Doc 13 usa meta >= 0.70 para top-1 | Doc 13 §9 e §28 |
| Retrieval freshness | memória/documento expirado reduz score ou bloqueia decisão | Doc 05 §5.8; Doc 13 §9 |
| Tenant isolation | retrieval com namespace errado é bloqueio/incidente | Doc 12 §5.6.2; Doc 13 §9 |
| Context precision | evita jogar pastas inteiras no prompt | Doc 05 §5.3; Doc 13 §9 |
| Context recall | garante que informação necessária não ficou de fora | Doc 13 §9 |
| Evidence coverage | outputs de risco médio+ devem citar evidência; Doc 13 usa meta >= 80% | Doc 13 §6, §28 |
| Contradiction risk | conflito aciona Metacognik | Doc 05 §5.5; Doc 18 §6 |

Se retrieval quality estiver abaixo do threshold aplicável, o sistema deve: reduzir confidence, pedir mais contexto, acionar Metacognik ou bloquear uso em decisão de alto risco. Fonte: Doc 13 §16 e §27.

---

# 12. Cost Policy

RAG tem custo em três momentos: ingestão, embedding/re-embedding e retrieval/summarization. Todo custo deve ser atribuível a run, project, workflow, agent ou knowledge asset. Fonte: Doc 13 §4, §14; DNA/14_RAG `rag_cost_policy.md`.

Regras:

1. Não embedar conteúdo não classificado ou descartável.
2. Não re-embedar conteúdo sem mudança de content hash, model policy ou chunking policy.
3. Multimodal embedding exige cost estimate e privacy check antes de execução.
4. Query ampla em muitas coleções exige budget/policy; se custo estimado passa soft limit, precisa approval.
5. Retrieval deve preferir dados internos frescos antes de collectors externos quando ambos servem à intent.
6. Cost per useful retrieval deve alimentar eval/learning loop.

Fonte: Doc 13 §14 cost guard; Doc 18 §3 policy-controlled; Doc 26 connector cost boundaries.

---

# 13. Conexão com objetos do Runtime

| Objeto | Como Doc 28 se conecta | Dono primário |
|---|---|---|
| `nodes` | Knowledge assets podem evidenciar, bloquear, apoiar ou derivar nodes via object relationships | Doc 11 §5, §10 |
| `evidence_items` | Evidência aprovada é indexável e recuperável por `evidence_id` | Doc 18 §9; Doc 11 §15 |
| `memories` | Note/memory retrieval usa scope, freshness e permission level | Doc 05 §5.6; Doc 11 §14 |
| `documents` | Uploads, notes e docs parseados entram como documents/chunks | Doc 11 §14 |
| `artifacts` | Artifact versions podem ser parseadas e linkadas a chunks | Doc 11 §17 |
| Creative DNA | Referências e padrões criativos podem ser recuperados para direção, não como decisão automática | DNA/14_RAG `creative_dna_indexing.md` |
| Work Orders | Work Orders consomem context packs e note support; Doc 28 fornece retrieval governado | Doc 27; Layer 13 Note 18 §10 |
| `context_packs` | Doc 28 fornece retrieval candidates; Doc 05/10 decidem context assembly | Doc 05 §5.7; Doc 11 §13 |
| `eval_results` | Retrieval quality é avaliada por evals e logs | Doc 13 §9; Doc 11 §19 |

---

# 14. Security Rules

Regras não-negociáveis:

1. Namespace é pré-condição, nunca pós-filtro.
2. PII não entra em embedding sem classification e policy explícita.
3. `permission_level` controla memória/RAG antes do retorno de candidatos.
4. Storage usa path scoped por tenant e URLs assinadas quando asset é arquivo.
5. Cross-tenant vector leak é incidente P0/P1 e gera audit log.
6. External models não recebem conteúdo PII/confidential sem policy de model privacy.
7. Outputs de RAG não podem revelar source proibido por permissão, mesmo em resumo.

Fonte: Doc 12 §5.6.2, §5.14, §11 e §13; Doc 11 §25; Doc 18 §3.

---

# 15. Testing Rules

Antes de qualquer implementação futura do Doc 28, os testes mínimos são:

| Teste | Critério |
|---|---|
| namespace precondition | Query sem namespace é recusada antes do vector store. |
| cross-tenant isolation | Dados de outro tenant não aparecem em candidatos nem logs expostos. |
| permission filtering | Memory/document chunk com clearance maior não retorna ao ator sem permissão. |
| PII classification | Conteúdo PII não classificado é bloqueado na indexação. |
| source lineage | Todo chunk retorna source path/ref, versão e provenance. |
| evidence retrieval | Evidence chunk retorna `evidence_id`, confidence e source tier. |
| stale memory | Memória expirada gera warning ou bloqueio conforme risk level. |
| retrieval eval | `rag_results.score`, context precision/recall e retrieval logs são persistidos. |
| cost guard | Embedding/retrieval registra custo e respeita soft/hard limits. |
| no silent promotion | Study note recuperada não vira canonical/long memory sem approval. |

Fonte: Doc 12 §14-§15; Doc 13 §9, §16, §27-§29; Layer 13 Note 18 §14-§17.

---

# 16. Failure Modes

| ID | Falha | Sintoma | Mitigação |
|---|---|---|---|
| FM-01 | Namespace como pós-filtro | Resultado cross-tenant aparece antes de filtro | Bloquear query; incidente; teste obrigatório. |
| FM-02 | Study note vira verdade | Agente cita estudo como canon | Trust metadata e Metacognik audit. |
| FM-03 | Chunk sem lineage | Resumo não consegue citar fonte | Rejeitar chunk/indexação. |
| FM-04 | PII embedada sem policy | Dado sensível entra em vector store | Classification gate antes de embedding. |
| FM-05 | Retrieval irrelevante | Context packet inclui ruído | Retrieval quality eval; pedir melhor contexto. |
| FM-06 | Re-embedding caro sem necessidade | Cost ledger cresce sem mudança de conteúdo | Content hash + cost guard. |
| FM-07 | Evidence sem evidence_id | Claim vira texto solto | Evidence indexing somente pós Doc 18 pipeline. |
| FM-08 | Conflito não detectado | Duas notas contraditórias aparecem sem aviso | Contradiction check + Metacognik. |
| FM-09 | Visual asset sem rights | Referência não reutilizável entra no pack | Rights/source metadata obrigatória. |
| FM-10 | Long memory escrita cedo demais | Output rejeitado reaparece como memória | Quality gate before memory write. |

Fonte: Doc 05 §12; Doc 12 §15; Doc 13 §27; Layer 13 Note 18 §15.

---

# 17. MVP P0 Scope

Para o thin-slice do GATE 5, Doc 28 recomenda escopo mínimo:

**Incluído em P0:**

- Markdown/text documents, canonical docs, study notes e approved evidence textual.
- `documents`, `document_chunks`, `embeddings`, `memories`, `rag_queries`, `rag_results`, `retrieval_logs` conforme Doc 11 §14.
- Namespace por org/workspace/project como precondition.
- Metadata mínima: source refs, confidence, provenance, classification, permission, memory_type, rag_priority.
- Retrieval quality logging com relevance, freshness e permission_filtered.
- Cost attribution para embedding/retrieval.
- Manual/audited promotion RAW → STUDY → CANONICAL.

**Fora do P0:**

- Multimodal vector search avançado.
- Auto-promoção de study note para canon.
- Cross-project/org semantic search sem política específica.
- Re-embedding automático em larga escala.
- Visual similarity como decisão criativa.
- Qualquer backend/API/migration criado por este documento.

Fonte: Doc 11 §26 MVP P0 Data Model; Doc 12 §5.6.2; Doc 13 §9; DNA/14_RAG folder.

---

# 18. Patches sugeridos ao Doc 11

As sugestões abaixo são especificações textuais para uma futura sessão de patch do Doc 11. Não são DDL, migrations ou autorização de schema.

## 18.1 Note object materialization

**Sugestão:** decidir se notas serão:

- especialização de `documents.kind = note`; ou
- tabela dedicada `notes` com link para `documents`; ou
- objeto registrado em `object_registry` com document backing.

Campos candidatos: `note_type`, `canonical_status`, `memory_type`, `rag_priority`, `provenance_status`, `confidence`, `valid_until`, `review_required`, `related_work_order_id`, `related_decision_id`.

## 18.2 Document metadata refinement

**Sugestão:** expandir `documents` com metadata conceitual: `source_type`, `source_ref`, `content_hash`, `lifecycle_state`, `canonical_status`, `data_classification`, `permission_level`, `provenance_status`, `confidence`, `rights_status`, `ingestion_status`.

## 18.3 Document chunks refinement

**Sugestão:** expandir `document_chunks` com `heading_path`, `source_page`, `source_line_start`, `source_line_end`, `time_range`, `region_ref`, `content_hash`, `chunk_version`, `language`, `lifecycle_state`, `confidence`, `provenance_status`.

## 18.4 Embeddings refinement

**Sugestão:** expandir `embeddings` com `source_kind`, `source_id`, `vector_collection_id`, `embedding_model_version`, `dims`, `modality`, `content_hash`, `classification`, `permission_level`, `expires_at`, `reembed_required`.

## 18.5 RAG query/result refinement

**Sugestão:** expandir `rag_queries`, `rag_results` e `retrieval_logs` com `namespace`, `query_intent_type`, `query_policy_ref`, `cost_estimate`, `cost_actual`, `retrieval_quality_score`, `freshness_score`, `source_reliability_score`, `permission_status`, `used_in_context_pack_id`, `blocked_reason`.

## 18.6 Knowledge asset lifecycle

**Sugestão:** criar ou registrar lifecycle states para knowledge assets: `raw`, `classified`, `parsed`, `chunked`, `embedded`, `indexed`, `reviewed`, `canonical`, `archived`, `rejected`, `expired`.

## 18.7 Negative memory

**Sugestão:** avaliar se `memories.type` ou `memory_write_events.write_type` deve suportar `negative_memory` para registrar outputs rejeitados que previnem repetição de erro.

---

# 19. ARCHITECTURE_QUESTIONS em aberto

| ID | Pergunta | Por que precisa decisão |
|---|---|---|
| AQ-01 | Notas serão `documents.kind=note`, tabela dedicada `notes` ou objeto registry-backed? | Afeta Doc 11, migrations e como RAG referencia notas. |
| AQ-02 | Qual embedding model/dims por modalidade e privacy class? | Fontes exigem embeddings, mas não definem modelo/dimensões. |
| AQ-03 | Quais tamanhos numéricos de chunk por tipo de conteúdo? | Doc 28 define política, mas thresholds precisam validação técnica. |
| AQ-04 | Multimodal embedding entra no P0 ou fica pós-P0 com OCR/transcript primeiro? | Impacta custo, privacidade e model routing. |
| AQ-05 | Cross-project retrieval dentro do mesmo tenant será permitido para quais roles? | Precisa política de segurança e audit. |
| AQ-06 | Como versionar re-chunking/re-embedding quando canonical docs mudarem? | Afeta lineage e stale retrieval. |
| AQ-07 | `negative_memory` será tipo canônico de memória ou apenas flag de QA/learning? | Evita reaparecimento de erros sem criar ruído. |
| AQ-08 | Quando uma study note recuperada pode influenciar Work Order de alto risco? | Requer regra Founder/Metacognik. |
| AQ-09 | Quais rights/licensing fields são obrigatórios para visual assets? | Necessário antes de Creative DNA/visual retrieval forte. |
| AQ-10 | Qual é a política de retenção para chunks expirados, PII e raw uploads rejeitados? | Afeta segurança, custo e compliance. |

---

# 20. Related Notes

- `01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md` — memory layers, RAG as context retrieval, embeddings not source of truth, trust hierarchy and context packet.
- `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md` — context packs, memories, documents, document_chunks, embeddings, rag_queries, rag_results, retrieval_logs, evidence_items and vector namespace.
- `03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md` — RLS, vector namespace isolation, PII classification, permission level and cross-tenant leak rules.
- `03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md` — retrieval relevance, freshness, context precision/recall, cost guard, quality gates and memory-write evals.
- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL.md` — evidence-first principles, private RAG namespace and Evidence Object Model.
- `07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md` — connectors and external providers remain governed access surfaces outside Doc 28.
- `07_EVOLUTION_SYSTEM/27_AI_FIRST_WORK_ORDERS_AND_MULTI_SESSION_ORCHESTRATION_ARCHITECTURE.md` — Work Orders consume note/RAG context but do not own knowledge architecture.
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/04_NOTES_AS_OPERATIONAL_MEMORY_STUDY.md` — note taxonomy and note-as-memory rule.
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/12_RAG_METADATA_AND_VECTOR_CATEGORY_STUDY.md` — metadata candidate, trust hierarchy and retrieval rules.
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/18_AI_FIRST_PROJECT_NOTE_SYSTEM_AND_RAG_GOVERNANCE_STUDY.md` — note governance, RAG metadata and non-authority boundaries.
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/README.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/rag_overview.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/document_chunking_policy.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/embedding_pipeline.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/supabase_vector_schema.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/creative_dna_indexing.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/evidence_indexing.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/memory_indexing.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/multimodal_embedding_strategy.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/image_to_text_retrieval.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/rag_query_policy.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/rag_retrieval_quality_score.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/rag_cost_policy.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/text_to_image_retrieval.md`
- `000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/14_RAG_VECTOR_SYSTEM/visual_asset_indexing.md`

## Patch 1.0.0 — Criação do documento

**Data:** 2026-06-02  
**Sessão:** `S-P1-GATE3-CODEX-20260602-001`  
**Modo:** `canonical_patch` documental  
**Gate:** GATE 3 — Doc 28 Notes/RAG/Knowledge Architecture

**Escopo criado:**

- Arquitetura canônica de notas como objetos CKOS;
- taxonomia de knowledge assets;
- ingestion pipeline;
- embedding strategy;
- chunking policy;
- RAG query policy;
- retrieval quality scoring;
- cost policy;
- runtime object connections;
- security and testing rules;
- MVP P0 scope;
- Doc 11 patch suggestions;
- ARCHITECTURE_QUESTIONS.

**Limites preservados:**

- Nenhum backend criado.
- Nenhuma API criada.
- Nenhuma migration criada.
- Doc 11 não foi alterado.
- Doc 05 e Doc 18 não foram duplicados.
- Doc 26 permanece dono de conectores externos.
- Doc 27 permanece dono de Work Orders/multi-session orchestration.
