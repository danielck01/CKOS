---
title: Taxonomy and Naming
file: 00_TAXONOMY_AND_NAMING.md
phase: 00_SYSTEM_GOVERNANCE
category: taxonomy
version: 2.3.0
status: active
owner: PMO_CKOS
responsible_agent: PMO_CKOS
reviewers:
  - metacognik
approval_required:
  - founder
  - metacognik
purpose: Taxonomia oficial e naming freeze do CKOS — nomes canônicos de sistema, agentes, objetos, execução, runtime, memória e produto.
inputs: Visão CKOS AI First; auditoria de arquitetura 2026-05-24; necessidade de multiagentes e whitelabel.
outputs: Glossário operacional; naming convention; naming freeze; termos proibidos; mapa de objetos e agentes.
framework: 7 famílias — System, Agent, Object, Execution, Runtime, Memory, Product/UI.
edge_cases: Papel sem skill; prompt tratado como skill; dashboard fixo por canal; nome fora do freeze.
integrations: Aplica-se a todos os docs canônicos, schema de dados, prompts e identificadores de runtime.
prompts: Prompt de classificação taxonômica; prompt de decisão agent-vs-skill.
metrics: 0 nomes fora do freeze; redução de papéis duplicados; workflows separados de skills.
related_notes:
  - 00_MASTER_MAP.md
  - 00_DOCUMENT_TEMPLATE.md
  - 00_DEPENDENCY_MAP.md
tags: [governance, taxonomy, naming, freeze, glossary]
---

# 1. Propósito

Definir a taxonomia oficial e o **naming freeze** do CKOS. Sem taxonomia travada, o CKOS vira entropia semântica e os nomes inconsistentes vazam para schema, mentions, prompts e código gerado.

Esta versão `2.0.0` incorpora o naming freeze decidido na auditoria de 2026-05-24.

# 2. Função dentro do CKOS

Fonte única para nomear documentos, objetos, agentes, skills, prompts, nodes, workflows, runtime, memória, transformers e interfaces. Nenhum nome novo de agente/superagent pode ser usado em qualquer doc sem ser registrado aqui primeiro.

# 3. Inputs

- visão CKOS AI First;
- auditoria de arquitetura (2026-05-24);
- necessidade de multiagentes, workflow canvas e whitelabel real;
- necessidade de usar Manus, Claude, Codex e Antigravity sem dependência de uma única ferramenta.

# 4. Outputs

- glossário operacional; naming convention; naming freeze; termos proibidos; mapa de objetos; mapa de agentes.

# 5. NAMING FREEZE OFICIAL (autoridade máxima)

Estes são os **únicos** nomes oficiais de sistema e agentes. Qualquer outro é proibido até ser registrado aqui.

```txt
Sistema:     CKOS
Cognitivo:   Cognik
Metacog.:    Metacognik
Interface:   Nick
Governança:  PMO_CKOS
QA:          QA Lead
Build orq.:  Builder Lead
Build exec.: Builder Subagents
Dados:       Datta
Operações:   Ops
Campanha:    Campaign
```

## 5.1 Correções aplicadas (changelog de naming)

| Forma errada (originais) | Forma oficial | Regra |
|---|---|---|
| `Metaconik`, `@metaconik` | `Metacognik`, `@metacognik` | Defeito de grafia do superagent metacognitivo. |
| `PMO Agent`, `PMO pesquisador` | `PMO_CKOS` | Owner/orquestrador de governança. |
| `QA Agent` | `QA Lead` | Owner de qualidade. |
| `Builder Agent` (orquestra) | `Builder Lead` | Coordena implementação. |
| `Builder Agents` (executam) | `Builder Subagents` | Executores: Frontend, Backend, Data, RAG, Automation, Design System, QA Builder. |
| `Product Architect` | `PMO_CKOS` + skill `product-strategy` | Papel não existia na taxonomia; absorvido por PMO_CKOS; trabalho de produto é skill, não agente novo. |
| `Research Agent` / `Research Ops Agent` | `Research Subagent` + skill `research-pack-generation` | Executor de pesquisa, não orquestrador. Manus é a **tool externa** que cumpre essa skill na fase atual. |
| `Prompt Engineer Agent` | `PMO_CKOS` (owner) + skill `prompt-library-curation` | Curadoria de prompt é skill, não agente. |

## 5.2 Pendência para decisão do Founder

