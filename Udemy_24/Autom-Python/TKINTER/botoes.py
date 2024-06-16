from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title('botoes')


def enviar():
    print('dados enviados com sucesso')

def mensagem_messagebox():
    messagebox.showinfo('titulo', 'mensagem')

botao_enviar = Button(janela, text='enviar').pack()
botao_enviar_com_funcao = Button(janela, text='enviar com função', command=mensagem_messagebox).pack()
botao_sair = Button(janela, text='sair', command=janela.destroy).pack(side=BOTTOM)

botao_verde = Button(janela, text='VERDE', bg='green', fg='white').pack(side=LEFT)
botao_vermelho = Button(janela, text='VERMELHO', bg='red', fg='white').pack(side=LEFT)


janela.mainloop()