---
title: work-order-draft
file: work-order-draft.md
phase: 02_EXECUTION_SYSTEM
category: skill_note
status: active_draft
skill_id: work-order-draft
skill_family: operations
owner_agent: PMO_CKOS
review_agent: Metacognik
runtime_authority: false
implementation_authorized: false
source_skill: C:/Users/GustavoBxx/.codex/skills/work-order-draft/SKILL.md
---

# work-order-draft

Cria rascunho de Work Order governado. Task e unidade atomica; Work Order e envelope governado em torno de uma ou mais tasks.

# Quando Usar

- Trabalho precisa de escopo, forbidden scope, approval, risco, ROI, evidencia e release.
- Um briefing/context pack ja permite organizar execucao.
- Consolidacao, patch, auditoria ou implementacao precisam de envelope.

# Quando Nao Usar

- Para tratar draft como approval.
- Para criar schema, queues, agentes, API routes ou automacoes.
- Para despachar trabalho sem evidencia e release requirements.

# Entradas

- project_seed
- briefing
- context_pack
- task_candidates
- risk_gap_review
- source_refs
- requested_output
- approval_context

# Workflow

1. Nomear a decisao ou artifact que o Work Order desbloqueia.
2. Definir allowed scope e forbidden scope.
3. Converter trabalho candidato em tasks atomicas.
4. Atribuir risk ceiling, ROI hypothesis, evidence requirements e approval rules.
5. Definir session mode: read-only, canonical patch, implementation, audit ou fan-in.
6. Definir release requirements e postura de memory update.
7. Marcar readiness.

# Saida Verificavel

Um `CKOS Work Order Draft` contendo:

- identity;
- scope;
- tasks;
- governance;
- ROI hypothesis;
- evidence and validation;
- memory and RAG posture;
- readiness.

# Guardrails

- Approval e release sao distintos.
- Risky Work Order nao pode self-approve.
- Escrita em canonico exige checkout lock e release explicitos.
- Task candidata precisa rastrear briefing, intent, source ou audit finding.

# Proxima Skill

- [[risk-gap-review]] para auditar o draft.
- [[ckos-implementation-brief]] quando Work Order tecnico estiver aprovado para execucao.
