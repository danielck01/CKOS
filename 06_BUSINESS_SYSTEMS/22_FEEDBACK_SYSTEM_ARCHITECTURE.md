---
title: 22_FEEDBACK_SYSTEM_ARCHITECTURE
system_id: feedback_system_architecture
version: 1.0.0
status: draft
category: business_system
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - founder
  - technical
  - metacognik
  - qa_lead
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
  - 20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md v1.2.0
  - 21_ROI_ARCHITECTURE.md v1.0.0
  - ARCHITECTURE_PATCH_REPORT.md v1.4.0
outputs:
  - feedback_system_architecture
  - feedback_type_registry (14 types)
  - feedback_object_model (11 objects)
  - feedback_routing_rules
  - feedback_classification_framework
  - feedback_state_machine (14 states)
  - feedback_events (16 events)
  - feedback_learning_loop
  - feedback_mvp_p0_scope
related_notes:
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - ../04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md
  - ../04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md
  - ../04_PRODUCT_SYSTEM/16_NODE_CANVAS_ARCHITECTURE.md
  - ../05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md
  - 21_ROI_ARCHITECTURE.md
  - 23_SUPPORT_SYSTEM_ARCHITECTURE.md
  - 24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md
  - ../ARCHITECTURE_PATCH_REPORT.md
tags: [business_system, feedback, learning_loop, signals, routing, decisions, improvement, artifacts, agents]
---

> **TESE CENTRAL — DOC 22:**
> Feedback in CKOS is not a comment system. It is a governed learning loop that captures
> signals from users, stakeholders, clients, agents and system outcomes, then routes them
> into decisions, nodes, artifacts, support, ROI and continuous improvement.
>
> Em português: Feedback no CKOS não é um sistema de comentários. É um ciclo governado
> de aprendizado que captura sinais de usuários, stakeholders, clientes, agentes e resultados
> do sistema, e transforma esses sinais em decisões, nodes, artifacts, suporte, ROI e
> melhoria contínua.

---

# 1. Propósito

Este documento estabelece como o CKOS captura, classifica, avalia, roteia e transforma feedback em aprendizado, decisões, nodes, artifacts, suporte e melhoria contínua.

O Feedback System Architecture define:
- Como feedback é capturado de qualquer canal (humano ou sistema) com rastreabilidade completa
- Os 14 tipos de feedback e suas regras de classificação, roteamento e responsabilidade
- O objeto model completo que sustenta o ciclo de vida do feedback
- As regras de roteamento que conectam feedback a ROI, suporte, agentes e QA
- O learning loop governado que transforma sinais em melhorias — sem auto-modificação irrestrita
- Como feedback se conecta ao Dashboard, Command Center, Node Canvas e demais sistemas
- O sistema de eventos e state machine para rastreabilidade total

```txt
Feedback capturado sem decisão é ruído.
Feedback com decisão sem rastreabilidade é risco.
Feedback com rastreabilidade, owner e learning loop é inteligência.
```

---

# 2. O que este documento é — e o que não é

## É

- Arquitetura de sistema de feedback do CKOS
- Learning loop governado de captura → classificação → decisão → ação → aprendizado
- Sistema de sinais de qualidade que alimenta ROI, suporte, agentes e produto
- Mecanismo de melhoria contínua baseado em evidência e aprovação humana
- Fonte de input para eval, pesquisa, decisão e evolução da plataforma

## Não é

- Mural de comentários sem consequência
- Chat de suporte (ver doc 23)
- Caixa de sugestões sem owner ou decisão
- Sistema de aprovação automática de mudanças baseado em feedback
- Substituto para QA formal (doc 20)
- Sistema de treinamento automático de modelos de linguagem

---

# 3. Princípio Central

> **No feedback should disappear without classification, ownership, decision or explicit dismissal reason.**
>
> Em português: Nenhum feedback deve desaparecer sem classificação, responsável, decisão
> ou motivo explícito de descarte.

Todo feedback capturado no CKOS deve:
- Receber classificação (type, urgency, impact, sentiment) dentro do SLA definido
- Ter um `owner_id` atribuído que é responsável pela decisão
- Resultar em uma das saídas formais: converted_to_node | converted_to_task | linked_to_artifact | linked_to_support | linked_to_roi | dismissed (com rationale) | resolved
- Ter seu ciclo de vida rastreado em `feedback_status_transitions`
- Emitir eventos auditáveis em cada mudança de estado

Feedback sem owner + sem decisão + sem timestamp de resolução é um failure mode crítico (FM-F1, FM-F2).

---

# 4. Feedback Philosophy

1. **Signal-based:** Todo feedback é tratado como sinal — não como verdade. Sinais precisam de classificação, contexto e evidência para gerar ação
2. **Decision-linked:** Todo feedback resulta em uma decisão explícita — mesmo que a decisão seja "descartar com justificativa"
3. **Evidence-aware:** Feedback subjetivo não é evidência objetiva; hipóteses derivadas de feedback precisam de validação antes de alterar ROI, arquitetura ou escopo
4. **Owner-assigned:** Todo feedback tem um `owner_id` humano responsável pela resolução dentro do SLA
5. **State-machine-driven:** Feedback segue estados formais com transições auditáveis — não pode avançar informalmente
6. **ROI-connected:** Feedback que valida ou contradiz ROI aciona o pipeline de `roi_model` update de doc 21
7. **Support-aware:** Feedback que indica bloqueio, bug ou fricção operacional é roteado para o Support System (doc 23)
8. **Agent-evaluable:** Feedback sobre output de agente alimenta eval criteria e pode acionar revisão de autonomy_level
9. **Learning-loop-ready:** Feedback aprovado pode se transformar em `feedback_learning_signal` — proposta de melhoria que requer aprovação antes de ser aplicada
10. **Auditable by Metacognik:** Metacognik pode rever qualquer feedback_item e bloquear decisões incorretas (ex: uso de feedback emocional como evidência objetiva)
11. **Privacy-first:** Feedback contendo PII é mascarado antes de roteamento; visibilidade de cliente é opt-in explícito, não padrão
12. **Non-automatic:** Nenhum aprendizado derivado de feedback modifica o sistema automaticamente — toda mudança requer aprovação humana

---

# 5. Feedback Types

## 5.1 client_feedback

**Definição:** Feedback originado de um cliente externo (pagante) sobre entregáveis, propostas ou experiência.

**Origem:** Portal de cliente (futuro), aprovação de proposta, comentário de artifact, comunicação direta registrada.

**Quando usar:** Quando a fonte é o cliente pagante ou usuário-final do entregável, não a equipe interna.

**Inputs:** Comunicação de cliente, revisão de proposta, revisão de artifact, ticket de suporte com origem em cliente.

**Outputs:** Solicitação de revisão de artifact, discussão de escopo, atualização de ROI, ticket de suporte, decision request ao Founder (para mudanças de escopo).

**Risco:** Scope creep se executado sem Founder approval; exposição de PII; bias em direção à satisfação de curto prazo vs. valor estratégico.

**Quem revisa:** Client owner (Project Lead) + PMO_CKOS; feedback estratégico escala ao Founder.

**Exemplo prático:** Cliente diz "Esta proposta não aborda nossas necessidades de campanha sazonal" → solicitação de revisão de artifact + research gap + decisão de escopo.

---

## 5.2 stakeholder_feedback

**Definição:** Feedback de stakeholders internos ou externos que não são o cliente primário.

**Origem:** Sessão de revisão, fluxo de aprovação, apresentação, portal de stakeholder (futuro).

**Quando usar:** Quando stakeholder não-primário fornece input sobre entregável ou decisão.

**Inputs:** Sessão de revisão, solicitação de aprovação, apresentação de resultado.

**Outputs:** Solicitação de revisão, revisão de decisão, nota de risco, escalonamento.

**Risco:** Múltiplos inputs conflitantes sem prioridade clara → paralisia de decisão.

**Quem revisa:** Project Lead + PMO_CKOS; escala ao Founder se impactar escopo ou decisão estratégica.

**Exemplo prático:** Gerente de marca diz "Este conteúdo não está alinhado com o tom da campanha Q2" → revision request + node de alinhamento de marca.

---

## 5.3 founder_feedback

**Definição:** Feedback originado pelo Founder sobre produto, decisão arquitetural, entregável ou estratégia.

**Origem:** Input manual, decisão de aprovação, revisão, gate review.

**Quando usar:** Sempre que o Founder fornecer input sobre qualquer dimensão do projeto ou produto.

**Inputs:** Revisão de proposta, revisão de arquitetura, decisão de negócio, gate review.

**Outputs:** Ação imediata ou escalonamento com urgência alta; pode criar novo requisito de gate.

**Risco:** Feedback mal interpretado como diretiva absoluta sem registro formal; deve ser registrado explicitamente.

**Quem revisa:** PMO_CKOS registra e roteia; Metacognik valida consistência com arquitetura aprovada.

**Exemplo prático:** Founder diz "Essa estimativa de ROI é muito agressiva sem mais evidências" → `roi_model` update requerido + Metacognik audit de confiança.

---

## 5.4 user_feedback

**Definição:** Feedback de membros da equipe que usam o sistema CKOS (usuários internos).

**Origem:** CommandBar intent, ação no dashboard, comentário de node, sessão de retrospectiva.

