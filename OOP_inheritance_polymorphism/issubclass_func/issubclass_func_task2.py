from typing import Tuple


class Thing:
    def __init__(self, name: str, price: float, weight: float) -> None:
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self) -> hash(Tuple[str, float, float]):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    def __init__(self, things: dict = None) -> None:
        things = {} if things is None else things

        if not isinstance(things, dict):
            raise TypeError('аргумент должен быть словарем')

        if things and not all(isinstance(key, Thing) for key in things):
            raise TypeError('ключами могут быть только объекты класса Thing')

        super().__init__(things)

    def __setitem__(self, key: Thing, value: Thing):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')

        super().__setitem__(key, value)


def main() -> None:
    th_1 = Thing('Лыжи', 11000, 1978.55)
    th_2 = Thing('Книга', 1500, 256)
    dict_things = DictShop()
    dict_things[th_1] = th_1
    dict_things[th_2] = th_2

    for x in dict_things:
        print(x.name)

    # dict_things[1] = th_1  # исключение TypeError


if __name__ == '__main__':
    main()