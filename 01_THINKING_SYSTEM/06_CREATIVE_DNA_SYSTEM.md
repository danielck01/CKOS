---
title: Creative DNA System
file: 06_CREATIVE_DNA_SYSTEM.md
phase: 01_THINKING_SYSTEM
category: object_model
version: 0.1.0
status: draft
owner: PMO_CKOS
responsible_agent: Cognik
reviewers:
  - Metacognik
approval_required:
  - founder
  - pmo_ckos
  - metacognik
purpose: Definir o Creative DNA como objeto vivo do CKOS, consolidando metodologia dos dois estudos DNA sem importar material bruto.
inputs: Intencao do usuario; briefing vivo; sinais; referencias; outputs aprovados; feedback; memoria; evidencias; estudos DNA.
outputs: Modelo de Creative DNA; estados de maturidade; regras de descoberta, aplicacao, auditoria e crescimento.
framework: DNA-0 a DNA-vivo; discovery inteligente; research proativo; skill-mestre; apply/audit loop; feedback-to-memory.
edge_cases: Projeto sem DNA; DNA contraditorio; referencia externa tentadora para copiar; output bonito mas fora do DNA; founder sobrecarregado.
integrations: Object Model; Agent Operating Model; Memory; Skills Registry; Runtime; Evals; ROI; RAG.
prompts: Prompts de bootstrap, aplicacao, auditoria e calibracao de Creative DNA.
metrics: Consistencia com DNA; reducao de retrabalho; maturidade do DNA; reuso de memoria; outputs reprovados por genericidade.
related_notes:
  - 02_AI_FIRST_OBJECT_MODEL.md
  - 03_AGENT_OPERATING_MODEL.md
  - 05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - ../02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md
  - ../000_ROADMAPS/22_CONSOLIDATION/02_DNA_SYSTEM_COMPARISON_AND_INTEGRATION_MAP.md
  - ../000_STUDY_NOTES/DNA_SYSTEM/DNA_system_vault/README.md
  - ../000_STUDY_NOTES/DNA_SYSTEM/SUPERAGENT_Director_Visual/DNA/01-DNA-Master.md
tags: [thinking, creative_dna, object_model, memory, skills, ai_first]
---

# 1. Proposito

Definir o **Creative DNA System** como a camada do CKOS que identifica, estrutura, aplica e evolui a identidade estrategica, criativa e operacional de um projeto.

O DNA nao e um questionario fixo nem um manual estetico. No CKOS, DNA e um **objeto vivo**: nasce fraco, cresce por interacao, acumula evidencias, orienta decisoes e melhora com feedback.

# 2. Funcao dentro do CKOS

O Creative DNA System conecta intencao, briefing, memoria, skills, agentes, QA e ROI. Ele responde:

- o que torna este projeto reconhecivel;
- quais escolhas sao coerentes ou incoerentes;
- quais padroes de linguagem, produto, visual, oferta e comportamento devem ser preservados;
- quais anti-padroes devem ser evitados;
- quando o sistema sabe o suficiente para executar e quando deve perguntar.

Ele nao substitui `02_AI_FIRST_OBJECT_MODEL.md`; ele adiciona um objeto especializado que deve ser incorporado ao modelo oficial quando aprovado.

# 3. Inputs

- Intencao inicial do Founder, cliente ou usuario.
- Briefing vivo do projeto.
- Sinais: mensagens, arquivos, imagens, referencias, decisoes, outputs, feedbacks.
- Evidencias internas e externas.
- Memorias aprovadas e memorias negativas.
- Skills de estrategia, pesquisa, copy, visual, produto, social, motion e QA.
- Estudos em `000_STUDY_NOTES/DNA_SYSTEM`.

# 4. Outputs

- Objeto `CreativeDNA`.
- Estado de maturidade do DNA.
- Constraints, principles, anti-patterns e quality rubrics.
- Perguntas inteligentes de alto ganho.
- Briefing enriquecido.
- Instrucao para agentes e skills.
- Auditoria de consistencia com DNA.
- Eventos de aprendizado e memoria.

# 5. Framework operacional

## 5.1 Os dois sistemas analisados

O CKOS possui dois estudos principais de DNA:

| Sistema | Origem | Valor | Uso no CKOS |
|---|---|---|---|
| `DNA_system_vault` | Rascunho operacional CKOS-style | Estrutura de runtime, heartbeat, skills, transformers e Creative DNA como objeto | Extrair modelo operacional e campos uteis; nao importar em massa |
| `SUPERAGENT_Director_Visual` | Sistema Human Academy / Director Visual | Profundidade de oficio, documentos-mestre, orquestracao tipo Maestro e calibracao criativa | Extrair metodologia; nao copiar conteudo nem depender de operacao manual |

