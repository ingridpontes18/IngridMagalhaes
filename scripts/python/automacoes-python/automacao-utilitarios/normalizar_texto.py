"""
Normalização de textos para uso em bases de dados.
"""

import unicodedata
import re

def normalizar_texto(texto: str) -> str:
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    texto = re.sub(r"[^a-z0-9\s]", "", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


if __name__ == "__main__":
    exemplos = [
        "São Paulo - SP",
        "Relatório Técnico Nº 123",
        " Automação & Dados! "
    ]

    for e in exemplos:
        print(e, "→", normalizar_texto(e))
