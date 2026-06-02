---
title: DNA System Comparison and Integration Map
file: 02_DNA_SYSTEM_COMPARISON_AND_INTEGRATION_MAP.md
layer: auxiliary
doc_type: pmo_analysis
phase: 000_ROADMAPS
category: consolidation
status: draft
version: 0.1.0
created_at: 2026-06-01
updated_at: 2026-06-01
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers:
  - founder
  - metacognik
approval_required:
  - founder
  - pmo_ckos
confidence: medium
provenance_status: pmo_survey_unverified
source_tool: claude_opus_4_8
purpose: Comparar os 2 sistemas DNA existentes (rascunho ChatGPT vs Human Academy), extrair metodologia aplicável ao CKOS sem copiar, e mapear como o conceito de "DNA" entra nos contextos do CKOS e como a documentação acelera o crescimento do DNA do usuário.
intelligence_level: highest
non_authority_boundary: >
  Documento auxiliar/PMO. Nao e canonico. Nao copia nenhum dos dois sistemas DNA. Nao
  cria docs 28-34, nao altera docs 01-27, nao implementa. Toda adocao de metodologia vira
  patch candidate gated. Material da Human Academy e referencia/benchmark, nao ativo a copiar.
related_notes:
  - 00_CKOS_CONSOLIDATION_MAP_AND_GAP_AUDIT.md
  - ../../000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/README.md
  - ../../000_STUDY_NOTES/DNA_SYSTEM/SUPERAGENT_Director_Visual/DNA/01-DNA-Master.md
  - ../../02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md
  - ../../01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md
  - ../../01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
tags: [dna, comparison, methodology, creative-dna, integration, gate2]
---

# DNA System — Comparação + Mapa de Integração (GATE 2)

> **Princípio:** não copiar nenhum dos dois. Comparar, extrair **metodologia**, e aplicar
> com a vantagem que nenhum dos dois tem: **inteligência, ROI, aprendizado e autonomia**.
> O grande diferencial do CKOS é automatizar o que esses sistemas exigem **manualmente**.

---

## 1. Os dois sistemas, sem confusão

| | **Sistema A — `DNA_system_vault`** | **Sistema B — `SUPERAGENT_Director_Visual` (Human Academy)** |
|---|---|---|
| Origem | Seu rascunho com ChatGPT | Produto da Human Academy, feito para Claude |
| Natureza | **Runtime operacional** CKOS-style (backend-first) | **Creative/Brand DNA de produção de conteúdo** |
| Estrutura | 20 pastas espelhando o canônico (runtime, briefing, question engine, creative DNA core, RAG, skills, transformers…) | "Maestro" + documentos-mestre de disciplina (Voice&Tone, Photography, Visual System, Brand Strategy) + DNA.md + opensquad |
| Forte em | Arquitetura de fluxo, binding nota→backend, heartbeat | **Profundidade de ofício** (canon de copy, fotografia, marca) e padrão de orquestração |
| Fraco em | Qualidade do conteúdo (notas **copy-paste idênticas** — ex. `creative_dna_definition` == `creative_dna_resolver` palavra por palavra) | **Exige participação manual** do founder/creator (discovery, setup wizard, upload de referências, aprovações) |
| Autonomia | Desenha autonomia, não a entrega | Zero autonomia — é assistivo, o humano puxa cada etapa |

**Veredito:** A é redundante com o canônico 01-27 (≈80% sobreposição) mas tem 2 joias; B é a **metodologia de profundidade** que falta ao CKOS. Nenhum é fonte de verdade.

---

## 2. O que extrair de cada um (metodologia, não conteúdo)

### Do Sistema A (rascunho) — **2 joias, descartar o boilerplate**
1. **Creative DNA Core como objeto de 1ª classe** — `creative_dna_object_model`, score, constraints, to-memory/to-roi/to-workflow rules. O canônico **não tem** um objeto "Creative DNA" explícito. → **patch candidate p/ Doc 02 (Object Model) + Doc 05 (Memory)**.
2. **Heartbeat operacional** — `awake → reading_context → asking_questions → planning → executing → auditing → updating_memory → done` com campos mínimos (`run_id`, `confidence`, `cost_so_far`, `evidence_refs`, `next_action`). → **patch candidate p/ Doc 03/10**.
3. ⚠️ **Descartar:** as ~9 notas idênticas do `06_CREATIVE_DNA_CORE`. Promover só o object model curado, não o copy-paste.