Veredito: o CKOS deve fundir a **arquitetura operacional** do Sistema A com a **profundidade metodologica** do Sistema B, invertendo o ponto fraco dos dois: em vez de um wizard manual ou de notas redundantes, o DNA cresce por uso, memoria, evidencias, feedback e auditoria.

## 5.2 Objeto `CreativeDNA`

```yaml
creative_dna_id:
project_id:
workspace_id:
status: draft | active | archived
maturity_state: DNA-0 | DNA-1 | DNA-2 | DNA-3 | DNA-vivo
confidence_score: 0.0-1.0
source_signals:
principles:
voice_and_tone:
visual_direction:
product_behavior:
audience_model:
offer_logic:
content_patterns:
anti_patterns:
constraints:
quality_rubrics:
evidence_refs:
memory_refs:
negative_memory_refs:
last_calibrated_at:
owner_agent:
review_agent:
approval_status:
```

## 5.3 Estados de maturidade

```txt
DNA-0      nenhum sinal confiavel
DNA-1      sementes: intencao, algumas preferencias e primeiras restricoes
DNA-2      parcial: briefing + research + referencias com confianca media
DNA-3      maduro: multiplos outputs aprovados e rubricas claras
DNA-vivo   auto-calibrado: feedback loop ativo, memoria recorrente e auditoria historica
```

Regra: o sistema nunca trava por falta de DNA. Ele executa com o estado disponivel, declara confianca e incrementa o DNA durante a missao.

## 5.4 Discovery inteligente

O CKOS nao deve empurrar um formulario longo. Cognik deve perguntar apenas quando a resposta aumentar muito a clareza, reduzir risco ou evitar retrabalho.

Perguntas iniciais recomendadas:

- O que este projeto nunca pode parecer?
- Quem precisa reconhecer valor imediatamente?
- Qual comportamento, visual ou tom ja esta proibido?
- Qual referencia inspira metodologia, mas nao deve ser copiada?
- O que define um output ruim mesmo que ele esteja bonito?

## 5.5 Aplicacao do DNA

Antes de produzir um artefato relevante, o agente executor deve:

1. recuperar o `CreativeDNA` do projeto;
2. identificar maturidade e confianca;
3. selecionar skills-mestre relevantes;
4. aplicar principles, constraints e anti-patterns;
5. declarar risco quando o DNA for fraco ou contraditorio.

Depois de produzir, Metacognik ou QA Lead deve auditar:

- consistencia com principles;
- ausencia de anti-patterns;
- aderencia ao publico e oferta;
- qualidade tecnica do artefato;
- evidencias usadas;
- necessidade de approval humano.

## 5.6 Skill-mestre

O padrao forte extraido do Sistema B e o **documento-mestre de disciplina**. No CKOS, isso vira skill de alto nivel, nao prompt solto.

Uma skill-mestre deve conter:

- doutrina da disciplina;
- quando usar e quando nao usar;
- principios;
- anti-padroes;
- exemplos aprovados e reprovados;
- rubrica 0-10;
- checklist de auditoria;
- relacao com memoria e ROI.

Exemplos de skills-mestre candidatas:

- `brand-dna-diagnosis`
- `voice-and-tone-master`
- `visual-direction-master`
- `content-format-master`
- `offer-and-positioning-master`
- `creative-dna-audit`

## 5.7 Loop de crescimento

```txt
signal_received
-> dna_bootstrap_or_update
-> briefing_enrichment
-> skill_master_selection
-> artifact_generation
-> dna_consistency_audit
-> human_or_metacognik_feedback
-> memory_update
-> dna_calibration
```

Cada output aprovado aumenta o DNA. Cada output rejeitado pode virar negative memory quando revelar um anti-pattern recorrente.

# 6. Agente responsavel

`Cognik` e responsavel por interpretar sinais, criar ou atualizar o objeto `CreativeDNA` e escolher skills relevantes.

`PMO_CKOS` e owner documental. `Metacognik` revisa confianca, risco e coerencia.

# 7. Superagentes envolvidos

- **Nick**: coleta intencao e apresenta perguntas essenciais.
- **Cognik**: cria, atualiza e aplica o DNA.
- **Metacognik**: audita consistencia e decide se precisa de approval.
- **PMO_CKOS**: governa patch candidates e evita importacao bruta.
- **QA Lead**: valida rubricas e regressao em outputs repetidos.
- **Campaign / Branddock pendente**: aplica DNA em campanhas, marca e conteudo quando ativado.

