---
title: Evals, Observability and Cost Control
file: 13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
phase: 03_RUNTIME_SYSTEM
category: runtime_observability
version: 1.1.0
status: draft
owner: PMO_CKOS
responsible_agent: QA Lead
reviewers:
  - metacognik
  - qa_lead
approval_required:
  - founder
  - technical
  - metacognik
purpose: Camada de confiança operacional do CKOS — evals por agente/skill/workflow/RAG/modelo/output; observabilidade de custo, qualidade e segurança; loop detection; quality gates; audit Metacognik e QA Lead; run replay para incident review; learning loop metrics; alertas P0–P3; dashboards internos.
inputs: Runtime (10 v1.1.0) — eval_runner, cost_guard, loop_detector, evalRegistry, costPolicyRegistry, model_router; Data Model (11 v1.1.1) — eval_results, eval_scores, cost_ledger, model_calls, run_replays, audit_logs, hallucination_checks, learning tables; Security (12 v1.1.0) — 14 tipos de evento de segurança, severidades P0–P3, approval policies.
outputs: Evals por 14 target kinds; 14 tipos de score; cost per run/workflow/project/model/agent/tool/collector; quality gates em 8 pontos críticos; alertas P0–P3; 10 dashboards internos; incident replay; 18 métricas de performance; learning loop; MVP P0 observability scope.
framework: eval_runner (executa evals) + cost_guard (impõe limites) + loop_detector (detecta ciclos) + learning_loop_engine (agrega outcomes) + Metacognik (audit de risco) + QA Lead (review de qualidade) + audit_logs como fonte de verdade de segurança.
edge_cases: Output bom sem evidência; modelo caro performando mal; RAG correto de tenant errado; custo estoura no meio do run; eval LLM-as-judge discorda de humano; artifact aprovado depois de dado obsoleto; segurança bloqueia workflow legítimo; loop de agentes invisível.
integrations: eval_runner + cost_guard + loop_detector (10 §5.15); eval_results + cost_ledger + model_calls + run_replays + audit_logs (11); security events (12 §5.21); learning tables (11 §24); OpenRouter (custo/modelo); vault/redação (12 §5.15).
prompts: Prompt de eval LLM-as-judge; prompt de hallucination check; prompt de evidence coverage score.
metrics: trace completeness ≥ 99%; evidence coverage ≥ 80%; avg confidence ≥ 0.75; hallucination risk ≤ 5%; retrieval relevance ≥ 0.7; policy violation rate → 0; approval bottleneck ≤ 10%; agent success rate ≥ 85%.
related_notes:
  - 10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - 11_DATA_MODEL_AND_PERSISTENCE.md
  - 12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md
  - ../05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md
  - ../05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md
tags: [runtime, evals, observability, cost_control, quality, security_observability, run_replay, loop_detection, learning_loop, metacognik_audit, model_router]
---

> **Nota de categoria:** `runtime_observability` não está no enum de categorias do template v2.2.0. Registrado como **patch sugerido para `00_DOCUMENT_TEMPLATE.md §8`** — adicionar `runtime_observability` ao lado de `evals`. Não alterar governança sem autorização explícita.

# 1. Propósito

Definir como o CKOS **sabe se está funcionando** — se a IA está acertando, se um agente está errando, se um workflow está caro, se uma resposta não tem evidência, se o RAG está ruim, se um modelo está degradando, se um agente entrou em loop, se um collector falhou, se houve risco de segurança, se uma policy foi violada, se uma aprovação foi burlada, se o custo passou do limite, ou se um output precisa ser bloqueado por Metacognik ou QA Lead.

Sem esta camada, um sistema agêntico acumula custo silencioso, regressão de qualidade invisível e incidentes de segurança não detectados — até virar falha de produto ou responsabilidade jurídica. O doc 13 é a **camada de confiança operacional**: o sistema só é confiável se puder ser medido, auditado e corrigido.

# 2. Função dentro do CKOS

```txt
doc 10 (Runtime)   → executa    │
doc 11 (Data Model) → persiste   ├─→ doc 13 MEDE, AUDITA, ALERTA, BLOQUEIA, APRENDE
doc 12 (Security)  → protege    │
doc 25 (Self-Evolving) ← aprende ← doc 13 alimenta
```

- **Runtime (10)**: `eval_runner`, `cost_guard`, `loop_detector` e `learning_loop_engine` são engines definidos em 10 §5.15 e 5.23-5.28; este doc especifica **o que medir e como agir** sobre o que esses engines retornam.
- **Data Model (11)**: tabelas `eval_results`, `eval_scores`, `cost_ledger`, `model_calls`, `run_replays`, `audit_logs`, `hallucination_checks`, `learning tables` são a persistência; este doc define **as queries, thresholds e alertas** sobre elas.
- **Security (12)**: os 14 eventos de segurança definidos em 12 §5.21 se tornam **métricas, alertas e SLAs** neste doc.
- **Self-Evolving (25)**: as métricas de performance de agentes, skills, prompts e workflows produzidas por este doc são o **substrato** das decisões de melhoria do sistema.

# 3. Observability Principles

Os sete princípios que governam toda a camada de observabilidade do CKOS:

1. **Everything important emits events.** Toda ação relevante de agente, tool, workflow, coletor, modelo e aprovação gera evento estruturado no event store (11 §7). Sem evento = sem rastreabilidade = sem auditoria.

2. **Every run must be traceable.** Cada `agent_run` e `workflow_run` tem `trace_id`, `correlation_id` e `causation_id`. A cadeia causal completa é reconstituível via `run_replays` (11 §22) sem logging paralelo — o event store é a única fonte de verdade.

3. **Every output must be evaluable.** Todo `agent_output` com `schema_id` passa por eval de contrato (schema compliance). Todo output estratégico, gerado por skill de risco médio ou alto, passa por eval de qualidade (evidence coverage, hallucination check, contradiction check).

4. **Every cost must be attributable.** Cada unidade de custo (model token, tool call, collector run) é registrada em `cost_ledger` com `scope`, `scope_ref` e `source_event_id`. Custo anônimo não existe.

