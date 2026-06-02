---
title: 21_ROI_ARCHITECTURE
system_id: roi_architecture
version: 1.0.0
status: draft
category: business_system
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - founder
  - technical
  - metacognik
  - finance_admin
approval_required:
  - founder
  - technical
  - metacognik
inputs:
  - 10_SYSTEM_RUNTIME_ARCHITECTURE.md v1.1.1
  - 11_DATA_MODEL_AND_PERSISTENCE.md v1.2.0
  - 13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md v1.1.0
  - 14_PROJECT_DASHBOARD_ARCHITECTURE.md v1.2.0
  - 15_COMMAND_CENTER_ARCHITECTURE.md v1.2.1
  - 16_NODE_CANVAS_ARCHITECTURE.md v1.2.0
  - 17_IMPLEMENTATION_PROTOCOL.md v1.2.1
  - 18_RESEARCH_PROTOCOL.md v1.0.0
  - 20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md v1.2.0
  - ARCHITECTURE_PATCH_REPORT.md v1.3.0
outputs:
  - roi_system_architecture
  - roi_type_registry (12 types)
  - roi_object_model (11 objects)
  - roi_calculation_layers (11 layers)
  - roi_confidence_framework (5 levels)
  - roi_state_machine (11 states)
  - roi_events (16 events)
  - roi_dashboard_projection_rules
  - roi_mvp_p0_scope
related_notes:
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - ../04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md
  - ../04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md
  - ../04_PRODUCT_SYSTEM/16_NODE_CANVAS_ARCHITECTURE.md
  - ../05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md
  - ../ARCHITECTURE_PATCH_REPORT.md
  - 22_FEEDBACK_SYSTEM_ARCHITECTURE.md
  - 23_SUPPORT_SYSTEM_ARCHITECTURE.md
  - 24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md
tags: [business_system, roi, value_intelligence, evidence, confidence, cost, decisions, outcomes]
---

> **TESE CENTRAL — DOC 21:**
> ROI in CKOS is not a static financial metric. It is a governed value intelligence system
> that connects costs, evidence, hypotheses, decisions, outcomes and confidence across
> financial, strategic, operational, brand, content, acquisition, retention, efficiency
> and learning dimensions.
>
> Em português: ROI no CKOS não é uma métrica financeira estática. É um sistema governado
> de inteligência de valor que conecta custos, evidências, hipóteses, decisões, resultados
> e confiança em dimensões financeiras, estratégicas, operacionais, de marca, conteúdo,
> aquisição, retenção, eficiência e aprendizado.

---

# 1. Propósito

Este documento estabelece como o CKOS mede, estima, acompanha, audita e comunica valor gerado — de decisões informadas por pesquisa a resultados financeiros observados, de eficiência operacional a redução de risco, de aprendizado acumulado a impacto de marca.

O ROI Architecture define:
- Como valor é estruturado como sistema de inteligência governado (não como planilha)
- Os 12 tipos de ROI que o CKOS suporta e suas regras de evidência
- O objeto model completo que sustenta cálculos, hipóteses e projeções
- As camadas de cálculo e como se encadeiam
- O framework de confiança que controla o que pode ou não ser exibido
- Como ROI se conecta ao Dashboard, Command Center, Node Canvas, Evals e Cost Ledger
- O sistema de eventos e a state machine para rastreabilidade

```txt
ROI sem evidência é promessa.
ROI sem confiança é ilusão.
ROI sem limitação é mentira.
ROI com todos os três é inteligência de valor.
```

---

# 2. O que este documento é — e o que não é

## É

- Arquitetura de sistema de ROI do CKOS
- Sistema de inteligência de valor baseado em evidências
- Framework de hipóteses, premissas, confiança e limitações
- Base para widgets de Dashboard, propostas, cost guard e decisões de negócio
- Protocolo de governança para exibição e aprovação de ROI
- Definição dos tipos de ROI suportados e suas regras

## Não é

- Promessa de resultado garantido
- Planilha financeira simplificada
- Argumento comercial sem evidência ou confiança
- Sistema contábil ou ERP
- Integração com gateways de pagamento ou sistemas financeiros externos
- Definição de pricing ou billing (ver doc 24)
- Substituição de análise financeira profissional

---

# 3. Princípio Central

> **No ROI claim can be shown without evidence, assumptions, confidence level, and limitations.**
>
> Em português: Nenhuma afirmação de ROI pode ser exibida sem evidências, premissas,
> nível de confiança e limitações.

Toda projeção de ROI no CKOS deve ser acompanhada de:
- Pelo menos um `evidence_link` com `reliability_score` documentado
- Lista de `roi_assumptions` com owner e data de expiração
- `confidence_level` visível (high | medium | low | speculative | insufficient_data)
- Lista de `roi_gaps` abertos quando confidence ≤ medium
- Seção de limitações quando exibido em proposta ou relatório externo

Nenhum agente, nenhuma projeção, nenhum widget pode exibir um valor de ROI sem cumprir estas condições.

---

# 4. ROI Philosophy

1. **Evidence-based:** Toda afirmação de ROI requer evidência rastreável com fonte, tier e reliability_score
2. **Hypothesis-aware:** Estimativas são hipóteses — rotuladas como tal até que outcomes sejam observados e verificados
3. **Confidence-scored:** Toda projeção tem confidence_level visível; confiança baixa ativa avisos e bloqueios
4. **Cost-connected:** ROI nunca existe sem custo — custo real (cost_ledger) sempre entra no cálculo antes do valor estimado
5. **Decision-linked:** ROI deve ser conectável à decisão que o motivou ou à decisão que ele informa
6. **Outcome-aware:** O sistema rastreia o que foi prometido vs. o que foi observado; desvios são registrados
7. **Risk-adjusted:** Toda projeção considera riscos que podem invalidar premissas ou reduzir o valor realizado
8. **Time-aware:** Toda projeção tem horizonte temporal; premissas expiram; resultados têm janela de observação
9. **Explainable:** Qualquer número de ROI deve poder ser decomposto em camadas, premissas e fontes por qualquer ator autorizado
10. **Auditable by Metacognik:** Metacognik pode rever qualquer roi_model e vetar exibição se evidência for insuficiente
11. **Founder-approved for external use:** Uso de ROI em proposta ou comunicação externa requer aprovação explícita do Founder
12. **Never a sales pitch substitute:** ROI não substitui proposta de valor — é evidência que a sustenta, com limitações explícitas

---

# 5. ROI Types

## 5.1 financial_roi

**Definição:** Retorno monetário direto — receita gerada, custos reduzidos ou economias realizadas como resultado direto de atividades do CKOS.

**Quando usar:** Quando há baseline financeiro mensurável e outcome verificável em moeda.

**Inputs:** cost_ledger, credit_transactions, billing_events, dados de receita (quando conectados), comparação antes/depois de custo.

**Outputs:** net_financial_gain, payback_period_days, roi_percentage (net_gain / total_cost × 100).

**Evidências requeridas:** invoices ou contratos de custo, registros de pagamento, dados contábeis com fonte verificável. Mínimo Tier 2.

**Riscos:** erro de atribuição (CKOS não foi o único fator), flutuação de moeda, realização atrasada do valor.

**Limitações:** requer baseline financeiro documentado; difícil isolamento de causalidade; não disponível em projetos sem componente financeiro claro.

**Exemplo prático:** Produção de conteúdo reduziu de R$50k/mês (agência externa) para R$15k/mês (CKOS + equipe interna). Financial ROI = R$35k/mês de economia com payback em ~3 meses.

---

## 5.2 strategic_roi

**Definição:** Valor de melhor posicionamento estratégico, capacidades aumentadas, decisões de maior qualidade ou redução de risco estratégico.

**Quando usar:** Quando o benefício é vantagem competitiva, qualidade de decisão ou desenvolvimento de capacidade — não diretamente financeiro.

**Inputs:** decision_quality_roi metrics, evidência de pesquisa, dados de benchmark competitivo, auditorias de decisão antes/depois.

**Outputs:** strategic_value_score, decision_improvement_index, capability_growth_indicator.

**Evidências requeridas:** evidência de pesquisa Tier 1–3, benchmarks comparativos, auditoria de decisões antes/depois. Mínimo Tier 3.

**Riscos:** difícil de quantificar; altamente baseado em proxy; realização atrasada no tempo.

**Limitações:** incerteza alta; frequentemente especulativo sem dados longitudinais; nunca converter para moeda sem Founder approval e evidência Tier 1.

**Exemplo prático:** Pesquisa do CKOS revelou segmentação de mercado que mudou a estratégia go-to-market, evitando campanha estimada em R$200k com baixa probabilidade de conversão.

---

## 5.3 operational_roi

**Definição:** Valor de processos mais rápidos, menos retrabalho, menos erros e melhor coordenação operacional.

**Quando usar:** Quando há processo mensurável com comparação antes/depois disponível.

**Inputs:** workflow_runs timing, agent_runs timing, estimativas de tempo economizado, métricas de taxa de erro, dados de retrabalho.

**Outputs:** time_saved_hours, rework_reduction_percentage, throughput_increase_ratio.

**Evidências requeridas:** dados de timing de workflow, logs de erro, comparação de processo antes/depois. Mínimo Tier 3.

**Riscos:** difícil separar contribuição do CKOS de outras melhorias; estimativas de tempo frequentemente subjetivas.

