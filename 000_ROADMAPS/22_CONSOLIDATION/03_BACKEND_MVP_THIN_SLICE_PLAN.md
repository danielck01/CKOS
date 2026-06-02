---
title: Backend MVP Thin Slice Plan
file: 03_BACKEND_MVP_THIN_SLICE_PLAN.md
phase: 000_ROADMAPS
category: planning
status: ready_for_founder_gate5_review
owner: pmo_ckos
responsible_agent: codex_2
created_at: 2026-06-02
gate: GATE 5
session_id: S-P1-GATE5-CODEX2-20260602-001
checkout_lock: LOCK-P1-GATE5-CODEX2-20260602-001
checkout_release: REL-P1-GATE5-CODEX2-20260602-001
source_docs:
  - 000_ROADMAPS/22_CONSOLIDATION/00_CKOS_CONSOLIDATION_MAP_AND_GAP_AUDIT.md
  - 000_ROADMAPS/22_CONSOLIDATION/CKOS_MASTER_EXPANSION_ROADMAP.md
  - 000_UPGRADE/13_MVP_FUNCTIONAL/sprints.md
  - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md
  - 01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - 03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - 03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - 06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md
  - 07_EVOLUTION_SYSTEM/27_AI_FIRST_WORK_ORDERS_AND_MULTI_SESSION_ORCHESTRATION_ARCHITECTURE.md
  - 07_EVOLUTION_SYSTEM/28_NOTES_RAG_AND_KNOWLEDGE_ARCHITECTURE.md
no_runtime_authority: true
implementation_authorized: false
founder_gate5_approved: false
confidence: high
provenance_status: planning_from_canonical_sources
---

# 1. Proposito

Este arquivo especifica o menor slice vertical de backend AI-first do CKOS para GATE 5.

O slice prova uma coisa: uma intencao real entra no runtime, percorre o pipeline completo, produz um output simples e deixa rastro auditavel em evento, evidencia, memoria e ROI.

Este arquivo nao aprova implementacao. Ele nao cria API, migration, worker, UI, agente real, automacao runtime, MCP server, webhook, JSON n8n ou schema novo. A aprovacao Founder do GATE 5 e o passo separado que autoriza iniciar F1.

# 2. Dentro e Fora do Slice

| Dentro do slice | Fora do slice |
|---|---|
| Backend ingress por evento/API para uma intencao | UI, frontend, chat visual, painel lateral, dashboard ou componentes |
| Intent Resolver e context state minimo | Catalogo amplo de agentes, marketplace, CKStore ou civilizacao de agentes |
| Cognik para interpretar a intencao e gerar hipotese | Builder Subagents autonomos ou self-evolving runtime |
| Metacognik para risco, confianca e approval gate | Auto-aprovacao ampla ou bypass de Founder/Metacognik |
| Work Order como envelope governado do Doc 27 | Tabela fisica `work_orders` inventada neste arquivo |
| Agent Run minimo com output simples | Conectores externos alem do minimo autorizado |
| Event Log append-only como fonte de verdade | Estado salvo fora do event log como verdade operacional |
| Evidencia anexada e fronteira Evidence to Memory | Internals de RAG, chunking, embeddings, vector schema ou query policy |
| ROI proxy backend com custo, tempo e qualidade | ROI financeiro externo, promessa comercial ou dashboard de ROI |
| RLS/tenant scope desde o inicio | Dados cross-tenant, permissao como pos-filtro ou acesso sem audit log |

# 3. Principio: Backend Antes de UI

O Master Roadmap define: documentacao antes de runtime; runtime antes de UI.

Por isso, o item antigo do `sprints.md` sobre "UI de chat + painel lateral" fica explicitamente fora deste thin-slice. Em S1, ele deve ser reescrito como backend ingress: aceitar uma intencao por evento/API, persistir `IntentSubmitted`, montar contexto minimo e produzir um output simples rastreavel.

Qualquer tela futura deve ler projecoes do runtime. Nenhuma UI escreve estado diretamente, e nenhuma tela e criterio de GATE 5.

# 4. Slice Vertical em Uma Pagina

```txt
Intencao entra pelo backend
  -> IntentSubmitted em `events`
  -> Intent Resolver classifica e cria `IntentResolved`
  -> Context state minimo via `context_packs`
  -> Cognik interpreta, gera hipotese e nivel de reasoning
  -> Metacognik avalia risco, confianca e approval
  -> Work Order envelope e declarado conforme Doc 27
  -> Workflow/Agent Run executa um output simples
  -> Event Log grava cada transicao com correlation_id e causation_id
  -> Evidencia e anexada ao output
  -> Memory Writer registra apenas a fronteira autorizada
  -> ROI proxy registra custo, tempo, evidencia e alerta de confianca
```

