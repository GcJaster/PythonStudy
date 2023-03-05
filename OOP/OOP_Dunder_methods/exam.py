import random
from typing import Tuple


class Cell:
    """Class describing a cell of the playing field"""

    def __init__(self) -> None:
        self.value = 0

    def __bool__(self) -> bool:
        return not self.value


class TicTacToe:
    """Class describing a game pole"""

    FREE_CELL: int = 0  # Free cell
    HUMAN_X: int = 1  # Crosses (Player - human)
    COMPUTER_O: int = 2  # Noughts  (Player - computer)

    def __init__(self) -> None:
        self._size = 3
        self._win = 0  # 0 - Game ; 1 - Human win; 2 - Computer win; 3 - Draw
        self.pole = tuple(tuple(Cell() for _ in range(self._size)) for _ in range(self._size))

    def __bool__(self) -> bool:
        return self._win == 0 and self._win not in (1, 2, 3)

    def __getitem__(self, item) -> int:
        self.__check_index(item)
        row, col = item
        return self.pole[row][col].value

    def __setitem__(self, key, value) -> None:
        self.__check_index(key)
        row, col = key
        self.pole[row][col].value = value
        self.__update_win_status()

    @property
    def is_human_win(self) -> bool:
        print('w')
        return self._win == 1

    @property
    def is_computer_win (self) -> bool:
        return self._win == 2

    @property
    def is_draw (self) -> bool:
        return self._win == 3

    def __check_index(self, index: Tuple[int, int]) -> None:
        if type(index) not in (tuple, list) or len(index) != 2:
            raise IndexError('некорректно указанные индексы')
        row, col = index
        if not (0 <= row < self._size) or not (0 <= col < self._size):
            raise IndexError('некорректно указанные индексы')

    def __update_win_status(self):
        for row in self.pole:
            if all(x.value == self.HUMAN_X for x in row):
                self._win = 1
                return
            if all(x.value == self.COMPUTER_O for x in row):
                self._win = 2
                return

        for i in range(self._size):
            if all(x.value == self.HUMAN_X for x in (row[i] for row in self.pole)):
                self._win = 1
                return
            if all(x.value == self.COMPUTER_O for x in (row[i] for row in self.pole)):
                self._win = 2
                return

        if all(self.pole[i][i].value == self.HUMAN_X for i in range(self._size)) or \
                all(self.pole[i][-1 - i].value == self.HUMAN_X for i in range(self._size)):
            self._win = 1
            return

        if all(self.pole[i][i].value == self.COMPUTER_O for i in range(self._size)) or \
                all(self.pole[i][-1 - i].value == self.COMPUTER_O for i in range(self._size)):
            self._win = 2
            return

        if (x.value != self.FREE_CELL for row in self.pole for x in row):
            self._win = 3

    def init(self) -> None:
        self.__init__()

    def human_go(self) -> None:
        if not self:
            return

        while True:
            i, j = map(int, input("Введите координаты клетки: ").split())
            if not (0 <= i < self._size) or not (0 <= j < self._size):
                continue
            if self.pole[i][j].value == self.FREE_CELL:
                self.pole[i][j].value = self.HUMAN_X
                break

    def computer_go(self) -> None:
        if not self:
            return

        while True:
            row = random.randint(0, self._size - 1)
            col = random.randint(0, self._size - 1)
            if self.pole[row][col].value != self.FREE_CELL:
                continue
            self.pole[row][col].value = self.COMPUTER_O
            break

    def show(self) -> None:
        # show all game pole cells
        for row in self.pole:
            print(*map(lambda x: '#' if x.value == 0 else x.value, row))


def main():
    game = TicTacToe()
    game.init()
    step_game = 0
    while game:
        game.show()

        if step_game % 2 == 0:
            game.human_go()
        else:
            game.computer_go()

        step_game += 1

    game.show()

    if game.is_human_win:
        print("Поздравляем! Вы победили!")
    elif game.is_computer_win:
        print("Все получится, со временем")
    else:
        print("Ничья.")


if __name__ == '__main__':
    main()