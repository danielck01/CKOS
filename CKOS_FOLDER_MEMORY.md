---
title: CKOS Folder Memory
system_id: ckos_folder_memory
category: vault_memory
status: draft
version: 1.8.0
updated_at: 2026-05-28
owner: ceo_agent
reviewers:
  - founder
  - pmo_ckos
  - metacognik
related_notes:
  - ARCHITECTURE_PATCH_REPORT.md
  - QA_DOCUMENTATION_CHECKLIST.md
  - CKOS_VAULT_MAP_REFRESH_REPORT.md
  - CKOS_FILETREE_MAP.md
  - 000_UPGRADE/CKOS_UPGRADE_INDEX.md
  - 000_UPGRADE/CKOS_CONTINUATION_PLAN.md
  - 000_UPGRADE/CKOS_CREATOR_MODE_PACK/00_README_START_HERE.md
  - 000_UPLOADS/00_UPLOADS_INDEX.md
  - 000_STUDY_NOTES/00_STUDY_INDEX.md
  - 000_ROADMAPS/README.md
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
  - 000_STUDY_NOTES/12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md
  - 000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/README.md
created_for: CKOS_DOCUMENTATION_REVIEWED
---

# CKOS Folder Memory

## Estado executivo

O vault `CKOS_DOCUMENTATION_REVIEWED` e a fonte operacional revisada da documentacao CKOS. O estado real atual e mais avancado que alguns packs de continuidade em `000_UPGRADE`: docs 21-24 existem em `06_BUSINESS_SYSTEMS`, `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` existe em draft, e `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` foi preservado como historico/superseded.

Formula correta para agentes paralelos:

> Docs 21-24 estao documentalmente concluidos, aguardando aprovacao formal Founder + Technical + Metacognik. Implementacao continua bloqueada.

Nenhum agente deve recriar docs 22-24, iniciar docs 26-34, renumerar arquivos ou tratar packs antigos como source-of-truth sem aprovacao humana.

`000_ROADMAPS/` foi estabilizada em 2026-05-28 como camada auxiliar governada de planejamento vivo. Ela nao e canonica, nao autoriza implementacao e deve ser usada como controle de trafego para sessoes Codex, Claude, Antigravity, CEO Agent, PMO Auditor e especialistas.

`000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md` foi criada em 2026-05-28 como study note auxiliar para o padrao Intent -> Question -> Plan -> Execution. Ela nao e canonica e nao autoriza implementacao.

P1.7 criou `000_ROADMAPS/SESSION_REGISTRY.md`, `000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md` e `000_STUDY_NOTES/12_SESSION_GATES/` para governar sessoes simultaneas, checkout lock/release, nivel de inteligencia e gate Antigravity Design Study. P1.7 e auxiliar, nao canonico, nao cria docs 26-34, nao inicia UI/UX e nao inicia Antigravity.

P1.7.1 promoveu os tres arquivos principais de P1.7 para v1.0.0, adicionou a frase obrigatoria da politica, criou `000_STUDY_NOTES/12_SESSION_GATES/ck_memory.md` como memoria ativa da pasta, preservou `_folder_memory.md` como legacy/superseded e registrou P1.7/P1.7.1 em `ARCHITECTURE_PATCH_REPORT.md`.

Em 2026-05-30, a Study Layer `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/` foi criada como infraestrutura cognitiva auxiliar para estudar Project AI-first, Task AI-first, Notes AI-first, perguntas inteligentes, approval batch, ROI, feedback, learning e candidatos para Doc 27. Ela e study-only, nao canonica, nao cria docs 27-34 e nao autoriza implementacao, agentes reais ou runtime.

## Travas de refresh 2026-05-26

- Docs 21-24 Business Systems ja existem em `06_BUSINESS_SYSTEMS/`.
- Gate I esta documentalmente completo, e o microgate Self-Evolving esta registrado conforme `ARCHITECTURE_PATCH_REPORT.md` v1.9.0.
- Nao recriar docs 21-24.
- Nao criar docs 26-34 sem autorizacao explicita do Founder.
- Nao iniciar UI/UX implementation.
- Nao iniciar backend, migrations, API, banco de dados, agentes reais ou automacoes runtime.
- Nao mover, deletar, renomear ou renumerar arquivos sem relatorio previo.
- Nao transformar n8n em core CKOS.
- Nao tratar Manus como infraestrutura definitiva do CKOS.
- Self-Evolving ativo agora e doc 25 em `07_EVOLUTION_SYSTEM/`; ROI permanece doc 21.
- Connectors, MCP and Integrations ativo agora e doc 26 em `07_EVOLUTION_SYSTEM/`; vendors permanecem substituiveis e governados.

## Travas de microgate 2026-05-27

- `000_UPLOADS/` foi criada como camada RAW aprovada pelo Founder.
- `000_STUDY_NOTES/` foi criada como camada STUDY aprovada pelo Founder.
- Nenhum arquivo existente foi movido para essas pastas neste microgate.
- Nenhum doc canonico 01-24 foi alterado neste microgate.
- `00_MASTER_MAP.md`, `00_DOCUMENT_TEMPLATE.md`, `00_TAXONOMY_AND_NAMING.md`, `00_DEPENDENCY_MAP.md` e `ARCHITECTURE_PATCH_REPORT.md` permanecem para patch documental separado.
- RAW nao e fonte de verdade.
- STUDY nao e canonico.
- `09_APPROVED_FOR_CANONICAL_PATCH/` significa apenas pronto para patch plan.

## Travas de study note Intent Pattern 2026-05-28

- `000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/` e subpasta STUDY auxiliar.
- `01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md` registra padrao operacional, nao documento canonico.
- Docs 26-34 nao foram criados.
- UI/UX, Antigravity, backend, API, banco, migrations, JSONs n8n e agentes reais continuam bloqueados.
- Qualquer canonizacao futura exige patch candidate, QA documental e approval Founder.

## Travas de P1.7 Multi-Session 2026-05-28

- `SESSION_REGISTRY.md` foi criado antes dos demais arquivos P1.7.
- `MULTI_SESSION_EXECUTION_POLICY.md` e politica auxiliar, com `confidence: unverified` e `provenance_status: unverified`.
- `000_STUDY_NOTES/12_SESSION_GATES/` foi criada como pasta STUDY auxiliar para gates de sessao.
- Antigravity so pode operar futuramente em `design_study` apos gate formal aprovado pelo Founder.
- Nenhuma pergunta de decisao deve ser apresentada sem impacto em ROI, risco, custo ou governanca.
- P1.7 nao alterou `ARCHITECTURE_PATCH_REPORT.md`, docs canonicos, docs 26-34, UI, backend, API, banco, migrations, JSONs n8n ou agentes reais.

## Travas de P1.7.1 Memory Refresh 2026-05-28

