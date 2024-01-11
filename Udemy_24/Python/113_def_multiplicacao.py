def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1,2,3,4,5,6)
print(multiplicacao)
print('-'*10)
print(1*2*3*4*5*6)


def even_uneven(numero):
    by2 = numero % 2 == 0

    if by2:
        return f'{numero} é par'
    return f'{numero} é impar'

print(even_uneven(2))
print(even_uneven(5))
print(even_uneven(1))
