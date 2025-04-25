from customtkinter import *
import os

application = CTk()
centro = CTkTabview(application)
centro.pack()
centro.add('IDE Python')
centro.add('Terminal')
def executar():
    input = texto.get("1.0", END)
    try:
        def destruir():
            textocertopy.destroy()
        exec(input)
        textocertopy = CTkTextbox(centro.tab('IDE Python'))
        textocertopy.insert("1.0", "Código executado com sucesso")
        textocertopy.configure(state='disabled')
        textocertopy.pack()
        application.after(2000, destruir)
    except Exception as e:
        def destruir():
            textoerropy.destroy()
        textoerropy = CTkTextbox(centro.tab('IDE Python'))
        textoerropy.insert("1.0", "{}".format(e))
        textoerropy.configure(state='disabled')
        textoerropy.pack()
        application.after(2000, destruir)
def execos():
    def destruir():
        textocertoos.destroy()
    input = txt2.get('1.0', END)
    if input.strip():
        os.system(input)
        textocertoos = CTkTextbox(centro.tab('Terminal'))
        textocertoos.insert('1.0', 'Comando executado')
        textocertoos.configure(state='disabled')
        textocertoos.pack()
        application.after(2000, destruir)
application.title('IDE/Terminal')
texto = CTkTextbox(centro.tab('IDE Python'))
b1 = CTkButton(centro.tab('IDE Python'), text='Execute', command=lambda: executar())
txt2 = CTkTextbox(centro.tab('Terminal'))
b2 = CTkButton(centro.tab('Terminal'), text="Executar", command=lambda: execos())
texto.pack()
b1.pack()
txt2.pack()
b2.pack()

application.mainloop()
