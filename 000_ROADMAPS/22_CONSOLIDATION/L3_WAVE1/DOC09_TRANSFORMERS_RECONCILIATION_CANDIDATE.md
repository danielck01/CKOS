---
title: Doc 09 Transformers Reconciliation Candidate
file: DOC09_TRANSFORMERS_RECONCILIATION_CANDIDATE.md
layer: auxiliary
doc_type: pmo_patch_candidate
phase: 000_ROADMAPS
category: consolidation
status: awaiting_founder_approval
version: 0.1.0
created_at: 2026-06-04
owner: pmo_ckos
responsible_agent: codex_2
session_id: S-P1-L3-CODEX2-20260604-001
track: TR-TRANSF
companion_of: 00_WAVE1_DISPATCH_AND_PROTOCOL.md
target_canonical: 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md
inventory_source: 000_UPGRADE/08_TRANSFORMERS (11 arq) lidos @ 2026-06-04
reviewers:
  - founder
  - metacognik
  - claude_2_auditor
approval_required:
  - founder
  - metacognik
non_authority_boundary: >
  Patch candidate. PROPOE, nao aplica. Nao edita 09_TRANSFORMERS_AND_PIPELINES.md nem
  qualquer canonico 01-28. Nao move/arquiva/deleta 000_UPGRADE/08_TRANSFORMERS.
  Nao cria backend, UI, API, SQL, runtime, agentes reais, automacoes, workflows ou
  migrations. Aplicacao exige sessao canonical_patch separada com aprovacao Founder +
  Metacognik.
tags: [consolidation, transformers, doc09, patch-candidate, l3, bra]
---

# Doc 09 - Reconciliacao de Transformers (Patch Candidate)

> **L3 Wave 1 / TR-TRANSF.** Compara `000_UPGRADE/08_TRANSFORMERS/` contra o canonico
> `02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md` e propoe apenas candidatos.
> **Modo:** `patch_candidate`. Nada e aplicado no Doc 09 por este texto.

---

## 0. Veredito em uma linha (PMO, direto)

**`UPGRADE/08` e majoritariamente scaffold repetido, nao uma biblioteca real de transform.**
O Doc 09 canonico e mais forte no pipeline, tipos, criterios de aprovacao/reprovacao e registry.
O valor aproveitavel e pequeno: **um spec card operacional minimo** e **4 candidatos de transformer**
que podem reforcar F1/Doc 27/ROI se o Founder aprovar. O resto e alias de conceitos ja cobertos.

**Resposta curta ao PMO:** ha input e output declarados, mas nao ha steps, validacao, erro,
idempotencia, fallback nem contrato I/O tipado. Portanto, nao promover o conteudo em massa.

---

## 1. Metodo + prova de uniformidade

- Lidos: template Doc 03, Doc 09 canonico, `000_UPGRADE/08_TRANSFORMERS/` (README + 10 specs) e protocolo `L3_WAVE1`.
- Comparacao feita contra Doc 09 §§5.1-5.6, criterios §§14-15 e nota `F1_RUNTIME_IO`.
- Sinal real por arquivo do UPGRADE = nome do transformer + uma frase de funcao. Input, output e exemplo sao iguais nos 10 specs.
- O README e generico: "Transformers convertem dados de um estado para outro" e "tira o briefing da conversa e leva para execucao".

### 1.1 Prova de uniformidade (diff entre 2 instancias)

Comparacao entre `intent_to_briefing.md` e `briefing_to_task.md`:

```diff
- # Transformer - intent_to_briefing
+ # Transformer - briefing_to_task

- Transforma intencao bruta em briefing operacional.
+ Transforma briefing em tarefa.
```

Todo o restante e identico:

```txt
Input: Context State; Dados brutos; Tipo de briefing; Policies aplicaveis
Output: Entidade transformada; Confianca; Lacunas; Proximas acoes
Exemplo: recebe resposta ambigua, estrutura em YAML, detecta lacunas e gera pergunta seguinte ou output operacional
```

**Conclusao:** os 10 specs nao provam logica real `input -> steps -> output`; provam um
template leve de descricao. Nao ha validacao, error-handling, idempotencia, retries, owner,
approval gate, metricas, risk level ou fallback manual.

---

## 2. Inventario comparativo

### 2.1 Modelo canonico Doc 09

