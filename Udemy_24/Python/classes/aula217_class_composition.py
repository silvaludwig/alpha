class Client:
    def __init__(self, name):
        self.name = name
        self.addresses = []

    def insert_adress(self, street, number):
        self.addresses.append(Address(street, number))

    def list_addresses(self):
        for address in self.addresses:
            print(address.street, address.number)

    
class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number



client1 = Client('Maria')
client1.insert_adress('Rua dos Bobos', 0)
client1.insert_adress('Rua das Gaiolas', 38)
client1.list_addresses()

# print(client1.addresses[0].street, client1.addresses[0].number)