- `MULTI_SESSION_EXECUTION_POLICY.md`, `SESSION_REGISTRY.md` e `01_ANTIGRAVITY_STUDY_MODE_GATE.md` estao em `version: 1.0.0`.
- `12_SESSION_GATES/ck_memory.md` e a memoria ativa da pasta.
- `12_SESSION_GATES/_folder_memory.md` permanece preservado como legacy/superseded.
- `ARCHITECTURE_PATCH_REPORT.md` registra P1.7/P1.7.1 sem liberar implementacao.
- Antigravity, Design Study, UI/UX, backend, API, banco, migrations, JSONs n8n, agentes reais e docs 26-34 continuam bloqueados.

## Travas de Study Layer 13 2026-05-30

- `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/` e Study Layer auxiliar, nao canonica.
- A pasta prepara auditoria e decisao PMO para Doc 27, mas nao cria Doc 27 nem qualquer doc 28-34.
- Docs 01-26 nao devem ser alterados por esta camada de estudo.
- `ARCHITECTURE_PATCH_REPORT.md`, `QA_DOCUMENTATION_CHECKLIST.md`, `000_UPLOADS/` e `000_UPGRADE/` permanecem fora do escopo desta sessao.
- UI, backend, API, banco, migrations, MCP server real, JSONs n8n, agentes reais e automacoes runtime continuam bloqueados.
- Candidatos para Doc 27 dentro da pasta 13 sao hipoteses de estudo, nao patch plan aprovado.
- Proximo passo obrigatorio: auditoria Claude/Metacognik antes de qualquer canonizacao.

## Travas de microgate Self-Evolving 2026-05-27

- `07_EVOLUTION_SYSTEM/` foi criada como nova camada canonica draft.
- `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` foi criado apos aprovacao Founder.
- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` foi preservado no lugar original e marcado como superseded/historico.
- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md` permanece o doc 21 ativo.
- Docs 26-34 nao foram criados.
- UI/UX, backend, migrations, API, banco, agentes reais e automacoes runtime continuam bloqueados.

## Travas de P0 Roadmaps 2026-05-28

- `000_ROADMAPS/` e camada auxiliar governada, nao canonica.
- Controles raiz obrigatorios existem: `ck_memory.md`, `ck_tasks.md`, `ck_risks.md`, `ck_roi.md`, `ck_feedback.md`, `ck_agent_handoffs.md`.
- `05_SUPERAGENTS_AGENTS_SUBAGENTS_ROADMAP/` foi mantida sem rename.
- Uma sessao nova deve ler `README.md` + `ck_memory.md` antes de agir.
- Um agente escreve; outro audita.
- Antigravity/UI-UX continuam bloqueados ate handoff de estudo e approval Founder.
- Docs 26-34 continuam bloqueados.

## Memoria por pasta - refresh 2026-05-26

### Raiz do vault

- Nome da pasta: `CKOS_DOCUMENTATION_REVIEWED/`.
- Funcao da pasta: fonte operacional revisada da documentacao CKOS e ponto de entrada para agentes documentais.
- Documentos principais: `ARCHITECTURE_PATCH_REPORT.md`, `QA_DOCUMENTATION_CHECKLIST.md`, `CKOS_FOLDER_MEMORY.md`, `CKOS_FILETREE_MAP.md`, `CKOS_VAULT_MAP_REFRESH_REPORT.md`.
- Documentos auxiliares: `Memória GPT.md`.
- Documentos historicos/supersedidos: nenhum confirmado; `Memória GPT.md` ainda precisa classificacao.
- Ultimos arquivos adicionados: `CKOS_FILETREE_MAP.md`, `CKOS_VAULT_MAP_REFRESH_REPORT.md`, `CKOS_FOLDER_MEMORY.md`.
- Dependencias: todos os agentes devem cruzar raiz com `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md` e `000_UPGRADE/CKOS_UPGRADE_INDEX.md`.
- Riscos de confusao: usar memoria solta como canonica; ler trechos antigos do patch report sem considerar o header v1.7.0.
- Proximos passos recomendados: submeter Gate I para aprovacao formal e preparar microgate dos docs 26-31 antes de UI/UX.
- O que NAO fazer nesta pasta: nao criar codigo, app, UI, backend, migration ou agentes; nao mover arquivos sem relatorio.

### `00_SYSTEM_GOVERNANCE/`

- Nome da pasta: `00_SYSTEM_GOVERNANCE`.
- Funcao da pasta: governar mapa, template, taxonomia, naming e dependencias.
- Documentos principais: `00_MASTER_MAP.md`, `00_DOCUMENT_TEMPLATE.md`, `00_TAXONOMY_AND_NAMING.md`, `00_DEPENDENCY_MAP.md`.
- Documentos auxiliares: `00_README_SYSTEM_GOVERNANCE.md`.
- Documentos historicos/supersedidos: nenhum confirmado.
- Ultimos arquivos adicionados: nenhum novo em 2026-05-26; `00_MASTER_MAP.md` recebeu refresh documental v2.3.0.
- Dependencias: `CKOS_FILETREE_MAP.md`, `ARCHITECTURE_PATCH_REPORT.md`, docs 10-24.
- Riscos de confusao: mapa v2.2.0 historico ainda citava apenas 05_IMPLEMENTATION_SYSTEM como fechamento; refresh registra `06_BUSINESS_SYSTEMS/`.
- Proximos passos recomendados: apos decisao Founder, atualizar `00_DEPENDENCY_MAP.md` para refletir docs 21-24 e destino do Self-Evolving.
- O que NAO fazer nesta pasta: nao alterar taxonomia canonica sem patch registrado e aprovacao.

### `01_THINKING_SYSTEM/`

- Nome da pasta: `01_THINKING_SYSTEM`.
- Funcao da pasta: definir constituicao AI-first, objetos, agentes, autonomia, approvals, memoria e contexto.
- Documentos principais: `01_CKOS_AI_FIRST_CONSTITUTION.md`, `02_AI_FIRST_OBJECT_MODEL.md`, `03_AGENT_OPERATING_MODEL.md`, `04_AUTONOMY_AND_APPROVALS.md`, `05_MEMORY_AND_CONTEXT_ARCHITECTURE.md`.
- Documentos auxiliares: `00_README_THINKING_SYSTEM.md`.
- Documentos historicos/supersedidos: nenhum confirmado.
- Ultimos arquivos adicionados: nenhum novo no refresh.
- Dependencias: governance 00, doc 25 e futuras decisoes de docs 26-34.
- Riscos de confusao: reduzir CKOS a chat, dashboard ou app de tarefas.
- Proximos passos recomendados: usar esta camada como filtro para qualquer proposta de Learning, Planner, CKStore, Visual Director ou UI/UX.
- O que NAO fazer nesta pasta: nao adicionar agentes ou objetos novos sem amarrar a runtime/data/security.

