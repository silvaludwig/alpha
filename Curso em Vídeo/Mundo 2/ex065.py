# ler vários números > calcular a média > mostrar maior/menor > usuário escolhe se continua ou não

numero = contador = 0 
continuar = ''

numero = int(input('Digite um número: '))
continuar = str(input('Quer continuar? [S/N]' )).strip().upper()
# if continuar not in 'SN':
#     print('OPÇÃO INVÁLIDA!')

while continuar not in 'Nn':
    contador += 1
    numero = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N]' )).strip().upper()
    if continuar not in 'SN':
        print('OPÇÃO INVÁLIDA!')
print('FIM DO PROGRAMA')
    
    

