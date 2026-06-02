---
title: CK Memory Standard v1
file: ck_memory_standard_v1.md
layer: canonical
doc_type: canonical_doc
status: active
version: 1.0.0
created_at: 2026-05-31
updated_at: 2026-05-31
owner: pmo_ckos
responsible_agent: metacognik
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - pmo_ckos
purpose: Definir o padrão de ck_memory.md como memória local de pasta no vault CKOS.
inputs:
  - estudo em 99_RESEARCH_LAB/12_DOCUMENTATION_PATTERN_NORMALIZATION/04_ck_memory_standard.md
outputs:
  - template e regras de ck_memory.md
related_notes:
  - canonical_documentation_standard_v1.md
  - readme_standard_v1.md
  - ck_tasks_standard_v1.md
tags: [ckos, canonical, memory, governance, documentation]
---

# CK Memory Standard v1

## 1. Purpose

Definir o padrão para `ck_memory.md` como arquivo de memória local de pasta. Estabelecer distinção clara entre memória local, memória global e documentação canônica.

## 2. Regra Central

> `ck_memory.md` é memória local da pasta.
> Não é memória global.
> Não é spec.
> Não é roadmap.
> Não é substituto de patch report.

## 3. Estrutura Obrigatória

```md
# CK Memory — [Folder Name]

## Operational Status

## Current Context

## Decisions Registered

## Open Questions

## Active Constraints

## Related Tasks

## Last Updates

## Next Step
```

## 4. YAML Obrigatório

```yaml
---
title: CK Memory — [Folder Name]
file: ck_memory.md
layer: memory
doc_type: folder_memory
status:
version:
created_at:
updated_at:
owner:
responsible_agent:
reviewers: []
approval_required: []
source_type: local_folder_state
source_path:
source_tool:
provenance_status:
confidence:
risk_level:
canonical_candidate: false
tags: []
---
```

## 5. Conteúdo Permitido

- Contexto atual da pasta.
- Decisões locais registradas.
- Perguntas abertas.
- Restrições ativas.
- Tasks relacionadas (referência a `ck_tasks.md`).
- Próximo passo curto.

## 6. Conteúdo Proibido

- Regras canônicas finais.
- Instruções de implementação de backend (exceto se a pasta explicitamente permite trabalho de backend).
- Claims de memória global sem fonte.
- Decisões de promoção canônica não aprovadas.

## 7. Regra de Atualização

Atualizar `ck_memory.md` quando o estado local da pasta mudar. Não usar como substituto de release note ou patch report.

## 8. Sobre `_folder_memory.md` (Legado)

- `_folder_memory.md` é o padrão legado de memória de pasta.
- **Não deletar.**
- **Não renomear automaticamente.**
- Quando existir `ck_memory.md` ativo e aprovado, `_folder_memory.md` pode ser marcado como `legacy/superseded` apenas após patch report aprovado.
- Inventariar antes de qualquer ação — pode conter memória histórica valiosa.

## 9. O Que Não Fazer

- Não substituir `_folder_memory.md` automaticamente.
- Não tratar memória local como canônica.
- Não registrar decisões globais de sistema apenas em memória local.
- Não usar `ck_memory.md` para autorizar implementação de backend ou runtime.
