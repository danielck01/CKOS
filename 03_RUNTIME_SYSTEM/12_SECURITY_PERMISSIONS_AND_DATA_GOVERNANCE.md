---
title: Security, Permissions and Data Governance
file: 12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
phase: 03_RUNTIME_SYSTEM
category: security
version: 1.1.0
status: draft
owner: PMO_CKOS
responsible_agent: Metacognik
reviewers:
  - builder_lead
  - qa_lead
approval_required:
  - founder
  - technical
  - legal
purpose: Modelo de segurança do CKOS — deny-by-default, RBAC+ABAC, RLS multi-tenant, isolamento de vetor/storage/memória, permissões de agente/tool/collector/modelo, policyRegistry como fonte de autorização, approval policies, decision rights enforcement, audit trail append-only, whitelabel isolation e prevenção de vazamento cross-tenant/client.
inputs: Object Model (02); Autonomy (04); Data Model (11 v1.1.2); Runtime (10 v1.1.0) — policyRegistry, approvalPolicyRegistry, memoryPolicyRegistry, policy_engine, tool_router, agent_router, approval_gate, collector_runner, rag_retriever, Decision Rights Matrix §5.22.
outputs: Modelo de permissão RBAC+ABAC; regras de RLS por tenant; isolamento de vetor/storage/memória; política de agente/tool/collector/modelo; approval policies; decision rights enforcement; audit trail; safe defaults; whitelabel isolation; patches sugeridos para doc 11.
framework: deny-by-default + RBAC (papéis) + ABAC (atributos contextuais) + RLS (isolamento de linha Postgres) + capability scoping + policyRegistry como source-of-truth de autorização + audit trail append-only.
edge_cases: Agente tenta tool não permitida; cross-tenant vector leak; PII em prompt; segredo em log; self-escalation de agente; approval bypass; collector expõe actor/provider ao frontend; agente tenta modificar policy.
integrations: Postgres RLS (11); policy_engine + tool_router + agent_router + approval_gate + collector_runner + rag_retriever (10); vault de segredos; auth/SSO; tracing com redação (13).
prompts: Não aplicável (documento de arquitetura de segurança).
metrics: 0 vazamentos cross-tenant; 0 segredos em log/trace; 100% RLS nas tabelas de domínio; 0 self-escalation; % ações com authz check; % PII classificada na ingestão; tempo de revogação ≤ 1 min.
related_notes:
  - ../01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md
  - 10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - 11_DATA_MODEL_AND_PERSISTENCE.md
  - 13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - ../07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md
tags: [runtime, security, permissions, rbac, abac, rls, multi_tenant, audit, data_governance, collector, model_privacy, approval_policy, decision_rights, whitelabel]
---

# 1. Propósito

Definir como o CKOS impede que um agente, usuário ou projeto **veja ou execute** algo que não deveria. Em um sistema multi-tenant, whitelabel, agêntico e que processa dados de múltiplos clientes, esta camada separa "produto funcional" de "incidente jurídico e de segurança".

A v1.1.0 sincroniza com doc 10 v1.1.0 (policyRegistry, approvalPolicyRegistry, policy_engine, decision rights, collector/actor/provider separation) e com doc 11 v1.1.0 (tabelas de persistência, RLS, audit_logs, agent_permissions, approval_policies). Todo mecanismo aqui descrito tem uma contraparte de runtime em doc 10 e uma contraparte de dados em doc 11 — este doc é a **especificação de política** que aqueles dois executam.

# 2. Função dentro do CKOS

Governa três dimensões inseparáveis:

1. **Autorização** — quem (humano ou agente) pode executar qual ação em qual recurso, em qual contexto.
2. **Isolamento** — o que um tenant, projeto ou cliente consegue ver e tocar (multi-tenant + whitelabel).
3. **Governança de dados** — o que pode ser persistido, em que classificação, por quanto tempo e como é auditado.

É consultada pelo Runtime (10) em todo ingress, policy check, router e approval gate. É materializada na camada de dados (11) via RLS, tabelas de permissão e audit trail. Nenhuma ação de impacto acontece sem passar por esta camada.

# 3. Inputs

- **Object Model (02)**: objetos, tipos e relacionamentos que precisam ser autorizados.
- **Autonomy e Approvals (04)**: matriz de risco e níveis de autonomia que determinam quando approval é obrigatório.
- **Data Model (11 v1.1.0)**: tabelas `agent_permissions`, `approval_policies`, `audit_logs`, `vector_collections`, `context_packs.permissions_snapshot`, `project_members.role`, `agents.forbidden_actions`, `agents.model_policy_ref`.
- **Runtime (10 v1.1.0)**: policyRegistry, approvalPolicyRegistry, memoryPolicyRegistry, policy_engine, tool_router, agent_router, approval_gate, collector_runner, rag_retriever, Decision Rights Matrix (§5.22).
- **Auth/SSO**: identidade do usuário, token de sessão, escopo de tenant derivado do token.

# 4. Outputs

