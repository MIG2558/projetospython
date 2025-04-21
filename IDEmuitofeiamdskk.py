from tkinter import *
import tkinter as tk
from tkinter import ttk

application = tk.Tk()
def caracteres():
    input = texto.get("1.0", END)
    c = len(input) - 1
    l1.config(text="Caracteres: {}".format(c))
def palavras():
    input = texto.get("1.0", END)
    p = len(input.split(' '))
    l2.config(text="Palavras: {}".format(p))
def contar():
    palavras()
    caracteres()
def executar():
    input = texto.get("1.0", END)
    exec(input)
def criaraba():
    novaaba.destroy()
    index = centro.index(centro.select())
    centro.tab(index, text="main2.py")
    def caracteres():
        input = ntexto.get("1.0", END)
        c = len(input) - 1
        l1.config(text="Caracteres: {}".format(c))
    def palavras():
        input = ntexto.get("1.0", END)
        p = len(input.split(' '))
        l2.config(text="Palavras: {}".format(p))
    def contar():
        palavras()
        caracteres()
    def executar():
        input = ntexto.get("1.0", END)
        exec(input)
    ntexto = tk.Text(aba2)
    nl1 = tk.Label(aba2, text="Caracteres: 0")
    nl2 = tk.Label(aba2, text="Palavras: 0")
    nb = Button(aba2, text="Executar", command=lambda:executar())
    ntexto.pack()
    nl1.pack()
    nl2.pack()
    nb.pack()
    ntexto.bind("<KeyRelease>", lambda event: contar())
application.title("IDE Python")
centro = ttk.Notebook(application)
centro.pack()
aba1 = ttk.Frame(centro)
aba2 = ttk.Frame(centro)
centro.add(aba1, text="main.py")
centro.add(aba2, text="+")
texto = tk.Text(aba1)
l1 = tk.Label(aba1, text="Caracteres: 0")
l2 = tk.Label(aba1, text="Palavras: 0")
b = Button(aba1, text="Executar", command=lambda:executar())
novaaba = Button(aba2, text="Nova aba", command=lambda:criaraba())
texto.pack()
l1.pack()
l2.pack()
b.pack()
novaaba.pack()
texto.bind("<KeyPress>", lambda event: contar())

application.mainloop()
