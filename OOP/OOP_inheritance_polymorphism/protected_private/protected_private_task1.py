class AnimalDescriptor:
    def __set_name__(self, owner, name: str) -> None:
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        if instance is None:
            return property()
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Animal:
    name: str = AnimalDescriptor()
    kind: str = AnimalDescriptor()
    old: int = AnimalDescriptor()

    def __init__(self, name: str, kind: str, old: int) -> None:
        self.__name = name
        self.__kind = kind
        self.__old = old


if __name__ == '__main__':
    animals = [Animal('Васька', 'дворовый кот', 5), Animal('Рекс', 'немецкая овчарка', 8), Animal('Кеша', 'попугай', 3)]


