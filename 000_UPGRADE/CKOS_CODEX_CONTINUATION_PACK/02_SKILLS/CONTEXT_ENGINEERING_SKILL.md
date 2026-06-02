---
title: Context Engineering Skill
system_id: context_engineering_skill
version: 1.0.0
category: skill
---

# Context Engineering Skill

## Função

Montar contexto correto antes de qualquer agente, modelo ou ferramenta responder.

## Por que importa

Sem engenharia de contexto, cada IA responde como se estivesse começando do zero. O CKOS precisa evitar isso.

## Context Pack mínimo

1. Projeto ativo.
2. Objetivo do usuário.
3. Documento atual.
4. Estado do gate.
5. Políticas aplicáveis.
6. Memórias relevantes.
7. Resultados RAG.
8. Eventos recentes.
9. Custos e limites.
10. Output esperado.
11. Restrições.
12. Formato de resposta.

## Exemplo simples

Usuário pede: “Crie um briefing inteligente.”

O sistema não envia isso direto para um agente. Ele monta:

- projeto;
- tipo de briefing;
- setor;
- stakeholders;
- dados existentes;
- lacunas;
- política de coleta;
- modelos permitidos;
- créditos disponíveis;
- risco;
- formato de output.

Só depois chama o agente adequado.
