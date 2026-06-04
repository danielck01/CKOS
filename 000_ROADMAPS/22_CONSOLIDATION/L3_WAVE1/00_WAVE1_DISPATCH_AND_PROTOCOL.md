---
title: L3 Wave 1 — Dispatch & Comms Protocol (Skills · Transformers · Policies)
file: 00_WAVE1_DISPATCH_AND_PROTOCOL.md
layer: auxiliary
doc_type: pmo_dispatch
phase: 000_ROADMAPS
category: consolidation
status: awaiting_founder_batch_approval
version: 0.1.0
created_at: 2026-06-04
owner: pmo_ckos
responsible_agent: claude_opus_4_8
dispatcher_session: S-P1-L3DISPATCH-CLAUDE-20260604-001
companion_of: 04_CONSOLIDATION_EXECUTION_PLAN.md
governed_by:
  - 01_MULTI_SESSION_CONTROL_ROOM_RUNBOOK.md
  - ../MULTI_SESSION_EXECUTION_POLICY.md
  - ../SESSION_REGISTRY.md
non_authority_boundary: >
  Nota de dispatch auxiliar. Stage 0 = markdown + disciplina, SEM backend/queue/webhook.
  Esta nota PROPÕE prompts e entradas de registry; não as aplica e não concede autoridade.
  Autoridade de escrita vem do lock ativo + aprovação Founder do LOTE. Nenhuma sessão aqui
  edita canônico 01-28, cria docs 29-34, toca governance/patch report, ou implementa.
tags: [dispatch, multi-session, wave, l3, consolidation, bra, pmo]
---

# L3 — Onda 1 (Dispatch + Protocolo de Comunicação)

