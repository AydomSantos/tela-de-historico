import tkinter as tk

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
# criação das labels de cabeçalho
container_label = tk.Frame(root, bg="#FFFFFF", width=1055, height=50, border=1, relief="flat", highlightbackground="#000000", highlightthickness=1)
container_label.pack(fill=tk.X)

# Definindo os labels de cabeçalho
labels = ["Moeda de Origem", "Moeda de Destino", "Taxa de Câmbio", "Valor a Converter", "Resultado final"]

# Número total de colunas (labels + separadores)
num_columns = len(labels) * 2 - 1

# Largura de cada coluna (espaço disponível / número de colunas)
column_width = 1055 // num_columns

for i, text in enumerate(labels):
    label = tk.Label(container_label, text=text, bg="#FFFFFF", width=column_width // 10)
    label.grid(row=0, column=2 * i, sticky="nsew")

    

# Ajustando a largura das colunas no grid
for i in range(num_columns):
    container_label.grid_columnconfigure(i, minsize=column_width)

# ================================================================
# criação do frame para os dados
container_dados = tk.Frame(root, bg="#FFFFFF", width=1055, height=200)
container_dados.pack(fill=tk.X)

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
# Adicionando os dados ao container_dados
for row_index, row_data in enumerate(historico):
    for col_index, data in enumerate(row_data):
        label = tk.Label(container_dados, text=data, bg="#FFFFFF", width=column_width // 10)
        label.grid(row=row_index, column=2 * col_index, sticky="nsew")


# Ajustando a largura das colunas no grid
for i in range(num_columns):
    container_dados.grid_columnconfigure(i, minsize=column_width)

root.mainloop()
