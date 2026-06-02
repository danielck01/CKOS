---
title: "05 - Briefing Inteligente com Nick"
area: "Produto"
priority: "P0"
type: "deep-research-prompt"
project: "CKOS"
status: "draft"
tags: ["ckos", "briefing", "nick", "produto", "ia"]
---

# 05 - Briefing Inteligente com Nick

## Objetivo

Criar o fluxo de briefing adaptativo que transforma intenção em projeto, cards, proposta e execução.

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
Atue como arquiteto de conversação, PMO e estrategista de produto. Desenvolva o Deep Research do Briefing Inteligente do CKOS com a Nick.

ENTREGUE:
1. Objetivo do briefing.
2. Diferença entre formulário comum e briefing cognitivo.
3. Fluxo de perguntas adaptativas.
4. Como detectar lacunas, contradições e oportunidades.
5. Como transformar respostas em:
   - cards;
   - tarefas;
   - proposta;
   - stakeholders;
   - riscos;
   - orçamento;
   - workflows;
   - knowledge base.
6. Perguntas iniciais por tipo de projeto:
   - app;
   - plataforma;
   - campanha;
   - branding;
   - ecommerce;
   - produto digital;
   - automação;
   - proposta comercial.
7. Como a Nick deve falar com cliente leigo.
8. Como a Nick deve falar com founder.
9. Como a Nick deve falar com equipe técnica.
10. Modelo de dados.
11. Estados de UI.
12. Prompt de implementação.

REGRAS:
A Nick não deve parecer atendente genérica.
Ela deve conduzir com inteligência, clareza e precisão.
A cada resposta, ela deve estruturar algo útil no projeto.
```

## Outputs esperados

- Fluxo completo de briefing
- Banco de perguntas
- Modelo de transformação resposta → estrutura
- Prompt de implementação da Nick

## Critérios de aceitação

- O briefing gera estrutura, não apenas texto
- Detecta lacunas e cria próximos passos
- Pode iniciar qualquer projeto no CKOS

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

- Não fazer onboarding longo e chato
- Não perguntar coisas que já foram respondidas
- Não usar tom robótico

## Próximas conexões sugeridas

- [[README.md]]
- [[INDEX.md]]
- [[03_03-arquitetura-local-para-vps.md]]
