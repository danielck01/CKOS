---
title: 19 — Claude, Codex & Antigravity Execution Protocol
file: 19_CLAUDE_CODEX_ANTIGRAVITY_EXECUTION_PROTOCOL.md
system_id: ai_development_execution_protocol
phase: 05_IMPLEMENTATION_SYSTEM
category: implementation_system
version: 1.0.0
status: draft
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - founder
  - technical
  - metacognik
approval_required:
  - founder
  - technical
  - metacognik
inputs:
  - 10_SYSTEM_RUNTIME_ARCHITECTURE.md v1.1.1
  - 11_DATA_MODEL_AND_PERSISTENCE.md v1.2.0
  - 12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md v1.1.0
  - 13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md v1.1.0
  - 17_IMPLEMENTATION_PROTOCOL.md v1.2.1
  - 18_RESEARCH_PROTOCOL.md v1.0.0
outputs:
  - ai_coding_protocol
  - tool_selection_rules
  - execution_handoff_format
  - patch_review_protocol
  - safe_implementation_rules
  - prompt_to_code_governance
related_notes:
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md
  - ../03_RUNTIME_SYSTEM/12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE.md
  - ../03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - ../04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md
  - ../04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md
  - ../04_PRODUCT_SYSTEM/16_NODE_CANVAS_ARCHITECTURE.md
  - 17_IMPLEMENTATION_PROTOCOL.md
  - 18_RESEARCH_PROTOCOL.md
  - 20_QA_AND_FOUNDER_APPROVAL_PROTOCOL.md
  - ../ARCHITECTURE_PATCH_REPORT.md
supersedes: 19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md v1.1.0
tags:
  - implementation
  - ai-tools
  - claude-code
  - codex
  - antigravity
  - execution-protocol
  - governance
  - anti-entropy
---

> **Frase central:**
> "CKOS development must be tool-assisted, not tool-dependent. Claude, Codex and Antigravity are execution interfaces; the source of truth remains CKOS documentation, gates, policies, QA and founder approval."
>
> Em português: "O desenvolvimento do CKOS deve ser assistido por ferramentas, não dependente delas. Claude, Codex e Antigravity são interfaces de execução; a fonte da verdade continua sendo a documentação, os gates, as políticas, o QA e a aprovação do Founder."

> **Nota de supersessão:** Este documento substitui `19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md` v1.1.0. O protocolo anterior cobria apenas modos de execução e prompts operacionais. Este documento define a governança completa de desenvolvimento assistido por IA para o CKOS.

---

# 1. Propósito

Este documento define como usar ferramentas de desenvolvimento assistido por IA — Claude Code, Codex, Antigravity e equivalentes futuros — para implementar o CKOS com segurança, rastreabilidade e governança arquitetural.

O problema que este documento resolve: sem protocolo explícito, ferramentas de IA tendem a:
- inventar arquitetura que não existe nos docs aprovados
- expandir escopo silenciosamente durante a execução
- criar acoplamentos ocultos entre módulos
- produzir código tecnicamente correto mas arquiteturalmente errado
- ignorar policies, gates e approval checkpoints
- gerar divergência progressiva entre código e documentação

A solução não é não usar essas ferramentas. É usá-las com scope contracts, templates padronizados, hierarquia de fonte da verdade explícita e protocolo de review antes de merge.

```
Errado: "Claude, implementa o dashboard e já aproveita pra refatorar o runtime"
Correto: "Claude, implementa o widget Project Pulse conforme doc 14 §10,
         tocando apenas os arquivos listados no scope contract,
         seguindo a projection risk_gap_evidence_projection de doc 11 §21,
         sem alterar outros widgets nem o projection engine."
```

---

# 2. O que é este protocolo / O que NÃO é

**É:**
- Protocolo de execução assistida por IA para desenvolvimento do CKOS
- Regras de handoff entre documentação aprovada e código implementado
- Framework de seleção de ferramenta por tipo de tarefa
- Conjunto de templates de prompt para Claude, Codex e Antigravity
- Protocolo de redução de erro, retrabalho, alucinação e divergência arquitetural
- Catálogo de ações proibidas e modos de falha conhecidos
- Referência para qualquer engenheiro ou agente que execute código no CKOS

**NÃO é:**
- Guia de prompts soltos ou biblioteca de snippets
- Backlog de features ou roadmap de produto
- Autorização para implementar — autorização vem dos gates do doc 17
- Substituto do Technical Lead — ferramentas de IA não tomam decisões arquiteturais
- Substituto do Founder approval — decisões de produto, escopo e direção pertencem ao Founder
- Fonte da verdade do sistema — a verdade está nos docs 10–18, não no output de IA

---

# 3. Princípio central

> **Nenhuma ferramenta de código assistida por IA pode implementar além da arquitetura aprovada.**

Este princípio é absoluto. Quando uma ferramenta de IA sugere algo que não está coberto pelos docs 10–18:

```
Tool output: "Podemos adicionar uma camada de cache Redis aqui para melhorar performance"
Resposta correta: "Obrigado pela sugestão. Registrar como out_of_scope_recommendation.
                   Não implementar. Se fizer sentido, volta como patch sugerido para doc 10."
```

O corolário prático:
- Se está nos docs aprovados → pode ser implementado com o mode correto
- Se não está nos docs → não pode ser implementado sem patch + aprovação primeiro
- Se o doc está ambíguo → gerar `ARCHITECTURE_QUESTION`, não inventar solução

---

# 4. Tool Roles

Cada ferramenta tem um perfil de uso ideal e limites explícitos. Usá-las fora de seu perfil aumenta risco de divergência arquitetural e retrabalho.

## 4.1 Claude Code

**Ideal para:**
- Leitura e análise de contexto extenso (múltiplos arquivos, docs longos)
- Revisão arquitetural e consistência entre módulos
- Planejamento de implementação e definição de scope contract
- Refatoração estrutural com raciocínio explícito de trade-offs
- Criação de patches documentais e propostas de mudança
- Migração de código com múltiplas dependências
- Documentação técnica e geração de specs
- Análise de divergência entre código e docs
- Síntese de decisões e `ARCHITECTURE_QUESTION` generation
- QA review de output de outras ferramentas

**Limites conhecidos:**
- Pode superproduzir — gera mais do que o necessário sem constraints explícitas
- Pode inventar escopo quando o prompt é aberto
- Não deve receber tarefas abertas do tipo "implementa o dashboard"
- Não decide produto sozinho — retorna sempre opções e trade-offs, não decisão
- Não executa em produção — só planeja e propõe

**Quando NÃO usar:**
- Correções cirúrgicas de bug isolado (use Codex)
- Protótipos visuais (use Antigravity)
- Quando o contexto necessário é menor do que 10 arquivos (Codex é mais eficiente)

## 4.2 Codex

**Ideal para:**
- Implementação focada em arquivo(s) específico(s) com escopo fechado
- Correções de bug com diffs pequenos e bem definidos
- Criação de testes (unit, integration) a partir de spec clara
- Migrations derivadas de schema aprovado em doc 11
- Funções e handlers isolados com input/output definidos
- Debugging com contexto limitado ao módulo afetado
- Execução de tarefas repetitivas (geração de tipos, mocks, fixtures)
- Aplicação de patches planejados por Claude

