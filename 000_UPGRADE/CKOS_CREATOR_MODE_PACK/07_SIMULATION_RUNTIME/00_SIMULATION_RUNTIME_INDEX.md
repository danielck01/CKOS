---
title: Simulation Runtime Index
system_id: simulation_runtime_index
category: creator_mode_simulation_runtime
status: active
version: 1.0.0
owner: ceo_agent
reviewers:
  - founder
  - pmo_ckos
created_for: CKOS_CREATOR_MODE_PACK
created_at: 2026-05-26
---

# Simulation Runtime Index

## Proposito

Definir a camada documental que permite testar projetos no Codex como se o CKOS tivesse backend, API, conectores, policy engine, credit engine, PMO audit e event log.

Esta camada e uma simulacao operacional. Ela nao cria backend real, API real, banco de dados, migrations, automacoes, agentes reais ou conectores ativos.

## Status

Auxiliar.

Nao canonico.

Nao cria docs 25-30.

Nao altera arquitetura CKOS.

## O que esta camada permite

- Simular chamadas de API por nome.
- Simular servicos internos do backend.
- Simular conectores e integracoes.
- Simular estimativa de creditos.
- Simular policy decisions.
- Simular PMO audit.
- Simular checkout lock/release.
- Simular event log append-only.
- Gerar artifacts documentais a partir de projetos aprovados.

## O que esta camada nao permite

- Implementar UI.
- Criar backend real.
- Criar API real.
- Criar migrations.
- Criar tabelas reais.
- Criar agentes runtime.
- Executar conectores externos.
- Rodar n8n como core CKOS.
- Tratar Manus como infraestrutura definitiva.
- Alterar docs canonicos.
- Recriar docs 21-24.
- Criar docs 25-30.

## Ordem de leitura

1. `01_SIMULATED_BACKEND_CONTRACT.md`
2. `02_SIMULATED_API_ENDPOINT_MAP.md`
3. `03_CONNECTOR_REGISTRY_SIMULATION.md`
4. `04_MOCK_DATA_SCHEMAS.md`
5. `05_EVENT_LOG_SIMULATION.md`
6. `06_POLICY_MATRIX_FOR_SIMULATION.md`
7. `07_PROJECT_TEST_SCENARIO_TEMPLATE.md`
8. `08_DEMO_RUNBOOK_INTENT_TO_ARTIFACT.md`

## Fluxo de simulacao

```txt
FounderIntent
  -> CEO_AGENT_INTERPRETATION
  -> SimulatedBackendContract
  -> SimulatedAPIEndpointMap
  -> ConnectorRegistrySimulation
  -> MockDataSchemas
  -> PolicyMatrix
  -> CreditEstimate
  -> PMOAudit
  -> FounderApproval
  -> ArtifactGeneration
  -> DeliveryAudit
  -> EventLogSimulation
```

## Principio de seguranca

Toda simulacao deve carregar uma tarja conceitual:

```txt
SIMULATION_ONLY: true
NO_RUNTIME_EXECUTION: true
NO_BACKEND_CREATED: true
NO_API_CREATED: true
NO_CONNECTOR_EXECUTED: true
```

## Primeiro uso recomendado

Usar esta camada para testar um projeto em modo Planner, com uma intencao minima do Founder, sem iniciar implementacao.

O Projeto Miriam pode ser o primeiro case real depois de Founder approval especifico.