- **Branddock**: presente na taxonomia original como superagent de branding, **ausente** da lista de freeze fornecida no patch. Mantido provisoriamente como superagent registrado, marcado `pending_founder_confirmation`. Se o Founder não confirmar, rebaixar para skill `brand-diagnosis`/`brand-storytelling` sob Ops/Campaign.
- **Agents de domínio** (Lia, Neura, Philo, Story, Visual, Social, Commerce, Media, ROI, Legal/Ethos, CalendarOps, WhatsOps): retidos como **catálogo de hipóteses de agentes**, não como agentes ativos. Nenhum vira agente operacional sem skill contratada (ver §7.4).

# 6. System Terms

## CKOS
Sistema operacional cognitivo e metacognitivo AI First da CKCompany. Não é chatbot, dashboard, ferramenta de tarefas, proposta digital ou agência automatizada.

## AI First
Princípio onde a IA interpreta intenção, cria estrutura, recomenda nodes, aciona agentes, gera outputs, audita decisões, aprende com feedback e solicita aprovação quando necessário.

## Whitelabel
Separação entre arquitetura CKCompany e skin visual/operacional de cada projeto. Whitelabel real inclui tema, linguagem, módulos, agentes, capabilities, workflows, permissões, dados e apresentação — não só cor.

## Capability
Capacidade modular ativada por contexto (Commerce Intelligence, Campaign OS, Research OS…). Capability não é página default.

# 7. Agent Terms

## Founder
Humano responsável pela aprovação estratégica máxima.

## Superagent
Agente de alto nível que orquestra agentes, skills, workflows e decisões: **Nick, Cognik, Metacognik, PMO_CKOS, Builder Lead, QA Lead, Datta, Ops, Campaign** (e Branddock, pendente).

## Agent
Especialista de domínio (catálogo de hipóteses; só ativa com skill contratada).

## Subagent
Executor especializado acionado por agent/superagent: Briefing Parser, Gap Detector, Proposal Builder, Research Subagent, Builder Subagents, etc.

## Nick
Interface conversacional e orquestradora principal com o usuário. Agentic interface, não chat.

## Cognik
Camada cognitiva: interpreta sinais, contexto, padrões, dados e briefing em tempo real.

## Metacognik
Camada metacognitiva: audita qualidade do raciocínio, mede confiança, encontra lacunas, questiona hipóteses e controla risco. **(Grafia única e obrigatória: Metacognik.)**

## PMO_CKOS
Governança operacional: roadmap, dependências, escopo, handoffs, anti-entropia. Owner padrão de docs de governança e execução.

## QA Lead · Builder Lead · Builder Subagents · Datta · Ops · Campaign
Conforme freeze (§5).

### 7.4 Regra agent-vs-skill
Só recomende `agent` se houver domínio contínuo, responsabilidade clara, memória própria, outputs recorrentes e necessidade de orquestração. Caso contrário, é `skill`, `subagent` ou `prompt`.

# 8. Object Terms

`Workspace` · `Project` · `Stakeholder` · `Briefing` (vivo) · `Signal` · `Node` · `Capability` · `Agent` · `Skill` · `Workflow` · `Run` · `Event` · `Decision` · `Approval` · `Artifact` · `Memory` · `Evidence` · `Hypothesis` · `Gap` · `Risk` · `Insight` · `Integration` · `Metric`.

Definições completas em `02_AI_FIRST_OBJECT_MODEL.md` (conceitual) e materialização física em `11_DATA_MODEL_AND_PERSISTENCE.md`.

# 9. Execution Terms

## Skill
Capacidade reutilizável, versionada e auditável. Skill não é prompt.

## Prompt
Instrução textual usada por tool, agente ou workflow. Prompt não é skill nem workflow.

## Instruction
Regra persistente de comportamento.

## Transformer
Tradutor operacional: input bruto → objeto estruturado do sistema. (Não é a arquitetura técnica de LLM.)

## Pipeline
Sequência de transformers, workflows e approvals.

## Tool
Ferramenta externa/interna: Manus, Claude Code, Codex, Antigravity, Apify, Supabase, OpenRouter, Redis, vector store.

# 10. Runtime Terms (novo na v2)

## Event
Fato imutável registrado no event log: `node_created`, `approval_requested`, `run_completed`.

## Event Bus / Event Log
Espinha dorsal de mensageria e a fonte append-only de verdade de execução.

## Workflow Engine
Instancia e conduz workflows como máquinas de estado.

## Agent Router · Model Router · Tool Router
Roteiam, respectivamente, para agentes, modelos (via OpenRouter) e ferramentas, sob política.

## Run Scheduler / Queue
Agenda e enfileira runs com concorrência, retry, timeout e idempotência.

## Approval Gate (runtime)
Ponto de execução onde um workflow pausa aguardando approval, conforme `04_AUTONOMY_AND_APPROVALS.md`.

## UI Projection
Read model derivado de eventos que alimenta dashboards/canvas em tempo real.

