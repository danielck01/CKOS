---
title: Master Map
file: 00_MASTER_MAP.md
phase: 00_SYSTEM_GOVERNANCE
category: governance
version: 2.6.0
status: active
owner: PMO_CKOS
responsible_agent: PMO_CKOS
reviewers:
  - metacognik
approval_required:
  - founder
purpose: Mapa mestre da documentação CKOS — camadas RAW/STUDY/CANONICAL, árvore canônica, docs canônicos vs auxiliares, ordem de leitura/implementação e gates.
inputs: Árvore normalizada pós-auditoria; naming freeze; Runtime; Business Systems; Evolution System.
outputs: Mapa completo; ordem oficial; gates de fase; status de fase; bloqueios.
framework: RAW/STUDY/CANONICAL + fases canonicas — Governance, Thinking, Execution, Runtime, Product, Implementation, Business Systems, Evolution System.
edge_cases: Doc duplicando outro; prompt como skill; dashboard fixo; agente sem skill; protótipo confundido com produto.
integrations: Indexa toda a árvore CKOS_DOCUMENTATION_REVIEWED.
prompts: Prompt de classificação de novo documento.
metrics: 100% docs na hierarquia; 0 docs fora de fase; redução de retrabalho.
related_notes:
  - 00_DOCUMENT_TEMPLATE.md
  - 00_TAXONOMY_AND_NAMING.md
  - 00_DEPENDENCY_MAP.md
  - ../CKOS_FILETREE_MAP.md
document_layers: "RAW -> STUDY -> CANONICAL"
tags: [governance, master_map, index, phases, gates]
last_refresh: 2026-05-27
---

# 0. Refresh documental 2026-05-26

Este bloco registra o estado operacional atual do vault sem renumerar, mover ou promover arquivos automaticamente. Se houver conflito entre este bloco e secoes historicas abaixo, este bloco prevalece ate um patch taxonomico aprovado pelo Founder.

## 0.1 Estado atual confirmado

- Docs 21-24 Business Systems existem em `06_BUSINESS_SYSTEMS/`.
- `ARCHITECTURE_PATCH_REPORT.md` v1.7.0 registra Business Systems 21-24 e Gate I completo.
- Gate I esta documentalmente completo, mas ainda requer aprovacao formal Founder + Technical + Metacognik.
- Docs 26, 27 e 28 existem em `07_EVOLUTION_SYSTEM/`: Connectors/MCP/Integrations, AI-first Work Orders/Multi-Session Orchestration e Notes/RAG/Knowledge Architecture.
- Implementacao permanece bloqueada.
- Docs 29-34 nao devem ser criados sem autorizacao explicita do Founder e decisao de taxonomia (Doc 28 criado via GATE 3, 2026-06-02).
- UI/UX implementation, backend, migrations, agentes reais, APIs, banco de dados e automacoes runtime nao devem ser iniciados nesta fase.
- Arquivos nao devem ser movidos, deletados, renomeados ou renumerados sem relatorio previo.
- n8n deve permanecer como acelerador/prototipo auxiliar, nao como core CKOS.
- Manus deve permanecer como ferramenta temporaria de pesquisa/bootstrap, nao infraestrutura definitiva do CKOS.
- `000_UPLOADS/` e `000_STUDY_NOTES/` existem e foram reconhecidas como camadas auxiliares formais de governanca de conhecimento.
- `000_UPLOADS/` e zona RAW de ingestao; `000_STUDY_NOTES/` e zona STUDY de interpretacao.
- Nenhuma das duas e documentacao canonica.
- RAW -> STUDY -> CANONICAL e o fluxo oficial de promocao de conhecimento.
- Nada entra no canonico sem passar por STUDY, patch plan aprovado, QA documental e registro no `ARCHITECTURE_PATCH_REPORT.md`.

## 0.2 Estrutura observada no refresh

