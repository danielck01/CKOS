---
title: QA and Founder Approval Protocol
file: 20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md
phase: 05_IMPLEMENTATION_SYSTEM
category: qa
version: 1.2.0
status: draft
owner: PMO_CKOS
responsible_agent: QA Lead
reviewers:
  - Metacognik
  - founder
  - technical
  - qa_lead
approval_required:
  - founder
  - technical
  - metacognik
purpose: >
  Define the full QA and approval system for CKOS: Gates A–K, domain-specific checklists,
  Decision Rights Matrix, Founder/Metacognik/Technical approval protocols, rejection criteria,
  state machine for approvals, and release readiness framework. Every document, migration,
  runtime module, UI surface, agent action, and business system must pass explicit QA,
  approval, and rollback criteria before becoming canonical.
inputs:
  - Runtime Architecture (10 v1.1.0)
  - Data Model and Schema (11 v1.1.2)
  - Security and Policy (12 v1.1.0)
  - Evals, Observability and Cost Control (13 v1.1.0)
  - Autonomy and Approvals (04)
  - Implementation Protocol (17 v1.2.1)
  - Research Protocol (18 v1.0.0)
  - Claude/Codex/Antigravity Execution Protocol (19 v1.0.0)
outputs:
  - QA Gate System A–K (11 gates with criteria, verifiers, unblocks)
  - Decision Rights Matrix (16 decision types)
  - Domain QA Checklists (14 domains)
  - Founder Approval Protocol (format, SLA, absence handling)
  - Metacognik Veto Protocol (veto conditions, format, escalation)
  - Technical Approval Protocol (review steps, scope)
  - QA Report Format (mandatory template)
  - Release Readiness Checklist
  - State Machine for Approvals (10 states)
  - Rejection Criteria (automatic and formal)
  - MVP P0 QA Scope definition
framework: >
  Gate submission → domain QA → approval routing → actor decision →
  record → advance or rollback
edge_cases: >
  Founder non-responsive; QA/Metacognik conflict; beautiful delivery without function;
  AI output approved prematurely; multi-gate deadlock; security veto after approval;
  evidence insufficient for gate passage; cost spike post-approval; approval actor conflict;
  stale approval expiry; emergency patch during active gate review
integrations:
  - Runtime event bus (10)
  - Data Model projections (11)
  - Security policy engine (12)
  - Evals and cost controls (13)
  - Implementation Protocol gates (17)
  - Research pipeline (18)
  - AI tool execution protocol (19)
  - Audit logs (all domains)
prompts: >
  QA Lead prompt; Metacognik prompt; Founder briefing template; Technical review checklist;
  Veto format; Approval request format; QA Report template
metrics:
  - Gate passage rate per gate (%)
  - Rejection rate by domain (%)
  - Time from submission to decision (hours)
  - Rollback rate post-approval (%)
  - Metacognik veto rate (%)
  - Stale approval rate (approvals >90d without close)
related_notes:
  - ../01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md
  - ../03_RUNTIME_SYSTEM/10_RUNTIME_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_SCHEMA.md
  - ../03_RUNTIME_SYSTEM/12_SECURITY_AND_POLICY.md
  - ../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - 17_IMPLEMENTATION_PROTOCOL.md
  - 18_RESEARCH_PROTOCOL.md
  - 19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md
  - ../ARCHITECTURE_PATCH_REPORT.md
  - ../QA_DOCUMENTATION_CHECKLIST.md
tags: [implementation, qa, approval, founder, gates, governance, rollback, rejection, metacognik]
supersedes: 20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md v1.1.0
---

> **TESE CENTRAL — DOC 20:**
> CKOS cannot ship by confidence alone. Every document, migration, runtime module,
> UI surface, agent action, and business system must pass explicit QA, approval,
> and rollback criteria before becoming canonical. Approval is evidence-based,
> actor-attributed, time-stamped, and reversible.

---

# 1. Propósito

Definir o sistema completo de QA e aprovação do CKOS:

- Quem pode aprovar o quê, com qual evidência mínima
- Quais domínios têm checklists específicos
- Como os Gates A–K funcionam como fronteiras explícitas de avanço
- O que constitui evidência suficiente para aprovação
- Como rejeições são registradas e tratadas
- Como rollbacks são acionados e executados
- Quando o Founder deve ser acionado obrigatoriamente
- Quando Metacognik pode exercer veto incondicional

```txt
QA no CKOS não é revisão subjetiva. QA é um sistema de gates, critérios,
evidências, atores, rejeições, rollback e rastreabilidade total.
```

---

# 2. O que é — e o que não é — QA no CKOS

## O que é QA no CKOS

- Um sistema de gates formais (A–K) com critérios explícitos por domínio
- Um conjunto de checklists por área (documentação, schema, runtime, agentes, UI, etc.)
- Um protocolo de approval routing com atores, papéis e SLAs definidos
- Um mecanismo de rejeição com causa formal, não opinião
- Uma política de rollback obrigatória para toda aprovação de produção
- Um registro auditável de todas as decisões (quem, quando, com qual evidência)

## O que não é QA no CKOS

- Não é revisão subjetiva ("ficou bom?")
- Não é aprovação automática por AI tool
- Não é velocidade de entrega — é segurança de entrega
- Não é contornar um gate porque o prazo está apertado
- Não é aprovação informal via chat ou mensagem de voz
- Não é revisão feita pelo mesmo ator que criou o artefato (exceto auto-approval P4)
- Não é único ponto de controle — é sistema de camadas

---

# 3. Princípio Central

> **CKOS cannot ship by confidence alone.**
>
> Toda aprovação exige: (a) critério verificável cumprido; (b) ator humano identificado;
> (c) timestamp e referência de evidência; (d) rollback plan definido antes da aprovação.
>
> AI tools auxiliam revisão — não são atores de aprovação. Metacognik audita raciocínio —
> não é substituto de aprovação formal. Velocidade nunca justifica pulação de gate.

---

# 4. Filosofia de QA

1. **Gate-first:** Nada avança sem gate explícito — nem protótipos, nem "só para testar"
2. **Evidence-based:** Toda aprovação referencia evidência concreta (doc, teste, log, score)
3. **Actor-attributed:** Toda decisão tem um humano responsável com nome e timestamp
4. **Rollback-mandatory:** Toda aprovação de P0/P1/P2 tem rollback plan antes da aprovação
5. **Veto-preserved:** Metacognik pode bloquear qualquer aprovação sem evidência suficiente
6. **Founder-final:** Em conflito de atores ou decisão estratégica, Founder tem palavra final
7. **Audit-permanent:** Decisões não são deletadas — são arquivadas com justificativa
8. **Rejection-is-progress:** Rejeição com causa formal acelera o projeto — aprovação sem critério o afunda
9. **AI-output-last:** Output de AI tool nunca é canônico sem revisão humana (ver §23)
10. **One-gate-at-a-time:** Gates são sequenciais — não se abre Gate F enquanto Gate E tem bloqueador aberto
11. **Formal-channel-only:** Aprovações informais (chat, voz, emoji) não têm validade operacional
12. **Cross-domain-consistency:** QA de um domínio verifica consistência com todos os docs 10–19

---

# 5. Atores de Aprovação

## 5.1 Founder

| Atributo | Valor |
|---|---|
| Papel | Autoridade estratégica final: produto, pricing, produção, relações externas, decisões irreversíveis |
| Veto power | Absoluto em decisões estratégicas |
| Auto-approve | Não — Founder aprova explicitamente ou delega formalmente |
| SLA P0 | 6h |
| SLA P1 | 48h |
| SLA P2 | 5 dias úteis |
| SLA P3 | 2 semanas |
| Ausência P0 | Technical Lead faz decisão de emergência com revisão pós-hoc obrigatória do Founder |
| Ausência P1+ | Gate permanece bloqueado; PMO_CKOS escalona a cada 24h |