**Limitações:** requer medição de baseline; tempo economizado é proxy — não é caixa diretamente sem conversão por taxa horária.

**Exemplo prático:** Geração de proposta reduzida de 8h manual para 1.5h com CKOS. Tempo economizado = 6.5h por proposta × custo horário da equipe → operational ROI por proposta.

---

## 5.4 brand_roi

**Definição:** Valor de maior consistência de marca, qualidade percebida mais alta ou redução de risco de marca.

**Quando usar:** Quando output do CKOS afeta diretamente materiais de marca, conteúdo client-facing ou percepção de marca.

**Inputs:** content_performance_proxy, evidências de auditoria de marca, NPS proxy, feedback de cliente sobre consistência.

**Outputs:** brand_consistency_score, perceived_quality_index, brand_risk_reduction_indicator.

**Evidências requeridas:** feedback de cliente, resultados de auditoria de marca, dados de NPS, comparação de materiais antes/depois. Mínimo Tier 3.

**Riscos:** altamente subjetivo; atribuição difícil; horizonte temporal longo (meses a anos).

**Limitações:** sem conversão monetária direta sem dados adicionais; especulativo em estágios iniciais; nunca exibir como número em moeda sem evidência Tier 1–2.

**Exemplo prático:** Consistência visual e de tom em todos os materiais do cliente aumentou taxa de aceite de proposta de 40% para 55% (hipótese — validar com dados de conversão).

---

## 5.5 content_roi

**Definição:** Valor de produzir mais conteúdo, melhor e com maior consistência a custo menor.

**Quando usar:** Quando CKOS é usado para produzir assets de conteúdo (copy, briefs visuais, scripts, relatórios, posts).

**Inputs:** contagem de artifacts, estimativas de tempo de produção, quality scores de eval, dados de uso/reaproveitamento.

**Outputs:** content_per_hour_ratio, content_quality_score, content_reuse_rate, cost_per_unit_of_content.

**Evidências requeridas:** registros de artifacts, logs de tempo de produção, eval scores de qualidade. Mínimo Tier 3.

**Riscos:** trade-off quantidade vs. qualidade; conteúdo AI pode precisar de mais revisão do que esperado; rastreamento downstream limitado.

**Limitações:** requer rastreamento de uso de conteúdo para calcular valor completo; qualidade é parcialmente subjetiva.

**Exemplo prático:** CKOS produziu 40 posts sociais em 2h (vs. 2 dias em produção manual de agência). Content ROI = custo de 2h × automação vs. custo de 2 dias × tarifa de agência.

---

## 5.6 acquisition_roi

**Definição:** Valor de melhores propostas, qualificação mais rápida e maior conversão de clientes.

**Quando usar:** Quando atividades do CKOS são diretamente conectadas a pipeline de vendas e conversão.

**Inputs:** dados de proposta, taxas de conversão, estimativas de CAC, métricas de tempo-até-proposta, ticket médio.

**Outputs:** conversion_rate_change, cac_reduction_estimate, time_to_proposal_reduction.

**Evidências requeridas:** dados de CRM (quando conectado), registros de aceite de proposta, feedback da equipe de vendas. Mínimo Tier 2 para conversão financeira.

**Riscos:** complexidade do ciclo de vendas; atribuição de CKOS vs. outros fatores; dados de CRM raramente integrados.

**Limitações:** requer integração com dados de vendas (externa); proxy-heavy sem CRM; nunca projetar em moeda sem dados de conversão reais.

**Exemplo prático:** Propostas com CKOS tiveram 60% menos tempo de produção e 10% maior aceite em amostra de 20 propostas (requer validação estatística com amostra maior).

---

## 5.7 retention_roi

**Definição:** Valor de relacionamentos com clientes mais longos, churn reduzido e expansão de conta.

**Quando usar:** Quando atividades do CKOS reduzem fricção do cliente, melhoram qualidade de entrega ou aumentam NPS.

**Inputs:** feedback de cliente, support_tickets, dados de renovação, eventos de expansão, NPS tracking.

**Outputs:** retention_rate_change, ltv_impact_estimate, churn_risk_reduction_score.

**Evidências requeridas:** feedback de cliente, registros de renovação, NPS, qualidade de resolução de suporte. Mínimo Tier 2–3.

**Riscos:** retenção é multifatorial; erro de atribuição alto; LTV projection é especulativo em estágios iniciais.

**Limitações:** requer dados longitudinais; projeção de LTV é especulativa sem histórico de 12+ meses.

**Exemplo prático:** Sistema de detecção de fricção identificou 3 clientes de alto valor em risco de churn. Intervenção proativa manteve contratos — avoided_cost = valor anual desses contratos.

---

## 5.8 efficiency_roi

**Definição:** Valor de usar recursos existentes melhor — humanos, ferramentas, modelos, créditos.

**Quando usar:** Quando o benefício primário é fazer mais com o que já existe (não necessariamente economizar dinheiro).

**Inputs:** usage_events, credit_transactions, métricas de eficiência de workflow, utilização de agente, cost_per_output metrics.

**Outputs:** resource_utilization_rate, credit_efficiency_ratio, output_per_credit, cost_per_workflow.

**Evidências requeridas:** logs de usage, cost_ledger, comparação de consumo de recursos antes/depois. Mínimo Tier 2–3.

**Riscos:** ganho de eficiência pode mascarar perda de qualidade; eficiência de crédito ≠ entrega de valor.

**Limitações:** requer dados de baseline de uso; retornos diminuem conforme eficiência aumenta.

**Exemplo prático:** Otimização do model router reduziu custo médio por workflow completado em 35% sem degradação de quality score de eval.

---

## 5.9 learning_roi

**Definição:** Valor do sistema ficando mais inteligente — melhor pesquisa, melhores decisões, melhores prompts, melhores modelos selecionados.

**Quando usar:** Quando o benefício é conhecimento acumulado, maior precisão ou crescimento de capacidade ao longo do tempo.

**Inputs:** learning_loop_metrics, eval_scores ao longo do tempo, crescimento da base de conhecimento, decision_outcome tracking.

**Outputs:** decision_quality_trend, model_accuracy_trend, knowledge_velocity_score, eval_improvement_rate.

**Evidências requeridas:** eval results ao longo do tempo, rastreamento de outcomes de decisões, métricas de knowledge base. Mínimo Tier 2 (dados próprios do sistema).

**Riscos:** difícil de quantificar; pode não se traduzir em valor de negócio sem implantação downstream; dados de learning são internos.

**Limitações:** requer rastreamento longitudinal; sistemas em estágio inicial têm dados limitados; correlação ≠ causalidade.

**Exemplo prático:** Após 3 meses, qualidade de síntese de pesquisa subiu de score 0.62 para 0.78, reduzindo revisão manual de 2h para 30min por pesquisa.

---

## 5.10 risk_reduction_roi

**Definição:** Valor de prevenir erros, evitar decisões ruins, reduzir risco de compliance ou prevenir perda de dados.

**Quando usar:** Quando CKOS permite evitar um resultado negativo quantificável.

**Inputs:** incident logs, risk assessments, eventos de enforcement de policy, qualidade de audit trail, histórico de incidentes.

**Outputs:** incidents_avoided_count, estimated_loss_avoided, compliance_score, risk_exposure_reduction.

**Evidências requeridas:** dados históricos de incidentes, relatórios de avaliação de risco, resultados de auditoria. Mínimo Tier 2.

**Riscos:** contrafactual — difícil provar o que não aconteceu; custo evitado requer cenário baseline explícito.

**Limitações:** especulativo sem histórico real de incidentes; requer modelo de risco com probabilidade e impacto documentados.

**Exemplo prático:** Enforcement de RLS e política de dados de doc 12 preveniu acesso cross-tenant, evitando potencial multa de LGPD estimada em R$50k–R$500k.

---

## 5.11 decision_quality_roi

**Definição:** Valor de tomar decisões melhores mais rapidamente, com mais evidência e menos incerteza.

**Quando usar:** Quando CKOS suporta diretamente um processo de decisão (pesquisa, teste de hipótese, aprovação formal).

**Inputs:** decision_outcomes, evidência de cobertura de evidências, confidence_accuracy, time_to_decision, historico de revisão de decisões.

**Outputs:** decision_accuracy_rate, decision_speed_improvement, confidence_calibration_score, outcome_quality_delta.

**Evidências requeridas:** registros de outcomes de decisões, comparação de qualidade antes/depois, eval scores. Mínimo Tier 2–3.

**Riscos:** qualidade de decisão é subjetiva sem dados de outcome; correlação ≠ causalidade; loop de feedback longo.

**Limitações:** requer rastreamento de outcome após decisões; feedback loop pode levar meses; dados iniciais insuficientes.

**Exemplo prático:** Decisões baseadas em pesquisa CKOS mostraram 73% melhor alinhamento com resultado observado vs. decisões por intuição em auditoria histórica de 6 meses.

---

## 5.12 time_to_decision_roi

**Definição:** Valor da vantagem de velocidade obtida com processamento mais rápido de informação.

**Quando usar:** Quando velocidade de decisão é vantagem competitiva ou necessidade operacional crítica.

**Inputs:** time_to_decision metrics, timing de workflow, duração de research_run, oportunidades perdidas por lentidão (quando documentadas).

**Outputs:** decision_latency_reduction, opportunity_cost_avoided, time_advantage_score.

**Evidências requeridas:** dados de timing de workflow, dados de state machine de research_runs, comparação antes/depois. Mínimo Tier 3.