**Quando usar:** Quando membro da equipe fornece input sobre como o sistema funciona para ele — UX, velocidade, qualidade de output.

**Inputs:** Experiência de workflow, qualidade de output de tool, fricção de interface, tempo de espera.

**Outputs:** Sugestão de melhoria de produto, friction signal, atualização de eval, task de product backlog.

**Risco:** Volume alto de feedback de usuário; maioria não converte em ação; detecção de padrão necessária antes de agir.

**Quem revisa:** QA Lead para feedback de produto; PMO_CKOS para impacto de roadmap.

**Exemplo prático:** "O comando /research demora muito e não mostra progresso" → friction signal + user_feedback → product backlog item.

---

## 5.5 agent_feedback

**Definição:** Feedback gerado por um agente sobre sua própria performance ou sobre o output de outro agente.

**Origem:** Agent self-evaluation, output_validator, agent_run eval, Metacognik warning gerado por agente.

**Quando usar:** Quando um agente detecta problema de qualidade, incerteza ou oportunidade de melhoria em seu próprio output ou de outro agente.

**Inputs:** Resultado de agent_run, eval_score, resultado de output_validator, confiança de síntese.

**Outputs:** Atualização de eval criteria, revisão de autonomy level (via Metacognik), notificação de Metacognik, sugestão de melhoria de prompt.

**Risco:** Agentes não podem reduzir/aumentar própria autonomia automaticamente; feedback deve rotear para humano antes de qualquer mudança de policy.

**Quem revisa:** Metacognik (sempre obrigatório); Technical Lead para mudanças de autonomy_level.

**Exemplo prático:** ResearchAgent flags "Fontes Tier 1 insuficientes para esta query; confiança de síntese é baixa" → agent_feedback → Metacognik review → research re-run recomendada.

---

## 5.6 qa_feedback

**Definição:** Feedback originado do processo de QA formal (doc 20) — gate reviews, domain checklists, rejeições.

**Origem:** QA Report (doc 20 §29), gate review, domain checklist, rejeição formal.

**Quando usar:** Quando QA Lead ou Metacognik identifica problema durante revisão formal.

**Inputs:** QA Report, domain checklist, critérios de gate, rejeição formal com causa.

**Outputs:** Rejeição com causa, needs_patch status, conditions list; sempre cria feedback_item com urgency ≥ high.

**Risco:** QA feedback nunca pode ser descartado silenciosamente; sempre requer resposta documentada.

**Quem revisa:** PMO_CKOS rastreia; autor ou Technical resolve; Metacognik verifica resolução.

**Exemplo prático:** "Node Canvas widget está lendo da tabela source, não de projeção" → qa_feedback critical + rejection + feedback_item urgency=critical.

---

## 5.7 system_feedback

**Definição:** Feedback automatizado gerado pelo sistema a partir de eventos, monitores ou evals.

**Origem:** Cost guard alerts, falhas de eval, loop detection, staleness de projeção, circuit breaker, policy violation events.

**Quando usar:** Quando o runtime detecta comportamento anômalo, violação de política ou breach de threshold de eval.

**Inputs:** Event bus signals, cost_guard triggers, eval_scores, loop_detection events, security events de doc 12.

**Outputs:** Criação de incidente, ticket de suporte, restrição de autonomia, notificação de Metacognik.

**Risco:** Volume de sinais do sistema pode criar ruído; precisa de filtering antes do roteamento humano.

**Quem revisa:** Technical Lead para infraestrutura; Metacognik para problemas de qualidade.

**Exemplo prático:** eval_score de síntese de pesquisa cai abaixo de 0.60 → system_feedback → revisão de eval criteria + notificação de QA Lead.

---

## 5.8 support_feedback

**Definição:** Feedback originado de ou diretamente vinculado a uma interação de suporte.

**Origem:** Resolução de support_ticket, friction_signal, comunicação de helpdesk.

**Quando usar:** Quando interação de suporte revela problema de produto, gap ou necessidade de melhoria.

**Inputs:** Notas de resolução de support_ticket, friction_signals, registros de escalonamento.

**Outputs:** Sugestão de melhoria de produto, atualização de knowledge base, material de treinamento.

**Risco:** Feedback de suporte pode refletir exceção individual, não problema sistêmico; rastreamento de recorrência necessário.

**Quem revisa:** Support lead + QA Lead para problemas de produto.

**Exemplo prático:** 3 clientes fizeram a mesma pergunta sobre o comando /workflow → gap de conhecimento identificado → atualização de documentação.

---

## 5.9 artifact_feedback

**Definição:** Feedback especificamente sobre um artifact entregado (proposta, relatório, brief visual, script).

**Origem:** Comentário de artifact, rejeição de aprovação, revisão de cliente, QA review.

**Quando usar:** Quando o feedback é direcionado a um artifact específico e seu conteúdo ou qualidade.

**Inputs:** Conteúdo do artifact, status de aprovação, reação do cliente, quality score de eval.

**Outputs:** Solicitação de revisão, nova versão do artifact, atualização de eval de qualidade.

**Risco:** Confunde preferência subjetiva com problema objetivo de qualidade; classificação necessária.

**Quem revisa:** Owner do artifact + QA Lead para problemas de qualidade.

**Exemplo prático:** "Esta seção da proposta não tem análise competitiva" → revision request + research gap + nova versão de artifact.

---

## 5.10 workflow_feedback

**Definição:** Feedback sobre como um workflow executou — velocidade, qualidade, completude.

**Origem:** Resultado de workflow_run, revisão de usuário, revisão de output de agente.

**Quando usar:** Quando o feedback é direcionado ao desempenho de um workflow específico.

**Inputs:** Dados de workflow_run, qualidade de output, tempo de execução.

**Outputs:** Sugestão de melhoria de workflow, atualização de eval criteria, otimização de prompt.

**Risco:** Problemas de run único podem não ser sistêmicos; múltiplas instâncias necessárias antes de ação.

**Quem revisa:** QA Lead + Technical Lead para problemas de orquestração.

**Exemplo prático:** "O workflow de brief de campanha não seguiu as diretrizes de brand voice em 3 de 5 assets" → padrão de workflow + feedback_learning_signal.

---

## 5.11 node_feedback

**Definição:** Feedback sobre um node específico no Node Canvas.

**Origem:** Comentário de node no canvas, rejeição de aprovação de node, Metacognik warning em node.

**Quando usar:** Quando o feedback é direcionado a um node específico (briefing, pesquisa, hipótese, decisão).

**Inputs:** Conteúdo do node, estado do node, contexto de edges.

**Outputs:** Revisão de node, mudança de status do node, estado blocked.

**Risco:** Feedback de node sem owner assignment se perde; nodes críticos bloqueados sem resolução.

**Quem revisa:** Owner do node + Project Lead.

**Exemplo prático:** "Este node de pesquisa apresenta hipótese como fato verificado" → node revision required + Metacognik flag.

---

## 5.12 roi_feedback

**Definição:** Feedback especificamente sobre modelos de ROI ou claims de valor.

**Origem:** Revisão de Founder do ROI, reação de cliente a claim de valor, auditoria de Metacognik de ROI.

**Quando usar:** Quando o feedback desafia, valida ou modifica uma claim de ROI.

**Inputs:** roi_model, roi_snapshot, proposta com seção de ROI, outcome observado.

**Outputs:** Atualização de confidence, revisão de assumption, registro de outcome, auditoria de Metacognik.

**Risco:** Feedback de ROI de cliente pode conflitar com estimativas internas; conflito deve ser documentado como `RoiContradicted`.

**Quem revisa:** Metacognik + Founder para ROI estratégico.

**Exemplo prático:** Cliente diz que a economia real foi 40% do valor estimado → roi_outcome registrado + confidence downgraded + `RoiContradicted` emitido.

---

## 5.13 research_feedback

**Definição:** Feedback sobre qualidade de pesquisa, fontes ou evidências.

**Origem:** Revisão de output de research_run, revisão de implementation brief, contestação de evidência.

**Quando usar:** Quando o feedback desafia a qualidade da pesquisa, confiabilidade de fonte ou força de evidência.

**Inputs:** Output de research_pack, evidence_items, implementation_brief.

**Outputs:** Re-run de pesquisa, re-scoring de fonte, flag de contradição de evidência, atualização de freshness.

**Risco:** Feedback de pesquisa sem especificidade não é acionável; precisa de claim + fonte específica.

**Quem revisa:** Metacognik (qualidade de evidência); Research Lead para metodologia.

**Exemplo prático:** "Este dado de benchmark é de 2021 e precisa de atualização" → staleness flag na evidence_item + research re-run requisitada.

---

## 5.14 product_feedback

**Definição:** Feedback sobre o produto CKOS em si — não sobre um entregável específico de projeto.

**Origem:** Retrospectiva de equipe, entrevista de usuário, revisão de stakeholder, input de Founder.

**Quando usar:** Quando o feedback é sobre experiência do produto CKOS, features ou roadmap.

**Inputs:** Experiência de usuário, uso de features, capacidade ausente, comparação com alternativas.

**Outputs:** Item de backlog de produto, feature request, melhoria de UX, consideração de arquitetura.

**Risco:** Feedback de produto pode expandir escopo sem governança; Founder deve aprovar mudanças de roadmap.

