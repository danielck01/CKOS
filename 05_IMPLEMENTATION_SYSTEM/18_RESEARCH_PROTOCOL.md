---
title: 18 — Research Protocol
file: 18_RESEARCH_PROTOCOL.md
system_id: research_protocol
phase: 05_IMPLEMENTATION_SYSTEM
category: implementation_system
version: 1.0.0
status: draft
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - founder
  - technical
  - metacognik
approval_required:
  - founder
  - technical
  - metacognik
inputs:
  - 10_SYSTEM_RUNTIME_ARCHITECTURE.md v1.1.1
  - 11_DATA_MODEL_AND_PERSISTENCE.md v1.2.0
  - 12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md v1.1.0
  - 13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md v1.1.0
  - 17_IMPLEMENTATION_PROTOCOL.md v1.2.1
outputs:
  - research_capability_protocol
  - source_reliability_framework
  - evidence_pipeline
  - collector_research_rules
  - manus_bootstrap_deprecation_plan
related_notes:
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - ../04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md
  - ../04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md
  - ../04_PRODUCT_SYSTEM/16_NODE_CANVAS_ARCHITECTURE.md
  - 17_IMPLEMENTATION_PROTOCOL.md
  - ../ARCHITECTURE_PATCH_REPORT.md
supersedes: 18_RESEARCH_PROTOCOL_FOR_MANUS.md v1.1.0
tags:
  - research
  - evidence
  - collectors
  - rag
  - source-reliability
  - confidence-scoring
  - pipeline
  - governance
---

> **Frase central:**
> "Research in CKOS is not manual browsing. It is a governed evidence pipeline that collects, validates, normalizes, scores, stores and connects external and internal knowledge to decisions, nodes, hypotheses, artifacts and workflows."
>
> Em português: "Pesquisa no CKOS não é navegação manual. É um pipeline governado de evidências que coleta, valida, normaliza, pontua, armazena e conecta conhecimento externo e interno a decisões, nodes, hipóteses, artifacts e workflows."

> **Nota de supersessão:** Este documento substitui `18_RESEARCH_PROTOCOL_FOR_MANUS.md` v1.1.0. O protocolo anterior era restrito ao uso de Manus como ferramenta de bootstrap. Este documento define a Research Capability definitiva do CKOS.

---

# 1. Propósito

Este documento define como o CKOS realiza pesquisa com governança, rastreabilidade e evidência — como uma capacidade nativa da plataforma, não como um processo manual ou dependente de ferramentas externas ad hoc.

Research no CKOS é uma **capability sistêmica**: cada consulta de pesquisa é um evento rastreável que produz evidências estruturadas, conectadas a nodes, hipóteses, decisões e workflows no runtime. O resultado de uma pesquisa nunca é um link solto ou um resumo informal — é um conjunto de `evidence_items` com scores, fontes citadas, confidence level e rastreabilidade de volta ao agente e ao evento que a originou.

```
pesquisa ad hoc (obsoleto):  pergunta → link → pasta → decisão informal
CKOS research (alvo):        intent → pipeline → evidence_items → nodes + hypotheses + decisions + artifacts
```

Este documento cobre:
- Arquitetura do pipeline de pesquisa
- Fontes autorizadas e framework de confiabilidade
- Modelo de objeto de evidência
- Políticas, custo, privacidade e segurança
- Relação com Command Center, Node Canvas, Dashboard e Runtime
- MVP P0 da Research Capability
- Modos de falha e mitigações
- Patches sugeridos para docs de runtime

---

# 2. O que é este protocolo / O que NÃO é

**É:**
- Protocolo de Research Capability do CKOS — como pesquisa é executada, governada e rastreada como sistema.
- Definição do pipeline de evidências: coleta → normalização → scoring → síntese → armazenamento → conexão a objetos do runtime.
- Framework de confiabilidade de fonte (Tier 1–5) com critérios explícitos.
- Modelo de objeto de evidência com campos obrigatórios para persistência.
- Definição de fontes autorizadas, collectors aprovados e APIs permitidas.
- Protocolo de privacidade, custo e políticas de aprovação para research runs.
- Repositório de modos de falha conhecidos com mitigações.

**NÃO é:**
- Guia de prompts soltos para pedir pesquisa a um agente.
- Dependência de Manus ou de qualquer ferramenta externa específica.
- Lista de links ou bookmarks.
- Scraping irrestrito ou crawling não governado.
- Substituição para um sistema de BI ou analytics de produto.
- Implementação de código — este documento é especificação arquitetural.
- Definição completa de Collector Registry (ver doc futuro `26_COLLECTOR_REGISTRY.md`).

---

# 3. Princípios de pesquisa

Os 13 princípios abaixo governam toda operação de pesquisa no CKOS. Qualquer componente, agente ou workflow de pesquisa que os viole é considerado não-conformante.

**1. Evidence-first**
Nenhuma conclusão sem evidência citada. Afirmações sem fonte são hipóteses, não fatos. Hipóteses são marcadas explicitamente como tal com `confidence_score < 0.7`.

**2. Source-aware**
Toda evidência carrega metadata de fonte: origem, tipo, tier de confiabilidade, data de publicação, data de coleta. Evidência sem source_ref é inválida.

**3. Policy-controlled**
Toda pesquisa passa pela `research_policy_engine` antes de executar. Fontes sensíveis, collectors externos e queries de alto custo requerem aprovação explícita por role adequada.

**4. Tenant-isolated**
RAG privado e documentos internos são sempre consultados com `namespace = tenant_id + workspace_id` como pré-condição de busca, nunca como pós-filtro. Cross-tenant research leak é falha P0.

**5. Privacy-aware**
PII nunca é enviada para fonte externa sem policy explícita. Queries para APIs externas são sanitizadas antes do envio. Research runners rodam server-side.

**6. Citation-required**
Toda síntese referencia as `evidence_ids` dos itens que a embasam. Síntese sem citação é marcada como `unverified` e não pode ser usada como input para decisão.

**7. Confidence-scored**
Todo item de evidência tem `confidence_score` (0.0–1.0) derivado de: reliability do source tier, freshness, relevância e grau de corroboração por outras fontes. Confidence é propagado para hipóteses e sínteses.

**8. Freshness-aware**
Evidências têm `freshness_score` decrescente com o tempo. Evidências com `freshness_score < 0.4` são marcadas como stale e requerem verificação antes de uso em decisão. Contextos time-sensitive têm threshold mais alto.

**9. Bias-aware**
O sistema detecta quando evidências vêm de um único source tier, de fontes com relacionamento comercial ou de origem geográfica/idioma único. Bias warning é emitido e registrado. Metacognik é notificado para sínteses com alto risco de viés.

**10. Reproducible**
Toda pesquisa é reproduzível via `research_run_id`: mesmos parâmetros, mesmas fontes aprovadas, mesmo resultado esperado (dentro de variação de freshness). Logs de query são armazenados.

**11. Audit-ready**
Todo research run produz entrada em `audit_log` com `actor_id`, `source_event_id`, `cost_estimate`, `sources_queried`, `evidence_ids_created`.

**12. RAG-compatible**
Evidências aprovadas são indexadas no RAG privado do projeto com `namespace = tenant_id + workspace_id + project_id`. Evidências do RAG são priorizadas sobre fontes externas quando frescas e relevantes.

**13. Metacognik-auditable**
Syntheses de alta confiança (> 0.85) sobre tópicos de alto risco (decisão de produto, investimento, compliance) são enviadas para revisão do Metacognik antes de serem conectadas a decision nodes.

---

# 4. Status do Manus

**Decisão formal registrada em `ARCHITECTURE_PATCH_REPORT.md §13` e `17_IMPLEMENTATION_PROTOCOL.md §12`:**

