from typing import Any


class Cell:
    """Class describing a cell with data for a table"""
    def __init__(self, value) -> None:
        self.value = value


class SparseTable:
    """Class describing a sparse data table"""
    def __init__(self) -> None:
        self.rows = self.cols = 0
        self.table = {}

    def add_data(self, row: int, col: int, data: Any) -> None:
        self.table[(row, col)] = data
        self.update_indexes()

    def update_indexes(self) -> None:
        self.rows = max(key[0] for key in self.table) + 1
        self.cols = max(key[1] for key in self.table) + 1

    def remove_data(self, row: int, col: int) -> None:
        try:
            del self.table[(row, col)]
            self.update_indexes()
        except KeyError:
            raise IndexError("ячейка с указанными индексами не существует")

    def __getitem__(self, item: tuple[int, int]) -> Any:
        try:
            return self.table[item[0], item[1]].value
        except KeyError:
            raise ValueError("данные по указанным индексам отсутствуют")

    def __setitem__(self, key: tuple[int, int], value: Any) -> None:
        item = (key[0], key[1])
        if item not in self.table:
            self.table[item] = Cell(value)
            self.update_indexes()
        else:
            self.table[item] = Cell(value)


def main() -> None:
    st = SparseTable()
    st.add_data(2, 5, Cell("cell_25"))
    st.add_data(0, 0, Cell("cell_00"))
    st[2, 5] = 25  # изменение значения существующей ячейки
    st[11, 7] = 'cell_117'  # создание новой ячейки
    print(st[0, 0])  # cell_00
    st.remove_data(2, 5)
    print(st.rows, st.cols)  # 12, 8 - общее число строк и столбцов в таблице
    # val = st[2, 5]  # ValueError
    # st.remove_data(12, 3)  # IndexError


if __name__ == '__main__':
    main()