**Limites conhecidos:**
- Precisa de contexto limpo — degradação de qualidade com contexto ambíguo ou grande demais
- Não deve receber arquitetura ambígua — segue instrução literalmente
- Não deve criar módulos grandes sem plano prévio (use Claude para planejar primeiro)
- Pode criar acoplamentos ocultos se o scope contract não for explícito
- Não revisa trade-offs arquiteturais — executa o que foi especificado

**Quando NÃO usar:**
- Quando o problema requer raciocínio sobre múltiplos módulos (use Claude)
- Protótipos visuais (use Antigravity)
- Security-critical changes sem revisão humana

## 4.3 Antigravity

**Ideal para:**
- Protótipos visuais de UI em ambiente isolado (rota de lab)
- Exploração de interação, animação e fluxo de usuário
- Validação visual de layouts, componentes e design tokens
- Testes de fluxo com dados mock
- Iteração rápida sobre variações visuais (A/B de UI)
- Páginas isoladas sem lógica de backend sensível
- Whitelabel theming exploration com design tokens

**Limites conhecidos:**
- Output é protótipo — nunca é source-of-truth de lógica de negócio
- Não deve criar lógica de backend, auth ou chamadas a providers
- Não deve definir estrutura de runtime, event schema ou data model
- Não deve hardcodar regras de negócio (pricing, roles, limites de plano)
- Protótipos com dados reais precisam de aprovação antes de serem promovidos

**Quando NÃO usar:**
- Implementação de lógica de backend (use Codex + Technical review)
- Migração de schema (use Codex com spec de doc 11)
- Revisão arquitetural (use Claude)

## 4.4 Outras ferramentas e ferramentas futuras

Novas ferramentas de desenvolvimento assistido por IA (Cursor, Devin, GitHub Copilot Workspace, etc.) podem ser integradas ao workflow, mas precisam:
1. Ser registradas em `tool_usage_policy` com: nome, perfil de uso, limites, aprovador
2. Passar por avaliação de risco de segurança antes de receber acesso ao repositório
3. Operar dentro dos mesmos scope contracts e templates definidos neste protocolo
4. Nunca receber acesso a `.env`, credenciais, dados de produção ou `secret_refs`

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

---

# 5. Tool Selection Matrix

Seleção da ferramenta pela natureza da tarefa. Quando houver dúvida, prefer Claude para planejar e Codex para executar.

| Tipo de tarefa | Ferramenta primária | Secundária | Aprovação mínima |
|----------------|--------------------|-----------:|-----------------|
| Revisão arquitetural | Claude Code | — | Technical |
| Reescrita de documentação | Claude Code | — | PMO_CKOS |
| Análise de trade-offs | Claude Code | — | PMO_CKOS |
| Planejamento de implementação (sem código) | Claude Code | — | PMO_CKOS |
| Correção de bug isolado | Codex | Claude (complexo) | Technical |
| Criação de teste unitário | Codex | — | Technical |
| Teste de integração | Codex | Claude review | Technical |
| Migration derivada de doc 11 | Codex | Claude review + Technical | Founder P0/P1 |
| Handler de evento | Codex | — | Technical |
| Implementação de projection | Codex | Claude review | Technical |
| Protótipo visual de UI | Antigravity | — | PMO_CKOS |
| Componente visual isolado | Antigravity ou Codex | — | PMO_CKOS |
| Refatoração de módulo | Claude (plan) + Codex (exec) | — | Technical |
| Política de segurança | Claude + Technical review | — | Founder obrigatório |
| Widget de dashboard | Antigravity (UI) + Codex (lógica) | Claude review | Technical + PMO |
| QA crítico | Claude + testes + revisão humana | — | QA Lead + Technical |
| Schema novo | Claude (spec) + Codex (migration) | — | Founder obrigatório |
| Agente novo no registry | Claude (spec) | — | Founder + Metacognik |
| UI polish / motion | Antigravity | Claude review | PMO_CKOS |
| Research synthesis | Claude Code | — | Metacognik quando alto risco |
| Security: auth, RLS, tokens | Claude + Technical | — | Founder obrigatório |
| Cost/billing logic | Claude (spec) | Codex (execução) | Founder obrigatório |
| Self-evolving features | Claude (spec apenas) | — | Founder + Metacognik |

---

# 6. Source of Truth Hierarchy

Quando há conflito entre o que a IA gerou e o que está documentado, a hierarquia abaixo resolve. Hierarquia é rígida — item superior sempre vence.

```
1. Documentação CKOS aprovada (docs 10–18 em status approved)
   ↓
2. ARCHITECTURE_PATCH_REPORT (patches registrados como APPLIED)
   ↓
3. QA_DOCUMENTATION_CHECKLIST (critérios de qualidade)
   ↓
4. Decisões do Founder (registradas formalmente com data)
   ↓
5. Aprovação do Technical Lead (registrada no gate correspondente)
   ↓
6. Estado atual do repositório (branch protegida)
   ↓
7. Output de ferramenta de IA (Claude / Codex / Antigravity)
```

**Consequências práticas:**

| Situação | Resolução |
|----------|-----------|
| Codex gera tabela não definida em doc 11 | Rejeitar; registrar como patch sugerido; não fazer merge |
| Antigravity hardcoda lógica de pricing | Rejeitar; remover; registrar em forbidden actions log |
| Claude propõe arquitetura divergente do doc 10 | Gerar `ARCHITECTURE_QUESTION`; não implementar até resolução |
| Tool output contradiz decisão do Founder registrada | Tool output descartado; decisão do Founder prevalece |
| Doc aprovado diz X, repositório atual tem Y | Repositório está errado; registrar como divergência; corrigir |

---

# 7. Execution Handoff Format

Template obrigatório para toda tarefa enviada ao Claude, Codex ou Antigravity. Tarefas sem este formato não são iniciadas.

```markdown
## EXECUTION HANDOFF — [ID da tarefa] — [Data]

### Objetivo
[Uma frase clara descrevendo o que será implementado]

### Modo de execução
[documentation_only | architecture_review | patch_plan_only | code_patch |
 migration_draft | test_generation | ui_lab | qa_review | refactor | rollback_plan]

### Ferramenta
[Claude Code | Codex | Antigravity]

### Documentos de referência obrigatórios
- Doc N §X — [o que consultar]
- Doc M §Y — [o que consultar]

### Arquivos permitidos para modificação
- [path/to/file.ts] — [o que mudar]

### Arquivos proibidos (não tocar)
- [path/to/sensitive.ts] — [motivo]
- [.env, auth/, migrations/prod/] — dados sensíveis

### Constraints
- [constraint 1]
- [constraint 2]

### Não fazer
- [forbidden action 1]
- [forbidden action 2]

### Output esperado
[Descrição do artefato final: patch, spec, prototype, test, etc.]

### Checklist de QA
- [ ] Build passa sem erros
- [ ] Nenhum arquivo fora do escopo foi tocado
- [ ] Testes rodaram
- [ ] Nenhum segredo ou token exposto
- [ ] Rollback documentado

### Expectativa de rollback
[Como desfazer se houver problema]

### Formato do relatório final
Files changed | Summary | Risks | Open questions | Next step
```

---

# 8. Prompt Template — Claude Code

