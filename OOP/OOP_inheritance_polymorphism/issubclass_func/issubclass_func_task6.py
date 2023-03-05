from typing import Tuple


class IteratorAttrs:
    """Iterator class"""

    def __iter__(self) -> iter:
        return iter(self.__dict__.items())


class SmartPhone(IteratorAttrs):
    """Class describing phone"""

    def __init__(self, model: str, size: Tuple[int, int], memory: int) -> None:
        self.model = model
        self.size = tuple(size)
        self.memory = memory


def main() -> None:
    phone = SmartPhone("nokia", (1, 2), 4)

    for attr, value in phone:
        print(attr, value)


if __name__ == '__main__':
    main()
