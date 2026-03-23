# Conversão Inteligente de PDFs para Excel

Este projeto foi desenvolvido para extrair informações de documentos PDF extensos
(centenas de páginas) e gerar arquivos Excel estruturados, mantendo fielmente os
dados originais, sem perda de formatação ou erros de reconhecimento.

---

## O problema real

Conversores tradicionais de PDF para Word ou Excel frequentemente:

- Desconfiguram tabelas
- Perdem colunas e alinhamento
- Geram erros de leitura em documentos longos
- Exigem correção manual extensa

Este projeto resolve exatamente esse problema ao realizar a extração de forma controlada e estruturada.

---

## A solução

A solução utiliza uma pipeline modular composta por:

1. Leitura controlada do PDF
2. Extração precisa do conteúdo textual
3. Parser personalizado para identificar campos relevantes
4. Exportação estruturada para Excel

---

## Arquitetura do projeto

- **pdf_reader.py** → leitura do conteúdo do PDF  
- **parser.py** → interpretação e organização dos dados  
- **exporter.py** → geração do arquivo Excel final  
- **main.py** → orquestra todo o processo  

---

## Como executar

```bash
python main.py
