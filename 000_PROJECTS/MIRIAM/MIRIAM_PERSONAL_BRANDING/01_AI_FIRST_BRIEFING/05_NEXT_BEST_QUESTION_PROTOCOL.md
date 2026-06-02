# Next Best Question Protocol

Status: active_protocol

## Objetivo

Impedir que o briefing vire interrogatorio e garantir que cada pergunta tenha funcao operacional.

## Formato obrigatorio

```yaml
question:
why_now:
risk_reduced:
decision_unlocked:
artifact_unlocked:
answer_type:
blocked_if_unanswered:
```

## Criterios de escolha

- A pergunta precisa reduzir uma incerteza concreta.
- A resposta precisa atualizar contexto, risco ou decisao.
- A pergunta nao deve pedir gosto estetico cedo demais.
- Se houver risco etico, a pergunta de risco vem antes da pergunta de crescimento.

## Proxima pergunta atual

```yaml
question: "Qual e o objetivo primario de Miriam nos proximos 90 dias?"
why_now: "Sem objetivo primario, o sistema nao sabe se prioriza autoridade, captacao, carreira, educacao ou reposicionamento."
risk_reduced: "Evita gerar plano de conteudo desalinhado ou comercialmente agressivo."
decision_unlocked: "Define fluxo de perfil novo vs rebranding vs hibrido."
artifact_unlocked: "SOURCE_EVIDENCE_MAP_DRAFT + matriz de gaps"
answer_type: "single_choice_with_context"
blocked_if_unanswered: "posicionamento, tom, pilares, calendario, bio"
```
