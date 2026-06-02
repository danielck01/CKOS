---
title: Connector Registry Simulation
system_id: connector_registry_simulation
category: creator_mode_simulation_runtime
status: active
version: 1.0.0
owner: ceo_agent
reviewers:
  - founder
  - pmo_ckos
  - metacognik
created_for: CKOS_CREATOR_MODE_PACK
created_at: 2026-05-26
---

# Connector Registry Simulation

## Proposito

Registrar conectores que podem ser mencionados em simulacoes de projeto no Codex.

Este registry nao cria integracoes reais. Ele define nomes, riscos, custos, approvals e limites.

## Estados possiveis

| Status | Significado |
|---|---|
| `simulated_available` | Pode ser usado em plano/documento, sem execucao real |
| `requires_founder_approval` | So pode ser citado em execucao apos aprovacao |
| `requires_pmo_audit` | Exige auditoria antes de qualquer uso |
| `blocked_for_runtime` | Nao pode ser usado como runtime |
| `prototype_only` | Permitido apenas para prototipacao ou backoffice |
| `manual_import_only` | Fonte deve ser importada manualmente |

## Registry

| Connector | Tipo | Status | Risco | Custo simulado | Policies |
|---|---|---|---|---:|---|
| `LocalFiletreeScanner` | local | `simulated_available` | baixo | 1-3 CKC | `POLICY_LOCAL_READ_ONLY` |
| `VaultRAGConnector` | local knowledge | `simulated_available` | baixo/medio | 2-6 CKC | `POLICY_CONTEXT_PACK_REQUIRED` |
| `DocumentUploadConnector` | uploads | `simulated_available` | medio | 2-8 CKC | `POLICY_SOURCE_INDEX_REQUIRED` |
| `ManualResearchImportConnector` | manual | `simulated_available` | medio | 2-6 CKC | `POLICY_EVIDENCE_MAP_REQUIRED` |
| `GoogleDriveConnector` | external docs | `requires_founder_approval` | medio | 6-18 CKC | `POLICY_OAUTH_APPROVAL_REQUIRED` |
| `OABOfficialSourcesConnector` | regulated source | `requires_pmo_audit` | alto | 8-24 CKC | `POLICY_HUMAN_REVIEW_FOR_REGULATED_DOMAIN` |
| `WebResearchConnector_Perplexity` | web research | `requires_pmo_audit` | alto | 20-100 CKC | `POLICY_DEEP_RESEARCH_COST_APPROVAL` |
| `ApifyPublicSocialCollector` | public collector | `requires_pmo_audit` | alto | 12-40 CKC | `POLICY_CONNECTOR_SCOPE_LIMIT_REQUIRED` |
| `YouTubeTranscriptCollector` | media transcript | `requires_founder_approval` | medio | 6-20 CKC | `POLICY_EXTERNAL_SOURCE_CITATION_REQUIRED` |
| `MetaAdsInstagramConnector` | platform/ads | `requires_pmo_audit` | alto | 12-45 CKC | `POLICY_PLATFORM_TERMS_REVIEW_REQUIRED` |
| `N8NPrototypeConnector` | prototype automation | `prototype_only` | medio/alto | 8-30 CKC | `POLICY_N8N_ACCELERATOR_NOT_CORE` |
| `ManusBootstrapImportConnector` | manual bootstrap | `manual_import_only` | alto | 5-20 CKC | `POLICY_MANUS_NOT_INFRASTRUCTURE` |

## Regras por connector

### LocalFiletreeScanner

Permitido para:

- listar arquivos;
- detectar pastas;
- identificar arquivos novos;
- preparar contexto.

Proibido para:

- mover arquivos;
- deletar arquivos;
- renumerar documentos.

### VaultRAGConnector

Permitido para:

- simular busca em memoria local;
- recuperar docs relevantes;
- compor Context Pack.

Proibido para:

- declarar resposta como canonica se contradizer docs oficiais;
- substituir PMO.

### DocumentUploadConnector

Permitido para:

- indexar fontes anexadas pelo Founder;
- montar evidence map;
- separar fontes de opinioes.

Proibido para:

- usar upload sem origem clara;
- inferir permissao de uso comercial;
- enviar PII para pesquisa externa.

### WebResearchConnector_Perplexity

Permitido para:

- deep research autorizado;
- pesquisa externa com citacoes;
- benchmark publico.

Proibido para:

- executar sem custo aprovado;
- tratar resultados como verdade sem revisao;
- coletar dados sensiveis sem policy.

### ApifyPublicSocialCollector

Permitido para:

- coletar dados publicos quando autorizado;
- benchmark de conteudo publico;
- analise de sinais de plataforma.

Proibido para:

- scraping de perfil privado;
- coleta sem base legal;
- expor actor_id, token ou provider em logs.

### N8NPrototypeConnector

n8n e permitido para:

- prototipar integracoes;
- testar webhooks;
- conectar APIs em sandbox;
- backoffice;
- alertas;
- automacoes nao criticas.

n8n nao pode:

- virar core runtime;
- controlar credito de usuario;
- processar pagamento;
- armazenar dado sensivel como sistema definitivo;
- substituir backend proprio quando houver risco juridico, financeiro ou reputacional.

### ManusBootstrapImportConnector

Manus pode:

- apoiar pesquisa manual;
- gerar insumos temporarios;
- servir como bootstrap fora do pipeline.

Manus nao pode:

- ser infraestrutura definitiva;
- aparecer como source runtime;
- substituir source real;
- gravar evento como `source_type = manus`.

## Template de declaracao

```yaml
connector:
status:
simulation_only: true
real_execution: false
input_scope:
output_expected:
cost_estimate:
risk_level:
policies:
approval_required:
blocked_actions:
```