| Area | Doc 09 canonico |
|---|---|
| Definicao | Transformer = peca operacional que converte estado bruto em objeto estruturado util, auditavel e acionavel. |
| Pipeline mestre | Input -> Intent Detection -> Context Retrieval -> Object Mapping -> Transformer Selection -> Agent Routing -> Skill Execution -> Partial Output -> Metacognitive Audit -> Approval Gate -> Artifact Creation -> Memory Update -> Next Best Action. |
| Tipos | Intent, Briefing, Node, Evidence, Proposal, Artifact, Memory. |
| Registry | `transformer_id`, `name`, `input_object`, `output_object`, `owner_agent`, `review_agent`, `related_skill`, `related_workflow`, `risk_level`, `approval_required`, `metrics`. |
| MVP | `intent_to_object`, `briefing_to_live_diagnostic`, `gap_to_question`, `hypothesis_to_node`, `research_to_pack`, `proposal_to_workspace`, `decision_to_memory`. |
| Gates | Aprovado se tem I/O claro, reduz trabalho humano, nao oculta risco, registra memoria, e auditavel, tem fallback manual e respeita approval gates. |

### 2.2 UPGRADE/08 (10 specs + README)

| UPGRADE/08 transformer | Funcao declarada | Mapeia para Doc 09? | Veredito |
|---|---|---|---|
| `intent_to_briefing` | intencao bruta -> briefing operacional | `intent_to_object` + `briefing_to_live_diagnostic` | ja coberto; nao duplicar F1 `Message->Intent` |
| `answer_to_context` | resposta do usuario -> contexto estruturado | parcial: Context Retrieval/Object Mapping, mas sem transformer explicito | candidato baixo/medio |
| `context_to_questions` | contexto -> perguntas adaptativas | `gap_to_question` + pipeline de briefing inteligente | ja coberto, com alias possivel |
| `briefing_to_proposal` | briefing -> proposta | tipo Proposal + pipeline proposta -> sistema | ja coberto como Proposal |
| `briefing_to_task` | briefing -> tarefa | pipeline menciona tarefa, mas nao ha MVP transformer | candidato forte para F1 S5/Doc 27 |
| `briefing_to_sprint` | briefing -> sprint | parece workflow/planning, nao transformer puro | conflito de taxonomia |
| `briefing_to_project_pack` | briefing -> pack documental de projeto | aproxima Artifact/context pack, nao existe no MVP Doc 09 | candidato medio |
| `feedback_to_learning` | feedback -> memoria e melhoria | Memory transformer + `decision_to_memory`; F1 ja citou Feedback->Memory | ja coberto; nao promover 2x |
| `output_to_roi` | output -> metrica de valor | Doc 21/metricas, mas sem transformer dedicado | candidato medio |
| `research_to_insight` | pesquisa -> insight operacional | `research_to_pack` + pipeline pesquisa tipo Manus | ja coberto |

### 2.3 Respostas diretas as perguntas do PMO

| Pergunta | Resposta |
|---|---|
| Boilerplate vs real | Boilerplate repetido. Ha funcao de 1 linha + I/O generico, mas nao ha steps, validacao, erro, idempotencia nem fallback. Diff em §1.1 prova que so nome e funcao mudam. |
| Modelo de transformer | Doc 09 define transformer como conversor operacional de estado bruto para objeto estruturado dentro do pipeline mestre. UPGRADE/08 nao acrescenta contrato tipado completo; acrescenta apenas um spec card minimo e output envelope (`confianca`, `lacunas`, `proximas acoes`). |
| Net-new vs coberto | Net-new plausivel: `briefing_to_task`, `briefing_to_project_pack`, `output_to_roi`, talvez `answer_to_context`. Cobertos: `intent_to_briefing`, `context_to_questions`, `briefing_to_proposal`, `feedback_to_learning`, `research_to_insight`. `briefing_to_sprint` sobe como AQ. |
| Ligacao F1 | Direta: `answer_to_context` (S1/S2 context), `briefing_to_task` (S5 Work Order/task candidate), `briefing_to_project_pack` (S5 context pack/document pack), `output_to_roi` (ROI proxy). |
| Conflito de taxonomia | Sim: alguns itens parecem workflows, artifacts, task/Work Order generators ou metric extractors. Ver AQ-T09-1..4. |

---

## 3. A PROMOVER

> Promocao = entra como candidate para futuro patch no Doc 09. Aplicacao exige sessao separada.

### 3.1 Estrutural (valor real)

