"""
Validação básica de CPF (estrutura e dígitos).
"""

import re

def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r"\D", "", cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calcular_digito(cpf, peso):
        soma = sum(int(d) * p for d, p in zip(cpf, peso))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    d1 = calcular_digito(cpf[:9], range(10, 1, -1))
    d2 = calcular_digito(cpf[:10], range(11, 1, -1))

    return cpf[-2:] == f"{d1}{d2}"


if __name__ == "__main__":
    testes = ["111.444.777-35", "000.000.000-00"]

    for t in testes:
        print(t, "válido?" , validar_cpf(t))
