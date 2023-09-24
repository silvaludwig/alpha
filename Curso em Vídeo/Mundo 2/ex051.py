print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)

t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = t + (10 - 1) * r
for c in range(t, d + r, r):
    print(c, end=' > ')

print('acabou')
