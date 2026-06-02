---
title: "Contexto Mestre para Codex"
tipo: "instrucoes"
area: "Codex, Engenharia"
---

# Contexto Mestre para Codex

Você está trabalhando no CKOS, um sistema operacional AI-first da CKCompany para transformar intenção em projeto, briefing, proposta, execução, aprovação, ROI e aprendizado contínuo.

## Regra central

Não construa um app genérico.  
Construa uma arquitetura operacional que conecta:

```text
Projeto → Knowledge → Briefing → Agentes → Runs → Aprovações → Outputs → ROI → Feedback Loop
```

## Infra fase 1

A fase 1 deve priorizar:

- DigitalOcean para VPS e Docker;
- n8n como acelerador;
- Supabase para banco/auth/storage/vector;
- Cloudflare para DNS/CDN/segurança;
- Vercel/Cloudflare Pages para frontend;
- OpenRouter/OpenAI/Google para IA;
- Apify/Tavily para inteligência externa.

## Papel do n8n

n8n não é o core do CKOS.  
n8n é uma ponte rápida para validar automações e conectores.

## Ao gerar código ou automações

Sempre incluir:

- objetivo;
- inputs;
- outputs;
- variáveis de ambiente;
- credenciais necessárias;
- logs;
- tratamento de erro;
- idempotência;
- política de custo;
- quando migrar para código próprio.
