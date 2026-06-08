---
title: ckos-qa-gate
file: ckos-qa-gate.md
phase: 02_EXECUTION_SYSTEM
category: skill_note
status: p0_draft
skill_id: ckos-qa-gate
skill_family: development_hardening
owner_agent: QA Lead
review_agent: Metacognik
runtime_authority: false
implementation_authorized: false
source_refs:
  - ../../000_ROADMAPS/22_CONSOLIDATION/05_P0_DEV_HARDENING_SKILL_PACK_ARCHITECTURE.md
  - ../06_SKILLS_REGISTRY.md
  - ../09_TRANSFORMERS_AND_PIPELINES.md
  - ../../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
---

# ckos-qa-gate

Valida entrega tecnica CKOS antes de release, merge, deploy ou handoff. QA checa build/test e tambem escopo, canonicidade, seguranca, eventos, banco, custo, observabilidade e release evidence.

# Quando Usar

- No fim de qualquer implementacao ou patch tecnico.
- Antes de declarar entrega pronta.
- Quando um executor afirmar que algo "esta funcionando".

# Quando Nao Usar

- Para aprovar trabalho sem artefato verificavel.
- Para substituir Metacognik/Founder em risco alto.
- Para validar so por leitura superficial sem evidencias.

# Entradas Minimas

- Work Order ou implementation brief;
- lista de arquivos alterados;
- forbidden scope;
- comandos de validacao disponiveis;
- riscos e AQs;
- evidencia de build/test/manual checks.

# Workflow

1. Comparar entrega contra Work Order/brief.
2. Verificar scope drift e forbidden scope.
3. Executar ou registrar build/test/lint quando possivel.
4. Checar data/security/event/cost conforme superficies tocadas.
5. Checar rollback readiness.
6. Listar blockers e residual risks.
7. Emitir pass, fail ou conditional.

# Saida Verificavel

QA gate report com:

- pass/fail/conditional;
- coverage de acceptance criteria;
- scope drift;
- tests/build/lint;
- data/security/event/cost checks;
- rollback readiness;
- release blockers;
- evidence table;
- next action unica.

# Guardrails

- Build verde nao aprova RLS, policy, event log ou audit quebrados.
- QA nao aprova escopo proibido pelo Work Order.
- Risco que bloqueia security/replay nao vira follow-up cosmetico.
- Se teste nao foi possivel, declarar explicitamente.

# Proxima Skill

- [[checkout-release]] se aprovado ou encerrado com risco visivel.
- [[risk-gap-review]] se lacunas bloqueiam readiness.