5. **Every security incident must be reconstructable.** Os 14 eventos de segurança de 12 §5.21 persistem em `audit_logs` com snapshot de contexto. Qualquer incidente pode ser reconstruído via `run_replays` até o evento que o causou.

6. **Every model decision must be explainable.** `model_calls` (11 §8) registra `model_id`, `prompt_id`, `tokens_in/out`, `cost_usd`, `latency_ms`, `fallback_of`. O `model_router` registra a política aplicada. Nenhuma escolha de modelo é opaca.

7. **Every critical action must have approval/audit trail.** Ações com `risk_level ≥ medium` ou `reversible = false` têm `approval_ref` em `approvals` (11 §16) e entrada em `audit_logs`. Sem trilha = sem confiança.

# 4. Eval Architecture

O `eval_runner` (10 §5.15) executa evals registrados no `evalRegistry` contra os seguintes target kinds:

| Target Kind | Fonte de dados principal (doc 11) | Trigger padrão |
|---|---|---|
| `agent` | `agent_runs`, `agent_eval_results`, `agent_outputs` | fim de cada `agent_run` |
| `subagent` | `agent_runs` (subtype) | fim de cada subagent run |
| `skill` | `skill_performance` (§24) + `agent_runs` com `skill_id` | batch diário / on demand |
| `workflow` | `workflow_runs`, `workflow_performance` (§24) | fim de cada `workflow_run` |
| `prompt` | `prompt_performance` (§24) + `model_calls.prompt_id` | batch diário |
| `instruction` | `instructionRegistry` + agente que a usou | revisão periódica |
| `transformer` | `run_steps` com transformer + output schema | fim de transformer step |
| `rag` | `rag_queries`, `rag_results`, `retrieval_logs` | cada `rag_query` |
| `context_pack` | `context_packs`, `context_budget_logs` | criação do context pack |
| `model_output` | `model_calls`, `agent_outputs` | por model_call com risco médio+ |
| `collector_output` | `collector_runs`, `collector_normalized_records` | fim de `collector_run` |
| `artifact` | `artifacts`, `artifact_approval_status` | geração + pré-aprovação |
| `decision` | `decisions`, `decision_evidence_links` | registro de cada decisão |
| `approval` | `approvals`, `approval_events` | resolução de approval |
| `ui_projection` | `ui_projections` | atualização de projeção |

**Persistência de eval (tabelas doc 11 §19):**

```txt
evals(id, eval_key, target_kind, criteria_ref, baseline jsonb, status)
eval_criteria(id, eval_id fk, name, weight, type enum(assertion|rubric|metric))
eval_results(id, eval_id fk, target_run_id, target_kind, passed bool, created_at)
eval_scores(id, eval_result_id fk, metric, score numeric)
eval_failures(id, eval_result_id fk, criterion, detail jsonb)
eval_recommendations(id, eval_result_id fk, recommendation text)
quality_regressions(id, target_kind, target_ref, baseline, current, delta, detected_at)
hallucination_checks(id, agent_run_id fk, claims, ungrounded, risk, created_at)
contradiction_checks(id, agent_run_id fk, contradictions, detail jsonb, created_at)
evidence_coverage_scores(id, agent_run_id fk, claims, with_evidence, coverage, created_at)
```

# 5. Eval Types

| Tipo de eval | Descrição | Quem executa | Trigger |
|---|---|---|---|
| **Deterministic check** | Assertion binária sobre schema, formato, presença de campo obrigatório | `eval_runner` automático | todo output |
| **Schema compliance** | Output valida contra `schema_id` do `schemaRegistry` (10 §5.20) | `eval_runner` | todo `agent_output` com schema |
| **Evidence coverage score** | % de afirmações do output com evidência rastreável (`evidence_coverage_scores`) | `eval_runner` | outputs de risco médio+ |
| **Hallucination check** | Claims sem grounding em evidência/memória/RAG disponível | `eval_runner` (LLM-as-judge ou heurístico) | outputs estratégicos |
| **Contradiction detection** | Afirmação contradiz outra na mesma sessão/projeto (`contradiction_checks`) | `eval_runner` | outputs que referenciam decisões anteriores |
| **LLM-as-judge** | Modelo avalia qualidade de outro output por rubrica | `eval_runner` (modelo separado) | artifacts, propostas, outputs de alto risco |
| **Human review** | QA Lead ou operador revisa manualmente | QA Lead / operador | artifacts críticos, saídas para cliente |
| **Metacognik audit** | Avaliação metacognitiva de risco, confiança e coerência | Metacognik | risco alto, contradição, output estratégico |
| **QA Lead review** | Revisão técnica de qualidade de implementação | QA Lead | builds, migrations, workflows novos |
| **Policy compliance** | Output ou ação respeita as policies de 12 | `policy_engine` (10 §5.15) | toda ação de impacto |
| **Confidence scoring** | Score numérico de confiança do agente no output | agente + `eval_runner` | todo `agent_run` |
| **Uncertainty scoring** | Score de incerteza (complementar ao confidence) | `eval_runner` | outputs com alto risco |
| **Freshness scoring** | `memories.freshness_at` vs threshold por tipo de dado | `eval_runner` | RAG + context pack |
| **Source reliability scoring** | `source_reliability_scores` (11 §15) por tipo de fonte | `eval_runner` | toda recuperação de evidência |

# 6. Agent Eval Layer

Para cada `agent_run` completado, o `eval_runner` avalia:

