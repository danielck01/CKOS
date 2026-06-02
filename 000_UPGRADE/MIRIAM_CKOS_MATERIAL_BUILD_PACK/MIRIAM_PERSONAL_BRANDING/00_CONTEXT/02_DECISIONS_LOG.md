# Decisions Log

Status: active

## Decisoes registradas

| Data | Decisao | Autoridade | Status | Observacao |
| --- | --- | --- | --- | --- |
| 2026-05-27 | Usar Briefing Vivo, nao questionario fixo | Founder | approved | O sistema deve perguntar apenas o necessario para avancar |
| 2026-05-27 | Etica vence crescimento em caso de conflito | Founder/PMO | approved | Especialmente por OAB, direito penal e exposicao feminina |
| 2026-05-27 | Nao criar outputs finais de marca nesta fase | Founder/PMO | approved | Bloqueia tom, pilares, bio, calendario, lancamento e HTML final |
| 2026-05-27 | Usar CKOS + Branddock como simulacao documental | Founder | approved | Sem backend, UI, API ou agente real |

## Checkout lock documental

```yaml
task_id: miriam_ai_first_briefing_runtime_20260527
agent: Codex
role: PMO_CKOS_Cognik_Metacognik_Docs_Architect
folder_scope: MIRIAM_PERSONAL_BRANDING
files_allowed: markdown_docs_inside_new_runtime_folder
files_forbidden:
  - canonical_ckos_architecture
  - backend_files
  - ui_files
  - migrations
  - final_brand_strategy
approval_required: founder_for_strategy_outputs
risk_level: high
status: released_after_documentation_update
```

## Proximas decisoes pendentes

- Miriam aprova responder o Briefing Vivo?
- Founder aprova gerar evidence map e matriz de riscos?
- Havera pesquisa externa adicional ou apenas fontes locais nesta etapa?
