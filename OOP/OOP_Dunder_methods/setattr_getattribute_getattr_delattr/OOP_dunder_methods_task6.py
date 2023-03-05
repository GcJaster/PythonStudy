class Property:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'
        self.min = owner.MIN_DIMENSION
        self.max = owner.MAX_DIMENSION

    def __get__(self, instance, owner):
        if instance:
            return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.min <= value <= self.max:
            setattr(instance, self.name, value)


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    a = Property()
    b = Property()
    c = Property()

    def __init__(self, a: (int, float), b: (int, float), c: (int, float)):
        self.__a = a
        self.__b = b
        self.__c = c

    def __setattr__(self, key, value):
        if key == "MIN_DIMENSION" or key == "MAX_DIMENSION":
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        object.__setattr__(self, key, value)


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10
print(a, b, c)