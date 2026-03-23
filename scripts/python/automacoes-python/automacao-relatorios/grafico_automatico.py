"""
Geração automática de gráficos a partir de dados estruturados.
"""

import pandas as pd
import matplotlib.pyplot as plt

def gerar_grafico(caminho_excel: str, coluna_x: str, coluna_y: str):
    df = pd.read_excel(caminho_excel)

    if coluna_x not in df.columns or coluna_y not in df.columns:
        raise ValueError("Colunas informadas não existem no arquivo.")

    plt.figure()
    plt.plot(df[coluna_x], df[coluna_y])
    plt.xlabel(coluna_x)
    plt.ylabel(coluna_y)
    plt.title("Gráfico gerado automaticamente")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    gerar_grafico("dados.xlsx", "Data", "Valor")
