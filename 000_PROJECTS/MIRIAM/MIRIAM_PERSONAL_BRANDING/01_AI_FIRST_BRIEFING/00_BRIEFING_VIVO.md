# Briefing Vivo

Status: active_protocol

## Principio

O briefing nao e um formulario. Ele e uma conversa progressiva, auditavel e orientada por risco.

O sistema deve:

1. interpretar a intencao curta;
2. carregar contexto e fontes;
3. detectar lacunas;
4. escolher uma unica proxima pergunta necessaria;
5. registrar resposta como fato, hipotese, gap ou decisao;
6. gerar artefato parcial quando houver contexto suficiente;
7. acionar PMO/Metacognik antes de saida sensivel;
8. pedir aprovacao humana antes de avancar.

## Estado atual do briefing

```yaml
stage: pre_strategy
allowed_output:
  - questions
  - analysis_notes
  - evidence_map_draft
  - ethical_risk_matrix_draft
blocked_output:
  - final_positioning
  - final_tone_of_voice
  - final_content_pillars
  - content_calendar
  - final_bio
  - launch_plan
  - final_html
next_best_question_required: true
```

## Primeira pergunta recomendada

Qual e o objetivo primario de Miriam nos proximos 90 dias: construir autoridade, captar primeiros clientes, conseguir parceria/escritorio, educar audiencia, ou reposicionar uma conta ja existente?

## Como registrar a resposta

Cada resposta deve ser registrada em `04_RESPONSE_MEMORY.md` e gerar atualizacao de gaps em `../00_CONTEXT/03_ASSUMPTIONS_AND_GAPS.md`.