**Riscos:** decisões mais rápidas nem sempre são melhores; trade-off velocidade-precisão deve ser documentado.

**Limitações:** custo de oportunidade evitado é especulativo; requer medição de baseline; irrelevante sem pressão de tempo real.

**Exemplo prático:** CKOS reduziu tempo de pesquisa de mercado de 2 semanas para 3 horas, habilitando decisão de campanha antes do prazo da plataforma.

---

# 6. ROI Object Model

## 6.1 roi_model

Container principal de uma análise de ROI. Uma análise por tipo de ROI por projeto (ou por fase do projeto).

```sql
roi_models (
  id                      uuid PRIMARY KEY,
  tenant_id               uuid NOT NULL,           -- RLS
  org_id                  uuid NOT NULL,
  workspace_id            uuid NOT NULL,
  project_id              uuid NOT NULL,
  roi_type                roi_type_enum NOT NULL,   -- ver §5
  title                   text NOT NULL,
  description             text,
  status                  roi_status_enum NOT NULL, -- ver §21
  owner_id                uuid NOT NULL,
  confidence_level        confidence_level_enum NOT NULL, -- ver §9
  overall_confidence_score numeric(3,2),           -- 0.00–1.00
  estimated_value_low     numeric,                  -- currency
  estimated_value_mid     numeric,                  -- currency (ponto central)
  estimated_value_high    numeric,                  -- currency
  observed_value          numeric,                  -- currency (se observado)
  currency                text DEFAULT 'BRL',
  time_horizon_days       integer,                  -- horizonte da projeção
  created_by_agent_id     text,
  source_event_id         uuid,                     -- evento que originou
  related_workflow_id     uuid,
  related_artifact_id     uuid,
  related_decision_id     uuid,
  metacognik_reviewed     boolean DEFAULT false,
  metacognik_warning      text,
  created_at              timestamptz NOT NULL DEFAULT now(),
  updated_at              timestamptz NOT NULL DEFAULT now(),
  archived_at             timestamptz
)
```

**Regras:** RLS por `tenant_id`. Toda mudança via evento. `observed_value` apenas quando `roi_outcome` verificado existe. `estimated_value_*` requerem pelo menos 1 `roi_assumption` e 1 `roi_evidence_link`.

---

## 6.2 roi_metric

Métrica individual dentro de um roi_model. Um modelo pode ter N métricas por camada de cálculo.

```sql
roi_metrics (
  id                      uuid PRIMARY KEY,
  roi_model_id            uuid NOT NULL REFERENCES roi_models(id),
  tenant_id               uuid NOT NULL,
  metric_name             text NOT NULL,
  metric_type             enum(financial|proxy|proxy_leading|proxy_lagging|observed|estimated),
  calculation_layer       roi_calc_layer_enum NOT NULL, -- ver §8
  value_estimated         numeric,
  value_observed          numeric,
  unit                    text NOT NULL,  -- currency|hours|percentage|score|units|events
  confidence_score        numeric(3,2),
  formula_description     text,
  data_source             text,
  reliability_score       numeric(3,2),
  evidence_count          integer DEFAULT 0,
  assumption_count        integer DEFAULT 0,
  last_updated_at         timestamptz NOT NULL DEFAULT now()
)
```

---

## 6.3 roi_snapshot

Captura point-in-time do estado completo de um roi_model. Gerado por evento, não por query live.

```sql
roi_snapshots (
  id                      uuid PRIMARY KEY,
  roi_model_id            uuid NOT NULL REFERENCES roi_models(id),
  tenant_id               uuid NOT NULL,
  snapshot_at             timestamptz NOT NULL DEFAULT now(),
  cost_total              numeric NOT NULL DEFAULT 0,
  value_total_estimated   numeric,
  value_total_observed    numeric,
  confidence_level        confidence_level_enum NOT NULL,
  overall_score           numeric(3,2),
  gap_count               integer DEFAULT 0,
  risk_count              integer DEFAULT 0,
  assumption_count        integer DEFAULT 0,
  evidence_count          integer DEFAULT 0,
  payback_estimate_days   integer,
  trend_direction         enum(improving|stable|declining|unknown),
  metacognik_warnings     text[],
  metadata                jsonb,
  created_by_agent_id     text,
  source_event_id         uuid NOT NULL
)
```

---

## 6.4 roi_hypothesis

Uma hipótese de valor que precisa ser validada por evidência ou outcome.

```sql
roi_hypotheses (
  id                      uuid PRIMARY KEY,
  roi_model_id            uuid NOT NULL REFERENCES roi_models(id),
  tenant_id               uuid NOT NULL,
  hypothesis_text         text NOT NULL,
  hypothesis_type         enum(value_generation|cost_reduction|time_saving|risk_reduction|quality_improvement|adoption|retention|acquisition),
  status                  enum(proposed|testing|validated|invalidated|expired|uncertain),
  confidence_score        numeric(3,2),
  evidence_count          integer DEFAULT 0,
  owner_id                uuid,
  source                  text,
  related_evidence_ids    uuid[],
  contradiction_ids       uuid[],
  expiration_at           timestamptz,
  created_at              timestamptz NOT NULL DEFAULT now(),
  updated_at              timestamptz NOT NULL DEFAULT now()
)
```

**Regra:** `status = validated` requer pelo menos 1 `roi_evidence_link` com `evidence_type = supports` e `reliability_score ≥ 0.6`. Nenhum agente pode marcar como `validated` sem evidência.

---

## 6.5 roi_assumption

Uma premissa da qual o ROI depende. Toda premissa tem owner, expiração e risco se incorreta.

```sql
roi_assumptions (
  id                      uuid PRIMARY KEY,
  roi_model_id            uuid NOT NULL REFERENCES roi_models(id),
  tenant_id               uuid NOT NULL,
  assumption_text         text NOT NULL,
  source                  text,
  evidence_link           uuid REFERENCES evidence_items(id),
  owner_id                uuid NOT NULL,
  confidence              numeric(3,2),
  expiration_at           timestamptz,
  affected_metrics        uuid[],  -- roi_metric ids
  risk_if_wrong           text NOT NULL,
  status                  enum(active|expired|invalidated|under_review),
  created_at              timestamptz NOT NULL DEFAULT now(),
  updated_at              timestamptz NOT NULL DEFAULT now()
)
```

**Regras:** `status = expired` quando `expiration_at < now()`. Sistema deve re-calcular confidence do `roi_model` quando assumption expira. Premissa sem `risk_if_wrong` é rejeitada na criação.

---

## 6.6 roi_evidence_link

Conexão rastreável entre ROI e uma evidência específica do sistema de pesquisa (doc 18).

```sql
roi_evidence_links (
  id                      uuid PRIMARY KEY,
  roi_model_id            uuid NOT NULL REFERENCES roi_models(id),
  roi_metric_id           uuid REFERENCES roi_metrics(id),
  roi_hypothesis_id       uuid REFERENCES roi_hypotheses(id),
  evidence_item_id        uuid NOT NULL REFERENCES evidence_items(id),
  tenant_id               uuid NOT NULL,
  relevance_score         numeric(3,2) NOT NULL,
  contribution_weight     numeric(3,2),
  evidence_type           enum(supports|contradicts|qualifies|bounds|contextualizes),
  linked_by_agent_id      text,
  linked_at               timestamptz NOT NULL DEFAULT now()
)
```

**Regras:** `evidence_items.reliability_score < 0.4` não pode suportar `high_confidence` ROI. Evidências com `evidence_type = contradicts` reduzem automaticamente `confidence_score` do modelo afetado.

---

## 6.7 roi_outcome

Resultado observado após uma ação. A forma mais confiável de ROI — measurement real vs. estimativa.

```sql
roi_outcomes (
  id                      uuid PRIMARY KEY,
  roi_model_id            uuid NOT NULL REFERENCES roi_models(id),
  tenant_id               uuid NOT NULL,
  outcome_date            timestamptz NOT NULL,
  outcome_type            enum(financial|operational|strategic|brand|content|efficiency|learning|acquisition|retention),
  value_observed          numeric NOT NULL,
  unit                    text NOT NULL,
  description             text NOT NULL,
  verified                boolean DEFAULT false,
  verifier_id             uuid,  -- humano que verificou
  verified_at             timestamptz,
  source                  text NOT NULL,
  evidence_links          uuid[],
  created_at              timestamptz NOT NULL DEFAULT now()
)
```

**Regras:** `verified = true` requer `verifier_id` humano (não agente). `verified = false` outcomes são tratados como proxy — não como fact. Outcome verificado atualiza `roi_model.observed_value` via evento.

---

## 6.8 roi_gap

Dado ausente que impede estimativa confiante. Documentado explicitamente para que ações de resolução sejam rastreadas.

```sql
roi_gaps (
  id                      uuid PRIMARY KEY,
  roi_model_id            uuid NOT NULL REFERENCES roi_models(id),
  tenant_id               uuid NOT NULL,
  gap_description         text NOT NULL,
  gap_type                enum(missing_evidence|missing_baseline|missing_outcome|missing_benchmark|data_staleness|conflicting_data|unknown_assumption),
  severity                enum(blocking|significant|minor),
  resolution_action       text,
  owner_id                uuid,
  status                  enum(open|in_progress|resolved|accepted_risk),
  resolved_at             timestamptz,
  created_at              timestamptz NOT NULL DEFAULT now(),
  updated_at              timestamptz NOT NULL DEFAULT now()
)
```

