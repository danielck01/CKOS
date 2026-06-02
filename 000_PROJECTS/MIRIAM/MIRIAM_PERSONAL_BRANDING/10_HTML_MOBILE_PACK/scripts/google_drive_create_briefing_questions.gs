const TARGET_FOLDER_ID = "COLE_AQUI_O_ID_DA_PASTA_GOOGLE_DRIVE";

const QUESTIONS = [
  {
    id: "objetivo_90_dias",
    category: "intent",
    question: "Qual e o objetivo primario de Miriam nos proximos 90 dias?",
    whyNow: "Define se o sistema prioriza autoridade, captacao, parceria, educacao ou reposicionamento."
  },
  {
    id: "oab_status",
    category: "legal",
    question: "Qual e a situacao da inscricao na OAB e a seccional?",
    whyNow: "Sem isso, a linguagem publica e a bio ficam bloqueadas."
  },
  {
    id: "perfil_atual",
    category: "trust_architecture",
    question: "O perfil atual e pessoal, profissional ou misto?",
    whyNow: "Ajuda a decidir perfil novo, rebranding ou arquitetura hibrida."
  },
  {
    id: "arquitetura_perfil",
    category: "decision",
    question: "Qual arquitetura parece mais segura para testar?",
    whyNow: "Separa confianca, algoritmo e reputacao antes de escolher nome/bio."
  },
  {
    id: "area_penal",
    category: "domain",
    question: "Quais territorios penais Miriam quer validar primeiro?",
    whyNow: "Evita conteudo generico e reduz risco de temas sensiveis cedo demais."
  },
  {
    id: "exposicao",
    category: "format",
    question: "Qual nivel de exposicao Miriam sustenta com seguranca?",
    whyNow: "Define se a experiencia visual deve favorecer video, carrossel, texto ou bastidores."
  },
  {
    id: "prova_autoridade",
    category: "evidence",
    question: "Quais provas reais de autoridade podem ser usadas sem inflar curriculo?",
    whyNow: "Impede autoridade artificial e fortalece confianca cognitiva."
  },
  {
    id: "limites_publicos",
    category: "ethics",
    question: "Quais temas ou formatos estao proibidos publicamente?",
    whyNow: "Define limites antes de qualquer pauta ou prompt visual."
  },
  {
    id: "qa_revisor",
    category: "approval",
    question: "Quem revisa conteudos sensiveis antes da publicacao?",
    whyNow: "Conteudo juridico publico precisa de gate humano quando houver risco."
  },
  {
    id: "roi_metric",
    category: "roi",
    question: "Qual metrica de ROI importa sem prometer clientes?",
    whyNow: "Mede progresso por confianca, clareza e aprendizado, nao por promessa comercial."
  }
];

function createMiriamBriefingFiles() {
  const folder = DriveApp.getFolderById(TARGET_FOLDER_ID);

  const doc = DocumentApp.create("CKOS - Briefing Vivo Miriam - Perguntas");
  const body = doc.getBody();
  body.appendParagraph("CKOS - Briefing Vivo Miriam").setHeading(DocumentApp.ParagraphHeading.TITLE);
  body.appendParagraph("Status: simulation_only | Requires: Founder + PMO + Metacognik approval");
  body.appendParagraph("Regra: uma pergunta necessaria por rodada; sem estrategia final nesta etapa.");

  QUESTIONS.forEach((item, index) => {
    body.appendParagraph(`${index + 1}. ${item.question}`).setHeading(DocumentApp.ParagraphHeading.HEADING2);
    body.appendParagraph(`Categoria: ${item.category}`);
    body.appendParagraph(`Por que agora: ${item.whyNow}`);
    body.appendParagraph("Resposta: ");
    body.appendParagraph("Classificacao: fato | hipotese | ponto a validar | decisao | risco | gate");
  });

  doc.saveAndClose();
  const docFile = DriveApp.getFileById(doc.getId());
  folder.addFile(docFile);
  DriveApp.getRootFolder().removeFile(docFile);

  const sheet = SpreadsheetApp.create("CKOS - Briefing Vivo Miriam - Response Memory");
  const tab = sheet.getActiveSheet();
  tab.setName("Response Memory");
  tab.appendRow([
    "question_id",
    "category",
    "question",
    "why_now",
    "answer",
    "classification",
    "approval_status",
    "notes"
  ]);

  QUESTIONS.forEach((item) => {
    tab.appendRow([
      item.id,
      item.category,
      item.question,
      item.whyNow,
      "",
      "",
      "pending",
      ""
    ]);
  });

  tab.autoResizeColumns(1, 8);

  const sheetFile = DriveApp.getFileById(sheet.getId());
  folder.addFile(sheetFile);
  DriveApp.getRootFolder().removeFile(sheetFile);

  Logger.log(`Doc criado: ${doc.getUrl()}`);
  Logger.log(`Sheet criada: ${sheet.getUrl()}`);
}
