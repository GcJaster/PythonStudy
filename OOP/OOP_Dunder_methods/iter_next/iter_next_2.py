class TriangleListIterator:
    """iterator class describing a right triangle"""

    def __init__(self, lst: list) -> None:
        self._lst = lst

    def __iter__(self) -> None:
        for i in range(len(self._lst)):
            for j in range(i+1):
                yield self._lst[i][j]


def main() -> None:
    lst = [['x00', 'x01', 'x02'],
           ['x10', 'x11', 'x111'],
           ['x20', 'x21', 'x22', 'x23', 'x24'],
           ['x30', 'x31', 'x32', 'x33']]
    it = TriangleListIterator(lst)

    for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, x21, x22
        print(x)

    it_iter = iter(it)
    x = next(it_iter)


if __name__ == '__main__':
    main()