**Regra:** Gap com `severity = blocking` impede upgrade de `confidence_level` para `high_confidence`. Gaps `open` são sempre exibidos no widget de ROI ao lado do confidence indicator.

---

## 6.9 roi_risk

Um risco específico que pode invalidar premissas ou reduzir o valor realizado do ROI.

```sql
roi_risks (
  id                      uuid PRIMARY KEY,
  roi_model_id            uuid NOT NULL REFERENCES roi_models(id),
  tenant_id               uuid NOT NULL,
  risk_description        text NOT NULL,
  risk_type               enum(assumption_failure|data_staleness|market_change|execution_risk|external_dependency|measurement_failure|attribution_error),
  likelihood              enum(high|medium|low),
  impact                  enum(high|medium|low),
  risk_score              numeric(3,2),  -- calculated: likelihood × impact
  mitigating_action       text,
  owner_id                uuid,
  status                  enum(open|mitigated|accepted|materialized),
  materialized_at         timestamptz,
  created_at              timestamptz NOT NULL DEFAULT now(),
  updated_at              timestamptz NOT NULL DEFAULT now()
)
```

---

## 6.10 roi_projection (Read-Only UI Projection)

Projeção de leitura gerada pelo `roi_projection_engine` para consumo por Dashboard e Node Canvas. **Não é tabela de source — é projeção.**

```txt
Campos da roi_snapshot_projection (alimenta UI):
  roi_model_id            uuid
  tenant_id               uuid
  roi_type                roi_type_enum
  title                   text
  status                  roi_status_enum
  confidence_level        confidence_level_enum
  overall_confidence_score numeric(3,2)
  estimated_value_mid     numeric
  observed_value          numeric
  cost_total              numeric
  roi_ratio               numeric  -- (value - cost) / cost
  payback_estimate_days   integer
  gap_count               integer
  open_gap_severity_max   enum
  risk_count              integer
  assumption_count        integer
  expired_assumption_count integer
  evidence_count          integer
  trend_direction         enum
  metacognik_warnings     text[]
  last_snapshot_at        timestamptz

Fonte: roi_models + roi_snapshots + roi_gaps + roi_risks + roi_assumptions
Atualizado por: RoiSnapshotTaken (event)
Invalidado por: RoiContradicted, RoiGapDetected, RoiAssumptionExpired (events)
```

---

## 6.11 roi_decision_link

Conexão entre um roi_model e uma decisão que ele informou ou que foi informada por ele.

```sql
roi_decision_links (
  id                      uuid PRIMARY KEY,
  roi_model_id            uuid NOT NULL REFERENCES roi_models(id),
  decision_id             uuid NOT NULL,
  tenant_id               uuid NOT NULL,
  link_type               enum(informed_by|enabled|blocked_by|revised_by|contradicted_by),
  decision_context        text,
  decision_outcome        text,
  value_realized          numeric,
  created_at              timestamptz NOT NULL DEFAULT now()
)
```

---

# 7. ROI Data Sources

O sistema de ROI consume dados de múltiplas fontes do CKOS. Nenhuma fonte é escrita diretamente pelo sistema de ROI — ele lê e vincula.

| Fonte | Dados consumidos | ROI Types alimentados |
|---|---|---|
| `cost_ledger` (doc 11 §18) | model_costs, tool_costs, collector_costs | todos (raw_cost layer) |
| `usage_events` (doc 11 §18) | consumo por run, model, tool | efficiency_roi, operational_roi |
| `credit_transactions` (doc 11 §33) | débitos de crédito por atividade | financial_roi, efficiency_roi |
| `workflow_runs` (doc 11) | duração, status, custo, output | operational_roi, content_roi |
| `agent_runs` (doc 11) | duração, custo, quality_score | efficiency_roi, decision_quality_roi |
| `evidence_items` (doc 18 §9) | claims, scores, tiers, fontes | todos (evidence layer) |
| `roi_hypotheses` | hipóteses de valor | todos |
| `decisions` (doc 11) | decisões tomadas e seus outcomes | decision_quality_roi, strategic_roi |
| `approvals` (doc 11) | aprovações e seus custos de processo | operational_roi |
| `artifacts` (doc 11) | artefatos gerados, qualidade, uso | content_roi, acquisition_roi |
| `feedback_items` (doc 11 §31) | feedback explícito e implícito | retention_roi, brand_roi |
| `support_tickets` (doc 11 §32) | fricção, resolução, custo de suporte | operational_roi, risk_reduction_roi |
| `project_activity_feed` (doc 11 §35) | atividade do projeto | todos |
| `external collectors` (doc 18) | benchmarks de mercado, dados acadêmicos | strategic_roi, acquisition_roi |

**Regras de uso:**
- Toda fonte tem `reliability_score` implícito por tipo (dados internos do CKOS = Tier 2; dados externos via collector = Tier 3–4)
- Fontes externas requerem aprovação via `collector_runner` (doc 12 §5.11) — nunca chamadas diretas
- Dados sensíveis (custo, crédito, financeiro) requerem permissão por RBAC (ver §23)

---

# 8. ROI Calculation Layers

As 11 camadas são cumulativas — cada camada adiciona contexto e aumenta confiança quando suportada por evidência.

| # | Layer | Reliability | Source | Display Rules |
|---|---|---|---|---|
| 1 | `raw_cost` | Sempre disponível | cost_ledger, credit_transactions | Sempre visível; nunca estimado |
| 2 | `estimated_value` | Requer ≥1 assumption + ≥1 evidence | roi_assumptions, roi_evidence_links | Visível com confidence label |
| 3 | `observed_outcome` | Requer outcome verificado | roi_outcomes (verified=true) | Maior prioridade; sobrescreve estimativa |
| 4 | `avoided_cost` | Requer baseline documentado | roi_assumptions + baseline comparison | Exibir apenas com fonte do baseline |
| 5 | `time_saved` | Requer timing antes/depois | workflow_runs timing + hourly_rate assumption | Exibir como horas; conversão a moeda requer assumption explícita |
| 6 | `decision_quality_gain` | Requer historical decision data | decision_outcomes + eval_scores | Alta incerteza; sempre como index, não moeda |
| 7 | `risk_reduction` | Requer modelo de risco com probabilidade | roi_risks + incident history | Exibir como probability × impact; não como moeda sem Founder approval |
| 8 | `brand_value_proxy` | Alta incerteza | feedback_items + brand audit | Nunca em moeda sem evidência Tier 1–2 |
| 9 | `content_performance_proxy` | Moderada | artifact records + quality scores | Exibir como volume × quality index |
| 10 | `acquisition_proxy` | Requer dados de conversão real | proposal data + conversion rates | Exibir apenas com dados de conversão verificados |
| 11 | `confidence_adjusted_roi` | Derivado de todas as camadas | weighted avg de todas as camadas | Número final exibido; sempre com confidence_level label |

**Regra de composição:**
```txt
confidence_adjusted_roi =
  SUM(layer_value[i] × layer_confidence_weight[i])
  / SUM(layer_confidence_weight[i])

  Onde layer_confidence_weight = evidence_reliability × assumption_confidence × layer_inherent_weight
```

**Bloqueios:**
- `confidence_adjusted_roi` não é exibido quando `confidence_level = insufficient_data`
- `confidence_adjusted_roi` exibido como "Estimativa Especulativa" quando `confidence_level = speculative`
- `brand_value_proxy` e `risk_reduction` não são convertidos a moeda sem Founder approval + Tier 1–2 evidence

---

# 9. ROI Confidence Framework

## 9.1 high_confidence

| Atributo | Critério |
|---|---|
| Evidence | ≥3 fontes Tier 1–2; `reliability_score ≥ 0.8` |
| Outcomes | ≥1 outcome verificado (verified = true) |
| Contradições | Nenhuma não resolvida |
| Assumptions | Nenhuma expirada; todas com owner |
| Gaps | Nenhum gap `severity = blocking` |
| Metacognik | Revisão passou |
| Quando exibir | Sempre — com sumário de evidências |
| Quando bloquear | Nunca (high_confidence é sempre exibível para atores autorizados) |
| Quando pedir mais dados | Se evidence_count < 3 ou assumption prestes a expirar (< 30 dias) |
| Metacognik trigger | Auditoria trimestral ou em mudança de assumption |

---

## 9.2 medium_confidence

| Atributo | Critério |
|---|---|
| Evidence | ≥2 fontes Tier 1–3; `reliability_score ≥ 0.6` |
| Outcomes | Alguns outcomes observados (nem todos verificados) |
| Contradições | ≤1 não resolvida |
| Assumptions | ≤2 abertas; nenhuma expirada |
| Gaps | Nenhum gap `severity = blocking` |
| Quando exibir | Sim — com confidence label e lista de assumptions |
| Quando bloquear | Se assumption expirada ou contradição não resolvida |
| Quando pedir mais dados | Se < 2 outcomes verificados para ROI financeiro |
| Metacognik trigger | Em detecção de gap |

---

## 9.3 low_confidence

