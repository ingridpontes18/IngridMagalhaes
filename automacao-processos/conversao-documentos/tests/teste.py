"""
Testes básicos da pipeline de conversão de documentos.

Este script valida:
- Leitura do PDF
- Processamento dos dados
- Exportação final
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from src.pdf_reader import ler_pdf
from src.parser import processar_dados
from src.exporter import exportar_excel

def teste_pipeline():
    print("🔍 Iniciando teste da pipeline...\n")

    # Simula leitura
    linhas = ler_pdf("exemplo.pdf")
    print("📄 Leitura concluída:", linhas)

    # Processamento
    dados = processar_dados(linhas)
    print("🧠 Dados processados:", dados)

    # Exportação
    exportar_excel(dados, "teste_saida.xlsx")
    print("📊 Exportação concluída.\n")

    print("✅ Pipeline testada com sucesso!")


if __name__ == "__main__":
    teste_pipeline()