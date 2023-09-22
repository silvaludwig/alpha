# ex049 - tabuada usando o for

num = int(input('Digite um número pra ver a tabuada: '))
for c in range(1, 11):
    print(f'{num:02} x {c:02} = {num*c:02}')