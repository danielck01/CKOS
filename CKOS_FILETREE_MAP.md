---
title: CKOS Filetree Map
system_id: ckos_filetree_map
category: vault_memory
status: active
version: 1.6.0
owner: docs_architect_agent
reviewers:
  - founder
  - pmo_ckos
  - metacognik
related_notes:
  - CKOS_FOLDER_MEMORY.md
  - CKOS_VAULT_MAP_REFRESH_REPORT.md
  - ARCHITECTURE_PATCH_REPORT.md
  - 00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md
  - 000_UPGRADE/CKOS_UPGRADE_INDEX.md
  - 000_UPLOADS/00_UPLOADS_INDEX.md
  - 000_STUDY_NOTES/00_STUDY_INDEX.md
  - 000_ROADMAPS/README.md
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
  - 000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/README.md
created_for: CKOS_DOCUMENTATION_REVIEWED
last_scan: 2026-05-26
last_micro_refresh: 2026-05-28
---

# CKOS Filetree Map

## Trava executiva

Este arquivo e apenas mapa de filetree e memoria. Ele nao autoriza implementacao, UI, backend, migrations, banco de dados, agentes, APIs, promocao de n8n a core ou movimentacao de pastas.

Fatos operacionais atuais:

- Docs 21-24 Business Systems ja existem em `06_BUSINESS_SYSTEMS/`.
- Gate I esta documentalmente completo e o microgate Self-Evolving esta registrado em `ARCHITECTURE_PATCH_REPORT.md` v1.9.0.
- Docs 21-24 nao devem ser recriados.
- Doc 25 Self-Evolving foi criado em `07_EVOLUTION_SYSTEM/` apos decisao Founder.
- Doc 26 Connectors, MCP and Integrations Architecture foi criado em `07_EVOLUTION_SYSTEM/` apos microgate PMO.
- Docs 27-34 nao devem ser criados sem autorizacao Founder e patch plan especifico.
- UI/UX implementation, backend, migrations, agentes, APIs e automacoes permanecem bloqueados.
- Arquivos nao devem ser movidos, deletados ou renomeados sem relatorio previo e aprovacao Founder.
- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` foi preservado como historico/superseded; ROI permanece doc 21 em `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`.
- n8n e camada auxiliar de aceleracao/prototipo, nao core CKOS.
- Manus e ferramenta temporaria de pesquisa/bootstrap, nao infraestrutura definitiva do CKOS.
- `000_UPLOADS/` e `000_STUDY_NOTES/` foram criadas em 2026-05-27 apos aprovacao Founder do microgate `UPLOADS_STUDY_MICROGATE_PROPOSAL`.
- RAW nao tem autoridade canonica; STUDY nao e canonico; CANONICAL so muda por patch plan, QA e aprovacao humana.
- `000_ROADMAPS/` existe como camada auxiliar governada de planejamento vivo; nao e canonica e nao autoriza implementacao.
- Antigravity/UI-UX continuam bloqueados ate estabilizacao documental, study layer e approval Founder.
- `000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/` existe como subpasta STUDY auxiliar para padroes operacionais AI First; nao e canonica e nao autoriza implementacao.
- P1.7 criou `SESSION_REGISTRY.md`, `MULTI_SESSION_EXECUTION_POLICY.md` e `000_STUDY_NOTES/12_SESSION_GATES/` como controles auxiliares multi-sessao.
- Antigravity so pode operar futuramente em `design_study` apos gate formal aprovado pelo Founder; P1.7 nao inicia Antigravity.
- P1.7.1 promoveu os tres arquivos principais de P1.7 para v1.0.0, adicionou a frase obrigatoria de checkout lock/release, registrou P1.7 no `ARCHITECTURE_PATCH_REPORT.md` e criou `12_SESSION_GATES/ck_memory.md` como memoria ativa.
- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/` foi criada em 2026-05-30 como Study Layer auxiliar para preparar Doc 27; nao e canonica, nao cria docs 27-34 e nao autoriza implementacao, agentes reais ou runtime.

## Resumo da varredura

Varredura base executada em 2026-05-26 a partir de:

`C:\Users\Usuario\Documents\CKCompany\CKOS\Research\Arquitetura-System\CKOS_DOCUMENTATION_REVIEWED`

Contagem antes da criacao deste arquivo:

- Total de arquivos incluindo metadados ocultos: 157
- Arquivos Markdown: 129
- Arquivos JSON: 28
- Diretorios de topo: 9

Contagem atual apos micro-refresh do Creator Mode Simulation Runtime:

- Total de arquivos incluindo metadados ocultos: 215
- Arquivos Markdown: 187
- Arquivos JSON: 28

Contagem atual apos microgate RAW/STUDY de 2026-05-27:

- Total de arquivos incluindo metadados ocultos: 575
- Arquivos Markdown: 540
- Arquivos JSON: 29
- Diretorios de topo: 11

Complemento apos microgate Self-Evolving Conflict Resolution de 2026-05-27:

- Nova pasta canonica: `07_EVOLUTION_SYSTEM/`
- Novo doc canonico draft: `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`
- Arquivo historico preservado: `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`
- Docs 26-34 ainda nao foram criados.
- Contagem apos microgate: 578 arquivos, 543 Markdown, 29 JSON, 12 diretorios de topo.

Complemento apos P0 Roadmaps Stabilization de 2026-05-28:

- Nova camada auxiliar governada registrada: `000_ROADMAPS/`.
- Controles raiz criados: `ck_memory.md`, `ck_tasks.md`, `ck_risks.md`, `ck_roi.md`, `ck_feedback.md`, `ck_agent_handoffs.md`.
- YAML dos arquivos em `000_ROADMAPS/**/*.md` normalizado para padrao auxiliar snake_case.
- `05_SUPERAGENTS_AGENTS_SUBAGENTS_ROADMAP/` foi mantida sem rename.
- Docs 26-34 nao foram criados.
- UI/UX, backend, migrations, API, banco, agentes reais, JSONs n8n e Antigravity continuam bloqueados.
- Contagem apos P0: 677 arquivos incluindo metadados ocultos, 642 Markdown, 29 JSON, 13 diretorios de topo; `000_ROADMAPS/` contem 99 Markdown.