### `02_EXECUTION_SYSTEM/`

- Nome da pasta: `02_EXECUTION_SYSTEM`.
- Funcao da pasta: definir skills, workflows, prompts, transformers e pipelines.
- Documentos principais: `06_SKILLS_REGISTRY.md`, `07_WORKFLOW_BLUEPRINTS.md`, `08_PROMPT_LIBRARY.md`, `09_TRANSFORMERS_AND_PIPELINES.md`.
- Documentos auxiliares: `00_README_EXECUTION_SYSTEM.md`.
- Documentos historicos/supersedidos: nenhum confirmado.
- Ultimos arquivos adicionados: nenhum novo no refresh.
- Dependencias: Thinking System e Runtime System.
- Riscos de confusao: promover skills do continuation pack como registry canonico.
- Proximos passos recomendados: avaliar impactos de docs 25-29 no Skills Registry apenas depois de autorizados.
- O que NAO fazer nesta pasta: nao transformar prompts auxiliares em runtime ou automacao real.

### `03_RUNTIME_SYSTEM/`

- Nome da pasta: `03_RUNTIME_SYSTEM`.
- Funcao da pasta: definir runtime, data model, security, evals, observability e cost control.
- Documentos principais: `10_SYSTEM_RUNTIME_ARCHITECTURE.md`, `11_DATA_MODEL_AND_PERSISTENCE.md`, `12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`, `13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`.
- Documentos auxiliares: `00_README_RUNTIME_SYSTEM.md`.
- Documentos historicos/supersedidos: nenhum confirmado.
- Ultimos arquivos adicionados: nenhum novo em 2026-05-26; docs 10-13 foram consolidados em 2026-05-25.
- Dependencias: docs 01-09 e patches sugeridos P21-1 a P24-6.
- Riscos de confusao: tratar n8n, collectors externos ou JSONs como runtime canonico.
- Proximos passos recomendados: antes de qualquer implementacao, avaliar patches P21-1 a P24-6 para docs 10/11.
- O que NAO fazer nesta pasta: nao criar migrations, tabelas reais, backend ou workers.

### `04_PRODUCT_SYSTEM/`

- Nome da pasta: `04_PRODUCT_SYSTEM`.
- Funcao da pasta: projetar runtime em Dashboard, Command Center e Node Canvas.
- Documentos principais: `14_PROJECT_DASHBOARD_ARCHITECTURE.md`, `15_COMMAND_CENTER_ARCHITECTURE.md`, `16_NODE_CANVAS_ARCHITECTURE.md`.
- Documentos auxiliares: `00_README_PRODUCT_SYSTEM.md`.
- Documentos historicos/supersedidos: nenhum confirmado.
- Ultimos arquivos adicionados: nenhum novo em 2026-05-26; docs 14-16 foram consolidados em 2026-05-25.
- Dependencias: Runtime 10-13 e Business Systems 21-24 para projections futuras.
- Riscos de confusao: usar estudo visual como autorizacao de UI; CommandBar chamar agente direto.
- Proximos passos recomendados: manter UI/UX bloqueado ate docs futuros e gates.
- O que NAO fazer nesta pasta: nao criar telas, componentes, CSS, UX final ou prototipo navegavel.

### `05_IMPLEMENTATION_SYSTEM/`

- Nome da pasta: `05_IMPLEMENTATION_SYSTEM`.
- Funcao da pasta: definir protocolo de implementacao, pesquisa, execucao multiagente, QA e Founder approval.
- Documentos principais: `17_IMPLEMENTATION_PROTOCOL.md`, `18_RESEARCH_PROTOCOL.md`, `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`, `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`.
- Documentos auxiliares: `00_README_IMPLEMENTATION_SYSTEM.md`.
- Documentos historicos/supersedidos: `18_RESEARCH_PROTOCOL_FOR_MANUS.md`, `19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md`, `21_SELF_EVOLVING_SYSTEM.md`.
- Ultimos arquivos adicionados: docs 17-20 foram atualizados em 2026-05-25; nenhum arquivo novo em 2026-05-26.
- Dependencias: Runtime 10-13, Product 14-16, Governance 00, QA doc 20.
- Riscos de confusao: usar `21_SELF_EVOLVING_SYSTEM.md` como fonte ativa; Manus virar dependencia estrutural.
- Proximos passos recomendados: manter Self-Evolving ativo em `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`.
- O que NAO fazer nesta pasta: nao renomear, mover ou deletar o antigo Self-Evolving; nao executar implementacao; nao transformar Manus em infra CKOS.

### `06_BUSINESS_SYSTEMS/`

- Nome da pasta: `06_BUSINESS_SYSTEMS`.
- Funcao da pasta: definir sistemas de negocio de ROI, feedback, suporte, creditos, planos e billing.
- Documentos principais: `21_ROI_ARCHITECTURE.md`, `22_FEEDBACK_SYSTEM_ARCHITECTURE.md`, `23_SUPPORT_SYSTEM_ARCHITECTURE.md`, `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`.
- Documentos auxiliares: nenhum identificado.
- Documentos historicos/supersedidos: nenhum identificado.
- Ultimos arquivos adicionados: docs 21-24 criados/modificados em 2026-05-25.

### `07_EVOLUTION_SYSTEM/`

- Nome da pasta: `07_EVOLUTION_SYSTEM`.
- Funcao da pasta: definir evolucao segura do CKOS, incluindo learning loops, improvement proposals, sandbox, evals, approval, rollback e audit log.
- Documentos principais: `25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`; `26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`.
- Documentos auxiliares: `00_README_EVOLUTION_SYSTEM.md`.
- Documentos historicos/supersedidos: nenhum dentro da pasta; fonte historica externa preservada em `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`.
- Ultimos arquivos adicionados: `26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md` em 2026-05-29.
- Dependencias: Runtime 10, Data Model 11, Security 12, Evals 13, Implementation 17/20, Business Systems 21-24 e RAW/STUDY.
- Riscos de confusao: interpretar self-evolution como auto-deploy ou autonomia irrestrita; usar sandbox output como producao; tratar MCP, n8n, Apify, Perplexity, OpenRouter ou qualquer vendor como bypass de runtime, policy, approval, cost guard, audit ou tenant isolation.
- Proximos passos recomendados: Claude auditar o Doc 26 antes de patches em docs 10-13/18/24 ou abertura de docs 27-34.
- O que NAO fazer nesta pasta: nao implementar agentes, automacoes runtime, auto-deploy ou alteracoes automaticas de producao.
- Dependencias: docs 10-13, 14-16 e 17-20.
- Riscos de confusao: agentes antigos acharem que docs 22-24 faltam; confundir Gate I documental completo com liberacao de implementacao.
- Proximos passos recomendados: submeter Gate I para aprovacao formal Founder + Technical + Metacognik.
- O que NAO fazer nesta pasta: nao recriar docs 21-24, nao criar docs 26-34, nao implementar billing/credits/support/feedback/ROI.

