# analise de dados completa

#coleta de dados
si = 0
mi = 0
hmv = 0
nhmv = ''
mm20a = 0
for p in range(1, 5):
    print('-'*12, f'{p}ª PESSOA', '-'*12)
    nome = str(input('NOME: ')).strip().upper()
    idade = int(input('IDADE: '))
    genero = str(input('GENERO [M/F]: ')).strip().upper()
    si += idade
    if p == 1 and genero in 'Mm':
        hmv = idade
        nhmv = nome
    if genero in 'Mm'and idade > hmv:
        hmv = idade
        nhmv = nome
    if genero in 'Ff' and idade < 20:
        mm20a += 1
# média de idade do grupo
mi = si /  4
print(f'a média de idade do grupo é de {mi} anos')
# homem mais velho
print(f'o homem mais velho é {nhmv}.')
# mulheres abaixo de 20
print(f'ao todo são {mm20a} mulheres com menos de 20 anos.')
# fim do programa
print('-'*10, 'FIM DO PROGRAMA', '-'*10)
