from tkinter import *
import tkinter as tk
from tkinter import filedialog

def limpa():
    texto.delete("1.0", END)
application = tk.Tk()
application.title("BLOCO DE NOTAS")
def abrirarqv():
    a = filedialog.askopenfile()
    content = a.readlines()
    if a is not None:
        texto.delete("1.0", END)
        texto.insert("1.0", content)
def fsalvar():
    b = filedialog.asksaveasfile()
    content2 = texto.get("1.0", END)
    if b is not None:
        b.writelines(content2)
def update_label():
    length = len(texto.get("1.0", END)) - 1
    label.config(text="Caracteres: {}".format(length))
def palupdate_label():
    plength = len(texto.get("1.0", END).split())
    label2.config(text="Palavras: {}".format(plength))
def atualizatudo():
    update_label()
    palupdate_label()
def leitura():
    texto.config(state="disabled")
def enable():
    texto.config(state="normal")
label = tk.Label(application, text="Caracteres: 0")
label2 = tk.Label(application, text="Palavras: 0")
texto = tk.Text(application)
abrir = Button(application, text="Abrir", command=lambda:abrirarqv())
salvar = Button(application, text="Salvar", command=lambda:fsalvar())
limpar = Button(application, text="Limpar", command=lambda:limpa())
modoleitura = Button(application, text="Modo leitura", command=lambda:leitura())
buttonenable = Button(application, text="Modo de edição", command=lambda:enable())
modoleitura.pack()
buttonenable.pack()
texto.pack()
label.pack()
label2.pack()
abrir.pack()
salvar.pack()
limpar.pack()
texto.bind("<KeyPress>", lambda event: atualizatudo())
texto.bind("<Control-s>", lambda event: fsalvar())
texto.bind("<Control-o>", lambda event: abrirarqv())

application.mainloop()
