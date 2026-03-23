"""
Geração em lote de documentos.
"""

def gerar_todos(registros):
    for r in registros:
        print(f"Gerando documento para: {r}")