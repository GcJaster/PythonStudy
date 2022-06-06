class Clock:
    MAX_TIME = 100_000
    MIN_TIME = 0

    def __init__(self, time: int=0):
        self.__time = time

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @classmethod
    def __check_time(cls, tm):
        return type(tm) is int and cls.MIN_TIME <= tm < cls.MAX_TIME


def main():
    clock = Clock()
    clock.set_time(4530)
    print(clock.get_time())


if __name__ == '__main__':
    main()
