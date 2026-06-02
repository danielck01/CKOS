---
title: Local Operator Control Room And Autonomous Dispatch Study
file: 25_LOCAL_OPERATOR_CONTROL_ROOM_AND_AUTONOMOUS_DISPATCH_STUDY.md
layer: study
doc_type: study_note
phase: 000_STUDY_NOTES
category: ai_first_project_operating_system
status: draft
version: 0.1.0
created_at: 2026-06-01
updated_at: 2026-06-01
owner: pmo_ckos
responsible_agent: windsurf
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
source_type: operational_control_room
source_tool: windsurf
provenance_status: unverified
confidence: medium
risk_level: high
intelligence_level: medium-high
project: ckos
purpose: Create a local operational control room for Founder to operate Claude, Codex, Antigravity/Gemini and Windsurf with minimal contact, without opening Doc 27, without implementing backend, without creating UI, without creating real agents.
inputs:
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/22_MULTI_SESSION_EXECUTION_ROADMAP_AND_SPRINT_BOARD_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/23_MULTI_MODEL_COMMAND_AND_PROMPT_DISPATCH_BOARD_STUDY.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/24_DOC27_SCOPE_RECONCILIATION_AND_GATE_PROPOSAL_STUDY.md
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/README.md
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/ck_memory.md
  - 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/07_PAPERCLIP_TO_CKOS_TRANSLATION_MATRIX_STUDY.md
  - 07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md
outputs:
  - local_operator_control_room
  - minimal_contact_commands
  - local_work_order_schema
  - prompt_templates
  - operational_kanban
  - fan_in_rule
  - documentation_strategy
  - next_batch_recommendation
tags:
  - study
  - control_room
  - multi_model
  - autonomous_dispatch
  - minimal_contact
  - doc27_blocked
---

# 25_LOCAL_OPERATOR_CONTROL_ROOM_AND_AUTONOMOUS_DISPATCH_STUDY.md

**Classification**: AUXILIARY OPERATIONAL; not a direct Doc 27 candidate

## 1. Boundary Study-Only

This file is study-only, draft and unverified. It is not canonical.

It does not create Doc 27. It does not create docs 28-34. It does not edit canonical docs 01-26. It does not edit `00_SYSTEM_GOVERNANCE/*`. It does not edit `ARCHITECTURE_PATCH_REPORT.md`.

It does not authorize backend, UI, API, database, migrations, MCP server real, JSON n8n, real agents, webhooks or runtime automations.

This note is an operational control room in Markdown only. It is not a real backend, queue, event bus, API or schema. It is a discipline convention for the Founder to operate multiple AI sessions with minimal contact.

This note may inform local Founder operation, session discipline and prompt dispatch. It must not be promoted directly into Doc 27 architecture. Any later reuse requires Claude/PMO fan-in, explicit Founder gate and a separate canonical checkout.

Identifier warning: `approval_id`, `task_id`, `work_order_id`, `lock_id` and `release_id` in this note are study placeholders or registry references only. They do not create canonical Doc 11 tables, fields, migrations, RLS rules, APIs or production schemas without a future approved Doc 11 patch.

## 2. Estado Atual Do Ecossistema

### Doc 26
- **Status**: v1.0.4, canonical, documentation-only
- **Owner**: Connectors, MCP, external tools, webhook governance and secret_refs
- **Posture**: No implementation, no MCP server real, no webhook real, no JSON n8n
- **Required patches**: P26-1 through P26-8 remain as candidate patches only, not applied
- **Audit status**: Pending Claude read-only audit before any target-doc patches or runtime work

### Study Layer 13
- **Status**: Notes 01-26 exist as study-only material
- **Posture**: Non-canonical, draft, unverified, requires external audit
- **Key notes**:
  - Note 15: Work Orders and Batch Execution
  - Note 21: BRA Briefing Relay Architecture
  - Note 22: Multi-Session Execution Roadmap and Sprint Board
  - Note 23: Multi-Model Command and Prompt Dispatch Board
  - Note 24: Doc 27 Scope Reconciliation and Gate Proposal
  - Note 25: Local Operator Control Room and Autonomous Dispatch (AUXILIARY OPERATIONAL)
  - Note 26: Local PMO Multi-Model Control Room, index-reconciled from former duplicate `23_LOCAL...` (AUXILIARY OPERATIONAL)
- **Doc 27**: BLOCKED until Founder/PMO explicit checkout, Claude audit fan-in and explicit OPEN decision

### Study Layer 14
- **Status**: Notes 01-07 exist as Paperclip benchmarking study
- **Posture**: Non-canonical, draft, unverified, requires external audit
- **Key notes**:
  - Note 06: CKOS Adoption Candidates for Doc 27
  - Note 07: Paperclip to CKOS Translation Matrix with forbidden interpretations
