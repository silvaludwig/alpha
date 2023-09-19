# jogo de advinhação 
from random import randint
nc = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
nj = int(input('Em que número estou pensando? '))
if nj == nc:
    print('PARABÉNS! Vc acertou!')
else:
    print(f'GANHEI! Pensei no número {nc}!')