## 5.2 Technical Lead

| Atributo | Valor |
|---|---|
| Papel | Autoridade técnica: schema, segurança, runtime, integrações externas, riscos técnicos |
| Veto power | Sim — em segurança, integridade de schema, risco técnico crítico |
| Auto-approve | Sim — para P3/P4 reversível dentro de política |
| SLA P0 | 6h |
| SLA P1 | 24h |
| SLA P2 | 3 dias úteis |
| SLA P3 | 1 semana |

## 5.3 Metacognik

| Atributo | Valor |
|---|---|
| Papel | Auditor de evidência e raciocínio: bloqueia contradições, aprovações sem evidência, scope creep, outputs de AI sem validação |
| Veto power | Sim — em qualidade de evidência, contradições entre docs, AI output sem revisão humana |
| Auto-approve | Nunca — Metacognik é sempre review-based |
| SLA P0 | 4h |
| SLA P1 | 24h |
| SLA P2 | 3 dias úteis |
| Override | Founder pode sobrescrever veto Metacognik com nota formal de aceitação de risco |

## 5.4 QA Lead

| Atributo | Valor |
|---|---|
| Papel | Execução de QA por domínio: verifica que a entrega satisfaz os critérios definidos |
| Veto power | Sim — em critérios de domínio específicos |
| Auto-approve | Sim — para P3/P4 dentro do escopo de auto-approval definido em §5.5 |
| SLA P0 | 4h |
| SLA P1 | 24h |
| SLA P2 | 3 dias úteis |

## 5.5 PMO_CKOS

| Atributo | Valor |
|---|---|
| Papel | Orquestrador de processo: sequência de gates, rastreamento de aprovações abertas, escalonamento de bloqueadores |
| Veto power | Não — autoridade de processo, não de decisão |
| Auto-approve | Sim — para P4 (documentação interna, process decisions) |
| Responsabilidade | Emitir approval request no formato correto; garantir routing correto; registrar decisão final |

## 5.6 Auto-Approval Permitido

Permitido quando TODOS os critérios abaixo são verdadeiros:
- Impacto P3 ou P4
- Reversível sem consequência de dados
- Segue política existente sem alteração
- QA Lead ou PMO_CKOS aprova
- Custo < threshold definido em doc 13
- Não afeta dados sensíveis
- Não altera contrato, pricing ou escopo de produto
- Não cria novo agente, novo provider ou novo schema

Exemplos válidos: atualizar docs internos, organizar arquivos, rascunho de node, insight interno, resumo de pesquisa.

---

# 6. Decision Rights Matrix

| Tipo de Decisão | Pode Aprovar | Mínimo Necessário | Veto Metacognik | Founder Obrigatório |
|---|---|---|:---:|:---:|
| Criação de novo doc | PMO_CKOS | PMO_CKOS | Não | Não |
| Reescrita major de doc | PMO_CKOS + Metacognik | 2 atores | Sim | Opcional |
| Schema change (aditivo) | Technical | Technical | Não | Não |
| Schema change (breaking) | Technical + Founder | 2 atores | Sim | Sim |
| Novo evento no event catalog | Technical | Technical | Não | Não |
| Nova projeção | Technical + QA Lead | 2 atores | Não | Não |
| Novo agente registrado | PMO_CKOS + Technical | 2 atores | Sim | Sim |
| Aumento de autonomy_level | Metacognik + Founder | 2 atores | Sim | Sim |
| Novo provider externo (pago) | Technical + Founder | 2 atores | Sim | Sim |
| Mudança de política de segurança | Technical + Metacognik | 2 atores | Sim | Sim |
| Deploy de produção | Todos os 3 atores | 3 atores | Sim | Sim |
| Novo pricing/plano | Founder | 1 ator | Não | Sim |
| Nova superfície de UI | QA Lead + Technical | 2 atores | Não | Opcional |
| Novo sistema de negócio (21–24) | PMO_CKOS + Founder | 2 atores | Sim | Sim |
| Rollback de produção | Technical | 1 ator | Não | Post-hoc |
| Emergency patch P0 | Technical | 1 ator | Não (post-hoc) | Post-hoc |

---

# 7. Sistema de Gates A–K

Os 11 gates são sequenciais. Nenhum gate avança enquanto o anterior tem bloqueador aberto sem resolução formal.

## Gate A — Documentation Gate

**Valida:** Todos os docs de fundação (10–20) completos, consistentes e em status draft-aprovado ou superior.

**Critérios obrigatórios:**
1. Todos os docs 10–20 presentes na pasta `CKOS_DOCUMENTATION_REVIEWED`
2. YAML front matter completo e válido em cada doc (title, version, owner, reviewers, approval_required)
3. Nenhuma referência cruzada quebrada (`[[doc_name]]` sem arquivo correspondente)
4. Nenhuma contradição entre docs flagrada pelo Metacognik sem resolução registrada
5. ARCHITECTURE_PATCH_REPORT atualizado com todos os patches sugeridos nos docs 10–20
6. Nenhuma seção com "TBD" ou "TODO" em docs de fundação
7. Docs que supersederam versões anteriores marcados com campo `supersedes`
8. Sequência documental canônica correta (17→18→19→20→21→22→23→24)

**Verifiers:** PMO_CKOS (sequência e completude), Metacognik (consistência e contradições)

**Aprovação:** Founder + Technical + Metacognik

**Desbloqueia:** Submissão de Gate B

**Rollback se falha:** Doc retorna a draft; issue específica registrada; re-submissão requer resolução de todos os bloqueadores

---

## Gate B — Data Model Gate

**Valida:** Todos os schemas de doc 11 formalmente revisados; RLS verificado; plano de migração revisado.

**Critérios obrigatórios:**
1. RLS ativo em cada tabela de domínio (sem exceção)
2. `tenant_id`, `org_id`, `workspace_id` presentes em todas as tabelas aplicáveis
3. Nenhum token, secret ou credencial em tabela normal — apenas `secret_ref` apontando para vault
4. Todos os foreign keys definidos e documentados
5. Todos os enums documentados com valores permitidos
6. Namespace de vetor + tenant como pré-condição de busca semântica (não pós-filtro)
7. Indexes em `tenant_id`, `project_id`, `workspace_id` em todas as tabelas consultadas
8. Campos de audit trail (`created_by`, `updated_by`, `created_at`, `updated_at`, `archived_at`) em tabelas mutáveis
9. Soft delete implementado para registros auditáveis
10. `source_event_id` em registros gerados por eventos
11. Patches sugeridos nos docs 15, 16, 18, 19 registrados em ARCHITECTURE_PATCH_REPORT

**Verifiers:** Technical Lead (schema e RLS), Metacognik (completude e consistência com doc 11)

**Aprovação:** Technical + Metacognik (Founder se breaking change)

**Desbloqueia:** Gate C

---

## Gate C — Runtime Core Gate

**Valida:** Event bus, event sourcing, CQRS, projection engine.

**Critérios obrigatórios:**
1. Topologia do event bus documentada e alinhada com doc 10 §5.3
2. Todos os eventos de domínio no event catalog com schema, publisher e subscribers
3. Separação CQRS: read model e write model distintos
4. Nenhuma mutação direta de tabela — toda mudança de estado via evento
5. Policy engine com deny-by-default implementado
6. `audit_log` com entrada para toda mudança de estado
7. Rollback plan definido por tipo de evento
8. Projeções atualizadas por eventos, não por chamadas de API
9. Agent actions passam pelo `agent_router`

**Verifiers:** Technical Lead

**Aprovação:** Technical + Metacognik

**Desbloqueia:** Gate D

---

## Gate D — Security Gate

