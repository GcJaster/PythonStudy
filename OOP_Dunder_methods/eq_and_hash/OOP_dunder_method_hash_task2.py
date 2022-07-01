from __future__ import annotations
from dataclasses import dataclass


@dataclass
class ShopItem:
    """Store item."""

    name: str
    weight: (float, int)
    price: (float, int)

    def __eq__(self, other: ShopItem) -> bool:
        """Comparing class instances by their hash."""
        if isinstance(other, ShopItem):
            return hash(self) == hash(other)

    def __hash__(self) -> int:
        """Getting the hash of an object."""
        return hash((self.name.lower(), self.weight, self.price))


def main() -> None:
    lst_in = ['Системный блок: 1500 75890.56', 'Монитор Samsung: 2000 34000',
              'Клавиатура: 200.44 545', 'Монитор Samsung: 2000 34000']

    shop_items = {}
    for i in lst_in:
        name, weight, price = i.split(':')[0], i.split()[-2], i.split()[-1]
        obj = ShopItem(name, weight, price)
        shop_items.setdefault(obj, [obj, 0])
        shop_items[obj][1] += 1

    for key, value in shop_items.items():
        print(key.name, value)


if __name__ == '__main__':
    main()