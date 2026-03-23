"""
Limpeza e padronização de dados em planilhas Excel
"""

import pandas as pd

ARQUIVO_ENTRADA = "entrada.xlsx"
ARQUIVO_SAIDA = "dados_limpos.xlsx"

def limpar_dados():
    df = pd.read_excel(ARQUIVO_ENTRADA)

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df = df.drop_duplicates()
    df = df.fillna("Não informado")

    df.to_excel(ARQUIVO_SAIDA, index=False)
    print("Limpeza concluída.")

if __name__ == "__main__":
    limpar_dados()
