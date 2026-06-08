---
title: document-ingestion
file: document-ingestion.md
phase: 02_EXECUTION_SYSTEM
category: skill_note
status: active_draft
skill_id: document-ingestion
skill_family: knowledge_operations
owner_agent: PMO_CKOS
review_agent: Metacognik
runtime_authority: false
implementation_authorized: false
source_skill: C:/Users/GustavoBxx/.codex/skills/document-ingestion/SKILL.md
---

# document-ingestion

Prepara documentos, uploads, Markdown, research packs ou source material para uso governado de conhecimento.

# Quando Usar

- Um documento precisa de classificacao, source metadata, sensitivity review e RAG readiness.
- E preciso planejar chunking e metadata sem executar embeddings.
- A fonte pode alimentar briefing, context pack, RAG ou evidencia.

# Quando Nao Usar

- Para criar embeddings, vector collections, migrations, ingestion workers ou sync jobs.
- Para indexar PII/confidential sem policy explicita.
- Para tratar study notes como verdade canonica.

# Entradas

- file_path_or_source_ref
- raw_content_summary
- project_or_workspace
- source_type
- owner
- data_classification
- intended_use
- rights_or_permissions

# Workflow

1. Identificar source type.
2. Capturar metadata e lineage.
3. Classificar sensibilidade, direitos e permission constraints.
4. Propor chunking strategy sem criar chunks, salvo pedido explicito.
5. Definir RAG readiness: ready, needs_cleanup, needs_approval ou blocked.
6. Listar riscos de retrieval, stale, conflito e exclusoes.

# Saida Verificavel

Um `CKOS Document Ingestion Plan` contendo:

- source;
- classification;
- ingestion decision;
- chunking plan;
- retrieval metadata;
- risks;
- next step.

# Guardrails

- Namespace e pre-condicao futura de retrieval, nao pos-filtro.
- Sensitive source nao fica ready sem policy.
- O output e plano, nao evento de ingestao concluido.
- Preferir P0 textual ingestion antes de RAG complexo.

# Proxima Skill

- [[note-normalizer]] se o documento precisa virar nota.
- [[context-pack-builder]] se ja existe contexto suficiente para execucao.
