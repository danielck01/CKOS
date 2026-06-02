---
title: "08 - Organograma de Agentes"
area: "Multiagentes"
priority: "P0"
type: "deep-research-prompt"
project: "CKOS"
status: "draft"
tags: ["ckos", "agentes", "organograma", "governanca"]
---

# 08 - Organograma de Agentes

## Objetivo

Definir grupos, hierarquia, papéis, permissões e políticas dos agentes do CKOS.

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
Atue como Chief AI Architect. Crie a arquitetura do organograma de agentes do CKOS.

ENTREGUE:
1. Estrutura base:
   - CEO Agent;
   - PMO Agent;
   - CTO Agent;
   - UX Agent;
   - Branding Agent;
   - Data Agent;
   - Finance Agent;
   - QA Agent;
   - Support Agent.
2. Responsabilidade de cada agente.
3. O que cada agente pode fazer.
4. O que cada agente não pode fazer sem aprovação humana.
5. Políticas de orçamento por agente.
6. Políticas de modelo por agente.
7. Como agentes conversam entre si.
8. Como agentes questionam premissas.
9. Como agentes registram decisões.
10. Como criar grupos de agentes por projeto.
11. Modelo de dados.
12. UI Agents & Groups.
13. Prompt de implementação.

REGRAS:
Não criar agentes decorativos.
Cada agente deve ter função operacional clara, inputs, outputs e limites.
```

## Outputs esperados

- Mapa de agentes
- Políticas e permissões
- Modelo de dados
- Prompt para tela Agents & Groups

## Critérios de aceitação

- Cada agente tem utilidade real
- Define limites e aprovações
- Serve para MVP e expansão

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

- Não criar lista infinita de agentes sem função
- Não dar permissão total para todos
- Não ignorar custo por agente

## Próximas conexões sugeridas

- [[README.md]]
- [[INDEX.md]]
- [[03_03-arquitetura-local-para-vps.md]]
