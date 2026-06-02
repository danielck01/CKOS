---
title: Architecture Patch Report — Runtime System Coherence
file: ARCHITECTURE_PATCH_REPORT.md
phase: ROOT
category: governance_report
version: 1.10.2
status: active
owner: PMO_CKOS
responsible_agent: metacognik
reviewers:
  - founder
  - metacognik
  - qa_lead
approval_required:
  - founder
  - metacognik
generated_date: 2026-05-25
covers_sessions: Runtime System v1.1.x coherence pass (docs 10–13 + governance 00); Product System v1.2.x coherence pass (docs 14–16 + patches P10-1 + P11-1–P11-8); Implementation System v1.2.0 (doc 17); Implementation System docs 18/19/20 v1.0.0 (Research Protocol, Claude/Codex/Antigravity, QA and Founder Approval); Business Systems docs 21–24 v1.0.0 (ROI Architecture, Feedback System, Support System, Credits/Plans/Billing) — Gate I completo
purpose: Relatório auditável de todos os patches aplicados à documentação CKOS durante o passe de coerência do Runtime System — registra estado anterior, estado posterior, justificativa, dependências resolvidas, patches diferidos e gate de próxima fase.
---

# ARCHITECTURE PATCH REPORT
## Runtime System Coherence Pass — CKOS v1.1.x

> **Leitura obrigatória antes de iniciar docs 14–16 (Product System).**  
> Este relatório é fonte de rastreabilidade para PMO_CKOS, Metacognik e Founder.  
> Não implementa backend, migrations, UI ou agentes. É documentação pura.

---

# 1. Resumo Executivo

Este relatório cobre o passe completo de coerência da fase `03_RUNTIME_SYSTEM`, incluindo as correções de governança que o precederam. O resultado é um conjunto de 4 documentos runtime sincronizados e mutuamente referenciáveis:

| Doc | Título | Versão final | Status |
|-----|--------|:------------:|--------|
| `10` | System Runtime Architecture | **1.1.0** | draft |
| `11` | Data Model and Persistence | **1.1.1** | draft |
| `12` | Security, Permissions and Data Governance | **1.1.0** | draft |
| `13` | Evals, Observability and Cost Control | **1.1.0** | draft |

Governança atualizada em paralelo:

| Doc | Título | Versão final | Status |
|-----|--------|:------------:|--------|
| `00_DOCUMENT_TEMPLATE` | Document Template | **2.2.0** | active |
| `00_TAXONOMY_AND_NAMING` | Taxonomy and Naming | **2.2.0** | active |
| `00_MASTER_MAP` | Master Map | **2.2.0** | active |
| `00_DEPENDENCY_MAP` | Dependency Map | **2.2.0** | active |

**Pré-condição da Product System (14–16) verificada:** ✅  
Docs 10, 11, 12 e 13 existem, estão versionados e são mutuamente coerentes — conforme exige `00_DEPENDENCY_MAP §8`.

---

# 2. Escopo do Passe

## 2.1 O que foi feito

1. **Micro-correção de governança** — normalização de enums snake_case em todos os headers YAML dos docs de governança e runtime.
2. **Patch mínimo de alinhamento doc 10** — YAML + nota estratégica de Model Router.
3. **Criação integral doc 12** — Security, Permissions and Data Governance v1.1.0.
4. **Micro-patch doc 11 v1.1.1** — tabelas de RBAC, capability_grants e secret_refs.
5. **Criação integral doc 13** — Evals, Observability and Cost Control v1.1.0.
6. **Geração deste relatório e do QA_DOCUMENTATION_CHECKLIST.**

## 2.2 O que não foi feito (fora de escopo obrigatório)

- ❌ Nenhuma migration ou SQL de produção criado
- ❌ Nenhum backend, frontend ou UI implementado
- ❌ Nenhum novo agente criado fora da taxonomia
- ❌ Nenhuma nova fase ou pack criada
- ❌ Documentos originais em `CKOS_DOCUMENTATION/` não foram tocados

---

# 3. Log de Patches por Documento

## 3.1 `00_DOCUMENT_TEMPLATE.md` — v2.1.0 → v2.2.0

**Justificativa:** Enum `approval_required` usava valores em display_name (ex: `Metacognik`). A regra das três formas de naming (§13.1 da Taxonomy) exige snake_case para system_id em todos os enums YAML.

| Campo | Antes | Depois |
|-------|-------|--------|
| `version` | `2.1.0` | `2.2.0` |
| `reviewers` | `- Metacognik` | `- metacognik` |
| `approval_required` (exemplo) | `[founder, Metacognik]` | `[founder, metacognik]` |
| `approval_required` (enum §7.3) | `none \| founder \| pmo_ckos \| technical \| client \| legal \| Metacognik` | `none \| founder \| pmo_ckos \| technical \| client \| legal \| qa_lead \| metacognik` |
| `categories` (§8) | sem `runtime_data` | adicionado `runtime_data` |

**Adições:**
- §8: `runtime_data` — categoria exclusiva para documentos de schema físico/persistência (doc 11).
- §7.3: nota explícita sobre `system_id` em snake_case com referência a `§13.1`.

**Nota sobre `runtime_observability`:** doc 13 usa esta categoria. Patch para o template registrado como pendência — requer autorização Founder/PMO_CKOS explícita antes de aplicar.

---

## 3.2 `00_TAXONOMY_AND_NAMING.md` — v2.1.0 → v2.2.0

**Justificativa:** Ausência de regra formal sobre as três formas de naming causava inconsistência entre YAML, prose e prompts.

| Campo | Antes | Depois |
|-------|-------|--------|
| `version` | `2.1.0` | `2.2.0` |
| `reviewers` | `- Metacognik` | `- metacognik` |
| `approval_required` | `[founder, Metacognik]` | `[founder, metacognik]` |

**Adições:**
- **§13.1 Regra das três formas de naming (obrigatória):**

| system_id | display_name | mention |
|-----------|--------------|---------|
| nick | Nick | @nick |
| cognik | Cognik | @cognik |
| metacognik | Metacognik | @metacognik |
| pmo_ckos | PMO_CKOS | @pmo_ckos |
| qa_lead | QA Lead | @qa_lead |
| builder_lead | Builder Lead | @builder_lead |
| datta | Datta | @datta |
| ops | Ops | @ops |
| campaign | Campaign | @campaign |

**5 regras formalizadas:** campos YAML usam system_id; prose usa display_name; mentions usam @system_id; mistura é proibida; system_id é a forma raiz.

---

## 3.3 `00_MASTER_MAP.md` — v2.1.0 → v2.2.0

| Campo | Antes | Depois |
|-------|-------|--------|
| `version` | `2.1.0` | `2.2.0` |
| `reviewers` | `- Metacognik` | `- metacognik` |

`approval_required: [founder]` — já estava limpo, sem alteração.

---

## 3.4 `00_DEPENDENCY_MAP.md` — v2.1.0 → v2.2.0

| Campo | Antes | Depois |
|-------|-------|--------|
| `version` | `2.1.0` | `2.2.0` |
| `reviewers` | `- Metacognik` | `- metacognik` |

`approval_required: [founder]` — já estava limpo, sem alteração.

---

## 3.5 `10_SYSTEM_RUNTIME_ARCHITECTURE.md` — YAML patch + §5.5 Model Router note

**Versão:** mantida em `1.1.0` (o doc foi criado na versão correta; este foi um patch de YAML + adição estratégica).

| Campo | Antes | Depois |
|-------|-------|--------|
| `reviewers` | `[Metacognik, QA Lead]` | `[metacognik, qa_lead]` |
| `approval_required` | `[founder, technical, Metacognik]` | `[founder, technical, metacognik]` |

**Adição — §5.5 Model Router, nota estratégica:**

> CKOS não possui nem treina um foundation model. CKOS possui a **camada de orquestração de modelos**: model registry, model router, context pack, memory, prompts, instructions, policies, evals, fallbacks, cost guard e learning loop. LLMs externos são **cognitive engines substituíveis** — selecionados por task segundo risk level, privacy classification, budget envelope, latency requirement e quality threshold.
>
> A substituição de modelo nunca deve exigir mudanças de arquitetura — apenas updates no model registry e routing policy.

**Justificativa:** Clarifica um risco arquitetural frequente — assumir que CKOS "depende" de um modelo específico, quando o correto é que CKOS é o orchestration layer acima de qualquer LLM.

---

## 3.6 `11_DATA_MODEL_AND_PERSISTENCE.md` — v1.1.0 → v1.1.1

**Justificativa:** doc 12 (Security) ao ser criado revelou necessidade de 5 tabelas não cobertas no doc 11: `rbac_roles`, `role_permissions`, `user_role_assignments`, `capability_grants`, `secret_refs`. O micro-patch as adiciona sem reescrever o documento.

### Tabelas adicionadas

**§4.1 — RBAC Permission Tables (inseridas no Core Entity Model):**

```
rbac_roles          — papéis por org; system_role vs custom
role_permissions    — allow/deny por resource_type/action/conditions
user_role_assignments — binding user→role com scope_ref + expires_at
```

**§11 (Capability System Persistence) — tabela adicionada:**

```
capability_grants   — concessão de capability a project/workspace/org
                      com approval_ref, expires_at, revoked_at
```

**§12.1 (Security / Collector Section) — nova subseção:**

```
secret_refs         — referência a segredo em vault EXTERNO
                      vault_path NUNCA contém segredo real
                      6 regras de segurança obrigatórias
```

**Adições ao YAML:**
| Campo | Antes | Depois |
|-------|-------|--------|
| `version` | `1.1.0` | `1.1.1` |
| `reviewers` | `[Metacognik, QA Lead]` | `[metacognik, qa_lead]` |

**Seção adicionada ao corpo:** "Patch 1.1.1 — Security Data Support" com tabela de resumo, adições MVP P0 e status de dependências.

---

## 3.7 `12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md` — CRIADO v1.1.0

**Status:** documento novo (não existia na estrutura anterior). Criado diretamente na versão 1.1.0 (sincronizado com docs 10 v1.1.0 + 11 v1.1.1).

**Estrutura:** 34 seções (§1–§16 de template + 21 subseções de §5).

### Políticas definidas

| Política | Seção | Resumo |
|----------|-------|--------|
| Deny-by-default | §5.1 | Toda decisão de authz começa como DENY; ALLOW é exceção registrada |
| Hierarquia de scope | §5.2 | org → workspace → project → field |
| RBAC 7 papéis | §5.3 | owner, admin, member, analyst, viewer, agent_runner, auditor |
| ABAC 7 atributos | §5.4 | data.sensitivity, action.risk_level, action.reversible, action.cost, project.status, tenant, time_window |
| policyRegistry source-of-truth | §5.5 | Agentes NUNCA escrevem em policyRegistry; tentativa → P0 |
| RLS multi-tenant | §5.6 | org_id em todas as tabelas de domínio; pgRLS ativo |
| Isolamento de vetor | §5.7 | namespace como pré-condição, não pós-filtro |
| Isolamento de storage | §5.8 | path prefix org_id/project_id; cross-path negado |
| Isolamento de memória | §5.9 | org_id + project_id em todas as queries de memória |
| Vault-only para segredos | §5.15 | Tokens/chaves NUNCA em tabelas normais; só secret_ref→vault |
| Anti-self-escalation | §5.16 | Agentes não alteram approvalPolicyRegistry; PR + founder/technical |
| Model privacy policy | §5.12 | PII → modelos aprovados com DPA+no-train; 4 levels |
| Collector resolution server-side | §5.11 | Frontend APENAS POST /api/collectors/run; actor resolvido server-side |
| Decision Rights Matrix enforcement | §5.17 | Nick→Cognik→Metacognik→PMO→QA Lead→Founder→Client |
| Safe defaults | §5.20 | 8 defaults explícitos em caso de falha de authz |
| Whitelabel isolation | §5.19 | tenant_id + branding_config; cross-tenant structurally impossible |

### 14 Eventos de Segurança Definidos

| Severidade | Evento | SLA |
|-----------|--------|-----|
| P0 | TenantBoundaryViolationAttempted | ≤ 5 min |
| P0 | AgentPolicyModificationAttempt | ≤ 5 min |
| P0 | EmergencyBypassActivated | ≤ 5 min |
| P1 | SecretRedacted | ≤ 15 min |
| P1 | PolicyViolationDetected | ≤ 15 min |
| P1 | ApprovalPolicyChanged | ≤ 15 min |
| P1 | VectorNamespaceViolationAttempted | ≤ 15 min |
| P2 | PIIBlockedFromPrompt | ≤ 1 h |
| P2 | ModelPrivacyPolicyViolation | ≤ 1 h |
| P2 | CollectorProviderExposureBlocked | ≤ 1 h |
| P2 | CapabilityScopeViolation | ≤ 1 h |
| P2 | AgentPermissionDenied | ≤ 1 h |
| P3 | PIIAccessLogged | batch |
| P3 | PermissionDenied | batch |

### §5.21 Runtime Declaration (template §9.1)
- 7 registries, 7 engines, 2 state machines
- 14 security events (todos os acima)
- Todas as tabelas de doc 11 referenciadas
- Failure modes e rollback events
- Observability hooks para doc 13

---

## 3.8 `13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md` — CRIADO v1.1.0

**Status:** documento novo (substituiu esboço anterior). Criado diretamente em v1.1.0 (sincronizado com docs 10/11/12).

**Estrutura:** 34 seções (§1–§25 de conteúdo + §26–§34 de template).

### Cobertura por seção

| § | Conteúdo | Destaques |
|---|----------|-----------|
| §3 | 7 Princípios de Observabilidade | Base filosófica do sistema de confiança |
| §4 | 15 target kinds de eval | Com fonte em tabelas doc 11 |
| §5 | 14 tipos de eval | deterministic → LLM-as-judge → human review → Metacognik audit |
| §6 | 12 dimensões de eval de agente | thresholds + tabelas |
| §7–9 | Evals de skill/workflow/RAG | coverage, latência, hallucination, fonte |
| §10 | Model Observability | nota estratégica + 7 métricas + 11 critérios de routing |
| §11 | Cost Guard 8-step flow | budget_check → soft_warn → hard_block → escalation |
| §12 | Cost ledger metrics | 8 tabelas doc 11 §18 |
| §13 | 14 security events | P0–P3 severity + SLA de resolução |
| §14 | Run Replay | 9 dimensões de reconstrução de incidente |
| §15 | Loop Detection | 7 parâmetros + tabela de ação por tipo de loop |
| §16 | 8 Quality Gates | pontos críticos antes de output/artifact/proposal/RAG trust |
| §17 | Metacognik Audit Layer | 9 triggers + poder de veto |
| §18 | QA Lead Review Layer | 8 triggers |
| §19 | 10 Dashboards de Observabilidade | com fontes doc 11 |
| §20 | 14 entradas de alerting | P0–P3, canal, SLA |
| §21 | Learning Loop Metrics | 7 tabelas + semi-automático MVP |
| §22 | MVP P0 (11 itens in, 8 out) | scope freeze |
| §23 | 11 edge cases | |
| §24 | 18 métricas com targets | |
| §32 | Runtime Declaration | 4 registries, 5 engines, 4 state machines, 11 events, 19+ tabelas |

---

# 4. Matriz de Dependências Resolvidas

```
Doc 12 depende de:  10 (policyRegistry, engines) ✅   11 (tabelas domain) ✅
Doc 13 depende de:  10 (eval_runner, cost_guard) ✅   11 (eval_results, cost_ledger) ✅   12 (security events) ✅
Doc 11 v1.1.1 depende de:  12 (tabelas RBAC, secret_refs como patch reverso) ✅

Cadeia completa:  10 → 11 → 12 → 13   (bidirecional por cross-reference)
```

### Tabelas cross-referenced entre docs

| Tabela | Definida em | Usada em |
|--------|-------------|----------|
| `rbac_roles`, `role_permissions`, `user_role_assignments` | 11 §4.1 | 12 §5.3 |
| `capability_grants` | 11 §11 | 12 §5.13 |
| `secret_refs` | 11 §12.1 | 12 §5.15 |
| `audit_logs` | 11 §17 | 12 §5.21, 13 §13 |
| `eval_results`, `eval_scores` | 11 §15 | 13 §4, §5 |
| `cost_ledger`, `cost_daily_totals` | 11 §18 | 13 §11, §12 |
| `model_calls` | 11 §18 | 13 §10 |
| `run_replays`, `run_replay_events` | 11 §22 | 13 §14 |
| `hallucination_checks` | 11 §15 | 13 §8 |
| `learning tables` (7) | 11 §24 | 13 §21 |
| `policyRegistry` | 10 §5.6 | 12 §5.5, 12 §5.16 |
| `approvalPolicyRegistry` | 10 §5.6 | 12 §5.16 |

---

# 5. Patches Diferidos (não aplicados)

Os itens abaixo foram identificados durante o passe mas explicitamente diferidos. Cada um requer decisão de governança antes de aplicar.

