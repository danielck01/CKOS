---
title: Prompt Codex — GATE 1 Patches A+B+C
file: 05_PROMPT_CODEX_GATE1_PATCH_ABC.md
phase: 000_ROADMAPS
category: prompts
status: ready_for_use
owner: pmo_ckos
created_at: 2026-06-02
session_origin: S-P1-GATE1-CLAUDE-20260602-002
purpose: Prompt pronto para sessão canonical_patch Codex executar os 3 patches do GATE 1.
---

## EXECUTION HANDOFF — GATE1-PATCH-ABC — 2026-06-02

### Objetivo
Executar os 3 patches estruturais do GATE 1 que eliminam os defeitos G-01, G-02 e G-03 do canônico CKOS, conforme auditoria PMO (sessões S-P1-GATE1-CLAUDE-20260601-001 e S-P1-GATE1-CLAUDE-20260602-002).

### Modo de execução
`canonical_patch` — documentação apenas, sem código, sem backend, sem UI.

### Ferramenta
Codex

### Documentos de referência obrigatórios
- `05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md` — linha 94 (fonte do Patch A)
- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md` — §5.3, §5.4, §5.5 (fonte do Patch B)
- `02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md` — §5.4 entrada `research-pack-generation` (destino Patch B)
- `05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md` — §4 Tool Roles (destino Patch A)

---

## PATCH A — par 19 (Execution Protocol)

**Problema:** `19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md` (canônico) não lista os 7 Builder Subagents nem âncora `00_TAXONOMY §5.1`. Essa informação existe apenas no doc supersedido e se perderia.

**Ação 1 — adicionar §4.5 ao ANTIGRAVITY:**

No arquivo `05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`, após o bloco `## 4.4 Outras ferramentas e ferramentas futuras` e antes do `---` que separa a seção 5, inserir:

```markdown
## 4.5 Builder Subagents

O `Builder Lead` orquestra os Builder Subagents — executores especializados do CKOS:

| Subagent | Domínio |
|---|---|
| Frontend Builder | Componentes, UI, design system |
| Backend Builder | APIs, handlers, migrations |
| Data Builder | Schema, projections, queries |
| RAG Builder | Pipeline de evidência, indexação |
| Automation Builder | Workflows, triggers, automações |
| Design System Builder | Tokens, estilos, whitelabel |
| QA Builder | Testes, validação, regressão |

> **Referência taxonômica:** `00_TAXONOMY §5.1` — antigo nome "Builder Agent(s)", renomeado para Builder Subagents. Subordinados ao `Builder Lead`; nunca operam sem scope contract.
```

**Ação 2 — arquivar doc perdedor:**

No arquivo `05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md`, atualizar frontmatter:
- `status: draft` → `status: archived`
- Adicionar linha: `superseded_by: 05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md`

---

## PATCH B — par 18 (Research Protocol)

**Problema:** `18_RESEARCH_PROTOCOL_FOR_MANUS.md` contém 3 blocos operacionais únicos (scoring de referências, regra anti-cópia, lição de CSV) que não existem no canônico `18_RESEARCH_PROTOCOL.md` nem em `06_SKILLS_REGISTRY.md`. Se o doc for arquivado sem porte, esse conhecimento some.

**Ação 1 — expandir entrada `research-pack-generation` em Doc 06:**

No arquivo `02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md`, substituir a linha:

```markdown
- **`research-pack-generation`** — o que o Manus faz hoje, internalizado. Resp.: Research Subagent. Review: Datta + Metacognik.
```

Por:

```markdown
- **`research-pack-generation`** — curadoria governada de referências de pesquisa (visual, sistêmica, estratégica, de mercado). Internaliza o que Manus fazia no bootstrap. Resp.: Research Subagent. Review: Datta + Metacognik.

  **Scoring obrigatório de referências** (toda referência recebe pontuação antes de entrar no pack):

  | Critério | Peso |
  |---|---:|
  | Aplicabilidade real ao CKOS | 25 |
  | Transferibilidade técnica | 20 |
  | Valor estratégico | 20 |
  | Originalidade sem gimmick | 10 |
  | Viabilidade de performance | 10 |
  | Clareza de uso | 10 |
  | Direitos / link / autoria | 5 |

  **Regra de aplicação:** toda referência deve responder — o que observar? o que não copiar? como traduzir para CKOS? qual componente nasce disso? qual risco de interpretação? Referência sem resposta a essas perguntas é reprovada.

  **Regra de qualidade de CSV:** `references_master.csv` deve ter campos com vírgula entre aspas para não desalinhar colunas no parser. Shortlist sempre validada contra o CSV limpo antes da entrega. (Lição de auditoria — ver histórico `MANUS_RESEARCH_FIX_REPORT.md` se disponível.)
```

