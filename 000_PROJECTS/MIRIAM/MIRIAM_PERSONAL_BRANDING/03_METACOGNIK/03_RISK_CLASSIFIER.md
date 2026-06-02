# Metacognik - Risk Classifier

Status: active_policy

## Funcao

Classificar riscos antes de cada artefato.

## Classes

| Classe | Descricao | Exemplo |
| --- | --- | --- |
| Legal/OAB | Publicidade juridica e etica profissional | Promessa de resultado |
| Reputacional | Percepcao publica e profissional | Influencerizacao vazia |
| Plataforma | Algoritmo, distribuicao e sinais sociais | Comentarios superficiais |
| Genero/exposicao | Presenca feminina em tema sensivel | Assedio, julgamento moral, sexualizacao |
| Comercial | Captacao indevida ou expectativa falsa | Chamada agressiva |
| Documental | Decisao sem fonte ou sem log | Estrategia sem evidence map |

## Nivel padrao do projeto

```yaml
default_risk_level: high
reason: "Direito penal + publicidade juridica + redes sociais + advogada recem-formada"
```
