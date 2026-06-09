# 02_RESEARCH_SYNTHESIS

## Função

Consolidar deep research externas em sínteses PMO, comparativos e mapas de evidência **antes** de qualquer promoção ao canônico ou ao F1.

## Conteúdo atual (2026-06-09)

| Arquivo | Origem | Tema | Status |
|---|---|---|---|
| `SYSTEM_RESPONSE.md` | Founder, 2026-06-09 | Smart Response Engine (proposta, 25 seções) | sob triagem PMO |
| `deep-research-report (5).md` | DR externa, 2026-06-09 | Qualidade de resposta LLM/copilotos (anti-padrões, métricas, user/audit mode) | bruta |
| `deep-research-report (6).md` | DR externa, 2026-06-09 | Aprendizado progressivo + memória de usuário (declarada/observada/inferida/validada) + federated learning + privacy | bruta |
| `deep-research-report (7).md` | DR externa, 2026-06-09 | Interfaces adaptativas / cognitive UX / glassmorphism / presets de modo | bruta |
| `deep-research-report (8).md` | DR externa, 2026-06-09 | Threat model agêntico + approval flows (OWASP Agentic Top 10) | bruta |
| `deep-research-report (9).md` | DR externa, 2026-06-09 | Governança de runtime agêntico (NIST AI RMF, OPA, AI Act, two-phase approval, SCITT) | bruta |
| `deep-research-report (10).md` | DR externa, 2026-06-09 | Smart Questions Engine (EVIG, ask-vs-assume, traceability question→slot→KPI) | bruta |
| `deep-research-report (11).md` | DR externa, 2026-06-09 | Observabilidade, tracing e telemetria de agentes (OpenTelemetry, Agent Run, LGPD) | bruta |
| `deep-research-report (12).md` | DR externa, 2026-06-09 | Agent Operating Systems em 2026 (OpenAI/Anthropic/Google/Temporal/LangGraph + MCP/A2A) | bruta |

## Status PMO

Sob triagem pela sessão `S-USER-PMO-CLAUDE-20260609-001`. Estado vivo em [`ck_memory.md`](ck_memory.md).

**Verdict preliminar:** as 8 DRs + `SYSTEM_RESPONSE.md` **reforçam** mas **não alteram estruturalmente** o veredito do `000_ROADMAPS/22_CONSOLIDATION/F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md` (2026-06-04, claude_opus_4_8). Detalhes em `ck_memory.md`.

## O que pode entrar

Research synthesis, comparativos, conclusões PMO, mapas de evidência, e deep research bruta enquanto está em triagem.

## O que não pode entrar

- Patch aplicado ao canônico
- Output de IA sem provenance
- Conteúdo pessoal sensível sem necessidade

## Naming

- **Síntese PMO:** `YYYYMMDD_source-tool_topic_owner_status.md`
- **Deep research bruta:** mantém nome de origem **temporariamente** até a triagem PMO virar síntese.

## Regra de saída

Gerar decision log ou patch candidate quando houver decisão clara. Promoção ao canônico **nunca** direta — sempre via patch plan e sessão `canonical_patch` separada.

## Política de PII / provenance

Sínteses removem dados pessoais; sempre listar related_notes e fontes (URL ou citation). Deep research bruta retém metadados de origem.

## Risco principal

Misturar fontes com confidence diferentes sem marcar contradições; ou fazer DR virar documentação canônica sem PMO triagem (refabrica fragmentação 1:35).

## Memória da pasta

→ [`ck_memory.md`](ck_memory.md) (substitui `_folder_memory.md`; padrão atualizado em 2026-06-09).