**Valida:** RLS, ABAC, tenant isolation, deny-by-default, audit trails completos.

**Critérios obrigatórios:**
1. RLS ativo e testado em todas as tabelas de domínio
2. ABAC roles definidos para todos os novos recursos
3. Nenhum acesso cross-tenant possível por query padrão
4. Todos os endpoints de API requerem autenticação
5. Nenhum secret hardcoded — secrets exclusivamente via vault/secret manager
6. `audit_log` cobre todos os eventos de segurança (login, mudança de permissão, acesso a dados, export)
7. Frontend nunca chama provider diretamente
8. Nenhum token, `actor_id` ou API key em código client-side
9. Agentes não podem alterar suas próprias políticas de segurança (prevenção de auto-escalação)
10. Isolamento multi-tenant testado em nível de dados
11. Plano de pentest ou revisão de segurança equivalente documentado

**Verifiers:** Technical Lead, Metacognik

**Aprovação:** Founder + Technical + Metacognik

**Desbloqueia:** Gate E

---

## Gate E — Projection Gate

**Valida:** Todas as projeções de UI (doc 11 §21) definidas; frontend lê projeções exclusivamente.

**Critérios obrigatórios:**
1. Todas as 13 projeções de doc 11 §21 definidas com schema
2. Frontend lê projeções — nunca recalcula verdade
3. Nenhum SQL direto de camada de frontend
4. Nenhuma chamada de provider de frontend
5. Triggers de atualização de projeção definidos (qual evento atualiza qual projeção)
6. Política de staleness de projeção definida (quando projeção é considerada stale)
7. Projeções atualizadas por eventos do event bus, não por chamadas de API

**Verifiers:** Technical Lead, QA Lead

**Aprovação:** Technical

**Desbloqueia:** Gate F

---

## Gate F — Product Surface Gate

**Valida:** Command Center, Node Canvas, Project Dashboard alinhados com docs 15, 16, 14.

**Critérios obrigatórios:**
1. Taxonomia de intenção do Command Center implementada (10 famílias de doc 15)
2. Todos os slash commands com `intent_type`, `required_context`, `emitted_event` definidos
3. Slash commands roteiam pelo event bus — não execução direta
4. Object model do Node Canvas alinhado com doc 16 (node types, edge types, state machines)
5. Dashboard lê projeções aprovadas de doc 11 §21
6. Nenhuma lógica de negócio na camada de produto
7. Sistema de tokens whitelabel definido
8. Mobile read-only verificado para Node Canvas
9. Permissões de produto alinhadas com RBAC/ABAC de doc 12

**Verifiers:** QA Lead, Metacognik

**Aprovação:** Founder + Technical

**Desbloqueia:** Gate G

---

## Gate G — Agent Runtime Gate

**Valida:** Registry de agentes, orquestração, autonomy levels, audit trails de ações.

**Critérios obrigatórios:**
1. Todos os agentes registrados em `agent_registry` (system_id, display_name, skills, autonomy_level)
2. Autonomy levels enforced pela policy engine
3. Nenhuma auto-escalação de agente possível (bloqueada por política)
4. Human-in-the-loop para `autonomy_level ≥ 3`
5. Custos de agente rastreados por run
6. Entrada de `audit_log` para cada ação de agente
7. Agente não pode alterar próprio registry ou política
8. Rollback plan definido por tipo de ação de agente
9. Output de agente passa por `output_validator` antes de escrever
10. Nenhum agente chama provider externo diretamente — via `collector_runner` apenas

**Verifiers:** Technical Lead, Metacognik

**Aprovação:** Founder + Technical + Metacognik

**Desbloqueia:** Gate H

---

## Gate H — External Tools Gate

**Valida:** Collectors, integrações de provider, roadmap de substituição de Manus.

**Critérios obrigatórios:**
1. Nenhuma chamada de provider direto de frontend
2. Todos os collectors via `POST /api/collectors/run` exclusivamente
3. Padrão `secret_ref` enforced para chaves de provider
4. Rate limit policies definidas para APIs externas
5. Cost controls ativos em chamadas de API externas
6. Manus oficialmente marcado como deprecado ou com schedule de substituição ativo registrado em ARCHITECTURE_PATCH_REPORT
7. Roadmap de substituição (Perplexity/Apify/PubMed/RAG) documentado
8. Novos providers requerem aprovação Founder + Technical antes de integração

**Verifiers:** Technical Lead

**Aprovação:** Technical (Founder para novos providers pagos)

**Desbloqueia:** Gate I

---

## Gate I — Business Systems Gate

**Valida:** Docs 21–24 (ROI, Feedback, Support, Credits/Plans/Billing) presentes e aprovados.

**Critérios obrigatórios:**
1. Doc 21 (ROI Architecture) presente e em status draft-aprovado
2. Doc 22 (Feedback System) presente e em status draft-aprovado
3. Doc 23 (Support System) presente e em status draft-aprovado
4. Doc 24 (Credits/Plans/Billing) presente e em status draft-aprovado
5. Nenhum cálculo financeiro no runtime sem aprovação Founder
6. Billing events emitidos via event bus (não mutations diretas)
7. Credits rastreados em tabela dedicada com audit trail
8. Workflow feedback→melhoria definido
9. State machine de suporte definida

**Verifiers:** PMO_CKOS, Founder

**Aprovação:** Founder + Technical

**Desbloqueia:** Gate J

---

## Gate J — Self-Evolving Gate

**Valida:** Learning loops, atualizações de memória, melhoria sem auto-modificação irrestrita.

**Critérios obrigatórios:**
1. Nenhum agente pode modificar sua própria política ou registry
2. Learning é proposal-based — proposta requer aprovação antes de aplicação
3. Mudanças de docs passam por Gate A novamente
4. Metacognik revisa todas as propostas de learning
5. Rollback plan para cada batch de learning
6. Memória de aprendizado auditável e reversível
7. Nenhuma mudança de autonomy_level por learning automático

**Verifiers:** Metacognik, Technical Lead

**Aprovação:** Founder + Metacognik

**Desbloqueia:** Gate K

---

## Gate K — Release Gate

**Valida:** Prontidão total do sistema para deploy de produção.

**Critérios obrigatórios:**
1. Todos os gates A–J passados sem bloqueador aberto
2. MVP P0 scope confirmado (ver §31)
3. Rollback plan de produção documentado e testado
4. Monitoramento e alertas configurados
5. Baselines de Evals (doc 13) estabelecidos
6. Cost caps configurados e testados
7. Plano de resposta a incidentes documentado
8. Nenhuma issue crítica (P0/P1) aberta
9. Founder sign-off explícito
10. Release readiness checklist (§24) completo com todos os itens aprovados

**Verifiers:** Todos os atores

**Aprovação:** Founder + Technical + Metacognik

**Desbloqueia:** Deploy de produção

---

# 8. Documentation QA

Checklist para revisão de qualquer documento do sistema CKOS.

| # | Critério | Verificador |
|---|---|---|
| D1 | YAML front matter completo (title, version, status, owner, reviewers, approval_required) | PMO_CKOS |
| D2 | Versão incrementada corretamente (patch/minor/major segundo mudança) | PMO_CKOS |
| D3 | Nenhuma referência cruzada quebrada — todos os `[[doc_name]]` resolvem | PMO_CKOS |
| D4 | Tese central / propósito claramente declarado | Metacognik |
| D5 | Todos os inputs/outputs do YAML existem no documento | QA Lead |
| D6 | Nenhuma contradição com docs 10–19 (verificado por Metacognik) | Metacognik |
| D7 | ARCHITECTURE_PATCH_REPORT atualizado se doc modifica arquitetura | PMO_CKOS |
| D8 | Campo `supersedes` presente se documento substitui versão anterior | PMO_CKOS |
| D9 | Edge cases cobrem os failure modes conhecidos do domínio | QA Lead |
| D10 | Related notes completas e válidas | PMO_CKOS |
| D11 | Nenhuma seção com placeholder ("TBD", "TODO") em draft final | QA Lead |
| D12 | Manus corretamente posicionado como ferramenta bootstrap temporária (onde aplicável) | Metacognik |
| D13 | Patches sugeridos registrados em ARCHITECTURE_PATCH_REPORT, não aplicados no doc | PMO_CKOS |

