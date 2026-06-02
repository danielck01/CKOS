---
title: Client Project Creator Mode Roadmap — ck_memory
file: ck_memory.md
phase: 000_ROADMAPS
category: folder_memory
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
tags: [memory, 09_client_project_creator_mode_roadmap]
---

# ck_memory — Client Project Creator Mode Roadmap

## Último estado conhecido

Pasta criada como parte do `000_ROADMAPS`. Ainda não substitui documentação canônica. Deve ser usada para orientar execução documental, handoffs e planejamento.

## Decisões já tomadas

- Roadmaps devem operar como camada auxiliar.
- Nenhum agente deve criar docs canônicos sem microgate.
- Toda execução relevante precisa registrar custo, risco, aprovação e impacto.
- Segurança, governança e custo são lanes permanentes, não fases finais.

## Arquivos principais

- `README.md`
- `ck_tasks.md`
- `ck_risks.md`
- `ck_roi.md`
- `ck_feedback.md`
- `ck_agent_handoffs.md`

## Próximas ações

- Validar escopo da pasta com Founder.
- Preencher tarefas específicas.
- Conectar com docs canônicos relevantes.
- Atualizar esta memória após cada entrega.

## Regras de atualização

1. Atualizar antes e depois de qualquer alteração significativa.
2. Registrar decisões, não apenas tarefas.
3. Não transformar hipótese em decisão aprovada.
4. Se houver conflito com docs canônicos, pausar e abrir PMO audit.
