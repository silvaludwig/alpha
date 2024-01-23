class Pessoa:
    ano = 2024 #atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_anonima(cls, idade):
        return cls('Anônima', idade)
    
    @classmethod
    def criar_50_anos(cls, nome):
        return cls(nome, 50)
    

p1 = Pessoa.criar_50_anos('Maria')
p2 = Pessoa.criar_anonima(25)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)

