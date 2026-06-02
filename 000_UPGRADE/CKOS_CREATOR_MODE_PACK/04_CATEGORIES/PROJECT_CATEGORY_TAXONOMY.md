---
title: Project Category Taxonomy
system_id: project_category_taxonomy
category: creator_mode_taxonomy
status: active
version: 1.0.0
owner: pmo_ckos
created_for: CKOS_CREATOR_MODE_PACK
---

# Project Category Taxonomy

## Categorias iniciais

```txt
business_strategy
personal_branding
legal_marketing
research_pack
content_strategy
product_documentation
infra_automation
visual_research
prompt_pack
client_project
internal_ckos_protocol
```

## Campos obrigatorios

```yaml
project_type:
category:
subcategory:
risk_level:
regulated_domain:
client_facing:
requires_sources:
requires_pmo:
requires_founder:
```

## Regras

- Categoria define filetree inicial.
- Subcategoria define policies.
- Risco define approval.
- Dominio regulado bloqueia estrategia final sem fonte e revisao humana.

## Categorias sensiveis

- `legal_marketing`
- `health_marketing`
- `financial_advice`
- `children_or_minors`
- `public_reputation`
- `data_sensitive`
- `regulated_profession`

Essas categorias sempre exigem PMO audit.
