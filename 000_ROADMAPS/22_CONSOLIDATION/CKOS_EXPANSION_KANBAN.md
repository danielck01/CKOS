---

kanban-plugin: basic
title: CKOS Expansion Kanban

---

# CKOS Expansion Kanban

> Board estratégico de expansão AI-first. Companion de `CKOS_MASTER_EXPANSION_ROADMAP.md`.
> Lanes = horizonte de tempo. Tags: #F0..#F7 (fase), #FX (governança), #gate, #dna, #agentes, #runtime, #produto, #conectores, #autonomia, #negocio.
> Sincronizado por PMO em 2026-06-02. **GATEs 1/3/4 ✅ (fan-in Claude) | caminho crítico agora: GATE 5 (arquivo 03) → F1.**

## ✅ Concluído

- [x] GATE 0 — Declarar canônico 01-27 como fonte de verdade única #F0 #gate
- [x] GATE 1 — Patch plan estrutural (Patches A+B+C aplicados 2026-06-02) #F0 #gate
- [x] GATE 2 — Comparação dos 2 sistemas DNA + mapa de integração #F0 #gate #dna
  - **Link:** `02_DNA_SYSTEM_COMPARISON_AND_INTEGRATION_MAP.md`
- [x] GATE 3 — Doc 28 Notes/RAG/Knowledge (criado + fan-in Claude ✅ 2026-06-02) #F0 #gate
  - **Link:** `../../07_EVOLUTION_SYSTEM/28_NOTES_RAG_AND_KNOWLEDGE_ARCHITECTURE.md`
- [x] GATE 4 — Control Room Runbook v1.1 (atualizado + fan-in ✅ 2026-06-02) #F0 #gate
  - **Link:** `01_MULTI_SESSION_CONTROL_ROOM_RUNBOOK.md`
- [x] Doc 27 — Work Orders & Multi-Session Orchestration (aprovado) #F0 #runtime
- [x] Mapa de Consolidação + Auditoria de Gaps #F0
  - **Link:** `00_CKOS_CONSOLIDATION_MAP_AND_GAP_AUDIT.md`
- [x] Runbook do Control Room (3 Claude + 2 Codex + 1 Windsurf) #F0 #gate
  - **Link:** `01_MULTI_SESSION_CONTROL_ROOM_RUNBOOK.md`
- [x] Kanban operacional sincronizado #F0
  - **Link:** `../TASK_KANBAN.md`

## 🔵 Agora — F0 Convergência Documental

> **F0 — FOCO REPRIORIZADO (Founder, 2026-06-02):** a convergência agora prioriza **consolidar as 3 camadas** (canônico ↔ study ↔ upgrade) ANTES de construir backend. Sinal:ruído = **1:35** (42 canônico : ~1.450 resto). GATE 5 spec pronta, mas **em espera** até a consolidação reduzir o ruído.
> **F0 contém:** GATEs 0-5 (feitos) + reconciliação + **Consolidação L1-L4** (foco atual) + Doc 11 candidate.
> **Saída da F0:** vault consolidado + GATE 5 decidido. **Fora da F0:** Docs 29-34, Vault Loop, Fan-In recorrente.

- [ ] CONSOLIDAÇÃO das 3 camadas — colapsar fragmentação 1:35 #F0 #FX **[EM EXECUÇÃO — 510 arq reorganizados]**
  - **Plano:** `04_CONSOLIDATION_EXECUTION_PLAN.md` · Decisões D1-D4 ✅
  - **L1 ✅** Miriam (100) → `000_PROJECTS/` (commit 9aae8c3)
  - **L2 ✅** Brain (410) → `000_KNOWLEDGE_BASE/` (commit afc61d0)
  - **L3 (EM CURSO — ANÁLISE, não move):** UPGRADE reconciliação com promoção AGRESSIVA (comparar espelho vs canônico → patch candidate)
    - **L3-Agentes ✅** `DOC03_AGENTS_RECONCILIATION_CANDIDATE.md` (S-009): UPGRADE/03 (65 arq) = scaffold raso; canônico Doc 03 mais rico. A promover: I/O Contract (ALTA) + bundle + 11 nomes net-new (gated em skill, §1). 4 ARCHITECTURE_QUESTIONS (taxonomia commanders vs personas) = entregável central. Aplicação no Doc 03 = P1, sessão separada c/ Founder+Metacognik
    - **L3 restante:** Skills (Doc 06 vs UPGRADE/04+DNA/17), Transformers (Doc 09 vs UPGRADE/08), Data Models (Doc 11 vs UPGRADE/11), Policies (Doc 12 vs UPGRADE/07), Tools/Connectors (Doc 26 vs UPGRADE/05/06)
    - **L3-Onda 1 DESPACHADA (paralela, 5 sessões) 🚀** `L3_WAVE1/` — **2 Claude** (Dispatcher + Auditor que ordena×audita pro Founder) + **2 Codex** (TR-SKILLS, TR-TRANSF) + **1 Windsurf** (TR-POLICY); 3 tracks de escrita disjuntos; padrão de prompt CKOS + protocolo BRA/Q&A; **aguarda aprovação do LOTE L3-W1 (Founder)**. TR-DATAMODELS + TR-CORERUNTIME = GATE-5-atados (Onda futura)
  - **L4:** DNA vault + SUPERAGENT (benchmark externo — mapear estudo de tradução do DNA antes) + dups UI/UX
  - **Mecanismo validado:** git mv preserva links (wikilinks por nome) + commit por lote reversível
