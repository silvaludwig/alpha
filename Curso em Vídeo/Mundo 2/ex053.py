# identificando um palindromo

fr = str(input('Digite uma frase: ')).strip().upper()
pl = fr.split()
jt = ''.join(pl)
inv = ''
for lt in range(len(jt) - 1, -1, -1):
    inv += jt[lt]
print(f'O inverso de {jt} é {inv}')
if inv == jt:
    print('Temos um palindromo!')
else:
    print('A frase n é um palindromo')

