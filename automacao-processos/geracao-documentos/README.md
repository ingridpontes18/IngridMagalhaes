# Geração Automatizada de Documentos Técnicos

Este projeto automatiza a geração de documentos técnicos (Word e PDF)
a partir de dados estruturados em planilhas Excel, reduzindo trabalho manual
e garantindo padronização em larga escala.

O problema
Em cenários com grande volume de documentos, a criação manual de arquivos:
- Consome muito tempo
- Está sujeita a erros
- Dificulta padronização
- Não escala bem

A Solução
A solução implementada permite:

- Modelar os dados em planilhas Excel
- Gerar documentos individuais ou em lote
- Exportar para Word e PDF
- Selecionar documentos específicos para geração ou impressão
- Utilizar uma interface simples para operação

Arquitetura do Projeto 
- painel.py → interface para seleção e controle das operações
- gerar_parecer.py → geração de documentos individuais
- gerar_todos.py → geração em lote

Interface
O projeto inclui um painel que permite:

- Gerar um ou mais documentos específicos
- Gerar todos os documentos de uma vez
- Exportar em Word ou PDF
- Imprimir documentos selecionados ou em lote

Distribuição
Para facilitar o uso por usuários não técnicos, o sistema pode ser distribuído
como um executável (.exe), sem necessidade de acesso ao código-fonte.


