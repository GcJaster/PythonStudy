class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        self.items.pop(indx-1)


class TeleProperty:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.name == '__id' and isinstance(value, int) and value >= 1:
            setattr(instance, self.name, value)
        elif self.name == '__duration' and isinstance(value, int):
            setattr(instance, self.name, value)
        elif isinstance(value, str):
            setattr(instance, self.name, value)


class Telecast:
    id = TeleProperty()
    name = TeleProperty()
    duration = TeleProperty()

    def __init__(self, id: int, name: str, duration: int):
        self.id = id
        self.name = name
        self.duration = duration


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с ", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")