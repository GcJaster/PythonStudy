# Объявите в программе класс Triangle, объекты которого создаются командой:
# tr = Triangle(a, b, c) - где a, b, c - длины сторон треугольника

# Необходимо сформировать объекты класса Triangle, но только в том случае, если не возникло никаких исключений.
# Все созданные объекты представить в виде списка с именем lst_tr.


class Triangle:
    def __init__(self, a, b, c):
        self.__check_value(a, b, c)
        self.__check_triangle(a, b, c)
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def __check_value(*args, **kwargs):
        for i in args:
            if type(i) not in (int, float) or i <= 0:
                raise TypeError('стороны треугольника должны быть положительными числами')

    @staticmethod
    def __check_triangle(*args):
        a, b, c = args
        if a > b + c or b > a + c or c > a + b:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


if __name__ == '__main__':
    input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]


    lst_tr = []
    for data in input_data:
        try:
            temp = Triangle(*data)
        except (TypeError, ValueError):
            pass
        else:
            lst_tr.append(temp)

    print(lst_tr)