---

# 9. Architecture QA

Checklist para revisão de decisões de arquitetura.

| # | Critério | Verificador |
|---|---|---|
| A1 | Decisão segue Source of Truth Hierarchy (docs aprovados → AI output por último) | Metacognik |
| A2 | Nenhuma mudança de arquitetura sem patch note em ARCHITECTURE_PATCH_REPORT | PMO_CKOS |
| A3 | Consistência cross-doc: nova arquitetura não contradiz docs 10–19 | Metacognik |
| A4 | Nenhuma nova fase, nenhum novo agente sem registro de taxonomia | PMO_CKOS |
| A5 | Toda mudança de estado via evento — nenhuma mutation direta | Technical |
| A6 | Deny-by-default: permissão é pré-condição, não pós-filtro | Technical |
| A7 | Nenhuma lógica de negócio no frontend | Technical |
| A8 | UI lê exclusivamente projeções — nunca recalcula verdade | Technical |
| A9 | Multi-tenant: `tenant_id` em todos os registros de domínio | Technical |
| A10 | Nenhuma auto-modificação irrestrita de agente | Metacognik |
| A11 | Rollback plan definido para decisão irreversível | Technical |
| A12 | Product System projeta e manipula objetos do Runtime — não cria lógica fora do Runtime | Metacognik |

---

# 10. Data Model QA

Checklist para revisão de schema e mudanças de data model.

| # | Critério | Verificador |
|---|---|---|
| DM1 | RLS em cada tabela de domínio sem exceção | Technical |
| DM2 | `tenant_id` + `org_id` + `workspace_id` em todas as tabelas aplicáveis | Technical |
| DM3 | Nenhum token, secret ou credencial em coluna de tabela — apenas `secret_ref` | Technical |
| DM4 | Todos os foreign keys definidos e documentados | Technical |
| DM5 | Todos os enums com valores permitidos documentados | Technical |
| DM6 | Namespace de vetor + tenant como pré-condição de busca semântica | Technical |
| DM7 | Indexes em `tenant_id`, `project_id`, `workspace_id` em tabelas consultadas | Technical |
| DM8 | Audit trail (`created_by`, `updated_by`, `created_at`, `updated_at`, `archived_at`) em tabelas mutáveis | Technical |
| DM9 | Soft delete para registros auditáveis (não hard delete) | Technical |
| DM10 | `source_event_id` em registros gerados por eventos | Technical |
| DM11 | Patches sugeridos em ARCHITECTURE_PATCH_REPORT registrados | PMO_CKOS |
| DM12 | Breaking schema change acompanhado de plano de migração revisado | Technical |

---

# 11. Security QA

Checklist para revisão de segurança, RLS, ABAC e isolamento multi-tenant.

| # | Critério | Verificador |
|---|---|---|
| S1 | RLS ativo e testado em todas as tabelas de domínio | Technical |
| S2 | ABAC roles definidos para todos os novos recursos | Technical |
| S3 | Nenhum acesso cross-tenant possível por query padrão | Technical |
| S4 | Todos os endpoints de API requerem autenticação | Technical |
| S5 | Nenhum secret hardcoded em qualquer arquivo do repositório | Technical |
| S6 | Todos os secrets exclusivamente via secret_ref → vault/secret manager | Technical |
| S7 | `audit_log` cobre todos os eventos de segurança | Technical |
| S8 | Frontend nunca chama provider diretamente | Technical |
| S9 | Nenhum token, `actor_id` ou API key em código client-side | Technical |
| S10 | Agentes não podem alterar suas próprias políticas de segurança | Metacognik |
| S11 | Isolamento multi-tenant testado no nível de dados | Technical |
| S12 | Plano de pentest ou revisão de segurança equivalente documentado | Technical |

---

# 12. Runtime QA

Checklist para revisão do runtime: event bus, CQRS, projections, policy engine.

| # | Critério | Verificador |
|---|---|---|
| RT1 | Topologia do event bus alinhada com doc 10 §5.3 | Technical |
| RT2 | Todos os eventos de domínio no event catalog com schema, publisher, subscribers | Technical |
| RT3 | CQRS: read model separado de write model | Technical |
| RT4 | Nenhuma mutation direta de tabela — toda mudança via evento | Technical |
| RT5 | Policy engine deny-by-default implementado | Technical |
| RT6 | `audit_log` para toda mudança de estado | Technical |
| RT7 | Rollback plan por tipo de evento | Technical |
| RT8 | Projeções atualizadas por eventos, não por chamadas diretas | Technical |
| RT9 | Ações de agente passam pelo `agent_router` | Technical |
| RT10 | Autonomy levels enforced per doc 04 | Technical |
| RT11 | Cost controls ativos e testados | Technical |
| RT12 | Circuit breaker definido para dependências externas | Technical |

---

# 13. Command Center QA

Checklist para revisão do Command Center e intent routing.

| # | Critério | Verificador |
|---|---|---|
| CC1 | Taxonomia de intenção implementada (10 famílias de doc 15 §5.3) | QA Lead |
| CC2 | Todos os 22 slash commands registrados com intent_type, required_context, emitted_event | QA Lead |
| CC3 | Slash commands roteiam pelo event bus — não execução direta | Technical |
| CC4 | Nenhuma lógica de negócio na camada do Command Center | Technical |
| CC5 | `runtime_dependency` definido para cada comando | Technical |
| CC6 | Permissões enforced por RBAC/ABAC para cada família de intenção | Technical |
| CC7 | Tabela `command_history` implementada (patch sugerido em doc 15 §13) | Technical |
| CC8 | Sugestões são AI-generated, nunca execução direta | Metacognik |
| CC9 | Command Center nunca escreve em tabelas de domínio diretamente | Technical |
| CC10 | Error responses seguem schema de erro padrão | QA Lead |

---

# 14. Project Dashboard QA

Checklist para revisão do Project Dashboard.

| # | Critério | Verificador |
|---|---|---|
| PD1 | Dashboard lê exclusivamente de projeções aprovadas (doc 11 §21) | Technical |
| PD2 | Todos os widgets definidos em schema de projeção | Technical |
| PD3 | Nenhuma query SQL direta da camada de dashboard | Technical |
| PD4 | Widgets ROI/custo usam metodologia de cálculo aprovada | Founder |
| PD5 | Filtros aplicam `tenant_id` como pré-condição | Technical |
| PD6 | Timeline é event-sourced, não reverse-calculated | Technical |
| PD7 | Permissões do dashboard alinhadas com RBAC | Technical |
| PD8 | Função de export inclui entrada no `audit_log` | Technical |
| PD9 | Layout responsivo / mobile verificado | QA Lead |
| PD10 | Nenhum cálculo real-time — baseado em projeção exclusivamente | Technical |

---

# 15. Node Canvas QA

Checklist para revisão do Node Canvas.