## 10.1 Termos de Runtime registrados (v2.1)

Termos oficiais introduzidos com a expansão de `10_SYSTEM_RUNTIME_ARCHITECTURE`. Uso obrigatório nesta grafia:

- **Capability Registry** — catálogo de capabilities ativáveis por contexto (10 §5.14/5.17).
- **Schema Registry** / **Contract Registry** — catálogo de contratos de output (10 §5.20). Sinônimos operacionais; "Schema Registry" é o nome do registry, "Contract Registry" descreve seu papel.
- **State Machine Registry** — catálogo de máquinas de estado (10 §5.25).
- **Policy Registry** — catálogo de políticas de autorização/operação (10 §5.14; 12).
- **Model Registry** — catálogo de modelos disponíveis (10 §5.14).
- **Collector Registry** / **Provider Registry** / **Actor Registry** — ver definições em §10.2.
- **Artifact Registry** — catálogo de tipos de artifact (10 §5.14).
- **Eval Registry** — golden sets e rubricas (10 §5.14; 13).
- **Cost Ledger** — registro de custo por escopo (run/agent/workflow/model/tool/collector/projeto/cliente/dia/mês), base do Cost Guard (10 §5.23; 13).
- **Context Pack Builder** — engine que monta o contexto antes de qualquer chamada de IA (10 §5.19).
- **Evidence Trail** — cadeia de evidências ligadas a hipóteses/decisões, com confiança e origem (10 §5.21).
- **Decision Rights Matrix** — quem decide/aprova o quê (10 §5.22).
- **Run Replay** — reconstrução completa de um run a partir de eventos (10 §5.26).
- **Simulation Mode** / **Sandbox** — execução prevista/isolada sem efeito externo (10 §5.27).
- **Compensating Action** — evento que reverte efeito por compensação, não DELETE (10 §5.13).
- **UI Projection Engine** — engine que mantém read models e faz streaming para a UI (10 §5.15).
- **Learning Loop Engine** — engine que agrega outcomes em aprendizado persistente (10 §5.28).

## 10.2 Collector / Actor / Provider (definições oficiais)

- **Collector** = abstração CKOS **visível para o produto**. É o que a UI conhece e chama (`POST /api/collectors/run`).
- **Actor** = **executor técnico interno** (conta/credencial/sessão) que realiza a coleta. Resolvido server-side, nunca exposto ao frontend.
- **Provider** = **fornecedor/API externa** (Apify, plataforma social, etc.). Nunca chamado direto pelo frontend.

Regra de naming/segurança: frontend nunca expõe provider, token ou actor id (10 §5.18; 12).

# 11. Memory Terms

`Short-term` (sessão) · `Mid-term` (projeto) · `Long-term` (organização) · `RAG` · `Embeddings` · `Context Pack` · `Decision Log` · `Evidence Trail`. Materialização em `11_DATA_MODEL_AND_PERSISTENCE.md`.

# 12. Product/UI Terms

`Command Center` (centro operacional, não busca) · `CommandBar` (roteador de intenção) · `Canvas` (workspace vivo) · `Dashboard` (adaptativo, não fixo) · `Proposal Experience`. Cada um é **projeção do runtime**, não fonte de verdade.

# 13. Naming convention

Documentos: `NN_DOCUMENT_NAME.md`.

Objetos (prefixos oficiais):
```txt
project_, node_, agent_, superagent_, subagent_, skill_, workflow_, run_,
event_, approval_, artifact_, evidence_, hypothesis_, gap_, risk_, capability_,
memory_, decision_, integration_
```

Identificadores de agente em código/mentions usam a grafia exata do freeze: `@nick`, `@cognik`, `@metacognik`, `@pmo_ckos`, `@qa_lead`, `@builder_lead`, `@datta`, `@ops`, `@campaign`.

## 13.1 Regra das três formas de naming (obrigatória)

Todo agente, superagent e papel de aprovação possui **três formas canônicas**, cada uma com uso distinto:

| Forma | Regra | Exemplos |
|---|---|---|
| `system_id` | snake_case obrigatório; usado em: YAML (`approval_required`, `owner`, `responsible_agent`), schema de banco, event log, API, código, registry | `metacognik`, `pmo_ckos`, `qa_lead`, `builder_lead`, `nick`, `cognik`, `datta`, `ops`, `campaign` |
| `display_name` | Capitalização humana; usado em: texto corrido de documentos, UI, relatórios, explicações | `Metacognik`, `PMO_CKOS`, `QA Lead`, `Builder Lead`, `Nick`, `Cognik`, `Datta`, `Ops`, `Campaign` |
| `mention` | `@` + `system_id`; usado em: menções em docs, prompts, logs de handoff, threads de decisão | `@metacognik`, `@pmo_ckos`, `@qa_lead`, `@builder_lead`, `@nick`, `@cognik`, `@datta`, `@ops`, `@campaign` |