| Dimensão | Métrica | Tabela doc 11 | Threshold padrão |
|---|---|---|---|
| **Task success** | run completado sem erro crítico | `agent_runs.state = completed` | 100% |
| **Output quality** | score de eval do output (rubrica) | `eval_scores.metric = output_quality` | ≥ 0.75 |
| **Adherence to role** | ações dentro de `agents.allowed_object_types` + `forbidden_actions` | `agent_permissions` + `agent_eval_results` | 100% |
| **Tool usage correctness** | tools usadas ∈ `agent.tools` ∩ `skill.allowed_tools` | `tool_calls.status` | 100% sem violação |
| **Context usage** | tokens usados ≤ budget; sources relevantes | `context_budget_logs` | tokens ≤ max_tokens |
| **Evidence usage** | evidence_coverage_score das afirmações | `evidence_coverage_scores` | ≥ 0.80 |
| **Policy compliance** | 0 `PermissionDenied` durante o run | `audit_logs` filtrado por `agent_run` | 0 violations |
| **Cost efficiency** | `agent_costs.cost_usd` ≤ `agent_budgets.limit_usd` | `agent_costs`, `agent_budgets` | ≤ budget |
| **Latency** | `agent_runs.ended_at - started_at` ≤ timeout | `agent_runs` | ≤ `timeout_policy` |
| **Handoff quality** | handoff completo com `context_summary` e `required_inputs` | `agent_handoffs` | completeness = 1.0 |
| **Error rate** | `agent_errors` / total runs | `agent_errors` | ≤ 5% |
| **Hallucination risk** | `hallucination_checks.risk` | `hallucination_checks` | ≤ 0.10 |

Regressão detectada: `quality_regressions` emite alerta quando `current < baseline - threshold`.

# 7. Skill and Skill Chain Evals

| Dimensão | Descrição | Tabela doc 11 |
|---|---|---|
| **Skill success rate** | % runs de skill completados com sucesso | `skill_performance.success_rate` (§24) |
| **Reuse quality** | output reutilizável em contextos similares (schema+content) | `eval_scores` por `skill_id` |
| **Failure patterns** | tipo recorrente de `eval_failures` para a skill | `eval_failures` agrupado por `skill_id` |
| **Dependencies** | skill depende de outra que está degradando | `skillChainRegistry` + `skill_performance` |
| **Chain breakpoints** | ponto de falha em skill chains (`skillChainRegistry`) | `run_steps.status=failed` com chain_ref |
| **Cost per skill** | custo médio por ativação de skill | `cost_ledger.scope=run` agrupado por `skill_id` |
| **Output consistency** | variância de score entre runs similares | `eval_scores` std_dev por skill |
| **Schema adherence** | % outputs válidos contra `schemaRegistry` para a skill | `eval_results.passed` por target_kind=skill |

# 8. Workflow Evals

| Dimensão | Métrica | Tabela doc 11 |
|---|---|---|
| **Completion rate** | `workflow_runs.state=completed` / total | `workflow_runs`, `workflow_performance.success_rate` |
| **Stuck runs** | runs em estado não-terminal há > timeout | `workflow_runs.state` + `run_state_transitions` lag |
| **Retry rate** | `run_retries` / `workflow_runs` | `run_retries` |
| **Timeout rate** | `workflow_runs` com `state=timed_out` | `run_errors.code=timeout` |
| **Approval bottlenecks** | approvals em `status=requested` há > 80% do `expires_at` | `approvals` + `approval_expirations` |
| **State transition health** | transições inválidas detectadas | `state_transition_logs` com `invalid_transition` |
| **Cost per workflow** | custo total por `workflow_id` por período | `cost_ledger.scope=workflow` |
| **Time to output** | `workflow_runs.ended_at - started_at` | `workflow_runs` |
| **Human intervention rate** | % workflows com pelo menos uma approval humana | `approvals.approver` tipo `user` |

# 9. RAG / Memory / Context Evals

| Dimensão | Métrica | Tabela doc 11 |
|---|---|---|
| **Retrieval relevance** | score médio do top-1 resultado | `rag_results.score` |
| **Retrieval freshness** | `memories.freshness_at` vs threshold | `rag_results` → `memories.freshness_at` |
| **Source reliability** | `source_reliability_scores.score` médio dos resultados usados | `source_reliability_scores` |
| **Tenant isolation** | `retrieval_logs.permission_filtered` > 0 = vazamento bloqueado | `retrieval_logs` |
| **Context precision** | % tokens de contexto relevantes para a intent | `context_budget_logs` + eval score |
| **Context recall** | % informação necessária presente no context pack | eval score por `context_pack_id` |
| **Context overload** | `context_budget_logs.used_tokens / max_tokens` > 0.95 | `context_budget_logs` |
| **Memory pollution** | memórias com `confidence < 0.5` sendo recuperadas | `rag_results` → `memories.confidence` |
| **Stale memory use** | memórias com `valid_until` expirado usadas no context | `rag_results` → `memories.valid_until` |
| **Cross-project leakage attempts** | `retrieval_logs.permission_filtered` sem namespace correto | `retrieval_logs` + `audit_logs` evento `VectorNamespaceViolationAttempted` |
| **Vector namespace violations** | busca semântica sem namespace de tenant como pré-condição | `audit_logs` evento `VectorNamespaceViolationAttempted` (P0) |

# 10. Model Strategy and Model Router Observability

## 10.1 Posicionamento estratégico (registro permanente)

> **CKOS does not own or train a foundation model at MVP stage.** CKOS owns the **model orchestration layer**: model registry, model router, context pack, memory, prompts, instructions, policies, evals, fallbacks, cost guard and learning loop. External LLMs are **replaceable cognitive engines** — selected per task by risk level, privacy classification, budget envelope, latency requirement and quality threshold. Model substitution must never require architecture changes; only model registry and routing policy updates. (Registrado também em doc 10 §5.5.)

## 10.2 Observability do Model Router

O `model_router` (10 §5.5) registra cada decisão de roteamento em `model_calls` (11 §8). Métricas por `model_id`:

| Métrica | Fonte | Freq |
|---|---|---|
| **Usage count** | `model_calls` agrupado por `model_id` + período | por run |
| **Cost per call / per 1k tokens** | `model_calls.cost_usd / tokens_in+out` | contínuo |
| **Latency p50/p95/p99** | `model_calls.latency_ms` | contínuo |
| **Failure rate** | `model_calls` com `status=failed` / total | diário |
| **Fallback rate** | `model_calls.fallback_of IS NOT NULL` / total | diário |
| **Quality by task type** | `eval_scores` filtrado por `model_id` | por eval |
| **Privacy level adherence** | model usado vs `data_classification` do context pack | por call |

**Critérios de roteamento registrados (para auditoria):**