## 5.1 `runtime_observability` no template §8

**Situação:** doc 13 usa `category: runtime_observability` conforme especificado. O enum do template §8 ainda não inclui esta categoria (tem `runtime_data` adicionado, não tem `runtime_observability`).

**Impacto:** inconsistência menor de template — doc 13 é válido semanticamente mas não passa em validação automática de enum se esta for implementada.

**Ação requerida:** Founder/PMO_CKOS autoriza explicitamente; então aplicar patch ao template v2.2.0 → v2.3.0 adicionando `runtime_observability`.

**Responsável:** PMO_CKOS  
**Gate:** antes de qualquer validator automático de YAML ser implementado

---

## 5.2 Migração global `owner`/`responsible_agent` para snake_case

**Situação:** §13.1 da Taxonomy define que system_id (snake_case) é a forma raiz. Campos `owner` e `responsible_agent` em todos os 25 docs canônicos ainda usam display_name (ex: `owner: PMO_CKOS`, `responsible_agent: Metacognik`).

**Impacto:** inconsistência de naming que não afeta runtime MVP mas viola a regra §13.1 em documentação.

**Escopo:** ~25 docs; mudança mecânica, sem lógica.

**Ação requerida:** passar explicitamente pelo PMO_CKOS antes de iniciar; aplicar em uma única PR com regex; verificar docs auxiliares (READMEs) também.

**Responsável:** PMO_CKOS  
**Gate:** pode ser feito em qualquer momento sem bloquear Product System

---

## 5.3 READMEs auxiliares com `reviewers: - Metacognik`

**Situação:** `00_README_SYSTEM_GOVERNANCE.md` e possivelmente outros READMEs auxiliares ainda têm `reviewers: - Metacognik` (display_name).

**Impacto:** baixo — READMEs não são docs canônicos.

**Ação requerida:** sweep de normalização; pode ser feito junto com 5.2.

---

# 6. Riscos Residuais Documentais

| Risco | Severidade | Mitigação atual |
|-------|:----------:|-----------------|
| Doc 12 e 13 em `status: draft` — nenhuma aprovação formal registrada | Médio | Aprovação formal requerida antes de iniciar implementação (doc 17 §6) |
| Tabelas MVP P0 são descrições, não SQL executável | Baixo/Desejado | Intencionais — migrations ficam com o implementador, não na documentação |
| `runtime_observability` não no template enum | Baixo | Nota visível no doc 13; patch registrado como pendência §5.1 |
| `owner`/`responsible_agent` em display_name | Baixo | Deferred migration; não bloqueia runtime nem produto |
| Docs 14–16 ainda na versão anterior à coerência do Runtime | Alto | **Gate obrigatório:** docs 14–16 devem ser revisados à luz de 10–13 antes de implementação |

---

# 7. Gate de Entrada para Product System (14–16)

Antes de iniciar ou validar docs 14–16, verificar:

- [ ] **10 System Runtime Architecture** — v1.1.0 ✅ draft (requer aprovação formal)
- [ ] **11 Data Model and Persistence** — v1.1.1 ✅ draft (requer aprovação formal)
- [ ] **12 Security, Permissions and Data Governance** — v1.1.0 ✅ draft (requer aprovação formal)
- [ ] **13 Evals, Observability and Cost Control** — v1.1.0 ✅ draft (requer aprovação formal)
- [ ] Aprovações formais (Founder + Technical + Metacognik) registradas em `audit_logs`
- [ ] `QA_DOCUMENTATION_CHECKLIST.md` revisado e gate passado
- [ ] Docs 14–16 revisados à luz da §8.1 do Dependency Map (dependências de componentes de runtime)

---

# 8. Cronograma de Patches (resumo)

| Data | Doc | Patch | Trigger |
|------|-----|-------|---------|
| 2026-05-25 | 00_DOCUMENT_TEMPLATE | v2.1.0→2.2.0 | enum snake_case + runtime_data |
| 2026-05-25 | 00_TAXONOMY_AND_NAMING | v2.1.0→2.2.0 | §13.1 três formas de naming |
| 2026-05-25 | 00_MASTER_MAP | v2.1.0→2.2.0 | reviewers snake_case |
| 2026-05-25 | 00_DEPENDENCY_MAP | v2.1.0→2.2.0 | reviewers snake_case |
| 2026-05-25 | 10_SYSTEM_RUNTIME_ARCHITECTURE | YAML patch | reviewers/approval_required snake_case + Model Router note |
| 2026-05-25 | 11_DATA_MODEL_AND_PERSISTENCE | v1.1.0→1.1.1 | RBAC tables + capability_grants + secret_refs |
| 2026-05-25 | 12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE | CREATED v1.1.0 | full security spec |
| 2026-05-25 | 13_EVALS_OBSERVABILITY_AND_COST_CONTROL | CREATED v1.1.0 | full observability spec |
| 2026-05-25 | ARCHITECTURE_PATCH_REPORT | CREATED v1.0.0 | runtime coherence complete |
| 2026-05-25 | QA_DOCUMENTATION_CHECKLIST | CREATED v1.0.0 | runtime coherence complete |

---

# 9. Próximos Passos Recomendados

**Ordem sugerida pelo PMO_CKOS:**

1. **Aprovação formal dos 4 docs runtime** (Founder + Technical + Legal para doc 12; Founder + Technical + Metacognik para 10, 11, 13). Status deve mudar de `draft` → `approved`.

2. **Revisão docs 14–16** à luz de docs 10–13 (UI Projection Engine, State Machine Registry, Data Model como dependências). Ver `00_DEPENDENCY_MAP §8.1`.

3. **Patch `runtime_observability` no template** (§5.1 acima) antes de qualquer CI/lint automático.

4. **Migração global owner/responsible_agent** (§5.2 acima) — pode ser paralela à revisão de 14–16.

5. **Iniciar doc 17 (Implementation Protocol)** somente após approval formal de 10–13 e revisão de 14–16. Ver `00_DEPENDENCY_MAP §7`: `17_IMPLEMENTATION: → 10, 12, 13, 04`.

---

# 10. Aprovação Deste Relatório

| Papel | Status |
|-------|--------|
| PMO_CKOS | pendente |
| Metacognik | pendente |
| Founder | pendente |

> Este relatório é informativo e rastreável. Não requer aprovação para ser gerado, mas requer revisão antes de ser citado em decisões de implementação.

---

# 11. Post-Approval Gate — Patches P1–P4 Aplicados

**Data de aplicação:** 2026-05-25  
**Trigger:** Runtime Approval Gate retornou `APPROVED WITH REQUIRED PATCHES` — 4 patches documentais obrigatórios pré-implementação identificados.

## Status de cada patch

| # | Patch | Arquivo | Resultado |
|---|-------|---------|-----------|
| **P1** | Adicionar `audit_logs` com schema completo em seção dedicada | `11_DATA_MODEL_AND_PERSISTENCE.md` | ✅ APLICADO — §16.1 adicionado; Patch 1.1.2 registrado; versão → 1.1.2 |
| **P2** | Atualizar YAML `inputs`: `11 v1.1.0` → `11 v1.1.2` | `12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md` | ✅ APLICADO — YAML YAML `inputs` corrigido |
| **P3** | Remover textos `[PATCH SUGERIDO DOC 11 §4.1]` e `[PATCH SUGERIDO DOC 11 §12.1]` | `12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md §5.3, §5.11` | ✅ APLICADO — trocado por referência às seções existentes em doc 11 |
| **P4** | Corrigir referência `DOC 11 §4.2` → `DOC 11 §12.1` | `12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md §5.15` | ✅ APLICADO — referência de seção corrigida |

## Versões pós-patch

| Doc | Versão anterior | Versão atual |
|-----|:--------------:|:------------:|
| 11 Data Model and Persistence | 1.1.1 | **1.1.2** |
| 12 Security, Permissions and Data Governance | 1.1.0 | **1.1.0** (sem bump de versão — patches documentais em inputs e cross-refs, sem alteração de conteúdo de política) |

## Gate de Runtime — Status Atualizado

> **GATE STATUS: APPROVED FOR PRODUCT SYSTEM REVIEW** ✅  
>
> Todos os 4 patches obrigatórios foram aplicados. Os docs 10–13 estão documentalmente coerentes, sincronizados e com cross-references corretos. Um engenheiro pode derivar o schema completo de Supabase/Postgres a partir de doc 11 v1.1.2 + doc 12 v1.1.0 sem inventar arquitetura.
>
> **Autorizado:** revisão de docs 14–16 (Product System) como UI projection do Runtime.  
> **Ainda bloqueado:** implementação — aguarda aprovação formal Founder + Technical + Legal (doc 12) / Metacognik (docs 10, 11, 13).

---

# 12. Product/Business Architecture Gaps Before Product System

> Estas lacunas são **pendências oficiais** registradas antes da revisão dos docs 14–16.  
> Não resolver agora. Não criar tabelas, agentes ou implementações.  
> Objetivo: garantir que Product System não seja revisado sem considerar admin, cliente, custos, planos, créditos, suporte, feedback e ROI.

## 12.1 ROI Architecture

**Descrição:** O CKOS precisa ter uma arquitetura clara para medir e comunicar retorno sobre investimento em múltiplos níveis de granularidade.

**Escopo necessário:**
- ROI por projeto (custo total vs resultado gerado)
- ROI por workflow (custo de execução vs output aprovado)
- ROI por campanha (custo vs conversão/alcance)
- ROI por agente (custo vs qualidade + aprovação)
- ROI por node (utilidade vs redundância — via `node_performance`)
- ROI por artifact (custo de geração vs aproveitamento pelo cliente)
- Custo vs valor gerado (diferencial para cliente final)
- Indicadores de retorno para cliente, founder e admin (views diferenciadas)

**Dependências futuras:**
- `14_PROJECT_DASHBOARD_ARCHITECTURE.md` — dashboard de ROI por projeto/cliente
- `15_COMMAND_CENTER_ARCHITECTURE.md` — ROI como métrica de priorização no Command Center
- `13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md` — cost ledger + learning loop como base de cálculo
- `17_IMPLEMENTATION_PROTOCOL.md` — instrumentação de ROI desde a primeira feature

**Nota:** Base de dados já preparada em doc 11 §18 (cost_ledger) e §24 (learning tables), mas a camada de cálculo e apresentação de ROI não está modelada.

---

## 12.2 Feedback System

**Descrição:** O CKOS precisa registrar feedbacks explícitos (botão, formulário, comentário) e implícitos (retrabalho, reprovação, reabertura de node) como insumo para evals e learning loop.

**Escopo necessário:**
- Feedback de founder sobre outputs, decisões e workflows
- Feedback de cliente sobre propostas, artifacts e escopo
- Feedback de stakeholder sobre decisões e riscos
- Feedback sobre outputs de agente (aprovação/reprovação com contexto)
- Feedback sobre artifacts (qualidade, pertinência, uso)
- Feedback sobre workflows (eficiência, aderência ao objetivo)
- Feedback sobre propostas (aceite, rejeição, motivo)
- Feedback como sinal implícito: retrabalho, reabertura, override de agente
- Feedback como insumo direto para `eval_scores`, `decision_outcomes` e `learning_loop_engine`

**Dependências futuras:**
- `13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md` — feedback alimenta `decision_outcomes` e `prompt_performance`
- `14_PROJECT_DASHBOARD_ARCHITECTURE.md` — visualização de feedback por projeto/agente
- `15_COMMAND_CENTER_ARCHITECTURE.md` — feedback como sinal de priorização
- `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` — feedback é gatilho primário do ciclo de auto-evolução

**Nota:** As tabelas `eval_results` e `decision_outcomes` (doc 11) são base, mas falta modelar o mecanismo de coleta de feedback (tabela `feedback_entries`, eventos `FeedbackSubmitted`, `FeedbackImplicit`).

---

## 12.3 Support System

**Descrição:** O CKOS precisa prever suporte operacional para clientes, admins e erros de sistema — tanto como produto quanto como runtime.

**Escopo necessário:**
- Suporte para cliente: dúvidas sobre outputs, artifacts e propostas
- Suporte para admin: erros de configuração de workspace, billing, permissões
- Suporte para erros de agente: comportamento inesperado, output incorreto, loop
- Suporte para erros de cobrança: estouro de budget, cobrança inesperada
- Suporte para erros de execução: run failed, tool timeout, collector parcial
- Incident reporting: canal para reportar incidentes de segurança e qualidade
- Help center: base de conhecimento interna (skills, workflows, capabilities)
- Ticket interno: rastreamento de issues por projeto/workspace
- Handoff para humano: quando o agente escalona para operador humano
- Status de resolução: rastreabilidade de tickets abertos/resolvidos

**Dependências futuras:**
- `14_PROJECT_DASHBOARD_ARCHITECTURE.md` — dashboard de tickets abertos por projeto
- `15_COMMAND_CENTER_ARCHITECTURE.md` — suporte como fluxo no Command Center
- `17_IMPLEMENTATION_PROTOCOL.md` — instrumentação de suporte desde MVP

**Nota:** Modelo de dados de suporte (tabelas `support_tickets`, `ticket_events`, `incident_reports`) não está em doc 11. Deve ser adicionado antes de doc 17 ou como seção de doc 11 v2.x.

---

## 12.4 Credits, Plans and Billing

**Descrição:** O CKOS precisa de uma arquitetura de monetização e controle de consumo que suporte múltiplos modelos de negócio (SaaS, whitelabel, enterprise).

**Escopo necessário:**
- Planos com features e limites definidos (free, starter, professional, enterprise)
- Créditos por consumo (run, modelo, tool, collector, artifact) — cumulativos ou não cumulativos a definir
- Wallet por org/workspace com saldo, histórico e recarregamento
- Invoices: geração, linha de itens, tributação, emissão
- Billing events: toda ação que consome crédito ou gera cobrança emite evento
- Usage ledger: log append-only de consumo (paralelo ao cost_ledger de doc 11 §18, mas focado em billing)
- Upgrade/downgrade de plano com proratização e aprovação
- Approval para custos extras (consumo acima do plano)
- Limites por projeto e por cliente (whitelabel billing separado)
- Admin financeiro: visão consolidada de receita, consumo, inadimplência e projeção

**Dependências futuras:**
- `11_DATA_MODEL_AND_PERSISTENCE.md` — tabelas de billing (`billing_plans`, `org_wallets`, `billing_events`, `invoices`, `usage_ledger`) não existem ainda
- `13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md` — cost_ledger é base; billing_ledger é camada acima
- `14_PROJECT_DASHBOARD_ARCHITECTURE.md` — dashboard financeiro para admin e cliente
- `17_IMPLEMENTATION_PROTOCOL.md` — billing é dependência de MVP para operação comercial

**Nota:** Doc 11 §18 cobre custo interno de runtime (tokens, tools, collectors). Billing para cliente é uma camada separada e não está modelada. Risco: Product System ser revisado assumindo que cost_ledger = billing — são conceitos diferentes.

---

# 13. Manus Status Correction

**Data da decisão:** 2026-05-25  
**Origem:** Runtime Approval Gate — revisão de referências a ferramentas externas.

## 13.1 Decisão oficial

| Item | Status |
|------|--------|
| Manus como ferramenta de pesquisa temporária | ✅ CONFIRMADO |
| Manus como provider oficial do runtime CKOS | ❌ NÃO É |
| Manus como parte do produto final | ❌ NÃO É |
| Manus como infraestrutura permanente | ❌ NÃO É |
| Manus como fonte canônica de arquitetura | ❌ NÃO É |

## 13.2 Papel correto do Manus

Manus é uma **ferramenta externa de bootstrap** usada durante a fase inicial de pesquisa e desenvolvimento do CKOS para:
- Investigação de referências visuais, técnicas e de produto
- Curadoria de benchmarks e packs de implementação
- Geração de pacotes estruturados para insumo de Claude/Codex

**Escopo temporal:** fase de documentação e pré-implementação apenas.

## 13.3 Arquitetura de pesquisa no CKOS real

No CKOS maduro, pesquisa e coleta são tratadas por **capabilities e collectors** registrados:

| Fonte | Uso no CKOS |
|-------|-------------|
| OpenRouter / Perplexity | Web research e síntese de informação |
| Apify actors | Coleta estruturada de plataformas externas |
| PubMed / bases acadêmicas | Pesquisa científica e técnica |
| Bases públicas de mercado | Dados setoriais e regulatórios |
| APIs de plataformas | Google, Meta, LinkedIn, TikTok via collectorRegistry |
| Documentos internos do cliente | RAG privado do projeto (doc 11 §14) |
| Fontes verificadas por policy | Conforme memoryPolicyRegistry e capabilityRegistry |

## 13.4 Arquivos afetados

| Arquivo | Ação tomada |
|---------|-------------|
| `ARCHITECTURE_PATCH_REPORT.md` | Esta seção registra a correção oficial |
| `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md` | Nota de status adicionada ao topo do documento corpo |
| Documentos de Runtime (10–13) | Nenhuma referência a Manus encontrada — não afetados |

