---
title: 02_RESEARCH_SYNTHESIS Memory
file: ck_memory.md
layer: study
phase: 000_STUDY_NOTES
category: research_synthesis_memory
status: active
version: 0.1.0
owner: pmo_ckos
responsible_agent: claude_opus_4_7
reviewers:
  - pmo_ckos
  - metacognik
  - founder
approval_required:
  - founder
  - pmo_ckos
confidence: unverified
provenance_status: unverified
source_tool: claude_code
created_at: 2026-06-09
purpose: >
  Memória ativa da pasta 02_RESEARCH_SYNTHESIS — registra triagem PMO das 8 deep researches
  e do SYSTEM_RESPONSE.md adicionados em 2026-06-09 sobre User System / Smart Questions /
  Smart Responses; não concede autoridade canônica nem de implementação.
inputs:
  - README.md
  - SYSTEM_RESPONSE.md
  - deep-research-report (5..12).md
  - 000_ROADMAPS/22_CONSOLIDATION/F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md
  - 000_ROADMAPS/22_CONSOLIDATION/GATE5_FOUNDER_DECISION_PACKAGE.md
  - 000_ROADMAPS/22_CONSOLIDATION/03_BACKEND_MVP_THIN_SLICE_PLAN.md
outputs:
  - triagem PMO das 8 DRs vs canônico
  - confirmação de AQ-IO-1 (user-first) como decisão central do GATE 5
  - sinalização de itens NÃO-promover (fragmentação)
tags: [research-synthesis, memory, pmo, user-system, response-engine, gate-5, aq-io-1]
related_notes:
  - 000_ROADMAPS/22_CONSOLIDATION/F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md
  - 000_ROADMAPS/22_CONSOLIDATION/GATE5_FOUNDER_DECISION_PACKAGE.md
  - 000_ROADMAPS/22_CONSOLIDATION/03_BACKEND_MVP_THIN_SLICE_PLAN.md
  - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
---

# Memória — 02_RESEARCH_SYNTHESIS

## 1. Contexto (2026-06-09)

Founder solicitou estudo do **User System / Smart Questions+Responses** como possível primeiro sistema antes do backend F1. Subiu na pasta:

1. `SYSTEM_RESPONSE.md` — Smart Response Engine proposal (25 seções: arquitetura, response object, response contract V1, anti-padrões, integração com Work Orders, roadmap em 9 sprints, recomendação crítica).
2. 8 deep researches (5..12) — substrato externo para sustentar a proposta.

Pergunta do Founder em uma linha: *"devemos começar pelo user system?"*

## 2. Verdict PMO em uma linha

**Não como sistema separado. SIM como o front do F1.** A pergunta já foi respondida estruturalmente em 2026-06-04 pelo `F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md` (~75% canônico, 10 itens net-new cirúrgicos). As 8 novas DRs **reforçam** os 4 mais fortes (U1, U2, R1, R2) mas **não criam um sistema novo** nem mudam o veredito. Caminho crítico = decidir GATE 5 com AQ-IO-1 = `user`, e o F1-Sprint-1 carrega `user_id` + 1ª intenção desde o ingress.

## 3. Sinal vs ruído nas 8 DRs (mapa para o canônico)

| DR | Tema | O que reforça | Casa canônica | Net-new? |
|---|---|---|---|---|
| **5** | Qualidade de resposta LLM | R1 (`response_type` + `depth_level`), R2 (anti-padrões: over-explain/over-ask/fake-certainty), R5 (User vs Audit Mode), métricas (precisão, completude, follow-up rate) | Doc 03 §5.5 (Agent Run) + Doc 04 (comportamento) + Doc 13 (evals) | reforça os 3 itens R1/R2/R5 já em F1 candidate |
| **6** | Aprendizado progressivo + memória | U2 (memória escopada `user_id`), U3 (declarado→observado→inferido→validado com confidence), differential privacy, federated learning | Doc 05 §5.1/5.6 + Doc 12 (privacy) | reforça U2/U3 |
| **7** | Interfaces adaptativas / glass | princípio "visual responde a estado, não é tema" | **F4** (Docs 14/15/16) | **NÃO entra agora** — Princípio #1 (doc→runtime→UI); construir agora = "Notion bonito com IA" |
| **8** | Threat model agêntico (OWASP) | já canônico em Doc 12 §13 (14 security events com P0-P3 + SLA) | Doc 12 | confirma — **0 net-new estrutural** |
| **9** | Governança runtime (NIST/OPA/AI Act) | OPA pattern (decisão ≠ enforcement), two-phase approval, SCITT/attestation | Doc 10 (engines) + Doc 04 (autonomy) + Doc 12 (policies) | reforça padrão; possível enriquecimento Doc 13 sobre attestation |
| **10** | Smart Questions Engine | R3 (gate de lacuna em 3 níveis: leve→hipótese / média→responde+sinaliza / crítica→pergunta-antes), EVIG, ask-vs-assume, traceability question→slot→KPI | Doc 03 Question Engine + F1-S2 | reforça R3 |
| **11** | Observabilidade / tracing | `trace_id` (W3C Trace Context) + `run_id` (UUIDv7) + `idempotency_key` + OpenTelemetry GenAI semconv | Doc 13 + Doc 03 §5.5 (já tem trace_id/idempotency_key após PATCH 1) | confirma — pode citar OpenTelemetry como standard |
| **12** | Agent OS 2026 (panorama) | validação arquitetural: diferencial CKOS = memory de marca + evidence graph + policies adaptativas + skill packs + evals identity-aligned + multi-tenancy. Commodity = scheduler/queue/vector/chat embed (não reinventar) | sem doc específico — princípio de prioridade | influencia GATE 5 AQ-G5-02 (job runner: usar pg-boss/Supabase Queues, não Temporal próprio) e AQ-G5-05 (model gateway: **OpenRouter único** para Claude 4.7 Opus + GPT-5.5; fallback mútuo via o mesmo gateway, não separados — confirmado Founder 2026-06-09) |

