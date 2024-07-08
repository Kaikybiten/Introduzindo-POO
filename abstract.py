from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    @abstractmethod
    def __init__(self, name):
        self._name = name

    @property
    @abstractmethod
    def name(self):
        ...

    @name.setter
    @abstractmethod
    def name(self, name):
        ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # Inutil

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name