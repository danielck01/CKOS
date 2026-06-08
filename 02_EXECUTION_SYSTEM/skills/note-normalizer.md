---
title: note-normalizer
file: note-normalizer.md
phase: 02_EXECUTION_SYSTEM
category: skill_note
status: active_draft
skill_id: note-normalizer
skill_family: knowledge_operations
owner_agent: PMO_CKOS
review_agent: Metacognik
runtime_authority: false
implementation_authorized: false
source_skill: C:/Users/GustavoBxx/.codex/skills/note-normalizer/SKILL.md
---

# note-normalizer

Transforma conteudo solto em nota CKOS governada. A saida e rascunho normalizado, nao verdade canonica.

# Quando Usar

- Notas brutas, study notes, meeting notes, release notes ou observacoes precisam de metadata.
- Conteudo precisa de provenance, confidence, memory role, lifecycle e roteamento.
- Uma nota precisa ficar pronta para briefing, RAG, Work Order ou patch candidate.

# Quando Nao Usar

- Para promover study note a canonico.
- Para criar campos Doc 11, tabelas, IDs reais ou migrations.
- Para tratar placeholder como runtime record.

# Tipos De Nota

`canonical_note`, `study_note`, `roadmap_note`, `task_note`, `work_order_note`, `decision_note`, `memory_note`, `learning_note`, `feedback_note`, `prompt_note`, `risk_note`, `roi_note`, `handoff_note`, `patch_candidate_note`, `source_manifest_note`.

# Workflow

1. Identificar fonte, origem, data e contexto de projeto.
2. Classificar tipo de nota e camada de memoria.
3. Atribuir confidence e provenance.
4. Extrair decisoes, claims, riscos, perguntas e follow-ups.
5. Decidir roteamento: briefing, context pack, Work Order, RAG, archive ou patch candidate.
6. Marcar conteudo stale, unverified, sensitive ou conflitante.

# Saida Verificavel

Uma `Normalized CKOS Note` contendo:

- metadata;
- summary;
- claims com source_ref;
- links;
- risks and gaps;
- routing;
- RAG/index recommendation.

# Guardrails

- Canonico vence conflito.
- Sensitive content deve ser classificado.
- Nota recuperavel nao pode parecer verdade canonica.
- Follow-up precisa apontar proxima skill.

# Proxima Skill

- [[document-ingestion]] quando a nota/documento precisa entrar em knowledge flow.
- [[context-pack-builder]] quando a nota ja pode alimentar execucao.
