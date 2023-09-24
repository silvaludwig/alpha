# analisar uma lista de pesos e determinar o maior

for pessoa in range(1, 6):
    peso = float(input(f'Qual o peso da {pessoa}ª pessoa?'))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso é {maior:.2f}kg, o menor é {menor:.2f}kg')
