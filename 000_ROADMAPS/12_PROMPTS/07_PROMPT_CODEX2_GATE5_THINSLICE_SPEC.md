---
title: Prompt Codex 2 — GATE 5 · Backend MVP Thin-Slice Spec (arquivo 03)
file: 07_PROMPT_CODEX2_GATE5_THINSLICE_SPEC.md
phase: 000_ROADMAPS
category: prompts
status: ready_for_use
owner: pmo_ckos
created_at: 2026-06-02
session_origin: S-P1-GATE1-CLAUDE-20260602-002
purpose: Prompt pronto para Codex 2 criar a spec do backend MVP thin-slice (arquivo 03), em paralelo com Doc 28.
---

## EXECUTION HANDOFF — GATE5-THINSLICE-SPEC — 2026-06-02

### Objetivo
Criar `000_ROADMAPS/22_CONSOLIDATION/03_BACKEND_MVP_THIN_SLICE_PLAN.md` — a especificação
do slice vertical mínimo do backend AI-first do CKOS. Este arquivo foi prometido no mapa de
consolidação §7 e nunca criado. É o que desbloqueia o GATE 5 e a Fase F1.

### Modo de execução
`planning` (auxiliar) — é um documento de PMO/planejamento, NÃO é doc canônico, NÃO autoriza
implementação. Vive em `000_ROADMAPS/`, não em `07_EVOLUTION_SYSTEM/`. Aprovação do GATE 5 pelo
Founder é o que autoriza construir — este arquivo apenas especifica.

### Ferramenta
Codex 2

### Inteligência exigida
`high` — cruza múltiplos docs canônicos; ambiguidade vira ARCHITECTURE_QUESTION, não suposição.

---

## ⚠️ Boundary crítico (anti-conflito com Codex 1)

O Codex 1 está criando o **Doc 28 (Notes/RAG/Knowledge)** em paralelo. Para os dois não
escreverem specs de RAG conflitantes:

- O arquivo 03 **referencia** o Doc 28 para tudo que for ingestão/embedding/RAG/retrieval.
- Na parte "Evidência → Memória" do slice, escreva apenas a interface (que evento entra, que
  objeto sai) e marque: `// detalhe de RAG/indexação → Doc 28 (em criação por Codex 1)`.
- **NÃO** especificar chunking, embedding, vector schema ou query policy aqui. Isso é Doc 28.

---

## Leitura obrigatória ANTES de escrever (nesta ordem)

1. `000_ROADMAPS/22_CONSOLIDATION/00_CKOS_CONSOLIDATION_MAP_AND_GAP_AUDIT.md` §6 e §7 — o esqueleto já rascunhado do thin-slice
2. `000_ROADMAPS/22_CONSOLIDATION/CKOS_MASTER_EXPANSION_ROADMAP.md` — seção F1 (o slice vertical oficial)
3. `000_UPGRADE/13_MVP_FUNCTIONAL/sprints.md` — os 6 sprints (ATENÇÃO: ver constraint sobre UI abaixo)
4. `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md` — intent resolver, context, policy, run scheduler, agent/model router
5. `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md` — tabelas event log, work order, run
6. `07_EVOLUTION_SYSTEM/27_AI_FIRST_WORK_ORDERS_AND_MULTI_SESSION_ORCHESTRATION_ARCHITECTURE.md` — Work Order envelope
7. `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md` — os 4 agentes do MVP (Cognik, PM/Builder, Metacognik, ROI)
8. `01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md` — approval gates
9. `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md` — ROI mínimo do slice

---

## Constraint crítico: thin-slice é BACKEND PURO

O `sprints.md` lista "UI de chat + painel lateral" no Sprint 1. **IGNORAR a UI.**
O Princípio #1 do Master Roadmap é: *documentação antes de runtime; runtime antes de UI.*
O thin-slice oficial (Master Roadmap F1) é:

```
Intenção (Doc 15) → Intent Resolver + Cognik (Doc 03/10) → Metacognik approval (Doc 04)
→ Work Order (Doc 27) → Agent Run (Doc 03) → Event Log (Doc 10/11/13)
→ Evidência → Memória (Doc 05 + Doc 28) → ROI (Doc 21)
```

Sem UI. Sem dashboard. Sem frontend. O slice prova que **uma intenção percorre o pipeline
inteiro e deixa rastro auditável** — via API/eventos, não via tela.

---

## Estrutura de seções obrigatória do arquivo 03

