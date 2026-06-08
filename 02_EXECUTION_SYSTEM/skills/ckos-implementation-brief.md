---
title: ckos-implementation-brief
file: ckos-implementation-brief.md
phase: 02_EXECUTION_SYSTEM
category: skill_note
status: p0_draft
skill_id: ckos-implementation-brief
skill_family: development_hardening
owner_agent: PMO_CKOS
review_agent: QA Lead
runtime_authority: false
implementation_authorized: false
source_refs:
  - ../../000_ROADMAPS/22_CONSOLIDATION/05_P0_DEV_HARDENING_SKILL_PACK_ARCHITECTURE.md
  - ../06_SKILLS_REGISTRY.md
  - ../07_WORKFLOW_BLUEPRINTS.md
  - ../09_TRANSFORMERS_AND_PIPELINES.md
---

# ckos-implementation-brief

Transforma Work Order, briefing, context pack ou decisao Founder em briefing tecnico executavel para Claude Code, Codex ou Windsurf.

# Quando Usar

- Antes de implementacao, refatoracao, migration, API, worker, teste ou patch tecnico.
- Quando o pedido ainda esta em linguagem de produto/estrategia.
- Quando varios executores precisam receber o mesmo contrato de escopo.

# Quando Nao Usar

- Para brainstorming sem autorizacao de execucao.
- Para editar Doc 06/10/11/12/13 sem gate documental.
- Para substituir [[work-order-draft]].

# Entradas Minimas

- objetivo tecnico;
- fonte de autoridade;
- allowed_scope e forbidden_scope;
- arquivos ou superficies provaveis;
- risco, dados sensiveis, custo, rollback e criterios de aceite.

# Workflow

1. Confirmar fonte de autoridade.
2. Extrair objetivo tecnico e non-goals.
3. Gerar file impact map.
4. Classificar risco e superficies tocadas.
5. Selecionar executor: Claude Code, Codex, Windsurf ou outro.
6. Anexar guardas obrigatorias: data, security, event, backend ou QA.
7. Definir comandos de validacao e release evidence esperado.

# Saida Verificavel

Um implementation brief contendo:

- executor recomendado;
- task decomposition;
- file impact map;
- forbidden scope;
- acceptance criteria;
- validation commands;
- rollback/fallback;
- checks de security/data/event/cost;
- release evidence esperado.

# Guardrails

- Sem fonte de autoridade, parar e pedir Work Order/context pack.
- Schema/migration sem Doc 11 vira `ARCHITECTURE_QUESTION`.
- Risk high, dados sensiveis, billing, policy ou deploy exigem approval.

# Proxima Skill

- [[ckos-backend-thin-slice]] se tocar backend P0.
- [[ckos-data-model-migration]] se tocar banco/schema.
- [[ckos-policy-rls-security]] se tocar policy/security.
- [[ckos-event-runtime-contract]] se tocar eventos/runtime.
- [[ckos-qa-gate]] no fechamento.
