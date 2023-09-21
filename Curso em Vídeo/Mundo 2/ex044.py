# ex044 - simulador caixa loja
compras = float(input('Preço das compras: R$'))
desconto = (compras * 5) / 100
juros = (compras * 3) / 100
pagamento = int(input('''Escolha a opção de pagamento:
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista crédito 
[ 3 ] parcelado crédito '''))

if pagamento == 1:
    print(f'Sua compra de R${compras} vai custar R${compras - desconto} pagando à vista no dinheiro ou pix')
elif pagamento ==2:
    print(f'Sua compra de R${compras} vai custar R${compras + juros} pagando à vista no crédito.')
elif pagamento ==3:
    parcelas = int(input('Em quantas parcelas? '))
    juros_compras = compras + (juros * parcelas)
    print(f' Sua compra de R${compras} vai custar R${juros_compras} em {parcelas}x de R${juros_compras / parcelas}!')