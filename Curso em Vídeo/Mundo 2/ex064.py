# somando valores desconsiderando o flag
soma = cont = n = 0
n = int(input('Digite um número: '))

while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: '))
    
print(f'vc digitou {cont} números, o total é {soma}')