- Modelo de permissão RBAC+ABAC com mapeamento de papéis e atributos;
- Regras de RLS (Row Level Security) por tenant/org/workspace/project;
- Especificação de isolamento: vetor, storage, memória, Redis;
- Políticas de agente, tool, collector, provider, actor e modelo;
- Approval policies (quem aprova o quê, com que timeout e escalonamento);
- Decision Rights enforcement (quem decide o quê — integrado ao runtime);
- Audit trail: quais eventos são auditados, em que tabela, com que retenção;
- Safe defaults: o que acontece quando não há política explícita;
- Whitelabel isolation: separação estrutural entre clientes;
- Patches sugeridos para doc 11 (tabelas ainda não definidas lá).

# 5. Framework operacional

## 5.1 Princípio mestre: deny-by-default

**Nenhum ator — humano, agente ou sistema — tem acesso sem concessão explícita.**

Toda decisão de autorização é avaliada como:
```
pode(ator, ação, recurso, contexto) → allow | deny
```

- Negação é o **default silencioso**; concessão é a **exceção registrada**.
- A ausência de política equivale a `deny`.
- Erros de configuração e políticas incompletas sempre resultam em negação, nunca em permissão acidental.
- Toda negação relevante gera evento `PermissionDenied` → `audit_logs`.

## 5.2 Camadas de escopo de permissão

```txt
org → workspace → project → object → field
```

- Permissão concedida no nível mais alto propagado para baixo.
- Restrição pode ser aplicada em qualquer nível inferior (nunca ampliação implícita).
- Token de sessão carrega `org_id + workspace_id + project_id` como contexto mínimo.
- Toda query SQL filtrada por esses identificadores via RLS — camada de aplicação não controla isolamento; o banco enforce.

## 5.3 RBAC — papéis e permissões

Papéis canônicos (definição de escopo e capacidades):

| `role_key` | Escopo | Capacidades principais |
|---|---|---|
| `founder` | org | tudo, inclui mudança de política, aprovações estruturais, acesso a todos os tenants (CKCompany apenas) |
| `org_admin` | org | gerir workspaces, membros, billing, permissões de workspace |
| `workspace_owner` | workspace | gerir projetos, membros do workspace, capabilities ativas |
| `operator` | project | operar nodes/workflows, acionar agentes, solicitar approvals |
| `reviewer` | project | ler e revisar outputs; não executa ações de impacto externo |
| `client` | project (curado) | ver projeção curada; aprovar o que lhe compete (escopo/proposta); nunca vê dados de outro cliente |
| `agent_service` | run-scoped (efêmero) | executar apenas skills/tools concedidas ao run corrente; token expira ao fim do run |

**Tabelas de persistência (doc 11 §4 e §4.1):**

```txt
project_members(id, project_id fk, user_id fk, role enum, invited_by, joined_at, expires_at)
-- definida em doc 11 §4

-- As tabelas abaixo estão definidas em doc 11 §4.1 (Patch 1.1.1 — Security Data Support).
-- Reproduzidas aqui para referência de política; a fonte canônica é doc 11 §4.1.

rbac_roles(id, org_id, role_key text unique, display_name, scope_level enum(org|workspace|project|run),
           description, is_system_role bool, created_at)

role_permissions(id, role_id fk→rbac_roles, scope_level, resource_type text,
                 action text, effect enum(allow|deny), conditions jsonb, priority int)

user_role_assignments(id, user_id fk, role_id fk→rbac_roles, scope_level,
                      scope_ref text, granted_by, granted_at, expires_at, revoked_at)
```

> **Nota:** RBAC estático (tabelas acima) é o piso. ABAC (§5.4) refina em runtime via atributos dinâmicos. O `policy_engine` (§5.5) combina ambos.

## 5.4 ABAC — atributos que refinam o RBAC

A decisão final combina **papel** e **atributos contextuais**. Um `operator` pode criar nodes, mas **não** executar ação com `risk_level=high + reversible=false` sem approval gate.

Atributos avaliados pelo `policy_engine` (10 §5.15):

| Atributo | Origem | Efeito exemplo |
|---|---|---|
| `data.sensitivity` | classificação do dado (§5.14) | `PII` → bloqueia sem mascaramento/policy explícita |
| `action.risk_level` | autonomy matrix (04) | `high` → exige approval |
| `action.reversible` | skill/workflow definition | `false + high risk` → exige approval + Metacognik review |
| `action.cost` | estimativa do Cost Guard (13) | acima do `cost_policy.max` → bloqueia |
| `project.status` | estado do projeto | `archived` → bloqueia mutações |
| `tenant` | `org_id` do token | cross-tenant → nega sempre |
| `time_window` | política de horário | fora da janela → nega ações de alto impacto |
| `agent.autonomy_level` | agentRegistry | autonomia insuficiente → exige humano |

## 5.5 Policy Engine e policyRegistry (fonte de autorização)

O `policy_engine` (doc 10 §5.15) é o **único árbitro de autorização** em runtime. Ele consulta três registries do policyRegistry como source-of-truth:

```txt
policyRegistry         → políticas de autorização geral (RBAC+ABAC rules)
approvalPolicyRegistry → quem aprova o quê, em qual risco, com qual timeout
memoryPolicyRegistry   → o que pode ser armazenado em memória, por quanto tempo, com que escopo
```

Esses registries seguem o **hybrid registry strategy** (doc 11 §6): definidos em arquivos canônicos → carregados ao DB no deploy → versionados em `registry_item_versions` → auditados via `audit_logs`. **Nenhum agente pode escrever diretamente nesses registries** — mudanças de política exigem PR aprovado + founder/technical approval.

