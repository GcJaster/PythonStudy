import itertools
from typing import Union

U = Union[int, float]


class ShopInterface:
    """Class of description a shop"""

    def get_id(self) -> NotImplementedError:
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    """Class of description a item for shop"""

    id_generator = itertools.count(1)

    def __init__(self, name: str, weight: U, price: U):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.get_new_id()

    def get_id(self) -> int:
        return self.__id

    @classmethod
    def get_new_id(cls) -> int:
        return next(cls.id_generator)


if __name__ == '__main__':
    item1 = ShopItem("имя1", 3, 20.5)
    item2 = ShopItem("имя2", 4.5, 10)
    print(item1.get_id())
    print(item2.get_id())