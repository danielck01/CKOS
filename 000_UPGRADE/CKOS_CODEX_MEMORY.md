---
title: CKOS Codex Memory
system_id: ckos_codex_memory
category: upgrade_memory
status: draft
version: 1.2.0
owner: ceo_agent
reviewers:
  - founder
  - pmo_ckos
  - metacognik
related_notes:
  - ../CKOS_FILETREE_MAP.md
  - ../000_UPLOADS/00_UPLOADS_INDEX.md
  - ../000_STUDY_NOTES/00_STUDY_INDEX.md
  - CKOS_CODEX_CONTINUATION_PACK/00_README_START_HERE.md
  - CKOS_CODEX_CONTINUATION_PACK/00_CONTEXT/CKOS_CURRENT_STATE.md
  - CKOS_CODEX_CONTINUATION_PACK/06_ROADMAP/DEVELOPMENT_PLAN_WITHOUT_UI.md
created_for: CKOS_DOCUMENTATION_REVIEWED
---

# CKOS Codex Memory

## Refresh 2026-05-26

O estado real do vault prevalece sobre o continuation pack:

- Docs 21-24 Business Systems ja existem em `06_BUSINESS_SYSTEMS/`.
- Gate I esta documentalmente completo no `ARCHITECTURE_PATCH_REPORT.md` v1.7.0.
- Nao recriar docs 21-24.
- Nao criar docs 25-30 sem autorizacao Founder e decisao taxonomica.
- Nao iniciar UI/UX implementation, backend, migrations, APIs, banco de dados, agentes reais ou automacoes runtime.
- Nao mover, deletar, renomear ou renumerar arquivos sem relatorio previo.
- n8n permanece acelerador/prototipo auxiliar, nao core CKOS.
- Manus permanece ferramenta temporaria de pesquisa/bootstrap, nao infraestrutura definitiva.

Arquivo de referencia para filetree completo: `../CKOS_FILETREE_MAP.md`.

Conflito de numeracao registrado, sem renumeracao neste refresh:

- `../05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`
- `../06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`

Opcoes futuras: renumerar Self-Evolving para doc 25 apos auditoria e aprovacao, manter como auxiliar/historico, ou criar categoria futura de Evolution/Learning System.

## Microgate RAW/STUDY 2026-05-27

Founder aprovou `UPLOADS_STUDY_MICROGATE_PROPOSAL`.

Criado de forma controlada:

- `../000_UPLOADS/` como camada RAW.
- `../000_STUDY_NOTES/` como camada STUDY.
- Templates locais em `../000_STUDY_NOTES/_templates/`.
- Indices `../000_UPLOADS/00_UPLOADS_INDEX.md` e `../000_STUDY_NOTES/00_STUDY_INDEX.md`.

Escopo respeitado:

- Nenhum doc canonico 01-24 alterado.
- Nenhum Business System 21-24 alterado.
- `21_SELF_EVOLVING_SYSTEM.md` nao foi renomeado.
- Nenhum arquivo foi movido ou deletado.
- Nenhum JSON n8n foi alterado.
- Nenhuma UI, backend, migration, API, banco, agente real ou automacao runtime foi criada.

Regra operacional nova:

- RAW nao e fonte de verdade.
- STUDY nao e canonico.
- Nada entra no canonico sem STUDY, patch plan, QA e aprovacao Founder.
- `09_APPROVED_FOR_CANONICAL_PATCH/` significa pronto para patch plan, nao aprovado para aplicacao direta.

## Resumo do pack

O `CKOS_CODEX_CONTINUATION_PACK` orienta a continuidade documental do CKOS enquanto multiplas ferramentas sao usadas em paralelo. Ele reforca que o CKOS e um AI-first Operating System, nao chat, nao dashboard e nao app de tarefas. O pack posiciona Codex como agente de auditoria, patch controlado, consistencia Markdown e PMO tecnico; Antigravity como apoio de pesquisa visual futura; Claude como revisao estrategica quando disponivel.

Conteudos principais:

- `00_README_START_HERE.md`: regra central de nao implementar e ordem canonica.
- `00_CONTEXT/CKOS_CURRENT_STATE.md`: definicao operacional do CKOS como control plane cognitivo.
- `00_CONTEXT/FILETREE_EXPECTED_MAP.md`: mapa esperado para auditoria.
- `01_PROMPTS/`: prompts para Codex, Antigravity e Visual Director.
- `02_SKILLS/`: skills conceituais de planner, context engineering, PMO documentation e research collector.
- `03_ARCHITECTURE_NOTES/`: notas futuras 25-29.
- `04_RESEARCH/`: ideia de deep research via YouTube.
- `05_VISUAL_HTML_STUDY/`: estudo visual futuro, nao implementacao.
- `06_ROADMAP/`: sequencia docs 21-30 e plano sem UI.

