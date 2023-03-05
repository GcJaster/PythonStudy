from typing import NoReturn


class ListMath:
    def __init__(self, lst_math: list = None) -> NoReturn:
        if lst_math:
            self.lst_math = [i for i in lst_math if type(i) in (float, int)]
        else:
            self.lst_math = []

    def __add__(self, other):
        return ListMath(list(map(lambda x: x + other, self.lst_math)))

    def __iadd__(self, other):
        self.lst_math = list(map(lambda x: x + other, self.lst_math))
        return self

    def __radd__(self, other):
        return ListMath(list(map(lambda x: other + x, self.lst_math)))

    def __sub__(self, other):
        return ListMath(list(map(lambda x: x - other, self.lst_math)))

    def __isub__(self, other):
        self.lst_math = list(map(lambda x: x - other, self.lst_math))
        return self

    def __rsub__(self, other):
        return ListMath(list(map(lambda x: other - x, self.lst_math)))

    def __mul__(self, other):
        return ListMath(list(map(lambda x: x * other, self.lst_math)))

    def __imul__(self, other):
        self.lst_math = list(map(lambda x: x * other, self.lst_math))
        return self

    def __rmul__(self, other):
        return ListMath(list(map(lambda x: other * x, self.lst_math)))

    def __truediv__(self, other):
        return ListMath(list(map(lambda x: x / other, self.lst_math)))

    def __itruediv__(self, other):
        self.lst_math = list(map(lambda x: x / other, self.lst_math))
        return self

    def __rtruediv__(self, other):
        return ListMath(list(map(lambda x: other - x, self.lst_math)))


def main():
    lst = ListMath([1, "abc", -5, 7.68, True])
    lst = lst + 76  # сложение каждого числа списка с определенным числом
    print(f"lst = lst + 76: ", lst.lst_math)
    lst += 76.7  # сложение каждого числа списка с определенным числом
    print(f"lst += 76.7", lst.lst_math)
    lst = lst - 76  # вычитание из каждого числа списка определенного числа
    print(f"lst = lst - 76:", lst.lst_math)
    lst = 7.0 - lst  # вычитание из числа каждого числа списка
    print(f"lst = 7.0 - lst: ", lst.lst_math)
    lst -= 76.3
    print(f"lst -= 76.3: ", lst.lst_math)
    lst = lst * 5  # умножение каждого числа списка на указанное число (в данном случае на 5)
    print(f"lst = lst * 5: ", lst.lst_math)
    lst = 5 * lst  # умножение каждого числа списка на указанное число (в данном случае на 5)
    print(f"lst = 5 * lst: ", lst.lst_math)
    lst *= 5.54
    print(f"lst *= 5.54: ", lst.lst_math)
    lst = lst / 13  # деление каждого числа списка на указанное число (в данном случае на 13)
    print(f"lst = lst / 13: ", lst.lst_math)
    lst /= 13.0
    print(f"lst /= 13.0: ", lst.lst_math)


if __name__ == '__main__':
    main()