```txt
CKOS_DOCUMENTATION_REVIEWED/
|-- 000_UPLOADS/
|-- 000_STUDY_NOTES/
|-- 00_SYSTEM_GOVERNANCE/
|-- 01_THINKING_SYSTEM/
|-- 02_EXECUTION_SYSTEM/
|-- 03_RUNTIME_SYSTEM/
|-- 04_PRODUCT_SYSTEM/
|-- 05_IMPLEMENTATION_SYSTEM/
|-- 06_BUSINESS_SYSTEMS/
|-- 07_EVOLUTION_SYSTEM/
|-- 000_UPGRADE/
|-- ARCHITECTURE_PATCH_REPORT.md
|-- QA_DOCUMENTATION_CHECKLIST.md
|-- CKOS_FOLDER_MEMORY.md
|-- CKOS_FILETREE_MAP.md
`-- CKOS_VAULT_MAP_REFRESH_REPORT.md
```

## 0.3 Canonicos confirmados no refresh

- Governance/Thinking/Execution/Runtime/Product docs 00-16 permanecem fonte canonica de arquitetura.
- Implementation docs canonicos atuais: `17_IMPLEMENTATION_PROTOCOL.md`, `18_RESEARCH_PROTOCOL.md`, `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`, `20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md`.
- Business Systems canonicos atuais: `21_ROI_ARCHITECTURE.md`, `22_FEEDBACK_SYSTEM_ARCHITECTURE.md`, `23_SUPPORT_SYSTEM_ARCHITECTURE.md`, `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md`.

## 0.4 Auxiliares e historicos

- `000_UPGRADE/` e area auxiliar de continuidade, research, infra temporaria, n8n e memoria operacional.
- `000_UPLOADS/` e zona de ingestao RAW. Recebe insumos brutos, pesquisas, outputs de IA, prints, PDFs, CSVs, benchmarks, referencias, exports, transcricoes e materiais de cliente. Nao tem autoridade canonica.
- `000_STUDY_NOTES/` e zona de interpretacao STUDY. Transforma RAW em notas estudaveis com provenance, confidence, riscos, hipoteses, lacunas, recomendacoes PMO e possiveis patch candidates. Nao e canonica.
- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md` e variante historica/legada e nao define Manus como infra CKOS.
- `05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md` e protocolo anterior, provavelmente superseded pelo protocolo com Antigravity.
- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` foi preservado como historico/superseded.
- A arquitetura canonica Self-Evolving agora vive em `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`.

## 0.5 Conflito de numeracao registrado

Conflito critico:

- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` (superseded/historico)
- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md`
- `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`

Opcoes futuras, sem execucao neste refresh:

- Decisao aplicada: Self-Evolving foi recriado como `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`, sem mover ou deletar o arquivo antigo.
- Opcao B: manter Self-Evolving como auxiliar/historico.
- Opcao C: criar uma categoria futura de Evolution/Learning System, com patch de taxonomia.

Recomendacao PMO: preferir Opcao A apenas apos aprovacao formal e busca completa de referencias.

## 0.6 Camadas documentais reconhecidas em 2026-05-27

O vault agora opera com tres camadas documentais:

```txt
RAW / 000_UPLOADS
  -> material bruto, sem autoridade canonica
  -> exige provenance antes de qualquer uso

STUDY / 000_STUDY_NOTES
  -> interpretacao, source manifests, study notes, decision logs e patch candidates
  -> pode recomendar patch, mas nao altera docs oficiais

CANONICAL / docs versionados
  -> docs oficiais 00-24 atuais e docs futuros aprovados
  -> so muda por patch plan, aprovacao humana, QA documental e patch report
```

Regra principal: nenhum material externo, output de IA, export de conector, benchmark, print, PDF, CSV ou referencia visual entra em documento canonico sem passar por STUDY.

`000_UPGRADE/` nao e camada oficial de ingestao. Permanece como zona auxiliar de continuidade, pacotes, memorias, transicao e propostas. Material em `000_UPGRADE/` tambem deve passar por STUDY antes de qualquer canonizacao.

# 1. Propósito

Definir o mapa mestre da documentação do CKOS AI First, travando hierarquia, ordem de criação, função de cada fase, dependências e gates mínimos para evitar entropia documental, técnica e estratégica.

Versão `2.0.0`: introduz a fase **03_RUNTIME_SYSTEM** (antes ausente) e renumera Product (14–16) e Implementation (17–21).

# 2. Função dentro do CKOS

Índice executivo e operacional. Responde o que existe, em que ordem deve ser criado/lido, o que bloqueia o quê e quando uma ideia vira documento oficial.

# 3. Inputs

- árvore normalizada pós-auditoria (2026-05-24);
- naming freeze (`00_TAXONOMY_AND_NAMING`);
- necessidade de Runtime, Data Model, Security e Evals antes de qualquer produto/backend.

# 4. Outputs

- mapa completo da documentação;
- ordem oficial de geração e leitura;
- gates de aprovação por fase;
- status de cada fase;
- bloqueios de implementação.

# 5. Framework operacional

```txt
000_UPLOADS              -> RAW: entrada bruta sem autoridade canonica
000_STUDY_NOTES          -> STUDY: interpretacao, manifests, decisions e patch candidates
00_SYSTEM_GOVERNANCE     → organiza a documentação
01_THINKING_SYSTEM       → define pensamento, objetos, agentes, autonomia e memória (conceitual)
02_EXECUTION_SYSTEM      → define skills, workflows, prompts e transformers
03_RUNTIME_SYSTEM        → define runtime, registries, engines, state machines, dados, segurança, evals, custos, replay e approval gates (executável)
04_PRODUCT_SYSTEM        → projeta runtime em dashboard, command center e node canvas
05_IMPLEMENTATION_SYSTEM → define pesquisa, execução, QA, founder approval e self-evolving
```

Princípio: **Thinking define o quê. Execution define a capacidade. Runtime define como executa. Product projeta. Implementation constrói.** Product e Implementation são *projeção* e *construção* sobre o Runtime — nunca fonte de verdade.

## 5.1 Complemento Evolution System 2026-05-27

`06_BUSINESS_SYSTEMS` define ROI, feedback, suporte, creditos, planos e billing.

`07_EVOLUTION_SYSTEM` define evolucao segura, learning loops, sandbox, approval, rollback, capability evolution, connectors/MCP/integrations, Work Orders and multi-session orchestration.

Self-Evolving ativo e `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`. O arquivo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` esta preservado como superseded/historico. ROI permanece doc 21.

