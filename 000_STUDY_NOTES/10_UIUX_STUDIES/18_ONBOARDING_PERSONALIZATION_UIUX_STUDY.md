---
title: "18 Onboarding and Personalization UI/UX Study"
system_id: study_notes_onboarding_personalization_uiux_study_20260528
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
  - "000_STUDY_NOTES/10_UIUX_STUDIES/05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/11_COST_CREDITS_AND_ROI_AWARE_UX_STUDY.md"
tags:
  - uiux
  - study
  - onboarding
  - personalization
  - cognitive_load
  - neurodesign
---

# 18 Onboarding and Personalization UI/UX Study

## 1. Propósito

Esta nota de estudo especifica os padrões de design UI/UX e neurodesign para o **Onboarding e Personalização** do CKOS. O objetivo é criar diretrizes conceituais para a recepção de novos usuários, calibração inicial de perfis, definição de níveis de exposição a dados técnicos (densidade visual) e configuração de metas base de eficiência e retorno de investimento.

## 2. O Que Este Padrão Resolve

* **Sobrecarga Cognitiva Inicial**: Evita o impacto de apresentar uma interface de canvas 2D densa com timelines técnicas para usuários de negócios não familiarizados com sistemas AI-first.
* **Desalinhamento de Nível Técnico**: Ajusta a exibição automática de logs profundos e terminais de subagentes com base na função do tomador de decisão (RBAC/ABAC).
* **Ausência de Linha de Base (Baseline)**: Estabelece as métricas de tempo e custo manuais históricos antes da primeira execução para possibilitar a comparação real de ROI no dashboard.

## 3. O Que Não Pode Virar

* **Janela Pop-up de Boas-Vindas Genérica**: Não deve ser um guia passivo com imagens estáticas contendo um botão "Avançar" mecânico.
* **Pesquisa de Briefing Longa**: Evita questionários burocráticos sem retorno visível na configuração imediata da interface.
* **Customização Puramente Estética**: Não se limita a escolher papéis de parede ou avatares; a personalização deve alterar as regras de exposição de dados e alertas de segurança.

## 4. Relação com Runtime / Dashboard / Command Center / Node Canvas

* **Preferences Service (Configuração de Usuário)**: O onboarding grava dados diretamente nas tabelas de preferências do banco de dados, configurando os filtros visuais padrão das projeções.
* **Command Center**: O modo de Commandbar (atalhos sugeridos) adapta-se ao nível técnico selecionado no onboarding.
* **Node Canvas**: O nível de zoom inicial e a visibilidade de dependências complexas são configurados com base nas preferências coletadas.

## 5. Fluxo de Integração e Calibração de Perfil (Onboarding Wizard)

* **Etapas Interativas Curtas (Máximo 3)**:
  1. *Perfil de Acesso e RBAC*: O usuário declara sua função (ex: Administrador, Auditor, Gestor, Desenvolvedor).
  2. *Densidade Visual de IA*: Ajuste deslizável de exposição técnica:
     - **Low Density**: Foco em outputs e aprovações sem exibição de logs de terminais ou diffs profundos.
     - **High Density (Auditor/Dev)**: Terminais ativos, diffs de código completos e lineage em grafos 2D visíveis por padrão.
  3. *Métricas de Eficiência Base*: Entrada opcional do tempo médio que a organização leva para realizar as tarefas manualmente (criação da linha de base de ROI).

## 6. Personalização de Nível de IA e Carga Cognitiva

* **Configuração de Fadiga de Decisão**: Limitação do número de alertas de aprovação simultâneos dependendo do perfil (perfis de alto nível gerencial recebem apenas portões P0 críticos).
* **Divulgação Preditiva de Recursos**: Ocultação de atalhos e coletores avançados no Command Center até que o usuário conclua com sucesso as primeiras tarefas básicas.

## 7. Relação com Dimensões CKOS

* **Intention**: Captura as preferências iniciais de operação do usuário.
* **Context**: Adapta a interface às restrições de privilégios e dados do tenant.
* **ROI**: Define a linha de base de tempo economizado que será usada pelas projeções de ROI.
* **Learning**: Adapta as mensagens de Nick (IA do sistema) com base no nível técnico do perfil.

## 8. Comportamento Web vs. Mobile

* **Web**:
  - Wizard interativo em tela cheia com animações de transição de estado suaves.
* **Mobile**:
  - Formulário condensado na metade inferior, otimizando o preenchimento por meio de cartões de seleção rápidos com o polegar.

## 9. Anti-Patterns

* **Interface Factual Única**: Tentar forçar o mesmo nível de dados técnicos densos para administradores financeiros e desenvolvedores de infraestrutura (falha de adequação cognitiva).
* **Falta de Opção de Reset**: Impedir que o usuário ajuste suas preferências de densidade visual nas configurações do painel após a conclusão do onboarding.

## 10. Acceptance Criteria

* O perfil calibrado no onboarding deve determinar as configurações de exibição das timelines técnicas no primeiro login do usuário.
* As métricas de ROI base digitadas devem ser salvas de forma segura para subsidiar os cálculos do painel de retorno financeiro.
* O fluxo de onboarding deve poder ser abortado, assumindo configurações padrão seguras e sem quebrar as permissões RBAC.
