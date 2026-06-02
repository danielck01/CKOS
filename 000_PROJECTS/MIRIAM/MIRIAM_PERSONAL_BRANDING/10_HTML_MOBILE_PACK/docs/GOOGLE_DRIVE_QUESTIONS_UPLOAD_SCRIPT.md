# Google Drive Questions Upload Script

Status: ready_to_use_after_human_review

## Objetivo

Criar no Google Drive um Google Doc e uma Google Sheet com as perguntas do Briefing Vivo da Miriam.

## Fonte tecnica

O script usa Google Apps Script, que roda no ambiente do Google Workspace e permite usar servicos como Drive, Docs e Sheets por JavaScript. Referencia oficial: [Google Apps Script intro](https://codelabs.developers.google.com/codelabs/apps-script-intro/) e [clasp / Apps Script local workflow](https://codelabs.developers.google.com/codelabs/clasp).

## Como usar

1. Abrir `script.google.com`.
2. Criar um novo projeto.
3. Copiar o conteudo de `../scripts/google_drive_create_briefing_questions.gs`.
4. Ajustar `TARGET_FOLDER_ID`.
5. Executar `createMiriamBriefingFiles`.
6. Autorizar acesso quando o Google solicitar.
7. Conferir o Doc e a Sheet na pasta alvo.

## O que o script cria

- Google Doc: `CKOS - Briefing Vivo Miriam - Perguntas`
- Google Sheet: `CKOS - Briefing Vivo Miriam - Response Memory`

## Campos da Sheet

- question_id;
- category;
- question;
- why_now;
- answer;
- classification;
- approval_status;
- notes.

## Cuidado

Nao executar em pasta errada. Nao compartilhar publicamente sem revisar permissoes.
