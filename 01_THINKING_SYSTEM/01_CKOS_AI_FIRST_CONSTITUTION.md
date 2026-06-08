---
title: CKOS AI First Constitution
file: 01_CKOS_AI_FIRST_CONSTITUTION.md
phase: 01_THINKING_SYSTEM
category: constitution
version: 1.1.0
status: active
owner: PMO_CKOS
responsible_agent: PMO_CKOS
reviewers:
  - Metacognik
approval_required:
  - founder
purpose: Travar a visão central do CKOS como sistema operacional AI First cognitivo e metacognitivo, não dashboard/chatbot/gerador de proposta.
inputs: Visão CKCompany; tese CKOS; aprendizado Goddess; intenção de "Manus próprio"; necessidade de reduzir prompts manuais do Founder.
outputs: Princípios não negociáveis; definição de AI First real; limites; regras de adaptação; visão de evolução.
framework: Sinais → Interpretação → Nodes → Agentes → Hipóteses → Evidências → Decisões → Execução → Aprendizado.
edge_cases: Módulo sem sentido; recomendação com baixa evidência; "automatizar tudo"; projeto muda de natureza; output bonito sem função.
integrations: Claude Code, Codex, Antigravity, Manus, Base44, OpenRouter, Supabase, Redis, RAG, Apify (meios, não o sistema).
prompts: Estrutura de prompt constitucional; prompt proibido vs correto.
metrics: Tempo intenção→node; redução de perguntas manuais; % outputs com approval; decisões registradas.
related_notes:
  - 02_AI_FIRST_OBJECT_MODEL.md
  - 03_AGENT_OPERATING_MODEL.md
  - 04_AUTONOMY_AND_APPROVALS.md
  - 05_MEMORY_AND_CONTEXT_ARCHITECTURE.md
  - ../03_RUNTIME_SYSTEM/10_SYSTEM_RUNTIME_ARCHITECTURE.md
tags: [thinking, constitution, ai_first, principles, whitelabel]
---

# 1. Propósito

Travar a visão central do CKOS como um **sistema operacional AI First cognitivo e metacognitivo**, não como dashboard, chatbot, repositório, gerador de propostas ou coleção de páginas bonitas.

A constituição impede três desvios fatais:

1. transformar o CKOS em SaaS genérico com IA anexada;
2. criar módulos fixos antes de entender o projeto;
3. tratar agentes como personagens decorativos em vez de força operacional real.

O CKOS é uma camada viva de interpretação, decisão, execução e aprendizado: recebe sinais, organiza contexto, cria nodes, aciona agentes, pede aprovação quando necessário, executa ações permitidas e aprende com os resultados.

# 2. Função dentro do CKOS

Fonte de verdade para decisões de produto, arquitetura de agentes, nodes, CommandBar, Canvas, workflows, memória, autonomia, aprovações e implementação (Claude, Codex, Antigravity, Manus ou agentes internos futuros).

Sempre que houver dúvida entre "construir uma tela bonita" e "construir uma operação inteligente", este documento vence.

# 3. Inputs

- visão estratégica da CKCompany; tese do CKOS; necessidade de whitelabel; aprendizado Goddess × CKCompany; intenção de ter um Sistema operacional AI FIRST; necessidade de reduzir prompts manuais do Founder; necessidade de aprovação humana em decisões críticas; arquitetura de agents/superagents/subagents/skills/nodes/workflows/memória.

# 4. Outputs

- princípios não negociáveis; definição de AI First real; limites do que o CKOS não deve ser; regras de adaptação por projeto; princípios de autonomia e aprovação; visão de evolução; diretrizes anti-entropia.

# 5. Framework operacional

## 5.1 Definição principal

**CKOS é um sistema operacional cognitivo e metacognitivo para transformar intenção, contexto, dados, arquivos, stakeholders, agentes e decisões em operação inteligente.** Ele não espera o usuário terminar tudo para gerar relatório — diagnostica em tempo real.

## 5.2 Fórmula operacional

```txt
Sinais → Interpretação → Nodes → Agentes → Hipóteses → Evidências → Decisões → Execução → Aprendizado
```

Esta fórmula é materializada concretamente em `10_SYSTEM_RUNTIME_ARCHITECTURE.md`.

## 5.3 Sistema com IA vs AI First real

```txt
Com IA:    Usuário navega → clica → pergunta → IA responde
AI First:  Usuário expressa intenção → sistema interpreta → cria nodes → aciona agentes
           → audita riscos → recomenda decisões → executa com aprovação → aprende
```

## 5.4 Princípios constitucionais

