class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __add__(self, other):
        self.verify_len(other)
        return Vector(*map(sum, zip(self.coords, other.coords)))

    def __iadd__(self, other):
        sc = other
        if isinstance(other, Vector):
            self.coords = [x1 + x2 for (x1, x2) in zip(self.coords, sc.coords)]
        else:
            for i in range(len(self.coords)):
                self.coords[i] += other

        return self

    def __sub__(self, other):
        self.verify_len(other)
        return Vector(*[x1 - x2 for (x1, x2) in zip(self.coords, other.coords)])

    def __isub__(self, other):
        sc = other
        if type(other) is Vector:
            self.coords = [x1 - x2 for (x1, x2) in zip(self.coords, sc.coords)]
        else:
            for i in range(len(self.coords)):
                self.coords[i] -= other

        return self

    def __mul__(self, other):
        self.verify_len(other)
        return Vector(*[x1 * x2 for (x1, x2) in zip(self.coords, other.coords)])

    def __eq__(self, other):
        self.verify_len(other)
        return all(x == y for x, y in zip(self.coords, other.coords))

    def verify_len(self, value):
        if len(self.coords) != len(value.coords):
            raise ArithmeticError("размерности векторов не совпадают")


v2 = Vector(1, 4, 3)
v1 = Vector(1, 2, 3)
print((v1 + v2).coords)  # [5, 7, 9]
v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True