Template mestre para tarefas enviadas ao Claude Code. Usar verbatim, preenchendo os campos.

```markdown
## PAPEL
Você é [Technical Architect | Documentation Reviewer | Implementation Planner | QA Reviewer].
Você NÃO é o Product Owner. Você NÃO decide produto, escopo ou visão.
Você opera dentro da documentação CKOS aprovada.

## CONTEXTO
Sistema: CKOS (AI First Cognitive OS) — event-sourced, CQRS, multi-tenant, whitelabel.
Docs relevantes (leia antes de executar):
- [Doc N v X.Y.Z — motivo]
Repositório atual: [branch] | Estado: [resumo do estado atual]
Decisões anteriores: [lista de decisões já tomadas relevantes para esta tarefa]

## TAREFA
[Uma frase única e clara. Não mais de 2 linhas.]

## ESCOPO
Arquivos que PODE modificar:
- [arquivo 1] — [o que mudar]
- [arquivo 2] — [o que mudar]

Arquivos PROIBIDOS:
- [arquivo] — [motivo]
- Nunca: .env, production databases, auth tokens, secret_refs

Docs que DEVE seguir:
- [Doc N §X] — [qual regra segue]

## CONSTRAINTS
- [constraint 1]
- [constraint 2]
[Quantas forem necessárias — seja específico]

## NÃO FAZER
- Não expandir escopo além do listado em ESCOPO
- Não criar tabelas, módulos ou agentes não definidos nos docs
- Não implementar fora dos gates aprovados (ver doc 17)
- Não tomar decisão de produto silenciosamente
- Não alterar arquivos de auth, security, RLS ou billing sem aprovação explícita
- [outros proibições específicas da tarefa]

## CRITÉRIOS DE APROVAÇÃO
- [critério 1]
- [critério 2]

## CRITÉRIOS DE REJEIÇÃO
- [critério de rejeição 1]
- [critério de rejeição 2]

## RELATÓRIO FINAL OBRIGATÓRIO
Ao concluir, entregue:
```
FILES_CHANGED: [lista de arquivos modificados]
SUMMARY: [o que foi feito em 3–5 linhas]
ARCHITECTURE_REFERENCES: [docs e seções seguidas]
RISK_LEVEL: [P0 | P1 | P2 | P3 | P4]
TESTS_RUN: [lista de testes executados]
ROLLBACK: [como desfazer]
OPEN_QUESTIONS: [perguntas arquiteturais não resolvidas]
NEXT_STEP: [próxima ação recomendada]
OUT_OF_SCOPE_FOUND: [itens encontrados mas não implementados]
```
```

---

# 9. Prompt Template — Codex

Template mestre para tarefas enviadas ao Codex. Codex recebe scope fechado — sem ambiguidade.

```markdown
## OBJETIVO TÉCNICO
[Uma frase técnica única. Ex: "Criar handler para evento NodeCreated em /src/events/node.ts"]

## ARQUIVOS ALVO
- [/path/to/file.ts] — [o que fazer exatamente]
- [/path/to/test.ts] — [quais testes criar]

## DIFFS ESPERADOS
[Descrição do que deve mudar por arquivo. Pode ser pseudocódigo ou descrição funcional.]

Arquivo 1: adicionar função `handleNodeCreated(event: NodeCreatedEvent): void`
Arquivo 2: adicionar test `it('emits NodeCreated with tenant_id', ...)`

## TESTES ESPERADOS
- [test 1]: [o que valida]
- [test 2]: [o que valida]

## COMANDOS PERMITIDOS
```bash
pnpm typecheck
pnpm test --filter [package]
pnpm --filter [package] build
```

## COMANDOS PROIBIDOS
- `git push` sem revisão
- `DROP TABLE` ou qualquer DDL destrutivo
- Modificar `.env` ou arquivos de configuração de produção
- Acessar banco de dados de produção diretamente
- Instalar dependências não aprovadas (`npm install` / `pnpm add` sem verificação)

## LIMITE DE ESCOPO
NÃO tocar:
- [arquivo proibido 1]
- [arquivo proibido 2]
NÃO criar:
- Novos módulos fora do listado
- Novas tabelas (precisam de patch aprovado em doc 11)
- Novos agentes (precisam de taxonomia e aprovação)

## SCHEMA DE REFERÊNCIA
[Colar schema relevante do doc 11 quando a tarefa envolve persistência]

## RELATÓRIO FINAL
```
FILES_CHANGED: [lista exata de arquivos]
BUILD_STATUS: [pass | fail | partial]
TEST_STATUS: [N passed | N failed | not run]
RISKS: [lista de riscos técnicos]
ROLLBACK: [comando ou instrução para reverter]
NEXT_STEP: [próxima ação]
```
```

---

# 10. Prompt Template — Antigravity

Template mestre para tarefas enviadas ao Antigravity. Contexto visual — sem backend.

```markdown
## OBJETIVO VISUAL
[Uma frase descrevendo o UI a criar. Ex: "Protótipo do widget Project Pulse com dados mock"]

## ROTA ISOLADA
[/lab/pulse-widget] — rota de protótipo, não de produção

## COMPONENTES PERMITIDOS
- [design system ou biblioteca de componentes]
- [tokens de design disponíveis]

## DESIGN SYSTEM
- Glassmorphism dark como fallback CK (quando sem whitelabel)
- Tokens: [listar tokens relevantes]
- Sem cores hardcodadas — use tokens
- Sem fontes hardcodadas — use variável CSS

## REFERÊNCIAS VISUAIS
- [screenshot path ou URL]
- [wireframe reference]
- [doc 14 §X — descrição do widget]

## PROIBIDO
- Nenhuma lógica de backend
- Nenhuma chamada direta a provider (OpenAI, Anthropic, etc.)
- Nenhum dado real de usuário ou projeto sem mascaramento
- Nenhum dado mock sem label [MOCK] visível durante dev
- Nenhuma source-of-truth criada no frontend
- Nenhum controle de admin visível para role client/viewer
- Nenhuma ação irreversível sem modal de confirmação
- Nenhum token, secret ou actor_id exposto
- Nenhum hardcode de lógica de pricing ou plano

## CRITÉRIOS DE UX
- [mobile readable?]
- [acessibilidade mínima: aria-labels, contraste]
- [estado vazio, loading, erro — todos mapeados?]
- [responsividade: mobile, tablet, desktop]

## RELATÓRIO FINAL
```
COMPONENTS_CREATED: [lista]
ROUTE: [rota do protótipo]
MOCK_DATA_USED: [lista de dados mock utilizados]
UX_NOTES: [observações sobre UX, estados, interações]
PRODUCTION_READINESS: [o que falta para promover ao prod]
RISKS: [hardcodes, acoplamentos, dependências não aprovadas]
NEXT_STEP: [próxima ação]
```
```

---

# 11. Allowed Execution Modes

Cada sessão de trabalho com ferramenta de IA começa com declaração explícita do modo. Misturar modos na mesma sessão é proibido.

