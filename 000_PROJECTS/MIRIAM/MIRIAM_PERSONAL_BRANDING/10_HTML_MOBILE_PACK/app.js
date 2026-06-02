const questions = [
  {
    id: "objetivo_90_dias",
    stage: "Intent",
    question: "Qual e o objetivo primario de Miriam nos proximos 90 dias?",
    why: "Define se o sistema prioriza autoridade, captacao, parceria, educacao ou reposicionamento.",
    options: ["Autoridade", "Primeiros clientes", "Parceria/escritorio", "Educacao", "Reposicionamento"]
  },
  {
    id: "oab_status",
    stage: "Legal",
    question: "Qual e a situacao da inscricao na OAB e a seccional?",
    why: "Sem isso, a linguagem publica e a bio ficam bloqueadas.",
    options: ["Ativa", "Pendente", "Nao informar agora"]
  },
  {
    id: "perfil_atual",
    stage: "Trust architecture",
    question: "O perfil atual e pessoal, profissional ou misto?",
    why: "Ajuda a decidir perfil novo, rebranding ou arquitetura hibrida.",
    options: ["Pessoal", "Misto", "Profissional", "Sem perfil"]
  },
  {
    id: "arquitetura_perfil",
    stage: "Decision",
    question: "Qual arquitetura parece mais segura para testar?",
    why: "Separa confianca, algoritmo e reputacao antes de escolher nome/bio.",
    options: ["Perfil novo", "Rebranding", "Hibrido", "Ainda nao sei"]
  },
  {
    id: "area_penal",
    stage: "Domain",
    question: "Quais territorios penais Miriam quer validar primeiro?",
    why: "Evita conteudo generico e reduz risco de temas sensiveis cedo demais.",
    options: ["Processo penal", "Audiencia de custodia", "Juri", "Garantias", "Atualidades"]
  },
  {
    id: "exposicao",
    stage: "Format",
    question: "Qual nivel de exposicao Miriam sustenta com seguranca?",
    why: "Define se a experiencia visual deve favorecer video, carrossel, texto ou bastidores.",
    options: ["Baixa", "Media", "Alta", "A validar"]
  },
  {
    id: "prova_autoridade",
    stage: "Evidence",
    question: "Quais provas reais de autoridade podem ser usadas sem inflar curriculo?",
    why: "Impede autoridade artificial e fortalece confianca cognitiva.",
    options: ["Cursos", "Artigos", "Estagio", "Eventos", "Rotina de estudo"]
  },
  {
    id: "limites_publicos",
    stage: "Ethics",
    question: "Quais temas ou formatos estao proibidos publicamente?",
    why: "Define limites antes de qualquer pauta ou prompt visual.",
    options: ["Casos reais", "Crime midiatico", "Stories pessoais", "Opiniao forte", "Ainda mapear"]
  },
  {
    id: "qa_revisor",
    stage: "Approval",
    question: "Quem revisa conteudos sensiveis antes da publicacao?",
    why: "Conteudo juridico publico precisa de gate humano quando houver risco.",
    options: ["Miriam", "Mentor juridico", "Founder/PMO", "Sem revisor ainda"]
  },
  {
    id: "roi_metric",
    stage: "ROI",
    question: "Qual metrica de ROI importa sem prometer clientes?",
    why: "Mede progresso por confianca, clareza e aprendizado, nao por promessa comercial.",
    options: ["Perguntas qualificadas", "Saves", "DMs educativas", "Convites", "Clareza de perfil"]
  }
];

const artifacts = {
  evidence: {
    title: "Source Evidence Map",
    body: "Conecta Deep Research, OAB, algoritmo, notas do pack e respostas de Miriam. Classifica cada item como fato, hipotese, risco ou decisao possivel."
  },
  risk: {
    title: "Matriz de Risco Etico",
    body: "Classifica publicidade juridica, promessa implicita, sensacionalismo penal, exposicao feminina, autoridade artificial e risco de plataforma."
  },
  briefing: {
    title: "Response Memory",
    body: "Registra cada resposta real: pergunta, resposta bruta, classificacao, impacto, artifact destravado e proxima pergunta."
  },
  pmo: {
    title: "PMO Audit",
    body: "Audita escopo, custo, duplicidade, ordem correta, fontes, bloqueios e aprovacao humana antes de qualquer saida final."
  }
};

const state = {
  answers: JSON.parse(localStorage.getItem("ckos_miriam_answers") || "{}"),
  lastIntent: localStorage.getItem("ckos_miriam_intent") || ""
};