Fluxo de avaliação do `policy_engine`:

```txt
1. Recebe: (actor_id, actor_type, action, resource_ref, context_snapshot)
2. Resolve papéis do ator via RBAC (rbac_roles + user_role_assignments)
3. Coleta atributos contextuais (ABAC): sensitivity, risk, reversible, cost, tenant...
4. Avalia regras do policyRegistry por prioridade descendente
5. Primeiro match wins: allow | deny
6. Se nenhuma regra: deny (default)
7. Emite PermissionGranted | PermissionDenied → events + audit_logs
```

**Proteção anti-self-escalation:** agentes **nunca** podem escrever em policyRegistry, approvalPolicyRegistry ou memoryPolicyRegistry. Tentativa gera `PolicyViolationDetected` + alerta imediato. (Ver também §5.7 e doc 21.)

## 5.6 Tenant isolation multi-nível

Isolamento de tenant é **estrutural**, não cosmético. Funciona em quatro camadas independentes — um bug de aplicação não deve ser suficiente para cruzar a fronteira de tenant.

### 5.6.1 RLS no Postgres

- Toda tabela de domínio tem `org_id` (e muitas têm `workspace_id`/`project_id`).
- Política RLS aplica `WHERE org_id = current_setting('app.current_org_id')` antes de qualquer query.
- Token de sessão define `current_org_id` no início da conexão/transaction.
- RLS é `FORCE` (aplica a todos, inclusive superusers da aplicação — nunca ao DB superuser, que não é exposto).
- **Resultado:** bug em ORM, controller ou agente não vaza dados de outro tenant — o Postgres nega na camada de storage.

```txt
Tabelas com RLS obrigatório (lista mínima — completa em doc 11):
organizations, workspaces, projects, project_members,
objects, object_versions, events, agent_runs, agent_permissions,
nodes, workflows, workflow_runs, capabilities, collectors,
context_packs, memories, evidence_items, decisions, artifacts,
cost_ledger_entries, eval_results, audit_logs, approval_requests,
approval_policies, registry_items, vector_collections
```

### 5.6.2 Vector namespace isolation

- Cada `vector_collection` tem `namespace = org_id::project_id` (definido em doc 11 `vector_collections.namespace`).
- O `rag_retriever` (doc 10 §5.15) recebe `namespace` como **pré-condição obrigatória** da busca semântica — **não como pós-filtro**.
- Busca sem `namespace` explícito é recusada pelo retriever antes de qualquer chamada ao vector store.
- Embeddings de um projeto/cliente nunca aparecem em resultado de outro: o índice é por namespace.

```txt
Regra de ouro: namespace ≠ pós-filtro de resultado → namespace = partição de índice.
```

### 5.6.3 Storage path isolation

- Artifacts binários (imagens, documentos, exports) armazenados em object storage com path estruturado:
  ```
  /{org_id}/{workspace_id}/{project_id}/{artifact_type}/{artifact_id}/{version}
  ```
- URLs de acesso são **signed + scoped**: geradas server-side com TTL e scope de tenant.
- Frontend nunca recebe paths raw ou credenciais de storage — recebe apenas signed URLs com escopo.
- Nenhum prefixo de path é acessível sem validar que `org_id` do path == `org_id` do token de sessão.

### 5.6.4 Redis isolation

- Keys Redis com prefixo `{org_id}:{namespace}:{key}` em todos os caches, queues e locks.
- Separação por namespace impede que um tenant leia/escreva keys de outro.
- Credenciais de Redis não são expostas a agentes ou ao frontend.

## 5.7 Agent permissions e capability scoping

Cada agente tem um **escopo fixo de capacidades** registrado em `agentRegistry` (doc 10 §5.14) e materializado em `agent_permissions` (doc 11):

```txt
agent_permissions(id, agent_id fk, scope enum(org|workspace|project|object|field),
                  resource text, action text, effect enum(allow|deny))
```

Regras de operação:

1. **Token efêmero por run**: o `agent_service` recebe um token com o mínimo necessário (least privilege), scoped ao run corrente. Expira ao fim do run — sem token persistente entre runs.
2. **Forbidden actions**: `agents.forbidden_actions jsonb` (doc 11) lista ações que o agente nunca pode executar, independente de permission grant.
3. **Data access scope**: `agents.data_access_scope jsonb` (doc 11) define quais objetos/tipos o agente pode ler/escrever.
4. **Anti-self-escalation**: agentes não podem solicitar aumento de permissão para si mesmos nem modificar `agent_permissions`, `policyRegistry` ou `approvalPolicyRegistry`. Qualquer tentativa é bloqueada + auditada.
5. **Tenant scope**: `agents.tenant_scope` (doc 11) define se o agente opera em escopo de org, workspace ou projeto — não pode operar acima do seu escopo.

## 5.8 Tool permissions (Tool Router deny-by-default)

O `tool_router` (doc 10 §5.5) implementa a regra de interseção:

```txt
allowed_tools = skill.allowed_tools  ∩  agent.capabilities  ∩  project.allowed_tools
```