# 6. Estrutura oficial (canônica)

```txt
CKOS_DOCUMENTATION_REVIEWED/
├── 000_UPLOADS/                                (RAW auxiliar, nao canonico)
│   ├── 00_UPLOADS_INDEX.md
│   ├── README.md
│   └── _folder_memory.md
│
├── 000_STUDY_NOTES/                            (STUDY auxiliar, nao canonico)
│   ├── 00_STUDY_INDEX.md
│   ├── README.md
│   ├── _folder_memory.md
│   └── _templates/
│
├── 00_SYSTEM_GOVERNANCE/
│   ├── 00_README_SYSTEM_GOVERNANCE.md      (auxiliar)
│   ├── 00_MASTER_MAP.md
│   ├── 00_DOCUMENT_TEMPLATE.md
│   ├── 00_TAXONOMY_AND_NAMING.md
│   └── 00_DEPENDENCY_MAP.md
│
├── 01_THINKING_SYSTEM/
│   ├── 00_README_THINKING_SYSTEM.md        (auxiliar)
│   ├── 01_CKOS_AI_FIRST_CONSTITUTION.md
│   ├── 02_AI_FIRST_OBJECT_MODEL.md
│   ├── 03_AGENT_OPERATING_MODEL.md
│   ├── 04_AUTONOMY_AND_APPROVALS.md
│   └── 05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
│
├── 02_EXECUTION_SYSTEM/
│   ├── 00_README_EXECUTION_SYSTEM.md        (auxiliar)
│   ├── 06_SKILLS_REGISTRY.md
│   ├── 07_WORKFLOW_BLUEPRINTS.md
│   ├── 08_PROMPT_LIBRARY.md
│   └── 09_TRANSFORMERS_AND_PIPELINES.md
│
├── 03_RUNTIME_SYSTEM/                        ← NOVA FASE
│   ├── 00_README_RUNTIME_SYSTEM.md          (auxiliar)
│   ├── 10_SYSTEM_RUNTIME_ARCHITECTURE.md
│   ├── 11_DATA_MODEL_AND_PERSISTENCE.md
│   ├── 12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
│   └── 13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
│
├── 04_PRODUCT_SYSTEM/
│   ├── 00_README_PRODUCT_SYSTEM.md          (auxiliar)
│   ├── 14_PROJECT_DASHBOARD_ARCHITECTURE.md
│   ├── 15_COMMAND_CENTER_ARCHITECTURE.md
│   └── 16_NODE_CANVAS_ARCHITECTURE.md
│
└── 05_IMPLEMENTATION_SYSTEM/
    ├── 00_README_IMPLEMENTATION_SYSTEM.md   (auxiliar)
    ├── 17_IMPLEMENTATION_PROTOCOL.md
    ├── 18_RESEARCH_PROTOCOL.md (supersedes: 18_RESEARCH_PROTOCOL_FOR_MANUS.md — preserved as historical/legacy)
    ├── 19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md (supersedes: 19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md — preserved as historical/legacy)
    ├── 20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md
    └── 21_SELF_EVOLVING_SYSTEM.md             (superseded/historico)
│
└── 07_EVOLUTION_SYSTEM/
    ├── 00_README_EVOLUTION_SYSTEM.md          (auxiliar)
    ├── 25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md
    ├── 26_CONNECTORS_MCP_AND_INTEGRATIONS_ARCHITECTURE.md
    ├── 27_AI_FIRST_WORK_ORDERS_AND_MULTI_SESSION_ORCHESTRATION_ARCHITECTURE.md
    └── 28_NOTES_RAG_AND_KNOWLEDGE_ARCHITECTURE.md
```

