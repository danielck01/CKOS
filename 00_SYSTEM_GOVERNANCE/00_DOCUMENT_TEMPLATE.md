---
title: Document Template
file: 00_DOCUMENT_TEMPLATE.md
phase: 00_SYSTEM_GOVERNANCE
category: template
version: 2.3.0
status: active
owner: PMO_CKOS
responsible_agent: PMO_CKOS
reviewers:
  - metacognik
approval_required:
  - founder
  - metacognik
purpose: Padrão obrigatório de YAML, enums e estrutura de corpo para todo documento canônico do CKOS.
inputs: Arquitetura macro do CKOS; necessidade de padronizar docs para humanos, RAG e agentes.
outputs: Template universal; enums controlados; checklist de QA documental.
framework: 4 camadas — metadados YAML, propósito/função, operação, controle.
edge_cases: Documento curto demais; documento misturando assuntos; doc externo sem template.
integrations: Obsidian/RAG; pipeline de QA documental; geração assistida por agentes.
prompts: Prompt de geração documental; prompt de QA documental.
metrics: 100% docs com YAML válido; 0 enums fora do padrão; 0 docs fora da hierarquia.
related_notes:
  - 00_MASTER_MAP.md
  - 00_TAXONOMY_AND_NAMING.md
  - 00_DEPENDENCY_MAP.md
tags: [governance, template, standard, yaml, enums]
---

# 1. Propósito

Definir o template mestre obrigatório para todos os documentos canônicos do CKOS, travando o bloco YAML, os enums controlados e a ordem das seções de corpo.

Sem template mestre, cada agente, builder ou ferramenta externa cria documentação em formato próprio — o que aumenta fricção, retrabalho, ambiguidade e entropia. Esta é a versão `2.0.0`, que substitui a `1.0.0` após a auditoria de arquitetura de 2026-05-24.

# 2. Função dentro do CKOS

Fonte oficial de estruturação documental. Qualquer documento estratégico, técnico, operacional ou de implementação deve seguir este template ou justificar exceção explícita no corpo.

## 2.1 Decisão de interpretação (registrada)

A especificação do patch lista um conjunto de campos para o YAML. Os campos de **metadados** (`title`, `file`, `phase`, `category`, `version`, `status`, `owner`, `responsible_agent`, `reviewers`, `approval_required`, `tags`) vivem no **bloco YAML**. Os campos de **conteúdo** (`purpose`, `inputs`, `outputs`, `framework`, `edge_cases`, `integrations`, `prompts`, `metrics`, `related_notes`) aparecem **duas vezes**, de forma intencional:

1. no YAML, como **resumo de uma linha** (abstract legível por máquina, útil para RAG e triagem); e
2. no **corpo**, como **seções numeradas completas**.

Motivo: embutir `framework` ou `edge_cases` inteiros como escalares YAML produz documentos ilegíveis e não-versionáveis. Mantém-se o abstract no YAML e a profundidade no corpo. A regra de QA é: o resumo YAML não pode contradizer a seção de corpo correspondente.

# 3. Inputs

- arquitetura macro do CKOS;
- necessidade de padronizar documentação para humanos, RAG e agentes;
- enums controlados de `status`, `approval_required`, `phase`.

# 4. Outputs

- template universal em Markdown;
- bloco YAML obrigatório com enums controlados;
- checklist de aprovação documental.

# 5. Framework operacional

Todo documento oficial deve conter quatro camadas:

```txt
1. YAML        → metadados + abstract de uma linha por campo de conteúdo
2. Propósito   → por que existe e onde se encaixa (seções 1-2)
3. Operação    → inputs, outputs, framework, agentes, skills, integrações, prompts (seções 3-11)
4. Controle    → edge cases, métricas, aprovação, reprovação, related notes (seções 12-16)
```

# 6. Template mestre oficial

```md
---
title:
file:
phase:
category:
version: 0.1.0
status: draft
owner:
responsible_agent:
reviewers:
  - metacognik
approval_required:
  - none
purpose:
inputs:
outputs:
framework:
edge_cases:
integrations:
prompts:
metrics:
related_notes:
tags: []
---

# 1. Propósito

# 2. Função dentro do CKOS

# 3. Inputs

# 4. Outputs

# 5. Framework operacional

# 6. Agente responsável

# 7. Superagentes envolvidos

# 8. Skills necessárias

# 9. Prompts relacionados

# 10. Integrações

# 11. Memória e contexto

# 12. Edge cases

# 13. Métricas de sucesso

# 14. Critérios de aprovação

# 15. Critérios de reprovação

# 16. Related notes
```

# 6.1 Template resumido para RAW/STUDY

Notas em `000_UPLOADS/` e `000_STUDY_NOTES/` seguem o padrao CKOS, mas usam campos adicionais para provenance, confidence e layer. Elas nao substituem o template canonico; servem para transformar material bruto em estudo auditavel antes de qualquer patch oficial.

