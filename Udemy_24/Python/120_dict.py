pessoa = {
    'nomes': ['Joyce Cristina', 'Ludwig', 'Ricardo'],
    'sobrenomes': ['Ferreira', 'Sousa e Silva', 'Nocera'],
    'idades': [26, 30, 48],
}

print(pessoa['nomes'])
print(pessoa['nomes'][0], pessoa['sobrenomes'][0], pessoa['idades'][0])
print()
for chave in pessoa:
    print(chave, pessoa[chave])


