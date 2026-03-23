"""
Responsável por exportar dados para Excel.
"""

import pandas as pd


def exportar_excel(dados, saida="saida.xlsx"):
    df = pd.DataFrame(dados)
    df.to_excel(saida, index=False)
    print(f"Arquivo gerado: {saida}")