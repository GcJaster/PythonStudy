class Vector:
    _allowed_types = (int, float)
    error_message = 'числами'

    def __init__(self, *coords) -> None:
        self.__check_coords(coords)
        self._coords = coords

    def __len__(self) -> int:
        return len(self._coords)

    def __add__(self, other):
        self.__is_vector(other)
        self.__check_length(other)

        new_vector = tuple(x + y for x, y in zip(self._coords, other.get_coords()))
        return self.__make_vector(new_vector)

    def __sub__(self, other):
        self.__is_vector(other)
        self.__check_length(other)

        new_vector = tuple(x - y for x, y in zip(self._coords, other.get_coords()))
        return self.__make_vector(new_vector)

    def get_coords(self) -> tuple:
        return tuple(self._coords)

    def __check_coords(self, coords):
        if not all(type(x) in self._allowed_types for x in coords):
            raise ValueError(f'координаты должны быть {self.error_message}')

    def __check_length(self, other):
        if len(self) != len(other):
            raise TypeError("размерность векторов не совпадает")

    def __make_vector(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    @staticmethod
    def __is_vector(obj):
        if not isinstance(obj, Vector):
            raise TypeError("операнд должен быть класса Vector или любого дочернего от него класса")


class VectorInt(Vector):
    _allowed_types = (int,)
    error_message = 'целыми числами'


def main() -> None:
    v1 = Vector(1, 2, 3)
    v2 = Vector(1, 2, 3)
    # v3 = VectorInt(1, 2.0, 3)  # Исключение - координаты должны быть целыми числами
    res1 = v1 + v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
    res2 = v1 - v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
    print(res1.get_coords())
    print(res2.get_coords())


if __name__ == '__main__':
    main()