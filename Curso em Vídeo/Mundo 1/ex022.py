# tratamento e analise de strings
nc = str(input('Nome completo: ')).strip()
print(f'Texto em MAIUSCULAS: {nc.upper()}')
print(f'Texto em minusculas: {nc.lower()}')
print(f'Quantidade de letras: {(len(nc)) - nc.count(" ")}')
print(f'Seu primeiro nome tem {nc.find(" ")} letras')