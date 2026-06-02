---
title: Multi-Session Control Room Runbook
file: 01_MULTI_SESSION_CONTROL_ROOM_RUNBOOK.md
layer: auxiliary
doc_type: pmo_runbook
phase: 000_ROADMAPS
category: consolidation
status: draft
version: 1.1.0
created_at: 2026-06-01
updated_at: 2026-06-02
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - founder
  - metacognik
approval_required:
  - founder
  - pmo_ckos
confidence: medium
provenance_status: pmo_synthesis_unverified
source_tool: claude_opus_4_8
purpose: Operacionalizar o Control Room multi-modelo no estado pos-Docs 26/27 e pos-GATE 1, com 3 Claude Code + 2 Codex + 1 Windsurf em paralelo, Antigravity sob gate de design_study, Founder fora do caminho critico e geracao automatica de prompts/BRA.
intelligence_level: high
non_authority_boundary: >
  Runbook auxiliar/operacional. Stage 0 = markdown + disciplina, SEM backend, queue,
  event bus ou webhook real. Nenhuma convencao aqui concede autoridade de escrita;
  autoridade vem de SESSION_REGISTRY, lock ativo ou aprovacao Founder/PMO. Nao cria
  docs canonicos, nao implementa.
related_notes:
  - ../../000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/26_LOCAL_PMO_MULTI_MODEL_CONTROL_ROOM_STUDY.md
  - ../../000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/25_LOCAL_OPERATOR_CONTROL_ROOM_AND_AUTONOMOUS_DISPATCH_STUDY.md
  - ../../000_STUDY_NOTES/13_AI_FIRST_PROJECT_OPERATING_SYSTEM/21_BRA_BRIEFING_RELAY_ARCHITECTURE_STUDY.md
  - ../MULTI_SESSION_EXECUTION_POLICY.md
  - ../SESSION_REGISTRY.md
tags: [runbook, multi-session, control-room, bra, dispatch, pmo]
---

# Runbook — Control Room Multi-Modelo (Stage 0)

> **Objetivo:** você opera **decidindo**, não roteando. As sessões rodam em paralelo;
> um **Dispatcher** (Windsurf ou 1 sessão Claude dedicada) gera os prompts e BRA por você.
> Isto remove o **relay manual via ChatGPT** do caminho crítico (gargalo diagnosticado na Note 26 §2).
> **Stage 0 = markdown + disciplina. Zero backend.**

---

## 1. Layout das 6 sessões + Antigravity gated + você

| Slot | Surface | Papel | Modo padrão | Escreve? |
|---|---|---|---|---|
| 1 | **Claude Code #1** | **Dispatcher / Prompt-Engineer / fan-in** - lê registry, gera prompts e consolida releases | `planning` / `audit` | só arquivos de controle quando houver lock |
| 2 | **Claude Code #2** | Auditor de arquitetura / canonical-readiness | `audit` | não |
| 3 | **Claude Code #3** | Auditor de Study Layer / consolidação | `audit` | não |
| 4 | **Codex #1** | Escritor primário em checkout fechado | `execution` / `study` / `canonical_patch` | sim, só no lock |
| 5 | **Codex #2** | Escritor paralelo em escopo não-overlap | `execution` / `study` / `canonical_patch` | sim, só em lock disjunto |
| 6 | **Windsurf** | PMO local de suporte e dispatch operacional | `planning` / coordenação auxiliar | só controle quando autorizado |
| gated | **Antigravity** | Design study / protótipo visual isolado | `design_study` | somente estudo visual sob gate Founder |
| — | **Você (Founder)** | Decide. Aprova lotes. Não roteia. | decisão | autoridade |

> **Nota sobre seu pedido nº1:** o "Claude que faz a própria engenharia de prompt de cada tarefa/BRA" = **Slot 1 (Dispatcher)**. Ele lê o vault e produz prompts prontos para colar nos Slots 2-5. É o que substitui você como roteador.

Regra curta (Note 26 §4): **Codex escreve. Claude audita. Dispatcher prepara prompts. Você decide. Nenhuma identidade dá permissão; o lock e o Founder dão.**

### 1a. Mapa de ferramentas vigente

Base: Doc 19 ANTIGRAVITY §4.1-4.3 para Claude Code, Codex e Antigravity; Note 26 para Windsurf como PMO local auxiliar.

