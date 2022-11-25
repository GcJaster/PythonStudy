from typing import Union

U = Union[int, float]


class Track:
    def __init__(self, start_x: U, start_y: U) -> None:
        self.start = (start_x, start_y)
        self.coords = []

    @staticmethod
    def validator(method):
        def wrapper(self: "Track", key: int, *args, **kwargs):
            if 0 <= key < len(self.coords):
                return method(self, key, *args, **kwargs)
            raise IndexError('некорректный индекс')

        return wrapper

    @validator.__get__(0)
    def __getitem__(self, item: U):
        coords, speed = self.coords[item]
        return coords, speed

    @validator.__get__(0)
    def __setitem__(self, key: U, value: U) -> None:
        self.coords[key][1] = value

    def add_point(self, x: U, y: U, speed: U) -> None:
        self.coords.append([(x, y), speed])



def main() -> None:
    tr = Track(10, -5.4)
    tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
    tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
    tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

    tr[2] = 60
    c, s = tr[2]
    print(c, s)

    res = tr[3]  # IndexError


if __name__ == '__main__':
    main()
