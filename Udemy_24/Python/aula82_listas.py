""" Minha SOlução """

lista = ['Maria', 'Joana', 'Joyce']

lista.append('Joao')


for nome in lista:
    print(lista.index(nome), nome)


"""Solução do curso"""

lista2 = ['Fernanda', 'Renata', 'Joana']
lista2.append('Joaquina')

indices = range(len(lista2))


for indice in indices:
    print(indice, lista2[indice], type(lista2[indice]))


