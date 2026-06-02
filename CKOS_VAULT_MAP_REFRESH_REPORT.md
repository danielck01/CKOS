---
title: CKOS Vault Map Refresh Report
system_id: ckos_vault_map_refresh_report
category: governance_report
status: draft
version: 1.5.0
owner: docs_architect_agent
reviewers:
  - founder
  - pmo_ckos
  - metacognik
related_notes:
  - CKOS_FOLDER_MEMORY.md
  - CKOS_FILETREE_MAP.md
  - ARCHITECTURE_PATCH_REPORT.md
  - QA_DOCUMENTATION_CHECKLIST.md
  - 000_UPGRADE/CKOS_UPGRADE_INDEX.md
  - 000_UPGRADE/CKOS_CONTINUATION_PLAN.md
  - 000_UPLOADS/00_UPLOADS_INDEX.md
  - 000_STUDY_NOTES/00_STUDY_INDEX.md
  - 000_ROADMAPS/README.md
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
  - 000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/README.md
created_for: CKOS_DOCUMENTATION_REVIEWED
---

# CKOS Vault Map Refresh Report

## 1. Data da auditoria

Auditoria executada em 2026-05-26.

Complemento de microgate executado em 2026-05-27 para criacao controlada de `000_UPLOADS/` e `000_STUDY_NOTES/` apos aprovacao Founder.

Complemento de microgate executado em 2026-05-27 para resolucao do conflito Self-Evolving: `07_EVOLUTION_SYSTEM/` foi criada, `25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` foi criado em draft, e `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` foi preservado como historico/superseded. ROI permanece doc 21.

Complemento P0 executado em 2026-05-28 para estabilizacao de `000_ROADMAPS/` como camada auxiliar governada. A camada recebeu controles raiz, YAML normalizado e registro nos mapas auxiliares. Ela nao e canonica e nao autoriza implementacao.

Complemento STUDY executado em 2026-05-28 para criacao de `000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md`. A nota registra um padrao AI First auxiliar de intencao, perguntas inteligentes, plano, approval, execucao controlada e memoria. Ela nao e canonica e nao autoriza implementacao.

Complemento P1.7 executado em 2026-05-28 para criar politica auxiliar de execucao multi-sessao, registry de sessoes e gate Antigravity Study Mode. O patch e auxiliar governado, nao canonico, nao autoriza implementacao, nao cria docs 26-34, nao atualiza `ARCHITECTURE_PATCH_REPORT.md` e nao inicia Antigravity.

Complemento P1.7.1 executado em 2026-05-28 para aplicar refresh minimo apos auditoria PMO/Metacognik. O refresh promoveu os tres arquivos principais de P1.7 para v1.0.0, adicionou a frase obrigatoria da politica, criou `12_SESSION_GATES/ck_memory.md`, preservou `_folder_memory.md` como legacy/superseded e registrou P1.7/P1.7.1 em `ARCHITECTURE_PATCH_REPORT.md`.

Complemento UI/UX Visual Reference Study executado em 2026-05-28 para a criação de `01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md`, `02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md`, `03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md`, `04_MOBILE_COMMAND_FIRST_ERGONOMICS.md`, `05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md`, `06_UIUX_ANTI_PATTERNS_AND_GENERIC_AI_UI_RISKS.md` e `ck_memory.md` sob `000_STUDY_NOTES/10_UIUX_STUDIES/`, traduzindo referências visuais em linguagem de runtime baseada em agentes, sem código.

Complemento UI/UX Audit Patch executado em 2026-05-28 para a eliminação sistemática de referências a "Project Pulse", expansão de neurodesign para exatamente 8 princípios cognitivos, anti-padrões para exatamente 10 e a criação das notas de estudo `07_AGENT_ACTIVITY_STREAM_UIUX_STUDY.md` e `08_WHITELABEL_TOKEN_SYSTEM_UIUX_STUDY.md`.

Complemento UI/UX Operational Patterns Study executado em 2026-05-28 para a criação das notas de estudo `09_EXECUTION_PLAN_WIDGET_UIUX_STUDY.md`, `10_INTENT_CLARIFIER_AND_SMART_QUESTIONS_UIUX_STUDY.md`, `11_COST_CREDITS_AND_ROI_AWARE_UX_STUDY.md`, `12_APPROVAL_GATE_AND_REVERSIBILITY_UX_STUDY.md` e `13_EVIDENCE_TRUST_AND_DECISION_UIUX_STUDY.md` sob `000_STUDY_NOTES/10_UIUX_STUDIES/`, detalhando os padrões conceituais de widgets e UX para planos de execução, perguntas inteligentes, wallets/créditos, portões de aprovação e mapas de evidências, sem código ou implementação visual.

Complemento Study Layer 13 AI-first Project Operating System executado em 2026-05-30 para a criacao de `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/` com 21 arquivos auxiliares de estudo e controle sobre Project AI-first, Task AI-first, Notes AI-first, perguntas inteligentes, briefing-to-tasks, approval batch, ROI, feedback, learning, RAG metadata e candidatos para Doc 27. A camada e study-only, nao canonica, nao cria docs 27-34, nao altera docs 01-26 e nao autoriza implementacao.

Observacao sobre datas: o filesystem disponibilizou `CreationTime` e `LastWriteTime`. Em alguns packs importados, `CreationTime` e posterior ao `LastWriteTime`, indicando copia/importacao local. Portanto, usei `CreationTime` para detectar chegada local de arquivos e `LastWriteTime` + `ARCHITECTURE_PATCH_REPORT.md` para entender ordem documental. Quando houver divergencia, o patch report e o conteudo canonico prevalecem.

## 2. Metodo usado

- Filetree completa via `rg --files`.
- Timestamps via `Get-ChildItem -Recurse -File`.
- Cruzamento com `ARCHITECTURE_PATCH_REPORT.md` v1.9.0.
- Cruzamento com `CKOS_FOLDER_MEMORY.md`.
- Cruzamento com `000_UPGRADE/CKOS_UPGRADE_INDEX.md`.
- Cruzamento com packs em `000_UPGRADE`.

## 3. Filetree resumido

```txt
CKOS_DOCUMENTATION_REVIEWED/
|-- ARCHITECTURE_PATCH_REPORT.md
|-- QA_DOCUMENTATION_CHECKLIST.md
|-- CKOS_FOLDER_MEMORY.md
|-- CKOS_VAULT_MAP_REFRESH_REPORT.md
|-- Memória GPT.md
|-- 000_UPLOADS/
|-- 000_STUDY_NOTES/
|   `-- 13_AI_FIRST_PROJECT_OPERATING_SYSTEM/
|-- 000_ROADMAPS/
|-- 00_SYSTEM_GOVERNANCE/
|-- 01_THINKING_SYSTEM/
|-- 02_EXECUTION_SYSTEM/
|-- 03_RUNTIME_SYSTEM/
|-- 04_PRODUCT_SYSTEM/
|-- 05_IMPLEMENTATION_SYSTEM/
|-- 06_BUSINESS_SYSTEMS/
|-- 07_EVOLUTION_SYSTEM/
`-- 000_UPGRADE/
    |-- CKOS_CODEX_MEMORY.md
    |-- CKOS_INFRA_AUTOMATION_MEMORY.md
    |-- CKOS_RESEARCH_MEMORY.md
    |-- CKOS_UPGRADE_INDEX.md
    |-- CKOS_CONTINUATION_PLAN.md
    |-- CKOS_CODEX_CONTINUATION_PACK/
    |-- ckos_digitalocean_n8n_pack/
    `-- pack_notas_ckos_deep_research/
