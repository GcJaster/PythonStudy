from typing import Union


class RadiusVector:
    def __init__(self, *args) -> None:
        self.coords = list(args)

    def __getitem__(self, item: Union[int, slice]) -> Union[int, slice]:
        return tuple(self.coords[item]) if type(item) == slice else self.coords[item]

    def __setitem__(self, key, value) -> None:
        self.coords[key] = value


def main() -> None:
    v = RadiusVector(1, 1, 1, 1)
    print(v[1])  # 1
    v[:] = 1, 2, 3, 4
    print(v[2])  # 3
    print(v[1:])  # (2, 3, 4)
    v[0] = 10.5


if __name__ == '__main__':
    main()