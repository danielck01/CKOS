---
title: Claude #1 — Dispatcher (gera prompts · fan-in mecânico · registry/Kanban)
file: S-CLAUDE1_DISPATCHER.md
layer: auxiliary
doc_type: pmo_session_task
phase: 000_ROADMAPS
category: consolidation
status: active
version: 0.1.0
created_at: 2026-06-04
owner: pmo_ckos
session_id: S-P1-L3DISPATCH-CLAUDE-20260604-001
role: dispatcher
companion_of: 00_WAVE1_DISPATCH_AND_PROTOCOL.md
non_authority_boundary: >
  Sessão de coordenação. Gera prompts e propõe entradas de registry; NÃO canoniza, NÃO
  edita canônico 01-28, NÃO aprova lote (isso é Founder), NÃO sobrescreve releases de outras
  sessões. Autoridade vem do lock + Founder, não do papel.
tags: [session-task, claude, dispatcher, slot1, l3]
---

# Claude #1 — Dispatcher (Slot 1 do Runbook)

> **Esta é a sessão que você está lendo agora.** Papel: tirar o relay manual do caminho crítico.
> Não escreve candidate de reconciliação; **gera os prompts dos escritores, faz o fan-in mecânico
> e mantém registry + Kanban**. Continuidade: se outro Claude assumir o dispatch, cola a §A.

---

## A. META-PROMPT (Runbook §5c) — para colar se outro Claude assumir o Dispatcher

```txt
You are a CKOS session under MULTI_SESSION_EXECUTION_POLICY.
ROLE: Dispatcher / PMO local. MODE: coordenação. SESSION: S-P1-L3DISPATCH-CLAUDE-20260604-001.
READ: SESSION_REGISTRY.md, 00_WAVE1_DISPATCH_AND_PROTOCOL.md, ck_tasks/ck_memory,
      00_CKOS_CONSOLIDATION_MAP_AND_GAP_AUDIT.md.
TASK:
  1. Liste o estado (locks ativos, releases recentes, próximo do backlog).
  2. Confirme os 3 tracks da Onda 1 não-overlap (TR-SKILLS/TR-TRANSF/TR-POLICY).
  3. Para cada escritor sem nota pronta, gere a nota-sessão (template do S-CODEX1_TR-SKILLS).
  4. Marque dependências (Claude#2 Auditor depende dos 3 releases).
  5. Proponha as entradas de SESSION_REGISTRY (não aplique sem lote aprovado).
OUTPUT: notas-sessão prontas + tabela de dispatch + o que exige decisão do Founder.
FORBIDDEN: abrir canônico, aprovar canon/lote, sobrescrever registry de terceiros, implementar.
```

## B. Responsabilidades da sessão (o que EU faço por você)

1. **Gerar** as 5 notas-sessão da Onda (✅ feito: as 5 existem em `L3_WAVE1/`).
2. **Fan-in mecânico:** quando um escritor cola `CHECKOUT RELEASE`, eu confiro registry/lock/escopo/fronteiras e libero o próximo passo. Julgamento de mérito = Claude #2 (Auditor).
3. **Manter estado:** atualizar `SESSION_REGISTRY.md` + o Kanban de relance (§6 da nota de dispatch).
4. **Recusar** prompt que colida com lock ativo (anti-conflito, Runbook §4).

## C. ← PERGUNTAS PARA O FOUNDER (decisões que eu NÃO tomo)

- Aprovar o **LOTE L3-W1** (§0 da nota de dispatch) — destrava as 4 sessões.
- Composição: Windsurf escreve TR-POLICY (inventário+rascunho) ou fica de suporte? (3 opções na minha mensagem).
- **GATE 5** segue como caminho crítico paralelo.

## D. SESSÃO FINALIZADA
```txt
status: active (dispatcher permanece aberto durante a Onda; libera no fan-in final)
next_step: aguardar aprovação do LOTE L3-W1 → liberar escritores → coletar releases → acionar Claude#2
```
