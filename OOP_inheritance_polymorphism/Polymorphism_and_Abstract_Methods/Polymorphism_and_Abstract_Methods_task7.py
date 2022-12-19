from typing import Union, Tuple


U = Union[int, float]


class PointTrack:
    def __init__(self, x: U, y: U) -> None:
        self.__valid_value(x, y)
        self._x = x
        self._y = y

    def __str__(self):
        return f'PointTrack: {self._x}, {self._y}'

    @staticmethod
    def __valid_value(value1, value2):
        if type(value1) not in (int, float) or type(value2) not in (int, float):
            raise TypeError('координаты должны быть числами')


class Track:
    def __init__(self, *args: PointTrack):
        if len(args) == 2:
            self.__points = PointTrack(*args)
        else:
            self.__points = list(args)

    @property
    def points(self) -> Tuple[PointTrack, ...]:
        return tuple(self.__points)

    def add_back(self, pt: PointTrack) -> None:
        self.__points.append(pt)

    def add_front(self, pt: PointTrack) -> None:
        self.__points.insert(0, pt)

    def pop_back(self) -> None:
        self.__points.pop()

    def pop_front(self) -> None:
        self.__points.pop(0)


if __name__ == '__main__':
    tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
    tr.add_back(PointTrack(1.4, 0))
    tr.pop_front()
    for pt in tr.points:
        print(pt)