| ID | Item a promover | Por que e melhor que o canonico | Secao-alvo Doc 09 | Forca |
|---|---|---|---|---|
| **PROMOTE-T1** | **Transformer Spec Card minimo**: `funcao`, `input_contract`, `output_contract`, `example_usage`, `output_quality{confidence,gaps,next_actions}` | Doc 09 registry tem metadados, mas nao obriga uma ficha operacional legivel por transformer. UPGRADE/08 e fraco, mas mostra um formato simples que pode virar spec card governado se acrescido de validacao/fallback/error_policy/idempotency. | §5.5 Transformer registry + §14 criterios de aprovacao | **ALTA** |

**Observacao:** `validation`, `fallback`, `error_policy` e `idempotency_key/semantics` nao existem no UPGRADE/08; por isso entram como **lacunas obrigatorias do patch futuro**, nao como conteudo promovido da fonte.

### 3.2 Transformers candidatos

| ID | Transformer candidato | O que promover | Por que > canonico atual | Secao-alvo Doc 09 | F1 | Forca |
|---|---|---|---|---|---|---|
| **PROMOTE-T2** | `briefing_to_task` | Transformer MVP: briefing vivo -> task candidate / Work Order candidate | O pipeline fala em tarefa, mas §5.6 nao tem transformer que materializa tarefa. Liga direto ao Doc 27 sem criar schema. | §5.6 Transformers prioritarios MVP | S5 Work Order | **ALTA** |
| **PROMOTE-T3** | `briefing_to_project_pack` | Transformer especializado: briefing -> project/context pack documental | Cobre empacotamento documental antes da execucao; pode servir ao fan-out/fan-in sem backend. | §5.3 pipelines especializados ou §5.6 | S5 context pack | MEDIA |
| **PROMOTE-T4** | `output_to_roi` | Transformer de avaliacao: output/artifact -> sinal de valor/ROI proxy | Doc 09 mede sucesso, mas nao transforma output em metrica de valor. Conecta Doc 21 sem decidir formula. | §5.2 novo tipo "Value/ROI" ou §5.6 | ROI proxy | MEDIA |
| **PROMOTE-T5** | `answer_to_context` | Transformer de ingestao incremental: resposta do usuario -> context state estruturado | Doc 09 tem Context Retrieval/Object Mapping, mas nao nomeia a atualizacao incremental do contexto durante briefing. | §5.3 Briefing inteligente ou §5.6 | S1/S2 context | MEDIA-BAIXA |

**Nao promover como nome separado agora:** `intent_to_briefing` (ja e composicao de `intent_to_object` + `briefing_to_live_diagnostic`) e `feedback_to_learning` (ja coberto por Memory/`decision_to_memory` e pela nota F1_RUNTIME_IO). Promover de novo criaria duplicacao.

---

## 4. JA COBERTO (sem acao no canonico)

- **`intent_to_briefing`**: coberto por `intent_to_object` + `briefing_to_live_diagnostic`; cruza com F1 `Message->Intent`, ja tratado na nota F1_RUNTIME_IO.
- **`context_to_questions`**: coberto por `gap_to_question` e pipeline de briefing inteligente; pode virar alias, nao novo transformer.
- **`briefing_to_proposal`**: coberto pelo tipo Proposal e pelo pipeline "Proposta -> sistema".
- **`feedback_to_learning`**: coberto por Memory transformer, `decision_to_memory` e F1 `Feedback->Memory`.
- **`research_to_insight`**: coberto por `research_to_pack` e pipeline de pesquisa tipo Manus.
- **I/O generico dos 10 specs**: util como lembrete de ficha, mas insuficiente como contrato canonico.
- **Exemplo de uso repetido**: nao promove; e o mesmo texto em todos os specs.

---

## 5. CONFLITOS -> ARCHITECTURE_QUESTIONS (nao decidir aqui)

