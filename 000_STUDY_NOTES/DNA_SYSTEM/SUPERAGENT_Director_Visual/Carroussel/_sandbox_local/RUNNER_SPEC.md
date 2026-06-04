# RUNNER SPEC — Carroussel Sandbox Teste 0

> Handoff para engenharia de prompt / implementação do runner.
> Este documento é autocontido. Funciona em Claude, Codex ou Windsurf sem contexto de sessão anterior.

---

## Contexto em uma frase

Este diretório é um sandbox isolado de um pipeline de geração de carrossel de Instagram. O scaffolding (configs, contratos de dados, copy de exemplo) já existe e está commitado. **Falta o runner** — o script que consome esses contratos e gera os 9 placeholders de slide do Teste 0.

---

## O que já existe (não tocar)

```
_sandbox_local/
  README.md                          ← orientação geral do sandbox
  config/
    brand.json                       ← identidade da marca (cor, voz, slug)
    render-provider.json             ← provider=mock | mode=image
    sources.json                     ← fontes de notícia (não usadas no Teste 0)
  input/
    tema.txt                         ← "como pequenos negócios podem usar IA no atendimento"
    noticia.json                     ← entrada alternativa (não usada no Teste 0)
  state/2026-06-04/
    news.json                        ← pauta normalizada
    narrativa.json                   ← headline + caption + 18 campos / 9 slides
    visual-plan.json                 ← image_brief por slide (caminho A/B/C)
    render-requests.json             ← 9 prompts prontos + copy literal por slide
    slides/                          ← VAZIO — runner preenche aqui
  output/2026-06-04/                 ← VAZIO — runner copia entrega final aqui
```

---

## Tarefa do runner (Teste 0 — dry run sem imagem real)

### O que o runner faz

1. Lê `config/brand.json` e `config/render-provider.json`.
2. Lê `input/tema.txt` (ou aceita `--tema="..."` como argumento de linha de comando).
3. Lê `state/2026-06-04/render-requests.json` — os 9 prompts já montados.
4. Para cada slide `n` (1–9), com `provider=mock`:
   - Gera um **placeholder PNG 810×1080px** (proporção 3:4) com:
     - Fundo: `brand_color_light` (`#F1ECE3`)
     - Texto da copy do slide carimbado na imagem (pode ser simples — fonte do sistema, cor `brand_color_dark`)
     - Número do slide e função (ex.: `Slide 1 — Capa`) como cabeçalho interno do placeholder
   - Grava em `state/2026-06-04/slides/slide-0N.png`
5. Copia os 9 PNGs para `output/2026-06-04/slide-0N.png`.
6. Grava `state/2026-06-04/logs.txt` com:
   - Timestamp de início
   - Status de cada slide: `OK slide-01 (123ms)` ou `FAIL slide-01 (motivo)`
   - Tempo total
   - Sumário: `9/9 OK` ou `8/9 OK — 1 falha`

### CLI mínima

```bash
python runner.py                         # usa input/tema.txt, data=hoje
python runner.py --date 2026-06-04       # força uma data específica
python runner.py --slide 3               # re-render de slide específico (1-9)
python runner.py --tema="outro tema"     # override do tema
```

### Critério de aprovação (Teste 0)

- [ ] Roda `python runner.py` sem argumentos e termina sem exceção
- [ ] Gera 9 PNGs em `state/YYYY-MM-DD/slides/` com proporção 3:4
- [ ] Cada PNG carrega o texto de copy do slide (legível, sem truncar)
- [ ] Copia os 9 PNGs para `output/YYYY-MM-DD/`
- [ ] Grava `logs.txt` com status por slide e tempo total
- [ ] `--slide N` re-renderiza apenas o slide N sem afetar os outros
- [ ] Trocar `render-provider.json` de `provider=mock` para `provider=openrouter` NÃO quebra o runner — apenas ativa o branch de provider real (pode ser stub no Teste 0)
- [ ] Nenhuma dependência de Notion, Higgsfield, API key externa

---

## Contratos de dados que o runner consome

### `render-requests.json` — shape de cada slide