### `000_UPLOADS/`

- Nome da pasta: `000_UPLOADS`.
- Funcao da pasta: camada RAW de entrada bruta para pesquisas, referencias, outputs de IA, documentos, datasets, media, exports de conectores e insumos de cliente.
- Documentos principais: `README.md`, `_folder_memory.md`, `00_UPLOADS_INDEX.md`.
- Documentos auxiliares: READMEs e `_folder_memory.md` em todas as subpastas.
- Documentos historicos/supersedidos: nenhum; pasta criada em 2026-05-27.
- Ultimos arquivos adicionados: estrutura completa RAW aprovada no microgate `UPLOADS_STUDY_MICROGATE_PROPOSAL`.
- Dependencias: `000_STUDY_NOTES/`, docs de governance e protocolos de research/QA.
- Riscos de confusao: tratar upload, output de IA, export de conector, Manus ou n8n como fonte canonica.
- Proximos passos recomendados: usar somente para novas entradas brutas; nao mover material antigo sem patch plan.
- O que NAO fazer nesta pasta: nao colocar secrets, nao canonizar direto, nao implementar conectores ou automacoes.

### `000_STUDY_NOTES/`

- Nome da pasta: `000_STUDY_NOTES`.
- Funcao da pasta: camada STUDY de interpretacao, source manifests, notas estudadas, syntheses, decision logs e patch candidates.
- Documentos principais: `README.md`, `_folder_memory.md`, `00_STUDY_INDEX.md`, `_templates/*`.
- Documentos auxiliares: READMEs e `_folder_memory.md` em todas as subpastas.
- Documentos historicos/supersedidos: nenhum; pasta criada em 2026-05-27.
- Ultimos arquivos adicionados: `11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md`; `12_SESSION_GATES/README.md`, `ck_memory.md`, `_folder_memory.md` e `01_ANTIGRAVITY_STUDY_MODE_GATE.md`; `10_UIUX_STUDIES/` com notas de estudo UI/UX e seu `ck_memory.md`; `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/` com 21 arquivos de Study Layer AI-first para Project, Task, Notes, perguntas inteligentes, approval batch, ROI, feedback, learning e candidatos Doc 27; alem dos templates RAW/STUDY e estrutura completa de estudo.
- Dependencias: `000_UPLOADS/`, governance, QA, approval protocols, doc 25 e futuros docs 26-34.
- Riscos de confusao: tratar study note como canonico, usar `09_APPROVED_FOR_CANONICAL_PATCH/` como autorizacao de patch aplicado ou interpretar gate criado como Antigravity ativo.
- Proximos passos recomendados: Claude/Metacognik auditar Study Layer 13 antes de qualquer Doc 27; manter Antigravity blocked ate sessao futura `design_study` aprovada pelo Founder.
- O que NAO fazer nesta pasta: nao aplicar patch canonico, nao mover docs oficiais, nao criar implementacao.

### `000_STUDY_NOTES/10_UIUX_STUDIES/`

- Nome da pasta: `000_STUDY_NOTES/10_UIUX_STUDIES/`.
- Propósito: Armazenar notas de estudo conceituais estruturadas fáceis de ler, focadas em traduzir referências de design do Canvas OS / AI OS para Designers em linguagem operacional de runtime baseada em agentes do CKOS.
- Regras de Entrada: Relatório e imagens de referência da pasta de uploads/estudo; diretrizes conceituais do Founder.
- Regras de Saída: 13 notas de estudo cobrindo taxonomia visual, gramática operacional, matriz de transição de estados de IA, ergonomia mobile, regras de neurodesign/carga cognitiva, riscos/anti-patterns de interfaces de IA genéricas, stream de atividades de agentes, tematização whitelabel, widgets de plano de execução, perguntas inteligentes/clarificador, wallets/custos/créditos, portões de aprovação/reversibilidade e mapas de evidências/confiança.
- Documentos principais: `ck_memory.md`, `01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md`, `02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md`, `03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md`, `04_MOBILE_COMMAND_FIRST_ERGONOMICS.md`, `05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md`, `06_UIUX_ANTI_PATTERNS_AND_GENERIC_AI_UI_RISKS.md`, `07_AGENT_ACTIVITY_STREAM_UIUX_STUDY.md`, `08_WHITELABEL_TOKEN_SYSTEM_UIUX_STUDY.md`, `09_EXECUTION_PLAN_WIDGET_UIUX_STUDY.md`, `10_INTENT_CLARIFIER_AND_SMART_QUESTIONS_UIUX_STUDY.md`, `11_COST_CREDITS_AND_ROI_AWARE_UX_STUDY.md`, `12_APPROVAL_GATE_AND_REVERSIBILITY_UX_STUDY.md` e `13_EVIDENCE_TRUST_AND_DECISION_UIUX_STUDY.md`.
- Status: active auxiliary STUDY folder (draft notes).
- Próximos passos: Revisão do PMO Auditor e aprovação do Founder para embasar futuras especificações de UI/UX nas lanes corretas.
- O que NAO fazer nesta pasta: Não implementar código real (React, HTML, CSS, Tailwind), não criar design systems implementáveis, não produzir mockups ou componentes finais, e não propor alterações automáticas à arquitetura canônica.


### `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/`

- Nome da pasta: `000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/`.
- Proposito: Estudar a infraestrutura cognitivo-operacional que conecta intencao minima, perguntas inteligentes, briefing, plano, tarefas AI-first, superagents/agents/subagents, notas, memoria, feedback, ROI, learning e autodesenvolvimento documental.
- Regras de Entrada: contexto obrigatorio dos roadmaps, policy multi-sessao, padrao Intent -> Question -> Plan -> Execution, docs 05-13 e Doc 26 v1.0.2.
- Regras de Saida: candidatos e criterios para futura decisao PMO sobre Doc 27; nenhuma saida e canonica sem patch plan, QA e approval Founder.
- Documentos principais: `README.md`, `ck_memory.md`, `ck_tasks.md`, `ck_risks.md`, `ck_roi.md`, `ck_feedback.md`, `ck_agent_handoffs.md`, notas `01` a `14`.
- Status: active auxiliary STUDY folder, draft, unverified.
- Proximos passos: Claude/Metacognik auditar a camada antes de qualquer Doc 27 ou patch canonico.
- O que NAO fazer nesta pasta: nao criar Doc 27, nao criar docs 28-34, nao implementar UI/backend/API/banco/migrations, nao criar MCP server real, nao tocar JSONs n8n, nao criar agentes reais e nao iniciar automacoes runtime.


### `000_ROADMAPS/`

