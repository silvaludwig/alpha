class Intro:
    def __init__(self):
        self.intro = str(input('Oi! Meu nome é Jorge. Como vai vc? '))
        if self.intro in 'Nada bem' 'Péssimo' 'Triste' 'Horrível':
            print('Poxa... que pena! Melhoras aí!')
        else:
            print('É isso aí, bom demais!')
        
class Name:
    def __init__(self):
        self.name = str(input('Qual seu nome? '))
        if self.name in 'Maria' 'José' 'Pedro':
            print('Seu nome é bem comum')
        else:
            print('Muito prazer!')
        

class Age:
    def __init__(self):
        self.age = int(input('Quantos anos vc tem? '))
        if self.age > 18:
            print('já é maior de idade!')
        elif self.age < 18:
            print('Praticamente um bebê!')

class Job:
    def __init__(self):
        self.job = str(input('Trabalha com o que? '))
        if self.job in 'Nada' 'Por enquanto nada':
            job2 = input('Mas é por falta de opção? ')
            if job2 == 'Sim':
                print('Ah... mas fica firme que vai dar certo!')
            if job2 in 'Nao' 'Não' 'nao' 'não':
                print('Entendi...')
        else:
            print('Que legal!')
        
class Love:
    def __init__(self):
        self.love = str(input('E esse coraçãozinho aí... tem dono já? '))
        if self.love in 'Sim' 'sim' 'ja' 'aham''já':
            print('ah, o amor é lindo...')
        else:
            print('sua hora vai chegar bebê!')


    pass

#script de dialogo# 

user_intro = Intro()

user_name = Name()

user_age = Age()
    
user_job = Job()

user_love = Love()




