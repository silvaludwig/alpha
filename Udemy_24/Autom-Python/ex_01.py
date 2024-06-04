"""
Exercício Análise de Números

Objetivo: Desenvolver um programa que solicita ao usuário a entrada de 
um número e, com base nesse número, realiza as seguintes operações:

    1. Mostrar o número informado.
    2. Informar se o número é par ou ímpar.
    3. Informar se o número é positivo, negativo ou zero.
    4. Se o número for positivo, calcular e mostrar sua raiz quadrada.

"""

# ask for a number
number = float(input('Input a number: '))

# showing the number
print(f"the number is: {number}")

# is it an even number:
if number % 2 == 0:
    print(f"{number} it's EVEN" )
else:
    print(f"{number} it's NOT EVEN")

# positive, negative or 0
if number == 0:
    print(f"{number} is zero")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is positive")


