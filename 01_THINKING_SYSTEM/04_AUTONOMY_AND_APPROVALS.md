---
title: Autonomy and Approvals
file: 04_AUTONOMY_AND_APPROVALS.md
phase: 01_THINKING_SYSTEM
category: autonomy
version: 1.1.0
status: active
owner: Metacognik
responsible_agent: Metacognik
reviewers:
  - PMO_CKOS
approval_required:
  - founder
purpose: Definir quando o CKOS pode sugerir, criar, executar, automatizar ou bloquear ações — AI First real sem abrir mão de controle, segurança e governança.
inputs: Intenção; agente responsável; tipo de ação; risco; custo; reversibilidade; impacto externo; sensibilidade de dados; confiança; histórico; política do workspace.
outputs: Nível de autonomia; approval required ou não; bloqueio; pedido de revisão; execução automática; run log; approval record; rollback plan.
framework: 7 níveis de autonomia (0-6) + approval gates + matriz de risco + decisão por critérios.
edge_cases: Auto-approval com efeito ruim; stakeholder aprovou sem entender; muitos approvals; agente tenta contornar.
integrations: Approval Gate de runtime em 10; políticas por risco em 12_SECURITY; assinatura/pagamentos/CRM/deploy.
prompts: Classificação de autonomia; pedido de aprovação executivo.
metrics: Approval sem retrabalho; tempo médio de aprovação; incidentes; auto-approval segura; custo evitado.
related_notes:
  - 03_AGENT_OPERATING_MODEL.md
  - 05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../05_IMPLEMENTATION_SYSTEM/20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md
tags: [thinking, autonomy, approvals, risk, rollback]
---

# 1. Propósito

Definir quando o CKOS pode sugerir, criar, executar, automatizar ou bloquear ações, permitindo AI First real sem abrir mão de controle, segurança, confiança e governança.

# 2. Função dentro do CKOS

Define níveis de autonomia, approval gates, auto-approval policies, decisões críticas, ações reversíveis, riscos, escalonamento, rollback e responsabilidade humana. A **aplicação em runtime** (onde o workflow pausa) está em `10_SYSTEM_RUNTIME_ARCHITECTURE §Approval Gate`; as **políticas por risco/permissão** em `12_SECURITY`.

# 3. Inputs

Intenção; agente responsável; tipo de ação; risco; custo; reversibilidade; impacto externo; sensibilidade de dados; confiança; histórico do projeto; política do workspace.

# 4. Outputs

Nível de autonomia; approval required ou não; bloqueio; pedido de revisão; execução automática; run log; approval record; rollback plan.

# 5. Framework operacional

## 5.1 Níveis de autonomia

```txt
Nível 0 — Observar:        registra e organiza informação.
Nível 1 — Sugerir:         recomenda, não cria objeto operacional.
Nível 2 — Criar rascunho:  cria draft.
Nível 3 — Criar + aprovar: prepara objeto e bloqueia até aprovação.
Nível 4 — Executar reversível: ações de baixo risco com log e rollback.
Nível 5 — Autonomia supervisionada: executa dentro de políticas aprovadas.
Nível 6 — Autonomia estratégica restrita: somente com política explícita do Founder.
```

## 5.2 Approval gates obrigatórios

Aprovação humana obrigatória para: envio de proposta a cliente; alteração de preço; alteração de contrato; publicação externa; contratação de ferramenta paga; compra de mídia; mudança de escopo; exclusão de dados; acesso a dados sensíveis; automação que impacte cliente; ativação de agente com custo relevante; mudança estrutural do produto; deploy em produção.

## 5.3 Auto-approval permitido

Para: criar draft; atualizar status interno; criar node sugerido; rodar diagnóstico interno; organizar arquivos; gerar resumo; registrar memória; criar tarefa de baixa prioridade; rodar QA não destrutivo; preparar prompt de implementação; abrir issue interna.

## 5.4 Matriz de risco

```txt
Baixo:  interno, reversível, sem custo, sem impacto externo
Médio:  afeta roadmap, consome crédito, altera prioridade ou expõe output a stakeholder interno
Alto:   afeta cliente, orçamento, contrato, publicação, dados sensíveis ou produção
```

## 5.5 Decisão por critérios

```txt
impacto externo = true        → approval required
custo > limite aprovado       → approval required
dados sensíveis = true        → approval required
reversível = false            → approval required
confiança < threshold         → Metacognik review (threshold definido em 13_EVALS)
risco alto                    → Founder approval
```

## 5.6 Approval object

```yaml
approval_id:
project_id:
requested_by:
requested_for:
object_type:
object_id:
action:
risk_level:
cost_estimate:
reversible:
evidence:
recommendation:
expires_at:
approver:
status:
decision_note:
```

## 5.7 Estados de aprovação

```txt
not_required · draft · requested · approved · rejected · changes_requested · expired · auto_approved · revoked
```

## 5.8 Escalonamento

```txt
Nick resume impacto → PMO_CKOS sugere opção segura → Metacognik aponta risco de não decidir → Founder/stakeholder decide
```

# 6. Agente responsável

`Metacognik` decide risco e necessidade de approval.

# 7. Superagentes envolvidos

Nick (solicita ao usuário); PMO_CKOS (organiza decisões); Cognik (contexto/evidências); QA Lead (risco técnico); Founder (decisões críticas).

# 8. Skills necessárias

risk-classification; approval-routing; auto-approval-policy; rollback-planning; decision-logging; confidence-scoring; stakeholder-routing.

# 9. Prompts relacionados

```txt
Classifique esta ação em nível de autonomia 0-6. Explique risco, reversibilidade, custo, impacto externo, confiança e se exige aprovação.
```

```txt
Resuma em linguagem executiva o que será aprovado, por que importa, riscos, alternativas e consequência de não aprovar.
```

# 10. Integrações

Assinatura eletrônica; pagamentos; CRM; Git/deploy; APIs de publicação; WhatsApp/email; calendário; plataformas de mídia; logs internos; Supabase approval table (schema em `11_DATA_MODEL`). Permissões por risco em `12_SECURITY`.

# 11. Memória e contexto

Toda aprovação vira memória longa: quem aprovou, quando, contexto, evidências, risco, consequência, objeto aprovado, versão.

# 12. Edge cases

- **Auto-approval gerou efeito ruim** → rollback imediato, incidente, redução de autonomia.
- **Stakeholder aprovou sem entender** → Nick oferece resumo e confirma entendimento para decisões críticas.
- **Muitos approvals travando** → política de auto-approval para baixo risco.
- **Agente tenta contornar approval** → bloqueio, log de incidente, revisão do Agent Operating Model (e da permissão em 12).

# 13. Métricas de sucesso

Approval sem retrabalho; tempo médio de aprovação; nº de incidentes; auto-approval segura; custo evitado por gate; decisões críticas com evidência; redução de bloqueios desnecessários.

# 14. Critérios de aprovação

Aprovado se define níveis claros, protege decisões críticas, permite automação segura, registra approvals, prevê rollback e reduz carga do Founder sem removê-lo.

# 15. Critérios de reprovação

Reprovado se bloquear tudo, liberar tudo, não diferenciar risco, não prever custo, não registrar decisão ou não tratar dados sensíveis.

# 16. Related notes

- [[03_AGENT_OPERATING_MODEL]]
- [[05_MEMORY_AND_CONTEXT_ARCHITECTURE]]
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]]
- [[20_QA_AND_FOUNDER_APPROVAL_PROTOCOL]]
