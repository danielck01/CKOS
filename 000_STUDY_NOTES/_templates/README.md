# _templates

## Funcao da pasta

Guardar templates oficiais da camada STUDY.

## O que pode entrar

Templates Markdown para RAW upload notes, study notes, source manifests, patch candidates e decision logs.

## O que nao pode entrar

Notas preenchidas, docs canonicos ou alteracoes no template canonico de governanca.

## Naming obrigatorio

`TYPE_TEMPLATE.md`

## Regra de saida

Copiar o template para a pasta de destino e preencher YAML.

## Quando mover para CANONICAL

Nunca. Templates locais podem embasar patch futuro em `00_DOCUMENT_TEMPLATE.md`, mas nao alteram canonicamente nada.

## Quando arquivar

Quando template for substituido por versao aprovada.

## Risco principal

Divergir do padrao canonico sem registrar patch.

## Politica de PII

Templates nao devem conter dados reais.

## Politica de provenance

Templates devem manter campos de source e provenance.

