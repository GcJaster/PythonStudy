class CellException(Exception): pass


class CellIntegerException(CellException): pass


class CellFloatException(CellException): pass


class CellStringException(CellException): pass


class Cell:
    """Class describing a cell without properties"""

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, '_' + k, v)
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value) -> None:
        self._value = self._is_valid(new_value)

    def _is_valid(self, new_value):
        raise NotImplementedError(f"метод _is_valid() должен быть переопределён в дочернем классе {self.__class__}")


class CellInteger(Cell):
    """Class describing a cell with type int"""

    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def _is_valid(self, value):
        if not self._min_value <= value <= self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')
        return value


class CellFloat(Cell):
    """Class describing a cell with type float"""

    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def _is_valid(self, value):
        if not self._min_value <= value <= self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')
        return value


class CellString(Cell):
    """Class describing a cell with type string"""

    def __init__(self, min_length, max_length):
        super().__init__(min_length=min_length, max_length=max_length)

    def _is_valid(self, value):
        if not self._min_length <= len(value) <= self._max_length:
            raise CellStringException('длина строки выходит за допустимый диапазон')
        return value


class TupleData:
    """Class describing a tuple with cells of different data types"""

    def __init__(self, *args):
        [self.__is_cell(x) for x in args]
        self.cells = tuple(args)

    @staticmethod
    def __is_cell(x):
        if not isinstance(x, Cell):
            raise TypeError("элементами объекта класса TupleData могут быть только объекты классов, унаследованные от класса Cell")

    def __getitem__(self, item):
        return self.cells[item].value

    def __setitem__(self, key, value):
        self.cells[key].value = value

    def __len__(self):
        return len(self.cells)

    def __iter__(self):
        for x in self.cells:
            yield x.value


if __name__ == '__main__':
    ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

    try:
        ld[0] = 1
        ld[1] = 20
        ld[2] = -5.6
        ld[3] = "Python ООП"
    except CellIntegerException as e:
        print(e)
    except CellFloatException as e:
        print(e)
    except CellStringException as e:
        print(e)
    except CellException:
        print("Ошибка при обращении к ячейке")
    except Exception:
        print("Общая ошибка при работе с объектом TupleData")