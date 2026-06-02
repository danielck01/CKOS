---
title: Project Creation From Intent Protocol
system_id: project_creation_from_intent_protocol
category: creator_mode_protocol
status: active
version: 1.1.0
updated_at: 2026-05-26
owner: ceo_agent
reviewers:
  - founder
  - pmo_ckos
  - metacognik
created_for: CKOS_CREATOR_MODE_PACK
---

# Project Creation From Intent Protocol

## Objetivo

Definir como um projeto nasce no CKOS a partir de uma intencao curta do Founder, sem pular briefing, contexto, risco, custo, auditoria e aprovacao.

O principio central e:

```txt
Nao criar projeto antes de entender o projeto.
Nao criar pack de notas antes de aprovar filetree.
Nao criar estrategia final antes de fontes, briefing e risco.
```

## Entrada minima

```txt
Criar projeto para [objetivo minimo].
```

## Interpretacao inicial obrigatoria

Toda intencao minima deve virar primeiro:

```txt
CEO_AGENT_INTERPRETATION

Intent detected:

Project type:

Category:

Subcategory:

Risk level:

Required context:

Source mode:
attached_sources | deep_research_requested | exploratory_no_sources

Recommended first action:

Estimated CKOS credits:

Blocked actions:

Needs PMO audit?

Founder approval needed?

Suggested output:

Question to Founder:
```

## Pipeline

```txt
1. IntentSubmitted
2. IntentResolved
3. ProjectTypeClassified
4. RiskClassified
5. ContextRequiredMapped
6. SourceModeRequested
7. CreditEstimateProduced
8. PMOReviewRequested
9. FiletreeProposalGenerated
10. FounderApprovalRequested
11. CheckoutLockCreated
12. FirstArtifactsGenerated
13. PMOAuditCompleted
14. CheckoutReleased
```

## Categorias e subcategorias

O CEO Agent deve classificar todo novo projeto antes de propor filetree.

Exemplos de categorias:

- `personal_branding`
- `legal_marketing`
- `research_project`
- `business_strategy`
- `product_strategy`
- `content_system`
- `operations_system`
- `internal_ckos_documentation`

Exemplos de subcategorias:

- `personal_branding_legal`
- `regulated_domain_strategy`
- `social_media_authority`
- `ethical_risk_mapping`
- `research_synthesis`
- `filetree_planning`
- `prompt_pack_creation`
- `client_delivery_artifact`

Se houver duvida de classificacao, o CEO deve registrar hipoteses e pedir PMO review antes de criar pasta.

## Modos de fonte

### Modo A - Usuario anexa fontes

Usar quando o Founder possui pesquisas, documentos, PDFs, notas ou links.

Conectores simulados:

- `DocumentUploadConnector`
- `GoogleDriveConnector`
- `VaultRAGConnector`

Politicas:

- `POLICY_SOURCE_INDEX_REQUIRED`
- `POLICY_EVIDENCE_MAP_REQUIRED`
- `POLICY_SOURCE_CONFIDENCE_REQUIRED`
- `POLICY_NO_UNSOURCED_FINAL_CLAIMS`

### Modo B - Deep research autorizado

Usar quando faltam fontes e o projeto exige contexto externo.

Conectores simulados:

- `WebResearchConnector_Perplexity`
- `OABOfficialSourcesConnector`
- `ApifyPublicSocialCollector`
- `YouTubeTranscriptCollector`

Politicas:

- `POLICY_DEEP_RESEARCH_COST_APPROVAL`
- `POLICY_EXTERNAL_SOURCE_CITATION_REQUIRED`
- `POLICY_HUMAN_REVIEW_FOR_REGULATED_DOMAIN`
- `POLICY_CONNECTOR_SCOPE_LIMIT_REQUIRED`
- `POLICY_RESEARCH_OUTPUT_IS_NOT_CANONICAL`

### Modo C - Briefing exploratorio sem fontes

Usar quando o Founder quer apenas estruturar perguntas e gaps.

Politicas:

- `POLICY_NO_FINAL_STRATEGY_WITHOUT_SOURCES`
- `POLICY_HYPOTHESIS_ONLY_OUTPUT`
- `POLICY_BRIEFING_BEFORE_STRATEGY`

## Plano antes de arquivos

Antes de criar qualquer pasta ou documento de projeto, o CEO deve mostrar ao Founder:

- plano de execucao;
- arquivos e memorias que pretende consultar;
- custo estimado em CKC;
- riscos;
- dependencias;
- opcoes de saida;
- aprovacao necessaria.

Se aprovado, o CEO pode criar somente os artefatos explicitamente autorizados.

## Artefatos obrigatorios antes do pack de notas

1. `PROJECT_INTENT_ANALYSIS.md`
2. `PROJECT_FILETREE_PROPOSAL.md`
3. `PROJECT_EXECUTION_PLAN.md`
4. `PMO_REVIEW_REQUEST.md`
5. `FOUNDER_APPROVAL_CHECKLIST.md`

## Regra de filetree

Nenhuma pasta de projeto vira oficial sem aprovacao Founder. O CEO pode propor filetree; PMO audita; Founder aprova; so entao o CEO cria o pack de notas.

O filetree proposto deve separar:

- `00_ADMIN`
- `01_CONTEXT`
- `02_SOURCES`
- `03_RESEARCH`
- `04_STRATEGY_DRAFTS`
- `05_RISK_AND_COMPLIANCE`
- `06_OUTPUTS`
- `07_PROMPTS`
- `08_PMO_AUDIT`
- `09_DECISIONS`

Essa estrutura pode ser reduzida conforme tamanho do projeto, mas nao pode ocultar fontes, riscos ou aprovacoes.

## Regra para dominios sensiveis

Se o projeto envolver direito, saude, financas, criancas, dados sensiveis, reputacao publica ou risco juridico, o output inicial deve ser `analysis_doc`, nao estrategia final.

## Projeto Miriam como futuro case

Se a intencao mencionar Miriam, advogada penal, advocacia criminal, Instagram juridico ou personal branding juridico, classificar como:

```txt
project_type: personal_branding_legal
category: personal_branding
subcategory: regulated_legal_marketing
risk_level: high
```

Fontes obrigatorias esperadas:

- Provimento 205/2021 da OAB;
- Codigo de Etica e Disciplina da OAB;
- pesquisas anexadas pelo Founder;
- limites de publicidade juridica;
- analise reputacional;
- benchmark seguro.

Bloqueios:

- nao criar tom de voz definitivo;
- nao criar pilares definitivos;
- nao criar plano de lancamento definitivo;
- nao criar identidade visual;
- nao fazer promessa comercial agressiva;
- nao afirmar conformidade juridica sem fonte e revisao humana.