O sucesso do slice nao e "chat funcionando". O sucesso e replay causal: a mesma intencao pode ser reconstruida a partir de eventos, runs, approvals, evidencia, memoria e custo.

# 5. Componentes Minimos do Runtime

| Componente minimo | Dono canonico | Uso no slice | Ainda nao precisa |
|---|---|---|---|
| `intent_router` / Intent Resolver | Doc 10 | Classificar uma intencao e emitir evento resolvido | Taxonomia completa de todos os intents |
| `context_pack_builder` | Doc 10/05/11 | Montar contexto minimo autorizado | RAG avancado, multimodal ou prompt pack complexo |
| `policy_engine` e approval gate | Doc 04/10/12 | Bloquear risco/custo/acao sensivel | Politicas amplas de produto inteiro |
| `workflow_engine` basico | Doc 10 | Orquestrar uma sequencia curta e event-sourced | Workflows longos, Temporal, DAGs complexos |
| `run_scheduler` e worker minimo | Doc 10 | Executar um `workflow_run` e um `agent_run` | Pool sofisticado, escala, multi-worker avancado |
| `agent_router` | Doc 03/10 | Roteamento para os 4 agentes MVP | Catalogo de 30 agentes |
| `model_router` | Doc 10/13/26 | Selecionar modelo por politica minima e registrar custo | Otimizacao sofisticada de modelos |
| `event_store` / Event Bus | Doc 10/11/13 | Fonte de verdade append-only | Broker externo como requisito |
| `memory_writer` | Doc 05/10/28 | Escrever memoria somente pela fronteira aprovada | Chunking, embedding e retrieval internals |
| `cost_guard` / ROI proxy | Doc 13/21 | Registrar custo, tempo e confianca | ROI financeiro externo ou billing |

# 6. Os 4 Agentes do MVP

| Agente | Papel no slice | Limite |
|---|---|---|
| Cognik | Interpreta intencao, monta hipotese, aponta contexto e sugere proximo passo. | Nao aprova sozinho, nao executa fora de policy. |
| PM/Builder | Planeja a execucao minima e organiza a unidade de trabalho. | Nao ativa Builder Subagents autonomos. |
| Metacognik-Risk | Audita risco, lacunas, confianca, approval e qualidade. | Nao substitui Founder em decisoes criticas. |
| ROI | Calcula proxies internos de valor, custo, tempo, evidencia e confianca. | Nao declara ROI financeiro externo sem evidencia e approval. |

Esses quatro papeis sao suficientes para provar o fluxo "cerebro, plano, consciencia, valor". Qualquer expansao de agentes fica fora do GATE 5.

# 7. Modelo de Dados Minimo

O slice usa apenas superficies ja previstas no Doc 11 para MVP P0 ou em docs canonicos relacionados.

| Superficie | Uso no thin-slice | Observacao de boundary |
|---|---|---|
| `events` | Event store append-only para todos os eventos causais. | Obrigatorio; fonte de verdade. |
| `workflow_runs` | Instancia curta do fluxo backend. | Estado reconstruivel por eventos. |
| `agent_runs` | Execucao dos 4 agentes MVP quando chamados. | Deve ter idempotency, trace e custo. |
| `context_packs` | Contexto autorizado da intencao/run. | Doc 05/10 montam; Doc 28 fornece candidatos de knowledge. |
| `approvals` e `approval_events` | Gate Metacognik/Founder quando risco exige. | Sem approval cosmetico. |
| `audit_logs` | Seguranca, authz, incidentes e replay de decisao. | Complementa `events`, nao substitui. |
| `cost_ledger` | Custo interno por run/model/tool. | Base do ROI minimo. |
| `memories` e `memory_write_events` | Escrita de memoria autorizada apos qualidade/evidencia. | Sem long memory automatica sem review. |
| `documents`, `document_chunks`, `rag_queries`, `rag_results` | Referencias para conhecimento quando necessario. | Internals pertencem ao Doc 28. |
| retrieval/audit logs | Registro de contexto recuperado e custo de retrieval. | Policy e detalhes ficam em Doc 28/13/12. |

`Work Order` neste arquivo e envelope governado do Doc 27, nao schema fisico. Persistencia fisica de Work Orders, se necessaria para F1, deve virar patch sugerido ao Doc 11 ou `ARCHITECTURE_QUESTION`, nunca tabela inventada por este arquivo.

RLS e tenant scope entram desde o primeiro sprint. Nenhuma query, memoria, evidencia, custo ou retrieval pode depender de permissao como pos-filtro.