**Quem revisa:** PMO_CKOS + Founder para impacto de roadmap.

**Exemplo prático:** "Times querem uma versão mobile-friendly do Node Canvas read-only" → product backlog item com urgency=medium.

---

# 6. Feedback Object Model

## 6.1 feedback_item

Container principal de um sinal de feedback. Um objeto por sinal capturado.

```sql
feedback_items (
  id                      uuid PRIMARY KEY,
  tenant_id               uuid NOT NULL,           -- RLS
  org_id                  uuid NOT NULL,
  workspace_id            uuid NOT NULL,
  project_id              uuid NOT NULL,
  feedback_type           feedback_type_enum NOT NULL,
  status                  feedback_status_enum NOT NULL DEFAULT 'captured',
  urgency                 enum(critical|high|medium|low) NOT NULL,
  impact                  enum(high|medium|low|unknown) DEFAULT 'unknown',
  sentiment               enum(positive|negative|neutral|mixed|unknown) DEFAULT 'unknown',
  confidence              numeric(3,2),             -- confiança na qualidade do sinal
  title                   text NOT NULL,
  body                    text NOT NULL,
  body_redacted           text,                     -- versão segura para vista de cliente
  source_channel          feedback_channel_enum NOT NULL,
  source_actor_id         uuid,                     -- humano ou agente que originou
  source_agent_id         text,                     -- se origem for agente
  owner_id                uuid,                     -- responsável pela resolução
  affected_object_type    text,                     -- artifact|workflow|node|agent|roi_model|...
  affected_object_id      uuid,
  affected_agent_id       text,
  affected_workflow_id    uuid,
  affected_artifact_id    uuid,
  decision_required       boolean DEFAULT false,
  support_required        boolean DEFAULT false,
  roi_relevance           boolean DEFAULT false,
  security_relevance      boolean DEFAULT false,
  is_client_visible       boolean DEFAULT false,    -- opt-in explícito
  is_redacted             boolean DEFAULT false,
  has_pii                 boolean DEFAULT false,
  is_recurring            boolean DEFAULT false,
  recurrence_count        integer DEFAULT 1,
  related_feedback_ids    uuid[],                   -- para detecção de padrão
  created_by_agent_id     text,
  source_event_id         uuid,
  reopened_count          integer DEFAULT 0,
  created_at              timestamptz NOT NULL DEFAULT now(),
  updated_at              timestamptz NOT NULL DEFAULT now(),
  resolved_at             timestamptz,
  archived_at             timestamptz
)
```

**Regras:**
- RLS por `tenant_id` obrigatório
- `owner_id` deve ser atribuído dentro de SLA (24h para critical/high; 72h para medium/low)
- `is_client_visible` nunca é `true` por padrão — requer aprovação explícita de Project Lead+
- `has_pii = true` → `body` mascarado antes de roteamento externo; `body_redacted` disponibilizado
- `reopened_count` tem cap configurável (padrão: 3 reaberturas antes de escalonamento obrigatório)

---

## 6.2 feedback_thread

Discussão ou elaboração sobre um feedback_item. Permite troca contextual sem criar novos items.

```sql
feedback_threads (
  id                      uuid PRIMARY KEY,
  feedback_item_id        uuid NOT NULL REFERENCES feedback_items(id),
  tenant_id               uuid NOT NULL,
  author_id               uuid,
  author_agent_id         text,
  body                    text NOT NULL,
  body_redacted           text,
  is_internal             boolean DEFAULT true,
  is_client_visible       boolean DEFAULT false,
  created_at              timestamptz NOT NULL DEFAULT now()
)
```

---

## 6.3 feedback_source

Metadados ricos sobre a origem do feedback — canal, ator, contexto.

```sql
feedback_sources (
  id                      uuid PRIMARY KEY,
  feedback_item_id        uuid NOT NULL REFERENCES feedback_items(id),
  tenant_id               uuid NOT NULL,
  source_type             enum(command_bar|artifact_comment|node_comment|approval_rejection|qa_review|support_ticket|client_note|stakeholder_review|agent_self_eval|metacognik_warning|friction_signal|dashboard_action|external_form),
  source_url_or_ref       text,
  source_actor_type       enum(human|agent|system),
  source_actor_id         uuid,
  source_context          text,
  captured_at             timestamptz NOT NULL DEFAULT now()
)
```

---

## 6.4 feedback_decision

Decisão formal tomada sobre o feedback. Toda resolução requer uma decisão explícita.

```sql
feedback_decisions (
  id                      uuid PRIMARY KEY,
  feedback_item_id        uuid NOT NULL REFERENCES feedback_items(id),
  tenant_id               uuid NOT NULL,
  decision_type           enum(convert_to_node|convert_to_task|link_to_artifact|link_to_support|link_to_roi|dismiss|defer|escalate|investigate|create_pattern),
  decision_rationale      text NOT NULL,            -- obrigatório mesmo para dismiss
  decided_by              uuid NOT NULL,            -- humano — agentes não decidem
  decided_at              timestamptz NOT NULL,
  conditions              text,
  follow_up_required      boolean DEFAULT false,
  follow_up_by            timestamptz
)
```

**Regras:**
- `decided_by` deve ser `uuid` de humano — agentes não são `decided_by`
- `decision_rationale` é obrigatório para `decision_type = dismiss` (prevenção de FM-F6)
- `decision_type = convert_to_node` requer `feedback_node_link` criado antes de resolução

---

## 6.5 feedback_status_transition

Audit trail imutável de cada mudança de status do feedback_item.

```sql
feedback_status_transitions (
  id                      uuid PRIMARY KEY,
  feedback_item_id        uuid NOT NULL REFERENCES feedback_items(id),
  tenant_id               uuid NOT NULL,
  from_status             feedback_status_enum,
  to_status               feedback_status_enum NOT NULL,
  transitioned_by         uuid,
  transitioned_by_agent_id text,
  reason                  text,
  source_event_id         uuid,
  transitioned_at         timestamptz NOT NULL DEFAULT now()
)
```

---

## 6.6 feedback_node_link

Conexão rastreável entre feedback_item e um node do Node Canvas.

```sql
feedback_node_links (
  id                      uuid PRIMARY KEY,
  feedback_item_id        uuid NOT NULL REFERENCES feedback_items(id),
  node_id                 uuid NOT NULL,
  tenant_id               uuid NOT NULL,
  link_type               enum(generated_node|references_node|feedback_on_node|blocked_node|evidence_for_node),
  created_at              timestamptz NOT NULL DEFAULT now()
)
```

---

## 6.7 feedback_artifact_link

Conexão entre feedback e um artifact — solicitações de revisão, versionamento, bloqueios.

```sql
feedback_artifact_links (
  id                      uuid PRIMARY KEY,
  feedback_item_id        uuid NOT NULL REFERENCES feedback_items(id),
  artifact_id             uuid NOT NULL,
  tenant_id               uuid NOT NULL,
  link_type               enum(requests_revision|references_artifact|feedback_on_artifact|blocks_artifact|generated_version),
  version_created         uuid,                     -- nova versão criada se aplicável
  created_at              timestamptz NOT NULL DEFAULT now()
)
```

---

## 6.8 feedback_roi_link

Conexão entre feedback e roi_model. Coordena com o sistema de ROI de doc 21.

```sql
feedback_roi_links (
  id                      uuid PRIMARY KEY,
  feedback_item_id        uuid NOT NULL REFERENCES feedback_items(id),
  roi_model_id            uuid NOT NULL,
  tenant_id               uuid NOT NULL,
  link_type               enum(validates_roi|contradicts_roi|updates_assumption|creates_gap|records_outcome|reduces_confidence|increases_confidence|requires_audit),
  impact_description      text,
  created_at              timestamptz NOT NULL DEFAULT now()
)
```

**Regra:** `link_type = contradicts_roi` → emite `RoiContradicted` via event bus automaticamente.

---

## 6.9 feedback_support_link

Conexão entre feedback e support ticket do sistema de suporte (doc 23).

```sql
feedback_support_links (
  id                      uuid PRIMARY KEY,
  feedback_item_id        uuid NOT NULL REFERENCES feedback_items(id),
  support_ticket_id       uuid NOT NULL,
  tenant_id               uuid NOT NULL,
  link_type               enum(generated_ticket|referenced_in_ticket|resolved_by_ticket),
  created_at              timestamptz NOT NULL DEFAULT now()
)
```

---

## 6.10 feedback_agent_eval_link

Conexão entre feedback sobre agente e o sistema de eval (doc 13).

```sql
feedback_agent_eval_links (
  id                      uuid PRIMARY KEY,
  feedback_item_id        uuid NOT NULL REFERENCES feedback_items(id),
  agent_run_id            uuid NOT NULL,
  agent_id                text NOT NULL,
  tenant_id               uuid NOT NULL,
  eval_impact             enum(positive|negative|neutral),
  suggested_action        enum(none|autonomy_review|eval_criteria_update|failure_mode_register|prompt_improvement|agent_retrain),
  metacognik_review_required boolean DEFAULT false,
  metacognik_reviewed     boolean DEFAULT false,
  created_at              timestamptz NOT NULL DEFAULT now()
)
```

**Regra:** `suggested_action = autonomy_review | agent_retrain` → `metacognik_review_required = true` automaticamente. Nenhuma mudança de autonomy_level sem aprovação de Metacognik + Technical.