| # | Critério | Verificador |
|---|---|---|
| NC1 | Canvas lê de `node_projection` e `edge_projection` apenas | Technical |
| NC2 | Nenhuma criação de node sem emissão de evento | Technical |
| NC3 | State machine exibida pelo Canvas — não controlada pelo Canvas | Technical |
| NC4 | Approval nodes corretamente gateados | QA Lead |
| NC5 | Agent nodes exibem estado atual (working/blocked/awaiting) | QA Lead |
| NC6 | Painel de evidências lê de `evidence_items` projection | Technical |
| NC7 | Cost badges leem de `cost_projection` | Technical |
| NC8 | Risk badges leem de `risk_projection` | Technical |
| NC9 | Permissões enforced (read-only vs. contributor vs. lead) | Technical |
| NC10 | Criação manual de node emite evento + `audit_log` | Technical |
| NC11 | Canvas nunca escreve em tabelas de source diretamente | Technical |
| NC12 | Sistema de tokens whitelabel aplicado | QA Lead |

---

# 16. Agent QA

Checklist para revisão de agentes registrados e suas ações.

| # | Critério | Verificador |
|---|---|---|
| AG1 | Agente registrado em `agent_registry` com `system_id`, `display_name`, `skills`, `autonomy_level` | PMO_CKOS |
| AG2 | `autonomy_level` alinhado com escopo declarado | Metacognik |
| AG3 | Auto-escalação de agente impossível (policy-enforced) | Technical |
| AG4 | Human-in-the-loop para `autonomy_level ≥ 3` | Technical |
| AG5 | Custos rastreados por run | Technical |
| AG6 | Entrada de `audit_log` para cada ação | Technical |
| AG7 | Agente não pode alterar próprio registry ou política | Technical |
| AG8 | Rollback plan por tipo de ação | Technical |
| AG9 | Output passa por `output_validator` antes de escrever | Technical |
| AG10 | Nenhuma chamada direta a provider externo — via `collector_runner` apenas | Technical |
| AG11 | Failure mode definido: fail-fast ou degrade-gracefully | Technical |

---

# 17. Research QA

Checklist para revisão de research runs, evidências e síntese.

| # | Critério | Verificador |
|---|---|---|
| RQ1 | Evidence items têm `source_tier`, `reliability_score`, `confidence_score` | Metacognik |
| RQ2 | Todos os claims linkados a `evidence_items` — nenhum assertado sem fonte | Metacognik |
| RQ3 | Outputs do Manus tratados como Tier 4 (no máximo) — nunca Tier 1 | Metacognik |
| RQ4 | Source reliability scored antes de síntese | Metacognik |
| RQ5 | Contradições detectadas e flagradas | Metacognik |
| RQ6 | Gaps documentados | Metacognik |
| RQ7 | Revisão Metacognik para todo output de síntese | Metacognik |
| RQ8 | Research run rastreado pela state machine de `research_runs` | Technical |
| RQ9 | Nenhuma síntese baseada exclusivamente em fontes Tier 5 | Metacognik |
| RQ10 | Implementation brief requer evidência backing | QA Lead |
| RQ11 | Créditos e direitos documentados | QA Lead |
| RQ12 | Audit trail do research pack completo | PMO_CKOS |

---

# 18. Cost and Credits QA

Checklist para revisão de custo, créditos e billing.

| # | Critério | Verificador |
|---|---|---|
| CQ1 | Nenhum cálculo de custo no frontend | Technical |
| CQ2 | Custo rastreado por evento/run/collector | Technical |
| CQ3 | Cost caps configurados e enforced | Technical |
| CQ4 | Dedução de crédito atômica (não eventual) | Technical |
| CQ5 | Billing events emitidos via event bus | Technical |
| CQ6 | Cost projection atualizada por billing event | Technical |
| CQ7 | Nenhuma mutation de custo sem `audit_log` | Technical |
| CQ8 | Rate limits definidos para operações caras | Technical |
| CQ9 | Estimativa de custo apresentada ao usuário antes de ação cara | QA Lead |
| CQ10 | Evento de refund/reversal definido | Technical |

---

# 19. ROI QA

Checklist para revisão de cálculos e projeções de ROI.

| # | Critério | Verificador |
|---|---|---|
| RO1 | Cálculos ROI baseados em dados de projeção — não em queries live | Technical |
| RO2 | Metodologia de ROI documentada e aprovada pelo Founder | Founder |
| RO3 | Nenhuma projeção de receita sem evidência backing | Metacognik |
| RO4 | Node type ROI registrado no `node_registry` | PMO_CKOS |
| RO5 | ROI events emitidos via event bus | Technical |
| RO6 | Dados históricos de ROI imutáveis (audit trail) | Technical |
| RO7 | Formato de relatório ROI revisado por Metacognik | Metacognik |
| RO8 | Nenhuma aprovação automática de ROI — sempre revisão humana | Founder |

---

# 20. Feedback QA

Checklist para revisão do sistema de feedback.

| # | Critério | Verificador |
|---|---|---|
| FQ1 | Feedback capturado na tabela `feedback_entries` (patch sugerido em docs 15/16 para doc 11) | Technical |
| FQ2 | Workflow feedback→melhoria definido | PMO_CKOS |
| FQ3 | Feedback events emitidos via event bus | Technical |
| FQ4 | Política de routing de feedback definida (quem revisa, quando) | PMO_CKOS |
| FQ5 | Loop de closure: feedback → ação → resultado → notificação ao usuário | QA Lead |
| FQ6 | Nenhuma divulgação de feedback cross-tenant | Technical |
| FQ7 | Node type de feedback registrado | PMO_CKOS |

---

# 21. Support QA

Checklist para revisão do sistema de suporte.

| # | Critério | Verificador |
|---|---|---|
| SU1 | Support tickets rastreados na tabela `support_tickets` (patch sugerido para doc 11) | Technical |
| SU2 | State machine de ticket definida | Technical |
| SU3 | Política de escalonamento de suporte definida | PMO_CKOS |
| SU4 | Support events emitidos via event bus | Technical |
| SU5 | Nenhuma visibilidade cross-tenant de tickets | Technical |
| SU6 | SLA definido por severidade de ticket | PMO_CKOS |
| SU7 | Resolução de ticket dispara opção de feedback loop | QA Lead |

---

# 22. UI/UX QA

Checklist para revisão de toda superfície de UI do CKOS.

| # | Critério | Verificador |
|---|---|---|
| UX1 | UI lê exclusivamente projeções — nunca recalcula verdade | Technical |
| UX2 | Nenhuma chamada de provider de frontend | Technical |
| UX3 | Nenhum token, `actor_id` ou API key em código client-side | Technical |
| UX4 | Sistema de tokens whitelabel aplicado consistentemente | QA Lead |
| UX5 | Mobile read-only verificado para Node Canvas | QA Lead |
| UX6 | Glassmorphism / design tokens alinhados com design system | QA Lead |
| UX7 | Error states definidos para todos os fluxos visíveis ao usuário | QA Lead |
| UX8 | Loading states definidos para todas as operações assíncronas | QA Lead |
| UX9 | Empty states definidos | QA Lead |
| UX10 | Acessibilidade mínima: keyboard navigation para core flows | QA Lead |
| UX11 | Nenhum conteúdo tenant-específico hardcoded em componentes compartilhados | Technical |

---

# 23. AI Tool Output QA

Checklist para revisão de qualquer output gerado por Claude, Codex ou Antigravity.

| # | Critério | Verificador |
|---|---|---|
| AI1 | Output de AI não é canônico até revisão humana | Metacognik |
| AI2 | Source of Truth Hierarchy respeitado (docs aprovados → AI output por último) | Metacognik |
| AI3 | Nenhum output de AI vira arquitetura sem aprovação Technical | Technical |
| AI4 | Nenhum output de AI modifica docs sem aprovação PMO_CKOS | PMO_CKOS |
| AI5 | Hallucination check: todos os fatos AI-declarados verificados contra fontes | Metacognik |
| AI6 | Scope check: output ficou dentro do escopo atribuído | QA Lead |
| AI7 | Forbidden actions check: nenhuma das FA1–FA20 (doc 19) foi acionada | QA Lead |
| AI8 | Nenhum output de AI commitado ao repo sem revisão humana | Technical |
| AI9 | Nenhuma migration AI-gerada aplicada sem revisão Technical | Technical |
| AI10 | Prompt e resposta do AI tool logados para audit | PMO_CKOS |

