---
title: risk-gap-review
file: risk-gap-review.md
phase: 02_EXECUTION_SYSTEM
category: skill_note
status: active_draft
skill_id: risk-gap-review
skill_family: metacognitive
owner_agent: Metacognik
review_agent: Founder
runtime_authority: false
implementation_authorized: false
source_skill: C:/Users/GustavoBxx/.codex/skills/risk-gap-review/SKILL.md
---

# risk-gap-review

Auditoria estilo Metacognik para briefings, notas, context packs, Work Orders, patches, releases ou planos.

# Quando Usar

- Antes de execucao ou release.
- Quando ha risco, lacuna, contradicao, evidencia fraca, scope drift, self-approval ou conflito canonico.
- Quando um artefato precisa de readiness honesto.

# Quando Nao Usar

- Para editar se o pedido e read-only.
- Para ser aprovador final do proprio output.
- Para tratar RAG/context retrieval como autoridade final.

# Entradas

- project_seed
- briefing
- normalized_note
- document_ingestion_plan
- context_pack
- Work Order draft
- patch plan
- release
- diff or source refs

# Workflow

1. Identificar artefato e decisao pretendida.
2. Checar escopo, forbidden scope, autoridade de fonte e approvals.
3. Checar evidencia, provenance, freshness, contradicoes e assumptions.
4. Checar riscos: security, PII, tenant leak, runtime drift, schema drift, cost, autonomy, canonical conflict.
5. Detectar self-approval.
6. Decidir readiness.
7. Produzir poucas perguntas que mudam acao ou risco.

# Saida Verificavel

Um `CKOS Risk And Gap Review` contendo:

- review target;
- findings;
- gaps;
- contradictions;
- risk register;
- approval and scope;
- questions;
- verdict.

# Guardrails

- Findings citam evidencia ou source refs.
- Perguntas sao poucas e acionaveis.
- Verdict nao implica implementation approval.
- Residual risk fica visivel.

# Proxima Skill

- [[work-order-draft]] se a auditoria pede novo envelope.
- [[ckos-qa-gate]] se o artefato ja e entrega tecnica.
- [[checkout-release]] se a sessao esta encerrando.
