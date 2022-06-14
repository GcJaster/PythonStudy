from typing import List


class Thing:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight: int) -> None:
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self) -> List[Thing]:
        return self.__things

    def add_thing(self, thing: Thing) -> None:
        if self.get_total_weight() + thing.weight < self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx: int) -> None:
        self.__things.pop(indx)

    def get_total_weight(self) -> float:
        return sum([thing.weight for thing in self.__things])


def main():
    bag = Bag(1000)
    bag.add_thing(Thing("Книга по Python", 100))
    bag.add_thing(Thing("Котелок", 500))
    bag.add_thing(Thing("Спички", 20))
    bag.add_thing(Thing("Бумага", 100))
    bag.add_thing(Thing("Карандаш", 400))
    w = bag.get_total_weight()
    for t in bag.things:
        print(f"{t.name}: {t.weight}")


if __name__ == '__main__':
    main()