---
title: Research Protocol for Manus
file: 18_RESEARCH_PROTOCOL_FOR_MANUS.md
phase: 05_IMPLEMENTATION_SYSTEM
category: research
version: 1.1.0
status: archived
superseded_by: 05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL.md
owner: PMO_CKOS
responsible_agent: Research Subagent
reviewers:
  - Metacognik
  - Datta
approval_required:
  - founder
purpose: Definir como o Manus é usado na fase inicial — como Research Subagent (tool externa) para investigação, curadoria e packs operacionais, não como executor de produto.
inputs: Objetivo da pesquisa; contexto do projeto; docs de governança; restrições; links; critérios.
outputs: Pacotes de pesquisa estruturados (README, CSV, shortlist, log, credits, implementation brief).
framework: Pergunta → pesquisa → curadoria → scoring → pacote → brief de implementação.
edge_cases: Referência bonita sem função; mistura whitelabel; lista sem créditos; sugerir copiar UI; pesquisa grande demais.
integrations: Pinterest, Behance, Dribbble, Awwwards, Mobbin, Product Hunt, docs, papers, repos; storage do CKOS; RAG (11).
prompts: Prompt base do Research Subagent; prompt de pesquisa de sistema.
metrics: Menos prompts para Claude/Codex; menos retrabalho; referências com função; direitos documentados.
related_notes:
  - ../02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md
  - 17_IMPLEMENTATION_PROTOCOL.md
  - 21_SELF_EVOLVING_SYSTEM.md
tags: [implementation, research, manus, curation, packs]
---

> **STATUS OFICIAL — Decisão PMO_CKOS (registrada em `ARCHITECTURE_PATCH_REPORT.md §13`):**
> Manus é uma **tool externa temporária de bootstrap de pesquisa**, usada exclusivamente na fase inicial de investigação/curadoria. Manus **não é** infraestrutura CKOS, **não é** provider/runtime component, e **não é** o Research Capability alvo da plataforma.
>
> A **CKOS Research Capability** definitiva será implementada via collectors especializados (Perplexity, Apify, PubMed, APIs de mercado, RAG privado) orquestrados pelo runtime de agentes — ver `doc 03_RUNTIME_SYSTEM/10` e `03_RUNTIME_SYSTEM/11`.
>
> Este documento descreve o protocolo de uso de Manus **exclusivamente como referência de processo** para a fase de pesquisa de bootstrap. Após a implementação dos collectors CKOS, este protocolo perde validade operacional.
>
> Nomenclatura canônica: `manus` (system_id) · `Manus` (display_name) · `@manus` (mention).

# 1. Propósito

Definir como o Manus é usado na fase inicial do CKOS: não como executor de produto, mas como **Research Subagent** (tool externa) para investigação, curadoria, benchmark, documentação, análise crítica e pacotes estratégicos.

> No futuro, a skill `research-pack-generation` (06) internaliza esse papel no próprio CKOS, com memória, execução e aprendizado contínuo (ver `21_SELF_EVOLVING_SYSTEM`). Manus é referência **temporária**.

# 2. Função dentro do CKOS

Manus entrega pacotes estruturados que reduzem retrabalho antes da implementação.

```txt
Correto:  pergunta estratégica → pesquisa → curadoria → scoring → pacote → brief de implementação
Errado:   pesquisa solta → lista de links → ideias bonitas → sem aplicação prática
```

# 3. Inputs

Objetivo da pesquisa; contexto do projeto; docs de governança; restrições visuais/técnicas; links; screenshots; critérios de seleção; formatos de entrega esperados.

# 4. Outputs

Obrigatórios: `README.md`, `research_log.md`, `references_master.csv`, `shortlist_priority_A.md`, `credits_and_rights.md`, `implementation_brief_for_claude.md`.
Sistêmicos (quando aplicável): `system_architecture_map.md`, `agent_orchestration_architecture.md`, `dashboard_architecture.md`, `workflow_references.md`, `risk_report.md`.

# 5. Framework operacional

## 5.1 Tipos de pesquisa

Visual · Product · System · Market · Technical · UX.

## 5.2 Processo

```txt
1. Definir pergunta central · 2. Termos de busca · 3. Coletar · 4. Classificar · 5. Pontuar
· 6. Filtrar · 7. Traduzir para CKOS · 8. O que não copiar · 9. Brief de implementação · 10. Direitos e links
```

## 5.3 Scoring obrigatório

| Critério | Peso |
|---|---:|
| Aplicabilidade real ao CKOS | 25 |
| Transferibilidade técnica | 20 |
| Valor estratégico | 20 |
| Originalidade sem gimmick | 10 |
| Viabilidade de performance | 10 |
| Clareza de uso | 10 |
| Direitos/link/autoria | 5 |

## 5.4 Regra de aplicação

Toda referência responde: o que observar? o que não copiar? como traduzir para CKOS? qual componente nasce disso? qual risco de interpretação?

## 5.5 Qualidade do CSV (lição da auditoria)

Todo `references_master.csv` deve ter **campos com vírgula entre aspas**, para não desalinhar colunas no parser. A shortlist é validada contra o CSV limpo (ver `MANUS_RESEARCH_FIX_REPORT.md`).

# 6. Agente responsável

`Research Subagent` (executor), subordinado a `PMO_CKOS`, auditado por `Metacognik`. (Antigo "Research Ops Agent" — `00_TAXONOMY §5.1`.)

# 7. Superagentes envolvidos

PMO_CKOS (objetivo/escopo); Cognik (padrões); Metacognik (qualidade/risco de copiar); Nick (traduz para o usuário); Datta (validação de fontes); Builder Lead (consome o brief).

# 8. Skills necessárias

research-pack-generation; benchmark-analysis; visual-curation; system-pattern-extraction; competitive-intelligence; implementation-briefing; rights-and-credits-check.

# 9. Prompts relacionados

Prompt base do Research Subagent e prompt de pesquisa de sistema em `08_PROMPT_LIBRARY §5.3`.

# 10. Integrações

Pinterest, Behance, Dribbble, Awwwards, Mobbin, Product Hunt, docs de produtos, papers, repos, screenshots, CSV; storage do CKOS; RAG (11).

# 11. Memória e contexto

Pesquisa aceita vira: referência no RAG (11); conhecimento do projeto; input para skills; fonte para prompts; restrição para QA; memória de design/produto.

# 12. Edge cases

Referência bonita sem função → reprovar; mistura paleta do projeto com sistema whitelabel → separar camada CK e skin; lista sem créditos → reprovar; sugerir copiar UI → bloquear; pesquisa grande demais → shortlist Priority A + backlog.

# 13. Métricas de sucesso

Menos prompts para Claude/Codex; menos retrabalho; clareza de implementação; referências com função; riscos mapeados; direitos documentados; pacote reutilizável.

# 14. Critérios de aprovação

README claro; CSV completo e bem formatado; shortlist útil; scoring aplicado; links rastreáveis; implementation brief direto; recomendações aplicáveis.

# 15. Critérios de reprovação

Lista genérica; estética sem sistema; ausência de links; ausência de "o que não copiar"; sem aplicação prática; sem brief; CSV malformado.

# 16. Related notes

- [[06_SKILLS_REGISTRY]]
- [[17_IMPLEMENTATION_PROTOCOL]]
- [[21_SELF_EVOLVING_SYSTEM]]