```txt
task_type        — tipo de tarefa (geração, análise, classificação, RAG...)
risk_level       — nível de risco da ação (04 §5.1-5.9)
quality_required — score mínimo de qualidade esperado
privacy_level    — classificação do dado no context pack (12 §5.14)
budget           — limite de custo do run/workflow
latency          — SLA de latência da skill
context_size     — tokens estimados de contexto
tool_need        — precisa de function calling
reasoning_need   — exige raciocínio em cadeia (CoT)
output_schema    — output estruturado obrigatório
fallback_available — há modelo alternativo caso o primário falhe
```

**Model degradation alert:** se `model_id.quality_score` cair > 15% em 7 dias → alerta P2 + sugestão de fallback automático.

# 11. Cost Control Architecture

O `cost_guard` (10 §5.23) impõe limites em tempo real durante a execução. A política vem do `costPolicyRegistry` (10 §5.14).

**Escopos de custo:**

```txt
project   → limite total por projeto/período
client    → limite por cliente whitelabel (billing)
agent     → limite por agente/período (agent_budgets)
workflow  → limite por tipo de workflow
run       → limite por run individual
model     → limite por modelo/período
tool      → limite por tool/período
collector → limite por collector/período
day       → limite diário (dashboard de controle)
month     → limite mensal (billing/forecast)
```

**Fluxo de enforcement pelo `cost_guard`:**

```txt
1. Run inicia → cost_guard consulta costPolicyRegistry para o escopo
2. Estimativa de custo calculada antes da model call (context tokens × preço)
3. Se estimativa > soft_limit → alerta P3 + requer confirmação
4. Se estimativa > hard_limit → run bloqueado antes da model call
5. Custo real registrado em cost_ledger após execução
6. Se custo acumulado do projeto > project_budgets.soft_limit_usd → alerta P2
7. Se custo acumulado > hard_limit → project_budgets.state = blocked_by_cost → novo run = approval required
8. Loop de custo detectado: custo crescente exponencial em causation_id chain → loop_detector + abort
```

**Limites em MVP P0:**

```txt
soft_limit  → alertar mas permitir (aprovação opcional)
hard_limit  → bloquear; exige approval explícita para prosseguir
per-run cap → abortar run se cost_usd > cap durante execução
```

# 12. Cost Ledger Metrics

Tabelas de persistência de custo (doc 11 §18) e queries de observabilidade:

| Tabela | Uso em observabilidade |
|---|---|
| `cost_ledger` | fonte append-only; base de todas as agregações; filtrável por scope/scope_ref/período |
| `run_costs` | view materializada; custo por run_id; usado em agent eval (§6 cost efficiency) |
| `model_costs` | agregação por model_id/período; alimenta model degradation alert (§10) |
| `tool_costs` | custo por tool; identifica tools excessivamente caras para a value entregue |
| `collector_costs` | custo por collector_run; alerta se coletor custa mais do que o dado vale |
| `project_budgets` | estado do orçamento: `within_budget / approaching_limit / blocked_by_cost / needs_approval` |
| `agent_budgets` | limite por agente; previne agente individual de consumir budget do projeto |
| `budget_alerts` | histórico de alertas disparados; audita padrão de estouro |

**Queries de gestão de custo:**

```txt
custo por projeto/mês    → cost_ledger WHERE scope=project GROUP BY scope_ref, month
custo por agente         → agent_costs JOIN agents por período
modelo mais caro         → model_costs ORDER BY cost_usd DESC
run mais caro            → run_costs ORDER BY cost_usd DESC LIMIT 20
collector ROI            → collector_costs vs evidence_items gerados pelo collector_run
forecast de estouro      → avg diário × dias restantes vs project_budgets.limit_usd
```

# 13. Security Observability

Absorve os 14 eventos de segurança de doc 12 §5.21 e define severidade, SLA e ação:

| Evento | Severidade | SLA de resposta | Ação automática | Ação humana |
|---|---|---|---|---|
| `TenantBoundaryViolationAttempted` | **P0** | ≤ 5 min | bloquear request; `audit_log` imediato | Metacognik + Founder alerta imediato; incident review |
| `AgentPolicyModificationAttempt` | **P0** | ≤ 5 min | bloquear + sandbox lock | Metacognik review; potencial disable do agente |
| `EmergencyBypassActivated` | **P0** | ≤ 5 min | log + alerta | Metacognik + QA Lead review obrigatório dentro de 24h |
| `SecretRedacted` (pattern detectado em log) | **P1** | ≤ 15 min | redação aplicada + `[SECRET_REF_REDACTED]` | Security review; rotation do segredo |
| `PolicyViolationDetected` | **P1** | ≤ 15 min | ação bloqueada | Metacognik audit; policy review |
| `ApprovalPolicyChanged` | **P1** | ≤ 15 min | registro em audit + `registry_item_versions` | QA Lead + Founder confirmação |
| `VectorNamespaceViolationAttempted` | **P1** | ≤ 15 min | busca bloqueada | Metacognik; revisar indexação |
| `PIIBlockedFromPrompt` | **P2** | ≤ 1h | PII removido do context | Metacognik; revisar classificação do dado |
| `ModelPrivacyPolicyViolation` | **P2** | ≤ 1h | run bloqueado | Security + model_router config review |
| `CollectorProviderExposureBlocked` | **P2** | ≤ 1h | response redatado | Eng review do endpoint |
| `CapabilityScopeViolation` | **P2** | ≤ 1h | tool bloqueada; alerta | Metacognik; revisar agent_permissions |
| `AgentPermissionDenied` (recorrente) | **P2** | ≤ 1h | log | Metacognik; revisar policy |
| `PIIAccessLogged` (acesso suspeito) | **P3** | ≤ 4h | audit entry | Security review periódica |
| `PermissionDenied` (isolado) | **P3** | batch | log | Análise de padrão diária |

**SLA de alerta por severidade:**

```txt
P0 → notificação em ≤ 5 min; incident criado automaticamente; Founder + Metacognik on-call
P1 → notificação em ≤ 15 min; Metacognik review obrigatório
P2 → notificação em ≤ 1h; review na próxima sessão de trabalho
P3 → agregado em relatório diário; nenhuma ação imediata obrigatória
```

# 14. Incident Review e Run Replay

Quando um incidente ou comportamento inesperado é detectado, o sistema reconstrói o run a partir do event store (sem logging paralelo — é event-sourced).

