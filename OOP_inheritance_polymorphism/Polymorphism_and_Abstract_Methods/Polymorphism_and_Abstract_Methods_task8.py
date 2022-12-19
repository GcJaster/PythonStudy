from typing import Union
from dataclasses import dataclass


@dataclass
class Food:
    _name: str
    _weight: Union[int, float]
    _calories: int


@dataclass
class BreadFood(Food):
    _white: bool


@dataclass
class SoupFood(Food):
    _dietary: bool


@dataclass
class FishFood(Food):
    _fish: str


if __name__ == '__main__':
    bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
    sf = SoupFood("Черепаший суп", 520, 890, False)
    ff = FishFood("Консерва рыбная", 340, 1200, "семга")
    lst = [bf, sf, ff]
    for food in lst:
        name, *other = list(food.__dict__.values())
        print(f'{name}: {other}')