import json

CAMINHO_ARQUIVO = 'aula206.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    

p1 = Pessoa('Carlos', 23)
p2 = Pessoa('Carla', 24)
p3 = Pessoa('Carlitos', 25)

bd = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii= False, indent= 2)

