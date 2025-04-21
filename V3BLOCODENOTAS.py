from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import tkinter as tk

application = tk.Tk()
centro = ttk.Notebook()
centro.pack(expand=True, fill='both')
aba1 = ttk.Frame(centro)
aba2 = ttk.Frame(centro)
centro.add(aba1, text="1° arquivo")
centro.add(aba2, text="+")
def cupdate():
    input = texto.get("1.0", END)
    lc = len(input) - 1
    l.config(text="Caracteres: {}".format(lc))
def pupdate():
    input = texto.get("1.0", END)
    lp = len(input.split(' '))
    p.config(text="Palavras: {}".format(lp))
def limpar():
    texto.delete("1.0", END)
def salvar():
    a = filedialog.asksaveasfile(filetypes=[("TXT"), "*.txt"])
    if a is not None:
        input = texto.get("1.0", END)
        a.writelines(input)
        def change_name():
            centro.tab(aba1, text="{}".format(a.name()))
        change_name()
def abrir():
    b = filedialog.askopenfile(filetypes=[("TXT", "*.txt")])
    if b is not None:
        conteudo = b.readlines()
        texto.delete("1.0", END)
        texto.insert("1.0", conteudo)
        def change_name():
            centro.tab(aba1, text="{}".format(b.name()))
        change_name()
def font():
    selecionado = listbox.get(tk.ACTIVE)
    texto.config(font="{}".format(selecionado))
def count():
    cupdate()
    pupdate()
def aba():
    bnovo.destroy()
    def change_name():
        centro.tab(aba2, text="2° arquivo")
    change_name()
    def cupdate():
        input = ntexto.get("1.0", END)
        lc = len(input) - 1
        nl.config(text="Caracteres: {}".format(lc))
    def pupdate():
        input = ntexto.get("1.0", END)
        lp = len(input.split(' '))
        np.config(text="Palavras: {}".format(lp))
    def limpar():
        ntexto.delete("1.0", END)
    def salvar():
        a = filedialog.asksaveasfile(filetypes=[("TXT"), "*.txt"])
        if a is not None:
            input = ntexto.get("1.0", END)
            a.writelines(input)
            def change_name():
                centro.tab(aba1, text="{}".format(a.name()))
            change_name()
    def abrir():
        b = filedialog.askopenfile(filetypes=[("TXT", "*.txt")])
        if b is not None:
            conteudo = b.readlines()
            ntexto.delete("1.0", END)
            ntexto.insert("1.0", conteudo)
            def change_name():
                centro.tab(aba2, text="{}".format(b.name()))
        change_name()
    def font():
        selecionado = nlistbox.get(tk.ACTIVE)
        ntexto.config(font="{}".format(selecionado))
    def count():
        cupdate()
        pupdate()
    def font():
        selecionado = nlistbox.get(tk.ACTIVE)
        ntexto.config(font="{}".format(selecionado))
    ntexto = tk.Text(aba2, height=15, width=40)
    nl = tk.Label(aba2, text="Caracteres: 0")
    np = tk.Label(aba2, text="Palavras: 0")
    nblimpar = Button(aba2, text="Limpar", command=lambda: limpar())
    nbsalvar = Button(aba2, text="Salvar", command=lambda: salvar())
    nbabrir = Button(aba2, text="Abrir", command=lambda: abrir())
    nhelper = tk.Label(aba2, text="Escolha a fonte:")
    nlistbox = tk.Listbox(aba2)
    nlistbox.insert(0, "Arial")
    nlistbox.insert(0, "Tahoma")
    nlistbox.insert(0, "Georgia")
    nlistbox.insert(0, "Verdana")
    nbfonte = Button(aba2, text="ir", command=lambda: font())
    ntexto.pack()
    nl.pack()
    np.pack()
    nblimpar.pack()
    nbsalvar.pack()
    nbabrir.pack()
    nhelper.pack()
    nlistbox.pack()
    nbfonte.pack()
    ntexto.bind("<KeyPress>", lambda event: count())
application.title("Bloco de notas v3.0")
texto = tk.Text(aba1, height=15, width=40)
l = tk.Label(aba1, text="Caracteres: 0")
p = tk.Label(aba1, text="Palavras: 0")
blimpar = Button(aba1, text="Limpar", command=lambda:limpar())
bsalvar = Button(aba1, text="Salvar", command=lambda:salvar())
babrir = Button(aba1, text="Abrir", command=lambda:abrir())
helper = tk.Label(aba1, text="Escolha a fonte:")
listbox = tk.Listbox(aba1)
listbox.insert(0, "Arial")
listbox.insert(0, "Tahoma")
listbox.insert(0, "Georgia")
listbox.insert(0, "Verdana")
bfonte = Button(aba1, text="ir", command=lambda:font())
bnovo = Button(aba2, text="Nova aba", command=lambda:aba())
texto.pack()
l.pack()
p.pack()
blimpar.pack()
bsalvar.pack()
babrir.pack()
helper.pack()
listbox.pack()
bfonte.pack()
bnovo.pack()
application.bind("<KeyPress>", lambda event: count())

application.mainloop()
