class ItemAttrs:
    def __getitem__(self, item):
        return self.__dict__[list(self.__dict__.keys())[item]]

    def __setitem__(self, key, value):
        self.__dict__[list(self.__dict__.keys())[key]] = value


class Point(ItemAttrs):

    def __init__(self, x, y):
        self.x = x
        self.y = y


def main() -> None:
    pt = Point(1, 2.5)
    x = pt[0]  # 1
    print(x)
    y = pt[1]  # 2.5
    print(y)
    a = pt[0] = 10
    print(a)
    print(pt.__dict__)


if __name__ == '__main__':
    main()
