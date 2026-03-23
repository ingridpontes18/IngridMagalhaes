"""
Renomeia arquivos PDF com base em padrão sequencial
"""

import os
PASTA_PDFS = "pdfs"

def renomear():
    # lista apenas PDFs e ordena para comportamento determinístico
    pdfs = sorted([f for f in os.listdir(PASTA_PDFS) if f.lower().endswith(".pdf")])
    for i, arquivo in enumerate(pdfs, start=1):
        novo_nome = f"documento_{i:03}.pdf"
        src = os.path.join(PASTA_PDFS, arquivo)
        dst = os.path.join(PASTA_PDFS, novo_nome)
        if os.path.abspath(src) == os.path.abspath(dst):
            continue  # já está com o nome desejado
        try:
            # os.replace substitui de forma portátil (Windows e POSIX)
            os.replace(src, dst)
        except Exception as e:
            print(f"Erro ao renomear {arquivo}: {e}")

    print("Renomeação concluída.")

if __name__ == "__main__":
    renomear()
