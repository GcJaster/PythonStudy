from typing import Union


class Ellipse:
    x1: Union[int, float, complex]
    y1: Union[int, float, complex]
    x2: Union[int, float, complex]
    y2: Union[int, float, complex]

    def __init__(self, *args) -> None:
        if len(args) == 4:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def __bool__(self):
        return {'x1', 'y1', 'x2', 'y2'} <= set(self.__dict__.keys())

    def get_coords(self):
        if bool(self):
            return self.x1, self.y1, self.x2, self.y2
        else:
            raise AttributeError('нет координат для извлечения')


def main() -> None:

    el1 = Ellipse()
    el2 = Ellipse()
    el3 = Ellipse(1,2,3,4)
    el4 = Ellipse(4,3,2,1)
    lst_geom = [el1, el2, el3, el4]
    for i in lst_geom:
        if bool(i):
            i.get_coords()


if __name__ == '__main__':
    main()