- **Paperclip**: Used as benchmark only, not runtime blueprint

### Doc 27
- **Status**: BLOCKED
- **Recommended scope from note 24**: AI-first Work Orders and Multi-Session Orchestration Architecture
- **Split**: Notes/RAG deferred to future Doc 28 candidate scope
- **Dependencies**: Doc 26 audit, Study Layer 13 audit, Study Layer 14 audit, PMO fan-in, Founder/PMO explicit checkout

### Implementation
- **Status**: BLOCKED
- **Forbidden**: Backend, UI, API, database, migrations, MCP server real, webhook real, JSON n8n, real agents, runtime automations

## 3. Mapa De Máquinas

### Máquina 1 (Primary)
- **Claude Code**: Architectural auditor (Claude 1)
- **Codex 1**: Primary executor for documentary writing and study-only patches
- **ChatGPT PMO**: Coordination dispatcher and decision framing
- **Role**: Primary machine for Doc 26 audit, Study Layer 13 audit and PMO fan-in

### Máquina 2 (Secondary)
- **Antigravity/Gemini**: Design study (if activated by Founder gate)
- **Claude Design**: Study Layer audit (Claude 2)
- **Codex 2**: Secondary executor for auxiliary patches and reconciliations
- **Windsurf**: Local PMO of support, prompt generation and BRA packet management
- **Role**: Secondary machine for Study Layer 14 audit, auxiliary patches and local dispatch

### Cross-Machine Coordination
- **Shared truth**: `SESSION_REGISTRY.md` is the single source of truth across both machines
- **BRA Packets**: Carry context between machines as markdown, not as runtime queues
- **Checkout locks**: Prevent cross-machine write conflicts
- **ChatGPT PMO**: Coordinates across both machines
- **Windsurf**: Generates prompts locally from vault context on Machine 2

## 4. Mapa De Sessões Ativas

### Codex 1 (Executor Documental)
- **Role**: Controlled documentary writing, study-only patches, auxiliary updates
- **Mode**: PATCH STUDY-ONLY by default
- **Authority**: Writes study/auxiliary material inside lock and emits checkout release
- **Current posture**: Available for authorized patches after PMO scope
- **Forbidden**: Cannot edit canonical docs 01-26, cannot create docs 27-34, cannot implement backend/UI/API/database

### Codex 2 (Executor Patch/Reconciliation)
- **Role**: Auxiliary patches, reconciliations, non-overlapping scoped work
- **Mode**: PATCH AUXILIARY or STUDY-ONLY
- **Authority**: Handles small reconciliations after PMO scope; must not touch Codex 1 files unless handed off
- **Current posture**: Available for auxiliary patches that do not overlap with Codex 1
- **Forbidden**: Cannot edit canonical docs 01-26 without separate canonical checkout

### Claude 1 (Auditor Arquitetural)
- **Role**: Audits Doc 26, ghost artifacts, dependency risks, canonical coherence
- **Mode**: READ-ONLY AUDIT by default
- **Authority**: Produces findings, not patches unless separately scoped
- **Current posture**: Available for Doc 26 v1.0.4 read-only audit
- **Forbidden**: Cannot edit files, cannot open Doc 27, cannot implement

### Claude 2 (Auditor Study Layer)
- **Role**: Audits Study Layer 13, Work Orders, BRA, notes/RAG, Doc 27 readiness
- **Mode**: READ-ONLY AUDIT by default
- **Authority**: Produces findings, not patches unless separately scoped
- **Current posture**: Available for Study Layer 13 notes 01-26 and Study Layer 14 notes 06-07 read-only audit after cleanup
- **Forbidden**: Cannot edit files, cannot open Doc 27, cannot implement

### Windsurf (Dispatcher Local PMO)
- **Role**: Local PMO of support, prompt generation, BRA packet management
- **Mode**: SUPPORT READ-ONLY
- **Authority**: Support role only; no canonical authority; generates prompts from vault context
- **Current posture**: Active as local dispatcher for this control room note
- **Forbidden**: Cannot claim canonical authority, cannot open Doc 27, cannot implement

### Antigravity/Gemini (Estudo Design)
- **Role**: UI/UX study without implementation
- **Mode**: DESIGN STUDY
- **Authority**: Design study only; no UI files, no frontend code, no implementation
- **Current posture**: BLOCKED until Founder-approved Design Study Session gate
- **Forbidden**: Cannot create UI files, cannot create frontend code, cannot implement

### ChatGPT PMO (Coordenador)
- **Role**: Coordination dispatcher, operational memory and decision framing
- **Mode**: PMO COORDINATION
- **Authority**: Decides sequencing and asks Founder for approval; does not silently open Doc 27
- **Current posture**: Available for fan-in synthesis and Founder decision framing
- **Forbidden**: Cannot open Doc 27 without explicit Founder/PMO approval