- Nome da pasta: `000_ROADMAPS`.
- Funcao da pasta: camada auxiliar governada para roadmaps vivos, tarefas, riscos, ROI operacional, feedback e handoffs entre sessoes.
- Documentos principais: `README.md`, `ck_memory.md`, `ck_tasks.md`, `ck_risks.md`, `ck_roi.md`, `ck_feedback.md`, `ck_agent_handoffs.md`, `SESSION_REGISTRY.md`, `MULTI_SESSION_EXECUTION_POLICY.md`, `ROADMAP_RECONCILIATION_REPORT.md`, `ROADMAP_ROUTING_MATRIX.md`.
- Documentos auxiliares: subpastas `00_MASTER_ROADMAP/` a `21_LEARNING_AND_KNOWLEDGE_ROADMAP/`.
- Documentos historicos/supersedidos: nenhum confirmado por rename/move/delete; `02`, `06`, `07` e `10` sao legacy-index candidates segundo `ROADMAP_ROUTING_MATRIX.md`.
- Ultimos arquivos adicionados: roadmaps `14-21`, `ROADMAP_RECONCILIATION_REPORT.md`, `ROADMAP_ROUTING_MATRIX.md`, `SESSION_REGISTRY.md` e `MULTI_SESSION_EXECUTION_POLICY.md`.
- Dependencias: mapas auxiliares, memoria da pasta, checkout lock e approval Founder para excecoes.
- Riscos de confusao: tratar roadmap como canonico; acionar Antigravity/UI-UX antes do study layer; agente ler contexto demais; sessoes paralelas editarem sem lock/registry; escolher roadmap antigo ou novo sem matriz; omitir nivel de inteligencia.
- Proximos passos recomendados: PMO/Metacognik auditar P1.7; Founder decidir se abre sessao futura `design_study` para Antigravity ou P2 para expansao das lanes.
- O que NAO fazer nesta pasta: nao criar docs canonicos, nao criar docs 26-34, nao implementar UI/backend/API/banco/migrations, nao rodar JSONs n8n, nao acionar Antigravity.

### `000_UPGRADE/`

- Nome da pasta: `000_UPGRADE`.
- Funcao da pasta: area auxiliar de packs, pesquisas, infra temporaria, n8n, prompts e memorias operacionais.
- Documentos principais: nenhum canonico.
- Documentos auxiliares: `CKOS_CODEX_MEMORY.md`, `CKOS_INFRA_AUTOMATION_MEMORY.md`, `CKOS_RESEARCH_MEMORY.md`, `CKOS_UPGRADE_INDEX.md`, `CKOS_CONTINUATION_PLAN.md`, `CKOS_CREATOR_MODE_PACK/`, `CKOS_CREATOR_MODE_PACK/07_SIMULATION_RUNTIME/`, `Bem-vindo.md`.
- Documentos historicos/supersedidos: roadmaps internos que tratam docs 22-24 como pendentes.
- Ultimos arquivos adicionados: Creator Mode Pack, `CKOS_CURRENT_STATE_SUMMARY.md`, `07_SIMULATION_RUNTIME/`, continuation pack, n8n pack, deep research pack e memorias criadas/importadas em 2026-05-26.
- Dependencias: deve ser lido contra `ARCHITECTURE_PATCH_REPORT.md`, `CKOS_FILETREE_MAP.md` e docs canonicos 00-24.
- Riscos de confusao: pack antigo virar source of truth; n8n virar core; estudos visuais dispararem UI/UX.
- Proximos passos recomendados: usar `CKOS_CREATOR_MODE_PACK/` e `07_SIMULATION_RUNTIME/` para novos chats de criacao de projeto antes do Projeto Miriam; manter indice de absorvido/auxiliar/desatualizado e usar packs apenas como insumo.
- O que NAO fazer nesta pasta: nao promover arquivos a canonicos, nao rodar JSONs n8n, nao criar backend/UI/migrations.

### `000_UPGRADE/CKOS_CREATOR_MODE_PACK/`

- Nome da pasta: `CKOS_CREATOR_MODE_PACK`.
- Funcao da pasta: pack auxiliar para simular Creator Mode no Codex, transformando intencao minima em plano auditavel, custo estimado, PMO audit, filetree proposta e artefatos aprovaveis.
- Documentos principais: nenhum canonico.
- Documentos auxiliares: `00_README_START_HERE.md`, `CKOS_CURRENT_STATE_SUMMARY.md`, `01_PROTOCOLS/*`, `02_TEMPLATES/*`, `03_SKILLS/*`, `04_CATEGORIES/*`, `05_EXAMPLES/*`, `06_HANDOFFS/*`, `07_SIMULATION_RUNTIME/*`.
- Documentos historicos/supersedidos: nenhum; pack criado apos aprovacao Founder.
- Ultimos arquivos adicionados: `CKOS_CURRENT_STATE_SUMMARY.md` e `07_SIMULATION_RUNTIME/` em 2026-05-26.
- Dependencias: `CKOS_UPGRADE_INDEX.md`, `CKOS_CONTINUATION_PLAN.md`, docs 07, 10, 15, 18, 20 e 24 como inspiracao operacional.
- Riscos de confusao: tratar skills simuladas como agentes reais; tratar endpoints simulados como API real; tratar Creator Mode Pack como doc canonico; iniciar Projeto Miriam antes de filetree aprovada.
- Proximos passos recomendados: usar este pack para abrir o chat CEO Agent e rodar primeiro teste controlado com uma intencao curta.
- O que NAO fazer nesta pasta: nao criar docs 26-34, nao implementar runtime, nao criar API/backend, nao executar conectores reais, nao gerar pack de notas de cliente sem approval de filetree.

### `000_UPGRADE/CKOS_CODEX_CONTINUATION_PACK/`

- Nome da pasta: `CKOS_CODEX_CONTINUATION_PACK`.
- Funcao da pasta: pack auxiliar para continuidade Codex/Claude/Antigravity.
- Documentos principais: nenhum canonico.
- Documentos auxiliares: `00_README_START_HERE.md`, `00_CONTEXT/*`, `01_PROMPTS/*`, `02_SKILLS/*`, `03_ARCHITECTURE_NOTES/*`, `04_RESEARCH/*`, `05_VISUAL_HTML_STUDY/*`, `06_ROADMAP/*`.
- Documentos historicos/supersedidos: `06_ROADMAP/DEVELOPMENT_PLAN_WITHOUT_UI.md` e partes de `DOCS_21_TO_30_SEQUENCE.md` que tratam 22-24 como pendentes.
- Ultimos arquivos adicionados: pack importado em 2026-05-26.
- Dependencias: `CKOS_UPGRADE_INDEX.md`, `CKOS_CONTINUATION_PLAN.md`, patch report v1.7.0.
- Riscos de confusao: criar docs 26-34 automaticamente ou iniciar estudo visual como UI.
- Proximos passos recomendados: usar notas 25-29 apenas como backlog de arquitetura futura.
- O que NAO fazer nesta pasta: nao executar prompts como implementacao; nao recriar docs 21-24.

