# ex050 - ler seis números e somar só os pares 
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'a soma dos números pares digitatos é {soma}')