```

## 4. Arquivos novos detectados

Nova Study Layer criada em 30/05/2026:

- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/README.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_tasks.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_risks.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_roi.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_feedback.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_agent_handoffs.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/01_PROJECT_AI_FIRST_OPERATING_MODEL.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/02_INTELLIGENT_QUESTION_SYSTEM_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/03_BRIEFING_TO_TASKS_TRANSFORMER_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/04_NOTES_AS_OPERATIONAL_MEMORY_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/05_TASK_AI_FIRST_SYSTEM_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/06_SUPERAGENT_AGENT_SUBAGENT_WORK_ALLOCATION_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/07_PARALLEL_EXECUTION_AND_CHECKOUT_LOCK_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/08_FOUNDER_APPROVAL_BATCH_CONTROL_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/09_ROI_AWARE_TASKS_NOTES_AND_QUESTIONS_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/10_FEEDBACK_TO_LEARNING_LOOP_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/11_PROJECT_SELF_DOCUMENTATION_SYSTEM_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/12_RAG_METADATA_AND_VECTOR_CATEGORY_STUDY.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md`
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/14_ACCEPTANCE_CRITERIA_FOR_DOC27.md`

Escopo da Study Layer 13:

- Estuda Project AI-first, Task AI-first, Notes AI-first e perguntas inteligentes antes de qualquer Doc 27.
- Registra candidatos para Doc 27 apenas como material auxiliar, sem canonizacao.
- Docs 01-26 nao foram alterados por esta sessao.
- Docs 27-34 nao foram criados.
- UI, backend, API, banco, migrations, MCP server real, JSONs n8n, agentes reais e automacoes runtime nao foram iniciados.

Novo arquivo STUDY criado em 28/05/2026:

- `000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md`

Escopo da study note:

- Define o padrao Intent -> Question -> Plan -> Execution.
- Diferencia pergunta comum de pergunta inteligente CKOS.
- Registra tipos de perguntas, modelo de pergunta inteligente, exemplo de intencao minima e anti-patterns.
- Nao cria docs canonicos.
- Docs 26-34 nao foram criados.
- UI/UX, backend, migrations, API, banco, agentes reais, JSONs n8n e Antigravity nao foram iniciados.

Novos arquivos operacionais criados em 28/05/2026 no P0 Roadmaps:

- `000_ROADMAPS/ck_memory.md`
- `000_ROADMAPS/ck_tasks.md`
- `000_ROADMAPS/ck_risks.md`
- `000_ROADMAPS/ck_roi.md`
- `000_ROADMAPS/ck_feedback.md`
- `000_ROADMAPS/ck_agent_handoffs.md`

Escopo do P0 Roadmaps:

- `000_ROADMAPS/` registrada como camada auxiliar governada, nao canonica.
- YAML de `000_ROADMAPS/**/*.md` normalizado para padrao auxiliar snake_case.
- `05_SUPERAGENTS_AGENTS_SUBAGENTS_ROADMAP/` mantida sem rename.
- Nenhum doc canonico criado.
- Docs 26-34 nao foram criados.
- UI/UX, backend, migrations, API, banco, agentes reais, JSONs n8n e Antigravity nao foram iniciados.

Complemento P1/P1.5/P1.6 Roadmaps em 28/05/2026:

- P1 criou os roadmaps auxiliares `14_RUNTIME_BACKEND_ROADMAP/` a `21_LEARNING_AND_KNOWLEDGE_ROADMAP/`.
- P1.5 criou `000_ROADMAPS/ROADMAP_RECONCILIATION_REPORT.md`.
- P1.6 criou `000_ROADMAPS/ROADMAP_ROUTING_MATRIX.md`.
- P1.6 corrigiu caracteres NUL nos READMEs dos roadmaps `14-21`.
- Pares `02/14`, `06/15`, `07/16` e `10/17` agora possuem roteamento auxiliar recomendado.
- `03/19`, `04/18`, `05/20` e `08/21` foram classificados como pares fonte/wrapper sem rename, move ou delete.
- Antigravity continua bloqueado ate handoff de Study Mode restrito aprovado.
- Contagem apos P1.6: 736 arquivos incluindo metadados ocultos, 701 Markdown, 29 JSON, 13 diretorios de topo; `000_ROADMAPS/` contem 157 Markdown.

Complemento P1.7 Multi-Session Execution Policy em 28/05/2026:

- `000_ROADMAPS/SESSION_REGISTRY.md` criado primeiro.
- `000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md` criado.
- `000_STUDY_NOTES/12_SESSION_GATES/` criado.
- `000_STUDY_NOTES/12_SESSION_GATES/README.md` criado.
- `000_STUDY_NOTES/12_SESSION_GATES/_folder_memory.md` criado.
- `000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md` criado.
- P1.7 registrou session types, checkout lock/release, permissoes por camada, intelligence levels e regra de perguntas com impacto em ROI, risco, custo ou governanca.
- Antigravity permanece bloqueado ate gate formal aprovado pelo Founder em sessao futura `design_study`.
- Contagem apos P1.7: 741 arquivos incluindo metadados ocultos, 706 Markdown, 29 JSON, 13 diretorios de topo; `000_ROADMAPS/` contem 159 Markdown e `000_STUDY_NOTES/` contem 37 Markdown.

Complemento P1.7.1 Memory Refresh em 28/05/2026:

- `000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md`, `000_ROADMAPS/SESSION_REGISTRY.md` e `000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md` promovidos para `version: 1.0.0`.
- Frase obrigatoria de checkout lock/release adicionada ao inicio do corpo de `MULTI_SESSION_EXECUTION_POLICY.md`.
- `000_STUDY_NOTES/12_SESSION_GATES/ck_memory.md` criado como memoria ativa.
- `000_STUDY_NOTES/12_SESSION_GATES/_folder_memory.md` preservado como legacy/superseded.
- `ARCHITECTURE_PATCH_REPORT.md` atualizado com secao P1.7/P1.7.1.
- Docs 26-34 nao foram criados; UI/UX, backend, API, banco, migrations, JSONs n8n, agentes reais, Antigravity e Design Study continuam bloqueados.
- Contagem apos P1.7.1: 742 arquivos incluindo metadados ocultos, 707 Markdown, 29 JSON, 13 diretorios de topo; `000_ROADMAPS/` contem 159 Markdown e `000_STUDY_NOTES/` contem 38 Markdown.

Novos arquivos operacionais criados em 27/05/2026 no microgate RAW/STUDY:

- `000_UPLOADS/README.md`
- `000_UPLOADS/_folder_memory.md`
- `000_UPLOADS/00_UPLOADS_INDEX.md`
- READMEs e `_folder_memory.md` em todas as subpastas de `000_UPLOADS/`.
- `000_STUDY_NOTES/README.md`
- `000_STUDY_NOTES/_folder_memory.md`
- `000_STUDY_NOTES/00_STUDY_INDEX.md`
- `000_STUDY_NOTES/_templates/*`
- READMEs e `_folder_memory.md` em todas as subpastas de `000_STUDY_NOTES/`.

Escopo do microgate:

- Nenhum doc canonico 01-24 alterado.
- Nenhum arquivo movido.
- Nenhum arquivo deletado.
- Nenhum Self-Evolving renomeado.
- Nenhum JSON n8n alterado.
- Nenhum backend, UI, migration, API, banco ou agente criado.

Novos arquivos operacionais criados em 26/05/2026:

- `CKOS_FOLDER_MEMORY.md`
- `CKOS_VAULT_MAP_REFRESH_REPORT.md`
- `CKOS_FILETREE_MAP.md`
- `000_UPGRADE/CKOS_CODEX_MEMORY.md`
- `000_UPGRADE/CKOS_INFRA_AUTOMATION_MEMORY.md`
- `000_UPGRADE/CKOS_RESEARCH_MEMORY.md`
- `000_UPGRADE/CKOS_UPGRADE_INDEX.md`
- `000_UPGRADE/CKOS_CONTINUATION_PLAN.md`

Packs importados/copiadados em 26/05/2026:

- `000_UPGRADE/CKOS_CODEX_CONTINUATION_PACK/`
- `000_UPGRADE/pack_notas_ckos_deep_research/`
- `000_UPGRADE/ckos_digitalocean_n8n_pack/`

## 5. Arquivos modificados recentemente

Modificados em 25/05/2026 e relevantes para o estado atual:

- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`
- `06_BUSINESS_SYSTEMS/22_FEEDBACK_SYSTEM_ARCHITECTURE.md`
- `06_BUSINESS_SYSTEMS/23_SUPPORT_SYSTEM_ARCHITECTURE.md`
- `06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`
- `ARCHITECTURE_PATCH_REPORT.md`
- `05_IMPLEMENTATION_SYSTEM/17_IMPLEMENTATION_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`
- docs 10-16 em Runtime/Product System.

Modificados em 26/05/2026:

- memorias e indices de `000_UPGRADE`;
- `CKOS_FOLDER_MEMORY.md`;
- `CKOS_VAULT_MAP_REFRESH_REPORT.md`;
- `Memória GPT.md` foi modificado recentemente e precisa classificacao.

## 6. Arquivos canonicos por pasta

### Raiz

- `ARCHITECTURE_PATCH_REPORT.md`
- `QA_DOCUMENTATION_CHECKLIST.md`

### 00_SYSTEM_GOVERNANCE

- `00_README_SYSTEM_GOVERNANCE.md`
- `00_MASTER_MAP.md`
- `00_DOCUMENT_TEMPLATE.md`
- `00_TAXONOMY_AND_NAMING.md`
- `00_DEPENDENCY_MAP.md`

### 01_THINKING_SYSTEM

- `00_README_THINKING_SYSTEM.md`
- `01_CKOS_AI_FIRST_CONSTITUTION.md`
- `02_AI_FIRST_OBJECT_MODEL.md`
- `03_AGENT_OPERATING_MODEL.md`
- `04_AUTONOMY_AND_APPROVALS.md`
- `05_MEMORY_AND_CONTEXT_ARCHITECTURE.md`

### 02_EXECUTION_SYSTEM

- `00_README_EXECUTION_SYSTEM.md`
- `06_SKILLS_REGISTRY.md`
- `07_WORKFLOW_BLUEPRINTS.md`
- `08_PROMPT_LIBRARY.md`
- `09_TRANSFORMERS_AND_PIPELINES.md`

### 03_RUNTIME_SYSTEM

- `00_README_RUNTIME_SYSTEM.md`
- `10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `11_DATA_MODEL_AND_PERSISTENCE.md`
- `12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`
- `13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`

### 04_PRODUCT_SYSTEM

- `00_README_PRODUCT_SYSTEM.md`
- `14_PROJECT_DASHBOARD_ARCHITECTURE.md`
- `15_COMMAND_CENTER_ARCHITECTURE.md`
- `16_NODE_CANVAS_ARCHITECTURE.md`

### 05_IMPLEMENTATION_SYSTEM

- `00_README_IMPLEMENTATION_SYSTEM.md`
- `17_IMPLEMENTATION_PROTOCOL.md`
- `18_RESEARCH_PROTOCOL.md`
- `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`
- `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`

### 06_BUSINESS_SYSTEMS

- `21_ROI_ARCHITECTURE.md`
- `22_FEEDBACK_SYSTEM_ARCHITECTURE.md`
- `23_SUPPORT_SYSTEM_ARCHITECTURE.md`
- `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`

Status dos docs 21-24: documentalmente concluidos, aguardando aprovacao formal Founder + Technical + Metacognik.

## 7. Arquivos auxiliares por pasta

### Raiz

- `CKOS_FOLDER_MEMORY.md`
- `CKOS_VAULT_MAP_REFRESH_REPORT.md`
- `Memória GPT.md` (pendente de classificacao)

### 000_UPGRADE

- `Bem-vindo.md`
- `CKOS_CODEX_MEMORY.md`
- `CKOS_INFRA_AUTOMATION_MEMORY.md`
- `CKOS_RESEARCH_MEMORY.md`
- `CKOS_UPGRADE_INDEX.md`
- `CKOS_CONTINUATION_PLAN.md`
- `CKOS_CODEX_CONTINUATION_PACK/*`
- `ckos_digitalocean_n8n_pack/*`
- `pack_notas_ckos_deep_research/*`

### 000_UPLOADS

- `README.md`
- `_folder_memory.md`
- `00_UPLOADS_INDEX.md`
- subpastas RAW com README e `_folder_memory.md`

### 000_STUDY_NOTES

- `README.md`
- `_folder_memory.md`
- `00_STUDY_INDEX.md`
- `_templates/*`
- `11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md`
- `12_SESSION_GATES/README.md`
- `12_SESSION_GATES/ck_memory.md`
- `12_SESSION_GATES/_folder_memory.md`
- `12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md`
- `10_UIUX_STUDIES/ck_memory.md`
- `10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md`
- `10_UIUX_STUDIES/02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md`
- `10_UIUX_STUDIES/03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md`
- `10_UIUX_STUDIES/04_MOBILE_COMMAND_FIRST_ERGONOMICS.md`
- `10_UIUX_STUDIES/05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md`
- `10_UIUX_STUDIES/06_UIUX_ANTI_PATTERNS_AND_GENERIC_AI_UI_RISKS.md`
- subpastas STUDY com README e memoria de pasta; `12_SESSION_GATES/` e `10_UIUX_STUDIES/` usam `ck_memory.md` como memoria ativa.

### 000_ROADMAPS

- `README.md`
- `ck_memory.md`
- `ck_tasks.md`
- `ck_risks.md`
- `ck_roi.md`
- `ck_feedback.md`
- `ck_agent_handoffs.md`
- `SESSION_REGISTRY.md`
- `MULTI_SESSION_EXECUTION_POLICY.md`
- `ROADMAP_RECONCILIATION_REPORT.md`
- `ROADMAP_ROUTING_MATRIX.md`
- subpastas de roadmaps vivos `00_MASTER_ROADMAP/` a `21_LEARNING_AND_KNOWLEDGE_ROADMAP/`

## 8. Arquivos superseded/historicos

Confirmados como superseded/historicos ou recomendados para classificacao:

- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md`: variante Manus; conflitante com decisao de que Manus nao e infraestrutura do CKOS.
- `05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md`: protocolo anterior sem Antigravity; provavelmente superseded por `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`.
- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`: superseded/historico; arquitetura ativa recriada em `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`.
- Roadmaps do `CKOS_CODEX_CONTINUATION_PACK` que tratam docs 22-24 como pendentes.

## 9. Ambiguidades de numeracao

Conflito Self-Evolving/ROI resolvido em 2026-05-27:

- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`
- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`
- `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`

Resolucao:

- ROI permanece doc 21 em `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`.
- Self-Evolving ativo passa a ser doc 25 em `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`.
- O arquivo antigo nao foi movido, renomeado ou deletado; foi marcado como superseded.
- Referencias diretas permitidas foram atualizadas para o doc 25.

## 10. Gaps de taxonomia

- Docs 26-34 ainda nao foram criados.
- `21_SELF_EVOLVING_SYSTEM.md` tem status final de superseded/historico.
- `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` e o doc ativo para Self-Evolving.
- `000_UPGRADE` contem notas 25-29, mas elas sao auxiliares, nao canonicas.
- `Memória GPT.md` nao tem classificacao documental.
- `QA_DOCUMENTATION_CHECKLIST.md` ainda nao reflete todo o estado Product/Implementation/Business.
- Master Map/Dependency Map podem precisar patch apos decisao de taxonomia.

## 11. Patches recomendados

P0 apos microgate RAW/STUDY:

- Decidir quando atualizar `00_MASTER_MAP.md`, `00_DOCUMENT_TEMPLATE.md`, `00_TAXONOMY_AND_NAMING.md`, `00_DEPENDENCY_MAP.md` e `ARCHITECTURE_PATCH_REPORT.md` para refletir oficialmente as camadas RAW/STUDY.
- Manter a regra: nada entra no canonico sem passar por STUDY.
- Usar templates de `000_STUDY_NOTES/_templates/` antes de qualquer patch candidate.

P0:

- Microgate de `26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md` executado; Doc 26 criado em `07_EVOLUTION_SYSTEM/`.
- Marcar packs antigos como auxiliares/desatualizados onde dizem que 22-24 faltam.
- Impedir que agentes usem `CKOS_CODEX_CONTINUATION_PACK/06_ROADMAP/*` como roadmap atual sem refresh.

P1:

- Atualizar mapas apenas por microgate aprovado.
- Usar `ROADMAP_ROUTING_MATRIX.md` antes de escolher entre roadmaps antigos e novos.
- Preparar Antigravity somente por `design_study` restrito com gate formal Founder aprovado.
- Registrar refresh no `ARCHITECTURE_PATCH_REPORT.md` por patch especifico.
- Expandir `QA_DOCUMENTATION_CHECKLIST.md` para cobrir docs 14-24.
- Auditar P1.7 antes de qualquer ativacao Antigravity.

P2:

- Classificar `Memória GPT.md`.
- Consolidar notas de pesquisa uteis em backlog de Deep Research, sem implementacao.

## 12. Proximo passo sugerido

Proxima acao exata apos P1.7: auditar `SESSION_REGISTRY.md`, `MULTI_SESSION_EXECUTION_POLICY.md` e `12_SESSION_GATES/` em PMO/Metacognik. Depois, Founder decide se abre uma sessao futura `design_study` para Antigravity ou P2 para expansao de lanes antes do estudo visual.

Sequencia segura:

1. Ler `SESSION_REGISTRY.md`, `MULTI_SESSION_EXECUTION_POLICY.md` e `ROADMAP_ROUTING_MATRIX.md`.
2. Preparar Antigravity apenas em `design_study` restrito, com gate Founder aprovado e sem execucao.
3. Qualquer canonizacao futura deve passar por patch candidate, QA documental e approval Founder.

Recomendacao PMO: manter MCP, conectores e integracoes antes de UI/UX canonico, sempre passando por policy, tool routing, cost guard, audit logs, tenant isolation e secret refs.

## 13. Arquivos analisados

Analisados por filetree e leitura/cross-check:

- raiz do vault;
- `00_SYSTEM_GOVERNANCE/`;
- `01_THINKING_SYSTEM/`;
- `02_EXECUTION_SYSTEM/`;
- `03_RUNTIME_SYSTEM/`;
- `04_PRODUCT_SYSTEM/`;
- `05_IMPLEMENTATION_SYSTEM/`;
- `06_BUSINESS_SYSTEMS/`;
- `000_UPGRADE/`;
- `000_UPGRADE/CKOS_CODEX_CONTINUATION_PACK/`;
- `000_UPGRADE/ckos_digitalocean_n8n_pack/`;
- `000_UPGRADE/pack_notas_ckos_deep_research/`.

## 14. Arquivos alterados neste refresh

- `CKOS_FOLDER_MEMORY.md`
- `000_UPGRADE/CKOS_UPGRADE_INDEX.md`
- `000_UPGRADE/CKOS_CONTINUATION_PLAN.md`
- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`
- `000_UPGRADE/CKOS_CODEX_MEMORY.md`
- `000_UPGRADE/CKOS_INFRA_AUTOMATION_MEMORY.md`
- `000_UPGRADE/CKOS_RESEARCH_MEMORY.md`
- `CKOS_VAULT_MAP_REFRESH_REPORT.md`

## 15. Arquivos criados neste refresh

- `CKOS_VAULT_MAP_REFRESH_REPORT.md`
- `CKOS_FILETREE_MAP.md`

## 16. Arquivos nao alterados

- Docs canonicos 10-24.
- `ARCHITECTURE_PATCH_REPORT.md`.
- `QA_DOCUMENTATION_CHECKLIST.md`.
- `00_DEPENDENCY_MAP.md`.
- `00_MASTER_MAP.md`.
- `00_DOCUMENT_TEMPLATE.md`.
- `00_TAXONOMY_AND_NAMING.md`.
- `21_SELF_EVOLVING_SYSTEM.md` (agora superseded/historico).
- JSONs n8n.
- Qualquer codigo, UI, backend, migration ou agente runtime.

## 16.1 Arquivos alterados no microgate RAW/STUDY 2026-05-27

- `CKOS_FILETREE_MAP.md`
- `CKOS_FOLDER_MEMORY.md`
- `CKOS_VAULT_MAP_REFRESH_REPORT.md`
- `000_UPGRADE/CKOS_UPGRADE_INDEX.md`
- `000_UPGRADE/CKOS_CODEX_MEMORY.md`

Arquivos canonicos bloqueados nao foram alterados neste microgate.

## 16.2 Arquivos alterados no microgate Self-Evolving 2026-05-27

- `07_EVOLUTION_SYSTEM/00_README_EVOLUTION_SYSTEM.md` criado.
- `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` criado.
- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` marcado como superseded.
- Mapas e referencias diretas permitidas foram atualizados.
- Business Systems 21-24 nao foram alterados.
- Docs 26-34 nao foram criados.
- UI/UX, backend, migrations, API, banco, agentes reais e automacoes runtime continuam bloqueados.

## 16.3 Arquivos alterados no P0 Roadmaps 2026-05-28

- `000_ROADMAPS/README.md` atualizado com governanca auxiliar, contexto minimo, checkout lock, handoff e bloco Security/Governance/Cost/Approval.
- `000_ROADMAPS/ck_memory.md` criado.
- `000_ROADMAPS/ck_tasks.md` criado.
- `000_ROADMAPS/ck_risks.md` criado.
- `000_ROADMAPS/ck_roi.md` criado.
- `000_ROADMAPS/ck_feedback.md` criado.
- `000_ROADMAPS/ck_agent_handoffs.md` criado.
- YAML de `000_ROADMAPS/**/*.md` normalizado.
- `CKOS_FILETREE_MAP.md`, `CKOS_FOLDER_MEMORY.md` e este refresh report atualizados como mapas auxiliares.
- Governanca canonica, `ARCHITECTURE_PATCH_REPORT.md`, docs 01-25, docs 26-34, UI, backend, API, banco, migrations, JSONs n8n e agentes reais nao foram alterados.

## 16.4 Arquivos alterados na study note Intent Pattern 2026-05-28

- `000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md` criado.
- `000_STUDY_NOTES/README.md` atualizado para registrar a subpasta de padroes operacionais AI First.
- `000_STUDY_NOTES/_folder_memory.md` atualizado com memoria da nota.
- `CKOS_FILETREE_MAP.md`, `CKOS_FOLDER_MEMORY.md` e este refresh report atualizados como mapas auxiliares.
- Governanca canonica, `ARCHITECTURE_PATCH_REPORT.md`, docs 01-25, docs 26-34, `000_ROADMAPS/`, UI, backend, API, banco, migrations, JSONs n8n, agentes reais, `.obsidian/` e `Memoria GPT.md` nao foram alterados por esta tarefa.

## 16.5 Arquivos alterados no P1.7 Multi-Session Execution Policy 2026-05-28

- `000_ROADMAPS/SESSION_REGISTRY.md` criado.
- `000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md` criado.
- `000_STUDY_NOTES/12_SESSION_GATES/README.md` criado.
- `000_STUDY_NOTES/12_SESSION_GATES/_folder_memory.md` criado.
- `000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md` criado.
- `000_ROADMAPS/ck_agent_handoffs.md` atualizado com P1.7.
- `000_ROADMAPS/ck_memory.md` atualizado com P1.7.
- `000_ROADMAPS/ck_tasks.md` atualizado com proxima acao.
- `000_ROADMAPS/ck_risks.md` atualizado com riscos multi-sessao.
- `000_ROADMAPS/ck_roi.md` atualizado com ROI operacional multi-sessao.
- `000_ROADMAPS/ck_feedback.md` atualizado com status PMO.
- `000_STUDY_NOTES/README.md` atualizado para registrar `12_SESSION_GATES/`.
- `000_STUDY_NOTES/_folder_memory.md` atualizado com memoria do gate.
- `CKOS_FILETREE_MAP.md`, `CKOS_FOLDER_MEMORY.md` e este refresh report atualizados como mapas auxiliares.
- `ARCHITECTURE_PATCH_REPORT.md`, `QA_DOCUMENTATION_CHECKLIST.md`, docs 01-25, docs 26-34, UI, backend, API, banco, migrations, JSONs n8n, agentes reais, `.obsidian/`, `000_UPGRADE/`, `000_UPLOADS/` e `Memoria GPT.md` nao foram alterados por P1.7.

## 16.6 Arquivos alterados no P1.7.1 Memory Refresh 2026-05-28

- `000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md` atualizado para `version: 1.0.0` e frase obrigatoria.
- `000_ROADMAPS/SESSION_REGISTRY.md` atualizado para `version: 1.0.0` e registro da sessao P1.7.1.
- `000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md` atualizado para `version: 1.0.0`.
- `000_STUDY_NOTES/12_SESSION_GATES/ck_memory.md` criado.
- `000_STUDY_NOTES/12_SESSION_GATES/_folder_memory.md` marcado como legacy/superseded.
- `000_STUDY_NOTES/12_SESSION_GATES/README.md`, `000_STUDY_NOTES/README.md` e `000_STUDY_NOTES/_folder_memory.md` atualizados para reconhecer `ck_memory.md` como memoria ativa.
- `CKOS_FILETREE_MAP.md`, `CKOS_FOLDER_MEMORY.md`, `CKOS_VAULT_MAP_REFRESH_REPORT.md` e `ARCHITECTURE_PATCH_REPORT.md` atualizados conforme lock separado.
- Docs canonicos 01-25, Business Systems 21-24, docs 26-34, `QA_DOCUMENTATION_CHECKLIST.md`, `Memoria GPT.md`, `000_UPLOADS/`, `000_UPGRADE/`, UI, backend, API, banco, migrations, JSONs n8n e agentes reais nao foram alterados por P1.7.1.

## 16.7 Arquivos alterados no UI/UX Visual Reference Study 2026-05-28

- `000_STUDY_NOTES/10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md` criado.
- `000_STUDY_NOTES/10_UIUX_STUDIES/02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md` criado.
- `000_STUDY_NOTES/10_UIUX_STUDIES/03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md` criado.
- `000_STUDY_NOTES/10_UIUX_STUDIES/04_MOBILE_COMMAND_FIRST_ERGONOMICS.md` criado.
- `000_STUDY_NOTES/10_UIUX_STUDIES/05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md` criado.
- `000_STUDY_NOTES/10_UIUX_STUDIES/06_UIUX_ANTI_PATTERNS_AND_GENERIC_AI_UI_RISKS.md` criado.
- `000_STUDY_NOTES/10_UIUX_STUDIES/ck_memory.md` criado como memoria ativa.
- `CKOS_FILETREE_MAP.md`, `CKOS_FOLDER_MEMORY.md` e este refresh report atualizados como mapas auxiliares.
- `000_ROADMAPS/SESSION_REGISTRY.md` atualizado com o lock e release da sessao.
- Docs canonicos 01-25, Business Systems 21-24, docs 26-34, `QA_DOCUMENTATION_CHECKLIST.md`, `Memoria GPT.md`, `000_UPLOADS/`, `000_UPGRADE/`, UI, backend, API, banco, migrations, JSONs n8n e agentes reais nao foram alterados.

## 16.8 Arquivos alterados no UI/UX Audit Patch 2026-05-28

- `000_STUDY_NOTES/10_UIUX_STUDIES/07_AGENT_ACTIVITY_STREAM_UIUX_STUDY.md` criado.
- `000_STUDY_NOTES/10_UIUX_STUDIES/08_WHITELABEL_TOKEN_SYSTEM_UIUX_STUDY.md` criado.
- `02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md` atualizado com a eliminação de referências a "Project Pulse".
- `03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md`, `04_MOBILE_COMMAND_FIRST_ERGONOMICS.md`, `05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md` (expandido para exatamente 8 princípios cognitivos) e `06_UIUX_ANTI_PATTERNS_AND_GENERIC_AI_UI_RISKS.md` (expandido para exatamente 10 anti-padrões) atualizados.
- `ck_memory.md`, `000_ROADMAPS/03_FRONTEND_UIUX_ROADMAP/01_UIUX_STUDY_TO_CANONICAL_ROADMAP.md` e `000_ROADMAPS/SESSION_REGISTRY.md` atualizados.
- Docs canônicos 01-25, Business Systems 21-24, docs 26-34, `QA_DOCUMENTATION_CHECKLIST.md`, `Memória GPT.md`, `000_UPLOADS/`, `000_UPGRADE/`, UI, backend, API, banco, migrations, JSONs n8n e agentes reais não foram alterados.

## 16.9 Arquivos alterados no UI/UX Operational Patterns Study 2026-05-28

- `000_STUDY_NOTES/10_UIUX_STUDIES/09_EXECUTION_PLAN_WIDGET_UIUX_STUDY.md` criado.
- `000_STUDY_NOTES/10_UIUX_STUDIES/10_INTENT_CLARIFIER_AND_SMART_QUESTIONS_UIUX_STUDY.md` criado.
- `000_STUDY_NOTES/10_UIUX_STUDIES/11_COST_CREDITS_AND_ROI_AWARE_UX_STUDY.md` criado.
- `000_STUDY_NOTES/10_UIUX_STUDIES/12_APPROVAL_GATE_AND_REVERSIBILITY_UX_STUDY.md` criado.
- `000_STUDY_NOTES/10_UIUX_STUDIES/13_EVIDENCE_TRUST_AND_DECISION_UIUX_STUDY.md` criado.
- `CKOS_FILETREE_MAP.md`, `CKOS_FOLDER_MEMORY.md`, `CKOS_VAULT_MAP_REFRESH_REPORT.md` (este relatório) e `000_ROADMAPS/SESSION_REGISTRY.md` atualizados.
- Docs canônicos 01-25, Business Systems 21-24, docs 26-34, `QA_DOCUMENTATION_CHECKLIST.md`, `Memória GPT.md`, `000_UPLOADS/`, `000_UPGRADE/`, UI, backend, API, banco, migrations, JSONs n8n e agentes reais não foram alterados.


## 16.10 Arquivos alterados no Study Layer 13 AI-first Project Operating System 2026-05-30

- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/README.md` criado.
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md` criado.
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_tasks.md` criado.
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_risks.md` criado.
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_roi.md` criado.
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_feedback.md` criado.
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_agent_handoffs.md` criado.
- Notas `01_PROJECT_AI_FIRST_OPERATING_MODEL.md` a `14_ACCEPTANCE_CRITERIA_FOR_DOC27.md` criadas como estudo auxiliar.
- `000_STUDY_NOTES/README.md`, `000_STUDY_NOTES/_folder_memory.md`, `CKOS_FILETREE_MAP.md`, `CKOS_FOLDER_MEMORY.md`, `CKOS_VAULT_MAP_REFRESH_REPORT.md` e `000_ROADMAPS/SESSION_REGISTRY.md` atualizados.
- `ARCHITECTURE_PATCH_REPORT.md` nao foi alterado por esta sessao.
- Docs 01-26, docs 27-34, `QA_DOCUMENTATION_CHECKLIST.md`, `000_UPLOADS/`, `000_UPGRADE/`, UI, backend, API, banco, migrations, MCP server real, JSONs n8n, agentes reais e automacoes runtime nao foram alterados.
- Contagem apos Study Layer 13: 1090 arquivos incluindo metadados ocultos, 1018 Markdown, 29 JSON, 13 diretorios de topo; `000_ROADMAPS/` contem 159 Markdown e `000_STUDY_NOTES/` contem 348 Markdown.