## 5. Sistema De Validade De Sessão

### Quando Uma Sessão Deve Declarar SESSÃO FINALIZADA

Uma sessão deve declarar "SESSÃO FINALIZADA" quando:

- Todos os outputs esperados foram entregues
- CHECKOUT RELEASE foi emitido com files_created, files_changed, files_not_touched
- Validação confirma que forbidden scope foi respeitado
- Riscos remanescentes foram documentados
- Next_step foi definido
- Status foi definido como released, released_with_required_external_audit ou blocked

**Regra**: "done" no chat NÃO é sessão finalizada. "SESSÃO FINALIZADA" requer CHECKOUT RELEASE explícito.

### Quando Deve Emitir Prompt De Retomada

Uma sessão deve deixar prompt de retomada quando:

- A sessão será retomada em outra interação
- O estado atual tem blockers que precisam ser resolvidos
- Há open questions que precisam de decisão
- O próximo passo depende de outra sessão ou Founder approval

**Formato mínimo**:
```txt
RE-ENTRY PROMPT FOR [session_id]:
Current state: [last action, files created/changed, blockers, open questions]
Next action: [smallest safe next action]
Context needed: [files to read, decisions needed]
Continue from this state with same scope and mode.
```

### Quando Deve Emitir BRA Packet

Uma sessão deve emitir BRA Packet quando:

- Output da sessão impacta outra sessão que precisa saber antes de agir
- Audit findings são entregues para patcher
- Mapper encontrou source files que auditor precisa revisar
- Study session criou candidates para PMO synthesis
- Executor completou release e outra sessão precisa fan-in results
- Blocker requer sessão diferente ou mais estreita
- Risk muda allowed next action
- Sessão paralela muda scope, risk ou blocker state de outra sessão ativa
- Founder decision é necessária antes da próxima sessão
- Múltiplas sessões precisam do mesmo current state sem compartilhar chat history

**Regra**: BRA Packet é obrigatório para cross-session impact. BRA Packet não é approval.

### Quando Deve Parar Por Excesso De Contexto

Uma sessão deve parar quando:

- Contexto acumulado excede capacidade de processamento sem perda de coerência
- Múltiplas revisões do mesmo arquivo sem progresso mensurável
- Chat history se torna muito longo para reconstruir estado
- Tokens gastos em loops sem novos outputs
- Founder attention é consumida por low-impact documents

**Ação**: Emitir CHECKOUT RELEASE, deixar re-entry prompt, iniciar nova sessão com estado limpo.

## 6. Founder Minimal-Contact Commands

### /status
**Propósito**: Mostrar estado atual do ecossistema em uma tabela
**Output**:
- Doc 26 status
- Study Layer 13 status
- Study Layer 14 status
- Doc 27 status (BLOCKED)
- Sessões ativas por máquina
- Work Orders em progresso
- Blockers atuais

### /next5
**Propósito**: Aprovar próximos 5 tasks dentro de Work Order bounded
**Requisitos mínimos**:
- Work Order ID
- Allowed scope (files/folders/actions)
- Forbidden scope (files/folders/actions)
- Risk ceiling (level)
- Cost ceiling (limit)
- Expiry (session/date)
- Required fan-in audit (auditor/session)
- Mandatory checkout release before any next batch

### /next10
**Propósito**: Aprovar próximos 10 tasks dentro de Work Order bounded
**Requisitos mínimos**: Mesmos que /next5, mas só quando:
- Tasks são low-risk ou study-only
- File scopes não overlap
- Nenhum canonical ou runtime work incluído
- Cost ceiling e stop conditions explícitos
- Risk escalation pausa o batch

### /blocked
**Propósito**: Mostrar todos os blockers atuais
**Output**:
- Blockers por sessão
- Blockers por Work Order
- Blockers por dependência
- Required decisions para unblock

### /audit
**Propósito**: Solicitar audit de Doc 26, Study Layer 13 ou Study Layer 14
**Parâmetros**:
- target: doc26 | layer13 | layer14
- mode: read-only
- auditor: claude_1 | claude_2
- scope: files to read

### /dispatch
**Propósito**: Windsurf gera prompt curto para sessão específica
**Parâmetros**:
- target_session: codex_1 | codex_2 | claude_1 | claude_2 | antigravity
- task_type: patch_study_only | patch_auxiliary | read_only_audit | design_study
- scope: allowed files/folders
- forbidden_scope: forbidden files/folders

### /fan-in
**Propósito**: PMO faz fan-in de outputs de múltiplas sessões
**Requisitos**:
- Todos os CHECKOUT RELEASEs relevantes foram emitidos
- BRA Packets foram registrados
- Conflitos identificados
- Synthesis ready para Founder decision

