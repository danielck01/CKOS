---
title: Example Miriam Planning Only
system_id: example_miriam_planning_only
category: creator_mode_example
status: active
version: 1.0.0
owner: ceo_agent
created_for: CKOS_CREATOR_MODE_PACK
---

# Example Miriam Planning Only

## Input minimo

```txt
Criar projeto para perfil no Instagram para recem advogada penal feminina no Brasil.
```

## CEO_AGENT_INTERPRETATION

Intent detected:

Criar um projeto estrategico de personal branding para uma advogada penal recem-formada no Brasil, com foco inicial em arquitetura de confianca, reputacao, etica e presenca em redes sociais.

Project type:

```yaml
project_type: personal_branding_legal
category: legal_marketing
subcategory: personal_branding_legal
risk_level: high
regulated_domain: true
client_facing: true
```

Risk level:

High.

Reason:

Envolve publicidade juridica, reputacao profissional, OAB, advocacia criminal, linguagem publica e possivel promessa implicita.

Required context:

- Provimento 205/2021 OAB.
- Codigo de Etica e Disciplina da OAB.
- Pesquisas anexadas pelo Founder.
- Briefing da Miriam.
- Historico da conta atual, se autorizado.
- Objetivos profissionais reais.

Recommended first action:

Criar `PROJECT_INTENT_ANALYSIS.md` e `PROJECT_FILETREE_PROPOSAL.md`, nao estrategia final.

Estimated CKOS credits:

```txt
Leitura local: 2-4 CKC
Analise inicial: 4-8 CKC
PMO audit: 5-10 CKC
Filetree proposal: 4-8 CKC
Total fase inicial: 15-30 CKC
Deep research externo opcional: +20-60 CKC
```

Blocked actions:

- SWOT final.
- Tom de voz final.
- Pilares editoriais definitivos.
- Plano de conteudo de 30 dias.
- Identidade visual.
- Promessa comercial.
- Declaracao de conformidade juridica.

Needs PMO audit?

Yes.

Founder approval needed?

Yes.

Suggested output:

`analysis_doc` + `filetree_proposal`.

Question to Founder:

```txt
Voce quer seguir com fontes anexadas, autorizar deep research externo ou criar apenas briefing exploratorio sem conclusoes finais?
```

## Tese estrategica

A decisao nao e perfil pessoal vs perfil profissional. A decisao real e qual arquitetura de confianca acelera autoridade, distribuicao e conversao para uma advogada iniciante.

## Filetree inicial sugerida

```txt
PROJECTS/2026_PROJETO_MIRIAM_PERSONAL_BRANDING_PENAL/
|-- 00_PROJECT_CONTROL/
|-- 01_BRIEFING/
|-- 02_SOURCES_AND_EVIDENCE/
|-- 03_RISK_AND_COMPLIANCE/
|-- 04_STRATEGY_HYPOTHESES/
|-- 05_SQUADS_AND_WORKFLOWS/
`-- 06_OUTPUTS_DRAFTS/
```

## Proxima acao correta

Founder aprova a filetree antes de qualquer pack de notas.
