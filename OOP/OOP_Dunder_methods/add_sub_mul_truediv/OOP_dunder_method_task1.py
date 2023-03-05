from typing import NoReturn


class NewList:
    def __init__(self, lst: list = None) -> NoReturn:
        self.lst = lst if lst else []

    def __sub__(self, other):
        other = other.lst if type(other) is self.__class__ else other
        a = [(x, type(x)) for x in self.lst]
        b = [(x, type(x)) for x in other]
        n_lst = []
        for i in a:
            b.remove(i) if i in b else n_lst.append(i[0])
        return NewList(n_lst)

    def __rsub__(self, other):
        other = other.lst if type(other) is self.__class__ else other
        return NewList(other) - self

    def get_list(self) -> list:
        return self.lst


def main():
    lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
    lst2 = NewList([0, 1, 2, 3, True])
    res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
    print(res_1.get_list())
    lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
    res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
    print(res_2.get_list())
    res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
    print(res_3.get_list())
    a = NewList([2, 3])
    res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
    print(res_4.get_list())


if __name__ == '__main__':
    main()