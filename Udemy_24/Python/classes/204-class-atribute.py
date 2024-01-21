class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    


p1 = Pessoa('João', 30)
p2 = Pessoa('Pedro', 10)

print(f'{p1.nome} tem {p1.idade} anos e nasceu em {p1.get_ano_nascimento()}')
print(f'{p2.nome} tem {p2.idade} anos e nasceu em {p2.get_ano_nascimento()}')

