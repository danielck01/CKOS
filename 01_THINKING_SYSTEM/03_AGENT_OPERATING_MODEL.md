---
title: Agent Operating Model
file: 03_AGENT_OPERATING_MODEL.md
phase: 01_THINKING_SYSTEM
category: agents
version: 1.2.0
status: active
owner: PMO_CKOS
responsible_agent: PMO_CKOS
reviewers:
  - Metacognik
approval_required:
  - founder
purpose: Definir como agentes, superagentes e subagentes operam — papéis, hierarquia, handoffs, runs, estados — sem criar "personagens IA" sem função.
inputs: Sinais; nodes ativos; briefing vivo; capabilities; workflows; memória; approvals; documentos; dados externos; decisões do Founder; outputs de outros agentes.
outputs: Agent runs; insights; hipóteses; riscos; lacunas; artefatos; prompts; código; documentação; QA reports; approval requests; events.
framework: Founder → PMO_CKOS → Nick → Cognik → Metacognik → superagents → agents → subagents → skills → tools.
edge_cases: Agentes discordam; output genérico; execução sem approval; agente duplicado; Founder sobrecarregado.
integrations: Roteamento e agendamento materializados em 10_RUNTIME (Agent Router, Run Scheduler); evals em 13.
prompts: Roteamento de agente; revisão metacognitiva; decomposição PMO.
metrics: Roteamento correto; tempo intenção→agente; runs aprovados; outputs reprovados por genericidade; custo/run; redução de prompts manuais.
related_notes:
  - 01_CKOS_AI_FIRST_CONSTITUTION.md
  - 02_AI_FIRST_OBJECT_MODEL.md
  - 04_AUTONOMY_AND_APPROVALS.md
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md
tags: [thinking, agents, orchestration, handoff, runs]
---

# 1. Propósito

Definir como agentes, superagentes e subagentes operam no CKOS. No CKOS, agente só existe se produzir mudança de estado, decisão, artefato, insight, evidência, risco, node, workflow ou aprovação. Nomes bonitos sem skill contratada são proibidos (`00_TAXONOMY §7.4`).

# 2. Função dentro do CKOS

Define tipos de agentes, papéis e limites, hierarquia, handoffs, runs, memória, autonomia, aprovação, qualidade, relação humano-IA e como o CKOS pode se desenvolver com Builder Subagents no futuro (ver `21_SELF_EVOLVING_SYSTEM`).

# 3. Inputs

Sinais; nodes ativos; briefing vivo; capabilities; workflows; memória; approvals; documentos; dados externos; decisões do Founder; outputs de outros agentes.

# 4. Outputs

Agent runs; insights; hipóteses; riscos; lacunas; artefatos; prompts; código; documentação; QA reports; recomendações; approval requests; events.

# 5. Framework operacional

## 5.1 Tipos de agentes

- **Human Founder**: autoridade final — visão estratégica, mudanças estruturais, orçamento, contratação, publicação externa, escopo, aprovação de autonomia, aceite de proposta. O CKOS reduz a carga do Founder, não o remove de decisões críticas.
- **Superagents**: orquestradores de alto nível (não executam toda tarefa pequena). Oficiais: `Nick, Cognik, Metacognik, PMO_CKOS, Builder Lead, QA Lead, Datta, Ops, Campaign` (e Branddock, pendente).
- **Agents (catálogo de hipóteses)**: especialistas de domínio que **só ativam com skill contratada** (Lia, Neura, Philo, Story, Visual, Social, Commerce, Media, ROI, Legal/Ethos, CalendarOps, WhatsOps). Até lá, são hipóteses de agente, não agentes ativos.
- **Subagents**: executores específicos — Briefing Parser, Gap Detector, Proposal Builder, Node Generator, Prompt Refiner, Research Subagent, Reels Collector, Competitor Mapper, ROI Calculator, Report Builder, Approval Manager, QA Regression Checker, **Builder Subagents** (Frontend, Backend, Data, RAG, Automation, Design System, QA Builder).

## 5.2 Superagents oficiais

- **Nick**: interface relacional — entende intenção, explica o sistema, cria comandos, aciona Cognik, pede aprovações, apresenta outputs, guia stakeholders.
- **Cognik**: camada cognitiva — interpreta sinais, gera hipóteses, cria nodes, sugere capabilities, conecta evidências, atualiza diagnóstico vivo, chama agentes.
- **Metacognik**: camada metacognitiva — audita raciocínio, detecta lacunas, mede confiança, aponta riscos, questiona decisões fracas, define approval e valida qualidade.
- **PMO_CKOS**: governança operacional — roadmap, dependências, sprints, escopo, handoffs, anti-entropia.
- **Builder Lead**: orquestra Builder Subagents — distribui implementação, escolhe executor, consolida código, revisa arquitetura, prepara entrega.
- **QA Lead**: valida qualidade e regressão — checks, fluxos, UI, código, build, release.