**Tabelas de replay (doc 11 §22):**

```txt
run_replays(id, run_id, run_kind, requested_by, created_at)
run_replay_events(id, run_replay_id fk, event_id fk→events, ordinal int)
run_replay_snapshots(id, run_replay_id fk, context_pack_id fk, snapshot jsonb)
run_replay_artifacts(id, run_replay_id fk, artifact_id fk→artifacts)
```

**Reconstrução completa de um run de incidente:**

| Dimensão | Fonte |
|---|---|
| O que aconteceu | `run_replay_events` ordenados por `ordinal` |
| Quem/qual agente fez | `events.actor_id` + `agents.display_name` |
| Qual contexto foi usado | `run_replay_snapshots.snapshot` + `context_packs` |
| Qual policy autorizou | `audit_logs` evento `PermissionGranted` com `context_snapshot` |
| Qual modelo foi chamado | `model_calls.model_id` + `prompt_id` |
| Quanto custou | `cost_ledger` por `correlation_id` |
| Qual output foi gerado | `agent_outputs` + `artifact_versions` |
| Quem aprovou | `approvals.approver` + `approval_events` |
| Onde falhou | `run_errors` + `eval_failures` + `agent_errors` |
| Qual política foi violada | `audit_logs` eventos P0/P1 com `source_event_id` |

**Trigger de replay:** qualquer evento P0/P1 dispara replay automático e persiste resultado em `run_replays` com `requested_by = system`. Replays manuais via `QA Lead` ou `Metacognik`.

# 15. Loop Detection

O `loop_detector` (10 §5.15) monitora padrões que indicam que o sistema entrou em ciclo.

**Parâmetros de detecção:**

```txt
max_run_depth         → profundidade máxima de causation_id chain (default: 10)
max_agent_handoffs    → handoffs em uma correlation_id (default: 8)
max_retry_chain       → retries consecutivos do mesmo run (default: 5)
max_cost_per_loop     → custo acumulado em 1h para um correlation_id (default: 10× run_avg)
repeated_event_pattern → mesmo event_type com mesmo aggregate_id > N vezes / hora
repeated_tool_failure  → mesma tool falhando > 3 vezes no mesmo agent_run
repeated_agent_handoff → agente A → B → A detectado via causation_id chain
```

**Ações por tipo de loop:**

| Loop detectado | Ação imediata | Ação Metacognik |
|---|---|---|
| `max_run_depth` excedido | `workflow_run` → `paused`; `loop_detected` event | Metacognik revisa cadeia e decide: abort ou continue |
| `max_agent_handoffs` excedido | `workflow_run` → `needs_approval` | Metacognik sugere reestruturação do workflow |
| Custo exponencial | run → `blocked_by_cost`; Cost Guard trigger | Metacognik + Founder aprovam prosseguimento |
| Tool failure loop | `agent_run` → `failed`; DLQ | QA Lead revisa tool config |
| Agent A→B→A | `workflow_run` → `failed`; incident criado | Metacognik revisa orquestração |

# 16. Quality Gates

Pontos de execução onde o sistema verifica qualidade antes de prosseguir:

| Gate | Quando | Quem verifica | Ação em falha |
|---|---|---|---|
| **Before output is shown** | pré-exibição de qualquer output ao usuário | `eval_runner` determinístico | output retido; Metacognik flagged |
| **Before artifact is approved** | pré-aprovação de artifact | `eval_runner` + LLM-as-judge | artifact → `under_review`; QA Lead |
| **Before proposal is sent** | pré-envio de proposta ao cliente | Metacognik audit + `eval_runner` | proposta retida; PMO_CKOS review |
| **Before collector runs** | pré-execução de collector | capability check + cost estimate | blocked se fora de scope/budget |
| **Before high-cost model call** | model call com `estimated_cost > soft_limit` | Cost Guard | pausa + confirmação ou fallback |
| **Before memory write** | gravação em `long_term` / `mid_term` memory | `eval_runner` (confidence + freshness) | write rejeitado se `confidence < 0.5` |
| **Before RAG source becomes trusted** | elevação de `source_reliability_score` | `eval_runner` + `source_reliability_scores` | fonte marcada `low_reliability` |
| **Before workflow auto-executes** | `autonomy_level` permite auto-exec sem approval | policy_engine + risk_level check | downgrade para `needs_approval` |

# 17. Metacognik Audit Layer

Metacognik (`@metacognik`) é acionado para audit em:

| Situação | Critério | Ação de Metacognik |
|---|---|---|
| Baixa confiança | `agent_runs.confidence < threshold` (default: 0.65) | review do output; recomendação ou block |
| Alto risco | `agent_runs.risk_level = high` | audit mandatório antes de output |
| Evidência insuficiente | `evidence_coverage_scores.coverage < 0.6` | solicitar evidência adicional ou flag |
| Contradição detectada | `contradiction_checks.contradictions > 0` | investigar e resolver antes de prosseguir |
| Custo alto (suspeito) | custo do run > 5× average para skill/agente | audit de loop/ineficiência |
| Ação irreversível | `action.reversible = false` + `risk ≥ medium` | revisão obrigatória antes de execução |
| Policy exception | tentativa de bypass de policy | block + incident P0/P1 |
| Output estratégico | tipo: proposta, contrato, diagnóstico, decisão crítica | review antes de entrega |
| Self-evolving action | mudança em agent/skill/policy/workflow | veto e revisão (doc 21) |

Metacognik tem poder de **veto** (12 §5.13): output com `metacognik_blocked = true` não é exibido/entregue independente de outras aprovações.

# 18. QA Lead Review Layer

QA Lead (`@qa_lead`) entra em:

| Situação | Critério | Ação de QA Lead |
|---|---|---|
| Mudança técnica | PR com alteração em skill, workflow, agent, policy | revisão obrigatória (doc 20) |
| Artifact crítico | `artifact.type` em [proposta, contrato, brandbook, relatorio] | review de qualidade antes de approval |
| Build/implementação | qualquer implementação de feature nova | sign-off no pipeline (doc 19) |
| Workflow novo | novo blueprint em `workflowRegistry` | validação de gates, risk_levels e edge cases |
| Security patch | alteração em policyRegistry, approvalPolicyRegistry | co-review com Metacognik |
| Migration (futura) | schema migration de tabelas de domínio | validação de backward compatibility + rollback |
| Integração externa | novo provider/tool/collector | validação de isolation + secret_refs |
| Automação de risco | workflow com `autonomy_level ≥ 7` | gate de qualidade + Founder awareness |

