from typing import NoReturn, Tuple, Union


class RadiusVector:
    def __init__(self, *args) -> NoReturn:
        if len(args) == 1 and isinstance(args[0], int) and args[0] > 1:
            self.vector = tuple([0] * args[0])
        elif all(isinstance(i, (int, float)) for i in args):
            self.vector = args
        else:
            self.vector = tuple()

    def get_coords(self) -> Tuple[int, ...]:
        return tuple(self.vector)

    def set_coords(self, *args) -> NoReturn:
        args = args[:len(self.vector)]
        self.vector = args + self.vector[len(args):]

    def __len__(self) -> int:
        return len(self.vector)

    def __abs__(self) -> Union[int, float]:
        return sum([coord ** 2 for coord in self.vector]) ** 0.5


def main():
    vector3D = RadiusVector(3)
    vector3D.set_coords(3, -5.6, 8)
    a, b, c = vector3D.get_coords()
    vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
    vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
    res_len = len(vector3D) # res_len = 3
    res_abs = abs(vector3D)
    print(res_len)
    print(res_abs)


if __name__ == '__main__':
    main()