| ID | Conflito | Pergunta para Founder + Metacognik / Claude#2 Auditor |
|---|---|---|
| **AQ-T09-1** | Transformer vs workflow vs Work Order. `briefing_to_task`, `briefing_to_sprint` e `briefing_to_project_pack` podem ser transformacoes de objeto, workflows de planejamento ou materializadores de Doc 27. | Doc 09 deve registrar estes como transformers MVP, ou eles pertencem ao Doc 07/Doc 27 com apenas cross-ref no Doc 09? |
| **AQ-T09-2** | Output envelope obrigatorio. UPGRADE/08 repete `confianca`, `lacunas`, `proximas acoes` para todos os transformers. | Todo transformer CKOS deve emitir esses campos, ou apenas transformers de briefing/pergunta/diagnostico? |
| **AQ-T09-3** | F1_RUNTIME_IO overlap. `intent_to_briefing`, `answer_to_context`, `feedback_to_learning` e futuras respostas tipadas encostam em Doc 10/Doc 27/F1. | O patch futuro do Doc 09 deve centralizar esses nomes ou apenas apontar para Doc 10/Doc 27 para evitar duplicacao? |
| **AQ-T09-4** | Registry incompleto vs fonte fraca. Doc 09 exige fallback/manual/gates; UPGRADE/08 nao declara validacao, erro, idempotencia ou fallback. | O patch do Doc 09 deve tornar `validation`, `error_policy`, `fallback_manual` e `idempotency_semantics` campos obrigatorios do registry antes de aprovar novos transformers? |

---

## 6. Risco P1 + nota de aplicacao

- **P1:** Doc 09 e core do Execution System. Alterar o registry ou MVP de transformers irradia para Docs 02, 06, 07, 10, 11, 13, 21 e 27.
- **Nao aplicar aqui:** este candidate nao edita Doc 09, nao cria runtime e nao cria task/Work Order schema.
- **Risco principal:** promover nomes rasos e transformar o UPGRADE/08 em um segundo canonico paralelo. Mitigacao: promover so PROMOTE-T1..T5, com AQs para o resto.
- **Risco F1:** `briefing_to_task` pode ser lido como autorizacao de Work Order runtime. Nao e. E apenas um transformer candidate para futuro patch documental.
- **Aplicacao futura:** sessao `canonical_patch` separada, apos fan-in Claude#2 + Metacognik + Founder, com escopo minimo em Doc 09 e cross-refs se necessario.

---

## 7. BRA Packet

```yaml
bra_id: BRA-TRANSF-20260604-01
from_session: S-P1-L3-CODEX2-20260604-001
to: PMO/Dispatcher
context_summary:
  - "UPGRADE/08 lido como README + 10 transformer specs."
  - "Specs sao uniformes; so nome e funcao de 1 linha mudam."
  - "Doc 09 e mais completo; candidatos reais sao estruturais e poucos."
outputs:
  - "DOC09_TRANSFORMERS_RECONCILIATION_CANDIDATE.md"
open_questions:
  - "AQ-T09-1: transformer vs workflow vs Work Order para briefing_to_task/sprint/project_pack."
  - "AQ-T09-2: output envelope confidence/gaps/next_actions deve ser universal?"
  - "AQ-T09-3: centralizar nomes F1 no Doc 09 ou cross-ref para Doc 10/27?"
  - "AQ-T09-4: tornar validation/error/fallback/idempotency campos obrigatorios do registry?"
blockers:
  - "none para o candidate; aplicacao canonica depende de fan-in e aprovacao Founder/Metacognik."
risk_flags:
  - "P1 se Doc 09 for patchado sem auditoria."
  - "Risco de duplicar F1_RUNTIME_IO e Doc 27 se nomes forem promovidos sem taxonomia."
recommended_next:
  - "Claude#2 Auditor consolidar com TR-SKILLS e TR-POLICY antes de qualquer canonical_patch."
```

---

## 8. CHECKOUT RELEASE

```txt
CHECKOUT RELEASE - S-P1-L3-CODEX2-20260604-001
files_created: 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/DOC09_TRANSFORMERS_RECONCILIATION_CANDIDATE.md
files_changed: 000_ROADMAPS/SESSION_REGISTRY.md (1 sessao released_with_required_external_audit + 1 lock released)
files_not_touched: 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md (RO); 000_UPGRADE/08_TRANSFORMERS/ (RO); Doc 06/07/12/04; canonic 01-28; docs 29-34; ARCHITECTURE_PATCH_REPORT.md; 00_SYSTEM_GOVERNANCE/*
validation: estrutura espelha DOC03 candidate; diff de uniformidade incluído; nada aplicado em canonico
risks_remaining: PROMOTE-T2/T3 podem colidir com Doc 07/Doc 27; output envelope universal ainda depende de AQ; patch futuro precisa definir validacao/error/fallback/idempotency
next_step: fan-in (Claude#2 Auditor) consolida com TR-SKILLS + TR-POLICY
status: released_with_required_external_audit
```