### `000_UPGRADE/ckos_digitalocean_n8n_pack/`

- Nome da pasta: `ckos_digitalocean_n8n_pack`.
- Funcao da pasta: pack auxiliar de decisao PMO infra, runway DigitalOcean e prototipos n8n.
- Documentos principais: nenhum canonico.
- Documentos auxiliares: `00_README_INDEX.md`, `00_DigitalOcean_PMO/*`, `01_Financas_ROI/*`, `02_N8N_Automations/*`, `03_Policies/*`, `04_Codex_Instructions/*`.
- Documentos historicos/supersedidos: nenhum confirmado; todos permanecem auxiliares.
- Ultimos arquivos adicionados: pack importado em 2026-05-26 com MD e JSONs n8n.
- Dependencias: docs 10, 11, 12, 13, 21 e 24 antes de qualquer uso real.
- Riscos de confusao: transformar n8n em core ou usar JSONs para billing/credits sem security, audit e approvals.
- Proximos passos recomendados: catalogar fluxos como prototipos com owner, risco, custo e criterio de migracao.
- O que NAO fazer nesta pasta: nao rodar automacoes, nao tratar DigitalOcean/n8n como arquitetura definitiva, nao criar infra.

### `000_UPGRADE/pack_notas_ckos_deep_research/`

- Nome da pasta: `pack_notas_ckos_deep_research`.
- Funcao da pasta: banco auxiliar de hipoteses, prompts e temas de pesquisa.
- Documentos principais: nenhum canonico.
- Documentos auxiliares: `README.md`, `INDEX.md`, notas 01-20.
- Documentos historicos/supersedidos: instrucoes internas que pedem React/backend/modelo de dados devem ser filtradas nesta fase.
- Ultimos arquivos adicionados: pack importado em 2026-05-26.
- Dependencias: `CKOS_RESEARCH_MEMORY.md`, docs 00-25 e decisao futura sobre docs 26-34.
- Riscos de confusao: transformar pesquisa em implementacao ou confundir CKOS com Branddock/app de tarefas.
- Proximos passos recomendados: consolidar perguntas de pesquisa P0/P1/P2 sem criar artefatos runtime.
- O que NAO fazer nesta pasta: nao gerar React, backend, migrations, APIs, UX final ou novos docs canonicos sem aprovacao.

## Filetree resumido

```txt
CKOS_DOCUMENTATION_REVIEWED/
|-- ARCHITECTURE_PATCH_REPORT.md
|-- QA_DOCUMENTATION_CHECKLIST.md
|-- CKOS_FOLDER_MEMORY.md
|-- CKOS_FILETREE_MAP.md
|-- CKOS_VAULT_MAP_REFRESH_REPORT.md
|-- Memória GPT.md
|-- 000_ROADMAPS/
|-- 000_UPLOADS/
|-- 000_STUDY_NOTES/
|-- 000_UPGRADE/
|   |-- CKOS_CODEX_MEMORY.md
|   |-- CKOS_INFRA_AUTOMATION_MEMORY.md
|   |-- CKOS_RESEARCH_MEMORY.md
|   |-- CKOS_UPGRADE_INDEX.md
|   |-- CKOS_CONTINUATION_PLAN.md
|   |-- CKOS_CREATOR_MODE_PACK/
|   |-- CKOS_CODEX_CONTINUATION_PACK/
|   |-- ckos_digitalocean_n8n_pack/
|   `-- pack_notas_ckos_deep_research/
|-- 00_SYSTEM_GOVERNANCE/
|-- 01_THINKING_SYSTEM/
|-- 02_EXECUTION_SYSTEM/
|-- 03_RUNTIME_SYSTEM/
|-- 04_PRODUCT_SYSTEM/
|-- 05_IMPLEMENTATION_SYSTEM/
`-- 06_BUSINESS_SYSTEMS/
```

## Raiz

### Proposito

Guardar relatorios, checklists, memoria operacional e arquivos de controle do vault inteiro.

### Arquivos canonicos

- `ARCHITECTURE_PATCH_REPORT.md`: relatorio mestre de patches, versionado em `1.7.0`; registra docs 21-24 e Gate I completo no header e nas secoes 21-24.
- `QA_DOCUMENTATION_CHECKLIST.md`: checklist de QA documental; ainda focado no Runtime Gate, deve ser expandido futuramente para Product, Implementation e Business Systems.

### Arquivos auxiliares

- `Memória GPT.md`: memoria avulsa/contextual; modificada recentemente e pendente de classificacao.
- `CKOS_FILETREE_MAP.md`: mapa completo do filetree e classificacao de arquivos.

### Arquivos recentes

- `CKOS_FOLDER_MEMORY.md`: memoria operacional da pasta.
- `CKOS_FILETREE_MAP.md`: mapa completo criado no refresh 2026-05-26.
- `CKOS_VAULT_MAP_REFRESH_REPORT.md`: relatorio de refresh do mapa do vault.

### Status

Raiz operacionalmente consistente, mas precisa separar com clareza relatorios canonicos, memorias auxiliares e notas historicas.

### Dependencias

- Todos os agentes devem ler `ARCHITECTURE_PATCH_REPORT.md`, `QA_DOCUMENTATION_CHECKLIST.md`, esta memoria, `CKOS_FILETREE_MAP.md` e `CKOS_VAULT_MAP_REFRESH_REPORT.md` antes de alterar docs.

### Riscos

- `ARCHITECTURE_PATCH_REPORT.md` contem trechos historicos antigos que dizem que docs 21-24 ainda faltavam; o header v1.7.0 e as secoes 21-24 representam o estado atual.
- `Memória GPT.md` pode conter memoria util, mas nao tem status canonico claro.

### Proximos passos

- Registrar em patch futuro que `CKOS_VAULT_MAP_REFRESH_REPORT.md` e memoria auxiliar.
- Classificar `Memória GPT.md` como historica, auxiliar ou pendente.

## 00_SYSTEM_GOVERNANCE

### Proposito

Definir autoridade documental, template, taxonomia, naming, mapa mestre e dependencias.

### Arquivos canonicos

- `00_README_SYSTEM_GOVERNANCE.md`
- `00_MASTER_MAP.md`
- `00_DOCUMENT_TEMPLATE.md`
- `00_TAXONOMY_AND_NAMING.md`
- `00_DEPENDENCY_MAP.md`

### Arquivos auxiliares

- Nenhum arquivo auxiliar identificado nesta pasta.

### Arquivos recentes

- Nenhum arquivo novo detectado nesta rodada. Arquivos de governanca foram modificados em 24-25/05/2026.

