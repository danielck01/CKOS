---
title: "13 Evidence, Trust and Decision UI/UX Study"
system_id: study_notes_evidence_trust_decision_uiux_study_20260528
phase: 000_STUDY_NOTES
category: uiux_study
status: draft
confidence: unverified
provenance_status: unverified
source_tool: antigravity
owner: pmo_ckos
responsible_agent: pmo_ckos
reviewers: [pmo_ckos, metacognik]
approval_required: [founder, pmo_ckos, metacognik]
related_notes:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/ck_memory.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md"
  - "000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md"
tags:
  - uiux
  - study
  - evidence_map
  - trust
  - confidence
  - neurodesign
---

# 13 Evidence, Trust and Decision UI/UX Study

## 1. Propósito

Esta nota de estudo especifica os padrões de design UI/UX e neurodesign para o **Evidence Map** (Mapa de Evidências), a exibição de **Confidence Scores** (Níveis de Confiança) e a apresentação de **Limitações de IA** no CKOS. O objetivo é assegurar a transparência epistemológica das decisões geradas pelos agentes inteligentes, impedindo que outputs de IA sejam consumidos sem validação científica e fornecendo as pistas visuais necessárias para a auditoria humana.

## 2. O Que Este Padrão Resolve

* **Alucinações Não Detectadas**: Evita a aceitação cega de dados errados ou fictícios inventados por modelos de linguagem complexos.
* **Falta de Rastreabilidade**: Resolve a opacidade das referências bibliográficas e documentais de briefing, estruturando as conexões causais das fontes na interface.
* **Falsa Autoridade de Respostas**: Combate a tendência de a IA expressar afirmações controversas com segurança excessiva, forçando-a a declarar seus limites de escopo e lacunas de dados.

## 3. O Que Não Pode Virar

* **Lista de Rodapé Estática Decorativa**: Não pode ser um mero agrupamento de links de "saiba mais" ou URLs genéricas soltas sem relação lógica com as afirmações da IA.
* **Log de RAG Raw Incompreensível**: Não deve se tornar uma listagem de fragmentos de JSON brutos de banco de dados vetorial inacessível ao tomador de decisão de negócios.
* **Badge Estético Sem Significado**: O score de confiança não pode ser um indicador puramente cosmético de progresso (ex: sempre exibindo 99% de acerto de forma fictícia).

## 4. Relação com Runtime / Dashboard / Command Center / Node Canvas

* **Command Center**: Nick integra badges de confiança e limitações nas suas respostas textuais em Explain Mode e Ask Mode.
* **Runtime (Evals Engine & Datta)**: O widget consome a tabela `evidence_items` e as chaves de relacionamento de `roi_evidence_links`, além dos resultados da auditoria `MetacognikReviewed` do runtime para desenhar os grafos de conformidade.
* **Node Canvas**: O Evidence Map funciona como um visualizador de malha conectiva 2D no canvas, ligando o nó do artefato final produzido aos nós de briefing que serviram de briefing.
* **Dashboard**: Consolida a métrica de acurácia epistemológica média e o volume de evidências validadas do projeto.

## 5. Estados Visuais

A interface mapeia os indicadores epistemológicos com base nas transições do runtime:

* **high_confidence (Confiança Alta)**: Badge e anel de progresso verde-azul brilhante. Fontes bem delineadas e validadas por co-auditoria Datta. Backlight Calma Glass estável.
* **medium_confidence (Confiança Média)**: Badge em amarelo suave. A interface destaca visualmente chips de "Possíveis Lacunas" ou sugere o acionamento de um collector complementar.
* **low_confidence (Confiança Baixa / Risco de Alucinação)**: Badge vermelho-alaranjado pulsante. Um backlight de aviso acende atrás do widget. A visualização de diff de arquivos ou formulários de aprovação é bloqueada preventivamente até confirmação do risco. O Metacognik dispara um alerta instantâneo visual de risco epistemológico elevado.
* **speculative (Especulativo)**: Badge em violeta translúcido pulsante. Indica inferências que carecem de comprovação experimental. O widget exige a aprovação do portão correspondente e ativa o Metacognik Alert de forma persistente.
* **insufficient_data (Dados Insuficientes)**: Badge cinza-hachurado. Sinaliza que o pipeline não localizou informações suficientes para sustentar qualquer conclusão sólida. A interface bloqueia o fluxo de decisão e apresenta um prompt destacado para execução de novos collectors de dados.

