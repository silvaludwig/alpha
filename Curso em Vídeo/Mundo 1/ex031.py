# calculo de preço/km percorrido

km = int(input('Quantos Km de viagem? '))
p1 = km * 5
p2 = km * 4

if km >= 200:
    print(f'o custo total é R${p2}')
elif km < 200:
    print(f'o custo total é R${p1}')
