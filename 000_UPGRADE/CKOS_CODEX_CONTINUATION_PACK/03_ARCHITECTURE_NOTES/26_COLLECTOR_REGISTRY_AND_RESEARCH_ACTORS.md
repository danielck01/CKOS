---
title: Collector Registry and Research Actors
system_id: collector_registry_and_research_actors
version: 0.1.0
status: draft
category: future_system
---

# 26 — Collector Registry and Research Actors

## Propósito

Definir como o CKOS coleta dados externos para pesquisa, benchmarking, feedback público, vídeos, comentários, artigos acadêmicos e fontes da web.

## Ideia central

No CKOS, “ator” não deve ser exposto como Apify Actor para o usuário. O usuário vê uma capacidade:

- Instagram Collector
- YouTube Research Collector
- PubMed Collector
- Competitor Collector
- Website Crawler
- Reviews Collector
- Ads Library Collector

O backend resolve provider, token, custo, política e normalização.

## YouTube Deep Research Collector

### Fontes

- Transcrição do vídeo.
- Título e descrição.
- Comentários públicos.
- Capítulos.
- Frames selecionados com análise visual quando necessário.
- Links citados.

### Pipeline

1. Receber tema ou canal.
2. Buscar vídeos relevantes.
3. Coletar metadados.
4. Transcrever.
5. Extrair argumentos principais.
6. Coletar comentários.
7. Classificar sentimento e dúvidas públicas.
8. Separar evidência, opinião, mito, hipótese e inspiração.
9. Gerar notas RAG.
10. Registrar confiabilidade.

## Exemplo de uso

Tema: Jung, arquétipos, sincronicidade, criança interior.

O collector deve gerar:

- resumo fiel;
- conceitos principais;
- alertas de pseudociência quando necessário;
- citações rastreáveis;
- comentários recorrentes;
- perguntas do público;
- potencial de uso para agentes de marca, psicologia e storytelling.

## Cuidados

- YouTube não é automaticamente fonte científica.
- Comentários são feedback público, não verdade.
- Conteúdo de espiritualidade deve ser marcado como inspiração, interpretação ou crença, quando não houver evidência científica.
- PubMed/universidades devem ter peso maior em claims científicos.

## Arquivos futuros

- `collectorRegistry.ts`
- `actorRegistry.ts`
- `providerRegistry.ts`
- `collectorRunner.ts`
- `collectorNormalizer.ts`
- `collectorPolicies.ts`
