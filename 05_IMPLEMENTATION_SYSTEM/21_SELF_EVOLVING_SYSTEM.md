---
title: Self-Evolving System
file: 21_SELF_EVOLVING_SYSTEM.md
phase: 05_IMPLEMENTATION_SYSTEM
category: self_evolving
version: 1.0.0
status: archived
superseded_by: 07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md
owner: PMO_CKOS
responsible_agent: Builder Lead
reviewers:
  - Metacognik
  - QA Lead
approval_required:
  - founder
  - technical
  - Metacognik
purpose: Definir, com controle e sem hype, a visão de Builder Subagents internos que evoluem o próprio CKOS — escada de autonomia, dependências e guardrails.
inputs: Runtime (10); Security (12); Evals (13); Autonomy (04); Implementation (17); QA/Approval (20).
outputs: Visão controlada; escada de 9 níveis de autonomia; guardrails duros; o que muda o papel do Founder.
framework: Loop pesquisa→proposta→patch→sandbox→QA→approval→merge, com autonomia crescente sob gates.
edge_cases: Agente quer alterar política; eval insuficiente; rollback falha; custo descontrolado; loop de auto-modificação.
integrations: Sandbox isolado; CI/CD; Git; Runtime (10); Security (12); Evals (13); Approval (04/20).
prompts: Proposta de melhoria; patch em sandbox; auto-QA.
metrics: % de melhorias propostas aceitas; prompts manuais do Founder evitados; regressões barradas antes do merge; rollbacks bem-sucedidos.
related_notes:
  - ../01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - 20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md
tags: [implementation, self_evolving, autonomy_ladder, guardrails, ai_dev_team]
---

> **Superseded Notice:**  
> This document is preserved as historical source material. The canonical Self-Evolving architecture has moved to `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`. Do not use this file as the active source of truth.

# 1. Propósito

Definir, **com controle e sem hype**, a visão futura em que o CKOS opera com um time interno de Builder Subagents que evolui o próprio sistema — reduzindo a dependência de prompts manuais do Founder para Manus, Claude, Codex e Antigravity.

> **Aviso de maturidade:** este documento é `draft` e **não habilita nada** sozinho. Cada nível da escada (§5.2) só liga quando Runtime (10), Security (12), Evals (13), sandbox, rollback e approval gates (04/20) existirem e estiverem aprovados. Sem essas fundações, este documento é visão, não capacidade.

# 2. Função dentro do CKOS

Descrever o destino (o "Manus próprio" da Constituição §3 e P10) e o caminho seguro até ele. Transforma o Founder de **prompt operator** em **approver/strategic operator**: ele aprova decisões críticas; o sistema pesquisa, propõe, executa em sandbox, valida e pede aprovação.

# 3. Inputs

Runtime (10); Security (12); Evals (13); Autonomy (04); Implementation Protocol (17); QA/Approval (20); backlog de melhorias; incidentes (13).

# 4. Outputs

Visão controlada; escada de autonomia; guardrails duros; mudança de papel do Founder; critérios para subir de nível.

# 5. Framework operacional

## 5.1 O que o sistema pode (futuramente) fazer

Propor melhorias; gerar research pack (18/`research-pack-generation`); criar code patch (19); executar QA (20); solicitar aprovação (04); aprender com a execução (13/11). **Tudo isso depende de runtime, security, evals, sandbox, rollback e approval gates.**

## 5.2 Escada de autonomia (9 níveis)

Cada nível só é habilitado quando o anterior é estável **e** as dependências de gate existem. Subir de nível exige decisão explícita do Founder.

| # | Nível | O que o sistema faz | Gate obrigatório |
|---|---|---|---|
| 1 | Pesquisa assistida | investiga e organiza packs | Evals de qualidade de pesquisa (13) |
| 2 | Proposta de melhoria | sugere mudança com justificativa | Metacognik review |
| 3 | Patch sugerido | escreve patch, **não aplica** | Scope contract (19) + revisão humana |
| 4 | Patch em sandbox | aplica patch em ambiente isolado | Sandbox isolado + 12 (least privilege) |
| 5 | QA automático | roda QA + evals no sandbox | Evals + regressão (13) + QA Lead |
| 6 | Aprovação Founder | empacota e pede approval | Approval gate (04/20) |
| 7 | Merge assistido | aplica em produção após aprovação | Founder approval + rollback pronto |
| 8 | Autonomia limitada | executa classes pré-aprovadas de mudança P3/P4 | Política explícita + auditoria contínua (13) |
| 9 | Autonomia supervisionada | opera dentro de políticas, Founder amostra | Tudo acima + incident review ativo |

