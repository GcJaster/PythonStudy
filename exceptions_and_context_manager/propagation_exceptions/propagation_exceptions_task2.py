class ValidatorString:
    """Сlass describing string validator"""

    def __init__(self, min_length: int, max_length: int, chars: str) -> None:
        if type(max_length) != int or type(min_length) != int:
            raise TypeError("min_length и max_length должны быть целыми числами")

        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string: str) -> None:
        """checking string for valid characters and length"""
        if type(string) != str or not (self.min_length <= len(string) <= self.max_length) or \
                self.chars and not any(char in self.chars for char in string):
            raise ValueError('недопустимая строка')


class LoginForm:
    """Class that handles the login form"""

    def __init__(self, login_validator: ValidatorString, password_validator: ValidatorString) -> None:
        self.login_validator = login_validator
        self.password_validator = password_validator
        self._login = None
        self._password = None

    def form(self, request: dict) -> None:
        keys = request.keys()
        if 'login' not in keys or 'password' not in keys:
            raise TypeError('в запросе отсутствует логин или пароль')

        login = request.get('login')
        passwod = request.get('password')

        self.login_validator.is_valid(login)
        self.password_validator.is_valid(passwod)
        self._login = login
        self._password = passwod


if __name__ == '__main__':
    login_v = ValidatorString(4, 50, "")
    password_v = ValidatorString(10, 50, "!$#@%&?")
    lg = LoginForm(login_v, password_v)
    login, password = input().split()
    try:
        lg.form({'login': login, 'password': password})
    except (TypeError, ValueError) as e:
        print(e)
    else:
        print(lg._login)
