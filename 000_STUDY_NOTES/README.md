# 000_STUDY_NOTES

## Funcao da pasta

Camada STUDY do CKOS. Transforma material RAW em notas interpretadas, auditaveis e prontas para decisao PMO.

## O que pode entrar

Source manifests, study notes, research synthesis, decision logs, patch candidates e notas de revisao.

## Subpastas especializadas

- `11_AI_FIRST_OPERATING_PATTERNS/`: estudos de padroes operacionais AI First, como intencao minima, perguntas inteligentes, plano, approval, execucao controlada e memoria.
- `12_SESSION_GATES/`: gates auxiliares para sessoes especializadas, incluindo Antigravity Study Mode; usa `ck_memory.md` como memoria ativa e nao autoriza implementacao nem canonizacao.
- `13_AI_FIRST_PROJECT_OPERATING_SYSTEM/`: estudos de Project AI-first, Task AI-first, Notes AI-first, perguntas inteligentes, approval batch, ROI, feedback, learning e candidatos para Doc 27; usa `ck_memory.md` e nao autoriza Doc 27, implementacao, agentes reais ou runtime.

## O que nao pode entrar

Documentacao canonica final, arquivo bruto sem interpretacao, secrets, PII nao classificada ou implementacao.

## Naming obrigatorio

`YYYYMMDD_source-tool_topic_owner_status.md`

## Regra de saida

Uma nota sai para patch candidate, decision log, archive ou patch plan aprovado. Ela nao altera canonicamente nada sozinha.

## Quando mover para CANONICAL

Nunca mover direto. A saida correta e patch plan aprovado pelo Founder, QA documental e registro posterior nos reports oficiais.

## Quando arquivar

Quando a nota for rejeitada, superada, duplicada, sem confidence suficiente ou nao aplicavel ao CKOS.

## Risco principal

Confundir interpretacao estudada com documentacao canonica.

## Politica de PII

Notas devem citar PII apenas quando necessario, com sanitizacao e classificacao explicita.

## Politica de provenance

Toda nota deve referenciar `source_path`, `source_type`, `source_tool` e `provenance_status`.

## Fluxo obrigatorio

`raw upload -> triage -> source manifest -> study note YAML -> PMO review -> specialist review -> patch candidate -> patch plan -> Founder approval -> canonical patch`
