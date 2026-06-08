---
title: Image Generation Engine CKOS
folder: DNA
type: image_generation_engine
status: draft
version: 1.0.0
owner: PMO_CKOS
agents:
  - Cognik
  - Metacognik
  - PMO_CKOS
---

# Image Generation Engine CKOS

## Engine Oficial

**Higgsfield CLI + Nano Banana 2 (`nano_banana_2`)**

Esta é a engine oficial de geração de imagem para o CKOS. Outras ferramentas podem aparecer como referência conceitual ou comparação histórica, mas não como fluxo operacional do treinamento.

## Stack de Geração por Tipo de Peça

### Hero Shot Fotorealista
- **Engine**: Higgsfield CLI + Nano Banana 2
- **Por quê**: Fotorrealismo + atmosfera com referências visuais
- **Resolução**: 2K (1088×1360 para 4:5)
- **Iterações**: 4 variações low quality → 1 escolha → 2 variações medium → 1 final
- **Custo estimado**: $0.80-1.50 por shot final

### Capa de Carrossel com Texto
- **Engine**: Higgsfield CLI + Nano Banana 2
- **Por quê**: Composição + texto curto revisível
- **Resolução**: 2K (1088×1360 para 4:5)
- **Iterações**: 4 variações low → 1 escolha → 2 variações medium → 1 final
- **Custo estimado**: $0.80-1.50 por capa

### Slide com Texto + Foto
- **Engine**: Higgsfield CLI + Nano Banana 2
- **Por quê**: Layout visual com referências da marca
- **Resolução**: 2K (1088×1360 para 4:5)
- **Iterações**: 2 variações medium → 1 final
- **Custo estimado**: $0.30-0.50 por slide

### Pessoa em Contexto Realista
- **Engine**: Higgsfield CLI + Nano Banana 2
- **Por quê**: Consistência via image references
- **Resolução**: 2K (1088×1360 para 4:5)
- **Iterações**: 4 variações low → 1 escolha → 2 variações medium → 1 final
- **Custo estimado**: $0.80-1.50 por shot

### Personagem Consistente em Série
- **Engine**: Higgsfield CLI + Nano Banana 2
- **Por quê**: Anchor sheet + referências recorrentes
- **Resolução**: 2K (1088×1360 para 4:5)
- **Iterações**: 1 master shot → variações com master como referência
- **Custo estimado**: $1.00-2.00 por série de 9

### Ilustração / Vetor Visual
- **Engine**: Higgsfield CLI + Nano Banana 2
- **Por quê**: Direção de arte visual; vetor final pode ser redesenhado se necessário
- **Resolução**: 2K (1088×1360 para 4:5)
- **Iterações**: 4 variações low → 1 escolha → 2 variações medium → 1 final
- **Custo estimado**: $0.80-1.50 por ilustração

### Ícone / Símbolo
- **Engine**: Higgsfield CLI + Nano Banana 2
- **Por quê**: Conceito visual; produção vetorial final se necessário
- **Resolução**: 1K (512×512 para 1:1)
- **Iterações**: 4 variações low → 1 escolha → 1 final
- **Custo estimado**: $0.20-0.30 por ícone

### Poster com Tipografia Forte
- **Engine**: Higgsfield CLI + Nano Banana 2
- **Por quê**: Texto curto + QA obrigatório
- **Resolução**: 2K (1088×1360 para 4:5)
- **Iterações**: 4 variações low → 1 escolha → 2 variações medium → 1 final
- **Custo estimado**: $0.80-1.50 por poster

### Product Shot Premium
- **Engine**: Higgsfield CLI + Nano Banana 2
- **Por quê**: Visual Intent + referências + polish
- **Resolução**: 2K (1088×1360 para 4:5)
- **Iterações**: 4 variações low → 1 escolha → 2 variações medium → 1 final
- **Custo estimado**: $0.80-1.50 por shot

## Quality Tiers

### Low (Iteração Rápida)
- **Resolução**: 1K
- **Uso**: Exploração de composição, validar layout
- **Custo**: $0.005-0.02 por imagem
- **Quando**: Primeiras 4 variações para escolher direção

### Medium (Padrão Premium)
- **Resolução**: 2K
- **Uso**: Aprovação interna, padrão premium
- **Custo**: $0.05-0.10 por imagem
- **Quando**: Iterações após escolha de direção

### High (Final Premium)
- **Resolução**: 4K (quando pedido)
- **Uso**: Versão final quando detalhe extremo for necessário
- **Custo**: $0.15-0.30 por imagem
- **Quando**: Hero campaign, capa importante

