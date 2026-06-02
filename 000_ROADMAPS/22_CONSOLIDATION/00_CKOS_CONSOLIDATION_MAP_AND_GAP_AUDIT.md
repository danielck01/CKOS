---
title: CKOS Consolidation Map and Gap Audit
file: 00_CKOS_CONSOLIDATION_MAP_AND_GAP_AUDIT.md
layer: auxiliary
doc_type: pmo_consolidation
phase: 000_ROADMAPS
category: consolidation
status: draft
version: 0.1.0
created_at: 2026-06-01
updated_at: 2026-06-01
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - founder
  - metacognik
approval_required:
  - founder
  - pmo_ckos
confidence: medium
provenance_status: pmo_survey_unverified
source_tool: claude_opus_4_8
purpose: Colapsar os 5 estados paralelos do CKOS em UMA fonte de verdade (canonico 01-27) e UM backlog unico, separando fumaca de lacuna real antes de qualquer construcao.
intelligence_level: highest
non_authority_boundary: >
  Este documento e auxiliar e study/PMO. Nao e canonico. Nao cria docs 28-34, nao
  altera docs 01-27, nao edita 00_SYSTEM_GOVERNANCE/*, nao move/renomeia/deleta arquivos,
  nao autoriza backend, UI, API, migrations, agentes reais ou automacoes runtime. Toda
  promocao, arquivamento ou renumeracao exige patch plan + aprovacao Founder.
tags: [consolidation, gap-audit, source-of-truth, pmo, backlog]
---

# CKOS — Mapa de Consolidação + Auditoria de Gaps

> **PMO, 2026-06-01.** Resposta ao diagnóstico: o CKOS não tem déficit de documentação,
> tem **fragmentação** (5 estados paralelos) e **gargalo de ativação** (relay manual).
> Este documento estabelece **uma fonte de verdade** e classifica todo o resto.

> **Reconciliação 2026-06-02:** este mapa foi escrito em 2026-06-01 declarando o canônico como **01-27** (estado do GATE 0). Desde então o **Doc 28 foi criado via GATE 3** e o canônico vivo passou a **01-28** (ver `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`). As referências "01-27" nas §8/§9 (GATE 0) permanecem como **registro histórico** do que o GATE 0 declarou — não reescrever. Ações derivadas agora abrem **doc 29+**, não 28+.

---

## 1. Fronteira de autoridade

Este é um documento de **PMO/planejamento auxiliar**. Ele **recomenda**; não governa, não canoniza, não implementa, não move arquivos. Qualquer ação derivada (promover material, arquivar pasta, renumerar doc, abrir doc 28+) exige **patch plan + gate do Founder**, conforme `MULTI_SESSION_EXECUTION_POLICY.md` e `00_SYSTEM_GOVERNANCE/`.

---

## 2. Inventário: os 5 estados paralelos

| # | Estado | O que é | Papel proposto |
|---|---|---|---|
| **E1** | **Vault canônico `01–27`** (`01_THINKING`…`07_EVOLUTION`) | Arquitetura completa, aprovada/auditada, com YAML e governança. | **FONTE DE VERDADE ÚNICA.** |
| **E2** | **`000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault`** | Build paralelo profundo: skills registry, transformers, prompt-engineering, model-routing, RAG, batch, frontend-prep, roadmap OS. | **MINA DE PROMOÇÃO** — material mais detalhado que o canônico em subsistemas específicos. |
| **E3** | **`000_UPGRADE/`** | Agent civilization, skills/tools registry (OpenRouter/Apify), MVP funcional, Creator Mode, Simulation Runtime, packs de pesquisa. | **MISTO** — parte promove, parte é referência, parte arquiva. |
| **E4** | **`99_RESEARCH_LAB/`** | Padrões técnicos: event-driven, agent runtime, model routing, observability, Supabase, workflow engines, background jobs. | **REFERÊNCIA DE IMPLEMENTAÇÃO** — insumo do backend, não spec de produto. |
| **E5** | **`paperclip_study/` + `000_STUDY_NOTES/14_PAPERCLIP`** | Codebase de referência externa + estudo de tradução para CKOS. | **BENCHMARK** — nunca copiar; só extrair padrões já traduzidos na Layer 14. |

**Regra-mãe da consolidação:** quando E2/E3/E4/E5 divergirem de E1, **E1 vence**. E2–E5 só entram no canônico via patch candidate aprovado.

---

## 3. Estado real do canônico `01–27` (a spec que já existe)

| Doc | Subsistema | Cobre |
|---|---|---|
| 01 | Constitution | princípios AI-first, pipeline intenção→memória→ROI |
| 02 | Object Model | objetos vivos (intent, node, run, evidence…) |
| 03 | Agent Operating Model | Nick, Cognik, Metacognik, PMO, Builder/QA Lead, agents, subagents, skills contratadas |
| 04 | Autonomy & Approvals | níveis de autonomia, approval gates |
| 05 | Memory & Context | memória, RAG, recuperação por nível |
| 06 | **Skills Registry** | skills como capacidade reutilizável (← você achava que faltava) |
| 07 | Workflow Blueprints | workflows estratégicos |
| 08 | Prompt Library | engenharia de prompt |
| 09 | Transformers & Pipelines | briefing→tasks, evidence→dna etc. |
| 10 | Runtime Architecture | ingress, intent resolver, context assembler, policy, workflow engine, run scheduler, agent/model router, approval gate, artifact pipeline, memory loop |
| 11 | Data Model & Persistence | schema, tabelas, Work Order/run/event |
| 12 | Security & Data Governance | permissões, secrets, isolamento |
| 13 | Evals, Observability & Cost | traces, custo, qualidade |
| 14 | **Project Dashboard** | o "Project Pulse" (← você achava que faltava) |
| 15 | Command Center | camada de intenção/aprovação |
| 16 | **Node Canvas** | objetos vivos do runtime (← você achava que faltava) |
| 17 | Implementation Protocol | como construir |
| 18 | Research Protocol | busca proativa / coleta |
| 19 | Claude/Codex/Antigravity Execution | protocolo multi-modelo |
| 20 | QA & Founder Approval | gate de qualidade |
| 21 | Self-Evolving System (Impl) | loop de auto-evolução |
| 21 | ROI Architecture (Business) | ROI operacional ⚠️ **colisão de ordinal** |
| 22 | Feedback System | loop de feedback |
| 23 | Support System | suporte IA-humano |
| 24 | Credits, Plans & Billing | monetização |
| 25 | Self-Evolving Architecture (Evolution) | ⚠️ **conceito duplicado com o 21 de Implementation** |
| 26 | Connectors, MCP & Integrations | OpenRouter, Apify, conectores |
| 27 | **Work Orders & Multi-Session Orchestration** | envelope governado (aprovado 2026-06-01) |

**Conclusão:** a arquitetura de ponta a ponta do seu modelo "Cognitive Runtime MVP" está **inteira no canônico**. O que falta não é desenhar — é (a) limpar defeitos estruturais, (b) puxar profundidade do DNA_SYSTEM, (c) ativar execução.

---

## 4. Matriz de disposição por subsistema

Para cada subsistema: doc canônico (E1) + melhor material paralelo + ação.

| Subsistema | Canônico (E1) | Material paralelo mais profundo | Ação de consolidação |
|---|---|---|---|
| Skills | Doc 06 | `DNA/17_SKILLS_REGISTRY` (skill_object_model, creation_prompt, quality_checklist), `000_UPGRADE/04_SKILLS_REGISTRY` | **Promover** object model + checklist do DNA → patch candidate p/ Doc 06 |
| Transformers | Doc 09 | `DNA/18_TRANSFORMERS` (12 transformers concretos) | **Promover** padrões → patch candidate p/ Doc 09 |
| Prompt Eng. | Doc 08 | `DNA/19_PROMPT_ENGINEERING`, Layer 13 nota 20 | **Promover** grammar de prompt → Doc 08 |
| Model Router | Doc 26 §router / Doc 10 | `DNA/10_REASONING_AND_MODEL_ROUTING`, `99_LAB/08`, `000_UPGRADE/tools/openrouter` | **Promover** tabela reasoning↔modelo → Doc 10/26 |
| Pesquisa proativa | Doc 18, Doc 26 | `DNA/09_RESEARCH`, `000_UPGRADE/research_commander`+`apify_operator`, `tools/apify` | **Promover** Research Commander → patch candidate p/ Doc 18/26 |
| RAG/Knowledge | Doc 05 | `DNA/14_RAG_VECTOR_SYSTEM` (9 notas) | **Promover** → insumo do futuro **Doc 28** |
| Agentes/Civilização | Doc 03 | `000_UPGRADE/03_AGENT_CIVILIZATION` (superagents/agents/io_contract) | **Reconciliar** catálogo → patch candidate p/ Doc 03 |
| Work Orders | Doc 27 ✅ | Layer 13 notas 15/24, Layer 14 | já canônico |
| Runtime/Eventos | Doc 10/11/13 | `99_LAB/01,03,04,10`, `DNA/16_BATCH` | **Referência** p/ backend (não duplica spec) |
| Frontend | Docs 14/15/16 | `DNA/15_FRONTEND_REACT_PREPARATION` (12 contratos UI) | **Reconciliar** contratos → backlog UI (docs 32-33) |
| Multi-sessão | Doc 27 + policy | Layer 13 notas 20-26, `MULTI_SESSION_EXECUTION_POLICY` | já coberto → vira **Runbook** (arquivo 01) |
| Billing/ROI | Docs 21/24 | `ckos_digitalocean_n8n_pack`, `pack_notas` | **Referência** (n8n = acelerador, não core) |

---

## 5. Auditoria de Gaps — fumaça vs lacuna real

### 5a. Defeitos estruturais REAIS no canônico (corrigir antes de construir)

| ID | Defeito | Severidade | Ação |
|---|---|---|---|
| G-01 | **Colisão de ordinal 21**: `05_IMPLEMENTATION/21_SELF_EVOLVING_SYSTEM` vs `06_BUSINESS/21_ROI_ARCHITECTURE` | Alta | Renumerar via patch plan (provável: ROI→21, Self-Evolving move) |
| G-02 | **Self-Evolving duplicado**: `05/21_SELF_EVOLVING_SYSTEM` e `07/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE` | Alta | Decidir doc canônico único; o outro vira pointer |
| G-03 | **Arquivos duplicados**: `18_RESEARCH_PROTOCOL` vs `18_..._FOR_MANUS`; `19_..._EXECUTION` vs `19_..._ANTIGRAVITY_EXECUTION` | Média | Consolidar em 1 cada; arquivar variante |
| G-04 | 5 estados sem índice-mestre que declare E1 como fonte única | Alta | **Este documento** + 1 README de fonte-de-verdade |

### 5b. Lacunas GENUÍNAS (não existem em lugar nenhum)

| ID | Lacuna real | Por que importa |
|---|---|---|
| L-01 | **Doc 28 — Notes/RAG/Knowledge canônico** | RAG só existe no DNA (não-canônico); é o próximo doc |
| L-02 | **Spec de "Skill Selector" em runtime** (o agente que escolhe skills na hora da tarefa) | Conceito existe (Cognik contrata skill) mas sem contrato de seleção/ranking executável |
| L-03 | **Loop "pedir/receber skill" (learning mode)** ligado ao Self-Evolving | Mencionado, nunca especificado como fluxo |
| L-04 | **Backlog único executável** (hoje há 5 roadmaps/kanbans parciais) | Sem isto, cada sessão re-decide prioridade |
| L-05 | **Runbook operacional do Control Room** (método real de rodar 3 Claude+2 Codex+1 Windsurf) | Estudado (nota 26) mas não operacionalizado → **arquivo 01** |

### 5c. FALSAS lacunas (você acha que falta, mas já existe)

| Você achava que faltava | Onde já está |
|---|---|
| Skills / pack de skills | **Doc 06 canônico** + DNA/17 + UPGRADE/04 |
| Cognik / Metacognik aplicados | **Doc 03 canônico** (superagents oficiais) |
| Engenharia de prompt | **Doc 08** + DNA/19 + Layer 13 nota 20 |
| Project Pulse / Command Center / Canvas | **Docs 14, 15, 16 canônicos** |
| Busca OpenRouter/Apify/Perplexity/deep research | **Doc 26** + DNA/09,10 + UPGRADE research_commander |
| Heartbeat | Layer 14 nota 02 + paperclip HEARTBEAT.md (benchmark) |
| Policies | Doc 04 + Doc 12 + MULTI_SESSION_EXECUTION_POLICY |
| Transformers | **Doc 09** + DNA/18 (12 transformers) |
| O MVP de 6 sprints | `000_UPGRADE/13_MVP_FUNCTIONAL/sprints.md` (idêntico) |

**Veredito de gaps:** ~70% do que parecia faltar é fumaça (já documentado, só disperso). A lacuna real é **L-04 (backlog único) + L-01 (Doc 28) + os defeitos estruturais G-01..G-04**. Nenhum deles exige backend para resolver.

---

## 6. Cognik / Metacognik no MVP — decisão

- **Entram no MVP:** Cognik (intenção, hipóteses, contexto = "Cognitive Governor") e Metacognik (auditoria, approval gate). São o mínimo viável: cérebro + consciência.
- **NÃO entram no MVP:** civilização auto-evolutiva de Builder Subagents (Doc 21/25), catálogo de 30 agentes, marketplace/CKStore, learning-mode de skills (L-03).
- **Os 4 agentes do MVP:** Cognik (governa) · PM/Builder (planeja) · Risk (Metacognik audita risco) · ROI (subagent ROI Calculator do Doc 03).

---

## 7. Esqueleto do Backend MVP (thin-slice) — vira arquivo 03 após sua revisão

Slice vertical mínimo (Sprint 1 de `sprints.md`), AI-first de verdade, fonte = canônico:

```txt
1 Intenção entra (Command Center / Doc 15)
  → Cognik resolve intent + gera 1 hipótese + nível de reasoning (Doc 03/10)
  → Metacognik decide se precisa aprovação (Doc 04)
  → 1 Work Order criada (Doc 27)
  → 1 Agent Run executa (Doc 03 §5.5)
  → Evidência anexada + Event Log grava (Doc 10/11/13)
  → Memória atualizada (Doc 05)
  → ROI registrado (Doc 21-ROI)
```
Stack de referência: `99_RESEARCH_LAB` (event-driven, Supabase, agent runtime, observability). **Sem UI complexa.** Model Router via OpenRouter (Doc 26). **Só depois da consolidação aprovada.**

---

## 8. Sequência recomendada (gates)

```txt
GATE 0 (agora)  → Aprovar este mapa: declarar canônico 01-27 = fonte única.
GATE 1          → Patch plan estrutural: corrigir G-01..G-04 (renumeração/dedup).
GATE 2          → Promoção dirigida: subir profundidade do DNA (skills, transformers,
                  model-router, RAG) como patch candidates aos docs 06/08/09/10/26.
GATE 3          → Criar Doc 28 (Notes/RAG/Knowledge) — L-01.
GATE 4          → Ativar Control Room (arquivo 01) como método operacional.
GATE 5          → Backend MVP thin-slice (arquivo 03) — só após GATE 1-2.
```

Arquivar (após GATE 0, via patch plan): roadmaps que dizem "22-24 faltam", prompts de implementação soltos, JSONs n8n como runtime, Manus como infra.

---

## 9. Critérios de aceitação deste documento

- Declara explicitamente **canônico 01-27 como fonte de verdade única**.
- Classifica os 5 estados (promover / reconciliar / referência / arquivar / benchmark).
- Separa fumaça (5c) de lacuna real (5b) e defeito estrutural (5a).
- Não cria doc canônico, não move/renomeia/deleta arquivo, não implementa.
- Permanece subordinado a `MULTI_SESSION_EXECUTION_POLICY.md`, governança e gate do Founder.
- Toda ação de consolidação fica como **proposta gated**, nunca aplicada por este texto.

---

## Próximos artefatos do pacote

- **`01_MULTI_SESSION_CONTROL_ROOM_RUNBOOK.md`** — método operacional (3 Claude + 2 Codex + 1 Windsurf, você fora do caminho crítico). [criado]
- **`02_DNA_SYSTEM_COMPARISON_AND_INTEGRATION_MAP.md`** — GATE 2: comparação dos 2 DNA + integração. [criado]
- **`03_BACKEND_MVP_THIN_SLICE_PLAN.md`** — spec do slice vertical. [após GATE 0-2]
