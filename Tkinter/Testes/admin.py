
import tkinter as tk

# Criar janela
janela = tk.Tk()
janela.title("Exemplo de Input")
janela.geometry("300x150")

# Label
label = tk.Label(janela, text="Digite algo:")
label.pack(pady=5)

# Campo de entrada (input)
entrada = tk.Entry(janela, width=25)
entrada.pack(pady=5)

# Label para mostrar o resultado
resultado = tk.Label(janela, text="")
resultado.pack(pady=5)

# Função que "lê" o input
def pegar_input():
    texto = entrada.get()  # Pega o valor digitado
    resultado.config(text=f"Você digitou: {texto}")

# Botão para confirmar
botao = tk.Button(janela, text="Enviar", command=pegar_input)
botao.pack(pady=5)

# Loop principal
janela.mainloop()
