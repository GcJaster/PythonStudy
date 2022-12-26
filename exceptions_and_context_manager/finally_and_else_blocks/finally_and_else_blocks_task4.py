# Объявите класс с именем Rect (прямоугольник), объекты которого создаются командой: r = Rect(x, y, width, height)
# где x, y - координаты верхнего левого угла (любые числа); width, height - ширина и высота прямоугольника
# (положительные числа). Ось абсцисс (Ox) направлена вправо, ось ординат (Oy) направлена вниз.
# В каждом объекте класса Rect должны формироваться локальные атрибуты с именами: _x, _y, _width, _height и
# соответствующими значениями. Если переданные аргументы x, y (не числа) и width, height не положительные числа, то
# генерировать исключение командой: raise ValueError('некорректные координаты и параметры прямоугольника')
# В классе Rect реализовать метод:  def is_collision(self, rect):
# который проверяет пересечение текущего прямоугольника с другим (с объектом rect). Если прямоугольники пересекаются,
# то должно генерироваться исключение командой: raise TypeError('прямоугольники пересекаются')
# Сформировать в программе несколько объектов класса Rect со следующими значениями:
# 0; 0; 5; 3
# 6; 0; 3; 5
# 3; 2; 4; 4
# 0; 8; 8; 1
# Сохранить их в списке lst_rect. На основе списка lst_rect сформировать еще один список lst_not_collision, в котором
# должны быть объекты rect не пересекающиеся ни с какими другими объектами в списке lst_rect.


class Rect:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        if key in ("_width", "_height") and value <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')

        object.__setattr__(self, key, value)

    def is_collision(self, rect):
        if not isinstance(rect, Rect):
            raise TypeError("аргумент метода is_collision() должен быть объектом класса Rect")

        if not (self._x + self._width < rect._x or rect._x + rect._width < self._x or
                self._y + self._height < rect._y or rect._y + rect._height < self._y):
            raise TypeError("прямоугольники пересекаются")


def is_collision(r1, r2):
    try:
        r1.is_collision(r2)
    except TypeError:
        return True
    return False


if __name__ == '__main__':
    lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
    length = len(lst_rect)
    lst_not_collision = [lst_rect[i] for i in range(length)
                         if not any(is_collision(lst_rect[i], lst_rect[j]) for j in range(length) if i != j)]