### O que NÃO promover (recusado por PMO desde Jun 4 + confirmado Jun 9)

- **`/CKOS_USER_SYSTEM/` 13 subpastas + SQL** → refabrica fragmentação 1:35 que F0 existe para colapsar
- **Smart Response Engine como sistema separado / docs 01-07** → é enriquecimento do Agent Run (Doc 03 §5.5) + Doc 10 §5.2, não sistema novo
- **Cognitive Atmosphere / Glass System / wallpaper / widgets** → F4 (Docs 14/15/16); registrar apenas o princípio agora
- **Banco de 100 smart questions** → prematuro; 7-12 amarradas a F1-S1/S2 bastam para o thin-slice
- **Schemas SQL (`user_profiles`, `response_objects`, `user_memory_events`...)** → Doc 11, gated pós-GATE 5

## 4. AQ-IO-1: a decisão central para o Founder

Pergunta canônica do `GATE5_FOUNDER_DECISION_PACKAGE.md` (grupo 🔴 trava-início):

> O thin-slice do MVP (arquivo 03) começa em **`user identity + 1ª intenção`** ou em **`project`**?

**Recomendação PMO (claude_opus_4_7 — Jun 9):** responder **`user`**.

Sustentação cruzada:
- DR 6 (memória escopada `user_id` é a peça que falta no Doc 05 — gap real)
- DR 12 (memória de marca/usuário = diferencial competitivo; chat/queue/vector = commodity)
- SYSTEM_RESPONSE §25 (Founder próprio: *"perguntar melhor → responder melhor → executar melhor → medir melhor → aprender melhor"* — a espinha começa no usuário)
- F1 candidate §0 (Jun 4): "U1 + U2 são os net-new mais fortes (ALTA)"
- Princípio #5 (anti-1:35): nomear o que falta no canônico (User como objeto vivo, memória `user_id`), **não** criar sistema novo

Impacto operacional ao responder `user`:
- F1-S1 (Intent Ingress) carrega `IntentReceived{user_id, intent_text, context_ref?}` em vez de só `{project_id, intent_text}`
- F1-S2 (Question Engine) usa o User Operating DNA (U1) + memória escopada (U2) como contexto para reduzir ask-rate
- Sequencia uma **única** sessão `canonical_patch` pós-GATE 5 aplicando U1/U2/U3 em Doc 02/05 e R1/R2/R3 em Doc 03/04, antes do código

## 5. Ordem de operações recomendada (PMO)

1. **Agora (sem código novo):** Founder decide GATE 5 (GO / GO parcial / NO-GO) + responde AQ-IO-1 (recomendação: `user`) + 3 AQs técnicas trava-início (AQ-G5-02 job runner, AQ-G5-05 model gateway, AQ-G5-09 secret store). A consolidação L3 Wave 2 (Data Models / Tools) pode rodar em paralelo.
2. **Após GO:** uma única sessão `canonical_patch` aplica U1/U2/U3 + R1/R2/R3 em Doc 02/03/04/05/10 (escopo cirúrgico, ~10 net-new fields/policies, GATE-5-gated, separação de papéis Founder + Metacognik).
3. **F1-Sprint-1 começa:** S1 (Intent Ingress carregando `user_id`) + S4 (Event Log) — backend puro, sem UI.
4. **Defer F4:** Cognitive Atmosphere / glass / wallpaper só após Sprint 6 (memória + ROI provados).

## 6. Riscos se ignorar essa orientação

| Risco | Probabilidade | Impacto |
|---|---|---|
| Criar `/CKOS_USER_SYSTEM/` como sistema separado | alta se PMO não bloquear | **P1** — fragmentação 1:35 volta; F0 perde sentido |
| Construir Cognitive Atmosphere / glass antes do runtime | média | **P1** — "Notion bonito com IA" (risco que o próprio Founder alertou na pergunta original) |
| Aplicar User-in patches antes do GATE 5 | média | **P1** — over-engineering antes de saber o que o thin-slice exige (mesmo erro do Doc 11 RAG schema) |
| Tratar Smart Response Engine como sistema novo (docs 01-07) | alta se interpretado literal | **P1** — duplica Doc 10 §5.2 inteiro (75% já é canônico) |

## 7. Owner / próximo audit

- **Sessão ativa:** `S-USER-PMO-CLAUDE-20260609-001` (read-only sobre as 8 DRs + SYSTEM_RESPONSE; produz síntese aqui, não toca canônico).
- **Próximo audit:** Metacognik ao virar o patch candidate de aplicação User-in + Response-out (pós-GATE 5).
- **Decisão pendente do Founder:** GATE 5 (go/no-go) + AQ-IO-1 + 3 AQs técnicas.

## 8. Confidence

- **Verdict estrutural:** confidence **alta** (cruza F1 candidate Jun 4 + 8 DRs + SYSTEM_RESPONSE + canônico atual).
- **Recomendação `user` em AQ-IO-1:** confidence **alta** — mas é decisão do Founder, não do PMO. PMO entrega base, Founder vira a chave.
- **Pesquisas brutas:** confidence **unverified** — citations nas DRs ainda não foram validadas independentemente.
