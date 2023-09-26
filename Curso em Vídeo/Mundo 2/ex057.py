# validação de dados

sexo = str(input('Sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf':
    print('INVALIDO!')
    sexo = str(input('Sexo [M/F]: '))
print(f'Sexo ({sexo}) registrado com sucesso!')
