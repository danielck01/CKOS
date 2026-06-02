---
title: Skills Registry
file: 06_SKILLS_REGISTRY.md
phase: 02_EXECUTION_SYSTEM
category: skills
version: 1.1.0
status: active
owner: PMO_CKOS
responsible_agent: PMO_CKOS
reviewers:
  - Metacognik
approval_required:
  - founder
  - PMO_CKOS
  - Metacognik
purpose: Registro mestre de skills — capacidades reutilizáveis, versionadas e auditáveis que transformam intenção em ação controlada. Skill não é prompt.
inputs: Object Model; Agent Operating Model; Autonomy; Memory; intenção; capabilities.
outputs: Taxonomia de skills; template de skill; skills MVP; níveis de autonomia por skill.
framework: 7 famílias de skills (Strategy, Research, Creative, Product/UX, Development, Operations, Metacognitive).
edge_cases: Skill sem output verificável; skill dependente de prompt genérico; skill sem owner; skill sem "quando não usar".
integrations: Executada por agentes via 10_RUNTIME; logada em runs; avaliada em 13_EVALS.
prompts: Cada skill referencia prompts base na 08_PROMPT_LIBRARY.
metrics: % skills com owner; % com outputs testáveis; tempo médio; retrabalho; aprovações evitadas com segurança.
related_notes:
  - 03_AGENT_OPERATING_MODEL.md
  - 04_AUTONOMY_AND_APPROVALS.md
  - 07_WORKFLOW_BLUEPRINTS.md
  - 08_PROMPT_LIBRARY.md
  - ../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
tags: [execution, skills, registry, autonomy, mvp]
---

# 1. Propósito

Definir o registro mestre de skills do CKOS. **Skill é uma capacidade modular, versionada e auditável que transforma uma intenção em uma ação controlada.** Skills impedem dependência de prompts soltos e padronizam execução, qualidade, riscos, inputs, outputs, autonomia e validação.

# 2. Função dentro do CKOS

Catálogo do que o sistema sabe fazer. Cada skill é chamável por agentes, superagents, workflows, CommandBar, nodes ou automações — e executada pelo runtime (`10`), logada como `Run` e avaliada em `13_EVALS`.

# 3. Inputs

Object Model (02); Agent Operating Model (03); Autonomy (04); Memory (05); intenção do usuário; capabilities ativas.

# 4. Outputs

Taxonomia de skills; template oficial de skill; conjunto MVP; tabela de autonomia por skill.

# 5. Framework operacional

## 5.1 Definição (o que uma skill contém)

objetivo; condições de uso; inputs; outputs; agente responsável; ferramentas permitidas; nível de autonomia; métricas; edge cases; prompts base; critérios de QA.

## 5.2 Taxonomia de skills

```txt
Strategy:    briefing-intelligence · brand-diagnosis · positioning-analysis · persona-strategy
             · stakeholder-mapping · proposal-scoping · decision-framing · product-strategy
Research:    market-research-pack · competitive-intelligence · social-intelligence · commerce-intelligence
             · reference-moodboard-research · evidence-extraction · source-validation · research-pack-generation
Creative:    visual-direction · campaign-concepting · image-prompt-engineering · video-shot-planning
             · brand-storytelling · copywriting-system
Product/UX:  ui-architecture · design-system-refinement · motion-system-design · component-specification
             · responsive-qa · accessibility-review · whitelabel-theme-adaptation
Development: frontend-implementation · backend-architecture · database-modeling · api-integration
             · rag-ingestion · memory-persistence · agent-run-logging · qa-bugfix-loop
Operations:  workflow-orchestration · task-breakdown · approval-routing · meeting-preparation
             · client-follow-up · delivery-management · risk-escalation · prompt-library-curation
Metacognitive: hypothesis-audit · confidence-scoring · gap-detection · bias-detection
             · decision-quality-review · agent-output-evaluation · rollback-assessment
```

> `product-strategy` e `prompt-library-curation` são skills (não agentes), absorvendo o que os originais chamavam de "Product Architect" e "Prompt Engineer Agent" (ver `00_TAXONOMY §5.1`).

## 5.3 Template de skill

```yaml
skill_id:
name:
category:
version:
status:
owner_agent:
review_agent:
autonomy_level:
approval_required:
allowed_tools:
required_inputs:
optional_inputs:
outputs:
trigger_events:
edge_cases:
metrics:
related_workflows:
related_transformers:
eval_ref:        # novo — golden set / rubric em 13_EVALS
```

## 5.4 Skills prioritárias para MVP