# 19. Observability Dashboards (internos)

Dashboards derivados de projections (11 §21) e `cost_projection`. **Leitura-only; nunca fonte de verdade.**

| Dashboard | Fonte principal (doc 11) | Atualização |
|---|---|---|
| **Runtime Health** | `agent_activity_projection`, `workflow_runs.state`, `run_errors` | tempo real |
| **Agent Performance** | `agent_performance`, `agent_eval_results`, `eval_scores` | por run + batch diário |
| **Workflow Health** | `workflow_performance`, `run_state_transitions`, `approval_projection` | por workflow_run |
| **Cost Control** | `cost_projection`, `project_budgets`, `budget_alerts` | contínuo |
| **Model Quality** | `model_calls` + `eval_scores` por model_id | por call + batch diário |
| **RAG Quality** | `retrieval_logs`, `rag_results.score`, `context_precision` | por query |
| **Security Incidents** | `audit_logs` filtrado por P0/P1/P2 | tempo real |
| **Approval Bottlenecks** | `approval_projection`, `approval_expirations` | a cada mudança de approval |
| **Collector Reliability** | `collector_runs.state`, `collector_errors`, `collector_costs` | por collector_run |
| **Product Projection Health** | `ui_projections.last_event_id` vs `events` lag | contínuo |

# 20. Alerting System

| Alerta | Trigger | Severidade | Canal |
|---|---|---|---|
| Cost threshold | `budget_alerts.level = exceeded` | P1/P2 | workspace_owner + PMO_CKOS |
| Policy violation | `PolicyViolationDetected` | P0/P1 | Metacognik + Founder (P0); Metacognik (P1) |
| Tenant leak attempt | `TenantBoundaryViolationAttempted` | P0 | Founder + Metacognik imediato |
| Low confidence output | `confidence < 0.5` em output ao cliente | P2 | Metacognik |
| Hallucination risk | `hallucination_checks.risk > 0.15` | P1 | Metacognik + QA Lead |
| Repeated retries | `run_retries.attempt > max_retry_chain` | P2 | QA Lead + Builder Lead |
| Collector failure | `collector_runs.state = failed` após 3 retries | P2 | ops + Metacognik |
| Model degradation | quality_score caiu > 15% em 7 dias | P2 | PMO_CKOS + QA Lead |
| Approval bottleneck | approval pendente em > 80% do `expires_at` | P2 | approver + PMO_CKOS |
| Stale memory use | memória com `valid_until` expirado em resultado RAG | P3 | Metacognik (batch) |
| Vector retrieval anomaly | score médio caiu > 20% em 7 dias | P2 | QA Lead |
| Secret redacted | segredo detectado e redatado em log | P1 | Security review |
| Loop detected | `loop_detector` disparou | P1 | Metacognik + workflow owner |
| Context overload | `used_tokens / max_tokens > 0.95` recorrente | P3 | QA Lead (batch) |

# 21. Learning Loop Metrics

O `learning_loop_engine` (10 §5.28) agrega outcomes em aprendizado persistente usando as tabelas de doc 11 §24:

| Tabela | O que mede | Como alimenta o aprendizado |
|---|---|---|
| `lessons_learned` | lições por projeto/skill/agente | sugere ajustes em prompts e workflows |
| `decision_outcomes` | resultado real de decisões (positivo/negativo/misto) | calibra `confidence_scores` futuros |
| `workflow_performance` | success_rate, avg_cost, avg_retries por workflow | router prioriza workflows de alta performance |
| `agent_performance` | avg_quality, reproval_rate, avg_cost por agente | model_router seleciona agente mais adequado por task |
| `prompt_performance` | approval_rate, avg_quality por prompt | Prompt Library curada; prompts ruins marcados para revisão |
| `skill_performance` | rework_rate, success_rate por skill | skills com rework_rate alto → review de definição |
| `node_performance` | usefulness, redundancy_rate por node_type | Node Canvas sugere remoção de nodes redundantes |

**Como o CKOS aprende:**

```txt
Outputs aprovados  → decision_outcomes.outcome = positive → reforça prompts/skills usados
Outputs reprovados → decision_outcomes.outcome = negative → flag para revisão de prompt/skill
Custo alto + qualidade baixa → agent_performance.reproval_rate + avg_cost → sugere modelo alternativo
RAG score baixo → quality_regressions → sugere re-embedding ou nova fonte
Workflow stuck → workflow_performance.success_rate caiu → Metacognik review do blueprint
Approval rate caindo → prompt_performance → Founder/PMO_CKOS review de critério de qualidade
```

O aprendizado é **semi-automático em MVP**: `learning_loop_engine` agrega e sugere; alterações em registries exigem aprovação humana. Self-Evolving autônomo é fase futura (21).

# 22. MVP P0 Observability

**Entra no MVP P0** (mínimo para o sistema ser operável e auditável):

```txt
Basic run trace         → agent_runs com trace_id + correlation_id + causation_id
Agent eval result       → eval_results + eval_scores por agent_run (mínimo: confidence + schema compliance)
Cost per run            → cost_ledger + run_costs (custo de toda model_call)
Model call logging      → model_calls (model_id, tokens_in/out, cost_usd, latency_ms)
Approval logging        → approvals + approval_events (todo approval gate)
RAG retrieval logging   → retrieval_logs (candidates, returned, permission_filtered, latency)
Security event logging  → audit_logs para eventos P0/P1 (TenantBoundary, PolicyViolation, SecretRedacted)
Simple internal dashboard → cost_projection + agent_activity_projection + approval_projection
Metacognik audit flag   → eval_results com flag para Metacognik review quando confidence < threshold
QA review flag          → artifacts com eval_failures → `under_review`
Event replay básico     → run_replays + run_replay_events (reconstituição causal básica)
```