## 5.3 O loop seguro

```txt
detectar oportunidade/incidente (13) → proposta (2) → patch (3) → sandbox (4)
→ auto-QA + evals (5) → empacotar approval (6) → Founder aprova (04/20) → merge assistido (7)
→ observar/regressão (13) → aprender (11) → [rollback se necessário (10 §5.13)]
```

## 5.4 Sandbox

Ambiente isolado (branch/worktree/container) onde Builder Subagents aplicam e testam patches **sem** tocar produção, dados reais ou segredos. Token efêmero least-privilege (12 §5.6). Nenhuma ação externa irreversível no sandbox.

# 6. Agente responsável

Owner documental `PMO_CKOS`; owner técnico `Builder Lead`; auditoria `Metacognik`; qualidade `QA Lead`; aprovação `Founder`.

# 7. Superagentes envolvidos

Builder Lead; Builder Subagents; Metacognik; QA Lead; PMO_CKOS; Founder.

# 8. Skills necessárias

implementation-planning; repo-inspection; rollback-assessment; agent-output-evaluation; qa-gate; risk-classification; decision-logging.

# 9. Prompts relacionados

```txt
Proponha uma melhoria do CKOS: problema, evidência, mudança proposta, impacto (P0-P4), risco, custo estimado, rollback. Não aplique nada.
```

```txt
Aplique este patch APENAS no sandbox. Rode build, testes e evals. Reporte scores, regressões e diffs. Não toque produção, dados reais ou segredos.
```

# 10. Integrações

Sandbox isolado; CI/CD; Git; Runtime (10); Security (12, least privilege + vault); Evals (13, gate de regressão); Approval (04/20).

# 11. Memória e contexto

Cada ciclo registra: proposta, decisão, patch, resultado de QA/eval, aprovação, resultado em produção, rollback (se houve), aprendizado → memória longa (11). Incidentes ajustam thresholds (13).

# 12. Edge cases (guardrails duros)

- **Agente tenta alterar política de segurança/aprovação/permissão** → proibido por design (12 §5.6). Auto-escalonamento é negado.
- **Eval insuficiente para a mudança** → não pode subir de nível nem fazer merge (13).
- **Rollback falha** → congela autonomia, incidente P0, intervenção humana.
- **Custo descontrolado** → throttle + approval (13 §5.7).
- **Loop de auto-modificação** (sistema mudando o que o avalia) → separação de poderes: quem gera ≠ quem avalia ≠ quem aprova. Detector de ciclo (10 §12).
- **Mudança em runtime/security/evals/approval** → sempre P0, sempre Founder, nunca autônoma.

# 13. Métricas de sucesso

% de melhorias propostas aceitas; nº de prompts manuais do Founder evitados (objetivo de P10); regressões barradas antes do merge; rollbacks bem-sucedidos; incidentes por mudança autônoma (meta baixa); tempo proposta→merge aprovado.

# 14. Critérios de aprovação

Aprovado quando: a escada é explícita e gateada; nenhum nível liga sem suas dependências; agentes não alteram política; sandbox isola de produção/dados/segredos; eval+regressão precedem merge; rollback sempre possível; Founder aprova mudanças críticas.

# 15. Critérios de reprovação

Reprovado se: promete autonomia sem gate; permite agente alterar segurança/aprovação; merge sem eval/regressão; sem sandbox; sem rollback; trata o Founder como removível de decisões críticas; qualquer "autonomia total" sem supervisão.

# 16. Related notes

- [[03_AGENT_OPERATING_MODEL]]
- [[10_SYSTEM_RUNTIME_ARCHITECTURE]]
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]]
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]]
- [[20_QA_AND_FOUNDER_APPROVAL_PROTOCOL]]