- [ ] GATE 5 — Spec do Backend MVP thin-slice (arquivo 03) #F0 #gate **[SPEC PRONTA + FAN-IN ✅ — EM ESPERA até consolidação]**
  - **Arquivo:** `03_BACKEND_MVP_THIN_SLICE_PLAN.md` (Codex2 criou; fan-in Claude ✅ 2026-06-02)
  - **Fan-in:** 16 seções, backend puro, event log central, RLS/tenant desde S1, 9 AQs. Doc 12 + secret handling adicionados no fan-in.
  - **Pendência única:** decisão Founder (aprovar = fecha F0, abre F1; é gate, não auto-aprovável)
  - **Pacote de decisão:** `GATE5_FOUNDER_DECISION_PACKAGE.md` (go/no-go, 9 AQs, o que libera/bloqueia)
- [ ] Doc 11 RAG schema — patch CANDIDATE (proposta, não aplicação) #F0 #runtime
  - **Depende de:** arquivo 03 (GATE 5) — sem ele vira over-engineering
  - **Prompt pronto:** `000_ROADMAPS/12_PROMPTS/08_PROMPT_CODEX_DOC11_RAG_SCHEMA_PATCH_CANDIDATE.md`
  - **Descoberta fan-in:** tabelas RAG já existem no Doc 11 §14 → é refinamento de campos, não criação. Diff mínimo = (Doc 28 §18 ∩ MVP usa ∩ não-existe)
  - **P1 schema:** aplicação real exige aprovação Founder + Technical em sessão canonical_patch separada
- [ ] F1 Runtime I/O Contracts — User-in + Response-out (patch CANDIDATE, não aplicação) #F0 #FX #runtime
  - **Nota:** `F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md` — reconcilia 2 propostas Founder (User System + Cognitive Response Engine) vs canônico
  - **Achado:** ~75% já é canônico (pipeline de resposta = Doc 10 §5.2 verbatim); net-new = 10 itens (U1-U5 + R1-R5), mais fortes U1/U2 + R1/R2
  - **Depende de:** GATE 5 — refina o runtime que o thin-slice define; sem ele vira over-engineering
  - **AQ-IO-1** (thin-slice começa no usuário ou no projeto?) → entra no `GATE5_FOUNDER_DECISION_PACKAGE.md`
  - **Não entra:** visual/atmosfera (F4) · folder-trees (fragmentação) · SQL (Doc 11 gated)
- [x] Reconciliação de fronteira canônica → 01-28 (policy, consolidation map, master roadmap, runbook, MASTER_MAP) ✅ 2026-06-02 #F0 #FX
  - **Método:** declaração viva atualizada; histórico do GATE 0 preservado via notas (não reescrito)
  - **Achado:** atualização do MASTER_MAP pelo Codex GATE 3 era parcial (linhas 41/43 desatualizadas) — corrigido

## 🟡 Curto — F1 Runtime Cognitivo MVP

> Abre após GATE 5 aprovado pelo Founder (spec = arquivo 03, vive em F0).
- [ ] S1 — Intent Resolver + Context State + output simples #F1 #runtime
- [ ] S2 — Question Engine + score de clareza + lacunas/risco #F1 #runtime
- [ ] S3 — Registry agentes/skills + policy checker + approval gates #F1 #runtime #agentes
- [ ] S4 — Event Log (sem ele, vira chat bonito) #F1 #runtime #blocker
- [ ] S5 — Work Order + Agent Run end-to-end #F1 #runtime
- [ ] S6 — Feedback + Memória + ROI #F1 #runtime
- [ ] Os 4 agentes MVP: Cognik / PM / Risk(Metacognik) / ROI #F1 #agentes

## 🟠 Médio — F2 Agentes&Skills + F3 DNA

- [ ] Catálogo de agentes (superagents + domínio + subagents) #F2 #agentes
- [ ] Skills como discipline-master docs (doutrina + anti-padrões + score 0-10) #F2 #agentes
- [ ] Skill Selector — escolhe/ranqueia skills na tarefa (L-02) #F2 #agentes
- [ ] Model Router OpenRouter (reasoning por decisão/risco/custo) #F2 #runtime
- [ ] Research proativo: Perplexity + deep research + Apify + dados reais #F2 #conectores
- [ ] Creative DNA objeto vivo (DNA-0 → DNA-vivo) #F3 #dna
- [ ] DNA bootstrapping just-in-time (missão sem DNA) #F3 #dna
- [ ] Briefing/perguntas/notas/research como depósitos de DNA #F3 #dna
- [ ] Calibração: feedback→learning + DNA-consistency no ROI/QA #F3 #dna #FX

