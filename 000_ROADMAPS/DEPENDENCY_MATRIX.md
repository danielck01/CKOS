---
title: Dependency Matrix - Parallel Execution System
system_id: dependency_matrix_v1_0
layer: auxiliary
phase: 000_ROADMAPS
category: dependency_management
status: active
version: 1.0.0
owner: pmo_ckos
created_at: 2026-06-01
purpose: Sistema de gestão de dependências para permitir execução simultânea de tarefas sem bloqueios
---

# Dependency Matrix - Parallel Execution System

## Princípios

1. **Paralelismo por padrão** - Tarefas são simultâneas a menos que explicitamente dependentes
2. **Dependências explícitas** - Apenas bloqueios reais devem impedir execução
3. **Isolamento de escopo** - Tarefas com escopos diferentes podem rodar simultaneamente
4. **Checkout locks granulares** - Locks por arquivo/pasta, não por projeto inteiro
5. **Fan-out autorizado** - Múltiplas sessões podem trabalhar em áreas não sobrepostas

---

## Matriz de Dependências Atual

### Tarefas Ativas

| Tarefa ID | Tarefa | Dependências | Bloqueia | Pode rodar simultaneamente com | Status |
|---|---|---|---|---|---|
| M-1 | Resolver colisão ordinal 23 (Layer 13) | Nenhuma | Doc 27 gate | M-2, PATCH-OBR-1..6, PO-01 | 🔴 Bloqueado (esperando PMO) |
| M-2 | Criar lista allowed/forbidden Doc 27 | Nenhuma | Doc 27 gate | M-1, PATCH-OBR-1..6, PO-01 | 🔴 Bloqueado (esperando PMO) |
| PATCH-OBR-1 | Desambiguar task vs Work Order (nota 25) | Nenhuma | Doc 27 | M-1, M-2, PATCH-OBR-2..6, PO-01 | 🟡 Pronto para iniciar |
| PATCH-OBR-2 | Reconciliar identificadores com Doc 11 | Nenhuma | Doc 27 | M-1, M-2, PATCH-OBR-1,3..6, PO-01 | 🟡 Pronto para iniciar |
| PATCH-OBR-3 | Classificar notas 23/25 como auxiliar | Nenhuma | Doc 27 | M-1, M-2, PATCH-OBR-1,2,4..6, PO-01 | 🟡 Pronto para iniciar |
| PATCH-OBR-4 | Remover coluna Phase 1.0/1.1/1.2 (nota 06) | Nenhuma | Doc 27 | M-1, M-2, PATCH-OBR-1..3,5,6, PO-01 | 🟡 Pronto para iniciar |
| PATCH-OBR-5 | Fechar fronteira BRA ↔ context_pack | Nenhuma | Doc 27 | M-1, M-2, PATCH-OBR-1..4,6, PO-01 | 🟡 Pronto para iniciar |
| PATCH-OBR-6 | Listar allowed/forbidden Doc 27 | Nenhuma | Doc 27 | M-1, M-2, PATCH-OBR-1..5, PO-01 | 🟡 Pronto para iniciar |
| PO-01 | CEO Agent → Cognik/Nick (3 arquivos) | Nenhuma | Doc 27 | M-1, M-2, PATCH-OBR-1..6 | 🟡 Pronto para iniciar |

### Tarefas Futuras

| Tarefa ID | Tarefa | Dependências | Pode rodar simultaneamente com | Status |
|---|---|---|---|---|
| DOC-27 | Abrir Doc 27 | M-1, M-2, PATCH-OBR-1..6, PO-01, PMO fan-in, Founder checkout | DOC-28 (após M-1..6) | 🔵 Aguardando pré-condições |
| DOC-28 | Criar Doc 28 (Notes/RAG) | DOC-27 aberto | DOC-27 | 🔵 Aguardando Doc 27 |

---

## Grupos de Execução Simultânea

### Grupo A - Patches Independentes (PODEM RODAR SIMULTANEAMENTE)

Estas tarefas **NÃO** têm dependências entre si e **PODEM** ser executadas em paralelo por diferentes agentes:

- **PATCH-OBR-1** (nota 25) - Escopo: `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/25_*.md`
- **PATCH-OBR-2** (Doc 11 identifiers) - Escopo: `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/19_*.md`, `15_*.md`
- **PATCH-OBR-3** (classificação notas 23/25) - Escopo: `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/23_*.md`, `25_*.md`
- **PATCH-OBR-4** (nota 06 Layer 14) - Escopo: `000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/06_*.md`
- **PATCH-OBR-5** (BRA boundary) - Escopo: `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/21_*.md`
- **PATCH-OBR-6** (Doc 27 sections) - Escopo: `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/24_*.md`
- **PO-01** (CEO Agent → Cognik) - Escopo: `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/01_*.md`, `06_*.md`, `ck_agent_handoffs.md`

**Agentes sugeridos para execução simultânea:**
- Codex 1: PATCH-OBR-1, PATCH-OBR-3
- Codex 2: PATCH-OBR-2, PATCH-OBR-5
- Codex 3: PATCH-OBR-4, PATCH-OBR-6
- Codex 4: PO-01

