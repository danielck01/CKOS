---
title: "10 - Models & Costs"
area: "FinOps AI"
priority: "P0"
type: "deep-research-prompt"
project: "CKOS"
status: "draft"
tags: ["ckos", "models-costs", "finops", "openrouter"]
---

# 10 - Models & Costs

## Objetivo

Projetar o painel de modelos, custos, tokens, orçamento, performance e otimização de uso.

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
Atue como AI FinOps Architect. Crie o Deep Research do módulo Models & Costs do CKOS.

ENTREGUE:
1. Objetivo do módulo.
2. Métricas essenciais:
   - custo por projeto;
   - custo por agente;
   - custo por run;
   - custo por modelo;
   - tokens input/output;
   - reasoning tokens;
   - latência;
   - taxa de erro;
   - qualidade percebida;
   - ROI por output.
3. Model Policy por papel.
4. Budget por projeto, agente, cliente e run.
5. Alertas de consumo.
6. Recomendações de otimização.
7. Integração com OpenRouter ou camada equivalente.
8. Logs necessários.
9. Modelo de dados.
10. UI premium.
11. Prompt de implementação.

REGRAS:
Não fazer painel financeiro decorativo.
O módulo precisa ajudar a reduzir custo e melhorar qualidade.
```

## Outputs esperados

- Spec Models & Costs
- Modelo de dados
- Políticas de orçamento
- Prompt UI

## Critérios de aceitação

- Permite controlar custo real
- Ajuda a escolher modelos por tarefa
- Conecta uso com ROI

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

- Não mostrar só gráfico sem decisão
- Não ignorar custos invisíveis
- Não tratar todos os modelos como iguais

## Próximas conexões sugeridas

- [[README.md]]
- [[INDEX.md]]
- [[03_03-arquitetura-local-para-vps.md]]
