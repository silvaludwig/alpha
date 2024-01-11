def multiplicar(numero):
    def fator(fator):
        if fator == 2:
            return f'o dobro de {numero} é:', numero * 2
        elif fator == 3:
            return f'o triplo de {numero} é:', numero * 3
        elif fator == 4:
            return f'o quadruplo de {numero} é:', numero * 4
    return fator


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)

print(dobro(2))
print(triplo(2))


