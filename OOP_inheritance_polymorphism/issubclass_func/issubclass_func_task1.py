class ListInteger(list):
    def __init__(self, lst):
        for i in lst:
            self.__check_type(i)
        super().__init__(lst)

    def __setitem__(self, key, value):
        self.__check_type(key, value)
        super().__setitem__(key, value)

    def append(self, item):
        self.__check_type(item)
        super().append(item)

    @staticmethod
    def __check_type(*args):
        for item in args:
            if type(item) != int:
                raise TypeError('можно передавать только целочисленные значения')


def main() -> None:
    s = ListInteger((1, 2, 3))
    s[1] = 10
    s.append(11)
    print(s)
    # s[0] = 10.5  # TypeError


if __name__ == '__main__':
    main()