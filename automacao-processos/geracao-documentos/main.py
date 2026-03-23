"""
Orquestrador da geração de documentos.
"""

from gerar_todos import gerar_todos


if __name__ == "__main__":
    registros = ["Doc 1", "Doc 2", "Doc 3"]
    gerar_todos(registros)