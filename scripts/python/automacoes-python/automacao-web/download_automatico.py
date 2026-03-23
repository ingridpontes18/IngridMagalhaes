"""
Download automático de arquivos a partir de uma URL
"""

import requests
from pathlib import Path

URL = "https://example.com/arquivo.pdf"
PASTA_SAIDA = Path("downloads")
ARQUIVO_SAIDA = PASTA_SAIDA / "arquivo.pdf"


def baixar():
    PASTA_SAIDA.mkdir(exist_ok=True)

    r = requests.get(URL, timeout=30)
    r.raise_for_status()

    with open(ARQUIVO_SAIDA, "wb") as f:
        f.write(r.content)

    print(f"Download finalizado: {ARQUIVO_SAIDA.resolve()}")


if __name__ == "__main__":
    baixar()
