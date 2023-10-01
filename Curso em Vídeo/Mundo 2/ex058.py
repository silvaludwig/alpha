# jogo advinhação 028 com while

from random import randint  

# MINHA SOLUÇÃO #
# print('''Oi! Sou seu computador...
# Vou pensar em um número de 0 a 10.
# Tente advinhar!''')
# computador = randint(0, 10)
# tentativas = 0
# jogador = int(input('Seu palpite: '))
# while jogador != computador: 
#     tentativas += 2
#     if jogador > computador:
#         print('Menos...')
#         jogador = int(input('Seu palpite: '))
#     if jogador < computador:
#         print('Mais...')
#         jogador = int(input('Seu palpite: '))
#     if jogador == computador:
#         print(f'Parabéns! Acertou em {tentativas} tentativas! ')

# SOLUÇÃO DO CURSO # 
print('''Oi! Sou seu computador...
      Vou pensar em um número de 0 a 10.
      Tente advinhar!''')
computador = randint(0,10)
tentativas = 0
acertou = False
while not acertou:
    jogador = int(input('Seu palpite: '))
    tentativas += 1
    if jogador == computador:
        acertou = True
        print(f'Acertou em {tentativas} tentativas!')
    elif jogador > computador:
        print('Menos...')
    else:
        print('Mais...')