### Status

Canonica. Deve continuar sendo fonte para naming, dependencia e formato de novos docs.

### Dependencias

- Todos os docs 10-24 dependem da taxonomia, template e dependency map.
- Docs 26-34 nao devem ser criados antes de decisao taxonomica especifica.

### Riscos

- `00_MASTER_MAP.md` e `00_DEPENDENCY_MAP.md` podem estar atrasados em relacao as memorias de upgrade e ao estado docs 21-24.

### Proximos passos

- Fazer patch controlado no Master Map/Dependency Map somente apos aprovacao do Founder.

## 01_THINKING_SYSTEM

### Proposito

Definir a constituicao AI-first, o modelo de objetos, agentes, autonomia, approvals, memoria e contexto.

### Arquivos canonicos

- `00_README_THINKING_SYSTEM.md`
- `01_CKOS_AI_FIRST_CONSTITUTION.md`
- `02_AI_FIRST_OBJECT_MODEL.md`
- `03_AGENT_OPERATING_MODEL.md`
- `04_AUTONOMY_AND_APPROVALS.md`
- `05_MEMORY_AND_CONTEXT_ARCHITECTURE.md`

### Arquivos auxiliares

- Nenhum arquivo auxiliar identificado nesta pasta.

### Arquivos recentes

- Nenhum arquivo novo detectado nesta rodada.

### Status

Canonica e estavel.

### Dependencias

- Base conceitual para Runtime, Product, Implementation, Business Systems e docs futuros 25-30.

### Riscos

- Prompts externos podem reduzir o CKOS a chat/dashboard se nao forem validados contra esta camada.

### Proximos passos

- Usar como filtro obrigatorio para qualquer doc futuro de Learning, Self-Evolving, Planner ou UI/UX.

## 02_EXECUTION_SYSTEM

### Proposito

Definir skills, workflows, prompts, transformers e pipelines que antecedem execucao real.

### Arquivos canonicos

- `00_README_EXECUTION_SYSTEM.md`
- `06_SKILLS_REGISTRY.md`
- `07_WORKFLOW_BLUEPRINTS.md`
- `08_PROMPT_LIBRARY.md`
- `09_TRANSFORMERS_AND_PIPELINES.md`

### Arquivos auxiliares

- Nenhum arquivo auxiliar identificado nesta pasta.

### Arquivos recentes

- Nenhum arquivo novo detectado nesta rodada.

### Status

Canonica e estavel.

### Dependencias

- Docs 25-29 devem referenciar skills/workflows/prompts/transformers existentes, sem criar runtime paralelo.

### Riscos

- Skills de `000_UPGRADE/CKOS_CODEX_CONTINUATION_PACK/02_SKILLS` sao auxiliares e nao devem substituir este registry.

### Proximos passos

- Quando docs 25-29 forem aprovados, avaliar se geram patches no Skills Registry.

## 03_RUNTIME_SYSTEM

### Proposito

Definir o kernel operacional: runtime, data model, security, policies, evals, observability, cost control e projections.

### Arquivos canonicos

