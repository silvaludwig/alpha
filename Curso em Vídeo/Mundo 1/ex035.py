# análise se forma triangulo 

r1 = float(input('primeira reta: '))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: 
    print('os segmentos PODEM FORMAR triangulo')
else: 
    print('os segmentos NÃO PODEM FORMAR triangulo')