## Decisoes travadas

- Nao implementar UI, backend, migrations, agentes reais ou banco nesta fase.
- O CKOS deve ser tratado como sistema operacional AI-first, event-driven, policy-governed e projection-driven.
- Frontend nao decide verdade, nao chama provider externo direto e nao expoe provider/token/actor_id.
- CommandBar nao envia direto para agente; passa por intent router, context pack builder, policy engine, model router, agent router/workflow engine, events, projections e UI update.
- Docs 25-29 devem vir antes de UI/UX.

## Divergencia encontrada

O pack diz que 22, 23 e 24 ainda faltam. O vault real contem:

- `06_BUSINESS_SYSTEMS/22_FEEDBACK_SYSTEM_ARCHITECTURE.md`
- `06_BUSINESS_SYSTEMS/23_SUPPORT_SYSTEM_ARCHITECTURE.md`
- `06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`

O `ARCHITECTURE_PATCH_REPORT.md` tambem registra docs 22-24 concluidos e Gate I fechado. Portanto, o pack e util como contexto historico, mas esta desatualizado no roadmap imediato.

## Riscos

- Recriar ou sobrescrever docs 22-24 por seguir o pack literalmente.
- Usar notas visuais para iniciar UI/UX antes de fechar 25-29.
- Transformar skills conceituais em runtime real antes da governanca aprovar.
- Misturar CKOS com Branddock ou criar dashboards fixos por dominio.

## Proximos passos

1. Tratar o pack como contexto auxiliar, nao como fonte canonica quando divergir do vault.
2. Atualizar plano de continuidade com base no estado real: 22-24 existentes; proximos candidatos 25-29.
3. Reconciliar duplicidades em `05_IMPLEMENTATION_SYSTEM` antes de novos patches estruturais.
4. Preparar squads/chats paralelos com arquivos permitidos e proibidos.

## Dependencias

- `ARCHITECTURE_PATCH_REPORT.md`
- `QA_DOCUMENTATION_CHECKLIST.md`
- `CKOS_FILETREE_MAP.md`
- `00_SYSTEM_GOVERNANCE/00_DEPENDENCY_MAP.md`
- `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md`
- `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md`
- `03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md`
- `03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md`
- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`
- `06_BUSINESS_SYSTEMS/22_FEEDBACK_SYSTEM_ARCHITECTURE.md`
- `06_BUSINESS_SYSTEMS/23_SUPPORT_SYSTEM_ARCHITECTURE.md`
- `06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`

## Arquivos que precisam ser cruzados

- `CKOS_CODEX_CONTINUATION_PACK/06_ROADMAP/DOCS_21_TO_30_SEQUENCE.md` com `ARCHITECTURE_PATCH_REPORT.md`.
- `CKOS_CODEX_CONTINUATION_PACK/00_CONTEXT/FILETREE_EXPECTED_MAP.md` com a filetree real.
- `CKOS_CODEX_CONTINUATION_PACK/03_ARCHITECTURE_NOTES/*` com os docs canonicos antes de promover qualquer nota para `25-29`.
- `CKOS_CODEX_CONTINUATION_PACK/05_VISUAL_HTML_STUDY/*` com futuro `30_UI_UX_ARCHITECTURE.md`, apenas depois dos gates anteriores.

## Perguntas pendentes para o Founder

- Confirmar se `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` deve virar doc 25, permanecer como nota auxiliar ou ser renumerado em patch aprovado.
- Confirmar se docs 25-29 devem entrar em `06_BUSINESS_SYSTEMS`, nova pasta `07_COMPLEMENTARY_SYSTEMS` ou outra taxonomia.
- Confirmar se `18_RESEARCH_PROTOCOL_FOR_MANUS.md` deve ser marcado como superseded.

## Tarefas recomendadas para outros chats/agentes

- PMO_AGENT_CKOS: reconciliar roadmap e estado real do vault.
- DOCS_ARCHITECT_AGENT: propor taxonomia para docs 25-30.
- RUNTIME_ARCHITECT_AGENT: revisar dependencias de Learning, Collectors e CKStore contra runtime.
- QA_AGENT: auditar duplicidades 18/19/21 e registrar patch report.
- METACOGNIK_AGENT: testar coerencia da tese AI-first OS contra todos os packs.
