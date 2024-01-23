class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    # def get_cor(self):
    #     return self.cor
    
    @property
    def cor(self):
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 'Mesma cor da tinta'

caneta = Caneta('Azul')

print(caneta.cor)  
print(caneta.cor_tampa)  

# print(caneta.get_cor())
