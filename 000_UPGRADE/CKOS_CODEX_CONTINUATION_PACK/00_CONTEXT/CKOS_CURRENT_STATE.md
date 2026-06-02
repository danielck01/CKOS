---
title: CKOS Current State
system_id: ckos_current_state
version: 1.0.0
status: active
category: context_memory
---

# Estado Atual do CKOS

## O que o CKOS é

CKOS é o control plane operacional AI-first da CKCompany. Ele organiza projetos, agentes, decisões, documentos, propostas, custos, ROI, suporte e aprendizado.

Ele deve funcionar como um sistema vivo:

1. usuário cria conta;
2. cria projeto;
3. Nick faz briefing inteligente;
4. Cognik interpreta contexto;
5. Metacognik audita lacunas, riscos e coerência;
6. agentes especializados montam proposta;
7. usuário ou stakeholders aprovam;
8. runtime cria workflows, nodes e artefatos;
9. sistema acompanha custo, crédito, ROI, feedback e suporte;
10. aprendizado volta para memória do projeto.

## O que o CKOS não é

- Não é só chat com IA.
- Não é só dashboard.
- Não é Trello com agentes.
- Não é apenas uma plataforma de prompts.
- Não é Branddock.
- Não é um app de produtividade comum.

## Tese operacional

**O CKOS não executa comandos diretamente do usuário. Ele interpreta intenção, monta contexto, consulta políticas, decide rota, chama agentes, exige aprovações quando necessário, registra eventos e projeta o estado nas interfaces.**

## Termos centrais

- **Runtime:** motor vivo do sistema. É a parte que recebe eventos, aplica políticas, chama agentes, executa workflows e registra tudo.
- **Policy Engine:** motor que decide se uma ação pode acontecer, se precisa aprovação, qual risco existe e quais dados podem ser usados.
- **Registry:** catálogo oficial de coisas permitidas: agentes, ferramentas, skills, modelos, collectors, node types, prompts e políticas.
- **Transformer:** peça que transforma uma entrada em outra forma estruturada. Exemplo: briefing bruto → contexto limpo; comentário → feedback classificado; vídeo → transcrição + insights.
- **Projection:** leitura visual derivada do estado real. Dashboard, Canvas e Command Center não inventam dados; eles projetam dados vindos do Runtime.
- **Event Bus:** sistema interno de eventos. Agentes não “conversam” apenas por texto; eles emitem eventos estruturados.
- **RAG:** recuperação de conhecimento do vault/base vetorial para dar contexto antes de responder.
- **Embedding:** representação numérica de texto, usada para busca semântica.
- **MCP:** Model Context Protocol. Em termos simples, é um padrão para conectar modelos de IA a ferramentas, arquivos, bancos, APIs e contexto externo de forma mais organizada.

## Regra de ouro

Frontend não decide verdade. Frontend não chama ator externo direto. Frontend não expõe provider, token ou segredo. Tudo passa pelo runtime.