| Ferramenta | Uso ideal | Limite operacional |
|---|---|---|
| **Claude Code** | Contexto extenso, revisão arquitetural, planejamento, patches documentais, síntese de decisões, `ARCHITECTURE_QUESTION`, QA de outras ferramentas. | Pode superproduzir se o prompt for aberto; não decide produto; não executa produção; deve devolver opções, trade-offs e fan-in. |
| **Codex #1** | Executor primário para diffs focados, arquivos específicos, patches planejados, testes e tarefas com scope contract fechado. | Degrada com contexto ambíguo; não resolve arquitetura aberta; não compartilha arquivo-alvo com Codex #2. |
| **Codex #2** | Executor simultâneo possível para patch auxiliar, reconciliação ou verificação em arquivo disjunto. | Só opera com lock próprio, allowed_scope explícito e zero overlap de escrita com Codex #1. |
| **Windsurf** | PMO local de suporte: lê contexto, checa locks, prepara/cola prompts, verifica BRA e dependências. | Recomenda e organiza; não canoniza, não abre gate e não substitui Founder/PMO/Metacognik. |
| **Antigravity** | Protótipo visual isolado, exploração de interação, layout, design tokens e fluxo com dados mock. | Bloqueado fora de `design_study` aprovado; não cria backend, auth, provider calls, schema, runtime, pricing ou regra de negócio. |

---

## 2. O ciclo (pseudo-webhook por markdown)

```txt
1. Você aprova um LOTE (5-10 tarefas) uma vez.            ← único ponto de contato obrigatório
2. Dispatcher lê SESSION_REGISTRY + ck_tasks + notas.
3. Dispatcher gera 1 prompt scoped por sessão (Seções 5).
4. Você cola cada prompt na sua sessão (ou Windsurf cola).
5. Sessão roda, emite CHECKOUT RELEASE + BRA Packet.
6. Dispatcher valida release, atualiza registry, identifica quem "assina" (depende).
7. Fan-in: Claude auditor consolida; Dispatcher propõe próximo lote.
8. Você só reaparece para: aprovar lote, gate canônico, risco acima do teto.
```

**Estado compartilhado = `SESSION_REGISTRY.md`.** Se não está no registry, o evento não aconteceu.

### 2a. Protocolo fan-in padrão atual

O ciclo operacional vigente é:

```txt
Codex executa -> cola release aqui -> Claude faz fan-in -> próximo prompt
```

1. Codex #1 ou Codex #2 executa uma sessão com checkout lock e escopo fechado.
2. A sessão emite `CHECKOUT RELEASE` com files_changed, validation, risks_remaining, next_step e status.
3. O release é colado no Control Room/Dispatcher.
4. Claude faz fan-in: confere registry, lock, release, dependências e fronteiras proibidas.
5. Claude devolve o próximo prompt scoped; Founder só entra se houver gate, risco acima do teto ou decisão real.

Sem release colado e fan-in lido, não existe próximo prompt dependente.

---

## 3. Como você sai do caminho crítico (regra dos 3 contatos)

Você só precisa tocar o sistema em **3 momentos**:

1. **Início do lote** — aprovar as próximas 5-10 tarefas como batch limitado (template Seção 6).
2. **Gate canônico** — abrir doc 28+, promover study→canônico, ativar Antigravity, aceitar risco acima do teto.
3. **Fan-in** — aceitar/rejeitar a síntese consolidada antes do próximo lote.

Tudo entre esses pontos é mecânico e roda sem você. Se uma sessão precisar de decisão fora desses 3, ela **espera** (Seção 4), não te interrompe item a item.

---

## 4. Regras de espera / paralelo / conflito (Note 26 §8-9, §12)

**Pode rodar em paralelo:** múltiplos read-only sobre os mesmos arquivos; 1 Codex escrevendo em lock + outras read-only; Codex #2 em arquivo não-overlap após escopo PMO.

**Deve esperar:** outra sessão tem lock do mesmo arquivo; auditoria requerida ainda não liberada; BRA referencia output inexistente; decisão do Founder pendente; numeração de arquivo em conflito.

**Pilha de prioridade em conflito:**
```txt
Decisão explícita do Founder
  > docs canônicos aprovados
  > lock de checkout ativo
  > decisão de risco PMO/Metacognik
  > último release válido
  > BRA Packet
  > memória de chat
  > inferência de agente
```

**Anti-conflito de escrita:** um arquivo, um escritor. Codex #1 e #2 nunca compartilham arquivo-alvo sem BRA + escopo PMO. Dispatcher recusa gerar prompt que colida com lock ativo.

---

## 5. Templates de prompt (o Dispatcher preenche e te entrega)

Todo prompt começa com o **preâmbulo de guardrail** (Note 26 §11):

```txt
You are a CKOS session under MULTI_SESSION_EXECUTION_POLICY.
- Fonte de verdade aprovada = canônico 01-28 (GATE 3 ✅ 2026-06-02); docs 29-34 gated.
- Não edite docs canônicos 01-28 nem crie docs 29-34 sem checkout/gate explícito.
- Não atualize ARCHITECTURE_PATCH_REPORT.md nem 00_SYSTEM_GOVERNANCE/*.
- Não crie backend, UI, API, migrations, n8n JSONs, agentes runtime, automações.
- read-only = só findings. patch study-only = só o arquivo permitido + CHECKOUT RELEASE.
- Study recomenda, nunca governa. Roadmap sequencia, nunca substitui canônico.
```

