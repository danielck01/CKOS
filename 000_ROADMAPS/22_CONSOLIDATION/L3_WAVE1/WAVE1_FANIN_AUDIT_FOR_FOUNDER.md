---
title: Wave 1 Fan-in — Auditoria Ordenada para o Founder (Skills · Transformers · Policies)
file: WAVE1_FANIN_AUDIT_FOR_FOUNDER.md
layer: auxiliary
doc_type: pmo_fanin_audit
phase: 000_ROADMAPS
category: consolidation
status: awaiting_founder_decision
version: 0.1.0
created_at: 2026-06-04
owner: pmo_ckos
responsible_agent: claude_opus_4_8
session_id: S-P1-L3-CLAUDE2-20260604-001
role: auditor
companion_of: 00_WAVE1_DISPATCH_AND_PROTOCOL.md
audits:
  - L3_WAVE1/DOC06_SKILLS_RECONCILIATION_CANDIDATE.md      # Codex#1 (TR-SKILLS)
  - L3_WAVE1/DOC09_TRANSFORMERS_RECONCILIATION_CANDIDATE.md # Codex#2 (TR-TRANSF)
  - L3_WAVE1/DOC12_POLICIES_RECONCILIATION_CANDIDATE.md     # Windsurf (TR-POLICY)
cross_referenced:
  - 22_CONSOLIDATION/F1_RUNTIME_IO_CONTRACTS_RECONCILIATION_CANDIDATE.md
reviewers:
  - founder
  - metacognik
approval_required:
  - founder
non_authority_boundary: >
  Auditoria read-only. Esta nota NÃO aplica patch, NÃO edita canônico 01-28, NÃO edita os
  3 candidates nem o F1, NÃO aprova. Consolida, ordena e audita canonical-readiness; agrega as
  ARCHITECTURE_QUESTIONS; entrega um pacote único de decisão. Go/hold por item = decisão do Founder.
  Aplicação de qualquer promoção = sessão canonical_patch separada, pós-aprovação.
tags: [consolidation, fan-in, audit, wave1, skills, transformers, policies, l3, pmo, founder-decision]
---

# Wave 1 — Auditoria de Fan-in para o Founder

> **O que esta nota é:** o Slot 2 do Runbook. Lê os 3 candidates dos escritores, **deduplica
> cross-track**, **ordena** o que promover por força × utilidade-F1 × risco, **audita
> canonical-readiness** item a item, **agrega** todas as ARCHITECTURE_QUESTIONS, e cruza com a
> nota `F1_RUNTIME_IO` para não promover 2× o mesmo net-new. Entrega **um** pacote: você decide
> go/hold por item.
> **O que esta nota não é:** não aplica nada. Read-only.

---

## 0. Veredito em uma linha (PMO, direto)

**A Onda 1 produz UM item realmente forte — um contrato de I/O de execução comum (skill + transformer) — e quase nada mais.** Os 3 escritores levantaram ~31 "promoções" cruas; depois de deduplicar cross-track e cruzar com o F1, isso colapsa para **2 promoções prontas (GO agora)**, **um punhado de nomes-candidatos que esperam GATE 5 ou uma decisão de taxonomia**, e **zero promoção de Policies**. O entregável mais valioso da onda **não são as promoções — são as ARCHITECTURE_QUESTIONS**, que convergem para **3 perguntas-mãe**. O risco real da onda é **bloat por catálogo**: despejar 20+ nomes de skill/transformer/policy sem owner/tool/eval violaria a constituição do próprio Doc 06/03.

---

## 1. Método + re-verificação (o que eu realmente fiz)

