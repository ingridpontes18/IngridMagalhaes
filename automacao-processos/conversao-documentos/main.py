from src.pdf_reader import ler_pdf
from src.parser import extrair_dados
from src.exporter import exportar_excel

def main():
    pdf_path = "examples/sample_input.pdf"
    output_path = "examples/output_example.xlsx"

    texto = ler_pdf(pdf_path)
    dados = extrair_dados(texto)
    exportar_excel(dados, output_path)

    print("✅ Arquivo Excel gerado com sucesso!")

if __name__ == "__main__":
    main()
