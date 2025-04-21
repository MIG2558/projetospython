from tkinter import *
import tkinter as tk
from tkinter import filedialog, ttk

application = tk.Tk()
application.title("BLOCO DE NOTAS: REVAMPED")
def caracteres():
    input = texto.get("1.0", END)
    c = len(input) - 1
    l1.config(text="Caracteres: {}".format(c))
    l1.config(text="Caracteres: {}".format(c))
def palavras():
    input = texto.get("1.0", END)
    d = len(input.split(' '))
    l2.config(text="Palavras: {}".format(d))
def contar():
    caracteres()
    palavras()
def abrir():
    a = filedialog.askopenfile(filetypes=[("Selecione um TXT", "*.txt")])
    if a is not None:
        conteudo = a.readlines()
        texto.delete("1.0", END)
        texto.insert("1.0", conteudo)
def salvar():
    b = filedialog.asksaveasfile(filetypes=[("Selecione um TXT", "*.txt")])
    if b is not None:
        input = texto.get("1.0", END)
        b.writelines(input)
def limpar():
    texto.delete("1.0", END)
def criaraba():
    def caracteres():
        input = ntexto.get("1.0", END)
        c = len(input) - 1
        nl1.config(text="Caracteres: {}".format(c))
        nl1.config(text="Caracteres: {}".format(c))
    def palavras():
        input = ntexto.get("1.0", END)
        d = len(input.split(' '))
        nl2.config(text="Palavras: {}".format(d))
    def contar():
        caracteres()
        palavras()
    def abrir():
         a = filedialog.askopenfile(filetypes=[("Selecione um TXT", "*.txt")])
         if a is not None:
            conteudo = a.readlines()
            ntexto.delete("1.0", END)
            ntexto.insert("1.0", conteudo)
    def salvar():
        b = filedialog.asksaveasfile(filetypes=[("Selecione um TXT", "*.txt")])
        if b is not None:
            input = ntexto.get("1.0", END)
            b.writelines(input)
    def limpar():
        ntexto.delete("1.0", END)
    ntexto = tk.Text(aba2)
    nl1 = tk.Label(aba2, text="Caracteres: 0")
    nl2 = tk.Label(aba2, text="Palavras: 0")
    nb1 = Button(aba2, text="Abrir", command=lambda:abrir())
    nb2 = Button(aba2, text="Salvar", command=lambda:salvar())
    nb3 = Button(aba2, text="Limpar", command=lambda:limpar())
    ntexto.pack()
    nl1.pack()
    nl2.pack()
    nb1.pack()
    nb2.pack()
    nb3.pack()
    novaaba.destroy()
    ntexto.bind("<KeyRelease>", lambda event: contar())
centro = ttk.Notebook()
centro.pack(expand=True, fill='both')
aba1 = ttk.Frame(centro)
aba2 = ttk.Frame(centro)
centro.add(aba1, text="Aba 1")
centro.add(aba2, text="+")
texto = tk.Text(aba1)
l1 = tk.Label(aba1, text="Caracteres: 0")
l2 = tk.Label(aba1, text="Palavras: 0")
b1 = Button(aba1, text="Abrir", command=lambda:abrir())
b2 = Button(aba1, text="Salvar", command=lambda:salvar())
b3 = Button(aba1, text="Limpar", command=lambda:limpar())
novaaba = Button(aba2, text="Nova aba", command=lambda:criaraba())
texto.pack()
l1.pack()
l2.pack()
b1.pack()
b2.pack()
b3.pack()
novaaba.pack()
texto.bind("<KeyPress>", lambda event: contar())
application.mainloop()
