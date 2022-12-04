from typing import Any, Tuple


class Cell:
    """Class describing a cell with data for a table"""

    def __init__(self, data: Any = 0) -> None:
        self.__data = data

    @property
    def data(self) -> Any:
        return self.__data

    @data.setter
    def data(self, new_data: Any) -> None:
        self.__data = new_data


class TableValues:
    """Class describing a sparse data table"""

    def __init__(self, rows: int, cols: int, type_data: Any = int) -> None:
        self.__rows = rows
        self.__cols = cols
        self.__type_data = type_data
        self.__cells = tuple(tuple(Cell() for _ in range(self.__cols)) for _ in range(self.__rows))

    def __check_index(self, index: Tuple[int, int]) -> None:
        row, col = index
        if (type(row) != int or not (0 <= row < self.__rows)) or (type(col) != int or not (0 <= col < self.__cols)):
            raise IndexError("неверный индекс")

    def __getitem__(self, item: Tuple[int, int]) -> Cell.data:
        self.__check_index(item)
        row, col = item
        return self.__cells[row][col].data

    def __setitem__(self, key: Tuple[int, int], value) -> None:
        self.__check_index(key)
        if type(value) != self.__type_data:
            raise TypeError("неверный тип присваиваемых данных")

        row, col = key
        self.__cells[row][col].data = value

    def __iter__(self):
        for row in self.__cells:
            yield (cell.data for cell in row)


def main() -> None:
    tb = TableValues(3, 2)
    tb[0, 0] = 2
    tb[1, 0] = 22

    for row in tb:  # перебор по строкам
        for value in row:  # перебор по столбцам
            print(value, end=' ')  # вывод значений ячеек в консоль
        print()


if __name__ == '__main__':
    main()