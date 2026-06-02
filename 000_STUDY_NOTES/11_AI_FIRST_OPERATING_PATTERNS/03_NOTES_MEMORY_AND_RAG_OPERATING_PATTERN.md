---
title: Notes, Memory and RAG Operating Pattern
file: 03_NOTES_MEMORY_AND_RAG_OPERATING_PATTERN.md
system_id: notes_memory_and_rag_operating_pattern
phase: 000_STUDY_NOTES
category: study_note
layer: auxiliary
version: 0.1.0
status: draft
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - metacognik
  - qa_lead
approval_required:
  - founder
  - pmo_ckos
  - metacognik
confidence: unverified
provenance_status: unverified
source_tool: claude
created_at: 2026-05-31
purpose: >
  Registrar o padrao auxiliar AI First de como pastas governadas, notes, memoria e RAG
  operacional do CKOS devem ser organizados para que markdown sirva como contexto recuperavel
  sem virar fonte canonica automatica nem ser confundido com o banco de dados de runtime.
inputs:
  - 000_ROADMAPS/SESSION_REGISTRY.md
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - 03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md
  - 000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md
outputs:
  - governed folder standard (mandatory + conditional notes)
  - notes-to-RAG promotion rules
  - documentation trust hierarchy
  - folder_memory migration guidance
  - YAML/embedding retrieval guidance
  - task-to-memory update discipline
  - ROI-per-folder and ROI-per-note rules
  - anti-patterns and acceptance criteria
framework: Governed Folder -> Notes -> Memory Layers -> Trust Hierarchy -> RAG Context -> Learning Loop
edge_cases:
  - markdown tratado como database de runtime
  - study note promovida a canon sem patch e approval
  - _folder_memory e ck_memory duplicados na mesma pasta
  - nota indexada no RAG sem permission scope
  - memoria duplicada entre roadmap e study note
  - prompt sem fonte virando evidencia
integrations: Cognik (memory write/retrieve), Metacognik (conflito/confianca), PMO_CKOS (memoria de governanca), Context Pack Builder (10), Memory Writer (10), RAG retriever (10), policy_engine (12)
prompts: Toda promocao de nota a memoria ou a RAG deve declarar fonte, confianca, escopo de permissao, expiracao e se requer approval.
metrics: Notas com YAML valido; pastas com README+ck_memory; zero _folder_memory novo; memoria sem duplicata; RAG sem lixo; prompts com fonte; ROI declarado quando ha decisao/custo.
related_notes:
  - 000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - 03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md
  - 000_ROADMAPS/MULTI_SESSION_EXECUTION_POLICY.md
tags:
  - study
  - ai_first
  - notes
  - memory
  - rag
  - folder_governance
  - trust_hierarchy
  - embeddings
  - auxiliary
---

# Notes, Memory and RAG Operating Pattern

## 1. Proposito

Esta study note registra um padrao operacional auxiliar para o CKOS: como pastas governadas, notes em markdown, memoria e RAG operacional devem ser organizados para que documentacao vire **contexto recuperavel** — sem virar fonte canonica automatica e sem ser confundida com o banco de dados de runtime.

Ela nao cria documento canonico, nao autoriza UI/UX, nao inicia Antigravity, nao implementa RAG real, nao cria backend, banco, API, migration ou automacao. Serve como estudo para futuras notas, patch candidates ou docs aprovados pelo Founder.

> **Separacao mestre (nao violar):** O markdown do vault e a camada de **documentacao e memoria operacional auxiliar**. O banco de dados de runtime (`memories`, `document_chunks`, `embeddings`, `events`) e definido em `11_DATA_MODEL_AND_PERSISTENCE.md` e e a fonte fisica de verdade. Esta nota governa a camada de markdown; ela **nao** substitui, nao espelha e nao compete com Doc 11.

## 2. Escopo e nao-autoridade

