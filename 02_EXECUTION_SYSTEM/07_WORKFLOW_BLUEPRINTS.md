---
title: Workflow Blueprints
file: 07_WORKFLOW_BLUEPRINTS.md
phase: 02_EXECUTION_SYSTEM
category: workflow
version: 1.1.0
status: active
owner: PMO_CKOS
responsible_agent: PMO_CKOS
reviewers:
  - Metacognik
approval_required:
  - founder
  - PMO_CKOS
  - Metacognik
purpose: Definir os fluxos operacionais reutilizáveis que conectam agentes, skills, nodes, transformers, approvals e memória para executar objetivos reais.
inputs: Object Model; Skills Registry; Transformers; Autonomy; Memory.
outputs: Anatomia de workflow; estados/eventos padrão; blueprints prioritários; regra anti-entropia.
framework: Workflow = sequência adaptativa de eventos, agentes, skills e approvals.
edge_cases: Pular briefing; briefing contraditório; projeto sem categoria; mistura de projetos; dados sensíveis.
integrations: Instanciado e conduzido pela Workflow Engine em 10_RUNTIME; eventos no event bus.
prompts: Ver 08_PROMPT_LIBRARY (por skill/etapa).
metrics: Tempo intenção→node; tempo briefing→proposta; nodes rejeitados; execuções com logs completos; workflows revertidos com sucesso.
related_notes:
  - 02_AI_FIRST_OBJECT_MODEL.md
  - 06_SKILLS_REGISTRY.md
  - 09_TRANSFORMERS_AND_PIPELINES.md
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
tags: [execution, workflows, blueprints, states, events]
---

# 1. Propósito

Definir os fluxos operacionais reutilizáveis do CKOS. **Workflow é uma sequência adaptativa de eventos, agentes, skills e approvals que transforma uma intenção em resultado operacional auditável.** Não é checklist fixo: é vivo, pode criar nodes, chamar agentes, pausar por lacunas e solicitar aprovação.

# 2. Função dentro do CKOS

Conecta as peças do Execution System em fluxos executáveis. A **engine** que instancia e conduz workflows como máquinas de estado vive em `10_SYSTEM_RUNTIME_ARCHITECTURE §Workflow Engine`.

# 3. Inputs

Object Model (02); Skills Registry (06); Transformers (09); Autonomy (04); Memory (05); intenção/trigger.

# 4. Outputs

Anatomia de workflow; estados/eventos padrão; blueprints prioritários; regra anti-entropia.

# 5. Framework operacional

## 5.1 Anatomia de um workflow

```yaml
workflow_id:
name:
trigger:
entry_agent:
owner_agent:
review_agent:
autonomy_level:
required_skills:
required_objects:
created_objects:
approval_gates:
rollback_plan:
success_metrics:
```

## 5.2 Estados padrão

```txt
draft · ready · running · waiting_user_input · waiting_agent · waiting_approval · blocked · completed · failed · rolled_back · archived
```

## 5.3 Eventos padrão

```txt
workflow_started · intent_detected · node_created · agent_called · skill_executed · partial_insight_found
· hypothesis_created · gap_detected · risk_detected · approval_requested · approval_granted · approval_denied
· artifact_created · memory_updated · workflow_completed
```

Esses eventos são emitidos no event bus do runtime (`10`).

## 5.4 Blueprints prioritários

### Intelligent Briefing Flow
Conversa inicial → diagnóstico vivo. Nick detecta intenção → Cognik cria Briefing Vivo → Nick pergunta o mínimo → Cognik cria hipóteses parciais → Metacognik audita lacunas em tempo real → nodes sugeridos → usuário aprova/edita/rejeita → briefing vira base da proposta.

### Proposal Generation Flow
Nick recebe intenção → Branddock (pendente) define tese → Cognik conecta briefing/memória/evidências → agents geram seções → Metacognik audita escopo/riscos/promessas → PMO_CKOS estrutura timeline/entregáveis/gates → Founder aprova → cliente aprova → proposta vira workspace operacional. **Approval gates**: investimento, escopo, promessa de resultado, cláusulas comerciais, uso de imagens, custos.

### Node Creation Flow
Intenção/lacuna detectada → Cognik propõe node → Metacognik classifica risco/confiança → Nick explica por que o node existe → usuário aprova ou deixa como hipótese → node nasce com owner, input, output, status. **Regra**: todo node nasce respondendo "Que decisão este node ajuda a tomar?".

### Research Pack Flow
Usuário pede investigação → Research Subagent define escopo → Datta valida fontes → Cognik classifica padrões → Metacognik detecta riscos de cópia/viés → PMO_CKOS cria README, CSV, shortlist, implementation brief → pack salvo como artifact.

### Implementation Flow
PMO_CKOS cria implementation brief → Builder Lead escolhe executor (Claude Code, Codex, Antigravity ou Builder Subagents) → execução em branch/rota isolada → QA Lead valida → Metacognik audita regressões/risco → Founder aprova → merge/deploy controlado.

### QA Gate Flow
QA Lead recebe entrega → valida critérios técnicos, visuais e narrativos → compara com docs de origem → gera relatório → classifica: aprovado / aprovado com ajustes / reprovado.

# 6. Agente responsável

`PMO_CKOS` é owner dos blueprints.

# 7. Superagentes envolvidos

Nick; Cognik; Metacognik; PMO_CKOS; Builder Lead; QA Lead; Datta; Branddock (pendente).

# 8. Skills necessárias

workflow-orchestration; task-breakdown; approval-routing; node-creation; research-pack-generation; implementation-brief; qa-gate.

# 9. Prompts relacionados

Por etapa/skill, em `08_PROMPT_LIBRARY.md`.

# 10. Integrações

Workflow Engine (10); event bus (10); skills (06); transformers (09); approval system (04/10); memory (05/11).

# 11. Memória e contexto

Cada workflow lê context packet (05/10) e grava eventos/decisões em memória (11).

# 12. Edge cases

Usuário quer pular briefing; briefing contraditório; projeto sem categoria clara; usuário mistura vários projetos; dados sensíveis.

# 13. Métricas de sucesso

Tempo intenção→node; tempo briefing→proposta; taxa de nodes rejeitados; retrabalho por falta de contexto; nº de aprovações por workflow; % execuções com logs completos; % workflows revertidos com sucesso.

# 14. Critérios de aprovação

Nenhum workflow começa sem: objetivo, trigger, owner, output, approval gate, rollback/fallback e métrica de sucesso.

# 15. Critérios de reprovação

Reprovado se workflow for checklist fixo, sem eventos, sem approval gate, sem rollback ou sem rastreabilidade.

# 16. Related notes

- [[02_AI_FIRST_OBJECT_MODEL]]
- [[06_SKILLS_REGISTRY]]
- [[09_TRANSFORMERS_AND_PIPELINES]]
- [[10_SYSTEM_RUNTIME_ARCHITECTURE]]
