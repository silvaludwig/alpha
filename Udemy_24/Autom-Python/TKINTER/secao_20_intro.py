from tkinter import *

janela = Tk() #instanciando e criando a janela
janela.title('Teste de interface') #titulo da janela

label_teste = Label(text='teste de label simples') #cria uma caixa de texto simples
label_teste.pack() #joga o texto na tela
label_teste2 = Label(text='teste de label FLAT', relief=FLAT) #cria uma caixa de texto sem relevo
label_teste2.pack() #joga o texto na tela
label_teste3 = Label(text='teste de label GROOVE', relief=GROOVE) #cria uma caixa de texto
label_teste3.pack() #joga o texto na tela
label_teste4 = Label(text='teste de label SUNKEN', relief=SUNKEN) #cria uma caixa de texto
label_teste4.pack() #joga o texto na tela
label_teste5 = Label(text='teste de label RAISED', relief=RAISED) #cria uma caixa de texto
label_teste5.pack() #joga o texto na tela
label_teste6 = Label(text='teste de label RIDGE', relief=RIDGE) #cria uma caixa de texto
label_teste6.pack() #joga o texto na tela
label_teste7 = Label(text='label com fundo verde', bg='green') #cria uma caixa de texto com fundo verde
label_teste7.pack() #joga o texto na tela
label_teste8 = Label(text='label com fonte rosa', fg='pink') #cria uma caixa de texto com a fonte amarela
label_teste8.pack() #joga o texto na tela
label_teste9 = Label(text='fundo preto e fonte branca', bg='black', fg='white') #cria uma caixa de texto com fundo preto e fonte branca
label_teste9.pack() #joga o texto na tela
label_teste10 = Label(text='mudando a fonte/tamanho', font='Times 20') #cria uma caixa de texto com fonte Times tamanho 20
label_teste10.pack() #joga o texto na tela
label_teste11 = Label(text='testando borderwidth 5', relief=SUNKEN, borderwidth=5, font='Arial 30', bg='orange', fg='red') #cria uma label com borda mais grossa (laele)
label_teste11.pack() #joga o texto na tela

texto_exemplo = """Qualquer texto aqui de exemplo
Com quebra de linha pra ficar supimpa
Programar é escrever coisas
muitas vezes sem sentido
E TÁ TUDO BEM!
ou não"""
label_teste12 = Label(
    text=texto_exemplo,
    font='Verdana 15 bold',
    bg='green',
    fg='white',
    relief=GROOVE,
).pack()



janela.mainloop() #mantendo a janela aberta
