"""
Demonstração de sistema de agendamento automatizado.

Este script simula:
- Controle de vagas por período
- Validação de disponibilidade
- Estrutura base de integração com sistemas externos
"""

from datetime import datetime
from collections import defaultdict


LIMITE_MANHA = 15
LIMITE_TARDE = 25


def normalizar_data(data_str: str):
    try:
        return datetime.strptime(data_str, "%d/%m/%Y")
    except ValueError:
        return None


def processar_agendamentos(dados):
    contador = defaultdict(int)
    resultados = []

    for item in dados:
        data = normalizar_data(item["data"])
        periodo = item["periodo"].lower()

        if not data or periodo not in ["manhã", "tarde"]:
            item["status"] = "Erro"
            resultados.append(item)
            continue

        chave = f"{data.strftime('%d/%m/%Y')}_{periodo}"
        limite = LIMITE_MANHA if periodo == "manhã" else LIMITE_TARDE

        if contador[chave] < limite:
            contador[chave] += 1
            item["status"] = "Confirmado"
        else:
            item["status"] = "Indisponível"

        resultados.append(item)

    return resultados


if __name__ == "__main__":
    dados_exemplo = [
        {"nome": "Cliente 1", "data": "10/02/2026", "periodo": "manhã"},
        {"nome": "Cliente 2", "data": "10/02/2026", "periodo": "tarde"},
    ]

    resultado = processar_agendamentos(dados_exemplo)

    for r in resultado:
        print(r)