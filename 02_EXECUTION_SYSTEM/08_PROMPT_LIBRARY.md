---
title: Prompt Library
file: 08_PROMPT_LIBRARY.md
phase: 02_EXECUTION_SYSTEM
category: prompt_library
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
purpose: Organizar prompts, instruções e comandos reutilizáveis conectados a skills, workflows, agentes, outputs e critérios de aprovação. Prompt não é skill.
inputs: Skills Registry; Workflow Blueprints; protocolos de execução.
outputs: Tipos de prompts; template de prompt; prompts base prioritários; instruções proibidas.
framework: System Instructions · Task Prompts · Executor Prompts · QA Prompts · Metacognitive Prompts.
edge_cases: Prompt sem skill associada; prompt sem critério de aprovação; instrução estética como especificação.
integrations: Curadoria via skill prompt-library-curation; executores externos (Manus/Claude/Codex/Antigravity).
prompts: Este documento é a própria biblioteca.
metrics: Prompts reutilizados; outputs aprovados sem retrabalho; prompts conectados a skills; execuções sem critérios (meta 0).
related_notes:
  - 06_SKILLS_REGISTRY.md
  - 07_WORKFLOW_BLUEPRINTS.md
  - ../05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md
tags: [execution, prompts, library, executors, qa]
---

# 1. Propósito

Organizar prompts, instruções e comandos reutilizáveis para desenvolvimento, pesquisa, QA, design, implementação e operação. **A Prompt Library não é depósito de frases bonitas**: todo prompt conecta-se a uma skill, workflow, agente, output e critério de aprovação.

# 2. Função dentro do CKOS

Ativo executável da fase de execução. Owner documental `PMO_CKOS`; curadoria contínua pela skill `prompt-library-curation` (substitui o antigo "Prompt Engineer Agent", que não é agente — `00_TAXONOMY §5.1`).

# 3. Inputs

Skills Registry (06); Workflow Blueprints (07); protocolos de implementação (17/19).

# 4. Outputs

Tipos de prompts; template; prompts base prioritários; instruções proibidas.

# 5. Framework operacional

## 5.1 Tipos de prompts

- **System Instructions**: comportamento de agentes permanentes (Nick, Cognik, Metacognik, PMO_CKOS, QA Lead).
- **Task Prompts**: tarefas específicas (criar README, investigar mercado, gerar seção, revisar código).
- **Executor Prompts** (por tool): Manus (pesquisa/benchmark/packs/docs); Claude Code (implementação, refatoração, UI, React, CSS, rotas); Codex (código, scripts, backend, migrações, testes); Antigravity (UI/UX, protótipos, animações, validação visual); Builder Subagents futuros (execução integrada com memória e approvals).
- **QA Prompts**: revisar outputs, detectar erros, comparar com critérios, gerar relatórios.
- **Metacognitive Prompts**: questionar raciocínio, detectar lacunas, vieses, overengineering, falta de evidência.

## 5.2 Template de prompt

```yaml
prompt_id:
name:
type:
related_skill:
related_workflow:
executor:
owner_agent:
review_agent:
required_inputs:
expected_outputs:
approval_required:
risk_level:
```

```md
# Prompt: <name>
## Quando usar
## Quando não usar
## Contexto obrigatório
## Prompt
## Output esperado
## Critérios de aprovação
## Critérios de reprovação
## Follow-up obrigatório
```

## 5.3 Prompts base prioritários

### Research Pack (executor: Manus)
```txt
Atue como Research Subagent do CKOS (PMO sênior + arquiteto de produto). Investigue o tema e entregue um pacote operacional, não lista de links.
Tema: {topic} · Contexto CKOS: {context} · Objetivo: {objective}
Entregáveis: README.md, references_master.csv, shortlist_priority_A.md, research_log.md, implementation_brief_for_claude.md, credits_and_rights.md.
Para cada referência: o que observar; o que não copiar; como traduzir para CKOS; risco; prioridade; componente aplicável. Traduza tudo em decisão prática.
```

### Claude Code Implementation
```txt
Atue como Senior Frontend Engineer + PMO técnico. Leia os docs anexados: {docs}. Objetivo: {objective}. Escopo permitido: {allowed_scope}. Escopo proibido: {forbidden_scope}. Critérios de aprovação: {approval_criteria}.
Antes de codar: liste arquivos a alterar; confirme riscos; proponha cortes; aguarde aprovação se risco alto.
Durante: preservar rotas; criar fallback; não inventar módulo fora do briefing; documentar arquivos alterados.
Depois: rodar build/teste; gerar relatório; atualizar README.
```

### Codex Build
```txt
Engenheiro de implementação focado em código limpo, testes e integrações. Tarefa: {task}. Arquivos: {files}.
Regras: alteração mínima suficiente; preservar compatibilidade; validação e tratamento de erro; evitar abstração prematura; documentar decisões críticas.
Entregue: diff resumido; comandos de teste; riscos; próximos passos.
```

### Antigravity UI Review
```txt
Diretor de UI/UX motion e QA visual. Analise {screen_or_route}.
Critérios: hierarquia visual, fluidez, consistência de glass, radius, spacing, clareza de ação, responsividade, ruído, acessibilidade, fidelidade ao design system CKOS.
Entregue: diagnóstico por seção; top 5 problemas; top 5 correções; riscos; prompt de patch para executor.
```

### Metacognik Audit
```txt
Atue como Metacognik, auditor metacognitivo do CKOS. Analise {content}.
Audite: coerência, evidência, lacunas, riscos, suposições escondidas, vieses, overengineering, impacto no projeto, necessidade de aprovação humana.
Classifique: confiança 0-100; risco 0-100; recomendação: aprovar, ajustar, pausar ou escalar.
```

# 6. Agente responsável

`PMO_CKOS` (owner); skill `prompt-library-curation` (manutenção).

# 7. Superagentes envolvidos

Nick; Cognik; Metacognik; QA Lead; Builder Lead.

# 8. Skills necessárias

prompt-library-curation; agent-output-evaluation.

# 9. Prompts relacionados

Este documento é a biblioteca. Prompts de runtime/segurança vivem referenciados nos docs 10–13.

# 10. Integrações

Executores externos (Manus/Claude/Codex/Antigravity); runtime model router (10); evals (13).

# 11. Memória e contexto

Prompts aprovados e suas taxas de sucesso viram memória (qual prompt funciona para qual skill).

# 12. Edge cases

Prompt sem skill associada; prompt sem critério de aprovação; instrução estética ("capriche", "deixe premium", "Apple level", "melhore tudo", "crie algo insano") usada como especificação operacional → reprovar.

# 13. Métricas de sucesso

Prompts reutilizados; outputs aprovados sem retrabalho; prompts conectados a skills; execuções sem critérios de aprovação (meta 0); tempo prompt→artifact validado.

# 14. Critérios de aprovação

Prompt aprovado se conectado a skill/workflow, com inputs, output esperado, critérios de aprovação/reprovação e follow-up.

# 15. Critérios de reprovação

Reprovado se for frase solta, sem skill, sem critério, ou se usar direção estética como especificação única.

# 16. Related notes

- [[06_SKILLS_REGISTRY]]
- [[07_WORKFLOW_BLUEPRINTS]]
- [[19_CLAUDE_CODEX_EXECUTION_PROTOCOL]]
