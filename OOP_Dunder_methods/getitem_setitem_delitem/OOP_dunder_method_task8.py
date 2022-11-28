from typing import Union


class Thing:
    """A class that describes a thing """
    def __init__(self, name: str, weight: Union[int, float]) -> None:
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight: Union[int, float]) -> None:
        self.__max_weight = max_weight
        self.__weight = 0
        self.__things = list()

    def add_thing(self, thing: Thing) -> None:
        # Checking the index and adding things to the list
        self.__check_weight(thing)
        self.__things.append(thing)
        self.__weight += thing.weight

    def __getitem__(self, item: int) -> Thing:
        # Checking the index and returning things by index
        self.__check_index(item)
        return self.__things[item]

    def __setitem__(self, key: int, value: Thing) -> None:
        #
        self.__check_index(key)
        thing = self.__things[key]
        self.__check_weight(value, thing)
        self.__things[key] = value
        self.__weight += (value.weight - thing.weight)

    def __delitem__(self, key: int) -> None:
        #
        self.__check_index(key)
        thing = self.__things.pop(key)
        self.__weight -= thing.weight

    def __check_index(self, index) -> None:
        if type(index) != int or not (0 <= index < len(self.__things)):
            raise IndexError('неверный индекс')

    def __check_weight(self, new_thing, old_thing=None) -> None:
        # Checking the total weight to add a new item or replace an old item
        total = self.__weight + new_thing.weight if old_thing is None \
            else self.__weight + new_thing.weight - old_thing.weight

        if total > self.__max_weight:
            raise ValueError('превышен суммарный вес предметов')


def main() -> None:
    bag = Bag(1000)
    bag.add_thing(Thing('книга', 100))
    bag.add_thing(Thing('носки', 200))
    bag.add_thing(Thing('рубашка', 500))
    # bag.add_thing(Thing('ножницы', 300))  # генерируется исключение ValueError
    print(bag[2].name)  # рубашка
    bag[1] = Thing('платок', 100)
    print(bag[1].name)  # платок
    del bag[0]
    print(bag[0].name)  # платок
    # t = bag[4]  # генерируется исключение IndexError


if __name__ == '__main__':
    main()
