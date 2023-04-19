from abc import ABC, abstractmethod


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Figure(ABC):
    """Абстрактный базовый класс"""

    def __init__(self, color: str) -> None:
        self.color: str = color

    @abstractmethod
    def square(self):
        """Абстрактный метод вычисления площади"""
        raise NotImplementedError(f"Метод square() должен быть переопределён в дочернем классе {self.__class__}")

    @abstractmethod
    def perimeter(self):
        """Абстрактный метод вычисления периметра"""
        raise NotImplementedError(f"Метод perimeter() должен быть переопределён в дочернем классе {self.__class__}")

    @abstractmethod
    def intersectTo(self):
        raise NotImplementedError(f"Метод intersectTo() должен быть переопределён в дочернем классе {self.__class__}")


class Polygon(Figure):
    def __init__(self, color: str, *args):
        super(Polygon, self).__init__(color)
        self.lst_points = args

    def square(self):
        length = len(self.lst_points)
        area = 0
        last = length - 1
        for i in range(length):
            area += self.lst_points[last][0] * self.lst_points[i][1] - self.lst_points[last][1] * self.lst_points[i][0]
            last = i
        return 0.5*abs(area)


class Triangle(Figure, ABC):
    def __init__(self, color: str, p1: Point, p2: Point, p3: Point) -> None:
        super(Triangle, self).__init__(color)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def square(self):
        """Вычисление площади треугольника"""
        return 0.5 * abs(((self.p2.x - self.p1.x) * (self.p3.y - self.p1.y) -
                     (self.p3.x - self.p1.x) * (self.p2.y - self.p1.y)))

    def perimeter(self):
        """Вычисление периметра треугольника"""
        v1 = 0.5 * ((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
        v2 = 0.5 * ((self.p3.x - self.p2.x)**2 + (self.p3.y - self.p2.y)**2)
        v3 = 0.5 * ((self.p3.x - self.p1.x)**2 + (self.p3.y - self.p1.y)**2)
        return v1 + v2 + v3


class Circle(Figure):
    def __init__(self, color: str, center: Point, radius: int) -> None:
        super(Circle, self).__init__(color)
        self.center: Point = center
        self.radius: int = radius

    def square(self):
        """Вычисление площади круга"""
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        """Вычисление периметра круга"""
        return 2 * 3.14 * self.radius


if __name__ == '__main__':
    total = 0
    c1 = Circle('синий', Point(0, 0), 2)
    tr1 = Triangle('красный', Point(3, 3), Point(5, 5), Point(4, 2))
    lst_figures = [c1, tr1]
    for fg in lst_figures:
        total += fg.square()

    print(total)

