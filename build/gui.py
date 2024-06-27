import tkinter as tk
from tkinter import ttk

# Função para o botão Voltar
def voltar():
    print("Botão Voltar pressionado")

# Configuração da janela principal
root = tk.Tk()
root.title("Histórico de Conversão de Moeda")
root.geometry("1070x300")
root.configure(bg="#F9F2ED")

# Construção do Header da tela de historico
# Criação do frame de cabeçalho
header = tk.Frame(root, bg="#F9F2ED", width=1055, height=72)
header.pack(fill=tk.X)

# Adicionando um título no frame de cabeçalho
titulo = tk.Label(header, text="Histórico de conversão", bg="#F9F2ED", fg="#000000", font=("Helvetica", 16))
titulo.place(x=20, y=20) 

# Adicionando um botão Voltar no frame de cabeçalho
btn_voltar = tk.Button(header, text="Voltar", bg="#FFA500", fg="#ffffff", font=("Helvetica", 12), command=voltar)
btn_voltar.place(x=900, y=7.5, width=137, height=57)  # Posição e tamanho do botão

# ================================================================
# criação da tabela de histórico
# Criando o frame para a tabela
container_tabela = tk.Frame(root, bg="#FFFFFF", width=1055, height=200)
container_tabela.pack(fill=tk.BOTH, expand=True)

# Definindo as colunas da tabela
colunas = ("origem", "destino", "taxa", "valor", "resultado")

# Estilo do Treeview
style = ttk.Style()
style.configure("Custom.Treeview", background="#FFFFFF", foreground="#000000", fieldbackground="#1F1F1F")
style.map("Custom.Treeview", background=[("selected", "#FFA500")], foreground=[("selected", "white")])

# Criando o Treeview
tree = ttk.Treeview(container_tabela, columns=colunas, show="headings", style="Custom.Treeview")
tree.pack(fill=tk.BOTH, expand=True)

# Definindo os cabeçalhos das colunas
tree.heading("origem", text="Moeda de Origem")
tree.heading("destino", text="Moeda de Destino")
tree.heading("taxa", text="Taxa de Câmbio")
tree.heading("valor", text="Valor a Converter")
tree.heading("resultado", text="Resultado final")

# Definindo a largura das colunas
tree.column("origem", width=200)
tree.column("destino", width=200)
tree.column("taxa", width=150)
tree.column("valor", width=150)
tree.column("resultado", width=150)

# Dados do histórico de conversão de moedas
historico = [
    ["USD", "BRL", "5.25", "100.00", "525.00"],
    ["EUR", "USD", "1.10", "200.00", "220.00"],
    ["GBP", "EUR", "1.17", "150.00", "175.50"],
    ["JPY", "USD", "0.0093", "10000.00", "93.00"],
    ["AUD", "GBP", "0.55", "250.00", "137.50"],
    ["CAD", "USD", "0.80", "300.00", "240.00"],
    ["USD", "JPY", "110.25", "50.00", "5512.50"],
    ["EUR", "GBP", "0.85", "180.00", "153.00"],
    ["GBP", "AUD", "1.82", "120.00", "218.40"],
    ["JPY", "CAD", "88.25", "75.00", "6618.75"],
    ["AUD", "USD", "0.75", "400.00", "300.00"],
    ["USD", "EUR", "0.91", "220.00", "200.20"],
    ["GBP", "JPY", "135.80", "80.00", "10864.00"],
    ["CAD", "EUR", "0.63", "150.00", "94.50"],
    ["EUR", "AUD", "1.45", "300.00", "435.00"],
    ["JPY", "GBP", "0.0074", "5000.00", "37.00"],
    ["AUD", "CAD", "0.96", "200.00", "192.00"],
    ["USD", "USD", "1.00", "1000.00", "1000.00"],
    ["EUR", "EUR", "1.00", "500.00", "500.00"],
    ["GBP", "GBP", "1.00", "700.00", "700.00"],
    ["JPY", "JPY", "1.00", "8000.00", "8000.00"],
    ["CAD", "CAD", "1.00", "300.00", "300.00"],
    ["AUD", "AUD", "1.00", "400.00", "400.00"],
    ["USD", "EUR", "0.89", "120.00", "106.80"],
    ["EUR", "GBP", "0.87", "250.00", "217.50"],
    ["GBP", "JPY", "139.20", "90.00", "12528.00"],
    ["JPY", "USD", "0.0095", "15000.00", "142.50"],
    ["AUD", "CAD", "0.95", "180.00", "171.00"],
    ["CAD", "USD", "0.78", "270.00", "210.60"],
    ["USD", "EUR", "0.87", "200.00", "174.00"],
    ["EUR", "GBP", "0.88", "150.00", "132.00"],
    ["GBP", "JPY", "140.50", "100.00", "14050.00"],
    ["JPY", "USD", "0.0097", "8000.00", "77.60"]
]

# Adicionando os dados ao Treeview
for row in historico:
    tree.insert("", "end", values=row)

root.mainloop()
