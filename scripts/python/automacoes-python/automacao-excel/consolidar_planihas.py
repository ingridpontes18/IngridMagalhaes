"""
Consolidação automática de múltiplas planilhas Excel
Uso comum: unir arquivos mensais em uma base única
"""

import pandas as pd
import glob
import os

PASTA_ENTRADA = "dados_excel"
ARQUIVO_SAIDA = "consolidado.xlsx"

def consolidar_planilhas():
    arquivos = glob.glob(os.path.join(PASTA_ENTRADA, "*.xlsx"))

    if not arquivos:
        print("Nenhum arquivo encontrado.")
        return

    bases = []

    for arquivo in arquivos:
        df = pd.read_excel(arquivo)
        df["arquivo_origem"] = os.path.basename(arquivo)
        bases.append(df)

    df_final = pd.concat(bases, ignore_index=True)
    df_final.to_excel(ARQUIVO_SAIDA, index=False)

    print(f"Arquivo consolidado gerado: {ARQUIVO_SAIDA}")

if __name__ == "__main__":
    consolidar_planilhas()