```
# 1. Propósito (o que o thin-slice prova)
# 2. O que está DENTRO do slice / O que está FORA
   (Tabela: dentro = intent→run→evento→memória→ROI backend; fora = UI, civilização de agentes,
    catálogo, marketplace, self-evolving, conectores além do mínimo)
# 3. Princípio: backend antes de UI
# 4. O slice vertical em uma página (diagrama do fluxo)
# 5. Componentes mínimos do runtime
   (mapear cada componente do Doc 10 que o slice precisa — e quais NÃO precisa ainda)
# 6. Os 4 agentes do MVP
   (Cognik / PM-Builder / Metacognik-Risk / ROI — papel de cada um no slice)
# 7. Modelo de dados mínimo
   (quais tabelas do Doc 11 o slice usa: events, work_orders, runs, memory; RLS desde o início)
# 8. Event Log — o coração do slice
   (sem event log, vira chat bonito — Princípio #5)
# 9. Sequência de sprints S1-S6 mapeada a docs
   (reescrever os 6 sprints do sprints.md SEM UI, cada um com doc-dono e critério de pronto)
# 10. Interface Evidência → Memória
   (apenas a fronteira; detalhe de RAG → Doc 28. NÃO especificar embedding/chunking aqui)
# 11. ROI mínimo do slice
   (que proxies de ROI o slice registra — Doc 21)
# 12. Stack de referência
   (apontar 99_RESEARCH_LAB para padrões event-driven/Supabase — referência, não decisão final)
# 13. Critérios de pronto do GATE 5
   (checklist: o que precisa estar especificado para o Founder aprovar e o backend começar)
# 14. Dependências e ordem
   (o que depende de Doc 28; o que pode começar antes; o que bloqueia o quê)
# 15. ARCHITECTURE_QUESTIONS em aberto
   (decisões que precisam de Founder/Technical antes de codar)
# 16. Riscos do slice
```

---

## Arquivos permitidos para modificação

- `000_ROADMAPS/22_CONSOLIDATION/03_BACKEND_MVP_THIN_SLICE_PLAN.md` — **CRIAR**
- `000_ROADMAPS/SESSION_REGISTRY.md` — registrar sessão + lock + release

## Arquivos proibidos (não tocar)

- Qualquer doc canônico 01-28 (apenas leitura/referência)
- `07_EVOLUTION_SYSTEM/28_...` — está sendo criado por Codex 1, NÃO tocar
- `CKOS_EXPANSION_KANBAN.md` e `CKOS_MASTER_EXPANSION_ROADMAP.md` — PMO/Claude atualiza no fan-in
- ARCHITECTURE_PATCH_REPORT.md, 00_SYSTEM_GOVERNANCE/
- Qualquer arquivo de implementação real (código, migrations, API, workers)

## Não fazer

- Não especificar UI, frontend, telas, componentes
- Não especificar internals de RAG/embedding/chunking (isso é Doc 28)
- Não criar código nem migrations reais (é spec, não implementação)
- Não inventar tabelas fora do Doc 11 (se faltar, registrar como ARCHITECTURE_QUESTION ou patch sugerido ao Doc 11)
- Não declarar GATE 5 como aprovado — só o Founder aprova gate

---

## Como declarar a sessão no SESSION_REGISTRY

```
session_id: S-P1-GATE5-CODEX2-20260602-001
task_id: GATE5_BACKEND_MVP_THIN_SLICE_SPEC_20260602
session_type: planning
agent: codex_2
scope: 000_ROADMAPS/22_CONSOLIDATION/03_BACKEND_MVP_THIN_SLICE_PLAN.md (CRIAR);
       000_ROADMAPS/SESSION_REGISTRY.md
status: active → released
started_at: 2026-06-02
expected_outputs: arquivo 03 criado (spec do thin-slice, sem UI, sem RAG internals)
estimated_cost: low-medium
intelligence_level: high
```

---

## Output esperado (CHECKOUT RELEASE)

```
FILES_CREATED: 03_BACKEND_MVP_THIN_SLICE_PLAN.md
FILES_CHANGED: SESSION_REGISTRY.md
SUMMARY: [o que o slice prova, em 5 linhas]
SPRINTS_MAPPED: [S1-S6 com doc-dono de cada]
DOC_28_DEPENDENCIES: [o que a seção 10 deixou para o Doc 28]
DOC_11_PATCH_SUGGESTIONS: [tabelas/campos que faltam, se houver]
ARCHITECTURE_QUESTIONS: [decisões em aberto para Founder/Technical]
RISKS: [riscos do slice]
NEXT_STEP: "Fan-in Claude: verificar que slice não tem UI nem RAG internals; preparar GATE 5 para aprovação Founder"
```

---

## Nota de fan-in (para o Claude depois)

Verificar:
- [ ] Slice é backend puro? (zero UI, zero frontend)
- [ ] Seção 10 referencia Doc 28 em vez de redefinir RAG?
- [ ] Os 6 sprints foram reescritos SEM a UI do sprints.md original?
- [ ] Event Log está no centro (Princípio #5)?
- [ ] RLS/tenant desde o primeiro sprint?
- [ ] Os 4 agentes do MVP corretos (Cognik/PM/Metacognik/ROI)?
- [ ] ARCHITECTURE_QUESTIONS registradas, não resolvidas silenciosamente?
- [ ] Nenhuma tabela inventada fora do Doc 11?
- [ ] É spec (planning), não implementação?

Se todos ✅ → arquivo 03 pronto; GATE 5 vai para aprovação Founder.
