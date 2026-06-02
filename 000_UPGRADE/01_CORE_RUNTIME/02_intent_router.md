# Intent Router

O Intent Router classifica a intenção do usuário antes de qualquer resposta.

## Tipos principais

- PROJECT_CREATION
- TASK_EXECUTION
- REELS_PRODUCTION
- CAMPAIGN_CREATION
- PROPOSAL_GENERATION
- DEEP_RESEARCH
- BRANDING_TOOL
- DESIGN_OUTPUT
- PRODUCT_SPEC
- AUTOMATION_BUILD
- SUPPORT_REQUEST
- DECISION_REQUEST
- FILE_ANALYSIS
- CONTENT_SYSTEM
- STRATEGIC_DIAGNOSIS
- ROI_ANALYSIS

## Saída do router

```json
{
  "intent_type": "REELS_PRODUCTION",
  "complexity": "medium",
  "requires_project": true,
  "requires_research": false,
  "requires_approval": true,
  "suggested_agents": ["Content Strategist", "Visual Director", "ROI Analyst"],
  "suggested_workflow": "reels_production_briefing"
}
```

## Regra
Se a intenção for pequena, o sistema pode criar tarefa direta.
Se a intenção tiver múltiplas dependências, vira mini-projeto.
Se gerar valor recorrente, pode virar projeto oficial.
