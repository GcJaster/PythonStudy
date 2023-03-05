import math


class Des:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) not in (int, float) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.name, value)


class Triangle:
    a = Des()
    b = Des()
    c = Des()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.triangle_check(self.a, self.b, self.c)

    @staticmethod
    def triangle_check(a, b, c):
        if a > b + c or b > a + c or c > a + b:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return self.a + self.b + self.c

    def __call__(self, *args, **kwargs):
        p = len(self) / 2
        square = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return square


def main() -> None:
    tr = Triangle(4, 6, 3)
    print(tr.a, tr.b, tr.c)
    print(tr())


if __name__ == '__main__':
    main()