## 17. Apendice - inventario de arquivos por pasta

### Raiz

- `ARCHITECTURE_PATCH_REPORT.md`
- `CKOS_FOLDER_MEMORY.md`
- `CKOS_VAULT_MAP_REFRESH_REPORT.md`
- `Memória GPT.md`
- `QA_DOCUMENTATION_CHECKLIST.md`

### `00_SYSTEM_GOVERNANCE/`

- `00_DEPENDENCY_MAP.md`
- `00_DOCUMENT_TEMPLATE.md`
- `00_MASTER_MAP.md`
- `00_README_SYSTEM_GOVERNANCE.md`
- `00_TAXONOMY_AND_NAMING.md`

### `01_THINKING_SYSTEM/`

- `00_README_THINKING_SYSTEM.md`
- `01_CKOS_AI_FIRST_CONSTITUTION.md`
- `02_AI_FIRST_OBJECT_MODEL.md`
- `03_AGENT_OPERATING_MODEL.md`
- `04_AUTONOMY_AND_APPROVALS.md`
- `05_MEMORY_AND_CONTEXT_ARCHITECTURE.md`

### `02_EXECUTION_SYSTEM/`

- `00_README_EXECUTION_SYSTEM.md`
- `06_SKILLS_REGISTRY.md`
- `07_WORKFLOW_BLUEPRINTS.md`
- `08_PROMPT_LIBRARY.md`
- `09_TRANSFORMERS_AND_PIPELINES.md`