### 5a. Codex (escritor)
```txt
[GUARDRAIL]
ROLE: Codex executor (patch study-only). SESSION: S-P1-XX-CODEX-[data]-[seq].
READ FIRST: [arquivos exatos]
ALLOWED TO WRITE: [1 caminho dentro do lock]
FORBIDDEN: docs 01-27, docs 28-34, governance, patch report, qualquer arquivo com lock ativo.
TASK: [1 tarefa scoped]
CLOSE WITH: CHECKOUT RELEASE (files_created, files_changed, files_not_touched, validation, risks_remaining, next_step, status).
```

### 5b. Claude (auditor)
```txt
[GUARDRAIL]
ROLE: Claude Code auditor (read-only). SESSION: S-P1-XX-CLAUDE-[data]-[seq].
READ: [arquivos]
AUDIT GOAL: [coerência | readiness | ghosts | ROI | consolidação]
RETURN: veredito; findings por severidade; open questions; patch_candidates (rotulados, não aplicados); blocked; próxima sessão PMO.
CLOSE WITH: CHECKOUT RELEASE (files_changed: none, status: released).
```

### 5c. Dispatcher (Claude #1) — meta-prompt que VOCÊ cola uma vez por lote
```txt
[GUARDRAIL]
ROLE: Dispatcher / PMO local. MODE: coordenação.
READ: SESSION_REGISTRY.md, 000_ROADMAPS/TASK_KANBAN.md, ck_tasks.md, ck_memory.md,
      000_ROADMAPS/22_CONSOLIDATION/00_CKOS_CONSOLIDATION_MAP_AND_GAP_AUDIT.md.
TASK:
  1. Liste o estado atual (locks ativos, releases recentes, próximo do backlog).
  2. Selecione as próximas N tarefas não-overlapping (N = tamanho do lote aprovado).
  3. Para cada uma, gere 1 prompt pronto (template 5a/5b) com escopo allowed/forbidden.
  4. Marque dependências e ordem; sinalize o que precisa esperar.
  5. Proponha as entradas de SESSION_REGISTRY (não aplique).
OUTPUT: bloco de prompts prontos para colar + tabela de dispatch + o que exige decisão sua.
FORBIDDEN: abrir doc canônico, aprovar canon, sobrescrever registry, implementar.
```

---

## 6. Session types vigentes

Fonte: `000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md` v1.0.0.

| session_type | Uso no Control Room | Escrita |
|---|---|---|
| `planning` | Preparar sequência, escopo, custos, riscos e handoff. | auxiliar somente com lock |
| `audit` | Revisar consistência, riscos, YAML, forbidden actions e release. | findings; sem patch no alvo auditado |
| `execution` | Aplicar patch auxiliar aprovado em escopo travado. | só arquivos no checkout lock |
| `study` | Criar ou ajustar material não-canônico de estudo. | `000_STUDY_NOTES/` quando autorizado |
| `research` | Reunir evidência sem canonizar. | pesquisa/estudo auxiliar quando autorizado |
| `design_study` | Estudar direção visual/produto sem implementar. | estudo visual sob gate Founder |
| `memory_refresh` | Atualizar mapas, memória e estado operacional. | memória/mapas auxiliares com lock |
| `patch_candidate` | Preparar candidato não-canônico para patch futuro. | pasta candidata autorizada |
| `canonical_patch` | Aplicar patch canônico aprovado em checkout separado. | somente arquivos canônicos/traceabilidade explicitamente permitidos |

Aliases antigos deste runbook: `read-only audit` agora deve ser registrado como `audit`; `patch study-only` deve ser registrado como `study` ou `execution` conforme o arquivo-alvo; qualquer patch canônico continua exigindo `canonical_patch` e gate separado.

## 7. Template de aprovação de lote (você preenche 1x)

```txt
LOTE APROVADO #[n] — [data]
Tarefas (5-10): [ids do backlog único]
Teto de risco: [baixo | médio]   (acima disso = me consultar)
Modos permitidos: [planning | audit | execution | study | research | design_study | memory_refresh | patch_candidate | canonical_patch]
Arquivos proibidos: docs 01-28, docs 29-34 sem gate, governance, patch report, backend/UI/API
Reviewers: PMO + Metacognik no fan-in
Expira em: [data]
```

---

## 8. "SESSÃO FINALIZADA" (Note 26 §14)

Dizer "pronto" no chat **não** é encerramento. Só conta com:
```txt
CHECKOUT RELEASE emitido
+ registry atualizado (ou update proposto ao Dispatcher)
+ lock liberado
+ next_step declarado
+ status (released | released_with_required_external_audit | blocked | cancelled)
```
O Dispatcher **não** gera prompt dependente enquanto a sessão de origem não estiver `SESSÃO FINALIZADA`.