Complemento apos study note Intent Question Plan Execution de 2026-05-28:

- Nova subpasta STUDY auxiliar: `000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/`.
- Nova nota auxiliar: `000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md`.
- A nota registra o padrao Intent -> Question -> Plan -> Execution, sem criar docs canonicos ou iniciar implementacao.
- Docs 26-34 nao foram criados.
- UI/UX, backend, migrations, API, banco, agentes reais, JSONs n8n e Antigravity continuam bloqueados.
- Contagem apos study note: 678 arquivos incluindo metadados ocultos, 643 Markdown, 29 JSON, 13 diretorios de topo; `000_STUDY_NOTES/` contem 34 Markdown.

Complemento apos P1/P1.5/P1.6 Roadmaps de 2026-05-28:

- P1 criou roadmaps auxiliares `000_ROADMAPS/14_RUNTIME_BACKEND_ROADMAP/` a `000_ROADMAPS/21_LEARNING_AND_KNOWLEDGE_ROADMAP/`.
- P1.5 criou `000_ROADMAPS/ROADMAP_RECONCILIATION_REPORT.md`.
- P1.6 criou `000_ROADMAPS/ROADMAP_ROUTING_MATRIX.md` e corrigiu caracteres NUL nos READMEs `14-21`.
- `000_ROADMAPS/` segue camada auxiliar governada, nao canonica.
- Docs 26-34 nao foram criados.
- UI/UX, backend, migrations, API, banco, agentes reais, JSONs n8n e Antigravity continuam bloqueados.
- Contagem apos P1.6: 736 arquivos incluindo metadados ocultos, 701 Markdown, 29 JSON, 13 diretorios de topo; `000_ROADMAPS/` contem 157 Markdown.

Complemento apos P1.7 Multi-Session Execution Policy de 2026-05-28:

- `000_ROADMAPS/SESSION_REGISTRY.md` criado antes dos demais arquivos P1.7.
- `000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md` criado como politica auxiliar de session types, checkout lock/release, permissoes por camada e nivel de inteligencia.
- Nova subpasta STUDY auxiliar: `000_STUDY_NOTES/12_SESSION_GATES/`.
- Novos arquivos: `000_STUDY_NOTES/12_SESSION_GATES/README.md`, `_folder_memory.md` e `01_ANTIGRAVITY_STUDY_MODE_GATE.md`.
- P1.7 nao atualizou `ARCHITECTURE_PATCH_REPORT.md`, nao alterou docs canonicos, nao criou docs 26-34, nao iniciou UI/UX e nao iniciou Antigravity.
- Contagem apos P1.7: 741 arquivos incluindo metadados ocultos, 706 Markdown, 29 JSON, 13 diretorios de topo; `000_ROADMAPS/` contem 159 Markdown e `000_STUDY_NOTES/` contem 37 Markdown.

Complemento apos P1.7.1 Memory Refresh de 2026-05-28:

- `000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md`, `000_ROADMAPS/SESSION_REGISTRY.md` e `000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md` promovidos para `version: 1.0.0`.
- Frase obrigatoria de abertura adicionada em `MULTI_SESSION_EXECUTION_POLICY.md`.
- `000_STUDY_NOTES/12_SESSION_GATES/ck_memory.md` criado como memoria ativa da pasta.
- `_folder_memory.md` preservado como legacy/superseded, sem move/delete.
- `ARCHITECTURE_PATCH_REPORT.md` atualizado com registro P1.7/P1.7.1.
- Docs 26-34 nao foram criados; UI/UX, backend, API, banco, migrations, JSONs n8n, agentes reais, Antigravity e Design Study continuam bloqueados.
- Contagem apos P1.7.1: 742 arquivos incluindo metadados ocultos, 707 Markdown, 29 JSON, 13 diretorios de topo; `000_ROADMAPS/` contem 159 Markdown e `000_STUDY_NOTES/` contem 38 Markdown.

Complemento apos UI/UX Visual Reference Study de 2026-05-28:

- Nova subpasta STUDY auxiliar: `000_STUDY_NOTES/10_UIUX_STUDIES/`.
- Novos arquivos auxiliares de estudo: `000_STUDY_NOTES/10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md`, `02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md`, `03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md`, `04_MOBILE_COMMAND_FIRST_ERGONOMICS.md`, `05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md`, `06_UIUX_ANTI_PATTERNS_AND_GENERIC_AI_UI_RISKS.md` e `ck_memory.md` (memória ativa da pasta).
- As notas de estudo traduzem referências visuais de design em gramáticas operacionais baseadas no runtime de agentes do CKOS, sem criar UI real, CSS, React ou HTML.
- Docs canônicos 01-25, docs 26-34 e `ARCHITECTURE_PATCH_REPORT.md` não foram alterados.
- Contagem apos UI/UX Study: 749 arquivos incluindo metadados ocultos, 714 Markdown, 29 JSON, 13 diretorios de topo; `000_ROADMAPS/` contem 159 Markdown e `000_STUDY_NOTES/` contem 45 Markdown.

Complemento apos UI/UX Audit Patch de 2026-05-28:

- Correção sistemática de referências a "Project Pulse", substituído por "Project Dashboard projection".
- Expansão de Neurodesign para exatamente 8 princípios e Anti-patterns para exatamente 10.
- Detalhamento de especificações ergonômicas mobile adicionadas em 04_MOBILE_COMMAND_FIRST_ERGONOMICS.md.
- Criação dos novos arquivos de estudo: `07_AGENT_ACTIVITY_STREAM_UIUX_STUDY.md` e `08_WHITELABEL_TOKEN_SYSTEM_UIUX_STUDY.md`.
- Contagem apos UI/UX Audit Patch: 751 arquivos incluindo metadados ocultos, 716 Markdown, 29 JSON, 13 diretorios de topo; `000_ROADMAPS/` contem 159 Markdown e `000_STUDY_NOTES/` contem 47 Markdown.