### 5.1 Diferenciação Epistemológica de Elementos

A interface do CKOS deve diferenciar claramente a semântica e a representação visual de cada categoria epistêmica no mapa de evidências:

* **Fato (Fact)**: Informação concreta e auditada de fontes canônicas ou dados brutos indubitáveis. Representado por um ícone de escudo verde sólido.
* **Inferência (Inference)**: Dedução lógica feita a partir de fatos estabelecidos. Representado por uma linha de conexão tracejada em azul.
* **Hipótese (Hypothesis)**: Proposição preliminar sob análise que carece de validação. Representada por uma linha pontilhada amarela.
* **Recomendação (Recommendation)**: Proposta de ação sugerida baseada na análise. Representado por um ícone de lâmpada ou chip direcionador.
* **Risco (Risk)**: Fatores de ameaça detectados pelo Metacognik que podem desestabilizar a operação. Representado por um triângulo de alerta vermelho.
* **Lacuna (Gap)**: Ausência identificada de dados necessários para a tomada de decisão. Representado por um slot vazio hachurado em cinza.
* **Decisão (Decision)**: Ação formal de aprovação ou alteração de estado no sistema. Representado por um badge de martelo ou check.
* **Contradição (Contradiction)**: Inconsistência ou divergência insolúvel entre duas ou mais evidências ativas. Representado por um link vermelho pulsante entre nós com o badge "Contradição de Fontes".
* **Evidência Vencida/Desatualizada (Outdated Evidence)**: Dados anteriormente válidos que foram superados por informações mais recentes. Representado por um relógio amarelo com sinal de alerta de expiração.
* **Evidência Insuficiente (Insufficient Evidence)**: Suporte informacional fraco ou incompleto para sustentar uma decisão. Representado por um badge cinza opaco.

### 5.2 Resolução e Alerta de Conflitos Epistemológicos

Quando o Metacognik detecta anomalias ou conflitos na camada de evidências, a interface deve reagir com comportamentos operacionais específicos:

* **Fontes Confiáveis em Contradição**: Quando duas fontes válidas de alta confiança se contradizem mutuamente, o canvas destaca a ligação de ambas em vermelho pulsante e força o status da run para `metacognik_audit_running` ou `blocked_by_missing_context`, suspendendo a aprovação automática até a intervenção manual do usuário para resolver a contradição de dados.
* **Contradição Temporal (Novo vs. Antigo)**: Se uma fonte recente contradiz uma fonte antiga, a interface renderiza uma linha degradê de transição temporal, destacando visualmente que a fonte antiga está marcada como `Outdated Evidence` e propondo a substituição automática das projeções de ROI ou dados de negócios.
* **Fonte Fraca em Decisão de Alto Impacto**: Se uma fonte de baixo peso (`speculative` ou `insufficient_data`) for usada para apoiar um portão de decisão classificado com alto risco ou alto custo de créditos, a interface ativa um alerta de Metacognik vermelho crítico no painel do Approval Gate, exigindo co-auditoria de um collector adicional e aprovação em dois níveis de RBAC.
* **Triggers de Alerta Metacognik**: O Metacognik aciona avisos visuais persistentes sempre que a confiança de um nó sob análise cair para `low_confidence`, `speculative` ou `insufficient_data`, mitigando o risco de alucinação de IA ser integrada inadvertidamente aos relatórios e faturas.

## 6. Inputs

* **Metacognik Audit Score**: Classificação numérica de confiança epistemológica (0 a 1).
* **Evidence Link Schema**: As referências físicas e metadados de lineage de dados das tabelas `evidence_items` e `roi_evidence_links`.
* **Declared Limitations List**: Array estruturado de tópicos ignorados ou não cobertos pelo modelo na sessão.

## 7. Outputs

* **Epistemic Audit Logs**: Registro de interações e contestações do usuário enviadas aos evals para retroalimentar os loops de aprendizado do sistema operacional.
* **Collector Run Trigger**: Evento de acionamento de pesquisas complementares caso o usuário exija mais evidências físicas para o mapa.

## 8. Riscos

