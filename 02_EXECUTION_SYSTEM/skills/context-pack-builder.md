---
title: context-pack-builder
file: context-pack-builder.md
phase: 02_EXECUTION_SYSTEM
category: skill_note
status: active_draft
skill_id: context-pack-builder
skill_family: operations
owner_agent: PMO_CKOS
review_agent: Metacognik
runtime_authority: false
implementation_authorized: false
source_skill: C:/Users/GustavoBxx/.codex/skills/context-pack-builder/SKILL.md
---

# context-pack-builder

Monta o menor pacote de contexto suficiente para sustentar decisao, auditoria, Work Order ou handoff.

# Quando Usar

- Antes de execucao governada.
- Antes de Work Order draft.
- Antes de auditoria, handoff ou sessao de modelo que precise contexto compacto e confiavel.

# Quando Nao Usar

- Para despejar pastas inteiras ou docs inteiros sem necessidade.
- Para substituir BRA Packet.
- Para sobrescrever permissions, approvals ou forbidden scope.

# Entradas

- project_seed
- briefing
- normalized_notes
- document_ingestion_plans
- active_decisions
- constraints
- risk_review
- source_refs
- intended_execution_or_audit

# Workflow

1. Definir finalidade do context pack.
2. Selecionar apenas fontes necessarias para a proxima acao.
3. Separar canonical facts, study context, assumptions e open questions.
4. Incluir allowed scope, forbidden scope, permissions, risk ceiling e cost constraints.
5. Adicionar evidence refs e memory refs quando houver.
6. Declarar o que foi excluido.

# Saida Verificavel

Um `CKOS Context Pack` contendo:

- purpose;
- intent and briefing;
- source set com authority_level;
- active decisions;
- constraints;
- relevant context;
- exclusions;
- open questions;
- readiness.

# Guardrails

- Context pack deve ser menor que o material fonte.
- Study context nao pode parecer canonico.
- Forbidden scope deve aparecer de forma explicita.
- BRA Packet e relay cross-session, nao lock ou approval.

# Proxima Skill

- [[work-order-draft]] quando o contexto suporta execucao.
- [[risk-gap-review]] quando ha risco ou incerteza.
- [[ckos-implementation-brief]] quando ja ha Work Order aprovado para traducao tecnica.
