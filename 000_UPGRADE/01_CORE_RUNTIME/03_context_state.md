# Context State

O Context State é o objeto vivo que representa o estado do briefing.

## Campos mínimos

```json
{
  "briefing_id": "",
  "project_id": "",
  "user_intent": "",
  "intent_type": "",
  "current_stage": "",
  "active_agents": [],
  "selected_skills": [],
  "selected_tools": [],
  "connectors_used": [],
  "evidence": [],
  "questions_asked": [],
  "answers": [],
  "risks": [],
  "decisions": [],
  "approval_gates": [],
  "outputs": [],
  "roi_hypothesis": [],
  "learning_events": []
}
```

## Função
Evitar que o sistema seja apenas conversacional. Cada resposta atualiza um estado operacional.
