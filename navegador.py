import webbrowser
from tkinter import *
import tkinter as tk
from tkinter import ttk

application = tk.Tk()
application.title("Navegador")
application.geometry("200x200")
navegador = ttk.Notebook(application)
tab1 = ttk.Frame(navegador)
tab2 = ttk.Frame(navegador)
navegador.pack(expand=True, fill='both')
navegador.add(tab1, text="Nova aba")
navegador.add(tab2, text="+")
label = tk.Label(tab1, text="Digite um URL:")
def url():
    input = entry.get()
    webbrowser.open(input)
l = tk.Label(tab1, text="Digite um URL:")
entry = tk.Entry(tab1)
button = Button(tab1, text="ir", command=lambda:url())
l2 = tk.Label(tab1, text="Ou, pesquise:")
def pesquisar():
    input2 = entry2.get()
    webbrowser.open("https://www.google.com/search?q={}".format(input2))
entry2 = tk.Entry(tab1)
b2 = Button(tab1, text="ir", command=lambda:pesquisar())
def aba():
    l = tk.Label(tab2, text="Digite um URL:")
    entry = tk.Entry(tab2)
    button = Button(tab2, text="ir", command=lambda:url())
    l2 = tk.Label(tab2, text="Ou, pesquise:")
    entry2 = tk.Entry(tab2)
    b2 = Button(tab2, text="ir", command=lambda:pesquisar())
    l.pack()
    entry.pack()
    button.pack()
    l2.pack()
    entry2.pack()
    b2.pack()
    novaaba.destroy()
def mudarnome():
    index = navegador.index(navegador.select())
    navegador.tab(index, text="Nova aba")
def criaraba():
    aba()
    mudarnome()
novaaba = Button(tab2, text="Nova aba", command=lambda:criaraba())
l.pack()
entry.pack()
button.pack()
l2.pack()
entry2.pack()
b2.pack()
novaaba.pack()

application.mainloop()