| Aspecto | Definição |
|---------|-----------|
| Papel | Ferramenta externa temporária de bootstrap de pesquisa |
| Período de uso | Fase inicial de investigação e documentação do CKOS |
| Status no runtime | Não é agente registrado no `agent_registry` de produção |
| Status como fonte | Não é source-of-truth no runtime — outputs são importados como `evidence_items` manualmente |
| Status como infra | Não é infraestrutura CKOS — não aparece em event bus, projections ou data model |
| Substituto alvo | CKOS Research Capability nativa (este documento) |

**O que Manus pode fazer durante o período de bootstrap:**
- Pesquisa assistida de mercado, competidores, referências técnicas e acadêmicas
- Curadoria e organização de materiais de referência
- Produção de pacotes estruturados (README, CSV, shortlists, briefs) que são depois importados como evidências manuais
- Suporte à fase de documentação arquitetural (concluída)

**O que Manus NÃO deve fazer:**
- Não aparece como source em `evidence_items` do runtime com `source_type = manus` — outputs são reimportados com source real (URL, documento, API)
- Não é chamado pelo `research_intent_router` — não integra ao pipeline
- Não acessa dados de tenant ou projeto diretamente
- Não persiste resultados no event store do CKOS

**Roadmap de substituição:**

| Capacidade | Substituto CKOS |
|------------|-----------------|
| Web search geral | Perplexity via OpenRouter |
| Web crawl estruturado | Apify actors aprovados |
| Pesquisa acadêmica | PubMed, CrossRef, APIs de universidades |
| Bases internas | RAG privado por projeto |
| Documentos internos | Document parser + evidence extractor |
| Competidores / e-commerce | Collectors especializados (ver doc 26) |
| Redes sociais públicas | Collectors via APIs aprovadas (ver doc 26) |
| Síntese e raciocínio | Cognik + synthesis_generator |

Após ativação da Research Capability nativa (MVP P0), o uso de Manus entra em processo de sunset gradual — permanecendo disponível apenas como ferramenta auxiliar manual fora do pipeline.

---

# 5. Research Capability Architecture

O pipeline de pesquisa do CKOS é composto pelos seguintes componentes. Nenhum deles implementa lógica de produto própria — todos são orquestrados pelo runtime via eventos.

## 5.1 Componentes do pipeline

| Componente | Função |
|------------|--------|
| `research_intent_router` | Sub-rota do `intent_router` (doc 10 §5.2) — identifica intenções de pesquisa, mapeia para source_selector e research runner adequado |
| `research_policy_engine` | Estende o `policy_engine` (doc 12) com políticas específicas de research: fontes permitidas por role, custo máximo por run, aprovação para collectors externos |
| `source_selector` | Dado o intent e o contexto do projeto, seleciona as fontes mais relevantes (prioridade: RAG privado → documentos internos → fontes externas aprovadas) |
| `collector_runner` | Executa collectors específicos (Apify actors, APIs autorizadas) com rate limiting, cost tracking e error handling |
| `web_research_runner` | Executa queries de web search via Perplexity/OpenRouter; retorna resultados estruturados com URLs e excerpts |
| `academic_research_runner` | Executa queries em PubMed, CrossRef, Google Scholar (quando legalmente disponível) e repositórios universitários |
| `rag_retriever` | Consulta o RAG privado do projeto com `namespace = tenant_id + workspace_id + project_id` como pré-condição; retorna chunks relevantes com scores |
| `document_parser` | Parseia documentos internos uploadados (PDF, DOCX, MD, CSV) em chunks estruturados para extração de evidência |
| `source_normalizer` | Normaliza outputs de diferentes fontes em formato canônico: título, autor/org, data, URL, excerpt, tipo de fonte |
| `evidence_extractor` | Extrai claims, fatos e afirmações verificáveis do conteúdo normalizado; produz `evidence_items` candidatos |
| `source_reliability_scorer` | Atribui `source_tier` (1–5) e `reliability_score` baseado no tipo de fonte, histórico e política |
| `confidence_scorer` | Calcula `confidence_score` combinando: reliability_score + freshness_score + relevance_score + corroboração por outras fontes |
| `contradiction_detector` | Compara evidence_items candidatos com evidências existentes no projeto; detecta conflitos e emite `ContradictionDetected` |
| `gap_detector` | Analisa cobertura da pesquisa em relação às hipóteses e decisões abertas; identifica gaps de conhecimento e emite `GapDetected` |
| `synthesis_generator` | Produz síntese estruturada a partir de evidence_items selecionados; toda síntese referencia `evidence_ids` |
| `metacognik_reviewer` | Audita sínteses de alta confiança ou alto risco; pode solicitar mais fontes, rebaixar confidence ou bloquear síntese |
| `evidence_store` | Persistência de `evidence_items` com RLS por tenant; alimenta RAG privado após aprovação |
| `research_projection_engine` | Gera e mantém as projections de research para Dashboard e Node Canvas: `risk_gap_evidence`, evidência por node, coverage status |

## 5.2 Relação com runtime (doc 10)

O pipeline de pesquisa é uma extensão do fluxo canônico do runtime, não um sistema paralelo:

```
intent_router (doc 10 §5.2)
  └── research_intent_router     ← sub-rota especializada
        └── research_policy_engine
              └── source_selector → [runners]
                    └── evidence_store → ui_projection_engine
```

Nenhum componente de research escreve diretamente em tabelas de domínio sem passar pelo event store.

---

# 6. Research Flow

O fluxo canônico de uma pesquisa no CKOS, do início ao output:

```
1. User/Agent submete intenção de pesquisa
   (ex: "/research benchmarks de conversão para e-commerce B2B")

2. research_intent_router
   → identifica intent_type: query.research.market
   → emite: ResearchIntentSubmitted

3. research_policy_engine
   → verifica: role do ator, fontes necessárias, custo estimado, aprovação necessária?
   → se aprovado: emite ResearchApproved
   → se custo alto ou fonte sensível: emite ApprovalRequested → pausa

4. source_selector
   → prioridade: RAG privado → documentos internos → web → collectors → academic
   → emite: SourcesSelected(source_ids[])

5. Runners em paralelo (conforme fontes selecionadas):
   ├── rag_retriever → chunks do RAG interno
   ├── web_research_runner → Perplexity/OpenRouter
   ├── collector_runner → Apify actor selecionado
   └── academic_research_runner → PubMed / CrossRef

6. source_normalizer
   → normaliza todos os outputs para formato canônico
   → emite: SourceNormalized(source_id, normalized_data)

7. evidence_extractor
   → extrai claims e fatos verificáveis
   → cria evidence_item candidatos
   → emite: EvidenceExtracted(evidence_ids[])

8. source_reliability_scorer
   → atribui source_tier (1–5) e reliability_score a cada evidence_item
   → emite: SourceScored(evidence_id, tier, reliability_score)

9. confidence_scorer
   → calcula confidence_score = f(reliability, freshness, relevance, corroboration)
   → atualiza evidence_items

10. contradiction_detector
    → compara com evidências existentes no projeto
    → se conflito: emite ContradictionDetected(evidence_id_a, evidence_id_b, description)
    → não força resolução — registra e expõe

11. gap_detector
    → analisa cobertura em relação às hipóteses e decisões abertas
    → emite GapDetected(description, related_hypothesis_ids[]) quando cobertura insuficiente

12. synthesis_generator
    → produz síntese com evidence_ids citados
    → emite SynthesisGenerated(synthesis_id, evidence_ids[], confidence_score)

13. metacognik_reviewer (condicional)
    → ativado quando: confidence > 0.85 + risco alto, OU contradição presente, OU fonte Tier 4/5 dominante
    → pode: aprovar síntese | solicitar mais fontes | rebaixar confidence | bloquear

14. evidence_store
    → persiste evidence_items aprovados com RLS + tenant_id
    → indexa no RAG privado do projeto
    → emite: ResearchCompleted(research_run_id, evidence_count, synthesis_id)

15. research_projection_engine
    → atualiza projeções: risk_gap_evidence, node_health, canvas_graph
    → SSE push para Dashboard e Node Canvas

16. Resultado visível:
    → Command Center: Nick explica síntese + cita fontes
    → Node Canvas: novos evidence_nodes + hypothesis_nodes se criados
    → Dashboard: widget Risk/Gap/Evidence Monitor atualizado
```