## 13.5 Nomenclatura canônica

| Termo anterior | Termo correto |
|---------------|---------------|
| "Manus research" | "temporary external research workflow (bootstrap phase)" |
| "CKOS Research via Manus" | "CKOS Research Capability" (arquitetura alvo — via collectors + RAG) |
| Manus como "Research Subagent do CKOS" | Ferramenta de bootstrap externa; não é subagent nativo |

> Renomeação de arquivos pendente de autorização explícita do Founder. Por ora, manter `18_RESEARCH_PROTOCOL_FOR_MANUS.md` com nota de status no corpo do documento.

---

# 14. Product System Review — Docs 15 e 16 Concluídos

**Data:** 2026-05-25  
**Trigger:** Gate de entrada §7 aprovado — Product System autorizado para revisão.

## 14.1 Documentos entregues

| Doc | Título | Versão anterior | Versão atual | Tipo de mudança |
|-----|--------|:--------------:|:------------:|-----------------|
| `15` | Command Center Architecture | 1.1.0 | **1.2.1** | Reescrita completa (1.2.0) + patch de Intent Taxonomy (1.2.1) |
| `16` | Node Canvas Architecture | 1.1.0 | **1.2.0** | Reescrita estrutural completa |

## 14.2 Doc 15 — Mudanças principais

**v1.1.0 → v1.2.0 (reescrita):**
- 7 modos definidos (Ask, Action, Approval, Explain, Support, Cost, Feedback)
- 16 slash commands com intent_type, eventos e permissões
- Nick como interface conversacional do CKOS (não chatbot genérico)
- 16 estados vivos mapeados a eventos do Runtime
- 7 ui_projections consumidas
- 6 eventos emitidos pelo Command Center
- 4 Business Gaps (§12.1–12.4) registrados
- Schema `command_history` proposto como patch para doc 11 v1.2.x
- MVP P0, edge cases, critérios de aprovação/reprovação

**v1.2.0 → v1.2.1 (patch — Intent Taxonomy):**
- Nova seção `§5.3 Intent Taxonomy` com 10 famílias de intenção
- Frase central: "Todo comando é um evento de intenção, não uma chamada direta de execução."
- Renumeração §5.3→§5.4, §5.4→§5.5, §5.5→§5.6
- Slash commands expandidos de 16 para 22 (cobrindo todas as 10 famílias)
- ROI/Cost reposicionado como família #8 de 10 (não o centro do Command Center)
- MVP P0 atualizado com /diagnosis, /workflow, /audit, /artifact

## 14.3 Doc 16 — Mudanças principais

**v1.1.0 → v1.2.0 (reescrita estrutural — 131 → ~700 linhas):**

| Seção | Conteúdo entregue |
|-------|-------------------|
| §1 Propósito | Lista completa de 15 capacidades do Canvas |
| §2 Função | Tabela de relação Canvas ↔ CC/Dashboard/Runtime/Data/Security/Evals |
| §3 Princípios | 14 princípios operacionais |
| §4 O que é um Node | Schema completo com 23 campos |
| §5 Node Types | 20 famílias com: quando aparece, quem cria, eventos, agents, projections, approvals |
| §6 Como Nodes são criados | §6.1 AI-created (fluxo completo) + §6.2 Manual (fluxo completo) |
| §7 Edges e Conexões | 14 tipos de edge + schema `node_edges` (patch sugerido para doc 11) |
| §8 Canvas Events | 16 eventos mapeados ao event bus de doc 10 |
| §9 State Machines | 3 máquinas: node (10 estados), workflow (9 estados), approval (6 estados) |
| §10 Relação com Agentes | Fluxo completo + 6 estados de agente visíveis no Canvas |
| §11 Relação com Workflows | 7 exemplos de cluster → workflow type |
| §12 Relação com Evidências | Side panel: evidências, confidence, gaps, contradições, Metacognik |
| §13 Relação com ROI/Custo | 9 tipos de informação + gap registrado |
| §14 Relação com Feedback/Support | 5 tipos de node + gaps registrados |
| §15 Permissões e Segurança | RBAC 5 roles + ABAC + tenant isolation + comportamento sem permissão |
| §16 Dependência de UI Projections | 7 projections com uso específico no Canvas |
| §17 UX Architecture | Descrição funcional completa (sem implementar) |
| §18 MVP P0 | O que entra vs. o que fica fora |
| §19 Edge Cases | 14 casos |
| §20 Product/Business Gaps | 6 gaps registrados |
| §21 Related Notes | 10 links cruzados |

## 14.4 Patches sugeridos para doc 11 v1.2.x

Os patches abaixo foram identificados durante a revisão dos docs 15 e 16. Estão **registrados como sugestões** — não aplicados. Requerem decisão de PMO_CKOS antes de aplicar.

| # | Tabela / seção | Origem | Urgência |
|---|----------------|--------|----------|
| P11-1 | `node_edges` — schema formal (source_node_id, target_node_id, edge_type, confidence, created_by, source_event_id, status, metadata) | Doc 16 §7 | Antes da implementação do Canvas |
| P11-2 | `command_history` — log append-only de comandos do usuário (mode, slash_command, intent_type, correlation_id, outcome) | Doc 15 §13 | MVP P0 Command Center |
| P11-3 | `feedback_entries` — tabela de feedback explícito e implícito | Doc 16 §14 | Feedback Mode MVP |
| P11-4 | `support_tickets` — tabela de tickets de suporte | Doc 16 §14 | Support Mode MVP |
| P11-5 | `roi_projection` — em §21 (ui_projections) para ROI Architecture | Doc 16 §13 | ROI Mode MVP |
| P11-6 | Confirmar campos em tabela `nodes`: `tenant_id` (RLS), `source_event_id`, `cost_estimate` jsonb | Doc 16 §4 | Antes da implementação do Canvas |

## 14.5 Frase central de cada doc — confirmação de posicionamento

> **Doc 15 — Command Center:**  
> "Todo comando é um evento de intenção, não uma chamada direta de execução."

> **Doc 16 — Node Canvas:**  
> "Node Canvas não é a fonte da verdade. Node Canvas é a superfície visual operacional para objetos, eventos, workflows, estados e aprovações do Runtime."

## 14.6 Princípio arquitetural reafirmado

Product System projeta e manipula objetos do Runtime. Product System **não cria lógica própria** fora do Runtime. Docs 15 e 16 foram escritos respeitando esta restrição — nenhum deles define engines, state machines, tabelas de domínio ou agentes como lógica própria do Product System.

## 14.7 Gate de implementação — status atualizado

| Doc | Status documentação | Gate de implementação |
|-----|--------------------|-----------------------|
| 14 Project Dashboard | v1.x (revisão pendente) | Aguarda revisão à luz de docs 10–13 |
| 15 Command Center | **v1.2.1 ✅** | Aguarda aprovação formal Founder + Metacognik |
| 16 Node Canvas | **v1.2.0 ✅** | Aguarda aprovação formal Founder + Metacognik + patches doc 11 |

> **Próximo passo recomendado:** revisar `14_PROJECT_DASHBOARD_ARCHITECTURE.md` para alinhar com docs 10–13 e com os princípios estabelecidos nos docs 15 e 16.

---

# 15. Product System — Doc 14 Concluído

**Data:** 2026-05-25  
**Trigger:** Docs 15 e 16 aprovados; doc 14 revisado na sequência.

## 15.1 Doc entregue

| Doc | Título | Versão anterior | Versão atual | Tipo de mudança |
|-----|--------|:--------------:|:------------:|-----------------|
| `14` | Project Dashboard Architecture | 1.1.0 | **1.2.0** | Reescrita estrutural completa |

## 15.2 Principais mudanças — v1.1.0 → v1.2.0

- 123 linhas → ~900 linhas; 16 seções → 33 seções.
- Tese central formalizada: "Project Dashboard is not a static analytics page. It is the executive projection of the project runtime state."
- Separação formal entre CKOS Home / Project Dashboard / Command Center / Node Canvas.
- 10 widgets obrigatórios (`fixed_required`) definidos com projeção base, permissão mínima e conteúdo.
- 7 tipos de widget (fixed_required, runtime_suggested, node_generated, user_pinned, admin_locked, plan_locked, experimental).
- Dashboard adaptativo: 4 perfis de projeto exemplo (branding, e-commerce, influencer, interno CKOS) — nenhum hardcoded como padrão.
- 9 tipos de ROI: financial, strategic, operational, brand, content, acquisition, retention, efficiency, learning.
- 8 presets de widget personalization com restrições MVP.
- CommandBar no Dashboard: 24 exemplos de intenção contextual; fluxo completo via intent_router.
- 4 views por perfil: Stakeholder, Client, Admin, Founder.
- 12 eventos emitidos pelo Dashboard (todos via Runtime — sem escrita direta).
- 3 state machines visíveis.
- RBAC: 8 roles com comportamento específico no Dashboard.
- MVP P0 vs. exclusões claramente separados.
- 20 edge cases cobertos.
- Visual direction registrada (sem implementação): bento grid, glassmorphism, cockpit cognitivo.

## 15.3 Novos patches sugeridos para doc 11 v1.2.x

| # | Tabela / seção | Urgência |
|---|---|---|
| P11-7 | `dashboard_preferences` — estado de layout por usuário/projeto (widget_configs, preset_selected, pinned_widgets) | Dashboard MVP |
| P11-8 | Confirmar `project_activity_feed` ou view derivada do event_bus para "recent events" feed | MVP P0 |

## 15.4 Novo patch sugerido para doc 10 v1.1.x

| # | Sugestão | Urgência |
|---|---|---|
| P10-1 | Especificar que `ui_projection_engine` expõe SSE para `project_pulse_projection` e `agent_activity_projection` — o Dashboard depende de streaming em tempo real para estes dois widgets | MVP P0 |

## 15.5 Product System — Status completo dos docs 14–16

| Doc | Título | Versão | Status documentação | Gate de implementação |
|-----|--------|:------:|--------------------|-----------------------|
| 14 | Project Dashboard Architecture | **v1.2.0** ✅ | draft | Aguarda aprovação formal Founder + Metacognik |
| 15 | Command Center Architecture | **v1.2.1** ✅ | draft | Aguarda aprovação formal Founder + Metacognik |
| 16 | Node Canvas Architecture | **v1.2.0** ✅ | draft | Aguarda aprovação formal Founder + Metacognik + patches doc 11 |

> **Product System (docs 14–16) documentalmente concluído.** Todos os 3 documentos foram reescritos e alinhados com Runtime (10–13). Patches sugeridos para doc 11 v1.2.x registrados (P11-1 a P11-8). Patch sugerido para doc 10 v1.1.x registrado (P10-1).
>
> **Próximo passo recomendado:** aprovação formal dos docs 14–16 (Founder + Metacognik) e aplicação dos patches P11-1 a P11-8 em doc 11 v1.2.x antes de iniciar doc 17 (Implementation Protocol).

---

# 16. Runtime/Data Model Patches Aplicados — Product System Support

**Data de aplicação:** 2026-05-25  
**Trigger:** Product System docs 14–16 aprovados para review; patches P11-1 a P11-8 e P10-1 identificados como obrigatórios antes da implementação.

## 16.1 Patches aplicados

| Patch | Doc | Status | Resultado |
|---|---|---|---|
| **P11-1** | `11_DATA_MODEL_AND_PERSISTENCE.md` | ✅ APLICADO | `node_edges` schema completo (14 edge types, 23 campos); `nodes` + `source_event_id` + `cost_estimate` |
| **P11-2** | `11_DATA_MODEL_AND_PERSISTENCE.md` | ✅ APLICADO | §30 ROI System Data Model — 7 tabelas: `roi_models, roi_metrics, roi_snapshots, roi_hypotheses, roi_evidence_links, roi_assumptions, roi_outcomes` |
| **P11-3** | `11_DATA_MODEL_AND_PERSISTENCE.md` | ✅ APLICADO | §31 Feedback System Data Model — 7 tabelas: `feedback_items, feedback_threads, feedback_sources, feedback_decisions, feedback_node_links, feedback_artifact_links, feedback_status_transitions` |
| **P11-4** | `11_DATA_MODEL_AND_PERSISTENCE.md` | ✅ APLICADO | §32 Support System Data Model — 7 tabelas: `support_tickets, support_ticket_events, support_categories, support_sla_policies, support_agent_links, support_resolution_notes, friction_signals` |
| **P11-5** | `11_DATA_MODEL_AND_PERSISTENCE.md` | ✅ APLICADO | §33 Credits/Plans/Billing Data Model — 11 tabelas: `plans, plan_features, subscriptions, credit_wallets, credit_transactions, credit_reservations, usage_events, billing_events, invoice_records, plan_limits, quota_policies` |
| **P11-6** | `11_DATA_MODEL_AND_PERSISTENCE.md` | ✅ APLICADO | §21 expandido: 7 → 13 projeções tipadas com source tables, update triggers, cache strategy, tenant scope, permission filtering |
| **P11-7** | `11_DATA_MODEL_AND_PERSISTENCE.md` | ✅ APLICADO | §34 `dashboard_preferences` — personalização de layout por usuário/projeto |
| **P11-8** | `11_DATA_MODEL_AND_PERSISTENCE.md` | ✅ APLICADO | §35 `project_activity_feed` — feed append-only de atividades do projeto |
| **P10-1** | `10_SYSTEM_RUNTIME_ARCHITECTURE.md` | ✅ APLICADO | §5.12.1 Live Projection Streaming — SSE para 7 projeções críticas, polling para 6 projeções periódicas; 6 estados de projeção; 6 regras obrigatórias do projection engine |

## 16.2 Versões pós-patch

| Doc | Versão anterior | Versão atual |
|-----|:--------------:|:------------:|
| 11 Data Model and Persistence | 1.1.2 | **1.2.0** |
| 10 System Runtime Architecture | 1.1.0 | **1.1.1** |
| ARCHITECTURE_PATCH_REPORT | 1.1.0 | **1.2.0** |

## 16.3 Critério de qualidade verificado

> Um engenheiro pode escrever migrations do Supabase/Postgres para suportar Project Dashboard (doc 14), Command Center (doc 15) e Node Canvas (doc 16) **sem inventar arquitetura nova**:
> - Nodes e edges: §10 + §21 (node_health_projection, canvas_graph_projection)
> - Dashboard widgets: §21 (13 projeções) + §34 (dashboard_preferences) + §35 (project_activity_feed)
> - ROI: §30 (roi_models, roi_snapshots) + §21 (roi_snapshot_projection)
> - Feedback: §31 (feedback_items, feedback_decisions) + §21 (feedback_loop_projection)
> - Suporte: §32 (support_tickets, friction_signals) + §21 (support_friction_projection)
> - Créditos/Billing: §33 (credit_wallets, credit_transactions, plans) + §21 (cost_credit_projection)
> - Streaming: doc 10 §5.12.1 (7 SSE + 6 polling; 6 regras do engine)

## 16.4 Dependências não resolvidas (requerem docs dedicados antes de implementação)

| Sistema | Tabelas adicionadas | Status | Bloqueio |
|---|---|---|---|
| ROI Architecture | §30 (roi_models, etc.) | Schema base ✅; lógica de cálculo ❌ | Aguarda doc de ROI Architecture |
| Feedback System | §31 (feedback_items, etc.) | Schema base ✅; fluxos completos ❌ | Aguarda doc de Feedback System |
| Support System | §32 (support_tickets, etc.) | Schema base ✅; SLAs/escalamentos completos ❌ | Aguarda doc de Support System |
| Billing/Credits | §33 (plans, wallets, etc.) | Schema base ✅; integração payment gateway ❌ | Aguarda doc de Credits/Billing Architecture |

## 16.5 Gate de implementação — status final do Product System

| Doc | Status documentação | Gate de implementação |
|-----|--------------------|-----------------------|
| 10 Runtime Architecture | **v1.1.1 ✅** | Aguarda aprovação formal Founder + Technical + Metacognik |
| 11 Data Model | **v1.2.0 ✅** | Aguarda aprovação formal Founder + Technical + Metacognik |
| 12 Security | v1.1.0 ✅ | Aguarda aprovação formal Founder + Technical + Legal |
| 13 Evals | v1.1.0 ✅ | Aguarda aprovação formal Founder + Technical + Metacognik |
| 14 Project Dashboard | v1.2.0 ✅ | Aguarda aprovação formal Founder + Metacognik |
| 15 Command Center | v1.2.1 ✅ | Aguarda aprovação formal Founder + Metacognik |
| 16 Node Canvas | v1.2.0 ✅ | Aguarda aprovação formal Founder + Metacognik |

