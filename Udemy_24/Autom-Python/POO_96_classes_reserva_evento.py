class Evento:
    def __init__(self, capacidade=10):
        self.capacidade = capacidade
        self.lugares_disponiveis = capacidade

    def reservar(self):
        if self.lugares_disponiveis == 0:
            print("Não há lugares disponíveis")
            return
        
        self.lugares_disponiveis -= 1
        print("reservado com sucesso!")

    
    def cancelar(self):
        if self.lugares_disponiveis == self.capacidade:
            print("Não há reservas para cancelar")
            return
        self.lugares_disponiveis += 1
        print("---Reserva cancelada com sucesso---")
        

    def mostrar_lugares_disponiveis(self):
        print(f"---lugares disponíveis: {self.lugares_disponiveis}---")

evento = Evento()

def menu():
    while True:    
        print("Seja bem vindo ao menu de reservas!")
        print("\n1. Reservar um Lugar \n2. Cancelar uma reseva \n3. Lugares disponíveis. \n4. Sair do sistema")
        escolha = input("\nEscolha uma das opções acima: ")
        
        if escolha == "1":
            evento.reservar()

        elif escolha =="2":
            evento.cancelar()

        elif escolha =="3":
            evento.mostrar_lugares_disponiveis()

        else:
            print("=> OBRIGADO! <=")
            return False
        
menu()