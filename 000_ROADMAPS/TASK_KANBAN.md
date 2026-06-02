---
kanban-plugin: basic
title: CKOS Task Kanban
---

# CKOS Task Kanban

> **Sincronizado em 2026-06-01 (PMO)** com `000_ROADMAPS/SESSION_REGISTRY.md`.
> Fonte de verdade dos releases = Session Registry + `ARCHITECTURE_PATCH_REPORT.md`.

## Backlog

- [ ] #doc28 Doc 28 — Notes/RAG/Knowledge Architecture
  - **Prioridade:** Alta
  - **Responsável:** PMO
  - **Dependências:** Doc 27 aprovado ✅ (dependência satisfeita)
  - **Base de estudo:** Layer 13 notas 04, 12, 18
  - **Tags:** #doc28 #notes #rag #knowledge

- [ ] #patch Target-doc patches diferidos (Docs 10/11/12/13/24)
  - **Prioridade:** Média
  - **Responsável:** PMO/Codex
  - **Origem:** sign-off do Doc 27 (`S-P1-27-CODEX-20260601-003`) deixou patches-alvo para checkouts separados
  - **Dependências:** Cada doc exige seu próprio gate/checkout
  - **Tags:** #patch #deferred #canonical

## Em Progresso

- [ ] _(nenhuma sessão de escrita ativa registrada)_

## Bloqueado

- [ ] #gate Ativação do Antigravity (design_study execution)
  - **Bloqueado por:** Gate formal do Founder não emitido
  - **Link:** `000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md`
  - **Tags:** #antigravity #gate #founder

- [ ] #gate Windsurf como executor governado
  - **Bloqueado por:** Registrado como `specialist_unregistered`; sem gate equivalente ao Antigravity
  - **Tags:** #windsurf #gate #risk

## Concluído

- [x] #doc27 Doc 27 — AI-first Work Orders and Multi-Session Orchestration Architecture
  - **Responsável:** Codex + Claude (auditoria) + Founder/PMO/Metacognik (sign-off)
  - **Data:** 2026-06-01
  - **Veredito:** `SIGN_OFF_APPROVED` — `status: approved`, `provenance: approved_after_external_audit`, `confidence: high`
  - **Cadeia de gate:** `-001` criação → `-002` LP-1/LP-2 → `-003` sign-off formal
  - **Nota:** LP-3 registrado como `DISPENSABLE_NOT_REQUIRED`
  - **Link:** `07_EVOLUTION_SYSTEM/27_AI_FIRST_WORK_ORDERS_AND_MULTI_SESSION_ORCHESTRATION_ARCHITECTURE.md`
  - **Tags:** #doc27 #canonical #approved

- [x] #patch M-1, M-2, PATCH-OBR-1..6, PO-01 (patches de readiness do Doc 27)
  - **Responsável:** Codex (study-only)
  - **Data:** 2026-06-01
  - **Status:** Resolvidos na sessão de cleanup `S-P1-13-CODEX-20260601-009` (colisão ordinal 23, task vs Work Order, ID Doc 11, fronteira BRA↔context_pack, classificação auxiliar-operacional, Paperclip tier, CEO→Cognik/Nick)
  - **Tags:** #patch #cleanup #layer13 #layer14

- [x] #audit Doc 26 v1.0.4 External Audit
  - **Responsável:** Claude Sonnet 4.6
  - **Data:** 2026-06-01
  - **Veredito:** Released with required formal approvals
  - **Link:** `000_ROADMAPS/SESSION_REGISTRY.md` (S-P1-26-CLAUDE-20260601-001)
  - **Tags:** #doc26 #audit #external

- [x] #study Study Layer 13 criação (notas 01-14)
  - **Responsável:** Codex
  - **Data:** 2026-05-30
  - **Status:** Released with required external audit
  - **Link:** `000_ROADMAPS/SESSION_REGISTRY.md` (S-P1-13-CODEX-20260530-001)
  - **Tags:** #study #layer13 #creation

- [x] #study Study Layer 14 Paperclip Regularization
  - **Responsável:** Codex
  - **Data:** 2026-06-01
  - **Status:** Released with required external audit
  - **Link:** `000_ROADMAPS/SESSION_REGISTRY.md` (S-P1-14-CODEX-20260601-001)
  - **Tags:** #study #layer14 #paperclip

- [x] #audit Criar template de auditoria automática
  - **Responsável:** Cascade
  - **Status:** Concluído
  - **Link:** `000_ROADMAPS/AUDIT_AUTOMATION_TEMPLATE.md`
  - **Tags:** #automation #template #audit

- [x] #audit Criar Kanban de tarefas
  - **Responsável:** Cascade
  - **Status:** Concluído (sincronizado por PMO em 2026-06-01)
  - **Link:** `000_ROADMAPS/TASK_KANBAN.md`
  - **Tags:** #kanban #visualization #obsidian

## Arquivado

- [ ] #legacy Auditorias manuais anteriores
  - **Nota:** Criadas manualmente antes da automação; achados já migrados e resolvidos
  - **Arquivos:**
    - `DOC_27_ECOSYSTEM_READINESS_AUDIT.md`
    - `STUDY_LAYER_13_AUDIT.md`
    - `AUDITOR_STUDY_LAYER_DOC_27_READINESS.md`
  - **Tags:** #legacy #manual-audit #migration

---

## Legenda

- **#audit** - Tarefa de auditoria
- **#patch** - Tarefa de patch/correção
- **#doc27** - Relacionado ao Doc 27
- **#doc28** - Relacionado ao Doc 28
- **#study** - Tarefa de estudo
- **#layer13** - Study Layer 13
- **#layer14** - Study Layer 14
- **#canonical** - Documento canônico
- **#gate** - Gate de aprovação
- **#blocker** - Bloqueia outras tarefas

## Instruções de Uso

1. **Para adicionar tarefa:** Adicione item à seção apropriada (Backlog, Em Progresso, Bloqueado, Concluído)
2. **Para mover tarefa:** Mova item entre seções conforme progresso
3. **Para atualizar status:** Edite os campos conforme necessário
4. **Para linkar:** Use caminhos relativos do vault
5. **Tags:** Adicione tags relevantes para filtragem

## Plugin Kanban

Este arquivo usa o formato do plugin **Kanban** do Obsidian. Se o plugin não estiver instalado:

1. Abra Settings → Community Plugins
2. Desabilite Safe Mode
3. Browse → Pesquise "Kanban"
4. Instale e habilite o plugin
5. Este arquivo será automaticamente renderizado como quadro Kanban