---

# 7. Source Types

Fontes organizadas por categoria. A seleção de fonte é governada por `research_policy_engine` com base em role, contexto e custo.

## 7.1 Fontes internas (prioridade máxima)

| Fonte | Descrição | Disponível no P0 |
|-------|-----------|:---:|
| **Private RAG** | Base vetorial privada do projeto: evidências aprovadas anteriores, documentos indexados | ✅ |
| **Uploaded documents** | PDFs, DOCXs, MDs uploadados pelo usuário ou por agente | ✅ |
| **Internal CKOS artifacts** | Artifacts gerados por runs anteriores (briefings, research reports, proposals) | ✅ |
| **Command history** | Histórico de comandos e respostas com contexto do projeto | ✅ |

## 7.2 Web search controlado

| Fonte | Descrição | Disponível no P0 |
|-------|-----------|:---:|
| **Perplexity via OpenRouter** | Web search com citações estruturadas; resposta com sources rastreáveis | ✅ |
| **Web search geral** | Search engines públicos via API autorizada | Parcial |

## 7.3 Collectors especializados (Apify e equivalentes)

| Fonte | Descrição | Disponível no P0 |
|-------|-----------|:---:|
| **Apify actors aprovados** | Collectors configurados para domínios específicos; lista de actors aprovados definida em doc 26 | Parcial (≤5 actors) |
| **Ecommerce collectors** | Produtos, preços, reviews de plataformas públicas | ⏳ P0+ |
| **Ad libraries** | Meta Ad Library, Google Ads Transparency quando permitido | ⏳ P0+ |
| **Social platforms via APIs aprovadas** | LinkedIn, Reddit, Twitter/X via APIs oficiais onde disponíveis | ⏳ P0+ |

## 7.4 Fontes acadêmicas

| Fonte | Descrição | Disponível no P0 |
|-------|-----------|:---:|
| **PubMed** | Literatura científica biomédica; via API NCBI | ✅ (quando relevante) |
| **CrossRef** | DOIs, metadados de artigos científicos | ✅ |
| **Google Scholar** | Quando legalmente disponível via API ou Apify actor aprovado | ⏳ P0+ |
| **Repositórios universitários** | Teses, dissertações, working papers públicos | ⏳ P0+ |
| **arXiv / SSRN** | Preprints de tecnologia, economia, ciências sociais | ✅ (quando relevante) |

## 7.5 Fontes institucionais e de mercado

| Fonte | Descrição | Disponível no P0 |
|-------|-----------|:---:|
| **Government sources** | Sites oficiais de governo, dados públicos regulatórios | ✅ |
| **Public datasets** | Data.gov, IBGE, Eurostat, World Bank Open Data | ✅ |
| **Competitor public websites** | Conteúdo público de sites de competidores | ✅ |
| **Industry reports (free tier)** | Gartner, McKinsey, Forrester quando publicamente acessíveis | ✅ |
| **APIs autorizadas** | Qualquer API com contrato e token gerido via `secret_refs` | Por aprovação |

---

# 8. Source Reliability Framework

Toda fonte recebe um `source_tier` no momento da coleta. O tier determina o peso da fonte na síntese, a necessidade de validação e o risco de viés.

## 8.1 Tabela de tiers

| Tier | Classificação | Exemplos |
|------|---------------|----------|
| **1** | Fonte primária / oficial / acadêmica revisada por pares / legal / governamental | PubMed, DOI revisado, legislação oficial, dados regulatórios, patentes, teses aprovadas |
| **2** | Fonte de indústria reconhecida | Gartner, McKinsey, IDC, relatórios de bancos centrais, documentação técnica oficial (RFC, W3C) |
| **3** | Mídia reputada / relatórios de mercado | TechCrunch, Reuters, The Economist, Nielsen, Statista (com metodologia), blogs de referência com autoria |
| **4** | Sinal social / conteúdo gerado por usuário | Reviews, comentários públicos, posts em redes sociais, fóruns, Reddit, Product Hunt |
| **5** | Fonte fraca / não verificada / baixa confiança | Sites sem autoria, conteúdo anônimo, dados sem data, fontes com conflito de interesse não declarado |

## 8.2 Critérios por tier

**Tier 1 — Fonte primária:**
- Quando usar: claims factuais críticos, base científica, compliance, regulação, dados históricos verificados
- Quando não usar: previsões de mercado sem metodologia declarada
- Peso na síntese: alto (0.8–1.0)
- Validação necessária: nenhuma adicional — source é aceita por padrão
- Risco de viés: baixo, mas atenção a limitações declaradas pelos próprios autores

**Tier 2 — Indústria reconhecida:**
- Quando usar: benchmarks de mercado, análises setoriais, projeções com metodologia
- Quando não usar: como única fonte para decisão de produto sem validação interna
- Peso na síntese: médio-alto (0.65–0.85)
- Validação necessária: cruzar com pelo menos 1 fonte Tier 1 ou outro Tier 2
- Risco de viés: médio — empresas de análise têm clientes corporativos

**Tier 3 — Mídia / relatórios:**
- Quando usar: contexto de mercado, tendências, opinião especializada qualificada
- Quando não usar: como evidência primária de fato científico ou dado regulatório
- Peso na síntese: médio (0.45–0.65)
- Validação necessária: cruzar com Tier 1 ou 2 para claims relevantes
- Risco de viés: médio-alto — linha editorial, patrocínio, click economy

**Tier 4 — Sinal social / UGC:**
- Quando usar: sentimento de mercado, percepção de usuário, feedback qualitativo, sinais de demanda
- Quando não usar: como base para decisão estratégica isolada
- Peso na síntese: baixo-médio (0.2–0.45)
- Validação necessária: volume mínimo de N amostras, distribuição de fonte, data range
- Risco de viés: alto — seleção de amostra, bots, viés de representatividade

**Tier 5 — Fonte fraca:**
- Quando usar: sinalização inicial para investigação — nunca como evidência final
- Quando não usar: decisões, hipóteses com confidence > 0.5, sínteses sem outra corroboração
- Peso na síntese: mínimo (0.0–0.2); não usado em sínteses críticas
- Validação necessária: obrigatória antes de qualquer uso
- Risco de viés: muito alto — pode ser desinformação intencional

## 8.3 Regra de síntese mínima

Para síntese com `confidence_score ≥ 0.7`, o corpus de evidências deve incluir:
- Ao menos 1 fonte Tier 1 ou 2, **OU**
- Ao menos 3 fontes Tier 3 concordantes **sem** source em Tier 5 dominando (> 50% das citações)

Síntese que não atende a regra mínima recebe `confidence_score ≤ 0.5` automaticamente.

---

# 9. Evidence Object Model

Uma evidência (`evidence_item`) é o átomo do sistema de pesquisa do CKOS. É um objeto persistido, rastreável, pontuado e conectável a outros objetos do runtime.

## 9.1 Schema canônico

