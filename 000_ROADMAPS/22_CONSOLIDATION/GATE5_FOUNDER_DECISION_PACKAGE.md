---
title: GATE 5 — Pacote de Decisão do Founder
file: GATE5_FOUNDER_DECISION_PACKAGE.md
phase: 000_ROADMAPS
category: gate_decision
status: awaiting_founder_decision
owner: pmo_ckos
created_at: 2026-06-02
updated_at: 2026-06-09
session_id: S-P1-GATE5PKG-CLAUDE-20260602-006
update_session: S-USER-PMO-CLAUDE-20260609-001
decides: GATE 5 (abre F1 / runtime)
base_file: 03_BACKEND_MVP_THIN_SLICE_PLAN.md
related_synthesis:
  - 000_STUDY_NOTES/02_RESEARCH_SYNTHESIS/ck_memory.md
  - 000_ROADMAPS/22_CONSOLIDATION/F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md
---

# GATE 5 — Pacote de Decisão (go / no-go)

> Página única para você decidir sem reler o arquivo 03. Fan-in Claude ✅ 2026-06-02.

## 1. O que você está aprovando (uma frase)

Aprovar o GATE 5 autoriza **iniciar a construção (F1)** do thin-slice de backend do arquivo 03: **uma intenção real percorrendo `intent → run → evento → memória → ROI`, backend puro, sem UI, com rastro auditável.** Nada além disso.

## 2. Dentro vs Fora

| DENTRO do slice | FORA (bloqueado mesmo com GATE 5 aprovado) |
|---|---|
| Event log append-only (fonte de verdade) | UI / frontend / dashboard (gate próprio) |
| 4 agentes: Cognik · PM-Builder · Metacognik-Risk · ROI | Catálogo/civilização de agentes |
| Work Order como envelope (Doc 27) | RAG completo (chunk/embedding internals → Doc 28) |
| RLS/tenant + policy_engine + approval gate desde o S1 | Self-evolving, conectores externos, billing real |
| ROI mínimo (proxies internos) | Docs 29-34 (paralelo, não pré-req) |

## 3. As 10 decisões que precisam de resposta ANTES de codar

Agrupadas por **quando** travam. Você não precisa responder todas hoje — só saber quem decide o quê.

**🔴 Travam o INÍCIO (responder antes do Sprint 1):**
- **AQ-IO-1** — **o slice começa no `user` ou no `project`?** Define se o S1 (intent ingress) carrega contexto de usuário (identidade + memória `user_id`/DNA — ver `22_CONSOLIDATION/F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md`) ou só `project`. É a tese *user-first*; **molda a forma do slice e o que o S1 ingere**. Origem: reconciliação User-in/Response-out + fan-in audit da Onda 1. **Reforço Jun 9:** 8 deep researches + `SYSTEM_RESPONSE.md` sintetizadas em `000_STUDY_NOTES/02_RESEARCH_SYNTHESIS/ck_memory.md` reforçam user-first (DR 6 memória escopada `user_id`; DR 12 memória = diferencial competitivo; SYSTEM_RESPONSE §25 do próprio Founder). **Recomendação PMO: `user`** (ver §7 abaixo). → *Founder + PMO*
- **AQ-G5-02** — job runner do MVP: pg-boss / Supabase Queues / BullMQ / Temporal? → *Technical*
- **AQ-G5-05** — modelo/gateway inicial do `model_router` (OpenRouter é referência, não decisão)? → *Technical*
- **AQ-G5-09** — secret store / como `agent_runs` resolvem tokens via `secret_refs` sem expor? → *Technical + Founder*

**🟠 Travam execução sensível (antes do S3/S5):**
- **AQ-G5-03** — limite de custo/risco para auto-approval no slice? → *Founder + Metacognik*
- **AQ-G5-01 / AQ-G5-04** — Work Orders: tabela física no Doc 11 ou derivados de events/`workflow_runs` no MVP? → *Technical + PMO + Founder*

