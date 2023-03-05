from typing import List


class FloatValue:
    def __set_name__(self, owner, name: str) -> None:
        self.name = "__" + name

    def __get__(self, instance, owner) -> float:
        return getattr(instance, self.name)

    def __set__(self, instance, value: float) -> None:
        self.verify(value)
        setattr(instance, self.name, value)

    @staticmethod
    def verify(value: float) -> None:
        if not isinstance(value, float):
            raise TypeError("Variable must be of float type.")


class Cell:
    value = FloatValue()

    def __init__(self, value: float = 0.0) -> None:
        self.value = value


class TableSheet:
    def __init__(self, N: int = 0, M: int = 0) -> None:
        """Table initialization """
        self.__m = M
        self.__n = N
        self.__cells = self.fill_table()

    def fill_table(self) -> List[List[Cell]]:
        res = []
        for i in range(1, self.__n + 1):
            res.append([])
            for j in range(i * self.__m - (self.__m - 1), i * self.__m + 1):
                res[i-1].append(Cell(float(j)))
        return res

    def show_table(self) -> None:
        for row in self.__cells:
            for cell in row:
                print(cell.value, end=' ')
            print()


def main():
    table = TableSheet(5, 3)
    table.show_table()


if __name__ == '__main__':
    main()