> **GATE STATUS: DOC 17 CONCLUÍDO — PRONTO PARA APROVAÇÃO FORMAL** ✅  
>
> Todos os patches documentais de coerência foram aplicados. Os docs 10–17 estão sincronizados e mutuamente referenciáveis. Um engenheiro pode derivar o schema completo de Supabase/Postgres a partir de doc 11 v1.2.0 + doc 12 v1.1.0 sem inventar arquitetura. O protocolo de implementação (doc 17 v1.2.0) define a ordem canônica, gates A–J, regras de engenharia e MVP P0.
>
> **Autorizado:** início da aprovação formal dos docs 10–17.  
> **Ainda bloqueado:** implementação — aguarda aprovação formal pelos papéis definidos na tabela acima + Gate A (Documentation Gate) conforme doc 17 §20.
>
> **Alertas críticos antes de implementação:**
> 1. ROI, Feedback, Support e Billing: schemas base estão em doc 11, mas os **sistemas completos** precisam de documentação arquitetural dedicada antes de qualquer implementação de produto.
> 2. SSE connections (doc 10 §5.12.1) exigem token efêmero por projeto (doc 12 §5.6) — implementar junto, não separado.
> 3. `credit_reservations` deve ser implementado junto com `credit_wallets` — operações de consumo sem reserva prévia podem causar saldo negativo em condições de concorrência.
> 4. `node_edges.archived_at` (soft-delete) — a lógica de "invalidar edge" nunca faz DELETE; sempre usa `status=invalidated` + `archived_at`.
> 5. `dashboard_preferences.hidden_widgets` não pode incluir `fixed_required` — validar na camada de aplicação E no `policy_engine`.

---

# 17. Implementation System — Doc 17 Concluído

**Data de aplicação:** 2026-05-25  
**Trigger:** Docs 10–16 sincronizados e aprovados para review; doc 17 v1.1.0 (16 seções, 164 linhas) insuficiente para documentação engineer-ready de protocolo de implementação completo.

## 17.1 Reescrita aplicada

| Doc | Versão anterior | Versão nova | Tipo |
|-----|:--------------:|:-----------:|------|
| `17_IMPLEMENTATION_PROTOCOL.md` | 1.1.0 (16 seções) | **1.2.0 (34 seções)** | Reescrita estrutural completa |

## 17.2 O que foi adicionado

| Seção | Conteúdo |
|-------|----------|
| §1–§3 | Propósito, O que é, O que NÃO é — delimitação clara do protocolo |
| §4 | 13 princípios de implementação não-negociáveis derivados de docs 10–16 |
| §5 | Tabela de relação com toda a documentação CKOS (10–16) + tabela de gaps bloqueantes |
| §6 | Ordem canônica de implementação (Fases 0–12) com paralelismo permitido documentado |
| §7–§19 | Fases 0–12 individualmente: objetivo, entradas, componentes, rollback, gate de saída |
| §20 | Gates A–J: critérios completos por gate, verificador por gate |
| §21 | MVP P0: tabelas P0, intents P0, widgets P0, node types P0, agentes P0, 5 user paths P0 |
| §22 | Explicitamente fora do P0: 12 domínios bloqueados com doc necessário antes de implementar |
| §23 | 13 regras de engenharia (R1–R13) derivadas dos docs 10–16 |
| §24 | 20 modos de falha catalogados com sintoma e mitigação |
| §25 | Rollback e simulação por camada (schema, events, projections, agent run, feature flag, release) |
| §26–§28 | Checkpoints separados: Fundador, Técnico, Metacognik — quando obrigatório + formato |
| §29 | Roadmap de 7 ondas com duração estimada, paralelismo e dependências entre ondas |
| §30 | 9 documentos futuros obrigatórios (docs 22–30) com urgência e dependências |
| §31 | Agentes, squads e skills do protocolo |
| §32 | 8 métricas de sucesso mensuráveis |
| §33 | 22 edge cases com comportamento esperado |
| §34 | Related notes completas |

## 17.3 Posicionamento de Manus (formalizado)

Manus está explicitamente documentado na Fase 5 (§12) como **ferramenta externa temporária de bootstrap de pesquisa** — não é infraestrutura CKOS, não é agente registrado no `agent_registry` de produção. O roadmap de substituição está documentado: Perplexity/OpenRouter (LLM search), Apify (web crawl), PubMed connectors (domain research), RAG privado (base interna), collectors especializados por vertical.

## 17.4 Documentos futuros registrados (sequência canônica corrigida em v1.2.1)

**Docs 18–20 — já existem (baseline de implementação):**

| Doc # | Título | Status |
|-------|--------|--------|
| 18 | `18_RESEARCH_PROTOCOL.md` | ✅ Existe |
| 19 | `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md` | ✅ Existe |
| 20 | `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md` | ✅ Existe |

**Business Systems (docs 21–24) — obrigatórios antes de implementação de domínio:**

| Doc # | Título | Urgência | Bloqueia |
|-------|--------|----------|---------|
| 21 | `21_ROI_ARCHITECTURE.md` | Alta | `/roi` command completo, ROI widget, ROI nodes |
| 22 | `22_FEEDBACK_SYSTEM_ARCHITECTURE.md` | Alta | Feedback Loop widget, Feedback nodes |
| 23 | `23_SUPPORT_SYSTEM_ARCHITECTURE.md` | Média | Support & Friction widget, Support nodes |
| 24 | `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md` | Alta | `/credits` command, billing nodes, quota |

**Sistemas complementares (docs 25–29):**

| Doc # | Título | Urgência | Bloqueia |
|-------|--------|----------|---------|
| 25 | `25_WHITELABEL_SYSTEM.md` | Média | Multi-brand features de docs 14–16 |
| 26 | `26_COLLECTOR_REGISTRY.md` | Média | Node type Collector, pesquisa especializada |
| 27 | `27_AGENT_MARKETPLACE.md` | Baixa | Fase 12+ |
| 28 | `28_NOTIFICATION_SYSTEM.md` | Média | Approval notifications completas |
| 29 | `29_EXTERNAL_API.md` | Baixa | Pós-launch |

## 17.5 Micro-patch de governança aplicado (v1.2.1)

**Data:** 2026-05-25  
**Trigger:** Aprovação do doc 17 v1.2.0 com micro-patch obrigatório de governança.

| Correção | Localização | Detalhe |
|----------|-------------|---------|
| Sequência documental | Doc 17 §30 + §22 + §24 + §29 + YAML | Docs 18/19/20 reconhecidos como existentes; Business Systems renumerados 21–24 |
| Nome canônico doc 19 | Doc 17 YAML + §34 | `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md` |
| Linguagem de gate | Doc 17 §7 + §20 | "Saída esperada" — aprovação formal exigida, não automática |
| Gate A | Doc 17 §20 | "O Gate A pode ser submetido para aprovação formal. A implementação continua bloqueada até aprovação registrada." |
| Gate status | ARCHITECTURE_PATCH_REPORT §17.5 | Linguagem corrigida: "pronto para revisão do Gate A", não "sistema documental completo" |

## 17.6 Gate de implementação — status final do Implementation System

| Doc | Status | Gate |
|-----|--------|------|
| 17 Implementation Protocol | **v1.2.1 ✅** | Aguarda aprovação formal Founder + Technical + Metacognik |

> **A base Runtime + Product + Implementation Protocol está pronta para revisão do Gate A.**
>
> Docs 10–17 existem, estão versionados e são mutuamente referenciáveis. O sistema documental completo ainda não está fechado — faltam docs 18/19/20 (revisão/expansão) e os Business Systems 21–24.
>
> O Gate A **pode ser submetido para aprovação formal**. A implementação **continua bloqueada** até aprovação registrada por Founder + Technical + Metacognik.
>
> **Próximo documento:** `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md` — revisão e expansão.  
> **Próximo passo documentacional de Business Systems:** Escrever docs 21–24 (ROI, Feedback, Support, Billing) durante as Ondas 3–4 para não bloquear a Onda 6.

---

# 18. Implementation System — Doc 18 Concluído

**Data:** 2026-05-25  
**Trigger:** Doc 17 v1.2.1 aprovado com sequência canônica corrigida. `18_RESEARCH_PROTOCOL_FOR_MANUS.md` v1.1.0 supersedido — scope restrito a Manus era insuficiente para a Research Capability definitiva do CKOS.

## 18.1 Documento criado

| Arquivo | Versão anterior | Versão nova | Tipo |
|---------|:--------------:|:-----------:|------|
| `18_RESEARCH_PROTOCOL_FOR_MANUS.md` | 1.1.0 (16 seções) | **supersedido** | — |
| `18_RESEARCH_PROTOCOL.md` | (novo) | **1.0.0 (28 seções)** | Criação — reescrita de scope |

## 18.2 Reposicionamento de Manus (§4)

| Aspecto | Antes (doc supersedido) | Agora (doc 18 v1.0.0) |
|---------|------------------------|----------------------|
| Papel | Agente de pesquisa operacional | Ferramenta externa temporária de bootstrap |
| Infra CKOS | Implícito como componente | Explicitamente não é infra CKOS |
| Runtime | Mencionado como integração | Não aparece no event bus nem em projections |
| Substituto | Self-evolving (futuro vago) | Roadmap concreto: Perplexity/OpenRouter + Apify + PubMed + RAG privado |
| Doc futuro | Referência vaga | `26_COLLECTOR_REGISTRY.md` como doc formal de substitutos |

## 18.3 Research Capability definida

**18 componentes do pipeline** (§5): `research_intent_router`, `research_policy_engine`, `source_selector`, `collector_runner`, `web_research_runner`, `academic_research_runner`, `rag_retriever`, `document_parser`, `source_normalizer`, `evidence_extractor`, `source_reliability_scorer`, `confidence_scorer`, `contradiction_detector`, `gap_detector`, `synthesis_generator`, `metacognik_reviewer`, `evidence_store`, `research_projection_engine`

**Source Reliability Framework** (§8): Tier 1–5 com critérios de uso, peso na síntese e risco de viés.

**Evidence Object Model** (§9): schema SQL completo de `evidence_items` + tabela auxiliar `research_runs` com 13 estados de state machine.

**20 Research Events** (§24) conectados ao event bus de doc 10.

## 18.4 Patches sugeridos para outros docs (não aplicados)

| Patch | Doc alvo | Descrição | Urgência |
|-------|----------|-----------|----------|
| **P18-1** | Doc 11 | Tabela `research_runs` com schema completo | Antes de Research Pipeline |
| **P18-2** | Doc 11 | Tabela `evidence_items` com schema completo (§9.1 do doc 18) | Antes de Research Pipeline |
| **P18-3** | Doc 11 | Tabela `hypotheses` como entidade formal | Antes de Evidence Object Model |
| **P18-4** | Doc 11 | Expandir `risk_gap_evidence_projection` com campos de research | Antes de Dashboard widget #10 |
| **P18-5** | Doc 10 | `research_intent_router` como sub-rota nomeada no fluxo canônico §5.2 | Antes de Research Pipeline |
| **P18-6** | Doc 26 (futuro) | Schema de `collectors_allowlist`: collector_id, rate_limit, pii_risk_level, authorization_level | Antes de qualquer Apify em produção |

## 18.5 Gate de implementação

| Doc | Status | Gate |
|-----|--------|------|
| 18 Research Protocol | **v1.0.0 ✅** | Aguarda aprovação formal Founder + Technical + Metacognik |

> **Próximo documento:** `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md` — revisão e expansão do protocolo de QA e aprovação do Founder.
>
> **Patches P18-1 a P18-5** devem ser aplicados ao doc 11 e doc 10 antes da implementação do Research Pipeline (Fase 6 do doc 17).

---

# 19. Implementation System — Doc 19 Concluído

**Data:** 2026-05-25
**Trigger:** Doc 18 v1.0.0 aprovado. `19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md` v1.1.0 supersedido — escopo restrito (16 seções, sem templates, sem tool matrix, sem anti-entropy rules) era insuficiente para governança completa de desenvolvimento assistido por IA.

## 19.1 Documento criado

| Arquivo | Versão anterior | Versão nova | Tipo |
|---------|:--------------:|:-----------:|------|
| `19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md` | 1.1.0 (16 seções) | **supersedido** | — |
| `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md` | (novo) | **1.0.0 (30 seções)** | Criação — reescrita de scope |

## 19.2 Principais decisões travadas

| Decisão | Localização |
|---------|-------------|
| Tese central: "CKOS deve ser tool-assisted, não tool-dependent" | §3 Princípio central |
| AI output é o item de menor autoridade na hierarquia de verdade | §6 Source of Truth Hierarchy (7 níveis) |
| Antigravity formalizado com perfil, limites e template próprios | §4.3 + §10 |
| Tool Selection Matrix com 20+ tipos de tarefa e aprovação mínima por tipo | §5 |
| 10 Allowed Execution Modes com permissão, risco e aprovação | §11 |
| 20 Forbidden Actions explícitas e rastreáveis | §12 |
| Patch Governance: P0–P4 com aprovador por nível | §13 |
| 10 Anti-Entropy Rules para evitar degradação progressiva | §19 |
| Gates A–J do doc 17 mapeados a aprovações específicas de AI tools | §29 |
| Nenhuma ferramenta de IA pode declarar gate como aprovado — humanos aprovam | §29 nota final |

## 19.3 Diferenciação de ferramentas

| Ferramenta | Uso principal | Limite crítico |
|------------|--------------|----------------|
| **Claude Code** | Arquitetura, revisão, planejamento, contexto extenso | Pode superproduzir; não decide produto |
| **Codex** | Implementação focada, testes, migrations, bugs isolados | Precisa de contexto limpo; não cria módulos grandes sem plano |
| **Antigravity** | Protótipos visuais, UI exploration, theming | Não é source-of-truth; nunca cria backend sensível |
| **Ferramentas futuras** | A definir | Devem ser registradas em `tool_usage_policy` antes de uso |

## 19.4 Como o protocolo impede entropia

| Mecanismo | Seção |
|-----------|-------|
| Scope contract antes de executar | §7 Execution Handoff Format |
| Templates padronizados com proibições explícitas | §8–§10 |
| 10 Allowed Modes — misturar modos é proibido | §11 |
| 20 Forbidden Actions com registro de incidente | §12 |
| 10 Anti-Entropy Rules | §19 |
| Documentation Sync Rules com `ARCHITECTURE_QUESTION` formal | §20 |
| QA Report Format obrigatório antes de merge | §26 |
| Gates A–J com aprovação humana obrigatória | §29 |

## 19.5 Gate de implementação

| Doc | Status | Gate |
|-----|--------|------|
| 19 Claude/Codex/Antigravity Execution Protocol | **v1.0.0 ✅** | Aguarda aprovação formal Founder + Technical + Metacognik |

> **Próximo documento:** `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md` — reescrita completa do protocolo de QA e aprovação do Founder (v1.1.0 → v1.2.0).

---

# 20. Implementation System — Doc 20 Concluído

**Data:** 2026-05-25  
**Trigger:** Docs 17, 18, 19 v1.x aprovados para review. `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md` v1.1.0 (16 seções, 130 linhas) era superficial — sem gate system, sem decision rights matrix, sem domain checklists, sem veto protocol, sem state machine, sem rollback formal. Reescrita completa requerida.

## 20.1 Documento reescrito

| Arquivo | Versão anterior | Versão nova | Tipo |
|---------|:--------------:|:-----------:|------|
| `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md` | 1.1.0 (16 seções, 130 linhas) | **1.2.0 (34 seções, ~1000 linhas)** | Reescrita estrutural completa |

## 20.2 O que foi adicionado

| Seção | Conteúdo entregue |
|-------|-------------------|
| §1–§3 | Propósito, O que é / não é QA, Princípio Central |
| §4 | 12 princípios de filosofia de QA |
| §5 | 5 atores de aprovação com veto power, SLA, ausência e auto-approve scope |
| §6 | Decision Rights Matrix (16 tipos de decisão × atores × veto power) |
| §7 | Gate System A–K (11 gates) — cada gate com critérios, verifiers, aprovação, unblocks, rollback |
| §8–§23 | 14 domain-specific QA checklists: Documentation, Architecture, Data Model, Security, Runtime, Command Center, Dashboard, Node Canvas, Agent, Research, Cost, ROI, Feedback, Support, UI/UX, AI Tool Output |
| §24 | Release Readiness Checklist (5 dimensões: gates, operacional, aprovações, issues, documentação) |
| §25 | Rejection Criteria: 10 automáticas (bloqueio imediato) + 10 formais (com registro) |
| §26 | Founder Approval Protocol: o que requer, formato obrigatório, SLA por prioridade, ausência |
| §27 | Metacognik Veto Protocol: 9 condições de veto, formato, escalação, override com risk statement |
| §28 | Technical Approval Protocol: scope, processo de 7 etapas, formato de revisão |
| §29 | QA Report Format — template obrigatório com submission ID, gate, domain, checklist, routing |
| §30 | State Machine de Aprovações: 10 estados + 12 transições + regras de stale/emergency |
| §31 | MVP P0 QA Scope — o que entra e o que fica fora de P0 |
| §32 | 27 Edge Cases detalhados |
| §33 | 9 documentos futuros requeridos + 4 patches sugeridos para docs 10/11 |
| §34 | Related Notes |