### Do Sistema B (Human Academy) — **3 padrões metodológicos**
1. **"Discipline-Master Document" pattern** — cada disciplina (copy, foto, marca) é um documento profundo com: doutrina + literatura canônica + princípios + anti-padrões exaustivos + parâmetros de qualidade (nota 0-10) + testes finais + checklist de quando consultar. → **é exatamente o que uma Skill de alto nível deveria ser** no Doc 06. Hoje nossas skills são rasas; estas são de nível sênior.
2. **"Maestro" orchestration** — um orquestrador que **consulta a skill-mestre antes de produzir e antes de auditar**, posiciona o output numa matriz tonal/contextual, roda anti-pattern scan, e só entrega se passa nos testes. → mapeia direto em **Cognik (consulta skill) + Metacognik (audita contra os critérios)**.
3. **Discovery → DNA build → calibração contínua** — protocolo de descoberta que constrói o DNA da marca e o calibra a cada peça (casos antes/depois). → metodologia para o **crescimento progressivo do DNA** (Seção 4).

---

## 3. A inversão CKOS: de manual para autônomo

O ponto central que você levantou. A Human Academy é poderosa mas **o humano é o motor**: ele faz discovery, sobe referências, aprova, calibra. O CKOS inverte isso:

| Etapa | Human Academy (manual) | **CKOS (AI-first, autônomo + gated)** |
|---|---|---|
| Descobrir DNA | Founder responde wizard | **Question Engine** (Doc 03/briefing) gera perguntas inteligentes só quando o ganho de clareza justifica |
| Reunir referências | Founder faz upload | **Research proativo** (Doc 18/26: OpenRouter, Perplexity, Apify) coleta evidência real |
| Aplicar DNA | Maestro consulta, humano aprova cada peça | **Cognik** aplica + **Metacognik** audita; aprovação só em risco/custo acima do teto (Doc 04) |
| Calibrar | Founder registra antes/depois | **Feedback→Learning loop** (Doc 22) promove acertos a memória, erros a policy |
| Medir | — (não existe) | **ROI** (Doc 21): consistência com DNA, retrabalho evitado, reuso |

> Em uma frase: **a Human Academy te dá um copiloto de marca; o CKOS deve dar um sistema que cresce o DNA sozinho e só te chama quando importa.**

---

## 4. "Creative DNA" como objeto vivo do CKOS — como ele entra em cada contexto

Você perguntou: como o DNA entra ao criar projeto, no briefing, ou numa missão que ainda não tem DNA. Proposta de modelo (study-only, vira patch candidate):

**Estados do DNA** (maturidade progressiva):
```txt
DNA-0 (vazio)  → DNA-1 (sementes)  → DNA-2 (parcial)  → DNA-3 (maduro)  → DNA-vivo (auto-calibrado)
nenhum sinal     1ª intenção+        briefing+research   múltiplos projetos   feedback loop ativo
                 perguntas           consolidados        + outputs aprovados   atualiza sozinho
```

**Entrada por contexto:**

| Contexto | Como o DNA entra |
|---|---|
| **Criação de projeto** | `intent_to_project` instancia um **DNA-0**; Question Engine puxa para DNA-1 com 3-5 perguntas de alto ganho |
| **Briefing** | Cada resposta + evidência alimenta o `creative_dna_object_model`; o briefing **é** o primeiro grande salto de maturidade |
| **Missão sem DNA ainda** | **DNA bootstrapping just-in-time**: antes de executar, Cognik checa maturidade; se DNA-0/1, dispara mini-discovery + research proativo escopado à missão, registra como semente, e só então executa. Nunca trava — opera com o DNA que tem e marca confiança. |
| **Qualquer momento** | Todo output aprovado e todo feedback **incrementam** o DNA via memory loop (Doc 05/22). DNA nunca é "preenchido uma vez"; ele acumula. |

