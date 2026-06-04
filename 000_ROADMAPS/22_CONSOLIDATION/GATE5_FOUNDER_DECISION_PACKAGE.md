---
title: GATE 5 — Pacote de Decisão do Founder
file: GATE5_FOUNDER_DECISION_PACKAGE.md
phase: 000_ROADMAPS
category: gate_decision
status: awaiting_founder_decision
owner: pmo_ckos
created_at: 2026-06-02
session_id: S-P1-GATE5PKG-CLAUDE-20260602-006
decides: GATE 5 (abre F1 / runtime)
base_file: 03_BACKEND_MVP_THIN_SLICE_PLAN.md
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
- **AQ-IO-1** — **o slice começa no `user` ou no `project`?** Define se o S1 (intent ingress) carrega contexto de usuário (identidade + memória `user_id`/DNA — ver `22_CONSOLIDATION/F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md`) ou só `project`. É a tese *user-first*; **molda a forma do slice e o que o S1 ingere**. Origem: reconciliação User-in/Response-out + fan-in audit da Onda 1. → *Founder + PMO*
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

- [ ] **GO** — autorizo F1; responderei as 3 AQs de início antes do Sprint 1.
- [ ] **GO parcial** — autorizo só o Sprint 1 (event ingress + event log) e reavalio.
- [ ] **NO-GO** — segurar; motivo: __________.

> Lembrete: nenhuma ferramenta de IA declara gate aprovado. Esta decisão é sua, registrada com data no SESSION_REGISTRY.
