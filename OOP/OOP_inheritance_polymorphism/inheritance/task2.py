import itertools
from typing import Tuple


class Thing:
    id_generator = itertools.count(1)

    def __init__(self, *args) -> None:
        self.id = self.get_id()
        self.name, self.price, self.weight, self.dims, self.memory, self.frm = args

    def get_data(self) -> dict.values:
        return self.__dict__.values()

    @classmethod
    def get_id(cls) -> int:
        return next(cls.id_generator)


class Table(Thing):
    def __init__(
            self,
            name: str,
            price: float,
            weight: float,
            dims: Tuple[float, float, float],
            memory: int = None,
            frm: str = None) -> None:
        super().__init__(name, price, weight, dims, memory, frm)


class ElBook(Thing):
    def __init__(
            self,
            name: str,
            price: float,
            memory: int,
            frm: str,
            weight: float = None,
            dims: Tuple[float, float, float] = None) -> None:
        super().__init__(name, price, weight, dims, memory, frm)


def main() -> None:
    table = Table("Круглый", 1024, 812.55, (700, 750, 700))
    book = ElBook("Python ООП", 2000, 2048, 'pdf')
    print(*table.get_data())
    print(*book.get_data())


if __name__ == '__main__':
    main()

