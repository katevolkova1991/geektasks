from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def need_fabric(self, *args):
        pass


class Clothes(MyAbstractClass):
    def __init__(self, **kwargs):
        self._name = kwargs.get('name', None)


class Coat(Clothes):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._v = kwargs.get('v', None)

    @property
    def need_fabric(self):
        return self._v / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._h = kwargs.get('h', None)

    @property
    def need_fabric(self):
        return self._h * 2 + 0.3


coat_1 = Coat(name = 'Пальто', v = 10)
suit_1 = Suit(name = 'Костюм', h = 170)

print(coat_1.need_fabric)
print(suit_1.need_fabric)