| Atributo | Critério |
|---|---|
| Evidence | 1–2 fontes (qualquer tier); `reliability_score < 0.6` |
| Outcomes | Nenhum outcome verificado |
| Contradições | Múltiplas abertas |
| Assumptions | Múltiplas abertas; ou ≥1 expirada |
| Gaps | ≥1 gap `severity = significant` ou `blocking` |
| Quando exibir | Apenas com aviso "Baixa Confiança" + lista de gaps |
| Quando bloquear | Bloquear de propostas e relatórios formais |
| Quando pedir mais dados | Sempre — prompt de coleta de evidência acionado |
| Metacognik trigger | Obrigatório antes de qualquer uso em decisão ou proposta |

---

## 9.4 speculative

| Atributo | Critério |
|---|---|
| Evidence | Nenhuma, ou apenas fontes Tier 5 |
| Outcomes | Nenhum |
| Assumptions | Todas estimadas; nenhuma validada |
| Gaps | Múltiplos não resolvidos |
| Quando exibir | Apenas em modo hipótese/planejamento com label "Estimativa Especulativa" |
| Quando bloquear | Bloquear de qualquer output aprovado (propostas, dashboards cliente, relatórios) |
| Quando pedir mais dados | Sempre — research run requerida antes de upgrade |
| Metacognik trigger | Obrigatório antes de qualquer uso |

---

## 9.5 insufficient_data

| Atributo | Critério |
|---|---|
| Evidence | Nenhuma |
| Outcomes | Nenhum |
| Assumptions | Nenhuma validada |
| Dados | Roi_model existe mas sem métricas, evidências ou outcomes |
| Quando exibir | Exibir model como "Aguardando Dados" — nunca mostrar valor estimado |
| Quando bloquear | Bloquear todos os claims de valor |
| Quando pedir mais dados | Imediatamente — prompt para research run ou coleta de baseline |
| Metacognik trigger | Notificado para flag de gap em sessão de planejamento |

---

# 10. ROI Assumptions

Toda premissa do ROI é um objeto formal com owner, fonte, evidência, expiração e risco se incorreta.

## 10.1 Campos obrigatórios de uma roi_assumption

```txt
assumption_text    — descrição clara e verificável da premissa
source             — onde essa premissa originou (benchmark, estimativa, histórico, etc.)
evidence_link      — link para evidence_item que suporta (opcional mas recomendado)
owner_id           — humano responsável por manter e validar a premissa
confidence         — 0.00–1.00 (deve ser honesto — inflação de confiança é failure mode FM-R15)
expiration_at      — data em que a premissa deve ser revisada
affected_metrics   — quais roi_metrics dependem desta premissa
risk_if_wrong      — consequência clara se a premissa se mostrar incorreta (obrigatório)
```

## 10.2 Regras de gestão

1. Toda `roi_assumption` com `expiration_at < now()` → status = `expired` automaticamente por evento
2. Assumption `expired` → recalcular `confidence_level` do `roi_model` afetado
3. Assumption invalidada por feedback ou outcome → `status = invalidated`; emitir `RoiContradicted`
4. `confidence` da assumption nunca pode ser maior que `reliability_score` da `evidence_link` (se houver)
5. Assumptions sem `risk_if_wrong` são rejeitadas na criação (validação server-side)
6. `owner_id` deve ser humano — agentes não podem ser owners de assumptions

---

# 11. ROI Evidence Rules

As regras a seguir governam como evidência sustenta (ou não) afirmações de ROI.

| Regra | Descrição |
|---|---|
| ER1 | Toda estimativa de valor deve ter pelo menos 1 `roi_evidence_link` |
| ER2 | Toda evidência tem `reliability_score` derivado do `source_tier` (doc 18 §8) |
| ER3 | Fontes Tier 4–5 não sustentam afirmações `high_confidence` de ROI |
| ER4 | Dados fracos (score < 0.4) não sustentam afirmações fortes — mesmo em quantidade |
| ER5 | Hipóteses devem ser separadas de fatos — `roi_hypothesis` ≠ `roi_outcome` |
| ER6 | Limitações devem aparecer em qualquer exibição externa de ROI (propostas, relatórios) |
| ER7 | Evidências contraditórias não podem ser ignoradas — devem ser registradas em `contradiction_ids` |
| ER8 | Evidência stale (Tier 3+ com mais de 18 meses) é downgraded para Tier N+1 para fins de ROI |
| ER9 | Output de Manus citado como evidência de ROI → máximo Tier 4; nunca Tier 1 |
| ER10 | Output de AI tool (Claude, Codex) sobre ROI → não é evidência sem fonte primária verificável |
| ER11 | Metacognik deve revisar qualquer roi_model com `confidence_level = low_confidence` antes de uso externo |

---

# 12. ROI e Cost Ledger

O ROI financeiro começa com custo real — nunca com valor estimado.

## 12.1 Conexão com tabelas de custo (doc 11 §18, §33)

```txt
cost_ledger entries → raw_cost layer do roi_model
credit_transactions (type=debit) → raw_cost layer
credit_reservations → custo comprometido (não confirmado)
usage_events → custo por operação específica (model, tool, collector, agent)
billing_events → custo confirmado de billing
```

## 12.2 Como custo é computado

```txt
total_raw_cost_for_project =
  SUM(cost_ledger.total_cost WHERE project_id = X AND tenant_id = T)
  + SUM(credit_transactions.amount WHERE type='debit' AND project_id = X AND tenant_id = T)
```

Esta operação é feita pelo `roi_projection_engine` — não pelo frontend e não pelo agente de ROI diretamente.

## 12.3 Regras de cost guard

1. `cost_ledger` é append-only — nenhuma mutation retroativa
2. `budget_thresholds` de doc 13 §11 continuam em vigor — ROI não bypassa cost guard
3. Se `raw_cost > estimated_value_mid`: sistema emite aviso `cost_exceeds_estimate`
4. Se `raw_cost > estimated_value_high`: sistema emite `RoiContradicted` automaticamente
5. `credit_reservations` pendentes devem ser incluídas no custo projetado total

---

# 13. ROI e Dashboard

O Project Dashboard (doc 14) exibe ROI como widget de projeção. Dashboard não calcula verdade — exibe `roi_snapshot_projection`.

## 13.1 ROI Snapshot Widget

**O que exibe:**
- Tipo de ROI e título do modelo
- `confidence_level` com cor visual (verde=high, amarelo=medium, laranja=low, vermelho=speculative)
- Custo total realizado (raw_cost) vs. valor estimado midpoint
- ROI ratio: `(estimated_value_mid - raw_cost) / raw_cost × 100%`
- Payback estimate (dias)
- Contador de gaps abertos com severity máxima
- Contador de assumptions ativas e expiradas
- Contador de evidências vinculadas
- `trend_direction` (improving | stable | declining | unknown)
- `metacognik_warnings` (se houver)
- Strategic value summary (quando `roi_type = strategic_roi | brand_roi | decision_quality_roi`)

**O que nunca exibe:**
- `roi_hypothesis` como se fosse fact observado
- Valor monetário de `brand_roi` ou `risk_reduction_roi` sem Founder approval e Tier 1–2 evidence
- ROI de outro tenant (RLS enforced)
- Dados financeiros completos para `project_member` sem permissão (ver §23)

## 13.2 Regras do widget

1. Widget é read-only — toda ação vai para o Command Center como intent
2. Click em "Ver detalhes" → intent `query.roi.detail` emitido ao runtime
3. Click em "Adicionar evidência" → intent `action.roi.add_evidence` emitido ao runtime
4. Widget mostra "Aguardando Dados" quando `confidence_level = insufficient_data`
5. Widget mostra banner de aviso quando ≥1 assumption está expirada
6. Dashboard never renders financial absolute values for `project_member` role (apenas ranges percentuais)

---

# 14. ROI e Command Center

O Command Center (doc 15) processa intenções relacionadas a ROI como qualquer outro tipo de intent — sem lógica própria.

## 14.1 Intenções ROI suportadas (família #8 — ROI, Cost & Usage)

| Intenção em linguagem natural | intent_type | Emits |
|---|---|---|
| "Qual o ROI esperado deste projeto?" | `query.roi.summary` | `IntentSubmitted` → `RoiQueried` |
| "O que mais gerou valor até agora?" | `query.roi.top_value_drivers` | `IntentSubmitted` → `RoiAnalyzed` |
| "O que está custando mais?" | `query.cost.breakdown` | `IntentSubmitted` → `CostQueried` |
| "Esse workflow vale a pena executar?" | `query.roi.workflow_estimate` | `IntentSubmitted` → `RoiEstimated` |
| "Qual hipótese sustenta esse ROI?" | `query.roi.hypothesis_detail` | `IntentSubmitted` → `RoiHypothesisQueried` |
| "Mostre ROI com baixa confiança" | `query.roi.low_confidence_list` | `IntentSubmitted` → `RoiFiltered` |
| "Simule ROI antes de executar" | `action.roi.simulate` | `IntentSubmitted` → `RoiSimulated` |
| "Adicione uma premissa ao ROI" | `action.roi.add_assumption` | `IntentSubmitted` → `RoiAssumptionCreated` |
| "Registre um resultado observado" | `action.roi.record_outcome` | `IntentSubmitted` → `RoiOutcomeRecorded` |
| "Atualize a confiança do ROI" | `action.roi.update_confidence` | `IntentSubmitted` → `RoiConfidenceUpdated` |

## 14.2 Regras do Command Center para ROI

1. `CommandBar` envia intent ao runtime — nunca executa ROI diretamente
2. Resposta do runtime é exibida no Command Center como projeção — não como dado live
3. Intenções financeiras requerem permissão mínima `project_lead` (ver §23)
4. `action.roi.*` (mutações) requerem aprovação per doc 20 §6 para mudanças de modelo aprovado