---

## 6.11 feedback_learning_signal

Sinal extraído do feedback para o learning loop. Proposta de melhoria que requer aprovação antes de ser aplicada.

```sql
feedback_learning_signals (
  id                      uuid PRIMARY KEY,
  feedback_item_id        uuid NOT NULL REFERENCES feedback_items(id),
  tenant_id               uuid NOT NULL,
  signal_type             enum(prompt_improvement|workflow_pattern|agent_eval_adjustment|research_gap|product_gap|knowledge_addition|policy_update|template_improvement|eval_criteria_update),
  signal_content          text NOT NULL,
  target_component        text,                     -- qual prompt/workflow/agente/policy melhorar
  confidence              numeric(3,2),
  approved_for_application boolean DEFAULT false,
  approved_by             uuid,                     -- humano
  approved_at             timestamptz,
  application_status      enum(pending|approved|applied|rejected|deferred) DEFAULT 'pending',
  applied_at              timestamptz,
  rejection_reason        text,
  created_at              timestamptz NOT NULL DEFAULT now()
)
```

**Regras:**
- `approved_for_application` nunca pode ser `true` sem `approved_by` humano
- `application_status = applied` somente após mudança verificada no componente alvo
- Metacognik revisa todos os sinais antes de `approved_for_application = true`
- Sinais com `signal_type = policy_update | agent_retrain` requerem aprovação adicional de Technical Lead

---

# 7. Feedback Data Sources

O sistema de Feedback captura e consome dados de múltiplos pontos do CKOS.

| Fonte | Tipo de sinal gerado | Feedback types alimentados |
|---|---|---|
| Command Center (intent) | Explicit user feedback intent | user_feedback, artifact_feedback, roi_feedback |
| Project Dashboard (ação) | Widget interaction, dashboard action | user_feedback, system_feedback |
| Node Canvas (comentário) | Node comment, node state change | node_feedback, artifact_feedback |
| Artifacts (comentário/rejeição) | Artifact comment, approval rejection | artifact_feedback, qa_feedback |
| Approvals (rejeição) | Approval rejected with reason | qa_feedback, founder_feedback |
| support_tickets (resolução) | Resolution note, friction signal | support_feedback, system_feedback |
| agent_outputs (output_validator) | Quality flag, confidence warning | agent_feedback, system_feedback |
| agent_eval_results | Eval score breach | agent_feedback, system_feedback |
| workflow_runs (resultado) | Completion, failure, quality score | workflow_feedback, system_feedback |
| research_outputs (review) | Evidence challenge, source weakness | research_feedback |
| roi_snapshots (contradição) | Contradição de valor observado | roi_feedback |
| project_activity_feed | Atividade anômala, reabertura | system_feedback |
| external forms (futuro) | Formulário de feedback de cliente | client_feedback, stakeholder_feedback |
| client portal (futuro) | Portal de revisão de cliente | client_feedback |
| stakeholder portal (futuro) | Portal de revisão de stakeholder | stakeholder_feedback |

---

# 8. Feedback Capture Channels

14 canais de captura formais. Cada canal emite `FeedbackCaptured` ao event bus.

| Canal | source_type | Actor típico | feedback_types |
|---|---|---|---|
| CommandBar intent | `command_bar` | user, project_lead | qualquer tipo |
| Artifact comment | `artifact_comment` | user, client | artifact_feedback |
| Node comment | `node_comment` | user, project_lead | node_feedback |
| Approval rejection | `approval_rejection` | reviewer, qa_lead | qa_feedback, founder_feedback |
| QA review | `qa_review` | qa_lead, metacognik | qa_feedback |
| Support ticket (origin) | `support_ticket` | user, client | support_feedback |
| Client note | `client_note` | client (registrado por team) | client_feedback |
| Stakeholder review | `stakeholder_review` | stakeholder | stakeholder_feedback |
| Agent self-evaluation | `agent_self_eval` | agent | agent_feedback |
| Metacognik warning | `metacognik_warning` | metacognik | qa_feedback, agent_feedback |
| System friction signal | `friction_signal` | system (automated) | system_feedback |
| Dashboard action | `dashboard_action` | user, project_lead | user_feedback |
| External form (futuro) | `external_form` | client, stakeholder | client_feedback |
| Portal de cliente (futuro) | `client_portal` | client | client_feedback |

---

# 9. Feedback Classification Framework

Todo feedback capturado deve ser classificado nesses 14 atributos antes de ser roteado.

| Atributo | Valores | Regra de classificação |
|---|---|---|
| `feedback_type` | 14 tipos (§5) | Obrigatório; definido na captura ou classificação manual |
| `urgency` | critical\|high\|medium\|low | `critical` = bloqueia; `high` = SLA 24h; `medium` = 72h; `low` = 1 semana |
| `impact` | high\|medium\|low\|unknown | Impacto no projeto, produto ou entregável |
| `confidence` | 0.00–1.00 | Confiança na qualidade do sinal (não no conteúdo) |
| `sentiment` | positive\|negative\|neutral\|mixed\|unknown | Classificado por agente de NLP ou manual |
| `affected_object_type` | artifact\|workflow\|node\|agent\|roi_model\|product\|architecture | O que foi afetado |
| `affected_object_id` | uuid | Referência específica ao objeto afetado |
| `affected_agent_id` | text | Se feedback for sobre agente específico |
| `affected_workflow_id` | uuid | Se feedback for sobre workflow específico |
| `affected_artifact_id` | uuid | Se feedback for sobre artifact específico |
| `decision_required` | boolean | Se requer decisão formal de Project Lead+ |
| `support_required` | boolean | Se indica necessidade de suporte operacional |
| `roi_relevance` | boolean | Se pode afetar estimativa ou confidence de ROI |
| `security_relevance` | boolean | Se envolve permissões, dados sensíveis ou policy |
| `owner_required` | boolean | Se não tem owner e urgência ≥ high (sempre true nesse caso) |

**Regras de classificação automática:**
- `feedback_type = qa_feedback` → `urgency ≥ high` automaticamente
- `feedback_type = founder_feedback` → `decision_required = true` automaticamente
- `security_relevance = true` → roteado para Technical antes de qualquer outro ator
- `has_pii = true` → `body_redacted` gerado antes de roteamento; `is_client_visible` bloqueado

---

# 10. Feedback State Machine

14 estados formais com transições auditadas.

```txt
States:
  captured              — feedback recém-capturado; aguarda classificação
  classified            — tipo, urgência e impacto atribuídos
  needs_owner           — classificado; sem owner atribuído ainda
  under_review          — owner atribuído; em revisão ativa
  needs_decision        — revisão concluída; decisão formal requerida
  converted_to_node     — decisão: criou node no canvas
  converted_to_task     — decisão: criou task/backlog item
  linked_to_artifact    — decisão: vinculado a revisão de artifact
  linked_to_support     — decisão: roteado para support system
  linked_to_roi         — decisão: vinculado a roi_model
  dismissed             — decisão: descartado com rationale explícito
  resolved              — ação tomada; feedback encerrado
  archived              — arquivado após resolução (auto: 90d ou explícito)
  reopened              — reaberto por nova evidência ou recorrência

Transições:
  captured          → classified          (agente ou usuário classifica)
  classified        → needs_owner         (sem owner; urgência aciona SLA)
  classified        → under_review        (owner atribuído automaticamente ou manualmente)
  needs_owner       → under_review        (owner atribuído)
  under_review      → needs_decision      (revisão completa; decisão humana requerida)
  under_review      → converted_to_node   (decisão direta: criar node)
  under_review      → converted_to_task   (decisão direta: criar task)
  under_review      → linked_to_artifact  (decisão direta: revisão de artifact)
  under_review      → linked_to_support   (decisão direta: rotear para suporte)
  under_review      → linked_to_roi       (decisão direta: vincular ROI)
  under_review      → dismissed           (decisão direta: descartar com rationale)
  needs_decision    → converted_to_node
  needs_decision    → converted_to_task
  needs_decision    → linked_to_artifact
  needs_decision    → linked_to_support
  needs_decision    → linked_to_roi
  needs_decision    → dismissed
  converted_to_node → resolved            (node criado e ação tomada)
  converted_to_task → resolved            (task criada)
  linked_to_artifact → resolved           (revisão de artifact concluída)
  linked_to_support → resolved            (ticket resolvido)
  linked_to_roi     → resolved            (ROI model atualizado)
  dismissed         → resolved            (dismissal registrado)
  resolved          → archived            (auto após 90d ou explícito)
  resolved          → reopened            (nova evidência ou recorrência detectada)
  reopened          → classified          (re-entra no ciclo)

Regras adicionais:
  - urgency=critical sem owner após 24h → escalonamento automático para PMO_CKOS
  - reopened_count > 3 → escalonamento obrigatório para Founder ou PMO_CKOS
  - status=dismissed requer feedback_decision com decision_rationale (não-nulo)
  - status=resolved sem feedback_decision → transição bloqueada
  - Nenhum agente pode marcar como dismissed — apenas humanos
```

---

# 11. Feedback Events

16 eventos conectados ao event bus de doc 10.

