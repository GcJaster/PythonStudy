from typing import Any


class Validator:
    def _is_valid(self, data: Any) -> bool:
        return True

    def __call__(self, data: Any):
        if self._is_valid(data):
            return True
        else:
            raise ValueError('данные не прошли валидацию')


class TypeValidator(Validator):
    data_type = None

    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: Any) -> bool:
        return type(data) == self.data_type and self.min_value <= data <= self.max_value


class IntegerValidator(TypeValidator):
    data_type = int


class FloatValidator(TypeValidator):
    data_type = float


def main() -> None:
    integer_validator = IntegerValidator(-10, 10)
    float_validator = FloatValidator(-1, 1)
    res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
    # res2 = float_validator(10)  # исключение ValueError
    print(res1)

if __name__ == '__main__':
    main()