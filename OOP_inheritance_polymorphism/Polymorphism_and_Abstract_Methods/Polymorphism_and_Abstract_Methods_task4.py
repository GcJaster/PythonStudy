from abc import ABC, abstractmethod
import itertools


class Model(ABC):
    _generator_id = itertools.count(1)

    @abstractmethod
    def get_pk(self):
        pass

    @classmethod
    def _get_new_id(cls):
        return next(cls._generator_id)

    @staticmethod
    def get_info() -> str:
        return f"Базовый класс Model"


class ModelForm(Model):
    def __init__(self, login: str, password: str) -> None:
        self._login = login
        self._password = password
        self._id = self._get_new_id()

    def get_pk(self):
        return self._id




if __name__ == '__main__':
    form = ModelForm("Логин", "Пароль")
    print(form.get_pk())