### `03_RUNTIME_SYSTEM/`

- `00_README_RUNTIME_SYSTEM.md`
- `10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `11_DATA_MODEL_AND_PERSISTENCE.md`
- `12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`
- `13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`

### `04_PRODUCT_SYSTEM/`

- `00_README_PRODUCT_SYSTEM.md`
- `14_PROJECT_DASHBOARD_ARCHITECTURE.md`
- `15_COMMAND_CENTER_ARCHITECTURE.md`
- `16_NODE_CANVAS_ARCHITECTURE.md`

### `05_IMPLEMENTATION_SYSTEM/`

- `00_README_IMPLEMENTATION_SYSTEM.md`
- `17_IMPLEMENTATION_PROTOCOL.md`
- `18_RESEARCH_PROTOCOL.md`
- `18_RESEARCH_PROTOCOL_FOR_MANUS.md`
- `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`
- `19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md`
- `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`
- `21_SELF_EVOLVING_SYSTEM.md` (superseded/historico)

### `06_BUSINESS_SYSTEMS/`

- `21_ROI_ARCHITECTURE.md`
- `22_FEEDBACK_SYSTEM_ARCHITECTURE.md`
- `23_SUPPORT_SYSTEM_ARCHITECTURE.md`
- `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`

### `07_EVOLUTION_SYSTEM/`

- `00_README_EVOLUTION_SYSTEM.md`
- `25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`
- `26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`

### `000_STUDY_NOTES/`

- `README.md`
- `_folder_memory.md`
- `00_STUDY_INDEX.md`
- `_templates/`
- `11_AI_FIRST_OPERATING_PATTERNS/`
- `11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md`
- `12_SESSION_GATES/`
- `12_SESSION_GATES/README.md`
- `12_SESSION_GATES/ck_memory.md`
- `12_SESSION_GATES/_folder_memory.md`
- `12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md`
- `10_UIUX_STUDIES/`
- `10_UIUX_STUDIES/ck_memory.md`
- `10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md`
- `10_UIUX_STUDIES/02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md`
- `10_UIUX_STUDIES/03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md`
- `10_UIUX_STUDIES/04_MOBILE_COMMAND_FIRST_ERGONOMICS.md`
- `10_UIUX_STUDIES/05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md`
- `10_UIUX_STUDIES/06_UIUX_ANTI_PATTERNS_AND_GENERIC_AI_UI_RISKS.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/README.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_memory.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_tasks.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_risks.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_roi.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_feedback.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/ck_agent_handoffs.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/01_PROJECT_AI_FIRST_OPERATING_MODEL.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/02_INTELLIGENT_QUESTION_SYSTEM_STUDY.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/03_BRIEFING_TO_TASKS_TRANSFORMER_STUDY.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/04_NOTES_AS_OPERATIONAL_MEMORY_STUDY.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/05_TASK_AI_FIRST_SYSTEM_STUDY.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/06_SUPERAGENT_AGENT_SUBAGENT_WORK_ALLOCATION_STUDY.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/07_PARALLEL_EXECUTION_AND_CHECKOUT_LOCK_STUDY.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/08_FOUNDER_APPROVAL_BATCH_CONTROL_STUDY.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/09_ROI_AWARE_TASKS_NOTES_AND_QUESTIONS_STUDY.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/10_FEEDBACK_TO_LEARNING_LOOP_STUDY.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/11_PROJECT_SELF_DOCUMENTATION_SYSTEM_STUDY.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/12_RAG_METADATA_AND_VECTOR_CATEGORY_STUDY.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md`
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/14_ACCEPTANCE_CRITERIA_FOR_DOC27.md`