- Se a interseção for vazia → tool bloqueada, `PermissionDenied` emitido.
- Tool **não** listada em nenhum dos três conjuntos → deny automático.
- Cada skill define `allowed_tools` explicitamente (doc 06 §skills_registry).
- Projeto pode restringir o conjunto de tools ativas (capability scoping via `capabilityRegistry`).
- Nenhum agente tem acesso irrestrito a todas as tools — least privilege é estrutural, não configurável por agente.

## 5.9 Collector / Provider / Actor permissions

Base taxonômica (doc 10 §10.2 / taxonomy §10.2):
- **Collector** = abstração CKOS visível ao produto → o que a UI/API conhece.
- **Actor** = executor técnico interno (conta/credencial/sessão) → resolvido server-side, **nunca exposto**.
- **Provider** = API externa (Apify, plataforma social, etc.) → **nunca chamado pelo frontend**.

**Regras de permissão de collector:**

```txt
1. Frontend chama APENAS POST /api/collectors/run  — sem acesso a provider, actor_id ou credencial.
2. collector_runner (doc 10 §5.18) valida, antes de executar:
   a. Collector registrado em collectorRegistry.
   b. Capability do collector habilitada para o projeto (capabilityRegistry).
   c. Actor tem credenciais válidas no vault (secret_ref válido + não expirado).
   d. Provider está no allowlist do projeto/org.
   e. Cost dentro do custo máximo definido na cost_policy do collector.
3. Actor_id NUNCA aparece em evento visível ao frontend, response body ou log não-redacted.
4. Provider endpoint NUNCA aparece em evento visível ao frontend.
5. Credenciais de actor ficam exclusivamente em vault; secret_ref é o único pointer.
```

**Tabelas de persistência relevantes (doc 11):**

```txt
agents(... data_access_scope jsonb, forbidden_actions jsonb)    -- inclui collectors como tipo de agente
agent_collectors(agent_id fk, collector_type)                   -- quais collectors o agente pode acionar
-- actorRegistry e providerRegistry: via registry_items (doc 11 §6), nunca expostos ao frontend
```

## 5.10 Model privacy policy

O `model_router` (doc 10 §5.5) consulta `modelRegistry.privacy_level` e `agents.model_policy_ref` (doc 11) antes de despachar uma chamada a modelo externo.

**Classificação de privacidade por dado:**

| Classificação do dado | Modelos permitidos |
|---|---|
| `public` | qualquer modelo registrado no modelRegistry |
| `internal` | modelos com `privacy_level ≥ internal` (exclui modelos sem GDPR/LGPD compliance) |
| `confidential` | apenas modelos aprovados com DPA assinado + lista restrita |
| `PII / sensitive` | modelos privacy-first explicitamente aprovados OU processamento on-premise |
| `PII + whitelabel client` | modelo aprovado pelo cliente + nunca train-on-data |

**Regras operacionais:**

1. `model_router` recebe `data_classification` do context pack (doc 10 §5.19) e filtra o `modelRegistry` antes de selecionar.
2. Nenhum dado PII/confidential é enviado a modelo externo sem que o `modelRegistry` item tenha `dpa_signed = true` e `trains_on_data = false`.
3. Em whitelabel: cada org pode ter `allowed_model_list` diferente — o model_router respeita o escopo de tenant.
4. Se nenhum modelo aprovado atender `data_classification`: run → `blocked` + `PermissionDenied` + Metacognik alert.
5. `agents.model_policy_ref` (doc 11) aponta para a política de modelo específica daquele agente (override do padrão).

## 5.11 Capability scoping

Capabilities (doc 10 §5.17) são portões funcionais que habilitam features por contexto (org/workspace/project). A segurança de capability funciona assim:

- Uma capability não ativada no projeto = feature inexistente para aquele tenant (não apenas ocultada — o `policy_engine` nega na execução).
- `capabilityRegistry` (doc 10 §5.14) define o conjunto de capabilities disponíveis.
- Ativação de capability requer: permissão de `workspace_owner` ou superior + registro no `capability_grants` (ver patch sugerido abaixo).
- Capabilities de alto risco (e.g., self-evolving, external data writes) exigem approval adicional.

```txt
-- A tabela abaixo está definida em doc 11 §11 (Patch 1.1.1 — Security Data Support).
-- Reproduzida aqui para referência de política de capability scoping; a fonte canônica é doc 11 §11.

capability_grants(id, org_id, workspace_id, project_id,
                  capability_id fk→capabilities,
                  granted_to_type enum(project|workspace|org),
                  granted_to_id uuid,
                  granted_by fk→users, granted_at,
                  expires_at, revoked_at,
                  status enum(active|revoked|expired),
                  approval_ref fk→approvals,
                  metadata jsonb)
```

## 5.12 Approval policies e approvalPolicyRegistry

O `approvalPolicyRegistry` (doc 10 §5.14) é a fonte canônica das regras de aprovação. O `approval_gate` (doc 10 §5.8) a consulta em todo ponto de pausa de workflow.

**Tabela de persistência (doc 11 — já definida):**

```txt
approval_policies(id, policy_key, action_or_risk, required_approvers jsonb,
                  auto_approval_allowed bool)  -- fonte: approvalPolicyRegistry
```

**Regras de operação:**

