---
title: Learning and Project Study Mode
system_id: learning_and_project_study_mode
version: 0.1.0
status: draft
category: future_system
---

# 25 — Learning and Project Study Mode

## Propósito

Criar uma camada de aprendizado dentro do CKOS para que o usuário entenda o próprio projeto, a arquitetura, os conceitos e as decisões sem depender de explicações soltas no chat.

## O que é

Uma biblioteca de estudo contextual dentro do CKOS. Não é um app separado. Pode futuramente estar dentro da CKStore ou como módulo nativo de cada projeto.

## O que resolve

- Founder não entende arquitetura técnica.
- Cliente não entende o que está sendo construído.
- Stakeholder se perde em documentos longos.
- Equipe precisa estudar antes de aprovar.
- IA precisa gerar material didático com base no vault.

## Capacidades

1. Gerar resumo de qualquer documento.
2. Explicar termos técnicos em linguagem simples.
3. Gerar flashcards.
4. Criar exercícios práticos.
5. Criar trilhas de estudo por perfil.
6. Criar mapa visual do projeto.
7. Gerar “modo apresentação” para cliente.
8. Gerar “modo founder” com decisões, riscos e ROI.
9. Gerar “modo técnico” com dependências e schema.
10. Gerar quiz para validar entendimento.

## Exemplo

Documento: `11_DATA_MODEL_AND_PERSISTENCE.md`

Learning Mode gera:

- O que é persistência?
- Por que existem tabelas?
- O que é append-only?
- O que é RLS?
- O que é event store?
- Por que dashboard não calcula verdade?
- Exercício: explique em 3 frases por que o frontend não pode chamar Apify direto.

## Relação com AI First

AI First não é só usar IA. É permitir que o próprio sistema transforme conhecimento complexo em aprendizado contextual, ação e decisão.

## MVP futuro

- Resumo por doc.
- Glossário automático.
- Flashcards.
- Checklist de entendimento.
- Botão “me explique como se eu fosse founder”.
