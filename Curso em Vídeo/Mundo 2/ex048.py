# ex048 - de 1 a 500,  somando os impares múltiplos de três. 

soma = 0
cont = 0
for c in range(1, 501, 2):
 if c % 3 == 0:
  soma += c
  cont += 1
print(f'A soma dos {cont} valores é {soma}.')