### Premium (Upscale + Polish)
- **Resolução**: 4K + upscale + iteração múltipla + polish
- **Uso**: Hero campaign, capa importante
- **Custo**: $0.50-1.00 por imagem
- **Quando**: Peças de alta visibilidade

## Schema do Image Brief

Toda peça produzida via IA gera primeiro um JSON estruturado:

```json
{
  "engine": "higgsfield_cli/nano_banana_2",
  "purpose": "tensão narrativa de urgência geracional",
  "subject": "um celular antigo Nokia 3310 caído numa mesa de café junto a um cappuccino derramado",
  "composition": "overhead 90°, objetos no terço inferior, espaço negativo no superior",
  "lighting": "luz natural lateral, sombras duras, ~10h da manhã",
  "color_treatment": "predominante cinza-quente + 1 ponto laranja-terracota no líquido derramado",
  "style": "fotografia editorial 35mm, grão fino, profundidade média",
  "mood": "abandono, ruptura silenciosa, pausa",
  "metaphor": "geração que desliga o telefone moderno e tropeça no analógico",
  "avoid": "sem mãos no quadro, sem rosto, sem texto sobre a imagem",
  "reference_images": ["url1", "url2"],
  "dimensions": {"width": 1088, "height": 1360},
  "resolution": "2k"
}
```

## Templates Canônicos de Prompt

### Template 1: Hero / Capa (Full-Bleed, Dramática)

```
A {dimensions.width}x{dimensions.height} {format_descriptor} hero/cover image.

{VISUAL_BRIEF_DECODED}

This is a HERO image. It MUST be visually arresting — magazine cover quality, the kind of image that stops the scroll.

═══ EMBEDDED IMAGE (full-bleed background) ═══
{image_brief.subject}

Composition: {image_brief.composition} — strong focal point, rule of thirds, leading lines if applicable, foreground/background separated by focus

Lighting: {image_brief.lighting} — dramatic (chiaroscuro, rim light, golden hour, or harsh side light). NEVER flat catalog lighting.

Color: {image_brief.color_treatment} — selective saturation: muted backdrop, saturated focal point ideally in {brand_color_primary}

Style: {image_brief.style} — never generic AI gloss

Mood: {image_brief.mood} — narrative tension. Something is happening or about to.

Metaphor: {image_brief.metaphor}

═══ COMPOSITION ═══
- Full-bleed image background as described above
- Heavy dark gradient overlay at the bottom 55-60% to ensure 4.5:1 contrast against headline
- Thin accent bar (6px) at the very top in {brand_color_primary}
- Headline anchored in lower 35% of canvas, left-aligned, generous left margin (~80px)
- Handle "{brand_handle}" small, above the headline block

═══ TEXT CONTENT ═══
- Brand bar (very top, small, low opacity): "POR {brand_name}  |  {brand_handle}  |  {year}"
- Handle: "{brand_handle}"
- Headline (largest element, bold condensed uppercase, tight kerning): "{HEADLINE_DA_CAPA}"
- Highlight in {brand_color_primary}: {LISTA_DE_PALAVRAS_CHAVE}

═══ TYPOGRAPHY ═══
- Headline: bold condensed sans-serif, weight 900, 88-108px, uppercase, letter-spacing -3px, line-height 0.95
- Handle: clean sans-serif, weight 600, 18px

═══ DETAIL SIGNATURE ═══
{DETAIL_SIGNATURE_DESCRITO_NO_VISUAL_BRIEF}
(footer consistency element repeated across all peças of this batch)

═══ ABSOLUTE NO-GO ═══
{image_brief.avoid}
+ universal no-go from brand:
Do NOT include: emojis, decorative icons, stock photo aesthetic, 3D glossy effects, lens flares (unless cinematic intent), generic gradients, AI-rendered faces with uncanny features, corporate handshakes, smiling group photos to camera, hands typing generically on laptop, lightbulb-as-idea cliché, gears-as-strategy cliché.

═══ MOOD TARGET ═══
This image should look like it was art-directed by a design magazine ({brand_aesthetic_anchor}) — not generated by AI. Confidence. Sharpness. Specificity. Tension.
```

### Template 2: Slide Interno / Post Body