```
evidence_items (
  id                   uuid pk,
  tenant_id            uuid NOT NULL,          -- RLS; pré-condição de toda query
  org_id               uuid fk→organizations [RLS],
  workspace_id         uuid fk→workspaces,
  project_id           uuid fk→projects,

  -- Fonte
  source_type          enum(
                         private_rag | uploaded_document | ckos_artifact |
                         web_search | perplexity | apify_collector |
                         pubmed | crossref | google_scholar | arxiv |
                         government | public_dataset | competitor_website |
                         industry_report | authorized_api | manual_import
                       ) NOT NULL,
  source_tier          smallint NOT NULL,       -- 1–5 conforme §8
  source_url_or_ref    text,                    -- URL, DOI, path interno, API ref
  source_collector_id  text,                    -- ID do Apify actor ou collector usado
  title                text,
  author_or_org        text,
  published_at         timestamptz,             -- data de publicação da fonte
  retrieved_at         timestamptz NOT NULL,    -- quando foi coletada pelo CKOS

  -- Scores
  freshness_score      numeric(3,2) NOT NULL,   -- 0.00–1.00, decrescente com tempo
  reliability_score    numeric(3,2) NOT NULL,   -- 0.00–1.00, derivado do source_tier
  relevance_score      numeric(3,2) NOT NULL,   -- 0.00–1.00, calculado vs. research intent
  confidence_score     numeric(3,2) NOT NULL,   -- 0.00–1.00, agregado dos três acima + corroboração

  -- Conteúdo
  claim                text NOT NULL,           -- afirmação verificável extraída
  excerpt              text,                    -- trecho original da fonte
  normalized_summary   text,                    -- resumo normalizado pelo evidence_extractor
  language             text default 'pt-BR',

  -- Flags de qualidade
  is_verified          boolean default false,
  has_contradiction    boolean default false,
  is_stale             boolean default false,   -- true quando freshness_score < threshold
  bias_warning         boolean default false,
  metacognik_reviewed  boolean default false,

  -- Rastreabilidade
  research_run_id      uuid fk→research_runs,
  created_by_agent_id  text,                    -- agent que executou o run
  source_event_id      uuid fk→events,         -- evento que originou a coleta
  audit_log_id         uuid fk→audit_log,

  -- Conexões a objetos do runtime
  related_project_id   uuid fk→projects,
  related_node_id      uuid fk→nodes,
  related_hypothesis_id uuid,                  -- FK para tabela de hipóteses (patch sugerido §27)
  related_decision_id  uuid fk→nodes WHERE node_type='decision',
  related_artifact_id  uuid fk→artifact_items,
  related_evidence_ids uuid[],                 -- evidências que corroboram
  contradiction_ids    uuid[],                 -- evidências que contradizem

  -- Meta
  metadata             jsonb,                  -- dados extras do collector
  created_at           timestamptz NOT NULL default now(),
  updated_at           timestamptz,
  archived_at          timestamptz             -- soft-delete; nunca DELETE
)
```

**Indexes obrigatórios:**
```
idx_evidence_project_confidence   ON evidence_items(project_id, confidence_score DESC)
idx_evidence_tenant_type          ON evidence_items(tenant_id, source_type, source_tier)
idx_evidence_node_link            ON evidence_items(related_node_id) WHERE related_node_id IS NOT NULL
idx_evidence_stale                ON evidence_items(project_id, is_stale) WHERE is_stale = true
```

**RLS:** `USING (tenant_id = current_setting('app.tenant_id')::uuid)`

## 9.2 Tabela auxiliar: research_runs

```
research_runs (
  id               uuid pk,
  tenant_id        uuid NOT NULL,
  org_id           uuid fk,
  workspace_id     uuid fk,
  project_id       uuid fk,
  research_intent  text NOT NULL,               -- intenção original em linguagem natural
  intent_type      text,                        -- ex: query.research.market
  status           enum(
                     requested | approved | queued | collecting |
                     normalizing | extracting_evidence | scoring_sources |
                     detecting_contradictions | synthesizing |
                     metacognik_review | completed | failed |
                     blocked_by_policy | blocked_by_cost | needs_more_sources
                   ),
  sources_selected text[],
  evidence_count   integer default 0,
  synthesis_id     uuid,
  cost_estimate    numeric,
  cost_actual      numeric,
  policy_approved_by text,
  started_at       timestamptz,
  completed_at     timestamptz,
  source_event_id  uuid fk→events,
  audit_log_id     uuid fk→audit_log,
  metadata         jsonb,
  created_at       timestamptz default now()
)
```

> **Patch sugerido P18-1:** Tabela `research_runs` precisa ser adicionada ao doc 11 v1.3.x antes da implementação do Research Pipeline. Ver §27.

---

# 10. Research Outputs

Uma pesquisa pode gerar os seguintes tipos de output, todos conectados ao runtime via eventos:

| Output | Tipo de objeto CKOS | Criação via |
|--------|--------------------|-------------|
| `evidence_items` | evidence_items table | research pipeline → event → runtime |
| Hipóteses | node (type: Hypothesis) | synthesis_generator → NodeCreated event |
| Gaps de conhecimento | node (type: Gap) | gap_detector → NodeCreated event |
| Riscos identificados | node (type: Risk) | gap_detector / evidence_extractor → NodeCreated event |
| Insights sintetizados | artifact_item (type: research_insight) | synthesis_generator → ArtifactCreated event |
| Benchmark summaries | artifact_item (type: benchmark_summary) | synthesis_generator → ArtifactCreated event |
| Competitor profiles | artifact_item (type: competitor_profile) | synthesis_generator → ArtifactCreated event |
| Academic summaries | artifact_item (type: academic_summary) | academic_research_runner → ArtifactCreated event |
| Source maps | artifact_item (type: source_map) | research_projection_engine → ArtifactCreated event |
| Node suggestions | sugestão no Command Center | synthesis_generator → intent response |
| Workflow suggestions | sugestão no Command Center | synthesis_generator → intent response |
| Proposal inputs | evidence links para proposal workflow | manual ou automático via workflow |
| ROI assumptions | evidence links para roi_assumptions | ver doc 21_ROI_ARCHITECTURE (futuro) |

**Regra crítica:** Nenhum output de pesquisa é diretamente aplicado como decisão. Todo output é evidência ou sugestão — a decisão é sempre do humano ou passa por approval gate conforme `autonomy_level` do agente.

---

# 11. Relação com Command Center

O Command Center (doc 15) é a superfície de entrada de intenção de pesquisa — não é um motor de pesquisa.

**O que o Command Center faz:**
- Recebe intenção de pesquisa do usuário via input natural ou slash command (`/research`, `/competitors`, `/evidence`, `/memory`)
- Encaminha para `intent_router` → `research_intent_router`
- Exibe resultado da síntese via Nick após conclusão do pipeline
- Cita fontes e confidence score na resposta

**O que o Command Center NÃO faz:**
- Não executa pesquisa diretamente
- Não acessa fontes externas — toda pesquisa é server-side
- Não persiste resultados — é UI de entrada e de exibição

**Fluxo:**
```
CommandBar: "/research benchmarks de conversão SaaS B2B"
  → IntentSubmitted (intent_type: query.research.market)
  → research_intent_router
  → research_policy_engine (verifica permissão + custo)
  → source_selector (seleciona: Perplexity + RAG interno)
  → runners em paralelo
  → evidence pipeline completo
  → ResearchCompleted event
  → command_center_context projection atualizada
  → SSE push
  → Nick exibe síntese com citações e confidence score
```

**Slash commands de pesquisa (subset do §5.4 do doc 15):**

| Comando | Intent type | Fontes prioritárias |
|---------|-------------|---------------------|
| `/research [tema]` | `query.research.*` | RAG + Perplexity + academic |
| `/competitors [vertical]` | `query.research.market` | Apify + competitor websites + Perplexity |
| `/evidence [claim]` | `query.research.evidence` | RAG + academic |
| `/memory [contexto]` | `query.memory.*` | RAG interno apenas |
| `/diagnosis [situação]` | `action.strategy.diagnosis` | RAG + Perplexity + academic |

---

# 12. Relação com Node Canvas

O Node Canvas (doc 16) é a superfície visual onde evidências e outputs de pesquisa se tornam objetos observáveis e conectáveis.