| Evento | Publisher | Subscribers | Schema mínimo |
|---|---|---|---|
| `FeedbackCaptured` | qualquer canal | feedback_router, classification_agent | item_id, feedback_type, urgency, source_channel, tenant_id |
| `FeedbackClassified` | classification_agent ou user | feedback_router, dashboard | item_id, urgency, impact, sentiment, decision_required |
| `FeedbackOwnerAssigned` | pmo_ckos ou system | owner (notification), dashboard | item_id, owner_id, sla_deadline |
| `FeedbackReviewStarted` | owner | dashboard | item_id, owner_id |
| `FeedbackDecisionRequested` | owner | decision_actors (routing) | item_id, decision_required_from, urgency |
| `FeedbackConvertedToNode` | feedback_agent | canvas_projection_engine | item_id, node_id, node_type, tenant_id |
| `FeedbackConvertedToTask` | feedback_agent | task_manager | item_id, task_id, tenant_id |
| `FeedbackLinkedToArtifact` | feedback_agent | artifact_engine | item_id, artifact_id, link_type, version_created |
| `FeedbackLinkedToSupport` | feedback_agent | support_router | item_id, support_ticket_id, tenant_id |
| `FeedbackLinkedToRoi` | feedback_agent | roi_projection_engine | item_id, roi_model_id, link_type (contradicts_roi → também emite RoiContradicted) |
| `FeedbackDismissed` | human (via system) | dashboard, audit_log | item_id, decided_by, decision_rationale |
| `FeedbackResolved` | system (após action) | dashboard, audit_log | item_id, resolution_type, resolved_at |
| `FeedbackReopened` | human ou system | feedback_router, owner | item_id, reason, reopened_count |
| `FeedbackPatternDetected` | pattern_detection_agent | pmo_ckos, metacognik, dashboard | pattern_type, feedback_ids[], recurrence_count, affected_component |
| `FeedbackLearningSignalCreated` | feedback_agent ou Metacognik | learning_loop_engine | signal_id, signal_type, target_component, confidence |
| `FeedbackPiiDetected` | pii_detector | security_monitor, owner | item_id, pii_type, redaction_required |

**Regras de eventos:**
- Todos os eventos passam pelo event bus de doc 10 §5.3 — nunca direto do frontend
- `audit_log` entry para cada evento que muta estado de `feedback_item`
- `FeedbackLinkedToRoi` com `link_type = contradicts_roi` → emite `RoiContradicted` como evento separado

---

# 12. Feedback Routing Rules

Regras que determinam para quem e como cada feedback é roteado após classificação.

| Tipo de feedback | Urgência | Roteado para | Condição |
|---|---|---|---|
| `artifact_feedback` | critical | Artifact owner + QA Lead | Imediato |
| `artifact_feedback` | high/medium | Artifact owner | SLA 24h/72h |
| `roi_feedback` | qualquer | ROI agent + Metacognik | Sempre |
| `agent_feedback` | qualquer | Metacognik | Sempre — agente não decide sobre si mesmo |
| `system_feedback` | critical | Technical Lead | Imediato |
| `system_feedback` | high | QA Lead + Technical | SLA 24h |
| `qa_feedback` | critical | PMO_CKOS + autor | Bloqueia gate imediatamente |
| `founder_feedback` | qualquer | PMO_CKOS registra + executa | Prioridade máxima |
| `client_feedback` (escopo) | qualquer | Client owner + PMO_CKOS + Founder | Founder obrigatório para mudança de escopo |
| `security_relevance = true` | qualquer | Technical Lead | Antes de qualquer outro ator |
| `support_required = true` | qualquer | Support System (doc 23) | Cria support_ticket via FeedbackLinkedToSupport |
| `research_feedback` | qualquer | Metacognik + Research Lead | Metacognik valida evidência |
| `product_feedback` | qualquer | PMO_CKOS | Founder se impacta roadmap |
| Recorrente (recurrence_count ≥ threshold) | qualquer | PMO_CKOS + Metacognik | FeedbackPatternDetected emitido |

**Regras de escalonamento:**
- `urgency = critical` sem owner em 24h → escalonamento automático para PMO_CKOS
- `security_relevance = true` → Technical Lead notificado antes de qualquer roteamento
- `has_pii = true` → `body_redacted` obrigatório; nunca rotear body original para canal externo
- `decision_required = true` + sem decision após SLA → escalonamento para Founder

---

# 13. Feedback e Command Center

O Command Center (doc 15) processa intenções de feedback como qualquer outro intent — sem lógica própria.

## 13.1 Intenções de feedback (parte da família #9 — Feedback & Support)

| Intenção em linguagem natural | intent_type | Evento emitido |
|---|---|---|
| "Registrar feedback sobre este artifact" | `action.feedback.create_artifact` | `FeedbackCaptured` |
| "Transforme esse feedback em node" | `action.feedback.convert_to_node` | `FeedbackConvertedToNode` |
| "Esse feedback muda a proposta?" | `query.feedback.proposal_impact` | `FeedbackQueried` |
| "Quais feedbacks estão pendentes?" | `query.feedback.pending_list` | `FeedbackListQueried` |
| "Mostre feedbacks críticos" | `query.feedback.critical_filter` | `FeedbackListQueried` |
| "Quais feedbacks alteraram decisões?" | `query.feedback.decision_impact` | `FeedbackQueried` |
| "Reabra esse feedback" | `action.feedback.reopen` | `FeedbackReopened` |
| "Descarte com justificativa" | `action.feedback.dismiss` | `FeedbackDismissed` |
| "Esse feedback afeta o ROI?" | `query.feedback.roi_relevance` | `FeedbackQueried` → `RoiQueried` |
| "Criar learning signal deste feedback" | `action.feedback.create_signal` | `FeedbackLearningSignalCreated` |

## 13.2 Regras do Command Center para Feedback

1. CommandBar envia intent ao runtime — nunca grava feedback diretamente em tabela
2. `action.feedback.*` requerem permissão mínima `project_member` (para criar) ou `project_lead` (para converter/descartar)
3. `action.feedback.dismiss` requer `decision_rationale` obrigatório no payload do intent
4. Resposta do runtime é exibida como projeção — não como dado live
5. Intenções que afetam ROI emitem evento adicional para `roi_projection_engine`

---

# 14. Feedback e Project Dashboard

O Project Dashboard (doc 14) exibe feedback como projeção de aprendizado e qualidade.

## 14.1 Widgets de Feedback

| Widget | O que exibe | Fonte de projeção |
|---|---|---|
| **Feedback Loop** | Visão geral: pendentes, críticos, convertidos, resolvidos | `feedback_loop_projection` |
| **Pending Feedback** | Feedback sem owner ou sem decisão além do SLA | `feedback_loop_projection` |
| **Critical Feedback** | Todos os `urgency = critical` abertos | `feedback_loop_projection` |
| **Feedback Converted to Nodes** | Feedback que gerou nodes no canvas | `feedback_loop_projection` + `canvas_graph_projection` |
| **Feedback Impacting ROI** | Feedback linkado a roi_models (contradições ou validações) | `feedback_loop_projection` + `roi_snapshot_projection` |
| **Feedback Awaiting Decision** | `status = needs_decision` além de SLA | `feedback_loop_projection` |
| **Feedback Trend** | Tendência: volume, urgência, types ao longo do tempo | `feedback_loop_projection` |
| **Recurrent Frictions** | Padrões detectados (FeedbackPatternDetected) | `feedback_loop_projection` |

## 14.2 Regras do Dashboard para Feedback

1. Dashboard lê exclusivamente de `feedback_loop_projection` — nunca de `feedback_items` diretamente
2. Cliente nunca vê `body` de feedback sem `is_client_visible = true` + aprovação de Project Lead
3. Click em qualquer widget envia intent ao Command Center — não executa ação direta
4. `feedback_loop_projection` é atualizada por evento (FeedbackCaptured, FeedbackResolved, FeedbackReopened, etc.)
5. Dados financeiros dentro de feedback (custo, ROI) seguem regras de permissão de §22

---

# 15. Feedback e Node Canvas

O Node Canvas (doc 16) exibe feedback convertido em nodes e edges operacionais.

## 15.1 Node Types de Feedback

| node_type | O que representa | Criado por | Eventos emitidos |
|---|---|---|---|
| `feedback_node` | feedback_item convertido em objeto visível do canvas | Manual ou FeedbackConvertedToNode | `FeedbackConvertedToNode` |
| `feedback_decision_node` | Decisão tomada a partir de feedback | Manual após feedback_decision | `FeedbackDecisionRequested` |
| `feedback_gap_node` | Gap de produto, pesquisa ou processo derivado de padrão de feedback | FeedbackPatternDetected | `FeedbackPatternDetected` |
| `feedback_support_node` | Feedback roteado para suporte | FeedbackLinkedToSupport | `FeedbackLinkedToSupport` |
| `feedback_roi_node` | Feedback que afeta ROI | FeedbackLinkedToRoi | `FeedbackLinkedToRoi` |
| `feedback_artifact_revision_node` | Solicitação de revisão de artifact derivada de feedback | FeedbackLinkedToArtifact | `FeedbackLinkedToArtifact` |

## 15.2 Edge Types de Feedback

