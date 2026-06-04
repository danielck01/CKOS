# 17 — Teste local sem Notion e sem Higgsfield

> Nota de teste do vault. Este documento NÃO assume acesso ao DNA System real.
> A pasta atual é tratada como especificação/nota de estudo. O objetivo é testar
> o fluxo mínimo antes de integrar com qualquer sistema canônico.

---

## Decisão de teste

Vamos testar uma versão local e isolada do pipeline:

- sem Notion;
- sem Higgsfield;
- sem Routine do Claude Desktop;
- sem depender do DNA System real;
- com estado local em arquivos;
- com provider de render substituível;
- primeiro com mock/placeholder, depois com OpenRouter se houver chave.

O teste não valida produção final. Ele valida arquitetura, dados mínimos,
contratos entre etapas e pontos de falha.

---

## O que fica dentro do vault

O vault acompanha:

1. premissas do teste;
2. estrutura local proposta;
3. contratos de entrada e saída;
4. resultados das execuções;
5. problemas encontrados;
6. decisões tomadas;
7. próximos passos para integrar ao DNA System real.

Nada do teste deve sobrescrever as notas 00-16. Qualquer implementação deve
ficar em uma pasta sandbox separada.

---

## Estrutura sandbox sugerida

```text
Carroussel/
  _sandbox_local/
    README.md
    config/
      brand.json
      render-provider.json
      sources.json
    input/
      tema.txt
      noticia.json
    state/
      2026-06-04/
        news.json
        narrativa.json
        visual-plan.json
        render-requests.json
        slides/
        logs.txt
    output/
      2026-06-04/
        slide-01.png
        ...
        slide-09.png
```

---

## Teste 0 — dry run sem imagem real

Objetivo: provar que o pipeline editorial gera artefatos estruturados.

Entrada:

```text
Tema: como pequenos negócios podem usar IA no atendimento
Marca: teste local
Provider: mock
```

Saídas esperadas:

- `news.json` ou `manual-input.json`;
- `narrativa.json` com headline, caption e 9 slides;
- `visual-plan.json` com direção visual por slide;
- `render-requests.json` com 9 prompts prontos;
- 9 placeholders em PNG ou HTML exportável;
- `logs.txt` com tempo e status.

Critério de aprovação:

- nenhuma etapa depende de Notion;
- nenhuma etapa depende de Higgsfield;
- o estado do dia é reprodutível;
- cada slide tem texto e direção visual próprios;
- o pipeline aceita re-render de slide específico por número.

---

## Teste 1 — imagem via OpenRouter

Objetivo: substituir o mock por geração real de imagem.

Pré-requisito:

```text
OPENROUTER_API_KEY configurada localmente
```

Entrada:

```text
--tema="como pequenos negócios podem usar IA no atendimento"
```

Saídas esperadas:

- 9 imagens reais;
- URLs ou arquivos locais baixados;
- registro do modelo usado;
- custo aproximado quando disponível;
- falhas por slide sem derrubar a run inteira.

Critério de aprovação:

- o adapter do provider recebe um contrato padrão;
- o pipeline não conhece detalhes internos do OpenRouter;
- trocar provider exige mexer só em `render-provider.json`;
- se o provider falhar, a run salva erro claro e não cria marcador de completo.

---

## Teste 2 — vídeo

Objetivo: validar se vídeo entra como etapa separada, não misturado ao carrossel.

Entrada:

```text
slides já gerados + prompt de motion por slide
```

Saídas esperadas:

- `video-plan.json`;
- 1 vídeo curto geral OU vídeos por slide;
- logs de job assíncrono;
- status `pending`, `processing`, `completed` ou `failed`.

Critério de aprovação:

- vídeo não bloqueia a entrega do carrossel;
- imagem continua sendo o produto mínimo;
- vídeo é enhancement posterior.

---

## Contratos mínimos

### `brand.json`

```json
{
  "brand_name": "Teste Local",
  "brand_handle": "@teste",
  "brand_slug": "teste-local",
  "brand_color_primary": "#EC5E26",
  "brand_color_dark": "#1B1411",
  "brand_color_light": "#F1ECE3",
  "brand_subject": "IA aplicada a pequenos negócios",
  "brand_audience_term": "empreendedores",
  "brand_voice_anchor": "Folha de S.Paulo",
  "brand_has_logo": false
}
```

### `render-provider.json`

```json
{
  "provider": "mock",
  "mode": "image",
  "image_model": null,
  "video_model": null,
  "aspect_ratio": "3:4",
  "quality": "test"
}
```

### `render-requests.json`

```json
{
  "slides": [
    {
      "n": 1,
      "aspect_ratio": "3:4",
      "text": ["..."],
      "visual_brief": "...",
      "prompt": "..."
    }
  ]
}
```

---

## O que este teste NÃO decide

- Não decide a arquitetura final do DNA System.
- Não decide provider definitivo de imagem.
- Não decide se Notion será removido para sempre.
- Não decide UX final.
- Não migra dados reais.
- Não altera páginas canônicas.

---

## Próximo passo recomendado

Criar `_sandbox_local/` com:

1. configs mínimas;
2. um runner simples;
3. provider `mock`;
4. geração de `narrativa.json`, `visual-plan.json` e 9 placeholders.

Depois que o dry run passar, trocar `provider=mock` por `provider=openrouter`.
