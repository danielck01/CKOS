---
title: Roadmap Integrado Claude + Codex
folder: 20_ROADMAP_OPERATING_SYSTEM
type: roadmap
status: draft
owner: CKOS PMO
agents: [Claude, Codex, PMO_CKOS, Cognik, Metacognik]
---
# Roadmap Integrado Claude + Codex

## Batch 0 — Study Mode
Claude lê `00_GOVERNANCE`, `03_INTENT_AND_BRIEFING_SYSTEM`, `04_QUESTION_ENGINE`, `06_CREATIVE_DNA_CORE` e cria perguntas de lacuna.
Codex lê `01_RUNTIME_FOUNDATION`, `02_PROJECT_RESOLUTION`, `13_MCP_API_INTEGRATION`, `14_RAG_VECTOR_SYSTEM` e valida implementabilidade.

## Batch 1 — Runtime Foundation
Codex prepara estrutura backend local, .env.example, scripts de healthcheck, pastas de logs e storage.
Claude audita policies, state machines, heartbeat e eventos.

## Batch 2 — MCP + API
Codex esboça MCP server, registry de tools/resources e REST contracts.
Claude valida segurança, acesso ao vault e limites de ferramentas.

## Batch 3 — RAG Multimodal
Codex prepara schema Supabase/pgvector e pipeline de embeddings configurável.
Claude define critérios de chunking, retrieval quality e promoção para memória.

## Batch 4 — Multimodal + Apify
Codex cria workers para análise de imagem, vídeo, frame e coleta Apify.
Claude define rubricas de evidência, sinais visuais e ROI.

## Batch 5 — Frontend Projection
Somente após runtime testado. React lê projeções, não executa lógica.
