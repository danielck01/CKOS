---
title: "01 Backup Diario Supabase Metadata"
tipo: "engenharia_de_prompt_n8n"
area: "n8n, automação, CKOS"
status: "draft"
json_workflow: "./01_Backup_Diario_Supabase_Metadata.json"
relacionado:
  - "../../../00_DigitalOcean_PMO/01_Decisao_PMO_Iniciar_com_DigitalOcean.md"
  - "../../../03_Policies/02_Policy_N8N_Prototipo_para_Codigo.md"
---

# 01 Backup Diario Supabase Metadata

## Objetivo

Rotina de backup de metadados e healthcheck operacional.

## Papel dentro do CKOS

Esta automação deve ser usada como atalho operacional para validar fluxo, integração e valor de negócio. Ela não deve virar core crítico sem migração posterior para código próprio.

## Engenharia de prompt para gerar automação no n8n

Use o prompt abaixo no Codex/Claude Code/n8n AI Builder:

```text
Você é um arquiteto de automações n8n para o CKOS.

Crie um workflow n8n para o seguinte objetivo:
Rotina de backup de metadados e healthcheck operacional.

Contexto:
- O CKOS é um sistema operacional AI-first para projetos, agentes, propostas, aprovações, ROI, suporte e execução.
- n8n deve atuar como acelerador, não como core crítico.
- Toda execução precisa ter project_id, user_id quando aplicável, audit_log, status e tratamento de erro.
- Nunca exponha segredos. Use variáveis de ambiente.
- Antes de executar ações caras ou sensíveis, aplicar Budget / Policy Gate.
- Persistir logs em endpoint interno do CKOS ou Supabase.
- O workflow precisa ser idempotente quando possível.

Crie:
1. Lista de nodes.
2. Campos de entrada esperados.
3. Variáveis de ambiente.
4. Tratamento de erro.
5. Estrutura JSON exportável do workflow.
6. Critérios para migrar esse fluxo para código próprio.
```

## Inputs esperados

```json
{
  "project_id": "uuid",
  "user_id": "uuid_optional",
  "source": "webhook_or_system",
  "payload": {},
  "estimated_cost_usd": 0
}
```

## Outputs esperados

```json
{
  "status": "success_or_blocked_or_error",
  "workflow": "01_Backup_Diario_Supabase_Metadata",
  "project_id": "uuid",
  "result": {},
  "audit_log_id": "uuid"
}
```

## Nodes sugeridos

- schedule
- httpRequest
- postgres
- slack

## Variáveis de ambiente

```bash
CKOS_API_URL=
CKOS_INTERNAL_API_KEY=
SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=
OPENROUTER_API_KEY=
APIFY_TOKEN=
SLACK_WEBHOOK_URL=
```

## Policy gate

Bloquear execução se:

- faltar project_id;
- houver custo estimado acima do budget;
- o usuário não tiver permissão;
- o conector estiver sem consentimento;
- o workflow exigir aprovação humana;
- ação envolver pagamento, crédito, exclusão ou envio externo.

## JSON base

Ver arquivo: `01_Backup_Diario_Supabase_Metadata.json`
