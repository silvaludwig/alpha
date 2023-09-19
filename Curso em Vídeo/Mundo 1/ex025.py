# tratamento e validação de strings (again)
name = str(input('Seu nome completo: ')).strip()
print(f'Seu nome tem Silva? {"SILVA" in name.upper()}')