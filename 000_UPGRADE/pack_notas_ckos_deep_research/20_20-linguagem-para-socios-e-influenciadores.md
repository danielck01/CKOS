---
title: "20 - Linguagem para Sócios e Influenciadores"
area: "Comercial"
priority: "P0"
type: "deep-research-prompt"
project: "CKOS"
status: "draft"
tags: ["ckos", "comercial", "maria-blanco", "influenciadores"]
---

# 20 - Linguagem para Sócios e Influenciadores

## Objetivo

Definir linguagem de apresentação para sócios/influenciadores como María Blanco, sem termos técnicos.

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
Atue como estrategista de narrativa comercial premium. Crie o Deep Research de linguagem para apresentar o produto a sócios/influenciadores como María Blanco.

ENTREGUE:
1. Como explicar o produto em 15 segundos.
2. Como explicar em 60 segundos.
3. Como explicar em uma apresentação.
4. O que evitar:
   - CKOS;
   - HTML;
   - canvas;
   - VPS;
   - API;
   - RAG;
   - multi-tenant;
   - jargões técnicos.
5. O que enfatizar:
   - produto;
   - comunidade;
   - monetização;
   - experiência;
   - suporte;
   - confiança;
   - crescimento;
   - diferencial real.
6. Proposta de sociedade.
7. Modelo de revenue share.
8. Copy para hero.
9. Copy para seção de planos.
10. Copy para seção de suporte.
11. Copy para seção de confiança.
12. Prompt para gerar página de apresentação.

REGRAS:
Clareza acima de sofisticação vazia.
Ela precisa entender oportunidade, papel e potencial de ganho.
```

## Outputs esperados

- Guia de linguagem comercial
- Copies prontas
- Argumentos de sociedade
- Prompt de página

## Critérios de aceitação

- Uma pessoa não técnica entende o produto
- Foco em oportunidade e monetização
- Evita jargão

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

- Não usar termos técnicos
- Não parecer pitch de ferramenta
- Não prometer ganhos irreais

## Próximas conexões sugeridas

- [[README.md]]
- [[INDEX.md]]
- [[03_03-arquitetura-local-para-vps.md]]
