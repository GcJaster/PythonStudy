class Integer:
    def __init__(self, start_value: int = 0) -> None:
        self.__value = start_value

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int) -> None:
        if type(value) != int:
            raise ValueError("должно быть целое число")
        self.__value = value

    def __repr__(self) -> str:
        return str(self.__value)


class Array:
    def __init__(self, max_lenght: int, cell) -> None:
        self.__cell = cell
        self.__max_lenght = max_lenght
        self.__array = [self.__cell() for i in range(self.__max_lenght)]

    def __getitem__(self, item: int) -> int:
        self.__check(item)
        return self.__array[item].value

    def __setitem__(self, key: int, value: int) -> None:
        self.__check(key)
        self.__array[key].value = value

    def __repr__(self) -> str:
        return " ".join(map(str, self.__array))

    def __check(self, indx: int) -> None:
        if type(indx) != int or not (-self.__max_lenght <= indx < self.__max_lenght):
            raise IndexError("неверный индекс для доступа к элементам массива")


def main() -> None:
    ar_int = Array(10, cell=Integer)
    print(ar_int[3])
    print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
    ar_int[1] = 10
    ar_int[1] = 10.5  # должно генерироваться исключение ValueError
    ar_int[10] = 1  # должно генерироваться исключение IndexError


if __name__ == '__main__':
    main()