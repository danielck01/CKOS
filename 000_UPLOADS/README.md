# 000_UPLOADS

## Funcao da pasta

Camada RAW do CKOS. Recebe material bruto importado antes de qualquer interpretacao, estudo ou promocao para documentacao canonica.

## O que pode entrar

- PDFs, prints, exports, benchmarks, documentos externos, pesquisas, CSVs, tabelas, imagens, videos, transcricoes, outputs de IA, exports de conectores e insumos de projetos.

## O que nao pode entrar

- Documentacao canonica.
- Patch aplicado em docs oficiais.
- Tokens, secrets ou credenciais em texto claro.
- Arquivo que declare decisao arquitetural como verdade sem passar por `000_STUDY_NOTES`.

## Naming obrigatorio

`YYYYMMDD_source-tool_topic_owner_status.ext`

Exemplo: `20260527_manus_mcp-connectors-research_pmo_ckos_raw.md`

## Regra de saida

Todo material sai por triagem para `90_READY_FOR_STUDY/`, depois vira source manifest e study note em `../000_STUDY_NOTES/`.

## Quando mover para STUDY

Mover apenas quando houver provenance minima, owner, classificacao de risco e utilidade clara para CKOS.

## Quando arquivar

Arquivar em `99_ARCHIVE/` quando duplicado, expirado, irrelevante, inseguro, sem provenance recuperavel ou rejeitado por PMO.

## Risco principal

Confundir material bruto, output de IA ou referencia externa com fonte de verdade canonica.

## Politica de PII

Qualquer material com PII deve ser marcado no nome/status ou em manifest futuro, revisado antes de estudo e nunca exposto em doc canonico sem sanitizacao.

## Politica de provenance

Todo item deve preservar origem, ferramenta, data, owner e contexto. Se a origem nao for verificavel, o status padrao e `unverified`.

## Fluxo

`RAW upload -> triage -> source manifest -> study note YAML -> review -> patch candidate -> Founder approval -> canonical patch`

## Proibido

- Mover arquivos existentes para esta pasta sem patch plan.
- Promover conteudo RAW direto para docs canonicos.
- Tratar Manus, n8n, Antigravity, ChatGPT, Claude ou Codex como fonte de verdade.
- Tratar MCP, n8n ou conectores como core runtime por estarem citados em uploads.

