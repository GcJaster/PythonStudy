from typing import Union

U = Union[int, float]


class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)


class Money:
    def __init__(self, value: U) -> None:
        self.__valid_value(value)
        self._money = value
        
    @property
    def money(self) -> U:
        return self._money
    
    @money.setter
    def money(self, new_value: U) -> None:
        self.__valid_value(new_value)
        self._money = new_value

    @staticmethod
    def __valid_value(value: U) -> None:
        if type(value) not in (int, float):
            raise TypeError('сумма должна быть числом')


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"


if __name__ == '__main__':
    m1 = MoneyR(1)
    m2 = MoneyD(2)
    m = m1 + 10
    print(m)  # MoneyR: 11
    m = m1 - 5.4
    print(m)
    # m = m1 + m2  # TypeError