| edge_type | Conecta | Direção |
|---|---|---|
| `feedback` | feedback_node → qualquer node afetado | feedback aponta para objeto alvo |
| `decision` | feedback_node → feedback_decision_node | feedback gerou decisão |
| `support` | feedback_node → feedback_support_node | feedback roteou para suporte |
| `roi` | feedback_node → feedback_roi_node | feedback afeta ROI |
| `artifact` | feedback_node → feedback_artifact_revision_node | feedback pede revisão |
| `blocked_by` | node afetado → feedback_node | node bloqueado por feedback crítico |
| `evidence` | feedback_node → evidence_node | feedback fornece evidência |
| `contradicts` | feedback_node → roi_node | feedback contradiz ROI |

## 15.3 Regras do Node Canvas para Feedback

1. `feedback_node` com `urgency = critical` tem badge vermelho visível
2. Canvas não cria feedback_item diretamente — toda captura via evento do canal de origem
3. Side panel de feedback_node exibe: status, owner, urgency, sentiment, affected_object, decision, thread
4. `feedback_node` com `is_client_visible = false` não aparece em vistas de cliente (permission filter)
5. Converter feedback em node → `FeedbackConvertedToNode` evento emitido → audit_log entry

---

# 16. Feedback e Artifacts

Feedback sobre artifacts aciona um pipeline específico de revisão e versionamento.

## 16.1 O que feedback pode fazer a um artifact

| Ação de feedback | Resultado | Condição |
|---|---|---|
| Solicitar revisão | `feedback_artifact_link` com `link_type = requests_revision` | Urgência ≥ medium |
| Criar nova versão | Nova versão de artifact gerada após revisão | Após aprovação de revisão |
| Bloquear aprovação | Artifact não pode ser aprovado enquanto feedback crítico estiver aberto | `urgency = critical` |
| Reabrir artifact | Artifact volta a estado `under_review` ou `needs_revision` | Após feedback pós-aprovação |
| Gerar QA review | QA review formal iniciado para artifact | `feedback_type = qa_feedback` |
| Gerar decision request | Decisão formal requerida sobre escopo ou mudança | `decision_required = true` |

## 16.2 Regras de artifact com feedback

1. **Artifact aprovado não pode ser alterado silenciosamente** — toda mudança cria nova versão com `source_event_id` do FeedbackLinkedToArtifact
2. Feedback crítico sobre artifact aprovado → estado da aprovação reverte para `needs_review`
3. Nova versão de artifact derivada de feedback deve referenciar o `feedback_item_id` original
4. `feedback_artifact_link` com `link_type = blocks_artifact` impede qualquer entrega até resolução
5. Feedback de cliente sobre artifact requer `is_client_visible = false` no thread interno de resolução

---

# 17. Feedback e ROI

Feedback é um dos principais sinais de ajuste do sistema de ROI (doc 21).

## 17.1 Mapeamento feedback → efeito em ROI

| Tipo de feedback | link_type em feedback_roi_link | Efeito no roi_model |
|---|---|---|
| Positivo sobre entrega (qualidade percebida) | `validates_roi` | Pode aumentar confidence_score; suporta roi_hypothesis |
| Negativo sobre entrega (retrabalho, insatisfação) | `contradicts_roi` | Reduz confidence; emite `RoiContradicted` |
| Sobre custo real (maior que estimado) | `updates_assumption` ou `contradicts_roi` | Atualiza assumption de custo; recalcula confidence |
| Sobre valor percebido (menor que estimado) | `reduces_confidence` | Confidence downgraded; Metacognik notificado |
| Sobre outcome real observado | `records_outcome` | Adiciona roi_outcome verificado ao modelo |
| Sobre assumption que se provou errada | `updates_assumption` | Assumption invalidada; roi_model recalculado |
| Sobre gap em estimativa | `creates_gap` | roi_gap criado no modelo afetado |
| Que exige revisão completa | `requires_audit` | Metacognik audit obrigatório |

## 17.2 Fluxo feedback → ROI

```txt
FeedbackCaptured (roi_relevance=true)
  → feedback_classification_agent: classifica link_type
  → FeedbackLinkedToRoi emitido
  → roi_agent: cria feedback_roi_link
  → Se link_type=contradicts_roi: emite RoiContradicted adicionalmente
  → roi_projection_engine: invalida roi_snapshot_projection
  → roi_snapshot regenerado com novo confidence_level
  → Dashboard widget atualizado
  → Se confidence_level downgraded para low/speculative: Metacognik notificado
```

---

# 18. Feedback e Support

Feedback vira suporte quando sinaliza bloqueio operacional, bug ou fricção que impede o usuário de avançar.

## 18.1 Quando feedback é roteado para Support System

| Condição do feedback | Ação de roteamento |
|---|---|
| Usuário não consegue executar ação | `support_required = true` → `FeedbackLinkedToSupport` |
| Bug identificado no sistema | `feedback_type = system_feedback` + `urgency = critical/high` → ticket P0/P1 |
| Dúvida operacional recorrente | `is_recurring = true` + `feedback_type = user_feedback` → ticket + knowledge gap |
| Fricção recorrente detectada | `FeedbackPatternDetected` → support ticket + product gap node |
| Erro de permissão | `security_relevance = true` → Technical + ticket imediato |
| Problema de cobrança ou crédito | `feedback_type = client_feedback` com conteúdo de billing → ticket + doc 24 routing |
| Falha de agente que bloqueou workflow | `affected_agent_id` + `urgency = high` → ticket P1 |

## 18.2 Regras de roteamento feedback → support

1. `FeedbackLinkedToSupport` cria `support_ticket` via event bus (doc 23) — nunca chamada direta
2. Ticket de suporte gerado herda `urgency` do feedback_item
3. Resolução do ticket emite `FeedbackResolved` no feedback_item original
4. Feedback de suporte com `is_recurring = true` → `FeedbackPatternDetected` antes de resolução individual

---

# 19. Feedback e Agents

Feedback sobre agentes é tratado com protocolo especial — agentes não decidem sobre si mesmos.

## 19.1 O que feedback pode fazer em relação a agentes

| Ação de feedback | Efeito em agente | Aprovação requerida |
|---|---|---|
| Avaliação positiva de output | Contribui para eval_score positivo | Metacognik registra (sem aprovação formal) |
| Avaliação negativa de output | Contribui para eval_score negativo; aciona revisão | Metacognik review obrigatório |
| Registrar failure mode | Novo failure mode na documentação do agente | Technical + PMO_CKOS |
| Criar sugestão de melhoria | `feedback_learning_signal` com `signal_type = agent_eval_adjustment` | Metacognik + Technical |
| Reduzir autonomy level | Proposta de redução de autonomy | Metacognik + Technical + Founder se autonomy_level ≥ 3 |
| Acionar Metacognik review | Metacognik audita agent_run e output | Automático para `metacognik_review_required = true` |
| Bloquear ação futura | Policy change temporária para agent_run | Technical |

## 19.2 Regras de feedback sobre agentes

1. Agentes nunca são `decided_by` em `feedback_decision` sobre si mesmos
2. `suggested_action = autonomy_review` → sempre `metacognik_review_required = true`
3. Qualquer mudança de autonomy_level requer Technical + Metacognik; se `autonomy_level ≥ 3`, também Founder
4. `feedback_learning_signal` derivado de agent_feedback não é aplicado sem `approved_by` humano
5. Agent feedback sobre outro agente → Metacognik review obrigatório (previne conflito entre agentes)

---

# 20. Feedback e Research

Feedback sobre pesquisa protege a qualidade das evidências que alimentam ROI, decisões e hipóteses.

## 20.1 O que feedback faz ao sistema de pesquisa

| Sinal de feedback | Efeito em research | Mecanismo |
|---|---|---|
| "Fonte está desatualizada" | `is_stale = true` na evidence_item; tier downgrade | FeedbackLinkedToArtifact → research_agent |
| "Fonte fraca para esse claim" | `reliability_score` reavaliado | Metacognik → re-score |
| "Evidência contradiz decisão" | `contradiction_ids` atualizado; Metacognik alerta | ContradictionDetected emitido |
| "Nova fonte disponível" | Research re-run requisitada | Novo research_intent criado |
| "Benchmark incorreto" | evidence_item invalidada; assumption afetada | roi_assumption.status → `under_review` |
| "Pesquisa incompleta" | roi_gap criado; research_feedback_signal criado | feedback_learning_signal |

## 20.2 Regras de feedback sobre research

1. Feedback que invalida evidência deve ser vinculado ao `evidence_item` específico (não genérico)
2. Invalidação de evidência com `source_tier = 1` requer Metacognik review antes de processar
3. Research re-run derivada de feedback segue mesmo pipeline de doc 18 (policy, cost guard, collector approval)
4. Feedback sobre research de Manus → máximo Tier 4; nunca promover para Tier 1 retroativamente

---

# 21. Feedback e QA

O sistema de QA (doc 20) e o sistema de Feedback são bidirecionalmente dependentes.

## 21.1 QA gera feedback

- Toda rejeição de gate (doc 20) cria automaticamente um `feedback_item` com `feedback_type = qa_feedback` e `urgency ≥ high`
- `changes_requested` em review cria feedback_thread no feedback_item correspondente
- Metacognik warning em qualquer domínio cria `agent_feedback` ou `qa_feedback` conforme contexto
- Domain checklist item com `✗` cria feedback_item rastreável

## 21.2 Feedback retroalimenta QA