## 20.3 Gates A–K — Resumo

| Gate | Nome | Aprovação mínima | Desbloqueia |
|------|------|:-----------------:|-------------|
| A | Documentation | Founder + Technical + Metacognik | Gate B |
| B | Data Model | Technical + Metacognik | Gate C |
| C | Runtime Core | Technical + Metacognik | Gate D |
| D | Security | Founder + Technical + Metacognik | Gate E |
| E | Projection | Technical | Gate F |
| F | Product Surface | Founder + Technical | Gate G |
| G | Agent Runtime | Founder + Technical + Metacognik | Gate H |
| H | External Tools | Technical (Founder para novos providers) | Gate I |
| I | Business Systems | Founder + Technical | Gate J |
| J | Self-Evolving | Founder + Metacognik | Gate K |
| K | Release | Founder + Technical + Metacognik | Produção |

## 20.4 Patches sugeridos para outros docs (não aplicados)

| Patch | Doc alvo | Descrição | Urgência |
|-------|----------|-----------|----------|
| **P20-1** | Doc 11 | Tabelas `approval_submissions` + `approval_decisions` (state machine §30) | Antes de Gate B |
| **P20-2** | Doc 11 | QA Report como artifact type no artifact registry | Antes de Gate F |
| **P20-3** | Doc 10 | Evento `MetacognikVetoEmitted` no event catalog | Antes de Gate C |
| **P20-4** | Doc 11 | Tabela `release_readiness_checks` para rastrear §24 | Antes de Gate B |

> Os patches acima são sugeridos e registrados. Não aplicar sem aprovação Technical + PMO_CKOS e versão incremental nos docs afetados.

## 20.5 Tese central do Doc 20

> **"CKOS cannot ship by confidence alone. Every document, migration, runtime module, UI surface, agent action, and business system must pass explicit QA, approval, and rollback criteria before becoming canonical."**

## 20.6 Gate de implementação — status final dos docs 17–20

| Doc | Título | Versão | Status documentação | Gate |
|-----|--------|:------:|--------------------|------|
| 17 | Implementation Protocol | **v1.2.1 ✅** | draft | Aguarda aprovação formal Founder + Technical + Metacognik |
| 18 | Research Protocol | **v1.0.0 ✅** | draft | Aguarda aprovação formal Founder + Technical + Metacognik |
| 19 | Claude/Codex/Antigravity Execution Protocol | **v1.0.0 ✅** | draft | Aguarda aprovação formal Founder + Technical + Metacognik |
| 20 | QA and Founder Approval Protocol | **v1.2.0 ✅** | draft | Aguarda aprovação formal Founder + Technical + Metacognik |

> **BASELINE IMPLEMENTATION SYSTEM (17–20) DOCUMENTALMENTE CONCLUÍDO.**
>
> Os 4 documentos do Implementation System existem, estão versionados, são mutuamente referenciáveis e cobrem o protocolo completo de: como implementar (17), como pesquisar com evidência (18), como usar ferramentas de AI sem entropia (19), e como fazer QA e aprovação de qualquer entrega (20).
>
> **O Gate A pode ser submetido para aprovação formal.** A implementação continua bloqueada até aprovação registrada por Founder + Technical + Metacognik.
>
> **Próximo passo documentacional obrigatório:** Escrever docs 21–24 (Business Systems: ROI, Feedback, Support, Credits/Plans/Billing) durante as Ondas 3–4 do roadmap de doc 17 §29 para não bloquear a Onda 6 (Business Operating System).
>
> **Patches P20-1 a P20-4** devem ser avaliados junto com os patches P18-1 a P18-6 e aplicados ao doc 11 v1.3.x antes da implementação das funcionalidades de QA e Research.

---

# 21. Business Systems — Doc 21 Concluído

**Data:** 2026-05-25  
**Trigger:** Baseline Implementation System (17–20) documentalmente concluído. Doc 21 é o primeiro documento do `06_BUSINESS_SYSTEMS/` — novo diretório criado neste registro.

## 21.1 Documento criado

| Arquivo | Diretório | Versão | Tipo |
|---------|-----------|:------:|------|
| `21_ROI_ARCHITECTURE.md` | `06_BUSINESS_SYSTEMS/` (NOVO) | **1.0.0 (28 seções)** | Criação |

## 21.2 Tese central

> **"ROI in CKOS is not a static financial metric. It is a governed value intelligence system that connects costs, evidence, hypotheses, decisions, outcomes and confidence across financial, strategic, operational, brand, content, acquisition, retention, efficiency and learning dimensions."**

## 21.3 O que foi definido

| Seção | Conteúdo entregue |
|-------|-------------------|
| §1–§4 | Propósito, O que é/não é, Princípio Central, 12 princípios de filosofia de ROI |
| §5 | 12 ROI Types completos (financial, strategic, operational, brand, content, acquisition, retention, efficiency, learning, risk_reduction, decision_quality, time_to_decision) — cada um com definição, quando usar, inputs, outputs, evidências, riscos, limitações e exemplo prático |
| §6 | 11 objetos do ROI Object Model com schemas SQL completos (roi_model, roi_metric, roi_snapshot, roi_hypothesis, roi_assumption, roi_evidence_link, roi_outcome, roi_gap, roi_risk, roi_projection [read-only], roi_decision_link) |
| §7 | 14 ROI Data Sources conectados ao runtime CKOS |
| §8 | 11 ROI Calculation Layers (raw_cost → confidence_adjusted_roi) com fórmulas e regras de display |
| §9 | ROI Confidence Framework: 5 níveis (high/medium/low/speculative/insufficient_data) com critérios, display rules, bloqueios e triggers Metacognik |
| §10 | ROI Assumptions: campos obrigatórios + 6 regras de gestão |
| §11 | 11 ROI Evidence Rules governando como evidência sustenta ou não claims de ROI |
| §12 | Conexão ROI ↔ Cost Ledger: 5 fontes de custo + 5 cost guard rules |
| §13 | ROI ↔ Dashboard: ROI Snapshot Widget com especificação completa do que exibe/nunca exibe |
| §14 | ROI ↔ Command Center: 10 intenções ROI com intent_type e eventos emitidos |
| §15 | ROI ↔ Node Canvas: 7 node types + 8 edge types de ROI |
| §16 | ROI ↔ Propostas: 8 regras de uso + template de seção ROI em proposta |
| §17–§19 | ROI ↔ Feedback, Support, Research |
| §20 | ROI ↔ Evals: 8 eval targets com thresholds |
| §21 | ROI State Machine: 11 estados + 13 transições |
| §22 | 16 ROI Events conectados ao event bus de doc 10 |
| §23 | ROI Permissions: matriz por dado × role + aprovação por tipo + RLS obrigatório |
| §24 | ROI QA: 10-item checklist + 4 critérios de rejeição automática |
| §25 | MVP P0: o que entra (3 roi_types, widget, 3 intents, roi_node) e o que fica fora |
| §26 | 22 Failure Modes com sintoma e mitigação |
| §27 | 6 patches sugeridos (P21-1 a P21-6) — não aplicados |
| §28 | Related Notes |

## 21.4 ROI Types registrados

| # | roi_type | Dimensão principal |
|---|---|---|
| 1 | `financial_roi` | Retorno monetário direto |
| 2 | `strategic_roi` | Posicionamento e capacidade |
| 3 | `operational_roi` | Eficiência de processo |
| 4 | `brand_roi` | Consistência e percepção de marca |
| 5 | `content_roi` | Produtividade de conteúdo |
| 6 | `acquisition_roi` | Conversão e CAC |
| 7 | `retention_roi` | Churn e LTV |
| 8 | `efficiency_roi` | Utilização de recursos |
| 9 | `learning_roi` | Crescimento de capacidade sistêmica |
| 10 | `risk_reduction_roi` | Custo evitado de riscos |
| 11 | `decision_quality_roi` | Qualidade e velocidade de decisão |
| 12 | `time_to_decision_roi` | Vantagem de velocidade decisória |

## 21.5 Patches sugeridos (não aplicados)

| Patch | Doc alvo | Descrição | Urgência |
|-------|----------|-----------|----------|
| **P21-1** | Doc 11 v1.3.x | Tabela `roi_gaps` — schema completo | Antes de Gate I |
| **P21-2** | Doc 11 v1.3.x | Tabela `roi_risks` — schema completo | Antes de Gate I |
| **P21-3** | Doc 11 v1.3.x | Tabela `roi_decision_links` — schema completo | Antes de Gate J |
| **P21-4** | Doc 10 v1.2.x | `roi_projection_engine` como componente nomeado do runtime | Antes de Gate I |
| **P21-5** | Doc 11 v1.3.x | Verificar e formalizar `roi_snapshot_projection` em §21 (trend_direction, metacognik_warnings, expired_assumption_count) | Antes de Gate F |
| **P21-6** | Doc 13 v1.2.x | Adicionar `roi_reasoning_quality`, `evidence_coverage`, `confidence_accuracy`, `outcome_tracking_rate` como eval targets formais em §4 | Antes de Gate G |

## 21.6 Gate de Business Systems — status atual

| Doc | Título | Versão | Status |
|-----|--------|:------:|--------|
| 21 | ROI Architecture | **v1.0.0 ✅** | draft — aguarda aprovação Founder + Technical + Metacognik |
| 22 | Feedback System Architecture | — | Não existe ainda |
| 23 | Support System Architecture | — | Não existe ainda |
| 24 | Credits, Plans and Billing Architecture | — | Não existe ainda |

> **Próximo passo:** `22_FEEDBACK_SYSTEM_ARCHITECTURE.md` — primeiro doc do Business Systems após ROI.
>
> **Gate I** requer docs 21–24 presentes e em status draft-aprovado antes de avançar.

---

# 22. Business Systems — Doc 22 Concluído

**Data:** 2026-05-25  
**Trigger:** Doc 21 (ROI Architecture) v1.0.0 criado e registrado. `22_FEEDBACK_SYSTEM_ARCHITECTURE.md` é o segundo documento do `06_BUSINESS_SYSTEMS/` — obrigatório para Gate I.

## 22.1 Documento criado

| Arquivo | Diretório | Versão | Tipo |
|---------|-----------|:------:|------|
| `22_FEEDBACK_SYSTEM_ARCHITECTURE.md` | `06_BUSINESS_SYSTEMS/` | **1.0.0 (29 seções)** | Criação |

## 22.2 Tese central

> **"Feedback in CKOS is not a comment system. It is a governed learning loop that captures signals, classifies them, routes them to owners, generates decisions, and closes the loop with traceable outcomes — or explicitly explains why it did not."**

## 22.3 Princípio central

> **"No feedback should disappear without classification, ownership, decision or explicit dismissal reason."**

## 22.4 O que foi definido

| Seção | Conteúdo entregue |
|-------|-------------------|
| §1–§4 | Propósito, O que é/não é, Princípio Central, 13 princípios de filosofia de Feedback |
| §5 | 14 Feedback Types completos (client, stakeholder, founder, user, agent, qa, system, support, artifact, workflow, node, roi, research, product) — cada tipo com definição, origem, quando usar, inputs, outputs, risco, reviewer e exemplo prático |
| §6 | 11 objetos do Feedback Object Model com schemas SQL completos: `feedback_items` (tabela principal com 36 campos), `feedback_threads`, `feedback_sources`, `feedback_decisions`, `feedback_status_transitions`, `feedback_node_links`, `feedback_artifact_links`, `feedback_roi_links`, `feedback_support_links`, `feedback_agent_eval_links`, `feedback_learning_signals` |
| §7 | Feedback Classification Engine: 5 dimensões de classificação + regras obrigatórias |
| §8 | Feedback Routing Rules: 14 regras de roteamento com destino e permissão |
| §9 | Feedback ↔ Decision System: 8 tipos de decisão + campo `decision_rationale` obrigatório |
| §10 | Feedback ↔ Learning System: `feedback_learning_signals` com 9 signal_types + 4 regras de governança (nunca auto-aplicado) |
| §11 | 14-state Feedback State Machine com transições completas e regras de bloqueio |
| §12 | 16 Feedback Events conectados ao event bus de doc 10 |
| §13 | Feedback ↔ Node Canvas: 6 node types + 8 edge types de feedback |
| §14 | Feedback ↔ Command Center: 10 intenções de feedback com intent_type e eventos |
| §15 | Feedback ↔ Dashboard: 8 widgets da Feedback Loop projeção |
| §16 | Feedback ↔ ROI: 8 tipos de link feedback↔roi (incluindo `contradicts_roi` que dispara `RoiContradicted`) |
| §17 | Feedback ↔ Support: fluxo de escalação, links bidirecionais, regras de handoff |
| §18 | Feedback ↔ Agents e Evals: `feedback_agent_eval_links` com `metacognik_review_required` |
| §19 | Feedback ↔ Research: feedback como entrada para Research Pipeline |
| §20 | 12-step Learning Loop: captured → classified → routed → reviewed → decision → action → outcome → learning_signal → Metacognik review → human approval → application → verification |
| §21 | Feedback Permissions: matriz por role × dado + RLS obrigatório + regras de redação de PII |
| §22 | Feedback QA: 12-item checklist + 5 critérios de rejeição automática |
| §23 | MVP P0: o que entra (client_feedback, founder_feedback, agent_feedback, qa_feedback; 5 intents) e o que fica fora |
| §24 | 22 Failure Modes (FM-F1 a FM-F22) com sintoma e mitigação |
| §25 | PII e Privacidade: 7 regras de governança de privacidade em feedback |
| §26 | Feedback como Sinal de Auto-Evolução: 6 condições de trigger para Self-Evolving System |
| §27 | 6 patches sugeridos (P22-1 a P22-6) — não aplicados |
| §28 | Edge Cases: 14 casos documentados |
| §29 | Related Notes |

## 22.5 Feedback Types registrados

| # | feedback_type | Origem principal | Reviewer obrigatório |
|---|---|---|---|
| 1 | `client_feedback` | Cliente final | founder ou lead |
| 2 | `stakeholder_feedback` | Stakeholder de projeto | project_lead |
| 3 | `founder_feedback` | Founder / decisor estratégico | Metacognik |
| 4 | `user_feedback` | Usuário interno (member, analyst) | qa_lead |
| 5 | `agent_feedback` | Agente CKOS (output avaliado) | Metacognik |
| 6 | `qa_feedback` | QA Lead, revisão formal | founder ou technical |
| 7 | `system_feedback` | Runtime automático (alert, eval) | technical |
| 8 | `support_feedback` | Suporte operacional | support_lead |
| 9 | `artifact_feedback` | Revisão de artifact gerado | artifact_owner |
| 10 | `workflow_feedback` | Revisão de workflow executado | workflow_owner |
| 11 | `node_feedback` | Revisão de node específico | node_owner |
| 12 | `roi_feedback` | Feedback sobre ROI model | roi_owner |
| 13 | `research_feedback` | Feedback sobre pesquisa/evidência | research_lead |
| 14 | `product_feedback` | Feedback sobre produto CKOS | PMO_CKOS |

## 22.6 Estado dos objetos — campos de segurança críticos

| Campo | Tabela | Regra |
|---|---|---|
| `is_client_visible` | `feedback_items`, `feedback_threads` | `DEFAULT false` — requer aprovação explícita para expor ao cliente |
| `is_internal` | `feedback_threads` | `DEFAULT true` — threads internas nunca visíveis ao cliente por padrão |
| `has_pii` | `feedback_items` | Se `true` → `body_redacted` obrigatório antes de qualquer display |
| `decided_by` | `feedback_decisions` | UUID humano — agentes **não podem** ser `decided_by` |
| `approved_for_application` | `feedback_learning_signals` | `DEFAULT false` — nunca auto-aplicado; requer aprovação humana |
| `metacognik_review_required` | `feedback_agent_eval_links` | Obrigatório sempre que feedback afeta eval de agente |

## 22.7 Patches sugeridos (não aplicados)

| Patch | Doc alvo | Descrição | Urgência |
|-------|----------|-----------|----------|
| **P22-1** | Doc 11 v1.3.x | Tabela `feedback_roi_links` — schema completo (link_type: contradicts_roi, supports_roi, qualifies_roi, revises_roi, validates_roi, bounds_roi, reopens_roi, escalates_roi) | Antes de Gate I |
| **P22-2** | Doc 11 v1.3.x | Tabela `feedback_support_links` — schema completo | Antes de Gate I |
| **P22-3** | Doc 11 v1.3.x | Tabela `feedback_agent_eval_links` — schema completo com `metacognik_review_required` + `suggested_action` enum | Antes de Gate G |
| **P22-4** | Doc 11 v1.3.x | Tabela `feedback_learning_signals` — schema completo com `approved_for_application DEFAULT false` + `approved_by` (human UUID) | Antes de Gate J |
| **P22-5** | Doc 11 v1.3.x | Expandir `feedback_loop_projection` em §21 com campos: `pending_decisions_count`, `converted_to_node_count`, `learning_signals_pending_approval`, `pii_detected_unredacted_count`, `recurring_friction_ids` | Antes de Gate F |
| **P22-6** | Doc 10 v1.2.x | Registrar `feedback_routing_engine` e `feedback_classification_agent` como componentes nomeados do runtime no §5.2 (flow) e §5.4 (component registry) | Antes de Gate G |

