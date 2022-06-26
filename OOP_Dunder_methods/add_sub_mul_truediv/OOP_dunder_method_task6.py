from typing import NoReturn, Union


class Box3D:
    width: Union[int, float]
    height: Union[int, float]
    depth: Union[int, float]

    def __init__(self,
                 width: Union[int, float],
                 height: Union[int, float],
                 depth: Union[int, float]) -> NoReturn:
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, box):
        if isinstance(box, Box3D):
            return Box3D(self.width + box.width,
                         self.height + box.height,
                         self.depth + box.depth)

    def __sub__(self, box):
        if isinstance(box, Box3D):
            return Box3D(self.width - box.width,
                         self.height - box.height,
                         self.depth - box.depth)

    def __mul__(self, num):
        if isinstance(num, (int, float)):
            return Box3D(self.width * num,
                         self.height * num,
                         self.depth * num)

    def __rmul__(self, num):
        return self * num

    def __truediv__(self, num):
        if isinstance(num, (int, float)):
            return Box3D(self.width / num,
                         self.height / num,
                         self.depth / num)

    def __mod__(self, num):
        if isinstance(num, (int, float)):
            return Box3D(self.width % num,
                         self.height % num,
                         self.depth % num)

    def __floordiv__(self, num):
        if isinstance(num, (int, float)):
            return Box3D(self.width // num,
                         self.height // num,
                         self.depth // num)


def main() -> NoReturn:
    box1 = Box3D(1, 2, 3)
    box2 = Box3D(2, 4, 6)

    box = box1 + box2  # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
    print(box.__dict__)
    box = box1 * 2  # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
    print(box.__dict__)
    box = 3 * box2  # Box3D: width=6, height=12, depth=18
    print(box.__dict__)
    box = box2 - box1  # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
    print(box.__dict__)
    box = box1 // 2  # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
    print(box.__dict__)
    box = box2 % 3  # Box3D: width=2, height=1, depth=0
    print(box.__dict__)


if __name__ == '__main__':
    main()