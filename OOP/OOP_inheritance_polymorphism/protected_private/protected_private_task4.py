from typing import Union

U = Union[int, float]


def int_positive_validator(value) -> bool:
    return type(value) == int and value > 0


def any_positive_validator(value) -> bool:
    return type(value) in (int, float) and value > 0


def str_validator(value) -> bool:
    return type(value) == str


def dict_validator(value) -> bool:
    return type(value) == dict


class Value:
    def __init__(self, validator=None, exception=TypeError('неверный тип аргумента')) -> None:
        self.validator = validator
        self.exception = exception

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner=None) -> str:
        return instance.__dict__[self.name]

    def __set__(self, instance, value) -> None:
        if self.validator is not None:
            if not self.validator(value):
                raise self.exception

        instance.__dict__[self.name] = value


class Aircraft:
    _model = Value(str_validator)
    _mass = Value(any_positive_validator)
    _speed = Value(any_positive_validator)
    _top = Value(any_positive_validator)

    def __init__(self, model: str, mass: U, speed: U, top: U) -> None:
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top


class PassengerAircraft(Aircraft):
    _chairs = Value(int_positive_validator)

    def __init__(self, model: str, mass: U, speed: U, top: U, chairs: int) -> None:
        super().__init__(model, mass, speed, top)
        self._chairs = chairs


class WarPlane(Aircraft):
    _weapons = Value(dict_validator)

    def __init__(self, model: str, mass: U, speed: U, top: U, weapons: dict) -> None:
        super().__init__(model, mass, speed, top)
        self._weapons = weapons


if __name__ == '__main__':
    planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
              PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
              WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
              WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