> Os patches acima são sugeridos e registrados. Não aplicar sem aprovação Technical + PMO_CKOS e versão incremental nos docs afetados.

## 22.8 Invariantes de segurança do sistema de feedback

1. **Agentes não decidem.** `feedback_decisions.decided_by` é sempre UUID humano — tentativa de agente → evento `PolicyViolationDetected` (P1).
2. **Learning signals não se auto-aplicam.** `approved_for_application DEFAULT false` — nenhum mecanismo automático pode mudar para `true` sem interação humana registrada.
3. **PII é redatado antes de exibição.** `has_pii=true` → `body_redacted` obrigatório; display de `body` raw bloqueado por policy.
4. **Client visibility é opt-in.** `is_client_visible DEFAULT false` — frontend nunca exibe feedback ao cliente sem flag explícito + permissão.
5. **Feedback nunca desaparece silenciosamente.** Toda transição para `dismissed` requer `decision_rationale` preenchido.
6. **RLS em todas as tabelas de feedback.** `tenant_id` + `org_id` em todas as tabelas; cross-tenant structurally impossible.
7. **Metacognik review obrigatório em agent eval links.** Qualquer feedback que afeta eval de agente dispara `metacognik_review_required=true`.

## 22.9 Gate de Business Systems — status atualizado

| Doc | Título | Versão | Status |
|-----|--------|:------:|--------|
| 21 | ROI Architecture | **v1.0.0 ✅** | draft — aguarda aprovação Founder + Technical + Metacognik |
| 22 | Feedback System Architecture | **v1.0.0 ✅** | draft — aguarda aprovação Founder + Technical + Metacognik |
| 23 | Support System Architecture | — | Não existe ainda |
| 24 | Credits, Plans and Billing Architecture | — | Não existe ainda |

> **Gate I requer docs 21–24 todos presentes e em draft-aprovado.** Docs 21 e 22 concluídos. Restam docs 23 e 24.
>
> **Próximo passo:** `23_SUPPORT_SYSTEM_ARCHITECTURE.md` — Support System como terceiro documento do Business Systems layer.

---

# 23. Business Systems — Doc 23 Concluído

**Data:** 2026-05-25  
**Trigger:** Docs 21 e 22 (ROI + Feedback) criados e registrados. `23_SUPPORT_SYSTEM_ARCHITECTURE.md` é o terceiro documento do `06_BUSINESS_SYSTEMS/` — obrigatório para Gate I.

## 23.1 Documento criado

| Arquivo | Diretório | Versão | Tipo |
|---------|-----------|:------:|------|
| `23_SUPPORT_SYSTEM_ARCHITECTURE.md` | `06_BUSINESS_SYSTEMS/` | **1.0.0 (29 seções)** | Criação |

## 23.2 Tese central

> **"Support in CKOS is not a helpdesk. It is a governed resolution system that captures operational friction, routes it to the right owner, tracks resolution with SLAs, escalates when needed, and feeds every unresolved issue back into the learning loop."**

## 23.3 Princípio central

> **"No support ticket should be closed without a resolution summary, a root cause classification, and a decision about whether the issue informs the product, the workflow, or the knowledge base."**

## 23.4 O que foi definido

| Seção | Conteúdo entregue |
|-------|-------------------|
| §1–§4 | Propósito, O que é/não é, Princípio Central, 12 princípios de filosofia de Support |
| §5 | 10 Support Types completos (client, admin, agent, billing, execution, security, incident, knowledge, onboarding, internal) — cada tipo com definição, origem, SLA padrão, reviewer, human handoff e exemplos |
| §6 | 12 objetos do Support Object Model com schemas SQL completos: `support_tickets` (36 campos), `support_ticket_events`, `support_categories`, `support_sla_policies`, `support_agent_links`, `support_resolution_notes`, `friction_signals`, `support_knowledge_articles`, `support_escalation_records`, `support_incident_reports`, `support_feedback_links`, `support_roi_links` |
| §7 | Support Classification Engine: 7 dimensões + 6 regras + fluxo completo |
| §8 | Support Routing Rules: tabela por tipo + 4 regras obrigatórias |
| §9 | Support SLA Policies: 4 priority tiers (P0/P1/P2/P3) com response, resolution, escalation, warning times |
| §10 | Support ↔ Feedback: 4 fluxos + 4 regras de integração |
| §11 | Support ↔ ROI: 5 ROI types afetados + quando criar `support_roi_links` |
| §12 | 13-state Support State Machine com transições completas e 6 regras |
| §13 | 16 Support Events conectados ao event bus de doc 10 |
| §14 | Support ↔ Node Canvas: 5 node types + 8 edge types + comportamento de badges |
| §15 | Support ↔ Command Center: 10 intents de suporte com intent_type e eventos |
| §16 | Support ↔ Dashboard: 6 widgets + `support_friction_projection` com 13 campos |
| §17 | Support ↔ Billing: regras de integração billing_support + 3 friction signals de billing |
| §18 | Support ↔ Agents e Evals: 5 agentes com papéis e limites + 5 eval targets |
| §19 | Human Escalation Protocol: 6 triggers + fluxo completo + handoff report format |
| §20 | Knowledge Base System: ciclo de vida de artigos + 4 métricas + 6 regras |
| §21 | Incident Management: 4 severity levels + lifecycle + 4 regras de post-mortem |
| §22 | Support Permissions: matriz 7 roles × 11 ações + 8 regras de segurança |
| §23 | Support QA Checklist: SU1–SU14 + 5 critérios de rejeição automática |
| §24 | MVP P0: componentes in/out com motivo e urgência |
| §25 | 20 Failure Modes (FM-S1 a FM-S20) com sintoma e mitigação |
| §26 | Support como Aprendizado Sistêmico: 6 fluxos de saída + invariante de fechamento de loop |
| §27 | 6 patches sugeridos (P23-1 a P23-6) — não aplicados |
| §28 | 14 Edge Cases |
| §29 | Related Notes |

## 23.5 Support Types registrados

| # | ticket_type | Prioridade padrão | Human obrigatório |
|---|---|:---:|:---:|
| 1 | `client_support` | P2 (P1 se contrato em risco) | Após 1 falha de agente |
| 2 | `admin_support` | P2 | Não obrigatório |
| 3 | `agent_support` | P2 (P1 se loop) | Após 2 falhas |
| 4 | `billing_support` | P1 / P2 | **Sempre** |
| 5 | `execution_support` | P2 (P1 se production-blocking) | Após diagnóstico falhar |
| 6 | `security_support` | P0 (sempre) | **Sempre** |
| 7 | `incident_support` | P0 / P1 | **Sempre** |
| 8 | `knowledge_support` | P3 | Para novos artigos |
| 9 | `onboarding_support` | P2 | Para enterprise |
| 10 | `internal_support` | P2 / P3 | Decisão PMO_CKOS |

## 23.6 SLA tiers

| Prioridade | Resposta | Resolução | Escalação | Warning |
|:----------:|:--------:|:---------:|:---------:|:-------:|
| P0 | ≤ 15 min | ≤ 4 h | 10 min | 80% |
| P1 | ≤ 1 h | ≤ 24 h | 45 min | 80% |
| P2 | ≤ 4 h | ≤ 72 h | 3 h | 80% |
| P3 | ≤ 24 h | ≤ 7 d | 20 h | 80% |

## 23.7 Invariante de fechamento de loop

> Todo ticket fechado deve ter pelo menos um de: knowledge article criado, friction_signal incrementado, feedback_item gerado, ou `root_cause_category` documentado como `no_pattern_detected`.

## 23.8 Patches sugeridos (não aplicados)

| Patch | Doc alvo | Descrição | Urgência |
|-------|----------|-----------|----------|
| **P23-1** | Doc 11 v1.3.x | Tabela `support_knowledge_articles` — schema completo com `source_ticket_ids`, `helpful_count`, `last_helpful_ratio`, RLS por `tenant_id` | Antes de Knowledge Base MVP |
| **P23-2** | Doc 11 v1.3.x | Tabela `support_escalation_records` — schema completo com `escalation_level`, `escalated_by_type`, `sla_breach_at` | Antes de Escalation Protocol MVP |
| **P23-3** | Doc 11 v1.3.x | Tabela `support_incident_reports` — schema completo com `timeline jsonb`, `affected_systems text[]`, `post_mortem_doc_url`, `lessons_learned` | Antes de Incident Management P1 |
| **P23-4** | Doc 11 v1.3.x | Tabela `support_feedback_links` — schema completo bidirecional | Antes de Gate I |
| **P23-5** | Doc 11 v1.3.x | Expandir `support_friction_projection` em §21 com campos: `agent_resolution_rate`, `human_handoff_rate`, `knowledge_gap_count`, `sla_compliance_rate`, `avg_resolution_hours_by_type` | Antes de Gate F |
| **P23-6** | Doc 10 v1.2.x | Registrar `support_classification_agent`, `friction_detection_engine`, `support_routing_engine` e `sla_engine` como componentes nomeados do runtime | Antes de Gate G |

> Patches P23-1 a P23-6 registrados. Não aplicar sem aprovação formal Technical + PMO_CKOS e versão incremental nos docs afetados.

## 23.9 Gate de Business Systems — status atualizado

| Doc | Título | Versão | Status |
|-----|--------|:------:|--------|
| 21 | ROI Architecture | **v1.0.0 ✅** | draft — aguarda aprovação Founder + Technical + Metacognik |
| 22 | Feedback System Architecture | **v1.0.0 ✅** | draft — aguarda aprovação Founder + Technical + Metacognik |
| 23 | Support System Architecture | **v1.0.0 ✅** | draft — aguarda aprovação Founder + Technical + Metacognik |
| 24 | Credits, Plans and Billing Architecture | — | Não existe ainda |

> **Gate I requer docs 21–24 todos presentes e em draft-aprovado.** Docs 21, 22 e 23 concluídos. Resta apenas o doc 24.
>
> **Próximo passo:** `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md` — quarto e último documento do Business Systems layer. Após doc 24, Gate I pode ser submetido para aprovação formal.

---

# 24. Business Systems — Doc 24 Concluído e Gate I Fechado

**Data:** 2026-05-25  
**Trigger:** Docs 21, 22 e 23 (ROI + Feedback + Support) criados e registrados. `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md` é o quarto e último documento do `06_BUSINESS_SYSTEMS/` — completa Gate I.

## 24.1 Documento criado

| Arquivo | Diretório | Versão | Tipo |
|---------|-----------|:------:|------|
| `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md` | `06_BUSINESS_SYSTEMS/` | **1.0.0 (29 seções)** | Criação |

## 24.2 Tese central

> **"Billing in CKOS is not a payment gateway integration. It is a governed monetization layer that translates runtime consumption into customer-facing value exchanges — with credit pre-reservation, quota enforcement, transparent invoicing, and a clean separation between what CKOS spends internally and what the customer is charged."**

## 24.3 Princípio central e invariante mais crítica

> **"Internal runtime cost and external customer billing are distinct systems that must never be confused: cost_ledger tracks what CKOS spends; billing_events track what customers owe. Only explicit billing events — not cost_ledger entries — generate charges."**

## 24.4 O que foi definido

| Seção | Conteúdo entregue |
|-------|-------------------|
| §1–§4 | Propósito, O que é/não é, Princípio Central, 12 princípios de filosofia de Billing |
| §5 | Plans Architecture: 4 tiers (Free/Starter/Professional/Enterprise) com feature gates, limites e overage policies completos |
| §6 | Credits Architecture: unidade universal de consumo, 10 resource types, ciclo de vida com balanços |
| §7 | Credit Reservation Pattern: fluxo completo (reserva → execução → consumo → liberação → expiração) com 6 regras obrigatórias |
| §8 | Quota Architecture: 6 quota types + enforcement flow + `quota_policies` schema |
| §9 | 13 Billing Objects com schemas SQL completos: `plans`, `plan_features`, `subscriptions`, `credit_wallets`, `credit_transactions`, `credit_reservations`, `usage_events`, `billing_events`, `invoice_records`, `plan_limits`, `credit_rate_config`, `billing_disputes`, `billing_alerts` |
| §10 | Distinção crítica Cost Ledger vs. Billing: tabela comparativa + fluxo de conversão |
| §11 | Subscription State Machine (6 estados) + Invoice State Machine (8 estados) com transições |
| §12 | 16 Billing Events conectados ao event bus de doc 10 |
| §13 | Billing ↔ Support: 4 fluxos + 4 regras de isolamento |
| §14 | Billing ↔ ROI: tabela custo/valor por perspectiva + 4 ROI types afetados |
| §15 | Billing ↔ Node Canvas: 4 node types + comportamento |
| §16 | Billing ↔ Command Center: 10 intents de billing com intent_type e eventos |
| §17 | Billing ↔ Dashboard: 6 widgets + `cost_credit_projection` campos de billing |
| §18 | Overage flow + Upgrade/Downgrade flow completos |
| §19 | Invoice Generation: ciclo de vida + rastreabilidade obrigatória + aprovações |
| §20 | Billing Disputes: processo completo com regras de governança |
| §21 | Whitelabel Billing: modelo de sub-tenant + 6 regras de isolamento |
| §22 | Billing Permissions: matriz 7 roles × 13 ações + 10 regras de segurança |
| §23 | Billing QA Checklist: BL1–BL16 + 5 critérios de rejeição automática |
| §24 | MVP P0: componentes in/out com motivo e urgência |
| §25 | 20 Failure Modes (FM-B1 a FM-B20) com sintoma e mitigação |
| §26 | Business Systems Gate — Status Final |
| §27 | 6 patches sugeridos (P24-1 a P24-6) — não aplicados |
| §28 | 14 Edge Cases |
| §29 | Related Notes |

## 24.5 Patches sugeridos (não aplicados)

| Patch | Doc alvo | Descrição | Urgência |
|-------|----------|-----------|----------|
| **P24-1** | Doc 11 v1.3.x | Tabela `credit_rate_config` — schema completo com versioning + `approved_by` (Founder) obrigatório | Antes de Billing MVP |
| **P24-2** | Doc 11 v1.3.x | Tabela `billing_disputes` — schema completo com `reviewed_by` (human UUID) + `resolution_note` obrigatório | Antes de Dispute flow P1 |
| **P24-3** | Doc 11 v1.3.x | Tabela `billing_alerts` — schema completo com `threshold_percent`, `threshold_credits`, `notify_roles`, `channel` | Antes de Alerts MVP |
| **P24-4** | Doc 11 v1.3.x | `idempotency_key UNIQUE` em `credit_transactions`, `usage_events` e `billing_events` | Antes de qualquer billing em produção |
| **P24-5** | Doc 11 v1.3.x | Expandir `cost_credit_projection` em §21 com campos: `balance_available`, `quota_monthly_percent`, `billing_alerts_active`, `invoice_overdue_count`, `subscription_status`, `plan_code` | Antes de Gate F |
| **P24-6** | Doc 10 v1.2.x | Registrar `quota_engine`, `billing_engine`, `credit_wallet_engine` e `feature_gate_engine` como componentes nomeados do runtime | Antes de Gate I |

## 24.6 Gate I — Business Systems Gate: FECHADO ✅

**Todos os quatro documentos obrigatórios do `06_BUSINESS_SYSTEMS/` existem e estão versionados.**

| Doc | Título | Versão | Patches sugeridos |
|-----|--------|:------:|:-----------------:|
| 21 | ROI Architecture | **v1.0.0 ✅** | P21-1 a P21-6 |
| 22 | Feedback System Architecture | **v1.0.0 ✅** | P22-1 a P22-6 |
| 23 | Support System Architecture | **v1.0.0 ✅** | P23-1 a P23-6 |
| 24 | Credits, Plans and Billing Architecture | **v1.0.0 ✅** | P24-1 a P24-6 |

**Total de patches sugeridos pelos Business Systems (não aplicados):** 24 patches (P21-1..P24-6)

