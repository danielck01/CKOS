# Skill — learning_extraction

## Definição
Extrair aprendizado de resultados e feedback.

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
  "skill": "learning_extraction",
  "result": "",
  "confidence": "low|medium|high",
  "risks": [],
  "next_actions": []
}
```

## Critério de sucesso
A skill deve gerar um resultado operacional que possa alimentar outro agente, tarefa, proposta, workflow ou decisão.