1. `approval_gate` pausa o workflow, emite `ApprovalRequested`, aguarda `ApprovalResolved`.
2. `required_approvers` é uma lista ordenada: o sistema tenta pela ordem, com timeout e escalonamento.
3. `auto_approval_allowed = true` apenas para ações de risco baixo + reversível (nível 04 §5.1-5.3).
4. **Agentes NUNCA podem criar, modificar ou deletar approval policies.** Qualquer tentativa gera `PolicyViolationDetected` + incident.
5. Mudança em approval policy = PR + `approval_required: [founder, technical]` + registro em `registry_item_versions`.
6. **Emergency bypass**: apenas Founder pode invocar; é time-limited (TTL máximo 24h), logged com justificativa, e gera alerta automático para Metacognik + QA Lead.

**Timeout e escalonamento:**

```txt
approval_expirations(id, approval_id fk, expires_at, action_on_expire enum(block|escalate|auto))
approval_escalations(id, approval_id fk, from_role, to_role, reason, escalated_at)
```

## 5.13 Decision rights enforcement

Baseado na Decision Rights Matrix (doc 10 §5.22). O `policy_engine` valida que o ator tem o direito de tomar a decisão antes de registrá-la.

**Hierarquia canônica:**

| Ator | `system_id` | Direito |
|---|---|---|
| Nick | `nick` | Sugere ação, coleta intent — não decide sozinho |
| Cognik | `cognik` | Interpreta, classifica, contextualiza — não decide por si |
| Metacognik | `metacognik` | **Veto**: bloqueia/audita decisões de risco alto; sem bypass por agente |
| PMO_CKOS | `pmo_ckos` | Recomenda estrutura, roadmap, escopo — não aprova sem Founder |
| QA Lead | `qa_lead` | Aprova qualidade técnica de outputs e builds |
| Founder | `founder` | Aprova decisões estruturais, mudanças de política, self-evolving |
| Client | `client` | Aprova escopo, proposta, contrato — não acessa internals |

**Regras de enforcement:**

1. Todo evento de decisão (`decision_made`) carrega `decision_level` e `decided_by`.
2. O `policy_engine` valida `decided_by.role` vs `decision_level` antes de registrar.
3. Metacognik tem poder de veto: se `metacognik_blocked = true` no evento, o workflow para independente de qualquer outra permissão.
4. Founder approval é requerido para: mudança de policy, ativação de self-evolving, novo superagent, mudança de taxonomia.
5. Client approval é limitado ao escopo definido no contrato do projeto (não acessa decisões internas do sistema).

## 5.14 PII e classificação de dados

**Classificação obrigatória em toda ingestão:**

```txt
public       → sem restrição de acesso ou distribuição
internal     → dentro do tenant; não compartilhado com terceiros sem consentimento
confidential → papéis específicos + log de todo acesso; não veta RAG dentro do tenant
PII          → criptografia em repouso; acesso auditado individualmente; mascaramento em prompts;
               não-vetorizável sem política explícita; retenção limitada por lei/contrato
sensitive    → combina PII + confidential; máxima restrição
```

**Regras operacionais:**

1. `memories.permission_level` (doc 11 §14) determina quem pode recuperar aquela memória no RAG.
2. PII **não entra** em context pack sem: necessidade comprovada + mascaramento automático quando possível.
3. `context_packs.forbidden_actions jsonb` (doc 11 §13) inclui ações proibidas para dados sensíveis do contexto.
4. RAG com dado `PII` requer `permission_level` explícito na `vector_collection` — vector sem classificação é recusado na indexação.
5. Campo PII descoberto em tabela não classificada → alerta para Metacognik + bloqueio de acesso até classificação.

## 5.15 Secrets management

**Regra fundamental: nenhum segredo persiste fora do vault.**

```txt
Proibido em produção:
- Token/API key em tabela de banco de dados (nem criptografado)
- Token/API key em variável de ambiente de aplicação
- Token/API key em event log ou trace
- Token/API key em response body ou prompt
- Token/API key em código-fonte ou config file versionado
```

**Arquitetura:**

1. `integrations.secret_ref` (doc 11) aponta para o vault path — nunca contém o segredo.
2. `actors.credential_ref` (actorRegistry item) aponta para vault — nunca exposto ao frontend.
3. O `collector_runner` (doc 10 §5.18) resolve o `secret_ref` server-side, usa a credencial e descarta — nunca propaga.
4. Logs e traces passam por **redação automática** antes de persistir: padrões de API key, token, senha são substituídos por `[REDACTED]`.
5. Rotação de segredos: vault-managed, com janela de sobreposição (old + new válidos durante rotação) e escopo por project/org.
6. Cada tenant tem suas credenciais isoladas — credencial de um projeto não é usada em outro (whitelabel real).

```txt
-- A tabela abaixo está definida em doc 11 §12.1 (Patch 1.1.1 — Security Data Support).
-- Reproduzida aqui para referência de política de secrets management; a fonte canônica é doc 11 §12.1.

secret_refs(
  id              uuid primary key,
  org_id          fk→organizations [RLS],
  workspace_id    fk→workspaces,
  project_id      fk→projects,
  ref_key         text,
  vault_path      text,        -- NUNCA contém o segredo real; caminho no vault externo
  secret_type     enum(api_key|oauth_token|service_account|webhook_secret|database_url|custom),
  owner_type      enum(integration|collector|tool|actor|provider),
  owner_ref       text,
  status          enum(active|rotating|revoked|expired),
  expires_at      timestamptz,
  last_rotated_at timestamptz,
  created_by      fk→users,
  created_at      timestamptz
)
```

