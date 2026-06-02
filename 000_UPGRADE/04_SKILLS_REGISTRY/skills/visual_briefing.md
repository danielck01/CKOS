# Skill — visual_briefing

## Definição
Criar direção visual e briefing de produção.

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
  "skill": "visual_briefing",
  "result": "",
  "confidence": "low|medium|high",
  "risks": [],
  "next_actions": []
}
```

## Critério de sucesso
A skill deve gerar um resultado operacional que possa alimentar outro agente, tarefa, proposta, workflow ou decisão.
