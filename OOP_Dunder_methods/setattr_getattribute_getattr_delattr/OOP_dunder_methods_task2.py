import itertools


class Product:
    __id = itertools.count(1)
    id: int
    name: str
    weight: (int, float)
    price: (int, float)

    def __init__(self, name: str, weight: (float, int), price: (int, float)) -> None:
        self.id = next(self.__id)
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value) -> None:
        if not isinstance(value, self.__annotations__.get(key)):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)


class Shop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.goods = []

    def add_product(self, product: Product) -> None:
        self.goods.append(product)

    def remove_product(self, product: Product) -> None:
        self.goods.remove(product)


def main():
    shop = Shop("Балакирев и К")
    book = Product("Python ООП", 100, 1024)
    shop.add_product(book)
    shop.add_product(Product("Python", 150, 512))
    for p in shop.goods:
        print(f"{p.id}, {p.name}, {p.weight}, {p.price}")


if __name__ == '__main__':
    main()
