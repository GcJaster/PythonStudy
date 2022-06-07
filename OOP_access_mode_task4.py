from typing import Tuple


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    def get_coords(self) -> Tuple[int, int]:
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args) -> None:
        self.set_coords(*args)

    def set_coords(self, *args) -> None:
        if isinstance(args[0], Point):
            self.__sp = args[0]
            self.__ep = args[1]
        else:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])

    def get_coords(self) -> Tuple[Point, Point]:
        return self.__sp, self.__ep

    def draw(self) -> None:
        print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")


rect = Rectangle(Point(0,0), Point(24,33))
rect.draw()