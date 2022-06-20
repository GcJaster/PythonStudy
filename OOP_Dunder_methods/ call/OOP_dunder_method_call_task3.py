from string import ascii_lowercase, digits


class LoginForm:
    def __init__(self, name: str, validators=None) -> None:
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request) -> None:
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self) -> bool:
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


class LengthValidator:
    def __init__(self, min_length: int, max_length: int) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, value: str, *args, **kwargs) -> bool:
        return isinstance(value, str) and self.min_length <= len(value) <= self.max_length


class CharsValidator:
    def __init__(self, allowed_chars: str) -> None:
        self.allowed_chars = allowed_chars

    def __call__(self, string: str, *args, **kwargs) -> bool:
        return all(symbol in self.allowed_chars for symbol in string)


if __name__ == '__main__':
    lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
    lg.post({"login": "root", "password": "panda"})
    if lg.is_validate():
        print("Дальнейшая обработка данных формы")