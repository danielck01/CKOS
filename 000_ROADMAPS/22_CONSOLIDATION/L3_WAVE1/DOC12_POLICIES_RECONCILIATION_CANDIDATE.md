---
title: Doc 12 Policies Reconciliation Candidate
file: DOC12_POLICIES_RECONCILIATION_CANDIDATE.md
layer: auxiliary
doc_type: pmo_patch_candidate
phase: 000_ROADMAPS
category: consolidation
status: awaiting_founder_batch_approval
version: 0.1.0
created_at: 2026-06-04
owner: pmo_ckos
responsible_agent: windsurf
session_id: S-P1-L3-WINDSURF-20260604-001
companion_of: 00_WAVE1_DISPATCH_AND_PROTOCOL.md
target_canonical:
  - 03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - 01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md
inventory_source: 000_UPGRADE/07_POLICIES/ (11 arq) lidos @ 2026-06-04
reviewers:
  - founder
  - metacognik
approval_required:
  - founder
non_authority_boundary: >
  Patch candidate. PROPÕE, não aplica. Não edita Doc 12 nem Doc 04 nem qualquer canônico 01-28.
  Não move/arquiva/deleta o UPGRADE/07. Tocar o Doc 12 ou Doc 04 é P1 e exige sessão canonical_patch
  separada com aprovação Founder + Metacognik. As policies listadas aqui são CANDIDATAS de catálogo,
  não políticas ativas.
tags: [consolidation, policies, doc12, doc04, patch-candidate, reconciliation, pmo, windsurf]
---

# Doc 12 — Reconciliação de Policies (Patch Candidate)

