from typing import NoReturn, Union


class Item:
    name: str
    money: Union[int, float]

    def __init__(self, name: str, money: Union[int, float]) -> NoReturn:
        self.name = name
        self.money = money

    def __add__(self, item) -> Union[int, float]:
        if isinstance(item, Item):
            return self.money + item.money
        if isinstance(item, (float, int)):
            return self.money + item

    def __radd__(self, item) -> Union[int, float]:
        return self + item

class Budget:
    def __init__(self) -> NoReturn:
        self.items = []

    def add_item(self, it: Item) -> NoReturn:
        """Add new Item in Budget"""
        if type(it) is Item:
            self.items.append(it)

    def remove_item(self, indx: int) -> NoReturn:
        """Remove Item from Budget by index"""
        self.items.pop(indx)

    def get_items(self) -> list:
        """Get Budget list of Items"""
        return self.items


def main() -> NoReturn:
    my_budget = Budget()
    my_budget.add_item(Item("Курс по Python ООП", 2000))
    my_budget.add_item(Item("Курс по Django", 5000.01))
    my_budget.add_item(Item("Курс по NumPy", 0))
    my_budget.add_item(Item("Курс по C++", 1500.10))

    # вычисление общих расходов
    s = 0
    for x in my_budget.get_items():
        s = s + x
    print(s)

if __name__ == '__main__':
    main()
