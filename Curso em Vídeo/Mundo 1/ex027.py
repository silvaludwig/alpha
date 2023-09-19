# analise e tratamento de strings still
n = str(input('Seu nome: ')).strip()
nc = n.split()
print(f'Seu primeiro nome é {nc[0]}')
print(f'Seu último nome é {nc[len(nc)-1]}')