**Ação 2 — arquivar doc perdedor:**

No arquivo `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md`, atualizar frontmatter:
- `status: draft` → `status: archived`
- Adicionar linha: `superseded_by: 05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL.md`

---

## PATCH C — G-01 + G-02 (ordinal 21 + self-evolving dup)

**Problema:** dois documentos ativos ostentam o ordinal "21" globalmente (`05/21_SELF_EVOLVING_SYSTEM` e `06/21_ROI_ARCHITECTURE`). O `05/21` já tem Superseded Notice no corpo mas frontmatter ainda diz `status: draft`. Formalizar o arquivo.

**Ação — atualizar frontmatter de `05/21_SELF_EVOLVING_SYSTEM.md`:**

No arquivo `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`, atualizar frontmatter:
- `status: draft` → `status: archived`
- Adicionar linha: `superseded_by: 07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`

> Nenhum porte de conteúdo necessário — o canônico `07/25` é rewrite completo com `source_type: rewritten_from_superseded_doc` e `source_path: 05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md`.

---

## Arquivos permitidos para modificação

- `05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md` — inserir §4.5
- `05_IMPLEMENTATION_SYSTEM/19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md` — frontmatter apenas
- `02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md` — expandir entrada §5.4
- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL_FOR_MANUS.md` — frontmatter apenas
- `05_IMPLEMENTATION_SYSTEM/21_SELF_EVOLVING_SYSTEM.md` — frontmatter apenas
- `000_ROADMAPS/SESSION_REGISTRY.md` — registrar sessão + lock + release

## Arquivos proibidos (não tocar)

- `05_IMPLEMENTATION_SYSTEM/18_RESEARCH_PROTOCOL.md` — canônico ativo, sem alteração
- `07_EVOLUTION_SYSTEM/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md` — canônico ativo, sem alteração
- `06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md` — canônico ativo, sem alteração
- `ARCHITECTURE_PATCH_REPORT.md` — fora do escopo desta sessão
- `00_SYSTEM_GOVERNANCE/` — qualquer arquivo
- Qualquer doc 01-27 não listado acima
- Qualquer arquivo de UI, backend, API, runtime, migrations

## Constraints

- Patches A e B são adição/expansão de conteúdo — nunca remover conteúdo existente
- Patch C é frontmatter update apenas — não alterar corpo do documento
- Não deletar, não renomear, não mover arquivos
- Não criar novos arquivos além dos listados
- Não alterar changelog ou versão dos docs canônicos ativos

## Não fazer

- Não executar de-numeração (rename de arquivo) — isso é operação separada
- Não abrir Doc 28 ou qualquer doc 28-34
- Não modificar o canônico `18_RESEARCH_PROTOCOL.md`
- Não modificar o `07/25_SELF_EVOLVING_SYSTEM_ARCHITECTURE.md`
- Não atualizar `ARCHITECTURE_PATCH_REPORT.md` nesta sessão

## Output esperado

Relatório CHECKOUT RELEASE com:
- FILES_CHANGED: lista exata
- SUMMARY: o que foi feito em 3-5 linhas
- VALIDATION: confirmação de que nenhum arquivo fora do escopo foi tocado
- RISKS_REMAINING: o que ficou em aberto
- NEXT_STEP: "Aguardar fan-in Claude para declarar GATE 1 ✅ e desbloquear GATE 3 (Doc 28)"

## Como declarar a sessão no SESSION_REGISTRY

```
session_id: S-P1-GATE1-CODEX-20260602-001
task_id: GATE1_STRUCTURAL_PATCHES_ABC_20260602
session_type: canonical_patch
agent: codex
scope: arquivos listados em "permitidos" acima
status: active → released
started_at: 2026-06-02
expected_outputs: Patches A, B, C aplicados; SESSION_REGISTRY atualizado
estimated_cost: low
intelligence_level: high
```
