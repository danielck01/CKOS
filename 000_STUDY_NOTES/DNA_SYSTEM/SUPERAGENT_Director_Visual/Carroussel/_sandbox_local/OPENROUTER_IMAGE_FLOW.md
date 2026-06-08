# OpenRouter image flow - Teste 1

## Como a imagem volta

O runner chama `POST https://openrouter.ai/api/v1/chat/completions` com:

- `model`: definido em `config/render-provider.json`
- `modalities`: `["image", "text"]` para modelos que retornam imagem e texto
- `image_config.aspect_ratio`: `3:4`
- `image_config.image_size`: `2K`
- `messages[0].content`: texto do prompt; opcionalmente imagens de referencia

A resposta esperada vem em:

```json
choices[0].message.images[0].image_url.url
```

Esse campo normalmente e um data URL base64:

```text
data:image/png;base64,...
```

O adapter decodifica esse base64, abre com Pillow, normaliza para `810x1080` com preenchimento na cor `brand_color_light`, aplica a copy localmente quando `local_text_overlay=true`, salva em `state/YYYY-MM-DD/slides/slide-0N.png`, e o runner copia para `output/YYYY-MM-DD/slide-0N.png`.

## Por que `local_text_overlay=true`

Modelos de imagem podem errar texto mesmo quando entendem bem o visual: duplicar palavras, omitir acentos, trocar pontuacao ou renderizar instrucoes tecnicas como `12px` e `55%`. Para carrossel, a copy e contrato. Por isso o modo recomendado e:

1. OpenRouter gera o visual/background sem texto.
2. O runner aplica a copy exata com Pillow.
3. O PNG final fica visualmente real, mas textual e auditavel.

## Como mandar imagem de referencia ou edicao

O contrato atual de `render-requests.json` ainda e text-to-image. Para image-to-image ou edicao, cada slide pode futuramente incluir:

```json
{
  "n": 1,
  "text": ["..."],
  "prompt": "...",
  "input_images": ["C:/path/local/reference.png"],
  "reference_images": ["https://example.com/style-reference.jpg"]
}
```

O adapter envia o texto primeiro e depois cada imagem como `image_url`, aceitando:

- URL publica `https://...`
- arquivo local, convertido para `data:image/...;base64,...`
- data URL ja pronta

Para edicao, o comportamento real depende do modelo. Recraft e Sourceful documentam parametros de image-to-image; modelos como Gemini/Grok podem aceitar referencias, mas cada pagina de modelo deve ser checada antes de tratar isso como contrato garantido.

## Upscale real

No OpenRouter, o recurso explicitamente documentado como enhancement/upscale no momento e `image_config.super_resolution_references`, limitado aos modelos Sourceful V2:

- `sourceful/riverflow-v2-fast`
- `sourceful/riverflow-v2-pro`

Isso nao e um endpoint generico de upscale. Ele so funciona quando ha imagem de entrada em `messages`; as referencias de super-resolucao ajudam a melhorar elementos de baixa qualidade, e a saida acompanha o tamanho da imagem de entrada. Para upscale puro de um PNG final, o caminho correto e tratar como etapa separada de pos-producao ou provider dedicado, nao como o mesmo render do carrossel.

## Modelos candidatos

- `google/gemini-3.1-flash-image-preview`: default atual do sandbox, bom para geracao rapida e `image_config`.
- `openai/gpt-5.4-image-2`: candidato para raciocinio visual + geracao, se disponivel na conta.
- `x-ai/grok-imagine-image-quality`: candidato forte quando texto dentro da imagem e realismo forem prioridade.
- `sourceful/riverflow-v2-pro`: candidato para edicao, fontes e enhancement/super-resolution.
- `recraft/recraft-v4.1-vector`: candidato para SVG, logo, icone e arte que precisa escalar limpo.

## Seguranca de chave

Nunca gravar `OPENROUTER_API_KEY` em `config/`, `README` ou logs. Definir apenas no ambiente:

```powershell
$env:OPENROUTER_API_KEY = "<sua-chave-openrouter>"
python runner.py --date 2026-06-04 --slide 1
```