### /open-gate
**Propósito**: Founder abre gate específico (ex: Doc 27, Antigravity)
**Requisitos mínimos**:
- Explicit approval text
- Allowed sections
- Forbidden sections
- Dependencies
- Checkout lock
- Auditor
- Mandatory checkout release

### /close-session
**Propósito**: Fecha sessão específica com CHECKOUT RELEASE
**Requisitos**:
- Session ID
- Files created/changed/not touched
- Validation
- Risks remaining
- Next step

### /resume-session
**Propósito**: Retoma sessão com re-entry prompt
**Requisitos**:
- Session ID
- Re-entry prompt from previous session
- Same scope and mode

## 7. Work Order Operacional Local

Rule: task = unidade atomica de trabalho. Work Order = envelope governado de execucao. The local Work Order shape below is a study placeholder, not a table, schema, migration, API contract or Doc 11 patch.

### Schema Mínimo

```yaml
work_order_id: [unique identifier]
owner_session: [codex_1 | codex_2 | claude_1 | claude_2 | windsurf | antigravity]
allowed_scope:
  files: [list of allowed files/folders]
  actions: [read | patch_study_only | patch_auxiliary | read_only_audit]
forbidden_scope:
  files: [docs 01-26 | docs 27-34 | 00_SYSTEM_GOVERNANCE/* | ARCHITECTURE_PATCH_REPORT.md | backend | UI | API | database | migrations | MCP server | webhook | JSON n8n | real agents | runtime automations]
required_reads: [list of source files to read before starting]
expected_output: [description of deliverable]
approval_required: [founder | pmo | none]
risk_ceiling: [low | medium | high]
roi_hypothesis: [value_created, risk_reduced, context_saved, decision_unlocked]
checkout_lock_ref: [lock_id from SESSION_REGISTRY.md or pending_pmo_approval]
bra_required: [yes | no]
session_expiry: [date or session_count]
```

### Exemplo De Work Order

```yaml
work_order_id: WO-CLAUDE1-DOC26-AUDIT-20260601-001
owner_session: claude_1
allowed_scope:
  files:
    - 07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md
    - 000_ROADMAPS/SESSION_REGISTRY.md
    - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
  actions: [read_only_audit]
forbidden_scope:
  files: [docs 01-26, docs 27-34, 00_SYSTEM_GOVERNANCE/*, ARCHITECTURE_PATCH_REPORT.md, backend, UI, API, database, migrations, MCP server, webhook, JSON n8n, real agents, runtime automations]
required_reads:
  - 07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md
expected_output: Audit findings, blockers, patch candidates, Doc 27 implications
approval_required: none
risk_ceiling: medium
roi_hypothesis: Reduces risk of premature Doc 27 creation, validates connector/MCP boundaries
checkout_lock_ref: not_required_read_only
bra_required: yes (emit BRA to Codex if patch candidates identified)
session_expiry: 2026-06-02
```

## 8. BRA Usage

### Quando BRA É Obrigatório

BRA Packet é obrigatório quando:

- Audit findings são entregues para patcher
- Mapper encontrou source files que auditor precisa revisar
- Study session criou candidates para PMO synthesis
- Executor completou release e outra sessão precisa fan-in results
- Blocker requer sessão diferente
- Risk muda allowed next action
- Sessão paralela muda scope/risk/blocker de outra sessão
- Founder decision é necessária
- Múltiplas sessões precisam do mesmo current state

### Quando BRA É Opcional

BRA Packet é opcional quando:

- Handoff é informativo, não requer ação
- Context sharing é para transparência, não para execução
- Estado é compartilhado para awareness, não para trigger

### Quando BRA É Proibido Como Autorização

BRA Packet NUNCA é:

- Checkout lock
- Approval
- Runtime queue
- Event message
- Permission para patch
- Permission para abrir Doc 27
- Permission para implementar

**Regra**: checkout_lock_ref aponta para lock state ou approval state only. Write authority vem de SESSION_REGISTRY, active checkout lock ou explicit PMO/Founder approval.

BRA Packet e Work Order `context_pack` nao sao intercambiaveis. BRA Packet e relay entre sessoes. Work Order `context_pack` e estado interno de execucao do Work Order. BRA nao substitui lock, approval ou context_pack; context_pack nao substitui BRA entre sessoes.

### Como Registrar BRA Em Texto Sem Backend

**Formato markdown**:
```yaml
bra_id: BRA-[ORIGIN]-[TARGET]-[TIMESTAMP]
timestamp: [ISO 8601]
origin_session: [session_id]
target_session: [session_id]
scope:
  allowed: [list]
  forbidden: [list]
mode: [read_only | patch_study_only | patch_auxiliary]
checkout_lock_ref: [lock_id | pending_pmo_approval | not_required_read_only]
intelligence_level: [low | medium | high | highest]
files_read: [list]
files_created: [list]
files_changed: [list]
findings: [list]
open_questions: [list]
risks: [list]
blocked_by: [type, detail]
handoff_request: [action description]
expiry: [ISO 8601]
recommended_next_action: [description]
founder_decision_required: [true | false]
roi_impact: [description]
```

