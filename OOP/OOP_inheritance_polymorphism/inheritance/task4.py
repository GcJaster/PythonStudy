class Singleton:
    __instance = None
    __instance_base = None


    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.__instance_base is None:
                cls.__instance_base = object.__new__(cls)
            return cls.__instance_base

        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


class Game(Singleton):
    def __init__(self, name: str) -> None:
        if 'name' not in self.__dict__:
            self.name = name


def main() -> None:
    game = Game('gaga')
    game1 = Game('haha')
    sing = Singleton()
    print(id(game), id(game1), id(sing))

if __name__ == '__main__':
    main()