- **`briefing-intelligence`** — conversa inicial → briefing vivo. Resp.: Nick + Cognik. Review: Metacognik. Outputs: briefing vivo, lacunas, hipóteses, nodes sugeridos, perguntas adaptativas, confidence score.
- **`node-creation`** — cria nodes dinâmicos conforme necessidade. Resp.: Cognik. Review: PMO_CKOS + Metacognik. Regra crítica: nenhum node de commerce/ads/finance/social nasce como default.
- **`proposal-generation`** — diagnóstico vivo → proposta interativa. Resp.: Nick + Branddock (pendente) + PMO_CKOS. Review: Metacognik + Founder.
- **`research-pack-generation`** — curadoria governada de referências de pesquisa (visual, sistêmica, estratégica, de mercado). Internaliza o que Manus fazia no bootstrap. Resp.: Research Subagent. Review: Datta + Metacognik.

  **Scoring obrigatório de referências** (toda referência recebe pontuação antes de entrar no pack):

  | Critério | Peso |
  |---|---:|
  | Aplicabilidade real ao CKOS | 25 |
  | Transferibilidade técnica | 20 |
  | Valor estratégico | 20 |
  | Originalidade sem gimmick | 10 |
  | Viabilidade de performance | 10 |
  | Clareza de uso | 10 |
  | Direitos / link / autoria | 5 |

  **Regra de aplicação:** toda referência deve responder — o que observar? o que não copiar? como traduzir para CKOS? qual componente nasce disso? qual risco de interpretação? Referência sem resposta a essas perguntas é reprovada.

  **Regra de qualidade de CSV:** `references_master.csv` deve ter campos com vírgula entre aspas para não desalinhar colunas no parser. Shortlist sempre validada contra o CSV limpo antes da entrega. (Lição de auditoria — ver histórico `MANUS_RESEARCH_FIX_REPORT.md` se disponível.)
- **`implementation-brief`** — estratégia → instrução para executor técnico. Resp.: PMO_CKOS. Review: QA Lead. Executores: Claude Code, Codex, Antigravity, Builder Subagents.
- **`qa-gate`** — valida entrega antes de aprovação/deploy. Resp.: QA Lead. Review: Metacognik.

## 5.5 Níveis de autonomia por skill

| Skill | Autonomia inicial | Pode automatizar depois? | Aprovação obrigatória |
|---|---:|---|---|
| briefing-intelligence | 2 | Sim | Humano aprova briefing final |
| node-creation | 2 | Sim (nodes baixo risco) | Nodes com custo/dados sensíveis |
| proposal-generation | 1 | Parcial | Founder/cliente |
| research-pack-generation | 3 | Sim | Uso externo/licenças |
| implementation-brief | 2 | Sim | Founder ou PMO_CKOS |
| frontend-implementation | 1 | Parcial | QA Lead + Founder para produção |
| qa-gate | 3 | Sim | Metacognik em alto risco |

# 6. Agente responsável

`PMO_CKOS` mantém o registry; cada skill tem owner próprio.

# 7. Superagentes envolvidos

Nick; Cognik; Metacognik; PMO_CKOS; Builder Lead; QA Lead; Datta.

# 8. Skills necessárias

Meta: `skill-registration`, `skill-versioning`, `skill-deprecation`, `agent-output-evaluation`.

# 9. Prompts relacionados

Cada skill aponta para prompts base em `08_PROMPT_LIBRARY.md`. Nenhum prompt vive solto fora do registry.

# 10. Integrações

Runtime (10) executa; runs logados (11); evals (13); tools conforme `allowed_tools`.

# 11. Memória e contexto

Cada execução de skill alimenta memória conforme `05`. Aprendizados de skill (o que funciona/falha) viram memória longa.

# 12. Edge cases

Skill sem output verificável; skill dependente de prompt genérico; skill sem owner; skill sem "quando não usar"; skill sem risco definido; skill sem conexão a workflow; skill que não registra aprendizado → todas reprovadas.

# 13. Métricas de sucesso

% de skills com owner claro; % com outputs testáveis; tempo médio de execução; taxa de retrabalho; nº de edge cases capturados; aprovações humanas evitadas com segurança; erros causados por prompt solto fora do registry (meta: 0).

# 14. Critérios de aprovação

Skill aprovada se tem output verificável, owner, "quando não usar", risco definido, conexão a workflow, prompts base e eval_ref.

# 15. Critérios de reprovação

Reprovada se: sem output verificável; depende de prompt genérico; sem owner; sem "quando não usar"; sem risco; sem workflow; sem registro de aprendizado.

# 16. Related notes

- [[03_AGENT_OPERATING_MODEL]]
- [[04_AUTONOMY_AND_APPROVALS]]
- [[07_WORKFLOW_BLUEPRINTS]]
- [[08_PROMPT_LIBRARY]]
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]]