- **Li integralmente** os 3 candidates (Doc 06 / Doc 09 / Doc 12) + a nota `F1_RUNTIME_IO` para cruzamento.
- **Confirmei a precondição:** as 3 sessões escritoras estão `released_with_required_external_audit` no `SESSION_REGISTRY.md` (linhas 136-139). Essa "external audit requerida" **é esta sessão**. Dependência satisfeita.
- **Re-verifiquei o Windsurf na fonte** (ordem do dispatch: *"você é o dono do julgamento de Policies, não o Windsurf"*). Li `000_UPGRADE/07_POLICIES/` direto:
  - **Boilerplate confirmado byte-a-byte.** `agent_policy`, `cost_policy`, `learning_policy`, `source_policy` são **idênticos** exceto a única linha "Definição". Blocos "Regras base" (5 linhas) e "Checklist" (6 linhas) são **100% iguais** em todos. Não há regra real (condição→ação→enforcement) em nenhum.
  - **Cobertura canônica confirmada real** (não alucinação do Windsurf): `Doc 12` retorna 141 ocorrências de permission/approval/PII/collector/secret/deny-by-default; `Doc 04` retorna 53 de autonomy/approval/risk. Os canônicos realmente especificam o que o Windsurf mapeou como "já coberto".
  - **Conclusão (minha, como dona):** o veredito do Windsurf "promover nada estrutural" está **correto**. Vou **além dele**: recomendo **HOLD até nos 5 nomes de catálogo** (ver §3 e §7-Q6).
- **Confiei** (sem re-ler arquivo a arquivo) no inventário dos 2 Codex — alta confiança, estrutura espelha o DOC03, prova de uniformidade incluída em cada um. Spot-check de coerência: OK.

---

## 2. Consolidação cross-track (o valor desta auditoria)

Os 3 tracks (+ F1) tocam **as mesmas capacidades por superfícies diferentes**. Sem deduplicar, o Founder veria 31 itens; deduplicando, são **6 clusters**. Isto é o que evita re-promover o que o F1 já adjudicou.

