---
title: 000_ROADMAPS — README
file: README.md
phase: 000_ROADMAPS
category: roadmap_governance
version: 1.0.0
status: active
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
  - metacognik
purpose: Planejar, governar e sincronizar a evolução documental e operacional do CKOS sem gerar implementação prematura.
inputs:
  - 00_SYSTEM_GOVERNANCE/00_MASTER_MAP.md
  - CKOS_FOLDER_MEMORY.md
  - CKOS_FILETREE_MAP.md
  - ARCHITECTURE_PATCH_REPORT.md
outputs:
  - plano rastreável
  - tarefas auditáveis
  - riscos abertos
  - critérios de aceite
framework: Sentir, Pensar, Criar, Conectar, Avaliar, Elevar
edge_cases: Roadmap treated as canonical source; agent reads excessive context; implementation starts from planning material.
integrations: codex, claude, antigravity, ceo_agent, pmo_auditor and founder review sessions.
prompts: Read README and ck_memory before task-specific planning, patching or handoff.
metrics: YAML valid; 0 canonical docs created; 0 implementation changes; handoff logged when sessions change.
confidence: unverified
provenance_status: unverified
source_tool: chatgpt
related_notes:
  - README.md
tags: [roadmaps, governance, planning]
---

# 000_ROADMAPS

## Status operacional P0

`000_ROADMAPS/` e uma camada auxiliar governada. Ela organiza plano vivo, tarefas, riscos, ROI operacional, feedback e handoffs, mas nao possui autoridade canonica.

Esta camada nao autoriza docs canonicos novos, docs 26-34, UI/UX implementation, backend, API, banco, migrations, JSONs n8n, Antigravity ou agentes reais.

## Ordem curta de leitura por agente

1. Ler a nota curta da tarefa ou handoff recebido.
2. Ler este `README.md`.
3. Ler `ck_memory.md` da raiz de `000_ROADMAPS/`.
4. Ler o `README.md` e o `ck_memory.md` da pasta-alvo.
5. Ler apenas 3 a 7 docs obrigatorios da tarefa.
6. Gerar plano, estimativa CKC e riscos.
7. Aguardar approval quando houver patch, custo, risco alto ou excecao.

O agente nao precisa saber tudo sempre. Ele precisa do contexto certo no momento certo.

## Regra de contexto minimo

Nenhuma sessao deve iniciar lendo o vault inteiro. Leituras amplas so acontecem quando a tarefa exige auditoria global e o checkout declara isso explicitamente.

Antes de qualquer escrita, a sessao deve registrar ou receber:

- task_id;
- objetivo;
- files_allowed;
- files_forbidden;
- estimated_ckc;
- approval_required;
- criterio de aceite.

## Checkout lock

Toda escrita nesta camada exige `CHECKOUT LOCK` com escopo fechado. O lock deve listar arquivos permitidos, arquivos proibidos, razao, custo estimado e aprovacao requerida.

Ao finalizar, a sessao deve emitir `CHECKOUT RELEASE` com arquivos criados, arquivos alterados, validacao, riscos remanescentes e proxima acao.

## Handoff entre sessoes

- CEO Agent planeja, prioriza, estima CKC e prepara handoff.
- PMO Auditor valida escopo, YAML, riscos, custo e governanca.
- Executor atua apenas dentro do escopo aprovado.
- Founder aprova bloqueios, proximos lotes e excecoes.
- Nenhum agente assume autoridade canonica.
- Um agente escreve, outro audita.
- Toda sessao nova deve ler `README.md` + `ck_memory.md` antes de agir.

## Security / Governance / Cost / Approval Impact

Toda tarefa relevante deve responder:

- toca dados sensiveis?
- precisa approval?
- tem custo?
- tem risco cross-tenant?
- usa secret?
- usa ferramenta externa?
- gera output publico?
- pode ser revertida?
- gera audit log?

Se a resposta for desconhecida, a tarefa fica em `Blocked` ate PMO Auditor ou Founder decidir.

Camada auxiliar para planejar a evolução do CKOS sem confundir estudo, decisão canônica e implementação. Esta pasta não substitui os documentos canônicos. Ela cria o plano vivo para que Founder, CEO Agent, PMO_CKOS, Codex, Claude, Antigravity e futuros agentes trabalhem sem entropia.

## Regra central

Todo roadmap precisa responder:

1. O que será sentido: problema, tensão, intenção e valor humano.
2. O que será pensado: dependências, riscos, políticas, custos e sequência lógica.
3. O que será criado: documentos, estudos, artefatos, templates, prompts ou patch candidates.
4. O que será conectado: pastas, docs, agentes, runtime, business systems e UI.
5. O que será avaliado: critérios de aceite, QA, Metacognik, ROI, segurança e custo.
6. O que será elevado: aprendizado, memória, próximos padrões e melhoria contínua.

## Estrutura mínima obrigatória por roadmap

Cada subpasta estratégica deve possuir:

- `README.md`: navegação humana e operacional.
- `ck_memory.md`: memória viva da pasta.
- `ck_tasks.md`: kanban do roadmap.
- `ck_risks.md`: riscos e mitigação.
- `ck_roi.md`: retorno esperado, custo e métrica de valor.
- `ck_feedback.md`: feedback Founder, PMO, Metacognik, QA e agentes.
- `ck_agent_handoffs.md`: handoffs entre Codex, Claude, Antigravity, CEO Agent, PMO e especialistas.

## Ordem de uso

1. Leia `00_MASTER_ROADMAP/README.md`.
2. Atualize o `ck_memory.md` da pasta antes de alterar qualquer nota.
3. Registre tarefas no `ck_tasks.md` antes de executar.
4. Registre riscos no `ck_risks.md` antes de propor patch.
5. Registre ROI no `ck_roi.md` quando houver custo, crédito, tempo ou valor estratégico.
6. Registre feedback no `ck_feedback.md` após revisão.
7. Registre handoff em `ck_agent_handoffs.md` ao trocar de modelo, chat ou executor.

## Bloqueios

Não criar docs canônicos 26–34 a partir daqui sem microgate. Não implementar UI/backend. Não criar migrations. Não promover n8n, Manus ou Antigravity a core runtime. Não mover arquivos sem patch plan.