| # | Modo | Descrição | Ferramenta | Aprovação | Risco |
|---|------|-----------|------------|-----------|-------|
| 1 | `documentation_only` | Ler e escrever documentação; sem código | Claude | PMO_CKOS | Baixo |
| 2 | `architecture_review` | Analisar arquitetura existente; sem código | Claude | Technical | Baixo |
| 3 | `patch_plan_only` | Propor patch sem aplicar | Claude | PMO_CKOS | Baixo |
| 4 | `code_patch` | Aplicar patch específico e fechado | Codex / Claude | Technical (P2+) / Founder (P0–P1) | Médio |
| 5 | `migration_draft` | Rascunhar migration a partir de doc 11 | Codex | Technical obrigatório | Alto |
| 6 | `test_generation` | Criar testes para código existente | Codex | Technical | Médio |
| 7 | `ui_lab` | Protótipo visual em rota isolada | Antigravity | PMO_CKOS | Baixo |
| 8 | `qa_review` | Revisar e reportar; sem implementar correções | Claude | QA Lead | Baixo |
| 9 | `refactor` | Melhorar estrutura sem mudar comportamento | Claude + Codex | Technical + revisão diffs | Alto |
| 10 | `rollback_plan` | Documentar e testar rollback | Claude / Codex | Technical antes de executar | Médio |

**Regras de modo:**
- Toda sessão começa com a declaração: `MODO: [nome]`
- Nenhuma tarefa pode mudar de modo sem declarar explicitamente e parar para re-aprovação
- `code_patch` e `migration_draft` requerem scope contract antes de iniciar
- `ui_lab` nunca é promovido a produção sem passar por `code_patch` review
- `refactor` é o modo de maior risco — requer review de diffs completo antes de merge

---

# 12. Forbidden Actions

As ações abaixo são proibidas para qualquer ferramenta de IA em qualquer contexto, sem exceção. Qualquer uma delas detectada durante review → task interrompida + registro de incidente.

| # | Ação proibida | Motivo |
|---|---------------|--------|
| FA1 | Criar backend sensível sem approval explícita | P0 de segurança |
| FA2 | Criar migration sem schema aprovado em doc 11 | Divergência de data model |
| FA3 | Alterar security, RLS ou auth sem doc 12 e Technical approval | P0 de segurança |
| FA4 | Criar UI que grava estado diretamente (sem evento → runtime) | Viola princípio event-driven |
| FA5 | Expor token, API key, actor_id ou provider no frontend ou em logs | P0 de segurança |
| FA6 | Hardcodar projeto específico, tenant ou org_id no core do sistema | Viola tenant isolation |
| FA7 | Chamar agente ou provider diretamente da UI (sem passar por `/api/...`) | Viola arquitetura de runtime |
| FA8 | Ignorar ou bypasear policy_engine em qualquer fluxo | Viola deny-by-default |
| FA9 | Escrever diretamente em banco de produção durante desenvolvimento | P0 operacional |
| FA10 | Apagar dados sem rollback documentado e aprovado | P0 de integridade |
| FA11 | Mudar lógica de auth sem approval do Founder | P0 de segurança |
| FA12 | Inventar tabela, enum ou campo sem registrar como patch sugerido | Divergência de data model |
| FA13 | Implementar billing ou créditos sem doc `24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md` aprovado | Gap documental bloqueante |
| FA14 | Implementar self-evolving sem aprovação formal do Founder + Metacognik | Viola Fase 12 do doc 17 |
| FA15 | Criar agente fora da taxonomia registrada | Viola agent registry |
| FA16 | Fazer "drive-by refactor" — alterar arquivos fora do scope enquanto resolve outra tarefa | Escopo não controlado |
| FA17 | Instalar dependência npm/pnpm sem aprovação técnica | Risco de supply chain |
| FA18 | Usar Manus como source-of-truth no runtime ou event store | Viola status de Manus (doc 18 §4) |
| FA19 | Criar collector externo não listado em `collectors_allowlist` | Viola política de research (doc 18 §16) |
| FA20 | Fazer push para branch protegida sem PR e review | Viola branch policy |

---

# 13. Patch Governance

Toda alteração — código, schema, configuração, documentação — deve produzir um patch summary antes de merge. Patches sem summary são rejeitados automaticamente.

## 13.1 Formato de patch summary

```markdown
## PATCH SUMMARY — [ID] — [Data]

### Tipo
[code | schema | config | documentation | test | refactor | rollback]

### Files Changed
- [arquivo 1] — [descrição da mudança]
- [arquivo 2] — [descrição da mudança]

### Architecture References
- [Doc N §X] — [qual regra foi seguida]
- [ARCHITECTURE_PATCH_REPORT §Y] — [patch relacionado]

### Risk Level
[P0 — quebra produção / P1 — altera fluxo central / P2 — componente importante / P3 — visual ou copy / P4 — documentação]

### Tests Run
- [tipo de teste]: [pass | fail | not applicable]

### Rollback Plan
[Instrução específica para reverter — não "só faz git revert", mas o que exatamente reverter e como]

### Open Issues
- [issue 1 — o que ficou em aberto]

### Out of Scope Found
- [item encontrado mas não implementado — registrar para backlog]

### Next Recommended Step
[Uma ação clara]
```

## 13.2 Classificação de risco e fluxo de aprovação

| Risk Level | Trigger | Aprovação |
|------------|---------|-----------|
| P0 | Quebra produção, auth, pagamento, dados, contratos | Founder obrigatório + rollback testado |
| P1 | Altera fluxo central, runtime, schema crítico | Founder + Technical |
| P2 | Altera componente importante (widget, handler, projection) | Technical + PMO_CKOS |
| P3 | Visual, copy, configuração não crítica | PMO_CKOS |
| P4 | Documentação sem alteração de código | Auto com revisão posterior |

---

# 14. File Scope Rules

Regras para controle de quais arquivos uma ferramenta pode tocar em cada sessão.

**R1 — Scope contract antes de executar:**
Antes de qualquer `code_patch`, listar explicitamente: arquivos permitidos, arquivos proibidos, arquivos de referência (só leitura). Nenhum arquivo fora desta lista é tocado.

**R2 — Sem drive-by refactor:**
Se a ferramenta detectar algo fora do escopo que "merece melhorar", registrar em `OUT_OF_SCOPE_FOUND` — nunca implementar silenciosamente.

**R3 — Design system protegido:**
Arquivos de design system, tokens, variáveis globais de estilo não são alterados sem autorização explícita de design review.

**R4 — Enums centrais protegidos:**
Alterar `event_type`, `node_type`, `role`, `status`, `edge_type` ou qualquer enum central requer patch documentado em doc 11 primeiro.

**R5 — Auth e security imutáveis sem gate:**
Arquivos de middleware de auth, RLS policies, permissões de role não são tocados sem Gate D aprovado (doc 17 §20).

**R6 — Migrations isoladas:**
Migrations ficam em pasta isolada e não são misturadas com migrations de outros patches. Uma migration por patch.

**R7 — Produção off-limits:**
Nenhuma ferramenta tem acesso direto ao banco de produção, ao `.env` de produção ou a arquivos de configuração de produção durante desenvolvimento.

---

# 15. Branch and Version Strategy

## 15.1 Tipos de branch

