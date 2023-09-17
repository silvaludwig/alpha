# calculo de aluguel de carro

d = int(input('Quantos dias ficou com o carro? '))
km = int(input('Quantos Km andou? '))
vkm = km * 1.5
vd = d * 25
vt = vkm + vd

print(f'O valor total da locação é de R${vt}.')