**Outputs de pesquisa que aparecem no canvas:**

| Tipo de node | Quando aparece | Criado por |
|-------------|----------------|------------|
| Research node | Run de pesquisa iniciado | `research_intent_router` → NodeCreated event |
| Evidence node | Evidence item com `confidence_score ≥ 0.6` | `evidence_store` → NodeCreated event |
| Hypothesis node | Síntese gera hipótese verificável | `synthesis_generator` → NodeCreated event |
| Risk node | `gap_detector` ou `evidence_extractor` identifica risco | pipeline → NodeCreated event |
| Gap node | `gap_detector` identifica ausência de cobertura | pipeline → NodeCreated event |
| Benchmark node | Benchmark summary gerado | `synthesis_generator` → NodeCreated event |
| Competitor node | Competitor profile gerado | `synthesis_generator` → NodeCreated event |
| ROI Assumption node | Evidence alimenta assumption de ROI | manual link + event |

**Regra crítica:** Toda criação de node passa pelo runtime via evento — o canvas não cria nodes diretamente. O usuário pode "aceitar" uma sugestão de node no canvas → ação emite evento → runtime cria.

**Side panel de evidence node:**
- Claim principal
- Source tier + reliability_score + freshness_score + confidence_score
- Excerpt original
- URL / DOI / ref
- Contradições linkadas (com `contradiction_ids`)
- Hipóteses que dependem desta evidência
- Metacognik review status

---

# 13. Relação com Project Dashboard

