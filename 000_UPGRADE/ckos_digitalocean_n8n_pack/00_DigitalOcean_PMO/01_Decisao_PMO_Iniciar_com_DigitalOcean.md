---
title: "Decisão PMO — Iniciar com DigitalOcean para runway, VPS e validação de receita"
tipo: "nota_estrategica"
area: "Infraestrutura, Finanças, ROI, PMO"
status: "v1"
relacionado:
  - "../01_Financas_ROI/01_Runway_e_Queima_de_Credito.md"
  - "../01_Financas_ROI/02_ROI_Infra_por_Projeto.md"
  - "../01_Financas_ROI/03_Planner_de_Execucao_Custos.md"
  - "../02_N8N_Automations/00_Principios/01_N8N_como_Acelerador_nao_Core.md"
  - "../03_Policies/01_Policy_Custos_Budget_Gates.md"
tags:
  - digitalocean
  - vps
  - runway
  - infra
  - roi
  - ckos
---

# Decisão PMO — Iniciar com DigitalOcean para runway, VPS e validação de receita

## Tese

O CKOS deve iniciar com DigitalOcean porque a plataforma oferece um equilíbrio forte entre simplicidade operacional, performance para VPS, curva de aprendizado aceitável e crédito inicial útil para validar o produto antes de assumir custos recorrentes.

A decisão não é “usar DigitalOcean porque é grátis”.  
A decisão correta é:

> Usar o crédito inicial como runway estratégico para transformar infraestrutura em receita, prova de valor e aprendizado operacional.

## Observação sobre crédito inicial

O valor exato da promoção pode variar por período, país, elegibilidade, referral, conta nova ou programa específico. O planejamento deve considerar dois cenários:

- Cenário conservador: US$100 de crédito.
- Cenário otimista: US$200 de crédito por período limitado.

Para PMO, o cenário-base será US$100, porque obriga disciplina financeira.

## Regra de ouro

Cada dólar de crédito precisa ser tratado como se fosse dinheiro real do caixa da CKCompany.

O crédito não deve ser consumido com experimentação solta. Ele deve ser “superfaturado” internamente como valor estratégico no planner de execução.

## O que significa superfaturar o crédito no planner

Não significa cobrar indevidamente de cliente.  
Significa registrar o crédito gratuito como alavanca econômica com valor ampliado na gestão interna.

Exemplo:

- Crédito real: US$100.
- Valor estratégico interno: US$300 a US$500.
- Motivo: esses US$100 permitem validar arquitetura, reduzir risco, gerar proposta, criar demos, fechar cliente e evitar contratação prematura de infraestrutura.

## Como esse crédito precisa se pagar

O crédito precisa financiar uma cadeia simples:

```text
Crédito DigitalOcean
→ VPS inicial
→ n8n + workers + automações
→ demos funcionais
→ proposta com ROI
→ primeiro cliente ou upgrade
→ receita recorrente
→ infraestrutura paga pelo próprio projeto
```

## Escopo permitido no crédito inicial

Pode usar para:

- VPS Docker.
- n8n self-hosted.
- Redis leve.
- pequenos workers.
- staging do CKOS.
- testes de webhooks.
- monitoramento básico.
- rotinas de integração.
- automações para proposta, suporte, scraping e logs.

Não usar para:

- Kubernetes.
- GPU desnecessária.
- múltiplas VPS sem motivo.
- banco crítico sem backup.
- produção sem logs.
- tráfego pesado sem limite.
- serviços duplicados que Supabase/Vercel/Cloudflare já resolvem.

## Arquitetura inicial recomendada

```text
Cloudflare
DNS, SSL, CDN e WAF

Vercel ou Cloudflare Pages
Frontend

Supabase
Postgres, Auth, Storage, Vector, Realtime

DigitalOcean VPS
Docker, n8n, Redis, workers e automações

OpenRouter/OpenAI/Google
LLMs, multimodal, imagem, voz

Apify/Tavily
Scraping e pesquisa

Stripe/Mercado Pago
Pagamentos, planos, créditos e add-ons
```

## Indicadores obrigatórios

A VPS só é saudável se o PMO conseguir medir:

- custo mensal previsto;
- consumo de CPU;
- consumo de RAM;
- espaço em disco;
- uptime;
- automações ativas;
- execuções do n8n;
- erros por workflow;
- leads/propostas geradas;
- receita atribuída;
- economia operacional estimada;
- custo por projeto;
- custo por cliente;
- tempo economizado.

## Critério de migração futura

Migrar de DigitalOcean para estrutura mais robusta somente quando houver:

- receita recorrente previsível;
- gargalo real de performance;
- automações críticas estabilizadas;
- logs suficientes para prever carga;
- risco de segurança que demande arquitetura superior;
- necessidade de isolamento forte por cliente;
- exigência contratual de compliance.

## Decisão

Começar com DigitalOcean como camada VPS inicial é aprovado.

Condição:
O crédito inicial precisa ser monitorado como runway, conectado a finanças, ROI e planner de execução. Nada deve ser criado sem hipótese de retorno, uso técnico claro e critério de desligamento.
