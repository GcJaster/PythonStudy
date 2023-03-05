from typing import Union


class Furniture:
    def __init__(self, name: str, weight: Union[int, float]) -> None:
        self.__verify_name(name)
        self.__verify_weight(weight)
        self._name = name
        self._weight = weight

    def __setattr__(self, key, value):
        verify = {'_name': self.__verify_name, '_weight': self.__verify_weight}
        if key in verify:
            verify[key](value)
        object.__setattr__(self, key, value)

    def get_attrs(self):
        return tuple(self.__dict__.values())

    def __verify_weight(self, weight):
        if type(weight) not in (int, float) or weight <= 0:
            raise TypeError('вес должен быть положительным числом')

    def __verify_name(self, name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square


if __name__ == '__main__':
    cl = Closet('шкаф-купе', 342.56, True, 3)
    chair = Chair('стул', 14, 55.6)
    tb = Table('стол', 34.5, 75, 10)
    print(tb.get_attrs())