| Pode | Nao pode |
|---|---|
| Definir padrao de pasta governada | Alterar docs canonicos 01-26 |
| Definir notes obrigatorias e condicionais | Criar docs 27-34 |
| Definir como nota vira contexto RAG | Implementar RAG, embeddings, banco ou API |
| Definir hierarquia de confianca documental | Promover qualquer nota a canon sem patch + approval |
| Recomendar migracao de `_folder_memory` | Mover, renomear ou deletar arquivos |

Esta nota e `auxiliary`, `confidence: unverified`, `provenance_status: unverified`. Vive em `000_STUDY_NOTES/` e nao tem autoridade canonica.

## 3. Padrao obrigatorio de pasta governada

Toda pasta governada do CKOS deve conter, no minimo, **dois arquivos**:

```txt
<pasta_governada>/
  README.md        # o que a pasta e, escopo, o que entra e o que nao entra, indice
  ck_memory.md     # memoria operacional viva da pasta: decisoes, estado, locks, proxima acao
```

Regras:

- `README.md` = **identidade e fronteira** da pasta. Responde: o que e, por que existe, o que entra, o que nao entra, quais notas existem e qual a proxima leitura.
- `ck_memory.md` = **estado vivo** da pasta. Responde: o que ja foi decidido, o que esta pendente, qual o ultimo lock/release, quais riscos abertos, qual a proxima acao. E append-orientado: nao reescreve historico, adiciona entradas datadas.
- Pasta governada sem esses dois arquivos esta **incompleta** e deve ser registrada como lacuna em sessao `memory_refresh` futura — nunca corrigida silenciosamente fora de escopo.

`README.md` e `ck_memory.md` sao a unidade minima. Sem eles, a pasta nao e governada — e apenas um deposito de arquivos.

## 4. Padrao condicional de notes

As notas abaixo **so existem quando ha sinal real** que as justifique. Criar uma delas vazia ou "por padrao" e anti-pattern (gera ruido e memoria morta).

| Nota condicional | Deve existir quando | Nao deve existir quando |
|---|---|---|
| `ck_tasks.md` | a pasta coordena trabalho com >1 etapa, owner ou handoff | a pasta e so referencia/leitura estatica |
| `ck_risks.md` | ha risco juridico, tecnico, de custo, reputacional ou de governanca aberto | nao ha risco material identificado |
| `ck_roi.md` | a pasta e estrategica e seu valor precisa ser justificado/priorizado | a pasta e utilitaria sem decisao de investimento |
| `ck_feedback.md` | ha feedback humano/agente/QA recorrente sobre o conteudo da pasta | nao houve feedback ainda |
| `ck_agent_handoffs.md` | mais de um agente/sessao escreve na pasta e ha transicao de contexto | uma unica sessao/escritor opera a pasta |
| `ck_learning.md` | a pasta acumula licoes, erros recorrentes ou padroes aprendidos | nao ha aprendizado consolidado a registrar |
| `ck_prompts.md` | a pasta reutiliza prompts versionados com fonte e criterio | prompts sao ad-hoc, descartaveis ou sem fonte |

Regra de ouro: **uma nota condicional nasce de um sinal, nao de um template.** Se voce nao consegue apontar a decisao, o risco, o custo, o handoff, o feedback ou o aprendizado que a justifica, a nota nao deve existir ainda.

## 5. Memoria: short-term, mid-term e long-term

Alinhado a `05_MEMORY_AND_CONTEXT_ARCHITECTURE.md` §5.1 (politica canonica) e `11_DATA_MODEL` §14 (materializacao fisica). O markdown desta camada **espelha intencao**, nao substitui a tabela `memories`.

| Camada | O que e | Onde vive (runtime, Doc 11) | Reflexo em markdown (esta camada) |
|---|---|---|---|
| **short-term** | sessao/run atual: conversa, comandos recentes, nodes abertos, estado temporario | Redis + `memories.scope=short_term` | normalmente **nao** vira nota; e efemero. So promover se virar decisao |
| **mid-term** | projeto em andamento: briefing vivo, hipoteses, decisoes pendentes, status | Postgres + vetor (`memories.scope=mid_term`) | `ck_memory.md` da pasta/projeto registra estado vivo e pendencias |
| **long-term** | conhecimento persistente: decisoes aprovadas, identidade, aprendizados, historico | Postgres + vetor + storage (`memories.scope=long_term`) | `ck_learning.md`, decisions registradas, notas promovidas com approval |

