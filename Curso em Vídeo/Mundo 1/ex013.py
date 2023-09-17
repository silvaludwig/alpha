# Calculo de aumento salarial
s = float(input('Salário atual: R$'))
a = float(input('% de aumento: '))
ns = s + (s*a) / 100

print(f'vc ganhava R${s}, mas com o aumento de {a}% seu salário passa a ser R${ns}.')