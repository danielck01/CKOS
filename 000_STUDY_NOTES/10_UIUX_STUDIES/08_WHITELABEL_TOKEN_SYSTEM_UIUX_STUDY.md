---
title: "Whitelabel Token System UI/UX Study"
file: "08_WHITELABEL_TOKEN_SYSTEM_UIUX_STUDY.md"
phase: 000_STUDY_NOTES
category: study_note
status: draft
version: 1.0.0
owner: pmo_ckos
responsible_agent: antigravity_design_study
reviewers:
  - pmo_ckos
  - metacognik
approval_required:
  - founder
confidence: unverified
provenance_status: unverified
source_tool: antigravity
purpose: "Definir o sistema de tokens whitelabel tematizável do CKOS para garantir flexibilidade de marca sem comprometer a usabilidade e o contraste."
inputs:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/01_VISUAL_REFERENCE_TAXONOMY_CANVAS_OS.md"
  - "000_STUDY_NOTES/10_UIUX_STUDIES/05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md"
outputs:
  - "08_WHITELABEL_TOKEN_SYSTEM_UIUX_STUDY.md"
framework: "Sentir -> Pensar -> Criar -> Conectar -> Avaliar -> Elevar"
edge_cases:
  - "Customização de cores destruindo o contraste mínimo WCAG exigido para legibilidade"
  - "Estilo de marca excessivo afetando cores semânticas de erro ou aprovação"
integrations:
  - "antigravity_design_study"
prompts:
  - "Especificar o sistema de design tokens whitelabel e customização do CKOS."
metrics:
  - "Zero de código implementado"
  - "100% de conformidade com regras WCAG e tokens invariantes mapeados"
related_notes:
  - "000_STUDY_NOTES/10_UIUX_STUDIES/05_NEURODESIGN_AND_COGNITIVE_LOAD_RULES.md"
tags:
  - "whitelabel"
  - "design_tokens"
  - "theming"
  - "design_study"
---

# Whitelabel Token System: UI/UX Study

Este estudo especifica a arquitetura de tokens visuais tematizáveis (*whitelabel*) do CKOS, garantindo que a customização por clientes corporativos não comprometa a usabilidade, o contraste e a semântica operacional do sistema de IA.

---

## 1. Tokens Invariantes do CKOS (Nunca Mudam)

Para manter a integridade visual da interface e preservar a clareza analítica do usuário sob qualquer tema, os seguintes tokens são declarados **invariantes** e não sofrem alteração:

* **Fundo Base Neutro Escuro (`--ckos-bg-base`)**: O preto profundo absoluto (`#000000` a `#0A0A0C`) permanece como o plano de fundo do sistema no tema escuro, garantindo o contraste necessário para a visualização dos backlights luminosos.
* **Tipografia Reflexiva (`--font-family-serif`)**: A tipografia serifada de alta qualidade (ex: Lora ou Playfair) utilizada nos painéis de memórias aprendidas (`ck_memory.md`) e no ROI Panel é preservada para sinalizar o estado cognitivo de reflexão.
* **Escala de Espaçamento (`--ckos-spacing-*`)**: A escala de padding e margins baseada em incrementos de 4px (`4px`, `8px`, `12px`, `16px`, `24px`, `32px`, `48px`, `64px`) é fixa para garantir harmonia espacial e consistência das Leis da Gestalt.
* **Raio de Arredondamento do Contêiner Base (`--ckos-radius-squircle`)**: O raio de squircle de `24px` a `32px` para cartões principais e widgets flutuantes é invariante para manter a geometria orgânica suavizada.

---

## 2. Tokens Tematizáveis por Cliente (Customizáveis)

Os clientes corporativos e parceiros podem customizar os seguintes tokens para expressar sua identidade de marca:

* **Cor de Destaque da Marca (`--brand-accent`)**: Cor primária aplicada a botões de ação secundários ativos, links de navegação estáticos, preenchimentos de seleção e foco de inputs.
* **Gradiente de Background Decorativo (`--brand-bg-gradient`)**: Os tons do gradiente orgânico subjacente que colore o canvas pontilhado nas zonas periféricas de repouso visual.
* **Tipografia Operacional (`--font-family-sans`)**: A fonte de comandos e interfaces quantitativas de alta precisão (ex: Outfit, Inter, Roboto), desde que garanta legibilidade sob renderização de alta densidade.
* **Intensidade do Backdrop Blur (`--brand-glass-blur`)**: O nível de desfoque dos contêineres de Calm Glass (variando de `15px` a `35px` físicos).

---

## 3. Tokens Proibidos de Alterar (Strictly Forbidden)

Sob nenhuma hipótese, configurações temáticas ou scripts whitelabel de parceiros podem alterar:

* **Cores Semânticas de Estado (`--state-color-*`)**: Vermelho de erro, verde de sucesso e amarelo de aprovação são reservados exclusivamente ao runtime e não podem ser substituídos pelas cores institucionais do cliente.
* **Tamanho Mínimo de Alvos de Toque (`--ckos-touch-target-min`)**: A especificação de `48px` x `48px` para interações críticas móveis é imutável.
* **Zonas de Segurança Física (`--ckos-safe-area-*`)**: Safe Areas superiores e inferiores móveis são calculadas pelo sistema a nível de hardware e protegidas contra sobreposição temática.

---

## 4. Estados Críticos de Cor e Semântica

As cores que comunicam a integridade operacional do sistema são padronizadas em HSL e Hex para garantir legibilidade e consistência universal:

