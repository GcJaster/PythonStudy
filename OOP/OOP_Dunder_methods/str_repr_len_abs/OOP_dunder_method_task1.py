import sys


class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"Книга: {self.title}; {self.author}; {self.pages}"


if __name__ == '__main__':
    lst_in = list(map(str.strip, sys.stdin.readlines())) # считывание списка из входного потока (эту строчку не менять)
    book = Book(*lst_in)
    print(book)