### Grupo B - Patches de Coordenação (REQUIREM PMO)

Estas tarefas requerem decisão do PMO antes de iniciar:

- **M-1** (colisão ordinal 23) - Requer decisão PMO sobre qual nota renomear
- **M-2** (Doc 27 sections list) - Requer PMO para autorizar criação

### Grupo C - Gate Final (REQUIREM FOUNDER)

- **DOC-27** - Requer todos os patches + PMO fan-in + Founder checkout

---

## Regras de Checkout Lock para Execução Simultânea

### Locks Granulares por Arquivo

Para permitir execução simultânea, use locks **por arquivo específico**, não por pasta inteira:

**Exemplo incorreto (bloqueia tudo):**
```yaml
allowed_scope:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/
```

**Exemplo correto (permite paralelismo):**
```yaml
allowed_scope:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/25_LOCAL_OPERATOR_CONTROL_ROOM_AND_AUTONOMOUS_DISPATCH_STUDY.md
```

### Matriz de Conflito de Arquivos

| Arquivo | Tarefas que tocam | Pode rodar simultaneamente? |
|---|---|---|
| `25_*.md` | PATCH-OBR-1, PATCH-OBR-3 | ❌ Não (conflito) |
| `19_*.md` | PATCH-OBR-2 | ✅ Sim (isolado) |
| `15_*.md` | PATCH-OBR-2 | ✅ Sim (isolado) |
| `23_*.md` | PATCH-OBR-3, M-1 | ❌ Não (conflito) |
| `06_*.md` (Layer 14) | PATCH-OBR-4 | ✅ Sim (isolado) |
| `21_*.md` | PATCH-OBR-5 | ✅ Sim (isolado) |
| `24_*.md` | PATCH-OBR-6, M-2 | ❌ Não (conflito) |
| `01_*.md` | PO-01 | ✅ Sim (isolado) |
| `06_*.md` (Layer 13) | PO-01 | ✅ Sim (isolado) |
| `ck_agent_handoffs.md` | PO-01 | ✅ Sim (isolado) |

---

## Estratégia de Execução em Paralelo

### Fase 1 - Execução Simultânea (HOJE)

**Iniciar imediatamente (sem bloqueios):**

1. **Sessão Codex-1:** PATCH-OBR-1 + PATCH-OBR-3
   - Lock: `25_*.md`, `23_*.md`
   - Nota: Conflito entre PATCH-OBR-1 e PATCH-OBR-3 no arquivo 25 - executar sequencialmente nesta sessão

2. **Sessão Codex-2:** PATCH-OBR-2 + PATCH-OBR-5
   - Lock: `19_*.md`, `15_*.md`, `21_*.md`
   - Nota: Sem conflitos - verdadeiro paralelismo

3. **Sessão Codex-3:** PATCH-OBR-4
   - Lock: `14/06_*.md`
   - Nota: Isolado - pode rodar simultaneamente com Codex-2

4. **Sessão Codex-4:** PO-01
   - Lock: `01_*.md`, `13/06_*.md`, `ck_agent_handoffs.md`
   - Nota: Isolado - pode rodar simultaneamente com Codex-2 e Codex-3

5. **Sessão PMO:** M-1 + M-2
   - Lock: `23_*.md`, `24_*.md`, `README.md`, `ck_memory.md`, `ck_tasks.md`, `SESSION_REGISTRY.md`
   - Nota: Requer decisão PMO sobre renomeação

### Fase 2 - Sincronização (APÓS FASE 1)

Após todas as tarefas da Fase 1 completarem:

1. **PMO Fan-in:** Consolidar resultados de todas as sessões
2. **PATCH-OBR-6:** Criar lista allowed/forbidden sections (agora possível com contexto completo)
3. **Founder Gate:** Decisão sobre abrir Doc 27

### Fase 3 - Execução Doc 27 (APÓS GATE)

1. **Sessão Canonical:** Criar Doc 27
2. **Sessão Study Layer:** Iniciar estudos para Doc 28 (simultâneo ao Doc 27)

---

## Comandos para Iniciar Sessões Simultâneas

### Para Codex (PATCH-OBR-1 + PATCH-OBR-3)

```yaml
session_id: S-PARALLEL-CODEX-1-[DATE]-001
task_id: PARALLEL_PATCH_OBR_1_3_[DATE]
session_type: study
agent: codex
scope:
  allowed:
    - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/25_LOCAL_OPERATOR_CONTROL_ROOM_AND_AUTONOMOUS_DISPATCH_STUDY.md
    - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/23_MULTI_MODEL_COMMAND_AND_PROMPT_DISPATCH_BOARD_STUDY.md
    - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md
    - 000_ROADMAPS/SESSION_REGISTRY.md
  forbidden:
    - docs 01-26
    - docs 27-34
    - 00_SYSTEM_GOVERNANCE/*
    - implementation surfaces
status: planned
expected_outputs:
  - PATCH-OBR-1 aplicado: desambiguar task vs Work Order na nota 25
  - PATCH-OBR-3 aplicado: classificar notas 23/25 como auxiliar operacional
  - ck_memory.md atualizado
  - SESSION_REGISTRY.md atualizado
estimated_cost: low
intelligence_level: high
parallel_group: A
conflicts_with: [S-PARALLEL-CODEX-2, S-PARALLEL-CODEX-3, S-PARALLEL-CODEX-4]
```