O Project Dashboard (doc 14) exibe o estado agregado da pesquisa do projeto via widget **Risk/Gap/Evidence Monitor** (widget #10, projeção `risk_gap_evidence_projection`).

**O que o dashboard exibe:**

| Informação | Source projection | Atualização |
|------------|-------------------|-------------|
| Cobertura de evidências por área de decisão | `risk_gap_evidence` | Polling 30s |
| Gaps de conhecimento abertos | `risk_gap_evidence` | Polling 30s |
| Riscos identificados por pesquisa | `risk_gap_evidence` | Polling 30s |
| Collector status (em execução / falha) | `agent_activity` | SSE |
| Freshness score médio das evidências | `risk_gap_evidence` | Polling 30s |
| Contradições não resolvidas | `risk_gap_evidence` | Polling 30s |
| Último research run: status e custo | `cost_credit` + `agent_activity` | SSE + polling |

**O que o dashboard NÃO faz:**
- Não exibe conteúdo raw de evidências (isso é side panel do Node Canvas)
- Não executa pesquisa — aciona Command Center quando usuário clica em "pesquisar"

---

# 14. Relação com ROI

Pesquisa é insumo crítico para o sistema de ROI (doc futuro `21_ROI_ARCHITECTURE.md`). Evidências de pesquisa alimentam:

| Input de ROI | Fonte de evidência | Tipo de fonte preferencial |
|-------------|-------------------|---------------------------|
| Market size assumptions | Benchmarks de mercado | Tier 1–2 |
| Conversion rate benchmarks | Estudos de indústria, competitors | Tier 2–3 |
| Cost avoidance estimates | Artigos acadêmicos, casos de indústria | Tier 1–2 |
| Strategic ROI hypotheses | Análise de mercado + competitors | Tier 2–3 |
| Brand ROI signals | Pesquisa de percepção, social signals | Tier 3–4 |
| Content ROI data | Benchmarks de performance de conteúdo | Tier 2–3 |
| Learning ROI | Literatura acadêmica sobre aprendizado organizacional | Tier 1 |

**Regra:** Toda `roi_assumption` deve referenciar ao menos um `evidence_id`. ROI assumption sem evidência é marcada como `unverified` e não pode ser usada em projeção apresentada ao cliente.

**Implementação de ROI Architecture bloqueada** até aprovação do doc `21_ROI_ARCHITECTURE.md`.

---

# 15. Relação com Feedback e Suporte

Feedback de usuário e tickets de suporte podem virar pesquisa — e pesquisa pode virar melhoria de produto.

**Feedback → Research:**
```
feedback_item (cliente reporta dúvida recorrente)
  → feedback_pattern_detector identifica tema
  → research_intent_router ativado: query.research.support
  → RAG interno consultado (documentação existente)
  → gap identificado: documentação insuficiente
  → GapDetected event → Gap node criado
  → workflow de melhoria sugerido
```

**Support → Research:**
```
support_ticket (fricção recorrente com feature X)
  → friction_signal detectado
  → research run: benchmark de UX de feature similar em competidores
  → evidence_items coletados
  → Hypothesis node: "feature X tem UX inferior ao mercado em 3 pontos"
  → decision node sugerido para revisão de produto
```

**Research → Feedback loop:**
Evidências de pesquisa podem revelar que produto atual está abaixo do benchmark de mercado — alimentando proativamente a queue de decisões sem esperar feedback explícito do usuário.

**Implementação de Feedback e Support Systems bloqueada** até aprovação dos docs `22_FEEDBACK_SYSTEM_ARCHITECTURE.md` e `23_SUPPORT_SYSTEM_ARCHITECTURE.md`.

---

# 16. Research Policies

A `research_policy_engine` aplica as seguintes políticas antes de qualquer run:

| Situação | Policy |
|----------|--------|
| Pesquisa simples no RAG interno | Automática — sem aprovação, custo cobrado do projeto |
| Web search via Perplexity (baixo custo) | Automática para `project_member+`; limite de N queries/dia por projeto |
| Collector externo (Apify) | Requer aprovação de `project_lead+` + custo pré-reservado |
| Fonte sensível (dados pessoais, financeiros, saúde) | Requer aprovação de `admin+` + registro em `audit_log` |
| Pesquisa acadêmica completa (PubMed, CrossRef) | Automática para `contributor+`; sem limite de custo pré-definido além do plano |
| Custo estimado > threshold do projeto | Requer aprovação + `credit_reservation` antes da execução |
| Pesquisa com PII potencial na query | Sanitização automática obrigatória + log de sanitização |
| RAG com dados classificados como `confidential` | RLS aplica; usuário com role `viewer` não acessa |
| Research run falhado 3× seguidas no mesmo collector | Collector suspenso automaticamente + Metacognik alertado |
| Síntese baseada majoritariamente em Tier 4/5 | Metacognik review obrigatório antes de uso |

**Regra geral:** RAG interno e documentos do projeto são sempre a primeira fonte consultada. Fontes externas são acionadas apenas quando RAG não tem cobertura suficiente ou quando a intenção é explicitamente externa (ex: competidores, mercado).

---

# 17. Privacidade e Segurança

Research é um vetor de risco específico porque envolve envio de contexto para sistemas externos. As seguintes regras são não-negociáveis:

**R1 — Tenant isolation absoluta:**
RAG é sempre consultado com `namespace = tenant_id + workspace_id + project_id`. Nunca cross-tenant. Tenant leak em research é falha P0.

**R2 — PII nunca para o exterior:**
Queries enviadas para Perplexity, Apify, PubMed ou qualquer API externa passam por `pii_sanitizer` antes do envio. PII detectada é substituída por placeholder genérico.

**R3 — Tokens geridos via secret_refs:**
API keys de Perplexity, Apify, PubMed, CrossRef são armazenadas como `secret_refs` — nunca em tabelas normais, nunca em logs.

**R4 — Runners server-side only:**
Nenhum runner de pesquisa executa no cliente (browser/frontend). Toda chamada a API externa é feita server-side pelo runtime.

**R5 — Logs sem segredo:**
Logs de research runs não contêm conteúdo de credenciais, PII não sanitizada ou dados de tenant cruzado.

**R6 — Dados sensíveis mascarados:**
Excerpts de fontes com `data_classification ≥ confidential` são mascarados na projection antes de serem enviados por SSE para usuários sem role adequada.

**R7 — Collector authorization:**
Nenhum Apify actor ou collector externo é executado sem estar listado na `collectors_allowlist` (ver doc futuro `26_COLLECTOR_REGISTRY.md`). Collector não autorizado → `ResearchBlocked` event.

**R8 — Legal compliance:**
Coleta de dados de sites, redes sociais e e-commerces respeita `robots.txt`, termos de serviço e legislação aplicável (LGPD, GDPR, CCPA). Violação detectada → collector desativado + Metacognik alert + Founder notificado.

---

# 18. Custo e Créditos

Pesquisa tem custo — tokens de LLM, chamadas de API, execuções de collector. O sistema de custo segue o framework de doc 13 e doc 11 §33.

**Custo por tipo de operação:**

| Operação | Unidade de custo | Aprovação necessária |
|----------|-----------------|---------------------|
| RAG retrieval (interno) | Embedding query (baixo) | Automática |
| Document parsing (upload) | Por página/chunk | Automática |
| Perplexity/OpenRouter query | Por query + tokens de resposta | Automática (abaixo do threshold) |
| Apify actor run | Por run + resultado | `project_lead+` aprovação |
| PubMed / CrossRef API | Por query (geralmente gratuito) | Automática |
| Model call (synthesis) | Por tokens de input + output | Automática (abaixo do threshold) |
| Full research run (todos acima) | Agregado | `credit_reservation` antes de executar |

**Regras de custo:**
- `credit_reservation` é feita antes de qualquer research run com custo estimado > 0 — previne saldo negativo
- Run bloqueado por crédito insuficiente emite `ResearchBlocked(reason: insufficient_credits)` — não falha silenciosamente
- Fallback barato: quando custo estimado excede threshold, `source_selector` sugere alternativa mais barata (ex: RAG apenas) e aguarda aprovação
- Research caro (ex: Apify run + síntese completa) emite `ApprovalRequested` antes de executar

**Cost tracking:**
Todo research run registra custo em `cost_ledger` (doc 13) com `cost_type = research_run` e rastreabilidade ao `research_run_id`.

---

# 19. Freshness e Recência

A validade temporal de uma evidência é tão importante quanto sua confiabilidade de fonte.

**freshness_score** decai segundo a fórmula:
```
freshness_score = max(0, 1 - (days_since_retrieval / freshness_ttl_days))
```

**TTL por fonte e contexto:**

| Contexto / tipo de dado | TTL (dias) | Threshold de stale |
|------------------------|:-----------:|:-----------------:|
| Dados de mercado em tempo real (pricing, ads) | 7 | 0.5 |
| Benchmarks de conversão e performance | 90 | 0.5 |
| Análises de competidores | 30 | 0.5 |
| Literatura acadêmica (fatos estabelecidos) | 1825 (5 anos) | 0.2 |
| Legislação e regulação | 365 | 0.4 |
| Dados históricos (imutáveis por natureza) | ∞ | N/A |
| RAG interno (documentos do projeto) | 180 | 0.3 |
| Social signals / sentimento | 14 | 0.6 |

**Quando re-pesquisar:**
- Evidence com `freshness_score < threshold` e referenciada em decisão aberta → `research_intent_router` sugere re-run
- Usuário pode forçar re-run via `/research --refresh`
- Re-run não sobrescreve evidências antigas — cria nova versão; evidência antiga é arquivada com `archived_at`

**Regra de expiração:**
Evidências expiradas (`is_stale = true`) não são automaticamente removidas do canvas ou da síntese — são marcadas visualmente e o usuário decide se quer atualizar.

---

# 20. Contradição e Viés

Evidências contraditórias são esperadas — especialmente em pesquisa de mercado, tendências e áreas em evolução. O sistema não força consenso falso.

**Detecção de contradição:**

```
ContradictionDetected quando:
  evidence_item_A.claim contradicts evidence_item_B.claim
  AND ambos têm confidence_score > 0.5
  AND related ao mesmo projeto/node/hipótese
```

**O que acontece após detecção:**
1. Ambas as evidências recebem `has_contradiction = true`
2. `contradiction_ids` de cada uma aponta para a outra
3. `ContradictionDetected` event emitido com descrição
4. Hipóteses ou nodes que dependem de qualquer uma das evidências recebem badge visual de contradição
5. Metacognik é notificado quando: confidence alto + contradição não resolvida há mais de N horas
6. Síntese **não é gerada** automaticamente quando contradição não resolvida está presente — aguarda input humano ou mais fontes

**Resolução de contradição:**
- Usuário pode: marcar uma como "preferida" + registrar decisão → `ConflictResolved` event
- Usuário pode: solicitar mais pesquisa → novo research run focado na contradição
- Usuário pode: aceitar ambas como "perspectivas diferentes" → ambas mantidas com flag `competing_view`

**Detecção de viés:**
`bias_warning = true` quando:
- ≥ 70% das evidências vêm do mesmo source tier
- ≥ 60% das evidências vêm do mesmo país/idioma (para pesquisa com escopo global)
- Todas as fontes têm relacionamento comercial com o mesmo vendor
- Evidências positivas superam negativas por ratio > 10:1 sem justificativa de scope

---

# 21. Protocolo de Pesquisa Acadêmica

Pesquisa acadêmica tem regras mais rígidas — a credibilidade de conclusões científicas depende de metodologia, não apenas de fonte.

**Fontes primárias:**
- PubMed (ciências da saúde, ciências do comportamento)
- CrossRef / DOI (qualquer área com peer review)
- arXiv (computação, física, matemática, economia — preprints)
- SSRN (direito, finanças, ciências sociais — preprints)
- Repositórios institucionais de universidades

**Regras obrigatórias para evidência acadêmica:**

| Regra | Descrição |
|-------|-----------|
| Não extrapolar ciência | O claim extraído deve estar dentro das conclusões explícitas do estudo — não inferido além |
| Separar evidência de hipótese | Estudos observacionais → `confidence_score ≤ 0.7`; RCTs e meta-análises → até 0.9 |
| Citar limitações | `normalized_summary` deve incluir limitações declaradas pelos autores |
| Marcar preprint | Fontes sem peer review recebem flag `is_preprint = true` e `confidence_score` reduzido em 0.1 |
| Não usar para compliance | Evidência acadêmica não substitui consulta jurídica ou regulatória |
| Data de publicação obrigatória | `published_at` é campo obrigatório para fontes acadêmicas |
| Grau de generalização | Estudos com N < 100 ou população específica têm `relevance_score` ajustado pelo `academic_research_runner` |

**academic_research_runner — comportamento:**
- Query estruturada: term + MeSH (PubMed) ou campo:valor (CrossRef)
- Retorna: título, autores, abstract, DOI, data, journal, tipo de estudo
- Não retorna texto completo de artigos pagos — retorna abstract + DOI para acesso manual
- Filtra por data, tipo de estudo e relevance score mínimo configurável

---

# 22. Protocolo de Pesquisa de Mercado e Competidores

Pesquisa de mercado e competidores é o uso mais frequente no contexto de projetos de estratégia e marketing.

**Fontes e métodos aprovados:**

| Dado | Fonte | Método |
|------|-------|--------|
| Pricing de competidor | Website público do competidor | Apify actor ou web_research_runner |
| Features de produto | Website, changelog, app stores | Apify actor + document_parser |
| Reviews de usuários | G2, Capterra, Trustpilot, App Store (público) | Apify actor aprovado |
| Anúncios ativos | Meta Ad Library, Google Ads Transparency | API oficial ou Apify actor aprovado |
| Social presence | Métricas públicas de seguidores, engagement | APIs oficiais quando disponíveis |
| Preços de e-commerce | Páginas de produto públicas | Apify actor aprovado |
| Vagas de emprego (como sinal estratégico) | LinkedIn, Indeed (públicos) | Apify actor aprovado |
| Benchmarks de categoria | Gartner, G2, SimilarWeb (tier público) | web_research_runner |

**Regras específicas:**
- Nunca coletar dados que exijam login no sistema do competidor
- Nunca simular usuário real para contornar rate limiting
- Ad library: apenas anúncios que a plataforma torna publicamente disponíveis
- Social: via APIs oficiais — nunca scraping de conteúdo de perfis privados
- Collector deve respeitar `robots.txt` e `rate_limit` configurado por domínio
- Todo dado de competidor é marcado com `source_type = competitor_website` e `retrieved_at` para freshness tracking

**Frequency:**
Dados de competidores têm TTL curto (7–30 dias conforme tipo). `research_projection_engine` sinaliza quando competitor profile está stale e o projeto tem decisões abertas dependendo de benchmarks de mercado.

---

# 23. State Machines de Research

O ciclo de vida de um research run é governado por state machine para garantir que nenhum passo seja pulado ou executado fora de ordem.

```
requested
  ↓ (policy check)
approved ──→ [blocked_by_policy] (se policy deny)
  ↓
queued
  ↓ (credit reservation)
collecting ──→ [blocked_by_cost] (se crédito insuficiente)
  ↓ (runners em paralelo)
normalizing
  ↓
extracting_evidence
  ↓
scoring_sources
  ↓
detecting_contradictions
  ↓
synthesizing
  ↓ (se metacognik_review necessário)
metacognik_review ──→ [needs_more_sources] (se cobertura insuficiente)
  ↓
completed
```

**Estados terminais:** `completed | failed | blocked_by_policy | blocked_by_cost`

**Estados de retenção:** `needs_more_sources` — run pausado aguardando novas fontes; pode ser retomado com `/research --extend`

**Transições:**
- Toda transição de estado emite evento correspondente (ver §24)
- Toda transição é validada pelo `research_policy_engine` para estados que envolvem recursos externos
- Rollback: se falha em `collecting`, evidências já coletadas são preservadas; run pode ser retomado do ponto de falha

---

# 24. Research Events

Todos os eventos abaixo são emitidos para o event bus do runtime (doc 10 §5.3). Nenhum componente de research executa ação sem emitir evento correspondente.

| Evento | Emitido por | Payload principal |
|--------|-------------|-------------------|
| `ResearchIntentSubmitted` | research_intent_router | intent_type, actor_id, project_id, research_query |
| `ResearchApproved` | research_policy_engine | research_run_id, approved_by, cost_estimate |
| `ResearchBlocked` | research_policy_engine | reason (policy\|cost\|collector_not_authorized) |
| `SourcesSelected` | source_selector | source_ids[], estimated_cost |
| `CollectorStarted` | collector_runner | collector_id, source_type, research_run_id |
| `SourceCollected` | [qualquer runner] | source_ref, source_type, raw_data_size |
| `SourceCollectionFailed` | [qualquer runner] | collector_id, error, retry_count |
| `SourceNormalized` | source_normalizer | source_id, normalized_format |
| `EvidenceExtracted` | evidence_extractor | evidence_ids[], claim_count |
| `SourceScored` | source_reliability_scorer | evidence_id, tier, reliability_score |
| `ContradictionDetected` | contradiction_detector | evidence_id_a, evidence_id_b, description |
| `GapDetected` | gap_detector | description, related_hypothesis_ids[], related_node_ids[] |
| `SynthesisGenerated` | synthesis_generator | synthesis_id, evidence_ids[], confidence_score |
| `MetacognikReviewRequested` | synthesis_generator | synthesis_id, reason |
| `MetacognikReviewCompleted` | metacognik_reviewer | synthesis_id, outcome (approved\|needs_more\|blocked) |
| `ResearchCompleted` | evidence_store | research_run_id, evidence_count, synthesis_id, cost_actual |
| `ResearchFailed` | [qualquer componente] | research_run_id, stage, error |
| `EvidenceArchived` | evidence_store | evidence_id, reason (stale\|superseded\|user_action) |
| `BiasWarningEmitted` | confidence_scorer | research_run_id, bias_type, description |
| `ConflictResolved` | [user action via runtime] | evidence_id_a, evidence_id_b, resolution_type |

---

# 25. MVP P0

O MVP P0 da Research Capability entrega o pipeline básico operacional com fontes essenciais e governança mínima.

**Dentro do MVP P0:**

| Componente / Feature | Prioridade |
|---------------------|------------|
| `rag_retriever` — RAG privado por projeto | P0 obrigatório |
| `document_parser` — PDFs e DOCXs uploadados | P0 obrigatório |
| `web_research_runner` — Perplexity via OpenRouter | P0 obrigatório |
| `source_normalizer` + `evidence_extractor` | P0 obrigatório |
| `source_reliability_scorer` (tiers 1–5) | P0 obrigatório |
| `confidence_scorer` | P0 obrigatório |
| `contradiction_detector` (básico) | P0 obrigatório |
| `gap_detector` (básico) | P0 obrigatório |
| `synthesis_generator` com evidence_ids citados | P0 obrigatório |
| `evidence_store` com RLS + tenant_id | P0 obrigatório |
| `research_runs` table | P0 obrigatório |
| `evidence_items` table completa (schema §9.1) | P0 obrigatório |
| `risk_gap_evidence` projection | P0 obrigatório |
| Apify: ≤ 5 actors pré-aprovados | P0 parcial |
| PubMed / CrossRef via API | P0 quando relevante |
| Metacognik review (manual/semi-automático) | P0 mínimo |
| Slash commands: `/research`, `/evidence`, `/memory` | P0 |

**Fora do MVP P0:**

| Feature | Motivo |
|---------|--------|
| Full academic engine (Google Scholar, arXiv automático) | P0+ |
| Crawler amplo / scraping irrestrito | Nunca sem collector registry aprovado (doc 26) |
| Full Apify actor marketplace | Aguarda doc 26 |
| Real-time social listening | Aguarda doc 26 + aprovação legal |
| ROI assumption linking automático | Aguarda doc 21 |
| Feedback → research pipeline automático | Aguarda doc 22 |
| Research marketplace / agentes especializados | Fase 12+ |
| Auto-publicação de research reports | Fase 12+ |

---

# 26. Modos de Falha

| # | Modo de falha | Sintoma | Mitigação |
|---|---------------|---------|-----------|
| F1 | Fonte Tier 5 usada como base de decisão crítica | Decisão incorreta com alta confidence aparente | `source_tier` condiciona `confidence_score`; Tier 5 não permite `confidence > 0.2` |
| F2 | Evidência desatualizada usada sem freshness check | Dados de mercado de 2 anos usados como benchmark atual | `freshness_score` visível; `is_stale` flag em projections; re-run sugerido automaticamente |
| F3 | Dado contraditório não detectado → síntese falsa | Conclusão oposta à realidade apresentada com alta confidence | `contradiction_detector` executa antes de síntese; síntese bloqueada se contradição > threshold |
| F4 | Collector falha silenciosamente | Research completa sem dados reais da fonte esperada | `SourceCollectionFailed` event sempre emitido; resultado parcial marcado como incompleto |
| F5 | Custo alto sem reserva prévia | Saldo negativo após run; run concorrentes afetados | `credit_reservation` obrigatória antes de run; `blocked_by_cost` se insuficiente |
| F6 | RAG contaminado com dados desatualizados | RAG retorna evidências stale como se fossem frescas | `freshness_score` indexado no RAG; retriever filtra por score mínimo configurável |
| F7 | PII enviada para fonte externa sem sanitização | Dados do cliente expostos em query externa | `pii_sanitizer` obrigatório antes de qualquer query externa; log de sanitização em audit_log |
| F8 | Viés de seleção de fonte | Pesquisa endossa apenas um ponto de vista | `bias_warning` emitido quando distribuição de tier é unilateral; Metacognik alertado |
| F9 | Alucinação de fonte (fonte que não existe) | Evidence_item com URL ou DOI inválido | `source_normalizer` valida URL/DOI antes de criar evidence_item; fonte inválida → rejected |
| F10 | Síntese sem evidência real | Conclusão sem `evidence_ids` citados | `synthesis_generator` não aceita síntese sem mínimo de 1 evidence_id |
| F11 | Extrapolação científica indevida | Estudo com escopo limitado generalizado como fato universal | `academic_research_runner` extrai scope + limitações; `normalized_summary` inclui limitações |
| F12 | Pesquisa duplicada sem cache | Mesmo query executado N vezes sem reuso de evidências | `research_run_id` hash de query + contexto; cache de resultados com TTL configurável |
| F13 | Pesquisa sem objetivo claro (scope creep) | Research run coleta dados sem conexão a hipótese ou decisão | `research_intent_router` requer `research_query` estruturado; query vaga → scope clarification request |
| F14 | Tenant leak em busca semântica | Usuário A vê evidências de Tenant B via RAG | RAG retrieval com `namespace = tenant_id + workspace_id` como WHERE clause — nunca pós-filtro |
| F15 | Fonte inacessível (paywall) | Collector retorna erro 403 ou página de paywall | `document_parser` detecta paywall; evidência marcada como `partial`; abstract + DOI retornados |
| F16 | Rate limit de API | Collector bloqueado após N requests | Exponential backoff + retry configurável por collector; `SourceCollectionFailed` com reason rate_limit |
| F17 | Dado legalmente sensível coletado sem autorização | GDPR / LGPD violation | `research_policy_engine` verifica classificação de dados antes do collector; sources com PII exigem aprovação `admin+` |
| F18 | Conflito entre fontes sem resolução imposta | Síntese inconsistente ou enviesada | Contradição nunca forçada a resolução; ambas evidências mantidas com flag; síntese marcada `contested` |
| F19 | Pesquisa usada como decisão sem aprovação | Hipótese de pesquisa vira decisão de produto diretamente | Hipóteses são nodes sugeridos; decision nodes requerem approval gate conforme doc 04 |
| F20 | Collector retorna HTML/CSS em vez de dados estruturados | Evidence extractor falha; dados sem estrutura | `source_normalizer` valida formato de output; HTML não estruturado → `SourceCollectionFailed` |
| F21 | Freshness score ignorado em dashboard | Evidence expirada exibida como atual | `research_projection_engine` sempre calcula freshness dinamicamente; projection inclui `is_stale` flag |
| F22 | Metacognik não auditou síntese de alto risco | Conclusão incorreta apresentada ao usuário com alta confidence | `metacognik_review_required` ativado automaticamente por threshold de confidence + risk_level |

---

# 27. Patches sugeridos para outros documentos

Estes patches são necessários para suportar a Research Capability. **Não foram aplicados**. Devem ser registrados como patches formais nos respectivos docs antes da implementação do pipeline.

| ID | Doc alvo | Patch | Urgência |
|----|----------|-------|----------|
| **P18-1** | `11_DATA_MODEL_AND_PERSISTENCE.md` | Adicionar tabela `research_runs` com schema completo (§9.2 deste doc) | Antes de implementar Research Pipeline |
| **P18-2** | `11_DATA_MODEL_AND_PERSISTENCE.md` | Expandir tabela `evidence_items` com schema completo (§9.1) — atualmente mencionada mas sem schema formal em doc 11 | Antes de implementar Research Pipeline |
| **P18-3** | `11_DATA_MODEL_AND_PERSISTENCE.md` | Adicionar tabela `hypotheses` como entidade formal (atualmente hipóteses são nodes implícitos) | Antes de implementar Evidence Object Model completo |
| **P18-4** | `11_DATA_MODEL_AND_PERSISTENCE.md` | Expandir `risk_gap_evidence_projection` (§21) para incluir: `research_run_status`, `collector_status`, `freshness_avg_score`, `contradiction_count`, `gap_count_open` | Antes de implementar Dashboard widget #10 com dados de research |
| **P18-5** | `10_SYSTEM_RUNTIME_ARCHITECTURE.md` | Adicionar `research_intent_router` como sub-rota nomeada do `intent_router` no fluxo canônico §5.2 | Antes de implementar Research Pipeline |
| **P18-6** | `26_COLLECTOR_REGISTRY.md` (doc futuro) | Definir: `collector_id`, `collector_type`, `source_type_mapping`, `rate_limit`, `cost_per_run`, `authorization_level`, `robots_txt_respected`, `pii_risk_level` | Antes de qualquer Apify collector em produção |

---

# 28. Related Notes

- [[10_SYSTEM_RUNTIME_ARCHITECTURE]] v1.1.1 — event bus, canonical flow; `research_intent_router` é sub-rota do `intent_router`
- [[11_DATA_MODEL_AND_PERSISTENCE]] v1.2.0 — `evidence_items` table; patches P18-1 a P18-5 pendentes
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]] v1.1.0 — RLS, secret_refs, data classification; governa privacy rules do §17
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]] v1.1.0 — `cost_ledger` para research runs; Metacognik audita research quality
- [[14_PROJECT_DASHBOARD_ARCHITECTURE]] v1.2.0 — widget Risk/Gap/Evidence Monitor; projeção `risk_gap_evidence`
- [[15_COMMAND_CENTER_ARCHITECTURE]] v1.2.1 — slash commands de research; `research_intent_router` downstream do `intent_router`
- [[16_NODE_CANVAS_ARCHITECTURE]] v1.2.0 — evidence nodes, hypothesis nodes, gap nodes, risk nodes no canvas
- [[17_IMPLEMENTATION_PROTOCOL]] v1.2.1 — Fase 6 (Context, Memory & Evidence); Manus status §12
- [[21_ROI_ARCHITECTURE]] (futuro) — ROI assumptions alimentadas por research (§14)
- [[22_FEEDBACK_SYSTEM_ARCHITECTURE]] (futuro) — feedback → research loop (§15)
- [[23_SUPPORT_SYSTEM_ARCHITECTURE]] (futuro) — support friction → research loop (§15)
- [[26_COLLECTOR_REGISTRY]] (futuro) — lista de collectors aprovados; autorização de Apify actors
- [[ARCHITECTURE_PATCH_REPORT]] v1.2.1 — patches P18-1 a P18-6 devem ser registrados
- [[18_RESEARCH_PROTOCOL_FOR_MANUS]] v1.1.0 — doc supersedido; usar apenas como referência histórica de processo de bootstrap

---

## Patch 1.0.0 — Criação do documento

**Supersede:** `18_RESEARCH_PROTOCOL_FOR_MANUS.md` v1.1.0

**O que mudou em relação ao doc anterior:**
- Escopo completamente reescrito: de "protocolo de uso de Manus" para "Research Capability Architecture do CKOS"
- Manus formalmente reposicionado como ferramenta temporária de bootstrap (§4) com roadmap de substituição explícito
- 28 seções engineer-ready vs. 16 seções operacionais do doc anterior
- Pipeline completo definido com 18 componentes (§5) e fluxo canônico de 16 passos (§6)
- Framework de confiabilidade de fonte: Tier 1–5 com critérios, pesos e riscos (§8)
- Evidence Object Model completo com schema SQL + indexes + RLS (§9)
- 5 patches sugeridos para docs 10 e 11 (§27) — não aplicados
- 22 modos de falha com mitigações (§26)
- Relações explícitas com Command Center, Node Canvas, Dashboard, ROI, Feedback e Suporte
- Privacy, security e cost frameworks derivados dos docs 12 e 13
- State machine de research com 13 estados (§23) e 20 eventos (§24)
- MVP P0 com in/out list explícito (§25)
