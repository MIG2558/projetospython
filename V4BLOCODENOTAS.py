rom customtkinter import filedialog
from customtkinter import *

application = CTk()
def caracteres():
    input = texto.get("1.0", END)
    c = len(input) - 1
    label1.configure(text="Caracteres: {}".format(c))
def palavras():
    input = texto.get("1.0", END)
    p = len(input.split(' '))
    l2.configure(text="Palavras: {}".format(p))
def contar():
    caracteres()
    palavras()
def salvar():
    a = filedialog.asksaveasfile(filetypes=[("TXT", "*.txt")])
    if a is not None:
        input = texto.get("1.0", END)
        a.writelines(input)
def limpar():
    texto.delete("1.0", END)
def abrir():
    a = filedialog.askopenfile(filetypes=[("TXT", "*.txt")])
    if a is not None:
        conteudo = a.readlines()
        texto.delete('1.0', END)
        texto.insert('1.0', conteudo)
def fonte():
    fonte = combobox.get()
    size = int(cb2.get())
    if fonte.strip() and size < 24 and size > 0:
        texto.configure(font=(fonte, size))
centro = CTkTabview(application)
centro.pack()
centro.add("1° Documento.")
application.title("Bloco de notas v4.0")
texto = CTkTextbox(centro.tab("1° Documento."), bg_color="white", fg_color="white", text_color="black")
label1 = CTkLabel(centro.tab("1° Documento."), text="Caracteres: 0")
l2 = CTkLabel(centro.tab("1° Documento."), text="Palavras: 0")
bsalvar = CTkButton(centro.tab("1° Documento."), text="Salvar", command=lambda:salvar())
labelseparacao = CTkLabel(centro.tab("1° Documento."), text="-")
blimpar = CTkButton(centro.tab("1° Documento."), text="Limpar", command=lambda:limpar())
lseparacao = CTkLabel(centro.tab("1° Documento."), text="-")
babrir = CTkButton(centro.tab("1° Documento."), text="Abrir", command=lambda:abrir())
bhelper = CTkLabel(centro.tab("1° Documento."), text="Fonte/Tamanho")
combobox = CTkComboBox(centro.tab("1° Documento."), values=["Arial", "Tahoma", "Verdana", "Georgia"])
combobox.set(value=12)
cb2 = CTkComboBox(centro.tab("1° Documento."), values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])
combobox.set('Arial')
cb2.set('12')
texto.pack()
label1.pack()
l2.pack()
bsalvar.pack()
labelseparacao.pack()
blimpar.pack()
lseparacao.pack()
babrir.pack()
bhelper.pack()
combobox.pack()
bhelper.pack()
cb2.pack()
application.bind("<KeyRelease>", lambda event: contar())
application.bind("<Motion>", lambda event: fonte())

application.mainloop()
