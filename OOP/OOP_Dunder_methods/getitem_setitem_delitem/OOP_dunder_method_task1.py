class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__attrs = tuple(self.__dict__.keys())
        self.__total_attrs = len(kwargs)

    def __check_indx(self, indx: int) -> None:
        if type(indx) != int or not (-self.__total_attrs <= indx < self.__total_attrs):
            raise IndexError("неверный индекс поля")

    def __getitem__(self, item):
        self.__check_indx(item)
        return getattr(self, self.__attrs[item])

    def __setitem__(self, key, value):
        self.__check_indx(key)
        setattr(self, self.__attrs[key], value)


def main():
    r = Record(pk=1, title='Python ООП', author='Балакирев')
    print(r.__dict__)
    print(a := r[1])


if __name__ == '__main__':
    main()