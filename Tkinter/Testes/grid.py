import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo Grid")
janela.geometry("500x150")


# tk.Label(janela, text="Usuário:").grid(row=0, column=0)
# tk.Entry(janela).grid(row=0, column=1)

# tk.Label(janela, text="Senha:").grid(row=1, column=0)
# tk.Entry(janela, show="*").grid(row=1, column=1)

# tk.Button(janela, text="Login").grid(row=2, column=0, columnspan=2)

tk.Label(janela, text="Nome:").grid(row=1, column=1)
tk.Entry(janela).grid(row=2, column=1, padx=5, pady=5)

tk.Label(janela, text="Materia:").grid(row=1, column=2)
tk.Entry(janela, show="*").grid(row=2, column=2)

tk.Label(janela, text="Nota:").grid(row=1, column=3)
tk.Entry(janela).grid(row=2, column=3, padx=5, pady=5)

tk.Button(janela, text="Login").grid(row=2, column=4, columnspan=1)

janela.mainloop()