**Como a documentação CKOS já potencializa isso** (sistemas que você JÁ tem):
- **Briefing + Perguntas** (Doc 03, briefing_sessions, intelligent_briefing_questions) → motor de descoberta de DNA.
- **Memória + Notas** (Doc 05) → onde o DNA persiste e cresce.
- **Projeto** (Doc 02 object model) → o DNA é atributo vivo do projeto.
- **Research** (Doc 18/26) → enriquece DNA com dados reais, não só LLM.
- **Skills** (Doc 06) → as discipline-master docs viram skills que aplicam o DNA com nível sênior.
- **ROI + Feedback** (Doc 21/22) → fecham o loop de calibração que a Human Academy faz à mão.

O CKOS **acelera** o DNA do usuário porque cada interação (intenção, pergunta, nota, execução, feedback) é um depósito no DNA — sem o usuário ter que "sentar e preencher um wizard".

---

## 5. Onde cada função do DNA mora no canônico (mapa de propriedade)

| Função DNA | Doc canônico dono | Patch candidate (gated)? |
|---|---|---|
| Objeto Creative DNA | Doc 02 Object Model | **Sim** (novo objeto) |
| Persistência/crescimento | Doc 05 Memory | Sim (regras DNA→memory) |
| Skills de disciplina (copy/foto/marca nível sênior) | Doc 06 Skills Registry | **Sim** (elevar profundidade) |
| Orquestração (Maestro) | Doc 03 Agentes (Cognik aplica, Metacognik audita) | Sim (padrão consult-before-produce) |
| Descoberta | Doc 03 briefing/question | Reuso |
| Enriquecimento | Doc 18/26 Research | Reuso |
| Calibração/ROI | Doc 21/22 | Sim (DNA consistency como métrica) |
| Score/constraints/anti-patterns | Doc 06 + Doc 13 (evals/QA) | Sim |

---

## 6. Patch candidates resultantes (todos gated — não aplicados aqui)

| ID | Patch candidate | Doc-alvo | Gate |
|---|---|---|---|
| DNA-PC-1 | Adicionar objeto **Creative DNA** (object model + estados DNA-0..vivo) | Doc 02 | Founder |
| DNA-PC-2 | Regras DNA→memory (crescimento progressivo, negative memory) | Doc 05 | Founder |
| DNA-PC-3 | Elevar Skills a **discipline-master pattern** (doutrina + anti-patterns + score 0-10 + testes) | Doc 06 | Founder |
| DNA-PC-4 | Padrão **consult-before-produce / audit-after** (Cognik+Metacognik como Maestro) | Doc 03 | Founder |
| DNA-PC-5 | **DNA bootstrapping just-in-time** para missões sem DNA | Doc 10 runtime | Founder |
| DNA-PC-6 | Heartbeat operacional com campos mínimos | Doc 03/10 | Founder |
| DNA-PC-7 | DNA-consistency como métrica de ROI/QA | Doc 21/13 | Founder |

Estes alimentam diretamente o futuro **Doc 28** (Notes/RAG/Knowledge) e o **Backend MVP thin-slice** (arquivo 03).

---

## 7. Riscos / armadilhas

- **Copiar a Human Academy** → violação de origem + perda do diferencial. Só metodologia.
- **Importar o `DNA_system_vault` em massa** → traz o copy-paste e duplica o canônico. Curar, não importar.
- **DNA virar wizard manual** → mataria o AI-first. DNA tem que crescer por uso, não por formulário.
- **Travar missão sem DNA** → nunca. Opera com o que tem + marca confiança baixa + enriquece em background.

---

## 8. Critérios de aceitação

- Identifica corretamente os 2 sistemas e o que extrair de cada (metodologia, não conteúdo).
- Registra o diferencial CKOS (autônomo vs manual) de forma acionável.
- Modela Creative DNA como objeto vivo com estados e entrada por contexto.
- Mapeia cada função DNA a um doc canônico dono.
- Produz patch candidates gated, sem aplicar nada.
- Não copia Human Academy; trata `DNA_system_vault` com curadoria, não import.
- Permanece subordinado a governança e gate do Founder.