```
A {dimensions.width}x{dimensions.height} {format_descriptor} content image.

{VISUAL_BRIEF_DECODED}

This is slide [N] of [TOTAL] — the {section_function}. NOT a cover.

Match the visual STYLE (palette, typography, composition, footer detail signature) of the cover and brand reference images, but show DIFFERENT content. Use reference for visual consistency, not for copying content.

═══ EMBEDDED IMAGE ═══
[bloco image_brief específico — ver schema acima]

═══ COMPOSITION ═══
- Background: {dark|light|gradient}
- Tag at top: "{tag_text}" in mono, weight 700, 13px, uppercase, letter-spacing 3px, color {tag_color}
- Body text in {body_position} third of canvas, left-aligned
- Brand bar at very top: handle + 0X/0Y counter

═══ TEXT CONTENT (KEEP MINIMAL — 2 short blocks max) ═══
texto A: "{text_block_a}"
texto B: "{text_block_b}"

═══ ABSOLUTE NO-GO ═══
{universal_no_go} + slide-specific {avoid_list}
```

### Template 3: Branding Placement (Logo em Contexto)

```
A photograph showing the {brand_name} logo / product naturally integrated into an unexpected real-world context.

═══ THE PLACEMENT ═══
Context: {unexpected_context}
   (Examples: 
    - "logo painted on the side of an old delivery truck stopped at a traffic light in São Paulo's Vila Madalena, 1998 morning light"
    - "logo as a tattoo on a man's forearm, holding an espresso cup, café table in Lisbon, golden hour"
    - "logo printed on a vintage book cover, lying on a wooden desk with a pair of tortoise-shell glasses on top")

═══ THE BRAND ELEMENT ═══
Logo / element: {brand_logo_description}
Position in frame: {composition_placement}
Imperfections: include realistic wear, fade, lighting interaction with surface texture. The logo should feel like it has BEEN there for a while — not photoshopped onto the scene yesterday.

═══ COMPOSITION ═══
- Lighting: {chosen_setup_from_7}
- Camera angle: {angle}
- Color treatment: {color_treatment}
- Grain: subtle film grain, {iso_equivalent}

═══ ABSOLUTE NO-GO ═══
- Pristine logo placement (looks fake)
- Logo bigger than would be realistic
- Logo as the SUBJECT of the image (subject is the context; logo is a presence)
- Generic "branded mockup" template aesthetic
```

## Pipeline de 3 Etapas

### Etapa A: Visual Intent (Claude extrai direção criativa do briefing)

```
Você é um diretor de arte de marca {brand_aesthetic_anchor}. Recebeu este briefing do cliente:

[BRIEFING DO CLIENTE]

Sua tarefa é extrair a direção visual em 6 dimensões:

1. SUBJECT (o produto + contexto): descreva visualmente o que aparecerá no quadro.
2. LIGHTING: qual dos 7 setups (Golden Hour, Low Key, Spotlight, Chiaroscuro, Cutter Lights, Hard Flash, Silhouette) melhor serve o mood?
3. COMPOSITION: ângulo, plano, posição do produto no quadro.
4. COLOR_TREATMENT: paleta, saturação, onde aparece a cor primária.
5. STYLE: editorial 35mm? Still life clássico? Render 3D matte? Risograph?
6. MOOD + METAFORA: sentimento + metáfora visual

Devolva em JSON do schema image_brief.
```

### Etapa B: Geração + Iteração

R2 chama Higgsfield CLI com image_brief + 3-5 referências:

```bash
UUID_1=$(higgsfield upload create "ref-1.png" | grep -oiE '[0-9a-f-]{36}' | head -1)
UUID_2=$(higgsfield upload create "ref-2.png" | grep -oiE '[0-9a-f-]{36}' | head -1)
JOB_ID=$(higgsfield generate create nano_banana_2 \
  --prompt "[image_brief estruturado]" \
  --image "$UUID_1" \
  --image "$UUID_2" \
  --aspect_ratio "4:5" \
  --json | grep -oiE '[0-9a-f-]{36}' | head -1)
higgsfield generate wait "$JOB_ID" --wait-timeout 30m --json
```

Gera a variação necessária. Se não servir, ajusta image_brief e roda de novo registrando tentativa, modelo, UUIDs e job_id.

### Etapa C: Polish Final (Upscale + Micro-Refinamentos)

```bash
# Refinamento via nova geração referenciada
REFINED_JOB=$(higgsfield generate create nano_banana_2 \
  --prompt "[descricao do refinamento localizado]" \
  --image "$CHOSEN_UUID" \
  --aspect_ratio "4:5" \
  --json | grep -oiE '[0-9a-f-]{36}' | head -1)
higgsfield generate wait "$REFINED_JOB" --wait-timeout 30m --json
```

