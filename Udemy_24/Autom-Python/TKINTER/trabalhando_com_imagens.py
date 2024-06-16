from tkinter import *
from PIL import ImageTk, Image

janela = Tk()
janela.title('trabalhando com imagens') # texto no titulo da janela
janela.geometry("3840x2160") # define o tamanho da janela


Label(janela, text='imagem', font='Verdana 15').pack() # adiciona um label com o texto sair com fonte e tamanhos definidos


botao_sair = Button(janela, text='sair', command=janela.destroy).pack(side=BOTTOM)

imagem_sair = ImageTk.PhotoImage(Image.open('C:\\Users\\Ludwig\\Desktop\\git-repo\\alpha\\Udemy_24\\Autom-Python\\TKINTER\\SAIR.jpg'))
imagem_fundo = ImageTk.PhotoImage(Image.open('C:\\Users\\Ludwig\\Desktop\\git-repo\\alpha\\Udemy_24\\Autom-Python\\TKINTER\\rick_alone.jpg'))

plano_de_fundo = Label(image=imagem_fundo).place(x=0, y=0)


botao_sair_com_imagem = Button(image=imagem_sair, command=janela.destroy).pack()

janela.mainloop()