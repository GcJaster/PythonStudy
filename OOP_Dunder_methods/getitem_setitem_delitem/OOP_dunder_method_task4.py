from typing import Tuple


class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner) -> int:
        return getattr(instance, self.name)

    def __set__(self, instance, value: int) -> None:
        if type(value) != int:
            raise ValueError("возможны только целочисленные значения")
        setattr(instance, self.name, value)


class CellInteger:
    value: IntegerValue() = IntegerValue()

    def __init__(self, start_value: int = 0) -> None:
        self.value = start_value


class TableValues:
    def __init__(self, rows: int, cols: int, cell=CellInteger) -> None:
        if not cell:
            raise ("параметр cell не указан")

        self._rows = rows
        self._cols = cols
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))


    def __check_index(self, index) -> None:
        r, c = index
        if type(r) != int or not (0 <= r < self._rows) or type(c) != int or not(0 <= c < self._cols):
            raise IndexError("")

    def __getitem__(self, index) -> int:
        return self.cells[index[0]][index[1]].value

    def __setitem__(self, key: Tuple[int, int], value: int) -> None:
        self.__check_index(key)
        self.cells[key[0]][key[1]].value = value


def main() -> None:
    table = TableValues(2, 3, cell=CellInteger)
    print(table[0, 1])
    table[1, 1] = 10
    # table[0, 0] = 1.45  # генерируется исключение ValueError

    # вывод таблицы в консоль
    for row in table.cells:
        for x in row:
            print(x.value, end=' ')
        print()


if __name__ == '__main__':
    main()
