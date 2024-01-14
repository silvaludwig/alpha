lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]
lista_soma = [
    x+y for x, y in zip(lista1, lista2)
]
print(lista_soma)

####################
# lista_soma = []

# for i in range(len(lista2)):
#     lista_soma.append(lista1[i] + lista2[i])

# print(lista_soma) 

####################

# lista_soma = []

# for i, _ in enumerate(lista2):
#     lista_soma.append(lista1[i] + lista2[i])

# print(lista_soma) 

###################

