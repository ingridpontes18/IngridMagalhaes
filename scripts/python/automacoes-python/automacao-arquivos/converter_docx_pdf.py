"""
Conversão simples de arquivos DOCX para PDF
"""

from docx2pdf import convert
import os

PASTA_DOCX = "docx"
PASTA_PDF = "pdf"

def converter():
    os.makedirs(PASTA_PDF, exist_ok=True)

    for arquivo in os.listdir(PASTA_DOCX):
        if arquivo.endswith(".docx"):
            convert(
                os.path.join(PASTA_DOCX, arquivo),
                os.path.join(PASTA_PDF, arquivo.replace(".docx", ".pdf"))
            )

    print("Conversão concluída.")

if __name__ == "__main__":
    converter()