---

# 24. Release Readiness Checklist

Checklist final para submissão de Gate K. Todos os itens devem estar aprovados.

## 24.1 Gates

- [ ] Gate A — Documentation: passado sem bloqueador aberto
- [ ] Gate B — Data Model: passado sem bloqueador aberto
- [ ] Gate C — Runtime Core: passado sem bloqueador aberto
- [ ] Gate D — Security: passado sem bloqueador aberto
- [ ] Gate E — Projection: passado sem bloqueador aberto
- [ ] Gate F — Product Surface: passado sem bloqueador aberto
- [ ] Gate G — Agent Runtime: passado sem bloqueador aberto
- [ ] Gate H — External Tools: passado sem bloqueador aberto
- [ ] Gate I — Business Systems: passado sem bloqueador aberto
- [ ] Gate J — Self-Evolving: passado sem bloqueador aberto

## 24.2 Operacional

- [ ] MVP P0 scope confirmado (§31)
- [ ] Rollback plan de produção documentado e testado
- [ ] Monitoramento e alertas configurados e testados
- [ ] Baselines de Evals (doc 13) estabelecidos
- [ ] Cost caps configurados e testados em staging
- [ ] Plano de resposta a incidentes documentado e revisado

## 24.3 Aprovações

- [ ] Founder sign-off explícito para produção
- [ ] Technical Lead sign-off para infraestrutura
- [ ] Metacognik revisão final sem veto aberto

## 24.4 Issues

- [ ] Nenhuma issue P0 aberta
- [ ] Nenhuma issue P1 aberta sem plano de resolução documentado
- [ ] Todas as issues P2 com owner e prazo atribuídos

## 24.5 Documentação

- [ ] ARCHITECTURE_PATCH_REPORT final revisado
- [ ] Todos os patches sugeridos aplicados ou formalmente adiados com justificativa
- [ ] Docs 10–24 em status `approved-draft` ou superior

---

# 25. Critérios de Rejeição

## 25.1 Rejeição Automática (bloqueio imediato, sem revisão adicional)

As seguintes situações resultam em rejeição imediata, sem possibilidade de aprovação condicional:

| # | Trigger de Rejeição Automática |
|---|---|
| RA1 | Token, secret ou credencial diretamente em coluna de tabela de domínio |
| RA2 | Frontend chamando provider diretamente (não via `/api/collectors/run`) |
| RA3 | Agente modificando sua própria política de segurança ou registry |
| RA4 | Schema change sem RLS na tabela afetada |
| RA5 | Aprovação concedida exclusivamente por AI tool — nenhum humano assinou |
| RA6 | Query com acesso cross-tenant sem isolamento por `tenant_id` |
| RA7 | `tenant_id` hardcoded em código compartilhado |
| RA8 | Busca vetorial sem namespace de tenant como pré-condição |
| RA9 | Migration SQL de produção sem dry-run documentado |
| RA10 | Gate pulado (ir de Gate X para Gate X+2 sem Gate X+1) |

## 25.2 Rejeição Formal (requer revisão e registro)

As seguintes situações requerem rejeição formal com causa documentada no QA Report:

| # | Trigger de Rejeição Formal |
|---|---|
| RF1 | Claim sem evidência backing (fonte não citada, não pontuada) |
| RF2 | Contradição com doc aprovado não registrada em ARCHITECTURE_PATCH_REPORT |
| RF3 | Output do Manus tratado como fonte canônica Tier 1 |
| RF4 | Novo agente sem registro na taxonomia de agentes |
| RF5 | Nova fase fora do roadmap aprovado |
| RF6 | Decisão arquitetural que invalida gate anteriormente passado |
| RF7 | Rollback plan ausente para operação irreversível |
| RF8 | Output de AI aprovado como arquitetura sem revisão Technical |
| RF9 | Aprovação informal (chat, voz) sem registro formal |
| RF10 | Aprovação stale (>90 dias sem close das condições) |

---

# 26. Founder Approval Protocol

## 26.1 O que sempre requer Founder

- Mudanças de visão de produto
- Novo provider externo pago
- Pricing e planos
- Deploy de produção (Gate K)
- Schema changes breaking
- Novo documento de sistema de negócio (docs 21–24)
- Novo agente com `autonomy_level ≥ 4`
- Publicação ou anúncio externo
- Decisão arquitetural com impacto em negócio
- Gates D (Security) e K (Release)

## 26.2 Formato Obrigatório de Approval Request

```txt
[FOUNDER APPROVAL REQUEST]
Título:            [nome curto da decisão]
Prioridade:        P0 | P1 | P2 | P3
Gate bloqueado:    [Gate A–K ou N/A]
Submission ID:     [UUID gerado por PMO_CKOS]
Data:              [ISO date]

Contexto (máx. 1 parágrafo):
[...]

Opções (máx. 3):
1. [...]
2. [...]
3. (se aplicável) [...]

Recomendação PMO_CKOS: Opção [N] — [1 frase]

Riscos se aprovado:
- [...]

Riscos se não aprovado:
- [...]

Custo estimado: [valor ou range]
Rollback: [como desfazer se aprovado e revertido]
Decisão necessária até: [data/hora com timezone]
```

## 26.3 SLA de Resposta

| Prioridade | SLA | Escalação |
|---|---|---|
| P0 | 6h | PMO_CKOS escalona a cada 2h; Technical Lead pode decidir com revisão pós-hoc |
| P1 | 48h | PMO_CKOS escalona ao completar SLA; gate permanece bloqueado |
| P2 | 5 dias úteis | Gate permanece bloqueado; nota de backlog adicionada |
| P3 | 2 semanas | Gate permanece bloqueado |

## 26.4 Ausência de Founder

- **P0:** Technical Lead faz decisão de emergência. Registra no audit_log como "emergency decision, pending Founder review". Founder revisa e confirma ou reverte em até 48h após retorno.
- **P1+:** Gate permanece bloqueado. PMO_CKOS registra bloqueio com timestamp. Sem unilateral substitution de ator Founder.

## 26.5 Registro de Aprovação

Toda aprovação do Founder deve ser registrada com:
- Quem aprovou (nome e identificador)
- Quando (timestamp ISO com timezone)
- Qual opção foi aprovada
- Condições (se houver)
- Referência ao Submission ID

---

# 27. Metacognik Veto Protocol

## 27.1 Condições de Veto

Metacognik exerce veto quando qualquer das condições abaixo é verdadeira:

| # | Condição de Veto |
|---|---|
| MV1 | Claim assertado sem evidência verificável |
| MV2 | Aprovação de AI tool tratada como canônica sem assinatura humana |
| MV3 | Contradição entre dois docs aprovados não registrada |
| MV4 | Scope creep: entrega excede escopo aprovado |
| MV5 | Source Reliability abaixo do threshold para o claim declarado |
| MV6 | Evidência stale (Tier 3+ com mais de 18 meses) usada como primária |
| MV7 | Alucinação detectada em documento de arquitetura |
| MV8 | Rollback ausente em operação irreversível de produção |
| MV9 | Conflito de interesse no chain de aprovação (mesmo ator que propõe também aprova) |

## 27.2 Formato de Veto

```txt
[METACOGNIK VETO]
Submission ID:    [UUID]
Data:             [ISO date]
Submission:       [o que foi submetido]

Condição de Veto: MV[N] — [descrição]

Evidência Gap:
[O que está faltando para resolver o veto]

Contradição detectada:
[Doc A §X afirma X; Doc B §Y afirma Y — conflict]

Ação requerida antes de re-submissão:
1. [...]
2. [...]
```

