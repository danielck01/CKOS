# _sandbox_local — Teste 0 (scaffolding)

> Sandbox isolado do pipeline de carrossel, conforme [`../17-Teste-Local-Sem-Notion-Higgsfield.md`](../17-Teste-Local-Sem-Notion-Higgsfield.md).
> **Não toca** as notas canônicas `00`–`17`. É experimento descartável de arquitetura e de contratos de I/O.

**Estado atual: `scaffolding`.** Configs, input e os contratos de exemplo estão prontos e preenchidos com um caso real. **Não há runner** — por decisão, código executável fica para o F1 (Codex, com git). Este diretório é o *alvo* que o runner vai consumir e preencher.

---

## O que isto é (e o que não é)

- **É:** a estrutura de pastas do doc 17 + os contratos de dados que o pipeline troca entre etapas, preenchidos com um exemplo real — tema *"como pequenos negócios podem usar IA no atendimento"*, marca de teste (`config/brand.json`).
- **Não é:** um executável. Não há runner Python/Node. Os PNGs em `state/2026-06-04/slides/` e `output/2026-06-04/` **ainda não existem** — são saída de runner.
- **Não decide:** arquitetura final do DNA System, provider definitivo de imagem, nem remoção do Notion (doc 17, seção *"O que este teste NÃO decide"*).

---

## Fluxo do pipeline e onde cada contrato entra

```
input/tema.txt
   │  (Scout / pesquisa — modo tema, doc 14)
   ▼
state/2026-06-04/news.json          pauta normalizada (shape do News Feed, doc 12)
   │  (Scriptwriter — arquitetura narrativa, doc 07)
   ▼
state/2026-06-04/narrativa.json     headline + caption + 18 campos / 9 slides
   │  (Art Director — direção visual, doc 09)
   ▼
state/2026-06-04/visual-plan.json   image_brief por slide (caminho A/B/C, hero, etc.)
   │  (Producer — monta prompts)
   ▼
state/2026-06-04/render-requests.json   9 prompts prontos + copy literal por slide
   │  (Render provider — config/render-provider.json)
   ▼
state/2026-06-04/slides/slide-0N.png    ← runner gera (mock = placeholder)
output/2026-06-04/                       ← entrega final do dia
```

---

## Contratos (arquivos de exemplo já preenchidos)

| Arquivo | Etapa | Schema vem de |
|---|---|---|
| `config/brand.json` | identidade da marca | doc 17 (verbatim) |
| `config/render-provider.json` | provider de render (`mock`) | doc 17 (verbatim) |
| `config/sources.json` | fontes de notícia (não exercido no Teste 0 por tema) | doc 04 (adaptado; doc 04 só dá a tabela do Notion) |
| `input/tema.txt` | entrada do Teste 0 (modo tema) | doc 14 / doc 17 |
| `input/noticia.json` | entrada alternativa (conteúdo colado) — **não usada junto com `tema.txt`** | doc 14 |
| `state/2026-06-04/news.json` | pauta normalizada | doc 12 (shape do News Feed) |
| `state/2026-06-04/narrativa.json` | copy: headline, caption, 18 campos/9 slides | doc 07 |
| `state/2026-06-04/visual-plan.json` | `image_brief` por slide | doc 09 |
| `state/2026-06-04/render-requests.json` | 9 prompts + copy literal por slide | doc 17 (shape) + doc 09 (template do prompt) |

> Campos `_nota` / `_modo` dentro dos JSON são comentários para esta sessão de scaffolding — um runner real ignora chaves com prefixo `_`.

---

## Os 3 testes (doc 17)

- **Teste 0 (este):** `provider=mock`, dry run, **sem API key, sem Playwright, sem ffmpeg**. O runner consome `render-requests.json` e grava 9 placeholders (PNG ou HTML) + `logs.txt`.
- **Teste 1:** `provider=openrouter` — exige `OPENROUTER_API_KEY` no ambiente. Gera 9 imagens reais. Trocar provider deve mexer **só** em `config/render-provider.json`.
- **Teste 2:** vídeo, etapa separada (não bloqueia o carrossel). Fora do escopo deste scaffolding.

---

## Critério de aprovação do Teste 0 (doc 17) — status

- [x] nenhuma etapa depende de Notion — estado todo em arquivos
- [x] nenhuma etapa depende de Higgsfield — `provider=mock`
- [x] o estado do dia é reprodutível — `state/2026-06-04/`
- [x] cada slide tem texto e direção visual próprios — `narrativa.json` + `visual-plan.json`
- [ ] o pipeline aceita re-render de slide específico por número — **depende do runner**

---

## O que falta para rodar (escopo do runner — F1/Codex)

Este scaffolding entrega os dados; falta o executável. Um runner mínimo de Teste 0 precisa:

1. ler `config/*` e `input/tema.txt`;
2. (opcional) regenerar `news.json` → `narrativa.json` → `visual-plan.json` → `render-requests.json`, **ou** apenas consumir os exemplos já presentes;
3. provider `mock`: para cada item de `render-requests.json`, gravar um placeholder em `state/2026-06-04/slides/slide-0N.png` (ou `.html` exportável) carimbando o texto do slide;
4. escrever `state/2026-06-04/logs.txt` com tempo e status por slide;
5. aceitar `--slide N` para re-render de um slide só;
6. trocar `provider=mock` → `openrouter` mexendo apenas em `config/render-provider.json` (Teste 1).

---

## Árvore

```
_sandbox_local/
  README.md                  ← este arquivo
  config/
    brand.json
    render-provider.json
    sources.json
  input/
    tema.txt
    noticia.json
  state/2026-06-04/
    news.json
    narrativa.json
    visual-plan.json
    render-requests.json
    slides/                  (vazio — runner preenche)
    logs.txt                 (não existe — runner gera)
  output/2026-06-04/         (vazio — runner preenche)
```
