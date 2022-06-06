class Book:
    def __init__(self, author: str, title: str, price: int) -> None:
        self.__author = author
        self.__title = title
        self.__price = price

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str) -> None:
        if type(author) is str:
            self.__author = author

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        if type(title) is str:
            self.__title = title

    @property
    def price(self) -> int:
        return self.__price

    @price.setter
    def price(self, price: int) -> None:
        if type(price) is int:
            self.__price = price




