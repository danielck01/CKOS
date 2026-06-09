---
title: Memory and Context Architecture
file: 05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
phase: 01_THINKING_SYSTEM
category: memory
version: 1.2.0
status: active
owner: Cognik
responsible_agent: Cognik
reviewers:
  - Metacognik
approval_required:
  - founder
purpose: Definir como o CKOS armazena, recupera, prioriza e audita contexto — camadas de memória, RAG, embeddings, trust hierarchy, context packets, expiração e permissões.
inputs: Conversas; arquivos; briefings; decisions; approvals; nodes; runs; artifacts; dados externos; outputs; eventos; métricas; feedback.
outputs: Contexto recuperado; memórias gravadas; embeddings; evidências; logs; resumos; knowledge packs; project/agent/stakeholder memory.
framework: Curto/médio/longo prazo + tipos de contexto + RAG pipeline + hierarquia de confiança + context packet + expiração.
edge_cases: Memória contraditória; RAG irrelevante; usuário muda decisão; whitelabel muda identidade; memória sensível.
integrations: Materialização física em 11_DATA_MODEL; permissões em 12_SECURITY; qualidade de RAG em 13_EVALS.
prompts: Context packet; conflito de memória; gravação de memória.
metrics: Respostas com contexto correto; redução de repetição; tempo de recuperação; precisão RAG; decisions com evidence.
related_notes:
  - 02_AI_FIRST_OBJECT_MODEL.md
  - 03_AGENT_OPERATING_MODEL.md
  - 04_AUTONOMY_AND_APPROVALS.md
  - ../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
tags: [thinking, memory, rag, context, trust_hierarchy]
---

# 1. Propósito

Definir como o CKOS armazena, recupera, prioriza e audita contexto. AI First real depende de memória: sem ela, o sistema vira chat repetitivo; com memória mal organizada, alucina, duplica decisões, gera ruído e perde confiança.

> Este documento define a **política** de memória. A **materialização física** (Postgres, vetor, Redis, storage) está em `11_DATA_MODEL_AND_PERSISTENCE.md`; a **qualidade de recuperação** (eval de RAG) em `13_EVALS`.

# 2. Função dentro do CKOS

Orienta memória curta/média/longa, RAG, embeddings, context routing, decision logs, evidence trail, recuperação por agente, esquecimento controlado, privacidade e whitelabel context.

# 3. Inputs

Conversas; arquivos; briefings; decisions; approvals; nodes; runs; artifacts; dados externos; outputs de agentes; eventos; métricas; feedback do usuário.

# 4. Outputs

Contexto recuperado; memórias gravadas; embeddings; evidências; logs; resumos; knowledge packs; project/agent/stakeholder memory.

# 5. Framework operacional

## 5.1 Camadas de memória

- **Curta**: sessão atual — conversa, comandos recentes, nodes abertos, agente ativo, arquivos enviados agora, estado temporário do Canvas. (Física: Redis.)
- **Média**: projeto em andamento — briefing vivo, hipóteses, decisões pendentes, agents ativos, artifacts em revisão, último diagnóstico, status de workflows. (Física: Postgres + vetor.)
- **Longa**: conhecimento persistente — identidade da marca, decisões aprovadas, histórico, aprendizados, stakeholders, performance, propostas, docs, outputs finais. (Física: Postgres + vetor + storage.)

## 5.2 Tipos de contexto

```txt
Conversation · Project · Brand · Stakeholder · Agent · Decision · Evidence · Artifact · Workflow · Technical
```

## 5.3 RAG

RAG recupera contexto relevante, não joga documentos inteiros no prompt.

```txt
query/intention → classify context need → retrieve candidates → rank by relevance
→ filter by permission → summarize context → attach evidence refs → send to agent → log what was used
```

O `filter by permission` é aplicado conforme `12_SECURITY`. A qualidade desse pipeline é avaliada em `13_EVALS §RAG retrieval quality`.

## 5.4 Embeddings

Para busca semântica em docs, briefings, decisions, artifacts, insights, project notes, stakeholder comments, research packs e implementation briefs. **Não usar embeddings como única fonte de verdade** — dados estruturados e decision logs têm prioridade.

## 5.5 Hierarquia de confiança

```txt
1. Approved decision
2. Signed contract / proposal
3. Structured database record
4. User direct instruction
5. Recent project artifact
6. Retrieved document
7. Agent inference
8. External web/research reference
9. Weak hypothesis
```

Conflito → Metacognik aciona revisão.

## 5.6 Memory object

```yaml
memory_id:
project_id:
user_id:           # novo — PROMOTE-U2: memória escopada por usuário, persistente entre projetos (AQ-IO-3 resolvida)
workspace_id:
type:
source_object:
content:
summary:
embedding_ref:
confidence:
permission_level:
created_by:
reviewed_by:
valid_until:
related_nodes:
related_decisions:
```

### 5.6.1 Escopo de memória: project, workspace, user (PROMOTE-U2)

A partir do PATCH 2, o `memory_object` admite **três dimensões de escopo simultâneas**, cada uma opcional dependendo do tipo da memória:

| Campo | Quando preencher | Lifecycle |
|---|---|---|
| `project_id` | memória ligada a um projeto específico (briefing vivo, decisões do projeto, artifacts) | dura enquanto o projeto está ativo + retenção pós-arquivamento conforme `12_SECURITY` |
| `workspace_id` | memória organizacional (políticas do workspace, identidade da marca, stakeholders comuns) | dura enquanto o workspace existir |
| `user_id` | memória do usuário **entre projetos** (preferências de resposta, autonomy preferences, tribos scored, User Operating DNA refs, padrões de decisão observados) | dura enquanto o User existir; sobrevive ao arquivamento de projetos |

**Regras de combinação:**
- Memória pode ter **um, dois ou os três escopos** preenchidos. Exemplos:
  - `{project_id, workspace_id}` — memória clássica de projeto (comportamento atual antes do PATCH 2)
  - `{user_id, workspace_id}` — preferências do usuário dentro de uma organização
  - `{user_id}` — preferência cross-workspace do usuário (rara; geralmente Founder-only)
- **Permission filter (`12_SECURITY`)** continua sendo aplicado: um usuário não enxerga memória `user_id` de outro usuário, mesmo no mesmo workspace, salvo se `permission_level` autorizar (default: deny).
- **Trust hierarchy (§5.5)** permanece: memória escopada `user_id` não tem prioridade especial — segue a mesma ordem (approved decision > signed contract > structured DB > etc.).
- **Esquecimento e expiração (§5.8)**: memória `user_id` tem retenção independente do ciclo de vida de projetos. Limpeza por solicitação explícita do usuário (LGPD) ou por `valid_until`.

Materialização física (índices `user_id`, RLS, namespace de vetor) é especificada em `11_DATA_MODEL` como patch candidate posterior — esta seção define apenas a **política**.

## 5.7 Context packet

```yaml
task:
project_summary:
relevant_decisions:
active_nodes:
constraints:
stakeholders:
evidence:
memory_refs:
approval_rules:
expected_output:
```

Montado pelo runtime antes de cada run (ver `10_RUNTIME §Context Assembler`).

## 5.8 Esquecimento e expiração

Expirar/revalidar: hipóteses antigas; dados de mercado; preços; métricas de campanhas; status de integração; preferências não confirmadas; outputs não aprovados.

# 6. Agente responsável

`Cognik` recupera e organiza contexto; `Metacognik` audita conflito, confiança e qualidade.

# 7. Superagentes envolvidos

Nick (usa contexto para responder); Cognik (recupera/interpreta); Metacognik (audita); Datta (valida dados estruturados); PMO_CKOS (memória de roadmap); Builder Lead (memória técnica); QA Lead (memória de regressão).

# 8. Skills necessárias

context-routing; memory-write; memory-retrieval; semantic-search; evidence-ranking; contradiction-detection; summarization; expiration-policy; permission-filtering.

# 9. Prompts relacionados

```txt
Monte um pacote de contexto mínimo suficiente para este agente executar a tarefa sem excesso de informação e sem perder decisões críticas.
```

```txt
Compare estas fontes e identifique qual deve prevalecer segundo a hierarquia de confiança. Se houver incerteza, solicite revisão.
```

```txt
Classifique este output: memória curta, média, longa, decision log, evidence ou apenas evento temporário?
```

# 10. Integrações

Supabase relacional; vector store; Redis; storage de arquivos; Obsidian/RAG; OpenRouter; logs de agents; event bus; analytics; permission system. Mapeamento físico em `11_DATA_MODEL`.

# 11. Memória e contexto

Regras: decisions aprovadas e artifacts finais → memória longa; hipóteses → memória média até validação; dados externos expiram; outputs rejeitados não são fonte forte; approvals têm prioridade sobre inferências.

# 12. Edge cases

- **Memória contraditória** → Metacognik cria conflict event.
- **RAG irrelevante** → agente declara baixa confiança e pede melhor contexto.
- **Usuário muda decisão** → nova decision, preservar histórico, não sobrescrever sem log.
- **Whitelabel muda identidade** → atualizar project theme memory, preservar core CK architecture.
- **Memória sensível** → permission filter antes do retrieval (12_SECURITY).

# 13. Métricas de sucesso

Respostas com contexto correto; redução de repetição; tempo de recuperação; conflitos detectados; precisão de RAG; decisions com evidence; outputs rejeitados por contexto errado; custo de contexto/run; % de memória expirada corretamente.

# 14. Critérios de aprovação

Aprovado se define três camadas, separa RAG de dado estruturado, define hierarquia de confiança, prevê context packets, expiração, permissões e execução por agentes.

# 15. Critérios de reprovação

Reprovado se memória for só histórico de chat, RAG for solução única, ou faltar trust hierarchy, expiração, permission filter ou decision logs.

# 16. Related notes

- [[02_AI_FIRST_OBJECT_MODEL]]
- [[03_AGENT_OPERATING_MODEL]]
- [[04_AUTONOMY_AND_APPROVALS]]
- [[11_DATA_MODEL_AND_PERSISTENCE]]
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]]