| Branch | Quando usar | Quem cria | Merge target |
|--------|-------------|-----------|--------------|
| `feature/[scope]-[desc]` | Nova feature aprovada | Developer | `main` via PR |
| `patch/[doc-ref]-[desc]` | Correção específica de bug ou schema | Developer | `main` via PR |
| `docs/[doc-id]-[desc]` | Atualização documental | Developer / Claude | `main` via PR |
| `lab/[component]-[desc]` | Protótipo visual Antigravity | Developer | Nunca direto para main |
| `refactor/[module]-[desc]` | Refatoração aprovada | Developer | `main` via PR com diff review |
| `security/[fix]-[desc]` | Security fix | Technical Lead | `main` via PR + security review |

**Nunca:** commit direto em `main`. Nunca: lab branch promovida a main sem code_patch review.

## 15.2 Versionamento documental

- Docs de arquitetura (10–18): `X.Y.Z` — Major.Minor.Patch
  - Major: reescrita de escopo completo
  - Minor: novas seções ou mudanças arquiteturais
  - Patch: correções, atualizações menores, micro-patches de governança
- ARCHITECTURE_PATCH_REPORT: registro cumulativo, não versionado isoladamente
- Changelog obrigatório no final de cada doc (seção `## Patch X.Y.Z — [descrição]`)

## 15.3 Regra de changelog

Todo merge de `docs/` branch adiciona entrada de changelog no doc alterado com:
- Versão nova
- Data
- O que mudou (3–5 bullets máximo por patch)

---

# 16. Testing Rules

Toda implementação requer teste correspondente antes de considerar completa. "Funciona no meu ambiente" não é evidência.

## 16.1 Hierarquia de testes obrigatórios por tipo de mudança

| Tipo de mudança | Testes obrigatórios |
|-----------------|---------------------|
| Schema novo (tabela, campo) | Migration test (up + down) + RLS test |
| Handler de evento | Unit test + event routing test |
| Projection nova | Projection test (dados corretos + permission filter) |
| Policy change | RLS/policy test com user sem permissão (deve bloquear) |
| Agent routing | Agent routing test (correct agent selected for task_type) |
| Model routing | Model router test (correct model for complexity + cost) |
| Cost tracking | Cost guard test (reservation antes de run; block se insuficiente) |
| UI component | Typecheck + UI smoke test |
| API endpoint | Integration test + auth test |
| Refactor | Regression test suite (mesmos outputs de antes) |

## 16.2 Tipos de teste e quando são obrigatórios

| Tipo | Quando obrigatório | Ferramenta |
|------|--------------------|------------|
| `typecheck` | Sempre, antes de qualquer PR | `pnpm typecheck` |
| `lint` | Sempre | `pnpm lint` |
| `unit tests` | Qualquer nova função ou handler | framework do projeto |
| `integration tests` | Novos endpoints, projections, workflows | framework do projeto |
| `RLS/policy tests` | Qualquer mudança em tabela ou role | testes com usuário sem permissão |
| `event tests` | Qualquer novo event type ou handler | simular event → verificar consumer |
| `projection tests` | Qualquer nova ou alterada projection | dados corretos + permission filter |
| `agent routing tests` | Mudança no agent_registry ou routing logic | simular intent → verificar agente selecionado |
| `model router tests` | Mudança no model_router | simular task_type → verificar modelo selecionado |
| `cost guard tests` | Mudança em créditos, reservas ou billing | simular run com saldo insuficiente |
| `UI smoke tests` | Qualquer mudança em UI de produção | rota acessível, sem erro de console |

---

# 17. AI Output Review Protocol

Nenhum output de ferramenta de IA vai direto para produção. Todo output passa por review proporcional ao risco.

## 17.1 Níveis de review por tipo de output

| Tipo de output | Review obrigatório | Critério de aprovação |
|----------------|--------------------|-----------------------|
| Documentação (sem código) | PMO_CKOS | Consistência com docs anteriores |
| Spec de implementação / patch plan | Technical | Viabilidade + consistência arquitetural |
| Code patch (P3–P4) | Technical | Build passa + scope respeitado |
| Code patch (P1–P2) | Technical + PMO_CKOS | Acima + teste + rollback |
| Migration de schema | Technical + Founder P0 | Rollback testado + RLS verificado |
| Security change | Technical + Founder | Security checklist completo |
| Agent ou policy change | Founder + Metacognik | Sem self-escalation; audit trail |
| UI prototype | PMO_CKOS | Sem backend; dados mock labelled; whitelabel ok |
| Research synthesis de alto risco | Metacognik | Evidências citadas; confidence score adequado |

## 17.2 Checklist de review de AI output

Antes de aprovar qualquer output de ferramenta de IA:

```
[ ] Escopo foi respeitado? (nenhum arquivo fora do scope contract)
[ ] Alguma tabela nova foi criada sem estar em doc 11? → Rejeitar
[ ] Algum segredo, token ou credencial foi exposto? → Rejeitar imediatamente
[ ] RLS foi mantido em todas as tabelas novas? → Verificar
[ ] Events foram usados para mudanças de estado? → Verificar
[ ] Frontend lê apenas de projections? → Verificar
[ ] Policy engine não foi bypassado? → Verificar
[ ] Testes foram rodados? → Verificar status
[ ] Rollback foi documentado? → Verificar
[ ] Algum drive-by refactor foi feito? → Identificar e separar
[ ] Dependência nova foi instalada? → Verificar necessidade e aprovação
```

---

# 18. Context Management

A qualidade do output de IA é diretamente proporcional à qualidade do contexto fornecido. Contexto mal estruturado produz output divergente.

## 18.1 O que incluir no contexto

| Item | Como incluir | Prioridade |
|------|-------------|-----------|
| Docs de arquitetura relevantes | Citar seção específica (ex: "doc 10 §5.2") | Alta |
| Estado atual do módulo | Snippet do arquivo, não o arquivo inteiro | Alta |
| Decisões anteriores | Lista de 3–5 decisões relevantes com data | Alta |
| Constraints explícitas | Lista de proibições específicas da tarefa | Alta |
| Exemplo de output esperado | Pseudocódigo ou estrutura esperada | Média |
| Exemplos de erro a evitar | O que foi tentado antes e falhou | Média |
| Schema relevante | Colar do doc 11 quando aplicável | Alta (se persistência) |

## 18.2 O que evitar no contexto

| Antipadrão | Por que é prejudicial |
|------------|----------------------|
| Mandar docs inteiros sem indicar seção | Ferramenta processa tudo com igual peso |
| Docs contraditórios sem explicar qual prevalece | Ferramenta escolhe arbitrariamente |
| Múltiplas tarefas em um único prompt | Prioridade ambígua; escopo expandido |
| Misturar design, backend, security e copy no mesmo prompt | Ferramenta não consegue travar escopo |
| Contexto de 3 semanas atrás sem atualização | Ferramenta usa estado desatualizado |
| "Você sabe o que fazer" sem spec | Ferramenta inventa arquitetura |
| Colar erro sem contexto do módulo | Ferramenta faz suposições erradas |

## 18.3 Tamanho de contexto por ferramenta

| Ferramenta | Sweet spot | Máximo recomendado |
|------------|-----------|-------------------|
| Claude Code | 5–15 arquivos / 3–5 docs referenciados | Quanto caber no context window com prioridade |
| Codex | 1–3 arquivos alvo + 1 schema de referência | Sem arquivos extras não relacionados |
| Antigravity | 1 rota/componente + visual references | Sem lógica de backend no contexto |

---

# 19. Anti-Entropy Rules

