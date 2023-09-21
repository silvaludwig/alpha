# ex043 - calculo de IMC com status
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu imc é de {imc:.1f}. ABAIXO DO PESO!')
elif 18.5 < imc <= 25:
    print(f'Seu imc é de {imc:.1f}. PESO IDEAL')
elif 25 < imc <= 30:
    print(f'Seu imc é de {imc:.1f}. SOBREPESO')
elif 30 < imc <= 40:
    print(f'Seu imc é de {imc:.1f}. OBESIDADE ')
else:
    print(f'Seu imc é de {imc:.1f}. OBESIDADE MORBIDA')