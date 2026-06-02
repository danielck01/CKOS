---
title: "23 UI/UX Canonical Patch Candidates"
system_id: study_notes_uiux_canonical_patch_candidates_20260528
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
  - "000_ROADMAPS/03_FRONTEND_UIUX_ROADMAP/01_UIUX_STUDY_TO_CANONICAL_ROADMAP.md"
tags:
  - uiux
  - study
  - canonical_candidates
  - governance
---

# 23 UI/UX Canonical Patch Candidates

## 1. Propósito

Esta nota de estudo especifica o catálogo de **Candidatos a Patches Canônicos de UI/UX (Canonical Patch Candidates)** para o CKOS. O objetivo é compilar, estruturar e qualificar as diretrizes operacionais desenvolvidas na camada de estudos (arquivos 01 a 22) para futura promoção aos documentos canônicos da arquitetura do sistema (01–25), garantindo que as regras visuais passem por homologação formal antes de se tornarem diretrizes definitivas de engenharia.

## 2. O Que Este Padrão Resolve

* **Desconexão Entre Estudo e Engenharia**: Fornece um canal formal para propor atualizações nos documentos canônicos oficiais sem fazer modificações diretas ad-hoc não autorizadas.
* **Perda de Rastreabilidade de Decisões**: Mantém o registro histórico de por que determinadas gramáticas ou restrições visuais foram promovidas ou rejeitadas.
* **Modificações Prematuras**: Evita vazamentos de conceitos provisórios de design para o núcleo estável do CKOS.

## 3. O Que Não Pode Virar

* **Modificação Direta de Documentos Canônicos 01–25**: Este arquivo é uma proposta e permanece na pasta de estudos auxiliares; ele não altera as regras oficiais até que uma sessão específica de `canonical_patch` seja autorizada pelo Founder.
* **Lista de Desejos Estéticos**: Não deve conter propostas cosméticas ou subjetivas de estilo; apenas alterações funcionais e neurocognitivas sustentadas por evidências e ROI.

## 4. Relação com Runtime / Dashboard / Command Center / Node Canvas

* **Workflow Engine / Schema Definition**: As propostas de alteração canônica afetam as definições de schemas das tabelas de runtime (ex: inclusão dos novos status na tabela de workflows).
* **Governance Registry**: Alinha-se diretamente com o fluxo descrito em `01_UIUX_STUDY_TO_CANONICAL_ROADMAP.md` para a promoção de diretrizes.

## 5. Catálogo de Candidatos a Patches Canônicos

A seguir, listamos as diretrizes da camada de estudo qualificadas como candidatas a promoção:

### 5.1 Candidato 1: Matriz de 19 Estados de Execução de Workflows
* **Escopo Alvo**: Alteração em [16_NODE_CANVAS_ARCHITECTURE.md](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/04_PRODUCT_SYSTEM/16_NODE_CANVAS_ARCHITECTURE.md) §9 (ou equivalente).
* **Proposta**: Integrar a matriz de estados de execução conceituais e triá-la contra as state machines oficiais já documentadas na arquitetura do Node Canvas, eliminando discrepâncias entre o que a IA executa e o que a interface exibe.

### 5.2 Candidato 2: 12 Elementos Obrigatórios do Approval Gate
* **Escopo Alvo**: Alteração em `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md` (Approval Gate).
* **Proposta**: Canonizar a regra rígida de que nenhum portão de aprovação visual pode ser renderizado ou assinado se omitir qualquer um dos 12 elementos de contexto definidos em `12_APPROVAL_GATE_AND_REVERSIBILITY_UX_STUDY.md`.

### 5.3 Candidato 3: Tripla Estrutura Epistêmica de Respostas
* **Escopo Alvo**: Alteração em `04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md`.
* **Proposta**: Forçar o Command Center e Nick a responderem estruturalmente dividindo toda afirmação em: Nível de Confiança, Links de Evidência e Declaração de Limitações.

### 5.4 Candidato 4: Regras de Validação WCAG no Runtime
* **Escopo Alvo**: Inclusão nos manuais de governança de design system.
* **Proposta**: Tornar obrigatória a validação matemática em tempo real de taxas de contraste no serviço de temas do CKOS antes de persistir customizações whitelabel.

### 5.5 Candidato 5: Tabela de Preferências de Densidade Visual (RBAC/ABAC)
* **Escopo Alvo**: Alteração em [11_DATA_MODEL_AND_PERSISTENCE.md](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md).
* **Proposta**: Criar formalmente a tabela `preferences`, com RLS policies por role (RBAC/ABAC), e registrar o evento `UserPreferenceUpdated` para salvar configurações de densidade de IA (Low vs. High Density) baseando-se no papel (role) do usuário. A definição de serviço de runtime correspondente é escopo de Doc 10/11 e não desta proposta de estudo.

### 5.6 Candidato 6: Tabelas de Governança da CKStore
* **Escopo Alvo**: Alteração em `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md`.
* **Proposta**: Adicionar as tabelas `available_capabilities` e `installed_capabilities` para registrar as habilidades e subagentes instalados, suas estimativas de quotas e assinaturas de segurança.