Docs canônicos numerados: **00 (×4) + 01–28 = 32 canônicos**, considerando que o antigo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` foi preservado como histórico/superseded e que `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md` permanece o doc 21 ativo. READMEs são auxiliares de navegação, não contam como canônicos.

Nota de refresh 2026-05-27: o conflito de numeracao foi resolvido por decisao Founder. `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md` permanece como doc 21. Self-Evolving ativo agora e `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`. O arquivo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` permanece preservado como material historico/superseded.

# 7. Ordem oficial de geração/leitura

Fluxo de promocao de conhecimento: `000_UPLOADS` -> `000_STUDY_NOTES` -> patch plan aprovado -> docs canonicos versionados.

```txt
00_MASTER_MAP → 00_DOCUMENT_TEMPLATE → 00_TAXONOMY_AND_NAMING → 00_DEPENDENCY_MAP
01 → 02 → 03 → 04 → 05 → 06 → 07    (01..28 na ordem numérica ativa)
```

# 8. Gates de fase

| Fase | Aprovada quando | Status atual |
|---|---|---|
| 00 Governance | hierarquia, template, taxonomia e dependências claros | **active** |
| 01 Thinking | CKOS separado de chatbot/dashboard, agentes com função, autonomia com limites, memória com arquitetura | **active** (pós-naming) |
| 02 Execution | skills, workflows, prompts e transformers com inputs/outputs/métricas | **active** (pós-naming) |
| 03 Runtime | runtime, registries, engines, state machines, dados, segurança, evals, custos, replay e approval gates especificados e aprovados | **draft — em revisão** |
| 04 Product | dashboard adaptativo, command center operacional, canvas com objetos reais, dependente de Runtime | **draft — depende de 03** |
| 05 Implementation | ferramentas obedecem protocolo, QA obrigatório, founder aprova sem microgerenciar | **draft — depende de 03** |
| 06 Business Systems | ROI, feedback, support, credits, plans e billing documentados | **documentalmente completo — implementação bloqueada** |
| 07 Evolution System | Self-Evolving governado por sandbox, eval, policy, approval, rollback, audit log, conectores, MCP, integracoes governadas, Work Orders, orquestracao multi-sessao, notas/RAG/conhecimento | **draft — docs 25-28 criados; docs 29-34 ainda não iniciados** |

# 9. Status do programa e bloqueio

```txt
FASE ATUAL: documentação arquitetural (RAW/STUDY reconhecido; Business Systems 21-24 completo; Evolution System doc 25 criado em draft).
IMPLEMENTAÇÃO DE PRODUTO/BACKEND: BLOQUEADA.
DESBLOQUEIO: requer sequência documental 25-31 resolvida, QA documental e aprovação Founder/PMO/Technical/Metacognik quando aplicável.
PERMITIDO AGORA: documentação e patch plans; não iniciar UI/UX, backend, banco, API, migrations, agentes reais ou automações runtime.
```

# 10. Critérios para novo documento

Um novo documento só nasce se definir conceito central, objeto, runtime, interface, skill, workflow, regra de aprovação, protocolo, reduzir risco ou eliminar ambiguidade operacional. Caso contrário, vira seção dentro de documento existente.

# 11. Edge cases

- Documento duplicando outro: fundir.
- Prompt tratado como skill: mover para Prompt Library.
- Dashboard fixo por canal: converter em capability contextual.
- Agente sem skill/responsabilidade: rebaixar para skill ou subagent.
- Protótipo visual confundido com produto: marcar `prototype_only`.

# 12. Métricas de sucesso

- 100% dos docs seguindo template v2;
- 0 documentos fora da hierarquia;
- 0 naming proibido;
- redução de retrabalho por ambiguidade;
- decisões críticas registradas.

# 13. Agente responsável

Owner: `PMO_CKOS` · Review: `Metacognik` · Aprovação: `Founder`.

# 14. Critérios de aprovação

Aprovado quando a árvore, os docs canônicos/auxiliares, a ordem, os gates e o bloqueio de implementação estiverem claros e consistentes com `00_DEPENDENCY_MAP`.

# 15. Critérios de reprovação

Reprovado se reintroduzir Product/Implementation sem Runtime, se permitir implementação antes do gate da fase 03, ou se divergir da taxonomia.

# 16. Related notes

- [[00_DOCUMENT_TEMPLATE]]
- [[00_TAXONOMY_AND_NAMING]]
- [[00_DEPENDENCY_MAP]]
- [[10_SYSTEM_RUNTIME_ARCHITECTURE]]