> **L3 da consolidação (D4 = promoção agressiva).** Compara o sistema de policies paralelo
> — `000_UPGRADE/07_POLICIES/` (11 arq) — contra os canônicos `Doc 12` (Security/Permissions/Data Governance)
> e `Doc 04` (Autonomy and Approvals), e propõe o que promover.
> **Modo:** `patch_candidate`. Nada é aplicado no Doc 12 ou Doc 04 por este texto.
> **⚠️ BAIXA CONFIANÇA (modelo grátis):** todo output aqui é hipótese. Julgamento final = fan-in (Claude#2).

---

## 0. Veredito em uma linha (PMO, direto)

**A `UPGRADE/07` é um scaffold gerado por template, raso. Os canônicos Doc 12 e Doc 04 são muito mais ricos.**
O valor real a promover é **quase zero** — os 11 arquivos são boilerplate idêntico com apenas 1 linha de "Definição" variando.
Todas as policies conceituais já estão cobertas em Doc 12 (security/permissões/data governance/RLS/secrets) ou Doc 04 (autonomy levels, approval, batches).
O único valor potencial seria **nomes de policy** para um catálogo futuro, mas mesmo isso é questionável dado que o conteúdo é template puro.
Esta sessão **não recomenda promoção de conteúdo** — apenas expõe o mapeamento e conflitos de camada para o fan-in revisar.

⚠️ **Alerta de constituição:** o Doc 12 é um documento de 682 linhas com especificação detalhada de deny-by-default, RBAC+ABAC, RLS, agent permissions, tool permissions, collector/actor/provider separation, model privacy, approval policies, decision rights, PII classification, secrets management, audit trail e whitelabel isolation. A `UPGRADE/07` é 11 arquivos de 20 linhas cada com boilerplate genérico. Promover qualquer conteúdo da UPGRADE seria **downgrade** do canônico.

---

## 1. Método

- Lidos: README + 11 arquivos de policies (agent, approval, connector, cost, data_privacy, execution, learning, quality, roi, source).
- Confirmada **uniformidade total**: os arquivos são o **mesmo template** com apenas a linha "Definição" trocada.
- Sinal real por arquivo = **(nome) + (definição de 1 linha)**. Todo o resto (Regras base, Checklist) é boilerplate idêntico entre instâncias.
- Comparação contra Doc 12 (682 linhas, 21 seções) e Doc 04 (175 linhas, 16 seções).
- Verificação cruzada com F1_RUNTIME_IO reconciliation candidate para policies já mencionadas lá (autonomy 1-5, budget gates, memory validation).

### 1.1 Prova da uniformidade (por que o conteúdo não promove)

| Arquivo | O que varia entre instâncias | O que é idêntico |
|---|---|---|
| Todos os 11 policies | só a linha **Definição** (1 linha) | "Regras base" (6 linhas idênticas), "Checklist" (6 linhas idênticas) |

> Os 11 arquivos são literamente o mesmo template com o título e a definição trocados. Não há regra real (condição→ação→enforcement) em nenhum deles — apenas boilerplate genérico que poderia se aplicar a qualquer policy.

**Exemplo de identidade (diff visual):**

```txt
agent_policy.md:     "Regras base: Aplicar antes de execução. Registrar decisão. Sinalizar risco. Solicitar aprovação se necessário. Alimentar aprendizado após conclusão."
approval_policy.md:  "Regras base: Aplicar antes de execução. Registrar decisão. Sinalizar risco. Solicitar aprovação se necessário. Alimentar aprendizado após conclusão."
connector_policy.md:  "Regras base: Aplicar antes de execução. Registrar decisão. Sinalizar risco. Solicitar aprovação se necessário. Alimentar aprendizado após conclusão."
[... idêntico em todos os 11 arquivos]
```

---

## 2. Inventário comparativo

### 2.1 Mapeamento para Doc 12 (Security/Permissions/Data Governance)

| UPGRADE/07 policy | Definição (1 linha) | Seção Doc 12 correspondente | Veredito |
|---|---|---|---|
| agent_policy | Define permissões por agente. | §5.7 "Agent permissions and capability scoping" | ✅ **JÁ COBERTO** |
| approval_policy | Define quando exigir aprovação humana. | §5.12 "Approval policies e approvalPolicyRegistry" | ✅ **JÁ COBERTO** |
| connector_policy | Define regras de uso de conectores. | §5.9 "Collector / Provider / Actor permissions" | ✅ **JÁ COBERTO** (connectors = collectors) |
| data_privacy_policy | Protege dados sensíveis e confidenciais. | §5.14 "PII e classificação de dados" | ✅ **JÁ COBERTO** |

### 2.2 Mapeamento para Doc 04 (Autonomy and Approvals)

| UPGRADE/07 policy | Definição (1 linha) | Seção Doc 04 correspondente | Veredito |
|---|---|---|---|
| execution_policy | Define quando executar, criar tarefa, agendar ou pedir confirmação. | §5.1-5.5 (autonomy levels, approval gates, risk matrix) | ✅ **JÁ COBERTO** |
| approval_policy | Define quando exigir aprovação humana. | §5.2 "Approval gates obrigatórios" | ✅ **JÁ COBERTO** (também em Doc 12) |

### 2.3 Policies não em Doc 12 nem Doc 04 (outros canônicos ou net-new)

| UPGRADE/07 policy | Definição (1 linha) | Casa canônica potencial | Veredito |
|---|---|---|---|
| cost_policy | Controla custo por modelo, agente, ferramenta, run e projeto. | Doc 13 (Evals, Observability, Cost Control) | ⚠️ **Provavelmente coberto em Doc 13** |
| learning_policy | Define como feedback vira memória e melhoria. | Doc 05 (Memory and Context Architecture) | ⚠️ **Provavelmente coberto em Doc 05** |
| quality_policy | Define padrões mínimos de output. | Doc 20 (QA and Founder Approval Protocol) | ⚠️ **Provavelmente coberto em Doc 20** |
| roi_policy | Define como medir valor e retorno. | Doc 21 (ROI Engine) ou Doc 24 (Budget Gates) | ⚠️ **Provavelmente coberto em Doc 21/24** |
| source_policy | Define exigência de fontes, citações e validação. | Doc 18 (Evidence) ou Doc 28 (Study Layer) | ⚠️ **Provavelmente coberto em Doc 18/28** |

> **Nota:** As 5 policies acima não foram verificadas contra seus canônicos potenciais (Doc 05, 13, 18, 20, 21, 24, 28) pois estão fora do escopo desta sessão (só Doc 12 + Doc 04). O fan-in deve decidir se requer verificação adicional.

### 2.4 Verificação contra F1_RUNTIME_IO (já mencionadas como cobertas)

| Policy F1_RUNTIME_IO | Menção no F1 candidate | Casa canônica |
|---|---|---|
| autonomy levels 1-5 | "Policies (autonomy 1-5, budget, approval) → Doc 04 + Doc 12 ✅ JÁ COBERTO" | Doc 04 §5.1 |
| budget gates | "Policies (autonomy 1-5, budget, approval) → Doc 04 + Doc 12 ✅ JÁ COBERTO" | Doc 24 (Budget Gates) |
| memory validation | "Memory taxonomy (project/agent/visual/ROI…) → Doc 05 §5.1–5.2 já tem camadas + tipos + memory object ✅ JÁ COBERTO" | Doc 05 |

---

## 3. A PROMOVER

> Sob D4 (agressivo), mas respeitando a qualidade do canônico. Promoção = entra no patch candidate p/ Doc 12 ou Doc 04;
> **aplicação é sessão separada.**

### 3.1 Estrutural (valor real — NENHUM)

| ID | Item a promover | Por que é melhor que o canônico | Seção-alvo | Força |
|---|---|---|---|---|
| — | **NENHUM** | O canônico Doc 12 (682 linhas) e Doc 04 (175 linhas) são muito mais ricos que o boilerplate da UPGRADE/07 | — | — |

### 3.2 Catálogo — nomes de policy (candidatos, NÃO conteúdo)

> Entram **apenas** como nomes de policy para um catálogo futuro. Cada um carrega só a definição de 1 linha como hipótese.
> **Não** promover o conteúdo de "Regras base" nem "Checklist" — é boilerplate idêntico e genérico.

| ID | Candidato | Definição-hipótese | Casa canônica principal | Seção-alvo | Força |
|---|---|---|---|---|---|
| PROMOTE-P1 | cost_policy | Controla custo por modelo, agente, ferramenta, run e projeto. | Doc 13 (não verificado nesta sessão) | catálogo de policies (future) | **BAIXA** |
| PROMOTE-P2 | learning_policy | Define como feedback vira memória e melhoria. | Doc 05 (não verificado nesta sessão) | catálogo de policies (future) | **BAIXA** |
| PROMOTE-P3 | quality_policy | Define padrões mínimos de output. | Doc 20 (não verificado nesta sessão) | catálogo de policies (future) | **BAIXA** |
| PROMOTE-P4 | roi_policy | Define como medir valor e retorno. | Doc 21/24 (não verificado nesta sessão) | catálogo de policies (future) | **BAIXA** |
| PROMOTE-P5 | source_policy | Define exigência de fontes, citações e validação. | Doc 18/28 (não verificado nesta sessão) | catálogo de policies (future) | **BAIXA** |

**Total a promover:** 0 estruturais + 5 candidatos de catálogo (nomes apenas, força BAIXA). **Nenhum conteúdo de regras/checklist** — é boilerplate.

> **Recomendação do Windsurf (baixa confiança):** Dado que o conteúdo é boilerplate puro e os canônicos são muito mais ricos, **não recomendaria promoção nem mesmo dos nomes** a menos que o fan-in identifique um gap real nos canônicos Doc 05/13/18/20/21/24/28. Os nomes são genéricos demais para terem valor de catálogo sem conteúdo real.

---

## 4. JÁ COBERTO (arquivar, sem ação no canônico)

- **agent_policy:** Doc 12 §5.7 "Agent permissions and capability scoping" — especificação detalhada de RBAC+ABAC, forbidden actions, data access scope, anti-self-escalation, tenant scope.
- **approval_policy:** Doc 12 §5.12 "Approval policies e approvalPolicyRegistry" + Doc 04 §5.2 "Approval gates obrigatórios" — especificação detalhada de approval gates, timeout, escalonamento, emergency bypass.
- **connector_policy:** Doc 12 §5.9 "Collector / Provider / Actor permissions" — especificação detalhada de collector/actor/provider separation, tool_router deny-by-default, vault isolation.
- **data_privacy_policy:** Doc 12 §5.14 "PII e classificação de dados" — especificação detalhada de classificação (public/internal/confidential/PII/sensitive), regras operacionais, RAG com PII, retenção.
- **execution_policy:** Doc 04 §5.1-5.5 — especificação detalhada de 7 níveis de autonomia (0-6), approval gates obrigatórios, auto-approval permitido, matriz de risco, decisão por critérios.
- **Todo o conteúdo de "Regras base" e "Checklist":** valor de promoção zero (templates idênticos genéricos).

---

## 5. CONFLITOS → ARCHITECTURE_QUESTIONS (não decidir aqui)

| ID | Conflito | Pergunta para Founder + Metacognik |
|---|---|---|
| **AQ-P12-1** | **Conflito de camada: policy de runtime/segurança vs policy cognitiva/comportamento.** agent_policy, connector_policy, data_privacy_policy são claramente Doc 12 (security/runtime). execution_policy é claramente Doc 04 (cognitivo/comportamental). Mas onde moram cost_policy, learning_policy, quality_policy, roi_policy, source_policy? | Qual é a fronteira entre "policy de security/runtime" (Doc 12) e "policy de comportamento/cognição" (Doc 04)? As 5 policies não verificadas (cost/learning/quality/roi/source) pertencem a Doc 12, Doc 04, ou a outros canônicos (05/13/18/20/21/24/28)? |
| **AQ-P12-2** | **Duplicação de approval_policy.** A UPGRADE/07 tem approval_policy, mas o conceito está em ambos Doc 12 (approvalPolicyRegistry, runtime enforcement) e Doc 04 (autonomy levels, approval gates). | approval_policy é um conceito de security (Doc 12) ou de cognição/comportamento (Doc 04)? Ou é um conceito híbrido que precisa de cross-ref entre os dois? |
| **AQ-P12-3** | **Valor de catálogo de nomes sem conteúdo.** As 5 policies não verificadas (cost/learning/quality/roi/source) têm apenas 1 linha de definição. | Tem valor criar um catálogo de policies com apenas nomes e definições de 1 linha? Ou o catálogo só faz sentido quando cada policy tem regras reais (condição→ação→enforcement)? |
| **AQ-P12-4** | **Boilerplate genérico vs especificação canônica.** A UPGRADE/07 usa "Regras base" e "Checklist" genéricos que se aplicam a qualquer policy. Doc 12 e Doc 04 têm especificações detalhadas e específicas por tipo de policy. | O boilerplate genérico da UPGRADE/07 tem algum valor como "template de policy" para policies futuras? Ou é apenas ruído que deve ser descartado? |

> Estas 4 AQs são o **produto mais valioso** desta sessão. Não são resolvidas por promoção — são decisão de arquitetura e taxonomia.

---

## 6. Plano de arquivamento do UPGRADE/07

**Sequência obrigatória (não inverter):**

1. Founder aprova este candidate (gate).
2. Se houver promoção aprovada (PROMOTE-P1..P5), sessão `canonical_patch` separada aplica no canônico apropriado (Doc 12, Doc 04, ou outro) com aprovação Founder + Metacognik.
3. **Só então** arquivar: `git mv 000_UPGRADE/07_POLICIES/` → `99_ARCHIVE/000_UPGRADE/07_POLICIES/` + README-pointer no lugar antigo.

- **Nunca deletar.** `99_ARCHIVE` é recuperável (git rollback). Preserva proveniência do sistema de policies paralelo.
- **Por que arquivar e não manter:** é scaffold raso de boilerplate; todo o valor durável (mapeamento + as 4 AQs) fica capturado neste candidate. Manter o bruto = manter o "2º canônico paralelo" que a consolidação existe para colapsar.
- **Mecanismo validado:** `git mv` preserva `[[wikilinks]]` (links por nome); commit por lote = reversível.

---

## 7. Risco P1 + nota de aplicação

- **P1:** Doc 12 e Doc 04 são core do Thinking System e Runtime System (`approval_required: founder`). Doc 12 tem 682 linhas de especificação detalhada. Doc 04 tem 175 linhas. Mexer em qualquer um é alto impacto — irradia para Docs 02, 03, 05, 10, 11. **Este texto não aplica nada.**
- **Aplicação:** se houver promoção aprovada, sessão `canonical_patch` separada, com Founder + Metacognik, escopo = só o canônico alvo + maps/patch report.
- **Guarda anti-bloat (Metacognik):** sob D4 a tentação é despejar os 11 nomes no catálogo. Recusado. Só 5 candidatos entram (P1-P5), e **como nomes apenas com definição de 1 linha**. Promover o boilerplate seria introduzir ruído genérico em canônicos ricos.
- **Dependência de verificação adicional:** as 5 policies não verificadas (cost/learning/quality/roi/source) precisam de verificação contra Docs 05/13/18/20/21/24/28 antes de qualquer decisão de promoção. Esta sessão não fez essa verificação (escopo = Doc 12 + Doc 04 apenas).

---

## 8. Resumo para o checkout

- **A promover:** 0 estruturais + 5 candidatos de catálogo (cost/learning/quality/roi/source) — força BAIXA, conteúdo não verificado.
- **Já coberto / arquivar:** 6 policies (agent/approval/connector/data_privacy/execution/approval duplicado) + todo o boilerplate.
- **Conflitos:** 4 ARCHITECTURE_QUESTIONS (AQ-P12-1..4) — o entregável central.
- **Próximo passo:** fan-in (Claude#2 Auditor) faz o julgamento final + consolida com TR-SKILLS + TR-TRANSF → Founder decide se há promoção ou apenas arquivamento.
