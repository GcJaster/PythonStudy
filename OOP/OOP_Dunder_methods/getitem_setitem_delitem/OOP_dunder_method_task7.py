class Cell:
    """A class that describes a square of the playing field in tic-tac-toe"""

    def __init__(self) -> None:
        self.is_free = True
        self.value = 0

    def __bool__(self) -> bool:
        return self.is_free


class TicTacToe:
    """Game pole class"""

    def __init__(self) -> None:
        # number of cells
        self._n = 3

        # playing field represented as a two-dimensional tuple
        self.pole = tuple(tuple(Cell() for col in range(self._n)) for row in range(self._n))

    def clear(self) -> None:
        """Clears the playing field (removes all tic-tac-toe, closes cells)"""

        self.__init__()

    def __check_index(self, item: tuple) -> None:
        """Checks that the coordinate does not go beyond the size of the field"""

        if type(item) != tuple or len(item) != 2:
            raise IndexError("неверный индекс клетки")
        if any(not (0 <= x < self._n) for x in item if type(x) != slice):
            raise IndexError("неверный индекс клетки")

    def __getitem__(self, item: tuple):
        """Getting value by x, y coordinates (one of the coordinates can be
        represented by a slice. In this case, all values located at the coordinate
        represented by an integer are selected). If both coordinates
        are integers - just return the element of the field located on
        corresponding coordinate"""

        self.__check_index(item)
        row, col = item

        if type(row) == slice:
            # All cells under the row column are returned
            return tuple(self.pole[x][col].value for x in range(self._n))

        if type(col) == slice:
            # All cells under the col column are returned
            return tuple(self.pole[row][x].value for x in range(self._n))

        # Returning a specific cell
        return self.pole[row][col].value

    def __setitem__(self, key, value):
        """Sets the value of a specific cell of the playing field"""

        self.__check_index(key)
        row, col = key
        if self.pole[row][col]:
            self.pole[row][col].value = value
            self.pole[row][col].is_free = False
        else:
            raise ValueError("клетка уже занята")


def main() -> None:
    game = TicTacToe()
    game.clear()
    game[0, 0] = 1
    game[1, 0] = 2
    game[2, 0] = 3
    # формируется поле:
    # 1 0 0
    # 2 0 0
    # 0 0 0
    # game[3, 2] = 2  # генерируется исключение IndexError
    if game[0, 0] == 0:
        game[0, 0] = 2
    v1 = game[:, 0]  # 1, 0, 0
    v2 = game[:, 0]  # 1, 2, 0
    for i in v1:
        print(i.value)


if __name__ == '__main__':
    main()