> **Objetivo:** tirar a carga de "só esta sessão trabalha". **5 sessões em paralelo** — 3 escritores
> (Codex #1, Codex #2, Windsurf) sobre 3 tracks disjuntos + 2 Claude coordenando: **#1 Dispatcher**
> (gera prompts, fan-in) e **#2 Auditor** (ordena × audita pro Founder). **Trabalho 100% F0 (consolidação),
> zero GATE-5-blocked** — roda em paralelo COM a decisão do GATE 5.
> **Modo:** Stage 0 do Runbook (§2). Esta nota é o que o Dispatcher (Slot 1) produz.

---

## 0. O que VOCÊ aprova (1 contato — Runbook §3/§7)

Você não roteia. Você aprova **o lote** uma vez. Template:

```txt
LOTE L3-W1 APROVADO — 2026-06-04
Sessões (5): Claude#1 Dispatcher · Claude#2 Auditor(ordena×audita pro Founder)
            · Codex#1 TR-SKILLS · Codex#2 TR-TRANSF · Windsurf TR-POLICY
Teto de risco: baixo
Modos: patch_candidate (escritores) + audit (Claude#2) — PROPÕE, não aplica em canônico
Proibido: canônico 01-28, docs 29-34, governance, patch report, SQL, UI, backend, move/rename/delete
Reviewers no fan-in: Claude#2 (auditor) + Metacognik → Founder
Expira: 2026-06-07
```

Aprovou → eu gero os 3 prompts prontos pra colar (a nota-sessão de cada um). Cada sessão roda sozinha e devolve um **BRA Packet** + `CHECKOUT RELEASE`. Você só reaparece no fan-in.

---

## 1. As 5 sessões da Onda (2 Claude + 2 Codex + 1 Windsurf)

**Roster — staffar TODOS os slots do Runbook §1, não só os escritores:**

| Sessão | Nota | Papel | Produz | Mode |
|---|---|---|---|---|
| **Claude #1** (esta) | `S-CLAUDE1_DISPATCHER.md` | **Dispatcher** — gera os prompts, fan-in mecânico, atualiza registry/Kanban | prompts + esta nota | planning |
| **Claude #2** | `S-CLAUDE2_AUDITOR.md` | **Auditor — ordena × audita pro Founder** — lê os 3 candidates, ordena A-PROMOVER por severidade, checa canonical-readiness, agrega as ARCHITECTURE_QUESTIONS → pacote de decisão | `WAVE1_FANIN_AUDIT_FOR_FOUNDER.md` (findings, sem patch) | audit |
| **Codex #1** | `S-CODEX1_TR-SKILLS_TASK.md` | Escritor TR-SKILLS | `DOC06_SKILLS_RECONCILIATION_CANDIDATE.md` | patch_candidate |
| **Codex #2** | `S-CODEX2_TR-TRANSF_TASK.md` | Escritor TR-TRANSF | `DOC09_TRANSFORMERS_RECONCILIATION_CANDIDATE.md` | patch_candidate |
| **Windsurf** | `S-WINDSURF_TR-POLICY_TASK.md` | Escritor TR-POLICY (inventário+rascunho; julgamento final no fan-in) | `DOC12_POLICIES_RECONCILIATION_CANDIDATE.md` | patch_candidate |

**Os 3 tracks de escrita (disjuntos — um arquivo, um escritor):**

| Track | Surface | Lê (fonte, RO) | Compara com (canônico, RO) | Escreve (output único) |
|---|---|---|---|---|
| **TR-SKILLS** | Codex #1 | `000_UPGRADE/04_SKILLS_REGISTRY/` (15) | `02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md` | `L3_WAVE1/DOC06_SKILLS_RECONCILIATION_CANDIDATE.md` |
| **TR-TRANSF** | Codex #2 | `000_UPGRADE/08_TRANSFORMERS/` (11) | `02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md` | `L3_WAVE1/DOC09_TRANSFORMERS_RECONCILIATION_CANDIDATE.md` |
| **TR-POLICY** | Windsurf | `000_UPGRADE/07_POLICIES/` (11) | `03_RUNTIME_SYSTEM/12_...DATA_GOVERNANCE.md` (+ `04_AUTONOMY_AND_APPROVALS.md`) | `L3_WAVE1/DOC12_POLICIES_RECONCILIATION_CANDIDATE.md` |

**Separação de papéis (Runbook §1, "um escreve, outro audita"):** Codex/Windsurf **escrevem** · Claude #1 **despacha** · Claude #2 **ordena × audita pro Founder** · você **decide**. Folders-fonte, docs-alvo e outputs todos distintos = **zero overlap de escrita** (§4). Tudo F0 consolidação, nenhum track mexe em runtime/GATE 5.

> **Capacidade:** Codex roda **2 sessões simultâneas** (Codex#1 ≠ Codex#2, locks disjuntos — Runbook §1/§4). Claude roda Dispatcher + Auditor em paralelo (um gera, outro audita). 5 sessões ativas sem colisão.

---

## 1b. Manual de operação (caps · planner · inteligência · confiança)

**Contato do Founder = mínimo:** aprova/reprova + libera lotes de até **10 tarefas**. Sessões puxam do lote até seu cap; ao dar `release`, puxam a próxima. Você só reaparece quando o lote esvazia, ou há gate/risco acima do teto.

**Máximo de tarefas por sessão (anti-degradação):**

| Sessão | Cap concorrente | Por quê |
|---|---|---|
| Claude #1 Dispatcher | 1 lote por vez | orquestra, não executa track |
| Claude #2 Auditor | 1 onda por vez (até os N candidates) | precisa consolidar tudo junto |
| Codex #1 / #2 | **1 arquivo/track por vez** | Codex degrada com contexto amplo (Runbook §1a) |
| Windsurf | **1 tarefa mecânica por vez** | modelo grátis, baixa confiança |

**Modo Planner — quando LIGAR:**
- LIGA: tarefa aberta/arquitetural/multi-step, escopo ambíguo, sequenciar onda, consolidar/ordenar.
- DESLIGA (execution): scope contract fechado, 1 arquivo, tarefa mecânica — o prompt já **é** o plano.
- Por sessão: **Claude#2 Auditor = ON** · **Dispatcher = ON** só ao montar onda nova · **Codex#1/#2 = OFF** (execution; liga só se achar conflito de arquitetura grande → vira AQ) · **Windsurf = OFF**.

**Nível de inteligência — quando MUDAR:**
- SOBE (high/highest): julgamento, arquitetura, risco, conflito, canonical-readiness, ordenar pro Founder.
- BAIXA (medium): inventário mecânico, detecção de boilerplate, listagem (cost control — Model Router, Doc 10).
- Por sessão: **Claude#2 = highest** · **Codex#1/#2 = high** · **Dispatcher = high** (medium no fan-in mecânico) · **Windsurf = medium**.

**Confiança Windsurf (modelo grátis):** todo output do Windsurf é **hipótese de baixa confiança**. Claude#2 **re-verifica cada item contra a fonte** antes de qualquer promoção. Nada do Windsurf entra no fan-in final sem re-verificação. Não dar a ele decisão de mérito.

---

**Fora da Onda 1 (não despachar agora):** TR-DATAMODELS (`11_DATA_MODELS` vs Doc 11) e TR-CORERUNTIME (`01_CORE_RUNTIME` vs Doc 10) são **GATE-5-atados** (schema/runtime) → esperam o GATE 5. Tools/Connectors (`05`+`06` vs Doc 26, 29 arq) entra na Onda 2.

---

## 2. Padrão de prompt CKOS (preâmbulo obrigatório — Runbook §5)

Toda nota-sessão abre com este guardrail, **sem exceção**:

```txt
You are a CKOS session under MULTI_SESSION_EXECUTION_POLICY.
- Fonte de verdade aprovada = canônico 01-28; docs 29-34 gated.
- NÃO edite canônico 01-28 nem crie docs 29-34 sem checkout/gate explícito.
- NÃO atualize ARCHITECTURE_PATCH_REPORT.md nem 00_SYSTEM_GOVERNANCE/*.
- NÃO crie backend, UI, API, migrations, n8n JSONs, agentes runtime, automações, SQL real.
- patch_candidate = só o arquivo-candidate permitido + CHECKOUT RELEASE. PROPÕE, não aplica.
- Study/UPGRADE = read-only (fonte de comparação). Não mover/renomear/deletar nada.
- Study recomenda, nunca governa. Roadmap sequencia, nunca substitui canônico.
```

Depois do preâmbulo vem o bloco scoped (template 5a do Runbook) — ver cada nota-sessão.

**Padrão de saída = o candidate do Doc 03** (`DOC03_AGENTS_RECONCILIATION_CANDIDATE.md`): §0 Veredito · §1 Método · §2 Inventário comparativo · §3 A PROMOVER (IDs + alvo + força) · §4 JÁ COBERTO · §5 CONFLITOS→ARCHITECTURE_QUESTIONS · §6 Risco P1. **Espelhar essa estrutura.**

---

## 3. Comunicação: BRA + Q&A bidirecional

**BRA = Briefing Relay Architecture** (study 21): pacote estruturado que uma sessão emite para falar com as outras/PMO **sem relay manual**. Campos do BRA Packet:

```yaml
bra_id:            # BRA-<TRACK>-<data>-<seq>
from_session:      # ex.: S-P1-L3-CODEX1-20260604-001
to:                # PMO/Dispatcher | Founder | outra sessão
context_summary:   # 3-5 linhas do que foi feito
outputs:           # arquivos/seções produzidos
open_questions:    # perguntas que ESTA sessão devolve (ver §3b)
blockers:          # o que trava (lock, dado faltante, decisão Founder)
risk_flags:        # risco/custo/cross-tenant/secret
recommended_next:  # próximo passo sugerido
```

### 3a. Perguntas que EU (PMO) faço a cada sessão
Vão dentro de cada nota-sessão, seção **"PERGUNTAS DO PMO →"**. São o guard-rail de raciocínio (evitam inventário raso). Ex.: *"o item da UPGRADE é template-boilerplate ou conteúdo real? prove com diff."*

### 3b. Perguntas que a sessão me devolve
Cada sessão preenche a seção **"← PERGUNTAS PARA O PMO (BRA)"** da própria nota + lista em `open_questions` do BRA. Regra: **conflito de arquitetura não se resolve na sessão** — vira `ARCHITECTURE_QUESTION` e sobe pro fan-in (como as 4 AQs do Doc 03). A sessão **não espera resposta item-a-item**; ela registra a pergunta, segue com hipótese marcada, e o fan-in resolve.

### 3c. Onde isto vive
Estado compartilhado = `SESSION_REGISTRY.md` + a nota-sessão de cada track (dentro de `L3_WAVE1/`). "Se não está no registry, não aconteceu" (Runbook §2).

---

## 4. Fan-in + "SESSÃO FINALIZADA" (Runbook §2a/§8)

```txt
Sessão executa → cola CHECKOUT RELEASE + BRA aqui → Claude faz fan-in → próximo passo
```

Uma sessão só conta como **FINALIZADA** com: `CHECKOUT RELEASE` emitido + registry atualizado + lock liberado + `next_step` + status. O Dispatcher **não** gera passo dependente antes disso. Fan-in consolida as 3 → uma lista única de A PROMOVER + as ARCHITECTURE_QUESTIONS agregadas → vai pro Founder.

---

## 5. Entradas de SESSION_REGISTRY propostas (NÃO aplicadas — Runbook §5c)

> O Dispatcher propõe; aplica quando o lote for aprovado e cada sessão pegar seu lock.

```txt
S-P1-L3DISPATCH-CLAUDE-20260604-001 | DISPATCHER | planning        | claude_1 | scope: read registry + 3 outputs; write L3_WAVE1/ prompts + Kanban + registry | active (esta sessão, já registrada)
S-P1-L3-CLAUDE2-20260604-001 | AUDITOR    | audit           | claude_2 | scope: read os 3 candidates + Doc 06/09/12/04 (RO); write L3_WAVE1/WAVE1_FANIN_AUDIT_FOR_FOUNDER.md + registry | planned (depende dos 3 releases)
S-P1-L3-CODEX1-20260604-001  | TR-SKILLS  | patch_candidate | codex_1  | scope: read 04_SKILLS_REGISTRY + Doc 06 (RO); write L3_WAVE1/DOC06_SKILLS_RECONCILIATION_CANDIDATE.md + registry | planned
S-P1-L3-CODEX2-20260604-001  | TR-TRANSF  | patch_candidate | codex_2  | scope: read 08_TRANSFORMERS + Doc 09 (RO); write L3_WAVE1/DOC09_TRANSFORMERS_RECONCILIATION_CANDIDATE.md + registry | planned
S-P1-L3-WINDSURF-20260604-001| TR-POLICY  | patch_candidate | windsurf | scope: read 07_POLICIES + Doc 12 + Doc 04 (RO); write L3_WAVE1/DOC12_POLICIES_RECONCILIATION_CANDIDATE.md + registry | planned
```

Cada uma com `forbidden`: canônico 01-28, docs 29-34, governance, patch report, SQL/UI/backend, move/rename/delete, arquivo-alvo de outra sessão.

---

## 6. Kanban de relance (espelho — Runbook §9)

```txt
READY (sem lock, aguarda lote)  | TR-SKILLS  Codex#1  | TR-TRANSF Codex#2 | TR-POLICY Windsurf
NOW (ativo, lock)               | —
WAITING (depende)               | TR-DATAMODELS, TR-CORERUNTIME → GATE 5
FOUNDER DECISION                | aprovar LOTE L3-W1 (§0) · GATE 5 (caminho crítico)
DONE (released)                 | DOC03 Agents (candidate, aguarda aprovação)
```

---

## 7. O que NÃO entra (guard-rails da onda)

- **Não** aplicar nada em Doc 06/09/12/04 — é candidate, aplicação é sessão `canonical_patch` pós-aprovação.
- **Não** mover/arquivar os folders UPGRADE (vem depois da aprovação do candidate, como no plano do Doc 03 §6).
- **Não** abrir TR-DATAMODELS / TR-CORERUNTIME (GATE-5-atados).
- **Não** criar SQL, UI, agente real. Stage 0.