---

# 15. ROI e Node Canvas

O Node Canvas (doc 16) exibe objetos de ROI como nodes conectados a outros nodes do projeto.

## 15.1 Node Types de ROI

| node_type | O que representa | Criado por | Eventos emitidos |
|---|---|---|---|
| `roi_node` | roi_model completo — o container de ROI | AI-suggested ou manual | `RoiModelCreated`, `RoiSnapshotTaken` |
| `roi_hypothesis_node` | roi_hypothesis a ser validada | AI-suggested ou manual | `RoiHypothesisCreated`, `RoiHypothesisValidated` |
| `roi_gap_node` | roi_gap bloqueando confiança | AI-detected | `RoiGapDetected` |
| `roi_risk_node` | roi_risk à projeção | Manual ou AI | `RoiRiskCreated` |
| `roi_evidence_node` | evidence_item vinculado ao ROI | De research pipeline | `RoiEvidenceLinked` |
| `cost_node` | Visualização de custo de um workflow/agente | De cost_ledger | `CostTracked` |
| `outcome_node` | roi_outcome observado e verificado | Manual (após verificação) | `RoiOutcomeRecorded` |

## 15.2 Edge Types de ROI

| edge_type | Conecta | Direção |
|---|---|---|
| `roi` | cost_node → roi_node | custo contribui para ROI |
| `cost` | workflow/agent node → cost_node | workflow gera custo |
| `evidence` | roi_evidence_node → roi_node | evidência suporta ROI |
| `risk` | roi_risk_node → roi_node | risco afeta ROI |
| `decision` | roi_node → decision node | ROI informa decisão |
| `blocked_by` | roi_node → roi_gap_node | gap bloqueia confiança |
| `contradicts` | roi_evidence_node → roi_hypothesis_node | evidência invalida hipótese |
| `validates` | roi_outcome_node → roi_hypothesis_node | outcome valida hipótese |

## 15.3 Regras do Node Canvas para ROI

1. Canvas exibe `confidence_level` como badge visual em cada `roi_node`
2. `roi_node` com `speculative` confidence mostra badge vermelho com aviso
3. Side panel de `roi_node` exibe: assumptions, evidence, gaps, risks, outcomes, Metacognik warnings
4. Canvas não calcula ROI — exibe `roi_snapshot_projection`
5. Criar `roi_node` manual emite evento + audit_log entry

---

# 16. ROI e Propostas

ROI entra em propostas como evidência governada — não como promessa.

## 16.1 Regras de uso de ROI em proposta

| Regra | Descrição |
|---|---|
| PR1 | Apenas roi_models com `confidence_level ≥ medium_confidence` podem aparecer em proposta |
| PR2 | Todo valor estimado em proposta deve ter `confidence_level` explícito |
| PR3 | Cenários (low/mid/high) devem ser exibidos — não apenas o midpoint |
| PR4 | Lista de assumptions ativas deve aparecer em seção de "Premissas e Limitações" |
| PR5 | `roi_gaps` significativos devem ser declarados explicitamente |
| PR6 | Nunca prometer `observed_value` sem roi_outcome verificado que o suporte |
| PR7 | ROI de `brand_roi` e `risk_reduction_roi` em moeda requer Founder approval antes de incluir |
| PR8 | Uso de ROI em proposta formal requer QA review (doc 20 §19) + Founder sign-off |

## 16.2 Template de seção ROI em proposta

```txt
## Valor Estimado

**Tipo de ROI:** [financial_roi | operational_roi | ...]
**Estimativa (cenários):**
  - Conservador: R$ [low]
  - Base: R$ [mid]
  - Otimista: R$ [high]
**Confiança:** [Medium / Low] — baseado em [N] evidências e [N] premissas
**Payback estimado:** [X dias] (baseado em premissas abaixo)

### Premissas
1. [assumption_text] — Owner: [owner] — Expira: [date]
2. ...

### Limitações
- [roi_gap description]
- [risk_description]
- Este valor é uma estimativa baseada em dados disponíveis em [date].
  Resultados reais dependem de [fatores externos].
```

---

# 17. ROI e Feedback

Feedback (doc 22) é um sinal de ajuste do ROI — tanto para validar quanto para contradizer.

## 17.1 Como feedback afeta ROI

| Tipo de feedback | Efeito no ROI |
|---|---|
| Feedback positivo sobre entrega (qualidade, valor percebido) | Suporte a `roi_hypothesis`; pode aumentar confidence |
| Feedback negativo sobre entrega (retrabalho, insatisfação) | Contradição de `roi_hypothesis`; reduz confidence |
| Feedback sobre custo (percepção de que custou mais do que gerou) | Cria `roi_gap` ou `roi_risk` |
| Feedback implícito (reabertura de node, override de agente) | Sinal de eficiência_roi negativo |
| Feedback de proposta aceita | Suporte a `acquisition_roi` |
| Feedback de proposta rejeitada | Potencial contradição de `roi_hypothesis` |
| Feedback sobre velocidade de entrega | Sinal de `time_to_decision_roi` ou `operational_roi` |

## 17.2 Fluxo de feedback → ROI

```txt
FeedbackSubmitted (event)
  → feedback_analysis_agent avalia relevância para roi_models do projeto
  → Se relevante: emite RoiEvidenceLinked (evidência = feedback_item) ou RoiContradicted
  → roi_model.confidence_level é recalculado
  → roi_snapshot_projection é invalidada e regenerada
  → Dashboard widget atualizado
```

---

# 18. ROI e Support

Support tickets (doc 23) revelam custo operacional oculto e fricção — insumo para `operational_roi` e `risk_reduction_roi`.

## 18.1 Como support alimenta ROI

| Sinal de support | ROI impactado |
|---|---|
| Ticket sobre workflow lento ou bloqueio | `operational_roi` — custo de fricção identificado |
| Ticket sobre erro repetitivo de agente | `efficiency_roi` negativo — custo de erro |
| Ticket sobre dificuldade de uso da UI | `retention_roi` negativo — risco de churn |
| Ticket sobre custo inesperado | `financial_roi` — custo real vs. estimado |
| Ticket resolvido rapidamente com alta satisfação | `retention_roi` positivo |
| Friction signal detectado automaticamente | `operational_roi` — custo de fricção mapeado |

## 18.2 Fluxo support → ROI

```txt
support_tickets (friction_signals) → support_analysis_agent
  → Detecta padrão de custo operacional oculto
  → Cria ou atualiza roi_model do tipo operational_roi
  → Emite RoiGapDetected (se o custo não estava no modelo) ou RoiOutcomeRecorded (se custo realizado)
  → roi_snapshot regenerado
```

---

# 19. ROI e Research

Research (doc 18) fornece as evidências de base que sustentam assumptions e hipóteses de ROI.

## 19.1 O que research alimenta

| Tipo de dado de research | Uso no ROI |
|---|---|
| Benchmark de mercado | `roi_assumption` (baseline de mercado) |
| Dado acadêmico ou científico | `roi_evidence_link` Tier 1–2 |
| Dado de competidor | `roi_assumption` (referência de mercado) |
| Comparação de pricing | `financial_roi` baseline |
| Padrão de indústria | `roi_assumption` + `roi_evidence_link` |
| Research de usuário (próprio) | `roi_evidence_link` Tier 2 |

## 19.2 Regras de research como evidência de ROI

1. Toda evidência de research deve ter `source_tier` (1–5 per doc 18 §8)
2. Research com `reliability_score < 0.5` não sustenta `medium_confidence` ou superior
3. Research com `is_stale = true` → tier downgraded automaticamente; roi_model notificado
4. Research run usado como base de ROI deve ser referenciado em `roi_evidence_link`
5. Metacognik de doc 18 e de ROI devem ser consistentes — contradiction cross-domain é reportada

---

# 20. ROI e Evals

O sistema de Evals (doc 13) avalia a qualidade do próprio sistema de ROI — não apenas os projetos que ele analisa.

## 20.1 O que Evals deve medir no sistema de ROI

| Eval Target | O que mede | Threshold MVP |
|---|---|---|
| `roi_reasoning_quality` | Qualidade do raciocínio do agente ao construir ROI | ≥ 0.70 |
| `evidence_coverage` | Proporção de claims com evidence_links | ≥ 0.80 |
| `assumption_clarity` | Clareza e especificidade das assumptions | ≥ 0.75 |
| `risk_visibility` | Proporção de risks documentados vs. gaps abertos | ≥ 0.70 |
| `confidence_accuracy` | Calibration: confidence declarada vs. outcome real | ≥ 0.65 |
| `outcome_tracking_rate` | % de roi_models com roi_outcome após prazo | ≥ 0.50 (P0) |
| `metacognik_review_rate` | % de low/speculative models revisados por Metacognik | 1.00 (obrigatório) |
| `assumption_expiry_rate` | % de assumptions com expiration_at definido | 1.00 (obrigatório) |

## 20.2 Como eval impacta ROI

- Se `confidence_accuracy < 0.5`: sistema emite aviso de calibração; Metacognik notificado
- Se `evidence_coverage < 0.6`: roi_model é downgraded automaticamente para `low_confidence`
- `metacognik_review_rate < 1.0` para `speculative` models → bloqueio de exibição em proposta

---

# 21. ROI State Machine

11 estados formais para o ciclo de vida de um roi_model.

