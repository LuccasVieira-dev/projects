#apenas um código estúpido que roda creep, se você quer que funcione baixa o exe em releases, esse aqui é só o código fonte

import sys
import os
import tkinter as tk
import pygame
from PIL import Image, ImageTk

# Caminhos da música e do fundo
if hasattr(sys, "_MEIPASS"):
    musica_path = os.path.join(sys._MEIPASS, "Radiohead - Creep [XFkzRNyygfk].mp3")
    fundo_path = os.path.join(sys._MEIPASS, "crepe.jpg")
else:
    musica_path = "Radiohead - Creep [XFkzRNyygfk].mp3"
    fundo_path = "crepe.jpg"

# Inicializar Pygame e tocar música
pygame.mixer.init()
pygame.mixer.music.load(musica_path)
pygame.mixer.music.play()

# Criar janela Tkinter
janela = tk.Tk()
janela.geometry("500x400")
janela.title("Creep - Radiohead")
janela.eval('tk::PlaceWindow . center')

# Carregar imagem base
img_base = Image.open(fundo_path)

# Label para o fundo
label_fundo = tk.Label(janela)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# Função para redimensionar o fundo automaticamente
def redimensionar(event=None):
    largura, altura = janela.winfo_width(), janela.winfo_height()
    foto = ImageTk.PhotoImage(img_base.resize((largura, altura)))
    label_fundo.config(image=foto)
    label_fundo.image = foto  # mantém referência

janela.bind("<Configure>", redimensionar)

# Label central para mostrar a letra
label = tk.Label(janela, font=("Arial", 25, "italic"), fg="white", bg="black")
label.place(relx=0.5, rely=0.5, anchor="center")  # centralizado

# Assinatura no canto inferior direito
assinatura = tk.Label(janela, text="Made by Luccas", font=("Arial", 10), fg="white", bg="black")
assinatura.place(relx=1.0, rely=1.0, anchor="se")

# Função para mudar a frase do karaokê
def mudar(frase):
    label.config(text=frase)
    label.lift()  # garante que o texto fique acima do fundo

# Lista de tempos e frases da música
letra = [
    (0, "♫"),
    (18600, "When you were here before"),
    (23500, "Couldn't look you in the eye"),
    (29000, "You're just like an angel"),
    (34000, "Your skin makes me cry"),
    (39000, "You float like a feather"),
    (44000, "In a beautiful world"),
    (49500, "I wish I was special"),
    (54500, "You're so fucking special"),
    (60000, "But I'm a creep"),
    (65000, "I'm a weirdo"),
    (70000, "What the hell am I doing here?"),
    (76000, "I don't belong here"),
    (81000, "I don't care if it hurts"),
    (86000, "I want to have control"),
    (91500, "I want a perfect body"),
    (96500, "I want a perfect soul"),
    (102000, "I want you to notice"),
    (107000, "When I'm not around"),
    (112000, "You're so fucking special"),
    (114500, "I wish I was special"),
    (123000, "But I'm a creep"),
    (128000, "I'm a weirdo"),
    (133000, "What the hell am I doing here?"),
    (139000, "I don't belong here"),
    (145000, "She's running out the door"),
    (155000, "She's running out"),
    (160500, "She run, run, run, run"),
    (164500, "Run"),
    (185000, "Whatever makes you happy"),
    (190500, "Whatever you want"),
    (195500, "You're so fucking special"),
    (200500, "I wish I was special"),
    (205500, "But I'm a creep"),
    (211000, "I'm a weirdo"),
    (216000, "What the hell am I doing here?"),
    (221500, "I don't belong here")
]

# Agendar a mudança das frases
for tempo, frase in letra:
    janela.after(tempo, mudar, frase)

# Rodar a janela
janela.mainloop()
