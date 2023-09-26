# jogo advinhação 028 com while

from random import randint  


print('''Oi! Sou seu computador...
Vou pensar em um número de 0 a 10.
Tente advinhar!''')
computador = randint(0, 10)
jogador = int(input('Seu palpite: '))
while jogador != computador: 
    if jogador > computador:
        print('Menos...')
        jogador = int(input('Seu palpite: '))
    if jogador < computador:
        print('Mais...')
        jogador = int(input('Seu palpite: '))
    if jogador == computador:
        print('Acertou! ')