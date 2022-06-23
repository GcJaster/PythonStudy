from typing import NoReturn, List


class PolyLine:
    def __init__(self, *args) -> NoReturn:
        self.coords = list(args)

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx: int) -> NoReturn:
        self.coords.pop(indx)

    def get_coords(self) -> List[tuple]:
        return self.coords


def main():
    poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
    print(poly.get_coords())


if __name__ == '__main__':
    main()
