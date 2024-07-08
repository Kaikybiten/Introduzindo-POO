# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Car:
    def __init__(self, name):
        self._name = name
        self.motor = None

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

class Motor:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self.name = value

class Fabricante:
    def __init__(self, name):
        self._name = name
        self.cars = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    def fabric(self, car, motor):
        self.cars.append(Car(car))
        self.cars[len(self.cars) -1].motor = Motor(motor)
        

    def list_cars(self):
        for c in self.cars:
            print(self.name)
            print(c.name)
            print(c.motor.name)
            print()

fiat = Fabricante('fiat')
fiat.fabric('palio', 'univesal')

fiat.fabric('uno', 'comum')

fiat.list_cars()
