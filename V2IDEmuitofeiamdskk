from tkinter import *
import tkinter as tk
from tkinter import filedialog, ttk

application = tk.Tk()
application.title("IDE V2.0")
def caracteres():
    input = texto.get("1.0", END)
    c = len(input) - 1
    l1.config(text="Caracteres: {}".format(c))
def palavras():
    input = texto.get("1.0", END)
    p = len(input.split(' '))
    l2.config(text="Palavras: {}".format(p))
def contar():
    caracteres()
    palavras()
def executar():
    input = texto.get("1.0", END)
    if input.strip():
        try:
            exec(input)
            text2 = tk.Text(aba1)
            sucesso = "Código executado com sucesso"
            text2.insert("1.0", sucesso)
            text2.config(state="disabled")
            text2.pack()
        except Exception as e:
            text2 = tk.Text(aba1)
            erro = "Erro: {}".format(e)
            text2.insert("1.0", erro)
            text2.config(state="disabled")
            text2.pack()
def abrir():
    a = filedialog.askopenfile(filetypes=[("Selecione um .py", "*.py")])
    if a is not None:
        a.readlines()
        texto.delete("1.0", END)
        texto.insert("1.0", a)
def salvar():
    b = filedialog.asksaveasfile(filetypes=[("Selecione um .py", "*.py")])
    if b is not None:
        input = texto.get("1.0", END)
        b.writelines(input)
def criaraba():
    def caracteres():
        input = ntexto.get("1.0", END)
        c = len(input) - 1
        nl1.config(text="Caracteres: {}".format(c))
    def palavras():
        input = ntexto.get("1.0", END)
        p = len(input.split(' '))
        nl2.config(text="Palavras: {}".format(p))
    def contar():
        caracteres()
        palavras()
    def executar():
        input = ntexto.get("1.0", END)
        if input.strip():
            try:
                exec(input)
                ntext2 = tk.Text(aba2)
                sucesso = "Código executado com sucesso"
                ntext2.insert("1.0", sucesso)
                ntext2.config(state="disabled")
                ntext2.pack()
            except Exception as e:
                erro = "Erro: {}".format(e)
                ntext2.insert("1.0", erro)
                ntext2.config(state="disabled")
                ntext2.pack()
    def abrir():
        a = filedialog.askopenfile(filetypes=[("Selecione um .py", "*.py")])
        if a is not None:
            a.readlines()
            ntexto.delete("1.0", END)
            ntexto.insert("1.0", a)
    def salvar():
        b = filedialog.asksaveasfile(filetypes=[("Selecione um .py", "*.py")])
        if b is not None:
            input = ntexto.get("1.0", END)
            b.writelines(input)
    index = centro.index(centro.select())
    centro.tab(index, text="main2.py")
    novaaba.destroy()
    ntexto = tk.Text(aba2)
    nl1 = tk.Label(aba2, text="Caracteres: 0")
    nl2 = tk.Label(aba2, text="Palavras: 0")
    nbutton = Button(aba2, text="Executar", command=lambda:executar())
    nbabrir = Button(aba2, text="Abrir", command=lambda:abrir())
    nbsalvar = Button(aba2, text="Salvar", command=lambda:salvar())
    ntexto.pack()
    nl1.pack()
    nl2.pack()
    nbutton.pack()
    nbabrir.pack()
    nbsalvar.pack()
    ntexto.bind("<KeyRelease>", lambda event: contar())
centro = ttk.Notebook(application)
aba1 = ttk.Frame(centro)
aba2 = ttk.Frame(centro)
centro.add(aba1, text="main.py")
centro.add(aba2, text="+")
centro.pack()
texto = tk.Text(aba1)
l1 = tk.Label(aba1, text="Caracteres: 0")
l2 = tk.Label(aba1, text="Palavras: 0")
button = Button(aba1, text="Executar", command=lambda:executar())
babrir = Button(aba1, text="Abrir", command=lambda:abrir())
bsalvar = Button(aba1, text="Salvar", command=lambda:salvar())
novaaba = Button(aba2, text="Novo arquivo", command=lambda:criaraba())
novaaba.pack()
texto.pack()
l1.pack()
l2.pack()
button.pack()
babrir.pack()
bsalvar.pack()
application.bind("<F5>", lambda event: executar() or "<Control+F5>", lambda event: executar())
texto.bind("<KeyRelease>", lambda event: contar())

application.mainloop()