Output final: PNG 2176×2720, qualidade entrega final, custo total ~$0.80-1.50 por shot final.

## Branding com IA

### Logo Placement
- **Nunca deixar IA "desenhar" logo** — sempre distorce
- **Logo via Pillow** (composição após geração)
- **Se logo precisa aparecer na imagem**: usar image-to-image com logo real como referência
- **Posicionamento natural**: logo como presença, não como subject principal

### Consistência de Personagem
- **Master shot + image-to-image**: gera 1 master excelente, usa como reference em todas as próximas
- **Higgsfield CLI + Nano Banana 2**: usar 1-3 imagens-âncora como `--image` em todas as próximas gerações
- **Anchor sheet**: criar uma folha mestre de personagem/produto e reutilizar como referência
- **Controle de variação**: mudar uma variável por iteração para não perder identidade

### Texto na Imagem
- **Render texto separado em design tool** (Figma, depois compor)
- **Manter texto curto** quando precisar vir no render
- **Inpaint/re-render** o texto correto em segundo passe
- **QA obrigatório**: conferir cada caractere, mesmo com Nano Banana 2

## Anti-Padrões de IA Generativa

### Anti-Padrões Técnicos
- ❌ Mãos com 6 dedos ou anatomia anormal
- ❌ Olhos vidrados, simetria estranha, expressão "morta"
- ❌ Texto incoerente em placas/cartazes/livros
- ❌ Sombras inconsistentes (luz em direção contraditória)
- ❌ Reflexos físicamente impossíveis
- ❌ Pele plástica supersuavizada
- ❌ Background com objetos derretendo
- ❌ Logo "desenhado" pela IA (sempre distorce)
- ❌ Marca d'água do gerador na peça final

### Anti-Padrões Estéticos Saturados
- ❌ "Estilo 3D Pixar" genérico (saturado 2023-2024)
- ❌ "Cyberpunk neon" sem propósito (cliché)
- ❌ Avatar IA "estilo Notion ilustrado" (saturado)
- ❌ Mulher genérica "perfeita" como influencer IA
- ❌ Hero com gradient roxo-azul + figura humana flutuando

### Anti-Padrões Éticos
- ❌ Imitação de fotógrafo vivo sem consentimento (legal cinza)
- ❌ Imitação de pessoa real (deepfake — ilegal em vários contextos)
- ❌ Apropriação de estilo de artista vivo sem crédito
- ❌ Geração de conteúdo enganoso (foto "real" que não é)

## Custos e Spending Limits

### Custos por Iteração
- **Low quality (1K)**: $0.005-0.02
- **Medium quality (2K)**: $0.05-0.10
- **High quality (4K)**: $0.15-0.30
- **Premium (upscale + polish)**: $0.50-1.00

### Recomendação de Spending Limit por Volume Mensal
- **Iniciante (5-15 peças/mês)**: $10/mês
- **Operacional (30-60 peças/mês)**: $40/mês
- **Intensivo (100-200 peças/mês)**: $100/mês
- **Profissional/agência (500+/mês)**: $300/mês

### Regra de Ouro
- Itera em low, valida em medium, finaliza em high
- Não custa nada testar 4 versões em low, escolher 1, finalizar em high
- Imagem comum (story, post, slide secundário): low quality, 1-2 iterações, $0.05 total
- Imagem importante (capa de carrossel, hero): medium quality, 3-5 iterações, $0.30
- Imagem hero campaign (capa de site, anúncio principal): high quality + upscale + polish, 10+ iterações, $1.50-3.00

## Checklist Operacional

### Antes de Gerar Imagem
1. Lê este arquivo (foco em seções 4, 5, 6)
2. Lê DNA.md (seção 3 — Estilo visual + 3.8 — Direção fotográfica)
3. Constrói image_brief estruturado (JSON)
4. Escolhe engine apropriada (seção 3)
5. Define quality tier (low/medium/high) baseado no contexto
6. Gera 4 variações
7. Auditoria (anti-padrões seção 12)
8. Polish (upscale, inpaint se necessário)

### Antes de Auditar Imagem IA
1. Verifica anti-padrões técnicos (mãos, olhos, texto, sombras)
2. Verifica aderência ao estilo da marca
3. Diagnóstico em prosa + sugestão concreta

---

## Próximo Passo

Definir Brand Behavior (como age em cada canal, crisis playbook).