**Regras de aplicação:**

1. Em campos YAML de qualquer doc canônico (`approval_required`, `owner`, `responsible_agent`, `reviewers`): usar **sempre** `system_id` (snake_case).
2. Em prosa de documentos, UI e relatórios: usar `display_name`.
3. Em menções diretas a agentes em prompts, logs, threads e handoffs: usar `mention` (`@system_id`).
4. **Proibido:** misturar formas no mesmo campo — e.g., `approval_required: PMO_CKOS` (display_name num campo de enum), `@Metacognik` (display_name com @).
5. O `system_id` é a forma raiz; `display_name` e `mention` derivam dele e nunca o contradizem.

```txt
Tabela canônica de formas:

system_id       display_name    mention
─────────────────────────────────────────────────
nick            Nick            @nick
cognik          Cognik          @cognik
metacognik      Metacognik      @metacognik
pmo_ckos        PMO_CKOS        @pmo_ckos
qa_lead         QA Lead         @qa_lead
builder_lead    Builder Lead    @builder_lead
datta           Datta           @datta
ops             Ops             @ops
campaign        Campaign        @campaign
```

## 13.2 Naming para uploads e study notes

Uploads RAW em `000_UPLOADS/` usam obrigatoriamente:

```txt
YYYYMMDD_source-tool_topic_owner_status.ext
```

Exemplo:

```txt
20260527_chatgpt_mcp-connectors-research_pmo_ckos_raw.md
```

Study notes em `000_STUDY_NOTES/` usam obrigatoriamente:

```txt
YYYYMMDD_study_topic_responsible-agent_status.md
```

Exemplo:

```txt
20260527_study_mcp-connectors-policies_pmo_ckos_draft.md
```

Regras:

1. Data sempre em `YYYYMMDD`.
2. `source-tool` sempre em snake_case ou nome curto normalizado (`chatgpt`, `claude`, `codex`, `manus`, `antigravity`, `apify`, `manual`, `other`).
3. `topic` usa kebab-case curto e descritivo.
4. `owner` e `responsible-agent` usam `system_id` em snake_case.
5. `status` deve expressar estado operacional simples: `raw`, `draft`, `review`, `approved`, `archived`, `rejected`.

## 13.3 Diferenca taxonomica entre RAW, STUDY, patch candidate e canonico

| Tipo | Camada | Autoridade | Uso correto |
|---|---|---|---|
| raw source | `raw` | nenhuma autoridade canonica | preservar origem bruta e provenance |
| study note | `study` | interpretacao PMO, nao canonica | resumir, comparar, medir risco, confidence e lacunas |
| patch candidate | `study` | proposta, nao patch aplicado | preparar mudanca canonica para approval |
| canonical doc | `canonical` | fonte oficial versionada | registrar arquitetura aprovada |

Regra: `system_id` continua em snake_case, `display_name` continua humano e `mention` usa `@system_id`.

# 14. Termos proibidos ou restritos

Proibidos como descrição principal: chatbot; dashboard bonito; automação de prompt; gerador de relatório; template; painel fixo; IA assistente genérica.

Proibidos como naming: `Metaconik`, `PMO Agent`, `QA Agent`, `Product Architect`, `Research Agent`, `Prompt Engineer Agent`.

Restritos: `Dashboard` (só com visão estruturada e adaptativa); `Agent` (só com skill+gate); `Skill` (≠ prompt); `AI First` (só se a IA não apenas responde texto); `Autônomo` (só com nível de autonomia + approval gate).

# 15. Prompts relacionados

```txt
Classifique esta ideia na taxonomia CKOS: é Project, Node, Workflow, Skill, Prompt, Agent, Subagent, Capability, Dashboard, Artifact, Evidence, Decision, Approval, Memory, Event ou Tool? Explique e indique onde documentar.
```

```txt
Antes de criar um agente, avalie se a função deveria ser skill, subagent, workflow ou prompt. Só recomende agent com domínio contínuo, responsabilidade clara, memória própria, outputs recorrentes e necessidade de orquestração.
```

# 16. Related notes

- [[00_MASTER_MAP]]
- [[00_DOCUMENT_TEMPLATE]]
- [[00_DEPENDENCY_MAP]]
- [[02_AI_FIRST_OBJECT_MODEL]]
- [[03_AGENT_OPERATING_MODEL]]
- [[11_DATA_MODEL_AND_PERSISTENCE]]