**🟡 Travam qualidade (antes do S6):**
- **AQ-G5-06** — separação memória curta/média/longa sem promover long memory cedo? → *Metacognik + Technical*
- **AQ-G5-07** — thresholds de evidence coverage / ROI confidence que bloqueiam output? → *Metacognik + QA*
- **AQ-G5-08** — quais patch suggestions do Doc 11 são obrigatórias para F1 (liga ao Doc 11 candidate, prompt 08)? → *PMO + Technical*

## 4. O que a aprovação LIBERA

- **F1 começa** na ordem: S1 event ingress → S4 event log hardening → S2/S3 inteligência+gates → S5 governed run → S6 memória/ROI.
- O **Doc 11 candidate** (prompt 08) passa a fazer sentido rodar — o slice define o schema mínimo real.
- **Codex volta como executor** (Claude arquiteta/revisa), agora com **git** dando rollback.

## 5. Recomendação PMO: **GO condicional**

**GO** para autorizar a F1 — **condicionado a responder as AQs de início** antes do Sprint 1: as 3 técnicas (job runner, modelo, secret store) **+ AQ-IO-1** (arquitetural: o slice começa no `user` ou no `project` — molda o S1). As outras 6 podem ser resolvidas no sprint correspondente.

> **AQ-IO-1 é a sua decisão-âncora:** é a tese *user-first* que você levantou. Responder "user" reordena o S1 (intent carrega identidade + memória `user_id`) e sequencia o PATCH 2 (F1 U/R). Responder "project" mantém o slice do arquivo 03 como está.

| | Risco |
|---|---|
| **Se NÃO aprovar agora** | Continuar acumulando documentação sem nunca validar a tese rodando — o risco nº 1 (ficar rico de docs, pobre de runtime). |
| **Se aprovar sem as 3 AQs** | Começar a codar runtime/secrets no escuro → retrabalho. **Mitigação:** responder as 3 antes do S1. |

## 6. Sua decisão

- [ ] **GO** — autorizo F1; responderei as 4 AQs de início antes do Sprint 1.
- [ ] **GO parcial** — autorizo só o Sprint 1 (event ingress + event log) e reavalio.
- [ ] **NO-GO** — segurar; motivo: __________.

> Lembrete: nenhuma ferramenta de IA declara gate aprovado. Esta decisão é sua, registrada com data no SESSION_REGISTRY.

---

## 7. Respostas recomendadas pelo PMO às 4 AQs trava-início

> Síntese registrada em [`000_STUDY_NOTES/02_RESEARCH_SYNTHESIS/ck_memory.md`](../../000_STUDY_NOTES/02_RESEARCH_SYNTHESIS/ck_memory.md) (sessão `S-USER-PMO-CLAUDE-20260609-001`, claude_opus_4_7). PMO entrega base; **Founder vira a chave**.

### 7.1 AQ-IO-1 · User vs Project como início do slice

| | |
|---|---|
| **Recomendação PMO** | **`user`** — o S1 carrega `user_id` desde o ingress |
| **Confidence** | alta |
| **Sustentação** | DR 6 (memória escopada `user_id`); DR 12 (memória = diferencial competitivo, chat/queue = commodity); SYSTEM_RESPONSE §25 do Founder ("perguntar→responder→executar→medir→aprender" começa no usuário); F1 candidate Jun 4 (PROMOTE-U1/U2 = ALTA) |
| **Impacto operacional** | S1 emite `IntentReceived{user_id, intent_text, ...}`; F1-S2 usa User DNA (U1) + memória `user_id` (U2) para reduzir ask-rate |
| **Sequenciamento** | Uma única sessão `canonical_patch` pós-GATE 5 aplica U1/U2/U3 em Doc 02/05 + R1/R2/R3 em Doc 03/04. Patch candidate a ser pré-montado (sessão separada futura) |

### 7.2 AQ-G5-02 · Job runner

