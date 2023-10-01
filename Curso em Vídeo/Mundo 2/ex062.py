# progressão aritmética usando while

numero = int(input('primeiro termo: '))
razao = int(input('razão da PA: '))
termo = numero
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} > ', end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais vc quer ver? '))
print(f'FIM DO PROGRAMA com {total} termos mostrados.')