## 🔴 Longo — F4 Produto + F5 Conectores + F6 Autonomia

- [ ] Project Pulse / Dashboard vivo (Doc 14) #F4 #produto
- [ ] Command Center (intenção/aprovação, emite eventos) (Doc 15) #F4 #produto
- [ ] Node Canvas (objetos vivos do runtime) (Doc 16) #F4 #produto
- [ ] Frontend como projeção do runtime #F4 #produto
- [ ] MCP + OAuth (Google/Meta) + Apify actors (Doc 26) #F5 #conectores
- [ ] n8n como acelerador; migrar fluxos críticos p/ código #F5 #conectores
- [ ] Níveis de autonomia + auto-approval baixo risco (Doc 04) #F6 #autonomia
- [ ] Approval batches (lotes 5-10, não item a item) #F6 #autonomia
- [ ] Builder Subagents sob Builder Lead #F6 #autonomia #agentes
- [ ] Self-Evolving System: sandbox + eval-antes-merge + rollback (Doc 21/25) #F6 #autonomia
- [ ] Heartbeat / proatividade (acorda→lê→age→audita→memória) #F6 #autonomia
  - **Precursor manual:** Vault Operating Loop (FX) — quando o heartbeat assume, aposentar os relatórios manuais
- [ ] Skill request / learning loop (agente pede skill, recebe) (L-03) #F6 #agentes

## 🌅 Visão — F7 Negócio & Escala

- [ ] ROI operacional como métrica de produto (Doc 21) #F7 #negocio
- [ ] Créditos / Planos / Billing + budget gates (Doc 24) #F7 #negocio
- [ ] Suporte IA-humano (Doc 23) #F7 #negocio
- [ ] Creator/Client Project Mode (projeto por intenção mínima) #F7 #negocio
- [ ] Marketplace / CKStore (skills, workflows, agentes, conectores) #F7 #negocio

## 🛡️ Contínuo — FX Governança & Segurança

- [ ] Segurança/Permissões/Data Governance: secrets, isolamento, RLS (Doc 12) #FX
- [ ] Evals/Observability/Cost: traces, qualidade, custo/run (Doc 13) #FX
- [ ] QA & Founder Approval gates (Doc 20) #FX
- [ ] Multi-session policy + checkout locks + BRA + fan-in (ativo) #FX
- [ ] Vault Operating Loop — cadência daily-intake / fan-in / nightly / weekly sobre a infra existente (process layer, NÃO runtime) #FX
  - **Limite:** opera os boards/registries que já existem; NÃO simula event store em Markdown (Princípios #1 e #5)
  - **Governança:** cada rotina tem dono + condição de morte (aposentada quando o Heartbeat F6 assume)
  - **Não fazer agora:** abrir Study Layer 15 (7 notas) nem os ~11 arquivos novos — empurra fragmentação no meio da F0
  - **Weekly Canonical Review** consome GATE 1 (Patch A/B), órfãos, dups e `RESEARCH_GAPS_QUEUE`

## Arquivado / Referência

- [ ] Docs 29-34 — rodam em paralelo com F1, não bloqueiam GATE 5 #F0
  - **Batch strategy:** Codex pode escrever docs canônicos em paralelo (Codex1 ≠ Codex2), mas NÃO em lote numa sessão (qualidade degrada, fan-in fica mais lento)
  - **Doc 29 candidate:** Vault Operating Loop / Documentation Automation — numeração gated por GATE 1 ✅
  - **Doc 30 recusado:** Agent Skill Registry duplica Docs 03/06 — revisar escopo antes de abrir
  - **Docs 31-34:** definir após GATE 5 — não antecipar sequência sem saber o que o backend vai exigir
- [ ] Curadoria do DNA_system_vault (descartar notas copy-paste) #F3 #dna
- [ ] Extrair metodologia Human Academy (sem copiar) #F3 #dna

---

## Legenda de fases

- **#F0** Convergência Documental (agora) · **#F1** Runtime Cognitivo MVP
- **#F2** Agentes & Skills · **#F3** Motor de DNA · **#F4** Superfícies de Produto
- **#F5** Conectores · **#F6** Autonomia & Auto-Evolução · **#F7** Negócio & Escala
- **#FX** Governança & Segurança (transversal)
- **#gate** = gate formal do Founder · **#blocker** = bloqueia outras frentes

## Como usar (Obsidian)

1. Requer o plugin **Kanban** (Settings → Community Plugins → "Kanban").
2. Cada lane = horizonte de tempo; arraste cards conforme avançam.
3. Filtre por tag (#F2, #dna, #gate…) para ver uma frente isolada.
4. Dependências macro: F0 → F1 → (F2 ∥ F3) → F4 → (F5 ∥ F6) → F7; FX em paralelo.
5. Detalhe e "porquê" de cada fase: `CKOS_MASTER_EXPANSION_ROADMAP.md`.