- `00_README_RUNTIME_SYSTEM.md`
- `10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `11_DATA_MODEL_AND_PERSISTENCE.md`
- `12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`
- `13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`

### Arquivos auxiliares

- Nenhum arquivo auxiliar identificado nesta pasta.

### Arquivos recentes

- Nenhum arquivo novo detectado nesta rodada.

### Status

Canonica. Implementacao segue bloqueada.

### Dependencias

- Business Systems 21-24 geraram patches sugeridos para docs 10 e 11, ainda nao aplicados.
- Docs 26-34 dependem de runtime, data, security, evals, cost guard e doc 25.

### Riscos

- n8n, collectors ou prompts de pesquisa virarem runtime paralelo.
- Frontend chamar provider, token ou actor_id diretamente.

### Proximos passos

- Antes de implementar qualquer Business System, avaliar patches P21-1 a P24-6 no doc 11 v1.3.x e componentes runtime no doc 10.

## 04_PRODUCT_SYSTEM

### Proposito

Definir Project Dashboard, Command Center e Node Canvas como projections do runtime, nao como fontes de verdade.

### Arquivos canonicos

- `00_README_PRODUCT_SYSTEM.md`
- `14_PROJECT_DASHBOARD_ARCHITECTURE.md`
- `15_COMMAND_CENTER_ARCHITECTURE.md`
- `16_NODE_CANVAS_ARCHITECTURE.md`

### Arquivos auxiliares

- Nenhum arquivo auxiliar identificado nesta pasta.

### Arquivos recentes

- Nenhum arquivo novo detectado nesta rodada.

### Status

Canonica. UI/UX final ainda bloqueado.

### Dependencias

- Depende dos docs 10-13.
- Docs 21-24 alimentam projections de ROI, feedback, support e billing.

### Riscos

- CommandBar ser tratada como envio direto para agente.
- Dashboards fixos por ecommerce/campanha/social sem node ativo.

### Proximos passos

- Usar docs 14-16 como restricao para qualquer estudo visual futuro.

## 05_IMPLEMENTATION_SYSTEM

### Proposito

Definir protocolo de implementacao, pesquisa, execucao multiagente, QA, Founder approval e limites de autonomia.

### Arquivos canonicos

- `00_README_IMPLEMENTATION_SYSTEM.md`
- `17_IMPLEMENTATION_PROTOCOL.md`
- `18_RESEARCH_PROTOCOL.md`
- `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`
- `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`

### Arquivos auxiliares

- `18_RESEARCH_PROTOCOL_FOR_MANUS.md`: variante historica/legada; pendente de classificacao como superseded.
- `19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md`: protocolo anterior; pendente de classificacao como superseded pelo protocolo com Antigravity.
- `21_SELF_EVOLVING_SYSTEM.md`: historico/superseded; fonte ativa movida conceitualmente para `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` sem rename fisico.

### Arquivos recentes

- `17_IMPLEMENTATION_PROTOCOL.md`, `18_RESEARCH_PROTOCOL.md`, `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md` e `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md` foram modificados em 25/05/2026.

### Status

Canonica com historico preservado. Nao renomear, mover ou deletar o antigo Self-Evolving.

### Dependencias

- Gate de implementacao depende de QA e approvals.
- Self-Evolving ativo depende de `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`.

### Riscos

- Referencias antigas podem apontar para `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`; tratar como historico/superseded.
- Manus ser interpretado como infraestrutura CKOS.

### Proximos passos

- Proximo passo: Claude auditar o Doc 26 Connectors/MCP.
- Manter ROI como doc 21 e Self-Evolving como doc 25.

## 06_BUSINESS_SYSTEMS

### Proposito

Definir os sistemas de negocio que governam ROI, feedback, suporte, creditos, planos e billing.

### Arquivos canonicos

- `21_ROI_ARCHITECTURE.md`
- `22_FEEDBACK_SYSTEM_ARCHITECTURE.md`
- `23_SUPPORT_SYSTEM_ARCHITECTURE.md`
- `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`

### Arquivos auxiliares

- Nenhum arquivo auxiliar identificado nesta pasta.

### Arquivos recentes

- `21_ROI_ARCHITECTURE.md`: criado/modificado em 25/05/2026 19:29.
- `22_FEEDBACK_SYSTEM_ARCHITECTURE.md`: criado/modificado em 25/05/2026 21:49.
- `23_SUPPORT_SYSTEM_ARCHITECTURE.md`: criado/modificado em 25/05/2026 22:01.
- `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`: criado/modificado em 25/05/2026 22:09.

### Status

Documentalmente concluidos, aguardando aprovacao formal Founder + Technical + Metacognik. Implementacao bloqueada.

### Dependencias

- Dependem dos docs 10-13, 14-16 e 17-20.
- Geram patches sugeridos P21-1 a P24-6 para runtime/data model.

### Riscos

- Agentes antigos tratarem 22-24 como faltantes.
- Confundir Gate I documentalmente completo com liberacao de implementacao.

### Proximos passos

- Submeter Gate I para aprovacao formal.
- Avaliar patches P21-1 a P24-6 antes de qualquer implementacao.

## 000_ROADMAPS

### Proposito

Controlar roadmaps vivos, tarefas, riscos, ROI operacional, feedback e handoffs entre sessoes sem autoridade canonica.

### Arquivos principais

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

### Status

Auxiliar governada, estabilizada em P0, roteada em P1.6 e expandida em P1.7 com politica multi-sessao em 2026-05-28. Nao e canonica e nao autoriza implementacao.

### Riscos

- Roadmap ser tratado como documento canonico.
- Antigravity/UI-UX iniciar antes de study layer.
- Sessoes paralelas editarem sem checkout lock.
- Agente gastar contexto lendo o vault inteiro.
- Roadmaps antigos e novos competirem sem leitura de `ROADMAP_ROUTING_MATRIX.md`.
- Sessao futura omitir registry, estimated_cost ou intelligence_level.

### Proximos passos

- Auditar P1.7 em PMO/Metacognik.
- Ativar Antigravity somente em sessao futura `design_study` se Founder aprovar o gate formal.
- Alternativamente abrir P2 para expansao das lanes antes do estudo visual.

## 000_UPLOADS

### Proposito

Camada RAW de entrada bruta. Recebe material importado sem autoridade canonica.

### Arquivos principais

- `README.md`
- `_folder_memory.md`
- `00_UPLOADS_INDEX.md`

### Status

Auxiliar ativa, criada em 2026-05-27 apos aprovacao Founder.

### Riscos

- Tratar upload como verdade.
- Promover output de IA direto para canonico.
- Guardar PII, tokens ou secrets sem controle.

### Proximos passos

- Usar apenas para novas entradas brutas.
- Converter material relevante em source manifest ou study note em `000_STUDY_NOTES/`.

## 000_STUDY_NOTES

### Proposito

Camada STUDY de interpretacao e preparo de patch candidates. Nao e canonica.

### Arquivos principais

- `README.md`
- `_folder_memory.md`
- `00_STUDY_INDEX.md`
- `_templates/*`
- `11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md`
- `12_SESSION_GATES/README.md`
- `12_SESSION_GATES/ck_memory.md`
- `12_SESSION_GATES/_folder_memory.md`
- `12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md`
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

### Status

Auxiliar ativa, criada em 2026-05-27 apos aprovacao Founder.

### Riscos

- Tratar study note como canonica.
- Usar `09_APPROVED_FOR_CANONICAL_PATCH/` como autorizacao de aplicacao direta.
- Tratar padrao operacional estudado como autorizacao para implementar UI, agentes ou runtime.
- Tratar gate de sessao criado como autorizacao para iniciar Antigravity.

### Proximos passos

- Usar templates YAML para toda nota nova.
- Usar `11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md` como referencia auxiliar para perguntas inteligentes e planejamento.
- Usar `12_SESSION_GATES/01_ANTIGRAVITY_STUDY_MODE_GATE.md` somente como gate pendente de ativacao Founder.
- Usar `12_SESSION_GATES/ck_memory.md` como memoria ativa; `_folder_memory.md` e apenas legado preservado.
- Usar `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/` como estudo auxiliar para Doc 27, sem canonizar automaticamente seus candidatos.
- Submeter qualquer patch candidate a patch plan, QA e aprovacao Founder.

## 000_UPGRADE

### Proposito

Area auxiliar de continuidade, packs de pesquisa, automacao, infra e memoria operacional. Nao e camada canonica.

### Arquivos canonicos

- Nenhum. Esta pasta e auxiliar.

### Arquivos auxiliares

- `Bem-vindo.md`
- `CKOS_CODEX_CONTINUATION_PACK/`
- `ckos_digitalocean_n8n_pack/`
- `pack_notas_ckos_deep_research/`
- `CKOS_CODEX_MEMORY.md`
- `CKOS_INFRA_AUTOMATION_MEMORY.md`
- `CKOS_RESEARCH_MEMORY.md`
- `CKOS_UPGRADE_INDEX.md`
- `CKOS_CONTINUATION_PLAN.md`

### Arquivos recentes

- Memorias criadas em 26/05/2026 03:18: `CKOS_CODEX_MEMORY.md`, `CKOS_INFRA_AUTOMATION_MEMORY.md`, `CKOS_RESEARCH_MEMORY.md`, `CKOS_UPGRADE_INDEX.md`, `CKOS_CONTINUATION_PLAN.md`.
- `CKOS_CODEX_CONTINUATION_PACK`: importado/copiadado em 26/05/2026, com LastWriteTime interno anterior.
- `pack_notas_ckos_deep_research`: importado/copiadado em 26/05/2026.
- `ckos_digitalocean_n8n_pack`: importado/copiadado em 26/05/2026.

### Status

Auxiliar. Contem material util, mas parte dele esta desatualizada em relacao ao vault real.

### Dependencias

- Deve ser lido contra `ARCHITECTURE_PATCH_REPORT.md`, `QA_DOCUMENTATION_CHECKLIST.md`, docs canonicos 00-24 e esta memoria.

### Riscos

- Packs antigos dizem que docs 22-24 faltavam.
- Deep research pack recomenda gerar React/backend em alguns prompts; isso esta bloqueado nesta fase.
- n8n pack pode ser mal interpretado como runtime definitivo.

### Proximos passos

- Usar `CKOS_UPGRADE_INDEX.md` como filtro de absorvido/auxiliar/desatualizado.
- Nao promover notas 25-29 do pack para o vault canonico sem decisao taxonomica.
