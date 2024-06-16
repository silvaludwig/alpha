from tkinter import *

janela = Tk()
janela.title('teste')


for linha in range(5):
    for coluna in range(3):
        tabela = Frame(
            master=janela,
            relief=SUNKEN,
            borderwidth=5,
            )
        tabela.grid(row=linha, column=coluna)
        label_teste = Label(
              master=tabela, 
              text= f'linha {linha} \ncoluna {coluna}', 
              fg='black'
              )
        label_teste.grid(row=0, column=0)

janela.mainloop()

