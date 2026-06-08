---
title: briefing-builder
file: briefing-builder.md
phase: 02_EXECUTION_SYSTEM
category: skill_note
status: active_draft
skill_id: briefing-builder
skill_family: operations
owner_agent: PMO_CKOS
review_agent: Metacognik
runtime_authority: false
implementation_authorized: false
source_skill: C:/Users/GustavoBxx/.codex/skills/briefing-builder/SKILL.md
---

# briefing-builder

Converte contexto espalhado em briefing CKOS estruturado, capaz de alimentar notas, context packs e Work Orders.

# Quando Usar

- Ha conversa, notas, uploads ou project seed sem estrutura.
- O objetivo, publico, sucesso, restricoes e nao-objetivos precisam ficar claros.
- Ainda existem lacunas antes de execucao.

# Quando Nao Usar

- Para transformar toda resposta em tarefa.
- Para criar runtime transformers, schemas, workflows ou agentes.
- Para ignorar falta de contexto e pular direto para Work Order.

# Entradas

- project_seed
- raw_intent
- pasted_conversation
- notes_or_uploads
- prior_decisions
- target_artifact
- constraints
- stakeholder_context

# Workflow

1. Extrair objetivo, audiencia, criterios de sucesso, restricoes e non-goals.
2. Separar fatos com fonte de assumptions.
3. Identificar gaps que viram perguntas.
4. Identificar notas candidatas para normalizacao.
5. Identificar Work Orders candidatos somente se o briefing estiver especifico.
6. Atribuir readiness.

# Saida Verificavel

Um `CKOS Briefing` contendo:

- summary;
- source context;
- requirements;
- non-goals;
- assumptions;
- gaps and smart questions;
- candidate notes;
- candidate Work Orders;
- acceptance criteria;
- readiness.

# Guardrails

- Todo claim importante preserva origem.
- Assumptions ficam explicitas.
- Trabalho de alto risco exige approval.
- Briefing deve ser util mesmo sem execucao.

# Proxima Skill

- [[note-normalizer]] para notas candidatas.
- [[context-pack-builder]] para montar contexto minimo.
- [[work-order-draft]] quando houver escopo suficiente.
