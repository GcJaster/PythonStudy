class Book:
    def __init__(self, title: str = "", author: str = "", pages: int = 0, year: int = 0) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key == 'title' or key == "author":
            if not isinstance(value, str):
                raise TypeError('Неверный тип присваиваемых данных.')

        elif key == 'pages' or key == "year":
            if not isinstance(value, int):
                raise TypeError('Неверный тип присваиваемых данных.')

        object.__setattr__(self, key, value)


def main():
    book = Book("Сергей Балакирев", "Python", 123, 2022)

    print(book.__dict__)


if __name__ == '__main__':
    main()

