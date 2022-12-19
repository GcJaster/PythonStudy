from abc import ABC, abstractmethod
import itertools


class Model(ABC):
    """Class description the model"""

    _generator_id = itertools.count(1)

    @abstractmethod
    def get_pk(self):
        pass

    @classmethod
    def _get_new_id(cls) -> int:
        """Return next universal id(int)"""
        return next(cls._generator_id)

    @staticmethod
    def get_info() -> str:
        """Return string with info about basic class"""
        return f"Базовый класс Model"


class ModelForm(Model):
    """Class description the form of model"""

    def __init__(self, login: str, password: str) -> None:
        self._login = login
        self._password = password
        self._id = self._get_new_id()

    def get_pk(self) -> int:
        """Return the universal id(int) for model"""
        return self._id




if __name__ == '__main__':
    form = ModelForm("Логин", "Пароль")
    print(form.get_pk())

