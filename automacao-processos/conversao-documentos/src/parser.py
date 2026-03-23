"""
Responsável por interpretar os dados extraídos.
"""

def processar_dados(linhas):
    dados = []

    for linha in linhas:
        dados.append({
            "conteudo": linha.strip()
        })

    return dados