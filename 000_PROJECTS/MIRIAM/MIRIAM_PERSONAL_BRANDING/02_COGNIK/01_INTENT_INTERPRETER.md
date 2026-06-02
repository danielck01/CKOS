# Cognik - Intent Interpreter

Status: simulation_protocol

## Funcao

Interpretar uma intencao curta do Founder ou de Miriam e transformar em objeto operacional.

## Entrada esperada

```txt
Criar projeto para perfil no Instagram para advogada penal recem-formada.
```

## Saida simulada

```yaml
intent_type: PROJECT_CREATION
domain: personal_branding_legal
risk_level: high
primary_risk:
  - OAB_publicidade_juridica
  - reputacao_profissional
  - tema_penal_sensivel
needs_context_pack: true
needs_pmo_audit: true
needs_human_approval: true
next_action: build_context_and_ask_next_best_question
```

## Regra

O interpretador nao cria estrategia final. Ele apenas transforma intencao em tarefa auditavel.
