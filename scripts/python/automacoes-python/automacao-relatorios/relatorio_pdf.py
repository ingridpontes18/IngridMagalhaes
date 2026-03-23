"""
Geração automática de relatório em PDF.
Projeto demonstrativo para automação de relatórios.
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def gerar_relatorio(texto: str, saida: str = "relatorio.pdf") -> None:
    """
    Gera um relatório simples em PDF a partir de um texto.
    """

    c = canvas.Canvas(saida, pagesize=A4)
    largura, altura = A4

    margem_x = 40
    margem_y = 50
    y = altura - margem_y

    for linha in texto.strip().split("\n"):
        c.drawString(margem_x, y, linha)
        y -= 18

        if y < margem_y:
            c.showPage()
            y = altura - margem_y

    c.save()


if __name__ == "__main__":
    conteudo = (
        "Relatório Automatizado\n"
        "----------------------\n"
        "Este documento foi gerado automaticamente\n"
        "a partir de dados estruturados.\n\n"
        "Objetivo:\n"
        "- Demonstrar geração de PDF via Python\n"
        "- Automatizar relatórios simples"
    )

    gerar_relatorio(conteudo)