```
+------------------------------------------------------------+
| ESTADOS CRÍTICOS DE COR (HSL SEMÂNTICO DO CKOS)            |
|                                                            |
| [state-success]   Hex #10B981 | HSL 142, 70%, 45% (Verde)  |
| [state-error]     Hex #EF4444 | HSL 346, 84%, 50% (Vermelho) |
| [state-warning]   Hex #F59E0B | HSL 45, 93%, 47%  (Amarelo) |
| [state-running]   Hex #3B82F6 | HSL 217, 91%, 60% (Azul)     |
| [state-blocked]   Hex #F97316 | HSL 18, 88%, 53%  (Laranja)  |
+------------------------------------------------------------+
```

Esses tokens de estado alimentam diretamente as state machines visuais descritas no estudo 03, garantindo que o cérebro associe instantaneamente o status do runtime semântico com a pista visual de cor, sem ambiguidade.

---

## 5. Regras Dark / Light / Glass

A customização whitelabel deve obedecer a regras estruturais de física de interface dependendo do modo ativo:

### A. Dark Mode (Padrão e Canônico)
* **Objetivo**: Reduzir a fadiga visual do usuário técnico e favorecer o foco orgânico dos backlights.
* **Fórmula do Vidro (Calm Glass)**:
  `background: rgba(10, 10, 12, 0.45);`
  `backdrop-filter: blur(25px);`
  `border: 1px solid rgba(255, 255, 255, 0.08);`

### B. Light Mode (Adaptativo sob Demanda)
* **Objetivo**: Garantir legibilidade em ambientes de alta iluminação solar direta.
* **Fórmula do Vidro (Calm Glass)**:
  `background: rgba(245, 245, 247, 0.75);`
  `backdrop-filter: blur(20px);`
  `border: 1px solid rgba(0, 0, 0, 0.08);`
* **Restrição**: No Light Mode, a opacidade dos vidros é aumentada para no mínimo `75%` para prevenir que gradientes claros de fundo destruam o contraste tipográfico.

### C. Glassmorphism Seguro
* O contorno do vidro deve sempre possuir uma sombra interna reflexiva ou uma borda fina de destaque com opacidade invertida ao fundo (ex: contorno branco translúcido no tema escuro, contorno escuro translúcido no tema claro). Isso demarca o Z-index tridimensionalmente sem sobrecarregar a tela com sombras pretas pesadas de SaaS genérico.

---

## 6. Validação de Contraste e Acessibilidade (WCAG 2.1)

Para evitar que esquemas de cores de clientes corporativos tornem o CKOS inutilizável ou causem fadiga ocular, o design system incorpora um validador algorítmico de contraste em tempo de configuração.

### A. Taxas Mínimas de Contraste Exigidas (WCAG 2.1 AA)
* **Texto Técnico de Logs e Dados (Menor que 18pt)**: Contraste mínimo de **4.5:1** contra a superfície de fundo adjacente.
* **Títulos e Labels Grandes (Maior ou igual a 18pt ou 14pt em Bold)**: Contraste mínimo de **3.0:1** contra o fundo.
* **Controles Interativos e Ícones de Status**: Contraste mínimo de **3.0:1** para demarcação física.

### B. Comportamento do Validador de Temas
1. O administrador do cliente insere a cor de marca institucional (ex: `#FFE600` - Amarelo limão).
2. O validador testa a legibilidade de textos brutos e brancos sobrepostos à cor da marca.
3. Se a taxa de contraste falhar (ex: texto branco sobre fundo amarelo limão resulta em `1.5:1`), o validador **bloqueia** a aplicação do tema.
4. O sistema sugere alternativas de acessibilidade próximas na escala tonal (ex: escurecer o amarelo para `#B88600`, que atinge a taxa de contraste `4.8:1`).

---

## 7. Brand Intensity Levels

A aplicação da marca customizada na interface do CKOS é dosada em três perfis de intensidade configuráveis pelo PMO:

* **Low (Minimalista Técnico)**: A marca é restrita à assinatura de cabeçalho e cor dos botões de ação final. A área de trabalho permanece estritamente neutra. (Indicado para auditoria técnica profunda e depuração de código).
* **Medium (Corporativo Integrado)**: A cor da marca colore sutilmente os backlights de tarefas concluídas, as pílulas ativas da Command Bar e o gradiente das dunas de repouso periférico.
* **High (Imersão de Marca)**: O tema do cliente penetra profundamente no sistema operacional. Os conectores de curvas Bézier no canvas usam cores da marca, as bordas de Calm Glass ganham contornos reflexivos estilizados e o Node Canvas utiliza texturas institucionais, desde que aprovado no validador de contraste.

---

## 8. Preservação de Usabilidade (UX Safeguards)

Para impedir que a customização do cliente destrua a inteligência operacional do sistema operacional de IA, a UI adota as seguintes salvaguardas:

* **Isolamento de Status**: Cores de marca nunca podem se sobrepor ou compartilhar o mesmo tom HSL de estados de execução. Se a cor da marca for verde, a cor de sucesso (`state-success`) adota uma variação esmeralda brilhante distinta ou é acompanhada obrigatoriamente de marcadores simbólicos de texto (`[SUCCESS]`, `[APPROVED]`) para que a interface permaneça compreensível para usuários daltônicos.
* **Máscaras de Contraste de Background**: Se o cliente carregar uma imagem de fundo complexa ou de alta saturação sob o canvas, a UI insere uma máscara sólida preta com opacidade de `45%` entre o fundo e os widgets operacionais, garantindo que o backdrop-blur não sofra vazamento de luz indesejado que oculte textos de logs finos.