- **P1. O projeto define os módulos, não o contrário.** Commerce, Ads, CRM, Events, Product, Community, Research e Finance entram como capabilities ativáveis, não páginas obrigatórias.
- **P2. O diagnóstico é vivo.** Hipóteses, lacunas, riscos, perguntas inteligentes e evidências aparecem durante o processo, não só no fim.
- **P3. O Canvas é o espaço de pensamento.** Ambiente onde nodes, agentes, evidências, decisões e workflows se conectam.
- **P4. CommandBar é centro operacional.** Entrada de intenção, comando, agente, arquivos, ações e execução contextual — não busca.
- **P5. Agentes precisam produzir mudança de estado.** Todo agente gera ao menos: insight, hipótese, node, tarefa, decisão, risco, evidência, prompt, artefato, workflow ou recomendação de aprovação.
- **P6. Metacognição é obrigatória.** Toda recomendação importante é auditável por Metacognik (confiança, lacunas, contradições, risco, dependências, necessidade de aprovação).
- **P7. O Founder aprova decisões de alto impacto.** A autonomia pode crescer, mas decisões críticas têm approval gates. O sistema recomenda, prepara e executa ações reversíveis sem atravessar limites estratégicos sem governança.
- **P8. Whitelabel não é só trocar cor.** Adapta tema, linguagem, módulos, agentes, capabilities, workflows, permissões, dados, outputs e apresentação por projeto.
- **P9. Tudo que importa vira memória.** Decisões, aprovações, hipóteses, outputs, erros e aprendizados são registrados. Sem memória, não há sistema — há conversa.
- **P10. A IA reduz a carga cognitiva do Founder.** O objetivo não é o Founder enviar prompts melhores para Claude/Codex/Manus, mas o CKOS preparar tarefas, distribuir para agentes, receber outputs, auditar qualidade e pedir aprovação quando necessário (ver `21_SELF_EVOLVING_SYSTEM.md`).

# 6. Agente responsável

`PMO_CKOS` mantém a constituição viva: protege coerência sistêmica, impede desvio para SaaS genérico, avalia features contra os princípios, exige documentação antes de implementação e mantém dependências claras.

# 7. Superagentes envolvidos

- **Nick**: interface relacional e orquestração com usuário.
- **Cognik**: interpretação de sinais e criação de hipóteses.
- **Metacognik**: auditoria do raciocínio, risco e confiança.
- **PMO_CKOS**: governança de roadmap, execução e dependências.
- **Builder Lead**: coordenação dos Builder Subagents.
- **QA Lead**: validação de qualidade, regressão e aprovação.

# 8. Skills necessárias

agent-orchestration; intelligent-briefing; realtime-diagnosis; node-creation; approval-routing; memory-routing; workflow-planning; quality-gate; implementation-handoff; risk-analysis.

# 9. Prompts relacionados

Estrutura de prompt constitucional:

```txt
Contexto → intenção → objeto afetado → agente responsável → output esperado → approval gate → métrica de sucesso → edge cases
```

```txt
Proibido:  Crie um dashboard bonito para X.
Correto:   Crie uma capability ativável para X: quando deve surgir, quais nodes cria, quais agentes aciona, quais dados exige, quais riscos gera, qual UI mínima precisa e quais aprovações são necessárias.
```

# 10. Integrações

Claude Code, Codex, Antigravity, Manus, Base44, OpenRouter, Supabase, Redis, Obsidian/RAG, Apify, Google Calendar, WhatsApp, ferramentas de pesquisa e de geração de imagem/vídeo. Integrações são meios; o CKOS é o sistema de coordenação.

# 11. Memória e contexto

Três camadas (detalhe em `05_MEMORY_AND_CONTEXT_ARCHITECTURE.md`, materialização em `11_DATA_MODEL_AND_PERSISTENCE.md`):

- **Curto prazo**: sessão ativa, conversa, comandos recentes, nodes em execução.
- **Médio prazo**: projeto, briefing vivo, decisões recentes, agentes ativos, outputs em aprovação.
- **Longo prazo**: histórico da marca, decisões aprovadas, aprendizados, identidade, stakeholders, performance, documentação e padrões.

# 12. Edge cases

1. Usuário pede módulo sem sentido → não criar automaticamente; perguntar, diagnosticar, classificar como hipótese/capability futura.
2. Agente recomenda ação com baixa evidência → Metacognik marca baixa confiança e pede dados/aprovação/experimento pequeno.
3. Founder quer automatizar tudo → autonomia progressiva, mas preservar approval gates em decisões críticas.
4. Projeto muda de natureza (branding → e-commerce) → criar nova capability e recalcular dependências sem quebrar o projeto.
5. Output bonito sem função → `PMO_CKOS` reprova. Beleza sem impacto é ruído.

# 13. Métricas de sucesso

Tempo intenção→node; redução de perguntas manuais repetitivas; % de outputs com approval claro; nº de decisões registradas; taxa de hipóteses com evidência; redução de retrabalho; qualidade dos handoffs; tempo proposta→operação; clareza do próximo passo; nº de módulos ativados por necessidade real.

# 14. Critérios de aprovação

Aprovado quando: impede dashboards fixos prematuros; diferencia AI First real de chatbot com dashboard; define papel de Cognik e Metacognik; preserva aprovação humana; orienta nodes dinâmicos; protege whitelabel real; reduz dependência de prompts manuais do Founder.

# 15. Critérios de reprovação

Reprovar se: CKOS descrito como dashboard; agentes como personas de chat; módulos como páginas fixas; diagnóstico só no fim; aprovação humana ignorada; memória como histórico de chat; whitelabel reduzido a cor.

# 16. Related notes

- [[02_AI_FIRST_OBJECT_MODEL]]
- [[03_AGENT_OPERATING_MODEL]]
- [[04_AUTONOMY_AND_APPROVALS]]
- [[05_MEMORY_AND_CONTEXT_ARCHITECTURE]]
- [[10_SYSTEM_RUNTIME_ARCHITECTURE]]
- [[15_COMMAND_CENTER_ARCHITECTURE]]
- [[16_NODE_CANVAS_ARCHITECTURE]]