**Registro**: Colocar BRA Packet em:
- Target session como prompt inicial
- Arquivo markdown temporário em `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/BRA_LOGS/` (se criado)
- SESSION_REGISTRY.md como referência em release log

## 9. Regras De Paralelismo

### O Que Pode Rodar Junto

- Múltiplas sessões read-only audit lendo os mesmos source files
- Um mapper preparando context map enquanto outro read-only auditor revisa lane diferente
- Um study note patch em arquivo locked enquanto outras sessões permanecem read-only
- Antigravity design study lendo contexto enquanto Codex patch study note diferente
- ChatGPT PMO coordenando releases enquanto execution sessions escrevem arquivos non-overlapping
- Claude 1 auditando Doc 26 enquanto Claude 2 auditando Study Layer 13
- Codex 1 patchando study note enquanto Codex 2 patchando arquivo auxiliar diferente
- Windsurf gerando prompts enquanto outras sessões executam

### O Que Deve Esperar

- Doc 27 creation
- Qualquer canonical patch em docs 10/11/12/13/18/24
- Qualquer backend, UI, API, database, migration, n8n, MCP server, webhook, agent ou runtime automation work
- Qualquer synthesis que claims final PMO decision antes de audit outputs serem released
- Qualquer memory/RAG promotion de unverified study findings
- Qualquer patch em arquivo que já tem lock ativo
- Qualquer ação que depende de audit output não released

### O Que Nunca Pode Rodar Junto

- Duas sessões escrevendo no mesmo arquivo
- Read-only audit se tornando patch session sem explicit scope change
- Session usando stale chat memory como authority
- Trae ou outro reader sendo tratado como approver
- Founder approval sendo inferred ao invés de recorded
- Patch sendo feito antes de relevant audit finishes
- Fan-out completando mas fan-in nunca happening
- Duas sessões com overlapping forbidden scope

## 10. Prompt Generator

### Template Curto Para Codex Executor

```txt
You are Codex acting as study-only patch executor for CKOS.

Mode: PATCH STUDY-ONLY
Allowed scope: [allowed files/folders]
Forbidden scope: docs 01-26, docs 27-34, 00_SYSTEM_GOVERNANCE/*, ARCHITECTURE_PATCH_REPORT.md, backend, UI, API, database, migrations, JSON n8n, real agents, runtime automations

Task: [brief task description]
Expected output: [expected deliverable]

Start with session declaration and checkout lock verification.
End with CHECKOUT RELEASE and SESSÃO FINALIZADA.
```

### Template Curto Para Codex Patch

```txt
You are Codex acting as auxiliary patch executor for CKOS.

Mode: PATCH AUXILIARY
Allowed scope: [allowed files/folders]
Forbidden scope: docs 01-26, docs 27-34, 00_SYSTEM_GOVERNANCE/*, ARCHITECTURE_PATCH_REPORT.md, backend, UI, API, database, migrations, JSON n8n, real agents, runtime automations

Task: [brief task description]
Expected output: [expected deliverable]

Start with session declaration and checkout lock verification.
End with CHECKOUT RELEASE and SESSÃO FINALIZADA.
```

### Template Curto Para Claude Auditor

```txt
You are Claude acting as PMO_CKOS + Metacognik auditor for CKOS.

Mode: READ-ONLY AUDIT
Files to read: [list of source files]
Audit questions: [list of audit questions]

Authority discipline:
- Study material can recommend, never govern
- Roadmaps can sequence, never replace canonical specs
- Memory can preserve context, never authorize implementation
- canonical_candidate means candidate, not approval

Expected output: Audit findings, blockers, patch candidates, open questions

Start with session declaration and read-only mode.
End with CHECKOUT RELEASE and SESSÃO FINALIZADA.
```

### Template Curto Para Windsurf Reader/Dispatcher

```txt
You are Windsurf acting as local PMO of support for CKOS.

Mode: SUPPORT READ-ONLY
Role: Generate prompts from vault context, manage BRA packets, coordination surface only

Allowed scope: Read vault files, generate prompts, create BRA packets
Forbidden scope: Canonical authority, Doc 27, implementation work

Task: [brief task description]
Context files: [list of files to read]

Expected output: Prompt or BRA packet

Start with session declaration and support role.
End with CHECKOUT RELEASE and SESSÃO FINALIZADA.
```

### Template Curto Para Antigravity Design Study