Principios herdados de Doc 05 §5.8 e §11:
- decisoes aprovadas e outputs finais -> long-term;
- hipoteses -> mid-term ate validacao;
- dados externos expiram (`valid_until`);
- outputs rejeitados nao sao fonte forte (viram memoria negativa quando uteis);
- nada de short-term efemero promovido a long-term sem decisao explicita.

## 6. Como notes viram contexto para RAG sem virar fonte canonica automatica

Indexar uma nota no RAG **da a ela recuperabilidade, nao autoridade**. Recuperavel != verdadeiro != canonico.

Fluxo correto (espelha Doc 05 §5.3 e Doc 09 §5.4):

```txt
nota markdown
  -> elegivel para chunking/embedding (se YAML valido + escopo permitido)
  -> indexada no vetor com namespace de tenant/projeto (12 §5.6)
  -> recuperada por relevancia
  -> FILTRADA por permissao (pre-condicao, nunca pos-filtro)
  -> entregue ao agente como CONTEXTO com label de confianca e fonte
  -> agente trata como evidencia recuperada (nivel 6 da hierarquia de runtime, Doc 05 §5.5)
  -> NUNCA promovida a decisao/canon sem patch + QA + approval
```

Regras duras:

1. **Recuperacao nao e canonizacao.** Uma study note recuperada pelo RAG entra como `retrieved_doc` / `agent inference support`, jamais como `approved_decision`.
2. **Canonizacao exige caminho explicito:** study note -> patch candidate -> QA documental -> approval Founder/PMO/Metacognik -> doc canonico. RAG nao curta-circuita esse caminho.
3. **Toda nota recuperavel carrega confianca e fonte.** Sem `confidence` e `provenance_status` no YAML, a nota nao deveria ser elegivel para indexacao de alta prioridade.
4. **Permission filter e pre-condicao** (Doc 12 §5.6): o namespace de tenant/projeto e aplicado antes da busca, nunca como pos-filtro.

## 7. Hierarquia de confianca (camada de documentacao)

Esta e a hierarquia de **proveniencia de documentos do vault** — usada para resolver conflito entre arquivos de documentacao:

```txt
1. Canonical docs (00-26 aprovados)
2. Approved patch reports (ARCHITECTURE_PATCH_REPORT e equivalentes aprovados)
3. Study notes (000_STUDY_NOTES, auxiliares)
4. Roadmaps (000_ROADMAPS, wrappers e planejamento)
5. Memory notes (ck_memory.md e notas condicionais ck_*)
6. AI outputs unverified (saidas de agente nao revisadas)
```

> **Nao confundir com a hierarquia de runtime.** A hierarquia de confianca de **recuperacao de runtime** (qual evidencia prevalece quando um agente decide) e a de `05_MEMORY_AND_CONTEXT_ARCHITECTURE.md` §5.5 (approved decision > contract > db record > user instruction > artifact > retrieved doc > agent inference > web > weak hypothesis). Aquela e canonica para execucao. **Esta** §7 governa apenas conflito entre arquivos de documentacao do vault. As duas coexistem: a §7 decide qual documento vence; a Doc 05 §5.5 decide qual evidencia vence em um run. Em qualquer conflito de execucao, Doc 05 §5.5 prevalece.

Conflito entre niveis -> Metacognik aciona revisao (Doc 05 §5.5).

## 8. Migracao de `_folder_memory` para `ck_memory.md`

O vault tem historico de `_folder_memory.md`. O padrao alvo e `ck_memory.md`. A migracao e **gradual e nao-destrutiva**:

