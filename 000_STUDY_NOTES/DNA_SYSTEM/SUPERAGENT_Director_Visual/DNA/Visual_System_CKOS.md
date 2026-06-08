---
title: Visual System CKOS
folder: DNA
type: visual_system
status: draft
version: 1.0.0
owner: PMO_CKOS
agents:
  - Cognik
  - Metacognik
  - PMO_CKOS
---

# Visual System CKOS

## Estética Anchor

**Referências principais**: Canvas OS, Notion, Linear, Vercel
**Filosofia**: Data-dense minimal, calm glass, chips translúcidos, gradientes suaves, tipografia geométrica

## Paleta de Cores

### Primárias
- **Primary**: #EC5E26 (Laranja Terracota)
  - Uso: CTAs, estados ativos, destaques, approval gates
  - Contexto: Ações principais, elementos que precisam de atenção
  - Acessibilidade: Passa em WCAG AA com texto branco (#FFFFFF)

- **Dark**: #1B1411 (Cinza Quente Escuro)
  - Uso: Texto principal, fundo escuro, bordas
  - Contexto: Conteúdo denso, seções de alta informação
  - Acessibilidade: Passa em WCAG AAA com texto claro (#F1ECE3)

- **Light**: #F1ECE3 (Bege Claro)
  - Uso: Fundo claro, cards, painéis
  - Contexto: Superfícies de conteúdo, áreas de leitura
  - Acessibilidade: Passa em WCAG AA com texto escuro (#1B1411)

### Secundárias
- **Accent**: #EC5E26 (Laranja Terracota - mesma da primária)
  - Uso: Chips, badges, indicadores de status
  - Contexto: Elementos de informação, tags, categorias

- **Muted Dark**: #2A2420 (Cinza Quente Médio-Escuro)
  - Uso: Texto secundário, bordas sutis
  - Contexto: Informação de suporte, separadores

- **Muted Light**: #FAF8F5 (Bege Claro-Extra)
  - Uso: Fundo de seções alternadas, hover states
  - Contexto: Variação de fundo para hierarquia visual

### Funcionais
- **Success**: #10B981 (Verde)
  - Uso: Estados de sucesso, aprovações, outputs positivos
  - Contexto: Approval gates aprovados, workflows completados

- **Warning**: #F59E0B (Amarelo)
  - Uso: Alertas, estados de atenção, warnings
  - Contexto: Riscos médios, decisões pendentes

- **Error**: #EF4444 (Vermelho)
  - Uso: Erros, estados críticos, bloqueios
  - Contexto: Falhas de workflow, approval gates rejeitados

- **Info**: #3B82F6 (Azul)
  - Uso: Informação neutra, estados informativos
  - Contexto: Dados, métricas, status neutro

### Transparências
- **Glass Dark**: rgba(27, 20, 17, 0.85)
  - Uso: Calm glass em fundo escuro
  - Contexto: Command Center, painéis flutuantes

- **Glass Light**: rgba(241, 236, 227, 0.92)
  - Uso: Calm glass em fundo claro
  - Contexto: Cards, modais, overlays

- **Chip Translucent**: rgba(236, 94, 38, 0.15)
  - Uso: Chips de informação, tags
  - Contexto: Categorias, filtros, badges

## Tipografia

### Fonte Principal
- **Família**: Inter (Google Fonts) ou sistema
- **Estilos**: Regular (400), Medium (500), Semibold (600), Bold (700)
- **Uso**: Texto de corpo, UI, parágrafos

### Fonte de Display
- **Família**: Inter Tight (Google Fonts) ou sistema
- **Estilos**: Semibold (600), Bold (700), Extrabold (800)
- **Uso**: Headlines, títulos, CTAs

### Fonte Monoespaçada
- **Família**: JetBrains Mono ou Fira Code
- **Estilos**: Regular (400), Medium (500)
- **Uso**: Código, comandos, dados técnicos

### Escala Tipográfica
- **Display XL**: 48px / 56px (line-height 1.1) - Hero headlines
- **Display L**: 36px / 44px (line-height 1.2) - Page titles
- **Display M**: 28px / 36px (line-height 1.3) - Section titles
- **Heading XL**: 24px / 32px (line-height 1.3) - Card titles
- **Heading L**: 20px / 28px (line-height 1.4) - Subheadings
- **Heading M**: 18px / 24px (line-height 1.3) - Small titles
- **Body L**: 16px / 24px (line-height 1.5) - Body text
- **Body M**: 14px / 20px (line-height 1.4) - Secondary text
- **Body S**: 12px / 16px (line-height 1.3) - Captions, labels
- **Caption**: 11px / 14px (line-height 1.3) - Fine print

### Peso e Uso
- **Regular (400)**: Texto de corpo, parágrafos longos
- **Medium (500)**: Texto secundário, labels
- **Semibold (600)**: Headlines, títulos, CTAs
- **Bold (700)**: Destaques, ênfase
- **Extrabold (800)**: Hero headlines (raro)

## Grid e Espaçamento

### Grid Base
- **Columns**: 12 columns
- **Gutter**: 24px
- **Margin**: 32px (desktop), 16px (mobile)
- **Max Width**: 1280px

### Escala de Espaçamento
- **0**: 0px
- **1**: 4px - Micro spacing, icon padding
- **2**: 8px - Small spacing, tight elements
- **3**: 12px - Default spacing, related elements
- **4**: 16px - Medium spacing, sections
- **5**: 24px - Large spacing, major sections
- **6**: 32px - XL spacing, page sections
- **7**: 48px - XXL spacing, major breaks
- **8**: 64px - Section breaks
- **9**: 96px - Page breaks

### Component Spacing
- **Button padding**: 12px 24px (vertical horizontal)
- **Card padding**: 24px
- **Input padding**: 12px 16px
- **Chip padding**: 6px 12px
- **Modal padding**: 32px

## Bordas e Cantos

### Border Radius
- **None**: 0px - Divisores, separadores
- **Small**: 4px - Botões, inputs pequenos
- **Medium**: 8px - Cards, painéis
- **Large**: 12px - Modais, containers grandes
- **XL**: 16px - Hero cards, featured elements
- **Full**: 9999px - Pills, badges, chips

### Border Width
- **None**: 0px - Elementos sem borda
- **Thin**: 1px - Separadores sutis
- **Medium**: 2px - Cards, inputs
- **Thick**: 3px - Destaques, CTAs
- **Heavy**: 4px - Elementos de alta ênfase

## Sombras

### Shadow Scale
- **None**: none - Elementos planos
- **Small**: 0 1px 2px rgba(27, 20, 17, 0.05) - Hover states
- **Medium**: 0 4px 6px rgba(27, 20, 17, 0.07) - Cards
- **Large**: 0 10px 15px rgba(27, 20, 17, 0.1) - Modals, dropdowns
- **XL**: 0 20px 25px rgba(27, 20, 17, 0.15) - Hero cards, featured

### Inner Shadow
- **Inset**: inset 0 2px 4px rgba(27, 20, 17, 0.05) - Inputs, pressed states

## Motion

### Durações
- **Instant**: 0ms - Mudanças de estado instantâneas
- **Fast**: 150ms - Hover states, micro-interações
- **Default**: 300ms - Transições padrão
- **Slow**: 500ms - Modais, grandes transições
- **Very Slow**: 700ms - Page transitions

### Easing
- **Linear**: linear - Movimento constante
- **Ease In**: cubic-bezier(0.4, 0, 1, 1) - Entrada suave
- **Ease Out**: cubic-bezier(0, 0, 0.2, 1) - Saída suave
- **Ease In Out**: cubic-bezier(0.4, 0, 0.2, 1) - Entrada e saída suaves (padrão)

### Animações
- **Fade In**: opacity 0 → 1
- **Fade Out**: opacity 1 → 0
- **Slide Up**: translateY(20px) → translateY(0)
- **Slide Down**: translateY(-20px) → translateY(0)
- **Scale In**: scale(0.95) → scale(1)
- **Scale Out**: scale(1) → scale(0.95)
- **Pulse**: scale(1) → scale(1.05) → scale(1)

## Componentes Visuais

### Buttons
- **Primary**: Fundo #EC5E26, texto branco, border-radius 8px, padding 12px 24px
- **Secondary**: Fundo transparente, borda 2px #EC5E26, texto #EC5E26, border-radius 8px, padding 12px 24px
- **Ghost**: Fundo transparente, texto #EC5E26, border-radius 8px, padding 12px 24px
- **Destructive**: Fundo #EF4444, texto branco, border-radius 8px, padding 12px 24px

### Cards
- **Default**: Fundo #F1ECE3, borda 1px #2A2420, border-radius 12px, padding 24px, shadow medium
- **Elevated**: Fundo #FAF8F5, borda 1px #2A2420, border-radius 12px, padding 24px, shadow large
- **Glass**: Fundo rgba(241, 236, 227, 0.92), backdrop-filter blur(25px), border-radius 12px, padding 24px

### Chips
- **Default**: Fundo rgba(236, 94, 38, 0.15), texto #EC5E26, border-radius 9999px, padding 6px 12px
- **Active**: Fundo #EC5E26, texto branco, border-radius 9999px, padding 6px 12px
- **Muted**: Fundo rgba(42, 36, 32, 0.1), texto #2A2420, border-radius 9999px, padding 6px 12px

### Inputs
- **Default**: Fundo #FAF8F5, borda 2px #2A2420, border-radius 8px, padding 12px 16px
- **Focus**: Bordas 2px #EC5E26, shadow small
- **Error**: Bordas 2px #EF4444

### Modals
- **Overlay**: Fundo rgba(27, 20, 17, 0.6), backdrop-filter blur(4px)
- **Content**: Fundo #F1ECE3, border-radius 16px, padding 32px, shadow XL, max-width 600px

## Layout Patterns

### Command Center
- **Width**: 100% (full width)
- **Height**: 64px (fixed height)
- **Background**: Glass dark (rgba(27, 20, 17, 0.85))
- **Border**: Bottom 1px #2A2420
- **Padding**: 16px horizontal
- **Elements**: Input central, chips laterais, cost guard top-right

### Node Canvas
- **Background**: #F1ECE3 com grid pattern sutil
- **Grid**: Dot pattern 20px spacing, cor #2A2420 com 0.1 opacity
- **Nodes**: Cards elevados com shadow medium
- **Connections**: Curvas Bézier suaves, cor #EC5E26 com 0.5 opacity

### Project Dashboard
- **Layout**: 3 columns (sidebar 280px, main auto, right panel 320px)
- **Sidebar**: Fundo #2A2420, texto #F1ECE3
- **Main**: Fundo #F1ECE3
- **Right Panel**: Fundo #FAF8F5, borda left 1px #2A2420

## Responsividade

### Breakpoints
- **Mobile**: < 640px
- **Tablet**: 640px - 1024px
- **Desktop**: 1024px - 1280px
- **Wide Desktop**: > 1280px

### Mobile Adaptations
- **Grid**: 4 columns
- **Spacing**: Reduzido para 16px margin
- **Typography**: Display L → 32px, Heading XL → 20px
- **Command Center**: Height 56px, padding 12px
- **Cards**: Padding 16px

## Acessibilidade

### Contraste
- **WCAG AA**: 4.5:1 para texto normal, 3:1 para texto grande
- **WCAG AAA**: 7:1 para texto normal, 4.5:1 para texto grande
- **Todas as cores primárias passam WCAG AA**

### Focus States
- **Outline**: 2px solid #EC5E26, offset 2px
- **Skip Links**: Visíveis quando focado
- **Keyboard Navigation**: Tab order lógico

### Screen Readers
- **ARIA labels**: Em todos os elementos interativos
- **Semantic HTML**: Uso correto de headings, lists, landmarks
- **Alt text**: Descritivo para imagens

## Anti-Padrões Visuais

### Evitar
- Gradientes genéricos roxo-azul
- "Estilo 3D Pixar" glossy
- Avatares IA óbvios com olhos vidrados
- Sombras duras não naturais
- Bordas arredondadas excessivas (> 20px)
- Cores neon saturadas sem propósito
- Padrões de grid óbvios e repetitivos
- Tipografia decorativa não legível
- Espaçamento inconsistente
- Animações excessivas ou distrativas

### Prefere
- Gradientes suaves monocromáticos
- Superfícies matte foscas
- Minimalismo técnico
- Sombras sutis e naturais
- Border radius consistente (8-12px)
- Paleta saturada com propósito
- Grid pattern sutil e elegante
- Tipografia geométrica legível
- Escala de espaçamento consistente
- Animações funcionais e rápidas

---

## Próximo Passo

Definir Photography Direction (7 setups de iluminação, composição, mood).
