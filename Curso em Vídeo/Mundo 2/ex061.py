# progressão aritmética usando while

n = int(input('primeiro termo: '))
r = int(input('razão da PA: '))
t = n
c = 1
while c <= 10:
    print(f'{t} > ', end='')
    t += r
    c += 1