### `000_ROADMAPS/`

- `README.md`
- `ck_memory.md`
- `ck_tasks.md`
- `ck_risks.md`
- `ck_roi.md`
- `ck_feedback.md`
- `ck_agent_handoffs.md`
- `SESSION_REGISTRY.md`
- `MULTI_SESSION_EXECUTION_POLICY.md`
- `ROADMAP_RECONCILIATION_REPORT.md`
- `ROADMAP_ROUTING_MATRIX.md`
- `00_MASTER_ROADMAP/`
- `01_DOCUMENTATION_ROADMAP/`
- `02_RUNTIME_BACKEND_ROADMAP/`
- `03_FRONTEND_UIUX_ROADMAP/`
- `04_CONNECTORS_MCP_INTEGRATIONS_ROADMAP/`
- `05_SUPERAGENTS_AGENTS_SUBAGENTS_ROADMAP/`
- `06_SECURITY_GOVERNANCE_ROADMAP/`
- `07_BUSINESS_ROI_BILLING_ROADMAP/`
- `08_LEARNING_STUDY_MEMORY_ROADMAP/`
- `09_CLIENT_PROJECT_CREATOR_MODE_ROADMAP/`
- `10_RELEASES_AND_GATES/`
- `11_TEMPLATES/`
- `12_PROMPTS/`
- `13_ACCEPTANCE_CRITERIA/`
- `14_RUNTIME_BACKEND_ROADMAP/`
- `15_SECURITY_GOVERNANCE_ROADMAP/`
- `16_BUSINESS_SYSTEMS_ROADMAP/`
- `17_RELEASES_GATES_ROADMAP/`
- `18_CONNECTORS_MCP_INTEGRATIONS_ROADMAP/`
- `19_UIUX_STUDY_ROADMAP/`
- `20_AGENT_CIVILIZATION_ROADMAP/`
- `21_LEARNING_AND_KNOWLEDGE_ROADMAP/`

