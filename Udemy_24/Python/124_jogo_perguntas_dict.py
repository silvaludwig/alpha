# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2 + 2?',
#         'Opções': ['1', '2', '4', '6'],
#         'Resposta': '4'
#     },
#     {
#         'Pergunta': 'Quanto é 3 + 2?',
#         'Opções': ['5', '2', '4', '6'],
#         'Resposta': '5'
#     },
#     {
#         'Pergunta': 'Quanto é 4 + 2?',
#         'Opções': ['1', '2', '4', '6'],
#         'Resposta': '6'
#     },
# ]


# for pergunta in perguntas:
#     print('PERGUNTA: ', pergunta['Pergunta'])
#     print()

#     for i, option in enumerate(pergunta['Opções']):
#         print(f'{i})', option)

#     print()

#     resposta = input('SUA RESPOSTA: ')

#     if resposta in pergunta['Resposta']:
#         print('ACERTOU MIZARAVEL!')
#     else:
#         print('QUE BURRO, DÁ ZERO PRA ELE!')



# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')

