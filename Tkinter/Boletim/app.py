import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Boletim Escolar")
janela.geometry("620x350")
    
tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
nome = tk.Entry(janela)
nome.grid(row=1, column=0, padx=5, pady=5)

tk.Label(janela, text="Matéria:").grid(row=0, column=1, padx=5, pady=5)
materia = tk.Entry(janela)
materia.grid(row=1, column=1, padx=5, pady=5)

tk.Label(janela, text="Nota 1:").grid(row=0, column=2, padx=5, pady=5)
nota1 = tk.Entry(janela)
nota1.grid(row=1, column=2, padx=5, pady=5)

tk.Label(janela, text="Nota 2:").grid(row=0, column=3, padx=5, pady=5)
nota2 = tk.Entry(janela)
nota2.grid(row=1, column=3, padx=5, pady=5)


colunas = ("nome", "materia", "nota1", "nota2", "media")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")

tabela.heading("nome", text="Nome")
tabela.heading("materia", text="Matéria")
tabela.heading("nota1", text="Nota 1")
tabela.heading("nota2", text="Nota 2")
tabela.heading("media", text="Média")

tabela.column("nome", width=150, anchor="center")
tabela.column("materia", width=120, anchor="center")
tabela.column("nota1", width=80, anchor="center")
tabela.column("nota2", width=80, anchor="center")
tabela.column("media", width=80, anchor="center")

tabela.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

def cal_media():
    valor1 = float(nota1.get())
    valor2 = float(nota2.get())
    return (valor1 + valor2) / 2
   
def add_linha():
    aluno = nome.get()
    mat = materia.get()
    media = cal_media()

    if aluno and mat and media is not None:
        tabela.insert("", "end", values=(
            aluno, mat, nota1.get(), nota2.get(), f"{media:.2f}"
        ))

        nome.delete(0, tk.END)
        materia.delete(0, tk.END)
        nota1.delete(0, tk.END)
        nota2.delete(0, tk.END)
    else:
        print("Preencha todos os campos corretamente!")

def extrair_boletim():
    print("Preencha todos os campos corretamente!")

botao = tk.Button(janela, text="Adicionar", command=add_linha)
botao.grid(row=1, column=4, padx=10)

botao = tk.Button(janela, text="Extrair", command=extrair_boletim)
botao.grid(row=4, column=4, padx=10)

janela.mainloop()
