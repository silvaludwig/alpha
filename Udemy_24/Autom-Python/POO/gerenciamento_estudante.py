class Estudante:
    def __init__(self, nome, idade, nota) -> None:
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def get_nome(self): # metodo getter atributo nome
        return self.nome # retorna o atributo nome
    
    def set_nome(self, nome): # metodo setter atributo nome
        self.nome = nome # atualiza o atributo nome
    
    def get_idade(self): # metodo getter atributo idade
        return self.idade # retorna o atributo idade
    
    def set_idade(self, idade): # metodo setter atributo idade
        self.idade = idade # atualiza o atributo idade

    def get_nota(self): # metodo getter atributo nota
        return self.nota # retorna o atributo nota
    
    def set_nota(self, nota): # metodo setter atributo nota
        self.nota = nota # atualiza o atributo nota


def menu():
    alunos_cadastrados = []
    while True:    
        print('1. NOVO CADASTRO')
        print('2. ATUALIZAR NOTA')
        print('3. VIZUALIZAR CADASTRO')
        print('4. APAGAR CADASTRO')
        print('5. SAIR DO SISTEMA')
        print('---------------------------')

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            nome = input('Nome do aluno: ')
            idade = int(input('Idade do aluno: '))
            nota = float(input('Nota do aluno: '))
            novo_aluno = Estudante(nome, idade, nota)
            alunos_cadastrados.append(novo_aluno)
            print(f'{nome} cadastrado com sucesso!')

        elif escolha == '2':
            for aluno in alunos_cadastrados:
                if aluno.get_nome() == nome:
                    nova_nota = float(input('Atualizar nota: '))
                    aluno.set_nota(nova_nota)
                    print('Nota atualizada com sucesso!')
                    break
            else:
                print('Aluno não encontrado!')

        elif escolha == '3':
            print('==============================')
            nome = input('Digite o nome do aluno a consultar: ')
            for aluno in alunos_cadastrados:
                if aluno.get_nome() == nome:
                    print(f'Nome: {aluno.get_nome()}\nIdade: {aluno.get_idade()}\nNota: {aluno.get_nota()} ')
                    break
            else:
                print('Aluno não encontrado!')

        elif escolha == '4':
            print('Listando todos os alunos cadastrados!')
            print('==============================')
            for aluno in alunos_cadastrados:
                print(f'Nome: {aluno.get_nome()}\nIdade: {aluno.get_idade()}\nNota: {aluno.get_nota()} ')
            

        elif escolha == '5':
            print('Saindo do sistema.')        
            break

        else:
            print('Opção inválida')

if __name__ == '__main__':
    menu()
