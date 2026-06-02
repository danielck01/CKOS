---
title: "14 - Issues, Pipeline e Checkout Lock"
area: "Operação"
priority: "P0"
type: "deep-research-prompt"
project: "CKOS"
status: "draft"
tags: ["ckos", "issues", "pipeline", "checkout-lock"]
---

# 14 - Issues, Pipeline e Checkout Lock

## Objetivo

Definir tarefas, pipeline, bloqueios, prioridades e checkout lock para evitar duplicidade de execução por agentes.

## Contexto de uso

Use esta nota para gerar uma pesquisa profunda e aplicável sobre o módulo/tema acima. A resposta da IA deve virar documentação, requisitos, decisões de produto, tarefas técnicas e insumos para implementação.

## Prompt principal

```text
CONTEXTO FIXO DO CKOS:
CKOS é o sistema operacional AI-first da CKCompany para criar, coordenar e executar projetos, propostas, plataformas, produtos, campanhas e soluções com agentes de IA. Não é Branddock. Branddock é o OS de branding e decisão estratégica. CKOS é o control plane operacional da CKCompany.

Estamos codando localmente agora e depois vamos migrar todo o ecossistema CKOS para uma VPS. Já temos CDN e host. A arquitetura precisa prever ambiente local, staging e produção, sem depender de gambiarra. O sistema deve suportar multi-tenant, projetos, agentes, briefings, propostas, créditos, pagamentos, logs, aprovações humanas, custos por modelo/agente/run, suporte, knowledge base e workflows.

Estética CK:
fundo preto #000000, dark luxury, glassmorphism refinado, cards grandes e muito arredondados, tipografia estilo Helvetica Rounded, gradiente CK como acento: #FF6A00, #FF0033, #FF00A8, #6A00FF, #0033FF, #00FF7F. UI premium, limpa, útil, sem dashboard genérico.

TAREFA:
Atue como PMO técnico e arquiteto de execução multiagente. Crie o Deep Research de Issues/Pipeline com checkout lock.

ENTREGUE:
1. O que é uma issue no CKOS.
2. Diferença entre issue, sprint, run, decision e artifact.
3. Campos essenciais.
4. Prioridade por impacto, urgência, ROI, risco e dependência.
5. Status possíveis.
6. Checkout lock:
   - quem pode pegar;
   - por quanto tempo;
   - como renovar;
   - como liberar;
   - como evitar duplicidade.
7. Relação com agentes.
8. Relação com sprints.
9. Relação com aprovações.
10. UI Pipeline.
11. Modelo de dados.
12. Prompt de implementação.

REGRAS:
Pipeline não pode parecer Trello genérico.
Deve operar com agentes, bloqueios, contexto e ROI.
```

## Outputs esperados

- Spec Issues/Pipeline
- Regras de checkout lock
- Modelo de dados
- Prompt UI

## Critérios de aceitação

- Evita trabalho duplicado
- Prioriza com lógica de ROI
- Conecta tarefas, agentes e decisões

## Prompt de refinamento para implementação

```text
Com base na pesquisa acima, transforme o conteúdo em:
1. arquitetura funcional;
2. entidades e tabelas;
3. componentes de UI;
4. eventos do sistema;
5. permissões;
6. estados vazios, carregando, erro e sucesso;
7. plano de implementação local;
8. plano de migração para VPS;
9. riscos técnicos;
10. checklist final para produção.

Mantenha o padrão visual CK: fundo #000000, dark luxury, glassmorphism refinado, cards grandes e arredondados, gradiente CK apenas como acento, UX premium e objetiva.
```

## Prompt para Claude Code

```text
Atue como engenheiro full-stack sênior e PMO técnico do CKOS. Pegue a especificação acima e implemente de forma incremental no projeto local.

Antes de codar:
1. leia a estrutura atual do projeto;
2. identifique rotas, componentes, entidades e padrões já existentes;
3. não duplique componentes;
4. preserve a estética CK;
5. crie apenas o necessário para um MVP funcional;
6. prepare a arquitetura para futura migração para VPS;
7. não exponha secrets;
8. não crie telas genéricas.

Depois entregue:
- arquivos alterados;
- decisões tomadas;
- pendências;
- testes necessários;
- riscos antes de subir para staging/produção.
```

## Prompt negativo

- Não fazer Kanban genérico
- Não deixar agente executar tarefa sem lock
- Não ignorar bloqueios

## Próximas conexões sugeridas

- [[README.md]]
- [[INDEX.md]]
- [[03_03-arquitetura-local-para-vps.md]]