# 8. Skills necessarias

- `creative-dna-bootstrap`
- `creative-dna-update`
- `creative-dna-audit`
- `brand-dna-diagnosis`
- `voice-and-tone-master`
- `visual-direction-master`
- `anti-pattern-scan`
- `memory-routing`
- `feedback-to-learning`

# 9. Prompts relacionados

```txt
Analise estes sinais do projeto e atualize o CreativeDNA. Separe principios, constraints, anti-patterns, evidencias, lacunas e perguntas de alto ganho. Retorne maturidade, confianca e proximo passo.
```

```txt
Antes de produzir este artefato, recupere o CreativeDNA aplicavel e declare: quais principios guiam a entrega, quais anti-patterns devem ser evitados, quais lacunas podem afetar qualidade e se approval e necessario.
```

```txt
Audite este output contra o CreativeDNA. Atribua score 0-10 para consistencia, liste desvios, riscos, evidencias usadas, memoria a atualizar e decisao: aprovado, ajustar ou reprovar.
```

# 10. Integracoes

- `02_AI_FIRST_OBJECT_MODEL.md`: deve receber `CreativeDNA` como objeto especializado.
- `03_AGENT_OPERATING_MODEL.md`: deve receber o padrao consult-before-produce / audit-after.
- `05_MEMORY_AND_CONTEXT_ARCHITECTURE.md`: deve persistir DNA, exemplos aprovados e negative memory.
- `06_SKILLS_REGISTRY.md`: deve elevar skills criativas ao padrao skill-mestre.
- Runtime: deve logar eventos `creative_dna_created`, `creative_dna_updated`, `creative_dna_applied`, `creative_dna_audited`.
- Evals/ROI: deve medir consistencia com DNA, retrabalho evitado e maturidade.
- RAG: deve indexar DNA por projeto, contexto, disciplina e evidencia.

# 11. Memoria e contexto

O DNA deve viver em tres niveis:

- **Projeto**: identidade e criterios especificos.
- **Workspace/cliente**: padroes recorrentes entre projetos.
- **CKCompany**: metodologia interna, rubricas e anti-padroes globais.

Memoria positiva guarda o que funcionou. Memoria negativa guarda o que nao deve ser repetido. Nenhuma memoria deve ser promovida sem QA ou feedback confiavel.

# 12. Edge cases

- **Projeto sem DNA**: criar `DNA-0`, fazer bootstrap minimo e executar com baixa confianca declarada.
- **DNA contraditorio**: registrar conflito e pedir decisao se afetar output critico.
- **Referencia externa forte demais**: extrair metodologia, nao copiar expressao, estrutura proprietaria ou material protegido.
- **Output bonito mas fora do DNA**: reprovar por incoerencia mesmo com boa estetica.
- **Founder sobrecarregado**: pedir approval apenas quando houver risco, custo, publicacao externa, decisao irreversivel ou baixa confianca com alto impacto.

# 13. Metricas de sucesso

- % de outputs aprovados por consistencia com DNA.
- Reducao de retrabalho por desalinhamento.
- Tempo de criacao de DNA-0 para DNA-2.
- Numero de memorias reutilizadas por projeto.
- Numero de perguntas evitadas por contexto recuperado.
- Taxa de outputs reprovados por genericidade.
- Score medio de `creative_dna_audit`.

# 14. Criterios de aprovacao

Aprovado se:

- define `CreativeDNA` como objeto vivo;
- diferencia os dois estudos DNA sem copiar nenhum;
- preserva AI-first e autonomia gated;
- conecta DNA a briefing, memoria, skills, agentes, QA e ROI;
- permite operar mesmo com DNA incompleto;
- transforma feedback em aprendizado rastreavel.

# 15. Criterios de reprovacao

Reprovado se:

- virar wizard manual obrigatorio;
- importar `DNA_system_vault` em massa;
- copiar metodologia proprietaria externa como conteudo;
- tratar DNA como documento estatico;
- executar sem auditoria de consistencia;
- promover memoria sem feedback ou QA.

# 16. Related notes

- [[02_AI_FIRST_OBJECT_MODEL]]
- [[03_AGENT_OPERATING_MODEL]]
- [[05_MEMORY_AND_CONTEXT_ARCHITECTURE]]
- [[06_SKILLS_REGISTRY]]
- [[02_DNA_SYSTEM_COMPARISON_AND_INTEGRATION_MAP]]
