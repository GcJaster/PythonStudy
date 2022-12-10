from typing import Union, Tuple


class Animal:
    def __init__(self, name: str, old: int) -> None:
        self.name = name
        self.old = old

    def get_info(self) -> str:
        return '{}: {}, {}, {}'.format(*self.__dict__.values())


class Cat(Animal):
    def __init__(self, name: str, old: int, color: str, weight: Union[int, float]) -> None:
        super().__init__(name, old)
        self.color = color
        self.weight = weight


class Dog(Animal):
    def __init__(self, name: str, old: int, breed: str, size: Tuple[int, int]) -> None:
        super().__init__(name, old)
        self.breed = breed
        self.size = tuple(size)


def main() -> None:
    cat = Cat('кот', 4, 'black', 2.25)
    dog = Dog('собака', 5, 'хаски', (1, 2))
    res = cat.get_info()
    res2 = dog.get_info()
    print(res)
    print(res2)


if __name__ == '__main__':
    main()