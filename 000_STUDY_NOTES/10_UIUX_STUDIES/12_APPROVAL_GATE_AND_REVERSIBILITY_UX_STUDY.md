---
title: "12 Approval Gate and Reversibility UX Study"
system_id: study_notes_approval_gate_reversibility_ux_study_20260528
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
  - approval_gate
  - reversibility
  - rollback
  - neurodesign
---

# 12 Approval Gate and Reversibility UX Study

## 1. Propósito

Esta nota de estudo especifica os padrões de design UI/UX e neurodesign para o **Approval Gate** (Portão de Aprovação) e a gestão de **Reversibilidade (Rollback)** no CKOS. O objetivo é assegurar o controle estrito do usuário sobre as ações automatizadas dos agentes inteligentes, detalhando visualmente as ramificações de cada decisão autorizada e definindo os caminhos ergonômicos de recuperação de erros em caso de desvios operacionais.

## 2. O Que Este Padrão Resolve

* **Perda de Controle de Automações**: Impede que agentes executem ações destrutivas (deleção de arquivos, modificação de configurações ou uploads públicos) sem autorização prévia.
* **Fadiga de Confirmação Mecânica**: Evita a aprovação cega de portões decisórios ao exigir a exibição explícita do diff de alterações e das consequências de cada escolha.
* **Medo de Dano Irreversível**: Reduz a ansiedade operacional do usuário ao classificar visualmente o nível de reversibilidade de cada tarefa e fornecer atalhos físicos rápidos de rollback em caso de falha.

## 3. O Que Não Pode Virar

* **Modal de Confirmação Tradicional Inócuo**: Não pode ser um alerta genérico estilo "Tem certeza? OK/Cancelar" que não exibe dados de escopo, custo ou risco.
* **Caixa de Diálogo Puramente Textual**: Não deve conter blocos longos de texto corrido sem estrutura tipográfica ou contraste adequado para atrair a atenção seletiva do tomador de decisão.
* **Portão de Ignoração de Políticas**: Não pode permitir que o usuário contorne regras rígidas de segurança ou governança sem o nível hierárquico (RBAC/ABAC) exigido.

## 4. Relação com Runtime / Dashboard / Command Center / Node Canvas

* **Runtime (Approval Gate Engine)**: O widget exibe de forma síncrona o estado da `approval_projection`. Ações do usuário emitem o evento `ApprovalSubmitted` para o runtime liberar ou abortar o workflow.
* **Command Center**: Quando o runtime dispara um portão de aprovação, o Command Center transita imediatamente para o **Approval Mode**, sobrepondo visualmente o cartão decisório no Z-index mais elevado.
* **Node Canvas**: O nó suspenso no canvas assume uma coloração amarela pulsante e estende conectores para os stakeholders que precisam decidir.
* **Dashboard**: Exibe o contador de decisões históricas registradas e portões pendentes agrupados por prioridade.

## 5. Estados Visuais

O widget do Approval Gate projeta estritamente a máquina de estados de aprovação do runtime:

* **Requested (Aprovação Exigida)**: O widget surge projetado à frente (backlight ouro pulsante suave). Ações paralelas de escrita na interface são bloqueadas por uma máscara escura translúcida. O avatar do aprovador brilha.
* **Approved (Autorizado)**: O widget inteiro realiza uma animação rápida de expansão em verde-esmeralda (200ms) e é recolhido para liberar a visualização do workflow ativo.
* **Rejected (Rejeitado)**: O widget brilha em vermelho sólido por 250ms antes de fechar. Abre imediatamente um formulário de feedback estruturado para instruir o agente sobre as razões da negativa.
* **Expired (Timeout de Segurança)**: Os botões de decisão são desabilitados e o widget assume um tom cinza-chumbo com a legenda "Expired (Timeout)".
* **Escalated (Alerta de Risco / Prioridade)**: O widget pulsa em vermelho-alaranjado rápido duas vezes para sinalizar que o portão decisório foi encaminhado para a próxima autoridade hierárquica por falta de resposta.

### 5.1 Diferenciação de Ações de Reversão e Controle UX

A interface do CKOS deve diferenciar conceitualmente e visualmente as seguintes ações de controle de execução:

* **Cancelar antes de executar (Abort / Cancel Run in-progress)**: Interrupção imediata de um pipeline ativo de agentes que está em execução. Utiliza o evento `CommandCancelled`. Representado por um botão "Stop" vermelho no stream de execução.
* **Pausar execução**: Interrupção temporária do pipeline, mantendo o estado de runtime na memória para retomada posterior. Representado por um botão de "Pause" amarelo.
* **Rejeitar aprovação**: Ação em um portão de aprovação ativo onde o usuário nega a autorização solicitada. O workflow de execução não é iniciado para o passo proposto. Dispara `ApprovalSubmitted` com status `rejected`.
* **Pedir revisão**: Retorno da proposta ao agente com comentários específicos de ajuste, sem cancelar o workflow geral. Dispara `ApprovalSubmitted` com status `changes_requested`. Representado por um ícone de lápis com balão de comentário.
* **Desfazer ação concluída (Workflow Rollback)**: Reversão física de uma transação ou fluxo já executado e persistido de volta ao estado inicial. Dispara `RollbackWorkflowRequested` ou `ExecutionReversalRequested`. Representado por um botão "Rollback" retrocedente curvo.
* **Restaurar versão anterior (Artifact Version Restore)**: Recuperação de um estado específico de um documento ou código a partir do histórico de versões de artefatos. Dispara `ArtifactVersionRestoreRequested`. Representado por um ícone de histórico de versões.
* **Compensar efeito já persistido (Compensation Action)**: Lançamento de transações compensatórias para mitigar ações que não possuem rollback físico possível (ex: estornar créditos após disparo de e-mail externo). Dispara `CompensationActionRequested`. Representado por um ícone de balança/estorno.

## 6. Inputs

* **Approval ID**: O identificador único da aprovação na tabela do banco de dados do runtime.
* **Reversibility Metadata**: Atributo booleano indicando se a ação pode ser desfeita (`reversible: true/false`).
* **Metacognik Audit Assessment**: O relatório de riscos e a recomendação técnica formulada pela auditoria de IA.
* **Approval Object Schema**: Estrutura contendo o solicitante (`requester`), aprovador (`approver`), dados afetados (`affected_data`), arquivos/objetos impactados (`impacted_files`), prazo limite (`timeout_countdown`), estimativa de custo (`cost_estimate`), risco associado (`risk_assessment`) e motivos semânticos (`reasons`).

## 7. Outputs

* **Decision Event Packet**: Evento `ApprovalSubmitted` contendo a decisão (`approved | rejected | changes_requested`) e os comentários de ajuste associados.
* **Reversal and Rollback Commands**: Disparo de eventos específicos de reversão baseados na ação concluída:
  - `RollbackWorkflowRequested` ou `ExecutionReversalRequested` (para reversão de workflows);
  - `ArtifactVersionRestoreRequested` (para restauração de arquivos/artefatos);
  - `CompensationActionRequested` (para transações compensatórias);
  - `ApprovalRevoked` (para revogação de aprovação prévia).
  *(Nota: O evento `CommandCancelled` é usado estritamente para cancelar execuções em progresso, nunca para reverter ações concluídas).*

## 8. Riscos

* **Bloqueio de Pipeline por Absenteísmo**: Workflows travados permanentemente porque o stakeholder responsável não está online para aprovar.
  * *Mitigação*: Implementar prazos de expiração visualizados em tempo real (contadores regressivos de timeout) e fluxos automáticos de escalação descritos na política de aprovação.
* **Rejeição sem Instrução Semântica**: O usuário rejeitar a tarefa e a IA repetir o mesmo erro por falta de feedback de contexto.
  * *Mitigação*: Exigir o preenchimento de justificativa curta sempre que a opção de rejeição for selecionada.

## 9. Regras de ROI

* **Prevenção de Perdas**: O widget deve computar e exibir o ROI de segurança gerado pelas revisões (ex: "Esta rejeição evitou o desperdício de $0.45 CKC em execuções de modelo desalinhadas").

## 10. Regras de Custo/Créditos

* O widget do portão de aprovação exibe no rodapé o custo preventivo acumulado da transação que está sendo autorizada (ex: `Custo a ser cobrado na aprovação: $0.12 CKC`).

