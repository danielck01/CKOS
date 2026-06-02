---
title: "01 - CKOS como AI-First Operating System"
area: "Fundamento"
priority: "P0"
type: "deep-research-prompt"
project: "CKOS"
status: "draft"
tags: ["ckos", "ai-first", "fundamento", "produto"]
---

# 01 - CKOS como AI-First Operating System

## Objetivo

Definir com precisão o que torna o CKOS um sistema operacional AI-first, evitando que ele pareça apenas um SaaS, app de tarefas ou chatbot.

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
Atue como arquiteto de produto AI-first e PMO técnico. Faça uma deep research conceitual e prática sobre o que significa o CKOS ser um AI-First Operating System.

ENTREGUE:
1. Definição curta, executiva e vendável do CKOS.
2. Definição técnica para equipe de produto.
3. Diferença entre OS, SaaS, chatbot, dashboard e automação.
4. Princípios inegociáveis de um OS AI-first.
5. Como isso se traduz em telas, entidades, agentes, rotinas e UX.
6. Riscos de parecer genérico.
7. Uma tese de posicionamento: “o projeto como organismo vivo”.
8. Aplicações no MVP local e requisitos para VPS.

REGRAS:
Não use linguagem hype.
Não usar “revolucionário” sem provar.
Não confundir CKOS com Branddock.
Foque em execução, decisão, ROI, agentes e operação.
```

## Outputs esperados

- Nota estratégica com definição oficial
- Quadro comparativo OS vs SaaS vs chatbot
- Lista de requisitos de produto
- Recomendações para MVP e VPS

## Critérios de aceitação

- O texto permite explicar o CKOS para sócio, dev e cliente
- Deixa claro que CKOS não é app comum
- Aponta implicações concretas para arquitetura e UI

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

- Não criar manifesto vazio
- Não usar linguagem excessivamente técnica para a proposta comercial
- Não tratar CKOS como gestor de tarefas

## Próximas conexões sugeridas

- [[README.md]]
- [[INDEX.md]]
- [[03_03-arquitetura-local-para-vps.md]]