## 5.3 Hierarquia operacional

```txt
Founder → (aprova visão, risco, orçamento, escopo)
PMO_CKOS → (organiza execução)
Nick → (interface e intenção)
Cognik → (interpretação e nodes)
Metacognik → (auditoria e approval gates)
Superagents especializados → (coordenam domínios)
Agents → (executam domínios)
Subagents → (tarefas atômicas)
Skills → (capacidades reutilizáveis)
Tools → (APIs e integrações)
```

## 5.4 Handoff protocol

```yaml
handoff_id:
from_agent:
to_agent:
project_id:
node_id:
reason:
context_summary:
required_inputs:
expected_output:
deadline:
approval_required:
risk_level:
memory_refs:
```

## 5.5 Agent Run

```yaml
run_id:
agent:
skill:
trigger:
input:
output:
confidence:
risks:
gaps:
next_actions:      # novo — alinha o Execution Output Envelope (Doc 06 §5.3.2)
evidence:
cost:
model:
status:
started_at:
completed_at:
review_agent:
approval_status:
idempotency_key:   # novo — ver 10_RUNTIME
trace_id:          # novo — ver 13_EVALS
```

## 5.6 Agent states

```txt
idle · listening · thinking · collecting · analyzing · drafting · executing
waiting_input · waiting_approval · blocked · reviewing · completed · failed · archived
```

O agendamento, concorrência e retry desses estados são definidos em `10_SYSTEM_RUNTIME_ARCHITECTURE.md §Run Scheduler`.

## 5.7 Autonomia dos Builder Subagents

```txt
Founder aprova objetivo → PMO_CKOS cria roadmap → Builder Lead distribui tarefas
→ Builder Subagents executam → QA Lead valida → Metacognik audita risco → Founder aprova release crítica
```

A arquitetura completa desse loop (sandbox, eval-antes-de-merge, rollback) vive em `21_SELF_EVOLVING_SYSTEM.md` e depende de `12_SECURITY` e `13_EVALS`.

# 6. Agente responsável

`PMO_CKOS` mantém o modelo.

# 7. Superagentes envolvidos

Nick; Cognik; Metacognik; Builder Lead; QA Lead; Datta; Ops; Campaign.

# 8. Skills necessárias

intent-routing; agent-routing; task-decomposition; handoff-generation; run-logging; metacognitive-review; approval-requesting; QA-gate; implementation-planning.

# 9. Prompts relacionados

```txt
Classifique a intenção do usuário, identifique o objeto afetado, escolha agente responsável, skill necessária, nível de autonomia e necessidade de aprovação.
```

```txt
Revise este output: confiança, evidências, lacunas, contradições, risco, custo, aprovação necessária e próximo passo.
```

```txt
Quebre este objetivo em tarefas executáveis por agentes, com dependências, approval gates, critérios de sucesso e ordem de execução.
```

# 10. Integrações

Model providers via OpenRouter; Claude/Codex/Antigravity como executores externos; Manus como Research tool temporária; Supabase para agent runs/logs; Redis para estado temporário; RAG para memória; APIs de coleta; Git/repo; deploy; QA automation. Roteamento concreto em `10_RUNTIME`.

# 11. Memória e contexto

Recuperação por nível: Nick (stakeholder, projeto, conversa, approvals); Cognik (sinais, briefing, nodes, hipóteses); Metacognik (decisões, riscos, lacunas, confiança); PMO_CKOS (roadmap, dependências, status); Builder Subagents (arquivos, código, issues, design system); QA Lead (regressões, critérios, relatórios).

# 12. Edge cases

- **Agentes discordam** → `agent_disagreement_event` e Metacognik decide.
- **Output genérico** → QA Lead reprova e pede especificidade.
- **Execução sem approval** → bloquear run, registrar incidente, revisar autonomia.
- **Agente duplicando outro** → PMO_CKOS consolida responsabilidades.
- **Founder sobrecarregado** → auto-approval policy para ações reversíveis de baixo risco (ver 04).

# 13. Métricas de sucesso

Roteamento correto; tempo intenção→agente; runs aprovados; outputs reprovados por genericidade; custo/run; tempo de handoff; nº de aprovações por fluxo; redução de prompts manuais; taxa de execução automática segura.

# 14. Critérios de aprovação

Aprovado se diferencia superagents/agents/subagents; define Nick/Cognik/Metacognik; contempla Builder Subagents; exige run logs; define handoffs; protege approval gates.

# 15. Critérios de reprovação

Reprovado se agentes forem só nomes, sem handoff, run log, QA, Metacognik ou relação com autonomia.

# 16. Related notes

- [[01_CKOS_AI_FIRST_CONSTITUTION]]
- [[02_AI_FIRST_OBJECT_MODEL]]
- [[04_AUTONOMY_AND_APPROVALS]]
- [[10_SYSTEM_RUNTIME_ARCHITECTURE]]
- [[21_SELF_EVOLVING_SYSTEM]]
