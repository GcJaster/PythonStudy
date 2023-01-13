from typing import Union


class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls, lst)

    def __str__(self):
        return ' '.join(map(str, self))

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    digits = list(map(float, '1 2 3 4 5'.split()))

    try:
        tl = TupleLimit(digits, 5)
        print(tl)
    except Exception as e:
        print(e)

