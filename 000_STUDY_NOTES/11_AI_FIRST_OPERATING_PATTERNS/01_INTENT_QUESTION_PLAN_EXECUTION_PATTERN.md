---
title: Intent Question Plan Execution Pattern
file: 01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md
phase: 000_STUDY_NOTES
category: study_note
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
purpose: Registrar o padrao AI First de transformar intencao minima em perguntas inteligentes, plano aprovado e execucao controlada.
inputs:
  - 01_THINKING_SYSTEM/01_CKOS_AI_FIRST_CONSTITUTION.md
  - 01_THINKING_SYSTEM/03_AGENT_OPERATING_MODEL.md
  - 01_THINKING_SYSTEM/04_AUTONOMY_AND_APPROVALS.md
  - 01_THINKING_SYSTEM/05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - 02_EXECUTION_SYSTEM/06_SKILLS_REGISTRY.md
  - 02_EXECUTION_SYSTEM/08_PROMPT_LIBRARY.md
  - 02_EXECUTION_SYSTEM/09_TRANSFORMERS_AND_PIPELINES.md
  - 03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
  - 03_RUNTIME_SYSTEM/13_EVALS_OBSERVABILITY_AND_COST_CONTROL.md
  - 06_BUSINESS_SYSTEMS/21_ROI_ARCHITECTURE.md
  - 06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md
  - 000_ROADMAPS/ck_memory.md
  - 000_ROADMAPS/ck_agent_handoffs.md
  - 000_ROADMAPS/ck_roi.md
  - 000_ROADMAPS/ck_risks.md
  - 000_ROADMAPS/ck_tasks.md
outputs:
  - study pattern
  - intelligent question model
  - planner gate guidance
  - UI projection notes
framework: Intent -> Question -> Plan -> Approval -> Execution -> Memory.
edge_cases: Pergunta generica; plano sem custo; execucao sem approval; UI bonita sem estado operacional; agente cria arquivo antes de aprovar filetree.
integrations: CEO Agent, PMO Auditor, Metacognik, QA Lead, Context Pack Builder, Approval Gate, Cost Guard, Memory Writer, future UI projections.
prompts: Toda pergunta CKOS deve declarar por que importa, ROI, risco, custo, recomendacao, alternativas e consequencia.
metrics: Perguntas com consequencia; planos com custo; approvals rastreados; menos retrabalho; menos execucao prematura.
related_notes:
  - 000_STUDY_NOTES/README.md
  - 000_STUDY_NOTES/_folder_memory.md
  - 000_ROADMAPS/ck_memory.md
confidence: unverified
provenance_status: unverified
source_tool: codex
tags: [study, ai_first, intent, questions, planner, approval, briefing]
---

# Intent -> Question -> Plan -> Execution Pattern

## 1. Proposito

Esta study note registra um padrao operacional auxiliar para o CKOS: transformar uma intencao minima em perguntas inteligentes, plano auditavel, aprovacao humana quando necessaria e apenas entao execucao controlada.

Ela nao cria documento canonico, nao autoriza UI/UX, nao inicia Antigravity e nao implementa runtime. Serve como estudo para futuras notas, patch candidates ou docs aprovados pelo Founder.

## 2. Definicao do padrao

O fluxo AI First correto e:

```txt
Intent
  -> Question
    -> Plan
      -> Approval
        -> Execution
          -> Memory
```

Definicoes:

- `Intent`: expressao minima do Founder, cliente ou usuario.
- `Question`: pergunta inteligente que reduz incerteza real antes do plano.
- `Plan`: sequencia de acao com escopo, custo, risco, outputs e criterios de aceite.
- `Approval`: decisao humana ou policy gate quando ha risco, custo, reversibilidade baixa ou impacto canonico.
- `Execution`: acao restrita ao escopo aprovado.
- `Memory`: registro do que foi decidido, feito, rejeitado, aprendido e bloqueado.

## 3. Pergunta comum vs pergunta inteligente CKOS

Pergunta comum coleta informacao. Pergunta inteligente CKOS muda a qualidade da decisao.

| Tipo | Caracteristica | Resultado |
|---|---|---|
| Pergunta comum | Pede dado solto | Aumenta conversa, mas nao necessariamente reduz risco |
| Pergunta inteligente CKOS | Explica consequencia, risco, custo, ROI e proxima decisao | Reduz retrabalho, melhora plano e protege approval gates |

Regra obrigatoria:

> Nenhuma pergunta deve aparecer sem ROI, risco, custo ou consequencia.

Se a pergunta nao altera plano, risco, custo, approval, escopo, contexto, evidencia, prioridade, rollback ou aprendizado, ela deve ser removida ou reescrita.

## 4. Tipos de perguntas

| Tipo | Funcao | Quando usar |
|---|---|---|
| Pergunta de intencao | Clarificar objetivo real | Quando a intencao minima e ambigua |
| Pergunta de escopo | Separar entra / nao entra | Antes de filetree, task pack ou handoff |
| Pergunta de risco | Expor risco juridico, reputacional, tecnico, operacional ou documental | Antes de plano ou output publico |
| Pergunta de custo/creditos | Estimar CKC, creditos, tempo ou consumo de modelos/tools | Antes de acionar agente, pesquisa ou executor |
| Pergunta de contexto faltante | Detectar lacunas de briefing, memoria, fonte ou stakeholder | Antes de montar context pack |
| Pergunta de aprovacao | Pausar quando a decisao exige humano | Antes de patch, envio, billing, canonizacao ou acao irreversivel |
| Pergunta de priorizacao | Ordenar P0/P1/P2/P3 | Quando ha multiplos caminhos viaveis |
| Pergunta de rollback | Verificar reversibilidade | Antes de mudanca que pode gerar dano ou retrabalho |
| Pergunta de aprendizado | Registrar o que deve virar memoria | Depois de decisao, erro, bloqueio ou feedback |
| Pergunta de ROI | Explicitar valor operacional ou de negocio | Antes de investir tempo, custo ou foco |

## 5. Modelo de pergunta inteligente CKOS

Toda pergunta inteligente deve carregar:

```txt
pergunta:
por_que_isso_importa:
impacto_no_roi:
risco_se_ignorar:
custo_estimado:
opcao_recomendada:
alternativas:
consequencia_da_decisao:
```

Exemplo:

```txt
pergunta: Devemos manter a pasta existente ou renomear agora?
por_que_isso_importa: A escolha afeta links, mapas auxiliares e risco de entropia.
impacto_no_roi: Manter reduz retrabalho e preserva continuidade.
risco_se_ignorar: Renomear sem patch pode quebrar referencias e confundir agentes.
custo_estimado: baixo para manter; medio/alto para renomear.
opcao_recomendada: manter neste ciclo.
alternativas: renomear com patch futuro; criar nova pasta; fundir depois.
consequencia_da_decisao: O P0 segue sem rename e P1 pode revisar sem urgencia.
```

## 6. Fluxo para intencao minima

Entrada exemplo:

```txt
criar projeto para perfil no Instagram de advogada penal recem-formada
```

Fluxo CKOS:

1. Detectar intencao: projeto de posicionamento/conteudo para perfil profissional.
2. Classificar dominio: marketing juridico, reputacao, comunicacao publica, risco regulatorio.
3. Detectar risco inicial: normas da OAB, promessa de resultado, linguagem sensacionalista, confidencialidade e posicionamento etico.
4. Montar context pack minimo: objetivo, publico, jurisdicao, restricoes, benchmark permitido, tom, evidencias, riscos e outputs esperados.
5. Gerar perguntas inteligentes: escopo, risco, custo, ROI, aprovacao e rollback.
6. Propor plano: filetree, artefatos, criterios de aceite, CKC estimado e limites.
7. Acionar PMO Auditor se houver risco juridico, output publico, custo relevante ou duvida de escopo.
8. Pedir aprovacao Founder antes de criar artefatos, filetree ou pacote de execucao.

Perguntas iniciais possiveis:

| Pergunta | Por que importa | Risco se ignorar | Recomendacao |
|---|---|---|---|
| O perfil deve priorizar autoridade local, educacao juridica ou captacao indireta? | Define posicionamento e conteudo | Conteudo generico ou anti-etico | Escolher uma prioridade P0 |
| Ha restricoes OAB especificas que devem ser consideradas? | Evita linguagem proibida | Risco juridico/reputacional | Tratar como risk gate |
| O output sera estudo, plano editorial ou assets prontos? | Define escopo e custo | Execucao prematura | Comecar com estudo e plano |
| Qual evidencia minima precisamos antes de recomendar narrativa? | Protege qualidade | Claims sem base | Criar source/context pack |

## 7. Como o CEO Agent deve agir

