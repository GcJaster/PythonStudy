class Dimensions:
    a: [int, float]
    b: [int, float]
    c: [int, float]

    def __init__(self, a: [int, float], b: [int, float], c: [int, float]) -> None:
        if any([True for i in (a, b, c) if i <= 0]):
            raise ValueError("габаритные размеры должны быть положительными числами")
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))


def main() -> None:
    lst_dims = []
    s_inp = '1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5'

    for i in s_inp.split('; '):
        a, b, c = list(map(lambda x: int(x) if '.' not in x else float(x), i.split()))
        lst_dims.append(Dimensions(a, b, c))

    lst_dims.sort(key=lambda x: hash(x))
    print(lst_dims)


if __name__ == '__main__':
    main()