# alistamento militar
from datetime import date
nasc = int(input('Que ano nasceu? '))
ano = date.today().year
idade = ano - nasc
if idade == 18:
    print(f'vc tem {idade} anos, deve se alistar!')
elif idade < 18:
    print(f'vc tem {idade} anos, não deve se alistar.')
elif idade > 18:
    print(f'vc tem {idade} anos, deveria ter se alistado há {idade - 18} anos.')