Complemento apos UI/UX Operational Patterns Study de 2026-05-28:

- Criação dos novos arquivos de estudo: `09_EXECUTION_PLAN_WIDGET_UIUX_STUDY.md`, `10_INTENT_CLARIFIER_AND_SMART_QUESTIONS_UIUX_STUDY.md`, `11_COST_CREDITS_AND_ROI_AWARE_UX_STUDY.md`, `12_APPROVAL_GATE_AND_REVERSIBILITY_UX_STUDY.md` e `13_EVIDENCE_TRUST_AND_DECISION_UIUX_STUDY.md`.
- As notas detalham os padrões conceituais de widgets e UX para planos de execução, perguntas inteligentes, wallets/créditos, portões de aprovação e mapas de evidências, sem código ou implementação visual.
- Contagem após UI/UX Operational Patterns Study: 756 arquivos incluindo metadados ocultos, 721 Markdown, 29 JSON, 13 diretórios de topo; `000_ROADMAPS/` contém 159 Markdown e `000_STUDY_NOTES/` contém 52 Markdown.

Complemento apos Study Layer 13 AI-first Project Operating System de 2026-05-30:

- Nova subpasta STUDY auxiliar: `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/`.
- Novos arquivos de estudo e controle: 21 Markdown, incluindo `README.md`, `ck_memory.md`, controles `ck_*` e notas 01-14.
- A camada estuda Project AI-first, Task AI-first, Notes AI-first, perguntas inteligentes, briefing-to-tasks, agent work allocation, checkout lock, Founder approval batch, ROI, feedback, learning, RAG metadata e candidatos para Doc 27.
- Docs 01-26 nao foram modificados por esta sessao; docs 27-34 nao foram criados.
- UI, backend, API, banco, migrations, MCP server real, JSONs n8n, agentes reais e automacoes runtime continuam bloqueados.
- `ARCHITECTURE_PATCH_REPORT.md`, `QA_DOCUMENTATION_CHECKLIST.md`, `000_UPLOADS/` e `000_UPGRADE/` nao foram alterados.
- Contagem apos Study Layer 13: 1090 arquivos incluindo metadados ocultos, 1018 Markdown, 29 JSON, 13 diretorios de topo; `000_ROADMAPS/` contem 159 Markdown e `000_STUDY_NOTES/` contem 348 Markdown.

## Contagem por pasta de topo

| Folder | Arquivos antes deste mapa | Classificacao |
|---|---:|---|
| `.obsidian/` | 5 | metadados do editor |
| `000_ROADMAPS/` | 159 | camada auxiliar governada de roadmaps vivos, nao canonica |
| 000_STUDY_NOTES/ | 348 | camada STUDY auxiliar, nao canonica |
| `000_UPGRADE/` | 167 | packs e memorias auxiliares |
| `000_UPLOADS/` | 41 | camada RAW auxiliar, sem autoridade canonica |
| `00_SYSTEM_GOVERNANCE/` | 5 | governanca canonica |
| `01_THINKING_SYSTEM/` | 6 | thinking system canonico |
| `02_EXECUTION_SYSTEM/` | 5 | execution system canonico |
| `03_RUNTIME_SYSTEM/` | 5 | runtime system canonico |
| `04_PRODUCT_SYSTEM/` | 4 | product projection canonico |
| `05_IMPLEMENTATION_SYSTEM/` | 8 | protocolos canonicos mais docs historicos/ambiguos |
| `06_BUSINESS_SYSTEMS/` | 4 | Business Systems canonicos docs 21-24 |
| `07_EVOLUTION_SYSTEM/` | 3 | Evolution System canonico draft; docs 25-26 |

## Arquivos recentes detectados

### Criados ou importados em 2026-05-26

- `CKOS_FOLDER_MEMORY.md`
- `CKOS_VAULT_MAP_REFRESH_REPORT.md`
- `CKOS_FILETREE_MAP.md`
- `000_UPGRADE/CKOS_CODEX_MEMORY.md`
- `000_UPGRADE/CKOS_INFRA_AUTOMATION_MEMORY.md`
- `000_UPGRADE/CKOS_RESEARCH_MEMORY.md`
- `000_UPGRADE/CKOS_UPGRADE_INDEX.md`
- `000_UPGRADE/CKOS_CONTINUATION_PLAN.md`
- `000_UPGRADE/CKOS_CREATOR_MODE_PACK/`
- `000_UPGRADE/CKOS_CREATOR_MODE_PACK/CKOS_CURRENT_STATE_SUMMARY.md`
- `000_UPGRADE/CKOS_CREATOR_MODE_PACK/07_SIMULATION_RUNTIME/`
- `000_UPGRADE/CKOS_CODEX_CONTINUATION_PACK/`
- `000_UPGRADE/ckos_digitalocean_n8n_pack/`
- `000_UPGRADE/pack_notas_ckos_deep_research/`

### Criados ou modificados em 2026-05-25 e relevantes ao estado atual

