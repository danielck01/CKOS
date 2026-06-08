---
title: Audience DNA CKOS
folder: DNA
type: audience_dna
status: draft
version: 1.0.0
owner: PMO_CKOS
agents:
  - Cognik
  - Metacognik
  - PMO_CKOS
---

# Audience DNA CKOS

## Persona Primária: The Technical Founder

### Perfil Demográfico
- **Idade**: 28-42 anos
- **Cargo**: Founder, CTO, VP of Engineering, Head of Product
- **Empresa**: Startup B2B SaaS (Seed a Series B), 5-50 funcionários
- **Setor**: Tecnologia, Fintech, Healthtech, Edtech
- **Localização**: Brasil (São Paulo, Rio, Belo Horizonte), EUA (SF, NY, Austin)
- **Formação**: Engenharia, Ciência da Computação, Design ou MBA técnico

### Psicografia
- **Mentalidade**: Early adopter de IA, mas cético com hype sem substância
- **Dor principal**: Sobrecarga cognitiva de coordenar múltiplos agentes, ferramentas e decisões
- **Motivação**: Escalar operação sem perder controle estratégico
- **Comportamento**: Testa ferramentas novas, mas abandona se não entregam valor real em 2 semanas
- **Medo**: Perder controle de decisões críticas, outputs inconsistentes, dependência de black-box

### Jobs-to-be-Done (JTBD)

**Job 1: Coordenar múltiplos agentes de IA sem sobrecarga manual**
- Contexto: Usa Claude, Codex, Manus, n8n simultaneamente
- Progresso: Atualmente escreve prompts manuais repetitivos
- Resultado esperado: Sistema interpreta intenção, distribui tarefas, recebe outputs coerentes

**Job 2: Documentar decisões estratégicas automaticamente**
- Contexto: Decisões ficam em conversas, Slack, Notion espalhado
- Progresso: Perde tempo documentando manualmente ou não documenta
- Resultado esperado: Cada decisão tem evidência, risco, dependência e aprovação registrados

**Job 3: Manter coerência entre outputs de diferentes agentes**
- Contexto: Múltiplos agentes produzem conteúdo inconsistente
- Progresso: Edita manualmente para alinhar com direção estratégica
- Resultado esperado: Single source of truth (DNA) que todos agentes leem antes de produzir

**Job 4: Aprovar decisões críticas sem ser bottleneck**
- Contexto: Precisa aprovar tudo, mas isso escala mal
- Progresso: Aprovações manuais em cada etapa
- Resultado esperado: Approval gates automáticos em decisões de alto impacto, autonomia progressiva

**Job 5: Aprender com erros e acertos continuamente**
- Contexto: Erros se repetem, acertos não são replicados
- Progresso: Aprendizado fica na cabeça, não no sistema
- Resultado esperado: Sistema registra hipóteses, evidências, resultados e atualiza memória

### Barreiras de Adoção
- **Ceticismo com "AI-powered"**: Já viu muitos tools com IA anexada que não funcionam
- **Medo de perder controle**: Não quer delegar decisões críticas sem visibilidade
- **Complexidade de setup**: Não quer gastar semanas configurando sistema
- **Integração com stack existente**: Já usa Notion, Linear, GitHub, n8n - precisa integrar

### Gatilhos de Compra
- **Sobrecarga cognitiva**: "Estou gastando 4h/dia só coordenando agentes e escrevendo prompts"
- **Inconsistência de outputs**: "Meus agentes produzem coisas que não parecem da mesma marca"
- **Decisões não documentadas**: "Não consigo lembrar por que tomamos decisão X há 3 meses"
- **Escalabilidade**: "Preciso escalar operação sem contratar 10 pessoas"

---

## Persona Secundária: The Technical Lead

### Perfil Demográfico
- **Idade**: 25-38 anos
- **Cargo**: Engineering Manager, Tech Lead, Senior Developer
- **Empresa**: Startup B2B SaaS (Seed a Series B), 10-100 funcionários
- **Setor**: Tecnologia, Fintech, Healthtech
- **Localização**: Brasil, EUA, Europa
- **Formação**: Engenharia, Ciência da Computação

### Psicografia
- **Mentalidade**: Pragmático, focado em execução, cético com abstrações sem código
- **Dor principal**: Precisa implementar mas não quer perder tempo com configuração complexa
- **Motivação**: Entregar features rápido com qualidade
- **Comportamento**: Testa ferramentas se prometem reduzir tempo de desenvolvimento
- **Medo**: Ferramenta que promete mas não entrega, aumenta complexidade

### Jobs-to-be-Done (JTBD)

**Job 1: Implementar features com IA sem perder tempo em prompts**
- Contexto: Usa Claude/Codex para gerar código
- Progresso: Escreve prompts longos, revisa muito
- Resultado esperado: Sistema prepara brief, distribui para agentes, recebe código pronto

**Job 2: Manter qualidade de código com múltiplos agentes**
- Contexto: Diferentes agentes geram estilos inconsistentes
- Progresso: Refatora manualmente para padronizar
- Resultado esperado: DNA define padrões, agentes seguem automaticamente

