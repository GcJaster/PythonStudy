class WordString:
    def __init__(self, string: str = None) -> None:
        self.__string = string

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, new_string: str) -> None:
        if type(new_string) is str:
            self.__string = new_string

    def __call__(self, indx: int) -> str:
        if indx < len(self.__string):
            return self.words(indx)

    def __len__(self) -> int:
        return len(self.string.split())

    def words(self, indx: int) -> str:
        return self.string.split()[indx]


if __name__ == '__main__':
    words = WordString()
    words.string = "Курс по Python ООП"
    n = len(words)
    first = "" if n == 0 else words(0)
    print(words.string)
    print(f"Число слов: {n}; первое слово: {first}")