### `000_UPGRADE/`

- `Bem-vindo.md`
- `CKOS_CODEX_MEMORY.md`
- `CKOS_CONTINUATION_PLAN.md`
- `CKOS_INFRA_AUTOMATION_MEMORY.md`
- `CKOS_RESEARCH_MEMORY.md`
- `CKOS_UPGRADE_INDEX.md`

### `000_UPGRADE/CKOS_CODEX_CONTINUATION_PACK/`

- `00_README_START_HERE.md`
- `ck.md`
- `00_CONTEXT/CKOS_CURRENT_STATE.md`
- `00_CONTEXT/FILETREE_EXPECTED_MAP.md`
- `01_PROMPTS/ANTIGRAVITY_PARALLEL_REVIEW_PROMPT.md`
- `01_PROMPTS/CHATGPT_VISUAL_DIRECTOR_IMAGE_PROMPT_BRIEF.md`
- `01_PROMPTS/CODEX_MASTER_PROMPT.md`
- `02_SKILLS/AI_FIRST_PROJECT_PLANNER_SKILL.md`
- `02_SKILLS/CONTEXT_ENGINEERING_SKILL.md`
- `02_SKILLS/PMO_DOCUMENTATION_SKILL.md`
- `02_SKILLS/RESEARCH_COLLECTOR_SKILL.md`
- `03_ARCHITECTURE_NOTES/25_LEARNING_AND_PROJECT_STUDY_MODE.md`
- `03_ARCHITECTURE_NOTES/26_COLLECTOR_REGISTRY_AND_RESEARCH_ACTORS.md`
- `03_ARCHITECTURE_NOTES/27_CKSTORE_AND_CAPABILITY_MARKETPLACE.md`
- `03_ARCHITECTURE_NOTES/28_PROJECT_PLANNER_AND_SELF_DOCUMENTING_PROJECTS.md`
- `03_ARCHITECTURE_NOTES/29_VISUAL_DIRECTOR_AND_IMAGE_PROMPT_PIPELINE.md`
- `04_RESEARCH/YOUTUBE_DEEP_RESEARCH_IDEA.md`
- `05_VISUAL_HTML_STUDY/HTML_STUDY_ARCHITECTURE_BRIEF.md`
- `05_VISUAL_HTML_STUDY/PINTEREST_KEYWORDS_AND_IMAGE_TYPES.md`
- `06_ROADMAP/DEVELOPMENT_PLAN_WITHOUT_UI.md`
- `06_ROADMAP/DOCS_21_TO_30_SEQUENCE.md`

