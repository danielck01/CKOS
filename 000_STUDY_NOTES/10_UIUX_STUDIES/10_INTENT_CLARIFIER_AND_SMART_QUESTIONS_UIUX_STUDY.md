---
title: "10 Intent Clarifier and Smart Questions UI/UX Study"
system_id: study_notes_intent_clarifier_smart_questions_uiux_study_20260528
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
  - "000_STUDY_NOTES/11_AI_FIRST_OPERATING_PATTERNS/01_INTENT_QUESTION_PLAN_EXECUTION_PATTERN.md"
  - "04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md"
tags:
  - uiux
  - study
  - intent_clarifier
  - smart_questions
  - briefing
  - neurodesign
---

# 10 Intent Clarifier and Smart Questions UI/UX Study

## 1. Propósito

Esta nota de estudo especifica os padrões de design UI/UX e neurodesign para o **Intent Clarifier** (Clarificador de Intenção) e a exibição de **Smart Questions** (Perguntas Inteligentes) no CKOS. Ela formaliza a estrutura visual e ergonômica que transforma intenções humanas rudimentares em diretrizes de projeto inequívocas, prevenindo execuções caras e desnecessárias baseadas em suposições da IA.

## 2. O Que Este Padrão Resolve

* **Incerteza de Briefing**: Evita o desperdício de recursos cognitivos e computacionais decorrente do processamento de comandos imprecisos ou ambíguos.
* **Fadiga de Conversação**: Substitui caixas de diálogo longas de chat em texto livre por um fluxo visual adaptativo de perguntas estruturadas de múltipla escolha e chips sugestivos.
* **Falta de Justificativa Epistêmica**: Garante que o usuário compreenda exatamente por que uma pergunta está sendo feita, qual o risco de ignorá-la e qual o impacto operacional de cada alternativa selecionada.

## 3. O Que Não Pode Virar

* **Chatbot Tradicional Passivo**: Não pode ser um clone do ChatGPT que responde apenas com caixas de texto contendo parágrafos longos desprovidos de estrutura operacional.
* **Formulário de Inscrição Estático**: Não deve se tornar uma pesquisa gigante e imutável de briefing que desencoraja o preenchimento por excesso de fricção.
* **Assistente de Sugestões Cosméticas**: Não pode exibir chips ou perguntas puramente decorativas ("Como está o seu dia?") sem conexão direta com o mapeamento de riscos ou execução do projeto.

## 4. Relação com Runtime / Dashboard / Command Center / Node Canvas

* **Command Center**: O Clarificador de Intenção atua acoplado diretamente à Commandbar. Chips e cards de perguntas flutuam abaixo do campo de texto principal como opções imediatas de interação.
* **Runtime**: O input de respostas do usuário emite eventos do tipo `IntentSubmitted` com o payload estruturado para o `intent_router` resolver a taxonomia semântica.
* **Node Canvas**: As respostas do clarificador geram e modificam dinamicamente nós do tipo "Briefing", "Context", "Evidence", "Gap", "Risk" ou "Decision" no canvas espacial, alimentando diretamente os *context packs* do projeto.
* **Dashboard**: Alimenta a projeção `project_dashboard_projection` com as contradições, lacunas ativas e prioridades operacionais do briefing coletado.

## 5. Estados Visuais

Os componentes do Clarificador de Intenção devem projetar os estados de processamento semântico do runtime:

* **Intent Parsing (Processando Intenção)**: Commandbar exibe um backlight pulsante roxo sutil. Chips translúcidos piscam suavemente enquanto o `intent_router` classifica o domínio e o risco (ex: `Classificando domínio...`).
* **Active Smart Question (Pergunta Ativa)**: Surge um cartão estruturado com desfoque de fundo de 25px (`Calm Glass`) e contorno reflexivo fino. Apresenta o título da pergunta, o badge de prioridade, a justificativa e as alternativas estruturadas em chips de clique rápido.
* **Uncertainty Highlight (Contradição de Briefing)**: Se houver contradição de inputs detectada por Cognik, os cartões de briefing envolvidos piscam em laranja e exibem um badge de alerta "Contradição Detectada".
* **Refined Intent Ready (Pronto para Execução)**: O widget assume um contorno verde-esmeralda contínuo e exibe o chip destacado "/workflow" ou "/briefing" para iniciar a montagem do plano.

## 6. Inputs

* **Raw Text Input**: O comando bruto digitado pelo usuário na Commandbar.
* **Contextual History**: Memórias do projeto ativas obtidas via `context_pack_builder` ou context packs existentes.
* **Smart Question Metadata**: O objeto JSON da pergunta inteligente gerado pelo agente executor ou CEO Agent, contendo os campos obrigatórios da taxonomia de perguntas (ROI, risco, custo, opções e consequências).

## 7. Outputs

* **Structured Intent Packet**: Payload formatado contendo as escolhas do usuário enviadas ao runtime via `IntentSubmitted` para redefinir as prioridades ou o planejamento de workflows.
* **User Refusal / Dismissal**: Sinal de cancelamento que recolhe o clarificador e redefine o Command Center para o modo neutro (Ask Mode).

