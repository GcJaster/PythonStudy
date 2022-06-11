from math import sqrt


class LineTo:
    def __init__(self, x=0, y=0) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        if type(value) is int:
            self.__x = value

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, value: int) -> None:
        if type(value) is int:
            self.__y = value

    def __repr__(self) -> str:
        return f"<Line leads to [{self.x}; {self.y}]>"


class PathLines:
    def __init__(self, *args) -> None:
        self.__args = [*args]

    def get_path(self) -> list:
        return self.__args

    def get_length(self) -> float:
        coord_s = (0, 0)
        total_length = 0
        for line in self.get_path():
            line_length = sqrt(pow(line.x - coord_s[0], 2) + pow(line.y - coord_s[1], 2))
            total_length += line_length
            coord_s = (line.x, line.y)
        return total_length

    def add_line(self, line: LineTo) -> None:
        self.__args.append(line)