```md
---
title:
file:
system_id:
display_name:
doc_type:
category:
layer:
status: draft
version: 0.1.0
created_at:
updated_at:
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - metacognik
approval_required:
  - founder
source_type:
source_path:
source_tool:
provenance_status: unverified
project: ckos
related_docs: []
related_notes: []
tags: []
risk_level: medium
confidence: unverified
---

# Proposito

# Contexto

# Fonte analisada

# O que este material revela

# O que isso muda no CKOS

# Decisoes possiveis

# Riscos

# Perguntas abertas

# Recomendacoes PMO

# Proxima acao

# Related Notes
```

Regra: uma study note pode sugerir patch, mas nao altera documento oficial. Um `patch_candidate` exige approval antes de canonizacao.

# 7. YAML obrigatório e enums controlados

```yaml
title:               # Nome legível do documento
file:                # Nome exato do arquivo .md
phase:               # enum de fase (ver abaixo)
category:            # categoria funcional (ver §8)
version:             # SemVer obrigatório, ex.: 1.0.0
status:              # enum: draft | active | deprecated | archived
owner:               # papel humano/organizacional dono (ver taxonomia)
responsible_agent:   # agente/superagent dono operacional (ver taxonomia)
reviewers:           # lista de revisores (agentes/papéis)
approval_required:   # lista do enum de aprovação (ver abaixo)
tags:                # lista livre de tags semânticas
```

## 7.1 Enum `status`

```txt
draft | active | deprecated | archived
```

Proibido: `draft_v1`, `v1_draft`, `active_v1`, `draft_v1` entre aspas, ou qualquer texto livre. A maturidade da versão é expressa em `version` (SemVer), não em `status`.

## 7.2 Enum `phase`

```txt
00_SYSTEM_GOVERNANCE
01_THINKING_SYSTEM
02_EXECUTION_SYSTEM
03_RUNTIME_SYSTEM
04_PRODUCT_SYSTEM
05_IMPLEMENTATION_SYSTEM
```

## 7.3 Enum `approval_required`

Sempre uma **lista YAML**, mesmo que com um único valor. Valores permitidos (todos em **snake_case** — regra obrigatória):

```txt
none | founder | pmo_ckos | technical | client | legal | qa_lead | metacognik
```

Proibido: texto livre como `"Founder + PMO + Metacognik"`, maiúsculas misturadas como `PMO_CKOS`, `QA Lead` ou `Metacognik` neste enum. Múltiplas aprovações usam array:

```yaml
approval_required:
  - founder
  - pmo_ckos
  - metacognik
```

> **Nota de consistência:** os valores deste enum são identificadores de sistema (`system_id`) em snake_case — ver `00_TAXONOMY_AND_NAMING §13.1`. O `display_name` correspondente (e.g., `PMO_CKOS`, `QA Lead`, `Metacognik`) é usado apenas em texto corrido, nunca como valor de enum.

## 7.4 Enum `version`

SemVer `MAJOR.MINOR.PATCH`. Exemplos: `0.1.0` (rascunho inicial), `1.0.0` (primeira versão aprovada), `1.1.0` (acréscimo compatível), `2.0.0` (mudança estrutural).

## 7.5 Enum `layer`

Usado em notas RAW/STUDY e em docs canonicos quando for necessario explicitar a camada documental.

```txt
raw | study | canonical
```

Definicoes:

- `raw`: material bruto em `000_UPLOADS/`, sem autoridade canonica.
- `study`: interpretacao em `000_STUDY_NOTES/`, com provenance, confidence, riscos, lacunas e recomendacao PMO.
- `canonical`: documento oficial versionado, alterado apenas por patch plan aprovado.

## 7.6 Enum `doc_type`

```txt
upload_note | study_note | source_manifest | patch_candidate | decision_log | canonical_doc
```

Definicoes:

- `upload_note`: nota de registro de material RAW.
- `study_note`: interpretacao estudavel de uma fonte.
- `source_manifest`: manifest de origem, ferramenta, path, escopo, PII e provenance.
- `patch_candidate`: proposta estudada de alteracao canonica; nao e patch aplicado.
- `decision_log`: registro de decisao PMO/Founder/reviewers.
- `canonical_doc`: documento oficial versionado.

## 7.7 Enum `confidence`

```txt
unverified | low | medium | high
```

Regra: output de IA sempre entra como `confidence: unverified` por padrao. `source_tool` identifica ferramenta, nao fonte de verdade.

## 7.8 Enum `provenance_status`

```txt
unverified | partial | verified | disputed | expired
```

Regras:

- `source_path` deve apontar para origem verificavel quando possivel.
- `source_tool` nunca canoniza uma informacao por si so.
- material com provenance `disputed` ou `expired` nao pode gerar patch canonico sem nova revisao.
- `patch_candidate` exige aprovacao antes de canonizacao.

