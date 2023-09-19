# identificar o maior e menor valor

n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero: '))
n3 = int(input('terceiro numero: '))

# verificando o menor valor 

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2: 
    menor = n3

# verificando o maior valor 

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2: 
    maior = n3

print(f'o maior valor é {maior}')
print(f'o menor valor é {menor}')
