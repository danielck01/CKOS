# Skill — quality_assurance

## Definição
Validar output contra critérios e policies.

## Quando usar
Quando a intenção, o briefing ou o agente exigir esta capacidade.

## Input
```json
{
  "context_state": {},
  "goal": "",
  "constraints": [],
  "evidence": []
}
```

## Output
```json
{
  "skill": "quality_assurance",
  "result": "",
  "confidence": "low|medium|high",
  "risks": [],
  "next_actions": []
}
```

## Critério de sucesso
A skill deve gerar um resultado operacional que possa alimentar outro agente, tarefa, proposta, workflow ou decisão.
