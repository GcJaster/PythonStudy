class StringValue:
    def __init__(self, validator) -> None:
        self.__validator = validator

    def __set_name__(self, owner, name) -> None:
        self.name = "__" + name

    def __get__(self, instance, owner) -> str:
        return getattr(instance, self.name)

    def __set__(self, instance, value) -> None:
        if self.__validator.validate(value):
            setattr(RegisterForm, self.name, value)
        else:
            raise self.__validator.error


class ValidateString:
    error = None

    def __init__(self, min_length: int = 3, max_length: int = 100):
        self.__min_length = min_length
        self.__max_length = max_length

    def validate(self, string: str) -> bool:
        if not isinstance(string, str):
            self.error = TypeError(f"Not string type '{string}' ")
            return False
        elif not (self.__min_length <= len(string) <= self.__max_length):
            self.error = ValueError(f"{self.__min_length} <= len({string}) <= {self.__max_length}")
            return False
        return True


class RegisterForm:
    login = StringValue(validator=ValidateString())
    password = StringValue(validator=ValidateString())
    email = StringValue(validator=ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self) -> list:
        return [self.login, self.password, self.email]

    def show(self) -> None:
        print(f"<form>\n"
              f"Логин: {self.login}\n"
              f"Пароль: {self.password}\n"
              f"Email: {self.email}\n"
              f"</form>",)


def main():
    a = RegisterForm('Vanya', '11111', 'test1@gmail.com')
    a.show()


if __name__ == '__main__':
    main()