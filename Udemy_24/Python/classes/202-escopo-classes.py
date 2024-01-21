class Animal:

    def __init__(self, nome):
        self.nome = nome

    def comer(self, alimento):
        return f'{self.nome} está comendo {alimento}'


leao = Animal('Leão')

print(leao.nome)
print(leao.comer('gazela'))