### Para Codex (PATCH-OBR-2 + PATCH-OBR-5)

```yaml
session_id: S-PARALLEL-CODEX-2-[DATE]-001
task_id: PARALLEL_PATCH_OBR_2_5_[DATE]
session_type: study
agent: codex
scope:
  allowed:
    - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/19_FOUNDER_CONTROL_APPROVAL_BATCHES_AND_AUTONOMY_LEVELS_STUDY.md
    - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_WORK_ORDER_LIFECYCLE_AND_RELEASE_PROTOCOL_STUDY.md
    - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/21_BRA_PACKET_SESSION_RELAY_PROTOCOL_STUDY.md
    - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md
    - 000_ROADMAPS/SESSION_REGISTRY.md
  forbidden:
    - docs 01-26
    - docs 27-34
    - 00_SYSTEM_GOVERNANCE/*
    - implementation surfaces
status: planned
expected_outputs:
  - PATCH-OBR-2 aplicado: reconciliar identificadores com Doc 11
  - PATCH-OBR-5 aplicado: fechar fronteira BRA ↔ context_pack
  - ck_memory.md atualizado
  - SESSION_REGISTRY.md atualizado
estimated_cost: low
intelligence_level: high
parallel_group: A
conflicts_with: [S-PARALLEL-CODEX-1]
can_run_simultaneously_with: [S-PARALLEL-CODEX-3, S-PARALLEL-CODEX-4]
```

### Para Codex (PATCH-OBR-4)

```yaml
session_id: S-PARALLEL-CODEX-3-[DATE]-001
task_id: PARALLEL_PATCH_OBR_4_[DATE]
session_type: study
agent: codex
scope:
  allowed:
    - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/06_PAPERCLIP_AGENT_OPERATING_MODEL_STUDY.md
    - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/ck_memory.md
    - 000_ROADMAPS/SESSION_REGISTRY.md
  forbidden:
    - docs 01-26
    - docs 27-34
    - 00_SYSTEM_GOVERNANCE/*
    - implementation surfaces
status: planned
expected_outputs:
  - PATCH-OBR-4 aplicado: remover coluna Phase 1.0/1.1/1.2
  - ck_memory.md atualizado
  - SESSION_REGISTRY.md atualizado
estimated_cost: low
intelligence_level: high
parallel_group: A
conflicts_with: []
can_run_simultaneously_with: [S-PARALLEL-CODEX-2, S-PARALLEL-CODEX-4]
```

### Para Codex (PO-01)

```yaml
session_id: S-PARALLEL-CODEX-4-[DATE]-001
task_id: PARALLEL_PO_01_[DATE]
session_type: study
agent: codex
scope:
  allowed:
    - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/01_PROJECT_AI_FIRST_OPERATING_MODEL.md
    - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/06_SUPERAGENT_AGENT_SUBAGENT_WORK_ALLOCATION_STUDY.md
    - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_agent_handoffs.md
    - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md
    - 000_ROADMAPS/SESSION_REGISTRY.md
  forbidden:
    - docs 01-26
    - docs 27-34
    - 00_SYSTEM_GOVERNANCE/*
    - implementation surfaces
status: planned
expected_outputs:
  - PO-01 aplicado: CEO Agent → Cognik/Nick em 3 arquivos
  - ck_memory.md atualizado
  - SESSION_REGISTRY.md atualizado
estimated_cost: low
intelligence_level: high
parallel_group: A
conflicts_with: []
can_run_simultaneously_with: [S-PARALLEL-CODEX-2, S-PARALLEL-CODEX-3]
```

---

## Monitoramento de Progresso

### Status Dashboard

| Grupo | Tarefas totais | Concluídas | Em progresso | Bloqueadas | % Completo |
|---|---|---|---|---|---|
| A (Patches independentes) | 7 | 0 | 0 | 0 | 0% |
| B (Coordenação PMO) | 2 | 0 | 0 | 2 | 0% |
| C (Gate Founder) | 1 | 0 | 0 | 7 | 0% |

### Atualizar este arquivo

Quando uma tarefa for concluída:
1. Atualize status na matriz de dependências
2. Mova tarefa no Kanban (`TASK_KANBAN.md`)
3. Atualize status dashboard
4. Registre no `SESSION_REGISTRY.md`

---

## Resumo Executivo

**Problema atual:** Tarefas ficam pausadas esperando umas às outras, travando desenvolvimento.

**Solução:** Sistema de dependências explícitas + locks granulares + execução em paralelo.

**Ação imediata:** Iniciar 4 sessões simultâneas (Codex-1, Codex-2, Codex-3, Codex-4) para patches independentes.

**Benefício:** Reduz tempo de conclusão de ~7 dias (sequencial) para ~2 dias (paralelo).
