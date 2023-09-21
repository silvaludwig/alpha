# Pedra, papel tesoura
import random
from time import sleep


print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jog = int(input('Qual a sua jogada? '))
comp = random.randint(0, 2)
itens = ('PEDRA', 'PAPEL', 'TESOURA')

print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA!!!')

print('='*30)
print(f'Você jogou {itens[jog]}')
print(f'O computador escolheu {itens[comp]}')
print('=' *30)

if comp == 0: #PEDRA
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('VOCÊ VENCEU')
    elif jog == 2:
        print('COMPUTADOR VENCEU')
elif comp == 1: #PAPEL
    if jog == 0:
        print('COMPUTADOR VENCEU')
    elif jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('VOCÊ VENCEU')
elif comp == 2: #TESOURA
    if jog == 0:
        print('VOCÊ VENCEU')
    elif jog == 1:
        print('COMPUTADOR VENCEU')
    elif jog == 2:
        print('EMPATE')