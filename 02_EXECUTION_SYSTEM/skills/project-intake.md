---
title: project-intake
file: project-intake.md
phase: 02_EXECUTION_SYSTEM
category: skill_note
status: active_draft
skill_id: project-intake
skill_family: operations
owner_agent: PMO_CKOS
review_agent: Metacognik
runtime_authority: false
implementation_authorized: false
source_skill: C:/Users/GustavoBxx/.codex/skills/project-intake/SKILL.md
---

# project-intake

Cria uma semente de projeto CKOS a partir de intencao do Founder/usuario, ideias iniciais, notas coladas ou contexto de negocio bruto.

# Quando Usar

- Pedido ainda esta em forma de ideia.
- Uma intencao precisa virar projeto governado.
- Ainda nao existe briefing, contexto, Work Order ou escopo claro.
- A conversa precisa separar objetivo, stakeholders, restricoes, riscos e ROI inicial.

# Quando Nao Usar

- Para executar trabalho tecnico diretamente.
- Para criar backend, banco, API, migrations, agentes reais, MCP, n8n ou automacoes.
- Para substituir briefing, context pack ou Work Order.

# Entradas

- raw_intent
- founder_goal
- business_context
- target_user_or_stakeholder
- constraints
- source_refs
- deadlines
- risk_tolerance
- expected_artifact_or_decision

# Workflow

1. Reescrever a intencao em uma frase precisa.
2. Identificar org, workspace, projeto candidato, stakeholders e dominio.
3. Separar fatos, assumptions, restricoes, riscos e perguntas.
4. Formular hipotese de ROI: valor, risco reduzido, tempo/custo economizado ou decisao habilitada.
5. Decidir o proximo objeto: briefing, research task, Work Order draft ou note normalization.
6. Bloquear execucao se faltar briefing/contexto para trabalho de risco.

# Saida Verificavel

Uma `CKOS Project Seed` contendo:

- intent interpretado;
- contexto do projeto;
- allowed_scope e forbidden_scope;
- riscos;
- hipotese de ROI;
- briefing needs;
- perguntas inteligentes;
- proximo objeto recomendado;
- readiness.

# Guardrails

- Canonico vence study notes.
- Study notes sao contexto, nao verdade.
- Fatos desconhecidos ficam como `unknown`.
- Nao implica aprovacao para executar.

# Proxima Skill

- [[briefing-builder]] quando a semente precisa virar briefing.
- [[context-pack-builder]] quando ja existe briefing/contexto suficiente.
- [[work-order-draft]] apenas quando escopo e evidencia estao maduros.