O CEO Agent nao executa impulsivamente. Ele:

- interpreta a intencao minima;
- classifica tipo de projeto, dominio, risco e valor;
- monta ou solicita context pack minimo;
- identifica lacunas e gera perguntas inteligentes;
- estima CKC, custo operacional e risco;
- aciona PMO Auditor quando ha risco, custo, escopo incerto, output publico ou potencial alteracao canonica;
- propoe plano com arquivos permitidos/proibidos;
- pede aprovacao Founder antes de execucao;
- prepara handoff para executor ou study agent;
- registra memoria e proxima acao.

## 8. Como o PMO Auditor deve agir

O PMO Auditor deve reprovar quando a decisao ainda nao esta segura. Ele:

- verifica escopo e arquivos permitidos;
- bloqueia implementacao prematura;
- aponta riscos documentais, tecnicos, juridicos, financeiros e operacionais;
- valida custo/ROI e estimativa CKC;
- valida governanca RAW -> STUDY -> CANONICAL;
- verifica se ha approval requerido;
- exige checkout lock antes de escrita;
- exige checkout release apos entrega;
- confirma que o output bate com a intencao.

## 9. Projecao futura na UI

Esta study note nao inicia UI, mas define como o padrao deve aparecer futuramente como projecao operacional:

- `Intent Clarifier Card`: mostra intencao detectada, confidence, lacunas e perguntas inteligentes.
- `Execution Plan Widget`: exibe escopo, etapas, arquivos permitidos/proibidos, CKC e criterios de aceite.
- `Approval Gate Card`: pausa execucao ate Founder/PMO/Technical/Client quando necessario.
- `Cost/ROI Panel`: compara custo estimado, valor operacional, risco reduzido e tradeoffs.
- `Agent Activity Stream`: mostra CEO Agent, PMO Auditor, Metacognik e executor com handoffs.
- `Evidence Map`: liga perguntas, fontes, decisoes, riscos, evidencias e memoria.

UI bonita sem estado operacional e anti-pattern. Toda interface futura deve projetar runtime, policy, custo, risco, approval e memoria.

## 10. Conexao com briefing inteligente

O briefing inteligente nao e formulario. Ele e um loop adaptativo:

```txt
intencao minima
  -> perguntas adaptativas
  -> diagnostico vivo
  -> lacunas e riscos
  -> context pack
  -> plano
  -> approval
  -> projeto documentado
```

Tipos de perguntas no briefing:

- perguntas adaptativas: mudam conforme resposta anterior;
- perguntas por risco: surgem quando ha risco juridico, tecnico, reputacional, financeiro ou operacional;
- perguntas por lacuna: surgem quando falta fonte, decisao, stakeholder ou criterio;
- perguntas por stakeholder: variam por Founder, cliente, PMO, QA, tecnico ou audiencia;
- perguntas por objetivo: conectam cada resposta ao output esperado;
- perguntas por evidencia: exigem fonte, exemplo, prova, benchmark ou decision log.

## 11. Acceptance criteria

- A nota permanece em `000_STUDY_NOTES/`, sem autoridade canonica.
- YAML possui os campos auxiliares obrigatorios.
- O padrao Intent -> Question -> Plan -> Execution esta definido.
- Toda pergunta inteligente inclui ROI, risco, custo ou consequencia.
- CEO Agent e PMO Auditor tem papeis separados.
- O exemplo da advogada penal recem-formada inclui risco regulatorio antes de conteudo.
- UI futura e descrita como projecao operacional, nao como implementacao.
- Nao cria docs 26-34.
- Nao inicia UI/UX, Antigravity, backend, API, banco, migrations, JSONs n8n ou agentes reais.

## 12. Anti-patterns

- Pergunta generica sem consequencia.
- Opcao sem impacto, custo, risco ou reversibilidade.
- Plano sem custo ou CKC estimado.
- Execucao sem aprovacao quando ha risco.
- UI bonita sem estado operacional.
- Agente criando arquivo antes de aprovar filetree.
- Context pack gigante que queima tokens sem melhorar decisao.
- PMO Auditor apenas aprovar, sem procurar conflito.
- ROI tratado apenas como dinheiro, ignorando valor operacional.

## 13. Proxima acao

Usar esta study note como referencia para P1 de roadmaps faltantes e para preparar, futuramente, handoff de Antigravity em modo estudo. Qualquer canonizacao futura exige patch candidate, QA documental e approval Founder.
