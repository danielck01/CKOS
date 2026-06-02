# Study Notes Index

## Fluxo RAW -> STUDY -> CANONICAL

1. Material bruto entra em `../000_UPLOADS/`.
2. PMO triage define origem, risco, PII e destino.
3. `source_manifest` ou `study_note` e criado nesta camada.
4. Nota vira synthesis, decision log ou patch candidate.
5. Patch candidate vai para patch plan aprovado.
6. Somente depois disso um doc canonico pode ser alterado.

## Como usar

- Use `_templates/` para toda nota nova.
- Mantenha YAML completo.
- Relacione `source_path` ao upload bruto.
- Use `related_docs` para apontar possiveis docs afetados.
- Registre confidence e risk_level com conservadorismo.

## Regras proibidas

- Nao colar study note em doc canonico.
- Nao usar `09_APPROVED_FOR_CANONICAL_PATCH` como status canonico.
- Nao usar output de IA como evidencia verificada.
- Nao pular PMO, Metacognik, Technical ou Founder quando aplicavel.
- Nao liberar UI/backend/API/migrations a partir de uma nota.

## Exemplos de naming

- `20260527_manus_mcp-connectors-research_pmo_ckos_study.md`
- `20260527_codex_uploads-yaml-template_pmo_ckos_patch-candidate.md`
- `20260527_apify_instagram-export_pmo_ckos_source-manifest.md`

## Exemplos de promocao

- RAW MCP research -> study note -> patch candidate para futuro doc 26.
- RAW connector export -> source manifest -> study note de integracao -> patch candidate para futuro doc 27.
- RAW UI reference -> UI study note -> backlog para docs 32-33, sem UI real.

## Exemplos de rejeicao

- Nota sem source_path.
- Pesquisa sem provenance.
- Output de IA sem validacao e sem confidence baixo.
- Material com PII nao classificada.
- Patch candidate sem related docs e sem decisao PMO.