```txt
States:
  proposed           — roi_model criado; sem métricas ou evidências ainda
  estimating         — evidências e assumptions sendo coletadas
  awaiting_data      — gaps identificados; aguardando dados externos ou outcomes
  low_confidence     — estimativa existe mas confidence_level = low ou speculative
  ready_for_review   — critérios de medium+ confidence atingidos; submetido para Metacognik/Founder
  approved           — revisado e aprovado por atores requeridos (ver §23)
  active             — ROI sendo monitorado; outcomes esperados dentro do time_horizon
  observed           — roi_outcome(s) verificados registrados; ROI realizável calculável
  contradicted       — evidência ou outcome contradiz o modelo; revisão requerida
  expired            — time_horizon passou sem outcome suficiente; modelo arquivado
  archived           — arquivado explicitamente (substituído por novo modelo ou projeto encerrado)

Transições:
  proposed         → estimating          (primeiro roi_assumption ou roi_evidence_link criado)
  estimating       → awaiting_data       (roi_gap com severity=blocking detectado)
  estimating       → low_confidence      (estimativa existe mas confidence_level = low|speculative)
  estimating       → ready_for_review    (confidence_level = medium+ e submission feita)
  awaiting_data    → estimating          (gap resolvido ou dado externo recebido)
  low_confidence   → estimating          (nova evidência ou assumption adicionada)
  low_confidence   → ready_for_review    (confidence upgrade para medium+)
  ready_for_review → approved            (aprovação por atores requeridos)
  ready_for_review → low_confidence      (Metacognik veto ou evidência insuficiente)
  approved         → active              (projeto em execução com ROI monitorado)
  active           → observed            (roi_outcome verificado registrado)
  active           → contradicted        (RoiContradicted emitido por feedback ou outcome adverso)
  active           → expired             (time_horizon ultrapassado sem outcome)
  observed         → contradicted        (novo dado contradiz outcomes anteriores)
  contradicted     → estimating          (revisão iniciada com novos dados)
  expired          → archived            (nenhuma ação de revisão tomada)
  any              → archived            (arquivamento explícito por PMO_CKOS ou Founder)
```

---

# 22. ROI Events

16 eventos formais conectados ao event bus de doc 10.

| Evento | Publisher | Subscribers | Schema |
|---|---|---|---|
| `RoiModelCreated` | roi_agent ou manual | roi_projection_engine, dashboard | model_id, roi_type, project_id, tenant_id |
| `RoiTypeSelected` | roi_agent | roi_projection_engine | model_id, roi_type |
| `RoiAssumptionCreated` | roi_agent ou manual | roi_projection_engine | assumption_id, model_id, confidence, expiration_at |
| `RoiAssumptionExpired` | scheduler | roi_projection_engine, dashboard | assumption_id, model_id, affected_metrics |
| `RoiEvidenceLinked` | roi_agent ou research_pipeline | roi_projection_engine | evidence_link_id, model_id, evidence_item_id, evidence_type |
| `RoiEstimateGenerated` | roi_calculation_engine | roi_projection_engine | model_id, value_low, value_mid, value_high, confidence_level |
| `RoiConfidenceUpdated` | roi_calculation_engine | roi_projection_engine, dashboard | model_id, old_confidence, new_confidence, reason |
| `RoiGapDetected` | roi_agent ou Metacognik | roi_projection_engine, dashboard | gap_id, model_id, severity, gap_type |
| `RoiRiskCreated` | roi_agent ou manual | roi_projection_engine | risk_id, model_id, likelihood, impact |
| `RoiReviewRequested` | pmo_ckos | metacognik, founder | model_id, confidence_level, review_type |
| `RoiApproved` | founder ou metacognik | roi_projection_engine, audit_log | model_id, approved_by, timestamp |
| `RoiSnapshotTaken` | roi_projection_engine | dashboard, canvas | snapshot_id, model_id, confidence_level, cost_total, value_mid |
| `RoiOutcomeRecorded` | manual (verified) | roi_projection_engine, dashboard | outcome_id, model_id, value_observed, verified_by |
| `RoiHypothesisValidated` | roi_agent | roi_projection_engine | hypothesis_id, model_id, evidence_count |
| `RoiHypothesisInvalidated` | roi_agent ou Metacognik | roi_projection_engine, dashboard | hypothesis_id, model_id, contradiction_source |
| `RoiContradicted` | roi_agent ou Metacognik | roi_projection_engine, dashboard, pmo_ckos | model_id, contradiction_source, old_confidence, trigger |

**Regras de eventos:**
- Todos os eventos passam pelo event bus de doc 10 §5.3
- Nenhum evento é emitido diretamente do frontend
- Todo evento tem: `event_id`, `tenant_id`, `project_id`, `timestamp`, `source_agent_or_actor`
- `audit_log` entry para cada evento que muta estado de `roi_model`

---

# 23. ROI Permissions

## 23.1 Matriz de permissões por dado de ROI

| Dado | Roles com acesso | Restricao |
|---|---|---|
| `roi_model` (full — valores absolutos) | founder, admin, finance_admin, project_lead | RLS por tenant_id + project_id |
| `roi_model` (redacted — apenas ranges %) | project_member, analyst | Valores absolutos ocultos |
| `cost_total` (raw_cost) | founder, admin, finance_admin, project_lead | Não visível para project_member |
| `roi_assumptions` (lista completa) | project_lead+, admin, founder | project_member vê apenas contagem |
| `roi_gaps` (lista completa) | project_lead+, admin, founder, metacognik | |
| `roi_risks` (lista completa) | project_lead+, admin, founder, metacognik | |
| `roi_outcomes` (valores verificados) | project_lead+, admin, founder | project_member vê se outcome é positivo/negativo apenas |
| **Vista de cliente** | Apenas excerpt aprovado por Founder | Sem valores absolutos; apenas ranges e indicadores |
| **Vista externa (proposta)** | Excerpt aprovado por Founder com seção de limitações | Ver §16 |

## 23.2 Aprovação de ROI por tipo

| Decisão | Requer |
|---|---|
| Aprovar roi_model para uso em proposta | Founder + Metacognik |
| Exibir `financial_roi` com valores absolutos para cliente | Founder approval explícita |
| Converter `brand_roi` ou `risk_reduction_roi` para moeda | Founder + evidência Tier 1–2 |
| Validar roi_hypothesis como "validated" | QA Lead (ou Metacognik para modelos complexos) |
| Arquivar roi_model | Project Lead ou PMO_CKOS |
| Alterar confidence_level manualmente | Metacognik (para downgrades) ou QA Lead (upgrades com evidência) |

## 23.3 Cross-tenant isolation

- RLS em todas as tabelas de ROI (`roi_models`, `roi_metrics`, `roi_snapshots`, `roi_hypotheses`, `roi_assumptions`, `roi_evidence_links`, `roi_outcomes`, `roi_gaps`, `roi_risks`, `roi_decision_links`)
- Agentes de ROI nunca têm acesso cross-tenant
- `roi_projection_engine` aplica `tenant_id` como pré-condição de qualquer query

---

# 24. ROI QA

## 24.1 Conexão com Doc 20

O ROI Architecture está sujeito ao Gate System de doc 20. Em particular:

- **Gate A (Documentation):** Este doc deve estar em status aprovado antes de Gate I
- **Gate I (Business Systems):** Todos os business system docs (21–24) passam pelo Gate I; ROI Architecture é pré-requisito
- **Gate K (Release):** ROI widget no Dashboard é parte do MVP P0 scope; incluso no Release Readiness Checklist

## 24.2 Checklist específico de ROI QA

| # | Critério | Verificador |
|---|---|---|
| RQ1 | Nenhum roi_model exibido sem confidence_level visível | QA Lead |
| RQ2 | Nenhum roi_model com speculative confidence em proposta aprovada | Metacognik |
| RQ3 | Nenhuma roi_hypothesis marcada como validated sem evidence_links | Metacognik |
| RQ4 | Nenhum valor de ROI em moeda sem evidence_link de reliability_score ≥ 0.6 | Metacognik |
| RQ5 | Nenhuma premissa sem risk_if_wrong (validação server-side) | Technical |
| RQ6 | Nenhuma premissa expirada contribuindo ativamente para estimativa | Technical |
| RQ7 | Dados financeiros de cliente protegidos por RLS e permissão explícita | Technical |
| RQ8 | Metacognik revisou todos os modelos com low_confidence antes de uso externo | Metacognik |
| RQ9 | roi_gaps com severity=blocking impedem upgrade para high_confidence | Technical |
| RQ10 | Cost total sempre inclui raw_cost layer antes de qualquer valor estimado | Technical |

## 24.3 Critérios de rejeição automática para ROI

- ROI exibido em proposta sem `confidence_level` label → rejeição automática (doc 20 §25.1)
- `roi_hypothesis` marcada como `validated` sem `evidence_links` → rejeição automática
- `roi_model.estimated_value_mid > 0` com `evidence_count = 0` → rejeição automática
- Output de AI agent sobre ROI usado como `evidence_item` sem fonte primária → rejeição (doc 20 §23 AI7)

---

# 25. MVP P0

## 25.1 Em escopo para P0

