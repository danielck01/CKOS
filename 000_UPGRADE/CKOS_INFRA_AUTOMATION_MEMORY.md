---
title: CKOS Infra Automation Memory
system_id: ckos_infra_automation_memory
category: upgrade_memory
status: draft
version: 1.1.0
owner: ceo_agent
reviewers:
  - founder
  - pmo_ckos
  - metacognik
related_notes:
  - ../CKOS_FILETREE_MAP.md
  - ckos_digitalocean_n8n_pack/00_README_INDEX.md
  - ckos_digitalocean_n8n_pack/00_DigitalOcean_PMO/01_Decisao_PMO_Iniciar_com_DigitalOcean.md
  - ckos_digitalocean_n8n_pack/03_Policies/02_Policy_N8N_Prototipo_para_Codigo.md
created_for: CKOS_DOCUMENTATION_REVIEWED
---

# CKOS Infra Automation Memory

## Refresh 2026-05-26

Esta memoria classifica DigitalOcean/n8n como insumo auxiliar de planejamento, nao como runtime canonico.

- n8n nao e core CKOS.
- DigitalOcean/n8n nao autorizam backend, migrations, banco, APIs, agentes reais ou automacoes runtime nesta fase.
- JSONs n8n sao prototipos revisaveis, nao implementacao aprovada.
- Billing, credits, wallet, PII, secrets e multi-tenant exigem security, audit, tests, approvals e runtime/data model canonicos antes de qualquer uso real.
- Docs 21-24 Business Systems ja existem; nao recriar.
- Docs 25-30 nao devem ser criados sem autorizacao Founder.
- `../CKOS_FILETREE_MAP.md` registra o estado completo do vault e conflitos de numeracao.

## Resumo da decisao DigitalOcean

O pack define DigitalOcean como escolha PMO inicial para runway, VPS e validacao de receita. A tese e nascer pequeno, provar valor, capturar receita e fazer a infraestrutura se pagar. Credito inicial deve ser tratado como runway estrategico, nao como permissao para gastar sem controle.

## O que e decisao temporaria

- Usar DigitalOcean como ambiente inicial enxuto.
- Usar VPS/servicos basicos para validar proposta, automacoes e operacao.
- Usar n8n como acelerador de prototipos, backoffice e integracoes nao criticas.
- Usar JSONs de n8n como base revisavel, nao como runtime canonico.

## O que e arquitetura futura

- Runtime proprio do CKOS.
- Event bus proprio.
- Policy engine propria.
- Model router proprio.
- Agent orchestration propria.
- Collector runner proprio.
- Cost ledger e credit ledger governados por codigo e banco.
- Observabilidade, evals e audit trail versionados.

## Onde n8n ajuda

- Prototipar webhooks e integracoes.
- Testar captura de leads e proposta inicial.
- Rodar automacoes internas e alertas.
- Fazer sync operacional de arquivos/knowledge.
- Apoiar suporte, observabilidade e handoffs em baixa criticidade.
- Validar demanda antes de promover fluxo para codigo proprio.

## Onde n8n vira risco

- Pagamentos, creditos e wallet.
- Dados sensiveis, PII, secrets e isolamento multi-tenant.
- Fluxos de alta frequencia.
- Experiencia principal do cliente.
- Decisoes com impacto juridico, financeiro ou reputacional.
- Fluxos que exigem testes automatizados, versionamento forte e controle fino de erro.

## Criterios de migracao para codigo proprio

Migrar quando o fluxo:

- envolve pagamento ou credito de usuario;
- envolve dados sensiveis;
- roda muitas vezes por dia;
- afeta experiencia principal;
- precisa de teste automatizado;
- precisa de versionamento forte;
- tem impacto financeiro, juridico ou reputacional;
- precisa estar sujeito ao policy engine canonico do CKOS.

## Riscos de custo

- Credito gratis virar gasto improdutivo sem ROI.
- Automacoes n8n consumirem modelos caros sem budget gate.
- Falta de custo por agente/modelo/tool/collector.
- Infra subir antes de haver planos, billing e credit policies consolidadas.
- Falta de alertas de overage, reservas e bloqueios preventivos.

## Riscos de vendor lock-in

- Workflows essenciais presos em JSON de n8n.
- Dependencia operacional de DigitalOcean sem plano de portabilidade.
- Uso de APIs externas sem abstrair provider, secrets e collectors.
- Automacoes de negocio ficarem fora do event bus e audit trail do CKOS.

## Relacao com creditos, planos e ROI

Infra e automacao devem ser governadas pelos sistemas 21 e 24:

- ROI mede se infra e agentes geram retorno.
- Credits/Billing define consumo, reserva, limite e bloqueio.
- Cost control impede que experimentos virem passivo.
- Budget gates devem existir antes de runs caros.

## Recomendacoes para VPS, workers, filas e automacoes

- Comecar com VPS enxuta e observabilidade minima obrigatoria.
- Separar processos por responsabilidade: app/runtime futuro, workers, n8n auxiliar, banco/cache quando aplicavel.
- Usar filas para jobs de collectors, RAG, processamento de arquivos e runs demorados.
- Registrar cada automacao n8n como prototipo com owner, risco, custo estimado, criterio de migracao e dependencia.
- Nunca expor tokens, providers ou actor_id no frontend.
- Nunca tratar n8n como core definitivo do CKOS.
