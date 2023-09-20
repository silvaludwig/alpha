# aprovando financiamento

vlr_imovel = float(input('Valor do imóvel: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financiamento? '))
prestação = vlr_imovel / (tempo * 12)
print(f'Para pagar uma casa de {vlr_imovel} em {tempo} anos, a prestação será de R${prestação:.2f}')
if prestação > (salario / 3):
    print('Financiamento NEGADO!')
else:
    print('Financiamento APROVADO!')