Secret handling (Doc 12): qualquer `agent_run` que chame modelo, tool ou provider resolve credenciais via `secret_refs` — nunca secret, token ou API key literal em codigo, evento, log ou context pack. Secret exposto e falha P0. (Adendo de fan-in PMO 2026-06-02: Doc 12 estava citado no corpo mas faltava como source e o secret handling nao estava explicito.)

# 8. Event Log: o Coracao do Slice

Sem event log, o backend vira chat bonito.

Cada transicao importante deve emitir evento com `correlation_id`, `causation_id`, ator, tenant/project scope e timestamp. O minimo esperado:

| Evento logico | Proposito |
|---|---|
| `IntentSubmitted` | Registra a intencao original. |
| `IntentResolved` | Registra classificacao, confidence e candidatos. |
| `ContextAssembled` | Registra contexto autorizado e sources usadas. |
| `PolicyChecked` | Registra permissao, risco e resultado. |
| `ApprovalRequested` / `ApprovalResolved` | Pausa ou libera execucao conforme Doc 04/10/12. |
| `WorkOrderScoped` | Registra envelope governado, sem criar schema fisico novo. |
| `WorkflowRunStarted` / `WorkflowRunCompleted` | Liga a execucao ao fluxo. |
| `AgentRunStarted` / `AgentRunCompleted` | Liga agente, modelo, output, custo e trace. |
| `EvidenceAttached` | Liga output a evidencia rastreavel. |
| `MemoryWriteRequested` / `MemoryWritten` | Registra fronteira de memoria. |
| `CostTracked` / `RoiProxyRecorded` | Registra custo, tempo, qualidade e valor proxy. |

Eventos sao append-only. Rollback futuro e compensacao, nao DELETE.

# 9. Sequencia de Sprints S1-S6 Mapeada a Docs

| Sprint | Entrega backend pura | Doc dono | Criterio de pronto |
|---|---|---|---|
| S1 | Runtime base: backend ingress, `IntentSubmitted`, Intent Resolver, context state minimo e 1 output simples. | 10/11/15 | Uma intencao entra sem UI e gera trace com correlation_id. |
| S2 | Question Intelligence: clareza, lacunas, risco e pergunta minima quando contexto e insuficiente. | 03/04/10/13 | Run registra clarity score, gap/risk e Metacognik review quando necessario. |
| S3 | Agentes/policies: 4 agentes MVP, registries minimos, policy checker e approval gates. | 03/04/06/10/12 | Execucao bloqueia acao sensivel e registra approval/audit. |
| S4 | Event Log: append-only, causalidade, audit trace e replay basico. | 10/11/13 | Pipeline reconstruivel por eventos, sem estado paralelo como verdade. |
| S5 | Work Order + Agent Run end-to-end: envelope governado e run completo. | 27/03/10/11 | Work Order e usado como governanca; `workflow_run` e `agent_run` completam com evidencia. |
| S6 | Feedback, Evidence to Memory e ROI proxy. | 05/21/22/28 | Output gera feedback hook, memory boundary e ROI proxy com custo/confianca. |

O Sprint 4 e central, nao opcional. Se S4 falhar, S5/S6 nao contam como AI-first auditable backend.

# 10. Interface Evidence to Memory

Esta secao define apenas a fronteira. Detalhe de RAG/indexacao/chunking/embedding/retrieval pertence ao Doc 28.

```txt
EvidenceAttached(event)
  -> quality/eval check
  -> memory_write_policy check
  -> MemoryWriteRequested(event)
  -> MemoryWritten(event) se aprovado
  -> detalhe de RAG/indexacao -> Doc 28
```

Entrada minima: `event_id`, `agent_run_id`, `project_id`, `tenant_id`, `evidence_ref`, `claim_ref`, `confidence`, `source_tier` quando houver, `data_classification`, `permission_level`, `memory_scope_requested`.

Saida minima: memoria curta/media/longa solicitada ou negada, motivo, policy aplicada, audit log, custo de escrita/retrieval quando aplicavel.

Nao especificar neste arquivo: chunk size, embedding model, vector dimensions, namespace shape, query policy, reranking, retrieval score formula ou schema fisico de RAG.

# 11. ROI Minimo do Slice

O ROI minimo e proxy interno de valor, nao promessa financeira externa.

