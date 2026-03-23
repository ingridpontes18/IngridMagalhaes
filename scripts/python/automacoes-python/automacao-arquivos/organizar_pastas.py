"""
Organiza arquivos por extensão em subpastas
"""

import os
import shutil

PASTA_BASE = "arquivos"

def organizar():
    for arquivo in os.listdir(PASTA_BASE):
        caminho = os.path.join(PASTA_BASE, arquivo)

        if os.path.isfile(caminho):
            ext = arquivo.split(".")[-1]
            pasta_ext = os.path.join(PASTA_BASE, ext)

            os.makedirs(pasta_ext, exist_ok=True)
            shutil.move(caminho, os.path.join(pasta_ext, arquivo))

    print("Arquivos organizados.")

if __name__ == "__main__":
    organizar()