function saveState() {
  localStorage.setItem("ckos_miriam_answers", JSON.stringify(state.answers));
  const input = document.getElementById("intentInput");
  if (input) localStorage.setItem("ckos_miriam_intent", input.value);
}

function renderQuestions() {
  const stack = document.getElementById("questionStack");
  stack.innerHTML = "";

  questions.forEach((item) => {
    const card = document.createElement("article");
    card.className = "question-card";

    const selected = state.answers[item.id];
    card.innerHTML = `
      <p class="eyebrow">${item.stage}</p>
      <h3>${item.question}</h3>
      <p>${item.why}</p>
      <div class="options"></div>
    `;

    const options = card.querySelector(".options");
    item.options.forEach((option) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = `option${selected === option ? " selected" : ""}`;
      button.textContent = option;
      button.addEventListener("click", () => {
        state.answers[item.id] = option;
        saveState();
        renderQuestions();
        updateProgress();
      });
      options.appendChild(button);
    });

    stack.appendChild(card);
  });
}

function updateProgress() {
  const answered = Object.keys(state.answers).length;
  const total = questions.length;
  const percent = Math.round((answered / total) * 100);
  document.getElementById("progressText").textContent = `${answered} de ${total} respostas`;
  document.getElementById("progressBar").style.width = `${percent}%`;
  document.getElementById("roiMeter").style.width = `${Math.max(12, percent)}%`;
  document.getElementById("stageLabel").textContent = answered >= 7 ? "Ready for PMO" : "Pre-strategy";

  const next = questions.find((question) => !state.answers[question.id]);
  document.getElementById("nextQuestion").textContent = next
    ? next.question
    : "Briefing inicial completo. Proxima acao: SOURCE_EVIDENCE_MAP.md + MATRIZ_DE_RISCOS_ETICOS.md.";
}

function renderArtifact(key) {
  const preview = document.getElementById("artifactPreview");
  const artifact = artifacts[key] || artifacts.evidence;
  preview.innerHTML = `<strong>${artifact.title}</strong>${artifact.body}`;
  document.querySelectorAll(".artifact-card").forEach((button) => {
    button.classList.toggle("active", button.dataset.artifact === key);
  });
}

function hydrateImages() {
  const map = window.CKOS_CDN_IMAGES || {};
  document.querySelectorAll(".visual-slot").forEach((slot) => {
    const url = map[slot.dataset.slot];
    if (!url) return;
    slot.style.backgroundImage = `linear-gradient(180deg, rgba(0,0,0,.08), rgba(0,0,0,.56)), url("${url}")`;
    slot.classList.add("has-image");
  });
}

function exportSummary() {
  const lines = [
    "CKOS BRIEFING VIVO - MIRIAM",
    "",
    `Intent: ${document.getElementById("intentInput").value}`,
    "Risk: high",
    "Policy: CKOS-LEGAL-ADV-001",
    "Blocked: posicionamento final, tom final, bio, calendario, HTML final",
    "",
    "Answers:"
  ];

  questions.forEach((question) => {
    lines.push(`- ${question.question}`);
    lines.push(`  resposta: ${state.answers[question.id] || "pendente"}`);
  });

  lines.push("");
  lines.push("Next safe action: criar SOURCE_EVIDENCE_MAP.md + MATRIZ_DE_RISCOS_ETICOS.md apos respostas reais.");
  document.getElementById("summaryOutput").textContent = lines.join("\n");
}

function simulateIntent() {
  saveState();
  const output = document.getElementById("summaryOutput");
  output.textContent = [
    "CEO_AGENT_INTERPRETATION",
    "",
    "Intent detected: personal branding juridico para advogada penal recem-formada.",
    "Project type: personal_branding_legal",
    "Risk level: high",
    "Needs PMO audit: yes",
    "Founder approval needed: yes",
    "Suggested output: analysis_doc + evidence_map + ethical_risk_matrix",
    "",
    "Next question:",
    document.getElementById("nextQuestion").textContent
  ].join("\n");
}

document.addEventListener("DOMContentLoaded", () => {
  if (state.lastIntent) document.getElementById("intentInput").value = state.lastIntent;
  renderQuestions();
  updateProgress();
  renderArtifact("evidence");
  hydrateImages();

  document.querySelectorAll(".artifact-card").forEach((button) => {
    button.addEventListener("click", () => renderArtifact(button.dataset.artifact));
  });
  document.getElementById("exportSummary").addEventListener("click", exportSummary);
  document.getElementById("runIntent").addEventListener("click", simulateIntent);
});
