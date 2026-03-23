"""
Conversão e padronização de datas.
"""

from datetime import datetime

def normalizar_data(valor):
    formatos = ["%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"]

    for formato in formatos:
        try:
            return datetime.strptime(valor, formato).strftime("%d/%m/%Y")
        except ValueError:
            pass

    return None


if __name__ == "__main__":
    datas = ["2025-01-10", "10/01/2025", "10-01-2025"]

    for d in datas:
        print(d, "→", normalizar_data(d))