- Feedback crítico aberto bloqueia gate submission (exemplo: feedback de cliente sobre artifact em Gate K)
- Padrões de feedback recorrente (`FeedbackPatternDetected`) geram novos critérios de domain checklist
- `feedback_learning_signal` aprovado pode atualizar domain checklists via patch formal no doc 20
- `feedback_resolution_time` e `feedback_reopen_rate` são métricas de QA do próprio sistema de feedback

## 21.3 Regras de integração QA ↔ Feedback

1. **QA feedback tem prioridade** — `feedback_type = qa_feedback` com `urgency = critical` bloqueia gate
2. **Rejection sempre cria feedback** — rejeição sem `feedback_item` vinculado é FM-F13
3. **Dismissed feedback precisa justificativa** — `decision_rationale` obrigatório; QA Lead pode reabrir se insuficiente
4. **Feedback crítico precisa owner** — `urgency = critical` sem `owner_id` em 24h → escalonamento automático

---

# 22. Feedback Permissions

## 22.1 Matriz de permissões por ação de feedback

| Ação | Roles autorizados | Restrição |
|---|---|---|
| Criar feedback_item | project_member+ | RLS por tenant_id + project_id |
| Ver feedback_item (interno) | project_member+ | Feedback de outros projetos não visível |
| Ver feedback com `security_relevance` | admin, founder, technical | Nunca project_member |
| Editar feedback_item | owner_id ou project_lead+ | Apenas owner ou lead+ |
| Descartar feedback | project_lead+ | `decision_rationale` obrigatório |
| Converter em node | project_lead+ | Requer canvas access |
| Vincular a ROI | project_lead+, founder | ROI é dado sensível |
| Tornar visível ao cliente | project_lead+ | Opt-in explícito; não padrão |
| Ver `body` de feedback com PII | admin, technical | `body_redacted` para outros |
| Criar feedback_learning_signal | project_lead+, metacognik | |
| Aprovar feedback_learning_signal | technical, metacognik, founder (por tipo) | Nunca auto-aprovado |
| Ver feedback de outros tenants | Impossível | RLS enforced |

## 22.2 Vista de cliente

- Cliente **nunca** vê feedback interno por padrão (`is_client_visible = false` default)
- Para exibir feedback ao cliente: `is_client_visible = true` + aprovação de Project Lead ou superior
- Vista de cliente sempre usa `body_redacted` quando `is_redacted = true`
- Feedback sobre pricing, custo interno ou arquitetura nunca é `is_client_visible = true`

---

# 23. Feedback Privacy e Redaction

## 23.1 Categorias de privacidade

| Categoria | Regra | Campos afetados |
|---|---|---|
| **PII** | `has_pii = true` → `body_redacted` gerado; body original acessível apenas a admin/technical | `body`, `body_redacted` |
| **Client visible** | `is_client_visible = false` por padrão; opt-in explícito por Project Lead+ | `body`, `feedback_thread.body` |
| **Internal only** | `is_internal = true` em feedback_thread → nunca exposto externamente | `feedback_thread.body` |
| **Sensitive feedback** | `security_relevance = true` → restrito a admin, technical, founder | `body`, `feedback_source.source_context` |
| **Agent-private** | `source_type = agent_self_eval` → agente não vê feedback sobre si mesmo de outros agentes | Routing policy |
| **Legal-sensitive** | Feedback sobre compliance, data breach → `security_relevance = true` + Legal notificado | Isolamento por label |
| **Support-sensitive** | Feedback de suporte com dados financeiros → segue regras de doc 23 + doc 24 | Cross-system redaction |

## 23.2 Redacted summaries

- Todo feedback com `has_pii = true` tem `body_redacted` gerado automaticamente por PII detector antes de roteamento
- `body_redacted` substitui nomes, e-mails, documentos, telefones por `[REDACTED]` com tipo identificado
- `body_redacted` é o único campo exibido em: cliente, stakeholder externo, relatórios exportáveis, dashboard de projeto (para project_member)
- `body` original preservado em tabela com acesso restrito por RLS + RBAC

---

# 24. Feedback Metrics

Métricas de saúde do sistema de feedback — alimentam eval e dashboard.

| Métrica | Definição | Target MVP |
|---|---|---|
| `feedback_count` | Total de feedback_items capturados no período | — (baseline) |
| `critical_feedback_count` | Feedback com `urgency = critical` no período | < 5% do total |
| `unresolved_feedback` | Feedback sem resolved_at além do SLA | < 10% |
| `feedback_resolution_time` | Tempo médio captured_at → resolved_at por urgência | critical < 24h; high < 72h |
| `feedback_to_node_rate` | % de feedback convertido em node | ≥ 20% (excluindo dismissed) |
| `feedback_to_artifact_revision_rate` | % de artifact_feedback que gerou nova versão | ≥ 50% (urgency ≥ high) |
| `feedback_reopen_rate` | % de feedback resolvido que foi reaberto | < 15% |
| `recurring_friction_count` | Padrões detectados por `FeedbackPatternDetected` | Rastrear; target: decrescer |
| `feedback_impact_on_roi` | Nº de roi_models afetados por feedback no período | — (baseline) |
| `agent_feedback_score` | Score médio de eval_impact de `feedback_agent_eval_links` | ≥ 0.65 |
| `stakeholder_feedback_sentiment` | Distribuição de sentiment de stakeholder_feedback | ≥ 60% positive/neutral |
| `dismissed_without_rationale_rate` | % de dismissed com `decision_rationale = null` | 0% (bloqueado por validação) |
| `owner_assignment_time` | Tempo médio captured → owner_assigned para urgency=critical | < 2h |
| `learning_signal_application_rate` | % de feedback_learning_signals aprovados e aplicados | ≥ 40% em 90d |

---

# 25. Feedback Learning Loop

O learning loop transforma feedback acumulado em melhoria sistemática — com aprovação obrigatória em cada etapa.

## 25.1 Ciclo completo

```txt
1. CAPTURED
   Sinal de feedback recebido de qualquer canal

2. CLASSIFIED
   Tipo, urgência, impacto, sentimento, objetos afetados atribuídos

3. ROUTED
   Roteado para owner, ator e sistema corretos (§12)

4. REVIEWED
   Owner analisa feedback com contexto; thread de discussão se necessário

5. DECISION
   Decisão formal registrada em feedback_decision (convert | dismiss | link | escalate)

6. ACTION
   Ação executada: node criado, artifact revisado, ticket aberto, ROI atualizado

7. OUTCOME
   Resultado da ação observado e registrado (resolução, melhoria, nova versão)

8. LEARNING_SIGNAL
   Pattern detection + Metacognik identifica sinal aprendível
   → feedback_learning_signal criado com signal_type, target_component, confidence

9. REVIEW (Metacognik)
   Metacognik valida: sinal é real? generalizável? não contradiz arquitetura aprovada?

10. HUMAN APPROVAL
    Technical / PMO_CKOS / Founder aprovam conforme signal_type:
    - prompt_improvement → PMO_CKOS
    - workflow_pattern → Technical
    - agent_eval_adjustment → Technical + Metacognik
    - policy_update → Technical + Founder
    - product_gap → PMO_CKOS + Founder

11. APPLICATION (quando approved_for_application=true)
    Sinal aplicado ao componente alvo:
    - prompt_library (doc 08)
    - workflow_blueprints (doc 07)
    - agent_registry (policy update)
    - policy engine
    - domain QA checklists (doc 20)
    - knowledge_base do projeto

12. VERIFICATION
    Verificação de que o componente alvo foi atualizado corretamente
    → application_status = applied
    → Novo eval run para confirmar melhoria
```

## 25.2 Regras do learning loop

1. **Nunca automático:** Nenhum sinal de aprendizado é aplicado sem `approved_by` humano
2. **Metacognik obrigatório:** Todo sinal passa por Metacognik antes de aprovação para aplicação
3. **Scope preservado:** Sinal aplicado não pode expandir escopo além do target_component declarado
4. **Rollback possível:** Todo sinal aplicado tem rollback plan definido antes da aplicação
5. **Auditável:** Cada etapa do loop tem `source_event_id` rastreável
6. **Não-modificação de modelos:** `feedback_learning_signal` não treina foundation models — apenas documenta e aplica melhorias em componentes CKOS (prompts, workflows, policies, templates)

---

# 26. MVP P0

## 26.1 Em escopo para P0

| Componente | Escopo P0 |
|---|---|
| `feedback_item` | Criação manual via CommandBar + geração automática por rejection/QA |
| `feedback_types` | 5 tipos: `client_feedback`, `user_feedback`, `qa_feedback`, `system_feedback`, `artifact_feedback` |
| `feedback_thread` | Discussão interna por item |
| `feedback_status_transitions` | Audit trail de todas as transições |
| Classificação | Manual por owner ou PMO_CKOS |
| Owner assignment | Manual |
| Status transitions | captured → classified → under_review → converted_to_node / linked_to_artifact / linked_to_support / dismissed / resolved |
| `feedback_decision` | Registro manual de decisão |
| `convert_to_node` | Manual via CommandBar intent |
| `link_to_artifact` | Manual via CommandBar intent |
| `link_to_support` | Manual → cria support_ticket via event |
| Feedback Loop widget no Dashboard | Básico: pending count + critical count + resolved count |
| Command Center intents | 4 intents: `create_artifact`, `pending_list`, `critical_filter`, `dismiss` |
| QA feedback path | Rejeição de gate cria feedback_item automaticamente |

