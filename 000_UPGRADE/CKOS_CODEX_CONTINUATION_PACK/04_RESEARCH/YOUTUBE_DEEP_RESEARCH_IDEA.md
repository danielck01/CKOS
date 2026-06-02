---
title: YouTube Deep Research Idea
system_id: youtube_deep_research_idea
version: 0.1.0
status: draft
category: research_system
---

# YouTube Deep Research para CKOS

## Ideia

Criar um collector capaz de pesquisar canais e vídeos públicos para transformar conteúdo em conhecimento útil para agentes e RAG.

## Exemplos de temas

- Jung.
- Arquétipos.
- Sincronicidade.
- Criança interior.
- Reprogramação mental.
- Hábitos.
- Psicologia do poder.
- Storytelling.
- Filosofia prática.
- Branding emocional.

## Exemplo de canal

Canais sobre arquétipos e Jung podem ser usados como fonte de inspiração, interpretação cultural e linguagem simbólica. Não devem ser tratados automaticamente como fonte científica.

## Pipeline técnico futuro

1. `youtube_search_collector`: busca vídeos por canal/tema.
2. `youtube_metadata_collector`: coleta título, descrição, data, views, duração.
3. `youtube_transcript_collector`: coleta transcrição quando disponível.
4. `youtube_comment_collector`: coleta comentários públicos.
5. `video_frame_sampler`: seleciona frames para análise visual em vídeos específicos.
6. `source_reliability_scorer`: classifica confiabilidade.
7. `knowledge_note_generator`: cria notas no vault.
8. `rag_ingestion_pipeline`: transforma notas em chunks e embeddings.

## Como usar comentários

Comentários podem revelar:

- dúvidas frequentes;
- dores emocionais;
- linguagem do público;
- objeções;
- crenças populares;
- desejos;
- transformação percebida;
- feedback público.

## Risco

Não confundir popularidade com verdade. O CKOS deve separar:

- evidência científica;
- opinião;
- interpretação;
- relato pessoal;
- inspiração;
- hipótese.