### `000_UPGRADE/pack_notas_ckos_deep_research/`

- `01_01-ckos-como-ai-first-operating-system.md`
- `02_02-ckos-vs-branddock.md`
- `03_03-arquitetura-local-para-vps.md`
- `04_04-project-pulse.md`
- `05_05-briefing-inteligente-com-nick.md`
- `06_06-proposal-engine.md`
- `07_07-agent-journey-e-runs.md`
- `08_08-organograma-de-agentes.md`
- `09_09-human-in-the-loop-e-aprovacoes.md`
- `10_10-models-costs.md`
- `11_11-sistema-de-creditos-planos-e-pagamentos.md`
- `12_12-knowledge-base-por-projeto.md`
- `13_13-decisions.md`
- `14_14-issues-pipeline-e-checkout-lock.md`
- `15_15-sprints-releases.md`
- `16_16-chat-operacional.md`
- `17_17-suporte-ia-humano.md`
- `18_18-seguranca-secrets-e-isolamento.md`
- `19_19-marketplace-de-workflows-e-docks.md`
- `20_20-linguagem-para-socios-e-influenciadores.md`
- `INDEX.md`
- `README.md`

### `000_UPGRADE/ckos_digitalocean_n8n_pack/`

- `00_README_INDEX.md`
- `00_DigitalOcean_PMO/01_Decisao_PMO_Iniciar_com_DigitalOcean.md`
- `01_Financas_ROI/01_Runway_e_Queima_de_Credito.md`
- `01_Financas_ROI/02_ROI_Infra_por_Projeto.md`
- `01_Financas_ROI/03_Planner_de_Execucao_Custos.md`
- `01_Financas_ROI/04_Modelo_de_Custo_por_Agente.md`
- `02_N8N_Automations/00_Principios/00_INDEX.md`
- `02_N8N_Automations/00_Principios/01_N8N_como_Acelerador_nao_Core.md`
- `02_N8N_Automations/00_Principios/01_N8N_como_Acelerador_nao_Core.json`
- `02_N8N_Automations/01_Leads_Propostas/00_INDEX.md`
- `02_N8N_Automations/01_Leads_Propostas/01_Captura_Lead/01_Webhook_Lead_para_Supabase.md`
- `02_N8N_Automations/01_Leads_Propostas/01_Captura_Lead/01_Webhook_Lead_para_Supabase.json`
- `02_N8N_Automations/01_Leads_Propostas/02_Proposta/01_Gerar_Resumo_de_Proposta_com_IA.md`
- `02_N8N_Automations/01_Leads_Propostas/02_Proposta/01_Gerar_Resumo_de_Proposta_com_IA.json`
- `02_N8N_Automations/02_Onboarding_Cliente/00_INDEX.md`
- `02_N8N_Automations/02_Onboarding_Cliente/01_Briefing/01_Briefing_Inteligente_para_Cards.md`
- `02_N8N_Automations/02_Onboarding_Cliente/01_Briefing/01_Briefing_Inteligente_para_Cards.json`
- `02_N8N_Automations/02_Onboarding_Cliente/02_Stakeholders/01_Mapear_Stakeholders_e_Aprovacoes.md`
- `02_N8N_Automations/02_Onboarding_Cliente/02_Stakeholders/01_Mapear_Stakeholders_e_Aprovacoes.json`
- `02_N8N_Automations/03_Knowledge_RAG/00_INDEX.md`
- `02_N8N_Automations/03_Knowledge_RAG/01_Ingestao/01_Ingestao_Arquivo_para_Knowledge.md`
- `02_N8N_Automations/03_Knowledge_RAG/01_Ingestao/01_Ingestao_Arquivo_para_Knowledge.json`
- `02_N8N_Automations/03_Knowledge_RAG/02_Sincronizacao/01_Sync_Google_Drive_para_Knowledge.md`
- `02_N8N_Automations/03_Knowledge_RAG/02_Sincronizacao/01_Sync_Google_Drive_para_Knowledge.json`
- `02_N8N_Automations/04_Content_Ops/00_INDEX.md`
- `02_N8N_Automations/04_Content_Ops/01_Instagram/01_Capturar_Reels_Apify_e_Gerar_Insights.md`
- `02_N8N_Automations/04_Content_Ops/01_Instagram/01_Capturar_Reels_Apify_e_Gerar_Insights.json`
- `02_N8N_Automations/04_Content_Ops/02_Roteiros/01_Gerar_Roteiro_Reels_por_Insight.md`
- `02_N8N_Automations/04_Content_Ops/02_Roteiros/01_Gerar_Roteiro_Reels_por_Insight.json`
- `02_N8N_Automations/05_Billing_Credits/00_INDEX.md`
- `02_N8N_Automations/05_Billing_Credits/01_Creditos/01_Budget_Gate_antes_de_Run_Caro.md`
- `02_N8N_Automations/05_Billing_Credits/01_Creditos/01_Budget_Gate_antes_de_Run_Caro.json`
- `02_N8N_Automations/05_Billing_Credits/02_Pagamentos/01_Evento_Stripe_Atualiza_Wallet.md`
- `02_N8N_Automations/05_Billing_Credits/02_Pagamentos/01_Evento_Stripe_Atualiza_Wallet.json`
- `02_N8N_Automations/06_Support/00_INDEX.md`
- `02_N8N_Automations/06_Support/01_Tickets/01_Ticket_Suporte_com_Contexto_do_Projeto.md`
- `02_N8N_Automations/06_Support/01_Tickets/01_Ticket_Suporte_com_Contexto_do_Projeto.json`
- `02_N8N_Automations/07_Observability/00_INDEX.md`
- `02_N8N_Automations/07_Observability/01_Logs/01_Log_Run_Agente_e_Custo.md`
- `02_N8N_Automations/07_Observability/01_Logs/01_Log_Run_Agente_e_Custo.json`
- `02_N8N_Automations/07_Observability/02_Alertas/01_Alerta_Erro_Workflow_ou_Custo.md`
- `02_N8N_Automations/07_Observability/02_Alertas/01_Alerta_Erro_Workflow_ou_Custo.json`
- `02_N8N_Automations/08_Connectors_OAuth/00_INDEX.md`
- `02_N8N_Automations/08_Connectors_OAuth/01_Google/01_Conector_Google_Drive_Calendar_Gmail.md`
- `02_N8N_Automations/08_Connectors_OAuth/01_Google/01_Conector_Google_Drive_Calendar_Gmail.json`
- `02_N8N_Automations/08_Connectors_OAuth/02_Meta/01_Conector_Meta_Ads_Instagram.md`
- `02_N8N_Automations/08_Connectors_OAuth/02_Meta/01_Conector_Meta_Ads_Instagram.json`
- `02_N8N_Automations/09_Agent_Handoffs/00_INDEX.md`
- `02_N8N_Automations/09_Agent_Handoffs/01_Handoffs/01_Handoff_entre_Agentes_com_Log.md`
- `02_N8N_Automations/09_Agent_Handoffs/01_Handoffs/01_Handoff_entre_Agentes_com_Log.json`
- `02_N8N_Automations/10_Internal_Ops/00_INDEX.md`
- `02_N8N_Automations/10_Internal_Ops/01_Backup/01_Backup_Diario_Supabase_Metadata.md`
- `02_N8N_Automations/10_Internal_Ops/01_Backup/01_Backup_Diario_Supabase_Metadata.json`
- `03_Policies/01_Policy_Custos_Budget_Gates.md`
- `03_Policies/02_Policy_N8N_Prototipo_para_Codigo.md`
- `04_Codex_Instructions/00_Contexto_Mestre_para_Codex.md`

