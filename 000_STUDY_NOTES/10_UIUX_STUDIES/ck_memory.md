---
title: "10 UI/UX Studies - ck_memory"
system_id: study_notes_uiux_studies_ck_memory_20260528
layer: auxiliary
phase: 000_STUDY_NOTES
category: folder_memory
status: study_not_canonical
version: 1.7.0
owner: pmo_ckos
responsible_agent: antigravity_design_study
reviewers:
  - founder
  - pmo_ckos
  - metacognik
approval_required:
  - founder
  - pmo_ckos
  - metacognik
confidence: unverified
provenance_status: unverified
source_tool: antigravity
created_at: 2026-05-28
purpose: "Manter a memória operacional da pasta de estudos de UI/UX da camada de estudo do CKOS."
inputs:
  - "000_STUDY_NOTES/04_UI_UX_STUDY/10_Referências_Design"
  - "000_ROADMAPS/19_UIUX_STUDY_ROADMAP/README.md"
outputs:
  - "ck_memory.md"
tags:
  - "uiux_studies"
  - "ck_memory"
  - "auxiliary"
---

# ck_memory - 10_UIUX_STUDIES

## Purpose

A pasta `000_STUDY_NOTES/10_UIUX_STUDIES/` armazena as notas de estudo conceituais focadas na tradução de referências visuais em gramáticas de interface operacionais para o CKOS. É uma camada de suporte de governança e design conceitual, sem autoridade de implementação ou modificação canônica.

## Folder Status

Status: study, not canonical (auxiliary study folder).

Esta pasta não autoriza desenvolvimento de front-end ou backend, criação de componentes reais React/HTML/CSS, modificações de banco de dados, migrações, automações runtime ou ativação de agentes em runtime real.

## Main Files

- `ck_memory.md`: Memória de execução e decisões desta pasta.
- `README.md`: Índice Mestre organizando as 23 notas de estudo de UI/UX em 10 famílias conceituais.
- `UIUX_STUDY_REVIEW_REPORT.md`: Relatório de revisão consolidado mapeando famílias, gaps conceituais, riscos e próximos passos recomendados.
- `UIUX_CANONICAL_CANDIDATE_TRIAGE_REPORT.md`: Relatório de triage dos 14 candidatos a patches canônicos de UI/UX, classificando sua elegibilidade de promoção.
- `01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md`: Taxonomia das famílias visuais das referências de design.
- `02_OPERATIONAL_UIUX_GRAMMAR_CKOS.md`: Mapeamento das 11 perguntas estratégicas para componentes e superfícies da interface do CKOS, com substituição completa do antigo conceito "Project Pulse" pelo read model "Project Dashboard projection" (referência histórica da nota de estudo; o nome canônico oficial confirmado em Docs 10, 11, 14 e 15 é `project_pulse_projection`).
- `03_WIDGET_STATE_MATRIX_AND_EXECUTION_FEEDBACK.md`: Matriz de transição de estados de IA nos widgets, custos e alinhamento com as state machines oficiais do doc 16.
- `04_MOBILE_COMMAND_FIRST_ERGONOMICS.md`: Regras ergonômicas de toque móvel baseadas na metade inferior, contendo especificações técnicas de breakpoints, targets, safe areas, teclado virtual e gestos.
- `05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md`: Fundamentação neurológica baseada em exatamente 10 princípios cognitivos aplicados ao CKOS, expandida para incluir a Lei de Fitts (targets de toque) e as Leis da Gestalt (agrupamento visual).
- `06_UIUX_ANTI_PATTERNS_AND_GENERIC_AI_UI_RISKS.md`: Relação de exatamente 10 anti-padrões e riscos visuais de interface, incluindo Empty State Decorativo e Aprovação Sem Consequência Clara.
- `07_AGENT_ACTIVITY_STREAM_UIUX_STUDY.md`: Especificação conceitual do stream de atividades dos agentes, diferenciando-o de outras superfícies e proibindo chat logs genéricos.
- `08_WHITELABEL_TOKEN_SYSTEM_UIUX_STUDY.md`: Diretrizes para customização visual tematizada whitelabel, listando tokens invariantes, tematizáveis, proibidos, estados críticos e regras de contraste WCAG.
- `09_EXECUTION_PLAN_WIDGET_UIUX_STUDY.md`: Estudo dos padrões de design do Widget de Plano de Execução, integrando progresso, custos, riscos e portões de aprovação.
- `10_INTENT_CLARIFIER_AND_SMART_QUESTIONS_UIUX_STUDY.md`: Estudo dos padrões do clarificador de intenções e das perguntas inteligentes, integradas a ROI, risco e custo.
- `11_COST_CREDITS_AND_ROI_AWARE_UX_STUDY.md`: Estudo da interface orientada a custos, pre-reserva de créditos de runtime, wallets e ROI com base em aprendizados.
- `12_APPROVAL_GATE_AND_REVERSIBILITY_UX_STUDY.md`: Estudo dos portões de aprovação de segurança, com consequências explícitas e botões de reversão (rollback).
- `13_EVIDENCE_TRUST_AND_DECISION_UIUX_STUDY.md`: Estudo do mapa de evidências interativo, com confidence scores do Metacognik, links de lineage das fontes e declaração de limitações de IA.
- `14_DASHBOARD_WIDGET_SYSTEM_UIUX_STUDY.md`: Estudo dos padrões do sistema de widgets do dashboard, organizados por colunas dinâmicas, com exposição de custos e ROI.
- `15_COMMAND_CENTER_OPERATIONAL_UX_STUDY.md`: Estudo da Commandbar central, com atalhos `/` e `@`, autocomplete contextual e backlight semântico.
- `16_NODE_CANVAS_GRAPH_UX_STUDY.md`: Estudo do canvas de grafos 2D, com navegação por teclado, spring physics de nós, lineages de evidência e fallback de acessibilidade.
- `17_CHAT_GROUPS_AGENT_THREADS_UIUX_STUDY.md`: Estudo das threads técnicas de agentes estruturadas de forma linear, limites de escopo e avisos contra loops de IA.
- `18_ONBOARDING_PERSONALIZATION_UIUX_STUDY.md`: Estudo de onboarding de novos usuários, com calibração de perfis de densidade visual e estabelecimento de ROI base.
- `19_CKSTORE_CAPABILITY_MARKETPLACE_UIUX_STUDY.md`: Estudo do marketplace de capacidades, com perfis de segurança, projeção de impacto de quotas e sandbox trial mode.
- `20_DESIGN_SYSTEM_THEME_GOVERNANCE_UIUX_STUDY.md`: Estudo da governança de temas whitelabel, distinguindo tokens semânticos invariantes de estilizações e forçando contraste WCAG.
- `21_MOTION_STATE_FEEDBACK_UIUX_STUDY.md`: Estudo do design cinético e micro-feedbacks, com restrição de tempos e mapeamento de estados de execução.
- `22_ACCESSIBILITY_REDUCED_MOTION_UIUX_STUDY.md`: Estudo de acessibilidade e redução de movimento, cobrindo WCAG 2.1, navegação por teclado dupla e fallbacks em árvore.
- `23_UIUX_CANONICAL_PATCH_CANDIDATES.md`: Estudo dos candidatos operacionais recomendados para promoção futura aos documentos canônicos oficiais.

