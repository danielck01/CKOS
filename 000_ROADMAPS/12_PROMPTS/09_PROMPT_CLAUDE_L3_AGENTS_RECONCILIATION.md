---
title: Prompt Claude — Consolidação L3 · Reconciliação de Agentes
file: 09_PROMPT_CLAUDE_L3_AGENTS_RECONCILIATION.md
phase: 000_ROADMAPS
category: prompts
status: ready_for_use
owner: pmo_ckos
created_at: 2026-06-02
continues: sessão de consolidação 2026-06-02 (chat anterior, grande demais)
---

## EXECUTION HANDOFF — CONSOL-L3-AGENTS-RECONCILIATION — 2026-06-02

### Onde estamos (cold-start context)
O CKOS está na **F0 (convergência documental)**, fase de **consolidação das 3 camadas**.
A arquitetura canônica (Docs 01-28) está madura; o problema é **fragmentação**, não falta de docs.

**Estado do git** (baseline já existe — `git init` feito): branch `master`, últimos commits:
```
cf5d0a2 registro L1/L2 + refinação ordem F1
afc61d0 L2: Brain → 000_KNOWLEDGE_BASE (410 arq)
9aae8c3 L1: Miriam → 000_PROJECTS (100 arq)
b3fc69f baseline do vault
```

**Já feito na consolidação:**
- **L1** Miriam → `000_PROJECTS/` ✅
- **L2** Brain → `000_KNOWLEDGE_BASE/` ✅ (knowledge base de domínio, não arquitetura)
- Decisões D1-D4 tomadas (ver `04_CONSOLIDATION_EXECUTION_PLAN.md` §6). **D4 = promoção AGRESSIVA.**

### Objetivo desta sessão
**Reconciliar o subsistema de Agentes:** comparar `000_UPGRADE/03_AGENT_CIVILIZATION/` (65 arq, 2º sistema paralelo) contra o canônico `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md`, e produzir um **patch candidate** com o que promover ao canônico.

### Modo de execução
`patch_candidate` — **PROPÕE, não aplica.** Tocar o Doc 03 é P1 → exige aprovação Founder + Technical depois. Esta sessão só produz a proposta.

### Critério de promoção (D4 — AGRESSIVO)
Promover **tudo que for melhor/mais profundo** que o canônico, mesmo sem necessidade imediata de F1 — não só o mínimo. Founder quer canônico mais rico.

### Leitura obrigatória (nesta ordem)
1. `000_ROADMAPS/22_CONSOLIDATION/04_CONSOLIDATION_EXECUTION_PLAN.md` — o plano (§3 classificação, §6 decisões)
2. `000_ROADMAPS/22_CONSOLIDATION/00_CKOS_CONSOLIDATION_MAP_AND_GAP_AUDIT.md` §4 — matriz de disposição (já mapeou "Agentes: reconciliar catálogo UPGRADE/03 → patch p/ Doc 03")
3. `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md` — o canônico atual (o que JÁ existe)
4. `000_UPGRADE/03_AGENT_CIVILIZATION/` — os 65 arquivos (o espelho; o que ele tem a mais)

### Output esperado
Criar `000_ROADMAPS/22_CONSOLIDATION/DOC03_AGENTS_RECONCILIATION_CANDIDATE.md` com:
- **Inventário comparativo:** o que o canônico Doc 03 já cobre vs o que UPGRADE/03 tem a mais
- **A PROMOVER** (tabela: item | por que é melhor | seção-alvo no Doc 03)
- **JÁ COBERTO** (arquivar no UPGRADE, sem ação no canônico)
- **CONFLITOS** (onde UPGRADE contradiz o canônico → ARCHITECTURE_QUESTION, não decidir)
- **Plano de arquivamento** do UPGRADE/03 após promoção (mover → `99_ARCHIVE/`, não deletar)
- Risco P1 + nota de que aplicação no Doc 03 é sessão separada com aprovação Founder

### Arquivos permitidos
- `000_ROADMAPS/22_CONSOLIDATION/DOC03_AGENTS_RECONCILIATION_CANDIDATE.md` (CRIAR)
- `000_ROADMAPS/SESSION_REGISTRY.md` (registrar sessão + lock + release)
- `000_ROADMAPS/22_CONSOLIDATION/CKOS_EXPANSION_KANBAN.md` (atualizar card consolidação)

### Arquivos proibidos
- `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md` — **NÃO editar** (só proposta; aplicação é P1 separado)
- Qualquer canônico 01-28; ARCHITECTURE_PATCH_REPORT; implementação

### Mecanismo de move (validado)
git mv preserva os `[[wikilinks]]` (Obsidian config vazia = links por nome). Commit por lote = reversível. Arquivar = mover para `99_ARCHIVE/`, **nunca deletar**.

### Declaração no SESSION_REGISTRY
```
session_id: S-P1-CONSOL-L3-CLAUDE-20260602-009 (ou data real)
session_type: patch_candidate
agent: claude_opus_4_8
scope: arquivos permitidos acima
intelligence_level: high
```

### CHECKOUT RELEASE ao fim
files_created/changed · resumo (quantos itens a promover) · ARCHITECTURE_QUESTIONS · risco P1 · next_step ("aprovação Founder p/ aplicar promoção no Doc 03; depois L3-Skills/Transformers/Policies").

---

## Pendências da consolidação (backlog após Agentes)
- **L3 restante:** Skills (Doc 06 vs UPGRADE/04 + DNA/17), Transformers (Doc 09 vs UPGRADE/08), Data Models (Doc 11 vs UPGRADE/11), Policies (Doc 12 vs UPGRADE/07), Tools/Connectors (Doc 26 vs UPGRADE/05/06).
- **L4:** DNA_system_vault (271, mina de promoção DNA-PC-1..7) + SUPERAGENT_Director_Visual (158, **benchmark externo** — mapear estudo de tradução no DNA antes de arquivar o bruto) + dups UI/UX (04_UI_UX_STUDY vs 10_UIUX_STUDIES) + 000_UPLOADS.
- **F1 (em espera):** arquivo 03 (thin-slice) + §17 (ordem refinada Codex: objeto-primeiro, dogfooding, <10min). Só após consolidação + GATE 5 Founder.