# 8. Categorias oficiais

```txt
governance · template · taxonomy · dependency_map
constitution · object_model · agents · autonomy · memory
skills · workflow · prompt_library · transformers
runtime · data_model · runtime_data · security · evals
product_architecture · interface
implementation · research · qa · approval · self_evolving
```

> **`runtime_data`**: categoria exclusiva para documentos que especificam schema físico, tabelas, migrations e estratégia de persistência de dados de runtime (atualmente: `11_DATA_MODEL_AND_PERSISTENCE.md`). Distinto de `data_model` (conceitual) e `runtime` (arquitetura de execução).

# 9. Regras de escrita

1. Toda afirmação deve ter consequência prática.
2. Evitar hype sem mecanismo.
3. Separar conceito (Thinking) de execução (Execution) de runtime (Runtime) de projeção (Product).
4. Registrar approval quando houver decisão crítica.
5. Respeitar whitelabel real: arquitetura CKCompany separada da skin do projeto.
6. Usar apenas os nomes oficiais de `00_TAXONOMY_AND_NAMING.md`.

## 9.1 Regras adicionais para RAW/STUDY

1. Output de IA sempre entra como `confidence: unverified` por padrao.
2. `source_tool` nao e fonte de verdade; ele registra ferramenta de origem/coleta.
3. `source_path` deve apontar para origem verificavel quando possivel.
4. Study notes podem sugerir patch, mas nao alteram documentos oficiais.
5. Patch candidates exigem aprovacao antes de qualquer canonizacao.
6. Nenhum conteudo RAW ou STUDY entra no canonico sem patch plan aprovado.

## 9.2 Regra adicional para documentos de Runtime (fase 03)

Todo documento da fase `03_RUNTIME_SYSTEM` deve declarar explicitamente (em seções de corpo ou tabela dedicada):

```txt
- registries afetados        (quais catálogos do §5.14 ele lê/escreve)
- engines afetados           (quais processos do §5.15 ele aciona)
- state machines afetadas    (quais máquinas do §5.25)
- eventos emitidos           (nomes de evento no event log)
- tabelas/logs necessários   (mapeados em 11_DATA_MODEL)
- policies envolvidas        (do policyRegistry / 12)
- failure modes              (o que pode falhar e como degrada)
- rollback / compensating actions  (eventos compensatórios)
- observability/evals/cost hooks   (o que é tracejado/avaliado/contabilizado em 13)
```

Um doc de Runtime que não declara seus registries, engines, state machines, eventos, failure modes e rollback é **reprovado** na QA documental.

# 10. Prompts relacionados

## Prompt de geração documental

```txt
Crie o documento seguindo estritamente o 00_DOCUMENT_TEMPLATE v2. Não pule YAML, propósito, inputs, outputs, framework, agente responsável, edge cases, integrações, prompts, métricas e related notes. Use apenas enums controlados de status, phase e approval_required. Use apenas nomes oficiais da taxonomia. Se uma seção não se aplicar, escreva "Não aplicável nesta fase" e explique por quê.
```

## Prompt de QA documental

```txt
Audite este documento contra o 00_DOCUMENT_TEMPLATE v2. Verifique: YAML completo, SemVer, status no enum, approval_required como lista do enum, ausência de naming proibido (Metaconik, PMO Agent, QA Agent), related_notes válidos e dependência de Runtime quando for doc de Product. Classifique como aprovado, aprovado com ajustes ou reprovado.
```

# 11. Memória e contexto

O bloco YAML é a unidade indexável por RAG. O abstract de uma linha por campo de conteúdo permite recuperação semântica sem carregar o documento inteiro. O corpo é a fonte de verdade quando houver conflito com o abstract.

# 12. Edge cases

- Documento curto demais: talvez seja seção, não documento.
- Documento misturando assuntos: dividir ou reestruturar.
- Documento externo sem template: converter para padrão CKOS antes de canonizar.
- Moodboard/visual sem aplicação operacional: não é documento canônico.

# 13. Métricas de sucesso

- 100% dos docs canônicos com YAML válido;
- 100% com `version` SemVer;
- 100% com `status` no enum;
- 100% com `approval_required` como lista controlada;
- 0 ocorrências de naming proibido;
- 0 docs fora da hierarquia.

# 14. Critérios de aprovação

- YAML completo e válido;
- enums respeitados;
- estrutura de corpo presente;
- naming oficial;
- related_notes consistentes.

# 15. Critérios de reprovação

- YAML ausente ou inválido;
- `status`/`version`/`approval_required` fora do padrão;
- naming proibido;
- seções obrigatórias ausentes sem justificativa.

# 16. Related notes

- [[00_MASTER_MAP]]
- [[00_TAXONOMY_AND_NAMING]]
- [[00_DEPENDENCY_MAP]]
