---
title: ckos-backend-thin-slice
file: ckos-backend-thin-slice.md
phase: 02_EXECUTION_SYSTEM
category: skill_note
status: p0_draft
skill_id: ckos-backend-thin-slice
skill_family: development_hardening
owner_agent: Builder Lead
review_agent: Metacognik
runtime_authority: false
implementation_authorized: false
source_refs:
  - ../../000_ROADMAPS/22_CONSOLIDATION/03_BACKEND_MVP_THIN_SLICE_PLAN.md
  - ../../000_ROADMAPS/22_CONSOLIDATION/05_P0_DEV_HARDENING_SKILL_PACK_ARCHITECTURE.md
  - ../../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
---

# ckos-backend-thin-slice

Guia planejamento ou implementacao de backend P0 como thin-slice auditavel, sem cair em UI-first, chat-first ou CRUD generico.

# Quando Usar

- Em tarefas GATE5/F1 backend.
- Quando o trabalho toca ingress, intent resolver, workflow run, agent run, context pack, event store, approval gate, memory boundary ou ROI proxy.
- Quando e preciso decidir se algo entra no backend P0 ou fica fora.

# Quando Nao Usar

- Para frontend, dashboard, painel, design system ou UX rica.
- Para especificar internals de RAG, embeddings, chunking ou vector ranking.
- Para autorizar implementacao antes de Founder approval.

# Entradas Minimas

- sprint ou slice alvo;
- fluxo `intent -> event -> run -> output`;
- componentes runtime afetados;
- superficies de dados previstas no Doc 11;
- policies de approval, tenant, secret e custo.

# Workflow

1. Confirmar backend-only boundary.
2. Mapear fluxo minimo de intent ate output.
3. Definir evento inicial e eventos consequentes.
4. Identificar context pack minimo.
5. Aplicar checkpoint de policy/approval.
6. Exigir trace, custo e evidencia.
7. Definir criterio de replay causal.

# Saida Verificavel

Plano ou execucao backend com:

- backend-only boundary;
- eventos causais;
- correlation_id, causation_id e idempotency_key;
- context pack minimo;
- policy/approval checkpoint;
- output simples com evidencia;
- custo e trace;
- replay causal.

# Guardrails

- UI nao e criterio de pronto.
- Estado operacional nao vive fora de eventos/projecoes.
- RLS/tenant isolation nao pode ser adiado.
- Work Order nao vira tabela fisica sem Doc 11 ou AQ.

# Proxima Skill

- [[ckos-event-runtime-contract]] para eventos/runs/projections.
- [[ckos-data-model-migration]] para schema.
- [[ckos-policy-rls-security]] para policy/RLS.
- [[ckos-qa-gate]] antes de release.
