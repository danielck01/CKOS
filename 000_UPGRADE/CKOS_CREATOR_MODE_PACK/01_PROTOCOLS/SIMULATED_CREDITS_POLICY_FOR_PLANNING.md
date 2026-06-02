---
title: Simulated Credits Policy For Planning
system_id: simulated_credits_policy_for_planning
category: creator_mode_policy
status: active
version: 1.1.0
updated_at: 2026-05-26
owner: pmo_ckos
reviewers:
  - founder
  - ceo_agent
created_for: CKOS_CREATOR_MODE_PACK
---

# Simulated Credits Policy For Planning

## Proposito

Simular creditos CKOS no Codex para educar o Founder sobre custo, risco e escopo antes de executar acoes documentais.

Os creditos CKOS neste pack sao demonstrativos. Eles nao representam cobranca real. Eles existem para tornar visivel o custo cognitivo, documental, operacional e de risco de cada acao.

## Tabela base

| Acao | Custo simulado | Risco |
|---|---:|---|
| Leitura local simples | 1-3 CKC | baixo |
| Analise documental | 3-8 CKC | baixo/medio |
| Plano de execucao | 4-10 CKC | baixo/medio |
| Proposta de filetree | 4-8 CKC | medio |
| Auditoria PMO | 5-15 CKC | medio |
| Revisao Metacognik | 8-20 CKC | medio/alto |
| Pack de notas pequeno | 8-15 CKC | medio |
| Pack de notas medio | 15-35 CKC | medio |
| Pack de notas grande | 35-80 CKC | alto |
| Deep research externo | 20-100 CKC | alto |
| Benchmark social externo | 12-40 CKC | medio/alto |
| Prompt pack | 8-20 CKC | medio |
| Visual research pack | 15-45 CKC | medio/alto |
| Criacao de projeto novo | 12-30 CKC | medio |
| Projeto em dominio regulado | 20-60 CKC | alto |
| Auditoria final de entrega | 5-12 CKC | medio |

## Gates de custo

- 0-5 CKC: pode ser auto-planejado, se risco baixo.
- 6-15 CKC: requer confirmacao Founder.
- 16-35 CKC: requer PMO audit.
- 36+ CKC: requer Founder + PMO + justificativa de escopo.
- Dominio sensivel: sempre requer PMO audit, mesmo com custo baixo.
- Novo projeto: sempre requer Founder approval antes de criar pack.
- Uso de fonte externa: sempre requer declarar conector, escopo e limite.
- Criacao de filetree: sempre requer PMO se houver risco medio ou alto.

## Formato de estimativa

```txt
SIMULACAO DE CREDITOS CKOS

Acao:
Custo estimado:
Risco:
Conectores simulados:
Policies aplicadas:
Aprovacao necessaria:
Alternativas mais baratas:
```

## Estimativa por fase de projeto

| Fase | Custo simulado | Observacao |
|---|---:|---|
| Interpretacao de intencao | 1-3 CKC | Sem criar arquivos |
| Context Pack local | 3-8 CKC | Leitura de memoria e uploads |
| Plano de execucao | 4-10 CKC | Inclui riscos e dependencias |
| PMO handoff | 5-15 CKC | Obrigatorio em risco medio/alto |
| Filetree proposal | 4-8 CKC | Nao cria pack ainda |
| Pack inicial aprovado | 8-25 CKC | So apos Founder approval |
| Deep research externo | 20-100 CKC | Exige escopo, fontes e aprovacao |
| Delivery audit | 5-12 CKC | Antes de marcar como pronto |

## Politicas de custo

- `POLICY_COST_VISIBILITY_REQUIRED`
- `POLICY_CREDIT_RANGE_NOT_ABSOLUTE`
- `POLICY_EXTERNAL_RESEARCH_COST_APPROVAL`
- `POLICY_PACK_CREATION_AFTER_FILETREE_APPROVAL`
- `POLICY_PMO_REQUIRED_FOR_HIGH_COST`
- `POLICY_REGULATED_DOMAIN_COST_ESCALATION`

## Conectores e custo

Conectores simulados de baixo custo:

- `VaultRAGConnector`
- `LocalFiletreeScanner`
- `DocumentUploadConnector`

Conectores simulados de custo medio:

- `GoogleDriveConnector`
- `NotionConnector`
- `YouTubeTranscriptCollector`
- `ApifyPublicSocialCollector`

Conectores simulados de custo alto:

- `WebResearchConnector_Perplexity`
- `OABOfficialSourcesConnector`
- `MultiSourceBenchmarkConnector`

O conector nao deve ser tratado como infraestrutura definitiva do CKOS. Ele e apenas uma simulacao operacional para planejamento.

## Ledger recomendado

Todo plano deve registrar:

```txt
CREDIT_LEDGER

task_id:
project:
phase:
local_reading_cost:
planning_cost:
pmo_cost:
external_research_cost:
artifact_generation_cost:
delivery_audit_cost:
total_estimated_range:
approval_required:
approved_by:
status:
```

## Regras

- Sempre usar faixas, nao valores absolutos.
- Sempre separar custo local de custo externo.
- Nunca executar deep research externo sem aprovar custo.
- Nunca gerar pack grande sem filetree aprovada.
- Custo simulado nao e cobranca real; e ferramenta de governanca.
- Nunca esconder custo de PMO, mesmo quando a auditoria for simulada.
- Sempre oferecer uma alternativa mais barata quando o custo passar de 35 CKC.
