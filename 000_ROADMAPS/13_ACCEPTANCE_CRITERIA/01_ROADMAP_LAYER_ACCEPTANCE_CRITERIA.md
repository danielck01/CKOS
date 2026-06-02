---
title: Roadmap Layer Acceptance Criteria
file: 01_ROADMAP_LAYER_ACCEPTANCE_CRITERIA.md
phase: 000_ROADMAPS
category: acceptance_criteria
version: 1.0.0
status: active
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
  - metacognik
purpose: Planejar, governar e sincronizar a evolução documental e operacional do CKOS sem gerar implementação prematura.
inputs:
  - 00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md
  - CKOS_FOLDER_MEMORY.md
  - CKOS_FILETREE_MAP.md
  - ARCHITECTURE_PATCH_REPORT.md
outputs:
  - plano rastreável
  - tarefas auditáveis
  - riscos abertos
  - critérios de aceite
framework: Sentir, Pensar, Criar, Conectar, Avaliar, Elevar
edge_cases: Roadmap treated as canonical source; agent reads excessive context; implementation starts from planning material.
integrations: codex, claude, antigravity, ceo_agent, pmo_auditor and founder review sessions.
prompts: Read README and ck_memory before task-specific planning, patching or handoff.
metrics: YAML valid; 0 canonical docs created; 0 implementation changes; handoff logged when sessions change.
confidence: unverified
provenance_status: unverified
source_tool: chatgpt
related_notes:
  - README.md
tags: [acceptance, qa, roadmaps]
---

# Roadmap Layer Acceptance Criteria

## Aceite estrutural

- [ ] `000_ROADMAPS/README.md` existe.
- [ ] Cada roadmap possui `README.md`, `ck_memory.md`, `ck_tasks.md`, `ck_risks.md`, `ck_roi.md`, `ck_feedback.md`, `ck_agent_handoffs.md`.
- [ ] YAML segue padrão CKOS.
- [ ] Não há alteração de docs canônicos.
- [ ] Não há implementação.

## Aceite operacional

- [ ] Um agente consegue iniciar pela pasta e entender contexto.
- [ ] Há tarefas em formato kanban.
- [ ] Há riscos registrados.
- [ ] Há ROI como hipótese, não claim final.
- [ ] Há prompt para Codex, Claude, Antigravity e PMO Auditor.

## Aceite de segurança

- [ ] Segurança aparece como lane permanente.
- [ ] Não há secrets.
- [ ] Não há bypass de policy engine, approval gate, cost guard ou audit logs.
- [ ] Não há promoção de n8n/Manus a core runtime.

## Aceite de governança

- [ ] RAW → STUDY → CANONICAL respeitado.
- [ ] Docs 26–34 não foram criados automaticamente.
- [ ] Handoffs foram previstos.
- [ ] CHECKOUT_LOCK/RELEASE estão disponíveis como templates.
