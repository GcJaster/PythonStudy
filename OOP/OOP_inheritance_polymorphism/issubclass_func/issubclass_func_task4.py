class Tuple(tuple):
    def __add__(self, other):
        return Tuple(super().__add__(tuple(other)))


def main() -> None:
    t = Tuple([1, 2, 3])
    t = t + "Python"
    print(t)  # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
    t = (t + "Python") + "ООП"


if __name__ == '__main__':
    main()

