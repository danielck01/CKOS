---
title: Self-Evolving Conflict Resolution Decision Study
file: 20260527_decision_self-evolving-conflict-resolution_pmo_ckos_draft.md
system_id: decision_self_evolving_conflict_resolution
display_name: Self-Evolving Conflict Resolution Decision Study
doc_type: decision_log
category: governance
layer: study
status: draft
version: 0.1.0
created_at: 2026-05-27
updated_at: 2026-05-27
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - metacognik
  - technical
approval_required:
  - founder
source_type: vault_reference_scan
source_path: 05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md
source_tool: codex
provenance_status: verified
project: ckos
related_docs:
  - 05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md
  - 06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md
  - 00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md
  - 00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md
  - ARCHITECTURE_PATCH_REPORT.md
related_notes: []
tags:
  - self_evolving
  - numbering_conflict
  - decision_log
  - patch_plan
risk_level: high
confidence: high
---

# Self-Evolving Conflict Resolution — Decision Study

## 1. Contexto

O vault CKOS reconhece oficialmente tres camadas documentais:

```txt
RAW -> STUDY -> CANONICAL
```

Docs 01-24 estao canonicos. Business Systems 21-24 existem em `06_BUSINESS_SYSTEMS/` e Gate I esta documentalmente completo. O proximo bloco planejado e docs 25-34, mas existe conflito previo:

- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`
- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`

Este estudo nao renomeia, move, deleta, cria doc 25 ou altera doc canonico. Ele registra evidencia e recomenda uma rota segura.

## 2. Problema

O numero 21 agora pertence oficialmente ao ROI Architecture em Business Systems. O Self-Evolving antigo tambem usa o numero 21 e ainda e referenciado por Runtime, Thinking, Implementation, mapas e reports.

Sem resolver isso antes do doc 25, agentes e humanos podem confundir:

- doc 21 como ROI;
- doc 21 como Self-Evolving;
- doc 25 como Self-Evolving;
- doc 25 como outro sistema futuro mencionado de forma vaga.

## 3. Referências encontradas no vault

Busca executada em 2026-05-27 com `rg`, excluindo `.obsidian/`.

### 3.1 Totais

| Grupo de busca | Matches | Arquivos |
|---|---:|---:|
| Self-Evolving / `21_SELF_EVOLVING_SYSTEM` / doc 25 Self-Evolving | 155 | 28 |
| ROI / `21_ROI_ARCHITECTURE` / docs 21 / doc 21 | 144 | 36 |

### 3.2 Arquivos que referenciam Self-Evolving

Arquivos canonicos ou de governanca com impacto direto:

- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md`
- `00_SYSTEM_GOVERNANCE/00_README_SYSTEM_GOVERNANCE.md`
- `01_THINKING_SYSTEM/01_CKOS_AI_FIRST_CONSTITUTION.md`
- `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md`
- `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md`
- `03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`
- `03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`
- `04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md`
- `05_IMPLEMENTATION_SYSTEM/00_README_IMPLEMENTATION_SYSTEM.md`
- `05_IMPLEMENTATION_SYSTEM/17_IMPLEMENTATION_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md`
- `05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`
- `ARCHITECTURE_PATCH_REPORT.md`

Arquivos auxiliares com referencias relevantes:

- `CKOS_FILETREE_MAP.md`
- `CKOS_FOLDER_MEMORY.md`
- `CKOS_VAULT_MAP_REFRESH_REPORT.md`
- `000_UPGRADE/CKOS_CODEX_MEMORY.md`
- `000_UPGRADE/CKOS_CONTINUATION_PLAN.md`
- `000_UPGRADE/CKOS_UPGRADE_INDEX.md`
- `000_UPGRADE/CKOS_CREATOR_MODE_PACK/CKOS_CURRENT_STATE_SUMMARY.md`
- `000_UPGRADE/CKOS_CREATOR_MODE_PACK/01_PROTOCOLS/CEO_AGENT_PLANNER_PROTOCOL.md`
- `000_UPGRADE/UPLOADS_STUDY_MICROGATE_PROPOSAL/*`

### 3.3 Arquivos que referenciam doc 21 como ROI

Arquivos canonicos ou de governanca com ROI/doc 21:

- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`
- `05_IMPLEMENTATION_SYSTEM/17_IMPLEMENTATION_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`
- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`
- `06_BUSINESS_SYSTEMS/22_FEEDBACK_SYSTEM_ARCHITECTURE.md`
- `06_BUSINESS_SYSTEMS/23_SUPPORT_SYSTEM_ARCHITECTURE.md`
- `06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`
- `ARCHITECTURE_PATCH_REPORT.md`

Arquivos auxiliares importantes:

- `CKOS_FILETREE_MAP.md`
- `CKOS_FOLDER_MEMORY.md`
- `CKOS_VAULT_MAP_REFRESH_REPORT.md`
- `000_UPGRADE/CKOS_CODEX_MEMORY.md`
- `000_UPGRADE/CKOS_CONTINUATION_PLAN.md`
- `000_UPGRADE/CKOS_UPGRADE_INDEX.md`
- packs em `000_UPGRADE/`
- memories locais de `000_UPLOADS/` e `000_STUDY_NOTES/`

### 3.4 Arquivos que podem quebrar se Self-Evolving for renumerado

Quebra provavel por referencia direta ao nome antigo, wikilink antigo ou "Self-Evolving (21)":

- `01_THINKING_SYSTEM/01_CKOS_AI_FIRST_CONSTITUTION.md`
- `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md`
- `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md`
- `03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`
- `03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`
- `05_IMPLEMENTATION_SYSTEM/00_README_IMPLEMENTATION_SYSTEM.md`
- `05_IMPLEMENTATION_SYSTEM/17_IMPLEMENTATION_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md`
- `05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`
- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md`
- `ARCHITECTURE_PATCH_REPORT.md`

### 3.5 Arquivos que ja consideram 25 como proximo doc

- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md`
- `05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`
- `ARCHITECTURE_PATCH_REPORT.md`
- `CKOS_FILETREE_MAP.md`
- `CKOS_FOLDER_MEMORY.md`
- `CKOS_VAULT_MAP_REFRESH_REPORT.md`
- `000_UPGRADE/CKOS_CONTINUATION_PLAN.md`
- `000_UPGRADE/CKOS_CODEX_MEMORY.md`
- `000_UPGRADE/UPLOADS_STUDY_MICROGATE_PROPOSAL/DOCS_25_34_SEQUENCE_PROPOSAL.md`
- `000_UPGRADE/UPLOADS_STUDY_MICROGATE_PROPOSAL/SELF_EVOLVING_RENUMBERING_RISK_REPORT.md`

Observacao importante: `06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md` tambem menciona "doc 25" em contexto de whitelabel billing. Essa referencia precisa ser auditada no patch futuro para evitar novo conflito semantico.

### 3.6 Arquivos que ainda tratam Self-Evolving como doc 21

- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md`
- `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md`
- `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md`
- `03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`
- `03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`
- `05_IMPLEMENTATION_SYSTEM/17_IMPLEMENTATION_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md`
- `05_IMPLEMENTATION_SYSTEM/00_README_IMPLEMENTATION_SYSTEM.md`
- `ARCHITECTURE_PATCH_REPORT.md`

## 4. Diagnóstico do arquivo atual

Arquivo auditado: `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`.

### 4.1 O conteúdo ainda é válido?

Sim, como visão conceitual e guardrail. O documento acerta ao tratar self-evolution como capacidade futura, gateada, dependente de Runtime, Security, Evals, Sandbox, Rollback e Founder approval.

### 4.2 Está maduro para virar doc canônico 25?

Nao diretamente. Esta maduro como base, mas insuficiente como doc 25 canonico atual.

Motivos:

- YAML esta fora do padrao atual em `owner`, `responsible_agent`, `reviewers` e `approval_required`.
- Numero 21 conflita com ROI.
- Escopo ainda e Implementation-centric.
- Nao incorpora RAW/STUDY.
- Nao incorpora Business Systems 21-24 como sinais de aprendizado.
- Nao define objetos, eventos, tables, registries e eval hooks em nivel engineer-ready.

### 4.3 Precisa de reescrita estrutural?

Sim. Deve ser reescrito como arquitetura de Evolution System, nao apenas renumerado. A reescrita deve preservar a tese e endurecer runtime, policy, evals, data model, approval gates e rollback.

### 4.4 Está no lugar errado?

Sim, parcialmente. O Self-Evolving depende de Implementation, mas nao pertence apenas a Implementation. Ele cruza:

- learning loop;
- evals;
- agent performance;
- prompt performance;
- workflow performance;
- capability evolution;
- system improvement proposals;
- sandbox/simulation;
- rollback;
- Metacognik audit;
- Founder approval.

### 4.5 Pertence a Implementation System ou a nova camada futura?

Recomendacao PMO: pertence a nova camada futura `07_EVOLUTION_SYSTEM/`, com doc 25 como primeiro documento. Implementation continua sendo dependencia e gate operacional, mas nao deve conter a arquitetura evolutiva inteira.

### 4.6 Seções a preservar

- Aviso de maturidade.
- Mudanca do papel do Founder de prompt operator para approver/strategic operator.
- Escada de autonomia.
- Loop seguro.
- Sandbox.
- Guardrails duros.
- Metricas de sucesso.
- Criterios de aprovacao e reprovacao.

### 4.7 Seções desatualizadas

- YAML com display names em campos que agora exigem `system_id`.
- `phase: 05_IMPLEMENTATION_SYSTEM`.
- `file: 21_SELF_EVOLVING_SYSTEM.md`.
- Referencia ao "Manus proprio" como imagem central; deve virar "CKOS Evolution Layer" e tratar Manus apenas como ferramenta historica/temporaria.
- Related notes sem docs 21-24 Business Systems e sem RAW/STUDY.

### 4.8 Conflitos com docs 10-24

- Conflito numerico com `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`.
- Docs 10, 11, 12 e 13 ainda referenciam Self-Evolving como 21.
- Doc 17 usa Self-Evolving como Fase 12, mas tambem reconhece Business Systems 21-24.
- Doc 20 ja aponta "25 Self-Evolving System Architecture" como gate futuro, criando uma trilha nova que o arquivo antigo ainda nao segue.
- Business Systems 21-24 criaram novos sinais de aprendizado que o Self-Evolving atual nao incorpora: ROI outcomes, feedback signals, support friction, billing/credit usage.

### 4.9 Dependências que deve respeitar

- `04_AUTONOMY_AND_APPROVALS.md`
- `05_MEMORY_AND_CONTEXT_ARCHITECTURE.md`
- `10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `11_DATA_MODEL_AND_PERSISTENCE.md`
- `12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`
- `13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`
- `17_IMPLEMENTATION_PROTOCOL.md`
- `18_RESEARCH_PROTOCOL.md`
- `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`
- `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`
- `21_ROI_ARCHITECTURE.md`
- `22_FEEDBACK_SYSTEM_ARCHITECTURE.md`
- `23_SUPPORT_SYSTEM_ARCHITECTURE.md`
- `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`

Futuros docs relacionados:

- `26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md`
- `27_COLLECTOR_REGISTRY_AND_RESEARCH_ACTORS_ARCHITECTURE.md`
- `28_KNOWLEDGE_INGESTION_UPLOADS_AND_SOURCE_GOVERNANCE_ARCHITECTURE.md`
- `29_STUDY_NOTES_AND_LEARNING_MODE_ARCHITECTURE.md`
- `30_CLIENT_PROJECT_PLANNER_AND_SELF_DOCUMENTING_PROJECTS_ARCHITECTURE.md`
- `31_CK_STORE_AND_CAPABILITY_MARKETPLACE_ARCHITECTURE.md`
- `34_FINAL_IMPLEMENTATION_READINESS_GATE.md`

### 4.10 Documentos que o futuro doc 25 deve citar

No minimo:

- docs 03, 04, 05;
- docs 10, 11, 12, 13;
- docs 17, 18, 19, 20;
- docs 21, 22, 23, 24;
- `000_UPLOADS/00_UPLOADS_INDEX.md`;
- `000_STUDY_NOTES/00_STUDY_INDEX.md`;
- `ARCHITECTURE_PATCH_REPORT.md`.

## 5. Opções avaliadas

### A) Renumerar para `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`

Beneficio:

- Resolve a ambiguidade de doc 21.
- Cria uma casa taxonomica correta para evolucao, learning, safe self-modification e capability evolution.
- Mantem Implementation como dependencia, nao como container conceitual.
- Prepara docs 26-34 com sequencia limpa.

Risco:

- Exige nova pasta canonica.
- Exige patch em Master Map, Dependency Map, Patch Report, filetree/memories e related notes.
- Exige reescrita estrutural, nao simples rename.

Esforco: alto, mas controlado.

Impacto:

- `00_MASTER_MAP.md`: adicionar `07_EVOLUTION_SYSTEM/`.
- `00_DEPENDENCY_MAP.md`: reposicionar doc 25 e dependencias.
- `ARCHITECTURE_PATCH_REPORT.md`: registrar renumeracao/supersession.
- Related notes: atualizar refs antigas para novo caminho.
- Arquivo antigo: manter como superseded/historico ou redirect.

Recomendacao PMO: recomendada.

### B) Renumerar para `05_IMPLEMENTATION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`

Beneficio:

- Menor mudanca taxonomica.
- Mantem proximo de docs 17-20 e Gate J.
- Menos custo de atualizacao de Master Map.

Risco:

- Mantem uma capacidade evolutiva ampla dentro de Implementation.
- Pode reduzir Self-Evolving a protocolo de build, quando ele tambem governa learning, runtime, business signals e capability evolution.
- Enfraquece a separacao futura de docs 25-34.

Esforco: medio.

Impacto:

- Menos arquivo estrutural novo.
- Ainda exige atualizar referencias antigas e Patch Report.
- Ainda exige reescrita do doc.

Recomendacao PMO: aceitavel apenas se Founder rejeitar nova camada.

### C) Manter como auxiliar histórico em `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`

Beneficio:

- Zero risco imediato de link quebrado.
- Preserva historico.
- Evita mudanca taxonomica agora.

Risco:

- Mantem conflito de doc 21.
- Bloqueia doc 25.
- Confunde Runtime e agentes futuros.
- Mantem duas verdades numericas: ROI 21 e Self-Evolving 21.

Esforco: baixo agora, alto depois.

Impacto:

- Master Map e Dependency Map continuariam carregando excecao.
- Patch Report precisaria repetir alerta.
- Docs 25-34 continuariam travados.

Recomendacao PMO: nao recomendada como destino final.

### D) Absorver em docs futuros 25, 30, 31 e 34

Beneficio:

- Evita criar uma camada nova.
- Permite distribuir o conteudo onde ele tem impacto.
- Partes do Self-Evolving podem alimentar Planner, CK Store e Final Gate.

Risco:

- Fragmenta ownership.
- Perde a arquitetura central de evolucao segura.
- Pode transformar self-evolution em anexos soltos.
- Dificulta auditoria e approval.

Esforco: medio/alto.

Impacto:

- Doc 25 ainda precisaria existir ou o conceito ficaria sem dono.
- Docs 30, 31 e 34 teriam dependencias cruzadas mais pesadas.

Recomendacao PMO: usar como estrategia complementar, nao como substituto do doc 25.

## 6. Comparativo PMO

| Opcao | Beneficio | Risco | Esforco | Impacto na numeracao | Recomendacao |
|---|---|---|---|---|---|
| A | taxonomia limpa e futuro escalavel | alto se sem patch plan | alto | resolve 21 e abre 25 | recomendada |
| B | menor mudanca estrutural | escopo limitado demais | medio | resolve 21, mas prende em Implementation | segunda opcao |
| C | sem churn agora | conflito permanece | baixo agora, alto depois | nao resolve | rejeitar como final |
| D | distribui conteudo | fragmenta ownership | medio/alto | incerto | complementar |

## 7. Recomendação

Recomendacao PMO: aprovar a Opcao A.

Destino futuro recomendado:

```txt
07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md
```

Condicoes:

- nao executar rename direto;
- criar doc 25 por reescrita estrutural;
- preservar o arquivo antigo como fonte historica/superseded;
- atualizar referencias em uma unica janela de patch;
- registrar tudo no `ARCHITECTURE_PATCH_REPORT.md`;
- exigir approval Founder + PMO + Metacognik + Technical.

Racional: Self-Evolving nao e apenas Implementation. Ele e a camada evolutiva do CKOS e precisa governar como o sistema aprende, sugere mudancas, testa em sandbox, mede regressao, pede approval, faz rollback e evolui capabilities.

## 8. Patch plan futuro

Nao aplicar neste microgate.

### 8.1 Arquivos que seriam alterados

Governanca:

- `00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md`
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md`
- `ARCHITECTURE_PATCH_REPORT.md`
- `CKOS_FILETREE_MAP.md`
- `CKOS_FOLDER_MEMORY.md`
- `CKOS_VAULT_MAP_REFRESH_REPORT.md`

Docs com referencias diretas:

- `01_THINKING_SYSTEM/01_CKOS_AI_FIRST_CONSTITUTION.md`
- `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md`
- `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md`
- `03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`
- `03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`
- `05_IMPLEMENTATION_SYSTEM/00_README_IMPLEMENTATION_SYSTEM.md`
- `05_IMPLEMENTATION_SYSTEM/17_IMPLEMENTATION_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md`
- `05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`

Possiveis docs a auditar:

- `06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`, por mencao vaga a "doc 25".
- packs em `000_UPGRADE/`, apenas se Founder quiser limpar memoria auxiliar.

### 8.2 Referências que seriam atualizadas

Substituicoes provaveis:

- `21_SELF_EVOLVING_SYSTEM.md` -> `25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`
- `[[21_SELF_EVOLVING_SYSTEM]]` -> `[[25_SELF_EVOLVING_SYSTEM_ARCHITECTURE]]`
- `Self-Evolving (21)` -> `Self-Evolving (25)`
- `doc 21 (Self-Evolving)` -> `doc 25 (Self-Evolving)`
- path antigo `../05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` -> `../07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`

Referencias ROI devem permanecer:

- `21_ROI_ARCHITECTURE.md`
- `doc 21` quando claramente ROI.

### 8.3 Novo caminho

```txt
07_EVOLUTION_SYSTEM/
  00_README_EVOLUTION_SYSTEM.md
  25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md
```

O README pode ser criado no mesmo patch se a nova pasta for aprovada como fase canonica.

### 8.4 Arquivo antigo

Recomendacao:

- manter `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` como superseded/historico;
- adicionar, em patch futuro, aviso no topo apontando para o novo doc 25;
- nao deletar;
- nao mover sem decisao Founder.

### 8.5 Registro no Patch Report

Adicionar secao:

```txt
# 26. Self-Evolving Conflict Resolution Patch
```

Registrar:

- conflito resolvido;
- doc 25 criado;
- arquivo antigo mantido como superseded;
- lista de referencias atualizadas;
- confirmacao de que ROI continua doc 21;
- confirmacao de que docs 26-34 ainda nao foram criados.

### 8.6 Atualizar Master Map

Adicionar:

- `07_EVOLUTION_SYSTEM/`;
- doc 25 como primeiro doc da camada;
- relacao com docs 10-13, 17-20, 21-24 e RAW/STUDY;
- nota de supersession do antigo Self-Evolving 21.

### 8.7 Atualizar Dependency Map

Adicionar:

- doc 25 depende de 04, 05, 10, 11, 12, 13, 17, 18, 19, 20 e Business Systems 21-24;
- docs 26-34 dependem do doc 25 quando envolverem learning, capability evolution ou final implementation readiness;
- UI/UX continua bloqueado ate 25-31.

### 8.8 Atualizar related_notes

Atualizar related notes nos docs que apontam para `21_SELF_EVOLVING_SYSTEM`.

Adicionar ao novo doc 25:

- `03_AGENT_OPERATING_MODEL.md`
- `04_AUTONOMY_AND_APPROVALS.md`
- `05_MEMORY_AND_CONTEXT_ARCHITECTURE.md`
- `10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `11_DATA_MODEL_AND_PERSISTENCE.md`
- `12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`
- `13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`
- `17_IMPLEMENTATION_PROTOCOL.md`
- `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`
- docs 21-24 Business Systems.

### 8.9 Gates humanos necessários

- Founder: aprova destino e criacao do doc 25.
- PMO_CKOS: aprova sequencia e patch plan.
- Metacognik: audita risco de autonomia e coerencia AI-first.
- Technical: audita runtime, sandbox, rollback, evals, security e data model.
- QA Lead: valida referencias, links e criterios de gate.

### 8.10 Critério de aprovação

O patch futuro so deve ser aprovado se:

- ROI permanece doc 21 sem ambiguidade.
- Self-Evolving vira doc 25 sem link quebrado.
- Arquivo antigo fica claramente superseded/historico.
- Novo doc 25 nao promete autonomia sem runtime/security/evals/sandbox/rollback.
- RAW/STUDY permanece como gate de conhecimento.
- Docs 26-34 nao sao criados no mesmo patch sem approval separado.

## 9. Arquivos que seriam impactados

Impacto alto:

- `00_MASTER_MAP.md`
- `00_DEPENDENCY_MAP.md`
- `ARCHITECTURE_PATCH_REPORT.md`
- `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`
- `03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`
- `05_IMPLEMENTATION_SYSTEM/17_IMPLEMENTATION_PROTOCOL.md`
- `05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`

Impacto medio:

- `01_THINKING_SYSTEM/01_CKOS_AI_FIRST_CONSTITUTION.md`
- `01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md`
- `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md`
- `05_IMPLEMENTATION_SYSTEM/00_README_IMPLEMENTATION_SYSTEM.md`
- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md`
- mapas auxiliares.

Impacto baixo/auxiliar:

- `000_UPGRADE/*`
- memories auxiliares;
- proposed reports antigos.

## 10. Arquivos que não devem ser tocados ainda

Neste microgate, nao tocar:

- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`
- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`
- docs 01-24
- `00_MASTER_MAP.md`
- `00_DOCUMENT_TEMPLATE.md`
- `00_TAXONOMY_AND_NAMING.md`
- `00_DEPENDENCY_MAP.md`
- `ARCHITECTURE_PATCH_REPORT.md`
- JSONs n8n
- `.obsidian/`
- `Memoria GPT.md`
- qualquer UI, backend, migration, API, banco, agente real ou automacao runtime.

## 11. Riscos

- Renomear direto e quebrar references/wiki links.
- Criar `07_EVOLUTION_SYSTEM/` sem atualizar Master Map e Dependency Map.
- Tratar doc 25 como autorizacao de self-modification real.
- Confundir learning loop com autonomia de producao.
- Ignorar Business Systems 21-24 como fontes de sinais evolutivos.
- Manter o arquivo antigo como doc ativo e perpetuar dupla numeracao 21.
- Criar docs 26-34 antes de fechar o destino do doc 25.

## 12. Critérios de aprovação Founder

Founder deve aprovar explicitamente:

- destino final: `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`;
- status do antigo `21_SELF_EVOLVING_SYSTEM.md` como superseded/historico;
- permissao para criar nova pasta canonica `07_EVOLUTION_SYSTEM/`;
- autorizacao para patchar referencias canonicas;
- criterio de que doc 25 e arquitetura, nao implementacao;
- manutencao de UI/UX bloqueado ate docs 25-31.

## 13. Próxima ação recomendada

Submeter esta decisao ao Founder.

Acao recomendada:

```txt
Aprovar Opcao A com reescrita estrutural controlada:
07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md
```

Apos aprovacao, executar um patch separado para criar `07_EVOLUTION_SYSTEM/`, escrever o novo doc 25 e atualizar referencias. Nao fazer rename direto.