| Cluster | Aparece como | Veredito de dedup |
|---|---|---|
| **A · Envelope de execução** | `S1` (skill I/O) + `T1` (transformer spec card) + `R1` (response typing, F1) | **1 decisão, não 3.** S1 e T1 carregam o **mesmo** envelope de qualidade `{confidence, risks/gaps, next_actions}`. `AQ-T09-2` é a semente. É o item mais forte da onda. |
| **B · ROI** | `S3c` roi-modeling (skill) + `T4` output_to_roi (transformer) + `P4` roi_policy (policy) | **1 conceito em 3 camadas.** O F1 já marcou ROI = **JÁ COBERTO (Doc 21)**. Promover 3 nomes ROI = re-promover o que o F1 fechou. **HOLD os 3.** |
| **C · Learning→memória** | `S3d` learning-extraction (skill) + `P2` learning_policy (policy) + `feedback_to_learning` (transformer, já recusado pelo Codex#2) | F1 **e** Codex#2 já marcaram learning→memória = **coberto (Doc 05)**. **HOLD/já-coberto.** |
| **D · Ingestão de contexto** | `S3b` context-engineering (skill) + `T5` answer_to_context (transformer) | Mesma superfície "→ context state", vista como skill vs transformer. Cai na pergunta-mãe de taxonomia. **HOLD atrás da AQ.** |
| **E · Intenção** | `S3a` intent-classification (skill) + `intent_to_briefing` (transformer, já recusado) + Intent Resolver (runtime, F1 passo 2) | A **capacidade já existe no runtime** (Intent Resolver, Doc 10). `S3a` é net-new só **como skill registrada**. Fronteira skill-vs-runtime = GATE 5. |
| **F · Fronteira skill/transformer/Work Order** | `AQ-S06-2`, `AQ-S06-3`, `AQ-T09-1` | Todas a **mesma** pergunta: "onde mora a capacidade X — skill / transformer / workflow / Work Order / tool?". **Colapsa em 1 AQ-mãe.** |

> **Achado central:** a nota `F1_RUNTIME_IO` **já pré-adjudicou** 4 desses clusters (ROI, learning, intent, context) como **JÁ COBERTO**. Boa parte do "net-new" dos catálogos da Onda 1 é, na verdade, **redundante com o que o F1 fechou**. Promover sem este cruzamento criaria duplicação.

---

## 3. A-PROMOVER — tabela única, deduplicada e ordenada

> Ordem = readiness × força × utilidade-F1 × risco. **Promoção = entra no patch candidate.**
> **Aplicação = sessão `canonical_patch` separada, pós-aprovação.** Nada aqui aplica nada.

| # | ID(s) | Item consolidado | Doc-alvo | Força | Canonical-readiness | **Recomendação** |
|---|---|---|---|---|---|---|
| **1** | **S1 + T1** (+R1 xref) | **Execution Envelope** — contrato I/O mínimo comum a skill e transformer com `{confidence, risks/gaps, next_actions}` | Doc 06 §5.3 + Doc 09 §5.5 | **ALTA** | **READY** como contrato documental (define forma, não "skill bonita") | **GO — 1º canonical_patch.** Condição: T1 entra **com** os campos que faltam (`validation`, `fallback`, `error_policy`, `idempotency`) como obrigatórios, não como conteúdo herdado do UPGRADE. |
| **2** | **S2** | Critério operacional de downstream (toda skill alimenta agente/tarefa/proposta/workflow/decisão) | Doc 06 §14/§15 | MÉDIA | **READY** (reforça critério de aprovação/reprovação; não infla catálogo) | **GO — junto do patch 1** (risco baixo, mesma superfície). |
| **3** | **T2** | `briefing_to_task` — transformer → task / Work Order candidate | Doc 09 §5.6 (+ xref Doc 27) | **ALTA** | Nome READY; **aplicação atada a `AQ-IO-1`** (thin-slice começa no user ou no project?) | **HOLD-GATE-5.** Promover o nome no candidate; aplicar só depois que o GATE 5 sequenciar Work Orders. |
| **4** | **S3a + S3b** | `intent-classification` + `context-engineering` (skills) | Doc 06 taxonomia | ALTA (nome) | **Sobrepõem o runtime** (Intent Resolver / Context Assembler, Doc 10 §5.2) | **HOLD-GATE-5.** Decidir fronteira skill-vs-runtime antes de registrar. |
| **5** | S3c + T4 + P4 | **ROI** (skill + transformer + policy do mesmo conceito) | Doc 06/09 + Doc 21 | MÉDIA→BAIXA | F1 já marcou ROI = **JÁ COBERTO (Doc 21)** | **HOLD.** 1 decisão de ROI, não 3 nomes. |
| **6** | S3d + P2 | learning-extraction + learning_policy | Doc 06 + Doc 05 | MÉDIA→BAIXA | F1+Codex#2 = **coberto (Doc 05)** | **HOLD / já-coberto.** |
| **7** | T3, T5, S3e–S3h | project_pack, answer_to_context, deep-research, apify, visual-briefing, reels | catálogo F2 (Doc 06/09) | BAIXA-MÉDIA | Especializações; **falham Doc 06 §1** como specs (sem owner/tools/eval) | **HOLD.** Backlog de catálogo F2 atrás da AQ de taxonomia (cluster F). |
| **—** | **P1, P3, P5** (+ P2/P4 acima) | cost / quality / source / learning / roi **policy** | — | BAIXA | **Boilerplate verificado na fonte; canônico muito mais rico; viola §1** | **NÃO PROMOVER.** Nenhum dos 5 nomes. O entregável do TR-POLICY é a AQ, não promoção. |

**Resumo numérico:** de ~31 itens crus → **2 GO agora (S1+T1, S2)** · **2 clusters HOLD-GATE-5 (T2; S3a/S3b)** · **3 clusters HOLD-taxonomia/já-coberto (ROI, learning, catálogo F2)** · **0 policies**.

---

## 4. ARCHITECTURE_QUESTIONS agregadas (não decidir aqui)

As 13 AQs dos 3 tracks + as 5 do F1 **convergem para 3 perguntas-mãe**. Agrego sem decidir.

### 4a. As 3 perguntas-mãe (o que realmente trava)

| AQ-mãe | Engloba | Pergunta para Founder + Metacognik |
|---|---|---|
| **AQ-W1-TAXONOMIA** | AQ-S06-2, AQ-S06-3, AQ-T09-1, AQ-IO-5, cluster D/E/F | **Onde mora cada capacidade?** Skill (Doc 06) vs transformer (Doc 09) vs workflow (Doc 07) vs Work Order (Doc 27) vs tool/connector (Doc 26) vs runtime (Doc 10). Micro-skills viram entradas próprias, aliases/subskills, ou só camada F2? |
| **AQ-W1-ENVELOPE** | AQ-S06-1, AQ-T09-2, AQ-T09-4, AQ-IO-5 | **Existe UM envelope de I/O canônico** `{confidence, risks/gaps, next_actions}` obrigatório para toda unidade executável (skill, transformer, Agent Run)? E `validation/error_policy/fallback/idempotency` viram campos obrigatórios do registry antes de aprovar novos? |
| **AQ-W1-CAMADA-POLICY** | AQ-P12-1, AQ-P12-2, AQ-P12-3, AQ-P12-4 | **Fronteira de policy:** security/runtime (Doc 12) vs comportamento/cognição (Doc 04). E as 5 policies não-canônicas (cost/learning/quality/roi/source) pertencem a Doc 24/05/20/21/18 — não a Doc 12/04. Catálogo de nomes-sem-regra tem valor, ou é ruído? |

### 4b. AQs que sobem direto para o GATE 5 (não se resolvem na Onda 1)

| AQ | Origem | Por que é GATE 5 |
|---|---|---|
| **AQ-IO-1** | F1 | *O thin-slice começa no `user`+1ª intenção ou no `project`?* Sequencia `T2 briefing_to_task` e tudo do F1. **Já é o entregável central do pacote do GATE 5.** |
| **AQ-IO-2/3/4** | F1 | User=objeto vs Stakeholder; memória `user_id`; tribo=objeto/score/projeção. Refina o runtime que o GATE 5 fixa. |
| **AQ-T09-3 / cluster B,C,E** | TR-TRANSF + F1 | Centralizar nomes (intent/context/ROI/learning) no Doc 09 vs cross-ref Doc 10/05/21 — depende do runtime do GATE 5. |

> **Leitura:** as AQs originais não desaparecem (rastreáveis acima); apenas mostro que **3 decisões-mãe + o GATE 5** resolvem todas. O Founder não precisa responder 18 perguntas — precisa responder 3 + sequenciar o GATE 5.

---

## 5. Pronto para canonical_patch  ×  espera GATE 5

| Estado | Itens | Justificativa |
|---|---|---|
| **PRONTO (F0, 1º patch pós-aprovação)** | **S1 + T1** (Execution Envelope, com gaps de T1) · **S2** (critério downstream) | São **contratos documentais** em Doc 06/09. Não ligam a espinha do runtime ainda; não dependem do GATE 5. Passam o teste do §1 (definem forma + critério, não "nome bonito"). |
| **HOLD-GATE-5** | **T2** (Work Order / `AQ-IO-1`) · **S3a/S3b** (skill-vs-runtime) · clusters **B/C/E** (ROI/learning/intent/context ligam Doc 10/05/21) · **tudo do F1 (U1-U5, R1-R5)** | A *aplicação* liga ao runtime cuja espinha o GATE 5 ainda vai fixar. Aplicar antes = over-engineering (mesmo padrão do schema RAG do Doc 11). Confirmado pelo Founder 2026-06-03: "GATE 5 primeiro". |
| **HOLD-TAXONOMIA** | catálogo F2 (#7) | Espera `AQ-W1-TAXONOMIA`. |
| **NÃO PROMOVER** | 11 policies UPGRADE/07 · 11 skills/transformers "já coberto" | Boilerplate (verificado) ou duplicata de canônico existente. Caminho = arquivar UPGRADE pós-aprovação, não promover. |

> **Correção honesta ao dispatch (§ Onda 1 "zero GATE-5-blocked"):** verdadeiro para **produzir** os candidates (análise F0). **Não** totalmente verdadeiro para **aplicar** — `T2`, `S3a/S3b` e os clusters B/C/E estão **atados ao GATE 5 na aplicação**. Os candidates são F0; um subconjunto das *aplicações* é GATE-5-sequenciado. Não muda o que rodou; muda a ordem do que se aplica.

---

## 6. Recomendação para o Founder (go/hold por item)

**Sequência ótima de canonical_patch (quando você aprovar):**

1. **PATCH 1 — Execution Envelope (S1 + T1 + S2).** Uma sessão `canonical_patch`, escopo = Doc 06 + Doc 09. Resolve **AQ-W1-ENVELOPE** primeiro (é pré-requisito de tudo que tem I/O). Inclui os campos faltantes de T1 como obrigatórios. **Esta é a única coisa que vale aplicar antes do GATE 5.**
2. **DECISÃO — AQ-W1-TAXONOMIA + AQ-W1-CAMADA-POLICY.** Não é patch, é decisão sua + Metacognik. Destrava #7 (catálogo) e fecha o TR-POLICY (arquivar UPGRADE/07).
3. **GATE 5** (caminho crítico, já em andamento). Inclua **AQ-IO-1** no pacote. Só depois: PATCH 2 sequencia `T2`, `S3a/S3b` e os clusters de runtime — **junto** com o patch do F1 (U/R), porque tocam os mesmos docs (Doc 02/05/03/04/10).
4. **TR-POLICY:** **go = arquivar, não promover.** `git mv 000_UPGRADE/07_POLICIES/ → 99_ARCHIVE/...` + README-pointer, **só após** a decisão de AQ-W1-CAMADA-POLICY confirmar que os 5 conceitos já têm casa (Doc 24/05/20/21/18). Nunca deletar.

**Go/hold compacto:** `GO`→ S1, T1, S2. `HOLD-GATE-5`→ T2, S3a, S3b, clusters B/C/E. `HOLD-DECISÃO`→ catálogo F2 (#7). `NÃO`→ 11 policies + 11 já-coberto.

---

## 7. Respostas às perguntas do PMO (seção B do dispatch)

1. **Dedup cross-track?** Sim — 6 clusters (§2). ROI/learning/context/intent aparecem em 2-3 tracks **e** já estão fechados no F1. Consolidados.
2. **Anti-bloat?** Sim, recusado e citado: as 5 policies do Windsurf são **boilerplate byte-idêntico** (li a fonte); vários nomes de catálogo skill/transformer são especializações sem spec. Promovê-los inflaria o Doc 06/09.
3. **Constituição?** Os nomes de catálogo (S3a-h, P1-P5, T2-T5) criam "**nome bonito sem skill/teste**" (§1 Doc 03/06) se entrarem como entradas canônicas — sinalizado, viram backlog atrás de AQ. **S1/T1/S2 não** violam: definem forma/critério, não fingem skill.
4. **GATE 5?** Sim — `T2`, `S3a/S3b`, clusters B/C/E são **hold-GATE-5 na aplicação** (§5). Os candidates em si são F0.
5. **Ordem pro Founder?** Envelope (S1+T1+S2) → 2 decisões-mãe → GATE 5 (com AQ-IO-1) → patch de runtime + F1 juntos → arquivar Policies. (§6)
6. **Windsurf re-verificado?** Sim, na fonte (`000_UPGRADE/07_POLICIES/` + grep Doc 12/04). Veredito "promover nada estrutural" = **correto**. Vou além: **HOLD até nos 5 nomes** — boilerplate verificado, cada conceito já tem casa canônica provável, e nome-sem-regra fura o §1. O produto do TR-POLICY é a `AQ-W1-CAMADA-POLICY`, não promoção. **Julgamento de Policies assumido por mim, não pelo Windsurf.**

---

## 8. BRA Packet

```yaml
bra_id: BRA-AUDIT-20260604-01
from_session: S-P1-L3-CLAUDE2-20260604-001
to: PMO/Dispatcher + Founder
context_summary:
  - "Lidos os 3 candidates (Doc 06/09/12) + F1_RUNTIME_IO; precondição (3 releases) confirmada no registry."
  - "Re-verifiquei Windsurf na fonte: UPGRADE/07 é boilerplate byte-idêntico; canônico Doc 12/04 cobre de verdade."
  - "31 itens crus colapsam em 6 clusters; F1 já pré-adjudicou ROI/learning/intent/context como já-coberto."
outputs:
  - "WAVE1_FANIN_AUDIT_FOR_FOUNDER.md (esta nota): veredito, tabela ordenada, AQs agregadas, readiness, go/hold."
open_questions:
  - "AQ-W1-TAXONOMIA: onde mora cada capacidade (skill/transformer/workflow/Work Order/tool/runtime)?"
  - "AQ-W1-ENVELOPE: UM envelope I/O canônico obrigatório + campos de robustez no registry?"
  - "AQ-W1-CAMADA-POLICY: fronteira Doc 12 vs Doc 04; 5 policies pertencem a Doc 24/05/20/21/18; catálogo-sem-regra tem valor?"
  - "AQ-IO-1 (sobe pro GATE 5): thin-slice começa no user ou no project?"
blockers:
  - "Nenhum para a auditoria. Go/hold por item depende de decisão do Founder."
  - "PATCH 2 (runtime + F1) depende do GATE 5."
risk_flags:
  - "Bloat de catálogo se 20+ nomes forem promovidos sem owner/tool/eval (viola §1)."
  - "Duplicação se ROI/learning/intent/context forem promovidos apesar de o F1 já tê-los fechado."
recommended_next:
  - "Founder: aprovar PATCH 1 (Execution Envelope S1+T1+S2) — único F0 aplicável antes do GATE 5."
  - "Founder + Metacognik: decidir as 2 AQs-mãe (taxonomia, camada-policy)."
  - "Incluir AQ-IO-1 no GATE5_FOUNDER_DECISION_PACKAGE.md; sequenciar PATCH 2 pós-GATE 5."
  - "TR-POLICY: arquivar UPGRADE/07 (não promover) após confirmar casas canônicas."
```

---

## 9. CHECKOUT RELEASE

```txt
CHECKOUT RELEASE — S-P1-L3-CLAUDE2-20260604-001
files_created: 000_ROADMAPS/22_CONSOLIDATION/L3_WAVE1/WAVE1_FANIN_AUDIT_FOR_FOUNDER.md
files_changed: 000_ROADMAPS/SESSION_REGISTRY.md (1 sessão + 1 lock)
files_not_touched: os 3 candidates Doc 06/09/12 (RO); F1_RUNTIME_IO (RO); canônico Doc 06/09/12/04 (RO);
  000_UPGRADE/04|07|08 (RO, só leitura de verificação); docs 01-28; docs 29-34;
  ARCHITECTURE_PATCH_REPORT.md; 00_SYSTEM_GOVERNANCE/*; CKOS_EXPANSION_KANBAN.md
validation: nada aplicado em canônico; síntese ordenada + dedup de 6 clusters + AQs agregadas (3 mães)
  + readiness por item + go/hold; Windsurf re-verificado na fonte (boilerplate confirmado, cobertura confirmada)
risks_remaining: bloat de catálogo; duplicação cross-track com F1; aplicação de T2/S3a/S3b/clusters atada ao GATE 5
next_step: Founder decide go/hold por item → PATCH 1 (Execution Envelope) é o único F0 aplicável já;
  resto sequenciado pós-GATE 5 / pós-decisão de taxonomia
status: released
```