## 8. Riscos

* **Fricção de Engajamento**: Excesso de perguntas em sequência pode fazer com que o usuário aborte a sessão.
  * *Mitigação*: Implementar divulgação progressiva, limitando a exibição simultânea a no máximo 2 perguntas principais na metade da tela, ordenando-as por urgência (P0).
* **Perguntas sem Alinhamento de Contexto**: A IA propor perguntas genéricas que ignoram dados já fornecidos em arquivos do projeto.
  * *Mitigação*: Validar as chaves de contexto no `context_pack_builder` antes de disparar o loop visual de clarificação.

## 9. Regras de ROI

> **Regra Rígida**: Nenhuma pergunta inteligente pode ser exibida ou proposta ao usuário na interface sem declarar explicitamente o seu impacto no ROI do projeto, o seu custo estimado e o seu risco operacional.

Cada pergunta inteligente renderizada deve conter o seguinte esquema visual obrigatório de suporte à decisão:

* **Impacto no ROI**: Uma linha curta explicando como a resposta melhora a eficiência ou reduz o tempo da entrega (ex: `ROI: Evita a criação manual de 3 versões de design redundantes`).
* **Risco se Ignorar**: Indicação clara de falha ou desvio potencial (ex: `Risco: Invasão de diretrizes éticas da OAB no copy final`).
* **Custo Estimado**: O custo aproximado do runtime caso a decisão seja tomada (ex: `Custo Adicional Estimado: $0.05 CKC`).

## 10. Regras de Custo/Créditos

* O widget do clarificador indica preventivamente se uma opção recomendada de resposta pode otimizar o uso de tokens ou ferramentas comerciais (ex: "Opção A economiza até 3.000 tokens em relação à Opção B").
* Exibe alertas visuais de aviso financeiro caso a alternativa selecionada pelo usuário acione collectors externos tarifados.

## 11. Regras de Aprovação Humana

* A conversão de uma intenção bruta refinada para um workflow em andamento exige a aprovação explícita do usuário via botão físico "Aprovar e Avançar Plano".
* O botão de aprovação do clarificador emite o evento de transição que libera a montagem do `Execution Plan Widget`.

## 12. Regras de Evidência

* Toda pergunta que exponha uma lacuna ou contradição deve conter um link de evidência apontando para o arquivo ou trecho de texto conflitante (ex: `Conflito com: briefing_inicial.md#L14`).
* Impede a formulação de perguntas com base em dados de fora do tenant ou do projeto ativo (segurança de isolamento).

## 13. Mobile Behavior

* **Foco Ergonômico na Metade Inferior**: O Clarificador de Intenção surge na metade inferior da tela do celular, posicionado acima do teclado virtual ativo.
* **Interface de Carrossel de Chips**: As alternativas estruturadas da pergunta inteligente são organizadas em um carrossel horizontal deslizável, permitindo a seleção rápida com o polegar.
* **Swipe to Dismiss**: O usuário pode recolher a pergunta ativa deslizando o cartão de diálogo para baixo com o gesto de arrastar.

## 14. Web Behavior

* **Painel Lateral Expansível (Split-Screen)**: No desktop, o clarificador abre em uma gaveta flutuante lateral esquerda. Ao passar o mouse sobre as alternativas, o painel direito atualiza em tempo real a projeção do diff de arquivos ou o mapeamento de dependências no canvas que seria afetado pela respectiva escolha.

## 15. Anti-Patterns

* **Pergunta Genérica sem Consequência**: Exibir questionamentos vagos ou abertos (ex: "O que você gostaria de adicionar à proposta?") sem oferecer alternativas estruturadas ou explicar o impacto em ROI, custo ou riscos.
* **Chips Decorativos Inativos**: Chips de classificação semântica no Clarificador de Intenção que funcionam apenas como tags estéticas sem gerar ação ou filtrar metadados operacionais no runtime.
## 16. Acceptance Criteria

* Toda pergunta inteligente renderizada deve conter em sua base a declaração explícita de ROI, Risco e Custo.
* O clarificador deve consumir as sugestões dinâmicas agregadas da projeção `command_center_suggestions` para atualizar os placeholders e atalhos rápidos de digitação.
* A resposta estruturada selecionada pelo usuário deve ser encapsulada em um evento `IntentSubmitted` emitido imediatamente para o runtime, sem desvios diretos de escrita no banco de dados.
* O histórico completo de respostas e questionamentos (briefing history trail) deve ser preservado de forma persistente.
* A interface do clarificador deve permitir a revisão não-destrutiva de qualquer resposta anterior na timeline do briefing sem resetar ou invalidar as respostas das outras perguntas do fluxo.

## 17. Próximas Perguntas para Founder/PMO

* Devemos limitar o número total de iterações do clarificador (perguntas de refinamento consecutivas) para evitar a fadiga do usuário, inserindo uma opção do tipo "Ignorar refinamentos e executar com heurísticas padrão"?
* O histórico de respostas do clarificador deve ser mantido como rascunhos visíveis em uma timeline secundária de auditoria do projeto ou apenas gravado como metadados agregados do workflow final?
