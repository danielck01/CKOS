---
title: CKOS Upgrade Index
system_id: ckos_upgrade_index
category: upgrade_index
status: draft
version: 1.5.0
updated_at: 2026-05-27
owner: ceo_agent
reviewers:
  - founder
  - pmo_ckos
  - metacognik
related_notes:
  - ../CKOS_FOLDER_MEMORY.md
  - ../CKOS_FILETREE_MAP.md
  - ../CKOS_VAULT_MAP_REFRESH_REPORT.md
  - CKOS_CODEX_MEMORY.md
  - CKOS_INFRA_AUTOMATION_MEMORY.md
  - CKOS_RESEARCH_MEMORY.md
  - CKOS_CONTINUATION_PLAN.md
  - CKOS_CREATOR_MODE_PACK/00_README_START_HERE.md
  - ../000_UPLOADS/00_UPLOADS_INDEX.md
  - ../000_STUDY_NOTES/00_STUDY_INDEX.md
created_for: CKOS_DOCUMENTATION_REVIEWED
---

# CKOS Upgrade Index

## Proposito

Este indice organiza `000_UPGRADE` como area auxiliar de continuidade, pesquisa, infra temporaria, automacao e memoria operacional. Ele nao substitui o vault canonico e nao deve guiar a sequencia documental quando divergir de `ARCHITECTURE_PATCH_REPORT.md` v1.7.0, `CKOS_FOLDER_MEMORY.md` ou `CKOS_VAULT_MAP_REFRESH_REPORT.md`.

## Estado real apos refresh

- Docs 21-24 existem em `06_BUSINESS_SYSTEMS`.
- Gate I esta documentalmente completo no `ARCHITECTURE_PATCH_REPORT.md` v1.7.0.
- Docs 21-24 aguardam aprovacao formal Founder + Technical + Metacognik.
- Implementacao continua bloqueada.
- Docs 25-30 nao devem ser criados ainda.
- UI/UX continua bloqueado ate sequencia documental aprovada.
- `../CKOS_FILETREE_MAP.md` registra a filetree completa, os arquivos novos e os conflitos de numeracao.
- Nenhum arquivo deve ser movido, deletado, renomeado ou renumerado sem relatorio previo e aprovacao Founder.
- n8n nao deve ser tratado como core CKOS.
- Manus nao deve ser tratado como infraestrutura definitiva do CKOS.
- `CKOS_CREATOR_MODE_PACK/` foi criado como pack auxiliar para simular Creator Mode no Codex.
- `CKOS_CREATOR_MODE_PACK/07_SIMULATION_RUNTIME/` foi criado como camada auxiliar para simular backend, API, conectores, policies, creditos e event log sem runtime real.
- `../000_UPLOADS/` foi criado como camada RAW aprovada no microgate `UPLOADS_STUDY_MICROGATE_PROPOSAL`.
- `../000_STUDY_NOTES/` foi criado como camada STUDY aprovada no mesmo microgate.
- Nada entra no canonico sem passar por STUDY, patch plan, QA e aprovacao humana.

## Microgate RAW/STUDY 2026-05-27

Arquivos estruturais criados fora de `000_UPGRADE`:

- `../000_UPLOADS/README.md`
- `../000_UPLOADS/_folder_memory.md`
- `../000_UPLOADS/00_UPLOADS_INDEX.md`
- `../000_STUDY_NOTES/README.md`
- `../000_STUDY_NOTES/_folder_memory.md`
- `../000_STUDY_NOTES/00_STUDY_INDEX.md`
- `../000_STUDY_NOTES/_templates/RAW_UPLOAD_NOTE_TEMPLATE.md`
- `../000_STUDY_NOTES/_templates/STUDY_NOTE_TEMPLATE.md`
- `../000_STUDY_NOTES/_templates/SOURCE_MANIFEST_TEMPLATE.md`
- `../000_STUDY_NOTES/_templates/PATCH_CANDIDATE_TEMPLATE.md`
- `../000_STUDY_NOTES/_templates/DECISION_LOG_TEMPLATE.md`

Status: estruturas auxiliares ativas. Nao sao documentacao canonica.

Travas:

- Nao mover arquivos antigos para essas pastas sem patch plan.
- Nao promover upload direto para canonico.
- Nao tratar study note como canonica.
- Nao atualizar docs 01-24 sem patch documental separado.

## O que veio de pack

### `CKOS_CODEX_CONTINUATION_PACK/`

Origem: pack de continuidade para Codex/Claude/Antigravity.

Conteudo:

- contexto atual do CKOS;
- filetree esperado;
- prompts para Codex, Antigravity e Visual Director;
- skills conceituais;
- notas futuras 25-29;
- estudo visual/HTML futuro;
- roadmap 21-30.

Status: referencia auxiliar. Parcialmente desatualizado.

Parte desatualizada:

- `00_README_START_HERE.md` e `06_ROADMAP/DOCS_21_TO_30_SEQUENCE.md` tratam 22-24 como pendentes/proximos.
- `06_ROADMAP/DEVELOPMENT_PLAN_WITHOUT_UI.md` ainda sugere concluir 22-24 como prioridade imediata.

Parte ainda util:

- regra de nao implementar UI/backend/migrations;
- tese CKOS como AI-first OS;
- prompts de revisao paralela sem implementacao;
- notas 25-29 como insumo auxiliar, nao como docs canonicos.

### `ckos_digitalocean_n8n_pack/`

Origem: pack PMO de infra temporaria, DigitalOcean e n8n.

Conteudo:

- decisao PMO para DigitalOcean;
- runway, ROI infra, planner de custos e custo por agente;
- automacoes n8n em Markdown/JSON;
- policies de budget gates e migracao de n8n para codigo proprio;
- contexto mestre para Codex.

Status: referencia auxiliar de infra/prototipo.

Parte absorvida como principio:

- n8n e acelerador, nao core;
- credito inicial e runway estrategico, nao caixa livre;
- fluxos criticos devem migrar para codigo proprio.

Parte que nao deve guiar a sequencia canonica:

- JSONs de n8n nao sao runtime;
- workflows n8n nao substituem event bus, policy engine, model router, collector runner ou orchestration propria;
- automacoes de billing/creditos/pagamentos nao podem virar core sem security, audit, tests e approvals.

### `pack_notas_ckos_deep_research/`

Origem: pack de prompts e temas de deep research.

Conteudo:

- AI-first OS;
- CKOS vs Branddock;
- VPS/local infra;
- Project Pulse;
- Briefing Inteligente;
- Proposal Engine;
- Agent Journey;
- HITL;
- models/costs;
- billing;
- knowledge base;
- decisions/issues/sprints;
- suporte;
- seguranca;
- marketplace;
- linguagem comercial.

Status: banco de hipoteses e pesquisa, nao source-of-truth.

Parte util:

- mapa de temas P0/P1/P2;
- prompts para aprofundar arquitetura;
- sinais de pesquisa para agentes futuros.

Parte bloqueada nesta fase:

- qualquer instrucao para gerar componentes React, backend, migrations ou plano de implementacao.

### `CKOS_CREATOR_MODE_PACK/`

Origem: aprovacao Founder em 2026-05-26 para criar uma camada auxiliar de Creator Mode no Codex.

Conteudo:

- protocolos de CEO Agent Planner;
- criacao de projeto a partir de intencao minima;
- politica simulada de creditos CKOS;
- protocolo de checkout lock/release;
- templates de analise, filetree, plano, PMO audit e Founder approval;
- skills simuladas de intent-to-project, context pack, PMO audit e credit estimation;
- taxonomia de categoria/subcategoria de projeto;
- exemplo Miriam em modo planning only;
- handoffs CEO -> PMO -> Founder.
- estado atual do CKOS em `CKOS_CURRENT_STATE_SUMMARY.md`;
- simulation runtime layer para contratos falsos, endpoints simulados, registry de conectores, mock schemas, event log, policy matrix e demo runbook.

Status: referencia auxiliar operacional. Nao e canonico. Nao cria docs 25-30.

Parte util:

