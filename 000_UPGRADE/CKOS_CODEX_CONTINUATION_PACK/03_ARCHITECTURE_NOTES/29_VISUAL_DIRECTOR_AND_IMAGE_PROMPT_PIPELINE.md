---
title: Visual Director and Image Prompt Pipeline
system_id: visual_director_and_image_prompt_pipeline
version: 0.1.0
status: draft
category: future_system
---

# 29 — Visual Director and Image Prompt Pipeline

## Propósito

Definir como o CKOS pode gerar direção visual, prompts de imagem e assets conceituais sem depender de improviso em chats separados.

## Problema atual

Hoje o Founder precisa abrir outro chat, explicar contexto e pedir imagem. Isso perde contexto, aumenta retrabalho e gera inconsistência.

## Solução futura

Criar um pipeline:

1. seção ou conceito;
2. Visual Director interpreta;
3. Metacognik audita coerência;
4. Prompt Engineer gera prompt;
5. Founder aprova;
6. Image tool gera asset;
7. asset vira artifact;
8. artifact entra no vault/projeto;
9. feedback visual ajusta o prompt.

## Modos

### Prompt-only Mode

Gera apenas o prompt. Ideal para usar em outro chat ou ferramenta.

### Concept Frame Mode

Gera uma descrição de composição e wireframe.

### Image Generation Mode

Gera imagem, quando autorizado.

### QA Visual Mode

Audita se a imagem respeita marca, composição, proporção e uso.

## Tipos de prompt

- hero image;
- section background;
- conceptual metaphor;
- glassmorphism UI mock;
- cinematic portrait;
- object metaphor;
- abstract system diagram;
- editorial still;
- motion storyboard.

## Regra atual

Não implementar gerador de imagem agora. Documentar pipeline e criar prompts auxiliares para usar manualmente.