- `ARCHITECTURE_PATCH_REPORT.md`
- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`
- `06_BUSINESS_SYSTEMS/22_FEEDBACK_SYSTEM_ARCHITECTURE.md`
- `06_BUSINESS_SYSTEMS/23_SUPPORT_SYSTEM_ARCHITECTURE.md`
- `06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`
- `05_IMPLEMENTATION_SYSTEM/17_IMPLEMENTATION_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`
- docs 10-16 em Runtime/Product System.

## Documentos canonicos confirmados

### Docs canonicos/de controle da raiz

- `ARCHITECTURE_PATCH_REPORT.md`
- `QA_DOCUMENTATION_CHECKLIST.md`

### `00_SYSTEM_GOVERNANCE/`

- `00_README_SYSTEM_GOVERNANCE.md`
- `00_MASTER_MAP.md`
- `00_DOCUMENT_TEMPLATE.md`
- `00_TAXONOMY_AND_NAMING.md`
- `00_DEPENDENCY_MAP.md`

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
- `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`
- `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`

### `06_BUSINESS_SYSTEMS/`

- `21_ROI_ARCHITECTURE.md`
- `22_FEEDBACK_SYSTEM_ARCHITECTURE.md`
- `23_SUPPORT_SYSTEM_ARCHITECTURE.md`
- `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`

## Documentos auxiliares confirmados

- `CKOS_FOLDER_MEMORY.md`
- `CKOS_FILETREE_MAP.md`
- `CKOS_VAULT_MAP_REFRESH_REPORT.md`
- `000_ROADMAPS/README.md`
- `000_ROADMAPS/ck_memory.md`
- `000_ROADMAPS/ck_tasks.md`
- `000_ROADMAPS/ck_risks.md`
- `000_ROADMAPS/ck_roi.md`
- `000_ROADMAPS/ck_feedback.md`
- `000_ROADMAPS/ck_agent_handoffs.md`
- `000_ROADMAPS/SESSION_REGISTRY.md`
- `000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md`
- `000_UPLOADS/00_UPLOADS_INDEX.md`
- `000_STUDY_NOTES/00_STUDY_INDEX.md`
- `000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md`
- `000_STUDY_NOTES/12_SESSION_GATES/README.md`
- `000_STUDY_NOTES/12_SESSION_GATES/ck_memory.md`
- `000_STUDY_NOTES/12_SESSION_GATES/_folder_memory.md`
- `000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/ck_memory.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/04_MOBILE_COMMAND_FIRST_ERGONOMICS.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/06_UIUX_ANTI_PATTERNS_AND_GENERIC_AI_UI_RISKS.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/07_AGENT_ACTIVITY_STREAM_UIUX_STUDY.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/08_WHITELABEL_TOKEN_SYSTEM_UIUX_STUDY.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/09_EXECUTION_PLAN_WIDGET_UIUX_STUDY.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/10_INTENT_CLARIFIER_AND_SMART_QUESTIONS_UIUX_STUDY.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/11_COST_CREDITS_AND_ROI_AWARE_UX_STUDY.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/12_APPROVAL_GATE_AND_REVERSIBILITY_UX_STUDY.md`
- `000_STUDY_NOTES/10_UIUX_STUDIES/13_EVIDENCE_TRUST_AND_DECISION_UIUX_STUDY.md`
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
- `Memória GPT.md`
- `000_UPGRADE/CKOS_CODEX_MEMORY.md`
- `000_UPGRADE/CKOS_INFRA_AUTOMATION_MEMORY.md`
- `000_UPGRADE/CKOS_RESEARCH_MEMORY.md`
- `000_UPGRADE/CKOS_UPGRADE_INDEX.md`
- `000_UPGRADE/CKOS_CONTINUATION_PLAN.md`
- todos os arquivos em `000_UPGRADE/CKOS_CREATOR_MODE_PACK/`
- todos os arquivos em `000_UPGRADE/CKOS_CREATOR_MODE_PACK/07_SIMULATION_RUNTIME/`
- todos os arquivos em `000_UPGRADE/CKOS_CODEX_CONTINUATION_PACK/`
- todos os arquivos em `000_UPGRADE/ckos_digitalocean_n8n_pack/`
- todos os arquivos em `000_UPGRADE/pack_notas_ckos_deep_research/`

## Documentos historicos, supersedidos ou ambiguos

- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md`: variante historica/legada especifica de Manus. Nao tratar Manus como infraestrutura CKOS.
- `05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md`: protocolo anterior, provavelmente superseded por `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`.
- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`: preservado como historico/superseded. A arquitetura ativa foi recriada como `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`.
- `000_UPGRADE/CKOS_CODEX_CONTINUATION_PACK/06_ROADMAP/*`: roadmap auxiliar, parcialmente desatualizado porque trata docs 22-24 como pendentes.
- `Memória GPT.md`: contexto util, ainda nao classificado como canonico, auxiliar ou historico.
- `000_UPGRADE/CKOS_CREATOR_MODE_PACK/07_SIMULATION_RUNTIME/*`: simulacao operacional de backend/API/conectores; auxiliar, nao runtime real.

## Conflitos de numeracao

Conflito critico resolvido em 2026-05-27:

- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`
- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`
- `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`

Resolucao: ROI permanece doc 21; Self-Evolving ativo e doc 25; o antigo Self-Evolving 21 fica historico/superseded.

Prefixos numericos duplicados adicionais:

- `18_RESEARCH_PROTOCOL.md` and `18_RESEARCH_PROTOCOL_FOR_MANUS.md`
- `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md` and `19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md`

Nenhum arquivo foi renomeado neste refresh.

## Decisao para o conflito do doc 21

Opcao aplicada: recriar Self-Evolving como `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`, sem mover, deletar ou renomear o arquivo antigo.

- Resultado: preserva Business Systems 21-24 e reduz ambiguidade.
- Risco residual: referencias historicas em packs auxiliares podem continuar citando o antigo doc 21; nao usar packs antigos como source of truth sem STUDY.

Status do antigo arquivo:

- Mantido no lugar original.
- Marcado com superseded notice.
- Nao e fonte ativa de verdade arquitetural.
- Contras: altera taxonomia e exige patch em Master Map/Dependency Map.

Recomendacao PMO: a Opcao A e o caminho futuro mais limpo, mas somente depois de aprovacao Founder e auditoria de referencias.

## Filetree completo

```txt
CKOS_DOCUMENTATION_REVIEWED/
|-- .obsidian/
|   |-- app.json
|   |-- appearance.json
|   |-- core-plugins.json
|   |-- graph.json
|   `-- workspace.json
|-- ARCHITECTURE_PATCH_REPORT.md
|-- CKOS_FILETREE_MAP.md
|-- CKOS_FOLDER_MEMORY.md
|-- CKOS_VAULT_MAP_REFRESH_REPORT.md
|-- Memória GPT.md
|-- QA_DOCUMENTATION_CHECKLIST.md
|-- 000_ROADMAPS/
|   |-- README.md
|   |-- ck_memory.md
|   |-- ck_tasks.md
|   |-- ck_risks.md
|   |-- ck_roi.md
|   |-- ck_feedback.md
|   |-- ck_agent_handoffs.md
|   |-- SESSION_REGISTRY.md
|   |-- MULTI_SESSION_EXECUTION_POLICY.md
|   |-- ROADMAP_RECONCILIATION_REPORT.md
|   |-- ROADMAP_ROUTING_MATRIX.md
|   |-- 00_MASTER_ROADMAP/
|   |-- 01_DOCUMENTATION_ROADMAP/
|   |-- 02_RUNTIME_BACKEND_ROADMAP/
|   |-- 03_FRONTEND_UIUX_ROADMAP/
|   |-- 04_CONNECTORS_MCP_INTEGRATIONS_ROADMAP/
|   |-- 05_SUPERAGENTS_AGENTS_SUBAGENTS_ROADMAP/
|   |-- 06_SECURITY_GOVERNANCE_ROADMAP/
|   |-- 07_BUSINESS_ROI_BILLING_ROADMAP/
|   |-- 08_LEARNING_STUDY_MEMORY_ROADMAP/
|   |-- 09_CLIENT_PROJECT_CREATOR_MODE_ROADMAP/
|   |-- 10_RELEASES_AND_GATES/
|   |-- 11_TEMPLATES/
|   |-- 12_PROMPTS/
|   |-- 13_ACCEPTANCE_CRITERIA/
|   |-- 14_RUNTIME_BACKEND_ROADMAP/
|   |-- 15_SECURITY_GOVERNANCE_ROADMAP/
|   |-- 16_BUSINESS_SYSTEMS_ROADMAP/
|   |-- 17_RELEASES_GATES_ROADMAP/
|   |-- 18_CONNECTORS_MCP_INTEGRATIONS_ROADMAP/
|   |-- 19_UIUX_STUDY_ROADMAP/
|   |-- 20_AGENT_CIVILIZATION_ROADMAP/
|   `-- 21_LEARNING_AND_KNOWLEDGE_ROADMAP/
|-- 000_UPLOADS/
|   |-- README.md
|   |-- _folder_memory.md
|   |-- 00_UPLOADS_INDEX.md
|   |-- 00_INBOX_RAW/
|   |-- 01_SOURCE_DOCUMENTS/
|   |-- 02_RESEARCH_AND_BENCHMARKS/
|   |-- 03_TECH_REFERENCES/
|   |-- 04_BUSINESS_LEGAL_REFERENCES/
|   |-- 05_UI_UX_REFERENCES/
|   |-- 06_AI_TOOL_OUTPUTS/
|   |   |-- chatgpt/
|   |   |-- claude/
|   |   |-- codex/
|   |   |-- manus/
|   |   |-- antigravity/
|   |   `-- other/
|   |-- 07_CLIENT_PROJECT_INPUTS/
|   |-- 08_MEDIA_AND_TRANSCRIPTS/
|   |-- 09_DATASETS_AND_TABLES/
|   |-- 10_CONNECTOR_EXPORTS/
|   |-- 90_READY_FOR_STUDY/
|   `-- 99_ARCHIVE/
|-- 000_STUDY_NOTES/
|   |-- README.md
|   |-- _folder_memory.md
|   |-- 00_STUDY_INDEX.md
|   |-- _templates/
|   |-- 00_INBOX_FOR_REVIEW/
|   |-- 01_UPLOAD_STUDY_NOTES/
|   |-- 02_RESEARCH_SYNTHESIS/
|   |-- 03_MCP_CONNECTORS_INTEGRATIONS/
|   |-- 04_UI_UX_STUDY/
|   |-- 05_BUSINESS_SYSTEMS_STUDY/
|   |-- 06_CLIENT_PROJECT_STUDY/
|   |-- 07_CANONICAL_PATCH_CANDIDATES/
|   |-- 08_DECISION_LOGS/
|   |-- 09_APPROVED_FOR_CANONICAL_PATCH/
|   |-- 11_AI_FIRST_OPERATING_PATTERNS/
|   |   `-- 01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md
|   |-- 12_SESSION_GATES/
|   |   |-- README.md
|   |   |-- ck_memory.md
|   |   |-- _folder_memory.md
|   |   `-- 01_ANTIGRAVITY_STUDY_MODE_GATE.md
|   |-- 13_AI_FIRST_PROJECT_OPERATING_SYSTEM/
|   |   |-- README.md
|   |   |-- ck_memory.md
|   |   |-- ck_tasks.md
|   |   |-- ck_risks.md
|   |   |-- ck_roi.md
|   |   |-- ck_feedback.md
|   |   |-- ck_agent_handoffs.md
|   |   |-- 01_PROJECT_AI_FIRST_OPERATING_MODEL.md
|   |   |-- 02_INTELLIGENT_QUESTION_SYSTEM_STUDY.md
|   |   |-- 03_BRIEFING_TO_TASKS_TRANSFORMER_STUDY.md
|   |   |-- 04_NOTES_AS_OPERATIONAL_MEMORY_STUDY.md
|   |   |-- 05_TASK_AI_FIRST_SYSTEM_STUDY.md
|   |   |-- 06_SUPERAGENT_AGENT_SUBAGENT_WORK_ALLOCATION_STUDY.md
|   |   |-- 07_PARALLEL_EXECUTION_AND_CHECKOUT_LOCK_STUDY.md
|   |   |-- 08_FOUNDER_APPROVAL_BATCH_CONTROL_STUDY.md
|   |   |-- 09_ROI_AWARE_TASKS_NOTES_AND_QUESTIONS_STUDY.md
|   |   |-- 10_FEEDBACK_TO_LEARNING_LOOP_STUDY.md
|   |   |-- 11_PROJECT_SELF_DOCUMENTATION_SYSTEM_STUDY.md
|   |   |-- 12_RAG_METADATA_AND_VECTOR_CATEGORY_STUDY.md
|   |   |-- 13_CANONICAL_PATCH_CANDIDATES_FOR_DOC27.md
|   |   `-- 14_ACCEPTANCE_CRITERIA_FOR_DOC27.md
|   |-- 10_UIUX_STUDIES/
|   |   |-- ck_memory.md
|   |   |-- 01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md
|   |   |-- 02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md
|   |   |-- 03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md
|   |   |-- 04_MOBILE_COMMAND_FIRST_ERGONOMICS.md
|   |   |-- 05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md
|   |   |-- 06_UIUX_ANTI_PATTERNS_AND_GENERIC_AI_UI_RISKS.md
|   |   |-- 07_AGENT_ACTIVITY_STREAM_UIUX_STUDY.md
|   |   |-- 08_WHITELABEL_TOKEN_SYSTEM_UIUX_STUDY.md
|   |   |-- 09_EXECUTION_PLAN_WIDGET_UIUX_STUDY.md
|   |   |-- 10_INTENT_CLARIFIER_AND_SMART_QUESTIONS_UIUX_STUDY.md
|   |   |-- 11_COST_CREDITS_AND_ROI_AWARE_UX_STUDY.md
|   |   |-- 12_APPROVAL_GATE_AND_REVERSIBILITY_UX_STUDY.md
|   |   `-- 13_EVIDENCE_TRUST_AND_DECISION_UIUX_STUDY.md
|   `-- 99_ARCHIVE/
|-- 00_SYSTEM_GOVERNANCE/
|   |-- 00_DEPENDENCY_MAP.md
|   |-- 00_DOCUMENT_TEMPLATE.md
|   |-- 00_MASTER_MAP.md
|   |-- 00_README_SYSTEM_GOVERNANCE.md
|   `-- 00_TAXONOMY_AND_NAMING.md
|-- 01_THINKING_SYSTEM/
|   |-- 00_README_THINKING_SYSTEM.md
|   |-- 01_CKOS_AI_FIRST_CONSTITUTION.md
|   |-- 02_AI_FIRST_OBJECT_MODEL.md
|   |-- 03_AGENT_OPERATING_MODEL.md
|   |-- 04_AUTONOMY_AND_APPROVALS.md
|   `-- 05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
|-- 02_EXECUTION_SYSTEM/
|   |-- 00_README_EXECUTION_SYSTEM.md
|   |-- 06_SKILLS_REGISTRY.md
|   |-- 07_WORKFLOW_BLUEPRINTS.md
|   |-- 08_PROMPT_LIBRARY.md
|   `-- 09_TRANSFORMERS_AND_PIPELINES.md
|-- 03_RUNTIME_SYSTEM/
|   |-- 00_README_RUNTIME_SYSTEM.md
|   |-- 10_SYSTEM_RUNTIME_ARCHITECTURE.md
|   |-- 11_DATA_MODEL_AND_PERSISTENCE.md
|   |-- 12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
|   `-- 13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
|-- 04_PRODUCT_SYSTEM/
|   |-- 00_README_PRODUCT_SYSTEM.md
|   |-- 14_PROJECT_DASHBOARD_ARCHITECTURE.md
|   |-- 15_COMMAND_CENTER_ARCHITECTURE.md
|   `-- 16_NODE_CANVAS_ARCHITECTURE.md
|-- 05_IMPLEMENTATION_SYSTEM/
|   |-- 00_README_IMPLEMENTATION_SYSTEM.md
|   |-- 17_IMPLEMENTATION_PROTOCOL.md
|   |-- 18_RESEARCH_PROTOCOL.md
|   |-- 18_RESEARCH_PROTOCOL_FOR_MANUS.md
|   |-- 19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md
|   |-- 19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md
|   |-- 20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md
|   `-- 21_SELF_EVOLVING_SYSTEM.md (superseded/historico)
|-- 06_BUSINESS_SYSTEMS/
|   |-- 21_ROI_ARCHITECTURE.md
|   |-- 22_FEEDBACK_SYSTEM_ARCHITECTURE.md
|   |-- 23_SUPPORT_SYSTEM_ARCHITECTURE.md
|   `-- 24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md
|-- 07_EVOLUTION_SYSTEM/
|   |-- 00_README_EVOLUTION_SYSTEM.md
|   |-- 25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md
|   `-- 26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md
`-- 000_UPGRADE/
    |-- .obsidian/
    |   |-- app.json
    |   |-- appearance.json
    |   |-- core-plugins.json
    |   |-- graph.json
    |   `-- workspace.json
    |-- Bem-vindo.md
    |-- CKOS_CODEX_MEMORY.md
    |-- CKOS_CONTINUATION_PLAN.md
    |-- CKOS_INFRA_AUTOMATION_MEMORY.md
    |-- CKOS_RESEARCH_MEMORY.md
    |-- CKOS_UPGRADE_INDEX.md
    |-- CKOS_CREATOR_MODE_PACK/
    |   |-- 00_README_START_HERE.md
    |   |-- CKOS_CURRENT_STATE_SUMMARY.md
    |   |-- 01_PROTOCOLS/
    |   |   |-- CEO_AGENT_PLANNER_PROTOCOL.md
    |   |   |-- CHECKOUT_LOCK_PROTOCOL.md
    |   |   |-- PROJECT_CREATION_FROM_INTENT_PROTOCOL.md
    |   |   `-- SIMULATED_CREDITS_POLICY_FOR_PLANNING.md
    |   |-- 02_TEMPLATES/
    |   |   |-- FOUNDER_APPROVAL_CHECKLIST_TEMPLATE.md
    |   |   |-- PMO_AUDIT_HANDOFF_TEMPLATE.md
    |   |   |-- PROJECT_EXECUTION_PLAN_TEMPLATE.md
    |   |   |-- PROJECT_FILETREE_PROPOSAL_TEMPLATE.md
    |   |   `-- PROJECT_INTENT_ANALYSIS_TEMPLATE.md
    |   |-- 03_SKILLS/
    |   |   |-- CONTEXT_PACK_BUILDER_SIMULATION_SKILL.md
    |   |   |-- CREDITS_ESTIMATION_SKILL.md
    |   |   |-- INTENT_TO_PROJECT_PLAN_SKILL.md
    |   |   `-- PMO_AUDIT_SIMULATION_SKILL.md
    |   |-- 04_CATEGORIES/
    |   |   |-- PROJECT_CATEGORY_TAXONOMY.md
    |   |   `-- PROJECT_SUBCATEGORY_RULES.md
    |   |-- 05_EXAMPLES/
    |   |   `-- EXAMPLE_MIRIAM_PLANNING_ONLY.md
    |   |-- 06_HANDOFFS/
    |   |   |-- CEO_TO_FOUNDER_APPROVAL_REQUEST.md
    |   |   |-- CEO_TO_PMO_HANDOFF.md
    |   |   `-- PMO_TO_CEO_REVIEW.md
    |   `-- 07_SIMULATION_RUNTIME/
    |       |-- 00_SIMULATION_RUNTIME_INDEX.md
    |       |-- 01_SIMULATED_BACKEND_CONTRACT.md
    |       |-- 02_SIMULATED_API_ENDPOINT_MAP.md
    |       |-- 03_CONNECTOR_REGISTRY_SIMULATION.md
    |       |-- 04_MOCK_DATA_SCHEMAS.md
    |       |-- 05_EVENT_LOG_SIMULATION.md
    |       |-- 06_POLICY_MATRIX_FOR_SIMULATION.md
    |       |-- 07_PROJECT_TEST_SCENARIO_TEMPLATE.md
    |       `-- 08_DEMO_RUNBOOK_INTENT_TO_ARTIFACT.md
    |-- CKOS_CODEX_CONTINUATION_PACK/
    |   |-- 00_README_START_HERE.md
    |   |-- ck.md
    |   |-- 00_CONTEXT/
    |   |   |-- CKOS_CURRENT_STATE.md
    |   |   `-- FILETREE_EXPECTED_MAP.md
    |   |-- 01_PROMPTS/
    |   |   |-- ANTIGRAVITY_PARALLEL_REVIEW_PROMPT.md
    |   |   |-- CHATGPT_VISUAL_DIRECTOR_IMAGE_PROMPT_BRIEF.md
    |   |   `-- CODEX_MASTER_PROMPT.md
    |   |-- 02_SKILLS/
    |   |   |-- AI_FIRST_PROJECT_PLANNER_SKILL.md
    |   |   |-- CONTEXT_ENGINEERING_SKILL.md
    |   |   |-- PMO_DOCUMENTATION_SKILL.md
    |   |   `-- RESEARCH_COLLECTOR_SKILL.md
    |   |-- 03_ARCHITECTURE_NOTES/
    |   |   |-- 25_LEARNING_AND_PROJECT_STUDY_MODE.md
    |   |   |-- 26_COLLECTOR_REGISTRY_AND_RESEARCH_ACTORS.md
    |   |   |-- 27_CKSTORE_AND_CAPABILITY_MARKETPLACE.md
    |   |   |-- 28_PROJECT_PLANNER_AND_SELF_DOCUMENTING_PROJECTS.md
    |   |   `-- 29_VISUAL_DIRECTOR_AND_IMAGE_PROMPT_PIPELINE.md
    |   |-- 04_RESEARCH/
    |   |   `-- YOUTUBE_DEEP_RESEARCH_IDEA.md
    |   |-- 05_VISUAL_HTML_STUDY/
    |   |   |-- HTML_STUDY_ARCHITECTURE_BRIEF.md
    |   |   `-- PINTEREST_KEYWORDS_AND_IMAGE_TYPES.md
    |   `-- 06_ROADMAP/
    |       |-- DEVELOPMENT_PLAN_WITHOUT_UI.md
    |       `-- DOCS_21_TO_30_SEQUENCE.md
    |-- pack_notas_ckos_deep_research/
    |   |-- README.md
    |   |-- INDEX.md
    |   |-- 01_01-ckos-como-ai-first-operating-system.md
    |   |-- 02_02-ckos-vs-branddock.md
    |   |-- 03_03-arquitetura-local-para-vps.md
    |   |-- 04_04-project-pulse.md
    |   |-- 05_05-briefing-inteligente-com-nick.md
    |   |-- 06_06-proposal-engine.md
    |   |-- 07_07-agent-journey-e-runs.md
    |   |-- 08_08-organograma-de-agentes.md
    |   |-- 09_09-human-in-the-loop-e-aprovacoes.md
    |   |-- 10_10-models-costs.md
    |   |-- 11_11-sistema-de-creditos-planos-e-pagamentos.md
    |   |-- 12_12-knowledge-base-por-projeto.md
    |   |-- 13_13-decisions.md
    |   |-- 14_14-issues-pipeline-e-checkout-lock.md
    |   |-- 15_15-sprints-releases.md
    |   |-- 16_16-chat-operacional.md
    |   |-- 17_17-suporte-ia-humano.md
    |   |-- 18_18-seguranca-secrets-e-isolamento.md
    |   |-- 19_19-marketplace-de-workflows-e-docks.md
    |   `-- 20_20-linguagem-para-socios-e-influenciadores.md
    `-- ckos_digitalocean_n8n_pack/
        |-- 00_README_INDEX.md
        |-- 00_DigitalOcean_PMO/
        |   `-- 01_Decisao_PMO_Iniciar_com_DigitalOcean.md
        |-- 01_Financas_ROI/
        |   |-- 01_Runway_e_Queima_de_Credito.md
        |   |-- 02_ROI_Infra_por_Projeto.md
        |   |-- 03_Planner_de_Execucao_Custos.md
        |   `-- 04_Modelo_de_Custo_por_Agente.md
        |-- 02_N8N_Automations/
        |   |-- 00_Principios/
        |   |   |-- 00_INDEX.md
        |   |   |-- 01_N8N_como_Acelerador_nao_Core.md
        |   |   `-- 01_N8N_como_Acelerador_nao_Core.json
        |   |-- 01_Leads_Propostas/
        |   |   |-- 00_INDEX.md
        |   |   |-- 01_Captura_Lead/
        |   |   |   |-- 01_Webhook_Lead_para_Supabase.md
        |   |   |   `-- 01_Webhook_Lead_para_Supabase.json
        |   |   `-- 02_Proposta/
        |   |       |-- 01_Gerar_Resumo_de_Proposta_com_IA.md
        |   |       `-- 01_Gerar_Resumo_de_Proposta_com_IA.json
        |   |-- 02_Onboarding_Cliente/
        |   |   |-- 00_INDEX.md
        |   |   |-- 01_Briefing/
        |   |   |   |-- 01_Briefing_Inteligente_para_Cards.md
        |   |   |   `-- 01_Briefing_Inteligente_para_Cards.json
        |   |   `-- 02_Stakeholders/
        |   |       |-- 01_Mapear_Stakeholders_e_Aprovacoes.md
        |   |       `-- 01_Mapear_Stakeholders_e_Aprovacoes.json
        |   |-- 03_Knowledge_RAG/
        |   |   |-- 00_INDEX.md
        |   |   |-- 01_Ingestao/
        |   |   |   |-- 01_Ingestao_Arquivo_para_Knowledge.md
        |   |   |   `-- 01_Ingestao_Arquivo_para_Knowledge.json
        |   |   `-- 02_Sincronizacao/
        |   |       |-- 01_Sync_Google_Drive_para_Knowledge.md
        |   |       `-- 01_Sync_Google_Drive_para_Knowledge.json
        |   |-- 04_Content_Ops/
        |   |   |-- 00_INDEX.md
        |   |   |-- 01_Instagram/
        |   |   |   |-- 01_Capturar_Reels_Apify_e_Gerar_Insights.md
        |   |   |   `-- 01_Capturar_Reels_Apify_e_Gerar_Insights.json
        |   |   `-- 02_Roteiros/
        |   |       |-- 01_Gerar_Roteiro_Reels_por_Insight.md
        |   |       `-- 01_Gerar_Roteiro_Reels_por_Insight.json
        |   |-- 05_Billing_Credits/
        |   |   |-- 00_INDEX.md
        |   |   |-- 01_Creditos/
        |   |   |   |-- 01_Budget_Gate_antes_de_Run_Caro.md
        |   |   |   `-- 01_Budget_Gate_antes_de_Run_Caro.json
        |   |   `-- 02_Pagamentos/
        |   |       |-- 01_Evento_Stripe_Atualiza_Wallet.md
        |   |       `-- 01_Evento_Stripe_Atualiza_Wallet.json
        |   |-- 06_Support/
        |   |   |-- 00_INDEX.md
        |   |   `-- 01_Tickets/
        |   |       |-- 01_Ticket_Suporte_com_Contexto_do_Projeto.md
        |   |       `-- 01_Ticket_Suporte_com_Contexto_do_Projeto.json
        |   |-- 07_Observability/
        |   |   |-- 00_INDEX.md
        |   |   |-- 01_Logs/
        |   |   |   |-- 01_Log_Run_Agente_e_Custo.md
        |   |   |   `-- 01_Log_Run_Agente_e_Custo.json
        |   |   `-- 02_Alertas/
        |   |       |-- 01_Alerta_Erro_Workflow_ou_Custo.md
        |   |       `-- 01_Alerta_Erro_Workflow_ou_Custo.json
        |   |-- 08_Connectors_OAuth/
        |   |   |-- 00_INDEX.md
        |   |   |-- 01_Google/
        |   |   |   |-- 01_Conector_Google_Drive_Calendar_Gmail.md
        |   |   |   `-- 01_Conector_Google_Drive_Calendar_Gmail.json
        |   |   `-- 02_Meta/
        |   |       |-- 01_Conector_Meta_Ads_Instagram.md
        |   |       `-- 01_Conector_Meta_Ads_Instagram.json
        |   |-- 09_Agent_Handoffs/
        |   |   |-- 00_INDEX.md
        |   |   `-- 01_Handoffs/
        |   |       |-- 01_Handoff_entre_Agentes_com_Log.md
        |   |       `-- 01_Handoff_entre_Agentes_com_Log.json
        |   `-- 10_Internal_Ops/
        |       |-- 00_INDEX.md
        |       `-- 01_Backup/
        |           |-- 01_Backup_Diario_Supabase_Metadata.md
        |           `-- 01_Backup_Diario_Supabase_Metadata.json
        |-- 03_Policies/
        |   |-- 01_Policy_Custos_Budget_Gates.md
        |   `-- 02_Policy_N8N_Prototipo_para_Codigo.md
        `-- 04_Codex_Instructions/
            `-- 00_Contexto_Mestre_para_Codex.md
```

## O que NAO fazer a partir deste mapa

- Nao inferir autorizacao para criar docs 26-34.
- Nao inferir autorizacao para implementar UI/UX, backend, migrations, schema de banco, agentes, APIs ou automacoes.
- Nao mover, deletar, renomear ou renumerar nenhum arquivo.
- Nao tratar `000_ROADMAPS/` como documentacao canonica; e camada auxiliar governada de planejamento.
- Nao acionar Antigravity a partir de roadmap sem handoff de estudo e approval Founder.
- Nao acionar Antigravity a partir do gate P1.7 sem sessao futura `design_study` aprovada explicitamente pelo Founder.
- Nao promover arquivos de packs a status canonico sem patch plan.
- Nao tratar JSONs n8n como runtime CKOS.
- Nao tratar arquivos especificos de Manus como infraestrutura definitiva do CKOS.
- Nao promover arquivos de `000_UPLOADS/` direto para docs canonicos.
- Nao tratar `000_STUDY_NOTES/09_APPROVED_FOR_CANONICAL_PATCH/` como canonico; significa apenas pronto para patch plan.
