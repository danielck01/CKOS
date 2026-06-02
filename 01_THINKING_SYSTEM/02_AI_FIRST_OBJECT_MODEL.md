---
title: AI First Object Model
file: 02_AI_FIRST_OBJECT_MODEL.md
phase: 01_THINKING_SYSTEM
category: object_model
version: 1.1.0
status: active
owner: PMO_CKOS
responsible_agent: Cognik
reviewers:
  - Metacognik
approval_required:
  - founder
purpose: Definir os objetos centrais (conceituais) que o CKOS manipula e suas relações, estados e lifecycle. A materialização física vive em 11_DATA_MODEL.
inputs: Intenção do usuário; briefing vivo; arquivos; dados externos; outputs de agentes; decisões; aprovações; eventos; memória; capabilities; contexto whitelabel.
outputs: Taxonomia de objetos; relações; estados operacionais; lifecycle de node; regras de criação dinâmica.
framework: Workspace→Project→Briefing→Signal→Node→Capability→Agent→Skill→Workflow→Run→Artifact/Decision→Memory.
edge_cases: Node duplicado; capability errada; dados conflitantes; insight sem evidência; workflow sem approval.
integrations: Materialização em 11_DATA_MODEL; execução em 10_RUNTIME; recuperação em 05_MEMORY.
prompts: Prompt de criação de node; prompt de capability detection.
metrics: Taxa de nodes úteis; capabilities corretas; tempo signal→node; % insights com evidência; redução de duplicidade.
related_notes:
  - 01_CKOS_AI_FIRST_CONSTITUTION.md
  - 03_AGENT_OPERATING_MODEL.md
  - 05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../04_PRODUCT_SYSTEM/16_NODE_CANVAS_ARCHITECTURE.md
tags: [thinking, object_model, nodes, lifecycle, capabilities]
---

# 1. Propósito

Definir os objetos centrais que o CKOS manipula. Sem modelo de objetos, agentes, dashboards e workflows viram peças soltas. Responde: o que existe; o que humanos e IA podem criar; o que é dinâmico; o que exige aprovação; como os objetos se relacionam; como evitar virar um conjunto de dashboards fixos.

> Este documento é **conceitual**. A persistência (tabelas, vetores, cache, isolamento multi-tenant) é definida em `11_DATA_MODEL_AND_PERSISTENCE.md`.

# 2. Função dentro do CKOS

Base conceitual para banco de dados, Canvas, CommandBar, workflows, agentes, memória, approvals, dashboards adaptativos, proposta inteligente e execução.

# 3. Inputs

Intenção; briefing vivo; arquivos; dados externos; outputs de agentes; decisões; aprovações; eventos de workflow; memória do projeto; capabilities; contexto whitelabel.

# 4. Outputs

Taxonomia de objetos; relações; estados operacionais; lifecycle de nodes; dependências para dashboards/workflows; regras de criação dinâmica.

# 5. Framework operacional

## 5.1 Objetos principais

```txt
Workspace · Project · Stakeholder · Briefing · Signal · Node · Capability · Agent · Skill
Workflow · Run · Insight · Hypothesis · Risk · Gap · Evidence · Decision · Approval
Artifact · Memory · Prompt · Integration · Metric · Event
```

## 5.2 Definições

- **Workspace**: container de organização/cliente/operação.
- **Project**: unidade operacional (branding, campanha, pesquisa, produto, proposta, evento, e-commerce, sistema).
- **Stakeholder**: founder, owner, sponsor, reviewer, operator, client, external partner, agent group.
- **Briefing**: objeto vivo (não formulário). Campos: `objective, context, constraints, audience, stakeholders, known_data, missing_data, current_hypotheses, active_nodes, confidence_score`.
- **Signal**: qualquer entrada que altere o entendimento (frase, imagem, arquivo, métrica, venda, concorrente, mudança de decisão).
- **Node**: unidade cognitiva/operacional do Canvas (análise, coleta, decisão, hipótese, tarefa, campanha, capability, workflow, documento, aprovação ou output).
- **Capability**: módulo ativável por necessidade. Não aparece por default.
- **Agent / Skill / Workflow / Run**: conforme taxonomia.
- **Insight / Hypothesis / Risk / Gap / Evidence**: objetos de raciocínio para diagnóstico vivo.
- **Decision**: escolha registrada com contexto, responsável, data, evidências e consequências.
- **Approval**: permissão explícita para avançar.
- **Artifact**: output material (proposta, prompt, imagem, relatório, plano, roadmap, componente).
- **Memory**: registro persistente recuperável.
- **Event**: mudança de estado (`node_created`, `agent_started`, `hypothesis_updated`, `risk_detected`, `approval_requested`, `artifact_generated`).