## 5.16 Audit trail

Toda ação relevante de segurança e acesso gera entrada append-only em `audit_logs` (doc 11 §26 MVP P0).

**Eventos que obrigatoriamente vão para audit_logs:**

```txt
PermissionGranted / PermissionDenied          — toda decisão de authz
ApprovalRequested / ApprovalResolved          — approval gate
PolicyViolationDetected                       — tentativa de auto-escalação ou bypass
SecretRedacted                                — token detectado e redatado em log
TenantBoundaryViolationAttempted              — tentativa cross-tenant
CapabilityScopeViolation                      — agente tenta tool fora do scope
AgentPermissionDenied                         — agente sem permissão para ação/tool
PIIAccessLogged                               — acesso a dado classificado como PII
AgentPolicyModificationAttempt                — agente tenta alterar policy
ApprovalPolicyChanged                         — mudança em approval policy (com quem mudou)
EmergencyBypassActivated                      — bypass de Founder (sempre auditado)
```

**Estrutura da tabela (doc 11 — definida, expandida aqui):**

```txt
audit_logs(
  id              uuid primary key,
  org_id          fk→organizations  [RLS],
  workspace_id    fk→workspaces,
  project_id      fk→projects,
  event_type      text,              -- tipo do evento de audit
  actor_id        text,              -- system_id do agente ou user_id do humano
  actor_type      enum(user|agent|system),
  resource_type   text,              -- tipo do recurso afetado
  resource_ref    text,              -- id do recurso
  action          text,
  effect          enum(allow|deny),
  context_snapshot jsonb,            -- snapshot mínimo: role, risk_level, tenant
  source_event_id fk→events,        -- evento de runtime que originou
  created_at      timestamptz default now()
) [APPEND-ONLY — sem UPDATE/DELETE; compensação por novo entry]
[idx: org_id, project_id, event_type, created_at, actor_id]
```

## 5.17 Retenção e ciclo de vida de dados

- Retenção definida por: classificação do dado + contrato whitelabel + lei aplicável.
- `memoryPolicyRegistry` (doc 10 §5.14) define políticas de retenção por tipo de memória e scope.
- Job de expiração aplica `soft delete` (nunca DELETE físico — compensating event `DataExpired`).
- Dados `PII` com retenção expirada são anonimizados/deletados por job auditado.
- `audit_logs` têm retenção mínima de 12 meses (regulatório) — imutáveis.
- `events` (event store, doc 11 §7) são imutáveis por design; expiração via archiving (não DELETE).

## 5.18 Whitelabel data isolation

Whitelabel real (Constituição §P8) requer isolamento estrutural:

| Camada | Isolamento |
|---|---|
| Banco de dados | `org_id` + RLS em toda tabela de domínio |
| Vector store | `namespace = org_id::project_id` — índice separado por tenant |
| Object storage | path prefix `/{org_id}/...` + signed URLs scoped |
| Redis / cache | key prefix `{org_id}:{ns}:` em todos os keys |
| Secrets / vault | credenciais isoladas por org/project — sem compartilhamento |
| Memória / RAG | `permission_level` + namespace: memória de um cliente nunca recuperável por outro |
| Logs / traces | logs filtrados por `org_id` antes de qualquer acesso de suporte |
| UI projections | read models computados por tenant; frontend recebe apenas projeção do próprio tenant |

**Skin de whitelabel** (tema, linguagem, módulos) é configuração em `workspace.theme_tokens` — independente e não-relacionada com o isolamento de dados acima.

## 5.19 Prevenção de vazamento cross-project/client

Além do isolamento por tenant (§5.6), o sistema aplica prevenção de vazamento a nível de projeto dentro do mesmo tenant:

1. **Compartilhamento de contexto**: context pack (doc 10 §5.19) inclui apenas objetos do projeto corrente. Referência a objetos de outro projeto requer `cross_project_correlation` explícita, aprovada e auditada.
2. **RAG cross-project**: bloqueado por default. Ativação requer policy explícita em `memoryPolicyRegistry` + permissão de `workspace_owner`.
3. **Agente com escopo de org**: apenas superagents com `tenant_scope = org` podem consultar múltiplos projetos — e apenas os campos definidos em `data_access_scope`.
4. **Client visibility**: usuário com papel `client` recebe projeção curada do próprio projeto; nunca tem acesso a nomes, dados ou artefatos de outro projeto/cliente — mesmo que ambos estejam na mesma org.
5. **Handoffs entre agentes**: event `AgentHandoff` carrega apenas o contexto explicitamente passado — não o contexto completo do run anterior.

## 5.20 Safe defaults

Quando não há política explícita ou configuração está incompleta:

```txt
Autorização         → deny (nunca allow acidental)
Capability          → desativada (usuário precisa ativar explicitamente)
Model selection     → modelo mais conservador/privado da lista
Data classification → internal (nunca public por default)
Approval gate       → requerido para qualquer ação de risco médio ou alto
Agent token scope   → run-scoped mínimo (sem token persistente)
Collector actor     → sem credencial sem vault_ref válido = bloqueado
Cross-project RAG   → bloqueado (opt-in)
Secrets in logs     → redatados automaticamente
Retry on deny       → sem retry automático (log + alert, espera intervenção humana)
```

