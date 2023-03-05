from math import sqrt
from typing import NoReturn, Union


class Complex:
    Real: Union[int, float] = Union[int, float]
    Img: Union[int, float] = Union[int, float]

    def __init__(self, real: Real, img: Img) -> NoReturn:
        self.__real = real
        self.__img = img

    @property
    def real(self) -> Real:
        return self.__real

    @real.setter
    def real(self, new_real: Real) -> NoReturn:
        self.__verify(new_real)
        self.__real = new_real

    @property
    def img(self) -> Img:
        return self.__img

    @img.setter
    def img(self, new_img: Img) -> NoReturn:
        self.__verify(new_img)
        self.__img = new_img

    def __abs__(self):
        return sqrt(self.real**2 + self.img**2)

    def __call__(self) -> complex:
        return complex(self.__real, self.__img)

    @staticmethod
    def __verify(value):
        if not isinstance(value, (int, float)):
            raise ValueError("Неверный тип данных.")


def main():
    cmp = Complex(real=7, img=8)
    cmp.real = 3
    cmp.img = 4
    c_abs = abs(cmp)
    print(c_abs)


if __name__ == '__main__':
    main()
