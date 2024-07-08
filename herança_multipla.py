class A:
    def quem_sou(self):
        print('A')

class B(A):
    
    #def quem_sou(self):
    #    print('B')

    ...

class C(A):
    def quem_sou(self):
        print('C')

class D(B, C):
    
    #def quem_sou(self):
    #    print('D')

    ...


d = D()

d.quem_sou()

print(D.__mro__) # Retorna a ordem que as classes da herança serão chamadas
# Nesse caso (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)