## 5.21 Declaração de componentes de runtime (template §9.1)

| Componente | Detalhe |
|---|---|
| **Registries afetados** | `policyRegistry` (lê + impõe); `approvalPolicyRegistry` (lê + impõe); `memoryPolicyRegistry` (lê); `capabilityRegistry` (lê para scoping); `actorRegistry` (lê para permissão de collector); `agentRegistry` (lê para capability scope e forbidden_actions); `modelRegistry` (lê para privacy policy) |
| **Engines afetados** | `policy_engine` (owner de autorização); `approval_gate` (enforce approval policies); `tool_router` (enforce tool deny-by-default); `agent_router` (enforce agent permissions); `collector_runner` (enforce actor/provider separation); `rag_retriever` (enforce vector namespace + permission_level); `context_pack_builder` (snapshot de permissões no context pack) |
| **State machines afetadas** | `approval` (pausa em approval gate); `agent_run` (blocked por permission deny ou policy violation) |
| **Eventos emitidos** | `PermissionGranted`, `PermissionDenied`, `ApprovalRequested`, `ApprovalResolved`, `PolicyViolationDetected`, `SecretRedacted`, `TenantBoundaryViolationAttempted`, `CapabilityScopeViolation`, `AgentPermissionDenied`, `PIIAccessLogged`, `AgentPolicyModificationAttempt`, `ApprovalPolicyChanged`, `EmergencyBypassActivated`, `DataExpired` |
| **Tabelas/logs necessários** | `audit_logs`, `agent_permissions`, `approval_policies`, `approval_expirations`, `approval_escalations`, `project_members`, `vector_collections`, `context_packs.permissions_snapshot`, `retrieval_logs.permission_filtered`, `events` (filtro por `event_type`) + patches sugeridos: `rbac_roles`, `role_permissions`, `user_role_assignments`, `capability_grants`, `secret_refs` |
| **Policies envolvidas** | policyRegistry (RBAC+ABAC rules); approvalPolicyRegistry (approval gates); memoryPolicyRegistry (retention + access); model privacy policies; capability grants; tool allowlists |
| **Failure modes** | vault indisponível → bloqueia runs que precisam de credencial (fail-closed); policy_engine timeout → deny (fail-closed); RLS misconfigured → acesso bloqueado até correção; approval timeout → escalona ou bloqueia (conforme `action_on_expire`) |
| **Rollback / compensating actions** | `PermissionRevoked` (compensa grant); `DataExpired` (compensa retenção); `ApprovalRevoked` (compensa approval); `EmergencyBypassRevoked` (compensa bypass); `CapabilityRevoked` (compensa capability_grant) |
| **Observability / evals / cost hooks** | Toda `PermissionDenied` + `PolicyViolationDetected` vai para eval de segurança (13); `SecretRedacted` gera alerta de nível P1; `TenantBoundaryViolationAttempted` gera alerta P0; audit_logs são a base do compliance report (13); sem cost hooks diretos (segurança não tem custo de modelo) |

# 6. Agente responsável

- Owner documental: `PMO_CKOS`
- Responsável de risco/auditoria: `Metacognik` (veto de decisões de alto risco; auditoria contínua)
- Implementação runtime: `Builder Lead`
- Validação de qualidade: `QA Lead`

# 7. Superagentes envolvidos

| Agente | Papel neste documento |
|---|---|
| Metacognik | Auditoria de risco; veto de ações de risco alto; detecção de self-escalation |
| Builder Lead | Implementação do policy_engine, RLS, tool_router e audit trail |
| QA Lead | Validação de cobertura de RLS; testes de permissão e isolamento |
| PMO_CKOS | Governança; owner de policyRegistry e approvalPolicyRegistry |
| Founder | Aprovação de mudanças em policies e approval policies; emergency bypass |

# 8. Skills necessárias

```txt
permission-check          — avalia pode(ator, ação, recurso, contexto)
rls-enforcement           — aplica RLS no banco; valida cobertura
pii-classification        — classifica dado na ingestão; mascara em prompts
secrets-resolution        — resolve secret_ref via vault; nunca retorna segredo nu
audit-logging             — registra eventos de segurança no audit_log
tenant-isolation-check    — valida que operação não cruza fronteira de tenant
capability-scoping        — verifica capability habilitada antes de executar feature
model-privacy-routing     — seleciona modelo compatível com data_classification
approval-policy-eval      — consulta approvalPolicyRegistry e determina approvers
decision-rights-check     — valida que ator tem direito à decisão que está tomando
```

# 9. Prompts relacionados

Não aplicável (documento de arquitetura). Prompts de `risk-classification` e `pii-classification` estão em `08_PROMPT_LIBRARY.md`.

# 10. Integrações