---

## 9. Kanban de relance (espelho de ck_tasks, não runtime)

```txt
NOW (ativo, lock)   | quem | lock_id | release esperado
WAITING (depende)   | espera_de | motivo
READY (sem lock)    | modo | escopo
FOUNDER DECISION    | decisão | impacto
DONE (released)     | release_id | status
```
Entra em NOW só com lock; sai só com release; chega em DONE só com SESSÃO FINALIZADA.

---

## 10. Fases F0-F7 e gates atuais

Fonte operacional: `CKOS_MASTER_EXPANSION_ROADMAP.md` + registros recentes em `SESSION_REGISTRY.md`.

| Fase | Leitura operacional no Control Room |
|---|---|
| **F0 Convergência Documental** | Fase atual dos gates. GATE 1 está concluído por fan-in/patches registrados; GATE 3 está em execução; GATE 4 é este runbook; GATE 5 prepara Backend MVP thin-slice. |
| **F1 Runtime Cognitivo MVP** | Só abre depois do GATE 5; este runbook não autoriza backend, API, database, migrations ou runtime. |
| **F2 Agentes & Skills** | Pode gerar estudos, audits e patch candidates; runtime de agentes fica bloqueado até gate próprio. |
| **F3 Motor de DNA** | Pode ser referenciado para fan-in e backlog; não altera Creative DNA canônico sem checkout separado. |
| **F4 Superfícies de Produto** | Antigravity pode estudar visualmente sob `design_study`; UI real segue bloqueada. |
| **F5 Conectores & Integrações** | Doc 26 governa conectores/MCP; Control Room não cria MCP, webhook, n8n ou providers. |
| **F6 Autonomia & Auto-Evolução** | Approval batches e heartbeat são candidatos/processo; autonomia runtime não é presumida. |
| **F7 Negócio & Escala** | ROI/billing/marketplace permanecem referências futuras; sem decisão de produto neste runbook. |

Gate snapshot atual:

```txt
GATE 1: concluído / fan-in registrado
GATE 3: em execução (Doc 28 / Notes-RAG-Knowledge)
GATE 4: este runbook, Control Room operacional auxiliar
GATE 5: Backend MVP thin-slice, ainda futuro e dependente de gate
```

`ARCHITECTURE_QUESTION`: nenhuma decisão de produto nova foi tomada nesta revisão. Se o fan-in identificar escolha de produto, custo, risco ou governança, ela deve sair como `ARCHITECTURE_QUESTION` separada.

---

## 11. Quando isto vira backend (e quando NÃO)

```txt
Stage 0 (este runbook): markdown + Dispatcher + relay humano mínimo.   ← AGORA
Stage 1: convenções mais rígidas (bra_id estável, lint de locks).
Stage 2: padrões auditados viram candidatos a Doc 28/29+ (só após gate).
Stage 3 (NÃO agora): queue/event/store reais, agentes runtime, automações.
         Exige gates dos Docs 10/11/12 + aprovação Founder/PMO/Metacognik + técnica.
```

O Control Room **não** abre Doc 28/29+ nem implementa por conta própria. Ele só te dá alavancagem operacional imediata enquanto a consolidação (arquivo 00), o DNA (arquivo 02) e o backend (arquivo 03) seguem seus próprios gates.

---

## 12. Critérios de aceitação

- Define os 6 slots principais + Antigravity gated + Founder e o Dispatcher como gerador de prompts/fan-in.
- Implementa a "regra dos 3 contatos" (você sai do caminho crítico).
- Reusa Note 26/policy sem criar autoridade nova nem backend.
- Templates de Codex/Claude/Dispatcher/lote prontos para uso.
- Registra Codex #1 e Codex #2 como executores simultâneos possíveis, desde que com locks disjuntos.
- Atualiza session types para a policy vigente.
- Amarra F0-F7 aos gates atuais sem alterar roadmap/kanban.
- Subordinado a SESSION_REGISTRY, policy e gate do Founder.

---

## 13. Changelog

### v1.1.0 - 2026-06-02

- Bump operacional do handoff GATE 4: `1.0.0 -> 1.1.0`.
- Atualizado para estado pós-Docs 26/27 e pós-GATE 1.
- Adicionado mapa de ferramentas com Claude Code, Codex #1, Codex #2, Windsurf e Antigravity.
- Adicionado protocolo fan-in padrão: `Codex executa -> cola release aqui -> Claude faz fan-in -> próximo prompt`.
- Atualizados session types para a `MULTI_SESSION_EXECUTION_POLICY`.
- Adicionado snapshot F0-F7 com GATE 1 concluído, GATE 3 em execução, GATE 4 neste runbook e GATE 5 como Backend MVP futuro.
