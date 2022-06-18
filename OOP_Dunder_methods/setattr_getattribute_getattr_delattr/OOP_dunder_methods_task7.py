import time


class Filter:
    def __init__(self, date) -> None:
        self.date = date

    def __setattr__(self, key, value) -> None:
        if key == 'date' and hasattr(self, key):
            pass
        else:
            object.__setattr__(self, key, value)


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:
    MAX_DATE_FILTER = 100
    d = {1: Mechanical, 2: Aragon, 3: Calcium}

    def __init__(self) -> None:
        self.slots = [None] * 3

    def add_filter(self, slot_num, filter):
        if self.d[slot_num] == type(filter):
            self.slots[slot_num - 1] = filter

    def remove_filter(self, slot_num):
        self.slots[slot_num - 1] = None

    def get_filters(self):
        return tuple(self.slots)

    def water_on(self):
        return all([i is not None and 0 <= time.time() - i.date <= self.MAX_DATE_FILTER for i in self.slots])



my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()
print(w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on()
print(w)
f1, f2, f3 = my_water.get_filters()
my_water.add_filter(3, Calcium(time.time()))
my_water.add_filter(2, Calcium(time.time()))
print(w)
print(f1.date, f2.date, f3.date)