---
title: Transformers and Pipelines
file: 09_TRANSFORMERS_AND_PIPELINES.md
phase: 02_EXECUTION_SYSTEM
category: transformers
version: 1.1.0
status: active
owner: Cognik
responsible_agent: Cognik
reviewers:
  - Metacognik
approval_required:
  - founder
  - PMO_CKOS
  - Metacognik
purpose: Definir como o CKOS transforma entradas brutas em objetos úteis, auditáveis e acionáveis. Transformer aqui é peça operacional, não a arquitetura técnica de LLM.
inputs: Object Model; Memory; Skills; Workflows; sinais brutos.
outputs: Tipos de transformers; pipeline mestre; transformer registry; transformers MVP.
framework: Input → objeto estruturado → node → workflow → output → decisão → memória.
edge_cases: Input ambíguo; dados insuficientes; node desnecessário; RAG antigo; output vira relatório; automação sem aprovação.
integrations: Executados pelo runtime (10); persistem em 11; avaliados em 13.
prompts: Ver 08_PROMPT_LIBRARY.
metrics: Intenção detectada corretamente; nodes aceitos; perguntas úteis; redução de prompts manuais; precisão RAG.
related_notes:
  - 02_AI_FIRST_OBJECT_MODEL.md
  - 05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - 07_WORKFLOW_BLUEPRINTS.md
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
tags: [execution, transformers, pipelines, rag, mvp]
---

# 1. Propósito

Definir como o CKOS transforma entradas brutas em objetos úteis, auditáveis e acionáveis.

# 2. Função dentro do CKOS

**Transformer não é a arquitetura técnica de modelos de linguagem.** É uma peça operacional que converte um estado bruto em um objeto estruturado do sistema:

```txt
Conversa solta → intenção detectada → briefing vivo → node sugerido → workflow → tarefa → agente → artifact → decisão → memória
```

> O **pipeline mestre canônico** (§5.1) é definido aqui e referenciado pelos demais docs; Command Center (15) e Workflows (07) **não o redefinem**, apenas apontam para cá. (Correção de redundância da auditoria.)

# 3. Inputs

Object Model (02); Memory (05); Skills (06); Workflows (07); sinais brutos.

# 4. Outputs

Tipos de transformers; pipeline mestre; transformer registry; transformers MVP.

# 5. Framework operacional

## 5.1 Pipeline mestre AI First (fonte canônica)

```txt
Input → Intent Detection → Context Retrieval → Object Mapping → Transformer Selection
→ Agent Routing → Skill Execution → Partial Output → Metacognitive Audit → Approval Gate
→ Artifact Creation → Memory Update → Next Best Action
```

A execução física desse pipeline (event bus, routers, scheduler) está em `10_SYSTEM_RUNTIME_ARCHITECTURE.md`.

## 5.2 Tipos de transformers

- **Intent**: linguagem natural → intenção operacional.
- **Briefing**: respostas fragmentadas → briefing vivo (sections, gaps, hypotheses, confidence).
- **Node**: hipótese/necessidade → node (status, prioridade, activation_trigger).
- **Evidence**: dados brutos → evidências.
- **Proposal**: diagnóstico vivo → seções de proposta.
- **Artifact**: outputs → artifacts reutilizáveis.
- **Memory**: aprendizado → memória curta/média/longa.

## 5.3 Pipelines especializados

- **Briefing inteligente**: user message → intent → briefing → gap detector → hypothesis builder → node suggestion → Metacognik audit → Nick next best question → live briefing update.
- **Proposta → sistema**: proposal accepted → scope → plan → agent contract → workspace creator → dashboard initializer → node activator → approval policy loader → memory seeding → operation started.
- **Pesquisa tipo Manus**: research command → scope extractor → source planner → reference collector → relevance scorer → rights checker → insight extractor → shortlist builder → implementation brief generator → artifact pack → memory update.
- **Implementação**: implementation brief → risk classifier → executor selector → task decomposition → file impact map → code gen/refactor → build/test → QA report → founder approval → merge/deploy.

## 5.4 Embeddings, RAG e memória nos pipelines

Embeddings: buscar contexto similar, comparar projetos, recuperar decisões, encontrar referências, detectar repetição de erro. RAG: recuperação contextual antes de gerar/decidir — **nenhum agente gera decisão estratégica sem consultar memória relevante quando ela existe**. Materialização em `11`, qualidade em `13`.

## 5.5 Transformer registry

```yaml
transformer_id:
name:
input_object:
output_object:
owner_agent:
review_agent:
related_skill:
related_workflow:
risk_level:
approval_required:
metrics:
```

## 5.6 Transformers prioritários MVP

| Transformer | Input | Output | Owner |
|---|---|---|---|
| `intent_to_object` | mensagem | intent + object candidates | Nick |
| `briefing_to_live_diagnostic` | respostas | briefing vivo + lacunas | Cognik |
| `gap_to_question` | lacuna | próxima pergunta | Nick |
| `hypothesis_to_node` | hipótese | node sugerido | Cognik |
| `research_to_pack` | comando pesquisa | artifact pack | Research Subagent |
| `proposal_to_workspace` | proposta aprovada | projeto operacional | PMO_CKOS |
| `decision_to_memory` | decisão | memória versionada | Metacognik |

# 6. Agente responsável

`Cognik` é owner dos transformers.

# 7. Superagentes envolvidos

Nick; Cognik; Metacognik; PMO_CKOS; Research Subagent (executor).

# 8. Skills necessárias

signal-classification; node-creation; research-pack-generation; proposal-scoping; memory-write.

# 9. Prompts relacionados

Em `08_PROMPT_LIBRARY.md`.

# 10. Integrações

Runtime (10) executa; persistência (11); evals de RAG (13); model router (10).

# 11. Memória e contexto

`decision_to_memory` e `Memory transformers` alimentam as 3 camadas (05/11).

# 12. Edge cases

Input ambíguo; dados insuficientes; transformer cria node desnecessário; agente executa com contexto errado; RAG recupera info antiga/irrelevante; memória contraditória; output vira relatório em vez de decisão; transformer automatiza ação que precisava de aprovação.

# 13. Métricas de sucesso

Intenção detectada corretamente; nodes aceitos; perguntas úteis; redução de prompts manuais; tempo input→next best action; retrabalho por contexto errado; precisão RAG; decisões com evidência vinculada.

# 14. Critérios de aprovação

Transformer aprovado se tem input/output claro, reduz trabalho humano, não oculta risco, registra memória, é auditável, tem fallback manual e respeita approval gates.

# 15. Critérios de reprovação

Reprovado se input/output ambíguo, oculta risco, não registra memória, não é auditável, sem fallback ou ignora approval gate.

# 16. Related notes

- [[02_AI_FIRST_OBJECT_MODEL]]
- [[05_MEMORY_AND_CONTEXT_ARCHITECTURE]]
- [[07_WORKFLOW_BLUEPRINTS]]
- [[10_SYSTEM_RUNTIME_ARCHITECTURE]]
