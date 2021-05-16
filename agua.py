#Instalar a biblioteca pygame (para o som)
#"py.exe -m pip install pygame" no cmd do windows

#Max

from tkinter import *
import pygame

root = Tk()

root.title('Beba água')

win_width, win_height = 360, 180

root.geometry('360x220+500+250')
root.resizable(False, False)
root.iconbitmap('bebaagua\water.ico')

frame1 = Frame(root, 
bg = '#48cae4'
)
frame1.place(relwidth = 1, 
relheight = 1
)

text = Label(root, 
wraplength = win_width,
bg = '#48cae4',
text='Vou te lembrar de beber água a cada 1 minuto. \n💧💧💧', 
font = 'Poppins'
)
text.pack()

text2 = Label(root, 
wraplength = win_width,
bg = '#48cae4',
font = 'Poppins 10'
)
text2.pack()   

pygame.mixer.init()

def som():
    pygame.mixer.music.load(r'bebaagua\bebeagua.mp3')
    pygame.mixer.music.play()
    root.after(60000, som)
    StopIteration

def sair():
    root.destroy()

botaoComecar = Button(root,
text = 'Começar/Reiniciar', 
font = 'Poppins', 
command=som
)
botaoComecar.pack(pady = 5)

botaoSair = Button(root, 
text = 'Sair',
font = 'Poppins',
command=sair
)
botaoSair.pack(pady = 5)

root.mainloop()