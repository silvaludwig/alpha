# analise e tratamento de valores

print('Seja bem vindo! ')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('><'*12)
fim = False
while not fim:
    usuário = int(input('''Dentre as opções abaixo:
[ 1 ] SOMA DOS VALORES
[ 2 ] QUAL É MAIOR?
[ 3 ] QUAL O PRODUTO?
[ 4 ] NOVOS VALORES
[ 5 ] SAIR DO PROGRAMA
>>>>>> Qual sua opção? '''))
    if usuário == 1:
        print(f'A soma entre {n1} e {n2} é ', (n1 + n2))
        print('><'*12)
    elif usuário == 2:
        if n1 > n2:
            maior = n1
            print(f'Entre {n1} e {n2}, o maior valor é {maior}.')
            print('><'*12)
        elif n1 < n2:
            maior = n2
            print(f'Entre {n1} e {n2}, o maior valor é {maior}.')
            print('><'*12)
        elif n1 == n2:
            print('Os valores são iguais.')
            print('><'*12)
        
    elif usuário == 3:
        print(f'O produto entre {n1} e {n2} é ', (n1 * n2))
        print('><'*12)
    elif usuário == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif usuário == 5:
        fim = True
        print('Fim do programa! Obrigado.')
        print('><'*12)
    else:
        print('Opção inválida!')
        print('><'*12)