## Registered Decisions

- **Substituição do Project Pulse**: O conceito não canônico temporário de "Project Pulse" foi inteiramente substituído por "Project Dashboard" e sua respectiva fonte de dados "Project Dashboard projection", prevenindo o vazamento de elementos de código rígidos.
- **Estruturação do Agent Activity Stream**: Definido como uma timeline de lineage técnica 1D alinhada à esquerda. Proibição explícita de layouts estilo chat (WhatsApp/ChatGPT) e foco total em mutabilidade de arquivos.
- **Neurodesign Expandido**: Consolidação de exatamente 10 princípios pragmáticos (Hick's, Miller's, Divulgação Progressiva, Hierarquia Tipográfica, Sinais de Confiança na IA, Recuperação de Erros, Carga Cognitiva, Fadiga de Decisão, Fitts's Law e Leis da Gestalt) no CKOS.
- **Resolução de Anti-padrões**: Entrega de exatamente 10 anti-padrões no catálogo de interface, adicionando obrigatoriamente os desvios de Empty State Decorativo e Aprovação Sem Consequência Clara.
- **Segurança Temática (Whitelabel)**: Criação de um sistema rígido de design tokens contendo verificação WCAG automática (taxa mínima de contraste 4.5:1 para texto normal) e isolamento estrito de cores semânticas de status para preservar a usabilidade.
- **Expansão de Padrões Operacionais**: Incorporação dos 5 estudos avançados de interface (Execution Plan Widget, Intent Clarifier, Cost/Credits, Approval Gate e Evidence Map) na camada auxiliar de UI/UX, detalhando regras operacionais rígidas e alinhando com a máquina de estados do runtime do CKOS.
- **Patch P1.8 - Alinhamento de Notas de Estudo UI/UX**: Executado o alinhamento das notas de estudo 09, 11, 12 e 13 às especificações de governança e arquitetura do CKOS.
- **Markdown Não é Runtime Database**: Firmada a decisão arquitetural rígida de que a interface (UI/UX) consome dados exclusivamente de event bus, CQRS projections e tabelas do banco de dados (ex: `roi_snapshot_projection`, `cost_projection`, `credit_wallets`, `credit_transactions`, `usage_events`, `billing_events`, `evidence_items`, `roi_evidence_links`, approvals e logs). Arquivos markdown (como `ck_memory.md`) funcionam exclusivamente como memória auxiliar documental e nunca devem ser parseados ou lidos pelo runtime da interface de produção.
- **Conclusão do Patch P1.9 - UI/UX Study Completion**: Criação e consolidação dos 10 estudos finais da camada UI/UX (arquivos 14 a 23) cobrindo todos os fluxos operacionais previstos, desde o Dashboard até a governança e acessibilidade. Todos os arquivos foram validados para garantir ausência total de implementações físicas e conformidade estrita com o mapeamento das 8 dimensões centrais do CKOS.
- **Alinhamento do Patch P1.9 (Audit Recommendations)**: Resolvidos os 3 bloqueadores P0 e lacunas críticas. Standardização de `project_dashboard_projection` no Intent Clarifier (Note 10), expansão da fundação de neurodesign para exatamente 10 princípios pragmáticos (Note 05), alinhamento estrutural do Command Center com Doc 15 v1.2.1 (Note 15), e ampliação do backlog de candidatos canônicos para no mínimo 13 candidatos mapeados (Note 23).
- **Consolidação e Mapeamento de Famílias (P1.10)**: Consolidação completa das 23 notas de estudo de UI/UX em exatamente 10 famílias conceituais e criação do relatório de revisão contendo 10 lacunas críticas de interface, 5 riscos operacionais e a recomendação de abertura de lane de homologação canônica.
- **Ajustes Leves (P1.10.2)**: Correção de referências ao `approved_memory_projection` na Note 02, alinhamento do `responsible_agent` e heading no Review Report, substituição de linguagem de backend na Note 23 (Candidato 5) e criação do Candidato 14.
- **Triage de Candidatos Canônicos (P1.11)**: Execução da triage oficial para os 14 candidatos a patches canônicos de UI/UX, catalogando-os em grupos de promoção, estudo, mais evidência, adiamento ou rejeição (como o Candidato 13, cuja projeção canônica mestre correta é a `project_pulse_projection`).
- **Reescrita Compreensiva do Triage (P1.11 v2.0.0)**: Reescrita integral do relatório de triage com cross-referencing profundo contra docs canônicos (Docs 10, 11, 13, 14, 15, 16, 24). Cada candidato agora inclui: base canônica consultada com linhas e seções, cross-referencing detalhado, condições para promoção e inconsistências registradas. Confirmou-se: `command_history` (INC-01) referenciada no Doc 15 em 5 pontos sem DDL no Doc 11; `project_pulse_projection` possui 24+ referências canônicas (INC-13); `dashboard_preferences` já existe no Doc 11 §34 com campo `density` (INC-05); Doc 15 §5.5 cobre 100% das 9 @mentions (Candidato 11 → KEEP_AS_STUDY); `AgentLoopDetected` referenciado no Doc 15 L882 sem schema no Doc 10 (INC-10).
- **P1.11 Light Patches Pós-Auditoria**: Aplicação dos patches leves PL-01 a PL-06 solicitados pela auditoria PMO+Metacognik, marcando "Project Dashboard projection" como referência histórica não-canônica, corrigindo targets e justificativas do triage report, removendo linguagem de implementação e distinguindo `AgentLoopDetected` de `LoopDetected`.

## P1.11.1 — PMO Closure Note

- P1.11 foi concluído operacionalmente.
- Os light patches foram aplicados.
- A camada `10_UIUX_STUDIES` está pronta para triage canônico futuro.
- A camada continua Study Layer.
- Nenhum estudo UI/UX pode ser tratado como source of truth canônico.
- Implementação segue bloqueada.
- Próximo passo recomendado: Doc 26 — Connectors, MCP and Integrations Architecture.
- UI/UX Canonical Triage só deve acontecer depois ou em paralelo com aprovação PMO explícita.

```txt
PMO decision:
UI/UX Study Layer may be used as reference material, not as implementation authority.
```

## Risks (Riscos Remanescentes)

- Confundir as diretrizes de estudo de interface com permissão para iniciar desenvolvimento de componentes React reais.
- Desenvolvedores ou subagentes tentarem implementar ou codificar as notas de estudo antes da abertura formal de uma lane P2 de interface e aprovação pelo Founder.
- Risco de o tema claro (Light Mode) configurado por clientes corporativos diminuir o contraste das timelines técnicas se as regras de máscara de contraste forem ignoradas pelas customizações de marca de alta intensidade.
- O excesso de informações financeiras, evidências e diffs de arquivos na interface móvel causar confusão visual se a hierarquia tipográfica e o colapsamento sob demanda de elementos não forem rigorosamente implementados.

## Next Steps (Próximos Patches)

- Usar a camada `10_UIUX_STUDIES` somente como material de referência para triage canônico futuro, sem autoridade de implementação.
- Priorizar o próximo passo recomendado: Doc 26 — Connectors, MCP and Integrations Architecture.
- Realizar UI/UX Canonical Triage somente depois ou em paralelo com aprovação PMO explícita.
