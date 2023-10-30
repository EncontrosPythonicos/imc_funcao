import tkinter as tk
from tkinter import *

def calcular_imc(entrada_peso, entrada_altura, resultado):
    peso = float(entrada_peso.get())
    altura = float(entrada_altura.get())
    imc = peso / (altura ** 2)
    
    if imc < 17:
        resultado["fg"] = "orange"
        resultado["text"] = f"Você está com o IMC de {imc:.2f}"
    elif 17 <= imc < 18.49:
        resultado["fg"] = "orange"
        resultado["text"] = f"Você está com o IMC de {imc:.2f} "
    elif 18.5 <= imc < 24.99:
        resultado["fg"] = "green"
        resultado["text"] = f"Você está com o IMC de {imc:.2f} "
    elif 25 <= imc < 29.99:
        resultado["fg"] = "yellow"
        resultado["text"] = f"Você está com o IMC de {imc:.2f} "
    elif 30 <= imc < 34.99:
        resultado["fg"] = "red"
        resultado["text"] = f"Você está com o IMC de {imc:.2f} "
    elif 35 <= imc < 39.99:
        resultado["fg"] = "red"
        resultado["text"] = f"Você está com o IMC de {imc:.2f} "
    else:
        resultado["fg"] = "red"
        resultado["text"] = f"Você está com o IMC de {imc:.2f}"

def criar_janela():
    janela = tk.Tk()
    janela.title("Encontros Pythônicos")
    janela.config(background="#000000")
    return janela

def criar_canvas(janela):
    altura_canvas = 100
    largura_canvas = 500
    margin = Canvas(janela, width=largura_canvas, bg='#00FF7F', height=altura_canvas, bd=15, highlightthickness=0, relief='ridge')
    margin.pack()
    texto = "CALCULADORA IMC"
    x_pos = 260  
    y_pos = 65
    margin.create_text(x_pos, y_pos, text=texto, fill='black', font=('Arial', 30, 'bold'))
    return margin

def criar_rotulos_campos(janela):
    label_peso = tk.Label(janela, text="INSIRA O PESO (kg):", bg='#00FF7F', font=('Montserrat', 11, 'bold'))
    label_peso.pack(anchor="center", pady=(100, 0)) 
    entrada_peso = tk.Entry(janela, width=25) 
    entrada_peso.pack(anchor="center", pady=(0, 10)) 

    label_altura = tk.Label(janela, text="INSIRA A ALTURA (m):", bg='#00FF7F', font=('Montserrat', 11, 'bold'))
    label_altura.pack(anchor="center", pady=(30, 0))   
    entrada_altura = tk.Entry(janela, width=26)  
    entrada_altura.pack(anchor="center", pady=(0, 30)) 
    return entrada_peso, entrada_altura

def criar_botao(janela, entrada_peso, entrada_altura, resultado):
    calcular = tk.Button(janela, text="Calcular IMC", command=lambda: calcular_imc(entrada_peso, entrada_altura, resultado), bg='#00FF7F', bd=5, font=('Montserrat', 14, 'bold'))
    calcular.pack()

def criar_resultado(janela):
    resultado = tk.Label(janela, text="", bg='#000000', font=('Montserrat', 14, 'bold'))
    resultado.pack(pady=(0, 30))
    return resultado

def criar_caixa_texto(janela):
    info_text = tk.Text(janela, width=55, height=11, wrap=tk.WORD, bg='#00FF7F', font=('Montserrat', 10, 'bold'))
    info_text.insert(tk.END, "\t\t    INFORMATIVO DO IMC\n\n")
    info_text.insert(tk.END, "\t  RESULTADO\t\t\t       SITUAÇÃO\n\n")
    info_text.insert(tk.END, "\tAbaixo de 17\t\t\tMuito abaixo do peso\n")
    info_text.insert(tk.END, "\tEntre 17 e 18.49\t\t\tAbaixo do peso\n")
    info_text.insert(tk.END, "\tEntre 18.5 e 24.99\t\t\tPeso normal\n")
    info_text.insert(tk.END, "\tEntre 25 e 29.99 \t\t\tAcima do peso\n")
    info_text.insert(tk.END, "\tEntre 30 e 34.99\t\t\tObesidade I\n")
    info_text.insert(tk.END, "\tEntre 35 e 39.99\t\t\tObesidade II (severa)\n")
    info_text.insert(tk.END, "\tAcima de 40\t\t\tObesidade III (mórbida)\n")
    info_text.pack(side="bottom", padx=0, pady=20)

def main():
    janela = criar_janela()
    margem = criar_canvas(janela)
    entrada_peso, entrada_altura = criar_rotulos_campos(janela)
    resultado = criar_resultado(janela)
    criar_botao(janela, entrada_peso, entrada_altura, resultado)
    criar_caixa_texto(janela)
    janela.mainloop()

main()