## 18. Complemento final do refresh 2026-05-26

Arquivos analisados:

- 158 arquivos apos a criacao de `CKOS_FILETREE_MAP.md`.
- 130 arquivos Markdown.
- 28 arquivos JSON.
- Pastas principais: raiz, `.obsidian/`, `000_UPGRADE/`, `00_SYSTEM_GOVERNANCE/`, `01_THINKING_SYSTEM/`, `02_EXECUTION_SYSTEM/`, `03_RUNTIME_SYSTEM/`, `04_PRODUCT_SYSTEM/`, `05_IMPLEMENTATION_SYSTEM/`, `06_BUSINESS_SYSTEMS/`.

Arquivos novos detectados:

- `CKOS_FILETREE_MAP.md`.
- Memorias e indices de `000_UPGRADE` criados em 2026-05-26.
- `CKOS_CODEX_CONTINUATION_PACK/`, `ckos_digitalocean_n8n_pack/` e `pack_notas_ckos_deep_research/` importados em 2026-05-26.
- Docs 21-24 Business Systems criados/modificados em 2026-05-25 e confirmados como existentes.

Arquivos atualizados neste complemento:

- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`: recebeu bloco de refresh v2.3.0, sem renumeracao.
- `CKOS_FOLDER_MEMORY.md`: recebeu memoria por pasta no padrao solicitado.
- `CKOS_FILETREE_MAP.md`: criado.
- `000_UPGRADE/CKOS_CODEX_MEMORY.md`: atualizado com locks de refresh.
- `000_UPGRADE/CKOS_UPGRADE_INDEX.md`: atualizado com filetree map e travas.
- `000_UPGRADE/CKOS_CONTINUATION_PLAN.md`: atualizado com status de refresh.
- `CKOS_VAULT_MAP_REFRESH_REPORT.md`: este relatorio atualizado.

Duplicidades encontradas:

- Prefixo `18`: `18_RESEARCH_PROTOCOL.md` e `18_RESEARCH_PROTOCOL_FOR_MANUS.md`.
- Prefixo `19`: `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md` e `19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md`.
- Prefixo `21`: `21_ROI_ARCHITECTURE.md` permanece ativo; `21_SELF_EVOLVING_SYSTEM.md` foi preservado como superseded/historico.
- Roadmaps do continuation pack duplicam a intencao de criar 22-24, mas os documentos ja existem.

Conflito de numeracao resolvido:

- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`
- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`
- `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`

Resolucao deste refresh: nao renomear o arquivo antigo; criar novo doc 25 em `07_EVOLUTION_SYSTEM/`; manter ROI como doc 21.

Decisao aplicada:

- Self-Evolving ativo: `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`.
- Self-Evolving antigo: `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` superseded/historico.

Documentos canonicos confirmados:

- Governance/Thinking/Execution/Runtime/Product docs 00-16.
- Implementation docs 17-20.
- Business Systems docs 21-24.
- Evolution System doc 25.
- `ARCHITECTURE_PATCH_REPORT.md` como rastreabilidade mestre.
- `QA_DOCUMENTATION_CHECKLIST.md` como checklist de QA documental.

Documentos historicos/supersedidos confirmados ou provaveis:

- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md`: legado Manus, nao infra CKOS.
- `05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md`: provavelmente superseded pelo protocolo com Antigravity.
- Roadmaps de `CKOS_CODEX_CONTINUATION_PACK/06_ROADMAP/` que tratam 22-24 como pendentes.

Restricoes reafirmadas:

- Nao recriar docs 21-24.
- Nao criar docs 26-34 ainda.
- Nao iniciar UI/UX implementation.
- Nao iniciar backend, migrations, APIs, banco de dados, agentes reais ou automacoes runtime.
- Nao mover, deletar, renomear ou renumerar arquivos sem relatorio previo.
- Nao transformar n8n em core.
- Nao tratar Manus como infraestrutura definitiva.

Recomendacao de proxima acao:

- Claude auditar `26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`.
- Antes de qualquer doc 27-34, confirmar dependencias, autorizacao PMO/Founder e invariantes de runtime.
