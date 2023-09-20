# classificação por idade
from datetime import date
for c in range(1,6): #pra testar todas as possibilidades
    nasc = int(input('Ano de nascimento: '))
    ano = date.today().year
    idade = ano - nasc

    if idade <= 9:
        print(f'com {idade} anos, MIRIM')
    elif 10 < idade <= 14:
        print(f'com {idade} anos, INFANTIL')
    elif 15 < idade <= 19:
        print(f'com {idade} anos, JUNIOR')
    elif 20 < idade <= 25:
        print(f'com {idade} anos, SÊNIOR')
    else: 
        print(f'com {idade} anos, MASTER')
