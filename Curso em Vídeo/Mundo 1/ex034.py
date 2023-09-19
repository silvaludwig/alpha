# calculo de salário com condicional 

s = float(input('Salário atual: R$'))

if s >= 1500:
    ns = s + (s * 15) / 100
else:
    ns = s + (s * 20) / 100

print(f'quem ganhava {s} agora ganhará {ns}')