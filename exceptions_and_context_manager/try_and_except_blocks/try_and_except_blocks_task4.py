# Объявите в программе класс FloatValidator, объекты которого создаются командой:
# fv = FloatValidator(min_value, max_value) где min_value, max_value - минимальное и максимальное допустимое значение.
# Объекты этого класса предполагается использовать следующим образом: fv(value)
# где value - проверяемое значение
# По аналогии, объявите класс IntegerValidator
# После этого объявите функцию с сигнатурой: def is_valid(lst, validators):  где lst - список из данных;
# validators - список из объектов-валидаторов (объектов классов FloatValidator и IntegerValidator).
# Эта функция должна отбирать из списка все значения, которые прошли хотя бы по одному валидатору.
# И возвращать новый список с элементами, прошедшими проверку.


from typing import List, Any, Union


U = Union[int, float]


class Validator:
    _type = None

    def __init__(self, min_value: U, max_value: U) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value: U):
        self.__check_type(value)
        self.__check_range(value)

    @classmethod
    def __check_type(cls, value: U):
        if type(value) != cls._type:
            raise ValueError('значение не прошло валидацию')

    def __check_range(self, value: U):
        if not self.min_value <= value <= self.max_value:
            raise ValueError('значение не прошло валидацию')


class FloatValidator(Validator):
    _type = float


class IntegerValidator(Validator):
    _type = int


def is_valid(lst: List[Any, ...], validators: List[FloatValidator, IntegerValidator, ...]) -> List[int, float]:
    out_lst = []

    for data in lst:
        for validator in validators:
            try:
                validator(data)
            except ValueError:
                continue
            else:
                out_lst.append(data)

    return out_lst


if __name__ == '__main__':
    fv = FloatValidator(0, 10.5)
    iv = IntegerValidator(-10, 20)

    print(is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv]))