Regras para evitar a degradação progressiva da qualidade arquitetural ao longo de muitas sessões de implementação.

**AE1 — Uma tarefa por vez:**
Nunca iniciar nova tarefa enquanto a anterior não tiver patch summary aprovado e PR fechado.

**AE2 — Um gate por vez:**
Não avançar para a próxima fase sem o gate anterior formalmente aprovado (doc 17 §20).

**AE3 — Um documento ou módulo por vez:**
Nunca alterar dois módulos não relacionados na mesma sessão.

**AE4 — Nada de "aproveita e ajusta":**
"Enquanto você está aqui, melhora também o X" → Bloquear. Registrar em `OUT_OF_SCOPE_FOUND`. Criar nova tarefa separada.

**AE5 — Nada de criar pasta nova sem registro:**
Qualquer nova pasta de módulo precisa de entrada no `ARCHITECTURE_MAP` equivalente e no ARCHITECTURE_PATCH_REPORT.

**AE6 — Nada de duplicar lógica:**
Antes de criar nova função ou módulo, confirmar que não existe equivalente. Se existir: reusar, não duplicar.

**AE7 — Nada de inventar nomes:**
Enums, status, event types, node types, edge types — tudo derivado dos docs aprovados. Nunca inventar nome novo sem patch sugerido.

**AE8 — Nada de abandonar file tree:**
Arquivos criados e não deletados viram dívida técnica. Cada tarefa entrega filetree limpa — arquivos temporários, mocks e labs são removidos ou movidos.

**AE9 — Não misturar prototype e produção:**
Código de lab (`lab/`, `prototype/`) nunca é importado por código de produção diretamente. Promover lab para produção é uma tarefa separada com code_patch review.

**AE10 — Sempre documentar antes de implementar:**
Se o que vai ser implementado não está documentado nos docs 10–18, a implementação espera. A ordem é sempre: doc → patch aprovado → implementação.

---

# 20. Documentation Sync Rules

A divergência entre código e documentação é um dos principais vetores de entropia no CKOS.

**Quando código diverge de documentação:**
1. Parar a implementação
2. Registrar: `DIVERGENCE_DETECTED: [arquivo] diverge de [Doc N §X] — [descrição]`
3. Propor patch documental ou patch de código (não ambos sem approval)
4. Não implementar workaround silencioso que "funciona mas não segue o doc"
5. Escalar para Technical se a divergência for arquitetural

**Quando documentação está ambígua:**
1. Gerar `ARCHITECTURE_QUESTION`:
```
ARCHITECTURE_QUESTION — [Data]
Doc: [N §X]
Ambiguidade: [descrição exata do que está impreciso]
Implicação: [o que cada interpretação causaria]
Decisão necessária: [quem deve decidir — Technical ou Founder]
```
2. Não inventar resolução
3. Aguardar resposta antes de implementar

**Quando implementação revela gap não coberto por nenhum doc:**
1. Registrar como patch sugerido no ARCHITECTURE_PATCH_REPORT
2. Implementar workaround temporário com flag `// TODO: awaiting doc [N] patch` no código
3. Nunca tratar workaround como solução definitiva

---

# 21. Runtime-Specific Rules

Regras derivadas diretamente dos docs 10–16 que nenhuma ferramenta pode violar.

| Regra | Descrição | Referência |
|-------|-----------|-----------|
| R-RT1 | Frontend nunca chama provider diretamente | Doc 10 §5.2; doc 17 R3 |
| R-RT2 | Toda mudança de estado começa com evento no event store | Doc 10 §5.3; doc 17 R1 |
| R-RT3 | Frontend lê apenas de projections — nunca de tabelas de domínio | Doc 10 §5.12; doc 17 R2 |
| R-RT4 | Policy engine é executado antes de qualquer ação de domínio | Doc 12 §4; doc 17 R4 |
| R-RT5 | RLS ativo em todas as tabelas — `tenant_id` como pré-condição | Doc 12; doc 17 R5 |
| R-RT6 | Vector search com namespace como WHERE, nunca pós-filtro | Doc 18 §17; doc 17 R6 |
| R-RT7 | Agentes não alteram suas próprias permissões | Doc 04; doc 17 R7 |
| R-RT8 | Node Canvas não escreve no banco — apenas emite eventos | Doc 16 §4 |
| R-RT9 | Dashboard widgets leem de projections — não recalculam dados | Doc 14 §8 |
| R-RT10 | Command Center não executa pesquisa — redireciona para research pipeline | Doc 15 §5.2; doc 18 §11 |
| R-RT11 | Credit reservation antes de qualquer agent run | Doc 11 §33; doc 17 R12 |
| R-RT12 | Audit log é append-only — sem UPDATE ou DELETE | Doc 11 §5; doc 17 R13 |
| R-RT13 | Event store é append-only — sem UPDATE ou DELETE | Doc 10 §5.3; doc 17 R1 |
| R-RT14 | SSE channel scoped a project_id + user_id — nunca broadcast | Doc 10 §5.12 |

---

# 22. UI/UX-Specific Rules

Regras para qualquer ferramenta trabalhando em interfaces visuais — Antigravity, Codex ou Claude em modo UI.

| Regra | Descrição |
|-------|-----------|
| R-UI1 | Whitelabel sempre: design tokens, não cores hardcodadas |
| R-UI2 | CK fallback: glassmorphism dark quando sem whitelabel ativo |
| R-UI3 | Acessibilidade mínima: aria-labels, contraste WCAG AA |
| R-UI4 | Mobile readable: todo dashboard e canvas funcional em tela < 768px (read-only ok) |
| R-UI5 | Dados mock sempre labelled com [MOCK] visível em ambiente de dev |
| R-UI6 | Nenhum dado hardcodado de projeto, tenant ou org |
| R-UI7 | Nenhum nome de provider exposto na UI (não "OpenAI", não "Anthropic") |
| R-UI8 | Controles de admin nunca visíveis para role client/viewer |
| R-UI9 | Ações irreversíveis (delete, aprovar, publicar) sempre com modal de confirmação |
| R-UI10 | Estado vazio, loading e erro mapeados para todos os componentes |
| R-UI11 | Frontend nunca expõe actor_id, tenant_id ou token no DOM |
| R-UI12 | Animações respeitam `prefers-reduced-motion` |
| R-UI13 | Nenhuma lógica de autorização no frontend — frontend exibe, backend decide |

---

# 23. Research-Specific Rules

Regras para quando ferramentas de IA são usadas em tarefas de pesquisa ou são alimentadas com output de pesquisa.

| Regra | Descrição | Referência |
|-------|-----------|-----------|
| R-RS1 | Não tratar Manus como infraestrutura CKOS | Doc 18 §4 |
| R-RS2 | Usar Research Capability como destino final; Manus é bootstrap temporário | Doc 18 §4 |
| R-RS3 | Todo claim tem source_ref — sem afirmações sem citação | Doc 18 §3 (evidence-first) |
| R-RS4 | Separar evidência de hipótese — hipóteses são marcadas com confidence < 0.7 | Doc 18 §3 |
| R-RS5 | Registrar freshness de toda evidência usada | Doc 18 §19 |
| R-RS6 | Fonte Tier 5 nunca é base para decisão sem corroboração | Doc 18 §8.2 |
| R-RS7 | Metacognik audita sínteses críticas antes de uso em decisão | Doc 18 §3 (Metacognik-auditable) |
| R-RS8 | PII nunca enviada para fonte externa sem sanitização | Doc 18 §17 |
| R-RS9 | Research runners são server-side only | Doc 18 §17 R4 |
| R-RS10 | Contradições não são forçadas a resolução — são expostas | Doc 18 §20 |

