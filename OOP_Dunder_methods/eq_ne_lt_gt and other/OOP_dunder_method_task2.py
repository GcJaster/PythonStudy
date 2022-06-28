from typing import Union
from dataclasses import dataclass


class Prop:
    def __set_name__(self, owner, name) -> None:
        self.name = "__" + name

    def __get__(self, instance, owner) -> str:
        return getattr(instance, self.name)

    def __set__(self, instance, value) -> None:
        if self.__verify_value(value):
            if instance.MIN_DIMENSION < value < instance.MAX_DIMENSION:
                setattr(instance, self.name, value)

    @classmethod
    def __verify_value(cls, value: Union[int, float]) -> Union[int, float]:
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно иметь тип int или float")
        return value


class Dimensions:
    MIN_DIMENSION: int = 10
    MAX_DIMENSION: int = 10000
    a = Prop()
    b = Prop()
    c = Prop()

    def __init__(self,
                 a: Union[int, float],
                 b: Union[int, float],
                 c: Union[int, float]) -> None:
        self.__a = a
        self.__b = b
        self.__c = c

    @classmethod
    def __verify(cls, other):
        """Verify obj on type Dimensions."""
        if not isinstance(other, Dimensions):
            raise TypeError("Операнд справа должен иметь тип Dimensions!")
        return other

    def get_volume(self) -> Union[int, float]:
        """Get volume of self."""
        return self.__a * self.__b * self.__c

    def __gt__(self, other) -> bool:
        if self.__verify(other):
            return self.get_volume() > other.__get_volume()

    def __ge__(self, other) -> bool:
        if self.__verify(other):
            return self.get_volume() >= other.__get_volume()


@dataclass
class ShopItem:
    """Create item."""
    name: str
    price: Union[int, float]
    dim: Dimensions


def main() -> None:
    trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
    umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
    fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
    chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
    lst_shop = (trainers, umbrella, fridge, chair)
    lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.get_volume())
    for i in lst_shop_sorted:
        print(i.dim.get_volume())


if __name__ == '__main__':
    main()