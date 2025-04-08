import tkinter as tk
import random

largura = 500
altura = 500
tamanho_quadrado = 20
velocidade = 100

COR_COBRA = "#00FF00"
COR_COMIDA = "#FF0000"
COR_FUNDO = "#000000"

direcao = "direita"
cobra = [(100, 100), (80, 100), (60, 100)]
comida = (0, 0)

def nova_comida():
    global comida
    x = random.randint(0, (largura - tamanho_quadrado) // tamanho_quadrado) * tamanho_quadrado
    y = random.randint(0, (altura - tamanho_quadrado) // tamanho_quadrado) * tamanho_quadrado
    comida = (x, y)
    canvas.create_rectangle(x, y, x + tamanho_quadrado, y + tamanho_quadrado, fill=COR_COMIDA, tag="comida")

def mover():
    global cobra, direcao

    x, y = cobra[0]

    if direcao == "cima":
        y -= tamanho_quadrado
    elif direcao == "baixo":
        y += tamanho_quadrado
    elif direcao == "esquerda":
        x -= tamanho_quadrado
    elif direcao == "direita":
        x += tamanho_quadrado

    nova_cabeca = (x, y)

    if x < 0 or x >= largura or y < 0 or y >= altura:
        fim_de_jogo()
        return

    if nova_cabeca in cobra:
        fim_de_jogo()
        return

    cobra = [nova_cabeca] + cobra[:-1]

    if nova_cabeca == comida:
        cobra.append(cobra[-1])
        canvas.delete("comida")
        nova_comida()

    desenhar()
    janela.after(velocidade, mover)

def desenhar():
    canvas.delete("cobra")
    for parte in cobra:
        x, y = parte
        canvas.create_rectangle(x, y, x + tamanho_quadrado, y + tamanho_quadrado, fill=COR_COBRA, tag="cobra")

def fim_de_jogo():
    canvas.delete("all")
    canvas.create_text(largura/2, altura/2, fill="red", font="Arial 24 bold", text="FIM DE JOGO")

def mudar_direcao(event):
    global direcao
    tecla = event.keysym
    if tecla == "Up" and direcao != "baixo":
        direcao = "cima"
    elif tecla == "Down" and direcao != "cima":
        direcao = "baixo"
    elif tecla == "Left" and direcao != "direita":
        direcao = "esquerda"
    elif tecla == "Right" and direcao != "esquerda":
        direcao = "direita"

janela = tk.Tk()
janela.title("Snake Game 🐍")
canvas = tk.Canvas(janela, width=largura, height=altura, bg=COR_FUNDO)
canvas.pack()

janela.bind("<KeyPress>", mudar_direcao)

nova_comida()
mover()

janela.mainloop()