---

# 24. Security-Specific Rules

Qualquer tarefa que toque os itens abaixo requer review técnico e documentação correspondente antes de merge. Sem exceção.

**Itens que requerem security review:**

| Item | Review obrigatório | Doc de referência |
|------|--------------------|------------------|
| Auth middleware | Technical + Founder | Doc 12 §3 |
| RLS policies | Technical | Doc 12 §4 |
| Roles e permissions | Founder + Technical | Doc 12 §5 |
| Secret handling (`secret_refs`) | Technical | Doc 12 §6; doc 17 R4 |
| Tenant scope queries | Technical | Doc 12 §4; doc 17 R5 |
| Billing / créditos | Founder | Doc 11 §33 |
| Provider tokens | Technical | Doc 17 R4 |
| Collectors e PII | Technical + revisão legal | Doc 18 §17 |
| JWT e sessão | Technical + Founder | Doc 12 §3 |
| Dados classificados como `confidential` | Technical + Founder | Doc 12 §7 |

**Checklist de security review:**
```
[ ] Nenhum segredo em código ou log
[ ] RLS ativo em novas tabelas
[ ] Tenant_id como pré-condição em todas as queries
[ ] JWT não exposto no frontend
[ ] Tokens resolvidos via secret_refs
[ ] PII sanitizada antes de envio externo
[ ] Auth mudança aprovada pelo Founder
[ ] Agente não pode alterar própria permissão
```

---

# 25. Cost and Credits Rules

Qualquer uso de modelo, collector ou ferramenta que gere custo deve seguir estas regras.

| Regra | Descrição | Referência |
|-------|-----------|-----------|
| R-CC1 | Todo run com custo tem `credit_reservation` antes de executar | Doc 11 §33; doc 17 R12 |
| R-CC2 | Custo é atribuível a `project_id + org_id + agent_run_id` | Doc 13 §cost_ledger |
| R-CC3 | Run com custo acima de threshold → `ApprovalRequested` antes de executar | Doc 17 §12; doc 18 §18 |
| R-CC4 | Bloqueio por crédito insuficiente nunca é silencioso — emite evento | Doc 17 R12 |
| R-CC5 | Model selection considera `cost_budget` do projeto | Doc 10 §5.7 |
| R-CC6 | Collector run pré-aprovado por `project_lead+` | Doc 18 §16 |
| R-CC7 | Fallback barato disponível quando custo excede threshold | Doc 18 §18 |
| R-CC8 | Custo de dev tools (Claude, Codex, Antigravity) é separado de custo de runtime | Operational distinction |

---

# 26. QA Report Format

Formato padrão que toda ferramenta deve entregar ao concluir uma tarefa. QA reports incompletos são devolvidos.

```markdown
## QA REPORT — [ID] — [Data] — [Ferramenta: Claude/Codex/Antigravity]

### Files Changed
| Arquivo | Tipo de mudança | Risk level |
|---------|----------------|------------|
| [arquivo] | [criado/alterado/deletado] | [P0-P4] |

### Summary
[3–5 linhas descrevendo o que foi feito]

### Tests Run
| Tipo | Status | Observações |
|------|--------|-------------|
| typecheck | [pass/fail] | — |
| lint | [pass/fail] | — |
| unit tests | [N passed / N failed] | — |
| [outros] | [status] | — |

### Risks
- [risco 1]: [probabilidade] — [mitigação proposta]
- [risco 2]: [probabilidade] — [mitigação proposta]

### Assumptions Made
- [assumpção 1 que o implementador fez e pode estar errada]

### Skipped Items
- [o que foi pulado e por quê]

### Out of Scope Found
- [item encontrado fora do escopo — não implementado]

### Rollback
[Instrução específica e testável para reverter]

### Next Step
[Uma ação clara e específica]
```

---

# 27. MVP P0 — AI Development Flow

Sequência de implementação P0 usando as ferramentas de IA, seguindo os gates do doc 17.

```
Passo 1 — Migrations base (Codex + Technical review)
  → Schema de doc 11 §1–§15 em migrations versionadas
  → Cada migration com test up + down
  → RLS ativo desde o primeiro migration

Passo 2 — Event store (Codex + Claude review)
  → Tabela `events` append-only
  → Tabela `audit_log` append-only
  → Constraints de banco verificadas

Passo 3 — Auth e policies mínimas (Codex + Technical + Founder)
  → JWT middleware
  → 4 roles mínimas (viewer, contributor, project_lead, admin)
  → Deny-by-default verificado com teste

Passo 4 — Projection engine mínima (Claude plan + Codex exec)
  → ui_projection_engine basic
  → SSE infrastructure para 3 projections P0
  → Permission filter antes de push

Passo 5 — Command Center MVP (Codex + Claude review)
  → intent_router com 6 slash commands P0
  → research_intent_router conectado
  → command_history table

Passo 6 — Project Dashboard P0 (Antigravity lab → Codex prod)
  → 5 widgets P0 (Pulse, Decision Queue, AI Activity, Node Health, Cost)
  → Cada widget lendo de projection correspondente
  → dashboard_preferences table

Passo 7 — Node Canvas P0 (Antigravity lab → Codex prod)
  → Canvas básico: criar node, ver node, conectar nodes
  → canvas_graph projection SSE
  → node_edges table

Passo 8 — Agentes iniciais (Claude spec + Technical approval)
  → Cognik no agent_registry
  → Metacognik no agent_registry
  → model_router com 2 modelos configurados

Passo 9 — Research P0 (Codex + Claude review)
  → rag_retriever básico
  → web_research_runner (Perplexity)
  → evidence_items table + research_runs table

Passo 10 — QA gates (Claude QA + QA Lead + Founder)
  → Todos os P0 user paths testados (doc 17 §21)
  → Gate I checklist completo
  → Rollback plano testado
```

---

# 28. Failure Modes

