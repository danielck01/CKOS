# Uploads Index

## Fluxo RAW -> STUDY -> CANONICAL

1. RAW entra em `000_UPLOADS/`.
2. PMO faz triagem, confere provenance, risco, PII e utilidade.
3. Material pronto vai para `90_READY_FOR_STUDY/`.
4. Uma nota ou manifest e criado em `../000_STUDY_NOTES/`.
5. Somente depois de estudo, revisao e patch plan o conteudo pode sugerir alteracao canonica.

## Como usar

- Salve material bruto na pasta mais especifica possivel.
- Use `00_INBOX_RAW/` apenas quando a classificacao ainda nao estiver clara.
- Mantenha o arquivo bruto intacto sempre que possivel.
- Crie uma study note separada para interpretacao.

## Regras proibidas

- Nao colocar secrets em arquivos.
- Nao editar doc canonico a partir de upload direto.
- Nao mover material para `000_STUDY_NOTES` sem triagem.
- Nao tratar output de IA como evidenciar verificada.
- Nao usar uploads para liberar UI, backend, migrations, APIs ou agentes.

## Exemplos de naming

- `20260527_manus_mcp-connectors-research_pmo_ckos_raw.md`
- `20260527_chatgpt_yaml-template-review_pmo_ckos_raw.md`
- `20260527_google-drive_client-brief_clientops_raw.pdf`
- `20260527_apify_instagram-benchmark_pmo_ckos_raw.csv`

## Exemplos de promocao

- Um PDF tecnico verificado sobre MCP pode gerar uma source manifest em `000_STUDY_NOTES/01_UPLOAD_STUDY_NOTES/`.
- Um export de conector pode gerar uma nota em `000_STUDY_NOTES/03_MCP_CONNECTORS_INTEGRATIONS/`.
- Um benchmark de UX pode gerar uma nota em `000_STUDY_NOTES/04_UI_UX_STUDY/`, sem iniciar UI.

## Exemplos de rejeicao

- Output de IA sem fonte primaria.
- CSV com PII sem autorizacao.
- Print sem contexto, data ou origem.
- Material que mistura CKOS com Branddock sem separar escopo.
- Referencia que exige implementacao imediata.

