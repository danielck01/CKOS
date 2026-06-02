---
title: Claude/Codex Execution Protocol
file: 19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md
phase: 05_IMPLEMENTATION_SYSTEM
category: implementation
version: 1.1.0
status: archived
superseded_by: 05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md
owner: PMO_CKOS
responsible_agent: Builder Lead
reviewers:
  - Metacognik
  - QA Lead
approval_required:
  - founder
purpose: Definir como Claude Code, Codex, Antigravity e Builder Subagents executam código — sem prompts soltos, escopo aberto, refatorações perigosas ou consumo desnecessário de créditos.
inputs: Implementation brief (17); docs de arquitetura; rota/módulo afetado; restrições; critérios; branch alvo; arquivos permitidos.
outputs: Patch; arquivos criados/alterados; build/test status; riscos; QA checklist; README atualizado; rollback instructions.
framework: Modos (Inspect/Plan/Patch/Build/Refactor/QA/Handoff) + regra dos 3 passos + scope contract + cortes + no silent decisions.
edge_cases: "Melhorias" sem pedir; Codex×Claude discordam; asset ausente; build falha; UI bonita/estratégia errada; mock vs real.
integrations: Git; dev server; terminal; Supabase; OpenRouter; Runtime (10); Security (12); RAG; CI/CD futuro.
prompts: Inspeção; patch; QA.
metrics: Build passa; 0 alteração fora do escopo; menor consumo de crédito; menos retrabalho; handoff claro.
related_notes:
  - 17_IMPLEMENTATION_PROTOCOL.md
  - ../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../02_EXECUTION_SYSTEM/08_PROMPT_LIBRARY.md
  - 20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md
tags: [implementation, executors, scope_contract, builder]
---

# 1. Propósito

Definir como Claude Code, Codex, Antigravity e os futuros Builder Subagents atuam no desenvolvimento do CKOS, evitando prompts soltos, escopo aberto, refatorações perigosas e consumo desnecessário de créditos. **Agnóstico de ferramenta** — define o comportamento de qualquer executor de código.

# 2. Função dentro do CKOS

Transformar arquitetura e briefs em implementação segura, incremental, auditável e validável.

```txt
Executores não são PMO. Executores não decidem produto sozinhos. Executores executam dentro do escopo aprovado.
```

# 3. Inputs

Implementation brief (17); docs de arquitetura; rota/módulo afetado; screenshots; bug report; assets; restrições; critérios de aprovação; branch/pasta alvo; arquivos permitidos.

# 4. Outputs

Patch; arquivos criados/alterados; build/test status; riscos; limitações; QA checklist; README atualizado; próximos passos; rollback instructions.

# 5. Framework operacional

## 5.1 Modos de execução

| Modo | Uso |
|---|---|
| Inspect | ler projeto e mapear arquivos |
| Plan | propor implementação sem codar |
| Patch | aplicar correção específica |
| Build | criar módulo novo aprovado |
| Refactor | melhorar arquitetura sem mudar comportamento |
| QA | validar e reportar |
| Handoff | documentar para próximo executor |

## 5.2 Regra dos 3 passos

```txt
1. Entender · 2. Planejar · 3. Executar
```

Pular para o código sem plano → tarefa interrompida.

## 5.3 Scope Contract

```txt
Pode alterar: [arquivos] · Não pode alterar: produção, auth, pagamentos, dados reais, rotas não relacionadas
Entrega esperada: [X, Y, Z]
```

Permissões de arquivo/rota respeitam `12_SECURITY` (least privilege para Builder Subagents).

## 5.4 Build strategy (cortes)

```txt
Corte 1 — estrutura · 2 — UI/componente · 3 — lógica · 4 — estados · 5 — QA · 6 — documentação
```

## 5.5 No silent decisions

Sem decisões silenciosas sobre: preço; planos; contrato; escopo de cliente; identidade visual central; arquitetura; remoção de features; integrações pagas; dados sensíveis; deploy. (Liga em 04/12.)

# 6. Agente responsável

`Builder Lead` (orquestra); executores: **Builder Subagents** — Frontend, Backend, Data, RAG, Automation, Design System, QA Builder. (Antigo "Builder Agent(s)" — `00_TAXONOMY §5.1`.)

# 7. Superagentes envolvidos

PMO_CKOS (escopo/prioridade); Metacognik (auditoria/riscos); Cognik (contexto/intenção); QA Lead (validação); Founder (aprovação crítica).

# 8. Skills necessárias

repo-inspection; frontend-implementation; backend-implementation; database-migration; rag-pipeline; ui-motion-build; debugging; testing; documentation; handoff.

# 9. Prompts relacionados

```txt
Modo INSPECT — não altere arquivos. Leia árvore, framework, rotas, componentes, CSS, assets e riscos. Relatório: estrutura, arquivos principais, onde implementar, riscos, plano.
```

```txt
Modo PATCH — Escopo: [...]. Pode alterar: [...]. Não pode alterar: [...]. Confirme plano em cortes; implemente; rode build/test; entregue relatório.
```

```txt
Modo QA — não implemente correções. Valide rota, console, responsividade, estados, interações, regressões e critérios. Entregue QA_REPORT.md com screenshots sugeridos.
```

# 10. Integrações

Git; local dev server; terminal; package manager; devtools; Supabase; OpenRouter/OpenAI; storage; RAG; Runtime (10); Security (12); CI/CD futuro; logs de execução.

# 11. Memória e contexto

Cada implementação gera: `implementation_log`, `decision_log`, `known_issues`, `todo_next`, `files_changed` → memória média (11).

# 12. Edge cases

"Melhorias" sem pedir → bloquear/backlog; Codex×Claude discordam → Metacognik compara, PMO_CKOS decide; asset ausente → listar, não inventar; build falha → corrigir no escopo ou reportar; UI bonita/estratégia errada → QA reprova; recurso local depende de API real → documentar mock vs real.

# 13. Métricas de sucesso

Build passa; 0 alteração fora do escopo; menor consumo de crédito (13); menos retrabalho; arquivos documentados; QA aprovado; rollback possível; handoff claro.

# 14. Critérios de aprovação

Plano antes do código; escopo respeitado; build/test executado; relatório claro; QA sem bloqueadores; docs atualizados.

# 15. Critérios de reprovação

Código sem plano; refatoração ampla sem autorização; alteração de produção indevida; ausência de relatório; quebrar rota; feature fora do escopo; ocultar limitações.

# 16. Related notes

- [[17_IMPLEMENTATION_PROTOCOL]]
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]]
- [[08_PROMPT_LIBRARY]]
- [[20_QA_AND_FOUNDER_APPROVAL_PROTOCOL]]