```txt
Regra 1: NAO criar nenhum _folder_memory novo. Pastas novas nascem com ck_memory.md.
Regra 2: NAO deletar _folder_memory existente fora de uma sessao autorizada.
Regra 3: Quando uma pasta com _folder_memory for tocada por sessao memory_refresh,
         criar ck_memory.md, copiar o estado vivo relevante, e marcar o
         _folder_memory legado com aviso "superseded by ck_memory.md (preserved)".
Regra 4: Nunca manter dois arquivos de memoria ativos divergindo. Um vivo (ck_memory.md),
         um legado preservado com aviso. Nao duas verdades.
```

Isso evita memoria duplicada (anti-pattern §13) e respeita "no move/rename/delete" sem autorizacao (Multi-Session Execution Policy §2).

## 9. Como YAML, tags, related_notes e system_id ajudam embeddings

Metadados nao sao decoracao — sao **sinais de recuperacao**. Uma nota com YAML pobre e recuperada pior e polui o RAG.

| Campo | Funcao na recuperacao vetorial |
|---|---|
| `system_id` | ancora estavel da nota; permite dedupe e citacao mesmo se o title mudar |
| `title` | sinal semantico primario do chunk de cabecalho |
| `tags` | filtros facetados pre-busca (reduz espaco de candidatos antes do ranking) |
| `related_notes` | grafo de vizinhanca; permite expansao de contexto (1-hop) sem busca cega |
| `category` / `phase` | particionamento logico; evita misturar runtime com study em uma mesma query |
| `confidence` / `provenance_status` | ponderacao de ranking; nota `unverified` nao deve dominar resultado |
| `purpose` / `inputs` / `outputs` | resumo denso para o chunk de topo; melhora match de intencao |
| `version` / `created_at` | freshness scoring (Doc 13); nota velha sinaliza revalidacao |

Regra: **YAML completo e pre-condicao de indexacao de qualidade.** Nota sem `system_id`, `tags`, `confidence` e `related_notes` deve ser tratada como candidata de baixa prioridade ate ser corrigida.

## 10. Como uma task atualiza memoria sem gerar caos

A ligacao task -> memoria segue o transformer `decision_to_memory` (Doc 09 §5.6) e a disciplina de append.

```txt
task concluida
  -> produz output + evidencia
  -> classifica: isso e short, mid, long, decision, evidence ou apenas evento? (Doc 05 prompt §9)
  -> se relevante: escreve UMA entrada datada em ck_memory.md (append, nao overwrite)
  -> se decisao: registra como decision (long-term), com fonte e confianca
  -> se aprendizado: ck_learning.md
  -> se risco novo: ck_risks.md
  -> nunca duplica a mesma memoria em duas notas; referencia por system_id
```

Regras anti-caos:
1. **Append datado, nao overwrite.** Historico preservado; correcao por nova entrada, nunca apagando a anterior.
2. **Uma memoria, um lar.** Cada fato mora em uma nota; outras notas referenciam por `system_id`, nao copiam.
3. **Toda escrita de memoria declara fonte e confianca.** Memoria sem fonte e rumor.
4. **Task so atualiza memoria dentro do checkout lock.** Fora do escopo declarado, nao escreve (Multi-Session Execution Policy §7).

## 11. Como feedback e aprendizado entram no loop

```txt
feedback (humano | agente | QA)
  -> ck_feedback.md (registro datado, com fonte e sentimento)
  -> triagem: vira task? vira risco? vira aprendizado? vira nada?
  -> se padrao recorrente -> ck_learning.md (licao consolidada)
  -> aprendizado aprovado -> candidato a memoria long-term / patch candidate
  -> erro recorrente -> alimenta anti-patterns e checklists
```

Principios:
- feedback isolado e dado; feedback recorrente e sinal — so o segundo vira aprendizado.
- aprendizado nao aprovado fica em `ck_learning.md` como hipotese, nao como verdade.
- nada de feedback bruto promovido direto a canon; passa por triagem e, se for canon, por patch + approval.

## 12. Como ROI deve aparecer

ROI aqui e **inteligencia de valor**, nunca promessa (alinhado a Doc 05 e a Study Note 01 §5).