```json
{
  "slides": [
    {
      "n": 1,
      "aspect_ratio": "3:4",
      "text": ["Atendimento que não dorme", "O cliente não some pelo preço. Some pela demora."],
      "visual_brief": "string descritiva da direção visual",
      "prompt": "prompt completo para provider real (ignorado no mock)"
    }
  ]
}
```

O runner mock usa `n`, `text` e `aspect_ratio`. Ignora `prompt` e `visual_brief` (esses campos são para o provider real no Teste 1).

### `brand.json` — campos relevantes para o mock

```json
{
  "brand_color_primary": "#EC5E26",
  "brand_color_dark":    "#1B1411",
  "brand_color_light":   "#F1ECE3",
  "brand_has_logo":      false
}
```

---

## Arquitetura do runner

### Estrutura recomendada

```
_sandbox_local/
  runner.py              ← ponto de entrada
  providers/
    mock.py              ← gera placeholder PNG
    openrouter.py        ← stub para Teste 1 (pode ser NotImplementedError)
  utils/
    config.py            ← carrega brand.json + render-provider.json
    state.py             ← resolve paths de state/output por data
```

### Seleção de provider

O runner lê `config/render-provider.json`:

```python
if provider_cfg["provider"] == "mock":
    from providers.mock import render_slide
elif provider_cfg["provider"] == "openrouter":
    from providers.openrouter import render_slide
else:
    raise ValueError(f"Provider desconhecido: {provider_cfg['provider']}")
```

Trocar o provider exige mexer **só** em `render-provider.json`. O runner não tem provider hardcoded.

### Provider mock — o que gera

Placeholder PNG 810×1080 (3:4) com:

```
┌──────────────────────────────┐
│  [cabeçalho interno, ~14px]  │  ← "Slide 1 — Capa | MOCK | 2026-06-04"
│                              │
│                              │
│  [copy do slide, ~18px,      │  ← texto[] do render-requests, word-wrap
│   cor brand_color_dark,      │
│   centralizado ou alinhado   │
│   à esquerda com margem]     │
│                              │
│                              │
│  [rodapé, ~12px, 55% opac]  │  ← "2026.06.04 · @teste"
└──────────────────────────────┘
   fundo: brand_color_light
```

Usar `Pillow` (PIL) para geração. Sem dependência de Playwright, ffmpeg ou qualquer API.

---

## Dependências Python permitidas

```
pillow       # geração dos placeholders PNG
```

Sem mais. O runner de Teste 0 não precisa de requests, httpx, openai SDK, nem nada externo.

---

## O que o runner NÃO deve fazer

- ❌ Chamar qualquer API (Notion, Higgsfield, OpenRouter, OpenAI)
- ❌ Baixar imagens da internet
- ❌ Modificar os arquivos em `config/`, `input/` ou qualquer `.json` de estado
- ❌ Apagar ou sobrescrever `narrativa.json`, `visual-plan.json`, `render-requests.json`
- ❌ Hardcodar o nome da marca, cor ou tema — sempre lê de `brand.json`
- ❌ Gerar slide com proporção diferente de 3:4

---

## Gate de revisão (obrigatório antes de fechar)

Quando o runner estiver pronto e os critérios acima estiverem passando, **não feche a tarefa sozinho**. Sinalize para revisão PMO:

1. Liste quais critérios estão OK e quais ainda falham.
2. Cole o output de `logs.txt` gerado por uma run completa.
3. Aguarde aprovação antes de marcar como concluído.

O revisor vai confirmar:
- Os 9 PNGs têm proporção 3:4 e copy legível.
- `--slide N` funciona isolado.
- O provider pode ser trocado sem alterar `runner.py`.

---

## Próximo passo após Teste 0 aprovado (fora do escopo deste handoff)

- **Teste 1:** trocar `render-provider.json` para `provider=openrouter`, implementar `providers/openrouter.py` com a key `OPENROUTER_API_KEY`, gerar 9 imagens reais.
- **Teste 2:** vídeo como etapa separada (não bloqueia carrossel).

Não implementar Teste 1 ou 2 até o Teste 0 estar aprovado pelo revisor.