| | |
|---|---|
| **Recomendação PMO** | **pg-boss** (primeira escolha) **ou** Supabase Queues (se decidir ficar 100% no ecossistema Supabase) |
| **Confidence** | média-alta |
| **Sustentação** | DR 12 (scheduler/queue = commodity, não reinventar); pg-boss é Postgres-native (zero infra extra, mesmo DB do event log); Temporal é overkill para thin-slice (mantém em radar para F6 self-evolving) |
| **Trade-off** | pg-boss = mais simples mas single-DB; Temporal = melhor para multi-node e durable workflows mas exige stack adicional |
| **Decisão** | Founder + Technical |

### 7.3 AQ-G5-05 · Modelo / model gateway

| | |
|---|---|
| **Recomendação PMO** | **OpenRouter único como gateway**; modelos primários: **Claude 4.7 Opus + GPT-5.5** com fallback mútuo via o mesmo gateway (não separados em gateways diferentes) |
| **Confidence** | alta |
| **Sustentação** | Doc 10 §5.5 (nota Model Router): CKOS é orquestração, LLM é cognitive engine substituível; DR 12 (model gateway = commodity); decisão Founder Jun 9: gateway único, modelos atuais Claude 4.7 Opus + GPT-5.5 (GPT-4 obsoleto) |
| **Implicação** | `model_registry` (Doc 10) e `model_router` ficam apontando para um único endpoint OpenRouter; substituir modelo = mudança de config, não de arquitetura. `secret_refs` (Doc 11 §12.1) guarda a chave OpenRouter |
| **Decisão** | Technical (config); Founder já fixou o pareamento Claude 4.7 Opus + GPT-5.5 |

### 7.4 AQ-G5-09 · Secret store

| | |
|---|---|
| **Recomendação PMO** | **Supabase Vault** com `secret_refs` (já modelado em Doc 11 §12.1 + Doc 12 §5.15) |
| **Confidence** | alta |
| **Sustentação** | Doc 12 §5.15 (Vault-only para segredos: tokens NUNCA em tabelas normais; só `secret_ref` → vault externo, 6 regras de segurança); Doc 11 §12.1 (`secret_refs` table com `vault_path` sem segredo real); zero infra extra se ficar no Supabase ecosystem |
| **Implicação** | `agent_runs` resolvem `secret_refs` em runtime via Vault, nunca expõem token bruto no log/trace/projection. Cobertura para chave OpenRouter (AQ-G5-05) + futuras chaves de conectores (MCP, Apify, OAuth tokens) |
| **Decisão** | Founder + Technical |

### 7.5 As 6 AQs restantes (não trava-início)

| AQ | Quando trava | Decide |
|---|---|---|
| AQ-G5-01 / AQ-G5-04 (Work Orders físicas no Doc 11 ou derivadas de events?) | antes do S3/S5 | Technical + PMO + Founder |
| AQ-G5-03 (limite de custo/risco para auto-approval) | antes do S3/S5 | Founder + Metacognik |
| AQ-G5-06 (separação memória curta/média/longa) | antes do S6 | Metacognik + Technical |
| AQ-G5-07 (thresholds de evidence coverage / ROI confidence) | antes do S6 | Metacognik + QA |
| AQ-G5-08 (quais patch suggestions do Doc 11 são obrigatórios para F1) | antes do S6 | PMO + Technical |

### 7.6 O que muda no `03_BACKEND_MVP_THIN_SLICE_PLAN.md` ao responder `user` em AQ-IO-1

O arquivo 03 atualmente sequencia: S1 event ingress → S4 event log → S2/S3 → S5 → S6 com `project_id` como contexto principal.

Ao responder `user`, ele passa a:
- S1 emitir `IntentReceived{user_id, intent_text, project_id?, ...}` (project é opcional na 1ª intenção)
- S2 (Question Engine) carregar `User Operating DNA` (U1) + memória `user_id` (U2) como context
- S6 (memória + ROI) escopar tanto `project_id` quanto `user_id`

**Não exige reescrever o arquivo 03.** Exige um **patch leve** (próxima sessão) sequenciando `user_id` antes de `project_id` nos contratos de evento e referenciando o patch candidate U1/U2 do `F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md`.
