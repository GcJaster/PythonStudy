from typing import Union


class Body:
    name: str
    ro: Union[int, float]
    volume: Union[int, float]

    def __init__(self,
                 name: str,
                 ro: Union[int, float],
                 volume: Union[int, float]) -> None:
        self.name = name
        self.ro = ro
        self.volume = volume

    def get_weight(self) -> Union[int, float]:
        return self.ro * self.volume

    def __eq__(self, other) -> bool:
        sc = self.__verify_data(other)
        return self.get_weight() == sc

    def __gt__(self, other) -> bool:
        sc = self.__verify_data(other)
        return self.get_weight() > sc

    def __lt__(self, other) -> bool:
        sc = self.__verify_data(other)
        return self.get_weight() < sc

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, float, Body)):
            raise TypeError("Операнд справа должен иметь тип - int/float/Body")

        return other if isinstance(other, int) else other.get_weight()


def main() -> None:
    b1 = Body('body1', 15, 10)
    b2 = Body('body2', 10, 10)
    print(f"b1 weight = {b1.get_weight()}, b2 weight = {b2.get_weight()}")
    print(b1 == 150)
    print(b1 < 10)


if __name__ == '__main__':
    main()