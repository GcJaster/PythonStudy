from typing import NoReturn


class Book:
    def __init__(self, title: str, author: str, year: int) -> NoReturn:
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self) -> NoReturn:
        self.book_list = []

    def __add__(self, book: Book) -> object:
        self.book_list.append(book)
        return self

    def __iadd__(self, book: Book) -> object:
        self.book_list.append(book)
        return self

    def __sub__(self, book: (Book, str, int)) -> object:
        if type(book) in (Book, str):
            self.book_list.remove(book)
            return self

        if type(book) is int:
            self.book_list.pop(book)
            return self

    def __isub__(self, book: (Book, str, int)) -> object:
        if type(book) in (Book, str):
            self.book_list.remove(book)
            return self

        if type(book) is int:
            self.book_list.pop(book)
            return self

    def __len__(self) -> int:
        return len(self.book_list)


def main():
    b1 = Book('test1', 'ha', 1999)
    b2 = Book('test2', 'he', 1998)
    lib = Lib()
    lib = lib + b1
    lib = lib + b2
    print(lib.__dict__)
    print(len(lib))
    lib -= 1
    print(lib.__dict__)
    print(len(lib))


if __name__ == '__main__':
    main()