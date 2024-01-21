class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        ...


p1 = Pessoa('Ludwig', 'Sousa e Silva')
# p1.nome = 'Ludwig'
# p1.sobrenome = 'Silva'

p2 = Pessoa('Joyce', 'Christine')
# p2.nome = 'Joyce'
# p2.sobrenome = 'Christine'


print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)

