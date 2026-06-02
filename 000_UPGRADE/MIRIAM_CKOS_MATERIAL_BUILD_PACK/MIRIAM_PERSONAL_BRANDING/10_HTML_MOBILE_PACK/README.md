# Miriam HTML Mobile Pack - CKOS AI-first Briefing

Status: prototype_initial_output
Scope: mobile static HTML
Created: 2026-05-27

## Funcao

Este pack cria uma experiencia mobile inicial para simular o CKOS + Branddock no projeto Miriam.

Ele nao e HTML final de marca, nao publica conteudo e nao implementa backend. O objetivo e mostrar como o sistema pode transformar uma intencao curta em:

- contexto atual;
- briefing vivo;
- perguntas simuladas;
- artefatos parciais;
- fontes;
- QA;
- ROI;
- gates de aprovacao;
- proximos passos.

## Arquivos principais

- `index.html` - experiencia mobile standalone.
- `styles.css` - visual system responsivo.
- `app.js` - simulacao local de perguntas, respostas, progresso e artefatos.
- `assets/cdn-image-map.js` - mapa de slots para trocar por links CDN.
- `assets/briefing_questions.json` - payload das perguntas.
- `docs/GOOGLE_DRIVE_QUESTIONS_UPLOAD_SCRIPT.md` - nota de uso do script.
- `scripts/google_drive_create_briefing_questions.gs` - Google Apps Script para criar Doc + Sheet com perguntas.

## Como abrir

Abra `index.html` no navegador. O arquivo funciona offline, sem build e sem servidor.

## Como usar as imagens

As imagens recebidas foram usadas como referencia de UI/UX: glass cards, mobile widgets, commandbar, cards flutuantes, moodboard visual e narrativa interativa.

Quando os links CDN chegarem, preencher `assets/cdn-image-map.js`.

## Como enviar pelo WhatsApp

Compacte a pasta `10_HTML_MOBILE_PACK` e envie o `.zip`. O destinatario pode extrair e abrir `index.html`.

## Bloqueios

- Nao usar como estrategia final.
- Nao usar como promessa juridica.
- Nao usar como material publico sem QA e revisao humana.
- Nao afirmar conformidade OAB sem revisao juridica.