## 26.2 Fora do escopo P0

| Componente | Por que adiado |
|---|---|
| Sentiment analysis automático (NLP) | Requer modelo de NLP integrado; P1+ |
| `feedback_roi_link` | ROI MVP cobre apenas 3 tipos; integração completa em P1 |
| `feedback_agent_eval_link` | Agent autonomy review é Gate G; P1+ |
| `feedback_learning_signal` aplicação automática | Nunca automático; processo manual em P1 |
| Pattern detection automático (`FeedbackPatternDetected`) | P1 — requer volume de dados |
| External form integration | Gate H (External Tools); P1+ |
| Client portal completo | Produto futuro; pós-launch |
| Stakeholder portal | Produto futuro; pós-launch |
| Advanced analytics (tendências, BI) | Gate F completo; P1+ |
| `feedback_types` restantes (9 tipos) | Adicionados progressivamente em P1–P2 |
| PII auto-detection | P1 — requer PII detector integrado |

---

# 27. Failure Modes

| # | Failure Mode | Sintoma | Mitigação |
|---|---|---|---|
| FM-F1 | Feedback sem owner | `owner_id = null` + urgency ≥ high além de 24h | Escalonamento automático; SLA enforced; validação na classificação |
| FM-F2 | Feedback ignorado | `status = captured` sem transição por 30+ dias | Monitor de SLA; PMO_CKOS notificado; relatório de `unresolved_feedback` |
| FM-F3 | Feedback duplicado | Múltiplos items idênticos sobre mesmo objeto sem deduplicação | Pattern detection + `related_feedback_ids`; classificador detecta duplicatas |
| FM-F4 | Feedback tratado como fato | Sentiment negativo usado como evidência objetiva em ROI ou decisão | Metacognik bloqueia; feedback ≠ evidence_item; doc 21 §11 ER5 |
| FM-F5 | Feedback privado mostrado ao cliente | `is_client_visible = true` sem aprovação de Project Lead | `is_client_visible = false` padrão; permissão obrigatória para ativar |
| FM-F6 | Feedback crítico descartado sem justificativa | `status = dismissed` com `decision_rationale = null` | Validação server-side; `decision_rationale` obrigatório (prevenido em §6.4) |
| FM-F7 | Feedback converte em node errado | Feedback de workflow vira briefing_node em vez de gap_node | Classification framework §9; validação de node_type no routing |
| FM-F8 | Feedback reabre artifact aprovado sem versioning | Alteração silenciosa de artifact aprovado sem nova versão | Regra §16.2: toda mudança cria versão com source_event_id obrigatório |
| FM-F9 | Feedback contradiz ROI sem acionar audit | `FeedbackLinkedToRoi` com `contradicts_roi` sem `RoiContradicted` | Evento automático: `contradicts_roi` → emite `RoiContradicted` (§11) |
| FM-F10 | Feedback de suporte não vira ticket | Bug ou fricção capturada mas `support_required` não detectado | Classification rule: `urgency = critical + system_feedback` → `support_required = true` |
| FM-F11 | Agent feedback reduz autonomia sem approval | Agente auto-modifica `autonomy_level` com base em próprio feedback | Policy: agentes não são `decided_by`; mudança de autonomy_level requer Technical + Metacognik |
| FM-F12 | Feedback de cliente altera escopo sem Founder | `client_feedback` gera scope change sem decisão formal | `decision_required = true` automático para escopo; Founder obrigatório (§12 routing) |
| FM-F13 | Feedback de QA não bloqueia release | `qa_feedback critical` em Gate K sem bloquear | Regra §21.3 #1: `qa_feedback + critical` bloqueia gate automaticamente |
| FM-F14 | Feedback emocional vira decisão sem evidência | Sentimento negativo cria roi_gap ou node sem claim específico | Metacognik bloqueia; `sentiment ≠ evidence`; rationale obrigatório |
| FM-F15 | Feedback recorrente não vira gap | `recurrence_count ≥ threshold` sem `FeedbackPatternDetected` | Pattern detection trigger com threshold configurável; PMO_CKOS notificado |
| FM-F16 | PII no feedback | `has_pii = false` mas body contém dado pessoal | PII detector (P1); validação manual em P0; `body_redacted` obrigatório quando flagrado |
| FM-F17 | Feedback sem tenant isolation | feedback_item visível cross-tenant | RLS obrigatório em todas as tabelas; Security QA §11 |
| FM-F18 | Feedback loop infinito | Feedback gera node, node gera feedback, sem resolução; `reopened_count` sem cap | `reopened_count > 3` → escalonamento obrigatório para Founder; cap configurável |
| FM-F19 | Feedback sem relação com objeto | `affected_object_id = null` com `urgency = critical`; não roteável | Validação: `urgency = critical` requer `affected_object_id` ou `affected_agent_id` |
| FM-F20 | Feedback usado para treinar agente sem permissão | `feedback_learning_signal` aplicado sem `approved_by` humano | Validação: `approved_for_application = true` requer `approved_by` não-nulo (§6.11) |
| FM-F21 | Feedback de agente sobre agente sem Metacognik | `agent_feedback` sobre outro agente sem trigger de revisão | Regra §19.2 #5: agent feedback cross-agent → Metacognik review obrigatório |
| FM-F22 | Feedback estratégico sem Founder awareness | `product_feedback` com impacto de roadmap sem notificação ao Founder | Routing rule §12: `product_feedback + decision_required` → PMO_CKOS + Founder |

---

# 28. Required Patches

Os patches abaixo foram identificados durante a criação deste documento. Estão **registrados como sugestões** — não aplicados.

| Patch | Doc alvo | Versão alvo | Descrição | Urgência |
|---|---|---|---|---|
| **P22-1** | `11_DATA_MODEL_AND_PERSISTENCE.md` | v1.3.x | Adicionar tabela `feedback_roi_links` ao §31 Feedback System Data Model (schema: id, feedback_item_id, roi_model_id, tenant_id, link_type, impact_description) | Antes de Gate I |
| **P22-2** | `11_DATA_MODEL_AND_PERSISTENCE.md` | v1.3.x | Adicionar tabela `feedback_support_links` ao §31 (schema: id, feedback_item_id, support_ticket_id, tenant_id, link_type) | Antes de Gate I |
| **P22-3** | `11_DATA_MODEL_AND_PERSISTENCE.md` | v1.3.x | Adicionar tabela `feedback_agent_eval_links` ao §31 (schema: id, feedback_item_id, agent_run_id, agent_id, tenant_id, eval_impact, suggested_action, metacognik_review_required) | Antes de Gate G |
| **P22-4** | `11_DATA_MODEL_AND_PERSISTENCE.md` | v1.3.x | Adicionar tabela `feedback_learning_signals` ao §31 (schema: id, feedback_item_id, tenant_id, signal_type, signal_content, target_component, confidence, approved_for_application, approved_by, application_status) | Antes de Gate J |
| **P22-5** | `11_DATA_MODEL_AND_PERSISTENCE.md` | v1.3.x | Verificar e expandir `feedback_loop_projection` em §21 com campos: `pending_count`, `critical_count`, `resolved_count`, `converted_to_node_count`, `pattern_count`, `roi_linked_count`, `avg_resolution_time_hours` | Antes de Gate E |
| **P22-6** | `10_SYSTEM_RUNTIME_ARCHITECTURE.md` | v1.2.x | Adicionar `feedback_routing_engine` e `feedback_classification_agent` como componentes nomeados do runtime (similar a `roi_projection_engine` de P21-4) | Antes de Gate I |

> Os patches acima são sugeridos e registrados em ARCHITECTURE_PATCH_REPORT.md §22.
> **Não aplicar** sem aprovação Technical + PMO_CKOS e versão incremental nos docs afetados.

---

# 29. Related Notes

- [[10_SYSTEM_RUNTIME_ARCHITECTURE]] — event bus, classification_agent, routing_engine, projection engine
- [[11_DATA_MODEL_AND_PERSISTENCE]] — tabelas feedback_items/threads/sources/decisions/node_links/artifact_links/status_transitions (§31), feedback_loop_projection (§21)
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]] — RLS, RBAC, PII masking, tenant isolation
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]] — agent eval integration, feedback como eval signal
- [[14_PROJECT_DASHBOARD_ARCHITECTURE]] — Feedback Loop widget, projeções de feedback
- [[15_COMMAND_CENTER_ARCHITECTURE]] — família #9 Feedback & Support; intents de feedback
- [[16_NODE_CANVAS_ARCHITECTURE]] — feedback_node, feedback_decision_node, feedback_gap_node; edge types
- [[20_QA_AND_FOUNDER_APPROVAL_PROTOCOL]] — QA gera feedback; feedback critical bloqueia gates
- [[21_ROI_ARCHITECTURE]] — feedback_roi_link; RoiContradicted; confidence update pipeline
- [[23_SUPPORT_SYSTEM_ARCHITECTURE]] — feedback → support ticket routing; support → feedback signal
- [[24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE]] — feedback de cobrança → routing especial
- [[ARCHITECTURE_PATCH_REPORT]] — patches P22-1 a P22-6; gate status de Business Systems
