# sequencia fibonacci

n = int(input('Quantos termos vc quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} > {t2} ', end='')
contador = 3
while contador <= n:
    t3 = t1 + t2
    print(f' > {t3}', end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' > FIM do programa' )
