# verificar a média e se for:
# abaixo de 5.0, reprovado
# entre 5.0 e 6.9, recuperação
# a partir de 7.0, aprovado

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2

if m <= 5:
    print(f'Sua média foi {m:.1f}, REPROVADO!')
elif 6.9 > m >= 5:
    print(f'Sua média foi {m:.1f}, RECUPERAÇÃO!')
elif m >= 7:
    print(f'Sua média foi {m:.1f}, APROVADO!')
