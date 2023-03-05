from typing import Tuple


class Thing:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    def __init__(self, name: str, weight: float, author: str, date: str) -> None:
        super().__init__(name, weight)
        self.author = author
        self.date = date


class Computer(Thing):
    def __init__(self, name: str, weight: float, memory: int, cpu: str) -> None:
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu


class Auto(Thing):
    def __init__(self, name: str, weight: float, dims: Tuple[float, float, float]) -> None:
        super().__init__(name, weight)
        self.dims = tuple(dims)


class Mercedes(Auto):
    def __init__(self, name: str, weight: float, dims: Tuple[float, float, float], model: str, old: int) -> None:
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):
    def __init__(self, name: str, weight: float, dims: Tuple[float, float, float], model: str, wheel: bool) -> None:
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel


###  2 vers ###

# class Thing:
#     arg = ['name', 'weight']
#
#     def __init__(self, *args):
#         for i in range(len(args)):
#             setattr(self, self.arg[i], args[i])
#
#
# class ArtObject(Thing):
#     arg = ['name', 'weight', 'author', 'date']
#
#
# class Computer(Thing):
#     arg = ['name', 'weight', 'memory', 'CPU']
#
#
# class Auto(Thing):
#     arg = ['name', 'weight', 'dims']
#
#
# class Mercedes(Auto):
#     arg = ['name', 'weight', 'dims', 'model', 'old']
#
#
# class Toyota(Auto):
#     arg = ['name', 'weight', 'dims', 'model', 'wheel']