```txt
You are Antigravity acting as UI/UX study designer for CKOS.

Mode: DESIGN STUDY
Founder gate reference: [reference to approved gate]

Allowed outputs: Design study notes, visual/product questions with ROI/risk/cost/governance impact, evidence maps, risk lists, non-canonical recommendations
Forbidden outputs: UI implementation, frontend files, backend/API/database/migrations, runtime agent creation, JSONs n8n, canonical docs, docs 26-34

Task: [brief task description]
Expected output: [expected deliverable]

Start with session declaration and design study mode.
End with CHECKOUT RELEASE and SESSÃO FINALIZADA.
```

## 11. Kanban Operacional

### Backlog

- PMO synthesis após Claude audits
- Ghost artifact register se Claude flags implied tables, services, events ou projections
- Narrow patch candidate list para Work Orders, BRA, smart questions e notes/RAG
- Decision se notes/RAG belong em Doc 27 ou futuro Doc 28
- Decision se target-doc patches 10/11/12/13/18/24 devem preceder Doc 27
- Regularização de Layer 14 YAML/status/index/tasks

### Ready

- Claude 1 read-only audit de Doc 26 v1.0.4
- Claude 2 read-only audit de Study Layer 13 notes 01-26
- Claude 2 read-only audit de Study Layer 14 notes 06-07
- Windsurf prompt generation para Codex/Claude sessions
- ChatGPT PMO fan-in template para comparar audit releases

### In Progress

- None. Cleanup applied; next action is read-only audit.

### Waiting Audit

- Doc 26 waiting para external architectural audit antes de target-doc patches ou runtime work
- Study Layer 13 waiting para external audit antes de Doc 27 scope decision
- Study Layer 14 waiting para external audit antes de Doc 27 scope decision
- Note 25 (este arquivo) waiting para PMO/Metacognik review antes de uso operacional forte

### Waiting Founder

- Approve ou reject next 5 ou 10 tasks apenas após Work Order scope, risk ceiling, cost ceiling e fan-in audit serem stated
- Decide se Doc 27 pode abrir após Claude audit fan-in
- Decide se qualquer target-doc canonical patch deve acontecer antes de Doc 27
- Approve ou reject Antigravity Design Study Session gate

### Blocked

- Doc 27 creation está blocked até Founder/PMO gate
- Backend, UI, API, database, migrations, agents, MCP servers, webhooks, n8n JSONs e runtime automations estão blocked
- Target patches em docs 10/11/12/13/18/24 estão blocked até separadamente scoped e approved
- Long-memory ou RAG promotion de unverified study output está blocked até audit
- Antigravity está blocked até Founder-approved Design Study Session gate

### Done

- Multi-session execution policy existe
- Session registry existe
- Study Layer 13 notes 01-26 existem como study material; note 26 is index reconciliation of the former duplicate `23_LOCAL...`
- Study Layer 14 notes 01-07 existem como study material
- Doc 26 v1.0.4 existe e permanece documentation-only
- Prompt pack e BRA study existem como study-only materials
- Note 24 Doc 27 scope reconciliation existe como study-only material
- Notes 23, 25 and 26 classified as AUXILIARY OPERATIONAL, not direct Doc 27 candidates

## 12. Regra De Fan-In

**Regra**: Nenhum avanço para Doc 27 sem reunir outputs de Claude 1, Claude 2, Codex 1, Codex 2 e Windsurf.

### Fan-In Requerido Para

- Conflicting Doc 27 scope recommendations
- Ghost artifact findings across Doc 26 e Study Layer 13
- Work Order, BRA, smart question e notes/RAG candidate classification
- Decision para approve next 5 ou 10 tasks
- Qualquer move de study-only material para canonical patch candidate
- Qualquer decision sobre Doc 27 scope

### Fan-In Process

1. Claude 1 emite CHECKOUT RELEASE com audit findings de Doc 26
2. Claude 2 emite CHECKOUT RELEASE com audit findings de Study Layer 13 e Layer 14
3. Codex 1 emite CHECKOUT RELEASE se patches foram aplicados
4. Codex 2 emite CHECKOUT RELEASE se reconciliações foram aplicadas
5. Windsurf emite CHECKOUT RELEASE com BRA packets gerados
6. ChatGPT PMO coleta todos os CHECKOUT RELEASEs
7. ChatGPT PMO identifica conflitos, blockers e candidatos
8. ChatGPT PMO cria synthesis memo
9. ChatGPT PMO apresenta synthesis para Founder com decision framing
10. Founder decide com explicit approval/rejection

### Sem Fan-In, Sem Avanço

Se fan-in não acontece:
- Doc 27 permanece BLOCKED
- Qualquer canonical patch permanece BLOCKED
- Qualquer decision de scope permanece pendente
- Work Orders permanecem em Waiting Founder

## 13. Estratégia Para Não Ficar Preso Em Documentação

### Quando Documentação Basta

