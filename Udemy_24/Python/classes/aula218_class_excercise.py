class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None
        self._manufactor = None
    
    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, value):
        self._engine = value

    @property
    def manufactor(self):
        return self._manufactor
    
    @manufactor.setter
    def manufactor(self, value):
        self._manufactor = value


class Engine:
    def __init__(self, name):
        self.name = name


class Manufactor:
    def __init__(self, name):
        self.name = name

    
voyage = Car('Voyage')
stilo = Car('Stilo Sporting')
engine_1_6 = Engine('1.6')
engine_1_8 = Engine('1.8')
engine_1_0 = Engine('1.0')
volkswagen = Manufactor('VolksWagen')
fiat = Manufactor('Fiat')

voyage.volkswagen = volkswagen
voyage.engine = engine_1_6

stilo.fiat = fiat
stilo.engine = engine_1_8

print(voyage.volkswagen.name, voyage.name, voyage.engine.name)
print('####################')
print(stilo.fiat.name, stilo.name, stilo.engine.name)



