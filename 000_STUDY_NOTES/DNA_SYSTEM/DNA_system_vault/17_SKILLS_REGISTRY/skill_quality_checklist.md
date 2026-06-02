---
title: Skill Quality Checklist
folder: 17_SKILLS_REGISTRY
type: documentation
status: draft
owner: CKOS PMO
agents:
  - Cognik
  - Metacognik
backend_modules:
  - runtime
  - workflow-engine
  - memory-writer
api_contracts:
  - /intent/submit
  - /workflows/start
  - /memory/update
database_entities:
  - projects
  - workflow_runs
  - memory_updates
skills:
  - context.assemble_packet
  - qa.audit_output
  - memory.write_update
transformers:
  - intent_to_project
  - output_to_memory_update
policies:
  - no_project_no_workflow
  - evidence_required_for_claims
  - cost_guard_policy
roi_refs:
  - roi_hypothesis
  - cost_efficiency
memory_refs:
  - project_memory
  - decision_memory
---


# Skill Quality Checklist

## 1. Resumo
Nota operacional da pasta 17_SKILLS_REGISTRY, criada para orientar Claude, Codex, superagents, agents e subagents na arquitetura backend-first do DNA_system.

## 2. Propósito
Definir uma unidade operacional do DNA_system para que Claude arquitete, leia, edite e audite documentação enquanto Codex implementa, testa e sincroniza resultados técnicos. Esta nota deve ser usada como fonte de verdade local antes de qualquer execução de backend, worker, MCP, RAG ou provider externo.

## 3. Quando usar
Use quando o CommandBar, Claude, Codex ou um superagent precisar decidir se deve perguntar, planejar, executar, auditar, calcular custo, registrar evidência, atualizar memória ou abrir um lote em segundo plano.

## 4. Inputs
- Intenção do founder ou usuário.
- Projeto ativo ou Project Draft.
- Context Packet.
- Evidências, arquivos, imagens, MP4, URLs ou pastas.
- Limite de custo/crédito.
- Policies aplicáveis.

## 5. Outputs
- Decisão operacional documentada.
- Tarefas para Claude e Codex.
- Skills e transformers necessários.
- Eventos, heartbeats, logs, QA, ROI e memória esperada.

## 6. Fluxo operacional
```txt
intent → project_resolver → context_packet → smart_questions → planner → batch_tasks → background_runs → QA → ROI → feedback → learning → memory
```

## 7. Skills necessárias
- context.assemble_packet
- qa.audit_output
- memory.write_update

## 8. Transformers relacionados
- intent_to_project
- output_to_memory_update

## 9. Policies aplicadas
- no_project_no_workflow
- evidence_required_for_claims
- cost_guard_policy

## 10. Agents envolvidos
- Cognik
- Metacognik

## 11. Heartbeat esperado
```txt
awake → reading_context → asking_questions → planning → executing/background → auditing → updating_memory → done
```
Campos mínimos: `run_id`, `agent_id`, `status`, `current_step`, `reason_for_wake`, `confidence`, `cost_so_far`, `evidence_refs`, `blocker_reason`, `next_action`.

## 12. Integração com backend
O backend deve expor estado por eventos e projeções. Claude e Codex não substituem o backend; eles operam sobre o vault, validam gaps e implementam módulos.

## 13. Integração com MCP/API
MCP expõe ferramentas controladas. REST API executa runtime. CLI permite operação local. Workers executam tarefas pesadas ou segundo plano.

## 14. Integração com RAG/memória
Toda nota relevante deve ser indexável no RAG. Outputs aprovados podem virar memória; outputs rejeitados viram negative memory quando úteis.

## 15. ROI e métricas
ROI deve ser tratado como hipótese com proxies, nunca promessa. Métricas possíveis: redução de retrabalho, tempo de execução, custo evitado, qualidade do output, consistência com DNA, reutilização de memória.

## 16. Feedback e aprendizado
Feedback humano ou técnico gera revisão. Aprendizados aprovados promovem memória; erros recorrentes alimentam policies e checklists.

## 17. Failure modes
- Executar sem projeto ativo.
- Rodar provider caro sem approval.
- Usar LLM sem evidência.
- Criar nota genérica sem relação com runtime.
- Claude e Codex editarem a mesma pasta sem lock.
- Atualizar memória sem QA.

## 18. Perguntas inteligentes
- Esta execução pertence a qual projeto?
- Há contexto suficiente para executar em paralelo?
- Qual custo máximo aceito?
- Precisa de análise multimodal ou pesquisa externa?
- O output deve atualizar memória?
- Qual critério define entrega ruim?

## 19. Critérios de QA
A nota deve ser específica, acionável, conectada a backend, skills, transformers, policies, heartbeat, ROI, learning e memória.

## 20. Próximas tarefas para Claude/Codex
Claude: revisar coerência, lacunas, policies, contexto e perguntas. Codex: validar estrutura, scripts, schemas, endpoints, .env, workers e testes.
