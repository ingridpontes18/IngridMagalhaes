"""
Painel de Automação de Documentos Técnicos (DEMO)

Este módulo demonstra uma interface gráfica para seleção e geração
automatizada de documentos técnicos em Word ou PDF.

A versão completa inclui:
- Integração real com planilhas Excel
- Geração efetiva de documentos
- Impressão automatizada
"""

import tkinter as tk
from tkinter import ttk, messagebox


# ================== FUNÇÕES DEMO ==================

def listar_ids_demo():
    """
    Retorna uma lista fictícia de identificadores apenas para demonstração.
    """
    return [
        "01/2025",
        "02/2025",
        "03/2025",
        "04/2025",
        "05/2025"
    ]


def gerar_documentos(ids, formato):
    """
    Demonstração da geração de documentos.
    """
    for item in ids:
        print(f"[DEMO] Gerando documento {item} em formato {formato.upper()}")
    messagebox.showinfo(
        "Processo concluído",
        f"{len(ids)} documento(s) processado(s) em {formato.upper()} (DEMO)."
    )


def imprimir_documentos(ids, formato):
    """
    Demonstração da impressão de documentos.
    """
    for item in ids:
        print(f"[DEMO] Enviando documento {item}.{formato} para impressão")
    messagebox.showinfo(
        "Impressão",
        f"{len(ids)} documento(s) enviados para impressão (DEMO)."
    )


# ================== SELEÇÃO ==================

def obter_selecionados():
    selecionados = lista_ids.curselection()
    if not selecionados:
        messagebox.showwarning("Atenção", "Selecione pelo menos um item.")
        return []
    return [lista_ids.get(i) for i in selecionados]


def gerar_selecionados(formato):
    ids = obter_selecionados()
    if ids:
        gerar_documentos(ids, formato)


def imprimir_selecionados(formato):
    ids = obter_selecionados()
    if ids:
        imprimir_documentos(ids, formato)


def gerar_todos(formato):
    gerar_documentos(listar_ids_demo(), formato)


def imprimir_todos(formato):
    imprimir_documentos(listar_ids_demo(), formato)


# ================== INTERFACE ==================

janela = tk.Tk()
janela.title("Automação de Documentos Técnicos")
janela.geometry("520x500")

tk.Label(
    janela,
    text="Painel de Automação de Documentos",
    font=("Calibri", 16, "bold")
).pack(pady=10)

# ---------- Lista ----------
frame_lista = ttk.LabelFrame(
    janela,
    text="Selecionar documentos (Ctrl ou Shift para múltiplos)"
)
frame_lista.pack(fill="both", padx=15, pady=10)

lista_ids = tk.Listbox(frame_lista, selectmode="extended", height=10)
lista_ids.pack(side="left", fill="both", expand=True)

scroll = ttk.Scrollbar(frame_lista, command=lista_ids.yview)
scroll.pack(side="right", fill="y")
lista_ids.config(yscrollcommand=scroll.set)

for item in listar_ids_demo():
    lista_ids.insert(tk.END, item)

# ---------- Selecionados ----------
frame_sel = ttk.LabelFrame(janela, text="Ações para Selecionados")
frame_sel.pack(fill="x", padx=15, pady=10)

ttk.Button(
    frame_sel,
    text="Gerar Word (Selecionados)",
    command=lambda: gerar_selecionados("word")
).pack(fill="x", pady=3)

ttk.Button(
    frame_sel,
    text="Gerar PDF (Selecionados)",
    command=lambda: gerar_selecionados("pdf")
).pack(fill="x", pady=3)

ttk.Button(
    frame_sel,
    text="Imprimir Word (Selecionados)",
    command=lambda: imprimir_selecionados("docx")
).pack(fill="x", pady=3)

ttk.Button(
    frame_sel,
    text="Imprimir PDF (Selecionados)",
    command=lambda: imprimir_selecionados("pdf")
).pack(fill="x", pady=3)

# ---------- Todos ----------
frame_todos = ttk.LabelFrame(janela, text="Ações Globais")
frame_todos.pack(fill="x", padx=15, pady=10)

ttk.Button(
    frame_todos,
    text="Gerar TODOS Word",
    command=lambda: gerar_todos("word")
).pack(fill="x", pady=3)

ttk.Button(
    frame_todos,
    text="Gerar TODOS PDF",
    command=lambda: gerar_todos("pdf")
).pack(fill="x", pady=3)

ttk.Button(
    frame_todos,
    text="Imprimir TODOS Word",
    command=lambda: imprimir_todos("docx")
).pack(fill="x", pady=3)

ttk.Button(
    frame_todos,
    text="Imprimir TODOS PDF",
    command=lambda: imprimir_todos("pdf")
).pack(fill="x", pady=3)

janela.mainloop()