**Fica fora do MVP P0** (evolução):

```txt
Eval marketplace (benchmark externo de modelos)
Advanced model benchmarking (A/B de modelos em produção)
Full self-evolving metrics (doc 21 scope)
Complex anomaly detection (ML sobre séries temporais de custo/qualidade)
Predictive cost optimization (forecast antes da execução)
Visual run replay completo (UI interativa de replay)
Learning loop autônomo (semi-automático no MVP; autônomo é pós-aprovação de 21)
Full LLM-as-judge fleet (apenas heurísticos no MVP)
```

# 23. Edge Cases

| Cenário | Tratamento |
|---|---|
| **Output bom, mas sem evidência** | `evidence_coverage_score < threshold` → `MetacognikAuditFlagged`; output retido até review |
| **Output ruim, mas barato** | `eval_scores.output_quality < threshold` mesmo com custo baixo → reprovado; custo não justifica qualidade |
| **Modelo caro performando mal** | `model_costs` alto + `eval_scores` baixo → `quality_regression` → alerta P2; model_router sugere fallback |
| **RAG retorna dado correto de tenant errado** | `retrieval_logs.permission_filtered > 0` → bloqueado; VectorNamespaceViolation P1; namespace correction |
| **Agente entra em loop** | `loop_detector` dispara; `workflow_run` → paused; Metacognik review; abort se custo > cap |
| **Approval expira** | `approval_expirations.action_on_expire` = block/escalate/auto; `approval_escalations` registra |
| **Collector parcial** | `collector_runs.normalized_count < expected`; registros válidos preservados; re-run do delta pendente |
| **Segurança bloqueia workflow legítimo** | policy muito restritiva → `PermissionDenied` + run paused; operador revisa e solicita exception aprovada |
| **Eval LLM-as-judge discorda de humano** | ambos registrados em `eval_results`; discordância → `contradiction_check` → QA Lead review manual |
| **Custo estoura no meio do run** | Cost Guard para a model call; run → `blocked_by_cost`; `budget_alerts` → approval para continuar |
| **Artifact aprovado depois de dado ficar obsoleto** | `memories.valid_until` expirou após approval; revalidar com novos dados; artifact volta para `under_review` |

# 24. Metrics

Métricas principais do sistema de observabilidade:

| Métrica | Definição | Target |
|---|---|---|
| **Trace completeness rate** | % runs com `trace_id` + `correlation_id` + todos os steps | ≥ 99% |
| **Evidence coverage rate** | `evidence_coverage_scores.coverage` médio por projeto | ≥ 80% |
| **Average confidence score** | `eval_scores[confidence]` médio por agente/período | ≥ 0.75 |
| **Hallucination risk rate** | `hallucination_checks.risk > 0.10` / total checks | ≤ 5% |
| **Contradiction rate** | `contradiction_checks.contradictions > 0` / total | ≤ 2% |
| **Retrieval relevance score** | `rag_results.score` médio top-1 | ≥ 0.70 |
| **Context precision score** | % tokens relevantes / total tokens no context pack | ≥ 0.65 |
| **Cost per successful run** | `run_costs` de runs com `state=completed` + `eval_results.passed=true` | trending down |
| **Cost per approved artifact** | `cost_ledger` por `artifact_id` aprovado | trending down |
| **Model fallback rate** | `model_calls.fallback_of IS NOT NULL` / total | ≤ 10% |
| **Workflow completion rate** | `workflow_runs.state=completed` / total | ≥ 85% |
| **Approval bottleneck rate** | approvals pendentes > 50% do TTL / total approvals | ≤ 10% |
| **Policy violation rate** | `PolicyViolationDetected` events / total runs | → 0% |
| **Tenant boundary violation attempts** | `TenantBoundaryViolationAttempted` / período | 0 (qualquer > 0 = incident) |
| **Agent success rate** | `agent_runs.state=completed` + `eval_results.passed=true` / total | ≥ 85% |
| **Skill success rate** | `skill_performance.success_rate` médio por skill | ≥ 85% |
| **Prompt performance score** | `prompt_performance.approval_rate` médio | ≥ 80% |
| **Output approval rate** | artifacts aprovados / artifacts gerados | ≥ 70% |

# 25. Related Notes

- [[10_SYSTEM_RUNTIME_ARCHITECTURE]]
- [[11_DATA_MODEL_AND_PERSISTENCE]]
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]]
- [[25_SELF_EVOLVING_SYSTEM_ARCHITECTURE]]
- [[19_CLAUDE_CODEX_EXECUTION_PROTOCOL]]
- [[20_QA_AND_FOUNDER_APPROVAL_PROTOCOL]]

---

# 26. Agente responsável

- Owner documental: `PMO_CKOS`
- Agente responsável operacional: `QA Lead` (executa reviews, valida gates, assina off em builds)
- Auditoria de risco: `Metacognik` (veto em output de alto risco; audit de confidence/evidence)
- Implementação: `Builder Lead`

# 27. Superagentes envolvidos

| Agente | Papel neste documento |
|---|---|
| Metacognik | Audit de risco; veto de outputs; loop detection review; incident P0/P1 |
| QA Lead | Review de artifacts/builds; gate de qualidade; co-review de security patches |
| PMO_CKOS | Owner de políticas de eval; aprovação de mudanças em evalRegistry/costPolicyRegistry |
| Builder Lead | Implementação de eval_runner, cost_guard, loop_detector, dashboards |
| Founder | Aprovação de thresholds críticos; emergency bypass de cost limits |

# 28. Skills necessárias

```txt
eval-execution          — executa evals contra target_kind por critério do evalRegistry
cost-attribution        — registra custo em cost_ledger com escopo e source_event_id
loop-detection          — detecta ciclos via causation_id chain + padrões de evento
quality-gate-check      — verifica qualidade antes de entrega/approval/escrita
incident-replay         — reconstrói run a partir de run_replay_events
metacognik-audit        — avaliação metacognitiva de confiança/risco/evidência
model-quality-routing   — seleciona modelo por qualidade×custo×privacidade
hallucination-check     — verifica claims não-fundamentados em evidência
evidence-coverage-check — mede cobertura de evidência por afirmação do output
budget-enforcement      — aplica limites hard/soft de custo em tempo de execução
```