## 27.3 Escalação de Veto

- Se veto Metacognik conflita com aprovação prévia do Founder: Metacognik prepara **Risk Statement** formal
- Founder pode sobrescrever o veto com nota explícita de aceitação de risco
- Nota de override e Risk Statement vão permanentemente para `audit_log`
- Override não elimina o registro — apenas autoriza o avanço com risco documentado

## 27.4 Resolução de Veto

- Submitter corrige as condições listadas no formato de veto
- Re-submete com referência ao Submission ID original
- Metacognik revisa especificamente os itens flagrados
- Se resolvidos: veto levantado e registrado no `audit_log`
- Se não resolvidos: novo veto emitido com referência ao anterior

---

# 28. Technical Approval Protocol

## 28.1 O que requer aprovação Technical

- Schema changes (aditivos ou breaking)
- Novos tipos de evento no event catalog
- Nova integração de API externa
- Mudanças de política de runtime ou segurança
- Mudanças no runtime de agentes
- Planos de migração
- Configuração de infraestrutura de produção

## 28.2 Processo de Revisão Technical

1. Ler a proposta contra os documentos 10–13
2. Verificar schema contra requisitos RLS de doc 11
3. Verificar eventos contra event catalog de doc 10
4. Verificar segurança contra políticas de doc 12
5. Verificar custo contra controles de doc 13
6. Confirmar que rollback plan é válido e executável
7. Aprovar (sim/não/condições) com justificativa escrita

## 28.3 Formato de Revisão Technical

```txt
[TECHNICAL REVIEW]
Submission ID:     [UUID]
Data:              [ISO date]
Proposta:          [nome]
Technical Lead:    [nome]

Verificação contra docs:
- Doc 10 (Runtime): [OK | Issue: ...]
- Doc 11 (Schema): [OK | Issue: ...]
- Doc 12 (Security): [OK | Issue: ...]
- Doc 13 (Evals/Cost): [OK | Issue: ...]

Rollback plan: [Válido | Inválido: motivo]

Decisão: Aprovado | Aprovado com condições | Rejeitado
Condições (se houver): [...]
Justificativa: [...]
```

---

# 29. Formato de QA Report

Todo QA Report deve seguir este template obrigatório.

```markdown
# QA Report

**Submission ID:**   [UUID gerado por PMO_CKOS]
**Título:**          [nome da entrega ou decisão]
**Gate:**            [A | B | C | D | E | F | G | H | I | J | K | N/A]
**Domínio:**         [documentation | schema | runtime | security | agent | product | ui | research | cost | roi | feedback | support | ai_output]
**Data:**            [ISO date]
**QA Lead:**         [nome/id]
**Status Final:**    [Aprovado | Aprovado com Condições | Needs Patch | Rejeitado]

---

## Checklist de Domínio

| # | Critério | Status | Nota |
|---|---|---|---|
| [D1..] | [critério] | ✓ / ✗ | [nota ou N/A] |

---

## Issues Encontradas

| Severidade | Issue | Ação Requerida |
|---|---|---|
| P0 / P1 / P2 / P3 | [descrição] | [ação] |

---

## Routing de Aprovação

| Ator | Necessário | Status | Data |
|---|---|---|---|
| Metacognik | Sim / Não | Pendente / Aprovado / Vetado | |
| Technical Lead | Sim / Não | Pendente / Aprovado / Rejeitado | |
| Founder | Sim / Não | Pendente / Aprovado / Rejeitado | |

---

## Rollback Plan

[Descrever explicitamente como desfazer se aprovado e depois revertido]

---

## Condições (se Aprovado com Condições)

1. [condição com prazo e owner]
2. [...]

---

## Decisão Final

[Status final + justificativa + referência a evidências]

**Aprovado por:** [nome] **em** [timestamp] **com referência:** [Submission ID]
```

---

# 30. State Machine de Aprovações

10 estados com transições formais.

```txt
States:
  draft                   — submissão sendo preparada pelo autor
  submitted               — formalmente submetida para revisão QA
  in_qa_review            — QA Lead revisando ativamente
  qa_passed               — QA Lead aprovou; aguardando atores de aprovação
  qa_failed               — QA rejeitou; retorna ao autor para rework
  pending_approval        — em fila de aprovação (Founder/Technical/Metacognik)
  approved                — todos os atores requeridos aprovaram
  approved_with_conditions — aprovado com follow-ups requeridos
  rejected                — formalmente rejeitado; não elegível para re-submissão sem major rework
  rollback_requested      — previamente aprovado; agora em processo de reversão

Transições:
  draft                → submitted              (autor completa submissão)
  submitted            → in_qa_review           (QA Lead inicia revisão)
  in_qa_review         → qa_passed              (QA Lead aprova)
  in_qa_review         → qa_failed              (QA Lead rejeita)
  qa_failed            → draft                  (autor faz rework)
  qa_passed            → pending_approval        (PMO_CKOS roteia para atores)
  pending_approval     → approved               (todos os atores requeridos aprovam)
  pending_approval     → approved_with_conditions (aprovação com condições)
  pending_approval     → rejected               (um ou mais atores vetam/rejeitam)
  approved             → rollback_requested      (rollback pós-aprovação acionado)
  approved_with_conditions → approved           (condições cumpridas e verificadas)
  approved_with_conditions → rollback_requested  (condições não cumpridas no prazo)
  rollback_requested   → draft                  (rework do zero após rollback)
  rejected             → draft                  (apenas após novo scoping aprovado por PMO_CKOS)

Estados finais:
  approved (sem condições abertas)
  rejected (permanente para aquela submissão)
  rollback_requested → draft (recomeça)

Regras adicionais:
  - Aprovação stale (>90d sem close de condições) → transição forçada approved_with_conditions → rollback_requested
  - Veto Metacognik em pending_approval → rejeição automática ou retorno a qa_failed
  - Emergency patch P0 → bypassa in_qa_review; vai direto a pending_approval com flag emergency_review
```

---

# 31. MVP P0 QA Scope

## 31.1 Em Escopo para P0 QA

| Área | Escopo P0 |
|---|---|
| Documentation | Docs 10–20 em status approved-draft |
| Data Model | Tabelas core de doc 11 MVP scope; RLS em todas |
| Runtime | Event bus bootstrap; CQRS básico; 3 projeções core |
| Security | RLS + ABAC baseline; tenant isolation; audit_log |
| Command Center | 6 slash commands core; intent routing básico |
| Node Canvas | 5 node types; edge básico; state machine display |
| Project Dashboard | 3 widgets core; timeline básico |
| Agents | 3 agentes core com autonomy_level 1–2 |
| User Paths | 5 user paths de doc 17 §21 |
| Gates | Gates A–D obrigatórios; E–F parciais; G–K não exigidos para P0 |

## 31.2 Fora do Escopo para P0 QA (adiado)

| Área | Bloqueio |
|---|---|
| Business Systems (docs 21–24) | Gates I depende desses docs |
| Self-Evolving System | Gate J — pós-MVP |
| Full provider integration (Perplexity/Apify/PubMed) | Gate H — pós-P0 |
| Agent autonomy_level ≥ 3 | Requer Gate G completo |
| Full Evals suite (doc 13) | Pós-P0; baselines mínimos em P0 |
| Multi-region deploy | Pós-release estável |
| 13 projeções completas | 3 core em P0; resto em P1+ |
| 22 slash commands completos | 6 core em P0 |

---

# 32. Edge Cases

**32.1 Founder aprovou mas Metacognik vetou:**
Founder pode sobrescrever com nota explícita de aceitação de risco. Risk Statement do Metacognik é permanente no `audit_log`. Override não elimina o registro — apenas autoriza avanço com risco documentado.