## 11. Regras de Aprovação Humana

> **Regra Rígida**: O Approval Gate não é um modal genérico. Nenhuma aprovação pode aparecer na interface sem declarar explicitamente as suas consequências imediatas, detalhando os seguintes blocos informativos:
> 1. **Ação Solicitada**: O comando exato proposto pelo agente inteligente.
> 2. **Motivo**: A justificativa semântica de por que esta ação é recomendada pelo pipeline.
> 3. **Risco**: Avaliação do Metacognik sobre o risco técnico ou de negócios.
> 4. **Custo**: Custo estimado de créditos CKC consumidos pelo processamento.
> 5. **Dados Afetados**: Quais estruturas e registros do banco de dados sofrerão alteração.
> 6. **Arquivos/Objetos Impactados**: Lista de arquivos na filetree com visualização em Diff de adições/deleções.
> 7. **Rollback Disponível**: Indicação explícita se o rollback físico está disponível (`reversible: true`) ou indisponível (`reversible: false`).
> 8. **Quem Pediu**: ID/nome do agente ou usuário solicitante.
> 9. **Quem Aprova**: Nível de autoridade RBAC/ABAC necessário para assinar o portão.
> 10. **Prazo**: Contagem regressiva (timeout) em tempo real para expiração automática da proposta.
> 11. **Consequência de Aprovar**: Detalhamento do impacto operacional imediato da liberação.
> 12. **Consequência de Rejeitar**: O impacto do cancelamento ou retorno ao estágio anterior.

* Se a ação for marcada como `reversible: false` (ex: envio de e-mail externo, transação financeira direta), um banner vermelho com a legenda "ESTA AÇÃO É IRREVERSÍVEL" é renderizado acima do botão de confirmação.

## 12. Regras de Evidência

* Toda solicitação de aprovação deve ser sustentada por um link de evidência com o lineage de dados que originou a necessidade da ação (ex: briefing assinado pelo cliente ou recomendação do PMO Auditor).

## 13. Mobile Behavior

* **Gestos Ergonômicos Táteis**: 
  * Deslizar (swipe) o botão "Approve" para a direita confirma a aprovação (gesto físico estável para evitar toques involuntários).
  * Toque longo no botão "Reject" abre o popover de justificativa no terço inferior da tela móvel.
* **Safe Position**: Posicionado de modo a ser operado estritamente pela metade inferior da tela, garantindo a facilidade de uso em dispositivos móveis com apenas uma mão.

## 14. Web Behavior

* **Interface Visual de Diff (Split-Screen)**: Exibe a lista lateral de arquivos afetados pela aprovação. Clicar em um arquivo abre instantaneamente o comparador de texto lado a lado (diff clássico colorido de adições e deleções de código/documentos) antes da confirmação da decisão.

## 15. Anti-Patterns

* **Aprovação Sem Consequência Clara**: Exibir apenas o botão "Aprovar" sem listar os arquivos que serão modificados no projeto ou as ferramentas de alto custo que serão disparadas no backend.
* **Ocultar Botão de Desfazer**: Omitir o botão de Rollback ou reverter para estados anteriores para workflows cujas ações no runtime são totalmente reversíveis.

## 16. Acceptance Criteria

* Toda tela de aprovação pendente deve listar o diff de arquivos alterados, a estimativa de custo de créditos, o indicador de reversibilidade e todos os 12 elementos obrigatórios do Approval Gate.
* A decisão do usuário deve resultar exclusivamente na emissão do evento `ApprovalSubmitted` para o runtime, sem escrita direta ad-hoc de tabelas.
* O widget de rollback (emitindo `RollbackWorkflowRequested` ou correlatos) deve ser exibido de forma destacada após a conclusão de qualquer workflow marcado como `reversible: true`.

## 17. Próximas Perguntas para Founder/PMO

* Devemos permitir a delegação temporária de portões de aprovação de um papel para outro (ex: Founder delegar aprovações de design para o PMO durante as férias) diretamente na interface ou essa regra deve ser rigidamente alterada apenas nas tabelas de política de segurança?
* No caso de ações de rollback em múltiplos arquivos complexos, a interface deve exibir um diff passo a passo da reversão ou apenas confirmar o retorno ao commit de segurança anterior?