- Quando conceito é study-only e não requer implementação imediata
- Quando roadmap é guidance, não canonical spec
- Quando memory é contexto, não authority
- Quando candidate é recommendation, não approval
- Quando BRA é handoff, não permission

### Quando Precisa Virar Canonical Doc

- Quando conceito foi auditado e aprovado por Founder/PMO/Metacognik
- Quando conceito afeta architecture de sistema
- Quando conceito requer implementation consistency
- Quando conceito é dependency de outros docs
- Quando conceito é boundary para runtime

### Quando Precisa Virar Backend

- Quando conceito foi aprovado como implementation readiness
- Quando Founder/PMO/Technical/Metacognik aprovam implementation gate
- Quando canonical docs estão estáveis e auditados
- Quando ROI justifica custo de implementation
- Quando risk é aceitável e mitigável

### Quando Precisa Virar UI

- Quando product requirements são claros e estáveis
- Quando UX patterns foram estudados e aprovados
- Quando backend APIs existem e são estáveis
- Quando Founder/PMO/Product aprovam UI gate
- Quando ROI justifica custo de UI development

### Quando Deve Ser Descartado

- Quando conceito é over-engineered para valor atual
- Quando conceito não tem ROI claro
- Quando conceito duplica outro conceito existente
- Quando conceito é implementation-adjacente sem approval
- Quando conceito é study material que não passou audit

### Anti-Patterns Para Evitar

- Criar novos study notes sem audit dos anteriores
- Tratar roadmap como authority
- Tratar memory como decision log
- Tratar candidate como approval
- Tratar BRA como permission
- Criar docs 27-34 sem gate
- Implementar sem canonical docs
- Criar UI sem product requirements
- Criar backend sem architecture approval
- Criar automações sem governance

## 14. Próximo Lote Recomendado

### Claude 1: Audit Doc 26 v1.0.4

**Prompt**:
```txt
You are Claude acting as PMO_CKOS + Metacognik auditor for CKOS.

Mode: READ-ONLY AUDIT
Files to read:
- 07_EVOLUTION_SYSTEM/26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md
- 000_ROADMAPS/SESSION_REGISTRY.md
- 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md

Audit questions:
1. Are P26-1 through P26-8 patches correctly scoped as candidates only, not applied?
2. Does Doc 26 correctly position connectors, MCP, webhooks and secret_refs as governed access surfaces?
3. Are there any ghost tables, services, events or projections implied?
4. Are there any dependencies on docs 10/11/12/13/18/24 that are unresolved?
5. Is Doc 26 ready for target-doc patches or does it need more work?

Expected output: Audit findings, blockers, patch candidates, open questions

Start with session declaration and read-only mode.
End with CHECKOUT RELEASE and SESSÃO FINALIZADA.
```

### Claude 2: Audit Study Layer 13 + Layer 14

**Prompt**:
```txt
You are Claude acting as PMO_CKOS + Metacognik auditor for CKOS.

Mode: READ-ONLY AUDIT
Files to read:
- 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md
- 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/15_PARALLEL_WORK_ORDERS_AND_BATCH_EXECUTION_STUDY.md
- 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/21_BRA_BRIEFING_RELAY_ARCHITECTURE_STUDY.md
- 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/22_MULTI_SESSION_EXECUTION_ROADMAP_AND_SPRINT_BOARD_STUDY.md
- 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/23_MULTI_MODEL_COMMAND_AND_PROMPT_DISPATCH_BOARD_STUDY.md
- 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/24_DOC27_SCOPE_RECONCILIATION_AND_GATE_PROPOSAL_STUDY.md
- 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/25_LOCAL_OPERATOR_CONTROL_ROOM_AND_AUTONOMOUS_DISPATCH_STUDY.md
- 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/26_LOCAL_PMO_MULTI_MODEL_CONTROL_ROOM_STUDY.md
- 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/06_CKOS_ADOPTION_CANDIDATES_FOR_DOC27_STUDY.md
- 000_STUDY_NOTES/14_PAPERCLIP_AGENT_OPERATING_MODEL/07_PAPERCLIP_TO_CKOS_TRANSLATION_MATRIX_STUDY.md

Audit questions:
1. Is note 24's recommended Doc 27 scope (Work Orders and Multi-Session Orchestration) narrow enough?
2. Is the Doc 28 split (Notes/RAG to future Doc 28) sufficient to protect scope?
3. Are Paperclip concepts correctly positioned as study guardrails, not runtime blueprint?
4. Are there any candidates that are too implementation-adjacent for Doc 27?
5. Are Work Order, BRA and Founder approval concepts ready for canonical promotion?

Expected output: Audit findings, blockers, Doc 27 gate recommendation, candidate classification

Start with session declaration and read-only mode.
End with CHECKOUT RELEASE and SESSÃO FINALIZADA.
```

### Codex 1: Aguardar Auditoria Ou Executar Patches Autorizados

