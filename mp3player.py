import pygame
from customtkinter import *

pygame.init()
pygame.mixer.init()

application = CTk()
def lermp3():
    a = filedialog.askopenfile(filetypes=[("MP3", "*.mp3")])
    if a:
        pygame.mixer.music.load(a.name)
        def loaded():
            label.configure(text='Loaded {}'.format(a.name))
        def play():
            pygame.mixer.music.play()
        def pause():
            pygame.mixer.music.pause()
        def unpause():
            pygame.mixer.music.unpause()
        while pygame.mixer.music.get_busy():
            continue
        label = CTkLabel(application, text='Loading {}...'.format(a.name))
        label.pack()
        application.after(1200, loaded)
        lseparacao = CTkLabel(application, text='--')
        bplay = CTkButton(application, text='Play', command=lambda:play())
        bpause = CTkButton(application, text='Pause', command=lambda:pause())
        bunpause = CTkButton(application, text='Unpause', command=lambda:unpause())
        lseparacao2 = CTkLabel(application, text='--')
        def salvar():
            b = filedialog.asksaveasfile(filetypes=[('TXT', '*.txt')])
            if b:
                b.write(a.name)
                from tkinter import messagebox
                messagebox.showinfo('sucesso', 'salvo')
            else:
                from tkinter import messagebox
                messagebox.showerror('arquivo não encontrado', 'tente novamente')
        bsalvar = CTkButton(application, text='Salvar nome da música', command=lambda:salvar())
        lseparacao.pack()
        bplay.pack()
        bpause.pack()
        bunpause.pack()
        lseparacao2.pack()
        bsalvar.pack()
button = CTkButton(application, text='Select MP3', command=lambda:lermp3())
button.pack()

application.mainloop()