| # | Modo de falha | Sintoma | Mitigação |
|---|---------------|---------|-----------|
| FM1 | Tool invents architecture | Tabela, módulo ou padrão não definido em nenhum doc | Scope contract explícito; review pré-merge com doc check |
| FM2 | Tool touches forbidden file | Auth, RLS, billing alterados sem approval | File scope rules declaradas antes de executar; review de diffs |
| FM3 | Tool creates duplicate component | Função ou módulo que já existe sob outro nome | Pre-flight search obrigatório antes de criar |
| FM4 | Tool hardcodes data | Tenant_id, project_id, ou preços no código | R-UI6; code review busca por constantes hardcodadas |
| FM5 | Tool bypasses runtime | Frontend chama provider diretamente | R-RT1; integration test verifica flow completo |
| FM6 | Tool exposes provider | Nome de modelo, API key ou endpoint no frontend/log | R-UI7 + R-CC8; log sanitization |
| FM7 | Tool creates table not in doc 11 | Migration com tabela não documentada | Pre-flight doc check; rejeitar migration sem schema em doc 11 |
| FM8 | Tool changes auth silently | Middleware de auth alterado como drive-by | File scope: auth/* proibido sem gate D + Founder |
| FM9 | Tool breaks RLS | RLS removido ou incorreto em nova tabela | RLS test com usuário cross-tenant; CI check |
| FM10 | Tool creates direct agent call | Frontend chama agente sem passar por `/api/intent` | R-RT1; code review verifica imports de SDK de agente no frontend |
| FM11 | Tool creates fake dashboard truth | Widget calcula dados localmente em vez de ler projection | R-RT3 + R-UI13; projection check no review |
| FM12 | Tool ignores cost guard | Run sem `credit_reservation`; saldo negativo possível | R-CC1; test com saldo zerado antes de merge |
| FM13 | Tool adds dependency without approval | `pnpm add` de package não aprovado | FA17; lockfile review antes de merge |
| FM14 | Tool creates UI not whitelabel | Cores hardcodadas, fontes fixas, lógica de brand no core | R-UI1; design token check |
| FM15 | Tool creates untested migration | Migration sem test up/down | Testing rule §16.1; migration sem test → rejected |
| FM16 | Tool updates docs inconsistently | Doc 14 atualizado, doc 10 não; schema diverge | Documentation sync rules §20; checklist de docs relacionados |
| FM17 | Tool causes version drift | Code implementa feature de versão futura não aprovada | Gate check antes de merge; doc version pinned em scope contract |
| FM18 | Tool misses rollback | PR sem rollback plan | QA report format §26 requer rollback; sem rollback → rejected |
| FM19 | Tool over-refactors | Refatoração ampla além do scope declarado | AE3 + AE4; diff review linha por linha |
| FM20 | Tool creates hidden coupling | Módulo A importa módulo B que não deveria saber de A | Dependency review; architecture consistency check |
| FM21 | Tool treats Manus as CKOS infra | Output de Manus vira source em runtime | R-RS1; nenhum `source_type = manus` no event store |
| FM22 | Tool generates synthesis without evidence_ids | Conclusão sem citação usada como base de decisão | R-RS3; synthesis_generator rejeita sem evidence_ids |

---

# 29. Approval Gates

Mapeamento dos gates do doc 17 §20 com as aprovações específicas para atividades de desenvolvimento assistido por IA.

| Gate | Nome | O que requer aprovação de IA tools | Aprovador |
|------|------|------------------------------------|-----------|
| A | Documentation | Todos os docs 10–18 revisados por Claude e aprovados | Founder + Technical + Metacognik |
| B | Schema | Migrations geradas por Codex revisadas e testadas | Technical (+ Founder se P0/P1) |
| C | Event | Event handlers implementados por Codex com testes | Technical + Metacognik |
| D | Policy | RLS e policies implementadas com security review | Founder + Technical |
| E | Workflow | Workflow engine e state machines implementados e testados | Technical + PMO_CKOS |
| F | Agent | Agent registry e model_router implementados | Technical + Metacognik |
| G | Projection | 13 projections implementadas e testadas com permission filter | Technical + PMO_CKOS |
| H | Product | CC + Canvas + Dashboard implementados com Antigravity→Codex flow | Founder + PMO_CKOS + QA Lead |
| I | QA | Todos os P0 paths passando — Claude QA report + QA Lead review | Founder + QA Lead + Metacognik |
| J | Launch | Security audit completo + rollback testado + Founder go/no-go | Founder (obrigatório) + todos |

**Regra de gate para IA tools:**
> Nenhuma ferramenta de IA pode declarar gate como "aprovado". Gates são aprovados por humanos (Founder, Technical, QA Lead) com base no output da ferramenta — não pela ferramenta.

---

# 30. Related Notes

- [[10_SYSTEM_RUNTIME_ARCHITECTURE]] v1.1.1 — event bus, canonical flow; R-RT1 a R-RT14 derivados daqui
- [[11_DATA_MODEL_AND_PERSISTENCE]] v1.2.0 — schema fonte da verdade para migrations; tabelas, enums, RLS
- [[12_SECURITY_PERMISSIONS_AND_DATA_GOVERNANCE]] v1.1.0 — RBAC, ABAC, RLS, secret_refs; fonte das security rules
- [[13_EVALS_OBSERVABILITY_AND_COST_CONTROL]] v1.1.0 — cost_ledger, eval_runner; fonte das cost rules
- [[14_PROJECT_DASHBOARD_ARCHITECTURE]] v1.2.0 — widgets e projections; R-UI e R-RT9 derivados daqui
- [[15_COMMAND_CENTER_ARCHITECTURE]] v1.2.1 — intent_router; R-RT10 derivado daqui
- [[16_NODE_CANVAS_ARCHITECTURE]] v1.2.0 — canvas events; R-RT8 derivado daqui
- [[17_IMPLEMENTATION_PROTOCOL]] v1.2.1 — gates A–J; engineering rules R1–R13; failure modes
- [[18_RESEARCH_PROTOCOL]] v1.0.0 — research capability; R-RS1 a R-RS10 derivados daqui
- [[20_QA_AND_FOUNDER_APPROVAL_PROTOCOL]] — protocolo completo de QA e aprovação
- [[ARCHITECTURE_PATCH_REPORT]] v1.2.1 — registro de patches; referência para divergências
- [[QA_DOCUMENTATION_CHECKLIST]] — checklist de qualidade de documentação
- [[19_CLAUDE_CODEX_EXECUTION_PROTOCOL]] v1.1.0 — doc supersedido; referência histórica apenas

---

## Patch 1.0.0 — Criação do documento

**Supersede:** `19_CLAUDE_CODEX_EXECUTION_PROTOCOL.md` v1.1.0

**O que mudou em relação ao doc anterior:**
- Escopo expandido de 16 para 30 seções com governança completa de desenvolvimento assistido por IA
- Tese central formalizada: "CKOS development must be tool-assisted, not tool-dependent"
- Antigravity adicionado como terceira ferramenta com perfil e template próprios (doc anterior mencionava sem estruturar)
- Tool Selection Matrix (§5): 20+ tipos de tarefa com ferramenta recomendada e aprovação mínima
- Source of Truth Hierarchy (§6): 7 níveis explícitos; AI output no último lugar
- 3 templates de prompt padronizados (§8–§10) para Claude, Codex e Antigravity
- 10 Allowed Execution Modes (§11) com permissão, risco e aprovação por modo
- 20 Forbidden Actions (§12) explícitas e rastreáveis
- Patch Governance format (§13) com classificação de risco P0–P4
- File Scope Rules (§14), Branch Strategy (§15), Testing Rules (§16)
- AI Output Review Protocol (§17) com checklist de 12 pontos
- Context Management (§18): o que incluir, o que evitar, tamanho por ferramenta
- 10 Anti-Entropy Rules (§19) para evitar degradação progressiva
- Documentation Sync Rules (§20): como resolver divergências e ambiguidades
- Runtime (§21), UI/UX (§22), Research (§23), Security (§24), Cost (§25) específicos
- QA Report Format padronizado (§26)
- MVP P0 AI Development Flow sequencial de 10 passos (§27)
- 22 Failure Modes com sintoma e mitigação (§28)
- Approval Gates mapeados aos gates A–J do doc 17 (§29)