- padroniza novos chats de CEO Agent, PMO Auditor e Project Creator;
- impede gerar pack de notas antes da filetree aprovada;
- introduz custo simulado em creditos antes de execucao;
- separa chat decide, documento registra, artifact entrega, PMO audita e Founder aprova.
- permite testar projetos como se houvesse backend/API/conectores, mantendo `simulation_only: true`.

Parte bloqueada:

- nao autoriza UI, backend, migrations, agentes reais, APIs ou automacoes runtime;
- nao autoriza estrategia final de cliente sem briefing, fontes e aprovacao;
- nao altera docs canonicos.
- nao executa conectores reais, OAuth, n8n, APIs externas ou reservas reais de credito.

## O que ja foi absorvido

- A tese de CKOS como AI-first Operating System foi absorvida na memoria operacional.
- A regra anti-UI/anti-implementacao foi reafirmada.
- O estado desatualizado dos docs 22-24 foi identificado.
- A decisao "n8n como acelerador, nao core" foi registrada.
- A necessidade de microgate para `21_SELF_EVOLVING_SYSTEM.md` foi registrada.
- O Creator Mode foi estruturado como pack auxiliar em `CKOS_CREATOR_MODE_PACK/`.
- A Simulation Runtime Layer foi estruturada em `CKOS_CREATOR_MODE_PACK/07_SIMULATION_RUNTIME/`.

## O que continua referencia auxiliar

- Prompts de Codex/Claude/Antigravity.
- Skills conceituais do continuation pack.
- Notas 25-29 do continuation pack.
- Estudos visuais e Pinterest keywords.
- Deep research prompts.
- DigitalOcean/n8n pack para planejamento de infra futura.
- Creator Mode Pack para novos projetos simulados no Codex.
- Simulation Runtime Layer para testar fluxo intent-to-artifact com backend/API/conectores simulados.

## O que nao deve guiar a sequencia canonica

- Roadmaps que dizem que 22-24 ainda faltam.
- Prompts que pedem implementacao.
- JSONs de n8n.
- Estudos visuais como se fossem doc 30.
- Qualquer referencia a Manus como infraestrutura do CKOS.
- Qualquer instrucao para mover ou renumerar arquivos sem patch plan aprovado.

## Memorias operacionais em `000_UPGRADE`

- `CKOS_CODEX_MEMORY.md`: resumo e riscos do continuation pack.
- `CKOS_INFRA_AUTOMATION_MEMORY.md`: decisao infra/n8n, riscos e criterios de migracao.
- `CKOS_RESEARCH_MEMORY.md`: mapa de pesquisas, fontes e prioridades.
- `CKOS_UPGRADE_INDEX.md`: este indice.
- `CKOS_CONTINUATION_PLAN.md`: plano de continuidade atualizado.
- `../CKOS_FILETREE_MAP.md`: mapa completo do vault, incluindo novos arquivos, auxiliares, historicos e conflitos.
- `CKOS_CREATOR_MODE_PACK/`: protocolos e templates auxiliares para criacao de projetos por intencao minima.
- `CKOS_CREATOR_MODE_PACK/07_SIMULATION_RUNTIME/`: contratos e runbooks auxiliares para simulacao de backend/API/conectores sem implementacao.

## Ordem recomendada para agentes

1. `../ARCHITECTURE_PATCH_REPORT.md`
2. `../CKOS_FILETREE_MAP.md`
3. `../CKOS_VAULT_MAP_REFRESH_REPORT.md`
4. `../CKOS_FOLDER_MEMORY.md`
5. `../000_UPLOADS/00_UPLOADS_INDEX.md`
6. `../000_STUDY_NOTES/00_STUDY_INDEX.md`
7. `CKOS_UPGRADE_INDEX.md`
8. `CKOS_CONTINUATION_PLAN.md`
9. Pack especifico apenas se a tarefa exigir.

## Regras de promocao para o vault canonico

- Nenhum arquivo de pack vira canonico automaticamente.
- Nenhum upload vira canonico automaticamente.
- Nenhuma study note vira canonica automaticamente.
- Qualquer promocao exige patch plan e aprovacao Founder.
- Docs 25-30 exigem decisao de taxonomia antes de criacao.
- `21_SELF_EVOLVING_SYSTEM.md` nao deve ser renumerado sem aprovacao.
