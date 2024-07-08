class Cliente:
    def __init__(self, name):
        self._name = name
        self.__andress = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    def add_andress(self, street, number):
        self.__andress.append(Andress(street, number))

    def list_andress(self):
        print()
        for a in self.__andress:
            print(a._street)
            print(a._number)

class Andress:
    def __init__(self, street, number):
        self._street = street
        self._number = number

c1 = Cliente('maria')
print(c1.name)

c1.name = 'debora'
print(c1.name)

c1.add_andress('rua fogo', 39)

c1.list_andress()

c1.add_andress('rua agua', 229)
c1.add_andress('rua terra', 234)

c1.list_andress()