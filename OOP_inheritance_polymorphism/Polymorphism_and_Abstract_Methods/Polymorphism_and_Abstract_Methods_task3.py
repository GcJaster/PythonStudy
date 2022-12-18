from typing import Any, Union
from functools import wraps
from typing import Callable


U = Union[int, float]


def abstract_method(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(*args, **kwds):
        raise NotImplementedError("в классе не переопределен метод _is_valid")

    return wrapper


class Validator:
    """Class of description the validator"""

    @abstract_method
    def _is_valid(self, data: U):
        pass


class TypeValidator(Validator):
    """Class of description the type for validator"""

    data_type = None

    def __init__(self, min_value: U, max_value: U) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: U) -> bool:
        return type(data) == self.data_type and self.min_value <= data <= self.max_value

    def __call__(self, data: U) -> bool:
        return self._is_valid(data)


class IntegerValidator(TypeValidator):
    """Class of description the Integer value"""

    data_type = int


class FloatValidator(TypeValidator):
    """Class of description the Float value"""

    data_type = float


if __name__ == '__main__':
    float_validator = FloatValidator(0, 10.5)
    res_1 = float_validator(1)  # False (целое число, а не вещественное)
    res_2 = float_validator(1.0)  # True
    res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])
    print(res_1, res_2, res_3)