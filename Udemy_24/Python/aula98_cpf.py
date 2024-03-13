# 441.577.010-03

cpf = '36778540087'
nove_digitos = cpf[:9]
contador_regressivo = 10

resultado = 0
for digito_1 in nove_digitos:
    resultado += int(digito_1) * contador_regressivo 
    contador_regressivo -= 1

digito_1 = (resultado * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

print(f'o primeiro digito do CPF <{cpf}> é <{digito_1}>')


dez_digitos = cpf[:9] + str(digito_1)
contador_regressivo_2 = 11

resultado_2 = 0
for digito_2 in dez_digitos:
    resultado_2 += int(digito_2) * contador_regressivo_2 
    contador_regressivo_2 -= 1

digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = nove_digitos + str(digito_1) + str(digito_2)

print(f'o segundo digito do CPF <{cpf}> é <{digito_2}>')

print(cpf_gerado)

if cpf == cpf_gerado:
    print(f'o cpf: <{cpf}> é válido')
else:
    print(f'o cpf: <{cpf}> NÃO é válido')
    