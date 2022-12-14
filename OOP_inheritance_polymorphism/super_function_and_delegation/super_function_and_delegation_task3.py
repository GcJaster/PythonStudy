from typing import Union


class Constractor:
    _name_core = ("name", "price")
    _name_add = ()

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__dict__.update(kwargs)
        if args:
            self.__dict__.update(zip((self._name_core + self._name_add), args))


class SellItem(Constractor):
    pass


class House(SellItem):
    _name_add = ("material", "square")


class Flat(SellItem):
    _name_add = ("size", "rooms")


class Land(SellItem):
    _name_add = ("square", )


class Agency(list):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def add_object(self, obj: Union[House, Flat, Land]) -> None:
        super().append(obj)

    def remove_object(self, obj: Union[House, Flat, Land]) -> None:
        if obj in self:
            super().remove(obj)

    def get_objects(self) -> list:
        return self


def main() -> None:
    ag = Agency("Рога и копыта")
    ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
    ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
    ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
    ag.add_object(House("дом, крипичный", price=35000000, material="кирпич", square=186.5))
    ag.add_object(Land("участок под застройку", 3000000, 6.74))
    for obj in ag.get_objects():
        print(obj.name)

    lst_houses = [x for x in ag.get_objects() if isinstance(x, House)]  # выделение списка домов


if __name__ == '__main__':
    main()