### 5.7 Candidato 7: Persistência do Histórico do Command Center
* **Escopo Alvo**: Alteração em `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md`.
* **Proposta**: Implementar a tabela `command_history` (conforme registrado como pendência no Doc 15 §13) para gerenciar o histórico de atalhos e intents enviados pelo usuário.

### 5.8 Candidato 8: Registro de Feedback Explícito no Learning
* **Escopo Alvo**: Alteração em `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md`.
* **Proposta**: Criar a tabela `feedback_entries` e os eventos `FeedbackSubmitted` / `FeedbackImplicit` para consolidar o feedback dos usuários em runs concluídos.

### 5.9 Candidato 9: Modelagem Financeira de Créditos e Wallets
* **Escopo Alvo**: Alteração em [24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/06_BUSINESS_SYSTEMS/24_CREDITS_PLANS_AND_BILLING_ARCHITECTURE.md).
* **Proposta**: Utilizar a modelagem financeira existente no Doc 24 para subsidiar a exibição de quotas e saldos do Cost Mode, mapeando as interfaces e projeções de runtime diretamente para as tabelas `credit_wallets`, `credit_transactions`, `credit_reservations`, `usage_events`, `billing_events`, `invoice_records`, `plan_limits`, `quota_policies` e `cost_ledger` (este último para conciliação de custos internos/runtime). Não devem ser propostas novas tabelas financeiras conflitantes.

### 5.10 Candidato 10: Evento de Monitoramento de Loops de IA
* **Escopo Alvo**: Alteração em `03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md` (ou State Machine).
* **Proposta**: Definir o evento formal `AgentLoopDetected` disparado pelo runtime quando uma conversa atinge 5 iterações sem intervenção, acionando o aviso visual correspondente.

### 5.11 Candidato 11: Mentions Oficiais do Ingress
* **Escopo Alvo**: Alteração em `04_PRODUCT_SYSTEM/15_COMMAND_CENTER_ARCHITECTURE.md`.
* **Proposta**: Formalizar o suporte na commandbar para as 9 mentions oficiais (`@nick`, `@cognik`, `@metacognik`, `@pmo_ckos`, `@qa_lead`, `@builder_lead`, `@datta`, `@ops`, `@campaign`).

### 5.12 Candidato 12: Persistência de Layout de Widgets do Dashboard
* **Escopo Alvo**: Alteração em `04_PRODUCT_SYSTEM/14_PROJECT_DASHBOARD_ARCHITECTURE.md`.
* **Proposta**: Criar o evento `LayoutPreferenceUpdated` para persistir alterações de ordenação e visibilidade efetuadas pelo usuário na grade de widgets.

### 5.13 Candidato 13: Standardização de Projeções de Leitura do Dashboard
* **Escopo Alvo**: Alteração em `03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md` (e referências RAG).
* **Proposta**: Banir terminologias obsoletas (como "Project Pulse") e fixar o nome `project_dashboard_projection` para o read model agregado de saúde do projeto.

### 5.14 Candidato 14: Validated Memory Projection / Approved Memory Read Model
* **Escopo Alvo**: Alteração em [11_DATA_MODEL_AND_PERSISTENCE.md](file:///c:/Users/Usuario/Documents/CKCompany/CKOS/Research/Arquitetura-System/CKOS_DOCUMENTATION_REVIEWED/03_RUNTIME_SYSTEM/11_DATA_MODEL_AND_PERSISTENCE.md).
* **Proposta**:
  * Definir o read model `approved_memory_projection` no Doc 11 canônico para expor memórias aprovadas, decisões consolidadas, aprendizados validados e feedbacks homologados a serem exibidos no painel de ROI & Aprendizados.
  * Deixar explícito que a projeção ainda não é canônica, não autoriza qualquer implementação de código física e deve ser formalmente integrada ao Doc 11 antes que qualquer interface dependa de seus dados.
  * O runtime da interface nunca lerá diretamente o arquivo `ck_memory.md` como banco de dados.
  * A projeção de banco de dados deve obedecer a regras rígidas de segurança de runtime, incluindo Row-Level Security (RLS), isolamento por tenant, audit_logs de auditoria, rastreabilidade de provenance, confidence scores e histórico de aprovação de eventos.

## 6. Relação com Dimensões CKOS

* **Learning**: Consolida feedbacks operacionais e empíricos coletados durante a fase de estudo para aprimorar as regras estáveis de arquitetura.
* **Evidence**: Cada proposta de promoção deve ser acompanhada de relatórios de conformidade e testes de usabilidade que atestem sua eficácia (ROI).
* **Approval**: A transição de candidato para canônico exige aprovação em três níveis: PMO Auditor, Metacognik Reviewer e Founder.

## 7. Anti-Patterns

* **Canonizar Sem Testes Práticos**: Promover uma diretriz visual de exibição de dados complexos que resulte em aumento de retrabalho ou fadiga vestibular detectados nos evals.
* **Vazamento de Propostas**: Permitir que equipes de front-end utilizem as especificações deste documento como regra rígida de produção antes da homologação formal de ativação de lane.

## 8. Critérios de Aceitação para Promoção

* A proposta deve ser descrita em formato de Diff de modificação aplicável ao respectivo documento canônico de destino.
* A estimativa de custos computacionais e operacionais para a implementação de cada candidato deve ser declarada.
* O Metacognik deve atestar a conformidade epistemológica de cada regra sugerida para canonização.
