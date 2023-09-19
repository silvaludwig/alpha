# verificar se o ano é bissexto 

from datetime import date
a = int(input('Que ano? 0 para o ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'o ano {a} é BISSEXTO')
else:
    print(f'o ano {a} NÃO É BISSEXTO')