**Posture**: WAITING FOR AUDIT

**Rationale**: Codex 1 não deve executar patches até Claude audits estejam completos e PMO fan-in tenha acontecido.

**Safe action now**: Read-only review de existing study notes, preparação de context maps, nenhum patch.

### Codex 2: Aguardar Auditoria Ou Reconciliar Outputs

**Posture**: WAITING FOR AUDIT

**Rationale**: Codex 2 não deve executar reconciliações até Claude audits estejam completos e PMO fan-in tenha acontecido.

**Safe action now**: Read-only review de existing study notes, preparação de context maps, nenhum patch.

### Windsurf: Manter Dispatch Board E Gerar Prompts Curtos

**Prompt**:
```txt
You are Windsurf acting as local PMO of support for CKOS.

Mode: SUPPORT READ-ONLY
Role: Maintain dispatch board, generate short prompts for Codex and Claude, manage BRA packets

Task: After Claude audits are complete, generate short prompts for next actions based on audit findings.

Context files to read:
- 000_ROADMAPS/SESSION_REGISTRY.md
- 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/25_LOCAL_OPERATOR_CONTROL_ROOM_AND_AUTONOMOUS_DISPATCH_STUDY.md

Expected output: Short prompts for Codex/Claude based on audit outputs

Start with session declaration and support role.
End with CHECKOUT RELEASE and SESSÃO FINALIZADA.
```

## 15. CHECKOUT RELEASE

```txt
CHECKOUT RELEASE
session: windsurf_local_operator_control_room_dispatch
mode: patch study-only
allowed_scope:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/25_LOCAL_OPERATOR_CONTROL_ROOM_AND_AUTONOMOUS_DISPATCH_STUDY.md
files_created:
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/25_LOCAL_OPERATOR_CONTROL_ROOM_AND_AUTONOMOUS_DISPATCH_STUDY.md
files_changed:
  - none
files_not_touched:
  - docs 01-26
  - docs 27-34
  - 00_SYSTEM_GOVERNANCE/*
  - ARCHITECTURE_PATCH_REPORT.md
  - auxiliary maps
  - backend
  - UI
  - API
  - database
  - migrations
  - MCP server real
  - webhook real
  - JSON n8n
  - real agents
  - runtime automations
validation:
  - created only the requested study-only control room note
  - included boundary study-only
  - included current ecosystem state (Doc 26, Layer 13, Layer 14, Doc 27 blocked)
  - included machine map (Machine 1: Claude Code, Codex 1, ChatGPT PMO; Machine 2: Antigravity/Gemini, Claude Design, Codex 2, Windsurf)
  - included active session map (Codex 1, Codex 2, Claude 1, Claude 2, Windsurf, Antigravity, ChatGPT PMO)
  - included session validity system (when to declare SESSÃO FINALIZADA, when to emit re-entry prompt, when to emit BRA Packet, when to stop for context excess)
  - included Founder minimal-contact commands (/status, /next5, /next10, /blocked, /audit, /dispatch, /fan-in, /open-gate, /close-session, /resume-session)
  - included local Work Order schema (work_order_id, owner_session, allowed_scope, forbidden_scope, required_reads, expected_output, approval_required, risk_ceiling, roi_hypothesis, checkout_lock_ref, bra_required, session_expiry)
  - included BRA usage (when mandatory, when optional, when prohibited as authorization, how to register in text without backend)
  - included parallelism rules (what can run together, what must wait, what never can run together)
  - included prompt generator (short templates for Codex executor, Codex patch, Claude auditor, Windsurf reader/dispatcher, Antigravity design study)
  - included operational Kanban (Backlog, Ready, In Progress, Waiting Audit, Waiting Founder, Blocked, Done)
  - included fan-in rule (no Doc 27 advancement without Claude 1, Claude 2, Codex 1, Codex 2 and Windsurf outputs)
  - included strategy to avoid getting stuck in documentation (when documentation suffices, when to turn into canonical doc, when to turn into backend, when to turn into UI, when to discard)
  - included next recommended batch (Claude 1 audit Doc 26, Claude 2 audit Layer 13 + Layer 14, Codex 1/2 waiting, Windsurf maintain dispatch board)
  - preserved Doc 27 as blocked
  - no implementation, UI, API, database, migrations, MCP server, webhook, JSON n8n, real agents or runtime automations created
risks_remaining:
  - this note still requires PMO/Metacognik audit before strong operational use
  - control room commands are markdown convention only, not real backend
  - Doc 27 remains blocked until explicit Founder/PMO checkout
  - parallel sessions may still diverge if they do not use registry, BRA packets and fan-in release
next_step:
  - Claude PMO read-only audit of this cleanup
  - PMO fan-in with Claude findings before any Founder Doc 27 gate decision
status: released_as_study_note_only
```