## 5.3 Relações principais

```txt
Workspace has many Projects
Project has many Stakeholders · has one Living Briefing
Briefing generates Signals → create/update Nodes → may activate Capabilities → summon Agents
Agents use Skills → execute Runs → produce Artifacts, Insights, Risks, Gaps, Evidence
Insights → Hypotheses → require Decisions → may require Approvals → trigger Workflows
Workflows generate Events → update Memory → updates future context
```

## 5.4 Estados de Node

```txt
draft · suggested · active · waiting_input · waiting_approval · running · blocked · completed · archived · reopened
```

A engine que aplica essas transições é definida em `10_SYSTEM_RUNTIME_ARCHITECTURE.md §Node State Machine`.

## 5.5 Lifecycle de Node

```txt
signal_received → node_suggested → node_created → agent_assigned → run_started
→ partial_outputs → metacognik_review → user_input_or_approval → artifact_generated
→ decision_logged → memory_updated
```

## 5.6 Capability activation logic

Uma capability só ativa se ao menos uma for verdadeira: usuário solicitou; Cognik detectou necessidade; Metacognik identificou lacuna crítica; PMO_CKOS recomendou para reduzir risco; workflow depende dela; stakeholder aprovou; dado externo confirma.

# 6. Agente responsável

`Cognik` é owner operacional do modelo de objetos (interpreta sinais e transforma em estrutura). `PMO_CKOS` é owner documental.

# 7. Superagentes envolvidos

Nick (cria por comando); Cognik (interpreta e cria nodes); Metacognik (audita objetos críticos); PMO_CKOS (dependências); Builder Lead (implementa objetos no produto); QA Lead (valida estados/edge cases).

# 8. Skills necessárias

node-creation; capability-detection; signal-classification; object-linking; memory-routing; approval-routing; event-logging; workflow-instantiation.

# 9. Prompts relacionados

```txt
Dado o contexto do projeto, classifique este sinal e decida: (1) atualizar briefing, (2) criar hipótese, (3) criar node, (4) ativar capability, (5) solicitar aprovação, (6) apenas registrar memória. Retorne motivo, confiança, riscos e próximo passo.
```

```txt
Analise se esta intenção exige capability ativa, sugerida ou nenhum módulo novo. Não ative capability por default.
```

# 10. Integrações

Supabase; Redis; vector store; RAG; OpenRouter/model providers; Apify; Google/WhatsApp/Calendar; Obsidian/export markdown. Mapeamento físico em `11_DATA_MODEL`.

# 11. Memória e contexto

Cada objeto indica se alimenta memória curta, média, longa, vetorial, log auditável, contexto de proposta ou de execução. A política de gravação/expiração está em `05_MEMORY_AND_CONTEXT_ARCHITECTURE.md`.

# 12. Edge cases

- **Node duplicado**: Cognik busca nodes semelhantes antes de criar.
- **Capability errada**: Metacognik rebaixa de active para suggested.
- **Dados conflitantes**: criar `conflict_event` e solicitar revisão.
- **Insight sem evidência**: existe, mas marcado low confidence.
- **Workflow sem approval**: se envolver custo, publicação, envio externo, contrato ou mudança de escopo, bloquear.

# 13. Métricas de sucesso

Taxa de nodes úteis; capabilities ativadas corretamente; tempo signal→node; % insights com evidência; redução de duplicidade; % decisões com approval log; workflows concluídos sem retrabalho.

# 14. Critérios de aprovação

Aprovado se evita dashboards fixos, permite nodes dinâmicos, separa signal/insight/hypothesis/decision/artifact, contempla approvals e prepara banco/Canvas (com materialização em 11).

# 15. Critérios de reprovação

Reprovado se dashboard for objeto central, node e workflow forem confundidos, capabilities nascerem todas ativas ou não houver eventos.

# 16. Related notes

- [[01_CKOS_AI_FIRST_CONSTITUTION]]
- [[03_AGENT_OPERATING_MODEL]]
- [[05_MEMORY_AND_CONTEXT_ARCHITECTURE]]
- [[11_DATA_MODEL_AND_PERSISTENCE]]
- [[16_NODE_CANVAS_ARCHITECTURE]]