| Nivel | Quando usar | Onde registrar |
|---|---|---|
| **ROI por pasta** | a pasta e estrategica: seu valor/prioridade precisa ser justificado vs outras frentes | `ck_roi.md` da pasta |
| **ROI por nota** | a nota carrega decisao, custo, produto, execucao ou priorizacao | bloco ROI dentro da propria nota |

Regras:
- ROI por nota e obrigatorio quando ha decisao, custo estimado, output de produto, execucao ou escolha de prioridade.
- ROI sem evidencia e premissa; ROI sem confianca e ilusao; ROI sem limitacao e mentira (Doc 21 / Study Note 01).
- ROI operacional conta (retrabalho evitado, risco reduzido, reuso de memoria), nao apenas dinheiro.
- Nenhuma pergunta de decisao na nota sem ROI, risco, custo ou consequencia (Multi-Session Execution Policy §9).

## 13. Anti-patterns

| Anti-pattern | Por que e ruim | Correcao |
|---|---|---|
| Notes soltas sem README+ck_memory | pasta nao-governada; contexto perdido | criar a unidade minima §3 |
| Nomes inconsistentes (`_folder_memory` vs `ck_memory`) | duplicacao e ambiguidade de verdade | migracao gradual §8 |
| Memoria duplicada em duas notas | duas verdades divergem com o tempo | uma memoria, um lar; referenciar por system_id §10 |
| Prompts sem fonte em `ck_prompts.md` | prompt vira "evidencia" sem proveniencia | exigir fonte + criterio; senao nao registrar |
| RAG com lixo (notas vazias/template) | polui recuperacao, derruba relevancia | YAML completo como pre-condicao de indexacao §9 |
| **Markdown tratado como database de runtime** | markdown nao tem RLS, transacao, append-only real | runtime e Doc 11; markdown e memoria auxiliar §1 |
| Study note tratada como canon | curto-circuita patch + QA + approval | recuperacao != canonizacao §6 |
| Nota condicional criada vazia "por padrao" | memoria morta, ruido | nota nasce de sinal, nao de template §4 |
| ck_memory.md reescrito (overwrite) | historico apagado, sem auditoria | append datado §10 |
| Nota indexada sem permission scope | risco de vazamento cross-tenant | permission filter como pre-condicao §6, Doc 12 §5.6 |

## 14. Acceptance criteria

- A nota permanece em `000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/`, sem autoridade canonica.
- YAML possui os campos auxiliares obrigatorios, incluindo `system_id`, `confidence: unverified`, `provenance_status: unverified`, `tags` e `related_notes`.
- Define o padrao obrigatorio README.md + ck_memory.md.
- Define as 7 notas condicionais e quando cada uma deve e nao deve existir.
- Diferencia short/mid/long-term memory e ancora em Doc 05 §5.1 e Doc 11 §14.
- Explica como notes viram contexto RAG sem virar canon automatico.
- Apresenta a hierarquia de confianca documental e a distingue explicitamente da hierarquia de runtime de Doc 05 §5.5.
- Define migracao nao-destrutiva de `_folder_memory` para `ck_memory.md`.
- Explica como YAML/tags/related_notes/system_id melhoram embeddings.
- Define disciplina task -> memoria (append, uma memoria um lar, fonte+confianca).
- Define loop de feedback e aprendizado.
- Define ROI por pasta (estrategica) e ROI por nota (decisao/custo/produto/execucao/priorizacao).
- Lista anti-patterns, incluindo markdown como database de runtime.
- Nao cria docs canonicos, docs 27-34, backend, banco, API, migration, RAG real ou automacao.
- Nao move, renomeia ou deleta arquivos.

## 15. Proxima acao

Usar esta study note como referencia para padronizar pastas governadas do vault e para preparar, futuramente, um patch candidate de governanca de notes/memoria. A pasta `000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/` atualmente **nao possui** `README.md` nem `ck_memory.md`; recomenda-se uma sessao `memory_refresh` dedicada para cria-los conforme §3 — fora do escopo desta sessao `study`, que cria apenas esta nota. Qualquer canonizacao exige patch candidate, QA documental e approval Founder.