| Sistema | Como integra |
|---|---|
| Postgres (doc 11) | RLS em toda tabela de domínio; tabelas de permissão, audit_logs |
| policy_engine (doc 10 §5.15) | Árbitro de autorização; consulta policyRegistry + approvalPolicyRegistry |
| tool_router (doc 10 §5.5) | Enforce interseção de tools permitidas |
| agent_router (doc 10 §5.5) | Enforce agent permissions |
| approval_gate (doc 10 §5.8) | Enforce approval policies em pausa de workflow |
| collector_runner (doc 10 §5.18) | Enforce actor/provider separation |
| rag_retriever (doc 10 §5.15) | Enforce vector namespace + permission_level |
| Vault de segredos | Armazena credenciais; `secret_ref` como único pointer |
| Auth/SSO | Identidade do usuário; derivação de `org_id` do token |
| Tracing (doc 13) | Redação automática de segredos; audit de eventos de segurança |

# 11. Memória e contexto

- `memories.permission_level` (doc 11 §14) governa acesso via RAG: cada memory tem classificação; RAG retriever filtra por `permission_level ≤ actor.max_clearance`.
- `context_packs.permissions_snapshot` (doc 11 §13) guarda snapshot de permissões no momento da criação do context pack — permite replay auditado.
- `context_packs.forbidden_actions` (doc 11 §13) transmite ao agente a lista de ações proibidas para o contexto corrente.
- Nenhum dado `PII` entra na memória de longo prazo sem política explícita; memória de curto prazo (sessão) é varrida ao fim da sessão.
- `memoryPolicyRegistry` define: o que pode ser memorizado, por qual tipo de agente, por quanto tempo, com qual classificação.

# 12. Edge cases

| Cenário | Resposta do sistema |
|---|---|
| **Agente tenta tool fora do scope** | `tool_router` nega; `CapabilityScopeViolation` → audit_log; run continua sem a tool; Metacognik alertado se recorrente |
| **Tentativa cross-tenant** | RLS bloqueia no banco; `TenantBoundaryViolationAttempted` → audit_log + alerta P0 imediato |
| **PII em prompt/context sem política** | `context_pack_builder` bloqueia inclusão; `PIIAccessLogged`; run pausa aguardando revisão |
| **Segredo detectado em log** | Redação automática substitui por `[REDACTED]`; `SecretRedacted` → audit_log + alerta P1 |
| **Agente tenta modificar policyRegistry** | `policy_engine` nega + `AgentPolicyModificationAttempt` → audit_log + incident P0 |
| **Approval expirado sem resolução** | `action_on_expire` determina: `block` congela o run; `escalate` sobe hierarquia; `auto` só para risco baixo |
| **Vault indisponível** | Fail-closed: runs que dependem de credencial são bloqueados; sem tentativa de fallback com credencial em memória |
| **Collector expõe actor_id ao frontend** | Nunca ocorre por design (resolver server-side); se detectado em resposta, redação + incident |
| **Cliente tenta ver dados de outro cliente** | RLS bloqueia; projeção curada só inclui dados do próprio tenant/projeto |
| **Self-evolving agente tenta ampliar próprias permissões** | Bloqueado + `PolicyViolationDetected` + sandbox lock (doc 21 §5.4) |

# 13. Métricas de sucesso

```txt
0 vazamentos cross-tenant confirmados
0 segredos em log ou trace (% de redações bem-sucedidas = 100%)
100% das tabelas de domínio com RLS ativo e testado
0 tentativas de self-escalation não detectadas
% de ações com authz check explícito = 100% para ações de impacto médio ou alto
% de PII classificada na ingestão ≥ 95% (meta: 100%)
Tempo de revogação de acesso (grant → efectivo) ≤ 60 segundos
% de approval policies com timeout e escalonamento definidos = 100%
Cobertura de audit_log para eventos de segurança = 100% dos listados em §5.21
```

# 14. Critérios de aprovação

- Deny-by-default documentado e implementado em `policy_engine`;
- RBAC+ABAC definidos com papéis, permissões e atributos;
- RLS cobre 100% das tabelas de domínio listadas em §5.6.1;
- Agentes operam com least privilege e token efêmero;
- Agentes não podem modificar policyRegistry/approvalPolicyRegistry;
- PII classificada, mascarada em prompts, não-vetorizável sem policy;
- Segredos exclusivamente em vault com `secret_ref`;
- Audit trail completo para eventos de §5.21;
- Vector namespace isolation como pré-condição (não pós-filtro);
- Storage paths scoped por tenant;
- Whitelabel isola estruturalmente dados, memória, embeddings e segredos;
- Decision Rights Matrix enforced pelo policy_engine;
- Approval policies não modificáveis por agentes.

# 15. Critérios de reprovação

- Acesso default-allow em qualquer camada;
- Ausência de RLS em qualquer tabela de domínio;
- Agentes com permissão de escrever em policyRegistry/approvalPolicyRegistry;
- PII vetorizada sem policy ou namespace;
- Segredos em tabela, log, código ou response body;
- Vector namespace aplicado como pós-filtro (risco de leak);
- Whitelabel apenas cosmético (sem isolamento estrutural);
- Audit trail incompleto (missing eventos de §5.21);
- Approval bypass sem registro e sem alerta;
- Collector expondo provider/actor ao frontend;
- Modelo externo recebendo dado PII sem DPA confirmado.

# 16. Related notes

- [[04_AUTONOMY_AND_APPROVALS]]
- [[10_SYSTEM_RUNTIME_ARCHITECTURE]]
- [[11_DATA_MODEL_AND_PERSISTENCE]]
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]]
- [[25_SELF_EVOLVING_SYSTEM_ARCHITECTURE]]