# 29. Prompts relacionados

```txt
Eval LLM-as-judge: "Avalie este output contra a rubrica [criteria]. 
Score 0-1 em: task_success, factual_accuracy, evidence_grounding, 
format_compliance, safety. Justifique cada score. 
Metadata: model={model}, risk={risk_level}, schema={schema_id}."

Hallucination check: "Identifique afirmações neste output que não 
estão fundamentadas nas fontes fornecidas. Liste cada claim, 
classifique como grounded/ungrounded, e estime o risco de alucinação 
(0-1). Fontes: [context_pack.sources]."

Evidence coverage: "Para cada afirmação factual neste output, 
identifique a evidência de suporte nas fontes disponíveis. 
Calcule: claims_with_evidence / total_claims. Se coverage < 0.8, 
liste as afirmações sem evidência."
```

# 30. Integrações

| Sistema | Como integra |
|---|---|
| `eval_runner` (doc 10 §5.15) | executa evals do evalRegistry; persiste em `eval_results` + `eval_scores` |
| `cost_guard` (doc 10 §5.23) | impõe limites de cost_ledger; emite eventos de threshold |
| `loop_detector` (doc 10 §5.15) | monitora causation_id chains; emite `loop_detected` |
| `learning_loop_engine` (doc 10 §5.28) | agrega outcomes nas learning tables (11 §24) |
| doc 11 (Data Model) | tabelas de persistência: eval_results, cost_ledger, model_calls, run_replays, audit_logs, learning tables |
| doc 12 (Security) | 14 eventos de segurança → métricas e SLAs de §13 deste doc |
| OpenRouter | custo/token por model_id; latência; fallback rate |
| Vault/redação (12 §5.15) | `SecretRedacted` feed → alertas P1 deste doc |

# 31. Memória e contexto

- `eval_results` alimentam `agent_performance` e `skill_performance` (tabelas de learning) que são recuperadas pelo `context_pack_builder` em futuras runs do mesmo agente/skill.
- `quality_regressions` são armazenadas em `memories.scope = long_term` para que o `learning_loop_engine` os use em calibração de thresholds.
- Thresholds de eval (confidence, hallucination_risk, evidence_coverage) vivem no `evalRegistry` — são configuração, não memória de sessão.
- `model_performance` agregada (§24) é lida pelo `model_router` para decisões de routing futuras.

# 32. Declaração de componentes de runtime (template §9.1)

| Componente | Detalhe |
|---|---|
| **Registries afetados** | `evalRegistry` (lê critérios); `costPolicyRegistry` (lê limites); `modelRegistry` (lê privacy + quality history); `approvalPolicyRegistry` (lê para approval gates em quality gates) |
| **Engines afetados** | `eval_runner` (executa evals); `cost_guard` (impõe limites); `loop_detector` (detecta ciclos); `learning_loop_engine` (agrega outcomes); `model_router` (consome quality metrics para routing) |
| **State machines afetadas** | `agent_run` (blocked/flagged por quality gate); `workflow_run` (paused por loop); `approval` (triggered por quality gate); `artifact` (under_review por eval failure) |
| **Eventos emitidos** | `EvalCompleted`, `EvalFailed`, `QualityRegressionDetected`, `CostThresholdExceeded`, `CostHardLimitReached`, `LoopDetected`, `MetacognikAuditFlagged`, `QAReviewRequired`, `IncidentReplayCreated`, `ModelDegradationDetected`, `BudgetAlertFired` |
| **Tabelas necessárias** | `eval_results`, `eval_scores`, `eval_failures`, `eval_recommendations`, `quality_regressions`, `hallucination_checks`, `contradiction_checks`, `evidence_coverage_scores`, `cost_ledger`, `run_costs`, `model_costs`, `project_budgets`, `agent_budgets`, `budget_alerts`, `run_replays`, `run_replay_events`, `audit_logs`, `model_calls`, `learning tables (§24)` |
| **Policies envolvidas** | `evalRegistry` (critérios e thresholds); `costPolicyRegistry` (limites por escopo); `approvalPolicyRegistry` (quality gates); policyRegistry (policy compliance checks) |
| **Failure modes** | eval_runner indisponível → outputs sem eval passam com flag `eval_skipped`; cost_guard indisponível → runs sem limitação (fail-open, alerta P1); loop_detector miss → custo descontrolado até Cost Guard hard limit |
| **Rollback** | `QualityGateFailed` compensa entrega prematura; `CostLimitCompensation` bloqueia runs subsequentes até orçamento recarregado; `EvalOverride` (com Founder approval) permite bypass documentado |
| **Observability** | este doc é a camada de observability; auto-referente; a própria saúde do eval_runner é monitorada por `eval_results.created_at` lag e ausência de records |

# 33. Critérios de aprovação

- Evals definidos para todos os 14 target kinds com critérios, thresholds e fonte de dados;
- Security observability cobre todos os 14 eventos de doc 12 §5.21 com severidade e SLA;
- Cost control cobre todos os escopos (project/agent/run/model/tool/collector/day/month);
- Model Router observability registra todos os critérios de roteamento e fallback;
- Run replay cobrindo as 9 dimensões de reconstrução de incidente;
- Loop detection com parâmetros, triggers e ações definidos;
- Quality gates nos 8 pontos críticos;
- Metacognik audit layer com critérios de veto;
- MVP P0 separado claramente do escopo completo;
- 18 métricas com targets definidos;
- Referências às tabelas de doc 11 v1.1.1 e eventos de doc 12 v1.1.0.

# 34. Critérios de reprovação

- Observability genérica sem conexão com tabelas de doc 11;
- Sem tratamento de Model Router (substituição de modelo = arquitetura opaca);
- Sem tratamento de custo por escopo;
- Sem integração com eventos de segurança de doc 12;
- Sem run replay para incident review;
- Sem Metacognik como camada de veto;
- Sem separação de MVP P0 do escopo completo;
- Thresholds sem fonte de dados (tabela) correspondente;
- Alertas sem severidade, SLA e responsável definidos.