* **Sobrecarga de Auditoria (Audit Fatigue)**: Apresentar dezenas de conexões e fontes para tarefas simples pode cansar o usuário e fazer com que ele ignore os links.
  * *Mitigação*: Implementar agrupamento de evidências por relevância hierárquica (P0 para fontes fundamentais de domínio, P1 para secundárias), expandindo os detalhes apenas sob demanda.
* **Avaliação de Confiança Enviesada**: O próprio modelo de auditoria de IA superestimar a sua acurácia.
  * *Mitigação*: Utilizar scores combinados entre evals automáticos de múltiplos modelos concorrentes e inputs humanos históricos do dashboard.

## 9. Regras de ROI

* **Prevenção de Retrabalho**: O Evidence Map deve apontar quanto tempo de revisão manual foi economizado pela validação automatizada de fontes (ex: `Evidências Auditadas: 8 referências cruzadas | -1h de Auditoria Manual`).

## 10. Regras de Custo/Créditos

* Se o score de confiança de um output da IA for marcado como `low_confidence`, a interface sugere um botão rápido de re-execução com modelo de alta capacidade (ex: `@metacognik via Claude 3.5 Opus`), exibindo o custo incremental correspondente (ex: `Custo Incremental: $0.15 CKC`).

## 11. Regras de Aprovação Humana

* Se o score de confiança epistemológica cair abaixo do limiar (threshold) de aceitação de qualidade técnica cadastrado no projeto, o workflow transita automaticamente para `Waiting Approval` antes de gravar qualquer artefato na memória do sistema.

## 12. Regras de Evidência

> **Regra Rígida**: Nenhum output de IA (diagnóstico, proposta, código ou resposta de Nick) pode ser apresentado ao usuário como verdade absoluta na tela sem exibir obrigatoriamente:
> 1. O Nível de Confiança (Confidence Score) de Metacognik/Evals (`high_confidence`, `medium_confidence`, `low_confidence`, `speculative`, `insufficient_data`).
> 2. O Link para as Fontes (`evidence_items` e `roi_evidence_links`) exatas de onde a informação foi extraída no RAG ou RAG privado.
> 3. A Declaração de Limitações (Limitation Statement) listando os escopos e dados ignorados na execução.

* O widget de resposta deve ser estruturado em colunas dedicadas para estes três blocos epistemológicos.

## 13. Mobile Behavior

* **Badge Epistêmico de Toque**: O Confidence Score é exibido em formato de anel colorido concêntrico no canto do cartão. Tocar no anel abre um slide-up na metade inferior da tela com a listagem de limitações e referências de fontes.
* **Gestos**: Deslizar o popover lateralmente alterna entre as referências documentais e o extrato de limitações da IA de forma ergonômica.

## 14. Web Behavior

* **Visualizador de Grafo Espacial Interativo (Canvas System)**: Na tela desktop, clicar em "Ver Mapa de Evidências" abre um overlay de grafo. Linhas curvas suaves conectam as frases exatas da proposta às fontes documentais de briefing no Node Canvas. Passar o mouse destaca o lineage de dados correspondente.

## 15. Anti-Patterns

* **Falsa Autoridade Epistêmica**: Exibir parágrafos afirmativos sem expor quais documentos de briefing ou memórias do vault subsidiaram aquela conclusão.
* **Ocultar Limitações**: Esconder as falhas ou ressalvas declaradas pelo modelo de IA no rodapé com tipografia minúscula e de baixo contraste para dar a ilusão de acurácia irrestrita.

## 16. Acceptance Criteria

* O widget de visualização de outputs de IA deve conter de forma obrigatória as três divisões epistemológicas: Score, Fontes e Limitações.
* As evidências listadas devem ler exclusivamente metadados das tabelas `evidence_items` e `roi_evidence_links` geradas no runtime, impossibilitando a exibição de links falsos.
* O badge de confiança deve transitar dinamicamente entre as cores verde-azul (`high_confidence`), amarelo (`medium_confidence`), vermelho-laranja (`low_confidence`), violeta (`speculative`) e cinza-hachurado (`insufficient_data`) conforme o status obtido do `MetacognikReviewed`.

## 17. Próximas Perguntas para Founder/PMO

* Como a interface deve apresentar contradições de evidências de fontes externas (ex: dados científicos divergentes coletados via PubMed Collector) de modo a não confundir o usuário não técnico?
* Devemos permitir que o usuário adicione notas manuais de contestações ou refutações diretamente aos nós de evidência do grafo espacial?
