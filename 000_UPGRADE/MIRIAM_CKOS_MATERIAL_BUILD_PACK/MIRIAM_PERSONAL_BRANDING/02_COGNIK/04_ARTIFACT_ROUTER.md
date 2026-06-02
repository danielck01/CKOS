# Cognik - Artifact Router

Status: simulation_protocol

## Funcao

Escolher qual artefato deve ser produzido a partir do estado do briefing.

## Regras de roteamento

| Estado | Artefato permitido | Artefato bloqueado |
| --- | --- | --- |
| Intencao curta sem respostas | Intent analysis | Estrategia |
| Fontes lidas, respostas ausentes | Gaps + next question | Tom final |
| Respostas iniciais coletadas | Evidence map draft | Calendario |
| Risco classificado | Matriz etica draft | Promessa comercial |
| Founder aprova estrategia preliminar | Plano preliminar | Conteudo publicado |

## Saida

```yaml
artifact_to_create:
reason:
required_inputs:
approval_gate:
blocked_outputs:
```
