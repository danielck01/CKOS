---
title: "02 - CKOS vs Branddock"
area: "Fundamento"
priority: "P0"
type: "deep-research-prompt"
project: "CKOS"
status: "draft"
tags: ["ckos", "branddock", "posicionamento", "arquitetura"]
---

# 02 - CKOS vs Branddock

## Objetivo

Separar semanticamente CKOS e Branddock para evitar confusão de produto, narrativa, arquitetura e proposta.

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
Atue como estrategista de arquitetura de produto. Crie uma análise profunda separando CKOS e Branddock.

ENTREGUE:
1. Definição de Branddock.
2. Definição de CKOS.
3. O que cada sistema faz e não faz.
4. Pontos de conexão entre os dois.
5. Entidades que podem ser compartilhadas.
6. Entidades que não devem ser compartilhadas.
7. Riscos de confusão de marca.
8. Como explicar para:
   - cliente leigo;
   - founder;
   - agência;
   - equipe técnica;
   - investidor.
9. Regras para UI, naming e navegação.

CONSIDERE:
Branddock = branding, decisão estratégica, metacognição de marca e ROI.
CKOS = operação AI-first, criação de soluções, execução, agentes, propostas, projetos e controle.
```

## Outputs esperados

- Tabela comparativa CKOS vs Branddock
- Regras de naming
- Mapa de conexão entre sistemas
- Copy explicativa por público

## Critérios de aceitação

- Qualquer pessoa entende a diferença em menos de 60 segundos
- A equipe sabe onde cada feature pertence
- Evita sobreposição conceitual

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

- Não vender Branddock como CKOS
- Não dizer que CKOS é só uma evolução da Branddock
- Não misturar módulos de branding com módulos operacionais sem critério

## Próximas conexões sugeridas

- [[README.md]]
- [[INDEX.md]]
- [[03_03-arquitetura-local-para-vps.md]]
