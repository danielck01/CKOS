---
title: "19 CKStore Capability Marketplace UI/UX Study"
system_id: study_notes_ckstore_capability_marketplace_uiux_study_20260528
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
  - "000_STUDY_NOTES/10_UIUX_STUDIES/11_COST_CREDITS_AND_ROI_AWARE_UX_STUDY.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/12_APPROVAL_GATE_AND_REVERSIBILITY_UX_STUDY.md"
tags:
  - uiux
  - study
  - marketplace
  - ckstore
  - capabilities
  - neurodesign
---

# 19 CKStore Capability Marketplace UI/UX Study

## 1. Propósito

Esta nota de estudo especifica os padrões de design UI/UX e neurodesign para a **CKStore (Capability Marketplace)** do CKOS. O objetivo é estabelecer diretrizes de interface para a navegação, seleção, simulação de impacto financeiro e instalação de novas habilidades (capabilities), subagentes especializados e conexões de ferramentas no sistema operacional.

## 2. O Que Este Padrão Resolve

* **Risco de Instalação Insegura**: Exige a exibição obrigatória de assinaturas digitais de segurança e auditorias do Metacognik antes da ativação.
* **Opacidade de Custo de Computação**: Simula preventivamente o impacto da nova ferramenta nas quotas mensais e no consumo médio de tokens do cliente.
* **Incerteza de Valor**: Apresenta dados estatísticos de ROI de outros workspaces que adotaram a capability para comprovar a utilidade real.

## 3. O Que Não Pode Virar

* **Loja de Aplicativos Móveis Convencional**: Não pode exibir anúncios comerciais, popups promocionais ou banners decorativos desprovidos de informações técnicas e de faturamento reais.
* **Repositório de Scripts Não Verificados**: Evita o download direto de códigos sem verificação automatizada de conformidade com as diretrizes do tenant.
* **Instalação Sem Consequência Financeira**: Não deve permitir a inclusão de capabilities tarifadas por cliques sem a devida autorização do administrador financeiro.

## 4. Relação com Runtime / Dashboard / Command Center / Node Canvas

* **Marketplace Service**: A interface lê metadados das tabelas de capabilities do tenant (`available_capabilities`, `installed_capabilities`).
* **Command Center**: O usuário busca e instala capabilities diretamente pela Commandbar (ex: `/install capabilities/github_collector`).
* **Node Canvas**: Habilidades recém-instaladas surgem como novos tipos de nós utilizáveis no canvas de workflows.

## 5. Cartão de Detalhes da Capacidade (Capability Details UX)

* **Perfil de Segurança do Desenvolvedor**: Badge informando a procedência (ex: *Oficial CKOS*, *Verificado por Auditor Terceiro*, *Código Aberto Comunitário*).
* **Projeção de Custo-Benefício (ROI)**: Bloco obrigatório exibindo a estimativa de tempo economizado por run (ex: `ROI Esperado: -30min por execução de auditoria`).
* **Simulador de Quotas (Quota Impact Snapshot)**: Gráfico minimalista de barras horizontais indicando a variação projetada no consumo mensal de storage e chamadas de API do workspace.

## 6. Execução em Sandbox (Trial Mode UX)

* **Visualizador de Sandbox**: Interface que delimita visualmente o modo de teste. O widget assume uma borda pontilhada cinza-violeta e isola os outputs gerados em uma pasta temporária restrita, impedindo modificações definitivas nos arquivos de produção.
* **Controle de Expiração**: Exibição em tempo real de contadores regressivos informando o término da sessão sandbox.

## 7. Relação com Dimensões CKOS

* **Cost**: Detalha taxas de licenciamento e estimativas de computação.
* **ROI**: Apresenta dados comparativos de valor agregado.
* **Approval**: Exige assinatura do responsável RBAC do tenant no botão físico "Aprovar e Instalar".
* **Learning**: Coleta dados de usabilidade da capability pós-uso para retroalimentar as notas de recomendação do marketplace.

## 8. Comportamento Web vs. Mobile

* **Web**:
  - Exibição de catálogo estruturado em formato de grid rico com filtros laterais densos (por categoria, por custo de créditos, por nível de risco).
* **Mobile**:
  - Layout simplificado de cartões deslizáveis (swiping deck) com foco em badges de conformidade e botão de instalação de toque rápido.

## 9. Anti-Patterns

* **Instalar Sem Simulação de Quotas**: Permitir que o usuário inclua uma capability que consome todos os seus créditos de runtime remanescentes em segundos devido a loops automáticos.
* **Ocultar Reputação de Erros**: Omitir dados sobre a estabilidade ou falhas técnicas históricas relatadas pelo Metacognik para a capability selecionada.

## 10. Acceptance Criteria

* O marketplace deve expor de forma clara se a capability exige co-pagamento externo ou consumo adicional de créditos do tenant.
* O acionamento de instalação de capacidades de risco `High` deve disparar obrigatoriamente um Approval Gate direcionado ao administrador do projeto.
* Toda capability instalada deve registrar seu ID e metadados no log de auditoria persistente do workspace.
