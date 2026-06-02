---
title: Research Collector Skill
system_id: research_collector_skill
version: 1.0.0
category: skill
---

# Research Collector Skill

## Função

Orientar agentes de pesquisa a coletar dados externos de forma auditável, sem depender de Manus como infraestrutura final.

## Fontes possíveis

- Perplexity via OpenRouter.
- Apify collectors.
- PubMed.
- CrossRef.
- arXiv.
- YouTube transcript collectors.
- Comentários públicos.
- Sites oficiais.
- Bases internas via RAG.

## Regra

Manus pode ser usado como bootstrap temporário, mas não é fonte final do CKOS.

## Pipeline de pesquisa

1. Capturar pergunta.
2. Classificar tipo de pesquisa.
3. Definir fontes permitidas.
4. Coletar dados.
5. Normalizar fontes.
6. Extrair evidências.
7. Classificar confiabilidade.
8. Gerar síntese.
9. Criar notas no vault.
10. Registrar evidência, lacuna e hipótese.

## YouTube Research

Um collector de YouTube deve separar:

- metadados do vídeo;
- transcrição;
- comentários;
- frames analisados por modelo visual quando permitido;
- descrição;
- capítulos;
- links citados;
- sinais de recepção pública nos comentários;
- insights úteis para RAG.

## Cuidado

Conteúdo de YouTube pode ser opinião, interpretação ou pseudociência. O sistema deve classificar confiabilidade e separar inspiração de evidência científica.
