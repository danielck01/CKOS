---
title: 000_ROADMAPS — ck_roi
file: ck_roi.md
phase: 000_ROADMAPS
category: roi_register
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
purpose: Definir ROI operacional da camada auxiliar governada 000_ROADMAPS.
inputs:
  - 000_ROADMAPS/README.md
  - 000_ROADMAPS/ck_tasks.md
outputs:
  - valor operacional
  - custo simulado
  - metricas de retorno
framework: Operational ROI, not direct financial ROI.
edge_cases: Roadmap treated as canonical source; agent reads excessive context; implementation starts from planning material.
integrations: codex, claude, antigravity, ceo_agent, pmo_auditor and founder review sessions.
prompts: Read README and ck_memory before task-specific planning, patching or handoff.
metrics: YAML valid; 0 canonical docs created; 0 implementation changes; handoff logged when sessions change.
confidence: unverified
provenance_status: unverified
source_tool: chatgpt
related_notes:
  - README.md
  - ck_tasks.md
tags: [roadmaps, roi, ckc]
---

# ck_roi — 000_ROADMAPS

## Definicao

ROI nesta camada significa valor operacional, nao retorno financeiro direto. O objetivo e reduzir custo cognitivo, risco documental e retrabalho antes de qualquer implementacao.

## Tipos de retorno

| roi_type | definicao | indicador esperado |
|---|---|---|
| menor_entropia | Menos arquivos soltos, decisoes duplicadas e roadmaps concorrentes | Agente encontra contexto em README + ck_memory |
| menor_custo_de_contexto | Menos leitura desnecessaria por sessao | Sessoes usam memoria curta + 3 a 7 docs obrigatorios |
| menos_duplicidade | Menos criacao de docs ou lanes ja existentes | PMO Auditor identifica fonte correta antes de patch |
| melhor_retomada_por_agentes | Nova sessao entende estado sem reler todo o vault | Handoff e ck_memory atualizados |
| previsibilidade | Proximos passos em P0/P1/P2/P3 ficam visiveis | Kanban e gates claros |
| controle_founder_pmo | Excecoes e bloqueios sob decisao humana | Founder aprova bloqueios, proximos lotes e excecoes |
| reducao_de_retrabalho | Menos correcoes por escopo ruim ou YAML invalido | YAML normalizado e acceptance criteria aplicados |

## Estimativa CKC simulada

| acao | estimated_ckc | retorno esperado |
|---|---:|---|
| Criar controles raiz | 8 | Retomada rapida e governanca por pasta |
| Normalizar YAML | 22 | Menos falhas de parser, RAG e auditoria |
| Atualizar README e regras | 8 | Menos risco de agentes agirem sem contexto |
| Registrar mapas auxiliares | 10 | Menos conflito de filetree |
| Validar P0 | 6 | Menos regressao documental |
| Criar matriz de roteamento P1.6 | 22 | Menos duplicidade entre roadmaps antigos e novos; handoff Antigravity mais seguro |
| Criar politica multi-sessao P1.7 | 28 | Menos conflito entre agentes simultaneos; locks e releases mais auditaveis |

## Retorno operacional P1.6

| acao | retorno operacional | indicador |
|---|---|---|
| Corrigir NULs nos READMEs `14-21` | leitura minima confiavel | 0 arquivos com caractere NUL nos READMEs novos |
| Criar `ROADMAP_ROUTING_MATRIX.md` | decisao mais rapida sobre qual roadmap usar | pares `02/14`, `06/15`, `07/16`, `10/17` roteados |
| Atualizar memorias e mapas auxiliares | retomada por agentes com menor custo de contexto | nova sessao encontra `14-21`, P1.5 e P1.6 sem reler todo vault |
| Manter Antigravity bloqueado ate handoff restrito | menos risco de UI prematura | Study Mode exige contexto minimo e approval |

## Retorno operacional P1.7

| acao | retorno operacional | indicador |
|---|---|---|
| Criar `SESSION_REGISTRY.md` | evita sessoes invisiveis e conflitos de escrita | toda sessao futura declara campos obrigatorios |
| Criar `MULTI_SESSION_EXECUTION_POLICY.md` | padroniza session types, locks, releases e nivel de inteligencia | matriz `planning` a `canonical_patch` visivel |
| Criar gate Antigravity em `12_SESSION_GATES` | reduz risco de Design Study virar UI prematura | Antigravity bloqueado ate approval Founder |
| Exigir impacto em ROI, risco, custo ou governanca nas perguntas | reduz ruido e retrabalho de decisao | perguntas sem consequencia sao removidas ou reescritas |

## Regra

`ck_roi.md` e obrigatorio nesta camada porque roadmaps geram custo, decisao, risco e coordenacao multiagente. Pastas simples do vault nao precisam de `ck_roi.md` salvo quando houver valor operacional mensuravel.
