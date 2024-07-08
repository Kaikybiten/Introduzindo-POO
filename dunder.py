    # STR e REPR
class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Voltado para gerar representações para devs
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x}, y={self.y})'
    
    # Voltado para gerar string do objeto
    def __str__(self):
        return f'({self.x}, {self.y})'

        #__str__ sempre será a prioridade quando ele existir no objeto

p1 = Ponto(123, 456)
p2 = Ponto(78, 90)

print(p1)
print(repr(p2)) # A função repr só é necessaria quando existir o metodo __str__ no objeto

# Ou
print()

print(f'{p2!s}')
print(f'{p1!r}')
# s = __str__, r = __repr__



class Calculo:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return f'Total: {self.x + other.x}'
    def __sub__(self, other):
        return f'Total: {self.x - other.x}'
    def __mul__(self, other):
        return f'Total: {self.x * other.x}'
    def __truediv__(self, other):
        return f'Total: {self.x / other.x}'

n1 = Calculo(4)
n2 = Calculo(7)
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print()



class Comparation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other): # Greater Than
        total_self = self.x + self.y
        total_other = other.x + self.y
        if total_other > total_self:
            return True
        return False
    
    def __lt__(self, other): # Less Than
        total_self = self.x + self.y
        total_other = other.x + self.y
        if total_other < total_self:
            return True
        return False
    
    def __eq__(self, other): # Equal
        total_self = self.x + self.y
        total_other = other.x + self.y
        if total_other == total_self:
            return True
        return False
    
    
    def __le__(self, other): # Less or Equal
        total_self = self.x + self.y
        total_other = other.x + self.y
        if total_other <= total_self:
            return True
        return False
    
    def __ge__(self, other): # Greater or Equal
        total_self = self.x + self.y
        total_other = other.x + self.y
        if total_other >= total_self:
            return True
        return False
    
    def __ne__(self, other): # Not Equal
        total_self = self.x + self.y
        total_other = other.x + self.y
        if total_other != total_self:
            return True
        return False
    
c1 = Comparation(12, 23) #35
c2 = Comparation(34, 56) #90
print(c1 > c2)
print(c1 < c2)
print(c1 <= c2)
print(c1 >= c2)
print(c1 == c2)
print(c1 != c2)