**Job 3: Rastrear decisões técnicas**
- Contexto: Por que escolhemos X em vez de Y?
- Progresso: Procura em Git history, Slack, Notion
- Resultado esperado: Cada decisão técnica tem evidência e contexto registrados

### Barreiras de Adoção
- **Foco em código**: "Preciso ver código funcionando, não documentação bonita"
- **Integração com CI/CD**: Precisa integrar com GitHub Actions, testes, deploy
- **Curva de aprendizado**: Não quer ler documentação extensa

### Gatilhos de Compra
- **Tempo de desenvolvimento**: "Estou gastando 50% do tempo só revisando código de IA"
- **Inconsistência**: "Cada agente gera código em estilo diferente"
- **Rastreabilidade**: "Não consigo explicar por que escolhemos essa arquitetura"

---

## Anti-Persona: The Non-Technical Manager

### Perfil
- **Cargo**: Marketing Manager, Sales Manager, HR Manager
- **Empresa**: Empresa tradicional, não-tech
- **Mentalidade**: Quer "AI solution" sem entender o que precisa
- **Comportamento**: Busca "ferramenta mágica" que resolve tudo sem esforço

### Por que não é target
- **CKOS é técnico**: Requer entendimento de agentes, workflows, aprovações
- **Não tem problema que CKOS resolve**: Não coordena múltiplos agentes técnicos
- **Expectativa irreal**: Quer "bot que faz tudo" sem governança
- **Não tem autoridade para aprovar**: Não pode aprovar decisões técnicas críticas

### Sinais de anti-persona
- Pergunta "Quanto custa o bot que faz posts?"
- Não entende diferença entre chatbot e sistema operacional
- Quer "AI solution" sem definir problema específico
- Não tem stack técnico (GitHub, Notion, n8n)

---

## Anti-Persona: The Enterprise CTO

### Perfil
- **Cargo**: CTO de empresa grande (500+ funcionários)
- **Empresa**: Enterprise, corporação
- **Mentalidade**: Precisa de compliance, segurança, aprovações em múltiplos níveis
- **Comportamento**: Processo de compra 6-12 meses, comitês, RFPs

### Por que não é target (ainda)
- **CKOS é early-stage**: Focado em startups Seed/Series B
- **Requisitos enterprise**: Compliance, SOC2, SSO, SLAs não implementados
- **Complexidade**: Precisa de customização profunda, consultoria
- **Processo de compra**: CKOS não tem estrutura para vendas enterprise

### Quando pode virar target
- Quando CKOS tiver versão Enterprise com:
  - SSO (Okta, Azure AD)
  - SOC2 compliance
  - SLAs garantidos
  - Suporte dedicado
  - Consultoria de implementação

---

## Segmentação por Maturidade de IA

### Segmento 1: AI Explorer (Early Adopter)
- **Características**: Já usa Claude, Codex, n8n, experimenta com IA
- **Dor**: Sobrecarga de coordenar múltiplos tools
- **Pronto para CKOS**: Sim - entende valor de coordenação
- **Mensagem**: "Você já usa IA. CKOS coordena tudo."

### Segmento 2: AI Skeptic (Late Adopter)
- **Características**: Cético com IA, prefere ferramentas tradicionais
- **Dor**: Vê concorrentes usando IA com sucesso
- **Pronto para CKOS**: Não - precisa de prova de valor
- **Mensagem**: "Case studies, ROI, trial gratuito"

### Segmento 3: AI Native (Already Operating)
- **Características**: Já construiu sistema interno de coordenação
- **Dor**: Sistema caseiro não escala, difícil de manter
- **Pronto para CKOS**: Sim - busca solução profissional
- **Mensagem**: "Seu sistema caseiro → CKOS whitelabel"

---

## Canais de Alcance

### Canais Primários
- **X (Twitter)**: Comunidade técnica brasileira e global
- **LinkedIn**: CTOs, VPs Engineering, Founders
- **GitHub**: Issues, discussions, open source
- **Communities**: Indie Hackers, Hacker News, r/startups

### Canais Secundários
- **Newsletters**: Tech newsletters brasileiras (Tecnino, etc.)
- **Podcasts**: Podcasts de tecnologia brasileiros
- **Conferences**: RubyConf, Python Brasil, QCon
- **Content Marketing**: Blog posts técnicos, case studies

---

## Métricas de Audience

### Métricas de Aquisição
- CAC por segmento (Explorer vs Skeptic vs Native)
- Taxa de conversão trial → pago
- Tempo até primeiro valor (time-to-value)
- Churn nos primeiros 30 dias

### Métricas de Engajamento
- DAU/MAU por persona
- Número de workflows criados por usuário
- Número de decisões registradas por usuário
- Taxa de uso de approval gates

### Métricas de Qualidade
- NPS por persona
- Feature requests por segmento
- Suporte tickets por tipo de usuário
- Tempo de resposta a support

---

## Próximo Passo

Definir Voice & Tone (vocabulário, registros por canal, construções, anti-AI-slop).
