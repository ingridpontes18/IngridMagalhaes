"""
Geração automática de relatório resumido em Excel
"""

import pandas as pd

ARQUIVO_ENTRADA = "dados.xlsx"
ARQUIVO_SAIDA = "relatorio.xlsx"

def gerar_relatorio():
    df = pd.read_excel(ARQUIVO_ENTRADA)

    resumo = df.groupby("categoria").size().reset_index(name="quantidade")

    resumo.to_excel(ARQUIVO_SAIDA, index=False)
    print("Relatório gerado.")

if __name__ == "__main__":
    gerar_relatorio()
