# ler as idades e dizer quem é menor de idade

from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0
for pessoa in range(1, 8):
    ano_nasc= int(input(f'Em que ano a {pessoa}ª nasceu? '))
    id = ano_atual - ano_nasc
    if id <= 18:
        menores += 1
    else:
        maiores += 1
print(f'Ao todo tivemos {maiores} pessoas maiores e {menores} menores.')

