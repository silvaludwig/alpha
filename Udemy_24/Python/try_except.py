try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    c = input('[*][+][-][/]')  
 
    if c == '*':
        result = a * b
        print(result)
    elif c == '+':
        result = a + b
        print(result)
    elif c == '-':
        result = a - b
        print(result)
    elif c == '/':
        result = a / b
        print(result)

    while c not in '*-+/':
        print('Operador inválido')
        c = input('[*][+][-][/]') 


except Exception as error:
    print(error)

