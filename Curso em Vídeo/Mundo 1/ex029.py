v = int(input('Velocidade do carro: '))
m = (v - 80) * 7
if v > 80:
    print('Tomou bonitão!')
    print(f'Receba seus R${m} de multa!')
else:
    print('Ta safe. Boa viagem!')