| Proxy | Fonte | Regra |
|---|---|---|
| raw cost | `cost_ledger`, model/tool usage | Sempre registrar antes de estimar valor. |
| run duration | `workflow_runs`, `agent_runs` | Mede tempo de execucao e bloqueios. |
| cost per run/output | `cost_ledger` + run status | Usar para detectar desperdicio. |
| approval/audit completeness | `approvals`, `audit_logs`, `events` | Sem audit completo, ROI fica low confidence. |
| feedback signal | Doc 22 feedback events | Pode criar gap/risco, nao valor automatico. |
| memory update | `memory_write_events` | Valor de aprendizado apenas se policy/eval passam. |
| evidence coverage | evidence refs + evals | Output sem evidencia reduz confidence. |
| low-confidence warning | ROI confidence framework | Qualquer valor especulativo deve aparecer como especulativo. |

Proibido neste slice: ROI financeiro externo, moeda em proposta, promessa de receita, comparacao comercial sem baseline, ou qualquer claim sem evidencia, premissa, confidence e limitacao.

# 12. Stack de Referencia

`99_RESEARCH_LAB` e referencia, nao decisao final.

| Area | Referencia permitida | Status |
|---|---|---|
| Event store | Supabase/Postgres append-only com envelope CKOS inspirado em CloudEvents | Referencia para decisao tecnica futura. |
| CQRS/projections | Projectors reconstruiveis a partir de `events` | Padrao de runtime, sem UI obrigatoria. |
| Background jobs | pg-boss, Supabase Queues, BullMQ ou Temporal como comparacao | Nenhum escolhido por este arquivo. |
| Model routing | OpenRouter como gateway candidato, registry/policy CKOS como camada propria | Adaptador, nao arquitetura final. |
| RAG/memory | pgvector/Supabase como referencia via Doc 28 | Detalhes pertencem ao Doc 28. |
| Observability | trace por correlation/run/approval/cost | Obrigatorio como criterio, tecnologia futura. |

A stack final exige checkout tecnico separado antes de qualquer implementacao.

# 13. Criterios de Pronto do GATE 5

GATE 5 pode ir para aprovacao Founder quando:

- O arquivo 03 existe e esta marcado como planning auxiliar.
- O slice esta definido como backend puro, sem UI/frontend/dashboard.
- O fluxo intent -> run -> evento -> memoria -> ROI esta descrito.
- Os 4 agentes MVP estao limitados a Cognik, PM/Builder, Metacognik-Risk e ROI.
- O Event Log aparece como fonte de verdade e nao como detalhe opcional.
- S1-S6 foram reescritos sem a UI do `sprints.md`.
- Doc 28 e referenciado como dono de RAG/knowledge internals.
- Doc 11 nao foi alterado e nenhuma tabela nova foi tratada como aprovada.
- Work Order foi tratado como envelope governado do Doc 27.
- RLS/tenant isolation aparece desde o inicio.
- AQs e riscos estao registrados em vez de resolvidos por suposicao.
- `SESSION_REGISTRY.md` registra sessao, lock e release.

Mesmo com todos os itens completos, GATE 5 continua nao aprovado ate decisao Founder.

# 14. Dependencias e Ordem

| Dependencia | Pode comecar antes de Doc 28 detalhe? | Bloqueia o que |
|---|---|---|
| Intent ingress + event log | Sim | Bloqueia todo o slice se nao existir. |
| Context pack minimo | Sim | Bloqueia Cognik se contexto nao for auditable. |
| Approval/policy gate | Sim | Bloqueia execucao sensivel. |
| Work Order governance | Sim, como envelope Doc 27 | Bloqueia fan-in/release governado se ausente. |
| Evidence to Memory internals | Parcial | Detalhe de indexacao/retrieval depende Doc 28. |
| RAG embeddings/chunking/query | Nao neste arquivo | Bloqueia RAG forte, nao o backend proof minimo. |
| ROI proxy | Sim | Bloqueia GATE 5 se custo/confianca nao forem registrados. |
| UI/dashboard | Nao entra | Nao bloqueia GATE 5. |

Ordem recomendada: S1 event ingress -> S4 event log hardening -> S2/S3 intelligence and gates -> S5 governed run -> S6 memory/ROI boundary. A ordem de sprint pode ser planejada linearmente, mas Event Log deve ser estabilizado cedo porque sustenta todos os demais criterios.

# 15. ARCHITECTURE_QUESTIONS em Aberto

