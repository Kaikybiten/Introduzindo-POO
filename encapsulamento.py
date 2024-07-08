# Convenções para referenciar public, protected e private
# Publico (sem underline)
# Pode ser usado em qualquer lugar.

# Protected ("_" um underline)
# Não deve ser usado fora da classe em que foi declarado ou de suas subclasses.

# Private ("__" dois underlines)
# Só deve ser usado na classe em que foi declarado

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

        