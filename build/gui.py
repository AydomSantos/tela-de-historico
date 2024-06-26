import tkinter as tk

# Função para o botão Voltar
def voltar():
    print("Botão Voltar pressionado")

# Configuração da janela principal
root = tk.Tk()
root.title("Histórico de Conversão de Moeda")
root.geometry("1563x160")
root.configure(bg="#F9F2ED")

# Criação do frame de cabeçalho
header = tk.Frame(root, bg="#ffffff", width=1055, height=72)
header.pack(fill=tk.X)

# Adicionando um título no frame de cabeçalho
titulo = tk.Label(header, text="Histórico de conversão", bg="#ffffff", fg="#000000", font=("Helvetica", 16))
titulo.place(x=20, y=20) 

# Adicionando um botão Voltar no frame de cabeçalho
btn_voltar = tk.Button(header, text="Voltar", bg="#FFA500", fg="#ffffff", font=("Helvetica", 12), command=voltar)
btn_voltar.place(x=1555 - 107 - 20, y=7.5, width=107, height=57)  # Posição e tamanho do botão

root.mainloop()
