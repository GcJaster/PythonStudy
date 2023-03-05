from typing import Union, Tuple


class Matrix:
    """class describing a square matrix"""

    def __init__(
            self,
            rows_or_list: Union[int, list],
            cols: int = 0,
            fill_value: Union[int, float] = 0) -> None:

        if type(rows_or_list) is list:
            self._rows = len(rows_or_list)
            self._cols = len(rows_or_list[0])
            if not all(len(row) == self._cols for row in rows_or_list) or \
                not all(self.__is_digit(x) for row in rows_or_list for x in row):
                raise TypeError("список должен быть прямоугольным, состоящим из чисел")

            self._lst = rows_or_list
        else:
            if type(rows_or_list) != int or type(cols) != int or type(fill_value) not in (int, float):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

            self._rows = rows_or_list
            self._cols = cols
            self._lst = [[fill_value for _ in range(cols)] for _ in range(rows_or_list)]

    @staticmethod
    def __is_digit(x) -> bool:
        return type(x) in (int, float)

    @staticmethod
    def __check_data_type(value: Union[int, float]) -> None:
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')

    def __check_index(self, index: Tuple[int, int]) -> None:
        row, col = index
        if not (0 <= row < self._rows) or not (0 <= col < self._cols):
            raise IndexError('недопустимые значения индексов')

    def __check_dimensions(self, matrix) -> None:
        rows, cols = matrix._rows, matrix._cols
        if self._rows != rows or self._cols != cols:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __getitem__(self, item):
        self.__check_index(item)
        row, col = item
        return self._lst[row][col]

    def __setitem__(self, key: Tuple[int, int], value: Union[int, float]) -> None:
        self.__check_index(key)
        self.__check_data_type(value)

        row, col = key
        self._lst[row][col] = value

    def __add__(self, other: Tuple[int, list[list, ...]]):
        if not isinstance(other, (int, Matrix)):
            raise ArithmeticError("Правый операнд должен быть int или Matrix")

        if isinstance(other, Matrix):
            self.__check_dimensions(other)
            return Matrix([[self[i, j] + other[i, j] for j in range(self._cols)] for i in range(self._rows)])
        else:
            self.__is_digit(other)
            return Matrix([[self[i, j] + other for j in range(self._cols)] for i in range(self._rows)])

    def __sub__(self, other: Tuple[int, list[list, ...]]):
        if not isinstance(other, (int, Matrix)):
            raise ArithmeticError("Правый операнд должен быть int или Matrix")

        if isinstance(other, Matrix):
            self.__check_dimensions(other)
            return Matrix([[self[i, j] - other[i, j] for j in range(self._cols)] for i in range(self._rows)])
        else:
            self.__is_digit(other)
            return Matrix([[self[i, j] - other for j in range(self._cols)] for i in range(self._rows)])


def main() -> None:
    mt = Matrix([[1, 2], [3, 4]])
    mt2 = Matrix([[5, 6], [7, 8]])
    m3 = mt + mt2
    res1 = mt[0, 0]  # 1
    res2 = mt[0, 1]  # 2
    res3 = mt[1, 0]  # 3
    res4 = mt[1, 1]  # 4
    print(m3._lst)  # 1 2 3 4

if __name__ == '__main__':
    main()