> **GATE I STATUS: DOCUMENTALMENTE COMPLETO — PRONTO PARA APROVAÇÃO FORMAL** ✅
>
> Os 4 documentos do Business Systems layer existem, estão versionados e são mutuamente referenciáveis. Cada documento define a arquitetura de seu sistema sem implementar backend, frontend, migrations ou agentes.
>
> **Aprovação requerida para Gate I:** Founder + Technical (conforme doc 20 §7 Gate I).  
> **Metacognik:** revisão obrigatória dos 4 documentos antes da aprovação do Founder.
>
> **Ainda bloqueado:** implementação de qualquer funcionalidade de Business Systems — aguarda aprovação formal dos 4 documentos + patches P21-1 a P24-6 avaliados e aplicados em doc 11 v1.3.x antes do início de implementação.
>
> **Patches de alta urgência antes de qualquer billing em produção:**  
> P24-4 (`idempotency_key` obrigatório) e P24-1 (`credit_rate_config` versioning) são pré-condições absolutas de qualquer operação de billing — devem ser os primeiros a serem aplicados em doc 11 v1.3.x.
>
> **Alertas críticos transversais aos 4 documentos:**
> 1. `cost_ledger` (doc 11 §18) e `billing_events` são sistemas distintos — implementá-los como um só é erro de arquitetura grave.
> 2. `credit_reservations.expires_at` é obrigatório — sem TTL, reservas presas causam `balance_reserved` crescendo indefinidamente.
> 3. `feedback_learning_signals.approved_for_application DEFAULT false` — nunca auto-aplicado.
> 4. `support_tickets` de tipo `billing_support` e `security_support` nunca resolvidos apenas por agente.
> 5. ROI claims sem `confidence_level` ou sem `evidence_links` nunca exibidos ao cliente.
> 6. Todos os sistemas têm RLS por `tenant_id` — cross-tenant structurally impossible em todas as 4 camadas.
>
> **Próximo passo documentacional:** Patch Plan 15 + reescrita Doc 16 conforme plano ativo em `.claude/plans/radiant-soaring-church.md`.

---

# 25. RAW/STUDY Governance Patch

**Data:** 2026-05-27  
**Trigger:** Microgate RAW/STUDY executado com sucesso e aprovado pelo Founder para reconhecimento canonico de governanca.

## 25.1 Criacao anterior reconhecida

As camadas reais abaixo ja foram criadas em microgate anterior:

- `000_UPLOADS/`
- `000_STUDY_NOTES/`

Tambem foram criados READMEs locais, `_folder_memory.md` por pasta, templates RAW/STUDY, indices locais e atualizacoes de mapas auxiliares autorizados.

## 25.2 Objetivo do patch atual

Formalizar nos documentos de governanca que o vault `CKOS_DOCUMENTATION_REVIEWED` opera com tres camadas documentais:

```txt
RAW / 000_UPLOADS
  -> material bruto, sem autoridade canonica

STUDY / 000_STUDY_NOTES
  -> interpretacao, provenance, confidence, riscos, lacunas, recomendacao PMO e patch candidates

CANONICAL / docs versionados
  -> documentos oficiais alterados apenas por patch plan, aprovacao humana, QA documental e registro neste report
```

Regra principal adicionada: nada entra no canonico sem passar por STUDY.

## 25.3 Arquivos alterados

| Arquivo | Versao anterior | Versao nova | Mudanca |
|---|:---:|:---:|---|
| `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md` | 2.3.0 | 2.4.0 | reconhece RAW/STUDY, posiciona `000_UPLOADS/` e `000_STUDY_NOTES/` antes das fases canonicas e formaliza RAW -> STUDY -> CANONICAL |
| `00_SYSTEM_GOVERNANCE/00_DOCUMENT_TEMPLATE.md` | 2.2.0 | 2.3.0 | adiciona suporte formal a notas RAW/STUDY, enums `layer`, `doc_type`, `confidence`, `provenance_status` e template resumido |
| `00_SYSTEM_GOVERNANCE/00_TAXONOMY_AND_NAMING.md` | 2.2.0 | 2.3.0 | formaliza naming de uploads e study notes e diferencia raw source, study note, patch candidate e canonical doc |
| `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md` | 2.2.0 | 2.3.0 | adiciona dependencia RAW/STUDY para docs futuros 25-34, bloqueia UI/UX ate docs 25-31 e registra invariantes de MCP/conectores |
| `ARCHITECTURE_PATCH_REPORT.md` | 1.7.0 | 1.8.0 | registra este patch de governanca |

## 25.4 Regras adicionadas

- `000_UPLOADS/` e camada RAW de ingestao, nao canonica.
- `000_STUDY_NOTES/` e camada STUDY de interpretacao, nao canonica.
- `000_UPGRADE/` permanece zona auxiliar de continuidade, packs, memorias e transicao; nao vira camada oficial de ingestao.
- RAW -> STUDY -> CANONICAL e o fluxo oficial de promocao de conhecimento.
- Output de IA entra como `confidence: unverified` por padrao.
- `source_tool` nao e fonte de verdade.
- `source_path` deve apontar para origem verificavel quando possivel.
- Study notes podem sugerir patch, mas nao alteram documentos oficiais.
- `patch_candidate` exige aprovacao antes de canonizacao.

## 25.5 MCP, conectores e integracoes

MCP, conectores e integracoes foram posicionados como temas obrigatorios antes de UI/UX. Nenhuma integracao pode bypassar:

- `policy_engine`
- `tool_router`
- `approval_gate`
- `cost_guard`
- `audit_logs`
- tenant isolation
- `secret_refs`

## 25.6 Confirmacoes de escopo

- Docs canonicos 01-24 nao foram alterados neste patch.
- Business Systems 21-24 nao foram alterados neste patch.
- Docs 25-34 nao foram criados.
- UI/UX nao foi iniciada.
- Backend, migrations, API, banco, agentes reais e automacoes runtime nao foram criados.
- Nenhum arquivo foi movido, deletado ou renomeado.
- JSONs n8n, `.obsidian/` e `Memoria GPT.md` nao foram alterados.
- Manus, n8n, Antigravity, Claude, Codex e ChatGPT nao foram promovidos a fonte canonica.

## 25.7 Status

**RAW/STUDY governance recognized.**

O vault agora reconhece formalmente a arquitetura documental:

```txt
RAW -> STUDY -> CANONICAL
```

## 25.8 Proximo microgate recomendado

**Microgate Self-Evolving Conflict Resolution** — concluido em 2026-05-27.

Resolucao aplicada em patch posterior: novo `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`, antigo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` preservado como superseded, ROI mantido como doc 21.

---

# 26. Self-Evolving Conflict Resolution Patch

**Data:** 2026-05-27  
**Trigger:** Founder aprovou o decision log `000_STUDY_NOTES/08_DECISION_LOGS/20260527_decision_self-evolving-conflict-resolution_pmo_ckos_draft.md`.

## 26.1 Objetivo

Resolver a ambiguidade documental entre:

- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`
- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`

Decisao aplicada: ROI permanece doc 21; Self-Evolving ativo passa a ser doc 25 em nova camada canonica `07_EVOLUTION_SYSTEM/`.

## 26.2 Arquivos criados

- `07_EVOLUTION_SYSTEM/00_README_EVOLUTION_SYSTEM.md`
- `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`

## 26.3 Arquivos alterados

- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` — adicionado superseded notice no topo; conteudo historico preservado.
- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md` — registra `07_EVOLUTION_SYSTEM/`, doc 25 e ROI como doc 21 ativo.
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md` — atualiza dependencias para Self-Evolving (25) e mantem UI/UX bloqueado ate docs 25-31.
- `CKOS_FILETREE_MAP.md` — registra nova pasta, doc 25 e status superseded do antigo 21.
- `CKOS_FOLDER_MEMORY.md` — registra memoria da pasta `07_EVOLUTION_SYSTEM/` e a decisao de preservacao historica.
- `CKOS_VAULT_MAP_REFRESH_REPORT.md` — registra o refresh do microgate Self-Evolving.

Referencias diretas permitidas tambem foram atualizadas em:

- `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md`
- `03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`
- `03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`
- `05_IMPLEMENTATION_SYSTEM/17_IMPLEMENTATION_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`

## 26.4 Regras confirmadas

- Nao houve rename direto.
- Nao houve move.
- Nao houve delete.
- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` permanece como historico/superseded.
- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md` permanece o doc 21 ativo.
- `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` e o doc ativo para Self-Evolving.
- Docs 26-34 nao foram criados.
- UI/UX continua bloqueado.
- Backend, migrations, API, banco, agentes reais e automacoes runtime continuam bloqueados.

## 26.5 Status

**Self-Evolving conflict resolved.**

## 26.6 Proximo microgate recomendado

**Microgate Connectors, MCP and Integrations Architecture**

Objetivo: criar o doc 26 somente apos validar a matriz MCP/API/collector/webhook/n8n/nativo, mantendo invariantes de `policy_engine`, `tool_router`, `approval_gate`, `cost_guard`, `audit_logs`, tenant isolation e `secret_refs`.

## 26.7 Doc 26 criado - Connectors, MCP and Integrations Architecture

**Trigger:** P1.11.1 PMO Closure Note recomendou Doc 26 como proximo passo documental.

**Arquivo criado:** `07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`

**Versao:** 1.0.0 draft.

**Escopo:** arquitetura documental de conectores, MCP, APIs, collectors, webhooks, ferramentas externas, research connectors, n8n prototype-only, `secret_refs`, `cost_guard`, `audit_logs`, tenant isolation, risk model, failure modes e MVP P0.

**Patches sugeridos, nao aplicados:**

| Patch | Doc alvo | Descricao | Urgencia |
|---|---|---|---|
| P26-1 | Doc 10 | Formalizar `connector_adapter` e `mcp_adapter` como subcomponentes ou camada adaptadora abaixo do `tool_router`, conforme P26-1 | Antes de connector runtime |
| P26-2 | Doc 11 | Criar/expandir `connector_registry`, `connector_runs`, `connector_credentials`, `connector_events`, `mcp_servers`, `mcp_tool_bindings` | Antes de migrations |
| P26-3 | Doc 12 | Expandir policies para connector grants, secret scopes e external data egress | Antes de processamento externo |
| P26-4 | Doc 13 | Adicionar evals de connector reliability, evidence quality, cost drift e privacy violations | Antes de conectores em producao |
| P26-5 | Doc 18 | Alinhar research connectors com connector registry | Antes de research connectors |
| P26-6 | Doc 24 | Mapear consumo de creditos por connector/tool/collector/webhook/MCP call | Antes de uso pago |

**Gate:** implementacao continua bloqueada. Claude deve auditar o Doc 26 antes de qualquer patch em docs 10-13/18/24 ou abertura de docs 27-34.

## 26.8 Doc 26 v1.0.1 - PMO/Metacognik audit light patch

**Trigger:** Auditoria PMO/Metacognik apontou patches obrigatorios P1-A a P1-F no Doc 26.

**Arquivo alterado:** `07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`

**Versao:** 1.0.0 -> 1.0.1 draft.

**Escopo:** patch documental leve; sem implementacao.

**Patches aplicados no Doc 26:**

| Patch | Correcao documental | Status |
|---|---|---|
| P1-A | `mcp_tool_bindings` agora inclui `org_id uuid [RLS]` e `workspace_id uuid` | aplicado |
| P1-B | P26-7 adicionado para `collectors_allowlist`, resolvendo deferral P18-6 | aplicado |
| P1-C | P26-1 explicita `connector_adapter` e `mcp_adapter` sob ou imediatamente abaixo do `tool_router` | aplicado |
| P1-D | P26-8 adicionado para registrar os 23 connector events do Doc 26 §17 no catalogo de eventos do Doc 10 §5.3 | aplicado |
| P1-E | P26-2 expandido com schemas futuros `webhook_registrations` e `webhook_deliveries` | aplicado |
| P1-F | `approval_policy` substituido por `approval_policy_ref uuid fk->approval_policies` nos schemas connector/MCP | aplicado |
| P2-A | Contratos minimos de `cost_profile jsonb` e `data_egress_policy jsonb` adicionados | aplicado |

**Confirmacoes de escopo:**

- Docs 10, 11, 12, 13, 18 e 24 nao foram alterados.
- Docs 27-34 nao foram criados.
- Nenhum backend, API, migration, MCP server real, JSON n8n, UI, agente real ou automacao runtime foi criado.
- P26-1 a P26-8 continuam patches sugeridos, nao aplicados aos docs alvo.

**Gate:** Claude/Metacognik deve auditar o Doc 26 v1.0.1 antes de qualquer patch real em docs 10/11/12/13/18/24.

## 26.9 Doc 26 v1.0.2 - PMO/Metacognik audit light patch

**Trigger:** Auditoria PMO/Metacognik aprovou o Doc 26 v1.0.1 com patches leves, mas bloqueou abertura do Doc 27 ate resolver L-01 a L-09.

**Arquivo alterado:** `07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`

**Versao:** 1.0.1 -> 1.0.2 draft; v1.0.2 mantida em patch complementar documental L-01 a L-09.

**Escopo:** patch documental leve; sem implementacao.

**Patches aplicados no Doc 26:**

| Patch | Correcao documental | Status |
|---|---|---|
| L-01 | `connector_events` agora inclui `org_id uuid [RLS]` | aplicado |
| L-02 | Extensao futura de `secret_refs.owner_type` explicita `connector`, `mcp_server` e `webhook` | aplicado |
| L-03 | Lifecycle de `connector_registry.status` explicitado; apenas conectores `active` podem executar | aplicado |
| L-04 | Grants de conectores devem ser action-scoped; wildcard nao autoriza mutacao externa nem data egress | aplicado |
| L-05 | Webhooks exigem tenant resolution, signing secret reference, allowed event types e idempotency policy antes de route | aplicado |
| L-06 | Conectores provider-facing exigem rate-limit e retry policy; ausencia de policy falha fechado | aplicado |
| L-07 | Outputs de research/collector exigem source metadata replayable antes de virar evidence/context | aplicado |
| L-08 | Fallback nao pode enfraquecer policy, tenant isolation, secret handling, approval ou audit | aplicado |
| L-09 | Ativacao runtime permanece bloqueada ate patches nos docs alvo, auditoria externa e aprovacao formal | aplicado |

**Confirmacoes de escopo:**

- Docs 10, 11, 12, 13, 18 e 24 nao foram alterados.
- Docs 27-34 nao foram criados.
- Nenhum backend, API, migration, MCP server real, webhook real, JSON n8n, UI, agente real ou automacao runtime foi criado.
- Nenhuma recomendacao L-01 a L-09 foi promovida para implementacao; todas permanecem como patch documental no Doc 26.

**Gate:** Doc 27 continua bloqueado ate auditoria externa confirmar Doc 26 v1.0.2 com L-01 a L-09.

## 26.10 Doc 26 v1.0.3 - Traceability reconciliation and open schema decisions

**Data:** 2026-05-31

**Trigger:** sessao claude_doc26_audit_readonly (2026-05-31) completou auditoria externa de v1.0.3 e emitiu CHECKOUT RELEASE REL-DOC26-AUDIT-20260531.

**Arquivo alterado:** `07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`

**Versao:** 1.0.2 -> 1.0.3 draft.

**Escopo:** patch documental leve; reconciliacao de rastreabilidade; sem implementacao.

**Traceabilidade reconciliada para L-03 a L-09:**

| Patch | Correcao documental aplicada no Doc 26 | Status |
|---|---|---|
| L-03 | Lifecycle de `connector_registry.status` explicitado; apenas conectores `active` podem executar | aplicado no Doc 26; rastreabilidade reconciliada |
| L-04 | Grants de conectores devem ser action-scoped; wildcard nao autoriza mutacao externa nem data egress | aplicado no Doc 26; rastreabilidade reconciliada |
| L-05 | Webhooks exigem tenant resolution, signing secret reference, allowed event types e idempotency policy antes de route | aplicado no Doc 26; rastreabilidade reconciliada |
| L-06 | Conectores provider-facing exigem rate-limit e retry policy; ausencia de policy falha fechado | aplicado no Doc 26; rastreabilidade reconciliada |
| L-07 | Outputs de research/collector exigem source metadata replayable antes de virar evidence/context | aplicado no Doc 26; rastreabilidade reconciliada |
| L-08 | Fallback nao pode enfraquecer policy, tenant isolation, secret handling, approval ou audit | aplicado no Doc 26; rastreabilidade reconciliada |
| L-09 | Ativacao runtime permanece bloqueada ate patches nos docs alvo, auditoria externa e aprovacao formal | aplicado no Doc 26; rastreabilidade reconciliada |

**Versionamento aplicado no Doc 26:**

- `version: 1.0.3`
- `updated_at: 2026-05-31`
- `version_note: "v1.0.3 reconciles L-03 to L-09 traceability, bumps version after normative connector constraints, and declares open schema decisions for P26-2."`

**Decisoes abertas declaradas para P26-2:**

1. `webhook_deliveries`: decidir entre append-only event model ou mutable status com companion table de attempts.
2. `connector_events`: decidir entre bridge table fisica ou view/read model derivada da tabela `events`.

**Confirmacoes de escopo:**

- Docs 01-25 nao foram alterados.
- Docs 27-34 nao foram criados.
- Docs 10, 11, 12, 13, 18 e 24 nao foram alterados.
- Nenhum backend, UI, API, migration, banco, MCP server real, webhook real, JSON n8n, agente real ou automacao runtime foi criado.
- P26-1, P26-2, P26-3, P26-4, P26-6 e P26-8 continuam nao resolvidos.

