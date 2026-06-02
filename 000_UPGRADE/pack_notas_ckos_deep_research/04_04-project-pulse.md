---
title: "04 - Project Pulse"
area: "Produto"
priority: "P0"
type: "deep-research-prompt"
project: "CKOS"
status: "draft"
tags: ["ckos", "project-pulse", "ux", "produto"]
---

# 04 - Project Pulse

## Objetivo

Definir a página que mostra o estado vivo do projeto com status, progresso, risco, ROI, prioridades e próximas ações.

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
Atue como product architect e UX strategist. Crie a especificação profunda da página Project Pulse do CKOS.

ENTREGUE:
1. Objetivo da página.
2. Quem usa: owner, cliente, agente, PMO, reviewer.
3. Cards essenciais.
4. Indicadores obrigatórios.
5. Como mostrar progresso real sem parecer dashboard genérico.
6. Como conectar Project Pulse com:
   - Briefing;
   - Agents & Groups;
   - Issues;
   - Sprints;
   - Decisions;
   - Models & Costs;
   - Proposals;
   - Support.
7. Estados vazios.
8. Estados críticos.
9. Microcopy premium.
10. Dados necessários no banco.
11. Eventos que atualizam o Pulse.
12. Prompt para gerar UI React premium.

REGRAS DE UI:
Dark luxury.
Cards úteis, não decorativos.
Sem excesso de botões.
Commandbar e dock separados.
Mostrar “o que exige decisão agora”.
```

## Outputs esperados

- Spec da página Project Pulse
- Lista de componentes
- Modelo de dados inicial
- Prompt de UI para Claude Code

## Critérios de aceitação

- A página responde: onde estamos, o que importa, o que trava e qual próximo passo
- Mostra ROI e risco de forma operacional
- Não vira dashboard decorativo

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

- Não fazer gráfico fake sem ação
- Não repetir informações de outras páginas sem síntese
- Não poluir a tela

## Próximas conexões sugeridas

- [[README.md]]
- [[INDEX.md]]
- [[03_03-arquitetura-local-para-vps.md]]
