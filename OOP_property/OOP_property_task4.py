class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x: int = 0, y: int = 0) -> None:
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, new_x: int) -> None:
        if self.__check_value(new_x):
            self.__x = new_x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, new_y: int) -> None:
        if self.__check_value(new_y):
            self.__y = new_y

    @classmethod
    def __check_value(cls, value: int) -> bool:
        return cls.MIN_COORD <= value <= cls.MAX_COORD

    @staticmethod
    def norm2(vector) -> int:
        return vector.x * vector.x + vector.y * vector.y