| ID | Pergunta | Dono sugerido | Impacto |
|---|---|---|---|
| AQ-G5-01 | Work Orders terao tabela fisica no Doc 11 ou serao derivados de `workflow_runs`/events no MVP? | Technical + PMO + Founder | Bloqueia migrations futuras, nao este planning doc. |
| AQ-G5-02 | Qual job runner MVP sera escolhido para `run_scheduler`: pg-boss, Supabase Queues, BullMQ, Temporal ou outro? | Technical | Impacta implementacao F1. |
| AQ-G5-03 | Qual e o limite de custo/risco para auto-approval no thin-slice? | Founder + Metacognik | Define quando pausar execucao. |
| AQ-G5-04 | Quais campos minimos de `WorkOrderScoped` entram como evento antes de schema fisico? | Technical + PMO | Evita inventar tabela precoce. |
| AQ-G5-05 | Qual modelo/gateway inicial sera usado pelo `model_router` no MVP? | Technical | OpenRouter e referencia, nao decisao final aqui. |
| AQ-G5-06 | Como separar memoria curta/media/longa no primeiro proof sem promover long memory cedo demais? | Metacognik + Technical | Evita memoria ruim virar verdade. |
| AQ-G5-07 | Quais thresholds de evidence coverage e ROI confidence bloqueiam output ou reduzem confianca? | Metacognik + QA | Impacta S6 e QA. |
| AQ-G5-08 | Quais Doc 28 patch suggestions sao obrigatorias para F1 e quais ficam pos-MVP? | PMO + Technical | Evita over-engineering de RAG. |
| AQ-G5-09 | Qual o mecanismo de `secret_refs`/secret store no MVP (Doc 12) e como `agent_runs` resolvem tokens de provider sem expor em log/evento/contexto? | Technical + Founder | Bloqueia chamadas seguras a modelo/tool em F1. |

# 16. Riscos do Slice

| Risco | Sintoma | Mitigacao |
|---|---|---|
| Virar UI antes de runtime | Sprint 1 volta a pedir chat/painel | Reescrever como backend ingress e evento. |
| RAG internals duplicados | Arquivo 03 define chunk/embedding/query | Remover e apontar para Doc 28. |
| Work Order virar schema inventado | `work_orders` aparece como tabela aprovada | Registrar como AQ ou patch sugerido Doc 11. |
| Event log tratado como log secundario | Estado vive em tabela/projecao sem evento causal | Reprovar GATE 5; event store e fonte de verdade. |
| ROI virar promessa | Output declara valor financeiro sem evidencia | Limitar a proxies internos e low confidence warnings. |
| RLS atrasado | Tenant filter vira pos-filtro | Bloquear implementacao F1 ate RLS/tenant scope estar no design. |
| Approval cosmetico | Run continua apesar de approval pendente | Workflow deve pausar em `waiting_approval`. |
| Over-engineering | Temporal, catalogo de agentes ou RAG completo entram no MVP | Voltar ao thin slice: 1 intencao, 4 agentes, 1 decisao, 1 evidencia, 1 memoria. |
| GATE 5 lido como aprovado | Planejamento vira permissao de build | Repetir que Founder approval e passo separado. |

# 17. Refinacao da ordem (Codex + Founder, 2026-06-02)

> **Frase-guia: primeiro o trilho governado, depois a inteligencia.**

Ordem de construcao refinada — **objetos e eventos antes de agentes**:

```txt
Project Kernel -> Briefing Intake -> Notes/Documents -> Event Log
  -> Work Order -> Artifact/Release -> RAG textual (source-aware) -> Agentes leves
```

- **Dogfooding:** o primeiro caso de uso do CKOS e desenvolver o proprio CKOS. O primeiro Work Order real pode ser um lote da consolidacao (ex: L3 UPGRADE), executado dentro do runtime quando ele existir. (Hoje ja fazemos isso a mao via gates/locks/releases — o runtime so automatiza o que ja funciona manualmente.)
- **Source-aware antes de RAG completo:** salvar docs/notas com metadata -> busca textual/chunking -> embeddings. Alinha com Doc 28.
- **Agentes por ultimo:** o primeiro "agente" e um botao ("gerar diagnostico", "gerar Work Order", "revisar lacunas"), nao automacao autonoma.
- **Criterio de sucesso brutalmente simples:** pegar um briefing novo e gerar uma decisao/artefato rastreavel em **< 10 minutos**.
- **Ressalva PMO (cockpit vs sem-UI):** este arquivo manda backend puro. Um cockpit minimo (read-only sobre o event log: Projeto/Briefing/Notas/WO/Artifacts/Timeline) pode entrar como **janela de observacao** para tornar o slice visivel — nunca como UI rica nem como ponto de partida. Decidir quando F1 abrir.

Esta refinacao melhora §9/§14 e vale quando o GATE 5 for aprovado. **Nao altera o status: F1 segue em espera ate a consolidacao avancar.**

Checkout release esperado desta sessao: arquivo 03 criado, registry atualizado, GATE 5 preparado para fan-in, sem aprovacao Founder e sem implementacao.
