---
title: Intent to Project Roadmap
file: 01_INTENT_TO_PROJECT_ROADMAP.md
phase: 000_ROADMAPS
category: creator_mode_roadmap
version: 1.0.0
status: draft
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
tags: [creator-mode, briefing, intent]
---

# Intent to Project Roadmap

## Fluxo

```txt
Founder escreve intenção mínima
→ CEO Agent interpreta
→ Prompt Enhancer refina intenção
→ Context Pack é sugerido
→ CEO propõe filetree
→ PMO audita
→ Founder aprova
→ CEO gera artefatos documentais
→ PMO valida
→ Founder decide próximo ciclo
```

## Exemplo

Input mínimo:

```txt
criar projeto para perfil no instagram para recém advogada penal feminina no brasil
```

Saída esperada antes de execução:

- categoria do projeto;
- risco regulatório;
- fontes obrigatórias;
- perguntas inteligentes;
- filetree proposta;
- custo simulado CKC;
- riscos;
- próximos artefatos;
- aprovação Founder.

## Briefing inteligente

O briefing não é formulário. É um sistema de perguntas adaptativas que consulta contexto, detecta lacunas, estima riscos, cria perguntas com função estratégica e transforma respostas em documentação do projeto.

Cada pergunta deve explicar:

- por que perguntamos;
- como a resposta será usada;
- qual risco reduz;
- qual artefato alimenta.