**Gate:** Doc 27 continua bloqueado ate auditoria externa confirmar Doc 26 v1.0.3.

## 26.11 Doc 26 v1.0.4 - Light governance patch after external audit

**Data:** 2026-05-31

**Trigger:** Auditoria externa do Doc 26 v1.0.3 aprovou com patches leves PL-01, PL-02, PL-04 e PL-05.

**Arquivo alterado:** `07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`

**Versao:** 1.0.3 -> 1.0.4 draft.

**Escopo:** patch documental leve; sem implementacao.

**Patches aplicados:**

| Patch | Correcao documental | Status |
|---|---|---|
| PL-01 | Doc 26 section 9 explicita que `connector_adapter` e `mcp_adapter` sao placeholders documentais pendentes de P26-1 em Doc 10. | aplicado |
| PL-02 | Doc 26 section 17 explicita que os 23 connector event types requerem P26-8 antes de qualquer runtime emitir eventos. | aplicado |
| PL-04 | Architecture Patch Report section 26.7 substitui a terminologia antiga por `connector_adapter` e `mcp_adapter` abaixo de `tool_router`, conforme P26-1. | aplicado |
| PL-05 | Architecture Patch Report section 26.10 referencia a auditoria externa `claude_doc26_audit_readonly` e o release `REL-DOC26-AUDIT-20260531`. | aplicado |

**Confirmacoes de escopo:**

- Docs 01-25 nao foram alterados.
- Docs 27-34 nao foram criados.
- Study Layer 13 nao foi tocada.
- Nenhum backend, UI, API, migration, banco, MCP server real, webhook real, JSON n8n, agente real ou automacao runtime foi criado.
- P26-1, P26-2, P26-3, P26-4, P26-6 e P26-8 continuam nao resolvidos nos docs alvo.

**Gate:** Doc 27 continua bloqueado/liberavel apenas condicionalmente, apos governanca PMO/Founder explicita. Nao abrir Doc 27 nesta sessao.

---

# 26. Multi-Session Execution Policy — P1.7/P1.7.1

**Data:** 2026-05-28  
**Trigger:** Auditoria PMO/Metacognik aprovou P1.7 com registros e solicitou refresh minimo P1.7.1.

## 26.1 Objetivo

Registrar a camada auxiliar governada de execucao multi-sessao do CKOS, permitindo coordenacao entre Codex, Claude, Antigravity e futuros chats especializados sem liberar implementacao, Design Study ou canonizacao automatica.

## 26.2 P1.7 - Arquivos criados

- P1.7 criou `000_ROADMAPS/SESSION_REGISTRY.md`.
- P1.7 criou `000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md`.
- P1.7 criou `000_STUDY_NOTES/12_SESSION_GATES/`.
- P1.7 criou `000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md`.

## 26.3 P1.7 - Decisoes registradas

- `12_SESSION_GATES/` foi criado fora de `07_CANONICAL_PATCH_CANDIDATES/` porque gates de sessao nao sao patch candidates.
- Antigravity esta bloqueado ate aprovacao explicita do Founder.
- Antigravity so pode operar futuramente em sessao `design_study` com checkout lock, escopo study-only e checkout release.
- A camada multi-session e auxiliar governada; ela nao substitui docs canonicos.

## 26.4 P1.7.1 - Refresh aplicado

- P1.7.1 fez bump dos tres arquivos principais para `version: 1.0.0`:
  - `000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md`;
  - `000_ROADMAPS/SESSION_REGISTRY.md`;
  - `000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md`.
- P1.7.1 adicionou a frase obrigatoria da politica em `MULTI_SESSION_EXECUTION_POLICY.md`.
- P1.7.1 corrigiu o padrao de memoria da pasta com `000_STUDY_NOTES/12_SESSION_GATES/ck_memory.md`.
- `_folder_memory.md` permanece como legacy/superseded, sem delecao.
- `SESSION_REGISTRY.md` registrou a propria sessao P1.7.1 como `memory_refresh`.

## 26.5 Confirmacoes de escopo

- Docs 26-34 continuam nao criados.
- Docs canonicos 01-25 nao foram alterados por P1.7/P1.7.1.
- Business Systems 21-24 nao foram alterados por P1.7/P1.7.1.
- UI/UX continua bloqueado.
- Antigravity Study Mode continua bloqueado.
- Design Study nao foi liberado.
- Backend, API, banco, migrations, JSONs n8n e agentes reais nao foram criados.
- Nenhum arquivo foi movido, deletado ou renomeado.

## 26.6 Status

**Multi-session layer governed.**

P1.7/P1.7.1 registra governanca auxiliar de sessoes, checkout lock/release, registry, nivel de inteligencia e gate Antigravity. Nao declara implementacao liberada e nao declara Design Study liberado.

---

# 27. Governance Maps Light Patch - PL-03/PL-07/PL-08-NOVO

**Data:** 2026-06-01

**Sessao:** `S-P1-26-CODEX-20260601-002`

**Trigger:** Auditoria externa do Doc 26 v1.0.4 identificou patches leves pendentes nos mapas de governanca.

**Escopo:** canonical_patch restrito a mapas auxiliares de governanca, registro de patch e registro de sessao; sem implementacao.

**Arquivos alterados:**

- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md`
- `ARCHITECTURE_PATCH_REPORT.md`
- `000_ROADMAPS/SESSION_REGISTRY.md`

## 27.1 Patches aplicados

| Patch | Correcao documental | Status |
|---|---|---|
| PL-03 | `00_MASTER_MAP.md` passa a listar `18_RESEARCH_PROTOCOL.md` como canonico e preserva `18_RESEARCH_PROTOCOL_FOR_MANUS.md` como historico/legacy superseded. | aplicado |
| PL-07 | `00_DEPENDENCY_MAP.md` substitui `18_RESEARCH_MANUS` por `18_RESEARCH_PROTOCOL` e registra o arquivo Manus como superseded/historical. | aplicado |
| PL-08-NOVO | `00_MASTER_MAP.md` passa a listar `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md` como canonico e preserva `19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md` como historico/legacy superseded. | aplicado |

## 27.2 Confirmacoes de escopo

- Docs 01-26 nao foram alterados por esta sessao.
- Docs 27-34 nao foram criados.
- Study Layer 13 e Study Layer 14 nao foram tocadas.
- Nenhum backend, UI, API, database, migration, MCP server, webhook, JSON n8n, agente real ou automacao runtime foi criado.
- `SESSION_REGISTRY.md` registra checkout lock e release da sessao.

## 27.3 Status

**PL-03, PL-07 e PL-08-NOVO aplicados.**

Doc 27 permanece bloqueado/liberavel apenas por decisao futura explicita de governanca PMO/Founder.

---

# 28. Doc 27 Canonical Draft Creation - AI-first Work Orders And Multi-Session Orchestration

**Data:** 2026-06-01

**Sessao:** `S-P1-27-CODEX-20260601-001`

**Task ID:** `DOC27_AI_FIRST_WORK_ORDERS_AND_MULTI_SESSION_ORCHESTRATION_CREATION_20260601`

**Checkout lock:** `LOCK-P1-27-CODEX-20260601-001`

**Checkout release:** `REL-P1-27-CODEX-20260601-001`

**Trigger:** Founder aprovou explicitamente a abertura do Doc 27 como canonical draft estreito para AI-first Work Orders and Multi-Session Orchestration Architecture.

**Gate traceability (LP-2):** Doc 27 foi aberto depois da cadeia de gate registrada em `SESSION_REGISTRY.md`: `S-P1-13-CLAUDE-20260531-001` auditou Study Layer 13 read-only; `S-P1-27-CLAUDE-20260601-002` auditou Layer 13/14 para Doc 27 readiness com verdict `OPEN_WITH_CONDITIONS` e PATCH-OBR-1..6; `S-P1-13-CODEX-20260601-009` aplicou o cleanup obrigatorio das camadas 13/14; `S-P1-13-CODEX-20260601-008` registrou a allowed/forbidden section list e gate conditions na Nota 24; PMO/Founder fan-in autorizou o checkout canonical draft `LOCK-P1-27-CODEX-20260601-001`.

**Escopo:** canonical_patch documental; sem backend, UI, API, database, migrations, MCP server real, webhook real, JSON n8n, agentes reais, automacoes runtime, slash-command runtime ou autonomous dispatch runtime.

## 28.1 Arquivo criado

- `07_EVOLUTION_SYSTEM/27_AI_FIRST_WORK_ORDERS_AND_MULTI_SESSION_ORCHESTRATION_ARCHITECTURE.md`

## 28.2 Arquivos alterados

- `000_ROADMAPS/SESSION_REGISTRY.md`
- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md`
- `ARCHITECTURE_PATCH_REPORT.md`

## 28.3 Conteudo canonico criado

Doc 27 define arquitetura documental para:

- Work Orders como envelopes governados de execucao;
- task como unidade atomica;
- Batch Execution;
- fan-out/fan-in audit;
- checkout lock and release;
- session routing for Codex, Claude, Windsurf, Antigravity and ChatGPT PMO;
- BRA Session Relay as documentary relay only;
- Work Order `context_pack` as internal Work Order state;
- Founder approval batches;
- smart questions;
- Cognik and Metacognik as roles only;
- ROI by Work Order and task;
- evidence, feedback and memory hooks.

## 28.4 Dependencias e limites

- Doc 26 remains the owner of connectors, MCP, webhooks, external tools and `secret_refs`.
- Future Doc 28 is cited only as the owner candidate for Notes/RAG, metadata, vector categories, embeddings and retrieval governance.
- Doc 11 is cited only as the required future owner of any real Work Order/task/BRA/context persistence schema.
- Docs 12, 13 and 24 are referenced as governance/evals/cost dependencies only.
- `MULTI_SESSION_EXECUTION_POLICY.md` remains the source for checkout lock/release discipline.

## 28.5 Confirmacoes de escopo

- Docs 01-26 nao foram alterados.
- Docs 28-34 nao foram criados.
- Study Layer 13 nao foi alterada.
- Study Layer 14 nao foi alterada.
- Doc 26 foi apenas referenciado.
- Doc 28 foi apenas citado como futuro.
- Doc 11 foi apenas citado para patch futuro.
- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md` recebeu apenas entrada minima para Doc 27.
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md` recebeu apenas entrada minima para Doc 27 e ajuste do futuro Doc 28.
- Nenhum backend, UI, API, database, migration, MCP server real, webhook real, JSON n8n, agente real ou automacao runtime foi criado.

## 28.6 Status

**Doc 27 criado como canonical draft documental, released_with_required_external_audit.**

Proximo passo: Claude/Metacognik read-only audit of Doc 27, then PMO fan-in before any target-doc patch candidates.

## 28.7 Light patch LP-1/LP-2

**Data:** 2026-06-01

**Sessao:** `S-P1-27-CODEX-20260601-002`

**Checkout lock:** `LOCK-P1-27-CODEX-20260601-002`

**Escopo:** patch leve de traceabilidade; sem alteracao de conteudo das secoes 1-23 do Doc 27.

**Patches aplicados:**

| Patch | Correcao documental | Status |
|---|---|---|
| LP-1 | Reconciliou a data de criacao e IDs de Doc 27 de 2026-06-02 para 2026-06-01 em Doc 27, SESSION_REGISTRY e ARCHITECTURE_PATCH_REPORT, alinhando com a data real do ambiente e da auditoria PMO. | aplicado |
| LP-2 | Adicionou a cadeia de gate da Nota 24/Layer 13/Layer 14/cleanup/PMO fan-in no `ARCHITECTURE_PATCH_REPORT.md` section 28. | aplicado |

**Confirmacoes de escopo:**

- Doc 27 sections 1-23 nao foram reescritas.
- LP-3 permanece nao aplicado, aguardando avaliacao Metacognik se necessario.
- Docs 01-26 nao foram alterados.
- Docs 28-34 nao foram criados.
- Study Layer 13 e Study Layer 14 nao foram alteradas.
- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md` e `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md` nao foram alterados por este patch leve.
- Nenhum backend, UI, API, database, migration, MCP server real, webhook real, JSON n8n, agente real ou automacao runtime foi criado.

## 28.8 Formal sign-off recording

**Data:** 2026-06-01

**Sessao:** `S-P1-27-CODEX-20260601-003`

**Checkout lock:** `LOCK-P1-27-CODEX-20260601-003`

**Checkout release:** `REL-P1-27-CODEX-20260601-003`

**Trigger:** Founder/PMO formal sign-off and Metacognik final sign-off for Doc 27.

**Veredito registrado:** `SIGN_OFF_APPROVED`.

**Mudancas aplicadas:**

- Doc 27 YAML updated from `status: draft` to `status: approved`.
- Doc 27 `provenance_status` updated to `approved_after_external_audit`.
- Doc 27 `confidence` updated to `high`.
- Doc 27 received a short `Formal Sign-Off` section.
- LP-3 recorded as `DISPENSABLE_NOT_REQUIRED` and not applied.

**Confirmacoes de escopo:**

- Approval is documentary only.
- No Docs 10/11/12/13/24 target patch was applied.
- Docs 10/11/12/13/24 remain deferred for future separate checkouts.
- Docs 01-26 except Doc 27 were not altered.
- Docs 28-34 were not created.
- Study Layer 13 and Study Layer 14 were not altered.
- `00_SYSTEM_GOVERNANCE/*` and CKOS auxiliary maps were not altered.
- No implementation, backend, UI, schema, API, migration, MCP server real, webhook, JSON n8n, real agent, runtime automation, slash-command runtime or autonomous dispatch runtime was authorized or created.

**Status:** Doc 27 formally approved as canonical documentary architecture.

---

# 29. Doc 28 Notes/RAG/Knowledge Architecture Creation — 2026-06-02

**Session ID:** `S-P1-GATE3-CODEX-20260602-001`

**Task ID:** `GATE3_DOC28_NOTES_RAG_KNOWLEDGE_CREATION`

**Checkout lock:** `LOCK-P1-GATE3-CODEX-20260602-001`

**Checkout release:** `REL-P1-GATE3-CODEX-20260602-001`

**Trigger:** GATE 1 was marked complete in `000_ROADMAPS/22_CONSOLIDATION/CKOS_EXPANSION_KANBAN.md` with audit sessions `S-P1-GATE1-CLAUDE-20260601-001` and `S-P1-GATE1-CLAUDE-20260602-002`; Codex session `S-P1-GATE1-CODEX-20260602-001` had already applied patches A+B+C and registered release.

**Escopo:** canonical_patch documental; sem backend, UI, API, database migration, runtime worker, vector store real, real agents, MCP server, webhook, JSON n8n ou automacao runtime.

## 29.1 Arquivo criado

- `07_EVOLUTION_SYSTEM/28_NOTES_RAG_AND_KNOWLEDGE_ARCHITECTURE.md`

## 29.2 Arquivos alterados

- `000_ROADMAPS/SESSION_REGISTRY.md`
- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md`
- `ARCHITECTURE_PATCH_REPORT.md`

## 29.3 Conteudo canonico criado

Doc 28 define arquitetura documental para:

- notas como objetos CKOS;
- tipos de knowledge assets;
- pipeline de ingestao upload/import -> parse -> classify -> chunk -> embed -> index -> link -> audit;
- namespace e isolamento de tenant como precondicao;
- estrategia de embedding textual, multimodal, Creative DNA, evidence, memory e visual assets;
- chunking policy;
- RAG query policy;
- retrieval quality scoring;
- cost policy para ingestao, embedding/re-embedding e retrieval;
- conexao com nodes, evidence_items, memories, DNA, artifacts e Work Orders;
- security/testing/failure modes;
- MVP P0 scope;
- patches sugeridos ao Doc 11;
- `ARCHITECTURE_QUESTIONS` abertas.

## 29.4 Dependencias e limites

- Doc 05 remains the owner of memory layers, RAG-as-context policy and context packet assembly.
- Doc 18 remains the owner of research collection, source scoring and Evidence Object Model.
- Doc 11 remains the owner of real database schema; Doc 28 only suggests future patches.
- Doc 12 remains the owner of RLS, PII and vector namespace security policy.
- Doc 13 remains the owner of eval/cost observability thresholds and quality gates.
- Doc 26 remains the owner of connectors, MCP, webhooks, providers and external tool access.
- Doc 27 remains the owner of Work Orders, task orchestration and multi-session/fan-in governance.

## 29.5 Confirmacoes de escopo

- Docs 01-27 were not edited for content by this session.
- Doc 11 was not patched; all schema items remain textual suggestions inside Doc 28.
- Study Layer 13 and DNA/RAG study files were read only.
- No docs 29-34 were created.
- No product/backend/UI/API/runtime/migration files were touched.
- No de-numbering, move, delete or rename operation was executed.

## 29.6 Status

**Doc 28 created as canonical draft documentary architecture, released_with_required_external_audit.**

Next step: Fan-in Claude: confirmar integridade do Doc 28 e declarar GATE 3 ✅.
