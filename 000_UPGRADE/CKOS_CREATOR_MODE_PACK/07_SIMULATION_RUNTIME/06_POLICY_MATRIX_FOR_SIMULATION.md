---
title: Policy Matrix For Simulation
system_id: policy_matrix_for_simulation
category: creator_mode_simulation_runtime
status: active
version: 1.0.0
owner: pmo_ckos
reviewers:
  - founder
  - ceo_agent
  - metacognik
created_for: CKOS_CREATOR_MODE_PACK
created_at: 2026-05-26
---

# Policy Matrix For Simulation

## Proposito

Ligar acoes simuladas a policies, approvals, riscos e bloqueios.

Esta matriz deve ser usada pelo CEO Agent e PMO Auditor antes de qualquer projeto sair de intencao para artefato.

## Matriz principal

| Acao simulada | Policy | Approval | PMO | Risco | Bloquear se |
|---|---|---|---|---|---|
| Interpretar intencao | `POLICY_PLANNER_FIRST` | nao | nao | baixo | CEO tentar executar direto |
| Ler memoria local | `POLICY_LOCAL_READ_ONLY` | nao | nao | baixo | leitura pedir move/delete |
| Montar Context Pack | `POLICY_CONTEXT_PACK_REQUIRED` | nao | se risco medio+ | baixo/medio | faltarem fontes essenciais |
| Propor projeto | `POLICY_FOUNDER_APPROVAL_BEFORE_EXECUTION` | sim | se novo projeto | medio | Founder nao aprovar |
| Propor filetree | `POLICY_FILETREE_APPROVAL_REQUIRED` | sim | sim | medio | pack for criado antes |
| Criar analysis doc | `POLICY_ANALYSIS_DOC_ALLOWED` | sim se novo arquivo | se risco medio+ | baixo/medio | estrategia final embutida |
| Criar pack de notas | `POLICY_PACK_AFTER_FILETREE_APPROVAL` | sim | sim | medio | filetree nao aprovada |
| Deep research externo | `POLICY_DEEP_RESEARCH_COST_APPROVAL` | sim | sim | alto | custo sem approval |
| Usar conector OAuth | `POLICY_OAUTH_APPROVAL_REQUIRED` | sim | sim | alto | credencial/token envolvido |
| Usar fonte regulada | `POLICY_HUMAN_REVIEW_FOR_REGULATED_DOMAIN` | sim | sim | alto | sem revisor humano |
| Benchmark social publico | `POLICY_PLATFORM_TERMS_REVIEW_REQUIRED` | sim | sim | alto | scraping privado |
| Simular creditos | `POLICY_COST_VISIBILITY_REQUIRED` | depende gate | se 16+ CKC | medio | sem faixa de custo |
| Simular n8n | `POLICY_N8N_ACCELERATOR_NOT_CORE` | sim | sim | medio/alto | virar core runtime |
| Importar output Manus | `POLICY_MANUS_NOT_INFRASTRUCTURE` | sim | sim | alto | virar source runtime |
| Gerar artifact final | `POLICY_DELIVERY_AUDIT_REQUIRED` | sim | sim | medio/alto | sem audit trail |

## Policies base

### POLICY_PLANNER_FIRST

CEO deve interpretar antes de executar.

Bloqueia:

- criacao direta de pasta;
- criacao direta de estrategia final;
- inicio de implementacao.

### POLICY_CONTEXT_PACK_REQUIRED

Todo projeto precisa declarar contexto antes de artifacts.

Bloqueia:

- plano sem documentos lidos;
- fonte externa sem source mode;
- conclusao sem evidence map quando houver pesquisa.

### POLICY_COST_VISIBILITY_REQUIRED

Toda acao com custo cognitivo, externo ou documental deve declarar faixa CKC.

Bloqueia:

- deep research sem custo;
- PMO ignorado em custo medio/alto;
- conector externo sem custo.

### POLICY_FOUNDER_APPROVAL_BEFORE_EXECUTION

Founder aprova antes de criar ou alterar packs relevantes.

Bloqueia:

- filetree oficial sem aprovacao;
- pack de notas sem aprovacao;
- estrategia final sem aprovacao.

### POLICY_CHECKOUT_LOCK_REQUIRED

Toda edicao documental relevante exige checkout lock/release.

Bloqueia:

- multiplos chats editando mesma pasta sem escopo;
- alteracao fora de files_allowed;
- ausencia de release.

### POLICY_CANONICAL_DOC_PROTECTION

Docs canonicos nao podem ser alterados por simulacao.

Bloqueia:

- criar docs 25-30;
- recriar docs 21-24;
- renumerar conflito de docs 21;
- alterar arquitetura sem patch plan.

### POLICY_NO_IMPLEMENTATION_IN_DOCUMENTAL_PHASE

CKOS esta em fase documental.

Bloqueia:

- UI;
- backend;
- migrations;
- APIs reais;
- agentes runtime;
- automacoes runtime.

### POLICY_N8N_ACCELERATOR_NOT_CORE

n8n pode ser prototipo, backoffice ou automacao auxiliar.

Bloqueia:

- n8n como core runtime;
- n8n gerindo credito/pagamento;
- n8n como fonte definitiva para dados sensiveis.

### POLICY_MANUS_NOT_INFRASTRUCTURE

Manus pode ser apoio temporario/manual, nunca infraestrutura definitiva.

Bloqueia:

- Manus como source runtime;
- Manus como event store;
- Manus substituindo Research Capability.

## Gate de decisao

```txt
baixo risco + baixo custo:
  CEO pode propor proxima acao, Founder aprova se criar arquivo.

medio risco ou 6-15 CKC:
  Founder confirma antes de executar.

alto risco ou 16+ CKC:
  PMO audit obrigatorio + Founder approval.

dominio regulado:
  PMO audit obrigatorio sempre.
```

