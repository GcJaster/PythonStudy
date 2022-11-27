class Cell:
    def __init__(self) -> None:
        self.is_free = True
        self.value = 0

    def __bool__(self) -> bool:
        return self.is_free


class TicTacToe:
    def __init__(self) -> None:
        self._n = 3
        self.pole = list(list(Cell() for _ in range(self._n)) for _ in range(self._n))

    def clear(self) -> None:
        for row in self.pole:
            for cell in row:
                cell.is_free = True
                cell.value = 0

    def check_index(self, item) -> None:
        if type(item) != tuple or len(item) != 2:
            raise IndexError("неверный индекс клетки")
        if any(not (0 <= x < self._n) for x in item if type(x) != slice):
            raise IndexError("неверный индекс клетки")

    def __getitem__(self, item):
        self.check_index(item)
        row, col = item
        if type(row) == slice:
            return tuple(self.pole[x][col] for x in range(self._n))
        if type(col) == slice:
            return tuple(self.pole[row][x] for x in range(self._n))

        return self.pole[row][col].value

    def __setitem__(self, key, value: int):
        self.check_index(key)
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
    # формируется поле:
    # 1 0 0
    # 2 0 0
    # 0 0 0
    # game[3, 2] = 2  # генерируется исключение IndexError
    if game[0, 0] == 0:
        game[0, 0] = 2
    v1 = game[0, :]  # 1, 0, 0
    v2 = game[:, 0]  # 1, 2, 0


if __name__ == '__main__':
    main()