**32.2 QA passou mas bug descoberto pós-aprovação:**
Estado `rollback_requested`. QA re-abre. Technical decide: P0/P1 → rollback imediato; P2 → patch urgente antes de próximo gate.

**32.3 Output de AI aprovado como arquitetura sem revisão humana:**
Rejeição automática (RA5). Output quaranteado. Entrada no `audit_log`. AI prompt e resposta revisados. Revisão humana obrigatória antes de nova submissão.

**32.4 Deadlock de gates (Gate G esperando Gate D que está em conflito):**
PMO_CKOS cria resolution plan com etapas ordenadas. Escalona para Founder se o conflito não for técnico. Nenhum gate avança enquanto deadlock não for resolvido.

**32.5 Output do Manus citado como evidência Tier 1:**
Metacognik rejeição automática (MV5). Evidência re-pontuada para Tier 4. Research run deve re-coletar com fontes primárias adequadas.

**32.6 Veto de segurança após aprovação de Gate K:**
Rollback de emergência. Todos os gates subsequentes a Gate D re-abertos. Technical Lead lidera investigação. Founder notificado em até 2h.

**32.7 Founder inalcançável para gate P0:**
Technical Lead faz decisão de emergência com flag `emergency_decision`. Founder revisa e confirma (ou reverte) em até 48h após retorno. PMO_CKOS rastreia resolução.

**32.8 Dois docs aprovados com conteúdo contraditório:**
Metacognik flaga. Doc mais recente prevalece. Patch registrado em ARCHITECTURE_PATCH_REPORT. Doc anterior marcado como `partially_superseded`. Gate A re-verificado para consistência.

**32.9 Novo agente registrado sem taxonomia:**
Bloqueado em Gate G (AG1). Requer atualização da taxonomia e aprovação PMO_CKOS antes de registro. Gate G não avança até resolução.

**32.10 Evidência insuficiente para implementation brief:**
Research run deve completar pipeline completo (collect → score → synthesize → Metacognik review) antes de gate avançar. Brief sem evidência backing = rejeição formal RF1.

**32.11 Cost spike descoberto após aprovação de Gate I:**
Cost QA re-abre (§18). Nova estimativa submetida. Founder approval se variação > 30% do estimado. Billing events revisados.

**32.12 Ator de aprovação em conflito de interesse:**
Ator deve se recusar (MV9). Próximo ator na hierarquia aprova. PMO_CKOS registra recusa e justificativa no `audit_log`.

**32.13 UI bonita que não corresponde ao data model:**
Rejeitada em Node Canvas QA (NC1). Design deve ser ajustado para alinhar com projeções aprovadas. Antigravity prototypes não são fonte de verdade de data model.

**32.14 Migration de schema quebra projeção existente:**
Gate B re-abre. Migration revisada. Projection trigger atualizado. QA de projeção re-executado antes de Gate E re-submissão.

**32.15 Dois tenants com mesmo `workspace_id`:**
Security QA rejeição automática (RA3 equivalente). Triado como P0. Correção imediata. Gate D re-abre para re-verificação de isolamento.

**32.16 Agente produz output que contorna QA:**
Bloqueado pelo `output_validator`. Flagrado no `audit_log`. `autonomy_level` do agente reduzido pela policy engine. Incident registrado em doc 13.

**32.17 Approval request sem rollback plan:**
Retornada ao submitter (RA7/RF7). Rollback plan obrigatório antes que QA possa passar.

**32.18 Síntese de pesquisa sem reliability scores:**
Metacognik bloqueia (MV1, MV5). Research run deve re-executar pipeline de scoring antes de síntese ser aceita.

**32.19 Scope creep durante revisão de P0 QA:**
QA Lead flaga. PMO_CKOS decide in/out com base no roadmap aprovado. Founder approval se o scope creep for significativo (muda MVP scope).

**32.20 Emergency patch durante revisão de gate ativo:**
Patches P0/P1 seguem protocolo de emergência (estado `emergency_review`). Revisão de gate em andamento é pausada. Patch é revisado primeiro por Technical Lead. Gate retoma após patch resolvido.

**32.21 Aprovação via canal informal (chat, emoji, mensagem de voz):**
Não válida. Aprovação formal deve ser re-emitida no formato correto (§26.2) com Submission ID e timestamp. Nenhum gate avança com base em aprovação informal.

**32.22 Template de QA Report não utilizado:**
Retornado ao submitter. Template é obrigatório (§29). Re-submissão requer formato completo.

**32.23 Aprovação stale (aprovada >90d, condições não cumpridas):**
Aprovação expira automaticamente. Estado transita para `rollback_requested`. Re-submissão requerida. PMO_CKOS notifica owner das condições não cumpridas.

**32.24 Contradição cross-doc descoberta após Gate A:**
ARCHITECTURE_PATCH_REPORT atualizado com a contradição. Gate afetado pelo conflito re-abre. Metacognik revisa resolução antes de re-submissão do gate.

**32.25 Todos os atores de aprovação indisponíveis simultaneamente:**
PMO_CKOS declara freeze formal. Nenhum gate avança. Plano de escalonamento ativado (email, canal alternativo). Prazo de resolução registrado. Founder é o primeiro ator a ser reinstalado.

**32.26 Agente tenta aprovar seu próprio QA Report:**
Bloqueado por policy (AG3, AG7). Aprovação humana requerida. `audit_log` flagrado. `autonomy_level` do agente auditado.

**32.27 SLA de revisão Metacognik não cumprido:**
PMO_CKOS escalona ao atingir SLA. Se 2x SLA sem resposta, Founder decide sobre escalonamento. Nenhum gate avança sem Metacognik review quando requerido.

---

# 33. Required Future Documents

Documentos necessários para completar o sistema QA e de aprovação do CKOS.

| Doc | Título | Necessário Antes de | Status |
|---|---|---|---|
| 21 | ROI Architecture | Gate I | Não existe |
| 22 | Feedback System Architecture | Gate I | Não existe |
| 23 | Support System Architecture | Gate I | Não existe |
| 24 | Credits, Plans and Billing Architecture | Gate I | Não existe |
| 25 | Self-Evolving System Architecture | Gate J | Existe em `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` |
| 26 | External Provider Registry | Gate H | Não existe |
| 27 | Agent Registry Full Schema | Gate G | Não existe |
| 28 | Whitelabel and Tenant Configuration | Gate F | Não existe |
| 29 | Performance and Load Testing Protocol | Gate K | Não existe |

## Patches sugeridos para doc 11 (não aplicados)

Estes patches são necessários para o sistema de QA funcionar completamente e devem ser aplicados em doc 11 antes dos gates correspondentes:

| Patch ID | Tabela/Componente | Gate Dependente |
|---|---|---|
| P20-1 | `approval_submissions` + `approval_decisions` (state machine de aprovações em §30) | Gate B |
| P20-2 | QA Report como tipo de artifact no artifact registry | Gate F |
| P20-3 | Evento `MetacognikVetoEmitted` no event catalog de doc 10 | Gate C |
| P20-4 | Tabela `release_readiness_checks` para rastrear §24 | Gate B |

> Os patches acima são sugeridos e registrados. **Não aplicar** nos docs 10/11 sem aprovação Technical + PMO_CKOS e versão incremental nos docs afetados.

---

# 34. Related Notes

- [[04_AUTONOMY_AND_APPROVALS]]
- [[10_RUNTIME_ARCHITECTURE]]
- [[11_DATA_MODEL_AND_SCHEMA]]
- [[12_SECURITY_AND_POLICY]]
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]]
- [[17_IMPLEMENTATION_PROTOCOL]]
- [[18_RESEARCH_PROTOCOL]]
- [[19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL]]
- [[ARCHITECTURE_PATCH_REPORT]]
- [[QA_DOCUMENTATION_CHECKLIST]]
