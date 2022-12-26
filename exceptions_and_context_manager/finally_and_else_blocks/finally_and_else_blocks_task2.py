# Объявите в программе класс Point, объекты которого должны создаваться командами: pt = Point()  pt = Point(x, y)
# где x, y - произвольные числа (координаты точки).
# В каждом объекте класса Point должны формироваться локальные атрибуты _x, _y с соответствующими значениями.
# Если аргументы не указываются (первая команда), то _x = 0, _y = 0.
# Далее, в программе вводятся два значения в одну строчку через пробел. Значениями могут быть числа, слова,
# булевы величины. Необходимо сформировать объект pt с применением блоков try/except finally


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self._x = x
        self._y = y

    def __str__(self):
        return f"{self.__class__.__name__}: x = {self._x}, y = {self._y}"


if __name__ == '__main__':
    x, y = input().split()
    try:
        pt = Point(int(x), int(y))
    except ValueError:
        try:
            pt = Point()
        except:
            pass

    finally:
        print(pt)