| Componente | Escopo P0 |
|---|---|
| roi_model | Criação manual ou AI-suggested para projetos ativos |
| roi_types | 3 tipos: `financial_roi`, `operational_roi`, `content_roi` |
| roi_assumption | Registro manual com owner e expiration |
| roi_evidence_link | Vinculação a evidence_items do pipeline de pesquisa |
| roi_snapshot | Geração por evento; polling (não SSE) em P0 |
| roi_gap | Detecção e registro manual; AI-detected em P1+ |
| confidence_level | Display com 5 níveis; bloqueios automáticos por nível |
| ROI widget no Dashboard | Snapshot básico: confidence + custo + valor + gaps + warnings |
| /roi intent no Command Center | 3 intenções: `query.roi.summary`, `query.cost.breakdown`, `action.roi.add_assumption` |
| roi_node no Node Canvas | Exibição com badge de confidence |
| Metacognik warning | Para speculative e low_confidence |
| cost_ledger connection | raw_cost layer sempre calculado |

## 25.2 Fora do escopo P0 (adiado)

| Componente | Por que adiado |
|---|---|
| Forecasting avançado (cenários probabilísticos) | Requer histórico de dados longitudinal |
| BI completo (relatórios exportáveis, PDF) | Gate F completo requerido |
| Atribuição multicanal complexa | Requer integração com dados externos (Gate H) |
| brand_roi em moeda | Requer evidência Tier 1–2 + Founder approval |
| financial modeling avançado (TIR, VPL) | Requer integração contábil (doc 24) |
| Integração contábil (ERP, SAP) | Fora do escopo CKOS (sistema externo) |
| roi_types: strategic, brand, acquisition, retention, efficiency, learning, risk_reduction, decision_quality, time_to_decision | P1+ |
| roi_outcome tracking automático | P1 — P0 é manual apenas |
| SSE streaming do roi_projection | P1 — P0 é polling-based |
| roi_decision_link | P1 — requer sistema de decisões formais |

---

# 26. Failure Modes

| # | Failure Mode | Sintoma | Mitigação |
|---|---|---|---|
| FM-R1 | ROI prometido sem evidência | `estimated_value_mid > 0` com `evidence_count = 0` | Rejeição automática; validação server-side |
| FM-R2 | Métrica financeira em projeto sem baseline financeiro | financial_roi criado sem custo_baseline documentado | Validação de tipo na criação; QA Lead bloqueia |
| FM-R3 | Assumption expirada contribuindo para estimativa | `assumption.expiration_at < now()` mas status ≠ expired | Scheduler event automático; recalculate confidence |
| FM-R4 | Fonte fraca sustentando claim forte | `evidence_item.reliability_score < 0.4` em high_confidence ROI | ER3 e ER4: bloqueio por evidence rules |
| FM-R5 | Custo omitido do cálculo de ROI | raw_cost_layer não inclui credit_transactions ou usage_events | Regra DM: cost_ledger sempre incluso; Technical QA |
| FM-R6 | Crédito consumido sem conexão de valor | credit_debit sem roi_evidence_link associado | Relatório de eficiência de crédito no Dashboard |
| FM-R7 | Dashboard apresenta ROI como verdade absoluta | Widget sem confidence badge, sem assumption count | Widget template obrigatório; QA Lead valida |
| FM-R8 | Cliente vê dado financeiro sensível | RLS falha ou permissão incorreta | RLS obrigatório; Security QA; Technical review |
| FM-R9 | ROI confundido com faturamento | `estimated_value` interpretado como receita bruta | Documentação clara de "valor líquido vs. custo"; training |
| FM-R10 | Feedback contradiz ROI mas modelo não é atualizado | `FeedbackSubmitted` ignorado pelo roi_agent | Subscriber de feedback no roi_agent; RoiContradicted emitido |
| FM-R11 | Support revela custo oculto não no ledger | Custo manual ou externo não rastreado | Support → roi_gap pipeline; PM registra manualmente |
| FM-R12 | Benchmark ruim como base de ROI | Tier 4 benchmark usado como Tier 1 | ER9 e source_tier enforcement; Metacognik review |
| FM-R13 | Research stale sustentando assumption | Research > 18 meses usada como primária | ER8: tier downgrade automático; staleness flag |
| FM-R14 | Collector falha silenciosamente | Apify/Perplexity falha → gap não detectado | `SourceCollectionFailed` event → roi_gap criado |
| FM-R15 | Confidence score inflado | Agente declara `high_confidence` sem cumprir critérios | §9 critérios automáticos; Metacognik audit |
| FM-R16 | Metacognik não acionado em ROI especulativo | `speculative` model em proposta sem revisão | Regra: `metacognik_review_rate = 1.0` para speculative |
| FM-R17 | ROI não atualizado após outcome observado | `roi_outcome` registrado mas `roi_model.status` permanece `active` | `RoiOutcomeRecorded` event → trigger de atualização de confidence |
| FM-R18 | ROI duplicado para o mesmo projeto | Dois `roi_models` do mesmo tipo sem diferenciação clara | Validação de unicidade por `project_id + roi_type`; QA check |
| FM-R19 | ROI sem owner | `roi_model.owner_id = null` | Campo obrigatório na criação; validação server-side |
| FM-R20 | ROI usado para vender promessa falsa | `speculative` ou `low_confidence` ROI apresentado sem avisos em proposta | Bloqueio por confidence level (§9); PR1 + PR2 rules |
| FM-R21 | roi_gap com severity incorrect | Gap `blocking` marcado como `minor`; confidence não downgraded | Metacognik review; severity validation |
| FM-R22 | roi_hypothesis validada sem evidência | `status = validated` sem evidence_links | Validação server-side; rejeição automática |

---

# 27. Required Patches

Os patches abaixo foram identificados durante a criação deste documento. Estão **registrados como sugestões** — não aplicados. Requerem decisão de Technical + PMO_CKOS antes de aplicar.

| Patch | Doc alvo | Versão alvo | Descrição | Urgência |
|---|---|---|---|---|
| **P21-1** | `11_DATA_MODEL_AND_PERSISTENCE.md` | v1.3.x | Adicionar tabela `roi_gaps` ao §30 ROI System Data Model (schema: id, roi_model_id, tenant_id, gap_description, gap_type, severity, resolution_action, owner_id, status, resolved_at, created_at, updated_at) | Antes de Gate I |
| **P21-2** | `11_DATA_MODEL_AND_PERSISTENCE.md` | v1.3.x | Adicionar tabela `roi_risks` ao §30 (schema: id, roi_model_id, tenant_id, risk_description, risk_type, likelihood, impact, risk_score, mitigating_action, owner_id, status, materialized_at) | Antes de Gate I |
| **P21-3** | `11_DATA_MODEL_AND_PERSISTENCE.md` | v1.3.x | Adicionar tabela `roi_decision_links` ao §30 (schema: id, roi_model_id, decision_id, tenant_id, link_type, decision_context, decision_outcome, value_realized) | Antes de Gate J |
| **P21-4** | `10_SYSTEM_RUNTIME_ARCHITECTURE.md` | v1.2.x | Adicionar `roi_projection_engine` como componente nomeado do runtime (similar a como `research_projection_engine` aparece em doc 18 §5) | Antes de Gate I |
| **P21-5** | `11_DATA_MODEL_AND_PERSISTENCE.md` | v1.3.x | Verificar e formalizar a `roi_snapshot_projection` em §21 (campo trend_direction, metacognik_warnings, expired_assumption_count) — pode já existir parcialmente do P11-2 | Antes de Gate F |
| **P21-6** | `13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md` | v1.2.x | Adicionar `roi_reasoning_quality`, `evidence_coverage`, `confidence_accuracy`, `outcome_tracking_rate` como eval targets formais no §4 | Antes de Gate G |

> Os patches acima são sugeridos e registrados em ARCHITECTURE_PATCH_REPORT.md §21.
> **Não aplicar** sem aprovação Technical + PMO_CKOS e versão incremental nos docs afetados.

---

# 28. Related Notes

- [[10_SYSTEM_RUNTIME_ARCHITECTURE]] — event bus, projection engine, runtime components
- [[11_DATA_MODEL_AND_PERSISTENCE]] — tabelas roi_models/metrics/snapshots/hypotheses/assumptions/evidence_links/outcomes (§30), cost_ledger (§18), credit_transactions (§33), roi_snapshot_projection (§21)
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]] — RLS, RBAC, permissões de dados financeiros
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]] — cost guard, eval targets, learning loop
- [[14_PROJECT_DASHBOARD_ARCHITECTURE]] — ROI Snapshot widget, dashboard projections
- [[15_COMMAND_CENTER_ARCHITECTURE]] — família de intenção #8 ROI, Cost & Usage; slash commands /roi /cost
- [[16_NODE_CANVAS_ARCHITECTURE]] — roi_node, cost_node, outcome_node, edge types de ROI
- [[17_IMPLEMENTATION_PROTOCOL]] — Gate I (Business Systems), roadmap de ondas
- [[18_RESEARCH_PROTOCOL]] — evidence_items como base de ROI; source_tier; reliability_score
- [[20_QA_AND_FOUNDER_APPROVAL_PROTOCOL]] — Gate I criteria; ROI QA checklist §19; rejection criteria
- [[22_FEEDBACK_SYSTEM_ARCHITECTURE]] — feedback como sinal de ROI
- [[23_SUPPORT_SYSTEM_ARCHITECTURE]] — support como custo operacional de ROI
- [[24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE]] — financial_roi como base de billing
- [[ARCHITECTURE_PATCH_REPORT]] — patches P21-1 a P21-6; gate status de Business Systems
